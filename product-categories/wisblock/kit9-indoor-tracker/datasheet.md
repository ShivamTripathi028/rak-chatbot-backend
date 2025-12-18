---
slug: /product-categories/wisblock/kit9-indoor-tracker/datasheet/
title: WisBlock Indoor Location Tracker Kit Datasheet
description: Contains a list of the modules and sensors included in this fully customizable WisBlock IoT Kit for indoor location tracking applications.
image: "https://images.docs.rakwireless.com/wisblock/kits/9_indoor_tracker_kit_1.png"
keywords:
  - datasheet
  - wisblock
  - WisBlock Indoor Location Tracker Kit
  - WisBlock Kit
sidebar_label: Datasheet
---

# WisBlock Indoor Location Tracker Kit Datasheet

## Overview

### Description

The **WisBlock Indoor Location Tracker Kit** is an advanced IoT kit designed specifically for indoor location tracking, utilizing a range of cutting-edge technologies and sensors. This kit is an ideal solution for companies, organizations, and individuals looking to keep track of their assets and resources in indoor environments.

The kit includes ultra-wideband (UWB) technology, accelerometers, and 9 degrees of freedom (9-DOF) sensors to provide highly accurate and reliable location-tracking capabilities. With customizable features, users can configure the kit to suit their specific needs, and it can be easily integrated into existing systems.

In addition to its powerful tracking capabilities, the WisBlock Indoor Location Tracker Kit also supports various connectivity options such as LoRaWAN, BLE, LTE-M, and NB-IoT. This allows users to select the network connectivity option that best meets their needs and preferences, ensuring seamless integration into existing networks.

### Features

