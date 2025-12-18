---
title: RAK7391 WisGate Connect Datasheet
description: Contains instructions and tutorials for installing and deploying your RAK7391. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device.
image: "https://images.docs.rakwireless.com/wisgate/rak7391/rak7391.png"
keywords:
  - RAK7391
  - Datasheet
  - WisGate
sidebar_label: Datasheet
---

# RAK7391 WisGate Connect Datasheet

## Overview

### Description

The RAK7391 WisGate Connect is a Raspberry Pi CM4-based gateway designed to support various radio and WisBlock modules. It features multiple interfaces to accommodate the diverse needs of developers, including HDMI, Ethernet, USB, mPCIe, CSI, DSI, M.2, WisBlock, PoE, and Raspberry Pi HAT. Additionally, it can serve as a basic LoRaWAN gateway, supporting up to four (4) separate modules. This allows for configurations such as a 16-channel sub-GHz LoRaWAN gateway and a 2.4 GHz LoRaWAN gateway operating on the same device.

The RAK7391 provides flexible power supply options, including a DC terminal, a Phoenix terminal, and optional PoE support. It features a fan interface for CPU cooling, with control based on the CPU temperature. The device also monitors its power supply, and its ultracapacitors ensure backup power during a failure. This enables the system to send notifications or handle brief power interruptions seamlessly.

### Features

#### Hardware

- Accepts the complete range of CM4 modules
- Flexible power supply modes such as DC terminal, Phoenix terminal, and POE (Optional)
- HDMI 2.0 connector
- 1 GB Ethernet with PoE support (Optional)
- 2.5 GB Ethernet without PoE support (Optional)
- USB2.0 + 2x USB3.0
- Type-C USB socket for updating the CM4
- Micro SD card socket for CM4 Lite modules
- Standard fan connector, compatible with 5 V and 12 V fans (jumper cap configuration)
- External power connector (+5 V, +12 V with PoE)
- MIPI DSI display FPC connectors (22 pins 0.5 mm pitch cable)
- 2x MIPI CSI-2 camera FPC connectors (22 pins 0.5 mm pitch cable)
- Raspberry Pi HAT connector
- PoE support via an optional module
- Debug UART port
- 2x WisBlock IO connectors
- 3x mPCIe slots
- 1x M.2 B-Key interface
- RTC with battery socket and ability to wake up CM4
- Configuration jumpers (WiFi and BLE enabling/disabling, EEPROM write enable, buzzer enabling)

#### Software

A custom distribution for the WisGate Connect, called RAKPiOS, has been developed. RAKPiOS is a fork of the Raspberry Pi OS, featuring all the necessary drivers for the device, security enhancements, helper scripts, and Docker preinstalled.

You can easily deploy several IoT services from a curated list of docker containers available from the device.

> **Image:** Software structure

### Typical Application

- LoRaWAN gateway (multichannel and multiband)
- Industrial gateway leveraging existing WisBlock modules (ModBUS, 4-20 mA, 0-5 V, and general IO)
- Edge gateway or standalone gateway
- Development platform for new products

## Specifications

### Overview

> **Image:** RAK7391 block diagram

### Hardware

The hardware specification is divided into three (3) parts:  

1. **Power Source and Backhaul Connectivity**: Details the primary specifications for power and network connectivity options.  
2. **Interfacing Options**: Explains the various interfacing capabilities available on the device.  
3. **Pinouts**: Provides the pinout details for the RAK7391 WisGate Connect.

#### Main Specifications

##### Power

| Feature    | Value                               |
|------------|-------------------------------------|
| DC inputs  | 3 (DC jack, Phoenix connector, PoE) |
| DC voltage | 10-28 V                        |
| PoE        | Active IEEE 802.3at or IEEE 802.3bt |

#####  Wireless (Optional)

| Feature                          | Value                |
|----------------------------------|----------------------|
| Wireless 2.4 GHz generation | WiFi 5               |
| Wireless 2.4 GHz standards  | IEEE 802.11 b/g/n/ac |
| Wireless 5.0 GHz generation | WiFi 5               |
| Wireless 5.0 GHz standards  | IEEE 802.11 b/g/n/ac |
| Bluetooth Low Energy             | 5.0                  |

##### Ethernet

