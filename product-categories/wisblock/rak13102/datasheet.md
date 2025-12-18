---
slug: /product-categories/wisblock/rak13102/datasheet/
title: RAK13102 WisBlock Blues Notecarrier Module Datasheet
description: Provides comprehensive information about your RAK13102 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak13102/rak13102.png"
keywords:
    - RAK13102
    - wisblock
    - datasheet
sidebar_label: Datasheet
---

# RAK13102 WisBlock Blues Notecarrier Module Datasheet

## Overview

### Description

**WisBlock RAK13102 Blues Notecarrier Module** is a part of the WisBlock Wireless series. It provides an interface to connect cellular Blues.IO Notecards to the WisBlock system.

### Features

- M.2 Blues.IO Notecard connector
- Blues Notecard NOTE-NBGL-500
- Quectel BG-95 M3
- Supports LTE-M, NB-IoT and GSM networks
- IPEX connectors for the cellular and GNSS antenna
- USB Type C debug and log output connector
- Nano SIM and ESIM options
- Two WisBlock Sensor Slot connectors
- 3.3 V power supply (requires an additional battery for operation)
- Small size: 29 mm x 50 mm

## Specifications

### Overview

The RAK13102 module can be mounted on the IO slot of the WisBlock Base board. **Figure 1** shows the mounting mechanism of the RAK13102 on a WisBlock Base module, such as a RAK19007.

> **Image:** RAK13102 mounting mechanism on a WisBlock Base module

### Hardware

The hardware specification is categorized into five parts. It shows the chipset of the module and discusses the pinouts and their corresponding functions and diagrams. It also covers the electrical and mechanical parameters that include the tabular data of the functionalities and standard ratings of the RAK13102 WisBlock GSM/GPRS Module.

#### Chipset

| Vendor   | Part number            |
| -------- | ---------------------- |
| Blues.IO | NoteCard NOTE-NBGL-500 |

#### Pin Definition

The RAK13102 WisBlock Blues Notecarrier module comprises a standard WisBlock IO slot connector. The WisBlock connector allows the RAK13102 module to be mounted on a WisBlock baseboard with an IO slot, such as RAK19007. The pin order of the connector and the pinout definition are shown in **Figure 2**.

> **Image:** RAK13102 Connector Pin Definition

:::tip NOTE
- RAK13102 WisBlock IO slot connector utilizes the **I2C** related pins, **ATTNP** via WB_IO5, **VBAT**, **3V3**, and **GND**.

- **VBAT** is the battery voltage input with a max voltage of 4.2 V. During cellular data mode, the peak current is ~2000 mA, respectively, which exceeds the USB port supply current. That is why you must use a dedicated battery.
:::

:::tip IMPORTANT
This datasheet covers only the specifications of the WisBlock Notecarrier module RAK13102. For detailed information on the Blues.IO Notecard, please check the Blues.IO datasheets from the [Blues Resources](https://dev.blues.io/datasheets/notecard-datasheet/note-nbgl-500/)
:::

#### Power Supply with External 5V

:::tip Info
The RAK13102 module and the connected WisBlock Base Board and Core module can be supplied with a regulated 5 V DC supply through the P1 connector on the bottom. A matching connector is available with our [M8 Power Connector.](https://store.rakwireless.com/products/m8-power-connector)
:::

> **Image:** 5V supply through M8 power connector

> **Image:** M8 power connector

#### Electrical Characteristics

##### Absolute Maximum Ratings

| Parameter                  | Minimum | Maximum | Unit |
| -------------------------- | ------- | ------- | ---- |
| VBAT                       | -0.3    | +4.2    | V    |
| VBUS                       | -0.3    | +5.5    | V    |
| EX_POWER                   | -0.3    | +5.5    | V    |
| Power supply peak current0 | 0       | 2       | A    |

##### Power Supply Ratings

| Symbol   | Description                      | Condition                               | Min. | Nom. | Max. | Unit |
| -------- | -------------------------------- | --------------------------------------- | ---- | ---- | ---- | ---- |
| VBAT     | Supply Voltage                   | Input voltage must be within this range | 3.3  | 4.0  | 4.2  | V    |
| EX_POWER | Supply Voltage                   | Input voltage must be within this range | 4.5  | 5.0  | 5.5  | V    |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 5** shows the dimensions and the mechanical drawing of the RAK13102 module.

:::tip IMPORTANT
The dimensions are without the Blues Notecard!
:::

> **Image:** RAK13102 Mechanical Drawing

##### WisConnector PCB Layout

> **Image:** WisConnector PCB Footprint and Recommendations

#### Schematic Diagram

##### Power Supply

The Blues.IO Notecard main power supply comes from **VBAT**, which is a battery voltage connected to the WisBlock Base board. **EX_POWER** is the supply from an externally regulated 5 V DC supply.

> **Image:** RAK13102 Power Supply

##### SIM Circuit

**Figure 8** shows the schematic of the RAK13102 module with the slot for a standard SIM card and an optional **ESIM** PCB footprint.

> **Image:** RAK13102 Notecarrier Module SIM Circuit

##### WisConnector

RAK13102 WisBlock IO slot connector utilizes **I2C** related pins, **ATTNP** via WB_IO5, **VBAT**, **3V3**, and **GND**.

> **Image:** RAK13102 Notecarrier IO Slot Connector

##### Debug Connector

**Figure 10** shows the RAK13102 USB debugging circuit.

> **Image:** RAK13102 USB Debugging

##### Blues Notecard M.2 connector

**Figure 11** shows the RAK13102 M.2 connector that is the interface to the Blues.IO Notecards.

> **Image:** RAK13102 Module M.2 Connector

##### WisBlock Sensor Slots

:::tip NOTE
When assembled in the IO slot, the RAK13102 IO module is covering the standard WisBlock Sensor Slots A and B. These two Sensor Slots are available on the RAK13102 module with the same functionality as the Sensor Slots on the Base Boards
:::

**Figure 12** shows the RAK13102 Sensor Slot Connectors.

> **Image:** RAK13102 Module Sensor Slots

