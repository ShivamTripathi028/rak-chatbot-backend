---
slug: /product-categories/wisblock/kit2-biometric-monitoring/datasheet/
title: WisBlock Biometric Monitoring Kit Datasheet
description: Contains a list of the modules and sensors included in this fully customizable WisBlock Biometric Monitoring Kit for your wearable monitoring IoT applications.
image: "https://images.docs.rakwireless.com/wisblock/kits/2_biometric_kit_2.png"
keywords:
    - datasheet
    - WisBlock Biometric Monitoring Kit
    - WisBlock Kit
    - WisBlock
sidebar_label: Datasheet
---

# WisBlock Biometric Monitoring Kit Datasheet

## Overview

### Description

The **WisBlock Biometric Monitoring Kit** is a comprehensive and customizable IoT kit designed for wearable biometric monitoring applications. This kit includes biometric sensors for monitoring heart rate and blood oxygen levels, as well as a non-contact body temperature sensor, providing valuable data for monitoring health and fitness. Depending on the use case, the kit supports various connectivity options such as LoRaWAN, BLE, LTE-M, and NB-IoT, enabling long-range and short-range communication.

With this kit, users can easily create custom biometric monitoring solutions for a variety of scenarios, including remote patient monitoring, sports performance tracking, and wellness applications. With its range of biometric sensors and connectivity options, it offers a versatile platform for creating customized solutions for a variety of use cases.

### Features

- Compatible with Arduino IDE
- USB C interface for data, power, and battery charging
- Supports Li-Ion batteries with built-in solar charging capabilities
- Multiple communication protocols: LoRa/LoRaWAN, BLE, LTE-M (optional), and NB-IoT (optional)
- Included modules:
    - Two WisBlock Core modules - [RAK4631 LPWAN Module](https://docs.rakwireless.com/product-categories/wisblock/rak4631/quickstart/)
    - One standard [RAK19007 WisBlock Base Board](https://docs.rakwireless.com/product-categories/wisblock/rak19007/quickstart/) with 4 sensor slots and 1 IO slot
    - One standard [RAK19003 WisBlock Mini Base Board](https://docs.rakwireless.com/product-categories/wisblock/rak19003/quickstart/) with 2 sensor slots
    - Two [RAK12003 IR Contactless Temperature Sensor](https://docs.rakwireless.com/product-categories/wisblock/rak12003/quickstart/)
    - Two [RAK12012 Heartrate Pulse Oximetry Sensor](https://docs.rakwireless.com/product-categories/wisblock/rak12012/quickstart/)
    - LoRaWAN Supported bands: RU864, IN865, EU868, AU915, US915, KR920, and AS923
    - (Optional) Cellular variant dependent on a country: two (2) [RAK5860](https://docs.rakwireless.com/product-categories/wisblock/rak5860/quickstart/) with 5G LTE NB-IoT capability and two (2) [RAK13101](https://docs.rakwireless.com/product-categories/wisblock/rak13101/quickstart/) with GSM/GPRS capability
- GPS built-in on Cellular modules

## Specifications

### Overview

The WisBlock Biometric Monitoring Kit includes the following modules:

> **Image:** Modules of WisBlock Biometric Monitoring Kit

### Hardware

#### WisBlock Base and Core

WisBlock Kits require WisBlock Base and WisBlock Core to be useful for any IoT application. The sensor and IO modules included in the kit will not work without the base and core.

The table shows the base and core included in the kit.

| RAK Model                                         | Function      | Feature                                                               |
| ------------------------------------------------- | ------------- | --------------------------------------------------------------------- |
| [RAK19003](https://docs.rakwireless.com/product-categories/wisblock/rak19003/) | WisBlock Base | USB-C, 2 sensor slots, battery/solar connector                        |
| [RAK19007](https://docs.rakwireless.com/product-categories/wisblock/rak19007/) | WisBlock Base | USB-C, 4 sensor slot, 1 IO slot, battery/solar connector              |
| [RAK4631](https://docs.rakwireless.com/product-categories/wisblock/rak4631)   | WisBlock Core | Based on nrf52840 (BLE) and SX1262 (LoRa), IPEX connector for antenna |

:::tip NOTE
RAK4631 is compatible with Arduino IDE. You can add the module to the board manager by following either the [Installation Guide in the Learn section](https://learn.rakwireless.com/hc/en-us/articles/26687371039383-How-To-Perform-Installation-of-Board-Support-Package-in-Arduino-IDE) or the [RAK Arduino BSP GitHub Repo](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).
:::

#### WisBlock Modules

The modules included in the kit and the chips used in them are listed below.

:::tip NOTE
Check individual modules for their specific requirements like needed battery, configurations, as well as its limitations.
:::

| RAK Model                                         | Function                         | Chip                   | Manufacturer     |
| ------------------------------------------------- | -------------------------------- | ---------------------- | ---------------- |
| [RAK12003](https://docs.rakwireless.com/product-categories/wisblock/rak12003) | Infrared Temperature Sensor      | MLX90632SLD-DCB-000-RE | Melexis          |
| [RAK12012](https://docs.rakwireless.com/product-categories/wisblock/rak12012) | Heart Rate Pulse Oximetry Sensor | MAX30102               | Analog Devices |

#### WisBlock Cellular Modules

The cellular modules support different cellular protocols as shown in the table.

| RAK Model                                         | Supported protocol | Chip   | Manufacturer |
| ------------------------------------------------- | ------------------ | ------ | ------------ |
| [RAK13101](https://docs.rakwireless.com/product-categories/wisblock/rak13101) | GSM/GPRS           | MC20CE | Quectel      |
| [RAK5860](https://docs.rakwireless.com/product-categories/wisblock/rak5860)   | LTE-M/NB-IoT       | BG77   | Quectel      |

#### Interconnections

The WisBlock Biometric Monitoring Kit is designed to get you started on your IoT projects. Before connecting various modules, you must first check for any potential conflicts. To determine whether there are conflicts, you can use the [WisBlock Pin Mapper tool](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool).