| Feature                   | Value           |
|---------------------------|-----------------|
| 1 GB Ethernet Port   | 1 (PoE enabled) |
| 2.5 GB Ethernet Port | 1               |

#####  Peripherals

| Feature                    | Value                                                                              |
|----------------------------|------------------------------------------------------------------------------------|
| mPCIe slots                | 3 (USB, SPI, I2C, UART, and PCIe interfaces)                                       |
| M.2 slots                  | 1 (B-key, USB, and PCIe interfaces)                                                |
| WisBlock IO slots          | 2, more than 20 compatible modules (0-5 V, 4-20 mA, ModBUS, LinBUS, I/O) |
| USB3 ports                 | 2                                                                                  |
| USB2 ports                 | 1                                                                                  |
| HDMI ports                 | 1                                                                                  |
| DSI connectors             | 1                                                                                  |
| CSI connectors             | 2                                                                                  |
| Standard 40-pin RPi header | 1                                                                                  |

##### Other

| Feature                 | Value                                                                               |
|-------------------------|-------------------------------------------------------------------------------------|
| Voltage monitor         | Yes                                                                                 |
| PCB temperature monitor | Yes                                                                                 |
| Real-time clock         | Yes                                                                                 |
| Onboard buzzer          | Yes                                                                                 |
| Operating temperature   | -20º C to 85º C (except for USB3 and Buzzer which are rated 0-70º C) |

##### CM4 Module Connectors

The RAK7391 is based on Raspberry Pi CM4. The following table shows the CPU features:

| Feature               | Description                       |
|-----------------------|-----------------------------------|
| CPU                   | Broadcom BCM2711                  |
| Architecture          | ARMv8 Cortex-A72 64 bits     |
| CPU core count        | 4                                 |
| CPU nominal frequency | 1.5 GHz                      |
| Operating system      | RAK Pi OS                         |
| RAM                   | 1, 2, 4, or 8 GB DDR4        |
| Storage               | 8, 16, or 32 eMMC (Optional) |

##### PSU Input

You can choose between three main power supply solutions:

- 2.1 x 5.5 mm DC input, center positive, 10-28 V<sub>DC</sub>
- Phoenix terminal input, 10-28 V<sub>DC</sub>
- Active IEEE 802.3at or IEEE 802.3bt on 1 GbE connector

:::tip NOTE
You can only use one of the previous power supply ways at the same time.
:::

The exact current required from the +12 V PSU is dependent on the application and what is connected to the RAK7391. It is recommended to budget 25 W for the CM4.

Under normal circumstances, it can provide 5 V<sub>out</sub>. If you want to supply 12 V<sub>out</sub> from the different PSU connectors on the board, you have to use PoE to feed the board with 12 V<sub>DCin</sub>.

:::tip NOTE
The 12 V<sub>DCout</sub> connectors in the board are directly connected to the power supply. Use only 12 V<sub>DC</sub> adapters when powering 12 V devices from the board.
:::

##### Full-Sized HDMI 2.0 Connector

The CM4 handles most of the interfacing for the HDMI interface, with most signals directly connected to the CM4. The current for the HDMI interface is limited to 500 mA.

##### Ethernet

The RAK7391 features two Ethernet ports: one 1 Gb port that supports PoE and one 2.5 Gb port that does not support PoE. To enable the PoE function, the RAK PoE module must be installed.

The CM4 module includes a built-in 1 Gb Ethernet interface. For high-speed network requirements, the 2.5 Gb Ethernet port can be utilized. This 2.5 Gb Ethernet port connects to the PCI bus, which is shared with other components such as USB 3.0, Mini PCIe slot #3, and the M.2 slot. The actual maximum speed depends on CPU usage and the other peripherals connected to the board. Under normal usage and without modifying the CM4 configuration, speeds of 1.8–2.0 Gbps can typically be achieved.

##### PoE HAT

If you want to use the PoE function of RAK7391, you need to have the RAK PoE module. The RAK7391 has an onboard PoE Hat interface. The PoE module supports both 802.3AT and 802.3BT standards to meet the different needs. The PoE input voltage ranges from 42 V to 57 V. AT module max output is 12 V 2.5 A (30 W), and BT max output is 12 V 6 A (72 W).

##### USB 2.0 Hub

The RAK7391 board includes two (2) onboard USB 2.0 hubs, which expand a single USB 2.0 port from the CM4 into seven (7) ports:  

