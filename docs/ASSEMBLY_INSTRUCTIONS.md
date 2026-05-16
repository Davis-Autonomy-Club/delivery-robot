# Assembly Instructions

Follow this in order. Do not install or plug in the LiPo battery until the wiring checklist tells you to.

The canonical wiring source is [`docs/CANONICAL_WIRING_V2.md`](CANONICAL_WIRING_V2.md). The old root-level wiring image is legacy and incomplete.

## Orientation

Use this convention for the whole build:

- Front: the side with the HC-SR04 openings, LED diffuser, and front camera.
- Rear: the side with the rear camera and lid-lock servo.
- Left/right: the robot's left and right when you stand behind it and look forward.
- Motors: `L1` = front-left, `L2` = rear-left, `R1` = front-right, `R2` = rear-right.

## 1. Print And Inspect The Parts

Print the files listed in `cad/PRINT_MANIFEST.md`. After printing:

1. Confirm the four base plates are flat and not curled.
2. Test an M3 screw through every base seam hole, panel hole, corner-post hole, tray hole, and camera-mount hole. Clear tight holes with a 3.0-3.2 mm drill bit by hand.
3. Dry-fit the four base plates on a table. The total base should be about 322 x 328 mm.
4. Confirm the v2.2 printed parts are present: camera mounts, servo lock mount, lock cam, lock keeper, Raspberry Pi tray, LTE tray, telemetry plate, and two buck-converter plates.
5. Confirm the non-printed v2.2 hardware is available before final assembly: external stop button, lid-closed switch, fuse holder, fuses, distribution block, compatible wheels, battery straps, and Raspberry Pi/microSD if you are building the camera/LTE stack.
6. Check the renders in `cad/renders/` against your printed parts so you know what the final shape should look like.

## 2. Assemble The Base

Parts:

- `base_plate_front_left.stl`
- `base_plate_front_right.stl`
- `base_plate_rear_left.stl`
- `base_plate_rear_right.stl`
- 2 x `base_seam_joiner_long_print_2.stl`
- 2 x `base_seam_joiner_short_print_2.stl`
- M3 x 12 screws, washers, and M3 nyloc nuts

Steps:

1. Place the four base plates face-up in a rectangle. The motor slot clusters should sit near all four outside corners.
2. Flip the base over while keeping the seams tight.
3. Put the long joiner bars across the long center seam and the short joiner bars across the short center seam.
4. Insert M3 x 12 screws from the top of the base, through the base and joiner bars. Add washers and nyloc nuts underneath.
5. Tighten until snug. Stop when the plastic stops moving; do not crush the printed parts.

## 3. Install Encoder Motors, Adapters, And Wheels

Parts:

- 4 x Pololu #4752-style 37D encoder gearmotors
- 4 x metal 37D motor brackets
- 4 x 12 mm hex adapters for 6 mm shafts
- 4 x 120 mm wheels
- 4 x optional printed motor spacers

Steps:

1. Attach each 37D motor to a metal bracket using the bracket manufacturer's screws. For Pololu 37D motors, do not drive screws deeper into the gearbox than the bracket instructions allow.
2. Place one bracket at each base corner. The motor shaft must point outward, away from the body.
3. Route the encoder cable inward through the nearest base slot before fully tightening the bracket.
4. Loosely bolt each bracket through the slotted holes in the base using M3 screws, washers, and nyloc nuts.
5. Slide a 12 mm hex adapter onto each 6 mm motor shaft. Put one set screw against the flat of the D shaft. Tighten both set screws.
6. Install the wheels on the adapters using the adapter's supplied wheel screw.
7. Put the robot on a flat table. Adjust the bracket slots until all four wheels touch the table evenly and do not rub the base.
8. Tighten the bracket bolts. Add the printed 37D motor spacers under the motor barrels if the motors vibrate or sag; hold spacers with zip ties through nearby cable slots.

## 4. Mount The Electronics

Parts:

