# Shopping List

This list is the compatible v2 bill of materials for the CAD package in `cad/print-ready/`. It keeps the existing Arduino Mega + 4 x BTS7960 architecture, but locks the mechanical design to common 37D 12 V gearmotors with 6 mm D shafts and 120 mm 12 mm-hex wheels.

Live California-friendly buying links are in [`docs/SOURCED_SHOPPING_LINKS_CA.md`](SOURCED_SHOPPING_LINKS_CA.md).

## Buy These Parts

| Qty | Item | Exact requirement | Good source / reference |
| ---: | --- | --- | --- |
| 1 | Arduino Mega 2560 Rev3 or compatible clone | 5 V logic, Mega footprint, USB-B programming cable | [Arduino Mega 2560 Rev3 datasheet](https://docs.arduino.cc/resources/datasheets/A000067-datasheet.pdf) |
| 4 | BTS7960 / IBT-2 motor driver modules | One 43 A BTS7960 module per motor; typical board 50 x 50 x 43 mm | [HandsOn BTS7960 guide](https://www.handsontec.com/dataspecs/module/BTS7960%20Motor%20Driver.pdf) |
| 4 | 12 V 37D metal gearmotor, 30:1, no encoder | 37 mm diameter, 6 mm D shaft, about 330 RPM; Pololu #4742 is the reference motor | [Pololu 37Dx52L 30:1 12 V motor](https://www.pololu.com/product-info-merged/4742) |
| 4 | 37D motor brackets | Metal brackets for 37D gearmotors; use metal, not printed load-bearing brackets | [Pololu 37D machined bracket #1995](https://www.pololu.com/product/1995) |
| 2 packs | 12 mm hex wheel adapters for 6 mm shaft | 2 adapters per pack, 4 total; standard or extended length is OK | [Pololu #2686 12 mm hex adapter](https://www.pololu.com/product/2686) |
| 4 | 120 mm wheels | 120 x 60 mm Dagu Wild Thumper wheels or any 1/10 RC wheel with 12 mm hex and about 120 mm OD | [Pololu adapter page showing 120 x 60 Wild Thumper wheel compatibility](https://www.pololu.com/product/2686) |
| 1 | 3S LiPo battery | 11.1 V nominal, 3500 mAh or larger, 30C or better, XT60 plug preferred | Match the original repo part list |
| 1 | Balance charger for 3S LiPo | Must support LiPo balance charging; do not charge through the robot wiring | Any reputable RC charger |
| 1 | 5 V buck converter | 6-27 V input, regulated 5 V output, at least 5 A | Needed for Mega + BTS7960 logic rail |
| 1 | Inline blade fuse holder | Rated 30 A or higher, installed close to battery positive | Automotive mini/ATO blade holder |
| 2 each | Blade fuses | 25 A and 30 A; start with 25 A, use 30 A only if nuisance trips occur | Automotive mini/ATO fuses |
| 1 | Main power switch or XT60 loop key | DC rated 30 A or higher | Put after the fuse |
| 2 | HC-SR04 ultrasonic sensors | Optional but the front CAD panels have matching openings | [HC-SR04 dimensions/reference](https://www.digikey.com/en/htmldatasheets/production/3822706/0/0/1/hc-sr04) |
| 1 | HC-05 Bluetooth module | Optional serial control; disconnect while uploading if using Mega pins 0/1 | Common Arduino HC-05 module |
| 1 | 5 V LED strip section | Optional front status light, 220-230 mm long | Use the printed clear diffuser |
| 1 | Food-safe lidded container | Must fit inside 205 x 145 x 70 mm outer dimensions; food goes here, under the robot lid, above the electronics shelf | Small sealed meal-prep/takeout container |

## Hardware And Consumables

| Qty | Item | Use |
| ---: | --- | --- |
| 1 roll | PETG filament, white or light color | Chassis, trays, body; PLA is OK for indoor demos but PETG is safer outdoors/in heat |
| 1 small length | Clear/natural PETG or PLA | Front LED diffuser |
| 80+ | M3 x 12 mm machine screws | Base seams, trays, cargo floor, cargo rails, panel joiners |
| 30+ | M3 x 20-25 mm machine screws | Body panels through corner posts |
| 100+ | M3 washers | Use under screw heads and nuts against printed plastic |
| 80+ | M3 nyloc nuts | All body/chassis fastening |
| 8 | M3 x 8 mm screws | Arduino/BTS board standoffs if your standoffs need short screws |
| 10 | M3 nylon standoffs, 6-10 mm tall | Arduino Mega and motor drivers |
| 12+ | Small zip ties | Backup board retention and wire strain relief |
| 2 | Velcro battery straps, 20 mm wide | Battery sled |
| 1 | Thin silicone mat or closed-cell foam sheet | Optional non-slip pad under the sealed food container |
| 2 m | 14 AWG red/black silicone wire | Battery, fuse, switch, distribution to driver power terminals |
| 3 m | 18 AWG red/black silicone wire | Motor leads from BTS7960 to motors |
| 1 kit | 22-26 AWG Dupont jumpers | Mega-to-BTS7960 logic wiring |
| 1 kit | XT60 connectors or XT60 pigtails | Battery connection and service disconnect |
| 1 | WAGO 221 or screw terminal distribution block | Battery positive/negative distribution |
| 1 | Heat-shrink tubing assortment | Insulate soldered/crimped connections |

## Tools

3D printer with at least a 220 x 220 mm bed, 2.0 mm and 2.5 mm hex keys, small Phillips screwdriver, needle-nose pliers, wire stripper, crimper or soldering iron, multimeter, flush cutters, and a LiPo-safe charging bag.

## Substitution Rules

The CAD is forgiving, but do not change these without editing the CAD first:

- Motors must be 37 mm diameter with 6 mm output shafts. The base slots tolerate motor length differences, but the wheel adapters and wheel caps assume 6 mm shaft + 12 mm hex.
- Wheels should be close to 120 mm outside diameter and no wider than 60 mm. Smaller wheels reduce ground clearance; wider wheels may hit the motor/bracket area.
- Motor drivers must be one BTS7960/IBT-2-style module per motor. Dual-channel drivers are not pin-compatible with the supplied wiring table.
- The battery must be a 3S pack. A 4S pack can exceed the safe input range of the listed BTS7960 modules and the existing Arduino power assumptions.
- The food container must be sealed and no larger than 205 x 145 x 70 mm outside. The printed cargo bay is a carrier, not a food-contact surface.
