---
slug: /product-categories/wisblock/rak12004/datasheet/
title: RAK12004 WisBlock MQ2 Gas Sensor Module Datasheet
description: Provides comprehensive information about your RAK12004 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak12004/rak12004.png"
keywords:
  - datasheet
  - RAK12004
  - wisblock
sidebar_label: Datasheet
---

# RAK12004 WisBlock MQ2 Gas Sensor Module Datasheet

## Overview

### Description

The RAK12004 is a gas sensor module, part of the RAKWireless WisBlock Sensor series. The sensor used is the MQ-2 from Zhengzhou Winsen Electronics.

### Features

* MQ-2 gas sensor
* Sensitivity to LPG, butane, propane, methane, alcohol, hydrogen, smoke, and other flammable steam
* I2C Interface
* Alert function
* Detection Range: 300～10000 ppm (flammable gas)
* 3.3 V Power Supply
* Chipset: Winsen MQ-2
* **Module size**: 25 x 35 mm

## Specifications
### Overview

#### Mounting

The RAK12004 WisBlock MQ2 Gas Sensor Module can be mounted to the IO slot of the [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock/quickstart/#wisblock-base) board. **Figure 1** shows the mounting mechanism of the RAK12005 on a WisBlock Base module.

> **Image:** RAK12004 WisBlock MQ2 Gas Sensor Mounting

### Hardware

The hardware specification is categorized into five (5) parts. It shows the chipset of the module and discusses the pinouts and their corresponding functions and diagrams. It also covers the electrical and mechanical characteristics that include the tabular data of the functionalities and standard values of the RAK12004 WisBlock MQ2 Gas Sensor Module.

####  Chipset

| Vendor | Part number |
| ------ | ----------- |
| Winsen | MQ-2        |

#### Pin Definition

The RAK12004 WisBlock MQ2 Gas Sensor Module comprises a standard 40-pin WisConnector. The WisConnector allows the RAK12004 module to mounted to a WisBlock Base Board. The pin order of the connector and the pinout definition is shown in **Figure 2**.

:::tip NOTE
 **I2C** related pin, **ALERT**, **EN**, **VBAT**, **3V3**, and **GND** are connected to 40-pin WisConnector.
:::

> **Image:** RAK12004 WisBlock MQ2 Gas Sensor Pinout

#### Electrical Characteristics

##### Recommended Operating Conditions

| Symbol | Description                  | Min. | Nom. | Max. | Unit |
| ------ | ---------------------------- | ---- | ---- | ---- | ---- |
| VBAT   | Supply Voltage               | 2.8  | -    | 4.2  | V    |
| VCCIO  | Digital IO Power Supply      | -    | 3.3  | -    | V    |
| VCC    | ADC to I2C Chip Power Supply | -    | 5    | -    | V    |

#### Mechanical Characteristics

##### Board Dimensions

Figure 3 shows the dimensions and the mechanic drawing of the RAK12004 module.

> **Image:** RAK12004 WisBlock MQ2 Gas Sensor Module Mechanic Drawing

##### WisConnector PCB Layout

> **Image:** WisConnector PCB Footprint and Recommendations

#### Schematic Diagram

##### Power Supply Circuit

Figure 5 shows RAK12004 step-up power supply circuit.

* **VBAT** Battery voltage (max voltage is 4.2 V)
* **EN** Power enable pin (active high). This pin is connected to **IO6** of WisBlock Core.

> **Image:** RAK12004 WisBlock MQ2 Gas Sensor Module Power Supply

##### Gas Detector Circuit

Figure 6 shows the gas detector circuit.

* **U2** Gas sensor

The heater voltage requires a 5 V supply which is provided by the 5 V step-up converter. This is needed to achieve the standard working temperature of the sensor. The pins 1 and 3 voltage (5 V) supply the detect voltage to load resistance R12. The **AOUT** pin is the voltage of load resistance R12 which represents the reading of the U2 sensor.

* **U3** ADC121C021 12-Bit Analog-to-Digital converter with alert function. The U3 power supply is 5 V.

> **Image:** RAK12004 WisBlock MQ2 Gas Detector Circuit

##### Voltage Level Shifter Circuit

The 40-pin WisConnector voltage has a voltage level of 3.3 V while U2 and U3 have 5 V. To interface the different voltage level between 40-pin Wisconnector and gas sensor, the RAK12004 has a built-in voltage level shifter circuit.

> **Image:** Voltage Level Shifter Circuit

##### I2C Address

The I2C address of the Analog-to-Digital converter chip of RAK12004 can be configured via resistor jumpers as shown in Figure 8.

> **Image:** RAK12004 I2C Address

##### J2 Connector Pinout

RAK12004 has an additional connector to provide an extra interface to the module. The pinout of J2 connector is shown in Figure 9.

> **Image:** J2 Connector Pinout

##### WisConnector

Figure 10 shows 40-pin WisConnector pinout.

* **VBAT** battery voltage
* **I2C1_SDA** and **I2C1_SCL** are I2C related pins
* **EN** is power chip enable pin
* **ALERT** is analog-to-digital converter alert pin

> **Image:** RAK12004 MQ2 Gas Sensor Module 40-pin WisConnector

