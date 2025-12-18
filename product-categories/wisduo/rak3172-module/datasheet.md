---
title: RAK3172 WisDuo LoRaWAN Module Datasheet | Specs & Features
description: Explore the RAK3172 datasheet for detailed specifications on this LoRaWAN module. Learn about its low-power design, UART interface, RF performance, and supported bands.
keywords:
  - lorawan module datasheet
  - stm32wle5ccu6 lora module
  - lorawan module stm32wle5ccu6
  - lora development module
  - rak3172 specifications
  - rak3172
  - rak3172 datasheet
  - rf module with lora p2p support
  - long-range lorawan transceiver specs
  - low-power lorawan module specs
  - lorawan module with uart interface
  - lorawan module with ble 5.0
sidebar_label: Datasheet
slug: /product-categories/wisduo/rak3172-module/datasheet/
date: 2021-04-12
download: true
---

# RAK3172 WisDuo LoRaWAN Module Datasheet

## Overview

### Description

The RAK3172 is a low-power, long-range transceiver module based on the STM32WLE5CC chip. It offers an easy-to-use, compact, and low-power solution for long-range wireless data applications. This module complies with Class A, B, and C of the LoRaWAN 1.0.3 specifications. It can effortlessly connect to various LoRaWAN server platforms, including TheThingsNetwork (TTN), Chirpstack, Actility, etc. Additionally, it supports LoRa Point-to-Point (P2P) communication mode, enabling the rapid implementation of customized long-range LoRa networks.

You can configure the module's mode and operation using AT commands via a UART interface. RAK3172 also offers low-power features, making it well-suited for battery-powered applications.

### Features

- Based on **STM32WLE5CCU6**
- **LoRaWAN 1.0.3** specification compliant
- **Supported bands**: EU433, CN470, IN865, EU868, AU915, US915, KR920, RU864, and AS923-1/2/3/4
- LoRaWAN activation via OTAA/ABP
- LoRa Point-to-Point (P2P) communication
- Custom firmware using Arduino via RUI3 API
- Easy to use AT command set via UART interface
- Long-range - greater than 15 km with optimized antenna
- ARM Cortex-M4 32-bit
- 256 kbytes flash memory with ECC
- 64 kbytes RAM
- Ultra-low-power consumption of 1.69 μA in sleep mode
- **Supply Voltage**: 2.0 V ~ 3.6 V
- **Temperature Range**:
  - **RAK3172**: -20° C ~ 85° C
  - **RAK3172-T**: -40° C ~ 85° C

:::tip NOTE
There are two certification variants available for the RAK3172 Module: (1) with the CE & UKCA Certification Mark and (2) with FCC, IC, & RCM Certification Mark.

