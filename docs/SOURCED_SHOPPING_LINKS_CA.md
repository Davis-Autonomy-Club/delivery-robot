# Sourced Shopping Links For California

Updated for the minimum first-principles outdoor baseline. The latest active-cart snapshot and line-item prices are in [`CURRENT_AMAZON_CART_SYNC.md`](CURRENT_AMAZON_CART_SYNC.md). Exact Amazon delivery dates, sellers, and availability change frequently, so re-check before purchase.

## Critical Robot Parts

| Qty | Item | Buy link | Notes |
| ---: | --- | --- | --- |
| 1 | Arduino Mega 2560 Rev3 | [Amazon official Arduino Mega 2560 Rev3 A000067](https://www.amazon.com/Arduino-ATmega2560-Compatible-Advanced-Projects/dp/B0046AMGW0) | Official board or compatible Mega clone |
| 4 | BTS7960 / IBT-2 motor driver modules | [Amazon 4-piece BTS7960 set](https://www.amazon.com/hiBCTR-High-Power-Limiting-Function-Suitable/dp/B0FND3VTGK) | One module per motor |
| 4 | 12 V 37D metal gearmotor, 30:1, 6 mm D shaft | [Pololu 37D gearmotor family](https://www.pololu.com/category/116/37d-metal-gearmotors) | Encoders are optional for the baseline and should be left unwired unless testing proves they are needed |
| 4 | 37D metal motor bracket | [Pololu #1995](https://www.pololu.com/product/1995) | Use metal brackets for motor loads |
| 2 packs | 12 mm hex wheel adapters for 6 mm shaft | [Pololu #2686](https://www.pololu.com/product/2686) | Buy two 2-packs |
| 1 set of 4 | 120 mm rubber-tread wheels, 12 mm hex | [Amazon GoHobby 120 mm 12 mm-hex wheel set](https://www.amazon.com/dp/B09KTKGZGF) | Verify rubber tread, hub depth, and wheel screw fit physically |
| 1 | 3S LiPo battery, 11.1 V, 5000-5200 mAh, 30C+, XT60 | [Amazon Zeee 3S 5200 mAh XT60 pack](https://www.amazon.com/dp/B0972RKJDS) | Verify pack dimensions and cable exit against the battery sled |
| 1 | RC balance charger with main output and balance lead support | [Amazon B6 80W balance charger with power supply and connectors](https://www.amazon.com/dp/B0F2H3XR6S) | Set correct 3S LiPo mode and charge current |
| 1 | 5 V buck converter, 5 A | [Pololu D24V50F5 5V 5A buck #2851](https://www.pololu.com/product/2851) | One rail for Arduino and BTS7960 logic |
| 1 each | 100 kOhm and 33 kOhm 1% resistors | [Amazon BOJACK metal film resistor assortment](https://www.amazon.com/dp/B07P3MFG5D) | Battery voltage divider to Arduino A0 |
| 1 | Small perfboard or terminal strip | [Amazon ELEGOO perfboard kit](https://www.amazon.com/dp/B072Z7Y19F) | Holds voltage divider |
| 1 | Inline blade fuse holder, 30 A+ | [Amazon Nilight 14 AWG inline fuse holders](https://www.amazon.com/dp/B07426WCLM) | Required unless an equivalent rated fuse holder is already on hand |
| 2 each | 25 A and 30 A blade fuses | [Amazon automotive blade fuse assortment](https://www.amazon.com/dp/B0899WR671) | Get size matching the fuse holder |
| 1 | Main power switch or XT60 loop key, 30 A+ | [Amazon XT60 loop key switch](https://www.amazon.com/dp/B0B1C88LSM) | XT60 loop key is safer than a tiny panel switch; weather-resistant panel switches are acceptable |
| 1 | Weather-resistant external stop button, normally closed | [Amazon 22 mm waterproof emergency stop search](https://www.amazon.com/s?k=22mm+waterproof+emergency+stop+normally+closed) | Wire one NC contact to Arduino D42/GND |
| 1 | USB A-to-B cable for Arduino Mega | [Amazon UGREEN USB A-to-B printer cable, 5 ft](https://www.amazon.com/dp/B00P0FO1P0) | Needed for Mega programming/serial unless your board kit includes one |
| 1 | Food-safe lidded container | [Amazon small food storage container search](https://www.amazon.com/s?k=food+storage+container+205+145+70+mm) | Must be sealed and no larger than 205 x 145 x 70 mm outside |

Do not buy Pi/LTE/camera/servo/lid-sensor/current-sensor/ultrasonic/LED hardware for the baseline. Keep those as re-add candidates only after a specific failed outdoor test justifies them.

## Hardware And Consumables

| Qty | Item | Buy link | Notes |
| ---: | --- | --- | --- |
| 1 roll | White/light PETG or ASA filament | [Amazon Overture white PETG](https://www.amazon.com/dp/B07PDV9RC8) | Do not use PLA outdoors; ASA is better for UV if your printer can handle it |
| 70+ | Stainless M3 x 12 mm machine screws | [Amazon stainless M3 x 12 socket-head screws search](https://www.amazon.com/s?k=stainless+M3+x+12mm+socket+head+screws) | Base, trays, cargo floor |
| 30+ | Stainless M3 x 20 and M3 x 25 screws | [Amazon stainless M3 x 20 and M3 x 25 screws search](https://www.amazon.com/s?k=stainless+M3+x+20mm+x+25mm+socket+head+screws) | Body posts and panels |
| 80+ | Stainless M3 washers | [Amazon stainless M3 flat washers search](https://www.amazon.com/s?k=stainless+M3+flat+washers) | Use against printed plastic |
| 70+ | Stainless M3 nyloc nuts | [Amazon stainless M3 nylon insert lock nuts search](https://www.amazon.com/s?k=stainless+M3+nyloc+nut) | Prevent vibration loosening |
| 10 | Stainless M3 x 8 screws | [Amazon stainless M3 x 8 screws search](https://www.amazon.com/s?k=stainless+M3+x+8mm+socket+head+screws) | Board/standoff screws |
| 10 | M3 nylon standoffs, 6-10 mm | [Amazon M3 nylon standoff kit](https://www.amazon.com/dp/B0F297R23T) | Arduino and drivers |
| 20+ | Small zip ties | [Amazon small zip ties](https://www.amazon.com/dp/B0DS6B9W4X) | Wire strain relief and board retention |
| 2 | 20 mm Velcro battery straps | [Amazon LiPo battery straps](https://www.amazon.com/dp/B019QWZYU8) | For battery sled |
| 1 | Thin silicone mat or closed-cell foam sheet | [Amazon silicone mat set](https://www.amazon.com/dp/B0CFTP6JR4) | Food-container anti-slip pad |
| 1 roll | Outdoor foam edge bumper | [Amazon Roving Cove HeftyFit edge protector, off white](https://www.amazon.com/dp/B086Z5B5B5) | Soft bumper around body perimeter |
| 1 sheet | Thin polycarbonate, HDPE, or corrugated plastic | [Amazon thin polycarbonate sheet search](https://www.amazon.com/s?k=thin+polycarbonate+sheet) | Cut a removable underbody splash sheet by hand |
| 1 roll | Closed-cell foam gasket tape | [Amazon closed cell foam gasket tape search](https://www.amazon.com/s?k=closed+cell+foam+gasket+tape) | Lid and upper body seam splash resistance |
| 1 kit | Rubber grommets or cable glands | [Amazon waterproof cable gland kit, PG7-PG19](https://www.amazon.com/dp/B09Z24H77M) | Protect panel/splash-sheet wire exits |
| 1 tube | Neutral-cure silicone sealant | [Amazon neutral cure silicone sealant search](https://www.amazon.com/s?k=neutral+cure+silicone+sealant+electronics) | Seal non-service seams and penetrations |
| 1 bottle | Electronics conformal coating | [Amazon MG Chemicals 422B conformal coating search](https://www.amazon.com/s?k=MG+Chemicals+422B+conformal+coating) | Optional divider-board protection; keep connectors uncoated |
| 1 small tube | Dielectric grease | [Amazon dielectric grease search](https://www.amazon.com/s?k=dielectric+grease) | Connector shell weather resistance |
| 2 m | 14 AWG red/black silicone wire | [Amazon 14 AWG silicone wire red/black](https://www.amazon.com/dp/B0746H96QK) | Main battery/driver power |
| 3 m | 18 AWG red/black silicone wire | [Amazon 18 AWG silicone wire red/black](https://www.amazon.com/dp/B07FMRDP87) | Motor leads |
| 2 m | 22-26 AWG signal wire | [Amazon 22 AWG silicone wire assortment](https://www.amazon.com/dp/B0DWJSB65V) | Logic, external stop, voltage divider |
| 1 kit | Dupont jumper wire kit | [Amazon Dupont jumper wire kit](https://www.amazon.com/dp/B01EV70C78) | Prototype signal wiring |
| 1 kit | XT60 connectors or pigtails | [Amazon XT60 pigtail kit](https://www.amazon.com/dp/B09M6KQWBL) | Battery/service disconnect |
| 1 | WAGO 221 or screw terminal distribution block | [Amazon WAGO 221 lever-nut assortment](https://www.amazon.com/dp/B0CJ5QF3VX) | Power distribution |
| 1 | Heat-shrink tubing assortment | [Amazon heat shrink tubing assortment](https://www.amazon.com/dp/B01MFA3OFA) | Insulate solder/crimp joints |

## Tools

| Item | Buy link | Notes |
| --- | --- | --- |
| 3D printer, 220 x 220 mm bed or larger | [Amazon Ender 3 style printer search](https://www.amazon.com/s?k=3D+printer+220x220+bed) | Any reliable 220 x 220 mm printer works; omit if printing is outsourced |
| 2.0 mm and 2.5 mm hex keys | [Amazon metric hex key set](https://www.amazon.com/dp/B0CJBRYQF3) | For M3 hardware |
| Small Phillips screwdriver | [Amazon precision screwdriver set](https://www.amazon.com/dp/B0D633J3C7) | Electronics screws |
| Needle-nose pliers | [Amazon needle nose pliers](https://www.amazon.com/dp/B0B5CQ6KNS) | Assembly and wire handling |
| Wire stripper | [Amazon wire stripper](https://www.amazon.com/dp/B0FH3BFDS7) | Must cover 22-14 AWG |
| Crimper or soldering iron | [Amazon ferrule crimper kit](https://www.amazon.com/dp/B0DRJ9CDNG) / [Amazon soldering iron kit](https://www.amazon.com/dp/B087767KNW) | Crimping is cleaner; soldering works if insulated well |
| Multimeter | [Amazon digital multimeter](https://www.amazon.com/dp/B01ISAMUA6) | Required before connecting battery power |
| Flush cutters | [Amazon flush cutters](https://www.amazon.com/dp/B0F9TG2G4S) | Zip ties and print cleanup |
| Utility knife or shears | [Amazon utility knife search](https://www.amazon.com/s?k=utility+knife) | Cutting gasket tape and splash sheet |
| LiPo-safe charging bag | [Amazon LiPo safe bag](https://www.amazon.com/dp/B07KZQZBN2) | Required for safe charging/storage |

## Notes

- Do not buy Pi/LTE/camera/servo/sensor hardware until a failed test justifies it.
- Do buy outdoor ruggedization basics now: stainless hardware, gasket tape, grommets/cable glands, bumper, and one simple splash sheet.
- For wheels, buy a 120 mm / 12 mm-hex set with rubber tread or another set that is explicitly about 120 mm OD and 12 mm hex.
- For the battery, verify exact dimensions, pack height, XT60 cable exit direction, and strap fit before printing battery-specific add-ons.
- For the food box, verify the exact outside dimensions of the container you will actually use.
