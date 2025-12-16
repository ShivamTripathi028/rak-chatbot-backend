---
slug: /product-categories/wisblock/rak17001/datasheet/
title: RAK17001 WisBlock H-Bridge Module Datasheet
description: Provides comprehensive information about your RAK17001 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak17001/rak17001.png"
keywords:
    - RAK17001
    - wisblock
    - datasheet
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK17001 WisBlock H-Bridge Module Datasheet

## Overview

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak17001/datasheet/rak17001_front_back.png" 
  figureCount="1"
  caption="RAK17001 WisBlock H-Bridge Module" 
   width="60%"
/>

### Description

RAK17001 is a WisBlock H-Bridge module which extends the WisBlock system with a STSPIN250 DC motor drive module from ST. It can drive dc motor and can be used as a PWM controller. Additionally, it can be mounted to IO slot of WisBlock Base board.

### Features

* **Sensor specifications**
    *  DC motor drive module
    *  Operating voltage from 1.8&nbsp;V to 10&nbsp;V
    *  Maximum output current 2.6&nbsp;Arms
    *  Full protection set

* **Size**
    * 25 x 35&nbsp;mm

## Specifications

### Overview

#### Mounting

**Figure 2** shows the mounting mechanism of the RAK17001 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. The RAK17001 module can be mounted on the IO slots.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak17001/datasheet/rak19xx_mounting.png" 
  figureCount="2"
  caption="RAK17001 WisBlock H-Bridge Module Mounting" 
   width="50%"
/>

### Hardware

The hardware specification is categorized into five parts. It shows the chipset of the module and discusses the pinouts, sensors, and the corresponding functions and diagrams. It also covers the electrical and mechanical parameters, including the tabular data of the functionalities and standard values of the RAK17001 WisBlock H-Bridge Module.

#### Chipset

| Vendor    | Part Number |
| --------- | ----------- |
| ST        | STSPIN250   |

#### Pin Definition

The RAK17001 WisBlock H-Bridge Module comprises a standard WisBlock connector. The WisBlock connector allows the RAK17001 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition are shown in **Figure 3**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak17001/datasheet/rak17001_pinout.png" 
  figureCount="3"
  caption="RAK17001 WisBlock H-Bridge Module Pinout Diagram" 
   width="50%"
/>

:::tip NOTE
 - **PWM**, **PH**, and **FAULT_CKECK,EN** are connected to WisIO connector.
 - **RESET** is not used by default. There is a reserved resistance for users.
 - **3V3_S** is used by default for STSPIN250's logic input voltage. There is a reserved resistance for users to change to **3V3**.
:::

#### Electrical Characteristics

##### Absolute Maximum Ratings

| Parameter                      | Minimum | Maximum | Unit |
| ------------------------------ | ------- | ------- | ---- |
| 3V3_S                          | - 0.3   | 5.5     | V    |
| VM(STSPIN250's Supply Voltage) | - 0.3   | 11      | V    |

##### Power Supply Ratings

| Symbol | Description                     | Condition                               | Min. | Nom.   | Max. | Unit |
| ------ | ------------------------------- | --------------------------------------- | ---- | ------ | ---- | ---- |
| 3V3_S  | Supply voltage                  | Input voltage must within this range    | -    | 3.3    | -    | V    |
| Vbat   | Vbat power supply STSPIN250     | normal operation                        | -    | -      | 4.2  | V    |
| Vin    | External power supply STSPIN250 | normal operation                        | 1.8  | -      | 10   | V    |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 4** shows the dimensions and the mechanic drawing of the RAK17001 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak17001/datasheet/rak19xx_mechanic_drawing.png" 
  figureCount="4"
  caption="RAK17001 WisBlock H-Bridge Module Mechanic Drawing" 
   width="60%"
/>

##### WisConnector PCB Layout

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak17001/datasheet/mxxs1003k6m.png" 
  figureCount="5"
  caption="WisConnector PCB footprint and recommendations" 
   width="100%"
/>

#### Schematic Diagram

**Figure 6** shows the schematic of the RAK17001 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak17001/datasheet/rak17001-schematic.png" 
  figureCount="6"
  caption="RAK17001 WisBlock H-Bridge Module schematics" 
   width="100%"
/>


<RkBottomNav/>
