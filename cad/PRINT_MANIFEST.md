# CAD Print Manifest

All STL files use millimeters. The source generator is `cad/source/generate_delivery_robot_cad.py`; it writes `cad/source/generated_manifest.json` with the same dimensions and generated file list.

## Print Settings

- Material: PETG preferred. PLA is acceptable for a first indoor prototype body, but use PETG for chassis and electronics trays.
- Layer height: 0.20 mm.
- Nozzle: 0.4 mm.
- Walls/perimeters: 4 for chassis, 3 for body.
- Top/bottom: 5 layers.
- Infill: 45% gyroid or cubic for chassis, 25% for trays and cargo floor, 15-20% for body panels, 80-100% for motor spacers.
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
| `cad/print-ready/chassis/printed_37d_motor_spacer_print_4.stl` | 4 | Optional vibration/support saddle behind each 37D motor |

The one-piece `cad/print-ready/full-size/v2_base_plate_full_size.stl` is included for reference, large-format printers, CNC, or remixing. Most printers should use the four split plates above.

## Electronics

| File | Qty | Notes |
| --- | ---: | --- |
| `cad/print-ready/electronics/arduino_mega_controller_tray.stl` | 1 | Mega tray with slotted tie-downs and M3 standoff holes |
| `cad/print-ready/electronics/bts7960_dual_driver_tray_print_2.stl` | 2 | Holds two BTS7960 modules per tray |
| `cad/print-ready/electronics/3s_lipo_battery_sled.stl` | 1 | Strapped tray for one 3S pack at a time; verify exact 5200 mAh pack dimensions and cable exit before printing battery-specific add-ons |
| `cad/print-ready/electronics/raspberry_pi_companion_tray.stl` | 1 | Raspberry Pi companion-computer tray for camera/LTE/teleop host |
| `cad/print-ready/electronics/usb_lte_modem_tray.stl` | 1 | Strap-down tray for a compact USB LTE modem |
| `cad/print-ready/electronics/battery_telemetry_sensor_plate.stl` | 1 | Mounting plate for ACS724 current sensor and voltage-divider board |
| `cad/print-ready/electronics/buck_converter_plate_print_2.stl` | 2 | Two 5 V buck plates: logic/accessory rail and Pi/camera/LTE rail |

## Cargo Bay

These parts create the food compartment. The food container sits above the electronics on the cargo floor, inside the retainer rails, under the removable lid.

| File | Qty | Notes |
| --- | ---: | --- |
| `cad/print-ready/cargo/cargo_floor_front_left.stl` | 1 | Upper cargo floor quadrant |
| `cad/print-ready/cargo/cargo_floor_front_right.stl` | 1 | Upper cargo floor quadrant |
| `cad/print-ready/cargo/cargo_floor_rear_left.stl` | 1 | Upper cargo floor quadrant |
| `cad/print-ready/cargo/cargo_floor_rear_right.stl` | 1 | Upper cargo floor quadrant |
| `cad/print-ready/cargo/cargo_shelf_support_block_print_4.stl` | 4 | Bolts to the inside of the corner posts and supports the cargo floor |
| `cad/print-ready/cargo/cargo_retainer_long_rail_print_2.stl` | 2 | Long rails that keep the food container from sliding sideways |
| `cad/print-ready/cargo/cargo_retainer_short_rail_print_2.stl` | 2 | Short rails that keep the food container from sliding forward/back |

Maximum food-safe container outer size: 205 x 145 x 70 mm. Use a sealed food-safe container; do not put bare food directly on printed plastic.

## Body

| File | Qty | Notes |
| --- | ---: | --- |
| `cad/print-ready/body/front_panel_left_hcsr04_led.stl` | 1 | Front-left panel, HC-SR04 and LED opening |
| `cad/print-ready/body/front_panel_right_hcsr04_led.stl` | 1 | Front-right panel, HC-SR04 and LED opening |
| `cad/print-ready/body/rear_panel_left.stl` | 1 | Rear-left panel |
| `cad/print-ready/body/rear_panel_right.stl` | 1 | Rear-right panel |
| `cad/print-ready/body/side_panel_front_half_print_2.stl` | 2 | Front half of each side |
| `cad/print-ready/body/side_panel_rear_half_print_2.stl` | 2 | Rear half of each side |
| `cad/print-ready/body/corner_post_print_4.stl` | 4 | Four vertical body posts |
| `cad/print-ready/body/panel_center_joiner_print_4.stl` | 4 | Center seams for front, rear, left, right panels |
| `cad/print-ready/body/lid_quadrant_print_4.stl` | 4 | Four-piece removable top lid |
| `cad/print-ready/body/camera_module_mount_print_2.stl` | 2 | Front and rear USB/UVC camera mounts with M2 holes and zip-tie slots |
| `cad/print-ready/body/micro_servo_lid_lock_mount.stl` | 1 | MG90S/SG90-size servo cradle for programmatic lid lock |
| `cad/print-ready/body/lid_lock_servo_cam.stl` | 1 | Printed cam that attaches to the micro-servo horn |
| `cad/print-ready/body/lid_lock_keeper_plate.stl` | 1 | Catch plate that the servo cam rotates under when locked |

## Accessories

| File | Qty | Notes |
| --- | ---: | --- |
| `cad/print-ready/accessories/wheel_white_cap_print_4.stl` | 4 | Cosmetic wheel caps for 120 mm wheels; mount through hub holes if your wheel/hub pattern allows |
| `cad/print-ready/accessories/front_led_diffuser_clear_print_1.stl` | 1 | Print in clear/natural material and snap/tape behind front LED slot |

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
| `cad/renders/checkpoint_3_cargo_shelf_and_food_box.png` | Rendered cargo shelf with max-size food box placeholder |
| `cad/renders/checkpoint_4_electronics_layout.png` | Rendered v2.2 electronics layout with Pi, LTE, telemetry, and buck plates |