If you need a LoRa module with BLE 5.0 capability, you can check out the [RAK11720](https://store.rakwireless.com/products/rak11720-ambiq-apollo3-module-for-lorawan?utm_source=RAK11720&utm_medium=Document&utm_campaign=BuyFromStore). The RAK11720 is pin-to-pin compatible with the RAK3172 and has additional pins for ground and a BLE RF antenna port.
:::

:::warning
Temperature ratings:

**RAK3172** is -20° C to 85° C

**RAK3172-T** is -40° C to 85° C

:::

## Specifications

This section covers the hardware and software specifications of the RAK3172. Also, it includes the block diagram and an updated firmware link for the RAK3172 WisDuo Module.

### Overview

#### Block Diagram

> **Image:** RAK3172 System Block Diagram

### Hardware

The hardware specification discusses the interfaces, pinouts, and their corresponding functions and diagrams. It also covers the parameters of both RAK3172 modules in terms of RF, electrical, mechanical, and operating characteristics.

#### Interfaces

| Module  |      Interfaces      |
| :-----: | :------------------: |
| RAK3172 | UART2/LPUART1, UART1 |

##### Sub-GHz SPI interface

A dedicated internal SPI interface called **SUBGHZSPI** is used to communicate with the RF subsystem of the **STM32WLE5CCU6**.

#### Pin Definition

> **Image:** Board Pinout for RAK3172

:::warning
When using `RF` pin for antenna and not the IPEX connector variant, there are design considerations to make sure optimum RF performance.

- RF traces must be away from interference (switching nodes of DC-DC supplies, high current/voltage pulses from controllers of inductive loads like motors, signal generators, etc.).
- RF traces must have 50 Ohm impedance. It is advisable to use impedance simulation software tools to achieve this requirement.
- If using an external antenna connector, place it close to the `RF` pin.
- Ground plane optimization is critical for certain antenna types, such as monopoles.
- GND traces used for RF path return must be directly connected to the GND plane and not treated as thermal reliefs.
- It is recommended that RF traces be routed in a curve rather than at a sharp 90 degrees.

In addition, with a commitment to making IoT easy, RAK offers a dedicated service for [Antenna RF Design](https://store.rakwireless.com/products/antenna-rf-design-service-including-pcb-design-tuning-matching-and-rf-test) which includes PCB design, tuning, matching, and RF testing.
:::

| **Pin No.** | **Name**      | **Type** | **Description**                                                                                   |
| ----------- | ------------- | -------- | ------------------------------------------------------------------------------------------------- |
| 1           | PA3/UART2_RX  | I        | Reserved - UART2/LPUART1 Interface (AT Commands and FW Update)                                    |
| 2           | PA2/UART2_TX  | O        | Reserved - UART2/LPUART1 Interface (AT Commands and FW Update)                                    |
| 3           | PA15/PIN_A4   | I/O      | GPIO and ADC                                                                                      |
| 4           | PB6/UART1_TX  | O        | UART1 Interface                                                                                   |
| 5           | PB7/UART1_RX  | I        | UART1 Interface                                                                                   |
| 6           | PA1           | I/O      | GPIO only                                                                                         |
| 7           | PA13/SWDIO    |          | Reserved - SWD debug pin (SWDIO)                                                                  |
| 8           | PA14/SWCLK    |          | Reserved - SWD debug pin (SWCLK)                                                                  |
| 9           | PA12/I2C_SCL  | I/O      | GPIO and I2C (SCL)                                                                                |
| 10          | PA11/I2C_SDA  | I/O      | GPIO and I2C (SDA)                                                                                |
| 11          | GND           |          | Ground connections                                                                                |
| 12          | RF            |          | RF Port (only available on **RAK3172 No-IPEX connector variant**)                                 |
| 13          | PA7/SPI1_MOSI | I/O      | GPIO and SPI (MOSI)                                                                               |
| 14          | PA6/SPI1_MISO | I/O      | GPIO and SPI (MISO)                                                                               |
| 15          | PA5/SPI1_CLK  | I/O      | GPIO and SPI (CLK)                                                                                |
| 16          | PA4/SPI1_NSS  | I/O      | GPIO and SPI (NSS)                                                                                |
| 17          | GND           |          | Ground connections                                                                                |
| 18          | GND           |          | Ground connections                                                                                |
| 19          | PA8           | I/O      | GPIO only                                                                                         |
| 20          | PA9           | I/O      | GPIO only                                                                                         |
| 21          | BOOT0         |          | Boot0 mode enable pin - high active                                                               |
| 22          | RST           |          | MCU Reset (NRST)                                                                                  |
| 23          | GND           |          | Ground connections                                                                                |
| 24          | VDD           |          | VDD - Voltage Supply                                                                              |
| 25          | PA10/PIN_A3   | I/O      | GPIO and ADC                                                                                      |
| 26          | PB2/PIN_A2    | I/O      | GPIO and ADC                                                                                      |
| 27          | PB12          | I/O      | 10 kΩ internally **pulled-up for high freq** variant or **pulled-down for low freq** variant |
| 28          | GND           |          | Ground connections                                                                                |
| 29          | PA0           | I/O      | GPIO only                                                                                         |
| 30          | PB5           | I/O      | GPIO only                                                                                         |
| 31          | PB4/PIN_A1    | I/O      | GPIO and ADC                                                                                      |
| 32          | PB3/PIN_A0    | I/O      | GPIO and ADC                                                                                      |

#### RF Characteristics

The RAK3172 supports two different frequency variations: RAK3172(L) Low Radio Frequency and RAK3172(H) High Radio Frequency.

:::tip NOTE
Performance test and evaluation of RAK3172-T (with TCXO), can be found on the [RAK3172-T TCXO Verification Report](https://downloads.rakwireless.com/LoRa/RAK3172-T/Test-Report/RAK3172_TCXO_Verification_Report%20_V1.2.pdf)
:::

##### Operating Frequencies

| Module | Region | Frequency |
| --- | --- | --- |
| RAK3172(L) | Europe | EU433 |
| RAK3172(L) | China | CN470 |
| RAK3172(H) | Europe | EU868 |
| RAK3172(H) | North America | US915 |
| RAK3172(H) | Australia | AU915 |
| RAK3172(H) | Korea | KR920 |
| RAK3172(H) | Asia | AS923-1/2/3/4 |
| RAK3172(H) | India | IN865 |
| RAK3172(H) | Russia | RU864 |

#### Electrical Characteristics

##### Operating Voltage

| Feature | Minimum | Typical | Maximum |   Unit    |
| :-----: | :-----: | :-----: | :-----: | :-------: |
|   VCC   |   2.0   |   3.3   |   3.6   | Volts (V) |

##### Operating Current

|      Feature      | Condition |               Minimum                | Typical | Maximum | Unit  |
| :---------------: | :-------: | :----------------------------------: | :-----: | :-----: | :---: |
| Operating Current |  TX Mode  | 87 (@ 20 dBm 868 Mhz) |         |         |  mA   |
|                   |  RX Mode  |                 5.22                 |         |         |  mA   |

##### Sleep Current

|       Feature       | Condition | Minimum (2.1 V) | Typical (3.3 V) | Maximum | Unit  |
| :-----------------: | :-------: | :------------------: | :------------------: | :-----: | :---: |
| Current Consumption |   EU868   |          -           |         1.69         |    -    |  μA   |
|                     |   US915   |          -           |         1.69         |    -    |  μA   |
|                     |   CN470   |          -           |         1.69         |    -    |  μA   |

:::tip NOTE
For the reference application schematic of RAK3172 with minimum components requirements, refer to the [RAK3272S Breakout Board Datasheet.](https://docs.rakwireless.com/product-categories/wisduo/rak3272s-breakout-board/datasheet/#schematic-diagram)
:::

#### Mechanical Characteristics

##### Module Dimensions

> **Image:** RAK3172 Physical Dimension

##### Layout Recommendation

> **Image:** RAK3172 Layout

#### Environmental Characteristics

##### Operating Temperature

|  Module   | Minimum | Typical | Maximum |   Unit   |
| :-------: | :-----: | :-----: | :-----: | :------: |
|  RAK3172  |   -20   |   25    |   85    | ° C |
| RAK3172-T |   -40   |   25    |   85    | ° C |

##### Storage Temperature

|       Feature       | Minimum | Typical | Maximum |   Unit   |
| :-----------------: | :-----: | :-----: | :-----: | :------: |
| Storage Temperature |   -40   |         |   85    | ° C |

##### Recommended Reflow Profile

> **Image:** Reflow Profile for RAK3172

Standard conditions for reflow soldering:

- Pre-heating Ramp (A) (Initial temperature: 150° C): **1~2.5° C/sec**
- Soaking Time (T2) (150\~180° C): **60~100 sec**
- Peak Temperature (G): **230~250° C**
- Reflow Time (T3) (> 220° C): **30~60 sec**
- Ramp-up Rate (B): **0~2.5° C/sec**
- Ramp-down Rate (C): **1~3° C/sec**

### Software

Download the latest RAK3172 WisDuo LoRaWAN Module firmware provided below. The RAK3172(L) and RAK3172(H) use the same firmware, and it will automatically detect the variant of the module being used.

The **bin file** contains only the application code. You will need the RAK DFU Tool to upload this file to the module.

The **hex file** contains both the bootloader and the application code. You need to [use STM32CubeProgrammer to upload](https://learn.rakwireless.com/hc/en-us/articles/26687606549911-How-To-Guide-STM32CubeProgrammer-for-RAK-Modules) this.

:::warning
Uploading the **`.hex`** file via STM32CubeProgrammer will erase all configured data on the device.
:::

RAK3172 uses UART2 serial pins to upload the latest firmware.

:::tip NOTE
RAK3172 should automatically go to BOOT mode when the firmware is uploaded via RAK DFU Tool or WisToolBox.

If BOOT mode is not initiated, you can manually send `AT+BOOT` command to start bootloader mode.
:::

### Firmware

|      Model       |                             Version                              |                                             Source                                                                         |
| :--------------: | :--------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------: |
|  RAK3172 (.bin)  |      RUI3 Application Code only (default baudrate = 115200)      |  [Download](https://downloads.rakwireless.com/RUI/RUI3/Image/RAK3172-E_latest.bin)              |
|  RAK3172 (.hex)  | RUI3 Bootloader and Application Code(default baudrate = 115200)  |  [Download](https://downloads.rakwireless.com/RUI/RUI3/Image/RAK3172-E_latest_final.hex)        |
| RAK3172-T (.bin) |      RUI3 Application Code only(default baudrate = 115200)       |  [Download](https://downloads.rakwireless.com/RUI/RUI3/Image/RAK3172-T_latest.bin)              |
| RAK3172-T (.hex) | RUI3 Bootloader and Application Code (default baudrate = 115200) |  [Download](https://downloads.rakwireless.com/RUI/RUI3/Image/RAK3172-T_latest_final.hex)        |
|  RAK3172 (OLD)   |         **DEPRECATED** V1.0.4 (default baudrate = 9600)          |  [Download](https://downloads.rakwireless.com/LoRa/RAK3172/Firmware/RAK3172_Latest_Firmware.zip)|

:::warning
There are RAK3172 devices loaded with old firmware versions which are not based on RUI3 (RAKwireless Unified Interface V3). These devices have v1.0.4 and below.

If the host microcontroller code is based on this old firmware, refer to the [RAK3172 AT Command migration guide](https://learn.rakwireless.com/hc/en-us/articles/26687498449559-AT-Command-Migration-Guide-of-RAK3172-to-RUI3-RAKwireless-Unified-Interface-V3) that explains in detail the few differences between the two AT commands set.
:::

## Models and Bundles

### Ordering Information

| P/N                 | Model      | TCXO                    | Antenna Interface | Frequency                           | SKU    |
| ------------------- | ---------- | ----------------------- | ----------------- | ----------------------------------- | ------ |
| RAK3172-8-SM-NI     | RAK3172    | Without TCXO            | No IPEX           | 8XX MHz for RU864/IN865/EU868       | 305044 |
| RAK3172-9-SM-NI     | RAK3172    | Without TCXO            | No IPEX           | 9XX MHz for US915/AU915/KR920/AS923 | 306041 |
| RAK3172-9-SM-NI     | RAK3172    | Without TCXO            | No IPEX           | AS923-1 Japan                       | 309044 |
| RAK3172-43-SM-NI    | RAK3172    | Without TCXO            | No IPEX           | EU433                               | 301026 |
| RAK3172-47-SM-NI    | RAK3172    | Without TCXO            | No IPEX           | CN470                               | 302033 |
| RAK3172-T-8-SM-NI   | RAK3172-T  | With ±2.5 ppm TCXO | No IPEX           | 8XX MHz for RU864/IN865/EU868       | 305054 |
| RAK3172-T-9-SM-NI   | RAK3172-T  | With ±2.5 ppm TCXO | No IPEX           | 9XX MHz for US915/AU915/KR920/AS923 | 306051 |
| RAK3172-T-9-SM-NI   | RAK3172-T  | With ±2.5 ppm TCXO | No IPEX           | AS923-1 Japan                       | 309054 |
| RAK3172-T-43-SM-NI  | RAK3172-T  | With ±2.5 ppm TCXO | No IPEX           | EU433                               | 301029 |
| RAK3172-T-47-SM-NI  | RAK3172-T  | With ±2.5 ppm TCXO | No IPEX           | CN470                               | 302037 |
| RAK3172-TE-8-SM-NI  | RAK3172-TE | With ±0.5 ppm TCXO | No IPEX           | 8XX MHz for RU864/IN865/EU868       | 305058 |
| RAK3172-TE-9-SM-NI  | RAK3172-TE | With ±0.5 ppm TCXO | No IPEX           | 9XX MHz for US915/AU915/KR920/AS923 | 306055 |
| RAK3172-TE-9-SM-NI  | RAK3172-TE | With ±0.5 ppm TCXO | No IPEX           | AS923-1 Japan                       | 309057 |
| RAK3172-TE-43-SM-NI | RAK3172-TE | With ±0.5 ppm TCXO | No IPEX           | EU433                               | -      |
| RAK3172-TE-47-SM-NI | RAK3172-TE | With ±0.5 ppm TCXO | No IPEX           | CN470                               | -      |
| RAK3172-8-SM-I      | RAK3172    | Without TCXO            | With IPEX         | 8XX MHz for RU864/IN865/EU868       | 305045 |
| RAK3172-9-SM-I      | RAK3172    | Without TCXO            | With IPEX         | 9XX MHz for US915/AU915/KR920/AS923 | 306042 |
| RAK3172-9-SM-I      | RAK3172    | Without TCXO            | With IPEX         | AS923-1 Japan                       | 309045 |
| RAK3172-43-SM-I     | RAK3172    | Without TCXO            | With IPEX         | EU433                               | 301025 |
| RAK3172-47-SM-I     | RAK3172    | Without TCXO            | With IPEX         | CN470                               | 302032 |
| RAK3172-T-8-SM-I    | RAK3172-T  | With ±2.5 ppm TCXO | With IPEX         | 8XX MHz for RU864/IN865/EU868       | 305055 |
| RAK3172-T-9-SM-I    | RAK3172-T  | With ±2.5 ppm TCXO | With IPEX         | 9XX MHz for US915/AU915/KR920/AS923 | 306052 |
| RAK3172-T-9-SM-I    | RAK3172-T  | With ±2.5 ppm TCXO | With IPEX         | AS923-1 Japan                       | 309055 |
| RAK3172-T-43-SM-I   | RAK3172-T  | With ±2.5 ppm TCXO | With IPEX         | EU433                               | 301030 |
| RAK3172-T-47-SM-I   | RAK3172-T  | With ±2.5 ppm TCXO | With IPEX         | CN470                               | 302038 |
| RAK3172-TE-8-SM-I   | RAK3172-TE | With ±0.5 ppm TCXO | With IPEX         | 8XX MHz for RU864/IN865/EU868       | 305057 |
| RAK3172-TE-9-SM-I   | RAK3172-TE | With ±0.5 ppm TCXO | With IPEX         | 9XX MHz for US915/AU915/KR920/AS923 | 306054 |
| RAK3172-TE-9-SM-I   | RAK3172-TE | With ±0.5 ppm TCXO | With IPEX         | AS923-1 Japan                       | 309056 |
| RAK3172-TE-43-SM-I  | RAK3172-TE | With ±0.5 ppm TCXO | With IPEX         | EU433                               | -      |
| RAK3172-TE-47-SM-I  | RAK3172-TE | With ±0.5 ppm TCXO | With IPEX         | CN470                               | -      |

## Certification

### Certifications
- **ANATEL:** https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_ANATEL_Certification.pdf
- **CE:** https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_CE_Certification.pdf
- **FCC:** https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_FCC_Certification.zip
- **ISED:** https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_ISED_Certification.pdf
- **JRL:** https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_JRL_Certfication.pdf
- **KC:** https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_KC_Certification.pdf
- **LORAWAN:** https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_Lora_Alliance_Certification.pdf
- **RCM:** https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_RCM_Certification.pdf
- **REACH:** https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_REACH_Report.pdf
- **ROHS:** https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_RoHS_Report.pdf
- **RSM:** https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_RSM_Certification.pdf
- **UKCA:** https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_UKCA_Certification.pdf
- **WPC:** https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_WPC_Certification.pdf

:::tip Note
For CE and FCC certifications we provide an AT command guide.    
You can find it in our [RUI3 documentation](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/certification-guide) or get it from our [Download Center](https://downloads.rakwireless.com/#RUI/RUI3/Certification%20Guide/).    
::: 