- Arduino Mega tray
- 2 x BTS7960 dual-driver trays
- Battery sled
- Raspberry Pi companion tray
- USB LTE modem tray
- Battery telemetry sensor plate
- 2 x buck-converter plates
- Arduino Mega
- 4 x BTS7960 driver modules
- Raspberry Pi
- USB LTE modem
- Pololu ACS724 current sensor
- 2 x 5 V buck converters
- Fuse holder, switch or XT60 loop key, external stop button, lid-closed switch, cable glands/strain relief, and terminal/distribution blocks

Suggested layout:

- Battery sled: centered on the base, low and balanced.
- Arduino Mega tray: centered and reachable from the top.
- BTS7960 trays: one tray for left-side motors, one tray for right-side motors.
- Raspberry Pi tray: away from the motor-driver heat sinks, with USB ports reachable.
- LTE modem tray: high enough for antenna/cable clearance, away from motor power wiring.
- Telemetry plate: near the fuse/switch and distribution blocks.
- Fuse and switch: close to battery positive, reachable through the lid.
- Buck converters: one for Arduino/BTS logic/servo, one for Pi/cameras/LTE.
- External stop button: on an outside panel where it can be hit quickly.
- Lid-closed switch: one half on the body/post area and the matching magnet or actuator on the lid.
- Cable glands/strain relief: on any cable exits that leave the protected electronics bay.

Steps:

1. Bolt or zip-tie the printed trays to the base through convenient base holes or printed slots.
2. Mount the Arduino Mega on nylon M3 standoffs in the Arduino tray.
3. Mount two BTS7960 modules on each driver tray. If your modules' mounting holes do not match, use zip ties through the tray slots.
4. Mount the Raspberry Pi on standoffs in the Pi tray.
5. Mount or strap the USB LTE modem into the LTE tray.
6. Mount the ACS724 current sensor and the voltage-divider perfboard on the telemetry plate.
7. Mount both buck converters to the buck plates.
8. Test-fit one battery pack in the sled with two Velcro straps, but leave it unplugged. Keep the second matching pack outside the robot as a charged spare.
9. Mount the external stop button and lid-closed switch hardware before final body closure.
10. Route motor wires, encoder wires, switch wires, and sensor wires through the corner cable slots toward the matching driver tray and Arduino.

## 5. Power Wiring

Keep the battery unplugged while building.

Important: do not use a solderless breadboard for any motor or battery power. Use real wire, crimped or soldered joints, distribution blocks, and strain relief.

Only one LiPo pack is installed in the robot at a time. The second matching pack is for repeated tests; it is not wired in parallel.

High-current path:

1. Battery XT60 positive goes to the inline fuse holder.
2. Fuse holder output goes to the main switch or XT60 loop key.
3. Switch output goes to ACS724 `IP+`.
4. ACS724 `IP-` goes to the positive distribution block.
5. Battery XT60 negative goes directly to the negative distribution block.
6. Every BTS7960 `B+` terminal connects to positive distribution with 14-18 AWG wire.
7. Every BTS7960 `B-` terminal connects to negative distribution with 14-18 AWG wire.
8. Logic/accessory buck input positive/negative connects to the distribution blocks.
9. Pi/camera/LTE buck input positive/negative connects to the distribution blocks.

5 V outputs:

1. Before connecting electronics, use a multimeter and adjust both bucks to 5.0-5.1 V.
2. Logic/accessory buck 5 V powers Arduino Mega `5V`, all BTS7960 `Vcc` pins, lid servo red wire, ACS724 `VCC`, and the top of the encoder 5 V rail.
3. Logic/accessory buck ground powers Arduino `GND`, all BTS7960 `Gnd` pins, lid servo ground, ACS724 ground, encoder grounds, and voltage-divider ground.
4. Pi/camera/LTE buck powers the Raspberry Pi through a USB-C power pigtail/breakout or equivalent 5 V input method. Do not feed raw 3S battery voltage to the Pi.
5. Plug the Arduino Mega, front camera, rear camera, and LTE modem directly into the Raspberry Pi for the first build. Skip the desk-style wall-adapter USB hub.
6. If later testing shows Pi USB brownouts, add a compact hub only if it can be powered cleanly from the onboard 5 V Pi rail.
7. The two 5 V positive rails stay separate. Their grounds are common.

