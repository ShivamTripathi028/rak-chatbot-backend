---
slug: /product-categories/wisblock/rak12020/datasheet/
title: RAK12020 WisBlock Light Sensor Datasheet
description: Provides comprehensive information about your RAK12020 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak12020/rak12020.png"
keywords:
  - datasheet
  - wisblock
  - RAK12020
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK12020 WisBlock Light Sensor Datasheet

## Overview

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12020/datasheet/rak12020_front_back.png"
  width="60%"
  caption="RAK12020 WisBlock Light Sensor"
/>

### Description

RAK12020 is a WisBlock Light Sensor module that extends the WisBlock system with an AMS TSL25911FN Light Sensor. It comes with a ready-to-use software library and tutorial, making it simple to build an ambient light-intensity data acquisition system.

The ambient light intensity data is interfaced via I2C. Additionally, RAK12020 can be mounted to the sensor slot of the WisBlock Base board.

### Product Features

* **Sensor specifications**
    *  Very high sensitivity light-to-digital converter
    *  Approximates human eye response
    *  I2C interface
    *  Two internal interrupt source
    *  Low power 3.0&nbsp;uA sleep state
    *  3.3&nbsp;V power supply

* **Size**
    * 10 x 10&nbsp;mm

## Specifications

### Overview

#### Mounting

**Figure 2** shows the mounting mechanism of the RAK12020 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. The RAK12020 module can be mounted on the slots: **A, C, D, E & F**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12020/datasheet/rak19xx_mounting.png"
  width="50%"
  caption="RAK12020 WisBlock Light Sensor Mounting"
/>

### Hardware

The hardware specification is categorized into five parts. It shows the chipset of the module and discusses the pinouts, sensors, and the corresponding functions and diagrams. It also covers the electrical and mechanical parameters, including the tabular data of the functionalities and standard values of the RAK12020 WisBlock Light Sensor.

#### Chipset

| Vendor    | Part Number |
| --------- | ----------- |
| AMS       | TSL25911FN  |

#### Pin Definition

The RAK12020 WisBlock Light Sensor comprises a standard WisBlock connector. The WisBlock connector allows the RAK12020 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 3**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12020/datasheet/rak12020_pinout.png"
  width="40%"
  caption="RAK12020 WisBlock Light Sensor Pinout Diagram"
/>

:::tip NOTE

Only the **I2C**-related pins, **VDD**, and **GND** are connected to this module. **INT** pin is the interrupt output.

:::

**INT** pin at **Pin 12/13** will depend on where sensor slot the module is plugged in. The table shows the compatible pins used by different sensor slots:

**INT (Interrupt Output Pin)**

| Slot A | Slot C | Slot D | Slot E | Slot F | 
| ------ | ------ | ------ | ------ | ------ |
| IO1    | IO3    | IO5    | IO4    | IO6    | 

#### Electrical Characteristics

##### Recommended Operating Conditions

| Symbol | Description                |  b  Condition                                            | Min. | Nom.   | Max. | Unit |
| ------ | -------------------------- | ---------------------------------------------------- | ---- | ------ | ---- | ---- |
| 3V3_S  | Operating Voltage          | Input voltage must within this range                 | 2.7  | 3.3    | 3.6  | V    |
| Isd    | Shutdown current           | Sleep state - no I2C activity                        | -    | 2.3    | 4    | uA   |
| IDD    | Operation mode current     | Active                                               | -    | 275    | 325  | uA   |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 4** shows the dimensions and the mechanic drawing of the RAK12020 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12020/datasheet/rak19xx_mechanic_drawing.png"
  width="60%"
  caption="RAK12020 WisBlock Light Sensor Mechanic Drawing"
/>

##### WisConnector PCB Layout

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12020/datasheet/mxxs1003k6m.png"
  width="100%"
  caption="WisConnector PCB footprint and recommendations"
/>

#### Schematic Diagram
**Figure 6** shows the schematic of the RAK12020 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12020/datasheet/rak12020-schematic.png"
  width="100%"
  caption="RAK12020 WisBlock Light Sensor schematics"
/>





<RkBottomNav/>