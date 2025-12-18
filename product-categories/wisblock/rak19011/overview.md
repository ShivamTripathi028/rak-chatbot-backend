---
slug: /product-categories/wisblock/rak19011/overview/
title: RAK19011 WisBlock Dual IO Base Board with Power Slot | RAKwireless Documentation Center
description: Get started with your IoT project with all the product information you need about the RAK19011 WisBlock Dual IO Base Board.
keywords: 
 - RAK19011 
 - wisblock 
 - IO Baseboard
image: https://images.docs.rakwireless.com/wisblock/rak19011/rak19011.png
sidebar_label: Product Overview
---

# RAK19011 WisBlock Dual IO Base Board with Power Slot

Thank you for choosing the **RAK19011 WisBlock Dual IO Base Board with Power Slot** for your awesome IoT project! 🎉 To help you get started, we have provided all necessary documentation for your product.

* [RAK19011 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak19011/quickstart/)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak19011/datasheet/)
* [WisBlock Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/quickstart/)
* [WisBlock Source Code Repository](https://github.com/RAKWireless/WisBlock/)
* [RAK19011 3D Model](https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK19011.stp)
* [24-Pin Female Connector 3D File (Sensor Slot)](https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/F24S1003K6M.stp)
* [40-Pin Female Connector 3D File (Core/IO/Power Slot)](https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/F40S1003K6M.stp)

## Product Description

**RAK19011** is a **WisBlock Dual IO Base Board with Power Slot** that connects **WisBlock Core**, **WisBlock Power**, and **WisBlock Modules**. It has one slot for the WisBlock Core module, one for the WisBlock Power module, two IO slots, and six sensor slots (A to F) for WisBlock Modules. There are also two **2.54 mm pitch headers** exposing all key input-output pins of the WisBlock Core, including UART, I2C, SPI, and many IO pins.

WisBlock Modules are connected to the RAK19011 WisBlock Dual IO Base Board with Power Slot via **high-speed board-to-board connectors**. They provide secure and reliable interconnection to ensure the signal integrity of each data bus. A set of screws is used for fixing the modules, which makes it reliable even in a vibrating environment. Additionally, it has a user-defined button.

### WisBlock IO Pin Mapping Tool

:::tip NOTE
For optimal results when building a WisBlock solution, utilize the [WisBlock IO Pin Mapping Tool](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool). This tool proactively identifies compatible pins for each module combination, thereby preventing pin conflicts.
:::

## Product Features

### Hardware

* Flexible building block design enabling modular functionality and expansion.
* High-speed interconnection connectors in the WisBlock Base board ensure signal integrity.
* **Multiple Headers and Modules Slots** for WisBlock Modules
    * One core slot
    * One power slot
    * Two I/O slots
    * Six sensor (A to F) slots
    * All key input/output pins of the WisBlock Core are exposed via headers.
    * Access to various communication buses via headers: I2C, SPI, UART, and USB.
    * One user-defined push-button switch
* **Size**
    * 60 mm x 67 mm

### Software 

#### Arduino IDE BSP Installation

**Programming via Arduino IDE**
- [RAKwireless BSP support for Arduino](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index)

In the Arduino IDE, once you install the BSP, examples for the WisBlock Core will be automatically included in the list of examples.

#### PlatformIO BSP Installation

**Programming via PlatformIO IDE:**
- [RAKwireless WisBlock modules in PlatformIO](https://github.com/RAKWireless/WisBlock/blob/master/PlatformIO/README)

## Prerequisites

The RAK19011 WisBlock Dual IO Base Board with Power Slot is easy to use and requires a **WisBlock Core**, **WisBlock Power Module**, and **WisBlock module** to start developing with the system.

:::warning

- RAK19011 requires a WisBlock power module for power and connector interfaces. It lacks USB and battery/power connectors; these functionalities must be added using an appropriate WisBlock power module.
- Securely fasten the modules with screws to ensure proper function.

:::

