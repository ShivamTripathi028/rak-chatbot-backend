---
slug: /product-categories/wisblock/kit6-light-and-color/datasheet/
title: WisBlock Light and Color Kit Datasheet
description: Contains a list of the modules and sensors included in this fully customizable WisBlock IoT Kit for measuring and controlling light and color-based applications.
image: "https://images.docs.rakwireless.com/wisblock/kit6-light-color/6_lightcolor_kit_1.png"
keywords:
  - datasheet
  - WisBlock
  - WisBlock Light and Color Kit
  - WisBlock Kit
sidebar_label: Datasheet
---

# WisBlock Light and Color Kit Datasheet

## Overview

### Description

The **WisBlock Light and Color Kit** is a comprehensive and customizable IoT kit that includes a range of sensors and modules for measuring and controlling light and color. This kit includes RGB, visible, and UV light sensors, as well as LED bar and RGB modules, providing a versatile platform for measuring and controlling light and color in a wide range of applications.

The kit is designed for easy integration with other WisBlock modules, and it supports different connectivity options like LoRaWAN, BLE, LTE-M, and NB-IoT, enabling you to choose the most suitable connectivity option for your specific use case. With this kit, you can easily measure light and color levels remotely, receive real-time alerts, and take appropriate action to control light and color in your application.

### Features

- Compatible with Arduino IDE
- USB C interface for data, power, and battery charging
- Supports Li-Ion battery with built-in solar charging capability
- Multiple communication protocols: LoRa/LoRaWAN, BLE, LTE-M (optional), and NB-IoT (optional)
- Included modules:
    - Two WisBlock Core modules - [RAK4631 LPWAN Module](https://docs.rakwireless.com/product-categories/wisblock/rak4631/quickstart/)
    - One standard [RAK19007 WisBlock Base Board](https://docs.rakwireless.com/product-categories/wisblock/rak19007/quickstart/) with 4 sensor slots and 1 IO slot
    - One [RAK19001 Dual IO WisBlock Base Board](https://docs.rakwireless.com/product-categories/wisblock/rak19001/overview/) with 6 sensor slots and 2 IO slots
    - Two [RAK12021 RGB Light Sensors](https://docs.rakwireless.com/product-categories/wisblock/rak12021/quickstart/)
    - Two [RAK12019 UV Light Sensors](https://docs.rakwireless.com/product-categories/wisblock/rak12019/quickstart/)
    - Two [RAK12010 Ambient Light Sensors](https://docs.rakwireless.com/product-categories/wisblock/rak12010/quickstart/) based on the VEML7700
    - Two [RAK1903 Ambient Light Sensors](https://docs.rakwireless.com/product-categories/wisblock/rak1903/quickstart/) based on the OPT3001
    - Two [RAK14003 LED Bar Modules](https://docs.rakwireless.com/product-categories/wisblock/rak14003/quickstart/)
    - Two [RAK14001 RGB LED Modules](https://docs.rakwireless.com/product-categories/wisblock/rak14001/quickstart/)
    - LoRaWAN supported bands: RU864, IN865, EU868, AU915, US915, KR920, and AS923
    - (Optional) Cellular variant dependent on a country: two (2) [RAK5860](https://docs.rakwireless.com/product-categories/wisblock/rak5860/quickstart/) with 5G LTE NB-IoT capability and two (2) [RAK13101](https://docs.rakwireless.com/product-categories/wisblock/rak13101/quickstart/) with GSM/GPRS capability
- GPS built-in on Cellular modules

## Specifications

### Overview

The WisBlock Light and Color Kit includes the following modules:

> **Image:** Modules of the WisBlock Light and Color Kit

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
Check individual modules for their specific requirements like needed battery, configurations, as well as its limitations.
:::

| RAK Model                                         | Function             | Chip                      | Manufacturer               |
| ------------------------------------------------- | -------------------- | ------------------------- | -------------------------- |
| [RAK12021](https://docs.rakwireless.com/product-categories/wisblock/rak12021) | RGB Sensor           | TCS37725FN                | AMS                        |
| [RAK12019](https://docs.rakwireless.com/product-categories/wisblock/rak12019) | UV Sensor            | LTR-390UV-01              | Lite-On                    |
| [RAK12010](https://docs.rakwireless.com/product-categories/wisblock/rak12010) | Ambient Light Sensor | VEML7700                  | Vishay Semiconductors      |
| [RAK1903](https://docs.rakwireless.com/product-categories/wisblock/rak1903)   | Ambient Light Sensor | OPT3001DNPR               | Texas Instruments          |
| [RAK14003](https://docs.rakwireless.com/product-categories/wisblock/rak14003) | LED Bar Graph        | MCP23017, KEM-102510A-RYG | Microchip, Hongke Lighting |
| [RAK14001](https://docs.rakwireless.com/product-categories/wisblock/rak14001) | RGB LED Module       | NCP5623B                  | On Semiconductors          |

#### WisBlock Cellular Modules

The cellular modules support different cellular protocols as shown in the table.

| RAK Model                                         | Supported Protocol | Chip   | Manufacturer |
| ------------------------------------------------- | ------------------ | ------ | ------------ |
| [RAK13101](https://docs.rakwireless.com/product-categories/wisblock/rak13101) | GSM/GPRS           | MC20CE | Quectel      |
| [RAK5860](https://docs.rakwireless.com/product-categories/wisblock/rak5860)   | LTE-M/NB-IoT       | BG77   | Quectel      |

#### Interconnections

The WisBlock Movement Detection Kit is designed to get you started on your IoT projects. Before connecting various modules, you must first check for any potential conflicts. To determine whether there are conflicts, you can use the [WisBlock Pin Mapper tool](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool).

