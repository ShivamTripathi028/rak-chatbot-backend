---
slug: /product-categories/wistrio/rak815/datasheet/
title: RAK815 WisTrio LPWAN Tracker Datasheet
description: Provides comprehensive information about your RAK815 WisTrio LPWAN Tracker to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wistrio/rak815/rak815.png"
keywords:
    - wistrio
    - datasheet
    - rak815
    - lpwan
    - tracker
    - lorawan
sidebar_label: Datasheet
---

# RAK815 WisTrio LPWAN Tracker Datasheet

## Overview

### Description

**RAK815 WisTrio LPWAN Tracker** is a wireless remote solution based on the RAK813 + GPS + MEMS + HT+LCD design. It integrates the latest LoRaWAN 1.0.2 protocol and Bluetooth 5.0, supporting the LoRaWAN working mode and Bluetooth transparent transmission up to 300 meters.

RAK815 (RAK813 BreakBoard) has a built-in GPS, acceleration, temperature, and humidity sensors expanded I2C LCD interface. A case applications are provided that can configure LoRaWAN parameters using Bluetooth, display sensor data using LCD, and upload sensor data to the LoRaWAN network. The board is equipped with three customizable buttons and two customizable LEDs, allowing users to implement their ideas with open-source code available on our **[Github Repository](https://github.com/RAKWireless/RAK813-BreakBoard).**

The board also supports battery-powered products, which greatly expand the product application scenarios. It is designed with a function to enter the low-power mode when the device is detected to be stationary to ensure battery life. The device also supports RAK831 + Ri3 gateway to use. You can graphically display the various data of the sensor in the Cayenne platform and can also support the real-time observation of sensor data on the phone.

Overall, this LoRa device has various functionalities designed in a single board that could help you develop your own LoRa projects.

### Features

- Based on Semtech SX1276 LoRaWAN Version V1.0.2
- Supports NRF52832 Bluetooth Version 5.0
- Equipped with U-Blox GPS
- Supports both ABP and OTAA activation
- Dedicated battery connector
- Micro USB interface for charging and configuration
- Equipped with MEMS and HT sensors + I2C LCD expansion
- Operation temperature: -20 ºC ~ 60 ºC

## Specifications

### Overview

The overview shows the RAK815 board and its block diagram. It shows the internal structure of the board which is composed of Semtech SX1276 and NRF52832.

#### Board Overview

**RAK815 WisTrio LPWAN Tracker** has outer dimensions of **74 mm x 43 mm 17 mm** including the Antenna interface.

> **Image:** RAK815 Breakout Board Dimensions

#### Block Diagram

Shown below is the System Diagram of the RAK815 Breakout Board.

> **Image:** RAK815 System Diagram

### Hardware

The hardware specification is categorized into three parts. It discusses the interfacing, pinouts, and their corresponding functions and diagrams of the board. It also covers the LoRaWAN frequency parameters necessary for the device setup.

#### Pin Definition

> **Image:** RAK815 Interface

:::tip NOTE
The pin numbers in the succeeding tables are sorted from top to bottom, as shown in **Figure 4**.
:::

##### SWD Debug Interface

> **Image:** RAK815 SWD Debug Interface

|  Pin  |    Name    | Description                                            |
| :---: | :--------: | ------------------------------------------------------ |
|   1   |   VCC3.3   | 3.3 V Power Supply                                |
|   2   |   SWDIO    | SWD Interface data pin for NRF52832                    |
|   3   |   SWDCLK   | SWD Interface clock pin for NRF52832                   |
|   4   | P0.21_NRST | P0.21 for NRF52832, can be used as Reset pin (Button3) |
|   5   |    GND     | Ground                                                 |

##### UART Switch Interface

> **Image:** RAK815 UART Switch Interface

|  Pin  |  Name   |                      Description                       |
| :---: | :-----: | :----------------------------------------------------: |
|   1   | GPS_TXD |              UART TXD pin for GPS module               |
|   2   | GPS_RXD |              UART RXD pin for GPS module               |
|   3   |  P0.28  |          P0.28 for NRF52832, Used as UART RXD          |
|   4   |  P0.29  |          P0.29 for NRF52832, Used as UART TXD          |
|   5   |   TXD   | The CP2102 converts the USB to the TXD pin of the UART |
|   6   |   RXD   | The CP2102 converts the USB to the RXD pin of the UART |

##### GPS Module Expansion

> **Image:** RAK815 GPS Module Expansion

|  Pin  |  Name   | Description                                        |
| :---: | :-----: | -------------------------------------------------- |
|   1   | VCC3.3  | 3.3 V Power Supply                            |
|   2   |   GND   | Ground                                             |
|   3   | GPS_TXD | UART TXD Pin for GPS Module                        |
|   4   | GPS_RXD | UART RXD Pin for GPS Module                        |
|   5   |  P0.30  | P0.30 for NRF52832, used to control GPS module PPS |

##### Reserved I2C Interface of the LCD

> **Image:** RAK815 Reserved I2C Interface

|  Pin  |  Name  | Description             |
| :---: | :----: | ----------------------- |
|   1   |  GND   | Ground                  |
|   2   | VCC3.3 | 3.3 V Power Supply |
|   3   |  SCL   | I2C SCL Clock Line      |
|   4   |  SDA   | I2C SDA Data Line       |

##### P1 and P3 Interface PINOUT

> **Image:** RAK815 P1 and P3 Pinout

##### Extension Interface P1

|  Pin  |  Name  | Description                                               |
| :---: | :----: | --------------------------------------------------------- |
|   1   |  GND   | Ground                                                    |
|   2   | P0.24  | P0.24 for NRF52832, used to control the expansion Button2 |
|   3   | P0.25  | P0.25 for NRF52832, used to control the expansion LED6    |
|   4   | P0.26  | P0.26 for NRF52832, used to control the expansion LED7    |
|   5   | P0.27  | P0.27 for NRF52832, used to control the expansion Button1 |
|   6   | P0.28  | P0.28 for NRF52832, used as UART RXD                      |
|   7   | P0.29  | P0.29 for NRF52832, used as UART TXD                      |
|   8   | P0.30  | P0.30 for NRF52832, used to control GPS module PPS        |
|   9   | P0.31  | P0.31 for NRF52832, used to control GPS module power      |
|  10   |  GND   | Ground                                                    |
|  11   |  GND   | Ground                                                    |
|  12   |  GND   | Ground                                                    |
|  13   | VCC3.3 | 3.3 V Power Supply                                   |
|  14   | VCC3.3 | 3.3 V Power Supply                                   |

##### Extension Interface P3

|  Pin  |    Name    | Description                                              |
| :---: | :--------: | -------------------------------------------------------- |
|   1   |    GND     | Ground                                                   |
|   2   |   SWDIO    | SWD Interface data pin for NRF52832                      |
|   3   |   SWDCLK   | SWD Interface clock pin for NRF52832                     |
|   4   |   P0.20    | P0.20 for NRF52832                                       |
|   5   |   P0.19    | P0.19 for NRF52832                                       |
|   6   |   P0.18    | P0.18 for NRF52832                                       |
|   7   |   P0.17    | P0.17 for NRF52832                                       |
|   8   |   P0.16    | P0.16 for NRF52832, used as I2C SCL                      |
|   9   |   P0.15    | P0.15 for NRF52832, used as I2C SDA                      |
|  10   |    GND     | Ground                                                   |
|  11   | P0.21_NRST | P0.21 for NRF52832, can be used as Reset pin (Button3)   |
|  12   |   P0.04    | P0.04 for NRF52832, used to control LIS3DH module INT1   |
|  13   |   P0.03    | P0.03 for NRF52832, used to control LIS3DH module INT2   |
|  14   |   P0.02    | P0.02 for NRF52832, used as ADC to detect battery charge |

#### RF Characteristics

##### Operating Frequencies

The board supports the following LoRaWAN frequency channels shown in the table below. The frequency parameter is easy to configure when configuring the device setup.

|    Region     | Frequency (MHz) |
| :-----------: | :-------------: |
|    Europe     |      EU868      |
| North America |      US915      |
|   Australia   |      AU915      |
|     Asia      |      AS923      |
|     India     |      IN865      |
|     Korea     |      KR920      |

#### Schematic Diagram

> **Image:** GPS-MAX 7Q Schematic Diagram

> **Image:** USB & UART and I2C with the GPS Module Schematic Diagram

> **Image:** LoRa BLE Schematic Diagram

> **Image:** U4, U8, and U6 Schematic Interface

### Firmware

Download the latest firmware of RAK813 WisTrio in the table provided below.

| Model                         | Source                                                       |
| ----------------------------- | ------------------------------------------------------------ |
| RAK815(RAK813 Breakout Board) | [Download](https://github.com/RAKWireless/RAK813-BreakBoard) |

## Models / Bundles

### Ordering Information

| Product                    | Description                                                          | Activation |
| -------------------------- | -------------------------------------------------------------------- | ---------- |
| RAK815 (RAK813 BreakBoard) | LoRaWAN Region Support EU868 / US915 / AS923 / AU915 / KR920 / IN865 | OTAA / ABP |

