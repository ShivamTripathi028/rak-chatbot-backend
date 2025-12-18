---
title: RAK11720 WisDuo LPWAN+BLE Module Datasheet
description: Provides comprehensive information about your RAK11720 WisDuo LPWAN Module to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisduo/rak11720-module/rak11720-module.png
keywords:
    - datasheet
    - wisduo
    - RAK11720
sidebar_label: Datasheet
slug: /product-categories/wisduo/rak11720-module/datasheet/
download: true
---

# RAK11720 WisDuo LPWAN+BLE Module Datasheet

## Overview

### Description

RAK11720 is a low-power, long-range LoRaWAN module based on the Ambiq Apollo3 Blue AMA3B1KK-KBR-B0 SoC MCU.  It supports Bluetooth 5.0 (Bluetooth Low Energy) and the SX1262 LoRa transceiver from Semtech. This module complies with LoRaWAN 1.0.3 specifications (Classes A, B, & C) and also supports LoRa Point-to-Point (P2P) communication, facilitating the quick implementation of customized LoRa networks. The module's dual RF communication capabilities (LoRa + BLE) make it suitable for various IoT applications, including home automation, sensor networks, building automation, and other IoT network applications.

The default RAK11720 firmware is based on RUI3 (RAKwireless Unified Interface). This allows easy use as a standalone module by developing custom firmware via Arduino-compatible RUI3 APIs.  Sensors and other external peripherals can be interfaced directly, eliminating the need for an additional MCU.  Additionally, RAK11720 can be interfaced with an external host MCU using AT commands via UART or a BLE connection.

:::tip NOTE
There are two variants available for the RAK11720 Module:

(1) With MHF4 IPEX connector to connect external antennas

(2) No IPEX connector but with RF pinout to connect custom antenna
:::

### Features

- Based on **AMA3B1KK-KBR-B0** and **SX1262**
- ARM Cortex-M4F
- 1 MB Flash and 348 KB SRAM
- **LoRaWAN 1.0.3** specification compliant
- **Supported bands**: EU433, CN470, IN865, EU868, AU915, US915, KR920, RU864, and AS923-1/2/3/4
- LoRaWAN Activation by OTAA/ABP
- LoRa Point-to-Point (P2P) communication
- Custom firmware using Arduino via RUI3 API
- Easy-to-use AT Command set via UART interface
- I/O ports: UART/I2C/SPI/ADC/GPIO
- Long-range - greater than 10 km with optimized antenna
- Ultra-low-power consumption of 2.37 μA in sleep mode
- **Supply Voltage**: 1.8 V ~ 3.6 V
- **Temperature range**: -40° C ~ 85° C

## Specifications

### Overview

#### Block Diagram

> **Image:** RAK11720 System Block Diagram

### Hardware

The hardware specification is categorized into three parts: RF, electrical, and mechanical parameters.  These include tabular data of the functionalities and standard values for the RAK11720 WisDuo LPWAN Module.

#### Internal Connections Between Apollo3 Blue MCU and SX1262 LoRa transceiver

| SX1262   | Apollo3  | Function               |
| -------- | -------- | ---------------------- |
| SPI_NSS  | GP11     | SPI select             |
| SPI_SCK  | GP8      | SPI clock              |
| SPI_MISO | GP9      | SPI Master in          |
| SPI_MOSI | GP10     | SPI Master out         |
| NRESET   | GP17     | SX1262 reset           |
| ANT_SW   | GP18     | SX1262 RF switch power | 
| DIO1     | GP15     | SX1262 DIO1            |
| BUSY     | GP16     | SX1262 BUSY            |

#### Interfaces

|  Module  |                  Interfaces                  |
|:--------:|:--------------------------------------------:|
| RAK11720 | UART0 (Default for AT command and FW update) |

#### Pin Definition

> **Image:** RAK11720 Pin Illustration

:::warning
When using `LORA RF` and `BLE RF` pins for antenna and not the IPEX connector variant, there are design considerations to make sure optimum RF performance.

- RF traces must be away from interference (switching nodes of DC-DC supplies, high-current/voltage pulses from controllers of inductive loads like motors, signal generators, etc.).
- RF traces must have 50 ohm impedance.  It is advisable to use an impedance simulation software tool to achieve this requirement.
- If using an external antenna connector, place it close to the LoRa RF and BLE RF pins.
- Ground plane optimization is critical for certain antenna types like monopoles.
- The GND trace used for the RF return path must be directly connected to the GND plane and not treated as a thermal relief.
- It is recommended that RF traces be routed in curves, not sharp 90 degree angles.

