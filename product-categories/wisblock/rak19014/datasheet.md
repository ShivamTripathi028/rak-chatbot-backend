---
slug: /product-categories/wisblock/rak19014/datasheet/
title: RAK19014 WisBlock Battery USB Power Slot Module Datasheet
description: Provides comprehensive information about the RAK19014 to help you use it. This information includes technical specifications, characteristics, and requirements, and also discusses the device components.
image: https://images.docs.rakwireless.com/wisblock/rak19014/rak19014.png
keywords:
  - datasheet
  - wisblock
  - RAK19014
sidebar_label: Datasheet
---

# RAK19014 WisBlock Battery USB Power Slot Module Datasheet

## Overview

### Description

The RAK19014 WisBlock Battery USB Power Slot Module is a modular power board comprising a battery connector (no charging circuitry onboard) and a USB Type-C connector used for reprogramming the WisBlock Core. It is designed for use with the WisBlock Base Board with Power Slot via the 40-pin WisBlock connector.

Optimally designed to support very low-power applications, the RAK19014 features only a USB connector, battery connector, and a 3.3 V switching regulator in the circuit, eliminating unnecessary components that contribute to extra current consumption.

### Features

- Designed for battery-only powered applications.
- Supports reprogramming of the WisBlock Core via USB connector.
- High-efficiency switching regulator.
- Optimized for low-power devices.
- Module size: 30 mm x 20 mm

## Specifications

### Overview

The RAK19014 module can be mounted on the power slot of the WisBlock Base board. **Figure 1** shows the mounting mechanism of the RAK19014 on a WisBlock Base module, such as the RAK19010.

> **Image:** RAK19014 mounting mechanism on a WisBlock Base module

### Hardware

The hardware specification is categorized into six parts. It discusses the interfacing, pinouts, and their corresponding functions and diagrams of the module. It also covers the electrical, environmental, and mechanical characteristics, including tabular data of the functionalities and standard values of the RAK19014 WisBlock Battery Power Slot Module.

#### Interfaces

The RAK19014 WisBlock Battery Power Slot Module provides the following interfaces:

* Two-pin battery interface
* Two LEDs
* One reset button
* One USB connector

> **Image:** USB, battery, and reset

> **Image:** WisBlock 40-pin board-to-board connector

##### Battery Connector

**Figure 4** shows the battery connector V+(VBAT) and V-(GND).

> **Image:** Battery polarity

:::tip NOTE
The voltage of the battery must not exceed 4.3 V.
:::

##### LEDs

Two LEDs are used to indicate the operating status. Their functions are:

- 🟢 **Green LED** - Connected to the MCU module, controlled by MCU defined by the user.
- 🔵 **Blue LED** - Connected to the MCU module, controlled by MCU defined by the user.

##### RESET Push Button

The Reset Push Button is shown in [**Figure 2**](#interfaces) and is connected to the MCU module. When pushed, it resets the MCU.

#### Pin Definition

The RAK19014 Battery Power Slot Module has a 40-pin WisConnector compatible with the WisBlock Power Slot. The connector's pin order and pinout definition are shown in **Figure 5**.

:::tip NOTE
VBAT, 3V3, RESET, LED1, LED2, and GND are connected to the WisBlock IO connector.
:::

> **Image:** RAK19014 pinout diagram

#### Electrical Characteristics

##### Absolute Maximum Ratings

The absolute maximum ratings of the device are shown in the table below. Stress ratings are for the functional operation of the device.

:::warning
1. If the stress rating exceeds the listed value, it may cause permanent damage to the device.
2. Exposure to maximum rated conditions may affect device reliability.
:::

| Ratings                    | Maximum Value   | Unit |
| -------------------------- | --------------- | ---- |
| Battery voltage (**VBAT**) | –0.3 to 4.3     | V    |
| IOs of WisConnector        | –0.3 to VDD+0.3 | V    |

#### Mechanical Characteristic

##### Board Dimensions

The mechanical dimensions of the RAK19014 module are shown in **Figure 6** below.

> **Image:** RAK19014 mechanical dimensions

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

#### Environmental Characteristics

The table below lists the operation and storage temperature requirements of RAK19014:

| **Parameter**                 | **Minimum** | **Typical** | **Maximum** |
| ----------------------------- | :---------: | :---------: | :---------: |
| Operational temperature range | –35º C | +25º C | +75º C |
| Extended temperature range    | –40º C | +25º C | +80º C |
| Storage temperature range     | –40º C | +25º C | +80º C |

#### Schematic Diagram

**Figure 8** shows the schematic of the RAK19014 power slot module.

> **Image:** RAK19014 schematics

<!-- ## Models / Bundles

|                               | **RAK19012** | **RAK19013** | **RAK19014** | **RAK19015** | **RAK19016** | **RAK19017** |
| ----------------------------- | --------- | --------- | --------- | --------- | --------- | --------- |
| Product Image                 | <img src="https://images.docs.rakwireless.com/wisblock/rak19012/rak19012.png" alt="img " style={{zoom:'15%'}}/>| <img src="https://images.docs.rakwireless.com/wisblock/rak19013/rak19013.png" alt="img " style={{zoom:'15%'}}/>| <img src="https://images.docs.rakwireless.com/wisblock/rak19014/rak19014.png" alt="img " style={{zoom:'15%'}}/>| <img src="https://images.docs.rakwireless.com/wisblock/rak19015/rak19015.png" alt="img " style={{zoom:'15%'}}/>|<img src="https://images.docs.rakwireless.com/wisblock/rak19016/rak19016.png" alt="img " style={{zoom:'15%'}}/>| <img src="https://images.docs.rakwireless.com/wisblock/rak19017/rak19017.png" alt="img " style={{zoom:'15%'}}/> |
| Features |  <ul><li> USB-C connector for programming and debugging the WisBlock Core 
</li><li> Compatible with LiPo rechargeable batteries
</li><li> Solar panel connector for battery charging
</li><li> Onboard battery charger chip
</li><li> LEDs for charging status and user-configurable LEDs  </li></ul> |   <ul><li> Flexible building-block design enabling modular function realization and expansion.
</li><li> Low-power battery power supply.
</li><li> Supports lithium-ion battery charging. 
</li><li> Supports solar charging.
</li><li> Meets industrial-level design requirements.  </li></ul>| <ul><li>  Designed for battery-powered applications 
</li><li> Supports reprogramming of WisBlock Core via USB connector
</li><li> High-efficiency switching regulator
</li><li> Optimized for low-power devices  </li></ul>| <ul><li> Designed for battery-only powered applications 
</li><li> High-efficiency switching regulator
</li><li> Optimized for low-power devices</li></ul>| <ul><li> Supports 5~24 V<sub>DC</sub> voltage supply input
</li><li> Uses three-pin screw terminal connector
</li><li> Compatible with LiPo rechargeable battery
</li><li> On-board battery charger chip
</li><li> LED for charging status and user-configurable LEDs
</li><li> Applicable to industrial and enterprise setting </li></ul>| <ul><li> POE Power Module (power supply only, no Ethernet connection capability) 
</li><li> 36 V to 57 V Input voltage range.
</li><li> Short-circuit protection and Over temperature protection  </li></ul>|
|Size|30 mm x 20 mm|30 mm x 20 mm|30 mm x 20 mm|30 mm x 20 mm|30 mm x 20 mm|30 mm x 50 mm|
|SKU|110088|110089|110104|100090|110091|100105| -->

