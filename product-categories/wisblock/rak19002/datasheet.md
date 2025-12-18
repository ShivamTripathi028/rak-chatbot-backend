---
slug: /product-categories/wisblock/rak19002/datasheet/
title: RAK19002 WisBlock Boost Module Datasheet
description: Provides comprehensive information about your RAK19002 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak19002/rak19002.png"
keywords:
  - datasheet
  - wisblock
  - RAK19002
sidebar_label: Datasheet
---

# RAK19002 WisBlock Boost Module Datasheet

## Overview

### Description

The RAK19002 is a step-up boost regulator module, part of the RAKwireless WisBlock Series. The module can supply 12 V/50 mA and could be mounted on the WisSensor slot of RAK5005-O. The output voltage of the module is controlled by **WisBlock Core** IO pin.

### Features

* TPS61046 step-up boost converter
* Input voltage: 3.3 V
* Output voltage: 12 V
* Up to 85% efficiency at 3.6 V input and 12 V output
* ±2 % output voltage accuracy
* 50 mA output current
* Chipset: Texas Instruments TPS61046
* Module size: 10 x 10 mm

## Specifications

### Overview

#### Mounting

The RAK19002 module can be mounted on the slots A, B, C or D of the WisBase board. **Figure 2** shows the mounting mechanism of the RAK19002 on a WisBase module, such as the RAK5005-O.

> **Image:** RAK19002 WisBlock boost module mounting

### Hardware

The hardware specification is categorized into five parts that cover the chipset and pinouts and the corresponding functions and diagrams of the board. It also presents the parameters and their standard values in terms of electrical and mechanical.

####  Chipset
| Vendor            | Part number |
| ----------------- | ----------- |
| Texas Instruments | TPS61046    |

#### Pin Definition

The RAK19002 WisBlock boost module comprises a standard WisSensor connector. The WisSensor connector allows the RAK19002 module to be mounted on a WisBlock baseboard, such as RAK5005-O. The pin order of the connector and the pinout definition is shown in **Figure 3**.

> **Image:** RAK19002 WisBlock Boost Module Pinout

> **Image:** RAK19002 power pins

The following table shows default IO used for different slots:

| SLOT A | SLOT B | SLOT C | SLOT D |
| :----: | :----: | :----: | :----: |
|  IO1   |  IO2   |  IO3   |  IO5   |

:::tip NOTE

- Only one **IO** (as a IC enable pin), **VDD**, and **GND** are connected to this module.
- Connect R1 or R3 resistor to select the **IO** pin. Check the schematic diagram in **Figure 7**.
- The slot B is not recommended because the IO2 pin is used to control power supply 3V3_S on WisBase RAK5005-O.
- The maximum recommended current is 50 mA  ( V<sub>IN</sub>=3.3 V ).

:::

#### Electrical Characteristics

##### Recommended Operating Conditions

| Symbol          | Description                   | Min. | Nom. | Max. | Unit |
| --------------- | ----------------------------- | ---- | ---- | ---- | ---- |
| V<sub>IN</sub>  | Input voltage                 | 2.7  | 3.3  | 3.6  | V    |
| V<sub>OUT</sub> | Output voltage                | -    | 12   | -    | V    |
| I<sub>OUT</sub> | Output current                | -    | -    | 50   | mA   |
| I<sub>SD</sub>  | Shutdown current (IC disable) | -    | -    | 0.8  | µA   |

#### Mechanical Characteristic

##### Board Dimensions

**Figure 5** shows the dimensions and the mechanic drawing of the RAK19002 module.

> **Image:** RAK19002 WisBlock Boost Module Mechanic Drawing

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

#### Schematic Diagram

**Figure 7** shows the schematic of RAK19002 boost module.

> **Image:** RAK19002 WisBlock Boost Module Schematic

