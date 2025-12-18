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

import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK19011 WisBlock Dual IO Base Board with Power Slot

Thank you for choosing the **RAK19011 WisBlock Dual IO Base Board with Power Slot** for your awesome IoT project! 🎉 To help you get started, we have provided all necessary documentation for your product.

* <a href="https://docs.rakwireless.com/product-categories/wisblock/rak19011/quickstart/" target="_blank">RAK19011 Quick Start Guide</a>
* <a href="https://docs.rakwireless.com/product-categories/wisblock/rak19011/datasheet/" target="_blank">Datasheet</a>
* <a href="https://docs.rakwireless.com/product-categories/wisblock/quickstart/" target="_blank">WisBlock Quick Start Guide</a>
* <a href="https://github.com/RAKWireless/WisBlock/" target="_blank">WisBlock Source Code Repository</a>
* <a href="https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK19011.stp" target="_blank">RAK19011 3D Model</a>
* <a href="https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/F24S1003K6M.stp" target="_blank">24-Pin Female Connector 3D File (Sensor Slot)</a>
* <a href="https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/F40S1003K6M.stp" target="_blank">40-Pin Female Connector 3D File (Core/IO/Power Slot)</a>

## Product Description

**RAK19011** is a **WisBlock Dual IO Base Board with Power Slot** that connects **WisBlock Core**, **WisBlock Power**, and **WisBlock Modules**. It has one slot for the WisBlock Core module, one for the WisBlock Power module, two IO slots, and six sensor slots (A to F) for WisBlock Modules. There are also two **2.54&nbsp;mm pitch headers** exposing all key input-output pins of the WisBlock Core, including UART, I2C, SPI, and many IO pins.

WisBlock Modules are connected to the RAK19011 WisBlock Dual IO Base Board with Power Slot via **high-speed board-to-board connectors**. They provide secure and reliable interconnection to ensure the signal integrity of each data bus. A set of screws is used for fixing the modules, which makes it reliable even in a vibrating environment. Additionally, it has a user-defined button.

### WisBlock IO Pin Mapping Tool

:::tip NOTE
For optimal results when building a WisBlock solution, utilize the <a href="https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool" target="_blank">WisBlock IO Pin Mapping Tool</a>. This tool proactively identifies compatible pins for each module combination, thereby preventing pin conflicts.
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
    * 60&nbsp;mm x 67&nbsp;mm

### Software 

#### Arduino IDE BSP Installation

<b>Programming via Arduino IDE</b>
- <a href="https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index" target="_blank">RAKwireless BSP support for Arduino</a>
<br/>In the Arduino IDE, once you install the BSP, examples for the WisBlock Core will be automatically included in the list of examples.

#### PlatformIO BSP Installation

<b>Programming via PlatformIO IDE:</b>
- <a href="https://github.com/RAKWireless/WisBlock/blob/master/PlatformIO/README" target="_blank">RAKwireless WisBlock modules in PlatformIO</a>

## Prerequisites

The RAK19011 WisBlock Dual IO Base Board with Power Slot is easy to use and requires a **WisBlock Core**, **WisBlock Power Module**, and **WisBlock module** to start developing with the system.

:::warning

- RAK19011 requires a WisBlock power module for power and connector interfaces. It lacks USB and battery/power connectors; these functionalities must be added using an appropriate WisBlock power module.
- Securely fasten the modules with screws to ensure proper function.

:::

<RkBottomNav/>