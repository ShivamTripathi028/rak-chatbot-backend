---
title: RAK811 WisDuo Breakout Board Datasheet
description: Provides comprehensive information about your RAK811 Breakout Board to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/rak811-breakout.png"
keywords:
    - RAK811 Breakout Board
    - wisduo
    - Datasheet
sidebar_label: Datasheet
slug: /product-categories/wisduo/rak811-breakout-board/datasheet/
download: true
---

# RAK811 Breakout Board Datasheet

## Overview

### Description

The **RAK811 Breakout Board** is a compact, low-power, and easy-to-use device featuring long-range LoRa technology with wireless transceiver capabilities. It is built around the RAK811 Stamp Module, mounted on a breakout board with an Xbee form factor and standard 2.00 mm headers.

The RAK811 Breakout Board complies with Class A and Class C of the LoRaWAN 1.0.2 specification. It also supports LoRa Point-to-Point (P2P) communications, enabling the implementation of private LoRa wireless applications. The module's mode and operation can be configured using AT commands via the UART interface. Additionally, the RAK811 Breakout Board features low-power capabilities, making it ideal for battery-powered applications.

### Features

- Based on **Semtech SX1276**.
- **LoRaWAN 1.0.2** specification compliant.
- **Supported bands**: EU433, CN470, IN865, EU868, AU915, US915, KR920, and AS923.
- LoRaWAN Activation by OTAA/ABP.
- LoRa Point-to-Point (P2P) communication.
- Integrates both **SMA** and **iPEX** antenna connectors.
- Xbee form factor with standard 2.00 mm headers.
- Easy to use AT Command Set via UART interface with configurable baud rate.
- Maximum output power 100 mW (20 dBm), adjustable from 5 to 20 dBm.
- High sensitivity at -148 dBm, enabling extremely long range connectivity.
- Long-range - greater than 15 km with optimized antenna.
- Low power consumption: 11 μA on on standby.
- Ultra-Low Power Consumption of 11.9 μA (down to 1.11 μA @ 2.1 V) in sleep mode.
- Multi-channel, dual data buffer (256 bytes each).
- LoRa/FSK/GFSK/OOK modulation, bidirectional two-way communication.
- Long battery life for battery-powered applications.
- LoRa technology is capable of demodulating 20 dB below noise level which significantly improves immunity to interference when combined with integrated forward error correction.
- **Operating temperature**: -30° C ~ 85° C (industrial grade)
- **Storage temperature**: -40° C ~ 85° C (non-condensing)

## Specifications

This section covers the hardware and software specifications of the RAK811 Breakout Board. All discussion presents both versions: RAK811(L) and RAK811(H).

### Overview

The **RAK811 Breakout Board** is shown in **Figure 1** with its corresponding board dimension of **42 mm x 25 mm**. This board weighs at about **0.2 kg**.

> **Image:** RAK811 Breakout Board Dimensions

### Hardware

The hardware specification is divided into six sections, covering the following:

- **Pinouts**: Details the board's pins, their corresponding functions, and diagrams.
- **RF Parameters**: Includes specifications related to radio frequency performance.
- **Electrical Parameters**: Provides information on power requirements and electrical characteristics.
- **Environmental Parameters**: Lists operating conditions such as temperature and humidity ranges.
- **Mechanical Parameters**: Describes the physical dimensions and structural details of the board.
- **Tabular Data**: Summarizes the functionalities and standard values of the RAK811 Breakout Board.

#### Interfaces

| Module                | Interfaces   |
| --------------------- | ------------ |
| RAK811 Breakout Board | UART1, GPIOs |

#### Pin Definition

The RAK811 Breakout Board supports two different frequency variations: **Low Radio Frequency** and **High Radio frequency**.

##### 1. Low Radio Frequency (RAK811(L))

