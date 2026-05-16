# Delivery Robot Arduino Platform


## Current v2.2 Build Package

This repo is now the v2.2 delivery-robot prototype package: CAD, Arduino firmware, wiring, shopping list/cart state, and assembly instructions for a four-wheel Arduino Mega + BTS7960 rover with encoder motors, a cargo bay, lid lock, cameras, LTE provision, battery telemetry, lid-closed sensing, and an external stop input.

Start here:

- Current bill of materials: [`docs/SHOPPING_LIST.md`](docs/SHOPPING_LIST.md)
- Current Amazon/Pololu cart sync and known missing items: [`docs/CURRENT_AMAZON_CART_SYNC.md`](docs/CURRENT_AMAZON_CART_SYNC.md)
- Purchase links: [`docs/SOURCED_SHOPPING_LINKS_CA.md`](docs/SOURCED_SHOPPING_LINKS_CA.md)
- Assembly instructions: [`docs/ASSEMBLY_INSTRUCTIONS.md`](docs/ASSEMBLY_INSTRUCTIONS.md)
- Wiring source of truth: [`docs/CANONICAL_WIRING_V2.md`](docs/CANONICAL_WIRING_V2.md)
- CAD print manifest: [`cad/PRINT_MANIFEST.md`](cad/PRINT_MANIFEST.md)

The old root-level wiring diagram and the old `3D Prints/` folder are retained only as original project history/reference. For the current build, use the v2.2 files under `cad/print-ready/`.

## Original Project Background

The original project was a simple Arduino four-wheel robot inspired by Droiid Package Delivery Robot. The current repo has been expanded into a full v2.2 delivery-robot prototype package.

Original project credit remains: [smartbuilds.io](https://smartbuilds.io)

## Complete v2.2 Build Package

The original repo only included four cut chassis STL files. This repo now includes a full compatible v2.2 build package:

- Print-ready CAD: [`cad/print-ready`](cad/print-ready)
- CAD source generator: [`cad/source/generate_delivery_robot_cad.py`](cad/source/generate_delivery_robot_cad.py)
- Print manifest and settings: [`cad/PRINT_MANIFEST.md`](cad/PRINT_MANIFEST.md)
- Full shopping list: [`docs/SHOPPING_LIST.md`](docs/SHOPPING_LIST.md)
- Current cart sync: [`docs/CURRENT_AMAZON_CART_SYNC.md`](docs/CURRENT_AMAZON_CART_SYNC.md)
- Full assembly, wiring, upload, and test instructions: [`docs/ASSEMBLY_INSTRUCTIONS.md`](docs/ASSEMBLY_INSTRUCTIONS.md)
- Canonical v2.2 wiring: [`docs/CANONICAL_WIRING_V2.md`](docs/CANONICAL_WIRING_V2.md)
- Visual render checks: [`cad/renders`](cad/renders)

The v2.2 CAD/package keeps the Arduino Mega + four BTS7960 drivetrain architecture, but now uses encoder 37D gearmotors, a Raspberry Pi companion computer, front and rear camera mounts, a USB LTE modem tray, battery voltage/current telemetry, a programmatic micro-servo lid lock, lid-closed sensing, and an external stop input. The cargo bay still carries a sealed food-safe container up to 205 x 145 x 70 mm.

Important: the old Fritzing/block-diagram files are retained only as original project history. Do not use them as the v2.2 wiring source. Use [`docs/CANONICAL_WIRING_V2.md`](docs/CANONICAL_WIRING_V2.md) and [`docs/ASSEMBLY_INSTRUCTIONS.md`](docs/ASSEMBLY_INSTRUCTIONS.md).


# Legacy Original Files

The following files are retained only as original-project history and reference material:

- `3D Prints/Droiid Mini v1.0 (Cut)-*.stl`
- `arduino-wheel-robot-diagram.png`
- `arduino-wheel-robot-diagram_bb.png`
- `arduino-wheel-robot-diagram.fzz`

Do not use those legacy STLs, diagrams, or historical part assumptions as the v2.2 build source. The current print files live in `cad/print-ready/`, and the current wiring source is [`docs/CANONICAL_WIRING_V2.md`](docs/CANONICAL_WIRING_V2.md).
