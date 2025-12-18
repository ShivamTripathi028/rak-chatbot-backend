---
slug: /product-categories/wisblock/rak12052/datasheet/
title: RAK12052 WisBlock Thermal IR Array Module Datasheet
description: Provides comprehensive information about your RAK12052 WisBlock Thermal IR Array Module to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisblock/rak12052/rak12052.png
keywords:
    - RAK12052
    - wisblock
    - datasheet
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK12052 WisBlock Thermal IR Array Module Datasheet

## Overview

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12052/datasheet/rak12052-front-back.png" 
  figureCount="1"
  caption="RAK12052 WisBlock Thermal IR Array Module" 
   width="60%"
/>

### Description

**RAK12052** is a 32&nbsp;x&nbsp;24 thermal IR array module based on MLX90640 from Melexis. MLX90640 is a fully-calibrated 32&nbsp;x&nbsp;24 pixels thermal IR array in an industry-standard 4-lead TO39 package with a digital interface. The MLX90640 contains 768&nbsp;FIR pixels. An ambient sensor is integrated to measure the ambient temperature of the chip, and a supply sensor to measure the VDD. The outputs of all sensors IR, Ta, and VDD are stored in internal RAM and accessible through I2C. It is comparable in having a thermal camera (or Predator's vision) but in compact but useable low resolution.

### Applications

- High precision non-contact temperature measurements
- Intrusion or Movement Detection
- Presence Detection or Person Localization
- Temperature sensing element for intelligent building air conditioning
- Thermal Comfort Sensor in automotive air conditioning control system
- Microwave oven
- Industrial temperature control of moving parts
- Visual IR thermometers

### Features

**Module Specifications**
- Easy to integrate
- Factory calibrated
- Noise Equivalent Temperature Difference (NETD) 0.1K&nbsp;RMS @ 1&nbsp;Hz refresh rate
- I2C compatible digital interface
- FOV options – 55°&nbsp;x&nbsp;35°
- Current consumption less than 23&nbsp;mA
- Power Supply：3.3&nbsp;V
- Operating Temperature: -40°&nbsp;C ~ 80°&nbsp;C

## Specifications

### Mounting

#### Mounting to WisBlock Base

The RAK12052 32&nbsp;x&nbsp;24 IR module can be mounted to the IO slot of the WisBlock base board. **Figure 2** shows the mounting mechanism of the RAK12052 on a WisBlock Base Board module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12052/datasheet/rak12052_mount_to_wisbase.png" 
  figureCount="2"
  caption="RAK12052 WisBlock Thermal IR Array Module Mounting" 
   width="50%"
/>

### Hardware

The hardware specification is categorized into five (5) parts. It shows the chipset of the module and discusses the pinouts, and their corresponding functions and diagrams. It also covers the electrical and mechanical parameters that include the tabular data of the functionalities and standard values of RAK12052 WisBlock Thermal IR Array Module.

#### Chipset

| Vendor  | Part Number                                                                                  |
| ------- | -------------------------------------------------------------------------------------------- |
| Melexis | [MLX90640](https://www.melexis.com/en/documents/documentation/datasheets/datasheet-mlx90640) |

#### Pin Definition

The RAK12052 WisBlock 32&nbsp;x&nbsp;24 IR module comprises a standard WisBlock IO slot connector. The WisBlock IO slot connector allows the RAK12052 module to be mounted to a WisBlock Base Board module. The pin order of the connector and the pinout definition is shown in **Figure 3**.

:::tip NOTE

**I2C** related pins, **3V3_S**, and **GND** are connected to WisBlock IO slot connector.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12052/datasheet/rak12052_pinout.png" 
  figureCount="3"
  caption="RAK12052 WisBlock Thermal IR Array Module Pinout" 
   width="60%"
/>

#### Electrical Characteristics

This table shows the RAK12052 module electrical characteristics.

| **Symbol** | Description          | **Min.** | **Nom.** | **Max.** | **Unit** |
| ---------- | -------------------- | -------- | -------- | -------- | -------- |
| 3V3_S      | Power Supply Voltage | -        | 3.3      |          | V        |


#### Mechanical Characteristic

##### Board Dimensions

**Figure 4** shows the dimensions and the mechanical drawing of the RAK12052 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12052/datasheet/rak12052_mechanic_drawing.png" 
  figureCount="4"
  caption="RAK12052 WisBlock Thermal IR Array Module Mechanical Drawing" 
   width="70%"
/>

##### WisConnector PCB Layout

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12052/datasheet/mxxs1003k6m.png" 
  figureCount="5"
  caption="WisConnector PCB footprint and recommendations" 
   width="100%"
/>

#### Schematic Diagram

**Figure 6** shows schematic diagram of RAK12052 module.

The I2C address of RAK12052 is 0110011. R10 and R11 are not populated on the RAK12052 due to the pull-up resistors already on the WisBlock Base Board.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12052/datasheet/rak12052_schematic.png" 
  figureCount="6"
  caption="RAK12052 WisBlock Thermal IR Array Module Schematic" 
   width="100%"
/>

##### Pixel Position

The array consists of 768 IR sensors (also called pixels). Each pixel is identified with its row and column position as Pix (*i*, *j*), where ***i*** is the row number (from 1 to 24) and ***j*** is the column number (from 1 to 32).

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12052/datasheet/rak12052_pixel.png" 
  figureCount="7"
  caption="Pixel in the whole FOV" 
   width="50%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12052/datasheet/rak12052_view.png" 
  figureCount="8"
  caption="RAK12052 WisBlock 32x24 IR Module View" 
   width="50%"
/>



<RkBottomNav/>