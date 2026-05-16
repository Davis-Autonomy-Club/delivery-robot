# Assembly Instructions

Follow this in order. Do not install or plug in the LiPo battery until the wiring checklist tells you to. This is a supervised fair-weather outdoor build for pavement, concrete, and packed paths. It is not a rain, puddle, mud, or submersion robot.

The canonical wiring source is [`docs/CANONICAL_WIRING_V2.md`](CANONICAL_WIRING_V2.md). The old root-level wiring image is legacy and incomplete.

## Orientation

Use this convention for the whole build:

- Front: the side you choose as forward in firmware testing.
- Rear: the opposite side.
- Left/right: the robot's left and right when you stand behind it and look forward.
- Motors: `L1` = front-left, `L2` = rear-left, `R1` = front-right, `R2` = rear-right.

## 1. Print And Inspect The Parts

Print the files listed in `cad/PRINT_MANIFEST.md`. After printing:

1. Confirm the four base plates are flat and not curled.
2. Test an M3 screw through every base seam hole, panel hole, corner-post hole, tray hole, and cargo-floor hole. Clear tight holes with a 3.0-3.2 mm drill bit by hand.
3. Dry-fit the four base plates on a table. The total base should be about 322 x 328 mm.
4. Confirm the minimum outdoor parts are present: split base, seam joiners, Arduino tray, BTS7960 tray, battery sled, one buck-converter plate, cargo floor, cargo support blocks, body panels, corner posts, panel joiners, and lid quadrants.
5. Use PETG or ASA for outdoor printed parts. Do not use PLA for outdoor chassis or body parts that may sit in sun or a warm car.
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

## 3. Install Motors, Adapters, And Wheels

Parts:

- 4 x 37D gearmotors
- 4 x metal 37D motor brackets
- 4 x 12 mm hex adapters for 6 mm shafts
- 4 x 120 mm wheels

Steps:

1. Attach each 37D motor to a metal bracket using the bracket manufacturer's screws. Do not drive screws deeper into the gearbox than the bracket instructions allow.
2. Place one bracket at each base corner. The motor shaft must point outward, away from the body.
3. Route the two motor leads inward through the nearest base slot before fully tightening the bracket. Add a drip loop before the wire enters the electronics bay so water cannot run straight along the wire into the robot.
4. If your motors have encoder leads, coil and secure them. Do not wire them for the baseline.
5. Loosely bolt each bracket through the slotted holes in the base using M3 screws, washers, and nyloc nuts.
6. Slide a 12 mm hex adapter onto each 6 mm motor shaft. Put one set screw against the flat of the D shaft. Tighten both set screws.
7. Install the wheels on the adapters using the adapter's supplied wheel screw.
8. Put the robot on a flat table. Adjust the bracket slots until all four wheels touch the table evenly and do not rub the base.
9. Tighten the bracket bolts.

## 4. Mount The Electronics

Parts:

- Arduino Mega tray
- BTS7960 dual-driver trays
- Battery sled
- Buck-converter plate
- Arduino Mega
- 4 x BTS7960 driver modules
- 5 V buck converter
- Fuse holder, switch or XT60 loop key, external stop button, voltage-divider perfboard, and terminal/distribution blocks

Suggested layout:

- Battery sled: centered on the base, low and balanced.
- Arduino Mega tray: centered and reachable from the top.
- BTS7960 trays: one tray for left-side motors, one tray for right-side motors.
- Fuse and switch: close to battery positive, protected from direct splash, and reachable through the lid.
- Buck converter: near the Arduino tray.
- External stop button: weather-resistant, on an outside panel where it can be hit quickly.

Steps:

1. Bolt or zip-tie the printed trays to the base through convenient base holes or printed slots.
2. Mount the Arduino Mega on nylon M3 standoffs in the Arduino tray.
3. Mount two BTS7960 modules on each driver tray. If your modules' mounting holes do not match, use zip ties through the tray slots.
4. Mount the buck converter to the buck plate.
5. Solder the voltage divider to perfboard or a terminal strip. Add heat-shrink and, for outdoor use, conformal coat only the exposed soldered resistor joints after testing.
6. Test-fit the battery pack in the sled with two Velcro straps, but leave it unplugged.
7. Mount the external stop button before final body closure.
8. Route motor wires, stop-switch wires, and signal wires through the corner cable slots toward the matching driver tray and Arduino. Any wire that crosses a printed edge or splash sheet must pass through a rubber grommet or cable gland.

