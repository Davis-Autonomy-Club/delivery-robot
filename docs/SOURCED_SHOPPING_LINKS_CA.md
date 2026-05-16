# Sourced Shopping Links For California

Updated for v2.2 on May 16, 2026. Exact Amazon delivery dates and seller quality change frequently, so re-check before purchase. Pololu links are preferred for drivetrain and sensor parts because the CAD and wiring depend on their dimensions/specs.

## Critical Robot Parts

| Qty | Item | Buy link | Notes |
| ---: | --- | --- | --- |
| 1 | Arduino Mega 2560 Rev3 | [Amazon official Arduino Mega 2560 Rev3 A000067](https://www.amazon.com/Arduino-ATmega2560-Compatible-Advanced-Projects/dp/B0046AMGW0) | Official board or compatible Mega clone |
| 4 | BTS7960 / IBT-2 motor driver modules | [Amazon 4-piece BTS7960 set](https://www.amazon.com/hiBCTR-High-Power-Limiting-Function-Suitable/dp/B0FND3VTGK) | One module per motor |
| 4 | 12 V 37D metal gearmotor, 30:1, encoder, 6 mm D shaft | [Pololu #4752](https://www.pololu.com/product/4752) | V2.2 uses encoder motors instead of no-encoder #4742 motors |
| 4 | 37D metal motor bracket | [Pololu #1995](https://www.pololu.com/product/1995) | Exact bracket for Pololu 37D gearmotors |
| 2 packs | 12 mm hex wheel adapters for 6 mm shaft | [Pololu #2686](https://www.pololu.com/product/2686) | Buy two 2-packs |
| 1 set of 4 | 120 mm wheels, 12 mm hex | [Amazon GoHobby 120 mm 12 mm-hex wheel set](https://www.amazon.com/GoHobby-inches-Course-Traxxas-Blackout/dp/B09KTKGZGF) | Verify hub depth and wheel screw fit before final assembly |
| 2 | 3S LiPo battery, 11.1 V, 5200 mAh, 30C+, XT60 | [Amazon Zeee 3S 5200 mAh XT60 pack](https://www.amazon.com/dp/B0972RKJDS) | Buy two matching packs for repeated route testing; verify pack dimensions and cable exit against the battery sled |
| 1 | RC balance charger with main output and balance lead support | [Amazon B6 80W balance charger with power supply and connectors](https://www.amazon.com/dp/B0F2H3XR6S) | Replaces the cheap XHR-only charger; set correct 3S LiPo mode and charge current |
| 2 | 5 V buck converter, 5 A | [Pololu D24V50F5 5V 5A buck #2851](https://www.pololu.com/product/2851) | One logic/accessory buck, one Pi/camera/LTE buck |
| 1 | Pololu ACS724 0-30 A current sensor | [Pololu #4046](https://www.pololu.com/product/4046) | Total battery current telemetry to Arduino A1 |
| 1 each | 100 kOhm and 33 kOhm 1% resistors | [Amazon metal film resistor assortment](https://www.amazon.com/s?k=100k+33k+1%25+metal+film+resistor) | Battery voltage divider to Arduino A0 |
| 1 | Small perfboard or terminal strip | [Amazon small perfboard search](https://www.amazon.com/s?k=small+perfboard+electronics) | Holds voltage divider |
| 1 | Inline blade fuse holder, 30 A+ | [Amazon inline blade fuse holder search](https://www.amazon.com/s?k=inline+blade+fuse+holder+30A+12V) | Automotive mini/ATO style is fine |
| 2 each | 25 A and 30 A blade fuses | [Amazon 25A 30A automotive blade fuse assortment](https://www.amazon.com/s?k=25A+30A+automotive+blade+fuse+assortment) | Get size matching the fuse holder |
| 1 | Main power switch or XT60 loop key, 30 A+ | [Amazon XT60 loop key switch search](https://www.amazon.com/s?k=XT60+loop+key+switch+30A) | XT60 loop key is safer than a tiny panel switch |
| 1 | External stop button, normally closed | [Amazon 2-pack 22 mm 2NC mushroom emergency stop](https://www.amazon.com/dp/B07R8PTTDX) | Wire one NC contact to Arduino D42/GND for firmware drive lockout; main switch remains hard power disconnect |
| 1 | Lid-closed reed/magnetic switch | [Amazon MC-31B wired magnetic reed switch 2-pack](https://www.amazon.com/dp/B0BX2ZRZ8T) | Wire to Arduino D43/GND so closed lid reads closed |
| 1 | MG90S metal-gear 9 g micro servo | [Amazon MG90S metal gear micro servo search](https://www.amazon.com/s?k=MG90S+metal+gear+micro+servo) | Programmatic lid lock |
| 1 | Raspberry Pi 4 Model B, 4 GB or better | [Amazon Raspberry Pi 4 Model B 4GB search](https://www.amazon.com/s?k=Raspberry+Pi+4+Model+B+4GB) | Companion computer for video/LTE/serial control |
| 1 | microSD card, 32 GB or larger | [Amazon high endurance microSD 32GB search](https://www.amazon.com/s?k=high+endurance+microSD+32GB) | Raspberry Pi OS |
| 1 | USB-C power pigtail or breakout | [Amazon USB-C power pigtail breakout search](https://www.amazon.com/s?k=USB-C+power+pigtail+5V+3A+breakout) | Connects Pi buck output to Raspberry Pi USB-C input |
| 2 | USB/UVC camera modules or compact webcams | [Amazon USB UVC camera module search](https://www.amazon.com/s?k=USB+UVC+camera+module+M12+lens) | One front, one rear; small board cameras fit the printed mounts best |
| 1 | USB 4G/LTE modem | [Amazon Raspberry Pi compatible USB LTE modem search](https://www.amazon.com/s?k=Raspberry+Pi+compatible+USB+4G+LTE+modem) | Needs carrier-compatible bands and activated SIM |
| 1 | LTE SIM/data plan | [Amazon prepaid data SIM search](https://www.amazon.com/s?k=prepaid+data+SIM+4G+LTE) | Match modem/carrier |
| 1 | USB A-to-B cable for Arduino Mega | [Amazon UGREEN USB A-to-B printer cable, 5 ft](https://www.amazon.com/dp/B00P0FO1P0) | Needed for Mega programming/serial unless your board kit includes one |
| 4 | Short USB cables/adapters | [Amazon short USB cable assortment search](https://www.amazon.com/s?k=short+USB+cable+assortment) | Pi to Arduino, cameras, LTE |
| 0 initially | USB hub | Do not buy the desk-style Sabrent wall-adapter hub for the first build | Pi has enough USB ports for Arduino + 2 cameras + LTE; add a rail-powered compact hub only if testing shows brownouts |
| 2 | HC-SR04 ultrasonic sensors, optional | [Amazon HC-SR04 2-pack search](https://www.amazon.com/s?k=HC-SR04+ultrasonic+sensor+2+pack) | Optional; front CAD holes still match HC-SR04 style boards |
| 1 | 5 V LED strip section, optional | [Amazon 5 V red LED strip search](https://www.amazon.com/s?k=5V+red+LED+strip+USB+cuttable) | Optional front status light; cut to 220-230 mm |
| 1 | Food-safe lidded container | [Amazon small food storage container search](https://www.amazon.com/s?k=food+storage+container+205+145+70+mm) | Must be sealed and no larger than 205 x 145 x 70 mm outside |

## Hardware And Consumables

| Qty | Item | Buy link | Notes |
| ---: | --- | --- | --- |
| 1 roll | White/light PETG filament | [Amazon Overture white PETG search](https://www.amazon.com/s?k=Overture+white+PETG+1.75mm) | PETG preferred for chassis/body |
| 1 small length | Clear/natural PETG or PLA | [Amazon clear PETG filament search](https://www.amazon.com/s?k=clear+PETG+filament+1.75mm) | Only needed for diffuser |
| 90+ | M3 x 12 mm machine screws | [Amazon M3 x 12 socket-head screws](https://www.amazon.com/s?k=M3+x+12mm+socket+head+screws) | Base, trays, camera mounts |
| 30+ | M3 x 20-25 mm machine screws | [Amazon M3 x 20 and M3 x 25 screws](https://www.amazon.com/s?k=M3+x+20mm+x+25mm+socket+head+screws) | Body posts |
| 100+ | M3 washers | [Amazon M3 flat washers](https://www.amazon.com/s?k=M3+flat+washers) | Use against printed plastic |
| 90+ | M3 nyloc nuts | [Amazon M3 nylon insert lock nuts](https://www.amazon.com/s?k=M3+nylon+insert+lock+nut) | Prevent vibration loosening |
| 12 | M3 x 8 mm screws | [Amazon M3 x 8 screws](https://www.amazon.com/s?k=M3+x+8mm+socket+head+screws) | Board/standoff screws |
| 14 | M3 nylon standoffs, 6-10 mm | [Amazon M3 nylon standoff kit](https://www.amazon.com/s?k=M3+nylon+standoff+kit+6mm+10mm) | Arduino, Pi, drivers |
| 8 | M2 x 6 mm screws and M2 nuts | [Amazon M2 screw nut assortment](https://www.amazon.com/s?k=M2+screw+nut+assortment) | Small camera modules |
| 20+ | Small zip ties | [Amazon small zip ties](https://www.amazon.com/s?k=small+zip+ties+4+inch) | Wire strain relief, cameras, servo |
| 2 | 20 mm Velcro battery straps | [Amazon 20 mm LiPo battery straps](https://www.amazon.com/s?k=20mm+LiPo+battery+strap) | For battery sled |
| 1 | Thin silicone mat or closed-cell foam sheet | [Amazon thin silicone mat sheet](https://www.amazon.com/s?k=thin+silicone+mat+sheet) | Optional food-container anti-slip pad |
| 1 kit | Cable glands / strain relief fittings | [Amazon waterproof cable gland kit, PG7-PG19](https://www.amazon.com/dp/B09Z24H77M) | For cable exits and enclosure strain relief |
| 1 roll | Foam edge bumper | [Amazon Roving Cove HeftyFit edge protector, off white](https://www.amazon.com/dp/B086Z5B5B5) | Soft bumper around the body perimeter |
| 2 m | 14 AWG red/black silicone wire | [Amazon 14 AWG silicone wire red black](https://www.amazon.com/s?k=14+AWG+silicone+wire+red+black) | Main battery/driver power |
| 3 m | 18 AWG red/black silicone wire | [Amazon 18 AWG silicone wire red black](https://www.amazon.com/s?k=18+AWG+silicone+wire+red+black) | Motor leads |
| 4 m | 22-26 AWG signal wire | [Amazon 22 AWG silicone wire assortment](https://www.amazon.com/s?k=22+AWG+silicone+wire+assortment) | Logic, encoder, servo, telemetry |
| 1 kit | Dupont jumper wire kit | [Amazon Dupont jumper wire kit](https://www.amazon.com/s?k=dupont+jumper+wire+kit+male+female) | Prototype signal wiring |
| 1 kit | XT60 connectors or pigtails | [Amazon XT60 connector pigtail kit](https://www.amazon.com/s?k=XT60+connector+pigtail+kit) | Battery/service disconnect |
| 1 | WAGO 221 or screw terminal distribution block | [Amazon WAGO 221 lever-nut assortment](https://www.amazon.com/Compact-Splicing-Connector-Assortment-221-2401/dp/B0CJ5QF3VX) | Power distribution |
| 1 | Heat-shrink tubing assortment | [Amazon heat shrink tubing assortment](https://www.amazon.com/s?k=heat+shrink+tubing+assortment) | Insulate solder/crimp joints |

## Tools

| Item | Buy link | Notes |
| --- | --- | --- |
| 3D printer, 220 x 220 mm bed or larger | [Amazon Ender 3 style printer search](https://www.amazon.com/s?k=3D+printer+220x220+bed) | Any reliable 220 x 220 mm printer works |
| 2.0 mm and 2.5 mm hex keys | [Amazon metric hex key set](https://www.amazon.com/s?k=metric+hex+key+set+2mm+2.5mm) | For M3 hardware |
| Small Phillips screwdriver | [Amazon precision screwdriver set](https://www.amazon.com/s?k=precision+screwdriver+set) | Electronics screws |
| Needle-nose pliers | [Amazon needle nose pliers](https://www.amazon.com/s?k=needle+nose+pliers) | Assembly and wire handling |
| Wire stripper | [Amazon wire stripper](https://www.amazon.com/s?k=wire+stripper+22+14+awg) | Must cover 22-14 AWG |
| Crimper or soldering iron | [Amazon ferrule crimper kit](https://www.amazon.com/s?k=ferrule+crimper+kit) / [Amazon soldering iron kit](https://www.amazon.com/s?k=soldering+iron+kit) | Crimping is cleaner; soldering works if insulated well |
| Multimeter | [Amazon digital multimeter](https://www.amazon.com/s?k=digital+multimeter) | Required before connecting battery power |
| Flush cutters | [Amazon flush cutters](https://www.amazon.com/s?k=flush+cutters) | Zip ties and print cleanup |
| LiPo-safe charging bag | [Amazon LiPo safe bag](https://www.amazon.com/s?k=LiPo+safe+charging+bag) | Required for safe charging/storage |

## Notes

- For wheels, buy the linked 120 mm / 12 mm-hex set or another set that is explicitly about 120 mm OD and 12 mm hex. Verify hub depth and screw fit physically.
- For the battery, verify exact dimensions, pack height, XT60 cable exit direction, and strap fit before printing any battery-specific add-ons.
- For the food box, verify the exact outside dimensions of the container you will actually use. The cargo rails assume no more than 205 x 145 x 70 mm.
- For the Pi kit, use the bare Pi board on the tray. Do not assume the CanaKit case, switch lead, or extras fit the CAD tray.
- Skip the USB hub at first. If the Pi reports USB brownouts, choose a compact hub powered from the onboard 5 V Pi rail, not a wall-adapter desk hub.
- For cameras, small USB/UVC board cameras are easier to mount than full-size consumer webcams.
- For LTE, check modem carrier bands before buying a SIM. The CAD only provides the tray and cable routing; carrier activation is outside the CAD package.
