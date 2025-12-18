---
title: RAK7394 WisGate Developer CM4 Datasheet
description: Provides comprehensive information about your RAK7394 WisGate Developer CM4 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisgate/rak7394/rak7394.png
keywords:
    - datasheet
    - wisgate
    - RAK7394
    - RAK7394P
    - RAK7394C
sidebar_label: Datasheet
---

# RAK7394 WisGate Developer CM4 Datasheet

## Overview

### Description

The **RAK7394 WisGate Developer CM4** is a LoRaWAN Gateway that has a cellular and a PoE variant. This gateway consists of a RAKR314 CM4 Carrier Board + Raspberry Pi Compute Module 4 (CM4), RAK2287 Concentrator, and RAK2287 Pi HAT.

- **Cellular Variant**: The RAK7394C includes the RAKR314 CM4 Carrier Board with a Raspberry Pi CM4, a RAK2287 Concentrator, a RAK2013 Cellular Pi HAT for cellular connectivity, and a RAK2287 Pi HAT.

- **PoE Variant**: The RAK7394P includes the RAKR314 CM4 Carrier Board with a Raspberry Pi CM4, a RAK2287 Concentrator, a RAK9003 for PoE support, and a RAK2287 Pi HAT.

The **RAK2287 Concentrator** includes a GPS module and a heat sink for better performance and thermal heat dissipation management, and its housing is built with an aluminum casing. It also uses the **SX1302** chip from Semtech® whose built-in LoRa concentrator IP core is a powerful digital signal processing engine. 

This concentrator can receive up to **8 LoRa packets** with different spreading factors on different channels and is available in multiple variants so it can be used for international standard bands. This unique capability allows the implementation of innovative network architectures advantageous over other short-range systems.

The **RAK2287 Pi HAT** is a converter board with a Raspberry Pi form factor that enables the RAK2287 module to be mounted on top of the RAKR314 CM4 Carrier Board. It integrates one (1) 40-pin female Pi HAT connector and one mPCIe connector to connect RAK2287 (RAK9003 in PoE variant/RAK2013 in Cellular variant) to the CM4 Carrier Board.

The **RAKR314 Carrier Board** is designed specifically for the Raspberry Compute Module CM4 following the Raspberry Pi4 form factor. This feature-packed board includes a standard 40 PIN GPIO and supports the RAK PoE HAT, making it an excellent choice for power-over-ethernet applications.

With two USB 2.0 ports, two USB 3.0 ports, two USB-type C ports (one for power and one for programming), and an Ethernet port, this board has all the connectivity options you need. The SD card slot also provides extra storage for the eMMC CM4 modules or serves as a main (boot) for non-eMMC modules. One of the best things about the RAKR314 is that it allows you to utilize the power of the CM4 module in the familiar Raspberry Pi form factor, so you can take advantage of all your existing HATs.

The **RAK7389** is designed for prototyping, proof-of-concept demonstrations, and evaluation. It features a ready-to-use LoRaWAN Gateway OS that connects seamlessly to a LoRaWAN server. With its developer-friendly design, it is easy to set up, even for users with limited technical expertise, making it an excellent choice for building LoRaWAN systems. Offering exceptional value and functionality, it supports a wide range of applications, including Smart Grid, Intelligent Farming, and other IoT enterprise solutions.

:::tip NOTE
By default, the CM4 comes with еMMC and the SD card can be used for additional storage. The SD card can be used for Boot only with CM4 Lite models.
:::

### Features

- Computing with Raspberry Pi Compute Module 4.
- Based on the LoRa Concentrator Engine: Semtech SX1302.
- Supports Cellular module (Quectel BG96 or EG95) for NB-IoT / LTE CAT-M1 / LTE CAT1 / LTE CAT4 (only in Cellular variant).
- Built-in Ublox ZOE-M8Q GPS Module.
- Built-in Heat Sink for thermal heat dissipation management.
- Supports 5 V / 3 A and Power-Over-Ethernet (only in PoE variant) power supply.
- IP30 housing.
- TX power up to 27 dBm, RX sensitivity down to -139 dBm @SF12, BW 125 kHz.
- LoRa Frequency band support: RU864, IN865, EU868, US915, AU915, KR920, AS923.
- Includes Pi-ready 'ID EEPROM', GPIO setup, and device tree can be automatically configured from vendor information.
- Supports a fully open-source LoRaWAN server.

## Specifications

### Overview

The overview covers the RAK7394 board and block diagram.

#### Circuit Board Modules Stack

The basic building blocks of the RAK7394 are summarized in **Figures 1-3**. A key component is the RAK2287, which provides LoRaWAN connectivity. It handles the transmission and reception of LoRa Frames, as well as signal modulation and demodulation. 

Higher-level protocol tasks and the processing of LoRa Frames are managed by the embedded host system (Raspberry Pi). Processed LoRa Frames are then forwarded to a LoRaWAN Server. The segmentation of protocol-related tasks is beyond the scope of this document.

> **Image:** RAK7394 System Structure

> **Image:** RAK7394C System Structure

> **Image:** RAK7394P System Structure

#### Block Diagram