- One port is available on the USB 2.0 connector on the board.  
- Two ports are connected to mPCIe slots #1 and #2.  
- Two ports are connected to the WisBlock slots.  
- The remaining two ports are converted to UART and connected to the WisBlock interfaces.  

There is an internal current limit switch to provide VBUS to the USB connectors. The current limit is set to approximately 500 mA.

##### USB 3.0 Hub

The RAK7391 board features an onboard PCIe to USB 3.0 hub that provides four (4) USB 3.0 interfaces:  

- Two are connected to the USB 3.0 connectors on the board.  
- One is connected to mPCIe slot #3.  
- One is connected to the M.2 interface.  

Note that the PCIe line is shared with the 2.5 Gb Ethernet port, as well as with modules connected to mPCIe slot #3 and the M.2 slot.

There is an internal current limit switch to provide VBUS to the USB connectors. The current limit is set to approximately 1 A.

##### USB Type-C Connector

The Type-C connector is used to flash the eMMC on CM4 non-lite versions via `rpiboot`. When a Type-C cable is connected, the USB 2.0 hub is automatically disabled, and the CM4 functions as a USB device.

You have two options to upload an image to the CM4 module. One way is to add a jumper to the eMMC Flash pair in the configuration header and power the board. The other way is to press the Flash Mode button while powering on the board, after powering on, you can release the button.

##### Micro SD Card Socket

The micro SD Card socket is a **PUSH-PUSH** socket. To release the micro SD Card a gentle push on the micro SD card will enable it to be removed. This socket is only used with CM4 Lite modules that do not have an onboard eMMC.

##### Fan Connector

This connector supports standard fans with PWM drive and tachometer output. The fan is controlled via I2C using an EMC2301 driver. It is compatible with both 5 V and 12 V fans, selectable through an optional jumper cap.

If you only have a 2-wire fan, you can also use it by connecting it to the 5 V-GND connectors.

##### DSI Display Connectors (22 Pin 0.5 mm Pitch Cable)

The DSI 4-channel interface is routed to separate 22-way 0.5 mm pitch connectors, identical to those on the CMIO board but different from the Raspberry Pi 4 Model B. To use a Raspberry Pi 4 Model B display, an adapter board will be required.

##### Dual CSI-2 Display Connectors (22 Pin 0.5 mm Pitch Cable)

Both CSI-2 interfaces (2-channel and 4-channel) are routed to separate 22-way 0.5 mm pitch connectors. These connectors are the same as those on the CMIO board but differ from the Raspberry Pi 4 Model B. To use a Raspberry Pi 4 Model B camera, an adapter board is required.

##### Raspberry Pi HAT Connector

The RAK7391 has a standard Raspberry Pi 40-way HAT connector. Mounting holes are also provided so that a standard HAT can be secured in place.

##### Real-Time Clock

The RAK7391 has a PCF85063AT RTC onboard. A battery socket is provided for a CR2032 battery. On initial setup, the **CLKOUT** of the RTC should be disabled to save power. The alarm output of the RTC is used to wake up the CM4 from a previous halt mode. If an alarm goes off during normal operation the CM4 will be reset, this can be used as a watchdog timer if required.

#### Pin Definitions

##### Jumpers

The J39 header can be optionally used to set some specific configurations:

| Pin   | Name       | Function                                                                                             |
|-------|------------|------------------------------------------------------------------------------------------------------|
| 1-2   | eMMC Flash | If installed, it forces USB booting. This feature is used to flash a new image onto the eMMC memory. |
| 3-4   | EEPROM_nWP | If installed, it enables write protection for the EEPROM on the CM4.                                 |
| 5-6   | WiFi OFF   | If installed, it disables the Wi-Fi functionality.                                                   |
| 7-8   | BT OFF     | If installed, it disables the Bluetooth functionality.                                               |
| 9-10  | Wake up    | Allows wakeup or reset functionality using the onboard RTC.                                          |
| 11-12 | Buzzer ON  | If installed, the buzzer is enabled.                                                                 |

##### CM4 IO Voltage Selection

By default, the RAK7391 board sets the CM4 IO voltage to +3.3 V through R11. To change the IO voltage to +1.8 V, move R11 to the R12 position.

##### I2C