Battery voltage divider:

1. Solder a 100 kOhm resistor from switched battery positive to Arduino A0.
2. Solder a 33 kOhm resistor from Arduino A0 to common ground.
3. Heat-shrink the divider and mount it on the telemetry plate.
4. This divider is only for sensing. It must not power anything.

## 6. Motor Output Wiring

Each BTS7960 controls one motor:

| Driver | Physical motor | BTS7960 motor terminals |
| --- | --- | --- |
| `L1` | Front-left motor | `M+` and `M-` to front-left motor leads |
| `L2` | Rear-left motor | `M+` and `M-` to rear-left motor leads |
| `R1` | Front-right motor | `M+` and `M-` to front-right motor leads |
| `R2` | Rear-right motor | `M+` and `M-` to rear-right motor leads |

If a wheel spins backward during testing, swap that motor's `M+` and `M-` wires at the BTS7960 terminal. Do not change the high-current battery wiring to fix motor direction.

## 7. Arduino Signal Wiring

### BTS7960 Control Pins

| Driver | RPWM | LPWM | R_EN | L_EN | R_IS | L_IS |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `L1` front-left | D3 | D2 | D11 | D12 | D10 | D13 |
| `L2` rear-left | D7 | D6 | D23 | D24 | D22 | D25 |
| `R1` front-right | D5 | D4 | D47 | D48 | D46 | D49 |
| `R2` rear-right | D9 | D8 | D51 | D52 | D50 | D53 |

For every driver:

- BTS7960 `Vcc` goes to the regulated logic/accessory 5 V rail.
- BTS7960 `Gnd` goes to common ground.
- Use 22-26 AWG signal wire.
- Keep signal wires away from motor power wires where practical.

### Encoder Pins

| Encoder | A channel | B channel |
| --- | ---: | ---: |
| `L1` front-left | D18 | D34 |
| `L2` rear-left | D19 | D35 |
| `R1` front-right | D20 | D36 |
| `R2` rear-right | D21 | D37 |

Each encoder also needs 5 V and ground from the logic/accessory rail. The sketch uses interrupts on the A channels and reads B channels for direction.

### Telemetry, Lid Lock, And Safety Inputs

| Function | Signal pin |
| --- | ---: |
| Lid-lock servo | D44 |
| External stop input | D42 |
| Lid-closed switch input | D43 |
| Battery voltage divider | A0 |
| ACS724 current sensor `VIOUT` | A1 |

The lid-lock servo gets power from the logic/accessory 5 V buck, not from a weak USB-only Arduino connection.

External stop wiring: use a normally-closed contact between D42 and Arduino GND. When the button is released and the wire is healthy, D42 reads LOW. Pressing the button or breaking the wire makes D42 read HIGH and the sketch refuses to drive.

Lid-closed wiring: wire the reed switch or microswitch between D43 and Arduino GND so a closed lid pulls D43 LOW. An open lid makes D43 HIGH and the sketch refuses to drive. For early bench testing before the lid switch is mounted, use a clearly labeled temporary jumper from D43 to GND, then remove the jumper when the real switch is installed.

## 8. Cameras, LTE, And Pi Link

1. Bolt the front and rear camera mounts to the matching body panels using M3 hardware.
2. Install one USB/UVC camera in each mount. Use M2 screws if the board holes line up; otherwise use zip ties through the camera-mount slots.
3. Connect both cameras to the Raspberry Pi.
4. Install the USB LTE modem in its tray and connect it to the Pi.
5. Install the activated SIM in the LTE modem.
6. Connect the Arduino Mega to the Pi by USB A-to-B cable. The Arduino sketch uses 9600 baud serial.
7. Do not use the Sabrent wall-adapter desk hub onboard. The four Pi USB ports are enough for Arduino, two cameras, and LTE. Revisit a rail-powered hub only if logs or testing show USB brownouts.

