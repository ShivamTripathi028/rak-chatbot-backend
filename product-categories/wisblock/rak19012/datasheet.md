---
slug: /product-categories/wisblock/rak19012/datasheet/
title: RAK19012 WisBlock USB LiPo Solar Power Slot Module Datasheet
description: Provides comprehensive information about the RAK19012 to help you use it. This information includes technical specifications, characteristics, and requirements, and also discusses the device components.
image: https://images.docs.rakwireless.com/wisblock/rak19012/rak19012.png
keywords:
    - RAK19012
    - wisblock
    - datasheet
sidebar_label: Datasheet
---

# RAK19012 WisBlock USB LiPo Solar Power Slot Module Datasheet

## Overview

### Description

The RAK19012 WisBlock USB LiPo Solar Power Slot Module is a power board comprising a USB-C connector, battery connector with an onboard charger, solar panel connector, LED indicator for charge status, two user-configurable LEDs, a reset button, and a power connector for connection with the WisBlock Base board. This power board allows debugging and firmware uploading to the WisBlock Core via the USB-C connector.

### Features

- USB-C connector for programming and debugging the WisBlock Core
- Compatible with LiPo rechargeable batteries
- Solar panel connector for battery charging
- Onboard battery charger chip
- LED for charging status and user-configurable LEDs
- Module size: 30 mm X 20 mm

## Specifications

### Overview

> **Image:** RAK19012 WisBlock Power Module top (left) and bottom (right) view

### Mounting Sketch

The RAK19012 module can be mounted on the power slot of a WisBlock Base board with a power slot. **Figure 2** shows the mounting mechanism of the RAK19012 on a WisBlock Base module, such as the RAK19010.

:::warning

The RAK19012 **only** supports WisBlock Base boards with a power slot. It is not compatible with all WisBlock Base boards.

:::

> **Image:** RAK19012 mounting mechanism on a WisBlock Base module

### Hardware

The hardware specification is categorized into six parts. It discusses the interfacing, pinouts, and their corresponding functions and diagrams of the module. It also covers the electrical, mechanical, and environmental characteristics, including tabular data of the functionalities and standard values of the RAK19012 WisBlock LiPo Solar Power Slot Module.

#### Interfaces

The RAK19012 WisBlock LiPo Solar Power Slot Module provides the following interfaces:

* One WisBlock power module
* Two-pin battery interface
* Two-pin solar interface
* Three LEDs
* One reset button

> **Image:** RAK19012 part labels

#### Battery and Solar Panel Connector

**Figure 4** shows the polarity of battery and solar panel connectors.

> **Image:** Battery and solar panel connector polarity

##### LEDs

Three LEDs indicate the operating status. Their functions are:

- 🔴 **Red LED:** Connected to the charger chip to indicate charging status. It illuminates while the battery charges and dims or turns off when the battery is full.

- 🟢 **Green LED:** Connected to the MCU module and controlled by user-defined MCU settings.

- 🔵 **Blue LED:** Connected to the MCU module and controlled by user-defined MCU settings.

##### RESET Push Button

The Reset Push Button, as shown in <a href="https://docs.rakwireless.com/product-categories/wisblock/rak19012/datasheet/#interfaces" target="_blank">**Figure 3**</a>, is connected to the MCU module. When pushed, it resets the MCU.

#### Pin Definition

The RAK19012 module has a 40-pin WisConnector that is compatible with the WisBlock Power Slot. The pin order of the connector and the pinout definition is shown in **Figure 5**.

:::tip NOTE
VBAT, 3V3, RESET, LED1, LED2, ADC_VBAT, and GND are connected to the WisIO connector.
:::

> **Image:** RAK19012 pinout diagram

#### Electrical Characteristics

##### Absolute Maximum Ratings

The absolute maximum ratings of the device are shown in the table below. Stress ratings are for the functional operation of the device.

:::warning
1. If the stress rating exceeds the listed value, it may cause permanent damage to the device.
2. Exposure to maximum rated conditions may affect device reliability.
:::

| Ratings                       | Maximum Value   | Unit |
| ----------------------------- | --------------- | ---- |
| Battery voltage (**VBAT**)    | –0.3 to 4.3     | V    |
| Solar panel voltage (**VIN**) | –0.3 to 5.5     | V    |
| IOs of WisBlock Connector     | –0.3 to VDD+0.3 | V    |

##### Battery Specification

The RAK19012 USB LiPo Solar Power Slot Module can be powered by a battery connected to the J4 connector. The battery's nominal operating voltage should be within the range shown in the following table.

| **Minimum** | **Typical** | **Maximum** | **Unit** |
| ----------- | ----------- | ----------- | -------- |
| 3.3         | 3.7         | 4.3         | V        |

A suitable Li-ion battery should have the following parameters, as shown in the table below:

| **Parameter**     | **Value**            |
| ----------------- | -------------------- |
| Standard voltage  | 3.7 V           |
| Charging voltage  | 4.2 V           |
| Capacity          | As required          |
| Discharge current | At least 500 mA |

:::tip NOTE
When using a solar panel, you can't use a non-rechargeable battery.
:::

#### Mechanical Characteristic

##### Board Dimensions

The mechanical dimensions of the RAK19012 module are shown in **Figure 6** below.

> **Image:** RAK19012 mechanical dimensions

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

#### Environmental Characteristics

The table below lists the operating and storage temperature requirements of the RAK19012:

| **Parameter**                 | **Minimum** | **Typical** | **Maximum** |
| ----------------------------- | :---------: | :---------: | :---------: |
| Operational temperature range | –35 ºC | +25 ºC | +75 ºC |
| Extended temperature range    | –40 ºC | +25 ºC | +80 ºC |
| Storage temperature range     | –40 ºC | +25 ºC | +80 ºC |

#### Schematic Diagram

**Figure 8** shows the schematic of the RAK19012 USB LiPo Solar Power Slot Module.

> **Image:** RAK19012 USB LiPo Solar Power Slot Module schematics

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

