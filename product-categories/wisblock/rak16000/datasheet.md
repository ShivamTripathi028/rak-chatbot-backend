---
slug: /product-categories/wisblock/rak16000/datasheet/
title: RAK16000 WisBlock DC Current Module Datasheet
description: Provides comprehensive information about your RAK16000 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak16000/rak16000.png"
keywords:
  - datasheet
  - wisblock
  - RAK16000
sidebar_label: Datasheet
---

# RAK16000 WisBlock DC Current Module Datasheet

## Overview

> **Image:** RAK16000 Top and Back View

### Description

RAK16000 is a part of the WisBlock Sensor Series that is capable of measuring DC current in the range of 0 to 3 A in a voltage range of 0 to 26 V. With the two measured DC values, you get the power consumption by multiplying the current and voltage. Additionally, this module uses the INA219BID from Texas Instruments that offers high accuracy maximum rate of 0.5% over temperature.

### Features

  * Measures DC current in the range of 0 to 3 A
  * Measure DC voltage in the range of 0 to 26 V
  * High accuracy of 0.5% (max) over temperature (INA219B)
  * 100 mΩ shunt resistor can provide a resolution of up to 0.1 mA
  * I2C interface
  * 3.3 V Power supply
  * Chipset: Texas Instruments INA219BID
  * 15 mm x 25 mm

## Specifications

### Overview

#### Mounting

The RAK16000 WisBlock DC Current Module can be mounted to the IO slot of the [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. **Figure 2** shows the mounting mechanism of the RAK16000 on a WisBlock Base module.

> **Image:** RAK16000 mounting mechanism on a WisBlock Base module

### Hardware

The hardware specification is categorized into five parts. It shows the chipset of the module and discusses the pinouts and the corresponding functions and diagrams of the module. It also covers the electrical and mechanical characteristics that include the tabular data of the functionalities and standard values of the RAK16000 WisBlock DC Current Module.

####  Chipset

| Vendor            | Part number |
| ----------------- | ----------- |
| Texas Instruments | INA219BID   |

#### Pin Definition

The RAK16000 WisBlock DC Current Module comprises a standard WisBlock connector. The WisBlock connector allows the RAK16000 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 3**.

> **Image:** RAK16000 WisBlock DC Current Module Pinout

:::tip NOTE

- Only the **I2C** related pins, **3V3_S** and **GND** are connected to the WisConnector.
- **3V3_S** voltage output from the WisBlock Base that powers the RAK16000 module can be controlled by the WisBlock Core via WB_IO2 (WisBlock IO2 pin). This makes the module ideal for low-power IoT projects since the WisBlock Core can totally disconnect the power of the RAK16000 module.
:::

#### Electrical Characteristics

This section shows the maximum and minimum ratings of the RAK16000 module and its recommended operating condition. Refer to the table presented below.

##### Recommended Operating Condition

| Parameter | Minimum | Maximum   | Unit |
| --------- | ------- | --------- | ---- |
| 3V3_S     | -       | 6         | V    |
| IN+,IN-   | -0.3    | 26        | V    |
| SDA       | -0.3    | 6         | V    |
| SCL       | -0.3    | 3V3_S+0.3 | V    |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 4** shows the dimensions and the mechanic drawing of the RAK16000 module.

> **Image:** RAK16000 WisBlock DC Current Module Mechanic Drawing

##### WisConnector PCB Layout

> **Image:** WisConnector PCB Footprint and Recommendations

#### Schematic Diagram

##### I2C Slave Address Select

The default 7-bit I2C address is 0x41. The I2C address can be changed by the pull-up resistors (R7 and R8) and pull-down resistors (R9 and R10).

> **Image:** I2C Slave Address Select

##### I2C Pull-Up Resistor

The pull-up resistor for I2C_SCL and I2C_SDA is already installed on the WisBlock Base board. Don't connect (NC) R2 and R3 on the RAK16000 module.

> **Image:** I2C Pull-Up Resistor

##### INA219BD

* R11, R12, and C3 are reserved for input filter circuit.
* R6 is the shunt resistor, and the default value is 100 mΩ (0.1 Ω +- 1%).

:::tip NOTE

- Using the 100 mΩ shunt resistor, you can measure current with a minimum value of 100 uA and LSB is 100 uA.
- Using the 1 Ω shunt resistor, you can measure 10 uA current, and the measure range will be 320 uA.

:::

> **Image:** INA219BD

##### Full Schematic

**Figure 9** shows the complete schematic of the RAK16000 module.

> **Image:** RAK16000 WisBlock DC Current Module Schematic

