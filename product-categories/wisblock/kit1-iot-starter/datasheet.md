---
slug: /product-categories/wisblock/kit1-iot-starter/datasheet/
title: WisBlock IoT Starter Kit Datasheet
description: Contains a list of the modules and sensors included in this fully customizable WisBlock IoT Starter Kit for your IoT applications.
image: "https://images.docs.rakwireless.com/wisblock/kits/1_iot_starter_kit_2.png"
keywords:
    - datasheet
    - wisblock
    - WisBlock Kit
    - IoT Starter Kit
sidebar_label: Datasheet
---

# WisBlock IoT Starter Kit Datasheet

## Overview

### Description

The **WisBlock IoT Starter Kit** is an all-in-one solution for quickly developing and prototyping IoT applications. This comprehensive kit includes multiple connectivity options, namely LoRaWAN, BLE, and LTE-M/NB-IoT. It also includes a range of different modules, like temperature and humidity, accelerometer, barometer, ambient light, and GPS. The kit supports multiple outputs, such as a buzzer, RGB LED, and I2C OLED.

With this kit, you can easily create custom IoT solutions for a variety of use cases, such as environmental monitoring, asset tracking, and smart agriculture. The kit is designed to be modular and customizable, allowing to mix and match different modules and connectivity options to create the perfect solution for your needs.

### Features

