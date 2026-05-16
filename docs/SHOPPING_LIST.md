# Shopping List

This is the minimum first-principles outdoor bill of materials for `cad/print-ready/`. It keeps only the hardware needed to make a supervised fair-weather outdoor delivery-robot prototype drive, stop, protect its battery, resist light splash/grit/vibration, and carry a sealed food container.

Buying links are collected in [`docs/SOURCED_SHOPPING_LINKS_CA.md`](SOURCED_SHOPPING_LINKS_CA.md). The live Amazon cart snapshot from the latest manual trim is recorded in [`docs/CURRENT_AMAZON_CART_SYNC.md`](CURRENT_AMAZON_CART_SYNC.md). Re-check exact availability before purchase.

## Current Cart Status

As of the May 16, 2026 cart sync, the active Amazon cart contains 36 line items / 38 units with a $617.05 pre-tax subtotal. The live Pololu cart was also verified at $379.35, so the combined active-cart subtotal is $996.40 before tax and shipping.

That active Amazon cart is not a complete build kit by itself. It assumes some required parts and tools are already on hand or will be supplied separately:

- Compatible 120 mm / 12 mm-hex wheels, fuses, inline fuse holder, power distribution block, printable filament, battery straps, LiPo-safe bag, and basic wiring/assembly tools are not active in the Amazon cart.
- The two cameras, LTE modem, SIM, and USB cabling are active, but the Raspberry Pi and microSD card are not. Keep that only if a Pi and microSD are already available; otherwise add them back before building the camera/LTE stack.
- The B6 charger and XT60 pigtail kit are still active. If the existing OVONIC X1 charger and MCIGICM XT60H connectors will replace them, delete those cart lines and update this section again.
- The known saved-for-later add-back subtotal for wheels, fuses, fuse holders, and WAGO connectors is at least $68.82 before tax/shipping, so the active carts are below $1,000 only because several required items are outside the active cart.

## Buy These Parts

