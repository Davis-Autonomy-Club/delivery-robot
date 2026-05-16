/*

  Author: Smartbuilds.io
  Description: Build you own Simple Arduino Wheeled Robot
  Website: https://smartbuilds.io

*/

/*
  PWM dictates the angle of turn of the motor
  Slow Turn => 60% PWM Duty Cycle
  Hard Turn => 95% PWM Duty Cycle
*/

//Mega PWM Pins (2-13) (44-46)

#include <RobojaxBTS7960.h>
#include <Servo.h>

int reserved_SerialRX = 0;
int reserved_SerialTX = 1;

// V2.2 accessory and safety pins
#define LID_LOCK_SERVO_PIN 44
#define ESTOP_PIN 42
#define LID_CLOSED_PIN 43
#define BATTERY_VOLTAGE_PIN A0
#define BATTERY_CURRENT_PIN A1

// Encoder A channels use external interrupt-capable Mega pins.
#define ENC_L1_A 18
#define ENC_L2_A 19
#define ENC_R1_A 20
#define ENC_R2_A 21
#define ENC_L1_B 34
#define ENC_L2_B 35
#define ENC_R1_B 36
#define ENC_R2_B 37

// Front-left motor driver
#define RPWM_L1 3 // define pin 3 for RPWM pin (output)
#define R_EN_L1 11 // define pin 2 for R_EN pin (input)
#define R_IS_L1 10 // define pin 5 for R_IS pin (output)
#define LPWM_L1 2 // define pin 6 for LPWM pin (output)
#define L_EN_L1 12 // define pin 7 for L_EN pin (input)
#define L_IS_L1 13 // define pin 8 for L_IS pin (output)

// Rear-left motor driver
#define RPWM_L2 7 // define pin 3 for RPWM pin (output)
#define R_EN_L2 23 // define pin 2 for R_EN pin (input)
#define R_IS_L2 22 // define pin 5 for R_IS pin (output)
#define LPWM_L2 6 // define pin 6 for LPWM pin (output)
#define L_EN_L2 24  // define pin 7 for L_EN pin (input)
#define L_IS_L2 25 // define pin 8 for L_IS pin (output)

// Front-right motor driver
#define RPWM_R1 5 // define pin 3 for RPWM pin (output)
#define R_EN_R1 47 // define pin 2 for R_EN pin (input)
#define R_IS_R1 46 // define pin 5 for R_IS pin (output)
#define LPWM_R1 4 // define pin 6 for LPWM pin (output)
#define L_EN_R1 48 // define pin 7 for L_EN pin (input)
#define L_IS_R1 49 // define pin 8 for L_IS pin (output)

// Rear-right motor driver
#define RPWM_R2 9 // define pin 3 for RPWM pin (output)
#define R_EN_R2 51 // define pin 2 for R_EN pin (input)
#define R_IS_R2 50 // define pin 5 for R_IS pin (output)
#define LPWM_R2 8 // define pin 6 for LPWM pin (output)
#define L_EN_R2 52 // define pin 7 for L_EN pin (input)
#define L_IS_R2 53 // define pin 8 for L_IS pin (output)


#define CW 1 // do not change
#define CCW 0 // do not change
#define debug 1 //change to 0 to hide serial monitor debugging infornmation or set to 1 to view

int PWM_max = 100; //max speed of the Motor (Wheels)
int PWM_min = 80; //min speed of the Motor (Wheels)

int delay_motor = 3000;
int motor_high = 750;

const int LEFT_FORWARD_DIR = CW;
const int LEFT_REVERSE_DIR = CCW;
const int RIGHT_FORWARD_DIR = CCW;
const int RIGHT_REVERSE_DIR = CW;

const int LID_LOCKED_ANGLE = 15;
const int LID_UNLOCKED_ANGLE = 95;
const float ADC_REF_V = 5.0;
const float BATTERY_DIVIDER_RATIO = (100.0 + 33.0) / 33.0; // 100k top, 33k bottom
const float LOW_BATTERY_CUTOFF_V = 10.5; // 3S LiPo under-load cutoff
const float CURRENT_SENSOR_ZERO_V = 0.50; // Pololu ACS724 0-30A carrier at 5V
const float CURRENT_SENSOR_V_PER_A = 0.133;
const unsigned long DRIVE_SAFETY_POLL_MS = 10;

Servo lidLockServo;
bool lidLocked = true;
unsigned long lastTelemetryMs = 0;

volatile long encL1 = 0;
volatile long encL2 = 0;
volatile long encR1 = 0;
volatile long encR2 = 0;

RobojaxBTS7960 motor_L1(R_EN_L1, RPWM_L1, R_IS_L1, L_EN_L1, LPWM_L1, L_IS_L1, debug);
RobojaxBTS7960 motor_L2(R_EN_L2, RPWM_L2, R_IS_L2, L_EN_L2, LPWM_L2, L_IS_L2, debug);

