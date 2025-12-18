---
slug: /product-categories/wisblock/rak12023/datasheet/
title: RAK12023 WisBlock Soil Moisture Sensor Connector Module Datasheet
description: Covers the comprehensive information of your RAK12023 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisblock/rak12023/rak12023.png
keywords:
  - datasheet
  - wisblock
  - RAK4631-R
sidebar_label: Datasheet
---

# RAK12023 WisBlock Soil Moisture Sensor Connector Module Datasheet

## Overview

> **Image:** RAK12023 WisBlock Soil Moisture Sensor Connector

### Description

RAK12023 is a soil moisture connector module. It has one (1) standard WisBlock IO connector, which you can connect with the WisBlock Base. It also has three (3) connectors dedicated to the RAK12035. RAK12035 is a separate soil moisture sensor probe that can be connected to the RAK12023 module. Only one RAK12035 soil moisture sensor can be connected to the RAK12023 simultaneously.

### Features

- A Separate sensor PCB module [RAK12035](overview.md) is required.
- Three (3) available connectors for the soil sensor PCB module RAK12035 (Only one sensor can be connected!).
- Module size: 15 x 25 mm

## Specifications

### Overview

#### Mounting

The RAK12023 WisBlock Soil Sensor Connector Module can be mounted to the IO slot of the [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. **Figure 2** shows the mounting mechanism of the RAK12023 on a WisBlock Base module.

> **Image:** RAK12023 Mounting Mechanism on a WisBlock Base Module

### Hardware

The hardware specification is categorized into three (3) parts. It discusses the pinouts and their corresponding functions and diagrams of the module. Also, it shows the mechanical characteristics of the RAK12023 WisBlock Soil Moisture Sensor Connector Module.

#### Pin Definition

The RAK12023 WisBlock Soil Sensor Module comprises a standard WisBlock connector. The WisBlock connector allows the RAK12023 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 3**.

> **Image:** RAK12023 Pinout Schematic

:::tip NOTE
- Only **I2C** related pin, **IO4**, **3V3_S**, and **GND** are connected to the WisConnector.
- **3V3_S** voltage output from the WisBlock Base that powers the RAK12023 module can be controlled by the WisBlock Core via WB_IO2 (WisBlock IO2 pin). This makes the module ideal for low-power IoT projects since the WisBlock Core can totally disconnect the power of the RAK12023 module.
:::

#### Mechanical Characteristics

##### Board Dimensions

**Figure 4** shows the mechanical dimensions of the RAK12023 Module.

> **Image:** RAK12023 Mechanical Dimensions

##### WisConnector PCB Layout

> **Image:** WisConnector PCB Footprint and Recommendations

#### Schematic Diagram

**Figure 6** shows the schematic of the RAK12023 module.

> **Image:** RAK12023 WisBlock Module Schematics