The RAK7394 serves as the central hardware solution for all LoRa-based radio communication. It handles the transmission and reception of radio messages, while the processing of these messages and protocol-related tasks is performed by the embedded host system (Raspberry Pi 4). Processed radio messages are forwarded to a LoRaWAN server. The block diagram of the RAK7394 is illustrated in **Figure 4**.

> **Image:** RAK7394C Block Diagram

##### RAK9003 Pi HAT

:::tip NOTE
The specific segmentation of protocol-related tasks is beyond the scope of this document.
:::

> **Image:** RPi to RAK9003

##### RAK2013 Cellular Pi HAT

The **RAK2013 Cellular Pi HAT** is an add-on board designed according to the Raspberry Pi HAT standard. It enables the transmission of UART data from the Raspberry Pi through a Cellular network and operates in LTE CAT4 mode.

An additional feature of the board is the integrated audio codec and audio amplifier, which allow for VoLTE support. Thus, there is an earphone connector, MIC connector, and speaker connector with an audio amplifier.

> **Image:** RAKR314 to RAK2013

### Hardware

#### Interfaces

The interfaces of RAK7394 are shown in **Figures 7 and 8**.

> **Image:** RAK7394/RAK7394P Interfaces

> **Image:** RAK7394C Interfaces

#### RF Characteristics

##### Operating Frequencies

The RAK7394 models support all LoRaWAN bands.

| Region | Frequency (MHz) |
| --- | --- |
| Europe | EU433 |
| China | CN470 |
| Russia | RU864 |
| India | IN865 |
| Europe | EU868 |
| North America | US915 |
| Australia | AU915 |
| Korea | KR920 |
| Asia | AS923 |

##### Cellular Frequency Bands (Only for RAK7394C)

The Quectel EG95 is a series of LTE CAT4 modules specifically optimized for M2M and IoT applications. Utilizing 3GPP Rel. 11 LTE technology, it offers data rates of 150 Mbps for downlink and 50 Mbps for uplink.

| Frequency | EG95-E | EG95-NA |
| --- | --- | --- |
| LTE FDD | B1 / B3 / B7 / B8 / B20 / B28A | B2 / B4 / B5 / B12 / B13 |
| WCDMA | B1 / B8 | B2 / B4 / B5 |
| GSM / EDGE | 900 / 1800 MHz | - |
| Region | Europe | North America |

##### LoRa RF Characteristics

###### Transmitter RF Characteristics

The RAK7394 features excellent transmitter performance. It is highly recommended to use an optimized power level configuration, included as part of the HAL, to achieve balanced RF output power and current consumption.

| PA Control | PWID Control | Power |
| --- | --- | --- |
| 0 | 10 | -6 dBm |
| 0 | 13 | -3 dBm |
| 0 | 17 | 0 dBm |
| 0 | 20 | 4 dBm |
| 1 | 0 | 8 dBm |
| 1 | 2 | 10 dBm |
| 1 | 4 | 12 dBm |
| 1 | 7 | 14 dBm |
| 1 | 9 | 16 dBm |
| 1 | 10 | 17 dBm |
| 1 | 12 | 19 dBm |
| 1 | 13 | 20 dBm |
| 1 | 16 | 23 dBm |
| 1 | 18 | 25 dBm |
| 1 | 20 | 26 dBm |
| 1 | 22 | 27 dBm |

:::tip NOTE
- Typically, there is a ±1.5 dBi variance between the actual test values and the table data.  
- Unless otherwise specified, measurements are taken at T = 25° C and VDD = 5 V (typical).
:::

| Parameter | Condition | Min. | Typical | Max. |
| --- | --- | --- | --- | --- |
| Frequency Range | - | 863 MHz | - | 870 MHz |
| Modulation Techniques | FSK/LoRa | - | - | - |
| TX Frequency Variation vs. Temperature | Power Level Setting: 20 | -3 kHz | - | +3 kHz |
| TX Power Variation vs. Temperature | Power Level Setting: 20 | -5 dBm | - | +5 dBm |
| TX Power Variation | - | -1.5 dBm | - | +1.5 dBm |

###### Receiver RF Characteristics

It is highly recommended, to use optimized RSSI calibration values, which is part of the HAL v3.1. For both, Radio 1 and 2, the RSSI-Offset should be set at -169.0. The following table gives the typical sensitivity level of the RAK2287.

| Signal Bandwidth (kHz) | Spreading Factor | Sensitivity (DBM) |
| --- | --- | --- |
| 125 | 12 | -139 |
| 125 | 7 | -125 |
| 250 | 12 | -136 |
| 250 | 7 | -123 |
| 500 | 12 | -134 |
| 500 | 7 | -120 |

#### Antenna Specifications

##### LoRa Antenna

The LoRa Antenna with RP-SMA male connector is shown in **Figure 9**.

> **Image:** LoRa Antenna

###### LoRa Antenna Dimensions

The antenna's mechanical dimensions are shown in **Figure 10**.

> **Image:** LoRa Antenna Dimensions

###### LoRa Antenna Parameters

