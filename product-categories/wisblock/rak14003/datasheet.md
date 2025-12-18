---
slug: /product-categories/wisblock/rak14003/datasheet/
title: RAK14003 WisBlock LED Bar Graph Module Datasheet
description: Provides comprehensive information about your RAK14003 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak14003/rak14003.png"
keywords:
  - datasheet
  - wisblock
  - RAK14003
sidebar_label: Datasheet
---

# RAK14003 WisBlock LED Bar Graph Module Datasheet

## Overview

### Description

RAK14003 is an LED Bar Graph that is part of WisBlock Display modules. It consists of 10 configurable LEDs (5 green color LEDs, 3 yellow color LEDs, and 2 red color LEDs). RAK14003 uses the **MCP23017** from Microchip as an I/O Expander and **KEM-102510A-RYG** from Hongke Lighting as the LED bar. Each LED in the module can be controlled separately so the module can build a multipurpose graphic feedback display.

### Features

- LED Bar Graph module
- 5 green color LEDs, 3 yellow color LEDs，and 2 red color LEDs
- Each LED can be controlled separately
- 3.3 V Power supply
- Chipset: Microchip MCP23017, Hongke Lighting KEM-102510A-RYG
- Module size: 25 x 45 mm

## Specifications

### Overview

> **Image:** RAK14003 Front and Back View

#### Mounting

The RAK14003 module can be mounted on the IO slot of the WisBlock Base board. **Figure 2** shows the mounting mechanism of the RAK14003 on a WisBlock Base module, such as the RAK5005-O.

> **Image:** RAK14003 Mounting Mechanism on a WisBlock Base Module

### Hardware

The hardware specification is categorized into four parts. It discusses the pinouts and its corresponding functions and diagrams of the module. It also covers the electrical and mechanical characteristics that include the tabular data of the functionalities and standard values of the RAK14003 WisBlock LED Bar Graph Module.

####  Chipset
| Vendor                     | Part number                |
| -------------------------- | -------------------------- |
| Microchip, Hongke Lighting | MCP23017, KEM-102510A-RYG  |

#### Pin Definition

The RAK14003 module has a 40-pin WisConnector that is compatible to the WisBlock Base IO Slot. The pin order of the connector and the pinout definition is shown in **Figure 3**.

> **Image:** RAK14003 Pinout Schematic

:::tip NOTE
- Only **I2C** related pin, **RESET**, **3V3_S**, and **GND** are connected to the WisConnector.
- **3V3_S** voltage output from the WisBlock Base that powers the RAK14003 module can be controlled by the WisBlock Core via WB_IO2 (WisBlock IO2 pin). This makes the module ideal for low-power IoT projects since the WisBlock Core can totally disconnect the power of the RAK14003 module.
:::

#### Electrical Characteristics

This section shows the maximum and minimum ratings of the RAK14003 module and its recommended operating conditions. Refer to the table presented below.

##### Absolute Maximum Ratings

| Parameter | Description                     | Min. | Nom. | Max.        | Unit |
| --------- | ------------------------------- | ---- | ---- | ----------- | ---- |
| 3V3_S     | Power Voltage Range             | -0.3 | -    | 5.5         | V    |

##### Power Supply Ratings

| Symbol | Description                | Condition                              | Min. | Nom. | Max. | Unit |
| ------ | -------------------------- | -------------------------------------- | ---- | ---- | ---- | ---- |
| 3V3_S  | Supply Voltage             | Input voltage must within this range   | -    | 3.3  | -    | V    |
| Imax   | Max Current                | Turn ON all LEDs                       | -    | -    | 170  | mA   |

##### LED Parameters

Table below shows the LED parameters. Color Code & Chip Characteristic: (Test Condition: IF=20 mA)

| Emitting Color | Peak Wavelength | Forward Voltage | Luminous Intensity IF=20 mA (mcd) |  |  |
| --- | --- | --- | --- | --- | --- |
|  | (λp) | Δλ | Typ | Max | Max |
| Amber | 605-615 | 30 | 1.9 | 2.4 | 30 |
| Super Green | 565-575 | 30 | 1.9 | 2.4 | 80 |
| Super Red | 625-640 | 20 | 1.8 | 2.3 | 100 |
| High Red | 640-660 | 20 | 1.8 | 2.3 | 12 |
| Yellow Green | 570-580 | 30 | 2.0 | 2.5 | 45 |
| Yellow | 590-600 | 35 | 2.0 | 2.5 | 60 |
| Blue | 465-475 | 40 | 3.0 | 3.5 | 200 |
| Pure Green | 515-525 | 40 | 3.0 | 3.5 | 600 |
| White |  |  | 3.0 | 3.5 | 180 |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 4** shows the mechanical dimensions of the RAK14003 Module.

> **Image:** RAK14003 Mechanical Dimensions

##### WisConnector PCB Layout

> **Image:** WisConnector PCB Footprint and Recommendations

#### Schematic Diagram

**Figure 6** shows the schematic of the RAK14003 module.

> **Image:** RAK14003 WisBlock Module Schematics

##### I/O Expander and LED Bar

> **Image:** RAK14003 I/O Expander and LED Bar

:::tip NOTE
- The current-limiting resistances are 68 Ω.
:::

##### Device Address Select

> **Image:** I2C Address Select

:::tip NOTE
- You can change the I2C slave address. The default 7-bit I2C address is **0x24**.
:::

##### I2C Pull-up Resistance

The I2C Pull-up resistors already exist on the WisBlock Base, such as the RAK5005-O, not on the RAK14003 module.

> **Image:** I2C Pull-up Resistance

