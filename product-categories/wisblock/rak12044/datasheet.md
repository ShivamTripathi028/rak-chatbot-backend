---
slug: /product-categories/wisblock/rak12044/datasheet/
title: RAK12044 WisBlock Hall Effect Sensor Datasheet
description: Provides comprehensive information about your RAK12044 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisblock/rak12044/rak12044.png
keywords:
    - RAK12044
    - wisblock
    - datasheet
sidebar_label: Datasheet
---

# RAK12044 WisBlock Hall Effect Sensor Datasheet

## Overview

> **Image:** RAK12044 WisBlock Hall Effect Sensor

### Description

RAK12044 is a WisBlock Hall Effect Sensor module that extends the WisBlock system with a DRV5056A4QDBZR Hall Sensor from Texas Instruments. It comes with a ready-to-use software library and tutorial, making it easy to build a magnetic field data acquisition system. Magnetic field data is interfaced via I2C. Additionally, the RAK12044 can be mounted to the sensor slot of the WisBlock Base board.

### Product Features

* **Sensor specifications**
    *  Based on DRV5056A4QDBZR
    *  Magnetic sensitivity options：15 mV/mT, 155-mT range
    *  I2C digital interfaces
    *  3.3 V power supply
    *  Operating Temperature Range：-40 °C to +80 °C

* **Size**
    * 10 x 10 mm

## Specifications

### Overview

#### Mounting

**Figure 2** shows the mounting mechanism of the RAK12044 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. The RAK12044 module can be mounted on the slots: **A, C, D, E, & F**.

> **Image:** RAK12044 WisBlock Hall Effect Sensor Mounting

### Hardware

The hardware specification is categorized into five parts. It shows the chipset of the module and discusses the pinouts, sensors, and the corresponding functions and diagrams. It also covers the electrical and mechanical parameters, including the tabular data of the functionalities and standard values of the RAK12044 WisBlock Hall Effect Sensor.

#### Chipset
| Vendor            | Part Number    |
| ----------------- | -------------- |
| Texas Instruments | DRV5056A4QDBZR |

#### Pin Definition

The RAK12044 WisBlock Hall Effect Sensor comprises a standard WisBlock connector. The WisBlock connector allows the RAK12044 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition are shown in **Figure 3**.

> **Image:** RAK12044 WisBlock Hall Effect Sensor Pinout Diagram

:::tip NOTE

When the RAK12044 is used with other sensor modules powered by **3V3_S** together, it can not be mounted on slot **B**.

:::

The **WisBlock Sensor** connector is used to this module and the IO used for **ALERT** pin at **Pin 12** will depend on where sensor slot the module is plugged in. The table shows the compatible pins used by different sensor slots:

**ALERT Pin**

| Slot A | Slot C | Slot D | Slot E | Slot F |
| ------ | ------ | ------ | ------ | ------ |
| IO1    | IO3    | IO5    | IO4    | IO6    |

#### Electrical Characteristics

##### Recommended Operating Conditions

| Symbol | Description                | Min. | Nom.   | Max. | Unit |
| ------ | -------------------------- | ---- | ------ | ---- | ---- |
| 3V3_S  | Power Supply Voltage       | -    | 3.3    | -    | V    |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 4** shows the dimensions and the mechanic drawing of the RAK12044 module.

> **Image:** RAK12044 WisBlock Hall Effect Sensor Mechanic Drawing

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

#### Schematic Diagram

**Figure 6** shows the schematic of the RAK12044 module.

> **Image:** RAK12044 WisBlock Hall Effect Sensor schematics

