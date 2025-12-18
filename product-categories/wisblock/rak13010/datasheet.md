---
slug: /product-categories/wisblock/rak13010/datasheet/
title: RAK13010 WisBlock SDI-12 Module Datasheet
description: Covers the comprehensive information of your RAK13010 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisblock/rak13010/rak13010.png
keywords:
  - datasheet
  - wisblock
  - RAK13010
sidebar_label: Datasheet
---

# RAK13010 WisBlock SDI-12 Module Datasheet

## Overview

### Description

RAK13010 is a WisBlock Interface module that extends the WisBlock system. The SDI-12 (Serial Digital Interface at 1200 baud rate) module is an asynchronous serial communications protocol for intelligent sensors that monitor environment data. It consists of 3 wires: **SDI-12_12V**, **SDI-12_DATA**, and **GND**.

The SDI-12 bus is a bidirectional interface for the conversion of commands and data into UART to SDI-12 and vice versa using a 3.3 V microcontroller. The data logger requests data from the intelligent sensors, each identified with a unique address. In short, The data logger is the master, and the sensors are slave devices on the bus. The RAK13010 makes it easier for you to connect wires from multiple SDI-12 sensors into one set of terminals on a data logger.
### Features

  * Voltage supply: **VBAT and 3.3 V**
  * SDI-12 communications protocol
  * Supports the 3-wire SDI-12 communication cable
  * Provides a built-in 12 V step-up supply (300 mA max) for the SDI-12 sensors and has an option to use an external 12 V supply if required.
  * Operating temperature: **-40° C ~ 85° C**
  * Module size: 35 x 25 mm

## Specifications

### Overview

> **Image:** RAK13010 WisBlock SDI-12 Module top and bottom view

#### Mounting

The RAK13010 WisBlock SDI-12 Module can be mounted on the IO slot of the WisBlock Base board. **Figure 2** shows the mounting mechanism of the RAK13010 on a WisBlock Base module.

> **Image:** RAK13010 mounting mechanism on a WisBlock Base module

### Hardware

The hardware specification is categorized into four (4) parts. It discusses the pinouts and their corresponding functions and diagrams of the module. It also covers the electrical and mechanical characteristics that include the tabular data of the functionalities and standard values of the RAK13010 WisBlock SDI-12 Module.

#### Pin Definition

The RAK13010 WisBlock module has a 40-pin WisConnector that is compatible with the WisBlock Base IO Slot. The pin order of the connector and the pinout definition is shown in **Figure 3**.

> **Image:** RAK13010 pinout diagram

:::tip NOTE
- Only **VBAT**, **3V3_S**, **IO2**, **RXD**, **TXD**, **OE**, and **GND** are connected to the WisBlock Connector.
- **3V3_S** voltage output from the WisBlock Base that powers the RAK13010 module can be controlled by the WisBlock Core via WB_IO2 (WisBlock IO2 pin). This makes the module ideal for low-power IoT projects since the WisBlock Core can disconnect the power of the RAK13010 module.
:::

#### Electrical Characteristics

This section shows the maximum and minimum ratings of the RAK13010 module and its recommended operating conditions. Refer to the table presented below.

##### Recommended Operating Conditions

| Symbol | Description | Min. | Typ. | Max. | Unit |
| --- | --- | --- | --- | --- | --- |
| 3V3_S | 3V3_S | - | 3.3 | - | V |
| VBAT | Battery | - | 4.2 | - | V |
| 5V | SN74LVC1G125DBVR supply voltage | - | 5 | - | V |
| 12V | Internal 12 V | - | 12 | - | V |
| 12V | Internal 12 V Output Current | - | - | 300 | mA |
| 12V_EX | External 12 V | - | 12 | - | V |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 4** shows the mechanical dimensions of the RAK13010 module.

> **Image:** RAK13010 mechanical dimensions

##### WisBlock Connector PCB Layout

> **Image:** WisBlock Connector PCB footprint and recommendations

#### Schematic Diagram

##### 12 V Power Supply Selection

**For Internal 12 V Power Supply**

- When you want to use the internal 12 V as the power supply for sensors, you need to install a jumper on pin 1 and pin 2 of J3.

**For External 12 V Power Supply**

- When you want to use an external 12 V as the power supply for sensors, you need to install a jumper on pin 2 and pin 3 of J3.
- Then connect the following:
    - 12 V line of external 12 V to pin 1 of J2;
    - GND line of external 12 V to pin 4 of J2.
- When using an external 12 V, the EN pin of U1 will be pulled low, so that U1 will be closed.

##### Conversion of SDI-12 and UART

The signal level conversion circuit interfaces a 3.3 V microcontroller with a 1200 baud UART to the SDI-12 bus. Q2 is a voltage translator, which translates the 5 V signal from the SDI bus to 3.3 V. U3 translates the 3.3 V from the UART TXD line to 5 V, and allows the microcontroller to place the line in the high impedance state when not transmitting, but de-asserting the OE line.

**Figure 6** shows the timing diagram of the RAK13010 module.

- **t0**: send data to the SDI-12 data bus
- **t1**: receive data from the SDI-12 data bus

> **Image:** RAK13010 WisBlock SDI-12 Module timing diagram

**Figure 7** below shows the schematic diagram of the RAK13010 module.

> **Image:** RAK13010 WisBlock SDI-12 Module schematic diagram