- Compatible with Arduino IDE
- USB-C interface for data, power, and battery charging
- Supports Li-Ion battery with built-in solar charging capability.
- Multiple communication protocols: LoRaWAN, BLE, LTE-M (optional), and NB-IoT (optional)
- Included modules:
    - Four WisBlock Core modules - [RAK4631 LPWAN Module](https://store.rakwireless.com/products/rak4631-lpwan-node?utm_source=RAK4631WisBlockLPWANModule&utm_medium=Document&utm_campaign=BuyFromStore) 
    - Two standard [RAK19007 WisBlock Base Board](https://store.rakwireless.com/products/rak19007-wisblock-base-board-2nd-gen?utm_source=RAK19007&utm_medium=Document&utm_campaign=BuyFromStore) with four (4) sensor slots and 1 IO slot
    - Two [RAK19001 Dual IO WisBlock Base Board](https://store.rakwireless.com/products/rak19001-wisblock-dual-io-base-board?utm_source=RAK19001&utm_medium=Document&utm_campaign=BuyFromStore) with six (6) sensor slots and 2 IO slots
    - Two [RAK1904 Acceleration Sensors](https://store.rakwireless.com/products/rak1904-lis3dh-3-axis-acceleration-sensor?utm_source=RAK1904&utm_medium=Document&utm_campaign=BuyFromStore) 
    - Two [RAK1905 9DOF Sensors](https://store.rakwireless.com/products/9dof-motion-sensor-tdk-mpu9250-rak1905?utm_source=RAK1905&utm_medium=Document&utm_campaign=BuyFromStore) 
    - Four [RAK13801 UWB Modules](https://store.rakwireless.com/products/uwb-module-decawave-dwm1000-rak13801?utm_source=RAK13801&utm_medium=Document&utm_campaign=BuyFromStore) 
    - LoRaWAN supported bands: RU864, IN865, EU868, AU915, US915, KR920, and AS923  
    - (Optional) Select a cellular variant that is applicable for your region:  
        - Two (2) [RAK5860](https://store.rakwireless.com/products/rak5860-lte-nb-iot-extension-board?utm_source=RAK5860&utm_medium=Document&utm_campaign=BuyFromStore) with 5G LTE NB-IoT capability
        - Two (2) [RAK13101](https://store.rakwireless.com/products/wisblock-gsm-module-rak13101?utm_source=RAK13101&utm_medium=Document&utm_campaign=BuyFromStore) with GSM/GPRS capability
- GPS built-in on Cellular modules (only works outdoor)  

## Specifications

### Overview

The WisBlock Indoor Location Tracker Kit includes the following modules:

> **Image:** Modules of the WisBlock Indoor Location Tracker Kit

### Hardware

#### WisBlock Base and Core

WisBlock Kits require WisBlock Base and WisBlock Core to be useful for any IoT application. The sensor and IO modules included in the kit will not work without the base and core.

The table shows the base and core included in the kit.

| RAK Model                                                                                                                                                                            | Function      | Feature                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- | --------------------------------------------------------------------- |
| [RAK19001](https://store.rakwireless.com/products/rak19001-wisblock-dual-io-base-board?utm_source=RAK19001&utm_medium=Document&utm_campaign=BuyFromStore) | WisBlock Base | USB-C, 6 sensor slot, 2 IO slot, battery/solar connector              |
| [RAK19007](https://store.rakwireless.com/products/rak19007-wisblock-base-board-2nd-gen?utm_source=RAK19007&utm_medium=Document&utm_campaign=BuyFromStore) | WisBlock Base | USB-C, 4 sensor slot, 1 IO slot, battery/solar connector              |
| [RAK4631](https://store.rakwireless.com/products/rak4631-lpwan-node?utm_source=RAK4631WisBlockLPWANModule&utm_medium=Document&utm_campaign=BuyFromStore)  | WisBlock Core | Based on nrf52840 (BLE) and SX1262 (LoRa), IPEX connector for antenna |

:::tip NOTE
**RAK4631** is compatible with Arduino IDE. You can add the module to the board manager by following either the [Installation Guide in the Learn section](https://learn.rakwireless.com/hc/en-us/articles/26687371039383-How-To-Perform-Installation-of-Board-Support-Package-in-Arduino-IDE) or the [RAK Arduino BSP GitHub Repo](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).
:::

#### WisBlock Modules

These are the modules included in the kit, showing the chips used inside them.

:::tip NOTE
Check the individual modules for their specific requirements, like needed batteries and configurations, as well as their limitations.
:::

| RAK Model                                                                                                                                                                               | Function            | Chip     | Manufacturer       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | -------- | ------------------ |
| [RAK1904](https://store.rakwireless.com/products/rak1904-lis3dh-3-axis-acceleration-sensor?utm_source=RAK1904&utm_medium=Document&utm_campaign=BuyFromStore) | 3-Axis Acceleration | LIS3DH   | STMicroelectronics |
| [RAK1905](https://store.rakwireless.com/products/9dof-motion-sensor-tdk-mpu9250-rak1905?utm_source=RAK1905&utm_medium=Document&utm_campaign=BuyFromStore)    | 9-Axis DOF Sensor   | MPU-9250 | TDK                |
| [RAK13801](https://store.rakwireless.com/products/uwb-module-decawave-dwm1000-rak13801?utm_source=RAK13801&utm_medium=Document&utm_campaign=BuyFromStore)    | UWB                 | DW10000  | Decawave           |

#### WisBlock Cellular Modules

The cellular modules support different cellular protocols, as shown in the table.

| RAK Model                                                                                                                                                                        | Supported Protocol | Chip   | Manufacturer |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------ | ------------ |
| [RAK13101](https://store.rakwireless.com/products/wisblock-gsm-module-rak13101?utm_source=RAK13101&utm_medium=Document&utm_campaign=BuyFromStore)     | GSM/GPRS           | MC20CE | Quectel      |
| [RAK5860](https://store.rakwireless.com/products/rak5860-lte-nb-iot-extension-board?utm_source=RAK5860&utm_medium=Document&utm_campaign=BuyFromStore) | LTE-M/NB-IoT       | BG77   | Quectel      |

#### Interconnections

The **WisBlock Indoor Location Tracker Kit** is designed to get you started on your IoT projects. Before connecting various modules, you must first check for any potential conflicts. To determine whether there are conflicts, you can use the [WisBlock Pin Mapper tool](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool).

