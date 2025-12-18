---
slug: /product-categories/wisblock/rak12037/datasheet/
title: RAK12037 WisBlock CO2 Sensor Module Datasheet
description: Provides comprehensive information about your RAK12037 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisblock/rak12037/rak12037.png
keywords:
    - RAK12037
    - wisblock
    - datasheet
sidebar_label: Datasheet
---

# RAK12037 WisBlock CO2 Sensor Module Datasheet

## Overview

### Description

RAK12037 is a WisBlock Sensor that extends the WisBlock system based on the SCD30 module. This module uses NDIR CO2 sensor technology to sense CO2 and has an integrated temperature and humidity sensor. Ambient humidity and temperature can be measured by monitoring and compensating for external heat sources without the need for additional components. The small module height allows easy integration into different applications. The SCD30 features dual-channel detection for superior stability and ±30ppm + 3% accuracy.

### Features

  * Voltage supply: **3.3 V ~ 5.5 V**
  * Current consumption: **19 mA @ 1 meas. per 2s**
  * Chipset: **SCD30**
  * Temperature range: **-40° C ~ 70° C**
  * Measurement range: **400 ppm – 10.000 ppm**
  * Accuracy: **±(30 ppm + 3%)**
  * Integrated temperature, humidity sensor, and CO2 sensor
  * Dual-channel detection for superior stability
  * I2C interface
  * Fully calibrated and linearized

## Specifications

### Overview

> **Image:** RAK12037 WisBlock CO2 Sensor Module top and bottom view

#### Mounting

**Figure 2** shows the mounting mechanism of the RAK12037 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. The RAK12037 module can be mounted on the IO slots.

> **Image:** RAK12037 WisBlock sensor mounting

### Hardware

The hardware specification is categorized into five (5) parts. It shows the chipset of the module and discusses the pinouts and their corresponding functions and diagrams. It also covers the electrical and mechanical parameters that include the tabular data of the functionalities and standard values of the RAK12037 WisBlock CO2 Sensor.

#### Chipset

| Vendor    | Part number |
| --------- | ----------- |
| Sensirion | SCD30       |

#### Pin Definition

The RAK12037 WisBlock CO2 Sensor comprises a standard WisBlock connector. The WisBlock connector allows the RAK12037 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 3**.

> **Image:** RAK12037 WisBlock Sensor pinout diagram

:::tip NOTE
- Only the **I2C** related pins, **PWM**, **RDY**, **3V3_S**, and **GND** are connected to this module.
- **3V3_S** voltage output from the WisBlock Base that powers the RAK12037 module can be controlled by the WisBlock Core via `WB_IO2` (WisBlock IO2 pin). This makes the module ideal for low-power IoT projects since the WisBlock Core can totally disconnect the power of the RAK12037 module.
:::

#### Electrical Characteristics
##### Electrical and Sensor Specifications
| Parameter             | Transmission Mode | Value                                   |
| --------------------- | ----------------- | --------------------------------------- |
| Voltage supply        | -                 | 3.3 V ~ 5.5 V                 |
| CO2 measurement range | I2C, PWM          | 0 ~ 40’000 ppm, 0 ~ 5’000 ppm |
| Humidity range        | -                 | 0% ~ 100% RH                       |
| Temperature range     | -                 | -40° C ~ 70° C                |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 4** shows the dimensions and the mechanic drawing of the RAK12037 module.

> **Image:** RAK12037 WisBlock Sensor mechanical drawing

##### WisBlock Connector PCB Layout

> **Image:** WisBlock Connector PCB footprint and recommendations

#### Schematic Diagram

##### SCD30 sensor Related Circuits

The default I2C address of the SCD30 sensor is **1100001**.

Resistors **R2** and **R3** do not need to be mounted on the RAK12037 module due to the pull-up resistors already built-in on the WisBlock Base board.

> **Image:** RAK12037 WisBlock sensor schematics

