---
title: RAK11300 WisDuo LPWAN Module Datasheet
description: Provides comprehensive information about the RAK11300 module to help you use it. This information includes technical specifications, characteristics, and requirements, and also discusses the device components.
image: "https://images.docs.rakwireless.com/wisduo/rak11300-module/rak11300-module.png"
keywords:
    - datasheet
    - wisduo
    - RAK11300
sidebar_label: Datasheet
slug: /product-categories/wisduo/rak11300-module/datasheet/
download: true
---

# RAK11300 WisDuo LPWAN Module Datasheet

## Overview

### Description

The RAK11300 WisDuo LPWAN Module is based on the Raspberry Pi RP2040 chip and SX1262 RF transceiver. It provides an easy-to-use, small, low-power solution for long-range wireless data applications. This module complies with LoRaWAN 1.0.2 Class A and C specifications. It can easily connect to various LoRaWAN server platforms such as The Things Network (TTN), ChirpStack, and Helium.

### Features

- Based on Raspberry Pi **RP2040** and Semtech **SX1262**
- **LoRaWAN 1.0.2** specification compliant
- **Supported bands**: EU433, CN470, IN865, EU868, AU915, US915, KR920, RU864, and AS923-1/2/3/4
- LoRaWAN Activation by OTAA/ABP
- Long-range - greater than 15 km with optimized antenna
- ARM Cortex-M0+ Dual Core
- 133 MHz CPU Clock
- 246 kbytes RAM
- **Supply Voltage**: 2.0 V ~ 3.6 V
- **Temperature Range**: -20° C ~ 85° C

## Specifications

This section covers the hardware and software specifications for the RAK11300. It also includes a block diagram of the module, showing its interfaces.

### Overview

#### Block Diagram

> **Image:** RAK11300 System Block Diagram

### Hardware

The hardware specification is divided into four sections, detailing the interfacing, pinouts with their corresponding functions, and diagrams. It also includes the RF and mechanical parameters of the RAK11300 WisDuo LPWAN module.

#### Internal Connections Between RP2040 MCU and SX1262 LoRa transceiver

| SX1262   | RP2040   | Function               |
| -------- | -------- | ---------------------- |
| SPI_NSS  | GPIO13   | SPI select             |
| SPI_SCK  | GPIO10   | SPI clock              |
| SPI_MISO | GPIO12   | SPI Master in          |
| SPI_MOSI | GPIO11   | SPI Master out         |
| NRESET   | GPIO14   | SX1262 reset           |
| ANT_SW   | GPIO25   | SX1262 RF switch power | 
| DIO1     | GPIO29   | SX1262 DIO1            |
| BUSY     | GPIO15   | SX1262 BUSY            |

#### Interfaces

|  Module  | Interfaces |
|:--------:|:----------:|
| RAK11300 | UART, USB  |

#### Pin Definition

> **Image:** RAK11300 Module Pinout

##### Pin Description

The table below shows the pin definition and description of RAK11300:

| Type |  Description   |
|:----:|:--------------:|
|  PI  |  Power Input   |
|  PO  |  Power Output  |
|  DI  | Digital Input  |
|  DO  | Digital Output |
|  IO  | Bidirectional  |
|  AI  |  Analog Input  |
|  AO  | Analog Output  |

##### Power Supply

|  Pin Name  |        Pin No.         |  Type  |                Description                |
|:----------:|:----------------------:|:------:|:-----------------------------------------:|
|  VBAT_SX   |           21           |   PI   |          Supply for the LoRa IC           |
| VBAT_SX_IO |           22           |   PI   | Supply for the Digital I/O interface pins |
|    DVDD    |           45           |   PI   |            Supply for the MCU             |
|    AVDD    |           46           |   PI   |           ADC Reference Voltage           |
|    GND     | 14, 17, 23, 37, 40, 44 | Ground |                  Ground                   |

##### I2C Interface
| Pin Name | Pin No. | Type |   Description    |
|:--------:|:-------:|:----:|:----------------:|
| I2C1_SDA |    4    |  IO  | I2C serial data  |
| I2C1_SCL |    5    |  DO  | I2C serial clock |
| I2C2_SDA |   24    |  IO  | I2C serial data  |
| I2C2_SCL |   25    |  DO  | I2C serial clock |

##### USB Interface

