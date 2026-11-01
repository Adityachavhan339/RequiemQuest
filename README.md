# RequiemQuest
RequiemQuest is custom portable handheld video game console

## Core Features
*   **The Brain:** Powered by a **Raspberry Pi Pico H**.
*   **Vibrant Display:** Features a **1.8-inch SPI TFT Color Screen (ST7735 Driver, 128x160 resolution)** operating over high-speed hardware SPI.
*   **Integrated LiPo Power Management:** Upgraded from a standard tethered USB device to a truly portable console utilizing an onboard **TP4056 lithium battery charging IC**. The system automatically powers the device and safely charges an attached 3.7V LiPo cell when micro-USB is plugged in.
*   **Ergonomic Layout & Control:** Built on a classic D-Pad layout (Up, Down, Left, Right) alongside an Action button.
*   **Chiptune Audio Synthesizer:** Includes a passive piezo buzzer driven by hardware PWM frequencies to parse and play polyphonic 8-bit theme music and in-game collision sound effects.



##BOM Table
| Part Description | Qty | Unit Price | Total Price | Vendor | Purpose / Function |
| :--- | :---: | :---: | :---: | :--- | :--- |
| **Raspberry Pi Pico (RP2040 Pre-soldered Headers)** | 1 | \$4.80 | \$4.80 | Sharvi Electronics | The Brain / Main Microcontroller |
| **1.8 Inch SPI 128x160 TFT LCD Display Module** | 1 | \$3.78 | \$3.78 | Robu | Primary Game Display |
| **Tactile Push Button Switch 6x6x5 (Pack of 10)** | 1 | \$0.20 | \$0.20 | Robu | Gamepad Input Array |
| **PCB Mounted Passive Buzzer Module** | 1 | \$0.31 | \$0.31 | Robu | Chiptune Sound Effects |
| **TP4056 Adjustable 1A Li-ion Charging Module** | 1 | \$0.20 | \$0.20 | Robu | Power Management & Battery Charger |
| **WLY501014 3.7V 50mAh 1S LiPo Battery** | 1 | \$1.73 | \$1.73 | Robu | Portable Power Source |
| **Slide Switch SS-12D00 1P2T** | 6 | \$0.02 | \$0.12 | Robu | Main Console Power Switch |
| **2.54mm 2x40 Pin Male Straight Header Strip** | 1 | \$0.13 | \$0.13 | Robu | Interconnect & Expansion Pins |
| **1N5819 Schottky Diode (DO-41)** | 1 | \$0.12 | \$0.12 | Robu | Reverse Polarity & Power Selection Diode |
| **2kΩ Resistor Network Array (0603x4)** | 1 | \$0.01 | \$0.01 | Robu | Circuit Resistor Tuning |
| **TDK 10uF 100V X7R Ceramic Capacitors (1210 SMD)** | 2 | \$0.30 | \$0.60 | Robu | Power Smoothing & Circuit Protection |
| **Custom Fabricated 2-Layer PCB** | 1 | \$9.95 | \$9.95 | Zbotic | Main System Interconnect Board |
| **💰 TOTAL** | | | **\$21.95**


##Few Images
Schematic:
<img width="1545" height="882" alt="Screenshot_20261101_213313" src="https://github.com/user-attachments/assets/d239cc59-44d0-4900-b5b5-ba3caf74a640" />
<img width="1920" height="1030" alt="Screenshot_20261101_213301" src="https://github.com/user-attachments/assets/512d67cb-13ff-4b62-b4a5-70cb5e6e6d8f" />

PCB:
<img width="1321" height="847" alt="Screenshot_20261101_213343" src="https://github.com/user-attachments/assets/91ed1da3-3cb9-430b-ab42-5a3a465d74d7" />
<img width="1920" height="1016" alt="Screenshot_20261101_213331" src="https://github.com/user-attachments/assets/3c024a31-d69e-450b-97cc-e331ce506a31" />


