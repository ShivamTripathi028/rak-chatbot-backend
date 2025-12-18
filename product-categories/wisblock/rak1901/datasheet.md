---
slug: /product-categories/wisblock/rak1901/datasheet/
title: RAK1901 WisBlock Temperature and Humidity Sensor Datasheet
description: Provides comprehensive information about your RAK1901 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak1901/rak1901.png"
keywords:
  - datasheet
  - wisblock
  - RAK1901
sidebar_label: Datasheet
---

# RAK1901 WisBlock Temperature and Humidity Sensor Datasheet

## Overview

> **Image:** RAK1901 WisBlock Sensor

### Description

RAK1901 is a WisBlock Sensor that extends the WisBlock system with a Sensirion SHTC3 temperature and humidity sensor. A ready-to-use SW library and tutorial make it easy to build up an environmental temperature and humidity data acquisition system.

### Features
* **Temperature sensor accuracy**: ±0.2° C
* **Temperature range**:  -40° C to +125° C
* **Humidity sensor accuracy**:±2.0% RH
* **Humidity range**:0 to 100%
* **Voltage Supply**: 3.3 V
* **Current Consumption**: 0.3 uA to 270 uA
* **Chipset**: Sensirion SHTC3
* **Module size**: 10 x 10 mm

## Specifications

### Overview

#### Mounting

**Figure 2** shows the mounting mechanism of the RAK1901 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. The RAK1901 module can be mounted on the slots: **A, B, C, D, E, & F**.

> **Image:** RAK1901 WisBlock Sensor Mounting

### Hardware

The hardware specification is categorized into six parts. It shows the chipset of the module and discusses the pinouts, sensors, and the corresponding functions and diagrams. It also covers the electrical and mechanical parameters that include the tabular data of the functionalities and standard values of the RAK1901 WisBlock Temperature and Humidity Sensor.

#### Chipset
| Vendor    | Part number |
| --------- | ----------- |
| Sensirion | SHTC3       |

#### Pin Definition

The RAK1901 WisBlock Temperature and Humidity Sensor comprises a standard WisBlock connector. The WisBlock connector allows the RAK1901 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 3**.

> **Image:** RAK1901 WisBlock Sensor Pinout Diagram

:::tip NOTE
Only the **I2C** related pins, **VDD** and **GND** are connected to this module.
:::

If a 24-pin WisBlock Sensor connector is used, the IO used for the output pulse depends on what slot the module is plugged in. The following table shows the default IO used for different slots:

| SLOT A | SLOTB  | SLOT C | SLOT D | SLOT E | SLOT F |
| ------ | ------ | ------ | ------ | ------ | ------ |
| WB_IO1 | WB_IO2 | WB_IO3 | WB_IO5 | WB_IO4 | WB_IO6 |

#### Sensors
##### Temperature Sensor

| Parameter          | Conditions |    Value    | Units |
| ------------------ | :--------: | :---------: | :---: |
| Accuracy Tolerance |    Typ.    |    ±0.2     |  °C   |
| Repeatability      |     -      |     0.1     |  °C   |
| Resolution         |     -      |    0.01     |  °C   |
| Specified Range    |     -      | -40 to +125 |  °C   |
| Response Time      |   τ 63%    |  <5 to 30   |   s   |
| Long-term Drift    |    Typ.    |    <0.2     | °C/y  |

###### Humidity Sensor
| Parameter          | Conditions |  Value   | Units |
| ------------------ | :--------: | :------: | :---: |
| Accuracy Tolerance |    Typ.    |   ±0.2   |  %RH  |
| Repeatability      |     -      |   0.1    |  %RH  |
| Resolution         |     -      |   0.01   |  %RH  |
| Hysteresis         |     -      |    ±1    |  %RH  |
| Specified Range    |  extended  | 0 to 100 |  %RH  |
| Response Time      |   τ 63%    |    8     |   s   |
| Long-term Drift    |    Typ.    |  <0.25   | %RH/y |

#### Electrical Characteristics
##### Recommended Operating Conditions
| Symbol            | Description                      | Min | Nom. | Max | Unit |
| ----------------- | -------------------------------- | :-: | :--: | :-: | :--: |
| V<sub>DD</sub>    | Power supply for the module      | 1.6 | 3.3  | 3.6 |  V   |
| I<sub>sleep</sub> | Sleep current                    |  -  | 0.3  |  -  |  uA  |
| I<sub>DD</sub>    | Measure current (normal mode)    |  -  | 430  |     |  uA  |
| I<sub>DD</sub>    | Measure current (low-power mode) |  -  | 270  |  -  |  uA  |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 4** shows the dimensions and the mechanic drawing of the RAK1901 module.

> **Image:** RAK1901 WisBlock Sensor Mechanic Drawing

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

#### Schematic Diagram
**Figure 5** shows the schematic of the RAK1901 module.

> **Image:** RAK1901 WisBlock Sensor schematics

