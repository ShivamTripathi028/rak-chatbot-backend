---
slug: /product-categories/wisblock/rak1903/datasheet/
title: RAK1903 WisBlock Ambient Light Sensor Module Datasheet
description: Provides comprehensive information about your RAK1903 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak1903/rak1903.png"
keywords:
  - datasheet
  - wisblock
  - RAK1903
sidebar_label: Datasheet
---

# RAK1903 WisBlock Ambient Light Sensor Module Datasheet

## Overview

### Description

The RAK1903 WisBlock Ambient Light Sensor Module, part of the RAK Wireless Wisblock series, is a single-chip ambient light sensor, measuring the intensity of light in the visible range. The precise spectral response and strong IR rejection of the device enables the RAK1903 module to accurately measure the intensity of light as seen by human eyes regardless of light sources. The strong IR rejection also aids in maintaining high accuracy when the industrial design requires to mount the sensor under dark glass due to aesthetic reasons. The RAK1903 module is designed for systems that create light-based experiences for humans. It is an ideal replacement for photodiodes, photoresistors, or other ambient light sensors with less visible range matching and IR rejection.

### Features
* **Measurement range**: 0.01 to 83865 lux
* Optical filtering to match human eye
* **Voltage Supply**: 3.3 V
* **Current Consumption**: 0.4 uA to 3.7 uA
* **Chipset**: TI OPT3001DNPR
* **Module size**: 10 x 10 mm

## Specifications
### Overview

#### Mounting

**Figure 1** shows the mounting mechanism of the RAK1903 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. The RAK1903 module can be mounted on the slots: **A, C, D, E, & F**.

> **Image:** RAK1903 WisBlock Sensor Mounting

### Hardware

The hardware specification is categorized into six parts. It shows the chipset of the module and discusses the pinouts, sensors, and the corresponding functions and diagrams. It also covers the electrical and mechanical parameters that include the tabular data of the functionalities and standard values of the RAK1903 WisBlock Ambient Light Sensor Module.

####  Chipset
| Vendor | Part number |
| ------ | ----------- |
| TI     | OPT3001DNPR |

#### Pin Definition

The RAK1903 WisBlock Ambient Light Sensor Module comprises a standard WisBlock connector. The WisBlock connector allows the RAK1903 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 2**.

> **Image:** RAK1903 WisBlock Sensor connector pinout

:::tip NOTE
Only the **I2C** related pins, **INT** pins, **VDD**, and **GND** are connected to this module.
:::

The pin12 or pin13 are connected to the INT of OPT3001DNPR (See **Figure 3**). The device has an interrupt reporting system that allows the Controller connected to the I2C bus to go to sleep until a user-defined event occurs. Alternatively, this mechanism can also be used with any system that can take advantage of a single digital signal that indicates whether the light is above or below the levels of interest.

If a 24-pin WisBlock Sensor connector is used, the IO used for the output pulse depends on what slot the module is plugged in. The following table shows the default IO used for different slots:

| SLOT A | SLOT B | SLOT C | SLOT D | SLOT E | SLOT F |
| ------ | ------ | ------ | ------ | ------ | ------ |
| WB_IO1 | WB_IO2 | WB_IO3 | WB_IO5 | WB_IO4 | WB_IO6 |

#### Sensors
##### Ambient Light Sensor
| Parameter                                                   | Test Condition                                                                                                   | Min. |     Typ.     |     Max.      |         Unit         |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---- | :----------: | :-----------: | :------------------: |
| Peak irradiance spectral responsibility                     |                                                                                                                  |      |     550      |               |          nm          |
| Resolution (LSB)                                            | Lowest full-scale range, RN[3:0] = 0000b                                                                         |      |     0.01     |               |         lux          |
| Full-scale illuminance                                      |                                                                                                                  |      |   83865.6    |               |         lux          |
| Measurement output result                                   | 0.64 lux per ADC code 
 2620.90 lux full-scale 
 (RN[3:0] = 0110) 
 2000 lux input | 2812 |     3125     |     3437      |      ADC codes       |
|                                                             |                                                                                                                  | 1800 |     2000     |     2200      |         lux          |
| Relative accuracy between gain ranges                       |                                                                                                                  |      |     0.2%     |               |                      |
| Infrared response (850 nm)                             |                                                                                                                  |      |     0.2%     |               |                      |
| Light source variation (incandescent, halogen, fluorescent) | Bare device 
 no cover glass                                                                                |      |      4%      |               |                      |
| Linearity                                                   | Input luminance > 40 lux 
 Input luminance < 40 lux                                               |      | 2% 
 5% |               |                      |
| Measured drift across temperature                           | Input luminance = 2000 lux                                                                                  |      |     0.01     |               |         %/°C         |
| Dark condition, ADC output                                  | 0.01 lux per ADC code                                                                                       |      |  0 
 0  | 3 
 0.03 | ADC codes 
 lux |
| Half-power angle                                            | 50% of full-power reading                                                                                        |      |      47      |               |       degrees        |

#### Electrical Characteristics
##### Recommended Operating Conditions

| Symbol           | Description                      | Min.  | Nom.  | Max.  | Unit  |
| ---------------- | -------------------------------- | :---: | :---: | :---: | :---: |
| V<sub>DD</sub>   | Power supply for the module      |  1.6  |  3.3  |  3.6  |   V   |
| I<sub>shut</sub> | Shutdown current                 |   -   |  0.4  |   -   |  uA   |
| I<sub>DD</sub>   | Active V<sub>DD</sub>=3.6 V |   -   |  3.7  |   -   |  uA   |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 3** shows the dimensions and the mechanic drawing of the RAK1903 module.

> **Image:** RAK1903 WisBlock Sensor Mechanic Drawing

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

#### Schematic Diagram

Figure 5 shows the schematic of the RAK1903 module.

> **Image:** RAK1903 WisBlock Sensor schematics

