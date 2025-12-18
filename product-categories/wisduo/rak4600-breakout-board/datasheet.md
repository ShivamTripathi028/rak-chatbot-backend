---
title: RAK4600 WisDuo Breakout Board Datasheet
description: Provides comprehensive information about your RAK4600 Breakout Board to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisduo/rak4600-breakout-board/rak4600-breakout.png"
keywords:
    - datasheet
    - wisduo
    - RAK4600 Breakout Board
sidebar_label: Datasheet
slug: /product-categories/wisduo/rak4600-breakout-board/datasheet/
download: true
---

# RAK4600 Breakout Board Datasheet

## Overview

### Description

The **RAK4600 Breakout Board** is specifically designed to provide easy access to the board's pins, simplifying development and testing. The breakout board's form factor converts the RAK4600 stamp module pinout to 2.54 mm headers.

The board itself has the RAK4600 at its core, integrating an **nRF52832 MCU** and an **SX1276 LoRa chip**. It has an ultra-low power consumption of 13.3 μA (down to 11.2 μA @ 2.0 V) in sleep mode, and high LoRa output power (20 dBm) in work mode. Its BLE output power is up to 4 dBm.

The board complies with **LoRaWAN 1.0.2 specification**. It also supports LoRa Point-to-Point (P2P) communication.

The RF communication capabilities of the board (LoRa + BLE) make it ideal for various IoT applications. These include home and building automation, sensor networks, and personal area networks for health and fitness monitoring.

### Features

- LoRa module for Smart City, Smart Agriculture, Smart Industry
- I/O ports: **UART/I2C/GPIO** (optional NFC interface)
- Frequency range: **863–923 MHz** (entire LoRa high band spectrum)
- Low-Power Wireless Systems with **7.8 kHz** to **500 kHz** Bandwidth
- LoRa Tx power up to **20 dBm**
- BLE 5.0 (Tx power -20 dBm to +4 dBm in 4 dB steps)
- Serial Wire Debug (SWD) interface
- Ultra-Low Power Consumption of 13.3 μA (down to 11.2 μA @ 2.0 V) in sleep mode
- Supply voltage: **2.0 V ~ 3.6 V**
- Temperature range: **-40° C ~ +85° C**

## Specifications

### Overview

The RAK4600 Breakout Board is shown in **Figure 1**, which displays the top view of the module.

> **Image:** RAK4600 Breakout Board Illustration

### Hardware

The hardware specification is categorized into five (5) parts. It discusses the interfacing, pinouts, and its corresponding functions and diagrams. It also covers the RF and electrical parameters that include the tabular data of the functionalities and standard values of the RAK4600 Breakout Board.

#### Interfaces

##### SWD Programming Interface

Connect the four debug/programming SWD pins of the board to the RAKDAP1 adapter:

1. **VDD**
2. **SWDIO**
3. **SWCLK**
4. **GND**

:::tip NOTE
For the aforementioned reason, it is best you leave these exposed for programming purposes and not to remap them as GPIOs.
:::

##### UART Port

There is one UART interface on the RAK4600 Breakout Board:

- **USART1** – recommended for debugging/firmware update

##### I2C interface

The following pins are intended for I2C (_require 10k resistance pull-up_):

- **I2C_SCL**
- **I2C_SDA**

##### RF interface

Both are utilizing an I-PEX connector, where one is for the LoRa antenna and the other for the BLE.

##### NFC interface

Two physical pins can be configured either as NFC antenna pins (factory default) or as GPIOs. When configured as NFC antenna pins, the GPIOs on those pins will automatically be set to DISABLE state and a protection circuit will be enabled to prevent the chip from being damaged in the presence of a strong NFC field. The protection circuit will short the two pins together if the voltage difference exceeds approximately 2 V.

#### Pin Definition

**Figure 2** shows the pinout of the RAK4600 Breakout Board:

> **Image:** RAK4600 Breakout Board Pinout

The pin definitions of the RAK4600 Breakout Board are shown in the following tables below:

##### J7 Pin Definitions

| **Pin** | **Name** | **I/O** | **Description**                              | **Alternate functions**                                 |
| :-----: | :------: | :-----: | :------------------------------------------: | :-----------------------------------------------------: |
| 1       | P0.18    | I/O     | GPIO NRF52832 P0.18                          | GPIO, Single wire output, Trace port output             |
| 2       | P0.19    | I/O     | GPIO NRF52832 P0.19                          | GPIO                                                    |
| 3       | NFC1     | I/O     | NFC antenna connection GPIO (NRF52832 P0.09) | NFC antenna connection
GPIO                          |
| 4       | NFC2     | I/O     | NFC antenna connection GPIO (NRF52832 P0.10) | NFC antenna connection
GPIO                          |
| 5       | SWDIO    | I/O     | SWD Programming                              | Serial wire debug I/O for debug and programming         |
| 6       | SWCLK    | I/O     | SWD Programming                              | Serial wire debug clock input for debug and programming |
| 7       | I2C_SCL  | I/O     | I2C (GPIO NRF52832 P0.12)                    | GPIO                                                    |
| 8       | I2C_SDA  | I/O     | I2C (GPIO NRF52832 P0.13)                    | GPIO                                                    |

