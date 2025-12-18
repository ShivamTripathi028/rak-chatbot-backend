---
slug: /product-categories/wisblock/rak11722/datasheet/
title: RAK11722 WisBlock LPWAN Module Datasheet
description: Provides comprehensive information about your RAK11722 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak11722/rak11722.png"
keywords:
  - datasheet
  - wisblock
  - RAK11722
sidebar_label: Datasheet
---

# RAK11722 WisBlock LPWAN Module Datasheet

## Overview

### Description

The RAK11722 WisBlock Core module is a RAK11720 stamp module with an expansion PCB and connectors compatible with the WisBlock Base Boards. It allows an easy way to access the pins of the RAK11720 module to simplify development and testing processes.

The module itself comprises a RAK11720 as its main component. The RAK11720 is a combination of an Ambiq Apollo3 Blue AMA3B1KK-KBR-B0 SoC MCU and an SX1262 LoRa chip. It features ultra-low power consumption of 2.37 uA during sleep mode and high LoRa output power up to 22 dBm during a transmission mode.

Additionally, RAK11722 complies with LoRaWAN 1.0.3 protocols and supports LoRa point-to-point communication. The RF communication characteristic of the module (LoRa + BLE) makes it suitable for a variety of applications. These include home automation, sensor networks, building automation, and personal area network applications. Examples are health/fitness sensors, monitors, and more.

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
- **I/O ports**: UART/I2C/SPI/ADC/GPIO
- Long-range - greater than 10 km with optimized antenna
- Ultra-low-power consumption of 2.37 μA in sleep mode
- **Supply Voltage**: 1.8 V ~ 3.6 V
- **Temperature range**: -40° C ~ 85° C

## Specifications

### Overview

The overview details the RAK11722 board and explains the mechanics of mounting it onto the baseboard.

#### Mounting Sketch

The RAK11722 module is designed to work with WisBlock Base Boards. **Figure 1** shows how a RAK11722 module should be mounted on top of a WisBlock Base Board.

> **Image:** RAK11722 Mounting Sketch

### Hardware

The hardware specification is categorized into three parts. It covers the RF, electrical, and mechanical parameters that include the tabular data for the functionalities and standard values of the RAK11722 WisBlock LPWAN Module.

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

#### Chipset

| Vendor         | Part Number             |
|----------------|-------------------------|
| Ambiq, Semtech | AMA3B1KK-KBR-B0, SX1262 |

#### RF Characteristics

The RAK11722 module supports the LoRaWAN bands shown in the table below. When buying a RAK11722 module, pay attention to specifying the correct core module RAK11720 H/L for your region, in which H stands for high-frequency regions and L for low-frequency regions.

:::tip NOTE
Detailed information about the RAK11722 BLE and LoRa antenna can be found on the [antenna datasheet](https://downloads.rakwireless.com/#LoRa/WisBlock/Accessories/).
:::

| Module    | Core Module | Region        | Frequency     |
|-----------|-------------|---------------|---------------|
| RAK11722L | RAK11722L   | Europe        | EU433         |
|           | RAK11722L   | China         | CN470         |
| RAK11722  | RAK11722    | Europe        | EU868         |
|           | RAK11722    | North America | US915         |
|           | RAK11722    | Australia     | AU915         |
|           | RAK11722    | Asia          | AS923-1/2/3/4 |
|           | RAK11722    | India         | IN865         |
|           | RAK11722    | Russia        | RU864         |

#### Electrical Characteristics

##### Power Consumption

| Feature           | Condition    | Minimum | Typical                               | Maximum | Unit |
|-------------------|--------------|---------|---------------------------------------|---------|------|
| Operating Current | LORA TX Mode | -       | 87 (@ 20 dBm, 868 MHz) | -       | mA   |
|                   | BLE TX Mode  | -       | 12.7 (@4.0 dBm)                  | -       | mA   |
| Sleep Current     | With Ch340   | -       | 20                                    |         | uA   |

##### Operating Voltage

| Feature | Minimum | Typical | Maximum | Unit |
|---------|---------|---------|---------|------|
| VCC     | 2.0     | 3.3     | 3.6     | V    |

##### Schematic Diagram

> **Image:** RAK11722 Schematic Diagram

- **WisConnector**: The core module allows the RAK11722 stamp module pinout to be transferred via the board-to-board WisConnector.
- **WisConnector Pin Order**: The pin order of the WisConnector is located in the bottom layer of the module.
- **Core Module**: The core module itself has a RAK11720 at its core, and it shows the core module pin and connection information.
- **SWD Interface**: The breakout module exposes an SWD debug interface. Additionally, the RST pin is used for resetting the core module RAK11720.

#### Mechanical Characteristics

##### Board Dimensions

> **Image:** Mechanical Dimensions

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

### Certification

:::tip Note
For CE and FCC certifications we provide an AT command guide.    
You can find it in our [RUI3 documentation](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/certification-guide) or get it from our [Download Center](https://downloads.rakwireless.com/#RUI/RUI3/Certification%20Guide/).    
::: 

