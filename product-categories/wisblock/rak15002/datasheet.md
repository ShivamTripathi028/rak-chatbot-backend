---
slug: /product-categories/wisblock/rak15002/datasheet/
title: RAK15002 WisBlock Micro SD Card Module Datasheet
description: Provides comprehensive information about your RAK15002 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak15002/rak15002.png"
keywords:
  - datasheet
  - RAK15002
  - wisblock
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK15002 WisBlock Micro SD Card Module Datasheet

## Overview

### Description

The RAK15002 is a Micro SD card module that can be mounted to the IO slot of the WisBlock Base board. This module uses a 4-line SPI interface to access the SD card and supports the card insert detection feature.

### Features

- Micro SD card socket
- 4-lines SPI interface
- 3.3&nbsp;V power supply
- SD card insert detected
- Module size: 25X35&nbsp;mm

## Specifications

### Overview

#### Mounting

The RAK15002 module can be mounted to the IO slot of the WisBlock Base board. Figure 1 shows the mounting mechanism of the RAK15002 on a WisBlock Base board.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak15002/datasheet/module-mounting.png"
  width="60%"
  caption="RAK15002 WisBlock SD Card Module Mounting"
/>

### Hardware

The hardware specification is categorized into four parts. It discusses the pinouts and its corresponding functions and diagrams. It also covers the electrical and mechanical parameters that include the tabular data of the functionalities and standard values of the RAK15002 WisBlock Micro SD Card Module.

#### Pin Definition

The RAK15002 WisBlock SD Card Module comprises a standard WisConnector. The WisConnector allows the RAK15002 module to be mounted on a WisBlock Base board. The pin order of the connector and the pinout definition is shown in Figure 2.

:::tip NOTE
- **SPI** related pins, **IO6**，**3V3**, and **GND** are connected to this module.
- **IO6**: Insert detected pin, Low active, internal pull-up.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak15002/datasheet/rak15002_pinout.svg"
  width="80%"
  caption="RAK15002 WisBlock SD Card Module Pinout"
/>

#### Electrical Characteristics

##### Recommended Operating Conditions

| Symbol | Description    | Min. | Nom. | Max. | Unit |
| ------ | -------------- | ---- | ---- | ---- | ---- |
| VDD    | Power supply   |      | 3.3  |      | V    |
| IDD    | Supply current | -    | TBD  |      | uA   |

#### Mechanical Characteristic

##### Board Dimensions

Figure 3 shows the dimensions and the mechanic drawing of the RAK15002 WisBlock SD Card Module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak15002/datasheet/mechanic-drawing.png"
  width="70%"
  caption="RAK15002 WisBlock SD Card Module Mechanic Drawing"
/>

##### WisConnector PCB Layout

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak15002/datasheet/footprint.png"
  width="100%"
  caption="WisConnector PCB Footprint and Recommendations"
/>

#### Schematic Diagram

Figure 5 shows the RAK15002 SD Card Module schematic. Only I2C1 related pins, IO6 (insert detection), **3V3**, and **GND** are connected to WisConnector.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak15002/datasheet/module-schematic.png"
  width="70%"
  caption="RAK15002 WisBlock SD Card Module Schematic"
/>

<RkBottomNav/>