| Qty | Item | Exact requirement | Good source / reference |
| ---: | --- | --- | --- |
| 1 | Arduino Mega 2560 Rev3 or compatible clone | 5 V logic, Mega footprint, USB-B programming cable | [Arduino Mega 2560 Rev3 datasheet](https://docs.arduino.cc/resources/datasheets/A000067-datasheet.pdf) |
| 4 | BTS7960 / IBT-2 motor driver modules | One module per motor; typical board 50 x 50 x 43 mm | [HandsOn BTS7960 guide](https://www.handsontec.com/dataspecs/module/BTS7960%20Motor%20Driver.pdf) |
| 4 | 12 V 37D metal gearmotors, 30:1, 6 mm D shaft | Encoders are not required for the baseline; if you buy encoder motors, leave encoder leads unconnected until a straight-line test proves they are needed | Pololu 37D class gearmotor |
| 4 | 37D motor brackets | Metal brackets for 37D gearmotors; do not use printed load-bearing brackets | [Pololu 37D machined bracket #1995](https://www.pololu.com/product/1995) |
| 2 packs | 12 mm hex wheel adapters for 6 mm shaft | 2 adapters per pack, 4 total | [Pololu #2686 12 mm hex adapter](https://www.pololu.com/product/2686) |
| 4 | 120 mm rubber-tread wheels | About 120 mm OD and no wider than 60 mm; avoid hard plastic tires outdoors; verify hub depth and body clearance before final assembly | [Pololu adapter page showing 120 x 60 Wild Thumper compatibility](https://www.pololu.com/product/2686) |
| 1 | 3S LiPo battery | 11.1 V nominal, 5000-5200 mAh target, 30C or better, XT60 plug preferred | Reputable RC pack |
| 1 | Real RC balance charger for 3S LiPo | Must use main pack output plus balance lead and show charge state clearly; do not charge through robot wiring | B6AC/IMAX-style RC charger or better |
| 1 | 5 V buck converter, 5 A | Powers Arduino and BTS7960 logic rail | [Pololu D24V50F5 5V 5A buck #2851](https://www.pololu.com/product/2851) |
| 1 | Inline blade fuse holder | Rated 30 A or higher, installed close to battery positive | Automotive mini/ATO blade holder |
| 2 each | Blade fuses | 25 A and 30 A; start with 25 A, use 30 A only if nuisance trips occur | Automotive mini/ATO fuses |
| 1 | Main power switch or XT60 loop key | DC rated 30 A or higher; weather-resistant if panel-mounted | Put after the fuse |
| 1 each | 100 kOhm and 33 kOhm 1% resistors | Battery voltage divider for Arduino A0; 100 kOhm from switched battery positive to A0, 33 kOhm from A0 to ground | Metal film resistors |
| 1 | Small perfboard or terminal strip | Holds voltage-divider resistors and strain relief | Any small solderable board |
| 1 | Weather-resistant external stop button | Latching mushroom-style switch with normally-closed contacts; wired to Arduino D42 as a drive lockout input | 22 mm NC emergency stop switch |
| 1 | USB A-to-B cable | Laptop to Arduino Mega USB-B programming/serial port | Short printer-style USB 2.0 cable |
| 1 | Food-safe lidded container | Must fit inside 205 x 145 x 70 mm outer dimensions; food stays in this sealed container | Small sealed meal-prep/takeout container |

Do not buy these for the baseline: Raspberry Pi, microSD card, LTE modem, SIM/data plan, USB cameras, second buck converter, current sensor, lid sensor, servo lock, ultrasonic sensors, LED strip, USB hub, camera hardware, wheel caps, or cosmetic lighting. Re-add only when a specific test in [`FIRST_PRINCIPLES_REDUCTION.md`](FIRST_PRINCIPLES_REDUCTION.md) fails.

## Hardware And Consumables

| Qty | Item | Use |
| ---: | --- | --- |
| 1 roll | PETG or ASA filament, white or light color | Outdoor chassis, trays, and body; do not use PLA for outdoor heat/sun |
| 70+ | Stainless M3 x 12 mm machine screws | Base seams, trays, cargo floor, and panel joiners |
| 30+ | Stainless M3 x 20-25 mm machine screws | Body panels through corner posts |
| 80+ | Stainless M3 washers | Use under screw heads and nuts against printed plastic |
| 70+ | Stainless M3 nyloc nuts | Chassis/body fastening |
| 10 | Stainless M3 x 8 mm screws | Arduino/BTS board standoffs if your standoffs need short screws |
| 10 | M3 nylon standoffs, 6-10 mm tall | Arduino Mega and motor drivers |
| 20+ | Small zip ties | Board retention and wire strain relief |
| 2 | Velcro battery straps, 20 mm wide | Battery sled |
| 1 | Thin silicone mat or closed-cell foam sheet | Non-slip pad under the sealed food container |
| 1 roll | Outdoor foam edge bumper | Soft bumper around the body perimeter for low-speed contact protection |
| 1 sheet | Thin polycarbonate, HDPE, or corrugated plastic | One flat removable splash sheet under the electronics bay; cut by hand, do not over-CAD it |
| 1 roll | Closed-cell foam gasket tape | Lid and upper body seam splash resistance |
| 1 kit | Rubber grommets or cable glands | Any wire exit through a panel or splash sheet |
| 1 tube | Neutral-cure silicone sealant | Seal non-service seams, cable-gland edges, and splash-sheet penetrations |
| 1 bottle | Electronics conformal coating | Optional but recommended for exposed perfboard divider joints; keep connectors and switches uncoated |
| 1 small tube | Dielectric grease | XT60 shell edges and exposed service connectors; do not use as a structural seal |
| 2 m | 14 AWG red/black silicone wire | Battery, fuse, switch, and distribution to driver power terminals |
| 3 m | 18 AWG red/black silicone wire | Motor leads from BTS7960 modules to motors |
| 2 m | 22-26 AWG signal wire | Mega-to-BTS7960 signals, external stop, and voltage divider |
| 1 kit | Dupont jumpers | Short bench-test logic wiring; replace loose jumpers with crimped leads before driving |
| 1 kit | XT60 connectors or XT60 pigtails | Battery connection and service disconnect |
| 1 | WAGO 221 or screw terminal distribution block | Battery positive/negative distribution |
| 1 | Heat-shrink tubing assortment | Insulate soldered/crimped connections |

## Tools

3D printer with at least a 220 x 220 mm bed, 2.0 mm and 2.5 mm hex keys, small Phillips screwdriver, needle-nose pliers, wire stripper, crimper or soldering iron, multimeter, flush cutters, LiPo-safe charging bag, deburring knife, and scissors/shears for the splash sheet.

## Substitution Rules

The CAD is forgiving, but do not change these without editing the CAD first:

- Motors must be 37 mm diameter gearmotors with 6 mm output shafts. Encoder motors are acceptable, but the baseline does not wire the encoders.
- Wheels should be close to 120 mm outside diameter and no wider than 60 mm. Use rubber tread, not slick hard plastic. Verify wheel offset, hub depth, screw length, and body clearance.
- Motor drivers must be one BTS7960/IBT-2-style module per motor. Dual-channel drivers are not pin-compatible with the supplied wiring table.
- The battery must be a 3S pack. A 4S pack can exceed the safe input range of the listed BTS7960 modules and the existing Arduino power assumptions.
- The battery sled is a strapped tray, not a sealed battery box. Verify pack footprint, height, cable exit direction, and XT60 clearance before printing battery-specific add-ons.
- Use one regulated 5 V buck rail for Arduino and BTS7960 logic. Grounds are common.
- The food container must be sealed and no larger than 205 x 145 x 70 mm outside. The printed cargo bay is a carrier, not a food-contact surface.
- The external stop is a firmware drive-lockout input. Keep the main switch or XT60 loop key as the hard power disconnect.
- This is splash-resistant fair-weather outdoor hardware, not a waterproof robot. Do not drive in rain, puddles, mud, sprinklers, or standing water without a ground-up sealed redesign.
