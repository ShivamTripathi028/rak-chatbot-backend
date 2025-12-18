---
title: RAK4630 LoRaWAN + BLE Module Datasheet | Specs & Features
description: Explore the RAK4630 LoRaWAN module datasheet—featuring the Nordic nRF52840 MCU, SX1262 transceiver, and low-power IoT connectivity. Get full specs now!
image: https://images.docs.rakwireless.com/wisduo/rak4630-module/rak4630-module.png
keywords:
  - rak4630
  - rak4630 module
  - rak4630 datasheet
  - lorawan module datasheet
  - lorawan ble module specs
  - ble 5 module specs
  - sx1262 lora transceiver
  - nrf52840 mcu
  - lorawan module for iot
  - nrf52840 lorawan development board
  - lora wireless module
  - low power mcu
  - lora p2p communiation
  - low power consumption modules
  - dual rf iot lorawan module
sidebar_label: Datasheet
slug: /product-categories/wisduo/rak4630-module/datasheet/
date: 2022-04-07
download: true
---

# RAK4630 WisBlock LoRaWAN+BLE Module Datasheet

## Overview

### Description

The RAK4630 is a low-power, long-range transceiver module featuring the Nordic nRF52840 MCU, which supports Bluetooth 5.0 (Bluetooth Low Energy) and the latest SX1262 LoRa transceiver from Semtech. This module adheres to Classes A, B, and C specifications of LoRaWAN 1.0.3 and also facilitates LoRa point-to-point (P2P) communication, enabling rapid implementation of custom LoRa networks.

With its dual RF communication capabilities (LoRa + BLE), the module is well-suited for diverse IoT applications, including home automation, sensor networks, building automation, and various IoT network scenarios.

The default firmware of the RAK4630 is built on RUI3 (RAKwireless Unified Interface), which simplifies using the RAK4630 as a standalone module by enabling the development of custom firmware through RUI APIs. This setup allows direct interfacing with sensors and other external peripherals without requiring an additional MCU.  Additionally, the RAK4630 can communicate with an external host MCU using AT commands via USB, UART, or a BLE connection.

### Features

- **LoRaWAN 1.0.3** specification compliant
- **Supported bands**: IN865, EU868, AU915, US915, KR920, RU864, and AS923
- LoRaWAN Activation by OTAA/ABP
- LoRa Point-to-Point (P2P) communication
- Custom firmware using Arduino via RUI3 API
- Easy-to-use AT Command set via UART interface
- TCXO crystal for LoRa chip
- IO ports: UART, I2C, GPIO, USB
- Temperature range: -40° C to +85° C
- Supply voltage: 2.0 ~ 3.6 V
- Low-Power Wireless Systems with 7.8 kHz to 500 kHz bandwidth
- Ultra-Low Power Consumption 4.23 uA in sleep mode
- LoRa PA Boost mode with 22 dBm output power
- BLE 5.0 (Tx power -20 to +4 dBm in 4 dB steps)
- Serial Wire Debug (SWD) interface
- Module size: 15 mm x 23 mm x 3 mm

## Specifications

### Overview

### Hardware

The hardware specification is categorized into three parts: RF, electrical, and mechanical parameters.  This includes tabular data detailing the functionalities and standard values of the RAK4630 WisBlock LoRaWAN module.

#### Internal Connections Between nRF52840 MCU and SX1262 LoRa transceiver

| SX1262   | nRF52840 | Function               |
| -------- | -------- | ---------------------- |
| SPI_NSS  | P1.10    | SPI select             |
| SPI_SCK  | P1.11    | SPI clock              |
| SPI_MISO | P1.13    | SPI Master in          |
| SPI_MOSI | P1.12    | SPI Master out         |
| NRESET   | P1.06    | SX1262 reset           |
| ANT_SW   | P1.05    | SX1262 RF switch power | 
| DIO1     | P1.15    | SX1262 DIO1            |
| BUSY     | P1.14    | SX1262 BUSY            |

#### Interfaces

| Module  | Interfaces |
| :-----: | :--------: |
| RAK4630 | USB, UART1 |

#### Pin Definition

> **Image:** RAK4630 module pinout diagram

:::warning
When using `RF_LoRa` and `RF_BT` pins for the antenna and not the IPEX connector variant, design considerations are necessary to ensure optimum RF performance.

