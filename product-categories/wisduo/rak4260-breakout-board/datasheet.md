---
title: RAK4260 WisDuo Breakout Board Datasheet
description: Provides comprehensive information about your RAK4260 Breakout Board to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/rak4260-breakout.png"
keywords:
  - datasheet
  - RAK4260 Breakout Board
  - wisduo
sidebar_label: Datasheet
slug: /product-categories/wisduo/rak4260-breakout-board/datasheet/
download: true
---

# RAK4260 WisDuo Breakout Board Datasheet

## Overview

### Description

The **RAK4260 Breakout Board** is designed to provide easy access to the board's pins, simplifying development and testing. Its breakout board form factor transfers the RAK4260 stamp module pinout to 2.54 mm headers, making debugging more convenient for developers.

The board itself has the RAK4260 at its core, which is a module that utilizes the **ATSAMR34J18B SIP**. This high level of integration allows for outstanding performance: 860 nA in sleep mode and LoRa TX Power of up to 20 dBm.

A key feature of this Breakout Board is the **ATECC608A Cryptographic Co-Processor**, which provides secure hardware-based key storage. This sets the board apart from the RAK4200 and RAK4600, adding an extra layer of security to future-proof your platform.

The board complies with LoRaWAN 1.0.2 protocols. It also supports LoRa Point-to-Point (P2P)communication.

The board's low-power, long-range LoRa communication capabilities make it ideal for various IoT applications, including home automation, sensor networks, building automation, and personal area networks such as health and fitness sensors and monitors.

### Features

- LoRa module for Smart City, Smart Agriculture, Smart Industry
- I/O ports: **UART/I2C/SPI/ADC**
- Frequency range: 863–923 MHz (entire LoRa high band spectrum)
- Low-Power Wireless Systems with 7.8 kHz to 500 kHz Bandwidth
- LoRa Tx power up to **20 dBm**
- Ultra-Low Power Consumption **860 nA in sleep mode**
- Core: **ARM 32-bit Cortex – M0+** with MPU
- Up to 256 KB flash memory with ECC
- 32 KB RAM
- 6 KB of data EEPROM with ECC
- **ATECC608A** cryptographic core
- Supply voltage: **2.0 V ~ 3.6 V**
- Temperature range: **-40° C ~ +85° C**

## Specifications

### Overview

**Figures 1 and 2** show the RAK4260 Breakout Board, highlighting the top and back views of the board, respectively.

> **Image:** RAK4260 Breakout Board Top View

> **Image:** RAK4260 Breakout Board Bottom View

### Hardware

The hardware specification is categorized into five (5) parts. It discusses the interfacing, pinouts and its corresponding functions and diagrams. It also covers the RF and electrical parameters that include the tabular data of the functionalities and standard values of the RAK4260 Breakout Board.

#### Interfaces

##### SWD Programming Interface

When programming via a DAPLink tool, it is required to have all of the following four (4) pins connected to your DAPLink tool:

1. **3V3**
2. **SWDIO**
3. **SWCLK**
4. **GND**

:::tip NOTE
It is recommended to leave these pins exposed for programming purposes and avoid remapping them as GPIOs.
:::

##### UART Port

There are two UART interfaces on the RAK4200 Breakout Board:

- **UART1** – the default interface
- **UART3** – reserved, can also act as GPIOs.

##### I2C Interface

**I2C_SCL** and **I2C_SDA** are connected to the ATECC608A crypto chip for the purpose of developing cryptographic applications: network end-point key management and exchange small message and PII data encryption, secure boot and protected download, ecosystem control, and anti-cloning.

##### RF Interface

**J4** is soldered to the antenna connector. Depending on your choice it can come with either SMA or IPEX style connector. Make sure to select the one you need when ordering.

#### Pin Definition

> **Image:** RAK4260 Breakout Board Pinout

The tables below show the pin definition of the RAK4260 Breakout Board:

##### J5 Pin Definitions

| Pin | Name     | I/O | Description                     | Alternate Functions                   |
| :-: | :------: | :-: | :-----------------------------: | :-----------------------------------: |
| 1   | UART3_RX | I   | UART3_RX (ATSAMR34J18B PA18)    | EIC/PTC/TC/AC/CCL/SERCOM1/SERCOM3     |
| 2   | UART3_TX | O   | UART3_TX (ATSAMR34J18B PA19)    | EIC/PTC/TC/AC/CCL/SERCOM1/SERCOM3     |
| 3   | GPIO     | I/O | GPIO (ATSAMR34J18B PA06)        | EIC/RSTC/ADC/PTC/OPAMP/TC/CCL/SERCOM0 |
| 4   | GPIO     | I/O | GPIO (ATSAMR34J18B PA07)        | EIC/RSTC/ADC/OPAMP/TC/CCL/SERCOM0     |
| 5   | GPIO     | I/O | GPIO (ATSAMR34J18B PA08)        | ADC/PTC/TC/CCL/SERCOM0/SERCOM2        |
| 6   | GPIO     | I/O | GPIO (ATSAMR34J18B PA09)        | EIC/ADC/PTC/TC/CCL/SERCOM0/SERCOM2    |
| 7   | SWDIO    | I/O | Programming (ATSAMR34J18B PA30) | -                                     |
| 8   | SWCLK    | I/O | Programming (ATSAMR34J18B PA31) | -                                     |