This repo does not yet include the Pi teleop dashboard. The Pi is now mechanically and electrically provisioned so the next software sprint can stream camera video, forward commands to the Arduino, and report telemetry over LTE.

## 9. Upload The Sketch

1. Install the Arduino IDE.
2. Install the Robojax BTS7960 library. The repo includes `Robojax-BTS7960-Motor-driver.zip`; in Arduino IDE use `Sketch > Include Library > Add .ZIP Library`.
3. Open `arduino-wheel-robot-code/arduino-wheel-robot-code.ino`.
4. Select `Arduino Mega or Mega 2560`.
5. Select the correct USB port.
6. Upload the sketch.

The sketch accepts these serial commands at 9600 baud: `Forward`, `Reverse`, `Left`, `Right`, `Stop`, `LOCK`, `UNLOCK`, `STATUS`, and `ZEROENC`. Short drive forms also work: `F`, `B`, `L`, `R`, `S`.

Telemetry prints once per second:

```text
TEL,V=12.10,I=1.25,LOW=0,ESTOP=0,LID_CLOSED=1,LOCK=1,ENC=123/121/119/124
```

## 10. First Power Test

Do this with the robot on blocks so the wheels are off the table.

1. Confirm the fuse is installed.
2. Confirm battery polarity with a multimeter before plugging in the battery.
3. Confirm both buck outputs are 5.0-5.1 V.
4. Turn the main switch off.
5. Plug in the battery.
6. Turn the main switch on.
7. Check Arduino power, Pi power, and the buck outputs.
8. Open Arduino Serial Monitor at 9600 baud.
9. Send `STATUS`. Confirm voltage is plausible for a 3S LiPo, `ESTOP=0`, and `LID_CLOSED=1`.
10. Press the external stop button and send `STATUS`; confirm `ESTOP=1`. Try `Forward`; the robot must refuse to drive. Reset the stop button before continuing.
11. Open the lid or move the lid-switch magnet away and send `STATUS`; confirm `LID_CLOSED=0`. Try `Forward`; the robot must refuse to drive. Close the lid before continuing.
12. Send `LOCK`, then `UNLOCK`, and verify the servo cam moves.
13. Send `ZEROENC`.
14. Spin each wheel by hand and send `STATUS`; encoder counts should change.
15. Send `Forward`. All four wheels should spin for about 0.75 seconds and stop.
16. Send `Reverse`, then `Left`, then `Right`, then `Stop`.

If one wheel spins the wrong way, swap that motor's two output wires. If an encoder count moves the wrong direction, swap that encoder's A/B signal wires in software or at the Arduino pins after documenting the change.

## 11. Build The Body, Cargo Bay, Cameras, And Lock

Parts:

- 4 x corner posts
- 4 x cargo shelf support blocks
- Cargo floor front-left, front-right, rear-left, rear-right quadrants
- 2 x cargo retainer long rails
- 2 x cargo retainer short rails
- Front-left and front-right panels
- Rear-left and rear-right panels
- 2 x side front-half panels
- 2 x side rear-half panels
- 4 x panel center joiners
- 4 x lid quadrants
- 2 x camera mounts
- Servo lock mount
- Servo lock cam
- Lock keeper plate

Steps:

