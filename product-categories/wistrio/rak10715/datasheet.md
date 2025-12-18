---
slug: /product-categories/wistrio/rak10715/datasheet/
title: RAK10715 WisTrio LTE-M NB-IoT LoRaWAN Development Board Datasheet 
description: Provides comprehensive information about your RAK10715 WisTrio LTE-M NB-IoT LoRaWAN Development Board to help you use it. This information includes technical specifications, characteristics, and requirements.
image: "https://images.docs.rakwireless.com/wistrio/rak10715/rak10715.png"
keywords:
    - RAK10715
    - wistrio
    - nb-iot
    - lte
    - lorawan
    - datasheet
sidebar_label: Datasheet
download: true
---

# RAK10715 WisTrio LTE-M NB-IoT LoRaWAN Development Board Datasheet

## Overview

### Description

The **RAK10715** is a versatile IoT device that combines cellular IoT (LTE-M/NB-IoT) and LoRaWAN technology, making it ideal for a wide range of IoT applications. The device is based on the Nordic nRF52840 SoC, Semtech SX1262 LoRa transceiver, and Quectel BG77 LTE module with built-in GPS, providing a powerful and flexible platform for IoT development.

RAK10715 also supports modular sensor modules based on the WisBlock platform. It provides developers with a range of sensors and interfaces that can be easily integrated with the device. This modular approach to sensor integration allows developers to quickly and easily customize the device to meet the specific needs of their application without having to design and build custom hardware.

Overall, the RAK10715 is a powerful and flexible IoT device that provides a range of connectivity options, security features, and modular sensor module support. It is an ideal device for developers looking to quickly and easily develop and deploy secure and customizable IoT applications.

### Features

- LoRaWAN 1.0.2 protocol stack (supports Class A & C)
- Bluetooth Low Energy 5.0 protocol stack
- NB-IoT and LTE-M
- Nordic nRF52840:
  - Ultra-low-power MCU
  - 32-bit ARM® Cortex-M4F CPU
  - 4 MHz CPU clock
  - 1 MB Flash, 256 KB RAM
  - Wide range of connections:
    - I2C, SPI, Analog inputs,
    - Digital inputs and outputs
- Semtech SX1262:
  - Low power and high range
  - LoRa transceiver
- Quectel BG77 module
  - UART communication with nRF52840
  - Programmable with Quectel AT command set
  - IPEX connectors for external LTE and GPS antennas
  - Nano SIM and ESIM options
  - Supports LTE CAT M1 and LTE CAT NB2
  - GNSS location
- Unify Enclosure 100x75x38 mm
  - IP65 enclosure
  - Prepared for USB access and an external LTE antenna
  - 3 dBi external LTE antenna
  - Matching SMA to IPEX connector
  - Internal LoRaWAN and BLE antenna on the mounting plate
  - Internal GNSS antenna

## Specifications

### Overview

> **Image:** RAK10715 Complete Set

### Hardware

The hardware specification is categorized into six parts. It discusses the interfaces, modules, RF sections, and their corresponding antennas. It also covers the standard parameters in terms of electrical, mechanical, and environmental of the RAK10715.

#### Interfaces

The RAK10715 is enclosed by a custom Unify Enclosure with holes for the following interfaces:

- USB-C for firmware update and debugging (also used for charging)
- M8 circular connector for charging
- SMA connector for cellular antenna

> **Image:** Circular M8 connector

| Pin | Wire Color on Breakout Cable | Usage                            |
| --- | ---------------------------- | -------------------------------- |
| 1   | Black                        | Ground                           |
| 2   | NA                           | NA                               |
| 3   | NA                           | NA                               |
| 4   | NA                           | NA                               |
| 5   | Red                          | Power (typical input 5.5 V) |

#### Modules Inside RAK10715

RAK10715 is composed of several WisBlock modules, which include base, core, and wireless module boards.

> **Image:** WisBlock Modules inside RAK10715

