---
slug: /product-categories/wisblock/rak1910/datasheet/
title: RAK1910 WisBlock GNSS Location Module Datasheet
description: Provides comprehensive information about your RAK1910 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device's components.
image: "https://images.docs.rakwireless.com/wisblock/rak1910/rak1910.png"
keywords:
  - datasheet
  - wisblock
  - RAK1910
sidebar_label: Datasheet
---

# RAK1910 WisBlock GNSS Location Module Datasheet

## Overview

> **Image:** RAK1910 WisBlock GNSS Location Module

### Description

The RAK1910 WisBlock GNSS Location Module module, part of the RAK Wireless Wisblock series, is a u-blox MAX-7Q GNSS (GPS, GLONASS, QZSS, and SBAS) module. This module features exceptional performance, high sensitivity, and minimal acquisition time, which makes it suitable for low-power IoT solutions. The RAK1910 positioning module is a GNSS receiver. It receives and tracks the GPS (including SBAS and QZSS) and the GLONASS signals. QZSS and SBAS signals (by default) can be received concurrently with GPS signals.

### Features
* **Voltage Supply**: 3.3 V
* **Current Consumption**: 15 uA to 22 mA
* **Chipset**: u-Blox MAX-7Q
* High accuracy of 2.5 m
* **Update rate**: 10 Hz
* **Velocity accuracy**: 0.1 m/s
* **Heading accuracy**: 0.5 degrees
* Fast location fix. 29 sec from cold start to first fix. 1 sec from hot start
* GPS and GLONASS satellite support
* **Module size**: 10 x 23 mm

## Specifications
### Overview

#### Mounting

**Figure 2** shows the mounting mechanism of the RAK12001 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. The RAK12001 module can be mounted on the slots: **A, E, F**.

> **Image:** RAK1910 WisBlock GNSS Location Module Mounting

### Hardware

The hardware specification is categorized into six parts. It shows the chipset of the module and discusses the pinouts, sensors, and the corresponding functions and diagrams. It also covers the electrical and mechanical parameters that include the tabular data of the functionalities and standard values of the RAK1910 WisBlock GNSS Location Module.

####  Chipset
| Vendor | Part number |
| ------ | ----------- |
| u-Blox | MAX-7Q      |

#### Pin Definition

The RAK1910 WisBlock GNSS Location Module comprises a standard WisBlock connector. The WisBlock connector allows the RAK1910 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 3**.

> **Image:** RAK1910 WisBlock GNSS Location Module Pinout Diagram

:::tip NOTE
- Only the **UART**-related pins, **1PPS** pin, **RESET** pin, **VDD**, and **GND** are connected to this module.
- The RAK1910 module can be installed in the Slot A only.
:::

If a 24-pin WisBlock Sensor connector is used, the IO used for the output pulse depends on what slot the module is plugged in. The following table shows the default IO used for different slots:

| SLOT A | SLOT E | SLOT F |
| ------ | ------ | ------ |
| WB_IO1 | WB_IO4 | WB_IO6 |

#### Sensors
##### GNSS Sensor

| Parameter | Specification |  |  |
| --- | --- | --- | --- |
| Receiver Type | 56 Channels u-blox 7 engine |  |  |
| Receiver Type | GPS/QZSS L1C/A |  |  |
| Receiver Type | SBAS: WAAS, EGNOS, MSAS |  |  |
| Time-To -First-Fix |  | MAX-7QW | MAX-7C |
| Time-To -First-Fix | Cold Start | 29s | 30s |
| Time-To -First-Fix | Warm Start | 28s | 28s |
| Time-To -First-Fix | Hot Start | 1s | 1s |
| Time-To -First-Fix | Aided Starts | 5s | 5s |
| Sensitivity |  | MAX-7QW | MAX-7C |
| Sensitivity | Tracking & Navigation | -161 dBm | -160 dBm |
| Sensitivity | Reacquisition | -160 dBm | -160 dBm |
| Sensitivity | Cold Start | -148 dBm | -147 dBm |
| Sensitivity | Warm Start | -148 dBm | -148 dBm |
| Sensitivity | Hot Start | -156 dBm | -155 dBm |
| Horizontal Position Accuracy | Autonomous | 2.5 m |  |
|  | SBAS | 2.0 m |  |

#### Electrical Characteristics

##### Recommended Operating Conditions
| Symbol           | Description                 | Min.  | Nom.  | Max.  | Unit  |
| ---------------- | --------------------------- | :---: | :---: | :---: | :---: |
| V<sub>DD</sub>   | Power supply for the module |  2.7  |  3.3  |  3.6  |   V   |
| I<sub>BCKP</sub> | Backup battery current      |   -   |  15   |   -   |  uA   |
| I<sub>cc</sub>   | Acquisition                 |   -   |  22   |   -   |  mA   |
| I<sub>cc</sub>   | Tracking                    |   -   | 17.5  |   -   |  mA   |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 3** shows the dimensions and the mechanic drawing of the RAK1910 module.

> **Image:** RAK1910 WisBlock GNSS Location Module Mechanic Drawing

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

#### Schematic Diagram
Figure 5 shows the schematic of the RAK1910 module.

> **Image:** RAK1910 WisBlock GNSS Location Module Schematic

