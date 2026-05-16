/*
  Minimum first-principles Arduino wheeled robot controller.

  Baseline capability:
  - Four BTS7960 motor drivers
  - Manual serial drive pulses
  - NC external stop drive lockout
  - 3S LiPo voltage telemetry and low-voltage drive lockout
*/

#include <RobojaxBTS7960.h>

// Mega PWM pins: 2-13 and 44-46.

#define ESTOP_PIN 42
#define BATTERY_VOLTAGE_PIN A0

// Front-left motor driver
#define RPWM_L1 3
#define R_EN_L1 11
#define R_IS_L1 10
#define LPWM_L1 2
#define L_EN_L1 12
#define L_IS_L1 13

// Rear-left motor driver
#define RPWM_L2 7
#define R_EN_L2 23
#define R_IS_L2 22
#define LPWM_L2 6
#define L_EN_L2 24
#define L_IS_L2 25

// Front-right motor driver
#define RPWM_R1 5
#define R_EN_R1 47
#define R_IS_R1 46
#define LPWM_R1 4
#define L_EN_R1 48
#define L_IS_R1 49

// Rear-right motor driver
#define RPWM_R2 9
#define R_EN_R2 51
#define R_IS_R2 50
#define LPWM_R2 8
#define L_EN_R2 52
#define L_IS_R2 53

#define CW 1
#define CCW 0
#define DEBUG_BTS7960 1

const int LEFT_FORWARD_DIR = CW;
const int LEFT_REVERSE_DIR = CCW;
const int RIGHT_FORWARD_DIR = CCW;
const int RIGHT_REVERSE_DIR = CW;

const int DRIVE_PWM_PERCENT = 55;
const unsigned long DRIVE_PULSE_MS = 500;
const unsigned long DRIVE_SAFETY_POLL_MS = 10;
const unsigned long TELEMETRY_INTERVAL_MS = 1000;

const float ADC_REF_V = 5.0;
const float BATTERY_DIVIDER_RATIO = (100.0 + 33.0) / 33.0; // 100k top, 33k bottom
const float LOW_BATTERY_CUTOFF_V = 10.5; // 3S LiPo under-load cutoff

unsigned long lastTelemetryMs = 0;

RobojaxBTS7960 motor_L1(R_EN_L1, RPWM_L1, R_IS_L1, L_EN_L1, LPWM_L1, L_IS_L1, DEBUG_BTS7960);
RobojaxBTS7960 motor_L2(R_EN_L2, RPWM_L2, R_IS_L2, L_EN_L2, LPWM_L2, L_IS_L2, DEBUG_BTS7960);
RobojaxBTS7960 motor_R1(R_EN_R1, RPWM_R1, R_IS_R1, L_EN_R1, LPWM_R1, L_IS_R1, DEBUG_BTS7960);
RobojaxBTS7960 motor_R2(R_EN_R2, RPWM_R2, R_IS_R2, L_EN_R2, LPWM_R2, L_IS_R2, DEBUG_BTS7960);

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(50);

  motor_L1.begin();
  motor_L2.begin();
  motor_R1.begin();
  motor_R2.begin();

  pinMode(BATTERY_VOLTAGE_PIN, INPUT);
  pinMode(ESTOP_PIN, INPUT_PULLUP);

  stop_All();
  Serial.println("Ready. Commands: F/B/L/R/S, STATUS.");
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    data.trim();
    data.toUpperCase();

    Serial.print("Command Received: ");
    Serial.println(data);

    if (data == "LEFT" || data == "L") {
      if (driveAllowed()) {
        turn_Left(DRIVE_PWM_PERCENT);
        Serial.println("Left");
      }
    } else if (data == "RIGHT" || data == "R") {
      if (driveAllowed()) {
        turn_Right(DRIVE_PWM_PERCENT);
        Serial.println("Right");
      }
    } else if (data == "FORWARD" || data == "F") {
      if (driveAllowed()) {
        motor_Forward(DRIVE_PWM_PERCENT);
        Serial.println("Forward");
      }
    } else if (data == "REVERSE" || data == "BACK" || data == "B") {
      if (driveAllowed()) {
        motor_Reverse(DRIVE_PWM_PERCENT);
        Serial.println("Reverse");
      }
    } else if (data == "STOP" || data == "S") {
      stop_All();
      Serial.println("Stop");
    } else if (data == "STATUS" || data == "TELEMETRY" || data == "T") {
      printTelemetry();
    } else {
      Serial.println("Unknown command. Use F, B, L, R, S, or STATUS.");
    }
  }

  if (millis() - lastTelemetryMs >= TELEMETRY_INTERVAL_MS) {
    printTelemetry();
    lastTelemetryMs = millis();
  }

  if (!safetyInputsOk() || batteryLow()) {
    stop_All();
  }
}

