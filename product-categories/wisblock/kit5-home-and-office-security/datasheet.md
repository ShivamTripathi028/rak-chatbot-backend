---
slug: /product-categories/wisblock/kit5-home-and-office-security/datasheet/
title: WisBlock Home and Office Security Kit Datasheet
description: Contains a list of the modules and sensors included in this fully customizable WisBlock IoT Kit for your home and office security applications.
image: "https://images.docs.rakwireless.com/wisblock/kits/5_homeoffice_kit_1.png"
keywords:
  - datasheet
  - wisblock
  - WisBlock Home and Office Security Kit
  - WisBlock Kit
sidebar_label: Datasheet
---

# WisBlock Home and Office Security Kit Datasheet

## Overview

### Description

The **WisBlock Home and Office Security Kit** is a comprehensive and customizable IoT kit that is designed to provide security for homes and offices. This kit includes a range of sensors and modules that focus on detecting intrusion and access control. The intrusion detection sensors include PIR, radar, and ultrasonic sensors that provide reliable and accurate detection of movement and intrusion. The access control modules include fingerprint, NFC, and barcode sensors that provide secure and convenient access to your home or office.

Depending on the use case, this kit supports different connectivity options, including LoRaWAN, BLE, LTE-M, and NB-IoT,enabling long-range and short-range communication. With this kit, you can easily monitor your home or office remotely, receive real-time alerts, and take appropriate action in the event of an intrusion or unauthorized access attempt.

### Features

- Compatible with the Arduino IDE
- USB C interface for data, power, and battery charging
- Supports Li-Ion batteries with built-in solar charging capability
- Multiple communication protocols: LoRa/LoRaWAN, BLE, LTE-M (optional), and NB-IoT (optional)
- Included modules:
    - Two WisBlock Core modules - [RAK4631 LPWAN Module](https://docs.rakwireless.com/product-categories/wisblock/rak4631/quickstart/)
    - One standard [RAK19007 WisBlock Base Board](https://docs.rakwireless.com/product-categories/wisblock/rak19007/quickstart/) with 4 sensor slots and 1 IO slot
    - One [RAK19001 Dual IO WisBlock Base Board](https://docs.rakwireless.com/product-categories/wisblock/rak19001/overview/) with 6 sensor slots and 2 IO slots
    - Two [RAK12001 Fingerprint Reader](https://docs.rakwireless.com/product-categories/wisblock/rak12001/quickstart/)
    - Two [RAK13600 NFC Card Reader](https://docs.rakwireless.com/product-categories/wisblock/rak13600/quickstart/)
    - Two [RAK12018 Bar Code Scanner](https://docs.rakwireless.com/product-categories/wisblock/rak12018/quickstart/)
    - Two [RAK12013 Radar Sensor](https://docs.rakwireless.com/product-categories/wisblock/rak12013/quickstart/)
    - Two [RAK12006 PIR Motion Sensor](https://docs.rakwireless.com/product-categories/wisblock/rak12006/quickstart/)
    - Two [RAK12007 Ultrasonic Sensor](https://docs.rakwireless.com/product-categories/wisblock/rak12007/quickstart/)
    - Two Relay modules; you can choose between RAK13001 110 V and RAK13007 220 V versions
    - LoRaWAN supported bands: RU864, IN865, EU868, AU915, US915, KR920, and AS923
    - (Optional) Cellular variant dependent on a country: two (2) [RAK5860](https://docs.rakwireless.com/product-categories/wisblock/rak5860/quickstart/) with 5G LTE NB-IoT capability and two (2) [RAK13101](https://docs.rakwireless.com/product-categories/wisblock/rak13101/quickstart/) with GSM/GPRS capability
- GPS built-in on Cellular modules

## Specifications

### Overview

The WisBlock Home Office Security Kit includes the following modules:

> **Image:** Modules of the WisBlock Home Office Security Kit

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

| RAK Model                                         | Function           | Chip        | Manufacturer                      |
| ------------------------------------------------- | ------------------ | ----------- | --------------------------------- |
| [RAK12001](https://docs.rakwireless.com/product-categories/wisblock/rak12001) | Fingerprint Module | R307        | GROW                              |
| [RAK13600](https://docs.rakwireless.com/product-categories/wisblock/rak13600) | NFC Reader Module  | PN532       | NXP                               |
| [RAK12018](https://docs.rakwireless.com/product-categories/wisblock/rak12018) | Code Scanner       | VL53L0X     | RAKINDA                           |
| [RAK12013](https://docs.rakwireless.com/product-categories/wisblock/rak12013) | Radar Sensor       | RCWL-9196   | RCWL                              |
| [RAK12006](https://docs.rakwireless.com/product-categories/wisblock/rak12006) | PIR Sensor         | AM312       | Senba Sensing Technology Co., Ltd |
| [RAK12007](https://docs.rakwireless.com/product-categories/wisblock/rak12007) | Ultrasonic Sensor  | CS100       | angoSense                         |
| [RAK13001](https://docs.rakwireless.com/product-categories/wisblock/rak13001) | Relay 110 V   | HF46F       | HONGFA                            |
| [RAK13007](https://docs.rakwireless.com/product-categories/wisblock/rak13007) | Relay 220 V   | G5LE-14-DC3 | OMRON                             |

#### WisBlock Cellular Modules

The cellular modules support different cellular protocols, as shown in the table.

| RAK Model                                         | Supported Protocol | Chip   | Manufacturer |
| ------------------------------------------------- | ------------------ | ------ | ------------ |
| [RAK13101](https://docs.rakwireless.com/product-categories/wisblock/rak13101) | GSM/GPRS           | MC20CE | Quectel      |
| [RAK5860](https://docs.rakwireless.com/product-categories/wisblock/rak5860)   | LTE-M/NB-IoT       | BG77   | Quectel      |

#### Interconnections

The WisBlock Home Office Security Kit is designed to get you started on your IoT projects. Before connecting various modules, you must first check for any potential conflicts. To determine whether there are conflicts, you can use the [WisBlock Pin Mapper tool](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool).

