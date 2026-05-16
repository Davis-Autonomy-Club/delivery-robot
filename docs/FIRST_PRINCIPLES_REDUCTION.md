# First-Principles Reduction Pass

The prompt describes a four-step algorithm, but only three named steps were provided. This pass applies the supplied steps in order and does not invent a fourth step.

## 1. Dumb Down The Requirements

Original v2.2 assumption:

- Build a delivery robot with Arduino drivetrain control, encoder motors, Raspberry Pi companion computer, front/rear cameras, LTE, current telemetry, servo lid lock, lid sensor, ultrasonic openings, LED diffuser, and a large generated CAD package.

Outdoor physics/operation actually require for the current repo:

- Carry a sealed food-safe container.
- Drive outdoors on pavement, concrete, or packed paths under direct human supervision.
- Stop immediately from a hard power switch and a firmware drive lockout.
- Protect the LiPo with a fuse, proper charger, and low-voltage cutoff.
- Keep motor power off solderless breadboards and strain-relieve wiring.
- Fit on a common 220 x 220 mm printer bed.
- Survive sun, warm body temperatures, vibration, grit, and light splash from the wheels.
- Keep water out of powered electronics during fair-weather use; this is not a rainstorm, puddle, or submersion vehicle.

The current repo does not include teleop dashboard software, route planning, camera streaming, LTE networking, obstacle avoidance, closed-loop odometry, or electronic access control. Those capabilities are therefore not baseline requirements. They are future experiments that must earn their way back with a failing test.

## 2. Remove The Part Or Process

Removed from the default build:

- Raspberry Pi, microSD, USB-C power pigtail, USB LTE modem, SIM/data plan, extra USB cables, and second 5 V buck rail.
- Front/rear cameras and camera mounts.
- Servo lid lock, servo mount, cam, keeper plate, and `LOCK`/`UNLOCK` firmware.
- Lid-closed sensor and its firmware drive lockout.
- ACS724 current sensor and current telemetry.
- Encoder wiring, encoder interrupts, `ZEROENC`, and encoder telemetry.
- HC-SR04 sensors, LED strip, and clear LED diffuser.
- Cosmetic wheel caps.
- Optional printed motor spacers as default parts.
- Cargo retainer rails as default parts; use the sealed container plus a rubber/foam pad or strap only if the payload slides during ground testing.

Kept because physics or safety still justify them:

- Arduino Mega, four BTS7960 motor drivers, four 37D gearmotors, metal motor brackets, wheel adapters, and 120 mm wheels.
- One 3S LiPo installed at a time, real RC balance charger, inline fuse, and hard main switch or XT60 loop key.
- One 5 V buck converter for Arduino/BTS logic.
- NC external stop input on D42.
- Battery voltage divider on A0 for low-voltage cutoff.
- Printed split chassis, simple body panels, corner posts, upper cargo floor, lid quadrants, and battery/electronics trays.
- Outdoor ruggedization: PETG/ASA instead of PLA, stainless hardware, sealed switch/stop hardware, cable glands or grommets for any exits, conformal coating or sealed heat-shrink on small solder joints, drip loops, closed-cell foam gasket tape at lid/panel seams, foam bumper, and one flat removable splash sheet under the electronics bay.

## 3. Simplify Or Optimize

The baseline target is a blunt, serviceable outdoor "children's toy" robot:

- Big simple plates, posts, trays, and panels.
- No delicate camera brackets or exposed extra sensor holes.
- One obvious battery path: battery, fuse, switch, distribution, drivers, buck.
- One low-voltage sense path.
- One manual firmware stop input.
- Short command vocabulary: `F`, `B`, `L`, `R`, `S`, and `STATUS`.
- No claim of full waterproofing. The simpler and more honest target is splash-resistant fair-weather operation.

## Re-Add Tests

Only re-add removed systems when a concrete test fails:

| Failing test | Re-add candidate |
| --- | --- |
| The robot cannot be driven without standing beside it | Raspberry Pi teleop stack, then one camera, then LTE only after local Wi-Fi teleop works |
| The robot cannot drive straight enough for the demo route | Encoder wiring and closed-loop speed control |
| The payload slides during normal turns | Foam pad, then one strap, then printed rails only if the strap fails |
| The body needs visible status for operators | One LED indicator, not a full decorative light strip |
| The lid opens during normal driving | Passive latch or strap first; servo lock only if remote electronic access is an actual requirement |
| Motor drivers overheat or fuses nuisance-trip with no obvious cause | Current sensor or clamp meter test fixture |
| Light wheel splash reaches electronics during tests | Larger single-piece splash sheet or simple wheel splash guards |
| The robot must operate in rain or through puddles | Redesign around sealed commercial enclosures and sealed motors; do not patch this prototype |

Until one of those tests fails, the best part is no part.