##### J6 Pin Definitions

| Pin | Name     | I/O | Description                       | Alternate Functions                        |
| :-: | :------: | :-: | :-------------------------------: | :----------------------------------------: |
| 1   | UART1_TX | O   | UART1_RX (ATSAMR34J18B PA04)      | EIC/RSTC/VREFB/ADC/AC/OPAMP/TC/CCL/SERCOM0 |
| 2   | UART1_RX | I   | UART1_RX (ATSAMR34J18B PA05)      | EIC/RSTC/ADC/AC/OPAMP/TC/CCL/SERCOM0       |
| 3   | GPIO     | I/O | GPIO (ATSAMR34J18B PA14)          | EIC/TC/GCLK/SERCOM2/SERCOM4                |
| 4   | RST      | -   | MCU RESET                         | -                                          |
| 5   | SPI_MISO | I/O | SPI Interface (ATSAMR34J18B PB02) | EIC/ADC/SERCOM5/TC/SUPC/CCL                |
| 6   | SPI_CLK  | I/O | SPI Interface (ATSAMR34J18B PB23) | EIC/SERCOM5/TC/GCLK/CCL                    |
| 7   | SPI_CS   | I/O | SPI Interface (ATSAMR34J18B PA22) | EIC/PTC/TC/AC/CCL/SERCOM3/SERCOM5          |
| 8   | SPI_MOSI | I/O | SPI Interface (ATSAMR34J18B PA23) | EIC/PTC/TC/AC/CCL/GCLK/SERCOM3/SERCOM5     |

##### J11 Pin Definitions

| Pin | Name  | I/O | Description                       | Alternate Functions               |
| :-: | :---: | :-: | :-------------------------------: | :-------------------------------: |
| 1   | USB_N | I/O | USB Interface (ATSAMR34J18B PA24) | EIC/SERCOM3/SERCOM5/TC/USB_DM/CCL |
| 2   | USB_P | I/O | USB Interface (ATSAMR34J18B PA24) | EIC/SERCOM3/SERCOM5/TC/USB_DP/CCL |

##### J12 Pin Definitions

| Pin | Name    | I/O | Description                       | Alternate Functions                 |
| :-: | :-----: | :-: | :-------------------------------: | :---------------------------------: |
| 1   | I2C_SDA | I/O | I2C Interface (ATSAMR34J18B PA16) | EIC/PTC/TC/GCLK/CCL/SERCOM1/SERCOM3 |
| 2   | I2C_SCL | I/O | I2C Interface (ATSAMR34J18B PA17) | EIC/PTC/TC/GCLK/CCL/SERCOM1/SERCOM3 |

##### J13 Pin Definitions

| Pin | Name | I/O | Description | Alternate Functions                    |
| :-: | :--: | :-: | :---------: | :------------------------------------: |
| 1   | GND  |     | Ground      | GND                                    |
| 2   | VDD  |     | DC3V3       | Supply voltage 2.0 V ~ 3.3 V |

##### J14 Pin Definitions

| Pin | Name | I/O | Description | Alternate Functions                    |
| :-: | :--: | :-: | :---------: | :------------------------------------: |
| 1   | GND  |     | Ground      | GND                                    |
| 2   | VDD  |     | DC3V3       | Supply voltage 2.0 V ~ 3.3 V |

#### RF Characteristics

##### Operating Frequencies

The RAK4260 Breakout Board supports the following LoRa bands:

| Module | Region | Frequency (MHz) |
| --- | --- | --- |
| RAK4260(H) | Russia | RU864 |
| RAK4260(H) | India | IN865 |
| RAK4260(H) | Europe | EU868 |
| RAK4260(H) | North America | US915 |
| RAK4260(H) | Australia | AU915 |
| RAK4260(H) | Korea | KR920 |
| RAK4260(H) | Asia | AS923 |

#### Electrical Characteristics

##### Power Consumption

| Item                         | Power Consumption      | Condition                  |
| :--------------------------: | :--------------------: | :------------------------: |
| Tx mode LoRa @20 dBm    | 126.3 mA          | PA_BOOST V=3.3 V      |
| Tx mode LoRa @17 dBm    | 95.6 mA           | PA_BOOST V=3.3 V      |
| Tx mode LoRa @14 dBm    | 33.1 mA (typical) | RFO_HF V=3.3 V        |
| Rx mode LoRa @37.5 Kbps | 13.6 mA           | -                          |
| Sleep mode                   | 860 nA            | Backup Mode V = 3.3 V |

##### Schematic Diagram

> **Image:** RAK4260 Breakout Board Schematic Diagram

#### Mechanical Characteristics

> **Image:** RAK4260 Mechanical Dimensions

### Software

Download the latest firmware of the RAK4260 Breakout Board in the table provided.

#### Firmware

| Model   | Source                                                                                          |
| :-----: | :---------------------------------------------------------------------------------------------: |
| RAK4260 | <a href="https://downloads.rakwireless.com/LoRa/RAK4260/Firmware/RAK4260_Latest_Firmware.rar" target="_blank">Download</a> |

## Certification

### Certifications
- **CE:** https://downloads.rakwireless.com/LoRa/RAK4260/Certification-Report/RAK4260H_CE_Certification.zip
- **FCC:** https://downloads.rakwireless.com/LoRa/RAK4260/Certification-Report/RAK4260H_FCC_Certification.zip