| Item | Specification |
| --- | --- |
| Voltage Standard Wave Ratio (VSWR) | 1.5:1 |
| Gain | -2.0 dBi |
| Working Temperature & Humidity | T:-35° C ~ +80° C, H: 0% RH ~ 95% RH |
| Storage Temperature & Humidity | T:-40° C ~ +85° C, H: 0% RH ~ 95% RH |

##### LTE Antenna

For a built-in BG96, there is one LTE antenna and one GPS antenna. For module built-in EG91/EG95, there are two LTE antennas and no GPS antenna.

> **Image:** LTE Antenna

###### LTE Antenna Dimensions

> **Image:** LTE Antenna Dimensions

###### LTE Antenna Parameters

| Item | Specification |
| --- | --- |
| Frequency (MHz) | 700 / 800 / 880 / 960 / 1710 / 1880 / 2170 |
| Voltage Standard Wave Ratio (VSWR) | 9.3 / 4.6 / 3.6 / 4.9 / 9.3 / 4.4 / 15 |
| Gain | 1.63 / 1.84 / 1.96 / 2.23 / 0.03 / 0.01 / 1.97 |
| Working Temperature & Humidity | T:-35° C ~ +80° C, H: 0% RH ~ 95% RH |
| Storage Temperature & Humidity | T:-40° C ~ +85° C, H: 0% RH ~ 95% RH |

##### GPS Antenna

The GPS antenna with SMA Male Connector for Developer Gateway is shown in **Figure 13**.

> **Image:** GPS Antenna

###### GPS Antenna Dimensions

> **Image:** GPS Antenna Dimensions

###### GPS Antenna Environmental Requirements

| Conditions | Temperature | Humidity |
| --- | --- | --- |
| Working | -35° C to +80° C | 0% RH ~ 95% RH |
| Storage | -40° C to +85° C | 0% RH ~ 95% RH |

###### GPS Antenna Parameters

| Items | Specifications | PET |
| --- | --- | --- |
| Range of Receiving Frequency | 1575.42±1.1 | ±2.5 |
| Center Frequency (MHz) w/ 30 mm2 GND plane | 1575.42 | ±3.0 |
| Bandwidth (MHz) (Return Loss ≤ -10 dB) | ≥10 | ±0.5 |
| VSWR (in Center Frequency) | ≤2.0 | ±0.5 |
| Gain (Zenith) (dBi Typ.) w/ 70 mm2 GND Plane | 4.5 | ±0.5 |
| Axial Ratio (dB) w/ 70 mm2 GND Plane | 3.0 | ±0.2 |
| Polarization | Right-Handed Circular | - |
| Impedance (Ω) | 50 | - |
| Frequency Temperature Coefficient (ppm/ºC) | 0±10 | - |

##### Amplifier Specifications

| Item | Specification |
| --- | --- |
| Frequency Range | 1575.42 MHz |
| Gain | 27 dB |
| VSWR | ≤ 2.0 V |
| Noise Coefficient | ≤ 2.0 dBm |
| DC Voltage | 3 ~ 5 V |
| DC Current | 5 ± 2 mA |

##### Environmental Test Performance Specifications

| Item | Normal Temp. | High Temp. | Low Temp. |
| --- | --- | --- | --- |
| Amplifier Gain | 27 dB ± 2.0 | 27 dB ± 2.0 | 27 dB ± 2.0 |
| VSWR | ≤ 2.0 | ≤ 2.0 | ≤ 2.0 |
| Noise Coefficient | ≤ 2.0 | ≤ 2.0 | ≤ 2.0 |

:::tip NOTE
- **High-Temperature Test**: The device was placed in a chamber for 24 hours with the temperature set to 85° C and humidity at 95% RH. Afterward, the temperature was returned to normal for at least an hour. **The device showed no physical deformation.**
- **Low-Temperature Test**: The device was placed in a chamber for 24 hours with the temperature set to -40° C. Afterward, the temperature was returned to normal for at least an hour. **The device showed no physical deformation.**
:::

#### Electrical Requirements

The RAK7394/RAK7394C/RAK7394P operates at 5 V / 3 A, which is provisioned through a USB Type-C port.

| Parameter | Min. | Typical | Max. |
| --- | --- | --- | --- |
| LoRa Tx mode | - | - | 950 mA |
| Standby power | - | 550 mA | - |
| Burn test mode | - | - | 940 mA |

#### Mechanical Dimension

The outer dimension of RAK7394 is **92 x 68.3 x 57.2 mm**.

:::tip NOTE
The dimensions are identical for both the RAK7394C and RAK7394P variants.
:::

> **Image:** RAK7394/RAK7394C/RAK7394P Dimensions

#### Environmental Requirements

| Parameter | Min. | Typical | Max. |
| --- | --- | --- | --- |
| Operation Temperature Range | -10° C | +25° C | +55° C |
| Storage Temperature Range | -40° C | - | +85° C |

#### Firmware/OS

| Version |                                                                       Source                                                                       |
| :-----: | :------------------------------------------------------------------------------------------------------------------------------------------------: |
| v0.7.1  | [Download](https://downloads.rakwireless.com/LoRa/Software_Firmware/RAKPiOS/History-Version-Release/20230815-rakpios-0.7.1-RAK7394-arm64-lite.zip) |

