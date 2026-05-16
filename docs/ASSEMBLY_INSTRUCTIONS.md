# Assembly Instructions

Follow this in order. Do not install the battery until the wiring checklist tells you to.

## Orientation

Use this convention for the whole build:

- Front: the side with the two HC-SR04 sensor openings and LED diffuser.
- Left/right: the robot's left and right when you stand behind it and look forward.
- Motors: `L1` = front-left, `L2` = rear-left, `R1` = front-right, `R2` = rear-right.

## 1. Print And Inspect The Parts

Print the files listed in `cad/PRINT_MANIFEST.md`. After printing:

1. Confirm the four base plates are flat and not curled.
2. Test an M3 screw through every base seam hole, panel hole, and corner-post hole. Clear tight holes with a 3.0-3.2 mm drill bit by hand.
3. Dry-fit the four base plates on a table. The total base should be about 322 x 328 mm.
4. Check the renders in `cad/renders/` against your printed parts so you know what the final shape should look like.

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

## 3. Install Motors, Brackets, Adapters, And Wheels

Parts:

- 4 x 37D gearmotors
- 4 x metal 37D motor brackets
- 4 x 12 mm hex adapters for 6 mm shafts
- 4 x 120 mm wheels
- 4 x optional printed motor spacers

Steps:

1. Attach each 37D motor to a metal bracket using the bracket manufacturer's screws. For Pololu 37D motors, do not drive screws deeper into the gearbox than the bracket instructions allow.
2. Place one bracket at each base corner. The motor shaft must point outward, away from the body.
3. Loosely bolt each bracket through the slotted holes in the base using M3 screws, washers, and nyloc nuts.
4. Slide a 12 mm hex adapter onto each 6 mm motor shaft. Put one set screw against the flat of the D shaft. Tighten both set screws.
5. Install the wheels on the adapters using the adapter's supplied wheel screw.
6. Put the robot on a flat table. Adjust the bracket slots until all four wheels touch the table evenly and do not rub the base.
7. Tighten the bracket bolts. Add the printed 37D motor spacers under the motor barrels if the motors vibrate or sag; hold spacers with zip ties through the nearby cable slots.

## 4. Mount The Electronics

Parts:

- Arduino Mega tray
- 2 x BTS7960 dual-driver trays
- Battery sled
- Arduino Mega
- 4 x BTS7960 driver modules
- Buck converter
- Fuse holder, switch, and terminal/distribution blocks

Suggested layout:

- Battery sled: centered on the base, low and forward/rear balanced.
- Arduino Mega tray: centered and easy to reach from the top lid.
- BTS7960 trays: one tray for left-side motors, one tray for right-side motors.
- Fuse and switch: close to battery positive, reachable through the lid.
- Buck converter: near Arduino, with airflow and no metal touching the board underside.

Steps:

1. Bolt the printed trays to the base through convenient base holes or zip-tie them through the printed slots.
2. Mount the Arduino Mega on nylon M3 standoffs in the Arduino tray.
3. Mount two BTS7960 modules on each driver tray. If your modules' mounting holes do not match, use zip ties through the tray slots.
4. Strap the battery into the sled with two Velcro straps, but leave it unplugged.
5. Route motor wires through the corner cable slots toward the matching driver tray.

## 5. Power Wiring

Keep all battery wiring unplugged while building.

1. Battery XT60 positive goes to the inline fuse holder.
2. Fuse holder output goes to the main switch or XT60 loop key.
3. Switch output goes to the positive distribution block.
4. Battery XT60 negative goes directly to the negative distribution block.
5. Every BTS7960 `B+` terminal connects to positive distribution with 14-18 AWG wire.
6. Every BTS7960 `B-` terminal connects to negative distribution with 14-18 AWG wire.
7. Buck converter input positive/negative connects to the same positive/negative distribution.
8. Before connecting the buck to the Arduino, use a multimeter and adjust the buck output to 5.0-5.1 V.
9. Buck 5 V output powers the Arduino Mega `5V` pin and the BTS7960 logic `Vcc` pins. Buck ground powers Arduino `GND` and all BTS7960 `Gnd` pins.

Important: all grounds must be common. Battery negative, buck negative, Arduino ground, and all BTS7960 grounds must connect together.

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

