---
slug: /product-categories/wisblock/rak12017/datasheet/
title: RAK12017 WisBlock IR Detection Sensor Module Datasheet
description: Provides comprehensive information for your RAK12017 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak12017/rak12017.png"
keywords:
  - datasheet
  - wisblock
  - RAK12017
sidebar_label: Datasheet
---

# RAK12017 WisBlock IR Detection Sensor Module Datasheet

## Overview

### Description

The RAK12017 is an IR detection module. This module uses ITR20001 optical switch from Everlight to detect whether the IR Signal reflects. Sample applications of this module are: to identify if an object is approaching and check changes between black and white lines.

### Features

- Detect whether IR Signal is reflected back
- λP=940 nm
- 3.3 V Power supply
- Current Consumption: < 21 mA
- Chipset: Everlight ITR20001
- Infrared Line Tracking Range: 1 cm to 5 cm
- Module Size: 15 mm x 25 mm

## Specifications

### Overview

#### Mounting

The RAK12017 WisBlock IR Detection Sensor Module can be mounted to the IO slot of the [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. **Figure 1** shows the mounting mechanism of the RAK12017 on a WisBlock Base module.

> **Image:** RAK12017 WisBlock IR Detection Module Mounting

:::tip NOTE
- RAK12017 has a connector(default NC), and if you need to get the module out of WisBlock Base board, you can solder it with cable and [RAK13003 WisBlock IO Expansion Module](https://store.rakwireless.com/products/io-expansion-module-rak13003) to position the module however you like.
:::

### Hardware
The hardware specification is categorized into five (5) parts. It shows the chipset of the module and discusses the pinouts and their corresponding functions and diagrams. It also covers the electrical and mechanical parameters that include the tabular data of the functionalities and standard values of the RAK12017 WisBlock IR Detection Sensor Module.

####  Chipset

| Vendor    | Part number |
| --------- | ----------- |
| Everlight | ITR20001    |

#### Pin Definition

The RAK12017 WisBlock IR Detection Sensor Module comprises a standard WisBlock connector. The WisBlock connector allows the RAK12017 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 2**.

:::tip NOTE
- **3V3_S**, **GND**, **AIN1**, **OUT** are connected to WisConnector.
:::

 
> **Image:** RAK12017 WisBlock IR Detection Module Pinout

#### Electrical Characteristics

| Symbol   | Description            | Min. | Nom. | Max. | Unit |
| -------- | ---------------------- | ---- | ---- | ---- | ---- |
| VDD      | Power supply           | -    | 3.3  | -    | V    |
| λP       | Peak Wavelength        | -    | 940  | -    | nm   |
| VF       | Forward Voltage        | -    | 1.2  | 1.5  | V    |
| IF       | Forward Current        | 18   | 21   | -    | ma   |
| ICEO     | Dark Current           | -    | -    | 100  | nA   |
| VCE(sat) | C-E Saturation Voltage | -    | -    | 0.4  | V    |
| tR       | Rise Time              | -    | 25   | -    | us   |
| tF       | Fall Time              | -    | 25   | -    | us   |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 3** shows the dimensions and the mechanical drawing of the RAK12017 module.

 
> **Image:** RAK12017 WisBlock IR Detection Module Dimensions

##### WisConnector PCB Layout

> **Image:** WisConnector PCB Footprint and Recommendations

#### Schematic Diagram

> **Image:** WisConnector and RAK12017 Schematic

:::tip NOTE
- **3V3_S** is supported by WisBase.
- **AIN1** is an analog input.
- The voltage depends on reflection strength.
- The reverse level of MCP606 can be adjusted by indicator.
- **D1** is an LED used as an indicator light.
- **J2** is used for cable when the module is out of the base.
:::
​

