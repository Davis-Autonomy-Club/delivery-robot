# Delivery Robot Arduino Platform

## Minimum Outdoor First-Principles Build

This repo is now organized around the smallest useful outdoor delivery-robot prototype: an Arduino Mega drives four BTS7960 motor drivers and four 37D gearmotors on a simple printed chassis. The robot carries a sealed food-safe container on an upper cargo shelf and is tested outdoors under direct human supervision on pavement, concrete, or packed paths.

The guiding rule is: the best part is no part, and the best process is no process. The previous v2.2 package provisioned a Raspberry Pi, LTE, cameras, encoder telemetry, a servo lid lock, current sensing, ultrasonic openings, an LED diffuser, and cosmetic accessories before the repo had software that required them. Those systems stay out of the default build. Outdoor use instead adds only ruggedization that physics forces: UV/heat-safe printed material, stainless hardware, sealed switch hardware, gasket tape, drip loops, strain relief, and a simple removable splash sheet under the electronics bay.

Start here:

- Print-ready CAD: [`cad/print-ready`](cad/print-ready)
- CAD source generator: [`cad/source/generate_delivery_robot_cad.py`](cad/source/generate_delivery_robot_cad.py)
- Print manifest and settings: [`cad/PRINT_MANIFEST.md`](cad/PRINT_MANIFEST.md)
- Shopping list: [`docs/SHOPPING_LIST.md`](docs/SHOPPING_LIST.md)
- Current Amazon/Pololu cart sync and known missing items: [`docs/CURRENT_AMAZON_CART_SYNC.md`](docs/CURRENT_AMAZON_CART_SYNC.md)
- Purchase links: [`docs/SOURCED_SHOPPING_LINKS_CA.md`](docs/SOURCED_SHOPPING_LINKS_CA.md)
- Assembly, wiring, upload, and test instructions: [`docs/ASSEMBLY_INSTRUCTIONS.md`](docs/ASSEMBLY_INSTRUCTIONS.md)
- Wiring source of truth: [`docs/CANONICAL_WIRING_V2.md`](docs/CANONICAL_WIRING_V2.md)
- Reduction audit: [`docs/FIRST_PRINCIPLES_REDUCTION.md`](docs/FIRST_PRINCIPLES_REDUCTION.md)

The old root-level wiring diagram and the old `3D Prints/` folder are retained only as original project history/reference. For the current build, use the files under `cad/print-ready/` and the current wiring source in [`docs/CANONICAL_WIRING_V2.md`](docs/CANONICAL_WIRING_V2.md).

## Original Project Background

The original project was a simple Arduino four-wheel robot inspired by Droiid Package Delivery Robot. Original project credit remains: [smartbuilds.io](https://smartbuilds.io).

## Legacy Original Files

The following files are retained only as original-project history and reference material:

- `3D Prints/Droiid Mini v1.0 (Cut)-*.stl`
- `arduino-wheel-robot-diagram.png`
- `arduino-wheel-robot-diagram_bb.png`
- `arduino-wheel-robot-diagram.fzz`

Do not use those legacy STLs, diagrams, or historical part assumptions as the current build source.

## Legacy Original Part List

This section is preserved from the original project for history. Do not buy from this list for the current build; use [`docs/SHOPPING_LIST.md`](docs/SHOPPING_LIST.md).

Motor parts:

- Battery LiPo 11.1 V, 3500 mAh
- 4 x 12 V DC geared motor x6, high torque, 300 RPM
- 4 x BTS7960b motor driver
- Arduino Mega

Hardware/chassis:

- Wheels, stroller style
- Chassis, 3D printed files provided in repo
- M3 screws

Sensors, optional in the original project:

- Bluetooth HC-05
- Ultrasonic sensors x 2

## Legacy BTS7960 Pin Reference

This robot uses BTS7960/IBT-2 style motor driver modules. Check the exact board you buy, but typical pins are:

| Pin | Function | Description |
| --- | --- | --- |
| 1 | RPWM | Forward PWM signal, active high |
| 2 | LPWM | Reverse PWM signal, active high |
| 3 | R_EN | Forward-drive enable |
| 4 | L_EN | Reverse-drive enable |
| 5 | R_IS | Forward current alarm output |
| 6 | L_IS | Reverse current alarm output |
| 7 | Vcc | 5 V logic supply |
| 8 | Gnd | Logic ground |

## Block Diagram

Legacy note: this image is incomplete for the current build. Use [`docs/CANONICAL_WIRING_V2.md`](docs/CANONICAL_WIRING_V2.md) instead.

![Droiid Block Diagram](arduino-wheel-robot-diagram.png)
