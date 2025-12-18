---
slug: /product-categories/wisblock/rak12008/datasheet/
title: RAK12008 WisBlock CO2 Sensor Datasheet
description: Provides comprehensive information about your RAK12008 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak12008/rak12008.png"
keywords:
  - datasheet
  - RAK12008
  - wisblock
sidebar_label: Datasheet
---

# RAK12008 WisBlock CO2 Sensor Datasheet

## Overview

> **Image:** RAK12008 WisBlock Sensor

### Description

RAK12008 is a WisBlock CO<sub>2</sub> Sensor Module that extends the WisBlock system with a Sensirion STC31 CO2 Sensor. The CO<sub>2</sub> concentration data is interfaced via I2C. The STC31 sensor from Sensirion is based on thermal conductivity.

A ready-to-use software library and tutorial is included, making it simple to build a CO<sub>2</sub> gas data acquisition system for high CO<sub>2</sub> concentrations. Additionally, it can be mounted to the sensor slot of the WisBlock Base board.

### Product Features

* **Sensor specifications**
    *  CO<sub>2</sub> sensor module
    *  Based on thermal conductivity
    *  I2C interface
    *  Measurement range：0 to 100 vol%
    *  Accuracy：0.5 vol% + 3% （0 to 25 vol%）；1 vol% + 3%（0 to 100 vol%）
    *  Built-in temperature sensor
    *  Operating temperature range：20 °C to +85 °C

* **Size**
    * 10 x 10 mm

## Specifications

### Overview

#### Mounting

**Figure 1** shows the mounting mechanism of the RAK12008 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. The RAK12008 module can be mounted on the slots: **A, B, C, D, E, & F**.

> **Image:** RAK12008 WisBlock Sensor Mounting

### Hardware

The hardware specification is categorized into six parts. It shows the chipset of the module and discusses the pinouts, sensors, and corresponding functions and diagrams. It also covers the electrical and mechanical parameters, including the tabular data of the functionalities and standard values of the RAK12008 WisBlock Temperature and Humidity Sensor.

#### Chipset
| Vendor    | Part Number |
| --------- | ----------- |
| Sensirion | STC31       |

#### Pin Definition

The RAK12008 WisBlock CO<sub>2</sub> Sensor comprises a standard WisBlock connector. The WisBlock connector allows the RAK12008 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition are shown in **Figure 2**.

> **Image:** RAK12008 WisBlock Sensor Pinout Diagram

:::tip NOTE
Only the **I2C** related pins, **VDD** and **GND** are connected to this module.
:::

#### Sensor Characteristics

##### CO2 Sensor

| Parameter                            | Values                                                |
| ------------------------------------ | ----------------------------------------------------- |
| Calibrated for                       | CO2 in N<sub>2</sub> and CO<sub>2</sub> in Air        |
| Accuracy (based on *Measured Range*) | 0.5 vol% + 3% of measured value (*from 0 to 25 vol%*) |
|                                      | 1 vol% + 3% of measured value (*from 0 to 100 vol%*)  |
| Repeatability                        | 0.2 vol%                                              |
| Temperature stability                | 0.025 vol%                                            |
| Resolution                           | 16 bit                                                |

#### Electrical Characteristics

##### Recommended Operating Conditions

| Symbol | Description        | Condition                            | Min. | Nom. | Max. | Unit |
| ------ | ------------------ | ------------------------------------ | ---- | ---- | ---- | ---- |
| 3V3_S  | Operating  Voltage | Input voltage must within this range | 2.7  | 3.3  | 5.5  | V    |
| IDD1   | Current on 3V3_S   | Measuring                            | -    | 3    | 5    | mA   |
| IDD2   | Current on 3V3_S   | Idle state                           | -    | 50   | -    | uA   |
| IDD3   | Current on 3V3_S   | Sleep mode                           | -    | -    | 1    | uA   |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 3** shows the dimensions and the mechanic drawing of the RAK12008 module.

> **Image:** RAK12008 WisBlock Sensor Mechanic Drawing

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

#### Schematic Diagram
**Figure 5** shows the schematic of the RAK12008 module.

> **Image:** RAK12008 WisBlock Sensor schematics