- RF traces must be away from interference (switching nodes of DC-DC supplies, high-current/voltage pulses from controllers of inductive loads like motors, signal generators, etc.).
- RF traces must have 50 
ohm impedance.  It is advisable to use impedance simulation software to achieve this requirement.
- If using an external antenna connector, place it close to the `RF_LoRa` and `RF_BT` pins.
- Ground plane optimization is critical for certain antenna types, such as monopoles.
- The GND trace used for the RF return path must be directly connected to the GND plane and not treated as a thermal relief.
- It is recommended that RF traces be routed in curves, not sharp 90 
degree angles.

In addition, with a commitment to making IoT easy, RAK offers a dedicated service for [Antenna RF Design](https://store.rakwireless.com/products/antenna-rf-design-service-including-pcb-design-tuning-matching-and-rf-test) which includes PCB design, tuning, matching, and RF testing.
:::

| **Pin No.** | **Name**                        |
| :---------: | :-----------------------------: |
| 1           | VBUS                            |
| 2           | USB-                            |
| 3           | USB+                            |
| 4           | P0.13/I2C_SDA                   |
| 5           | P0.14/I2C_SCL                   |
| 6           | P0.15/UART2_RX                  |
| 7           | P0.16/UART2_TX                  |
| 8           | P0.17/UART2_DE                  |
| 9           | P0.19/UART1_RX (AT Command)     |
| 10          | P0.20/UART1_TX (AT Command)     |
| 11          | P0.21/UART1_DE                  |
| 12          | P0.10/NFC2                      |
| 13          | P0.09/NFC1                      |
| 14          | GND                             |
| 15          | RF_BT                           |
| 16          | GND                             |
| 17          | NRF_RESET                       |
| 18          | SWDCLK                          |
| 19          | SWDIO                           |
| 20          | VBAT_SX                         |
| 21          | VBAT_IO_SX                      |
| 22          | GND                             |
| 23          | P0.24/I2C_SDA_2                 |
| 24          | P0.25/I2C_SCL_2                 |
| 25          | P1.01/SW1                       |
| 26          | P1.02/SW2                       |
| 27          | P1.03/LED1                      |
| 28          | P1.04/LED2                      |
| 29          | P0.03/QSPI_CLK                  |
| 30          | P0.02/QSPI_DIO3                 |
| 31          | P0.28/QSPI_DIO2                 |
| 32          | P0.29/QSPI_DIO1                 |
| 33          | P0.30/QSPI_DIO0                 |
| 34          | P0.26/QSPI_CS                   |
| 35          | GND                             |
| 36          | GND                             |
| 37          | RF_LoRa                         |
| 38          | GND                             |
| 39          | P0.31/AIN7                      |
| 40          | P0.05/AIN3                      |
| 41          | P0.04/AIN2                      |
| 42          | GND                             |
| 43          | VDD_NRF                         |
| 44          | VBAT_NRF                        |

##### SX1262 Setup

Information for writing custom firmware for the RAK4630 includes details about the internal connections between the RAK4630 and the necessary initialization parameters for the SX1262 LoRa transceiver.

| nRF52840 GPIO	| SX1262 Pin | function                          |
| :-----------: | :--------: | :-------------------------------: |
| P1.10         | NSS        | SPI NSS                           |
| P1.11         | SCK        | SPI CLK                           |
| P1.12         | MOSI       | SPI MOSI                          |
| P1.13         | MISO       | SPI MISO                          |
| P1.14         | BUSY       | BUSY signal                       |
| P1.15         | DIO1       | DIO1 event interrupt              |
| P1.06         | NRESET     | NRESET manual reset of the SX1262 |

Important for successful SX1262 initialization:
- Set up DIO2 to control the antenna switch.
- Set up DIO3 to control the TCXO power supply.
- Set up the SX1262 to use its DCDC regulator, not the LDO.
- The RAK4630 schematic shows GPIO P1.07 connected to the antenna switch, but it should not be initialized, as DIO2 will control the antenna switch.

#### RF Characteristics

When purchasing a RAK4630 module, it is essential to specify the correct core module, RAK4630 H/L, for your region. H indicates high-frequency regions, and L indicates low-frequency regions. The RAK4630 module supports LoRaWAN bands as outlined in the table below.

:::tip NOTE
Detailed information about the RAK4630 BLE and LoRa antenna can be found on the [antenna datasheet](https://downloads.rakwireless.com/#LoRa/WisBlock/Accessories/).
:::

| Region        | Frequency (MHz)  | Core Module |
| :-----------: | :--------------: | :---------: |
| India         | IN865            | RAK4630(H)  |
| Europe        | EU868            | RAK4630(H)  |
| Europe        | EU433            | RAK4630(L)  |
| North America | US915            | RAK4630(H)  |
| Canada        | US915            | RAK4630(H)  |
| Australia     | AU915            | RAK4630(H)  |
| Korea         | KR920            | RAK4630(H)  |
| Asia          | AS923-1/2/3/4    | RAK4630(H)  |
| China         | CN470            | RAK4630(L)  |

#### Electrical Characteristics

##### Power Consumption

| **Item**                                 | **Current Average** | **Condition - Voltage and Dwell Time**             |
| :--------------------------------------: | :-----------------: | :------------------------------------------------: |
| RAK4630 Module in One-Time Sleep         | 4.42 uA        | 3.3 V 10 seconds                         |
| RAK4630 Module System up in Idle mode    | 3.35 mA        | 3.3 V 10 seconds                         |
| RAK4630 Module in LoRaWAN One-Time Sleep | 4.23 uA        | 3.3 V 10 seconds                         |
| RAK4630 Module 15 Bytes Data TX Sending  | 67.8 mA        | 3.6 V 1 second (in RAK5005-O board)      |
| RAK4630 Module in RX Window Received     | 2.22 mA        | 3.6 V 1 second (in RAK5005-O board)      |

##### Absolute Maximum Ratings

| **Symbol** | **Description**               | **Min.** | **Nom.** | **Max.** | **Unit** |
| :--------: | :---------------------------: | :------: | :------: | :------: | :------: |
| VBAT_SX    | LoRa chip supply voltage      | -0.5     |          | 3.9      | V        |
| VBAT_SX_IO | LoRa chip supply for I/O pins | -0.5     |          | 3.9      | V        |
| VDD_NRF    | MCU power supply              | -0.3     |          | 3.9      | V        |
| VBUS       | USB supply voltage            | -0.3     |          | 5.8      | V        |
| VBAT_NRF   | MCU high voltage power supply | -0.3     |          | 5.8      | V        |

##### Recommended Operating Conditions

| **Symbol** | **Description**                    | **Min.** | **Nom.** | **Max.** | **Unit** |
| :--------: | :--------------------------------: | :------: | :------: | :------: | :------: |
| VBAT_SX    | SX1262 supply voltage              | 2.0      | 3.3      | 3.7      | V        |
| VBAT_SX_IO | SX1262 supply for I/O pins         | 2.0      | 3.3      | 3.7      | V        |
| VDD_NRF    | NRF52840 power supply              | 2.0      | 3.3      | 3.6      | V        |
| VBUS       | VBUS USB supply voltage            | 4.35     | 5.0      | 5.5      | V        |
| VBAT_NRF   | NRF52840 high voltage power supply | 2.5      |          | 5.5      | V        |

##### Schematic Diagram

> **Image:** SX1262 Section

> **Image:** nRF51840 and Module Pinout

#### Mechanical Characteristics

##### Module Dimensions

> **Image:** Board dimension

##### Layout Recommendation

> **Image:** PCB footprint and recommendations

## Certification

### Certifications
- **CE:** https://downloads.rakwireless.com/LoRa/RAK4630/Certification/RAK4630_RAK4631_CE_Certification.zip
- **FCC:** https://downloads.rakwireless.com/LoRa/RAK4630/Certification/RAK4630_RAK4631_FCC_Certification.zip
- **ISED:** https://downloads.rakwireless.com/LoRa/RAK4630/Certification/RAK4630_RAK4631_ISED_Certification.pdf
- **KC:** https://downloads.rakwireless.com/LoRa/RAK4630/Certification/RAK4630_RAK4631_KC_Certification.pdf
- **RCM:** https://downloads.rakwireless.com/LoRa/RAK4630/Certification/RAK4630_RCM_Certification.pdf
- **REACH:** https://downloads.rakwireless.com/LoRa/RAK4630/Certification/RAK4630_RAK4631_REACH_Report.pdf
- **ROHS:** https://downloads.rakwireless.com/LoRa/RAK4630/Certification/RAK4630_RAK4631_RoHS_Report.pdf

:::tip Note
For CE and FCC certifications we provide an AT command guide.    
You can find it in our [RUI3 documentation](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/certification-guide) or get it from our [Download Center](https://downloads.rakwireless.com/#RUI/RUI3/Certification%20Guide/).    
::: 

