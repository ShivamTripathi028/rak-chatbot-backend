---
slug: /product-categories/wisblock/rak12039/datasheet/
title: RAK12039 WisBlock Particle Matter Sensor Module Datasheet
description: RAK12039 is a WisBlock Sensor Module that extends the WisBlock system with Particle Matter sensing. It is based on PMSA003I digital particle concentration sensor, which obtains the number of suspended particles in the air.
image: https://images.docs.rakwireless.com/wisblock/rak12039/rak12039.png
keywords:
    - RAK12039
    - wisblock
    - datasheet
sidebar_label: Datasheet
---

# RAK12039 WisBlock Particle Matter Sensor Module Datasheet

## Overview

### Description

The RAK12039 is a Particle Matter Sensor module that is part of the RAKWireless WisBlock Sensor series. It is based on PMSA003I digital particle concentration sensor, which obtains the number of suspended particles in the air. It is interfaced via I2C bus and allows you to capture standard PM1.0, PM2.5, and PM10 values, as well as, a number of particles in micrometer on a 0.1 L particle standard volume.

### Features

  * Minimum distinguishable particle diameter: **0.3 micrometer**
  * Particle range of measurement:
    + **0.3~1.0 Micrometer（μm)**
    + **1.0~2.5 Micrometer（μm)**
    + **2.5~10 Micrometer（μm)**
  * I2C Interface
  * Power supply voltage：**5.0 V (on-board boost converter)**
  * Interface voltage: **3.3 V**
  * Active current: **< 100 mA**
  * Standby current: **< 200 uA**
  * Operating temperature: **-10° C ~ 60° C**
  * Storage temperature: **-40° C ~ 80° C**
  * Module size: **25 x 15 mm**
  * Particle Matter PMSA003I size: **38 x 35 x 12 mm**

## Specifications

### Overview

> **Image:** RAK12039 WisBlock Particle Matter Sensor Module - Top View

> **Image:** RAK12039 WisBlock Particle Matter Sensor Module - Bottom View

#### Mounting

The RAK12039 WisBlock Particle Matter Sensor Module can be mounted to the IO slot of the [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. **Figure 3** shows the mounting mechanism of the RAK12039 on a WisBlock Base module.

> **Image:** RAK12039 WisBlock Particle Matter Sensor mounting

### Hardware

The hardware specification is categorized into five (5) parts. It shows the chipset of the module and discusses the pinouts and their corresponding functions and diagrams. It also covers the electrical and mechanical characteristics that include the tabular data of the functionalities and standard values of the RAK12039 WisBlock Particle Matter Sensor Module.

####  Chipset

| Vendor    | Part Number |
| --------- | ----------- |
| Plantower | PMSA003I    |

#### Pin Definition

The RAK12039 WisBlock Particle Matter Sensor Module comprises a standard 40-pin WisConnector. The WisConnector allows the RAK12039 module to be mounted to a WisBlock Base Board. The pin order of the connector and the pinout definition is shown in **Figure 4**.

:::tip NOTE
 **VBAT**, **3V3_S**, **GND**, **I2C** pins, **RESET**, and **SET**  are connected to 40-pin WisConnector.
:::

> **Image:** RAK12039 WisBlock Particle Matter Sensor pinout

#### Electrical Characteristics

##### Recommended Operating Conditions

| Symbol           | Description                                | Min. | Nom. | Max. | Unit |
| ---------------- | ------------------------------------------ | ---- | ---- | ---- | ---- |
| 3V3_S            | Supply voltage to on-board boost converter | 2.2  | 3.3  |   -  | V    |
| VCC              | PMSA003I Supply voltage                    | 4.5  | 5.0  | 5.5  | V    |
| I2C Voltage Rail | Supply voltage                             | -    | 3.3  |   -  | V    |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 5** shows the dimensions and the mechanic drawing of the RAK12039 module.

> **Image:** RAK12039 WisBlock Particle Matter Sensor Module mechanic drawing

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

#### Schematic Diagram

The I2C address of RAK12039 is 0x12. R10 and R11 do not need to be mounted on the RAK12039 due to the pull-up resistors already on the WisBlock Base board.

> **Image:** RAK12039 schematic diagram

####  PMSA003I Installation Notes

1) Metal shell is connected to the GND, so be careful not to let it get shorted with the other parts of the circuit.
2) The best way of installation is to make the plane of the inlet and outlet close to the plane of the host. Or some shield should be placed between the inlet and outlet to prevent the airflow from the inner loop.
3) The blowhole in the shell of the host should not be smaller than the inlet.
4) The sensor should not be installed in the airflow way of the air cleaner or should be shielded by some structure.
5) When the sensor is used for outdoor fixed equipment, the equipment should be completed with protection from the sandstorm, rain, snow, etc.
6) The two screw holes can be used for positioning and fixing. For fixing holes, the screw depth can reach 3.4 mm, and the other should not exceed 1.9 mm.

