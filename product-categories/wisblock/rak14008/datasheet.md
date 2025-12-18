---
slug: /product-categories/wisblock/rak14008/datasheet/
title: RAK14008 WisBlock Gesture Sensor Module Datasheet
description: Provides comprehensive information about your RAK14008 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisblock/rak14008/rak14008.png
keywords:
  - datasheet
  - wisblock
  - RAK14008
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK14008 WisBlock Gesture Sensor Module Datasheet

## Overview

### Description

RAK14008 is a gesture sensor module based on PAJ7620U2. It is designed for gesture recognition applications with an I2C digital interface. It can recognize nine (9) human hand gesticulations such as moving up, down, left, right, forward, backward, circle-clockwise, circle-counter clockwise, and waving. It also offers built-in proximity detection in sensing approaching or departing objects from the sensor.

### Features

- Gesture speed:
    - 60-600&nbsp;°/s in Normal Mode
    - 60-1200&nbsp;°/s in Gaming Mode
- On-board low noise high PSRR voltage regulator
- Flexible power saving scheme
- I2C interface up to 400 Kbit/s
- Ambient light immunity
- Ambient light noise cancellation
- VBAT：3.2-5.5&nbsp;V
- VCC：2.8-3.3&nbsp;V
- Chipset: PixArt Imaging PAJ7620U2
- Operating Temperature: -40°&nbsp;C ~ 85°&nbsp;C
- Storage Temperature :-40°&nbsp;C ~ 125°&nbsp;C
- Module size: 25 X 15&nbsp;mm

## Specifications

### Overview

#### Mounting

The RAK14008 WisBlock Gesture Sensor Module can be mounted to the IO slot of the [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. **Figure 1** shows the mounting mechanism of the RAK14008 on a WisBlock Base module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14008/datasheet/mounting-mechanism.png"
  figureCount="1"
  caption="RAK14008 mounting mechanism on a WisBlock Base module" 
   width="60%"
/>

### Hardware

The hardware specification is categorized into five (5) parts. It shows the chipset of the module and discusses the pinouts and their corresponding functions and diagrams. It also covers the electrical and mechanical characteristics that include the tabular data of the functionalities and standard values of the RAK14008 WisBlock Module.

####  Chipset

| Vendor         | Part number |
|----------------|-------------|
| PixArt Imaging | PAJ7620U2   |

#### Pin Definition

The RAK14008 WisBlock Gesture Sensor Module comprises a standard WisBlock connector. The WisBlock connector allows the RAK14008 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 2**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14008/datasheet/rak14008_pinout.svg"
  figureCount="2"
  caption="RAK14008 Pinout Diagram" 
   width="70%"
/>

:::tip NOTE
- Only **I2C** related pin, **LDO_EN**, **INT_N**, **VBAT**, **3V3_S**, and **GND** are connected to the WisConnector.
- **3V3_S** voltage output from the WisBlock Base that powers the RAK14008 module can be controlled by the WisBlock Core via WB_IO2 (WisBlock IO2 pin). This makes the module ideal for low-power IoT projects since the WisBlock Core can totally disconnect the power of the RAK14008 module.
:::

#### Electrical Characteristics

This section shows the maximum and minimum ratings of the RAK14008 module and its recommended operating conditions. Refer to the table presented below.

##### Recommended Operating Conditions

| Symbol          | Description             | Min. | Nom. | Max. | Unit |
|-----------------|-------------------------|------|------|------|------|
| V<sub>BAT</sub> | MP20051 supply voltage  | 3.2  | -    | 5.5  | V    |
| 3V3_S           | AJ7620U2 supply voltage | 2.8  | -    | 3.3  | V    |

#### Mechanical Characteristics

##### Board Dimensions

The mechanical dimensions of the RAK14008 module are shown in **Figure 3** below.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14008/datasheet/mech-dimensions.png"
  figureCount="3"
  caption="RAK14008 mechanical dimensions" 
   width="75%"
/>

##### WisConnector PCB Layout

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14008/datasheet/wisconnector-pcb.png"
  figureCount="4"
  caption="WisConnector PCB footprint and recommendations" 
   width="100%"
/>

#### Schematic Diagram

**Figure 5** shows the schematic of the RAK14008 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14008/datasheet/rak14008-schematic.png"
  figureCount="5"
  caption="RAK14008 WisBlock Module schematic" 
   width="100%"
/>

##### VBAT to VLED

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14008/datasheet/vbatvled.png"
  figureCount="6"
  caption="VBAT to VLED" 
   width="50%"
/>

##### PAJ7620U2 Related Circuits

**R6** and **R8** resistors already exist on the WisBlock Base board and are not mounted on the RAK14008 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14008/datasheet/relatedcircuits.png"
  figureCount="7"
  caption="PAJ7620U2 related circuits" 
   width="50%"
/>

#### Gesture Direction

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14008/datasheet/rak14008-gesture.png"
  figureCount="8"
  caption="RAK14008 default direction" 
   width="30%"
/>

The gesture result mapping table for up/down/right/left is shown in the table below:



|               |        | ![rak14008-gesture-1.png](https://images.docs.rakwireless.com/wisblock/rak14008/datasheet/rak14008-gesture-1.png) | ![rak14008-gesture.png](https://images.docs.rakwireless.com/wisblock/rak14008/datasheet/rak14008-gesture.png) | ![rak14008-gesture-2.png](https://images.docs.rakwireless.com/wisblock/rak14008/datasheet/rak14008-gesture-2.png) | ![rak14008-gesture-3.png](https://images.docs.rakwireless.com/wisblock/rak14008/datasheet/rak14008-gesture-3.png) |
|---------------|--------|:-----------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| Bank0_Rcg0x43 | Bit[0] |                                                        Up                                                         |                                                     Left                                                      |                                                       Down                                                        |                                                       Right                                                       |
| Bank0_Rcg0x43 | Bit[1] |                                                       Down                                                        |                                                     Right                                                     |                                                        Up                                                         |                                                       Left                                                        |
| Bank0_Rcg0x43 | Bit[2] |                                                       Left                                                        |                                                     Down                                                      |                                                       Right                                                       |                                                        Up                                                         |
| Bank0_Rcg0x43 | Bit[3] |                                                       Right                                                       |                                                      Up                                                       |                                                       Left                                                        |                                                       Down                                                        |

<RkBottomNav/>
