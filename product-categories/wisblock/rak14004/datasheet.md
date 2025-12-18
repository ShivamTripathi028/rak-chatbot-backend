---
slug: /product-categories/wisblock/rak14004/datasheet/
title: RAK14004 WisBlock Keypad Module Datasheet
description: Provides comprehensive information about your RAK14004 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisblock/rak14004/rak14004.png
keywords:
  - datasheet
  - wisblock
  - RAK14004
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK14004 WisBlock Keypad Module Datasheet

## Overview

### Description

**RAK14004 WisBlock Keypad Module** was designed to be part of a production-ready IoT solution in a modular way and must be combined with a **WisBlock Core** and a **WisBlock Base** module.

The RAK14004 module is designed as an IO extension module that allows to add a keypad and create a customized IoT solution. This module can be used in conjunction with RAK14009, RAK14010, or RAK14011 keypad modules.

### Features

* **Module Specifications**

  * Up to 8 x 8 buttons using scan matrix arrangement
  * 3.3&nbsp;V Power supply
  * Chipset: Microchip ATMEGA328PB-AU

* **Size**
    * 35&nbsp;mm x 25&nbsp;mm

## Specifications

### Overview

**Figure 1** and **Figure 2** show the RAK14004 top and bottom view of the RAK14004 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14004/datasheet/rak14004_top-view.svg"
  width="30%"
  caption="RAK14004 top view"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14004/datasheet/rak14004_bottom-view.svg"
  width="30%"
  caption="RAK14004 bottom view"
/>

#### Mounting

The RAK14004 module can be mounted on the IO slot of the WisBlock Base board. **Figure 3** shows the mounting mechanism of the RAK14004 on a WisBlock Base module, such as a RAK5005-O.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14004/datasheet/image-20210225140319101.png"
  width="60%"
  caption="RAK14004 mounting mechanism on a WisBlock Base module"
/>
### Hardware

The hardware specification is categorized into five parts. It shows the chipset of the module and discusses the pinouts and their corresponding functions and diagrams. It also covers the electrical and mechanical parameters that include the tabular data of the functionalities and standard values of the RAK14004 WisBlock Keypad Module.

#### Chipset

| Vendor    | Part number    |
| --------- | -------------- |
| Microchip | ATMEGA328PB-AU |


#### Pin Definition

The RAK14004 comprises a standard WisBlock IO 40-pin connector. The WisBlock IO connector allows the RAK14004 module to be mounted on a WisBlock Base Board, such as RAK5005-O. The pin order of the connector and the pinout definition is shown in **Figure 4**.


:::tip NOTE
 **I2C** related pins, **UART** related pins, **INT**, **RESET**, **3V3**, and **GND** are connected to 40-pin WisBlock IO connector.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14004/datasheet/rak14004_pinouts.svg"
  width="60%"
  caption="RAK14004 Pin Definition"
/>





#### Electrical Characteristics


##### Power Supply Ratings

| Symbol | Description  | Min. | Nom. | Max. | Unit |
| ------ | ------------ | ---- | ---- | ---- | ---- |
| VDD    | Power supply | 1.8  | 3.3  | 5.5  | V    |



#### Mechanical Characteristics

##### Board Dimensions

**Figure 5** shows the dimensions and the mechanic drawing of the RAK14004 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14004/datasheet/image-20210717131126045.png"
  width="75%"
  caption="RAK14004 Mechanical Dimensions"
/>

##### WisConnector PCB Layout

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14006/datasheet/pcb-layout.png"
  width="100%"
  caption="WisConnector PCB footprint and recommendations"
/>

#### Schematic Diagram

The RAK14004 uses a Microchip ATMEGA328PB-AU microcontroller for matrix keyboard scanning and identification. A cable is used to connect RAK14004 to keypad modules such as RAK14009.

##### MCU Schematic


<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14004/datasheet/u1-mcu.png"
  width="60%"
  caption="MCU schematic"
/>

##### I2C Pull Up Resistor

The I2C Pull Up Resistor already exists on WisBlock Base Board. **R7** and **R8** are not mounted on the RAK14004 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14004/datasheet/i2c-pup.png"
  width="40%"
  caption="I2C Pull Up Resistor"
/>


##### MCU Debug

**J3** is the MCU debug connector.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14004/datasheet/j3-debug.png"
  width="30%"
  caption="MCU Debug connector"
/>

:::warning
Do not connect to this header or you lose the warranty and your RAK14004 will not work anymore.
:::


##### Matrix Buttons Module Connector

**J2** Matrix Buttons connector is used to connect RAK14004 to keypad modules such as RAK14009, RAK14010, and RAK14011.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14004/datasheet/image-20210728143632190.png"
  width="40%"
  caption="Matrix Buttons Connector"
/>

##### Full schematic

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14004/datasheet/rak14004-sch1.png"
  width="100%"
  caption="RAK14004 Schematic Diagram Part 1"
/>


<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14004/datasheet/rak14004-sch2.png"
  width="100%"
  caption="RAK14004 Schematic Diagram Part 2"
/>

<RkBottomNav/>