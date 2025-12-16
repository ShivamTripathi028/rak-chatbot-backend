---
slug: /product-categories/wisblock/rak1905/datasheet/
title: RAK1905 WisBlock 9-Axis Sensor Module Datasheet
description: Provides comprehensive information about your RAK1905 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak1905/rak1905.png"
keywords:
  - datasheet
  - wisblock
  - RAK1905
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK1905 WisBlock 9-Axis Sensor Module Datasheet

## Overview


### Description

RAK1905 is a 3-axis gyroscope, 3-axis accelerometer, and 3-axis magnetometer, part of the RAKwireless WisBlock Sensor series. It is based on MPU-9250 from TDK and designed for 9-axis motion tracking. The data can be obtained via I2C interface.

### Features

- Chipset: **TDK MPU-9250**
- Supply voltage: **3.3&nbsp;V**
- Current consumption: **8&nbsp;uA - 2.7&nbsp;mA**
- Accelerometer output: **±2&nbsp;g**, **±4&nbsp;g**, **±8&nbsp;g**, and **±16&nbsp;g**
- Gyroscope output: **±250**, **±500**, **±1000**, and **±2000&nbsp;°/sec**
- 16-bit ADCs
- Magnetometer full-scale measurement range: **±4800&nbsp;µT**
- Digital Motion Processor (DMP)
- I2C Interface
- Module size: **10&nbsp;mm x 10&nbsp;mm**

## Specifications

### Overview

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1905/datasheet/rak1905-overview.png"
  figureCount="1"
  caption="RAK1905 WisBlock 9-Axis Sensor Module top and bottom view" 
   width="35%"
/>



#### Mounting

**Figure 2** shows the mounting mechanism of the RAK1905 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. The RAK1905 module can be mounted on the slots: **A, B, C, D, E, & F**.


<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1905/datasheet/rak1905-mounting.png"
  figureCount="2"
  caption="RAK1905 WisBlock 9-Axis Module mounting" 
   width="50%"
/>

### Hardware

The hardware specification is categorized into five parts. It presents the chipset of the module and the pinouts and their corresponding functions and diagrams of the module. It also covers the electrical and mechanical characteristics that include the tabular data of the functionalities and standard values of the RAK1905 9-Axis Sensor Module.

#### Chipset

| Vendor | Part Number |
| ------ | ----------- |
| TDK    | MPU-9250    |

#### Pin Definition

The RAK1905 9-Axis Sensor WisBlock Module comprises a standard WisBlock connector. The WisBlock connector allows the RAK1905 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 3**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1905/datasheet/rak1905-pinout.png"
  figureCount="3"
  caption="RAK1905 WisBlock 9-Axis Sensor Module pinout" 
   width="60%"
/>

:::tip NOTE
**I2C** related pins, **INT**, **VDD33**, and **GND** are connected to WisBlock Sensor connector.
:::

If a 24-pin WisBlock Sensor connector is used, the IO used for the output pulse depends on what slot the module is plugged in. The following table shows the default IO used for different slots:

**INT (Interrupt Pin)**

| SLOT A | SLOT B | SLOT C | SLOT D | SLOT E | SLOT F |
| ------ | ------ | ------ | ------ | ------ | ------ |
| IO1    | IO2    | IO3    | IO5    | IO4    | IO6    |

:::tip NOTE
If there are other sensor modules connected on the base other than RAK1905 and are using the configurable 3V3_S voltage source, you cannot use SLOT B since 3V3_S is controlled via WB_IO2 pin.
:::

#### Electrical Characteristics

| Symbol | Description                                                                                | Min. | Nom. | Max. | Unit |
| ------ | ------------------------------------------------------------------------------------------ | ---- | ---- | ---- | ---- |
| VDD    | Power supply voltage                                                                       | -    | 3.3  | -    | V    |
| IDD    | 9-axis (no DMP), 1&nbsp;kHz gyro ODR, 4&nbsp;kHz accel ODR, 8&nbsp;Hz mag. repetition rate | -    | 2.7  | -    | mA   |
| IDDL   | Full Chip Idle Mode supply current                                                         | -    | 8    | -    | uA   |

#### Mechanical Characteristics

##### Board Dimensions

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1905/datasheet/mech-dimension.png"
  figureCount="4"
  caption="RAK1905 WisBlock 9-Axis Module mechanical drawing" 
   width="60%"
/>

##### WisBlock Connector PCB Layout

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1905/datasheet/pcb-footprint.png"
  figureCount="5"
  caption="WisBlock Connector PCB footprint and recommendations" 
   width="100%"
/>

#### Schematic Diagram

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1905/datasheet/rak1905-schematic.png"
  figureCount="6"
  caption="RAK1905 WisBlock 9-Axis Sensor Module schematic diagram" 
   width="100%"
/>

<RkBottomNav/>

