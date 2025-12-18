---
slug: /product-categories/wisblock/rak15003/datasheet/
title: RAK15003 WisBlock 32kByte FRAM Module Module Datasheet
description: Provides comprehensive information about your RAK15003 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak15003/rak15003.png"
keywords:
  - datasheet
  - wisblock
  - RAK15003
sidebar_label: Datasheet
---

# RAK15003 WisBlock 32kByte FRAM Module Datasheet

## Overview

> **Image:** RAK15003 WisBlock 32kByte FRAM Module

### Description

RAK15003 is a WisBlock 32kByte FRAM module that extends the WisBlock system with an MB85RC256VPNF-G-JNERE1 memory module from Fujitsu. This module is interfaced via I2C. Additionally, it can be mounted to the sensor slot of the WisBlock Base board.

### Product Features

* **Sensor specifications**
    *  Temperature Range：-40 °C to +85 °C
    *  I2C compatible digital interface, supports 1 MHz
    *  Operating power supply current 200 uA (Max @ 1 MHz)
    *  Standby current 27 uA (Typical)
    *  32,768 words x 8 bits
    *  High Reliability：
       - Read/write endurance：1,000,000,000,000/byte
       - Data retention：
           - 10 years (+85 °C)
           - 95 years (+55 °C)
           - Over 200 years(+35 °C)

* **Size**
    * 10 x 10 mm

## Specifications

### Overview

#### Mounting

**Figure 2** shows the mounting mechanism of the RAK15003 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. The RAK15003 module can be mounted on the slots: **A, C, D, E, & F**.

> **Image:** RAK15003 WisBlock 32kByte FRAM Module Mounting

### Hardware

The hardware specification is categorized into five parts. It shows the chipset of the module and discusses the pinouts, sensors, and the corresponding functions and diagrams. It also covers the electrical and mechanical parameters, including the tabular data of the functionalities and standard values of the RAK15003 WisBlock 32kByte FRAM Module.

#### Chipset

| Vendor    | Part Number            |
| --------- | ---------------------- |
| Fujitsu   | MB85RC256VPNF-G-JNERE1 |

#### Pin Definition

The RAK15003 WisBlock 32kByte FRAM Module comprises a standard WisBlock connector. The WisBlock connector allows the RAK15003 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition are shown in **Figure 3**.

> **Image:** RAK15003 WisBlock 32kByte FRAM Module Pinout Diagram

The **WisBlock Sensor** connector is also compatible for this module. IO used for **WP** pin at **Pin 12** will depend on what sensor slot the module is plugged in. The table below shows the compatible pins used by different sensor slots:

**WP (Write Protect Pin)**

| Slot A | Slot C | Slot D | Slot E | Slot F |
| ------ | ------ | ------ | ------ | ------ |
| IO1    | IO3    | IO5    | IO4    | IO6    |

:::tip NOTE

**RAK15003** should not be plugged in **Slot B**. It is a dedicated slot for **IO2 (WisBlock IO2 pin)** that controls the **3V3_S** voltage output.

:::

#### Electrical Characteristics

##### Recommended Operating Conditions

| Symbol | Description                     | Min. | Nom.   | Max. | Unit |
| ------ | ------------------------------- | ---- | ------ | ---- | ---- |
| VDD    | Power supply for the module     |      | 3.3    |      | V    |
| Isb    | Standby current                 | -    | -      | 27   | uA   |
| Icc    | Supply current, Read            | -    | -      | 200  | uA   |
| Icc    | Supply current, Write           | -    | -      | 200  | uA   |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 4** shows the dimensions and the mechanic drawing of the RAK15003 module.

> **Image:** RAK15003 WisBlock 32kByte FRAM Module Mechanic Drawing

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

#### Schematic Diagram
**Figure 6** shows the schematic of the RAK15003 module.

> **Image:** RAK15003 WisBlock 32kByte FRAM Module schematics

