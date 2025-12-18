---
slug: /product-categories/wisblock/rak12003/datasheet/
title: RAK12003 WisBlock Infrared Temperature Sensor Module Datasheet
description: Provides comprehensive information about your RAK12003 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak12003/rak12003.png"
keywords:
    - RAK12003
    - wisblock
    - datasheet
sidebar_label: Datasheet
---

# RAK12003 WisBlock Infrared Temperature Sensor Module Datasheet

## Overview

> **Image:** RAK12003 WisBlock Infrared Temperature Sensor Module 

### Description

The RAK12003 WisBlock Infrared Temperature Sensor Module is part of the RAKwireless WisBlock Series. It can be used for an accurate contactless thermal measurement for applications such as General purpose industry, temperature control of moving and hard to reach parts, body temperature measurement, non-contact thermometer for mobile and IoT application.

### Features

* **Sensor specifications**
  * I2C interface
  * Object temperatures between -20 °C and 100 °C
  * Accuracy ±0.2° C within the narrow object temperature range from 35 ˚C to 42 ˚C (medical applications)
  * Factory calibrated
  * 50 ° field of view
  * -20 °C to 85 °C operational temperature range
  * Refresh rate configurable between 0.5 Hz to 64 Hz
  * Power Supply Voltage: 3.3 V - 3.6 V
  * Sleep current: < 2.5 µA
  * Chipset: Melexis MLX90632SLD-DCB-000-RE

* **Size**
    * 10 x 10 mm

The refresh rate is the speed that the MLX90632 RAM will be updated with results. It is configurable and the rates are shown in the table below:

| Refresh Rate (Hz) | Time (ms) |
| :---------------: | :-------: |
|        0.5        |   2000    |
|         1         |   1000    |
|         2         |    500    |
|         4         |    250    |
|         8         |    125    |
|        16         |   62.5    |
|        32         |   31.25   |
|        64         |  15.625   |

## Specifications

### Overview

#### Mounting

**Figure 2** shows the mounting mechanism of the RAK12003 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. The RAK12003 module can be mounted on the slots: **A, B, C, D, E, & F**.

> **Image:** RAK12003 WisBlock Infrared Temperature Sensor Mounting

### Hardware

The hardware specification is categorized into five parts that cover the chipset and pinouts and the corresponding functions and diagrams of the board. It also presents the parameters and their standard values in terms of electrical and mechanical.

#### Chipset

| Vendor  |      Part Number       |   **Accuracy**   |
| :-----: | :--------------------: | :--------------: |
| Melexis | MLX90632SLD-DCB-000-RE | Medical accuracy |

> **Image:** Melexis MLX90632 FIR sensor

#### Pin Definition

The RAK12003 WisBlock Infrared Temperature Sensor Module comprises a standard WisBlock connector. The WisBlock connector allows the RAK12003 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 4**.

:::tip NOTE
Only the **I2C** related pins, **VDD**, and **GND** are connected to this module.
:::

> **Image:** RAK12003 WisBlock Infrared Temperature Sensor connector pinout

#### Electrical Characteristics

##### Recommended Operating Conditions

| Symbol           | Description                   | Min. | Nom. | Max. | Unit |
| ---------------- | ----------------------------- | ---- | ---- | ---- | ---- |
| V<sub>DD</sub>   | Power supply for the module   |      | 3.3  | 3.6  | V    |
| I<sub>DDPR</sub> | Sleep current                 |      | 1.5  | 2.5  | µA   |
| I<sub>DD</sub>   | Measure current (normal mode) | 0.5  | 1    | 1.4  | mA   |

#### Mechanical Characteristics

##### Board Dimensions

Figure 5 shows the dimensions and the mechanic drawing of the RAK12003 module.

> **Image:** RAK12003 WisBlock Infrared Temperature Sensor Mechanic Drawing

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

#### Schematic Diagram

> **Image:** RAK12003 WisBlock Infrared Temperature Sensor schematics

:::tip I2C address and pull-up
By default, the ADDR pin is connected to GND, and R1, R2, R3 are not connected. The WisBlock Base board has pull-up resistors and the I2C 7-bit slave address is 0x3a.
:::