GPIO2 and GPIO3 are used for the I2C interface (i2c1) and are connected to onboard I2C devices as well as external I2C interfaces (WisBlock, Raspberry Pi HAT, mPCIe slots). If an external I2C device conflicts with the address of an onboard I2C device, the external I2C bus can be reassigned by making the following changes:  

1. Move the 0 Ω resistors from R718 and R719 to R716 and R717.  
2. Increase the values of R720 and R721 to 4.7 kΩ.  
3. Remove R722 and R723.  

After these modifications, external I2C devices will be controlled via i2c3 (GPIO4 and GPIO5), while internal devices (RTC, ADC, GPIO Expanders) will remain on i2c1.

To use the ID_SC and ID_SD signals on the Raspberry Pi HAT, remove R711 and R712.

**I2C default addresses**

| Device             | Part      | Default Address |
|--------------------|-----------|-----------------|
| OLED Screen        | SSD1306   | 0x3C            |
| GPIO Expander #1   | TPT29555  | 0x27            |
| GPIO Expander #2   | TPT29555  | 0x26            |
| ADC                | SGM58031  | 0x4B            |
| FAN Controller     | EMC2301   | 0x2F            |
| Temperature Sensor | SHTC3     | 0x70            |
| Real-Time Clock    | PCF85063A | 0x51            |
| Secure IC          | ATECC608A | 0x60            |

:::tip NOTE
The address of certain onboard devices can be changed by adjusting the resistor configuration.
:::

##### ADC

If the I2C address of the ADC chip on the board conflicts with another I2C device, you can resolve the conflict by removing R648 and connecting it to one of R647, R649, or R650 to change the address. The available addresses are (default one in bold):

| Resistor | ADC Address        |
|----------|--------------------|
| R650     | 1001000 (0x48)     |
| R647     | 1001001 (0x49)     |
| R649     | 1001010 (0x4A)     |
| **R648** | **1001011 (0x4B)** |

##### GPIO Expander

You can change the GPIO expander address by modifying the resistor if there is an address conflict. The available addresses are as follows (default one in bold):

| First GPIO Expander (U134)                                     | Address            |
|----------------------------------------------------------------|--------------------|
| R701=NC, R704=4.7k, R702=NC, R705=4.7k, R703=NC, R706=4.7k     | 0100000 (0x20)     |
| R701=4.7, R704=NC, R702=NC, R705=4.7k, R703=NC, R706=4.7k      | 0100001 (0x21)     |
| R701=NC, R704=4.7k, R702=4.7k, R705=NC, R703=NC, R706=4.7k     | 0100010 (0x22)     |
| R701=4.7k, R704=NC, R702=4.7k, R705=NC, R703=NC, R706=4.7k     | 0100011 (0x23)     |
| R701=NC, R704=4.7k, R702=NC, R705=4.7k, R703=4.7k, R706=NC     | 0100100 (0x24)     |
| R701=4.7, R704=NC, R702=NC, R705=4.7k, R703=4.7k, R706=NC      | 0100101 (0x25)     |
| R701=NC, R704=4.7k, R702=4.7k, R705=NC, R703=4.7k, R706=NC     | 0100110 (0x26)     |
| **R701=4.7k, R704=NC, R702=4.7k, R705=NC, R703=4.7k, R706=NC** | **0100111 (0x27)** |
| **Second GPIO expander (U133)**                                | **Address**        |
| R633=NC, R634=4.7k, R635=NC, R636=4.7k, R637=NC, R638=4.7k     | 0100000 (0x20)     |
| R633=4.7, R634=NC, R635=NC, R636=4.7k, R637=NC, R638=4.7k      | 0100001 (0x21)     |
| R633=NC, R634=4.7k, R635=4.7k, R636=NC, R637=NC, R638=4.7k     | 0100010 (0x22)     |
| R633=4.7k, R634=NC, R635=4.7k, R636=NC, R637=NC, R638=4.7k     | 0100011 (0x23)     |
| R633=NC, R634=4.7k, R635=NC, R636=4.7k, R637=4.7k, R638=NC     | 0100100 (0x24)     |
| R633=4.7, R634=NC, R635=NC, R636=4.7k, R637=4.7k, R638=NC      | 0100101 (0x25)     |
| **R633=NC, R634=4.7k, R635=4.7k, R636=NC, R637=4.7k, R638=NC** | **0100110 (0x26)** |
| R701=4.7k, R704=NC, R702=4.7k, R705=NC, R703=4.7k, R706=NC     | 0100111 (0x27)     |

