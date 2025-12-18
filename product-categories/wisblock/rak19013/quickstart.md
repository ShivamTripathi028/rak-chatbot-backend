---
slug: /product-categories/wisblock/rak19013/quickstart/
title: RAK19013 WisBlock LiPo Solar Power Slot Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK19013. Instructions are written in a detailed, step-by-step manner for easier setup. Aside from hardware configuration, it also includes software setup with detailed example codes to help you get started.
image: https://images.docs.rakwireless.com/wisblock/rak19013/rak19013.png
keywords:
  - quickstart
  - wisblock
  - RAK19013
sidebar_label: Quick Start Guide
---

# RAK19013 WisBlock LiPo Solar Power Slot Module Quick Start Guide

## Prerequisite

Before going through each step of using the RAK19013 WisBlock LiPo Solar Power Slot module, make sure you have prepared the necessary items listed below:

- [RAK19013 WisBlock LiPo Solar Power Slot Module](https://store.rakwireless.com/products/rak19013-lipo-solar-power-slot-module?utm_source=RAK19013&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base/)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [RAK5804 WisBlock Interface Module](https://store.rakwireless.com/products/rak5804-io-extension-board?utm_source=RAK5804&utm_medium=Document&utm_campaign=BuyFromStore)(Reprogramming of the WisBlock Core via USB)

## Hardware Configuration

### Installation Guide

The RAK19013 WisBlock LiPo Solar Power Slot Module is a power board comprising a battery connector, a solar panel connector, a reset push button, and a power connector that connects to the WisBlock Base board.

For more information about RAK19013, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak19013/datasheet/).

#### Attach a WisConnector

The RAK19013 module can be mounted on the I/O slot of the WisBlock Base board, as shown in **Figure 1**. Also, always secure the connection of the WisBlock module by using compatible screws.

> **Image:** RAK19013 mounting connection to WisBlock Base module

#### Detach a WisConnector

The procedure for disassembling any type of WisBlock module is the same.

1. First, remove the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed, check the module's silkscreen to find the correct location for applying force.

> **Image:** Detach silkscreen on the WisBlock module

3. Apply force to the module at the connector's position, as shown in **Figure 6**, to detach it from the baseboard.

> **Image:** Applying even forces on the proper location of a WisBlock module

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts.
:::

### Battery Selector

#### Rechargeable Battery

> **Image:** RAK19013 pinout and connector assignments

:::tip NOTE
The voltage of the battery must not exceed 4.3 V.
:::

RAK19013 can be powered by a rechargeable Li-Ion/LiPo battery via the dedicated connectors, as shown in **Figure 7**. The matching connector for the rechargeable battery wires is a [JST PHR-2 2 mm pitch female](https://www.jst-mfg.com/product/detail_e.php?series=199). A cable assembly for the rechargeable battery connector is also available for purchase in [RAK store](https://store.rakwireless.com/products/battery-connector-cable).

> **Image:** Rechargeable battery connector pin

:::warning

- Batteries can cause harm if not handled properly.
- Only 3.7 V-4.2 V rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- Make sure the battery wires, both rechargeable and non-rechargeable, match the polarity on the RAK19013 board. Not all batteries have the same wiring.

:::

### Solar Panel Connection

The battery can be recharged, as well, via a small Solar Panel, as shown in **Figure 8**. The matching connector for the solar panel wires is an [JST ZHR-2 1.5 mm pitch female](https://www.jst-mfg.com/product/detail_e.php?series=287). A cable assembly for the solar panel connector is also available for purchase in [RAK store](https://store.rakwireless.com/products/solar-panel-connector-cable).

> **Image:** Solar panel connector VIN and GND

:::warning

- Only 5 V solar panels are supported. Do not use 12 V solar panels; this will destroy the charging unit and eventually other electronic parts.
- The GND pin of the solar panel connector is located on the edge of the board. Ensure the solar panel wires match the polarity on the RAK19013 board.

:::

## Product Configuration

### Software Setup

Since there is no USB port on the RAK19013, the only way to upload code is by using a RAK5804.

> **Image:** RAK19013 and RAK5804 Connector assignments

Based on your choice of WisBlock Core, select a development environment:

#### Arduino IDE BSP Installation

**Programming via Arduino IDE**
- [RAKwireless BSP support for Arduino](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index)

In the Arduino IDE, once you install the BSP, examples for the WisBlock Core will be automatically included in the list of examples.

#### PlatformIO BSP Installation

**Programming via PlatformIO IDE:**
- [RAKwireless WisBlock modules in PlatformIO](https://github.com/RAKWireless/WisBlock/blob/master/PlatformIO/README)

### Examples 

To quickly build your IoT device with less hassle, example codes for WisBlock Core are provided. You can access the codes on the [WisBlock Example code repository](https://github.com/RAKWireless/WisBlock/tree/master/examples). The example codes on folder `common` are compatible with RAK4631, RAK11200, and RAK11310 WisBlock Cores.
The two user LEDs of RAK19013 can be accessed using macrodefinitions `LED_GREEN` / `PIN_LED1` for the green LED and `LED_BLUE` / `PIN_LED2` for the blue LED. For the battery voltage reading, `WB_A0` is used.

## Tutorials and Resources

[Create Modular Power Supply with WisBlock Power Boards](https://www.youtube.com/watch?v=fv0y22VDVB0)

