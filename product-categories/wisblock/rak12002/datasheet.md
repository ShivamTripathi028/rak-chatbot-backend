---
slug: /product-categories/wisblock/rak12002/datasheet/
title: RAK12002 WisBlock RTC Module Datasheet
description: Provides comprehensive information about your RAK12002 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak12002/rak12002.png"
keywords:
  - datasheet
  - RAK12002
  - wisblock
sidebar_label: Datasheet
---

# RAK12002 WisBlock RTC Module Datasheet

## Overview

### Description

The RAK12002 is a Real-Time Clock module, part of the RAK Wireless WisBlock Series, designed to provide real-time clock capabilities to your WisBlock projects. The RTC chip is based on the RV-3028-C7 from Micro Crystal and uses the I2C interface.

### Features

- Built-in 32.768 kHz crystal oscillator
- Counters for seconds, minutes, hours, date, month, year, and day of the week.
- Automatic leap-year correction
- 3.3 V power supply
- I2C Interface
- Programmable Clock output
- Extreme low-current consumption 40 nA
- Super capacitor backup power supply
- Chipset: Micro Crystal RV-3028-C7
- Small size: 10 mm x 10 mm

## Specifications

### Overview

#### Mounting

The RAK12002 RTC module can be mounted on slot A, B, C, or D of the WisBlock Base board. Figure 1 shows the mounting mechanism of the RAK12002 on a WisBlock Base board.

> **Image:** RAK12002 WisBlock RTC Module Mounting

### Hardware

The hardware specification is categorized into five parts. It shows the chipset of the module and discusses the pinouts of the module and its corresponding functions and diagrams. It also covers the electrical and mechanical parameters, which include the tabular data of the functionalities and standard values of the RAK12002 WisBlock RTC Module.

#### Chipset
| Vendor        | Part number |
| ------------- | ----------- |
| Micro Crystal | RV-3028-C7  |

#### Pin Definition

The RAK12002 WisBlock RTC module includes a standard WisConnector. The WisConnector allows the RAK12002 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in Figure 2.

:::tip NOTE
**I2C** related pins,**INT**, **CLKOUT**, **3V3**, and **GND** are connected to WisConnector.
:::

> **Image:** RAK12002 WisBlock RTC Module Pinout

#### Electrical Characteristics

| Symbol  | Description                                                                       | Min. | Nom. | Max. | Unit |
| ------- | --------------------------------------------------------------------------------- | ---- | ---- | ---- | ---- |
| VDD     | Power Supply Voltage                                                              | -    | 3.3  | -    | V    |
| VBACKUP | Backup Supply Voltage                                                             | -    | 3.3  | -    | V    |
| IDD     | VDD supply current timekeeping I2C-bus inactive, CLKOUT disabled, average current | -    | -    | 400  | nA   |

#### Mechanical Characteristic

##### Board Dimensions

Figure 3 shows the dimensions and the mechanic drawing of the RAK12002 module.

> **Image:** RAK12002 WisBlock RTC Module Mechanic Drawing

##### WisConnector PCB Layout

> **Image:** WisConnector PCB Footprint and Recommendations

#### Schematic Diagram

Figure 5 shows the RAK12002 RTC Module Schematic Diagram. C2 and C3 are supercapacitors, default uses C2, 70 mF/3.3 V, 11 mF/3.3 V for reserved.

> **Image:** RAK12002 WisBlock RTC Module Schematic