float readBatteryVoltage() {
  float raw = analogRead(BATTERY_VOLTAGE_PIN);
  float pinV = raw * ADC_REF_V / 1023.0;
  return pinV * BATTERY_DIVIDER_RATIO;
}

bool batteryLow() {
  float v = readBatteryVoltage();
  return v > 7.0 && v < LOW_BATTERY_CUTOFF_V;
}

bool eStopActive() {
  // NC stop switch wiring: released = closed to ground, pressed or unplugged = HIGH.
  return digitalRead(ESTOP_PIN) == HIGH;
}

bool safetyInputsOk() {
  return !eStopActive();
}

bool driveAllowed() {
  if (eStopActive()) {
    stop_All();
    Serial.println("ESTOP_DRIVE_LOCKOUT");
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

void printTelemetry() {
  float voltage = readBatteryVoltage();

  Serial.print("TEL,V=");
  Serial.print(voltage, 2);
  Serial.print(",LOW=");
  Serial.print(batteryLow() ? 1 : 0);
  Serial.print(",ESTOP=");
  Serial.println(eStopActive() ? 1 : 0);
}

void holdDriveFor(unsigned long durationMs) {
  unsigned long startMs = millis();
  while (millis() - startMs < durationMs) {
    if (!safetyInputsOk() || batteryLow()) {
      stop_All();
      return;
    }
    delay(DRIVE_SAFETY_POLL_MS);
  }
}

void drive_Left(int pwmPercent, bool forward) {
  int dir = forward ? LEFT_FORWARD_DIR : LEFT_REVERSE_DIR;
  motor_L1.rotate(pwmPercent, dir);
  motor_L2.rotate(pwmPercent, dir);
}

void drive_Right(int pwmPercent, bool forward) {
  int dir = forward ? RIGHT_FORWARD_DIR : RIGHT_REVERSE_DIR;
  motor_R1.rotate(pwmPercent, dir);
  motor_R2.rotate(pwmPercent, dir);
}

void stop_All() {
  motor_L1.stop();
  motor_L2.stop();
  motor_R1.stop();
  motor_R2.stop();
}

void turn_Left(int pwmPercent) {
  drive_Left(pwmPercent, false);
  drive_Right(pwmPercent, true);
  holdDriveFor(DRIVE_PULSE_MS);
  stop_All();
}

void turn_Right(int pwmPercent) {
  drive_Left(pwmPercent, true);
  drive_Right(pwmPercent, false);
  holdDriveFor(DRIVE_PULSE_MS);
  stop_All();
}

void motor_Forward(int pwmPercent) {
  drive_Left(pwmPercent, true);
  drive_Right(pwmPercent, true);
  holdDriveFor(DRIVE_PULSE_MS);
  stop_All();
}

void motor_Reverse(int pwmPercent) {
  drive_Left(pwmPercent, false);
  drive_Right(pwmPercent, false);
  holdDriveFor(DRIVE_PULSE_MS);
  stop_All();
}
