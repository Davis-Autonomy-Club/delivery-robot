# Shopping List

This is the compatible v2.2 bill of materials for `cad/print-ready/`. It keeps the Arduino Mega + 4 x BTS7960 motor-driver architecture, but upgrades the prototype with encoder motors, a programmatic lid lock, front/rear cameras, a Raspberry Pi companion computer, USB LTE, battery telemetry, lid-closed sensing, and an external stop input.

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
| 4 | BTS7960 / IBT-2 motor driver modules | One 43 A BTS7960 module per motor; typical board 50 x 50 x 43 mm | [HandsOn BTS7960 guide](https://www.handsontec.com/dataspecs/module/BTS7960%20Motor%20Driver.pdf) |
| 4 | 12 V 37D metal gearmotor, 30:1, encoder | 37 mm diameter, 6 mm D shaft, about 330 RPM, 64 CPR encoder; Pololu #4752 is the reference motor | [Pololu #4752 encoder motor](https://www.pololu.com/product-info-merged/4752) |
| 4 | 37D motor brackets | Metal brackets for 37D gearmotors; use metal, not printed load-bearing brackets | [Pololu 37D machined bracket #1995](https://www.pololu.com/product/1995) |
| 2 packs | 12 mm hex wheel adapters for 6 mm shaft | 2 adapters per pack, 4 total; standard or extended length is OK | [Pololu #2686 12 mm hex adapter](https://www.pololu.com/product/2686) |
| 4 | 120 mm wheels | Prefer the exact sourced 120 mm x about 60 mm wheel set with 12 mm hex; verify hub depth and screw fit before final assembly | [Pololu adapter page showing 120 x 60 Wild Thumper compatibility](https://www.pololu.com/product/2686) |
| 2 | Matching 3S LiPo batteries | 11.1 V nominal, 5000-5200 mAh target, 30C or better, XT60 plug preferred; verify each pack's exact dimensions before printing around it | Reputable RC packs |
| 1 | Real RC balance charger for 3S LiPo | Must use main pack output plus balance lead, support adjustable charge current, and show charge state clearly; do not charge through the robot wiring | B6AC/IMAX-style RC charger or better |
| 2 | 5 V buck converters, 5 A each | One logic/accessory rail and one Pi/camera/LTE rail | [Pololu D24V50F5 5V 5A buck #2851](https://www.pololu.com/product/2851) |
| 1 | Inline blade fuse holder | Rated 30 A or higher, installed close to battery positive | Automotive mini/ATO blade holder |
| 2 each | Blade fuses | 25 A and 30 A; start with 25 A, use 30 A only if nuisance trips occur | Automotive mini/ATO fuses |
| 1 | Main power switch or XT60 loop key | DC rated 30 A or higher | Put after the fuse |
| 1 | Pololu ACS724 0-30 A current sensor | Measures total switched battery current before positive distribution; Arduino A1 reads `VIOUT` | [Pololu #4046 ACS724 0-30 A](https://www.pololu.com/product/4046) |
| 1 each | 100 kOhm and 33 kOhm 1% resistors | Battery voltage divider for Arduino A0; 100 kOhm from switched battery positive to A0, 33 kOhm from A0 to ground | Metal film resistors |
| 1 | Small perfboard or terminal strip | Holds voltage divider resistors and strain relief | Any small solderable board |
| 1 | External stop button | Latching mushroom-style switch with normally-closed contacts; wired to Arduino D42 as a drive lockout input | 22 mm NC emergency stop switch |
| 1 | Lid-closed sensor | Reed switch or microswitch; closed lid pulls Arduino D43 to ground | Wired reed switch or lever microswitch |
| 1 | Metal-gear 9 g micro servo | MG90S-size servo for the printed lid lock; 5 V accessory rail power | Common MG90S metal-gear servo |
| 1 | Raspberry Pi 4 Model B, 4 GB or better | Companion computer for cameras, LTE, and future teleop; CAD tray fits Pi 4/Pi 5 footprint class | [Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) |
| 1 | microSD card, 32 GB or larger | Raspberry Pi OS | High-endurance card preferred |
| 1 | USB-C power pigtail or breakout | Connects the dedicated 5 V Pi buck output to the Raspberry Pi USB-C power input | Rated 5 V, 3 A minimum |
| 2 | USB/UVC camera modules or compact webcams | One front, one rear; prefer small board cameras with M2 holes or zip-tie-friendly bodies | Generic USB UVC cameras |
| 1 | USB 4G/LTE modem | Linux/Raspberry Pi compatible, unlocked if possible | USB LTE modem plus activated SIM/data plan |
| 1 | Activated LTE SIM/data plan | Must match the modem bands/carrier | Carrier of choice |
| 1 | USB A-to-B cable | Raspberry Pi or laptop to Arduino Mega USB-B programming/serial port; required unless your Mega kit definitely includes one | Short printer-style USB 2.0 cable |
| 4 | Short USB cables/adapters | Pi to Arduino, two cameras, LTE modem; use short cables for strain relief | Match the device connectors |
| 0 initially | USB hub | Skip the desk-style wall-adapter hub for the first build. The Pi has four USB ports for Arduino, two cameras, and LTE. If brownouts occur later, add a compact hub that can be fed cleanly from the onboard 5 V Pi rail | Optional later |
| 2 | HC-SR04 ultrasonic sensors, optional | Front CAD panels still have matching openings | [HC-SR04 dimensions/reference](https://www.digikey.com/en/htmldatasheets/production/3822706/0/0/1/hc-sr04) |
| 1 | 5 V LED strip section, optional | Front status light, 220-230 mm long | Use the printed clear diffuser |
| 1 | Food-safe lidded container | Must fit inside 205 x 145 x 70 mm outer dimensions; food goes here, under the robot lid, above the electronics shelf | Small sealed meal-prep/takeout container |

## Hardware And Consumables

| Qty | Item | Use |
| ---: | --- | --- |
| 1 roll | PETG filament, white or light color | Chassis, trays, body; PLA is OK for indoor demos but PETG is safer outdoors/in heat |
| 1 small length | Clear/natural PETG or PLA | Front LED diffuser |
| 90+ | M3 x 12 mm machine screws | Base seams, trays, cargo floor, cargo rails, panel joiners, camera mounts |
| 30+ | M3 x 20-25 mm machine screws | Body panels through corner posts |
| 100+ | M3 washers | Use under screw heads and nuts against printed plastic |
| 90+ | M3 nyloc nuts | All body/chassis fastening |
| 12 | M3 x 8 mm screws | Arduino/BTS/Pi board standoffs if your standoffs need short screws |
| 14 | M3 nylon standoffs, 6-10 mm tall | Arduino Mega, Pi, and motor drivers |
| 8 | M2 x 6 mm screws and M2 nuts | Small camera boards and optional servo-cam retention |
| 20+ | Small zip ties | Board retention, camera retention, servo retention, and wire strain relief |
| 2 | Velcro battery straps, 20 mm wide | Battery sled |
| 1 | Thin silicone mat or closed-cell foam sheet | Optional non-slip pad under the sealed food container |
| 1 kit | Cable glands / strain-relief fittings | Outdoor-ish cable exits and enclosure strain relief; choose sizes that grip the actual cables |
| 1 roll | Foam edge bumper | Soft bumper around the body perimeter for low-speed contact protection |
| 2 m | 14 AWG red/black silicone wire | Battery, fuse, switch, current sensor, distribution to driver power terminals |
| 3 m | 18 AWG red/black silicone wire | Motor leads from BTS7960 to motors |
| 4 m | 22-26 AWG signal wire | Mega-to-BTS7960, encoders, servo, voltage divider, ACS724 signal |
| 1 kit | Dupont jumpers | Short logic wiring during test; replace loose jumpers with crimped leads for field use |
| 1 kit | XT60 connectors or XT60 pigtails | Battery connection and service disconnect |
| 1 | WAGO 221 or screw terminal distribution block | Battery positive/negative distribution |
| 1 | Heat-shrink tubing assortment | Insulate soldered/crimped connections |

## Tools

3D printer with at least a 220 x 220 mm bed, 2.0 mm and 2.5 mm hex keys, small Phillips screwdriver, needle-nose pliers, wire stripper, crimper or soldering iron, multimeter, flush cutters, and a LiPo-safe charging bag.

## Substitution Rules

The CAD is forgiving, but do not change these without editing the CAD first:

- Motors must be 37 mm diameter encoder gearmotors with 6 mm output shafts. The base slots tolerate motor length differences, but the wheel adapters and wheel caps assume 6 mm shaft + 12 mm hex.
- Wheels should be close to 120 mm outside diameter and no wider than 60 mm. Do not trust "any 1/10 wheel" blindly; verify wheel offset, hub depth, screw length, and body clearance.
- Motor drivers must be one BTS7960/IBT-2-style module per motor. Dual-channel drivers are not pin-compatible with the supplied wiring table.
- The battery must be a 3S pack. A 4S pack can exceed the safe input range of the listed BTS7960 modules and the existing Arduino power assumptions.
- The battery sled is a strapped tray, not a sealed battery box. Verify the exact pack footprint, height, cable exit direction, and XT60 clearance before committing to a pack or printing any battery-specific add-ons.
- Use two 5 V buck rails: one for Arduino/BTS logic/servo, one for Pi/cameras/LTE. Grounds are common; 5 V positives stay separate.
- The food container must be sealed and no larger than 205 x 145 x 70 mm outside. The printed cargo bay is a carrier, not a food-contact surface.
- Verify the actual outside dimensions of the Rubbermaid/meal container you intend to use before relying on the cargo retainer rails.
- The Raspberry Pi tray fits the Pi board footprint. Do not assume the CanaKit case, switch cable, or bundled extras fit on the printed tray.
- The external stop and lid-closed switch are firmware drive-lockout inputs. Keep the main switch or XT60 loop key as the hard power disconnect.