RobojaxBTS7960 motor_R1(R_EN_R1, RPWM_R1, R_IS_R1, L_EN_R1, LPWM_R1, L_IS_R1, debug);
RobojaxBTS7960 motor_R2(R_EN_R2, RPWM_R2, R_IS_R2, L_EN_R2, LPWM_R2, L_IS_R2, debug);

void updateEncoder(volatile long &count, int pinA, int pinB) {
  bool a = digitalRead(pinA);
  bool b = digitalRead(pinB);
  count += (a == b) ? 1 : -1;
}

void isrEncL1() { updateEncoder(encL1, ENC_L1_A, ENC_L1_B); }
void isrEncL2() { updateEncoder(encL2, ENC_L2_A, ENC_L2_B); }
void isrEncR1() { updateEncoder(encR1, ENC_R1_A, ENC_R1_B); }
void isrEncR2() { updateEncoder(encR2, ENC_R2_A, ENC_R2_B); }

void setup() {
  Serial.begin(9600);// setup Serial Monitor to display information
  Serial.setTimeout(50);

  //Initate Motors
  motor_L1.begin();
  motor_L2.begin();
  motor_R1.begin();
  motor_R2.begin();

  pinMode(BATTERY_VOLTAGE_PIN, INPUT);
  pinMode(BATTERY_CURRENT_PIN, INPUT);
  pinMode(ESTOP_PIN, INPUT_PULLUP);
  pinMode(LID_CLOSED_PIN, INPUT_PULLUP);

  pinMode(ENC_L1_A, INPUT_PULLUP);
  pinMode(ENC_L2_A, INPUT_PULLUP);
  pinMode(ENC_R1_A, INPUT_PULLUP);
  pinMode(ENC_R2_A, INPUT_PULLUP);
  pinMode(ENC_L1_B, INPUT_PULLUP);
  pinMode(ENC_L2_B, INPUT_PULLUP);
  pinMode(ENC_R1_B, INPUT_PULLUP);
  pinMode(ENC_R2_B, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(ENC_L1_A), isrEncL1, CHANGE);
  attachInterrupt(digitalPinToInterrupt(ENC_L2_A), isrEncL2, CHANGE);
  attachInterrupt(digitalPinToInterrupt(ENC_R1_A), isrEncR1, CHANGE);
  attachInterrupt(digitalPinToInterrupt(ENC_R2_A), isrEncR2, CHANGE);

  lidLockServo.attach(LID_LOCK_SERVO_PIN);
  lock_Lid();

  Serial.println("Ready. Commands: F/B/L/R/S, LOCK, UNLOCK, STATUS, ZEROENC.");

}

void loop() {

  // Debug - Run Robot Test 
  //  motor_test_directions();

  //Recieve Commands via Serial Comms to control the Robot.

  //Recieve Serial commands to control the Robot
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    data.trim();
    data.toUpperCase();
    Serial.print("Command Received: ");
    Serial.println(data);

    //Move Droiid Bot
    if (data == "LEFT" || data == "L") {
      if (driveAllowed()) {
        turn_Left(60);
        Serial.println("Left");
      }
    } else if (data == "RIGHT" || data == "R") {
      if (driveAllowed()) {
        turn_Right(60);
        Serial.println("Right");
      }
    } else if (data == "FORWARD" || data == "F") {
      if (driveAllowed()) {
        motor_Forward(60);
        Serial.println("Forward");
      }
    } else if (data == "REVERSE" || data == "BACK" || data == "B") {
      if (driveAllowed()) {
        motor_Reverse(60);
        Serial.println("Reverse");
      }
    } else if (data == "STOP" || data == "S") {
      stop_All();
      Serial.println("Stop");
    } else if (data == "LOCK") {
      lock_Lid();
      Serial.println("Lid locked");
    } else if (data == "UNLOCK") {
      unlock_Lid();
      Serial.println("Lid unlocked");
    } else if (data == "STATUS" || data == "TELEMETRY" || data == "T") {
      printTelemetry();
    } else if (data == "ZEROENC") {
      zeroEncoders();
      Serial.println("Encoders zeroed");
    } else {
      Serial.println("Unknown command. Use F, B, L, R, S, LOCK, UNLOCK, STATUS, or ZEROENC.");
    }
  }

  if (millis() - lastTelemetryMs >= 1000) {
    printTelemetry();
    lastTelemetryMs = millis();
  }

  if (!safetyInputsOk()) {
    stop_All();
  }

}

float readBatteryVoltage() {
  float raw = analogRead(BATTERY_VOLTAGE_PIN);
  float pinV = raw * ADC_REF_V / 1023.0;
  return pinV * BATTERY_DIVIDER_RATIO;
}

float readBatteryCurrent() {
  float raw = analogRead(BATTERY_CURRENT_PIN);
  float sensorV = raw * ADC_REF_V / 1023.0;
  float amps = (sensorV - CURRENT_SENSOR_ZERO_V) / CURRENT_SENSOR_V_PER_A;
  if (amps < 0) {
    amps = 0;
  }
  return amps;
}