In addition, with our commitment to making IoT easy, we offer dedicated service for [Antenna RF Design which includes PCB design, tuning, matching and RF testing](https://store.rakwireless.com/products/antenna-rf-design-service-including-pcb-design-tuning-matching-and-rf-test).
:::

| **Pin No.** | **Name**      | **Type** | **Description**                                                         |
|-------------|---------------|----------|-------------------------------------------------------------------------|
| 1           | GP43/UART1_RX | I/O      | GPIO and UART2 Interface (RX)                                           |
| 2           | GP42/UART1_TX | I/O      | GPIO and UART2 Interface (TX)                                           |
| 3           | GP12/ADC9     | I/O      | GPIO and ADC                                                            |
| 4           | GP39/UART0_TX | I/O      | GPIO and UART0 Interface(TX) - AT Command and FW Update                 |
| 5           | GP40/UART0_RX | I/O      | GPIO and UART0 Interface (RX) - AT Command and FW Update                |
| 6           | GP45          | I/O      | GPIO only                                                               |
| 7           | GP21/SWDIO    |          | GPIO and SWD debug pin (SWDIO)                                          |
| 8           | GP20/SWDCK    |          | GPIO and SWD debug pin (SWDCK)                                          |
| 9           | GP27/I2C2_SCL | I/O      | GPIO and I2C2 (SCL)                                                     |
| 10          | GP25/I2C2_SDA | I/O      | GPIO and I2C2 (SDA)                                                     |
| 11          | GND           | POWER    | Ground connections                                                      |
| 12          | LORA RF       | RF       | LORA RF Port (only available on **RAK11720 NO-IPEX connector variant**) |
| 13          | GP7/SPI0_MOSI | I/O      | GPIO and SPI0 (MOSI)                                                    |
| 14          | GP6/SPI0_MISO | I/O      | GPIO and SPI0 (MISO)                                                    |
| 15          | GP5/SPI0_CLK  | I/O      | GPIO and SPI0 (CLK)                                                     |
| 16          | GP1/SPI0_NSS  | I/O      | GPIO and SPI0 (NSS)                                                     |
| 17          | GND           | POWER    | Ground connections                                                      |
| 18          | GND           | POWER    | Ground connections                                                      |
| 19          | GP4           | I/O      | GPIO only                                                               |
| 20          | GP36          | I/O      | GPIO only                                                               |
| 21          | SWO           | I/O      | SBL log output (BOOT pin)                                               |
| 22          | RST           |          | MCU Reset (nRST)                                                        |
| 23          | GND           | POWER    | Ground connections                                                      |
| 24          | VDD           | POWER    | VDD - Voltage Supply                                                    |
| 25          | GP32/ADC4     | I/O      | GPIO and ADC                                                            |
| 26          | GP31/ADC3     | I/O      | GPIO and ADC                                                            |
| 27          | GP37          | I/O      | GPIO only                                                               |
| 28          | GND           | POWER    | Ground connections                                                      |
| 29          | GP44          | I/O      | GPIO only                                                               |
| 30          | GP38          | I/O      | GPIO only                                                               |
| 31          | GP33/ADC5     | I/O      | GPIO and ADC                                                            |
| 32          | GP13/ADC8     | I/O      | GPIO and ADC                                                            |
| 33          | BLE RF        | RF       | BLE RF Port (only available on **RAK11720 NO-IPEX connector variant**)  |
| 34          | GND           | POWER    | Ground connections                                                      |

#### RF Characteristics

The RAK11720 module supports the LoRaWAN bands, as shown in the table below. When buying an RAK11720 module, pay attention to specifying the correct core module, RAK11720 H/L, for your region. **H** denotes high-frequency regions and **L** denotes low-frequency regions.

| Module | Region | Frequency |
| --- | --- | --- |
| RAK11720 (L) | Europe | EU433 |
| RAK11720 (L) | China | CN470 |
| RAK11720 (H) | Europe | EU868 |
| RAK11720 (H) | North America | US915 |
| RAK11720 (H) | Australia | AU915 |
| RAK11720 (H) | Korea | KR920 |
| RAK11720 (H) | Asia | AS923-1/2/3/4 |
| RAK11720 (H) | India | IN865 |
| RAK11720 (H) | Russia | RU864 |

#### Electrical Characteristics

##### Operating Voltage

| Feature | Minimum | Typical | Maximum |   Unit    |
|:-------:|:-------:|:-------:|:-------:|:---------:|
|   VCC   |   1.8   |   3.3   |   3.6   | Volts (V) |

##### Operating Current

|      Feature      |  Condition   | Minimum |               Typical               | Maximum | Unit |
|:-----------------:|:------------:|:-------:|:-----------------------------------:|:-------:|:----:|
| Operating Current | BLE TX Mode  |    -    |         12.7 @4.0 dBm          |    -    |  mA  |
|                   | LORA TX Mode |    -    | 87 @ 20 dBm, 868 MHz |    -    |  mA  |

##### Sleep Current

|       Feature       | Condition | Minimum (2.1 V) | Typical (3.3 V) | Maximum | Unit |
|:-------------------:|:---------:|:--------------------:|:--------------------:|:-------:|:----:|
| Current Consumption |   EU868   |          -           |         2.37         |    -    |  μA  |
|                     |   US915   |          -           |         2.37         |    -    |  μA  |
|                     |   CN470   |          -           |         2.37         |    -    |  μA  |

#### Mechanical Characteristics

##### Module Dimensions

> **Image:** Board dimension

##### Layout Recommendation

> **Image:** PCB footprint and recommendations

#### Environmental Characteristics

##### Operating Temperature

|        Feature        | Minimum | Typical | Maximum |   Unit   |
|:---------------------:|:-------:|:-------:|:-------:|:--------:|
| Operating Temperature |   -40   |   25    |   85    | ° C |

##### Storage Temperature

|       Feature       | Minimum | Typical | Maximum |   Unit   |
|:-------------------:|:-------:|:-------:|:-------:|:--------:|
| Storage Temperature |   -40   |    -    |   85    | ° C |

##### Recommended Reflow Profile

> **Image:** Reflow Profile for RAK11720

Standard conditions for reflow soldering:

- Pre-heating Ramp (A) (Initial temperature: 150° C): **1 ~ 2.5° C/sec**
- Soaking Time (T2) (150 ~ 180° C): **60 ~ 100 sec**
- Peak Temperature (G): **230 ~ 250° C**
- Reflow Time (T3) (> 220° C): **30 ~ 60 sec**
- Ramp-up Rate (B): **0 ~ 2.5° C/sec**
- Ramp-down Rate (C): **1 ~ 3° C/sec**

### Firmware

Download the latest RAK11720 WisDuo LPWAN Module firmware provided below. RAK11720 (L) and RAK11720 (H) use the same firmware and it will automatically detect the variant of the module being used.

|          Model           |            Note             |                                                   Source                                                    |
|:------------------------:|:---------------------------:|:-----------------------------------------------------------------------------------------------------------:|
| RAK11720 (.bin via UART) | (default baudrate = 115200) |  [Download](https://downloads.rakwireless.com/RUI/RUI3/Image/RAK11720_latest_Nonsecure_OTA_Package_UART.bin)|
| RAK11720 (.bin via BLE)  |                             |  [Download](https://downloads.rakwireless.com/RUI/RUI3/Image/RAK11720_latest_Nonsecure_OTA_Package_BLE.bin) |
|     RAK11720 (.hex)      |                             |  [Download](https://downloads.rakwireless.com/RUI/RUI3/Image/RAK11720_latest_final.hex)          |

### Certification

### Certifications
- **CE:** https://downloads.rakwireless.com/LoRa/RAK11720/Certification/RAK11720_CE_Certification.pdf
- **FCC:** https://downloads.rakwireless.com/LoRa/RAK11720/Certification/RAK11720_FCC_Certification.pdf
- **ISED:** https://downloads.rakwireless.com/LoRa/RAK11720/Certification/RAK11720_ISED_Certification.pdf
- **RCM:** https://downloads.rakwireless.com/LoRa/RAK11720/Certification/RAK11720_RCM_Certification.pdf
- **ANATEL:** https://downloads.rakwireless.com/LoRa/RAK11720/Certification/RAK11720_ANATEL_Certification.pdf

:::tip Note
For CE and FCC certifications we provide an AT command guide.    
You can find it in our [RUI3 documentation](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/certification-guide) or get it from our [Download Center](https://downloads.rakwireless.com/#RUI/RUI3/Certification%20Guide/).    
::: 

