---
title: RAK3244 BastWAN Breakout Board Datasheet
description: Provides comprehensive information about your RAK3244 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisduo/bastwan/bastwan.png
keywords:
  - datasheet
  - wisduo
  - RAK3244
  - BastWAN
sidebar_label: Datasheet
slug: /product-categories/wisduo/bastwan/datasheet/
download: true
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK3244 BastWAN Breakout Board Datasheet

## Overview

### Description

The **RAK3244 BastWAN Breakout Board** is designed to be compatible with the **Feather format** while leveraging the capabilities of the RAK4260 module. At its core, the board features the RAK4260, a module built around the ATSAMR34J18B SiP. This high level of integration delivers exceptional performance, including LoRa TX power of up to 20&nbsp;dBm.

A key feature of this breakout board is the ATECC606A **cryptographic co-processor**, which provides secure, hardware-based key storage. This sets the RAK3244 BastWAN apart from the RAK4200 and RAK4600 by adding an extra layer of security to future-proof your platform.

The board complies with LoRaWAN 1.0.2 specification, and it also supports LoRa P2P Point-to-Point communication. The low power, long-range LoRa communication capabilities of the board make it suitable for a variety of applications in the IoT field such as home automation, sensor networks, building automation, and personal area networks applications such as health/fitness sensors and monitors.

### Features

- Feather compatible with a feather-like weight of 5 grams
- RAK4260 @ 48&nbsp;MHz with 3.3&nbsp;V logic/power
- 256&nbsp;KB of FLASH + 32KB of RAM
- 32.768&nbsp;kHz crystal for clock generation & RTC
- 3.3&nbsp;V regulator with 500&nbsp;mA peak current output
- USB native support, comes with a USB bootloader and serial port debugging
- Up to 20 GPIO pins
- Hardware Serial, hardware I2C, hardware SPI support
- PWM outputs on all pins
- 6 x 12-bit analog inputs
- 1 x 10-bit analog output (DAC)
- Built-in 100&nbsp;mA LiPoly charging port, with LED indicator
- Programmable built-in LED for customized applications
- Power/enable pin
- Four (4) mounting holes
- Reset button

## Specifications

### Overview

The RAK3244 BastWAN Breakout Board is shown in **Figure 1**, which displays the top and back view of the board, respectively.<br/><br/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/datasheet/rak3244-front-back.svg"
  width="40%"
  caption="RAK3244 BastWAN Breakout Board Front and Back View"
  zoomMode={true}
/>

#### Block Diagram

The block diagram of the RAK3244 BastWAN illustrates the various interfaces corresponding to the functionalities outlined in the product overview. <br/><br/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/datasheet/rak3244-block-diagram.svg"
  width="80%"
  caption="RAK3244 BastWAN Breakout Board Block Diagram"
  zoomMode={true}
/>

### Hardware

The hardware specification is divided into four sections, detailing the interfacing, pinouts with their corresponding functions, and diagrams. It also includes the RF and mechanical parameters of the RAK3244 BastWAN Breakout Board.

#### Interfaces

**Figure 3** shows the overview of interfaces available on the RAK3244 BastWAN Breakout Board.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/datasheet/rak3244-interface.svg"
  width="70%"
  caption="RAK3244 BastWAN Breakout Board Interface Overview"
  zoomMode={true}
/>

##### SWD Programming Interface

When programming using a DAPLink tool, ensure that all four (4) of the following pins are connected to your DAPLink tool:

1. **3V3**
2. **SWDIO**
3. **SWCLK**
4. **GND**

:::tip NOTE
It is recommended to leave these pins exposed for programming purposes and avoid remapping them as GPIOs.
:::

The proper connection between the DapLink tool and RAK3244 BastWAN Breakout Board is illustrated in **Figure 4**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/datasheet/rak3244_daplink.svg"
  width="45%"
  caption="RAK3244 BastWAN Breakout Board Pinout for DapLink tool"
  zoomMode={true}
/>

##### I2C Interface