bool batteryLow() {
  float v = readBatteryVoltage();
  return v > 7.0 && v < LOW_BATTERY_CUTOFF_V;
}

bool eStopActive() {
  // NC stop switch wiring: released = closed to ground, pressed or unplugged = HIGH.
  return digitalRead(ESTOP_PIN) == HIGH;
}

bool lidClosed() {
  // Lid switch wiring: closed lid pulls the input to ground.
  return digitalRead(LID_CLOSED_PIN) == LOW;
}

bool safetyInputsOk() {
  return !eStopActive() && lidClosed();
}

bool driveAllowed() {
  if (eStopActive()) {
    stop_All();
    Serial.println("ESTOP_DRIVE_LOCKOUT");
    printTelemetry();
    return false;
  }
  if (!lidClosed()) {
    stop_All();
    Serial.println("LID_OPEN_DRIVE_LOCKOUT");
    printTelemetry();
    return false;
  }
  if (batteryLow()) {
    stop_All();
    Serial.println("LOW_BATTERY_DRIVE_LOCKOUT");
    printTelemetry();
    return false;
  }
  return true;
}

void holdDriveFor(unsigned long durationMs) {
  unsigned long startMs = millis();
  while (millis() - startMs < durationMs) {
    if (!safetyInputsOk()) {
      stop_All();
      return;
    }
    delay(DRIVE_SAFETY_POLL_MS);
  }
}

void lock_Lid() {
  lidLockServo.write(LID_LOCKED_ANGLE);
  lidLocked = true;
}

void unlock_Lid() {
  lidLockServo.write(LID_UNLOCKED_ANGLE);
  lidLocked = false;
}

void zeroEncoders() {
  noInterrupts();
  encL1 = 0;
  encL2 = 0;
  encR1 = 0;
  encR2 = 0;
  interrupts();
}

void getEncoderSnapshot(long &l1, long &l2, long &r1, long &r2) {
  noInterrupts();
  l1 = encL1;
  l2 = encL2;
  r1 = encR1;
  r2 = encR2;
  interrupts();
}

void printTelemetry() {
  long l1, l2, r1, r2;
  getEncoderSnapshot(l1, l2, r1, r2);
  float voltage = readBatteryVoltage();
  float current = readBatteryCurrent();
  Serial.print("TEL,V=");
  Serial.print(voltage, 2);
  Serial.print(",I=");
  Serial.print(current, 2);
  Serial.print(",LOW=");
  Serial.print(batteryLow() ? 1 : 0);
  Serial.print(",ESTOP=");
  Serial.print(eStopActive() ? 1 : 0);
  Serial.print(",LID_CLOSED=");
  Serial.print(lidClosed() ? 1 : 0);
  Serial.print(",LOCK=");
  Serial.print(lidLocked ? 1 : 0);
  Serial.print(",ENC=");
  Serial.print(l1);
  Serial.print("/");
  Serial.print(l2);
  Serial.print("/");
  Serial.print(r1);
  Serial.print("/");
  Serial.println(r2);
}

void drive_Left(int PWM_pcntg, bool forward) {
  int dir = forward ? LEFT_FORWARD_DIR : LEFT_REVERSE_DIR;
  motor_L1.rotate(PWM_pcntg, dir);
  motor_L2.rotate(PWM_pcntg, dir);
}

void drive_Right(int PWM_pcntg, bool forward) {
  int dir = forward ? RIGHT_FORWARD_DIR : RIGHT_REVERSE_DIR;
  motor_R1.rotate(PWM_pcntg, dir);
  motor_R2.rotate(PWM_pcntg, dir);
}

void stop_All() {
  motor_L1.stop();
  motor_L2.stop();
  motor_R1.stop();
  motor_R2.stop();
}

void turn_Left(int PWM_pcntg) {
  drive_Left(PWM_pcntg, false);
  drive_Right(PWM_pcntg, true);

  holdDriveFor(motor_high);
  stop_All();

}

void turn_Right(int PWM_pcntg) {
  drive_Left(PWM_pcntg, true);
  drive_Right(PWM_pcntg, false);

  holdDriveFor(motor_high);
  stop_All();

}

void motor_Forward(int PWM_pcntg) {
  drive_Left(PWM_pcntg, true);
  drive_Right(PWM_pcntg, true);

  holdDriveFor(motor_high);

  stop_All();


}

void motor_Reverse(int PWM_pcntg) {
  drive_Left(PWM_pcntg, false);
  drive_Right(PWM_pcntg, false);

  holdDriveFor(motor_high);

  stop_All();

}

//Debug Motor Directions
void motor_test_directions() {
  turn_Left(60);
  delay(delay_motor);
  turn_Right(60);
  delay(delay_motor);
  motor_Forward(60);
  delay(delay_motor);
  motor_Reverse(60);
  delay(delay_motor);
}
