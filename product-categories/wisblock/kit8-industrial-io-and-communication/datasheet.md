---
slug: /product-categories/wisblock/kit8-industrial-io-and-communication/datasheet/
title: WisBlock Industrial IO and Communication Kit Datasheet
description: Contains a list of the modules and sensors included in this fully customizable WisBlock Industrial IO and Communication Kit for industrial applications.
image: "https://images.docs.rakwireless.com/wisblock/kits/8_industrial_comms_kit_1.png"
keywords:
  - datasheet
  - wisblock
  - WisBlock Industrial IO and Communication Kit
  - WisBlock Kit
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# WisBlock Industrial IO and Communication Kit Datasheet

## Overview

### Description

The **WisBlock Industrial IO and Communication Kit** is an IoT kit that is versatile and customizable for industrial applications. This kit offers a range of interfaces, including LIN, CAN, SDI-12, 4-20&nbsp;mA, RS485, Ethernet, Analog, and Relay for data acquisition and control. It also supports different connectivity options, such as LoRaWAN, BLE, LTE-M, NB-IoT, and PoE Ethernet, making integration with various systems easier.

Whether you are looking to measure and control various parameters in your industrial setting or interface with different systems, the WisBlock Industrial IO and Communication Kit is the perfect solution. The kit includes a range of module interfaces that allow you to monitor and control different variables, making it ideal for various applications. With its customizable design and flexibility, the WisBlock Industrial IO and Communication Kit offer a complete solution for a range of industrial IoT applications. It allows for easy expansion and customization, making it perfect for those who require specific functionality.

### Features