| Pin Name | Pin No. | Type |       Description        |
|:--------:|:-------:|:----:|:------------------------:|
|  USB_DM  |    2    |  IO  | USB differential data(-) |
|  USB_DP  |    3    |  IO  | USB differential data(+) |

##### UART Interface

| Pin Name | Pin No. | Type |  Description   |
|:--------:|:-------:|:----:|:--------------:|
| UART1_RX |    9    |  DI  | UART1 receive  |
| UART1_TX |   10    |  DO  | UART1 transmit |
| UART2_RX |    6    |  DI  | UART2 receive  |
| UART2_TX |    7    |  DO  | UART2 transmit |

##### SPI Interface

| Pin Name  | Pin No. | Type |          Description           |
|:---------:|:-------:|:----:|:------------------------------:|
| SPI0_SCK  |   30    |  DO  |           SPI clock            |
| SPI0_MISO |   33    |  DI  | SPI master input, slave output |
| SPI0_MOSI |   34    |  DO  | SPI master output. slave input |
| SPI0_CSN  |   35    |  DO  |        SPI chip select         |

##### SWD Interface

| Pin Name | Pin No. | Type  |                  Description                  |
|:--------:|:-------:|:-----:|:---------------------------------------------:|
|  SWCLK   |   19    | Debug | SWD clock input for debugging and programming |
|  SWDIO   |   20    | Debug |     SWD I/O for debugging and programming     |

##### RESET

| Pin Name | Pin No. | Type |         Description          |
|:--------:|:-------:|:----:|:----------------------------:|
|  RESET   |   18    |  DI  | Reset the module, Active Low |

##### Antenna Interface

:::warning
When using the `RF_LoRa` pin for the antenna and not the IPEX connector variant, design considerations are necessary to ensure optimum RF performance.

- The RF trace must be away from interference sources (switching nodes of DC-DC supplies, high-current/voltage pulses from controllers of inductive loads like motors, signal generators, etc.).
- The RF trace must have 50 ohm impedance.  Using impedance simulation software is advisable to achieve this.
- If using an external antenna connector, place it close to the `RF_LoRa` pin.
- Ground plane optimization is critical for certain antenna types, such as monopoles.
- The GND trace used for the RF return path must be directly connected to the GND plane and not treated as a thermal relief.
- It is recommended to route the RF trace in a curve, rather than with sharp 90 degree bends.

In addition, with a commitment to making IoT easy, RAK offers a dedicated service for <a href="https://store.rakwireless.com/products/antenna-rf-design-service-including-pcb-design-tuning-matching-and-rf-test" target="_blank">Antenna RF Design</a> which includes PCB design, tuning, matching, and RF testing.
:::

| Pin Name | Pin No. | Type |      Description       | Comment                                                                                                          |
|:--------:|:-------:|:----:|:----------------------:|------------------------------------------------------------------------------------------------------------------|
| RF_LoRa  |   38    |  IO  | LoRa antenna interface | 50 Ω Impedance
This pin can't be used on modules with an IPEX connector. If unused, keep this pin open. |

##### ADC and GPIO

|     Pin Name     | Pin No. |    Type     |                            Description                            |
|:----------------:|:-------:|:-----------:|:-----------------------------------------------------------------:|
|      GPIO7       |   11    |     IO      |                   General-purpose input/output                    |
|      GPIO8       |   12    |     IO      |                   General-purpose input/output                    |
|      GPIO9       |   13    |     IO      |                   General-purpose input/output                    |
|      GPIO22      |   27    |     IO      |                   General-purpose input/output                    |
|      GPIO23      |   28    |     IO      |                   General-purpose input/output                    |
|      GPIO24      |   29    |     IO      |                   General-purpose input/output                    |
|      GPIO27      |   41    |     IO      |                   General-purpose input/output                    |
| GPIO26
 ADC1 |   43    | IO
 AI  | General-purpose input/output 
 General-purpose ADC interface  |
| GPIO28
 ADC0 |   44    | IO 
 AI | General-purpose input/output 
  General-purpose ADC interface |

#### RF Characteristics

The RAK11300 supports two different frequency variations: RAK11300(L) Low Radio Frequency and RAK11300(H) High Radio Frequency.

##### Operating Frequencies

