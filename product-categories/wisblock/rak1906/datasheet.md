---
slug: /product-categories/wisblock/rak1906/datasheet/
title: RAK1906 WisBlock Environmental Sensor Module Datasheet
description: Provides comprehensive information about your RAK1906 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak1906/rak1906.png"
keywords:
  - datasheet
  - wisblock
  - RAK1906
sidebar_label: Datasheet
date: 2020-08-22
---

# RAK1906 WisBlock Environmental Sensor Module Datasheet

## Overview

> **Image:** RAK1906 WisBlock Environmental Sensor

### Description

The RAK1906 WisBlock Environmental Sensor Module, part of the RAK WisBlock Sensor series, is a 4-in-1 digital sensor board that comprises gas, humidity pressure, and temperature sensor, based on the Bosch® BME680 module. The RAK1906 is ideal for applications such as indoor air quality, home automation, and building IoT solutions.

### Features

* **Sensor specifications**
    * Voltage supply: 3.3 V
    * Current consumption: 0.15 uA to 350 uA
    * Chipset: BOSCH BME680
    * Temperature range: -40 °C to 85 °C
    * Humidity range: 0 to 100%
    * Pressure range: 300 hPa to 1100 hPa
    * Gas sensor response time < 1 sec
    * Sensor outputs can be used with the [Bosch BSEC library](https://github.com/BoschSensortec/BSEC-Arduino-library) algorithm to calculate the IAQ (Indoor Air Quality) index

* **Size**
    * 10 x 10 mm

## Specifications
### Overview

#### Mounting

**Figure 2** shows the mounting mechanism of the RAK12001 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. The RAK12001 module can be mounted on the slots: **A, B, C, D, E, & F**.

> **Image:** RAK1906 WisBlock Environmental Sensor Mounting

### Hardware

The hardware specification is categorized into six parts. It shows the chipset of the module and discusses the pinouts, sensors, and the corresponding functions and diagrams. It also covers the electrical and mechanical parameters that include the tabular data of the functionalities and standard values of the RAK1906 WisBlock Environmental Sensor Module.

####  Chipset

| Vendor | Part Number |
| ------ | ----------- |
| BOSCH  | BME680      |

#### Pin Definition

The RAK1906 WisBlock Environmental Sensor Module comprises a standard WisBlock connector. The WisBlock connector allows the RAK1906 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 3**.

> **Image:** RAK1906 WisBlock Environmental Sensor Pinout

:::tip NOTE
Only the **I2C** related pin, **VDD**, and **GND** are connected to this module.
:::

If a 24-pin WisBlock Sensor connector is used, the IO used for the output pulse depends on what slot the module is plugged in. The following table shows the default IO used for different slots:

| SLOT A | SLOT B | SLOT C | SLOT D | SLOT E | SLOT F |
| ------ | ------ | ------ | ------ | ------ | ------ |
| WB_IO1 | WB_IO2 | WB_IO3 | WB_IO5 | WB_IO4 | WB_IO6 |

#### Sensors
##### Temperature Sensor

| Parameter | Symbol | Condition | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| Operating Temperature Range | TA | Operational | -40 | 25 | 85 | °C |
| Supply Current | IDD,T | 1 Hz Forced Mode, Temperature Measurement Only |  | 1.0 |  | µA |
| Absolute Accuracy Temperature | AT,25 | 25 °C |  | ±0.5 |  | °C |
| Absolute Accuracy Temperature | AT,full | 0-65 °C |  | ±1.0 |  | °C |
| Output Resolution | RT | API Output Resolution |  | 0.01 |  | °C |

##### Humidity Sensor

| Parameter | Symbol | Condition | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| Operating Range |  |  | -40 | 25 | 85 | °C |
| Operating Range |  |  | 0 |  | 100 | % r.H. |
| Full Accuracy Range |  |  | 0 |  | 65 | °C |
| Full Accuracy Range |  |  | 10 |  | 90 | % r.H. |
| Supply Current | IDD,H | 1 Hz Forced Mode,Temperature and Humidity Measurement |  | 2.1 | 2.8 | µA |
| Absolute Accuracy | Ah | 20-80% r.H., 25 °C, including hysteresis |  | ±3 |  | % r.H. |

##### Pressure Sensor

| Parameter | Symbol | Condition | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| Operating Temperature Range | TA | Operational | -40 | 25 | 85 | °C |
| Operating Temperature Range | TA | Full Accuracy | 0 |  | 65 | °C |
| Operating Pressure range | P | Full Accuracy | 300 |  | 1100 | hPa |
| Supply Current | IDD,LP | 1 Hz Forced Mode, Pressure, and Temperature, Lowest Power |  | 3.1 | 4.2 | µA |
| Temperature Coefficient Of Offset | TCOP | 25-40 °C, 900 hPa |  | ±1.3 |  | Pa,K |
| Temperature Coefficient Of Offset | TCOP | 25-40 °C, 900 hPa |  | ±10.9 |  | cm/K |
| Absolute Accuracy Pressure | Ap,full | 300-1100 hPa0-65 °C |  | ±0.6 |  | hPa |

##### IAQ algorithm

:::tip NOTE
The IAQ is not calculated by the Bosch BME680 directly. The measured sensor values need to be send to the [Bosch BSEC library](https://github.com/BoschSensortec/BSEC-Arduino-library) algorithm to calculate the IAQ (Indoor Air Quality) index.
:::

| Parameter | Symbol | Condition | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| Accuracy Status | AXIAQ | Android Compatible | 0 |  | 3 |  |
| IAQ Resolution | IAQrs |  |  | 1 |  |  |
| IAQ Range | IAQrg |  | 0 |  | 500 |  |
| Sensor-to-sensor Deviation | IAQS2S | All Operation Modes |  | ±15%±15 |  |  |
| Durability To Siloxanes | IAQS2S | Sensor-to-sensor Deviation |  | ±15%±15 |  |  |
| Durability To Siloxanes | IAQdrift | Drift at Low & High Concentrations |  | ±1%±4 |  |  |

#### Electrical Characteristics
##### Recommended Operating Conditions
| Symbol            | Description                 | Min.  | Nom.  | Max.  | Unit  |
| ----------------- | --------------------------- | :---: | :---: | :---: | :---: |
| V<sub>DD</sub>    | Power supply for the module | 1.71  |  3.3  |  3.6  |   V   |
| I<sub>sleep</sub> | Sleep current               |   -   | 0.15  |   -   |  uA   |
| I<sub>DD</sub>    | Humidity Measure current    |   -   |  340  |   -   |  uA   |
| I<sub>DD</sub>    | Pressure Measure current    |   -   |  714  |   -   |  uA   |
| I<sub>DD</sub>    | Temperature Measure current |   -   |  350  |   -   |  uA   |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 4** shows the dimensions and the mechanic drawing of the RAK1906 module.

> **Image:** RAK1906 WisBlock Environmental Sensor mechanic dimensions

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

#### Schematic Diagram

**Figure 6** shows the schematic of the RAK1906 module.

> **Image:** RAK1906 WisBlock Environmental Sensor schematics

