---
slug: /product-categories/wisblock/rak12001/datasheet/
title: RAK12001 WisBlock Fingerprint Sensor Module Datasheet
description: Provides comprehensive information for your RAK12001 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak12001/rak12001.png"
keywords:
  - datasheet
  - RAK12001
  - wisblock
sidebar_label: Datasheet
---

# RAK12001 WisBlock Fingerprint Sensor Module Datasheet

## Overview

### Description

The RAK12001 is a fingerprint sensor module based on GROW R307. This module supports both fingerprint enrollment and fingerprint matching. When enrolling, it is required to place the finger two times in the sensor. The system will process the fingerprint images collected and generate a template, then store the fingerprint template in its memory. When matching, the sensor will determine if the finger placed in its optical sensor has a match on its memory.

### Features

- Fingerprint Sensor Module
- Interface: UART
- Window dimension: 19 mm x 21 mm
- Character file size: 256 bytes
- Scanning speed: < 0.3 second
- Verification speed: < 0.2 second
- 3.3 V Power supply (with built-in 5 V boost converter)
- Current Consumption: 50 mA
- Fingerprint Module: GROW R307
- Module size: 10 mm x 23 mm

## Specifications

### Overview

#### Mounting

**Figure 1** shows the mounting mechanism of the RAK12001 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. It can be mounted on the double-size sensor slots with UART pins like slots **A, E, & F** (also on slot **C** but only with [RAK19003 Mini Base board](https://docs.rakwireless.com/product-categories/wisblock/rak19003/overview/)).

> **Image:** RAK12001 WisBlock Fingerprint Sensor Module Mounting

### Hardware
The hardware specification is categorized into five (5) parts. It shows the chipset of the module and discusses the pinouts and their corresponding functions and diagrams. It also covers the electrical and mechanical parameters that include the tabular data of the functionalities and standard values of the RAK12001 WisBlock Fingerprint Sensor.

#### Chipset

| Vendor  | Part number |
| ------- | ----------- |
| GROW    |   R307      |

#### Pin Definition

The RAK12001 WisBlock Fingerprint Sensor comprises a standard WisBlock connector. The WisBlock connector allows the RAK12001 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 2**.

:::tip NOTE
- **UART Tx/Rx** pins, **TOUCH**, **3V3_S (optional)**, and **GND** are connected to WisBlock Connector.
:::

 
> **Image:** RAK12001 WisBlock Fingerprint Sensor Module Pinout

:::tip NOTE
- Slot B is not recommended because the IO2 pin is used to control power supply 3V3_S.
:::

#### Electrical Characteristics

| Symbol | Description                 | Min. | Nom. | Max. | Unit |
| ------ | --------------------------- | ---- | ---- | ---- | ---- |
| VDD    | Power supply for the module | 2.7  | 3.3  | 4.5  | V    |
| I      | Working current             | -    | 50   | -    | mA   |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 3** shows the dimensions and the mechanical drawing of the RAK12001 module.

 
> **Image:** RAK12001 WisBlock Fingerprint Sensor Module Dimensions

#### Schematic Diagram

> **Image:** WisConnector and RAK12001 Schematic

:::tip NOTE
- **R307** needs 4.2 V - 6 V, which is provided by the on-board **boost converter**.
- **TOUCH** is an input signal from **R307** when a finger is placed and detected by the sensor.
:::
​

