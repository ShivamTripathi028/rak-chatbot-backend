---
slug: /product-categories/wisblock/rak12040/datasheet/
title: RAK12040 WisBlock 8x8 IR Sensor Datasheet
description: Provides comprehensive information about your RAK12040 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak12040/rak12040.png"
keywords:
    - RAK12040
    - wisblock
    - datasheet
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK12040 WisBlock 8x8 IR Sensor Datasheet

## Overview

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12040/datasheet/rak12040_front_back.png" 
  caption="RAK12040 WisBlock 8x8 IR Sensor" 
   width="60%"
/>

### Description

RAK12040 is a WisBlock 8x8 IR Sensor Module that extends the WisBlock system with an AMG8833 chip from Panasonic. It comes with a ready-to-use software library and tutorial, making it easy to build a temperature data acquisition system. Temperature data is interfaced via I2C. Additionally, the RAK12040 can be mounted to sensor slot of WisBlock Base board.

### Product Features

* **Sensor specifications**
    *  Based on AMG8833
    *  Temperature detection of two-dimensional area：8x8 (64 pixels)
    *  I2C digital interfaces
    *  3.3&nbsp;V power supply
    *  Operating temperature range：0 to +80&nbsp;°C

* **Size**
    * 10 x 23&nbsp;mm

## Specifications

### Overview

#### Mounting

**Figure 2** shows the mounting mechanism of the RAK12040 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. The RAK12040 module can be mounted on the slots: **A & C**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12040/datasheet/rak19xx_mounting.png" 
  caption="RAK12040 WisBlock 8x8 IR Sensor Mounting" 
   width="50%"
/>

### Hardware

The hardware specification is categorized into five parts. It shows the chipset of the module and discusses the pinouts, sensors, and the corresponding functions and diagrams. It also covers the electrical and mechanical parameters, including the tabular data of the functionalities and standard values of the RAK12040 WisBlock 8x8 IR Sensor.


#### Chipset

| Vendor    | Part Number |
| --------- | ----------- |
| Panasonic | AMG8833     |

#### Pin Definition

The RAK12040 WisBlock 8x8 IR Sensor comprises a standard WisBlock connector. The WisBlock connector allows the RAK12040 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition are shown in **Figure 3**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12040/datasheet/rak12040_pinout.png" 
    caption="RAK12040 WisBlock 8x8 IR Sensor Pinout Diagram" 
   width="40%"
/>

:::tip NOTE

When the RAK12040 is used with other sensor modules powered by **3V3_S** together, it can not be mounted on slot **A**.

:::

#### Electrical Characteristics

##### Recommended Operating Conditions

| Symbol | Description                | Min. | Nom.   | Max. | Unit |
| ------ | -------------------------- | ---- | ------ | ---- | ---- |
| VCC    | Power Supply Voltage       | -    | 3.3    | -    | V    |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 4** shows the dimensions and the mechanic drawing of the RAK12040 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12040/datasheet/rak19xx_mechanic_drawing.png" 
    caption="RAK12040 WisBlock 8x8 IR Sensor Mechanic Drawing" 
   width="60%"
/>

##### WisConnector PCB Layout

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12040/datasheet/mxxs1003k6m.png" 
    caption="WisConnector PCB footprint and recommendations" 
   width="100%"
/>

#### Schematic Diagram

**Figure 6** shows the schematic of the RAK12040 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12040/datasheet/rak12040-schematic.png" 
    caption="RAK12040 WisBlock 8x8 IR Sensor schematics" 
   width="100%"
/>



<RkBottomNav/>