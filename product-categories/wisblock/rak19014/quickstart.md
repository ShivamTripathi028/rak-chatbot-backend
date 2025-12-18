---
slug: /product-categories/wisblock/rak19014/quickstart/
title: RAK19014 WisBlock Battery USB Power Slot Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK19014. Instructions are written in a detailed, step-by-step manner for easier setup. Aside from hardware configuration, it also includes software setup with detailed example codes to help you get started.
image: https://images.docs.rakwireless.com/wisblock/rak19014/rak19014.png
keywords:
  - quickstart
  - wisblock
  - RAK19014
sidebar_label: Quick Start Guide
---

# RAK19014 WisBlock Battery USB Power Slot Module Quick Start Guide

## Prerequisite

Before going through each step of using the RAK19014 WisBlock Battery USB Power Slot Module, make sure you have prepared the necessary items listed below:

- [RAK19014 WisBlock Battery USB Power Slot Module](https://store.rakwireless.com/products/usb-battery-power-slot-module-rak19014?utm_source=RAK19014&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base/)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- [External battery](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)

### Hardware Configuration

### Installation Guide

The RAK19014 WisBlock Battery USB Power Slot Module is a power board comprising a battery connector, a reset push button, and a power connector that connects to the WisBlock Base board.

For more information about the RAK19014, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak19014/datasheet/).

> **Image:** RAK19014 hardware setup

:::tip NOTE
The voltage of the battery must not exceed 4.3 V.
:::

##### Attach a WisConnector

The RAK19014 WisBlock Battery USB Power Slot Module can be mounted on the power slot of the WisBlock Base board, as shown in **Figure 2**. Also, always secure the connection of the WisBlock module using compatible screws.

> **Image:** RAK19014 mounting connection to WisBlock Base module

##### Detach a WisConnector

The procedure for disassembling any type of WisBlock module is the same.

1. First, remove the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed, check the module's silkscreen to find the correct location for applying force.

> **Image:** Detach silkscreen on the WisBlock module

3. Apply force to the module at the connector's position, as shown in **Figure 5**, to detach it from the baseboard.

> **Image:** Applying even forces on the proper location of a WisBlock module

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts.
:::

### Battery Selector

RAK19014 WisBlock Battery USB Power Slot Module can be powered by an external battery via the dedicated connectors, as shown in **Figure 6**. The matching connector for the battery cable is a [JST PHR-2 2 mm pitch female](https://www.jst-mfg.com/product/detail_e.php?series=199). A cable assembly for the battery connector is also available for purchase in [RAK store](https://store.rakwireless.com/products/battery-connector-cable).

> **Image:** External battery connector pin

:::warning

- Batteries can cause harm if not handled properly.
- Ensure the battery wires match the polarity on the RAK19014 board. Not all batteries have the same wiring.

:::

## Product Configuration

### Software Setup

The WisBlock Core is designed to interface with other WisBlock modules, such as sensors, displays, and other interfaces. To make useful devices, you need to upload source code to the WisBlock Core.
Based on your choice of WisBlock Core, select a development environment:

#### Arduino IDE BSP Installation

**Programming via Arduino IDE**
- [RAKwireless BSP support for Arduino](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index)

In the Arduino IDE, once you install the BSP, examples for the WisBlock Core will be automatically included in the list of examples.

#### PlatformIO BSP Installation

**Programming via PlatformIO IDE:**
- [RAKwireless WisBlock modules in PlatformIO](https://github.com/RAKWireless/WisBlock/blob/master/PlatformIO/README)

## Examples 

To quickly build your IoT device with less hassle, example codes for the WisBlock Core are provided. You can access the codes on the [WisBlock Example code repository](https://github.com/RAKWireless/WisBlock/tree/master/examples). The example codes on folder `common` are compatible with RAK4631, RAK11200, and RAK11310 WisBlock cores.
The two user LEDs of RAK19014 can be accessed using macro definitions `LED_GREEN` / `PIN_LED1` for the green LED and `LED_BLUE` / `PIN_LED2` for the blue LED.

## Tutorials and Resources

[Create Modular Power Supply with WisBlock Power Boards](https://www.youtube.com/watch?v=fv0y22VDVB0)