##### mPCIe Interfaces

The RAK7391 has three (3) mPCIe interfaces, which can connect different products, making the product very flexible. It greatly facilitates the creation of multi-radio access networks or the development of user-defined products. The following products support the three mPCIe interfaces:

| Socket   | Primary Use | Secondary Use                                                   | Compatible Modules                                                                                                                                          |
|----------|-------------|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mPCIe #1 | LoRaWAN     | Zigbee                                                          | RAK2247-USB/SPI, RAK2287-USB/SPI, RAK5146-USB/SPI
USB-based  Zigbee module (TBD)                                                                       |
| mPCIe #2 | LoRaWAN     | Zigbee, 4G                                                      | RAK2247-USB/SPI, RAK2287-USB/SPI, RAK5146-USB/SPI, RAK8213-USB
Quectel LTE EC25
USB-based Zigbee module (TBD)                                    |
| mPCIe #3 | 4G          | WiFi6, GbE, IA, SATA (via PCIe)
Adapters to M.2 A+E boards | RAK8213-USB
Hailo-8, Google Coral TPU
IO Crest 4  SATA
I210AT GbE
MiniPCIe to M.2 Key-E adapters
AX210 and AX211 (via an adapter) |

The mPCIe interfaces schematic:

> **Image:** mPCIe Schematic

  * SPI0.0 (`/dev/spidev0.0`) is available on slot #1.
  * SPI0.1 (`/dev/spidev0.1`) is available on slot #2.
  * UART0 (GPIO 14/15) is available on slot #1.
  * GPIO6 is reset signal on slot #2 (SX130X_RESET).
  * GPIO17 is reset signal on slot #1 (SX130X_RESET).
  * GPIO25 is connected to slot#1 pin 23 (RESET_GPS on some LoRaWAN concentrators).
  * GPIO26 is connected to slot#1 pin 19 (PPS on some LoRaWAN concentrators).
  * IO0.0 is connected to !WAKE on slot #3.
  * IO0.1 is connected to COEX1 on slot #3.
  * IO0.2 is connected to COEX2 on slot #3.
  * IO0.3 is connected to !DISABLE on slot #3.
  * IO0.4 is connected to !WAKE on slot #2.
  * IO0.5 is connected to !DISABLE on slot #2.
  * USB2.0 is available on slots #1 and #2.
  * USB3.0 is available on slot #3.
  * 1x PCIe lane is available on slot #3.

:::tip NOTE
MiniPCIe slot #1 has its UART connected to the main UART on the CM4. To use a LoRaWAN Concentrator with GPS support over UART, install it in this slot. Then, disable the login shell and enable the serial port using `raspi-config` to access GPS data on `/dev/ttyAMA0` or `/dev/ttyS0`.
:::

##### M.2 Interface

The RAK7391 features an M.2 B-key interface that provides PCIe and USB 3.0 signals. Currently, it supports the following products for the M.2 interface:

| Socket | Primary Use | Secondary Use | Compatible Modules                                                   |
|--------|-------------|---------------|----------------------------------------------------------------------|
| M.2    | NVMe Drive  | SATA 5G       | Any M.2 B-Key NVMe drive
Quectel RM510Q
JMB585-based  SATA |

##### WisBlock IO Slots

The WisBlock IO interface is a standard, open interface defined by RAK. It is compatible with many sensors and other modules, providing users with many different choices. The RAK7391 is compatible with the majority of WisBlock IO modules, allowing the user to use industrial protocols from the RAK7391 or connect sensors and actuators to it.

#### Mechanical Characteristics

The RAK7391 board uses a standard VIA Mini-ITX form factor. The board is 170 mm x 170 mm with four (4) support holes.

> **Image:** Mechanical drawing

### Certification

### Certifications
- **CE:** https://downloads.rakwireless.com/LoRa/RAK7391/Certification/RAK7391_CE_Certification.pdf
- **FCC:** https://downloads.rakwireless.com/LoRa/RAK7391/Certification/RAK7391_FCC_Certification.pdf
- **ISED:** https://downloads.rakwireless.com/LoRa/RAK7391/Certification/RAK7391_ISED_Certification.pdf

