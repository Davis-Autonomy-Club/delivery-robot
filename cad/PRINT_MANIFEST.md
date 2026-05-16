# CAD Print Manifest

All STL files use millimeters. The source generator is `cad/source/generate_delivery_robot_cad.py`; it writes `cad/source/generated_manifest.json` with the same dimensions and generated file list.

This manifest is the minimum first-principles outdoor baseline. Parts removed from the baseline should stay unprinted unless a failed test in `docs/FIRST_PRINCIPLES_REDUCTION.md` justifies re-adding them.

## Print Settings

- Material: PETG minimum, ASA preferred if your printer can handle it. Do not use PLA for outdoor chassis or body parts.
- Layer height: 0.20 mm.
- Nozzle: 0.4 mm.
- Walls/perimeters: 4 for chassis, 3 for body.
- Top/bottom: 5 layers.
- Infill: 45% gyroid or cubic for chassis, 25% for trays and cargo floor, 15-20% for body panels.
- Supports: none required if parts are placed flat as exported. Use a brim for `body/corner_post_print_4.stl`.
- Scale: 100%. Do not auto-scale.

## Chassis

| File | Qty | Notes |
| --- | ---: | --- |
| `cad/print-ready/chassis/base_plate_front_left.stl` | 1 | 162 x 165 x 8 mm |
| `cad/print-ready/chassis/base_plate_front_right.stl` | 1 | 162 x 165 x 8 mm |
| `cad/print-ready/chassis/base_plate_rear_left.stl` | 1 | 162 x 165 x 8 mm |
| `cad/print-ready/chassis/base_plate_rear_right.stl` | 1 | 162 x 165 x 8 mm |
| `cad/print-ready/chassis/base_seam_joiner_long_print_2.stl` | 2 | Under-side bars across the left/right seam |
| `cad/print-ready/chassis/base_seam_joiner_short_print_2.stl` | 2 | Under-side bars across the front/rear seam |

The one-piece `cad/print-ready/full-size/v2_base_plate_full_size.stl` is included for reference, large-format printers, CNC, or remixing. Most printers should use the four split plates above.

## Electronics

| File | Qty | Notes |
| --- | ---: | --- |
| `cad/print-ready/electronics/arduino_mega_controller_tray.stl` | 1 | Mega tray with slotted tie-downs and M3 standoff holes |
| `cad/print-ready/electronics/bts7960_dual_driver_tray_print_2.stl` | 2 | Holds two BTS7960 modules per tray |
| `cad/print-ready/electronics/3s_lipo_battery_sled.stl` | 1 | Strapped tray for one 3S pack at a time |
| `cad/print-ready/electronics/buck_converter_plate.stl` | 1 | One 5 V buck plate for Arduino/BTS7960 logic |

## Cargo Bay

The food container sits above the electronics on the cargo floor, under the removable lid.

| File | Qty | Notes |
| --- | ---: | --- |
| `cad/print-ready/cargo/cargo_floor_front_left.stl` | 1 | Upper cargo floor quadrant |
| `cad/print-ready/cargo/cargo_floor_front_right.stl` | 1 | Upper cargo floor quadrant |
| `cad/print-ready/cargo/cargo_floor_rear_left.stl` | 1 | Upper cargo floor quadrant |
| `cad/print-ready/cargo/cargo_floor_rear_right.stl` | 1 | Upper cargo floor quadrant |
| `cad/print-ready/cargo/cargo_shelf_support_block_print_4.stl` | 4 | Bolts to the inside of the corner posts and supports the cargo floor |

Maximum food-safe container outer size: 205 x 145 x 70 mm. Use a sealed food-safe container; do not put bare food directly on printed plastic. Add a foam pad or strap if the container slides during ground testing.

Outdoor note: the removable underbody splash sheet is intentionally not a printed STL. Cut it from thin polycarbonate, HDPE, or corrugated plastic so it is one flat, cheap, easily replaced part.

## Body

| File | Qty | Notes |
| --- | ---: | --- |
| `cad/print-ready/body/front_panel_left.stl` | 1 | Plain front-left panel |
| `cad/print-ready/body/front_panel_right.stl` | 1 | Plain front-right panel |
| `cad/print-ready/body/rear_panel_left.stl` | 1 | Plain rear-left panel |
| `cad/print-ready/body/rear_panel_right.stl` | 1 | Plain rear-right panel |
| `cad/print-ready/body/side_panel_front_half_print_2.stl` | 2 | Front half of each side |
| `cad/print-ready/body/side_panel_rear_half_print_2.stl` | 2 | Rear half of each side |
| `cad/print-ready/body/corner_post_print_4.stl` | 4 | Four vertical body posts |
| `cad/print-ready/body/panel_center_joiner_print_4.stl` | 4 | Center seams for front, rear, left, right panels |
| `cad/print-ready/body/lid_quadrant_print_4.stl` | 4 | Four-piece removable top lid |

## Reference Files

| File | Use |
| --- | --- |
| `cad/print-ready/full-size/original_four_piece_base_merged_full_size.stl` | Existing repo STLs merged into one full-size reference |
| `cad/print-ready/full-size/v2_robot_complete_reference_not_for_print.stl` | Assembly visualization only; not intended for slicing |
| `cad/renders/checkpoint_2_base_top.png` | Rendered top-down base layout check |
| `cad/renders/checkpoint_2_complete_robot_iso.png` | Rendered visual check |
| `cad/renders/checkpoint_2_complete_robot_low_angle.png` | Rendered wheel/body clearance check |
| `cad/renders/checkpoint_2_printed_panel_samples.png` | Rendered print-part sample check |
| `cad/renders/checkpoint_3_cargo_bay_lid_removed.png` | Rendered cargo-bay check with lid removed |
| `cad/renders/checkpoint_3_cargo_shelf_and_food_box.png` | Rendered cargo shelf with max food box placeholder |
| `cad/renders/checkpoint_4_electronics_layout.png` | Rendered minimum electronics layout |