| Module                                                       | Chipset                                               | Description                                                           |
| ------------------------------------------------------------ | ----------------------------------------------------- | --------------------------------------------------------------------- |
| [RAK4631](https://docs.rakwireless.com/product-categories/wisblock/rak4631/datasheet/)   | nRF52840 (Nordic Semiconductor) 
 SX1262 (Semtech) | WisBlock Core based on NRF52840 (MCU + BLE) and SX1262 (LoRa/LoRaWAN) |
| [RAK5860](https://docs.rakwireless.com/product-categories/wisblock/rak5860/datasheet/)   | BG77 (Quectel)                                        | WisBlock Cellular Wireless based on Quected BG77 NB-IoT and LTE-M     |
| [RAK19007](https://docs.rakwireless.com/product-categories/wisblock/rak19007/datasheet/) | NA                                                    | WisBlock Base board with USB connector and Li-ion Charger             |

#### RF and Antenna

##### LoRaWAN

RAK10715 supports the LoRaWAN bands, as shown in the table below:

| Region        | Frequency (MHz) | Core Module |
| ------------- | --------------- | ----------- |
| India         | IN865           | RAK4630(H)  |
| Europe        | EU868           | RAK4630(H)  |
| North America | US915           | RAK4630(H)  |
| Canada        | US915           | RAK4630(H)  |
| Australia     | AU915           | RAK4630(H)  |
| Korea         | KR920           | RAK4630(H)  |
| Asia          | AS923-1/2/3/4   | RAK4630(H)  |

##### Bluetooth (BLE)

The Bluetooth functionality of RAK10715 is a feature built-in to the nRF52840 MCU inside the WisBlock Core RAK4631.

| Parameter          | Detail                                                 |
| ------------------ | ------------------------------------------------------ |
| BLE Protocol       | BLE 5.0                                                |
| BLE Tx Power       | 8 dBm max                                         |
| BLE Rx Sensitivity | 95 dBm @ 1 Mbps BLE mode                     |
| BLE Data Rate      | 2 Mbps, 1 Mbps, 500 Kbps, 125 Kbps |

###### LoRaWAN and BLE Antenna

RAK10715 uses a WisBlock baseplate that has a built-in antenna for LoRa Sub-GHz antenna and 2.4 GHz for Bluetooth BLE.

> **Image:** WisBlock Mounting Plate with Antenna

The designs for 8xx and 9xx MHz are different to optimally achieve the best efficiency and range possible.

> **Image:** 8xx and 9xx MHz Marking

These PCB antennas are connected to WisBlock Core via an IPEX connector.

> **Image:** IPEX Connector of the Antenna 

You can check the complete [8xx MHz Antenna Datasheet](https://downloads.rakwireless.com/LoRa/WisBlock/Accessories/WisBlock%20Base%20Plate%20863-870Mhz%20Antenna%20Datasheet.pdf) and [9xx MHz Antenna Datasheet](https://downloads.rakwireless.com/LoRa/WisBlock/Accessories/WisBlock%20Base%20Plate%20902-928Mhz%20Antenna%20Datasheet.pdf) and get the more details.

##### Cellular

RAK10715 supports LPWAN Cellular technologies like LTE-M and NB-IoT.

###### Frequency Bands

|                          Cat M1                           |                        Cat NB2                        |                GNSS                 |
| :-------------------------------------------------------: | :---------------------------------------------------: | :---------------------------------: |
| B1/B2/B3/B4/B5/B8/B12/B13/B18/B19/B20/B25/B26/B27/B28/B66 | B1/B2/B3/B4/B5/B8/B12/B13/B18/B19/B20/B25/B28/B66/B71 | GPS, GLONASS, BeiDou, Galileo, QZSS |

###### Cellular Specification

| Item               | CAT M1                                       | CAT NB2                                        | CAT NB1                                    |
| ------------------ | -------------------------------------------- | ---------------------------------------------- | ------------------------------------------ |
| Data               | Max. 588 kbps (DL)/ 1119 kbps (UL) | Max. 127 kbps (DL) / 158.5 kbps (UL) | Max. 32 kbps (DL) / 70 kbps (DL) |
| Output Power (Max) | 21 dBm                                  | 21 dBm                                    | 21 dBm                                |
| VoLTE              | Supported                                    | Not Supported                                  | Not Supported                              |

###### Cellular Antenna

The dipole antenna for LTE-M and NB-IoT is externally connected via an SMA connector. You can check the [complete antenna datasheet](https://downloads.rakwireless.com/Accessories/Antenna/SMA-Antenna/SMA-J-Cellular_Antenna_Specification.pdf) to get more details about the antenna.

| Parameter             | Detail              |
| --------------------- | ------------------- |
| Frequency Range (MHz) | 600 - 6000 MHz |
| Peak Gain (dBi)       | -2.0 - 5.5 dBi |
| VSWR                  | < 3.5               |
| Return Loss           | < 5.0               |
| Polarization Mode     | Linear              |
| Radiation Pattern     | Omnidirectional     |
| Connector Type        | SMA                 |

###### GPS Antenna

> **Image:** GPS Antenna

| Item                                                           | Specifications        | PET  |
| -------------------------------------------------------------- | --------------------- | ---- |
| Range of Receiving Frequency                                   | 1575.42 ± 1.1         | ±2.5 |
| Center Frequency (MHz) w/ 30 mm<sup>2</sup> (2 GND plane) | 1575.42               | ±3.0 |
| Bandwidth (MHz) (Return Loss ≤ -10 dB)                    | ≥10                   | ±0.5 |
| VSWR (in center frequency)                                     | ≤1.5                  | ±0.5 |
| Gain (Zenith) (dBi Typ.) w/ 70 mm<sup>2</sup> GND Plane   | 4.5                   | ±0.5 |
| Axial Ratio (dB) w/ 70 mm<sup>2</sup> GND Plane           | 3.0                   | ±0.2 |
| Polarization                                                   | Right-Handed Circular |      |
| Impedance (Ω)                                                  | 50                    |      |
| Frequency Temperature Coefficient (ppm/ºC)                     | 0±10                  |      |

#### Electrical Characteristics

##### Absolute Maximum Ratings

Exposure to maximum rating conditions may affect device reliability therefore the functional operation of the device under the conditions listed below is not advised.

| Ratings                        | Maximum Value (V) |
| ------------------------------ | ----------------- |
| Vbus, power supply on UBS port | -0.3 - 5.5        |
| Vbat, battery voltage          | -0.3 - 4.3        |
| Vconn solar panel voltage      | -0.3 - 5.5        |

:::warning
The modules of RAK10715, like any electronic equipment, is sensitive to electrostatic discharge (ESD). Improper handling can cause permanent damage to the module.
:::

##### Power Requirements

:::tip NOTE
Complete details of the battery and solar changing connections can be found on the [RAK19007 datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak19007/datasheet/#electrical-characteristics).
:::

RAK10715 is powered by a rechargeable Li-ion battery. The nominal operating voltage of the battery should be within the range in the table:

| Min | Type | Max | Unit |
| --- | ---- | --- | ---- |
| 3.3 | 3.7  | 4.3 | V    |

The USB connector can be used as a charging port as well as via the M8 circular connector. The voltage and current fed to the battery through the port should not exceed the ones in the table below.

| Parameter        | Value                   |
| ---------------- | ----------------------- |
| Charging Voltage | 4.5 V ~ 5.5 V |
| Charging Current | 500 mA             |

A suitable Li-ion battery should have the following parameters:

| Parameter         | Value       |
| ----------------- | ----------- |
| Standard Voltage  | 3.7 V  |
| Charging Voltage  | 4.2 V  |
| Capacity          | As required |
| Discharge Current | 2 A    |

:::warning
- Batteries can cause harm if not handled properly.
- Only 3.7-4.2 V rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board, to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5 V solar panels are supported. Do not use 12 V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires match the polarity on the WisBlock Base board. Not all batteries have the same wiring.
:::

#### Environmental Characteristics

The table below lists the operation and storage temperature requirements:

|        Parameter        |     Min     |   Typical   |     Max     |
| :---------------------: | :---------: | :---------: | :---------: |
| Operational Temp. Range | -35° C | +25° C | +75° C |
|  Extended Temp. Range   | -40° C | +25° C | +80° C |
|   Storage Temp. Range   | -40° C | +25° C | +80° C |

#### Mechanical Characteristics

##### Module Dimensions

The complete details of module dimensions and enclosure can be found on their specific datasheet.

- [RAK19007 WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock/rak19007/datasheet/#mechanical-characteristics)
- [RAK5860 WisBlock Wireless](https://docs.rakwireless.com/product-categories/wisblock/rak5860/datasheet/#board-dimensions)
- [Outdoor Unify Enclosure 100x75x38](https://docs.rakwireless.com/product-categories/wisblock/rakbox-uo100x75x38/datasheet/#enclosure-mechanical-dimensions)

