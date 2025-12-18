---
slug: /product-categories/wisblock/rak13004/datasheet/
title: RAK13004 WisBlock PWM Expander Module Datasheet
description: Provides comprehensive information about your RAK13004 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak13004/rak13004.png"
keywords:
  - datasheet
  - wisblock
  - RAK13004
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK13004 WisBlock PWM Expander Module Datasheet

## Overview

### Description

The RAK13004 is a PWM expander module that can be mounted to the IO slot of WisBlock Base board. It can be controlled 16-channel LED, and the module uses PCA9685 from NXP, I2C interface.

### Features

- 16 LED drivers connector
- 1&nbsp;MHz Fast-mode Plus compatible I2C-bus interface
- 4096-step (12-bit) linear programable brightness per LED
- LED output frequency typically varies from 24&nbsp;Hz to 1526&nbsp;Hz
- Supports hot insertion
- Low Standby Current
- 5.5&nbsp;V tolerant inputs
- Operating Voltage: 2.3&nbsp;V to 5.5&nbsp;V @ -40&nbsp;°C to +85&nbsp;°C
- Chipset:  NXP Semiconductors PCA9685
- Module size: 25X35&nbsp;mm

### Applications

- RGB or RGBA LED drivers
- LED status information
- LED displays

## Specifications

### Overview

#### Mounting

The RAK13004 module can be mounted to the IO slots of the WisBlock Base board. Figure 1 shows the mounting mechanism of the RAK13004 on a WisBlock Base board.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13004/datasheet/rak13004-mounting.png"
  width="60%"
  caption="RAK13004 WisBlock PWM Expander Module Mounting"
/>

### Hardware

The hardware specification is categorized into five parts. It shows the chipset of the module and discusses the pinouts of the module and its corresponding functions and diagrams. It also covers the electrical and mechanical parameters that include the tabular data of the functionalities and standard values of the RAK13004 WisBlock PWM Expander Module.

#### Chipset

The RAK13004 PWM Expander Module uses PCA9685 from NXP Semiconductors.

| Vendor             | Part Number |
| ------------------ | ----------- |
| NXP Semiconductors | PCA9685     |

Figure 2 shows PCA9685 device addressing. Default A5, A4, and A3 are connected to ground, and A2, A1, and A0 are optional. It can be connected to 3.3&nbsp;V or GND. Default 7-Bits I2C address is 0x80.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13004/datasheet/pca9685-addressing.png"
  width="40%"
  caption="The PCA9685 device addressing"
/>

#### Pin Definition

The RAK13004 WisBlock PWM Expander Module comprises a standard WisConnector. The WisConnector allows the RAK13004 module to be mounted on a WisBlock Base board. The pin order of the connector and the pinout definition is shown in Figure 3.

:::tip NOTE
- **I2C** related pins, **OE**, **3V3_S**, and **GND** are connected to this module.
- **OE** output enable pin, low active, internal pull-up, disable output.
- **3V3_S** voltage output from the WisBlock Base that powers the RAK13004 module can be controlled by the WisBlock Core via WB_IO2 (WisBlock IO2 pin). This makes the module ideal for low-power IoT projects since the WisBlock Core can totally disconnect the power of the RAK13004 module.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13004/datasheet/rak13004_pinout.svg"
  width="70%"
  caption="RAK13004 WisBlock PWM Expander Module Pinout"
/>

#### Electrical Characteristics

##### Recommended operating Conditions

| Symbol | Description            | Min. | Nom. | Max. | Unit |
| ------ | ---------------------- | ---- | ---- | ---- | ---- |
| VDD    | Power supply           |      | 3.3  |      | V    |
| IDD    | Supply current         | -    | 6    | 10   | mA   |
| Istb   | Standby current        | -    | 2.2  | 15.5 | uA   |
| VPOR   | power-on reset voltage | -    | 1.7  | 2.0  | V    |

#### Mechanical Characteristic

##### Board Dimensions

Figure 4 shows the dimensions and the mechanic drawing of the RAK13004 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13004/datasheet/mechanic-drawing.png"
  width="70%"
  caption="RAK13004 WisBlock PWM Expand Module Mechanic Drawing"
/>

##### WisConnector PCB Layout

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13004/datasheet/pcb-footprint.png"
  width="100%"
  caption="WisConnector PCB Footprint and recommendations"
/>

#### Schematic Diagram
##### PWM Expander

Figure 6 shows RAK13004 PWM expander module IO expand schematic. Default use **3V3_S** for power supply.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13004/datasheet/rak13004-schematic.png"
  width="80%"
  caption="RAK13004 WisBlock PWM Expander Schematic"
/>

##### Device Address

Figure 7 shows device address bit2-bit0. Default is connected to ground.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13004/datasheet/device-adress-a2-a0.png"
  width="30%"
  caption="RAK13004 WisBlock Device Address A2-A0"
/>


<RkBottomNav/>