The low radio frequency is applicable to the bandwidth of regions EU433 and CN470. For more information, refer to the [RF Characteristics](#rf-characteristics).

###### Low RF Pin Outline

> **Image:** Board Pinout for RAK811 Breakout Low RF

###### Low RF Pin Definition

| **Pin No.** | **Name**       | **Type** | **Description**                             |
| ----------- | -------------- | -------- | ------------------------------------------- |
| 1           | VCC 3.3 V | P        | Main Power Voltage Source Input             |
| 2           | PA9/UART1_TX   | O        | UART1 Interface (AT Commands and FW Update) |
| 3           | PA10/UART1_RX  | I        | UART1 Interface (AT Commands and FW Update) |
| 4           | PB12/ADC       | I/O      | GPIO and ADC                                |
| 5           | RST            | I        | Reset Trigger Input, Low Active             |
| 6           | PA3/ADC        | I/O      | GPIO and ADC                                |
| 7           | PB5            | I/O      | GPIO only                                   |
| 8           | PA12           | I/O      | GPIO only                                   |
| 9           | PB4            |          | Boot mode GPIO enable pin - high active     |
| 10          | GND            |          | Ground connections                          |
| 11          | PA0/ADC        | I/O      | GPIO and ADC                                |
| 12          | PA1/ADC        | I/O      | GPIO and ADC                                |
| 13          | PA14           |          | SWD Debug Pin (SWCLK)                       |
| 14          | PA13           |          | SWD Debug Pin SWDIO                         |
| 15          | PA11           | I/O      | GPIO only                                   |
| 16          | PB15/ADC       | I/O      | GPIO and ADC                                |
| 17          | PA2/ADC        | I/O      | GPIO and ADC                                |
| 18          | PB13/ADC       | I/O      | GPIO and ADC                                |
| 19          | PA12/ADC       | I/O      | GPIO and ADC                                |
| 20          | PB14/ADC       | I/O      | GPIO and ADC                                |

##### 2. High Radio Frequency (RAK811(H))

The high radio frequency hardware supports the regions of EU868, US915, AU915, KR920, AS923, and IN865. For more information, refer to the [RF Characteristics](#rf-characteristics).

###### High RF Pin Outline

> **Image:** Board Pinout for RAK811 Breakout High RF

###### High RF Pin Definition

| **Pin No.** | **Name**       | **Type** | **Description**                             |
| ----------- | -------------- | -------- | ------------------------------------------- |
| 1           | VCC 3.3 V | P        | Main Power Voltage Source Input             |
| 2           | PA9/UART1_TX   | O        | UART1 Interface (AT Commands and FW Update) |
| 3           | PA10/UART1_RX  | I        | UART1 Interface (AT Commands and FW Update) |
| 4           | PB12/ADC       | I/O      | GPIO and ADC                                |
| 5           | RST            | I        | Reset Trigger Input, Low Active             |
| 6           | PB3            | I/O      | GPIO only                                   |
| 7           | PB5            | I/O      | GPIO only                                   |
| 8           | PA15           | I/O      | GPIO only                                   |
| 9           | BOOT0          |          | Boot mode GPIO enable pin - high active     |
| 10          | GND            |          | Ground connections                          |
| 11          | PA0/ADC        | I/O      | GPIO and ADC                                |
| 12          | PA1/ADC        | I/O      | GPIO and ADC                                |
| 13          | PA14           |          | SWD Debug Pin (SWCLK)                       |
| 14          | PA13           |          | SWD Debug Pin (SWDIO)                       |
| 15          | PB4            | I/O      | GPIO only                                   |
| 16          | PB15/ADC       | I/O      | GPIO and ADC                                |
| 17          | PA2/ADC        | I/O      | GPIO and ADC                                |
| 18          | PA8            | I/O      | GPIO only                                   |
| 19          | PA12           | I/O      | GPIO only                                   |
| 20          | PB14/ADC       | I/O      | GPIO and ADC                                |

#### RF Characteristics

##### Operating Frequencies

| Module    | Region        | Frequency |
| --------- | ------------- | --------- |
| RAK811(L) | Europe        | EU433     |
|           | China         | CN470     |
| RAK811(H) | Europe        | EU868     |
|           | North America | US915     |
|           | Australia     | AU915     |
|           | Korea         | KR920     |
|           | Asia          | AS923     |
|           | India         | IN865     |

| Feature        | Condition | Minimum | Typical | Maximum | Unit |
| -------------- | --------- | ------- | ------- | ------- | ---- |
| Transmit       | TX Power  |         | 14      | 20      | dBm  |
| RX Sensitivity | RSSI      | -130    |         |         | dBm  |
|                | SNR       | -15     |         |         | dB   |

#### Electrical Characteristics

##### Schematic Diagram

> **Image:** RAK811 Schematic Diagram

> **Image:** Reference Design

##### Operating Voltage

| Feature | Minimum | Typical | Maximum | Unit      |
| ------- | ------- | ------- | ------- | --------- |
| VCC     | 2.1     | 3.3     | 3.45    | Volts (V) |

##### Current Consumption

| Feature             | Condition | Minimum                 | Typical | Maximum | Unit |
| ------------------- | --------- | ----------------------- | ------- | ------- | ---- |
| Current Consumption | TX Power  | 30 (@ 14 dBm) |         |         | mA   |
|                     | RX Mode   | 5.5                     |         |         | mA   |

##### Sleep Current

| Feature             | Condition | Minimum (2.1V) | Typical (3.3V) | Maximum | Unit |
| ------------------- | --------- | -------------- | -------------- | ------- | ---- |
| Current Consumption | EU868     | 8.37           | 11.9           |         | μA   |
|                     | US915     | 1.11           | 11.8           |         | μA   |
|                     | CN470     | 1.65           | 3.07           |         | μA   |

#### Mechanical Characteristics

##### Module Dimensions

> **Image:** RAK811 Physical Dimension

#### Environmental Characteristics

##### Operating Temperature

| Feature               | Minimum | Typical | Maximum | Unit |
| --------------------- | ------- | ------- | ------- | ---- |
| Operating Temperature | -30     | 25      | 85      | °C   |

##### Storage Temperature

| Feature             | Minimum | Typical | Maximum | Unit |
| ------------------- | ------- | ------- | ------- | ---- |
| Storage Temperature | -40     |         | 85      | °C   |

### Software

Download the latest firmware of the RAK811 Breakout Board — both in low and high frequency — provided in the table below.

:::tip NOTE

The **bin file** contains the application code only, and you need the RAK DFU Tool to upload this file to the module.

The **hex file** contains both the bootloader and the application code. You need to use STM32CubeProgrammer to upload this.

:::

#### Firmware/OS

| Model     | Version     | Source                                                                                                        |
| --------- | ----------- | ------------------------------------------------------------------------------------------------------------- |
| RAK811(L) | V3.0.0.14.L | [Download](https://downloads.rakwireless.com/LoRa/RAK811-BreakoutBoard/Firmware/RAK811_L_Latest_Firmware.zip) |
| RAK811(H) | V3.0.0.14.H | [Download](https://downloads.rakwireless.com/LoRa/RAK811-BreakoutBoard/Firmware/RAK811_H_Latest_Firmware.zip) |

## Certification

### Certifications
- **CE:** https://downloads.rakwireless.com/LoRa/RAK811/Certification_Report/RAK811_CE_Certification.zip
- **FCC:** https://downloads.rakwireless.com/LoRa/RAK811/Certification_Report/RAK811_FCC_Certification.zip
- **KC:** https://downloads.rakwireless.com/LoRa/RAK811/Certification_Report/RAK811_KC_Certification.zip
- **MIC:** https://downloads.rakwireless.com/LoRa/RAK811/Certification_Report/RAK811_MIC_Certification.zip
- **ROHS:** https://downloads.rakwireless.com/LoRa/RAK811/Certification_Report/RAK811_RoHS_Report.zip

