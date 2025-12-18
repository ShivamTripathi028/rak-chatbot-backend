---
slug: /product-categories/wisblock/kit4-industrial/datasheet/
title: WisBlock Industrial 4.0 Kit Datasheet
description: Contains a list of the modules and sensors included in this fully customizable WisBlock Industrial Kit for industrial applications.
image: "https://images.docs.rakwireless.com/wisblock/kits/4_industrial_kit_1.png"
keywords:
  - datasheet
  - wisblock
  - WisBlock Industrial 4.0 Kit
  - WisBlock Kit
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# WisBlock Industrial 4.0 Kit Datasheet

## Overview

### Description

The **WisBlock Industrial 4.0 Kit** is a comprehensive and customizable IoT kit designed specifically for industrial settings. This kit includes a range of sensors, including inductive, proximity, fork, and current/coulomb sensors, as well as interfaces commonly used in industrial environments, such as relays, joysticks, and barcode scanners. These sensors and interfaces provide accurate and reliable data, making them ideal for a variety of use cases in the industrial sector.

Depending on the use case, this kit supports a variety of connectivity options, including LoRaWAN, BLE, LTE-M (optional), and NB-IoT (optional), enabling long-range and short-range communication. With this kit, users can easily create custom industrial solutions for a range of applications, including process automation, asset counting, and predictive maintenance.

### Features

- Compatible with Arduino IDE
- USB C interface for data, power, and battery charging
- Supports Li-Ion batteries with built-in solar charging capability
- Multiple communication protocols: LoRa/LoRaWAN, BLE, LTE-M (optional), and NB-IoT (optional)
- Included modules:
    - Two WisBlock Core modules - [RAK4631 LPWAN Module](https://docs.rakwireless.com/product-categories/wisblock/rak4631/quickstart/)
    - One standard [RAK19007 WisBlock Base Board](https://docs.rakwireless.com/product-categories/wisblock/rak19007/quickstart/) with 4 sensor slots and 1 IO slot
    - One [RAK19001 Dual IO WisBlock Base Board](https://docs.rakwireless.com/product-categories/wisblock/rak19001/overview/) with 6 sensor slots and 2 IO slots
    - Two [RAK16002 Coulomb Sensor](https://docs.rakwireless.com/product-categories/wisblock/rak16002/quickstart/)
    - Two [RAK12029 Inductive Sensor](https://docs.rakwireless.com/product-categories/wisblock/rak12029/quickstart/)
    - Two [RAK12028/RAK12031 Fork Sensor](https://docs.rakwireless.com/product-categories/wisblock/rak12031/quickstart/)
    - Two [RAK12017 IR Proximity Sensor](https://docs.rakwireless.com/product-categories/wisblock/rak12017/quickstart/)
    - Two [RAK12014 IR ToF Sensors](https://docs.rakwireless.com/product-categories/wisblock/rak12014/quickstart/)
    - Two [RAK12018 Bar Code Scanner](https://docs.rakwireless.com/product-categories/wisblock/rak12018/quickstart/)
    - Two [RAK16000 DC Current Sensor](https://docs.rakwireless.com/product-categories/wisblock/rak16000/quickstart/)
    - Two [RAK14007/RAK14013 Joystick/Button Modules](https://docs.rakwireless.com/product-categories/wisblock/rak14013/quickstart/)
    - Two relay modules; you can choose between RAK13001 110&nbsp;V and RAK13007 220&nbsp;V versions
    - LoRaWAN supported bands: RU864, IN865, EU868, AU915, US915, KR920, and AS923
    - (Optional) Cellular variant dependent on a country: two (2) [RAK5860](https://docs.rakwireless.com/product-categories/wisblock/rak5860/quickstart/) with 5G LTE NB-IoT capability and two (2) [RAK13101](https://docs.rakwireless.com/product-categories/wisblock/rak13101/quickstart/) with GSM/GPRS capability
- GPS built-in on Cellular modules

## Specifications

### Overview

The WisBlock Industrial 4.0 Kit includes the following modules:

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/kits/4_industrial_kit_2.png"
  figureCount="1"
  caption="Modules of the WisBlock Industrial 4.0 Kit" 
   width="80%"
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

These are the modules included in the kit, showing the chips used inside them.

:::tip NOTE
Check individual modules for their specific requirements, like needed batteries and configurations, as well as their limitations.
:::

| RAK Model                                         | Function             | Chip          | Manufacturer       |
| ------------------------------------------------- | -------------------- | ------------- | ------------------ |
| [RAK16002](https://docs.rakwireless.com/product-categories/wisblock/rak16002) | Coulomb Sensor       | LTC2941IDCB   | Analog Devices     |
| [RAK12029](https://docs.rakwireless.com/product-categories/wisblock/rak12029) | Inductive Sensor     | LDC1614       | Texas Instruments  |
| [RAK12031](https://docs.rakwireless.com/product-categories/wisblock/rak12031) | Fork Sensor          | EE-SX1041     | Omron              |
| [RAK12028](https://docs.rakwireless.com/product-categories/wisblock/rak12028) | RAK12031 Adapter     | --            | RAKwireless        |
| [RAK12017](https://docs.rakwireless.com/product-categories/wisblock/rak12017) | IR Detection         | ITR20001      | Everlight          |
| [RAK12014](https://docs.rakwireless.com/product-categories/wisblock/rak12014) | Time-of-Flight (ToF) | VL53L0X       | STMicroelectronics |
| [RAK12018](https://docs.rakwireless.com/product-categories/wisblock/rak12018) | Code Scanner         | LV3296        | RAKINDA            |
| [RAK16000](https://docs.rakwireless.com/product-categories/wisblock/rak16000) | DC Current Sensor    | INA219BID     | Texas Instruments  |
| [RAK14013](https://docs.rakwireless.com/product-categories/wisblock/rak14013) | Joystick             | ATTINY441-SSU | ATMEL              |
| [RAK13001](https://docs.rakwireless.com/product-categories/wisblock/rak13001) | Relay 110&nbsp;V     | HF46F         | HONGFA             |
| [RAK13007](https://docs.rakwireless.com/product-categories/wisblock/rak13007) | Relay 220&nbsp;V     | G5LE-14-DC3   | OMRON              |

#### WisBlock Cellular Modules

The cellular modules support different cellular protocols, as shown in the table.

| RAK Model                                         | Supported Protocol | Chip   | Manufacturer |
| ------------------------------------------------- | ------------------ | ------ | ------------ |
| [RAK13101](https://docs.rakwireless.com/product-categories/wisblock/rak13101) | GSM/GPRS           | MC20CE | Quectel      |
| [RAK5860](https://docs.rakwireless.com/product-categories/wisblock/rak5860)   | LTE-M/NB-IoT       | BG77   | Quectel      |

#### Interconnections

The WisBlock Industrial 4.0 Kit is designed to get you started on your IoT projects. Before connecting various modules, you must first check for any potential conflicts. To determine whether there are conflicts, you can use the [WisBlock Pin Mapper tool](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool).


<RkBottomNav/>