## 5. Power Wiring

Keep the battery unplugged while building.

Important: do not use a solderless breadboard for any motor or battery power. Use real wire, crimped or soldered joints, distribution blocks, and strain relief.

Outdoor routing rules:

- Put connectors and distribution blocks inside the body, above the splash sheet.
- Add drip loops anywhere a cable enters from below or outside.
- Keep all open screw terminals facing inward or downward, not upward where water can sit.
- Use heat-shrink on exposed solder/crimp joints.
- Use dielectric grease sparingly on service connector shells after electrical testing; do not fill signal sockets with grease.

High-current path:

1. Battery XT60 positive goes to the inline fuse holder.
2. Fuse holder output goes to the main switch or XT60 loop key.
3. Switch output goes to the positive distribution block.
4. Battery XT60 negative goes directly to the negative distribution block.
5. Every BTS7960 `B+` terminal connects to positive distribution with 14-18 AWG wire.
6. Every BTS7960 `B-` terminal connects to negative distribution with 14-18 AWG wire.
7. The 5 V buck input positive/negative connects to the distribution blocks.

5 V output:

1. Before connecting electronics, use a multimeter and adjust the buck to 5.0-5.1 V.
2. Buck 5 V powers Arduino Mega `5V` and all BTS7960 `Vcc` pins.
3. Buck ground powers Arduino `GND`, all BTS7960 `Gnd` pins, and voltage-divider ground.

Battery voltage divider:

1. Solder a 100 kOhm resistor from switched battery positive to Arduino A0.
2. Solder a 33 kOhm resistor from Arduino A0 to common ground.
3. Heat-shrink the divider and secure it near the Arduino, above the splash sheet.
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

- BTS7960 `Vcc` goes to the regulated 5 V rail.
- BTS7960 `Gnd` goes to common ground.
- Use 22-26 AWG signal wire.
- Keep signal wires away from motor power wires where practical.

### Battery Sense And Stop Input

| Function | Signal pin |
| --- | ---: |
| External stop input | D42 |
| Battery voltage divider | A0 |

External stop wiring: use a normally-closed contact between D42 and Arduino GND. When the button is released and the wire is healthy, D42 reads LOW. Pressing the button or breaking the wire makes D42 read HIGH and the sketch refuses to drive.

## 8. Upload The Sketch

1. Install the Arduino IDE.
2. Install the Robojax BTS7960 library. The repo includes `Robojax-BTS7960-Motor-driver.zip`; in Arduino IDE use `Sketch > Include Library > Add .ZIP Library`.
3. Open `arduino-wheel-robot-code/arduino-wheel-robot-code.ino`.
4. Select `Arduino Mega or Mega 2560`.
5. Select the correct USB port.
6. Upload the sketch.

The sketch accepts these serial commands at 9600 baud: `Forward`, `Reverse`, `Left`, `Right`, `Stop`, and `STATUS`. Short forms also work: `F`, `B`, `L`, `R`, `S`, and `T`.

Telemetry prints once per second:

```text
TEL,V=12.10,LOW=0,ESTOP=0
```

## 9. First Power Test

Do this with the robot on blocks so the wheels are off the table.

1. Confirm the fuse is installed.
2. Confirm battery polarity with a multimeter before plugging in the battery.
3. Confirm the buck output is 5.0-5.1 V.
4. Turn the main switch off.
5. Plug in the battery.
6. Turn the main switch on.
7. Check Arduino power and the buck output.
8. Open Arduino Serial Monitor at 9600 baud.
9. Send `STATUS`. Confirm voltage is plausible for a 3S LiPo and `ESTOP=0`.
10. Press the external stop button and send `STATUS`; confirm `ESTOP=1`. Try `Forward`; the robot must refuse to drive. Reset the stop button before continuing.
11. Send `Forward`. All four wheels should spin for about 0.5 seconds and stop.
12. Send `Reverse`, then `Left`, then `Right`, then `Stop`.

If one wheel spins the wrong way, swap that motor's two output wires.

## 10. Build The Body And Cargo Bay

Parts:

- 4 x corner posts
- 4 x cargo shelf support blocks
- Cargo floor front-left, front-right, rear-left, rear-right quadrants
- Front-left and front-right panels
- Rear-left and rear-right panels
- 2 x side front-half panels
- 2 x side rear-half panels
- 4 x panel center joiners
- 4 x lid quadrants

