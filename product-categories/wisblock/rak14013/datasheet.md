---
slug: /product-categories/wisblock/rak14013/datasheet/
title: RAK14013 WisBlock Joystick Module Datasheet
description: Covers the comprehensive information of your RAK14013 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisblock/rak14013/rak14013.png
keywords:
  - datasheet
  - wisblock
  - RAK14013
sidebar_label: Datasheet
---

# RAK14013 WisBlock Joystick Module Datasheet

## Overview

> **Image:** RAK14013 WisBlock Joystick Module

### Description

The RAK14013 is a joystick module with embedded MCU based on ATTINY441-SSU from Atmel. It has four common tactile push buttons and a rotary 2-axis analog joystick. The status of the buttons and voltage readings of an analog joystick is monitored by the MCU and converted to digital data via I2C interface. RAK14013 doesn't have a WisBlock standard connector so you need a RAK14007 adapter board to plug it into to WisBlock Base module. The RAK14013 communicates to the WisBlock Core via I2C interface.

### Features

- Joystick module and push buttons
- I2C interface
- 3.3 V Power supply
- Chipset: ATMEL ATTINY441-SSU
- Module Size: 54 mm x 85 mm

## Specifications

### Overview

#### Mounting

The RAK14013 WisBlock Joystick Module can be mounted to the IO slot of the WisBlock Base board. **Figure 2** shows the mounting mechanism of the RAK14006 on a WisBlock Base board, such as the [RAK5005-O](https://store.rakwireless.com/products/rak5005-o-base-board).

> **Image:** RAK14013 WisBlock Joystick Module mounting

### Hardware

The hardware specification is categorized into three parts. It provides the pinouts of the module and their corresponding functions and diagrams. Also, it shows the mechanical parameters of the RAK14013 WisBlock Joystick Module.

#### Chipset

| Vendor | Part number   |
| ------ | ------------- |
| ATMEL  | ATTINY441-SSU |

#### Pin Definition

The pin definition of the RAK14013 connector is shown in **Figure 3**.

 
> **Image:** RAK14013 WisBlock Joystick Module pinout

:::tip NOTE
- **3V3**, **I2C** related pin, **RESET**, and **INT** are connected to cable
- This connector is also for updating the  MCU software
:::

#### Mechanical Characteristics

##### Board Dimensions

**Figure 4** shows the dimensions and the mechanical drawing of the RAK14013 module.

 
> **Image:** RAK14013 WisBlock Joystick Module Dimensions

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

#### Schematic Diagram

**Figure 6** shows the schematic of the RAK14013 WisBlock Joystick Module.

> **Image:** RAK14013 WisBlock Joystick Module schematic

##### Power Supply and I2C

**Power supply** and **I2C** connections are shown in **Figure 7**.

> **Image:** RAK14013 Power supply and I2C

##### MCU Circuit

The RAK14013 uses ATTINY441-SSU microcontroller unit (MCU) to control the four tactile push buttons and a rotary series potentiometer of the joystick.

> **Image:** MCU circuit

##### Joystick Circuit

**Joystick** circuit diagram is shown in **Figure 9**.

> **Image:** RAK14013 joystick

##### Tactile Pushbuttons Circuit

**Tactile Pushbuttons** circuit diagram is shown in **Figure 10**.

> **Image:** RAK14013 tactile push buttons

##### Debug Connector

**Debug** connector circuit diagram is shown in **Figure 11**.

> **Image:** RAK14013 debug connector

