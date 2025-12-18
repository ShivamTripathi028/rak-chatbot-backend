---
slug: /product-categories/wisblock/rak19003/overview/
title: RAK19003 WisBlock Mini Base Board | Compact LoRaWAN & IoT Expansion Board
description: RAK19003 WisBlock Mini Base Board—compact, low-power LoRaWAN & IoT base board for custom sensor integration. Ideal for modular IoT projects & small enclosures.
image: https://images.docs.rakwireless.com/wisblock/rak19003/rak19003-n.png
keywords:
  - rak19003
  - wisblock base board
  - lorawan board
  - mini base board for lorawan
  - modular iot base board
  - iot custom sensor module
  - compact lorawan base board
  - boards for iot
  - low power iot board
date: 2021-10-10
sidebar_label: Product Overview
---

# RAK19003 WisBlock Mini Base Board

Thank you for choosing **RAK19003 WisBlock Mini Base Board** in your awesome IoT Project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

* [RAK19003 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak19003/quickstart/)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak19003/datasheet/)
* [WisBlock Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/quickstart/)
* [WisBlock Source Code Repository](https://github.com/RAKWireless/WisBlock/)
* RAK19003 3D Model
    * [RAK19003 VA & VB 3D Model](https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK19003-VA-VB.stp)
    * [RAK19003 VC, VD, & VD 3D Model](https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK19003-VC-VD-VE.step)
* [24-Pin Female Connector 3D File (Sensor Slot)](https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/F24S1003K6M.stp)
* [40-Pin Female Connector 3D File (Core Slot)](https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/F40S1003K6M.stp)

## Product Description

**RAK19003** is a **WisBlock Base** board that connects **WisBlock Core** and **WisBlock Modules**. It provides the power supply and interconnection to the modules attached to it. It has one slot reserved for the WisBlock Core module and two Slot C-D for WisBlock Modules. The WisBlock Core is attached on the top side, and the WisBlock Modules are attached to the bottom side of the RAK19003 WisBlock Base board. Slot D holds modules up to 23 mm in size, while Slot C supports 10 mm WisBlock Modules. Also, there are two **2.54 mm pitch headers** for extension interface with **BOOT**, **I2C**, and **UART** pins.

For convenience, there is a Type-C USB connector that is connected directly to WisBlock Core MCU’s USB port (if supported) or to a USB-UART converter depending on the WisBlock Core. It can be used for uploading firmware or serial communication. The USB-C connector is also used as a battery charging port.

WisBlock Modules are connected to the RAK19003 WisBlock Base board via **high-speed board to board connectors**. They provide secure and reliable interconnection to ensure the signal integrity of each data bus. A set of screws are used for fixing the modules, which makes it reliable even in an environment with lots of vibrations.

Using **RAK19003** as your WisBlock Base board, you can make your project compact, which is ideal in small enclosures. You can also use a [RAK19005 WisBlock Sensor Extension Cable](https://store.rakwireless.com/products/fpc-extension-cable-for-slot-a-to-d-rak19005) to position WisBlock Modules apart from the WisBlock Base board or in any part of your case. **RAK19003** has connectors for the following:

* 1 WisBlock Core module
* 2 WisBlock Modules compatible with Slot C-D
* 1 Type-C USB port for programming and debugging
* 3.7 V Rechargeable battery connector
* 5 V Solar Panel connector
* 2 Headers with BOOT, I2C, and UART pins accessible with solder contacts

Additionally, it has two user-definable LEDs - one power supply/charging indicator LED and a reset button.

## Product Features

* **Power supply**
  * Supports both 5 V USB and 3.7 V rechargeable battery as power supply.
  * Has a connector for a 5 V solar panel to recharge the battery in a remote solution.
  * Control of power consumption
  * Has an electronic load switch to power the **WisBlock modules**. The power supply for the **WisBlock modules** boards can be controlled by the **WisBlock Core** modules application.

* **Size**
  * A compact size of 30 x 35 mm, which lets you create solutions that fit into smallest housings.

## Prerequisites

WisBlock Mini Base is amazingly easy to use and requires only a Type-C USB cable to start developing with the system.

:::warning

- Only 3.7-4.2 V Rechargeable Li-Ion batteries are supported. Do not use other types of batteries with the system.
- Only 5 V solar panels are supported. Do not use 12 V solar panels. It will destroy the charging unit and eventually other electronic parts.
  :::