- Compatible with Arduino IDE
- USB-C interface for data, power, and battery charging
- Supports Li-Ion batteries with built-in solar charging capability.
- Multiple communication protocols (LoRaWAN, WiFi, BLE, LTE-M, and NB-IoT)
- Included modules:
    - One WisBlock Core modules - [RAK4631 LPWAN Module](https://store.rakwireless.com/products/rak4631-lpwan-node?utm_source=RAK4631WisBlockLPWANModule&utm_medium=Document&utm_campaign=BuyFromStore) 
    - One WisBlock Core modules - [RAK11200 WiFi Module](https://store.rakwireless.com/products/wiscore-esp32-module-rak11200?utm_source=WisBlockRAK11200&utm_medium=Document&utm_campaign=BuyFromStore) 
    - Two standard [RAK19007 WisBlock Base Board](https://store.rakwireless.com/products/rak19007-wisblock-base-board-2nd-gen?utm_source=RAK19007&utm_medium=Document&utm_campaign=BuyFromStore) with four (4) sensor slots and 1 IO slot
    - Two [RAK12010 Light Sensor](https://store.rakwireless.com/products/wisblock-ambient-light-sensor-rak12010?utm_source=RAK12010&utm_medium=Document&utm_campaign=BuyFromStore) 
    - Two [RAK1901 Temperature and Humidity Sensor](https://store.rakwireless.com/products/rak1901-shtc3-temperature-humidity-sensor?utm_source=RAK1901&utm_medium=Document&utm_campaign=BuyFromStore) 
    - Two [RAK12047 VOC Sensor](https://store.rakwireless.com/products/rak12047-voc-sensor-sensirion-sgp40?utm_source=RAK12047&utm_medium=Document&utm_campaign=BuyFromStore) 
    - Two [RAK1904 3-Axis Acceleration Sensor](https://store.rakwireless.com/products/rak1904-lis3dh-3-axis-acceleration-sensor?utm_source=RAK1904&utm_medium=Document&utm_campaign=BuyFromStore) 
    - Two [RAK18001 Buzzer Module](https://store.rakwireless.com/products/wisblock-buzzer-module-rak18001?utm_source=WisBlockRAK18001&utm_medium=Document&utm_campaign=BuyFromStore) 
    - Two [RAK14001 RGB LED Module](https://store.rakwireless.com/products/rgb-led-module-rak14001?utm_source=RAK14001&utm_medium=Document&utm_campaign=BuyFromStore) 
    - Two [RAK1921 OLED Display](https://store.rakwireless.com/products/rak1921-oled-display-panel?utm_source=RAK1921&utm_medium=Document&utm_campaign=BuyFromStore) 
    - Two [RAK12021 RGB Sensor Module](https://store.rakwireless.com/products/rak12021-wisblock-rgb-sensor?utm_source=RAK12021&utm_medium=Document&utm_campaign=BuyFromStore) 
    - LoRaWAN supported bands: RU864, IN865, EU868, AU915, US915, KR920, and AS923  
    - Select a cellular variant that is applicable for your region:  
        - Two (2) [RAK5860](https://store.rakwireless.com/products/rak5860-lte-nb-iot-extension-board?utm_source=RAK5860&utm_medium=Document&utm_campaign=BuyFromStore) with 5G LTE NB-IoT capability
        - Two (2) [RAK13101](https://store.rakwireless.com/products/wisblock-gsm-module-rak13101?utm_source=RAK13101&utm_medium=Document&utm_campaign=BuyFromStore) with GSM/GPRS capability
- GPS built-in on cellular modules

## Specifications

### Overview

The WisBlock IoT Starter Kit includes the following modules:

> **Image:** Modules of the WisBlock IoT Starter Kit

### Hardware

#### WisBlock Base and Core

WisBlock Kits require both the WisBlock Base and WisBlock Core to be useful for any IoT application. The sensor and IO modules included in the kit will not work without the base and core.

The table shows the base and core included in the kit.

| RAK Model                                                                                                                                                                             | Function      | Feature                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------------------------------------------------- |
| [RAK19007](https://store.rakwireless.com/products/rak19007-wisblock-base-board-2nd-gen?utm_source=RAK19007&utm_medium=Document&utm_campaign=BuyFromStore)  | WisBlock Base | USB-C, 4 sensor slot, 1 IO slot, battery/solar connector              |
| [RAK4631](https://store.rakwireless.com/products/rak4631-lpwan-node?utm_source=RAK4631WisBlockLPWANModule&utm_medium=Document&utm_campaign=BuyFromStore)   | WisBlock Core | Based on nrf52840 (BLE) and SX1262 (LoRa), IPEX connector for antenna |
| [RAK11200](https://store.rakwireless.com/products/wiscore-esp32-module-rak11200?utm_source=WisBlockRAK11200&utm_medium=Document&utm_campaign=BuyFromStore) | WisBlock Core | Based on ESP32 (WiFi + BLE), built-in PCB antenna                     |

:::tip NOTE
**RAK4631** is compatible with Arduino IDE. You can add the module to the board manager by following either the [Installation Guide in the Learn section](https://learn.rakwireless.com/hc/en-us/articles/26687371039383-How-To-Perform-Installation-of-Board-Support-Package-in-Arduino-IDE) or the [RAK Arduino BSP GitHub Repo](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).
:::

#### WisBlock Modules

The modules included in the kit and the chips used in them are listed below.

:::tip NOTE
Check individual modules for their specific requirements, such as needed battery, configurations, as well as their limitations.
:::

| RAK Model                                                                                                                                                                               | Function                    | Chip       | Manufacturer                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ---------- | --------------------------- |
| [RAK12010](https://store.rakwireless.com/products/wisblock-ambient-light-sensor-rak12010?utm_source=RAK12010&utm_medium=Document&utm_campaign=BuyFromStore)  | Ambient Light Sensor        | VEML7700   | Vishay Semiconductors       |
| [RAK1901](https://store.rakwireless.com/products/rak1901-shtc3-temperature-humidity-sensor?utm_source=RAK1901&utm_medium=Document&utm_campaign=BuyFromStore) | Temperature Humidity Sensor | SHTC3      | Sensirion                   |
| [RAK12047](https://store.rakwireless.com/products/rak12047-voc-sensor-sensirion-sgp40?utm_source=RAK12047&utm_medium=Document&utm_campaign=BuyFromStore)     | VOC Sensor                  | SGP40      | Sensirion                   |
| [RAK1904](https://store.rakwireless.com/products/rak1904-lis3dh-3-axis-acceleration-sensor?utm_source=RAK1904&utm_medium=Document&utm_campaign=BuyFromStore) | 3-Axis Accelerometer        | LIS3DH     | STmicroelectronics          |
| [RAK18001](https://store.rakwireless.com/products/wisblock-buzzer-module-rak18001?utm_source=WisBlockRAK18001&utm_medium=Document&utm_campaign=BuyFromStore) | Buzzer Module               | MLT-5020   | Jiangsu Huaneng Electronics |
| [RAK14001](https://store.rakwireless.com/products/rgb-led-module-rak14001?utm_source=RAK14001&utm_medium=Document&utm_campaign=BuyFromStore)                 | RGB LED Module              | NCP5623B   | On Semiconductors           |
| [RAK1921](https://store.rakwireless.com/products/rak1921-oled-display-panel?utm_source=RAK1921&utm_medium=Document&utm_campaign=BuyFromStore)                | OLED display                | SSD1306    | Solomon Systech Limited     |
| [RAK12021](https://store.rakwireless.com/products/rak12021-wisblock-rgb-sensor?utm_source=RAK12021&utm_medium=Document&utm_campaign=BuyFromStore)            | RGB Sensor                  | TCS37725FN | AMS                         |

#### WisBlock Cellular Modules

The cellular modules support different cellular protocols, as shown in the following table.

| RAK Model                                                                                                                                                                        | Supported Protocol | Chip   | Manufacturer |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------ | ------------ |
| [RAK13101](https://store.rakwireless.com/products/wisblock-gsm-module-rak13101?utm_source=RAK13101&utm_medium=Document&utm_campaign=BuyFromStore)     | GSM/GPRS           | MC20CE | Quectel      |
| [RAK5860](https://store.rakwireless.com/products/rak5860-lte-nb-iot-extension-board?utm_source=RAK5860&utm_medium=Document&utm_campaign=BuyFromStore) | LTE-M/NB-IoT       | BG77   | Quectel      |

#### Interconnections

The WisBlock IoT Starter Kit is designed to get you started on your IoT projects. Before connecting various modules, you must first check for any potential conflicts. To determine whether there are conflicts, you can use the [WisBlock Pin Mapper tool](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool).

