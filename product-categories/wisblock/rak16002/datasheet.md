---
slug: /product-categories/wisblock/rak16002/datasheet/
title: RAK16002 WisBlock Coulomb Sensor Module Datasheet
description: Provides comprehensive information about your RAK16002 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak16002/rak16002.png"
keywords:
  - datasheet
  - wisblock
  - RAK16002
sidebar_label: Datasheet
---

# RAK16002 WisBlock Coulomb Sensor Module Datasheet

## Overview

### Description

RAK16002 is a Coulomb sensor module based on LTC2941IDCB that features programmable high and low thresholds for the accumulated charge. If a threshold is exceeded, the device communicates an alert by setting a flag in the internal status register. It can measure the battery charge state in battery-powered IoT devices. Its operating range is perfectly suited for single-cell Li-Ion batteries.

The precision coulomb counter integrates current through an internal sense resistor between the battery’s positive terminal and the load or charger. The measured charge is stored in internal registers. An I2C interface accesses and configures the device.

### Applications

  * Low power IoT products
  * Indoor environment sensors
  * Air quality sensors
  * Soil moisture sensors
  * GNSS location trackers

### Features

  * Based on LTC2941IDCB
  * Indicates accumulated battery charge and discharge
  * ±1 A Sense current range
  * I2C interface
  * High accuracy analog integration
  * 1% Charge accuracy
  * Configurable alert output/charge complete input
  * 2.7 V to 5.5 V Operating range
  * Quiescent current less than 100 µA
  * Operating temperature: -40 °C ~ 85 °C
  * Storage temperature :-65 °C ~ 150 °C
  * 15 mm x 25 mm

## Specifications

### Overview

> **Image:** RAK16002 top and back view

#### Mounting

The RAK16002 Coulomb module can be mounted to the IO slot of the WisBase board. **Figure 2** shows the mounting mechanism of the RAK16002 on a WisBase module, such as the RAK5005-O.

> **Image:** RAK16002 mounting mechanism on a WisBlock Base module

### Hardware

The hardware specification is categorized into five parts. It shows the chipset of the module and discusses the pinouts and the corresponding functions and diagrams of the module. It also covers the electrical and mechanical characteristics that include the tabular data of the functionalities and standard values of the RAK16002 WisBlock Coulomb Sensor Module.

####  Chipset

| Vendor         | Part number |
| -------------- | ----------- |
| Analog Devices | LTC2941IDCB |

#### Pin Definition

The RAK16002 WisBlock Coulomb Sensor Module comprises a standard 40-pin WisConnector compatible with the WisBlock Base IO Slot. The WisConnector allows the RAK16002 Coulomb sensor module to be mounted to a WisBlock Base board, such as RAK5005-O. The pin order of the connector and the pinout definition is shown in **Figure 3.**

> **Image:** RAK16002 WisBlock Coulomb Sensor Module pinout

:::tip NOTE

- **I2C** related pin, **VBAT**, **AL/CC**，**3V3_S**, and **GND** are connected to WisIO connector.

:::

#### Electrical Characteristics

This section shows the maximum and minimum ratings of the RAK16002 module and its recommended operating condition. Refer to the table presented below.

##### Recommended Operating Condition

| Symbol             | Parameter                      | Conditions                                | Minimum | Typical | Maximum | Unit |
| ------------------ | ------------------------------ | ----------------------------------------- | ------- | ------- | ------- | ---- |
| V<sub>BAT</sub>    | Supply Voltage                 |                                           | 2.7     |         | 5.5     | V    |
| I<sub>SUPPLY</sub> | Supply Current                 | Device On                                 |         |         | 120     | uA   |
|                    |                                | Shutdown                                  |         |         | 2.5     | uA   |
|                    |                                | Shutdown, V<sub>SENSE+</sub> <=4.2 V |         |         | 1       | uA   |
| V<sub>UVLO</sub>   | Undervoltage Lockout Threshold | V<sub>SENSE+ Falling</sub>                | 2.5     | 2.6     | 2.7     | V    |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 4** shows the dimensions and the mechanic drawing of the RAK16002 module.

> **Image:** RAK16002 WisBlock Coulomb Sensor Module mechanic drawing

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

#### Schematic Diagram

##### LTC2941IDCB Main Circuit

The I2C address of LTC2941IDCB is 0x64. R3 and R4 already exist on WisBase. R3 and R4 are not mounted on RAK16002. See **Figure 6**.

:::tip NOTE

- **J2  charge/load select**
  - short pin1 and pin2, Internal charge/load
  - short pin2 and pin3, External charge/load

- **J4 battery select**
  - short pin1 and pin2, Internal battery measurement
  - short pin2 and pin3, External battery measurement

- **J3**
  - pin1, Connect to external charge+/load+
  - pin2, Connect to external charge-/load- & battery-
  - pin3, Connect to external battery+

:::

** For example **

If you want to use the internal battery and the external charge/load, you should do the following (Refer to **Figure 7**.):
- short J2-2 and J2-3;
- short J4-1 and J4-2;
- connect the external charge+/load+ to J3-1;
- connect the external charge-/load- to J3-2;
- connect the internal battery to P1.

> **Image:** RAK16002 main circuit

> **Image:** RAK16002 jumper and battery connectors

##### Full Schematic

**Figure 8** shows the complete schematic of the RAK16002 module.

> **Image:** RAK16002 WisBlock Coulomb Sensor Module schematic

