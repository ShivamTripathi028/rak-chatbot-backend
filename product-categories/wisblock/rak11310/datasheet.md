---
slug: /product-categories/wisblock/rak11310/datasheet/
title: RAK11310 WisBlock LPWAN Module Datasheet
description: Provides comprehensive information about your RAK11310 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak11310/rak11310.png"
keywords:
  - datasheet
  - wisblock
  - RAK11310

sidebar_label: Datasheet
---

# RAK11310 WisBlock LPWAN Module Datasheet

## Overview

### Description

**RAK11310** is a **WisBlock Core** module for the RAK hardware IoT platform **WisBlock**. It is powered by an RP2040 ARM microcontroller developed by the Raspberry Pi Foundation, combined with the SX1262 LoRa transceiver from Semtech. **RAK11310** can be programmed via the Arduino™ IDE, PlatformIO or MicroPython.

The RAK11310 WisBlock Core module has a RAK11300 LoRa stamp module in it together with a high-quality connector that is compatible with WisBlock Base boards. It allows an easy way to access the pins of the RAK11310 module in order to simplify the development of IoT devices.

The module complies with LoRaWAN 1.0.2 protocols, and also supports LoRa point-to-point communication.

The RF communication characteristic of the Lora module makes it suitable for a variety of applications in the IoT field such as home automation, sensor networks, building automation, personal area networks applications (health/fitness sensors, and monitors, etc.).

### Features

- Based on RAK11300
- Uses the RP2040 as the main processor
- Semtech SX1262 low power high range LoRa transceiver
- LoRaWAN 1.0.2 protocol stack
- **I/O ports**: UART/I2C/GPIO/USB
- Serial Wire Debug (SWD) interface
- **Module Size**: 20 x 30 mm
- **Supply Voltage**: 2.0 V ~ 3.6 V
- **Temperature Range**: -20 °C ~ 70 °C
- **Chipset**: Raspberry Pi Foundation RP2040, Semtech SX1262

## Specifications

### Overview

The overview covers the RAK11310 board overview and the mounting mechanics of the board into the baseboard.

#### Board Overview

> **Image:** RAK11310 Overview

#### Mounting Sketch

The RAK11310 module is designed to work with the RAK5005-O base board. **Figure 2** shows how a RAK11310 module should be mounted on top of the RAK5005-O.

> **Image:** RAK11310 Mounting Sketch

### Hardware

The hardware specification is categorized into four parts. It covers the RF, electrical, and mechanical parameters, which include the tabular data of the functionalities and standard values. It also shows and discusses the diagram of the RAK11310 WisBlock LPWAN Module.

#### Chipset
| Vendor                           | Part number        |
| -------------------------------- | ------------------ |
| Raspberry Pi Foundation, Semtech | RP2040, SX1262     |

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

#### RF Characteristics

The RAK11310 module supports the LoRaWAN bands, as shown in the table below. There are two types RAK11310 module: **RAK11310(L)** is for the low-frequency band regions and **RAK11310** (no extra suffix) is for the high-frequency band regions.

:::tip NOTE
Check the frequency and band regions, as shown in the table, when ordering your RAK11310 WisBlock Core.
:::

| Module      | Core Module | Region        | Frequency |
| ----------- | ----------- | ------------- | --------- |
| RAK11310(L) | RAK11300(L) | Europe        | EU433     |
|             | RAK11300(L) | China         | CN470     |
| RAK11310    | RAK11300    | Europe        | EU868     |
|             | RAK11300    | North America | US915     |
|             | RAK11300    | Australia     | AU915     |
|             | RAK11300    | Korea         | KR920     |
|             | RAK11300    | Asia          | AS923     |
|             | RAK11300    | India         | IN865     |
|             | RAK11300    | Russia        | RU864     |

#### Electrical Characteristics

##### Power Consumption

:::tip NOTE
The power consumption will be published after the hardware test results.
:::

| Feature                   | Condition | Minimum | Typical | Maximum | Unit |
| ------------------------- | --------- | ------- | ------- | ------- | ---- |
| Operating Average Current | TX        | -       |  24.6   | -       | mA   |
| Sleep Current             |           | -       |  3.8    | -       | mA   |

##### Voltage Ratings

| Feature | Minimum | Typical | Maximum | Unit |
| ------- | ------- | ------- | ------- | ---- |
| VCC     | 2.0     | 3.3     | 3.6     | V    |

#### Mechanical Characteristics

##### Board Dimensions

> **Image:** Mechanical Dimensions

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

#### Schematic Diagram

> **Image:** RAK11310 Schematic Diagram

- **WisConnector**: The breakout module exposes the RAK11310 stamp module pinout to the board-to-board WisConnector.

- **WisConnector Pin Order**: The pin order of the WisConnector is located on the bottom layer of the module.

- **Core Module**: The breakout module itself has a RAK11310 at its core, and it shows the core module pin and connection information. By default, the NFC function is disabled to preserve the low-power characteristic of this core.

- **SWD Interface**: The breakout module exposes an SWD debug interface. Additionally, the RST pin is used to reset the RAK11310 core module.

- **Power Up Automatic Reset**: The breakout module has a power-up automatic reset circuit, and the schematic shows the automatic reset mechanism. This module also can be reset through the WisBlock Base reset pin.

## Certification

### Certifications
- **CE:** https://downloads.rakwireless.com/LoRa/WisBlock/RAK11310/Certification/RAK11300_RAK11310_CE_Certification.pdf
- **FCC:** https://downloads.rakwireless.com/LoRa/WisBlock/RAK11310/Certification/RAK11300_RAK11310_FCC_Certification.zip
- **ISED:** https://downloads.rakwireless.com/LoRa/WisBlock/RAK11310/Certification/RAK11300_RAK11310_ISED_Certification.pdf
- **UKCA:** https://downloads.rakwireless.com/LoRa/WisBlock/RAK11310/Certification/RAK11300_RAK11310_UKCA_Certification.pdf

