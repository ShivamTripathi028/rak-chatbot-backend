---
slug: /product-categories/wisblock/rak3372/datasheet/
title: RAK3372 WisBlock LPWAN Module Datasheet
description: Provides comprehensive information about your RAK3372 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisblock/rak3372/rak3372.png
keywords:
  - datasheet
  - wisblock
  - RAK3372
sidebar_label: Datasheet
---

# RAK3372 WisBlock LPWAN Module Datasheet

## Overview

### Description

The RAK3372 WisBlock Core module is a [RAK3172 LoRa module](https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/datasheet/) with an expansion PCB and connectors compatible with the WisBlock Base Boards. It allows an easy way to access the pins of the RAK3172 module, simplifying development and testing processes.

The module itself comprises a RAK3172 as its main component. The RAK3372 is based on the STM32WLE5CCU6 LoRa SoC transceiver chip. It features ultra-low power consumption of less than 2.0 uA during sleep mode with configurable high LoRa output RF power up to 22 dBm during transmission mode.

Additionally, RAK3372 complies with LoRaWAN 1.0.3 protocols and supports LoRa point-to-point communication.

### Features

- Based on [STM32WLE5CCU6](https://www.st.com/resource/en/datasheet/stm32wle5cc.pdf)
- **I/O ports**: UART/I2C/GPIO
- **Temperature range**: -70° C to +85° C
- **Supply voltage**: 2.0 ~ 3.6 V
- Low-Power Wireless Systems with 7.8 kHz to 500 kHz Bandwidth
- Ultra-Low Power Consumption of less than 2.0 uA in sleep mode
- LoRa PA Boost mode with 22 dBm output power
- Serial Wire Debug (SWD) interface
- **Module size**: 20 mm x 30 mm

:::warning
- RAK3372 WB_IO3 (WisBlock IO Pin 3) is connected to PB12 of the RAK3172 module. This pin is internally connected to a 10 kΩ resistor as mentioned on the [pin definition table of the RAK3172 datasheet](https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/datasheet/#pin-definition). Other WisBlock modules that use this pin will have possible conflict.
:::

## Specifications

### Overview

> **Image:** RAK3372 Mounted in WisBlock Base

> **Image:** RAK3372 WisBlock Core Parts

### Hardware

The hardware specification is categorized into three parts. It covers the RF, electrical, and mechanical parameters that include the tabular data of the functionalities and standard values of the RAK3372 WisBlock LPWAN Module.

#### Chipset

| Vendor             | Part Number                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------|
| STmicroelectronics | [STM32WLE5CCU6](https://www.st.com/resource/en/datasheet/stm32wle5cc.pdf) |

#### RF Characteristics

The RAK3372 module supports the LoRaWAN bands shown in the table below. When buying a RAK3372 module, pay attention to specifying the correct core module for your region. The RAK3172 Module is available in two variants: (1) with CE and UKCA certification marks, and (2) with FCC, IC, and RCM certification marks.

:::tip NOTE

RAK3372 has a built-in IPEX connector on the RAK3172 module embedded in it. There is no other option for antenna connection than the IPEX connector.

:::

| Core Module | Region        | Frequency     |
|-------------|---------------|---------------|
| RAK3372(H)  | India         | IN865         |
| RAK3372(H)  | Europe        | EU868         |
| RAK3372(H)  | Russia        | RU864         |
| RAK3372(H)  | North America | US915         |
| RAK3372(H)  | Canada        | US915         |
| RAK3372(H)  | Australia     | AU915         |
| RAK3372(H)  | Korea         | KR920         |
| RAK3372(H)  | Asia          | AS923-1/2/3/4 |
| RAK3372(L)  | Europe        | EU433         |
| RAK3372(L)  | China         | CN470         |

#### Electrical Characteristics

##### Operating Voltage

| Feature | Minimum | Typical | Maximum | Unit      |
|---------|---------|---------|---------|-----------|
| VCC     | 2.0     | 3.3     | 3.6     | Volts (V) |

##### Operating Current

| Feature           | Condition | Minimum                              | Typical | Maximum | Unit |
|-------------------|-----------|--------------------------------------|---------|---------|------|
| Operating Current | TX Mode   | 87 (@ 20 dBm 868 Mhz) |         |         | mA   |
|                   | RX Mode   | 5.22                                 |         |         | mA   |

##### Sleep Current

| Feature             | Condition | Minimum (2.1 V) | Typical (3.3 V) | Maximum | Unit |
|---------------------|-----------|----------------------|----------------------|---------|------|
| Current Consumption | EU868     | -                    | 1.69                 | -       | μA   |
|                     | US915     | -                    | 1.69                 | -       | μA   |
|                     | CN470     | -                    | 1.69                 | -       | μA   |

##### Schematic Diagram

> **Image:** RAK3372 Schematic Diagram

- **WisConnector J1**: The 40-pin board-to-board WisBlock connector. This is attached to the WisBlock Base `Core Slot`.
- **RAK3172 Module U1**: The WisBlock Core's main chip.
- **SWD Interface P1**: The WisBlock Core module exposes an SWD debug interface. This can be used on firmware updates and debugging.
- **USB-UART Converter U2**: The firmware update and AT commands for the module are accessed via UART2. A built-in USB-to-serial converter allows for easy connection of the module to a computer.

#### Mechanical Characteristics

##### Board Dimensions

> **Image:** Mechanical Dimensions

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

:::tip NOTE

The RAK3372 firmware update can be found on the [RAK3372 Quick Start Guide miscellaneous section](https://docs.rakwireless.com/product-categories/wisblock/rak3372/quickstart/#upgrading-the-firmware).

:::

### Certification

:::tip Note
For CE and FCC certifications we provide an AT command guide.    
You can find it in our [RUI3 documentation](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/certification-guide) or get it from our [Download Center](https://downloads.rakwireless.com/#RUI/RUI3/Certification%20Guide/).    
::: 