##### J8 Pin Definitions

| **Pin** | **Name**  | **I/O** | **Description**                 | **Alternate Functions**                    |
| :-----: | :-------: | :-----: | :-----------------------------: | :----------------------------------------: |
| 1       | VDD       |         | DC 3V3                          | Supply voltage 2.0~3.3 V<sub>DC</sub> |
| 2       | USART1_TX | I/O     | USART1_TX (GPIO NRF52832 P0.23) | GPIO                                       |
| 3       | USART1_RX | I/O     | USART1_RX (GPIO NRF52832 P0.22) | GPIO                                       |
| 4       | GND       |         | Ground                          |                                            |
| 5       | MCU_NRST  | I/O     | MCU reset (GPIO NRF52832 P0.03) | GPIO, Configurable as reset pin            |
| 6       | Reserved  | I/O     | Reserved (GPIO NRF52832 P0.14)  | GPIO, Trace port output                    |
| 7       | Reserved  | I/O     | Reserved (GPIO NRF52832 P0.17)  | GPIO                                       |
| 8       | GND       | I/O     | Ground                          |                                            |

##### J4 Pin Definitions

| **Pin** | **Name** | **I/O** | **Description** | **Alternate Functions**                    |
| :-----: | :------: | :-----: | :-------------: | :----------------------------------------: |
| 1       | GND      |         | Ground          |                                            |
| 2       | VDD      |         | DC 3V3          | Supply voltage 2.0~3.3 V<sub>DC</sub> |

##### LoRa Transceiver IC Connection to RAK4600 Breakout Board

| **LoRa IC Pin** | **NRF52832 IO pin** |
| :-------------: | :-----------------: |
|      DIO0       |        P0.27        |
|      DIO1       |        P0.28        |
|      DIO2       |        P0.29        |
|      DIO3       |        P0.30        |
|      DIO4       |        P0.31        |
|      DIO5       |         NC          |
|    SPI1_CLK     |        P0.07        |
|    SPI1_MISO    |        P0.06        |
|    SPI1_MOSI    |        P0.05        |
|    SPI1_NSS     |        P0.04        |
|      VCTL1      |        P0.16        |
|      VCTL2      |        P0.15        |

:::tip NOTE
The LoRa Transceiver IC Connection pins are not exposed.
:::

##### RF Switch Control Logic Table

| **LoRa Mode** | **VCTL1 GPIO** | **VCTL2 GPIO** |
| :-----------: | :------------: | :------------: |
| TX mode       |       H        |       L        |
| RX mode       |       L        |       H        |

:::tip Logic Level
H level (1.8 V - 3.30 V)

L level (0 V)
:::

#### RF Characteristics

##### Operating Frequencies

The RAK4600 Breakout Board supports the following LoRa bands:

| **Module**      | **Region**    | **Frequency** |
| :-------------: | :-----------: | :-----------: |
| **RAK4600 (H)** | Russia        | RU864         |
|                 | India         | IN865         |
|                 | Europe        | EU868         |
|                 | North America | US915         |
|                 | Australia     | AU915         |
|                 | Korea         | KR920         |
|                 | Asia          | AS923         |

#### Electrical Characteristics

##### Power Consumption

The table below shows the power consumption of the RAK4600 Breakout Board:

| **Item**                        | **Power Consumption** | **Condition**                  |
| :-----------------------------: | :-------------------: | :----------------------------: |
| Tx mode LoRa @20 dBm       | 125 mA           | LoRa @ PA_BOOST & BT sleep     |
| Tx mode LoRa @17 dBm       | 92 mA            | LoRa @ PA_BOOST & BT sleep     |
| Tx mode BT @4 dBm          | 9 mA             | BT Tx mode & LoRa sleep        |
| Rx mode LoRa
@37.5 Kbps | 17 mA            | LoRa @ Receive mode & BT sleep |
| Rx mode BT @2 Mbps         | 11.5 mA          | BT Rx mode & LoRa sleep        |

##### Sleep Current

| Feature             | Condition | Minimum (2.0 V) | Typical (3.3 V) | Maximum | Unit |
| :-----------------: | :-------: | :------------------: | :------------------: | :-----: | :--: |
| Current Consumption | EU868     | 11.2                 | 13.3                 |         | μA   |
|                     | US915     | 11.5                 | 12.5                 |         | μA   |

#### Schematic Diagram

> **Image:** RAK4600 Breakout Board Schematic

### Software

Download the latest firmware of the RAK4600 Breakout Board in the table provided.

#### Firmware

| Model   | Version  | Source                                                                                          |
| :-----: | :------: | :---------------------------------------------------------------------------------------------: |
| RAK4600 | 3.4.0.14 | <a href="https://downloads.rakwireless.com/LoRa/RAK4600/Firmware/RAK4600_Latest_Firmware.zip" target="_blank">Download</a> |

## Certification

### Certifications
- **CE:** https://downloads.rakwireless.com/LoRa/RAK4270/Certification-Report/RAK4270_CE_Certification.zip
- **FCC:** https://downloads.rakwireless.com/LoRa/RAK4270/Certification-Report/RAK4270_FCC_Certification.zip