Wire the BTS7960 control header exactly like this:

| Driver | RPWM | LPWM | R_EN | L_EN | R_IS | L_IS |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `L1` front-left | D3 | D2 | D11 | D12 | D10 | D13 |
| `L2` rear-left | D7 | D6 | D23 | D24 | D22 | D25 |
| `R1` front-right | D5 | D4 | D47 | D48 | D46 | D49 |
| `R2` rear-right | D9 | D8 | D51 | D52 | D50 | D53 |

For every driver:

- BTS7960 `Vcc` goes to the regulated 5 V logic rail.
- BTS7960 `Gnd` goes to the common ground rail.
- Use 22-26 AWG signal wire.
- Keep signal wires away from the motor power wires where practical.

## 8. Optional Sensors And Lights

The CAD includes front openings for two HC-SR04 modules. A simple wiring plan:

| Sensor | VCC | GND | TRIG | ECHO |
| --- | --- | --- | ---: | ---: |
| Front-left HC-SR04 | 5 V | GND | D30 | D31 |
| Front-right HC-SR04 | 5 V | GND | D32 | D33 |

The current sketch does not use the ultrasonic sensors; these pins are reserved so you can add obstacle logic later without rewiring the body.

For the front LED slot, use a 5 V strip behind `front_led_diffuser_clear_print_1.stl`. Power it from the 5 V rail only if your buck converter has enough current margin.

## 9. Upload The Sketch

1. Install the Arduino IDE.
2. Install the Robojax BTS7960 library. The repo includes `Robojax-BTS7960-Motor-driver.zip`; in Arduino IDE use `Sketch > Include Library > Add .ZIP Library`.
3. Open `arduino-wheel-robot-code/arduino-wheel-robot-code.ino`.
4. Select `Arduino Mega or Mega 2560`.
5. Select the correct USB port.
6. If an HC-05 Bluetooth module is connected to pins 0/1, unplug it before uploading.
7. Upload the sketch.

The sketch accepts these serial commands at 9600 baud: `Forward`, `Reverse`, `Left`, `Right`, `Stop`. Short forms also work: `F`, `B`, `L`, `R`, `S`.

## 10. First Power Test

Do this with the robot on blocks so the wheels are off the table.

1. Confirm the fuse is installed.
2. Confirm battery polarity with a multimeter before plugging in the battery.
3. Turn the main switch off.
4. Plug in the battery.
5. Turn the main switch on.
6. Check the Arduino power LED and the buck converter output.
7. Open Arduino Serial Monitor at 9600 baud.
8. Send `Forward`. All four wheels should spin for about 0.75 seconds and stop.
9. Send `Reverse`, then `Left`, then `Right`, then `Stop`.

If one wheel spins the wrong way, swap that motor's two output wires. If an entire side spins backward, check that `L1/L2/R1/R2` drivers are not swapped.

## 11. Build The Body And Cargo Bay

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
12. Place the four lid quadrants on top. Use M3 screws through the available lid/post holes where you want a fixed lid, or leave the lid loose during debugging.

Where the food goes: remove the lid quadrants and place a sealed food-safe container on the cargo floor, inside the four retainer rails. The maximum outside size is 205 x 145 x 70 mm. Food must stay in the sealed container; printed PETG/PLA is not a food-contact surface.

## 12. Ground Test

1. Put the robot on the floor with at least 2 m of clear space.
2. Test first with the food container empty, then with a light payload.
3. Keep first payload tests at 500 g or less. Increase only after the robot drives straight and the motors stay warm, not hot.
4. Send `Forward` once. It should move straight for a short pulse.
5. If it veers left, either the left wheels are weaker or the right wheels are faster. Check bracket rubbing, wheel alignment, and battery charge.
6. Send `Left` and `Right`. The robot should pivot.
7. After one minute of testing, touch the motor drivers and motors carefully. Warm is normal; too hot to touch means stop and inspect binding or wiring.

## 13. LiPo Safety Rules

- Never charge the LiPo inside the robot.
- Never leave a charging LiPo unattended.
- Stop using the pack if it swells, smells sweet/solvent-like, gets hot, or has damaged insulation.
- Store the battery at storage voltage when not using the robot.
- Keep the fuse installed. Do not bypass it for testing.
