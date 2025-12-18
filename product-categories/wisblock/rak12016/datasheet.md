---
slug: /product-categories/wisblock/rak12016/datasheet/
title: RAK12016 WisBlock Flex Sensor Module Datasheet
description: Covers the comprehensive information of your RAK12016 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak12016/rak12016.png"
keywords:
  - datasheet
  - wisblock
  - RAK12016
sidebar_label: Datasheet
---

# RAK12016 WisBlock Flex Sensor Module Datasheet

## Overview

> **Image:** RAK12016 Flex Sensor Module

### Description

RAK12016 is a flex sensor module, a part of the RAKWireless WisBlock Sensor series. It uses an FS-L-0095-103-ST from Spectrasymbol, which can measure the amount of deflection or bending.

### Features

- Measure bending between 1 to 180 degrees
- Accuracy to 1 degree
- 3.3 V Power Supply
- Chipset: Spectrasymbol FS-L-0095-103-ST
- Module size: 15 X 25 mm

## Specifications

### Overview

#### Mounting

The RAK12016 WisBlock Flex Sensor Module can be mounted to the IO slot of the [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. **Figure 2** shows the mounting mechanism of the RAK12016 on a WisBlock Base module.

> **Image:** RAK12016 mounting mechanism on a WisBlock Base module

:::tip NOTE
- By using a JST PH2.54 Connector (J2), the flex sensor (FS-L-0095-103-ST) can also be an external module that is outside of the WisBlock unit, so it can measure bending on all kinds of objects.
:::

### Hardware

The hardware specification is categorized into five (5) parts. It shows the chipset of the module and discusses the pinouts and their corresponding functions and diagrams. It also covers the electrical and mechanical characteristics that include the tabular data of the functionalities and standard values of the RAK12016 WisBlock Module.

####  Chipset

|    Vendor     |   Part number    |
| ------------- | ---------------- |
| Spectrasymbol | FS-L-0095-103-ST |

#### Pin Definition

The RAK12016 WisBlock Flex Sensor Module comprises a standard WisBlock connector. The WisBlock connector allows the RAK12016 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 3**.

> **Image:** RAK12016 Pinout Schematic

:::tip NOTE
- Only **I2C** related pins, **3V3_S**, **GND**, and **ALERT** are connected to the WisConnector.
- **3V3_S** voltage output from the WisBlock Base that powers the RAK12016 module can be controlled by the WisBlock Core via WB_IO2 (WisBlock IO2 pin). This makes the module ideal for low-power IoT projects since the WisBlock Core can totally disconnect the power of the RAK12016 module.
:::

#### Electrical Characteristics

This section shows the maximum and minimum ratings of the RAK12016 module and its recommended operating conditions. Refer to the table presented below.

##### Recommended Operating Conditions

| Symbol | Description  | Min. | Nom. | Max.  | Unit |
| ------ | ------------ | ---- | ---- | ----- | ---- |
| VDD    | Power Supply | -    | 3.3  | -     | V    |

#### Mechanical Characteristic

##### Board Dimensions

The mechanical dimensions of the RAK12016 module are shown in **Figure 4** below.

> **Image:** RAK12016 Mechanical Dimensions

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

##### PCB Silkscreen

> **Image:** RAK12016 PCB Silkscreen

#### Schematic Diagram

**Figure 7** shows the schematic of the RAK12016 module.

> **Image:** RAK12016 WisBlock Module Schematics

##### Analog Input

**J2** is used to connect the flex sensor. The sensor acts like a variable resistor, the resistance changes due to the angle of bend by flexing the component. **R10** and the flex sensor constitute a series voltage divider. The MCP606 Comparator is used because the low input bias current of the Op Amp reduces the error due to the source impedance of the flex sensor as a voltage divider.

> **Image:** RAK12016 Analog Input Schematic

##### Analog to Digital Converter (ADC)

ADC121C021 is the ADC module used that features an I2C compatible serial interface. The **ALERT** feature provides a converting interrupt (Watchdog) function to ensure that the input voltage remains within the limits that are set in the Registers.

> **Image:** RAK12016 Analog to Digital Converter

##### ADC I2C Address Select

> **Image:** ADC I2C Address Select

##### I2C Pull-Up Resistance

> **Image:** RAK12016 I2C Pull-up Resistance

:::tip NOTE
- The built-in I2C pull-up resistors are on the WisBlock Base module and not on the RAK12016.
:::

