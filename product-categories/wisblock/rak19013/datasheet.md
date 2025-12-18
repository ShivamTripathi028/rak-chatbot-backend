---
slug: /product-categories/wisblock/rak19013/datasheet/
title: RAK19013 WisBlock LiPo Solar Power Slot Module Datasheet
description: Provides comprehensive information about the RAK19013 to help you use it. This information includes technical specifications, characteristics, and requirements, and also discusses the device's components.
image: https://images.docs.rakwireless.com/wisblock/rak19013/rak19013.png
keywords:
  - datasheet
  - wisblock
  - RAK19013
sidebar_label: Datasheet
---

# RAK19013 WisBlock LiPo Solar Power Slot Module Datasheet

## Overview

### Description

The RAK19013 WisBlock LiPo Solar module is a power board comprising a battery connector, a solar panel connector, a reset push button, a charger that can recharge a plugged-in battery, a charging LED indicating charging status, and a power connector for connection with a WisBlock Base board.

This board connects to a WisBlock Base board, such as the RAK19010, via the power slot.

### Features

- Flexible building-block design enabling modular function realization and expansion.
- Low-power battery power supply.
- Supports lithium-ion battery charging.
- Supports solar charging.
- Meets industrial-level design requirements.
- Module size: 30 mm X 20 mm

## Specifications

### Overview

> **Image:** RAK19013 WisBlock Power Module top (left) and bottom (right) view

### Mounting Sketch

The RAK19013 module can be mounted in the power slot of the WisBlock Base board. **Figure 2** shows the mounting mechanism of the RAK19013 on a WisBlock Base module, such as the RAK19010.

> **Image:** RAK19013 mounting mechanism on a WisBlock Base module

### Hardware

The hardware specification is categorized into six parts. It discusses the interfacing, pinouts, and their corresponding functions and diagrams of the module. It also covers the electrical, mechanical, and environmental characteristics, including tabular data of the functionalities and standard values of the RAK19013 WisBlock LiPo Solar Power Slot Module.

#### Interfaces

The RAK19013 WisBlock LiPo Solar Power Slot Module provides the following interfaces, headers, a button, and WisConnectors:

* One WisBlock power module
* Two-pin battery interface
* Two-pin solar interface
* Three LEDs
* One reset button

:::tip NOTE
The RAK19013 lacks a USB connector. Therefore, programming its core when used with the RAK19010 is impossible without a J-Link. To program the core, the RAK5804 is required; power is supplied via the RAK19013, and programming is done via the RAK5804.
:::

> **Image:** RAK19013 part labels

##### Battery Connector

**Figure 4** shows the battery connector V+ (VBAT) and V- (GND).

> **Image:** Battery connector pin order

:::tip NOTE
The voltage of the battery must not exceed 4.3 V.
:::

##### Solar Connector

A 5 V Solar panel can be connected to the board via the J2 connector to also serve the purpose of charging the battery. The matching connector for the solar panel wires is an <a href="https://www.jst-mfg.com/product/detail_e.php?series=287" target="_blank">JST ZHR-2 1.5 mm pitch female</a>. A cable assembly for the solar panel connector is also available for purchase in <a href="https://store.rakwireless.com/products/solar-panel-connector-cable" target="_blank">RAK store</a>.

**Figure 5** shows the solar connector V+ (VIN) and V- (GND).

> **Image:** Battery connector pin order

##### LEDs

Three LEDs indicate operating status. Their functions are:

- 🔴 **Red LED:** Connected to the charger chip to indicate charging status. It illuminates while the battery charges and dims or turns off when the battery is full.
- 🟢 **Green LED:** Connected to the MCU module and controlled by the user-defined MCU.
- 🔵 **Blue LED:** Connected to the MCU module and controlled by the user-defined MCU.

##### RESET Push Button

The Reset Push Button shown in [**Figure 3**](#interfaces) is connected to the MCU module. When pushed, it resets the MCU.

#### Pin Definition

The RAK19013 module has a 40-pin WisConnector compatible with the WisBlock Power Slot. The connector's pin order and pinout definition are shown in **Figure 6**.

:::tip NOTE
VBAT, 3V3, RESET, LED1, LED2, ADC_VBAT, and GND are connected to WisIO connector.
:::

> **Image:** RAK19013 pinout diagram

#### Electrical Characteristics

##### Absolute Maximum Ratings

The absolute maximum ratings of the device are shown in the table below. Stress ratings are for the functional operation of the device.

:::warning
1. If the stress rating exceeds the listed value, it may cause permanent damage to the device.
2. Exposure to maximum rated conditions may affect device reliability.
:::

| Ratings                                 | Maximum Value   | Unit |
| --------------------------------------- | --------------- | ---- |
| Battery voltage (**VBAT**)              | –0.3 to 4.3     | V    |
| Solar panel voltage (**VIN**)           | –0.3 to 5.5     | V    |
| IOs of WisConnector                     | –0.3 to VDD+0.3 | V    |

##### Panel Specification

The RAK19013 LiPo Solar Power Slot module can be powered by a battery connected to the J4 connector. The nominal operating voltage of the battery should be within the range shown in the following table.

| **Minimum** | **Typical** | **Maximum** | **Unit** |
| ----------- | ----------- | ----------- | -------- |
| 3.3         | 3.7         | 4.3         | V        |

A suitable Li-ion battery should have the following parameters as shown in the table below:

| **Parameter**     | **Value**            |
| ----------------- | -------------------- |
| Standard Voltage  | 3.7 V           |
| Charging Voltage  | 4.2 V           |
| Capacity          | As required          |
| Discharge current | At least 500 mA |

:::tip NOTE
When using a solar panel, you cannot use a non-rechargeable battery.
:::

#### Mechanical Characteristic

##### Board Dimensions

The mechanical dimensions of the RAK19013 module is shown in **Figure 7** below.

> **Image:** RAK19013 mechanical dimensions

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

#### Environmental Characteristics

The table below lists the operation and storage temperature requirements of RAK19013:

| **Parameter**                 | **Minimum** | **Typical** | **Maximum** |
| ----------------------------- | :---------: | :---------: | :---------: |
| Operational Temperature Range | –35º C | +25º C | +75º C |
| Extended Temperature Range    | –40º C | +25º C | +80º C |
| Storage Temperature Range     | –40º C | +25º C | +80º C |

#### Schematic Diagram

**Figure 9** shows the schematic of the RAK19013 LiPo Solar Power Slot module.

> **Image:** RAK19013 LiPo Solar Power Slot Module Schematics

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

