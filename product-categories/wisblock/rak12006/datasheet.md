---
slug: /product-categories/wisblock/rak12006/datasheet/
title: RAK12006 WisBlock PIR Sensor Module Datasheet
description: Provides comprehensive information about your RAK12006 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak12006/rak12006.png"
keywords:
  - datasheet
  - RAK12006
  - wisblock
sidebar_label: Datasheet
date: 2021-08-10
---

# RAK12006 WisBlock PIR Sensor Module Datasheet

## Overview

### Description

The RAK12006 is a Pyroelectric Infrared Radial (PIR) module. It is designed to detect occupancy and motion from the infrared radiated objects. The sensor uses AM312 from Senba Sensing Technology Co., Ltd.

### Features

- Digital signal processing
- Built-in filter, screens interference from other frequencies
- Schmitt Trigger Output REL
- 3.3 V Power supply
- Chipset: Senba Sensing Technology AM312
- **Module size:** 15 X 25 mm

## Specifications

### Overview

#### Mounting

The RAK12006 WisBlock PIR Sensor Module can be mounted on the IO slot of the [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. **Figure 1** shows the mounting mechanism of the RAK12006 on a WisBlock Base module.

> **Image:** RAK12006 mounting mechanism on a WisBlock Base module

### Hardware

The hardware specifications are categorized into five parts. It shows the chipset of the module, and discusses the pinouts, their corresponding functions, and related diagrams. It also covers the electrical and mechanical parameters that include the tabular data of the functionalities and standard values of the RAK12006 WisBlock PIR Sensor Module.

#### Chipset

| Vendor                            | Part Number |
| --------------------------------- | ----------- |
| Senba Sensing Technology Co., Ltd | AM312       |

#### Pin Definition

The RAK12006 module has a 40-pin WisConnector that is compatible with the WisBlock Base IO Slot. The pin order of the connector and the pinout definition are shown in **Figure 2**.

> **Image:** RAK12006 Pinout Schematic

:::tip NOTE
- Only **Digital OUT**, **3V3**, and **GND** are connected to WisConnector.

- An optional **3V3_S** supply voltage can be used to turn ON or OFF the RAK12006 module through the IO2 pin. This can be helpful in low-power applications.

- To disable the default **3V3** supply and use the alternative **3V3_S** supply source, the resistor jumper R1 must be 0 Ω and R2 must be NC (not connected).
:::

#### Electrical Characteristics

This section shows the maximum and minimum ratings of the RAK12006 module and its recommended operating condition. Refer to the table presented below.

##### Recommended Operating Condition

| Symbol | Description                     | Min. | Nom. | Max.        | Unit |
| ------ | ------------------------------- | ---- | ---- | ----------- | ---- |
| VDD    | Power Supply Voltage            | -    | 3.3  | -           | V    |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 3** shows the mechanical dimensions of the RAK12006 Module.

> **Image:** RAK12006 Mechanical Dimensions

##### WisConnector PCB Layout

> **Image:** WisConnector PCB Footprint and Recommendations

#### Schematic Diagram

**Figure 5** shows the schematic of the RAK12006 module.

> **Image:** RAK12006 WisBlock PIR Module Schematic