Steps:

1. Bolt the four corner posts to the base using the post holes near the body corners.
2. Bolt one cargo shelf support block to the inside face of each corner post using the extra hole row about 60 mm above the base. The flat top of each support block should face upward.
3. Place the four cargo floor quadrants on the support blocks. Together they form a flat shelf above the electronics.
4. Bolt the cargo floor down through the support-block holes using M3 x 12 screws, washers, and nyloc nuts.
5. Assemble the front panel halves with one center joiner.
6. Assemble the rear panel halves with one center joiner.
7. Assemble each side from one front-half panel, one rear-half panel, and one center joiner.
8. Bolt the panels to the corner posts using M3 x 20-25 screws, washers, and nyloc nuts.
9. Place the four lid quadrants on top. Use M3 screws through the available lid/post holes where you want a retained lid.
10. Add closed-cell foam gasket tape under the lid quadrants and along upper body seams where it does not interfere with service access.
11. Cut a single flat splash sheet from thin polycarbonate, HDPE, or corrugated plastic. Mount it under the electronics bay with zip ties or M3 screws so it blocks wheel splash from below but can be removed for service.
12. Apply neutral-cure silicone only to non-service seams and splash-sheet penetrations. Do not glue the lid shut.
13. Apply foam edge bumper around the outer body perimeter where it will not rub the wheels or cover the external stop button.

Where the food goes: place a sealed food-safe container on the cargo floor. The maximum outside size is 205 x 145 x 70 mm. Food must stay in the sealed container; printed PETG/PLA is not a food-contact surface.

Use the thin silicone mat or closed-cell foam sheet under the container for outdoor vibration. If the container still slides during ground testing, add one simple strap. Do not print extra retainer rails unless the simple fix fails.

## 11. Outdoor Ground Test

1. Start indoors on blocks, then on a dry garage floor, then move outside to dry pavement.
2. Use at least 3 m of clear outdoor space and keep a hand near the hard power switch or loop key.
3. Test first with the food container empty, then with a light payload.
4. Keep first outdoor payload tests at 500 g or less. Increase only after the robot drives straight and the motors stay warm, not hot.
5. Send `Forward` once. It should move straight for a short pulse.
6. If it veers left or right, check bracket rubbing, wheel alignment, tire friction, battery charge, and motor wiring before adding sensors.
7. Send `Left` and `Right`. The robot should pivot without wheel rub.
8. After one minute of outdoor testing, touch the motor drivers and motors carefully. Warm is normal; too hot to touch means stop and inspect binding, terrain load, or wiring.
9. Check that `TEL` voltage does not drop below the low-voltage cutoff during normal light-load tests.
10. Inspect the inside of the body after the first outdoor run. If dust or light splash reached electronics, improve the single splash sheet or cable sealing before driving again.
11. Do not test in rain, puddles, wet grass, mud, sprinklers, or loose gravel. Those are different requirements, not small tweaks.

## 12. Final Physical Fit Checks

Before printing duplicate replacement parts or expanding outdoor testing, verify these by hand:

- Wheel hub depth, wheel screw length, wheel offset, and body/bracket clearance with the exact wheel set.
- Battery pack footprint, height, XT60 cable exit direction, and strap fit against `3s_lipo_battery_sled.stl`.
- Food container outside dimensions against the cargo floor. The maximum outside size is 205 x 145 x 70 mm.
- The external stop button is reachable without removing the lid.
- Wiring is strain-relieved and cannot rub the wheels.
- The splash sheet does not reduce ground clearance enough to hit normal pavement seams.
- The body and lid gasket tape do not trap heat around the BTS7960 heat sinks during short outdoor runs.
- No connector, perfboard joint, or distribution block can collect water in an upward-facing pocket.

## 13. LiPo Safety Rules

- Never charge the LiPo inside the robot.
- Never leave a charging LiPo unattended.
- Use the RC balance charger, connect both the main pack lead and the balance lead, select 3S LiPo mode, and set a conservative charge current. For a 5200 mAh pack, 5.2 A is 1C; lower is gentler.
- Stop using the pack if it swells, smells sweet/solvent-like, gets hot, or has damaged insulation.
- Store the battery at storage voltage when not using the robot.
- Keep the fuse installed. Do not bypass it for testing.
- The low-voltage telemetry is a helper, not a replacement for LiPo safety discipline.
- Keep batteries out of direct sun when the robot is paused.