| Module | Region | Frequency |
| --- | --- | --- |
| RAK11300(L) | Europe | EU433 |
| RAK11300(L) | China | CN470 |
| RAK11300(H) | Europe | EU868 |
| RAK11300(H) | America | US915 |
| RAK11300(H) | Australia | AU915 |
| RAK11300(H) | Korea | KR920 |
| RAK11300(H) | Asia | AS923 |
| RAK11300(H) | India | IN865 |
| RAK11300(H) | Russia | RU864 |

#### Electrical Characteristics

##### Recommended Operating Conditions

| **Symbol** |      **Description**       | **Min.** | **Nom.** | **Max.** | **Unit** |
|:----------:|:--------------------------:|:--------:|:--------:|:--------:|:--------:|
|  VBAT_SX   |   SX1262 supply voltage    |   2.0    |   3.3    |   3.7    |    V     |
| VBAT_SX_IO | SX1262 supply for I/O pins |   2.0    |   3.3    |   3.7    |    V     |
|    DVDD    |    Power supply  of MCU    |   2.0    |   3.3    |   3.6    |    V     |
|    AVDD    |   ADC Reference Voltage    |    -     |   3.3    |    -     |    V     |

##### Absolute Maximum Ratings

| **Symbol** |        **Description**        | **Min.** | **Nom.** | **Max.** | **Unit** |
|:----------:|:-----------------------------:|:--------:|:--------:|:--------:|:--------:|
|  VBAT_SX   |   LoRa chip supply voltage    |   -0.5   |    -     |   3.9    |    V     |
| VBAT_SX_IO | LoRa chip supply for I/O pins |   -0.5   |    -     |   3.9    |    V     |
|    DVDD    |      Supply for the MCU       |   -0.5   |    -     |   3.6    |          |
|    AVDD    |     ADC Reference Voltage     |   -0.5   |    -     |   3.6    |          |
|  ESD HBM   |       Human Body Model        |    -     |    -     |   2000   |    V     |
|  ESD  CDM  |     Charged Device Model      |    -     |    -     |   500    |    V     |

#### Mechanical Characteristics

##### Module Dimensions

> **Image:** RAK11300 Physical Dimension

##### Layout Recommendation

> **Image:** RAK11300 Layout

#### Environmental Characteristics

##### Operating Temperature

|        Feature        | Minimum | Typical | Maximum |   Unit   |
|:---------------------:|:-------:|:-------:|:-------:|:--------:|
| Operating Temperature |   -20   |   25    |   85    | ° C |

##### Storage Temperature

|       Feature       | Minimum | Typical | Maximum |   Unit   |
|:-------------------:|:-------:|:-------:|:-------:|:--------:|
| Storage Temperature |   -20   |         |   85    | ° C |

##### Recommended Reflow Profile

> **Image:** Reflow Profile for RAK11300

Standard conditions for reflow soldering:

- Pre-heating Ramp (A) (Initial temperature: 150° C): **1 ~ 2.5° C/sec**
- Soaking Time (T2) (150 ~ 180° C): **60 ~ 100 sec**
- Peak Temperature (G): **230 ~ 250° C**
- Reflow Time (T3) (> 220° C): **30 ~ 60 sec**
- Ramp-up Rate (B): **0 ~ 2.5° C/sec**
- Ramp-down Rate (C): **1 ~ 3° C/sec**

### Software

Download the latest firmware of the RAK11300 WisDuo LPWAN Module provided below.

#### Firmware/OS
|  Model   | Version |                                              Source                                                                          |
|:--------:|:-------:|:----------------------------------------------------------------------------------------------------------------------------:|
| RAK11300 | V1.0.0  | <a href="https://downloads.rakwireless.com/LoRa/RAK11300/Firmware/RAK11300_Latest_Firmware.zip" target="_blank">Download</a> |

## Certification

### Certifications
- **CE:** https://downloads.rakwireless.com/LoRa/WisBlock/RAK11310/Certification/RAK11300_RAK11310_CE_Certification.pdf
- **FCC:** https://downloads.rakwireless.com/LoRa/WisBlock/RAK11310/Certification/RAK11300_RAK11310_FCC_Certification.zip
- **ISED:** https://downloads.rakwireless.com/LoRa/WisBlock/RAK11310/Certification/RAK11300_RAK11310_ISED_Certification.pdf
- **UKCA:** https://downloads.rakwireless.com/LoRa/WisBlock/RAK11310/Certification/RAK11300_RAK11310_UKCA_Certification.pdf