**I2C_SCL** and **I2C_SDA** are connected to the ATECC608A crypto chip, enabling the development of cryptographic applications such as network end-point key management, small message and PII data encryption, secure boot and protected downloads, ecosystem control, and anti-cloning. Additional I2C peripherals can be integrated using the breakout pins on connector J3.

##### RF Interface

The RF pin of the RAK4260 module is wired to an SMA antenna connector.

#### Pin Definition

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/datasheet/rak3244-pinout.svg"
  width="50%"
  caption="RAK3244 BastWAN Breakout Board Pinout"
  zoomMode={true}
/>

The following tables show the pin definition of the RAK3244 BastWAN Breakout Board:

##### J2 Pin Definitions

| Pin |Name | I/O |Description|
| --- | --- | --- | --------- |
| 1   | RST | -   | MCU reset |
| 2   | 3V3 | -   | 3V3 Power |
| 3   | GND | -   | GND       |
| 4   | GND | -   | GND       |
| 5   | A0  | I/O | PA09      |
| 6   | A1  | I/O | PA08      |
| 7   | A2  | I/O | PA07      |
| 8   | A3  | I/O | PA06      |
| 9   | A4  | I/O | PA04      |
| 10  | D3  | I/O | PB03      |
| 11  | SCK | I/O | PB23      |
| 12  |MOSI | I/O | PB02      |
| 13  |MISO | I/O | PA23      |
| 14  | RX  | I/O | PA19      |
| 15  | TX  | I/O | PA18      |
| 16  | GND | -   | GND       |

##### J3 Pin Definitions

| Pin | Name | I/O | Description                     |
| --- | --   | --- | ------------------------------- |
| 1   | BATT | -   | Battery Power                   |
| 2   | EN   | -   | Enable Pin for charging chip    |
| 3   | VBUS | -   | USB Power                       |
| 4   | D13  | I/O | PA22                            |
| 5   | D12  | I/O | PA28                            |
| 6   | D11  | I/O | PA05                            |
| 7   | D10  | I/O | PA14                            |
| 8   | D9   | I/O | PA15                            |
| 9   | D6   | I/0 | PB22                            |
| 10  | D5   | I/0 | PB27                            |
| 11  | SCL  | I/O | SCL                             |
| 12  | SDA  | I/O | SDA                             |

##### J5 Pin Definitions

| Pin | Name  | I/O | Description  |
| --- | ------| --- | ------------ |
| 1   | 3V3   | -   | 3V3 Power    |
| 2   | SWDIO | I/O | PA31         |
| 3   | SWCLK | I/O | PA30         |
| 4   | GND   | -   | GND          |

#### RF Characteristics

##### Operating Frequencies

The RAK3244 Breakout Board supports the following LoRa bands:

| Region | Frequency (MHz) |
|-|-|
| Europe | EU868 |
| North America | US915 |
| Australia | AU915 |
| Asia | AS923 |

##### Sensitivity Level

The following charts show the receiving sensitivity of RAK3244 BastWAN at 866&nbsp;Mhz operating frequency.<br/><br/>


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/datasheet/rak3244_sensitivity1.png"
  width="80%"
  caption="RAK3244 BastWAN Breakout Board Sensitivity Levels"
  zoomMode={true}
/>

<br/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/datasheet/rak3244_sensitivity2.png"
  width="55%"
  caption="RAK3244 BastWAN Breakout Board Sensitivity Plot @ SF7"
  zoomMode={true}
/>

<br/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/datasheet/rak3244_sensitivity3.png"
  width="55%"
  caption="RAK3244 BastWAN Breakout Board Sensitivity Plot @ SF12"
  zoomMode={true}
/>



#### Mechanical Characteristics

##### Board Dimensions

**Figure 9** shows the actual dimensions of the RAK3244 BastWAN Breakout Board measured in millimeters (mm). <br/><br/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/datasheet/rak3244_mechanical.png"
  width="65%"
  caption="RAK3244 BastWAN Breakout Board Board Dimension"
  zoomMode={true}
/>


<RkBottomNav/>