1. Bolt the four corner posts to the base using the post holes near the body corners.
2. Bolt one cargo shelf support block to the inside face of each corner post using the extra hole row about 60 mm above the base. The flat top of each support block should face upward.
3. Place the four cargo floor quadrants on the support blocks. Together they form a flat shelf above the electronics.
4. Bolt the cargo floor down through the support-block holes using M3 x 12 screws, washers, and nyloc nuts.
5. Bolt the two long cargo retainer rails and two short cargo retainer rails to the cargo floor. The rails form a rectangle for the food container.
6. Assemble the front panel halves with one center joiner. The HC-SR04 holes face outward.
7. Assemble the rear panel halves with one center joiner.
8. Assemble each side from one front-half panel, one rear-half panel, and one center joiner.
9. Bolt the panels to the corner posts using M3 x 20-25 screws, washers, and nyloc nuts.
10. Install the two HC-SR04 modules from inside the front panel if you bought them.
11. Tape or lightly glue the clear LED diffuser behind the front slot if you bought an LED strip.
12. Bolt one camera mount to the front panel and one to the rear panel.
13. Install the front and rear cameras in their mounts and route the USB cables to the Pi.
14. Bolt or zip-tie the micro servo into `micro_servo_lid_lock_mount.stl`.
15. Attach `lid_lock_servo_cam.stl` to the servo horn.
16. Mount the servo lock assembly near the rear top inside edge.
17. Mount `lid_lock_keeper_plate.stl` to the rear lid/post area so the cam can rotate under the keeper when locked and clear it when unlocked.
18. Mount the lid-closed switch so the closed lid pulls D43 to ground. Verify `LID_CLOSED=1` with the lid closed and `LID_CLOSED=0` with the lid open.
19. Test `LOCK` and `UNLOCK` with the lid off first, then with the lid in place. Adjust the servo angles in the sketch if your servo horn lands differently.
20. Place the four lid quadrants on top. Use M3 screws through the available lid/post holes where you want a retained lid.
21. Apply foam edge bumper around the outer body perimeter where it will not rub the wheels, block camera views, or cover the external stop button.

Where the food goes: unlock/remove the lid and place a sealed food-safe container on the cargo floor, inside the four retainer rails. The maximum outside size is 205 x 145 x 70 mm. Food must stay in the sealed container; printed PETG/PLA is not a food-contact surface.

The printed servo lock is a prototype latch, not theft-proof security hardware.

## 12. Ground Test

1. Put the robot on the floor with at least 2 m of clear space.
2. Test first with the food container empty, then with a light payload.
3. Keep first payload tests at 500 g or less. Increase only after the robot drives straight and the motors stay warm, not hot.
4. Send `ZEROENC`, then `Forward` once. It should move straight for a short pulse and all four encoder counts should change.
5. If it veers left, either the left wheels are weaker or the right wheels are faster. Check bracket rubbing, wheel alignment, tire friction, and battery charge.
6. Send `Left` and `Right`. The robot should pivot.
7. After one minute of testing, touch the motor drivers and motors carefully. Warm is normal; too hot to touch means stop and inspect binding or wiring.
8. Check that `TEL` voltage does not drop below the low-voltage cutoff during normal light-load tests.

## 13. Final Physical Fit Checks

Before printing duplicate replacement parts or committing to outdoor testing, verify these by hand:

- Wheel hub depth, wheel screw length, wheel offset, and body/bracket clearance with the exact wheel set.
- Battery pack footprint, height, XT60 cable exit direction, and strap fit against `3s_lipo_battery_sled.stl`.
- Food container outside dimensions against the cargo retainer rails. The maximum outside size is 205 x 145 x 70 mm.
- Raspberry Pi kit extras against the tray. The tray is for the bare Pi board; the CanaKit case and switch cable are not assumed to fit.
- Cable glands grip the actual cables without crushing USB leads, camera leads, or LTE wiring.

## 14. LiPo Safety Rules

- Never charge the LiPo inside the robot.
- Never leave a charging LiPo unattended.
- Use the RC balance charger, connect both the main pack lead and the balance lead, select 3S LiPo mode, and set a conservative charge current. For a 5200 mAh pack, 5.2 A is 1C; lower is gentler.
- Stop using the pack if it swells, smells sweet/solvent-like, gets hot, or has damaged insulation.
- Store the battery at storage voltage when not using the robot.
- Keep the fuse installed. Do not bypass it for testing.
- The low-voltage telemetry is a helper, not a replacement for LiPo safety discipline.