- Compatible with Arduino IDE
- USB C interface for data, power, and battery charging
- Supports Li-Ion battery with built-in solar charging capability
- Multiple communication protocols: LoRa/LoRaWAN, BLE, LTE-M (optional), and NB-IoT (optional)
- Included modules:
    - Two WisBlock Core modules - [RAK4631 LPWAN Module](https://docs.rakwireless.com/product-categories/wisblock/rak4631/quickstart/)
    - One standard [RAK19007 WisBlock Base Board](https://docs.rakwireless.com/product-categories/wisblock/rak19007/quickstart/) with 4 sensor slots and 1 IO slot
    - One [RAK19001 Dual IO WisBlock Base Board](https://docs.rakwireless.com/product-categories/wisblock/rak19001/overview/) with 6 sensor slots and 2 IO slots
    - Two [RAK13005 LIN Bus Modules](https://docs.rakwireless.com/product-categories/wisblock/rak13005/quickstart/)
    - Two [RAK13006 CAN Bus Modules](https://docs.rakwireless.com/product-categories/wisblock/rak13006/overview/)
    - Two [RAK13010 SDI-12 Modules](https://docs.rakwireless.com/product-categories/wisblock/rak13010/overview/)
    - Two [RAK5801 4-20&nbsp;mA Interface Modules](https://docs.rakwireless.com/product-categories/wisblock/rak5801/quickstart/)
    - Two [RAK5802 RS485 Interface Modules](https://docs.rakwireless.com/product-categories/wisblock/rak5802/quickstart/)
    - Two [RAK5811 0-5&nbsp;V Interface Modules](https://docs.rakwireless.com/product-categories/wisblock/rak5811/quickstart/)
    - Two Relay modules; you can choose between RAK13001 110&nbsp;V and RAK13007 220&nbsp;V versions
    - LoRaWAN supported bands: RU864, IN865, EU868, AU915, US915, KR920, and AS923
    - (Optional) Ethernet using RAK13800 module
    - (Optional) Cellular variant dependent on a country: two (2) [RAK5860](https://docs.rakwireless.com/product-categories/wisblock/rak5860/quickstart/) with 5G LTE NB-IoT capability and two (2) [RAK13101](https://docs.rakwireless.com/product-categories/wisblock/rak13101/quickstart/) with GSM/GPRS capability
- GPS built-in on Cellular modules
- (Optional) Ethernet module can also have a PoE daughter board


## Specifications

### Overview

The WisBlock Industrial IO and Communication Kit includes the following modules:

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/kits/8_industrial_comms_kit_2.png" 
  width="80%"
  caption="Modules of WisBlock Industrial IO and Communication Kit"
/>

### Hardware

#### WisBlock Base and Core

WisBlock Kits require WisBlock Base and WisBlock Core to be useful for any IoT application. The sensor and IO modules included in the kit will not work without the base and core.

The table shows the base and core included in the kit.

| RAK Model                                         | Function      | Feature                                                               |
| ------------------------------------------------- | ------------- | --------------------------------------------------------------------- |
| [RAK19001](https://docs.rakwireless.com/product-categories/wisblock/rak19003) | WisBlock Base | USB-C, 6 sensor slot, 2 IO slot, battery/solar connector              |
| [RAK19007](https://docs.rakwireless.com/product-categories/wisblock/rak19007) | WisBlock Base | USB-C, 4 sensor slot, 1 IO slot, battery/solar connector              |
| [RAK4631](https://docs.rakwireless.com/product-categories/wisblock/rak4631)   | WisBlock Core | Based on nrf52840 (BLE) and SX1262 (LoRa), IPEX connector for antenna |

:::tip NOTE
RAK4631 is compatible with Arduino IDE. You can add the module to the board manager by following either the [Installation Guide in the Learn section](https://learn.rakwireless.com/hc/en-us/articles/26687371039383-How-To-Perform-Installation-of-Board-Support-Package-in-Arduino-IDE) or the [RAK Arduino BSP GitHub Repo](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).
:::

#### WisBlock Modules

The modules included in the kit and the chips used in them are listed below.

:::tip NOTE
Check individual modules for their specific requirements, like needed batteries and configurations, as well as their limitations.
:::

| RAK Model                                         | Function         | Chip               | Manufacturer       |
| ------------------------------------------------- | ---------------- | ------------------ | ------------------ |
| [RAK13005](https://docs.rakwireless.com/product-categories/wisblock/rak13005) | LIN              | TLE7259-3          | Infineon           |
| [RAK13006](https://docs.rakwireless.com/product-categories/wisblock/rak13006) | CAN              | MCP2518FD, ATA6563 | Microchip          |
| [RAK13010](https://docs.rakwireless.com/product-categories/wisblock/rak13010) | SDI-12           | --                 | RAKwireless        |
| [RAK5801](https://docs.rakwireless.com/product-categories/wisblock/rak5801)   | 4-20&nbsp;mA     | LM2902             | STMicroelectronics |
| [RAK5802](https://docs.rakwireless.com/product-categories/wisblock/rak5802)   | RS485            | TP8485E            | 3PEAK              |
| [RAK5811](https://docs.rakwireless.com/product-categories/wisblock/rak5811)   | 0-5&nbsp;V       | LM2902             | STMicroelectronics |
| [RAK13001](https://docs.rakwireless.com/product-categories/wisblock/rak13001) | Relay 110&nbsp;V | HF46F              | HONGFA             |
| [RAK13007](https://docs.rakwireless.com/product-categories/wisblock/rak13007) | Relay 220&nbsp;V | G5LE-14-DC3        | OMRON              |
| [RAK13800](https://docs.rakwireless.com/product-categories/wisblock/rak13800) | Ethernet         | W5100S-L           | WIZnet             |


#### WisBlock Cellular Modules

The cellular modules support different cellular protocols, as shown in the table.

| RAK Model                                         | Supported protocol | Chip   | Manufacturer |
| ------------------------------------------------- | ------------------ | ------ | ------------ |
| [RAK13101](https://docs.rakwireless.com/product-categories/wisblock/rak13101) | GSM/GPRS           | MC20CE | Quectel      |
| [RAK5860](https://docs.rakwireless.com/product-categories/wisblock/rak5860)   | LTE-M/NB-IoT       | BG77   | Quectel      |

#### Interconnections

The WisBlock Movement Detection Kit is designed to get you started on your IoT projects. Before connecting various modules, you must first check for any potential conflicts. To determine whether there are conflicts, you can use the [WisBlock Pin Mapper tool](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool).

<RkBottomNav/>
