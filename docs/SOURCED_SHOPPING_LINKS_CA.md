# Sourced Shopping Links For California

Updated for v2.2 on May 16, 2026. The latest active-cart snapshot and line-item prices are in [`CURRENT_AMAZON_CART_SYNC.md`](CURRENT_AMAZON_CART_SYNC.md). Exact Amazon delivery dates and seller quality change frequently, so re-check before purchase. Pololu links are preferred for drivetrain and sensor parts because the CAD and wiring depend on their dimensions/specs.

## Critical Robot Parts

| Qty | Item | Buy link | Notes |
| ---: | --- | --- | --- |
| 1 | Arduino Mega 2560 Rev3 | [Amazon official Arduino Mega 2560 Rev3 A000067](https://www.amazon.com/Arduino-ATmega2560-Compatible-Advanced-Projects/dp/B0046AMGW0) | Official board or compatible Mega clone |
| 4 | BTS7960 / IBT-2 motor driver modules | [Amazon 4-piece BTS7960 set](https://www.amazon.com/hiBCTR-High-Power-Limiting-Function-Suitable/dp/B0FND3VTGK) | One module per motor |
| 4 | 12 V 37D metal gearmotor, 30:1, encoder, 6 mm D shaft | [Pololu #4752](https://www.pololu.com/product/4752) | V2.2 uses encoder motors instead of no-encoder #4742 motors |
| 4 | 37D metal motor bracket | [Pololu #1995](https://www.pololu.com/product/1995) | Exact bracket for Pololu 37D gearmotors |
| 2 packs | 12 mm hex wheel adapters for 6 mm shaft | [Pololu #2686](https://www.pololu.com/product/2686) | Buy two 2-packs |
| 1 set of 4 | 120 mm wheels, 12 mm hex | [Amazon GoHobby 120 mm 12 mm-hex wheel set](https://www.amazon.com/dp/B09KTKGZGF) | Saved for later, not active in the current Amazon cart. Required unless compatible wheels are already on hand. Verify hub depth and wheel screw fit before final assembly |
| 2 | 3S LiPo battery, 11.1 V, 5200 mAh, 30C+, XT60 | [Amazon Zeee 3S 5200 mAh XT60 pack](https://www.amazon.com/dp/B0972RKJDS) | Buy two matching packs for repeated route testing; verify pack dimensions and cable exit against the battery sled |
| 1 | RC balance charger with main output and balance lead support | [Amazon B6 80W balance charger with power supply and connectors](https://www.amazon.com/dp/B0F2H3XR6S) | Replaces the cheap XHR-only charger; set correct 3S LiPo mode and charge current |
| 2 | 5 V buck converter, 5 A | [Pololu D24V50F5 5V 5A buck #2851](https://www.pololu.com/product/2851) | One logic/accessory buck, one Pi/camera/LTE buck |
| 1 | Pololu ACS724 0-30 A current sensor | [Pololu #4046](https://www.pololu.com/product/4046) | Total battery current telemetry to Arduino A1 |
| 1 each | 100 kOhm and 33 kOhm 1% resistors | [Amazon BOJACK metal film resistor assortment](https://www.amazon.com/dp/B07P3MFG5D) | Active in the current Amazon cart; battery voltage divider to Arduino A0 |
| 1 | Small perfboard or terminal strip | [Amazon ELEGOO perfboard kit](https://www.amazon.com/dp/B072Z7Y19F) | Active in the current Amazon cart; holds voltage divider |
| 1 | Inline blade fuse holder, 30 A+ | [Amazon Nilight 14 AWG inline fuse holders](https://www.amazon.com/dp/B07426WCLM) | Saved for later, not active in the current Amazon cart. Required unless an equivalent rated fuse holder is already on hand |
| 2 each | 25 A and 30 A blade fuses | [Amazon automotive blade fuse assortment](https://www.amazon.com/dp/B0899WR671) | Saved for later, not active in the current Amazon cart. Required unless matching fuses are already on hand |
| 1 | Main power switch or XT60 loop key, 30 A+ | [Amazon XT60 loop key switch](https://www.amazon.com/dp/B0B1C88LSM) | Active in the current Amazon cart; XT60 loop key is safer than a tiny panel switch |
| 1 | External stop button, normally closed | [Amazon 2-pack 22 mm 2NC mushroom emergency stop](https://www.amazon.com/dp/B07R8PTTDX) | Wire one NC contact to Arduino D42/GND for firmware drive lockout; main switch remains hard power disconnect |
| 1 | Lid-closed reed/magnetic switch | [Amazon MC-31B wired magnetic reed switch 2-pack](https://www.amazon.com/dp/B0BX2ZRZ8T) | Wire to Arduino D43/GND so closed lid reads closed |
| 1 | MG90S metal-gear 9 g micro servo | [Amazon MG90S metal gear micro servo 2-pack](https://www.amazon.com/dp/B0BWJ4RKGV) | Active in the current Amazon cart; programmatic lid lock |
| 1 | Raspberry Pi 4 Model B, 4 GB or better | [Amazon Raspberry Pi 4 Model B 4GB search](https://www.amazon.com/s?k=Raspberry+Pi+4+Model+B+4GB) | Not active in the current Amazon cart. Required for video/LTE/serial control unless a Pi is already on hand |
| 1 | microSD card, 32 GB or larger | [Amazon SanDisk high-endurance 32 GB microSD](https://www.amazon.com/dp/B084CJLNM4) | Not active in the current Amazon cart. Required for Raspberry Pi OS unless a card is already on hand |
| 1 | USB-C power pigtail or breakout | [Amazon USB-C power pigtail 5-pack](https://www.amazon.com/dp/B0BFHXWCS9) | Active in the current Amazon cart; connects Pi buck output to Raspberry Pi USB-C input |
| 2 | USB/UVC camera modules or compact webcams | [Amazon Arducam 1080p USB camera module](https://www.amazon.com/dp/B0CGLW3Z1N) | Active in the current Amazon cart with quantity 2; one front, one rear |
| 1 | USB 4G/LTE modem | [Amazon Waveshare SIM7600G-H LTE USB dongle](https://www.amazon.com/dp/B08CSB596W) | Active in the current Amazon cart; needs carrier-compatible bands and activated SIM |
| 1 | LTE SIM/data plan | [Amazon EIOTCLUB data SIM](https://www.amazon.com/dp/B0DJ2SQZTQ) | Active in the current Amazon cart; match modem/carrier |
| 1 | USB A-to-B cable for Arduino Mega | [Amazon UGREEN USB A-to-B printer cable, 5 ft](https://www.amazon.com/dp/B00P0FO1P0) | Needed for Mega programming/serial unless your board kit includes one |
| 4 | Short USB cables/adapters | [Amazon short USB cable assortment](https://www.amazon.com/dp/B0BZYKPCR5) | Active in the current Amazon cart; Pi to Arduino, cameras, LTE |
| 0 initially | USB hub | Do not buy the desk-style Sabrent wall-adapter hub for the first build | Pi has enough USB ports for Arduino + 2 cameras + LTE; add a rail-powered compact hub only if testing shows brownouts |
| 2 | HC-SR04 ultrasonic sensors, optional | [Amazon HC-SR04 2-pack](https://www.amazon.com/dp/B0B1MJJLJP) | Active in the current Amazon cart; optional, front CAD holes still match HC-SR04 style boards |
| 1 | 5 V LED strip section, optional | [Amazon 5 V red LED strip](https://www.amazon.com/dp/B0CMCN9Z2K) | Active in the current Amazon cart; optional front status light, cut to 220-230 mm |
| 1 | Food-safe lidded container | [Amazon small food storage container search](https://www.amazon.com/s?k=food+storage+container+205+145+70+mm) | Must be sealed and no larger than 205 x 145 x 70 mm outside |

## Hardware And Consumables

| Qty | Item | Buy link | Notes |
| ---: | --- | --- | --- |
| 1 roll | White/light PETG filament | [Amazon Overture white PETG](https://www.amazon.com/dp/B07PDV9RC8) | Removed from the current Amazon cart. Required unless filament is already available |
| 1 small length | Clear/natural PETG or PLA | [Amazon clear PETG filament](https://www.amazon.com/dp/B0C8NT6M1M) | Not active in the current Amazon cart. Only needed for diffuser |
| 90+ | M3 x 12 mm machine screws | [Amazon M3 x 12 socket-head screws](https://www.amazon.com/dp/B07CNFTK99) | Active in the current Amazon cart; base, trays, camera mounts |
| 30+ | M3 x 20-25 mm machine screws | [Amazon M3 x 20-40 mm screw assortment](https://www.amazon.com/dp/B0CR35WB16) | Active in the current Amazon cart; body posts |
| 100+ | M3 washers | [Amazon M3 flat washers](https://www.amazon.com/dp/B0DDTNVRZW) | Active in the current Amazon cart; use against printed plastic |
| 90+ | M3 nyloc nuts | [Amazon M3 nylon insert lock nuts](https://www.amazon.com/dp/B0DZ2V6PRF) | Active in the current Amazon cart; prevent vibration loosening |
| 12 | M3 x 8 mm screws | [Amazon M3 x 8 screws](https://www.amazon.com/dp/B07CMQ1SQH) | Active in the current Amazon cart; board/standoff screws |
| 14 | M3 nylon standoffs, 6-10 mm | [Amazon M3 nylon standoff kit](https://www.amazon.com/dp/B0F297R23T) | Active in the current Amazon cart; Arduino, Pi, drivers |
| 8 | M2 x 6 mm screws and M2 nuts | [Amazon M2 screw nut assortment](https://www.amazon.com/dp/B0FGV5K8BT) | Active in the current Amazon cart; small camera modules |
| 20+ | Small zip ties | [Amazon small zip ties](https://www.amazon.com/dp/B0DS6B9W4X) | Active in the current Amazon cart; wire strain relief, cameras, servo |
| 2 | 20 mm Velcro battery straps | [Amazon LiPo battery straps](https://www.amazon.com/dp/B019QWZYU8) | Not active in the current Amazon cart. Required unless equivalent straps are already on hand |
| 1 | Thin silicone mat or closed-cell foam sheet | [Amazon silicone mat set](https://www.amazon.com/dp/B0CFTP6JR4) | Active in the current Amazon cart; optional food-container anti-slip pad |
| 1 kit | Cable glands / strain relief fittings | [Amazon waterproof cable gland kit, PG7-PG19](https://www.amazon.com/dp/B09Z24H77M) | For cable exits and enclosure strain relief |
| 1 roll | Foam edge bumper | [Amazon Roving Cove HeftyFit edge protector, off white](https://www.amazon.com/dp/B086Z5B5B5) | Soft bumper around the body perimeter |
| 2 m | 14 AWG red/black silicone wire | [Amazon 14 AWG silicone wire red/black](https://www.amazon.com/dp/B0746H96QK) | Active in the current Amazon cart; main battery/driver power |
| 3 m | 18 AWG red/black silicone wire | [Amazon 18 AWG silicone wire red/black](https://www.amazon.com/dp/B07FMRDP87) | Active in the current Amazon cart; motor leads |
| 4 m | 22-26 AWG signal wire | [Amazon 22 AWG silicone wire assortment](https://www.amazon.com/dp/B0DWJSB65V) | Active in the current Amazon cart; logic, encoder, servo, telemetry |
| 1 kit | Dupont jumper wire kit | [Amazon Dupont jumper wire kit](https://www.amazon.com/dp/B01EV70C78) | Active in the current Amazon cart; prototype signal wiring |
| 1 kit | XT60 connectors or pigtails | [Amazon XT60 pigtail kit](https://www.amazon.com/dp/B09M6KQWBL) | Active in the current Amazon cart; battery/service disconnect |
| 1 | WAGO 221 or screw terminal distribution block | [Amazon WAGO 221 lever-nut assortment](https://www.amazon.com/dp/B0CJ5QF3VX) | Saved for later, not active in the current Amazon cart. Required unless an equivalent rated distribution block is already on hand |
| 1 | Heat-shrink tubing assortment | [Amazon heat shrink tubing assortment](https://www.amazon.com/dp/B01MFA3OFA) | Active in the current Amazon cart; insulate solder/crimp joints |

## Tools

| Item | Buy link | Notes |
| --- | --- | --- |
| 3D printer, 220 x 220 mm bed or larger | [Amazon Ender 3 style printer](https://www.amazon.com/dp/B0F8J78BN1) | Not active in the current Amazon cart; fine to omit if printing is outsourced or a printer is already available |
| 2.0 mm and 2.5 mm hex keys | [Amazon metric hex key set](https://www.amazon.com/dp/B0CJBRYQF3) | Not active in the current Amazon cart; required for M3 hardware unless already on hand |
| Small Phillips screwdriver | [Amazon precision screwdriver set](https://www.amazon.com/dp/B0D633J3C7) | Active in the current Amazon cart; electronics screws |
| Needle-nose pliers | [Amazon needle nose pliers](https://www.amazon.com/dp/B0B5CQ6KNS) | Not active in the current Amazon cart; required for assembly and wire handling unless already on hand |
| Wire stripper | [Amazon wire stripper](https://www.amazon.com/dp/B0FH3BFDS7) | Not active in the current Amazon cart; required unless already on hand |
| Crimper or soldering iron | [Amazon ferrule crimper kit](https://www.amazon.com/dp/B0DRJ9CDNG) / [Amazon soldering iron kit](https://www.amazon.com/dp/B087767KNW) | Not active in the current Amazon cart; crimping is cleaner, soldering works if insulated well |
| Multimeter | [Amazon digital multimeter](https://www.amazon.com/dp/B01ISAMUA6) | Not active in the current Amazon cart; required before connecting battery power unless already on hand |
| Flush cutters | [Amazon flush cutters](https://www.amazon.com/dp/B0F9TG2G4S) | Not active in the current Amazon cart; useful for zip ties and print cleanup |
| LiPo-safe charging bag | [Amazon LiPo safe bag](https://www.amazon.com/dp/B07KZQZBN2) | Not active in the current Amazon cart; use the existing Zeee bag or add one before charging/storage |

## Notes

- For wheels, buy the linked 120 mm / 12 mm-hex set or another set that is explicitly about 120 mm OD and 12 mm hex. Verify hub depth and screw fit physically.
- For the battery, verify exact dimensions, pack height, XT60 cable exit direction, and strap fit before printing any battery-specific add-ons.
- For the food box, verify the exact outside dimensions of the container you will actually use. The cargo rails assume no more than 205 x 145 x 70 mm.
- For the Pi kit, use the bare Pi board on the tray. Do not assume the CanaKit case, switch lead, or extras fit the CAD tray.
- Skip the USB hub at first. If the Pi reports USB brownouts, choose a compact hub powered from the onboard 5 V Pi rail, not a wall-adapter desk hub.
- For cameras, small USB/UVC board cameras are easier to mount than full-size consumer webcams.
- For LTE, check modem carrier bands before buying a SIM. The CAD only provides the tray and cable routing; carrier activation is outside the CAD package.
