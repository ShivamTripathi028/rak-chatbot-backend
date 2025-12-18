---
slug: /product-categories/wisblock/rak12059/datasheet/
title: RAK12059 WisBlock Liquid Level Sensor Datasheet
description: Provides comprehensive information about your RAK12059 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisblock/rak12059/rak12059.png
keywords:
    - RAK12059
    - wisblock
    - datasheet
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK12059 WisBlock Liquid Level Sensor Datasheet

## Overview

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12059/datasheet/rak12059_front_back.png"
  figureCount="1"
  caption="RAK12059 WisBlock Liquid Level Sensor" 
   width="60%"
/>

### Description

RAK12059 is a WisBlock Liquid Level Sensor module that extends the WisBlock system with a Liquid Level Sensor from MILONE. It comes with a ready-to-use software library and tutorial, making it easy to build a liquid-level data acquisition system. Liquid-level data is interfaced via I2C. Additionally, it can be mounted to the sensor slot of the WisBlock Base board.

### Features

* **Sensor specifications**
    *  Active sensor length of MILONE eTape:
        * 213&nbsp;mm (12110215TC-8TJ)
        * 315&nbsp;mm (12110215TC-12TJ)
        * 618&nbsp;mm (12110215TC-24TJ)
    *  I2C interface
    *  3.3&nbsp;V power supply
    *  eTape operating temperature range：-9&nbsp;°C to +65&nbsp;°C

* **Size**
    * 10 x 23&nbsp;mm

## Specifications

### Overview

#### Mounting

**Figure 2** shows the mounting mechanism of the RAK12059 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. The RAK12059 module can be mounted on the slots: **A, C, D, E, & F**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12059/datasheet/rak19xx_mounting.png"
  figureCount="2"
  caption="RAK12059 WisBlock Liquid Level Sensor Mounting" 
   width="50%"
/>

### Hardware

The hardware specification is categorized into five parts. It shows the module and discusses the pinouts, sensors, and the corresponding functions and diagrams. It also covers the electrical and mechanical parameters, including the tabular data of the functionalities and standard values of the RAK12059 WisBlock Light Sensor.

#### Chipset

| Vendor    | Part Number          |
| --------- | -------------------- |
| MILONE    | Liquid Level Sensor  |

#### Pin Definition

The RAK12059 WisBlock Liquid Level Sensor comprises a standard WisBlock connector. The WisBlock connector allows the RAK12059 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition are shown in **Figure 3**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12059/datasheet/rak12059_pinout.png"
  figureCount="3"
  caption="RAK12059 WisBlock Liquid Level Sensor Pinout Diagram" 
   width="50%"
/>

:::tip NOTE

- **I2C**-related pins, **ALERT**, **3V3_S**, and **GND** are connected to the WisBlock connector.
- **RAK12059** should not be plugged in **Slot B** as it is dedicated for **IO2 (WisBlock IO2 pin)** that controls the **3V3_S** voltage output.

:::

The **WisBlock Sensor** connector is used to this module and the IO used for **ALERT** pin at **Pin 12** will depend on where sensor slot the module is plugged in. The table shows the compatible pins used by different sensor slots:

**ALERT Pin**

| Slot A | Slot C | Slot D | Slot E | Slot F |
| ------ | ------ | ------ | ------ | ------ |
| IO1    | IO3    | IO5    | IO4    | IO6    |

#### Electrical Characteristics

##### Recommended Operating Conditions

| Symbol | Description           | Min. | Nom.   | Max. | Unit |
| ------ | --------------------- | ---- | ------ | ---- | ---- |
| 3V3    | Power Supply Voltage  | -    | 3.3    | -    | V    |


#### Mechanical Characteristics

##### Board Dimensions

**Figure 4** shows the dimensions and the mechanic drawing of the RAK12059 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12059/datasheet/rak19xx_mechanic_drawing.png"
  figureCount="4"
  caption="RAK12059 WisBlock Liquid Level Sensor Mechanic Drawing" 
   width="60%"
/>

##### WisConnector PCB Layout

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12059/datasheet/mxxs1003k6m.png"
  figureCount="5"
  caption="WisConnector PCB footprint and recommendations" 
   width="100%"
/>

#### Schematic Diagram

**Figure 6** shows the schematic of the RAK12059 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12059/datasheet/rak12059-schematic.png"
  figureCount="6"
  caption="RAK12059 WisBlock Liquid Level Sensor schematics" 
   width="100%"
/>



<RkBottomNav/>