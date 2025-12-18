---
slug: /product-categories/wisblock/rak12054/datasheet/
title: RAK12054 WisBlock Encoder Sensor Datasheet
description: Provides comprehensive information about your RAK12054 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisblock/rak12054/rak12054.png
keywords:
    - RAK12054
    - wisblock
    - datasheet
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK12054 WisBlock Encoder Sensor Datasheet

## Overview

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12054/datasheet/rak12054_front_back.png"
  figureCount="1"
  caption="RAK12054 WisBlock Encoder Sensor" 
   width="60%"
/>

### Description

RAK12054 is a WisBlock Encoder Sensor module that extends the WisBlock system with an AS5600-ASOT Encoder Sensor from OSRAM. It comes with a ready-to-use software library and tutorial, making it easy to build a magnetic rotary position data acquisition system. Magnetic rotary position data is interfaced via I2C. Additionally, it can be mounted to sensor slot of WisBlock Base board.

### Product Features

* **Sensor specifications**
    *  Based on AS5600-ASOT
    *  Contactless angle measurement
    *  Simple user-programmable start and stop positions over the I2C interface
    *  Maximum angle programmable from 18° up to 360°
    *  Automatic magnet detection
    *  3.3&nbsp;V power supply
    *  Operating temperature range：-40&nbsp;°C to +85&nbsp;°C

* **Size**
    * 10 x 10&nbsp;mm

## Specifications

### Overview

#### Mounting

**Figure 2** shows the mounting mechanism of the RAK12054 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. The RAK12054 module can be mounted on the slots: **A, C, D, E, & F**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12054/datasheet/rak19xx_mounting.png"
  figureCount="2"
  caption="RAK12054 WisBlock Encoder Sensor Mounting" 
   width="50%"
/>

### Hardware

The hardware specification is categorized into five parts. It shows the chipset of the module and discusses the pinouts, sensors, and the corresponding functions and diagrams. It also covers the electrical and mechanical parameters, including the tabular data of the functionalities and standard values of the RAK12054 WisBlock Encoder Sensor.

#### Chipset
| Vendor    | Part Number |
| --------- | ----------- |
| OSRAM     | AS5600-ASOT |

#### Pin Definition

The RAK12054 WisBlock Encoder Sensor comprises a standard WisBlock connector. The WisBlock connector allows the RAK12054 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition are shown in **Figure 3**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12054/datasheet/rak12054_pinout.png"
  figureCount="3"
  caption="RAK12054 WisBlock Encoder Sensor Pinout Diagram" 
   width="40%"
/>

:::tip NOTE

When the RAK12054 is used with other sensor modules powered by **3V3_S** together, it can not be mounted on slot **B**.

:::

The **WisBlock Sensor** connector is used to this module and the IO used for **OUT_1** pin at **Pin 12** will depend on where sensor slot the module is plugged in. The table shows the compatible pins used by different sensor slots:

**OUT_1 Pin**

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

**Figure 4** shows the dimensions and the mechanic drawing of the RAK12054 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12054/datasheet/rak19xx_mechanic_drawing.png"
  figureCount="4"
  caption="RAK12054 WisBlock Encoder Sensor Mechanic Drawing" 
   width="60%"
/>

##### WisConnector PCB Layout

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12054/datasheet/mxxs1003k6m.png"
  figureCount="5"
  caption="WisConnector PCB footprint and recommendations" 
   width="100%"
/>

#### Schematic Diagram

**Figure 6** shows the schematic of the RAK12054 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12054/datasheet/rak12054-schematic.png"
  figureCount="6"
  caption="RAK12054 WisBlock Encoder Sensor schematics" 
   width="100%"
/>

 

<RkBottomNav/>