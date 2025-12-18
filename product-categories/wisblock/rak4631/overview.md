---
slug: /product-categories/wisblock/rak4631/overview/
title: RAK4631 WisBlock LoRaWAN Module | Low-Power LoRa & BLE for IoT
description: Discover the RAK4631 LoRaWAN & BLE module with Nordic nRF52840 & SX1262. Ideal for IoT projects, developers, and engineers. Read more and get started today!
image: https://images.docs.rakwireless.com/wisblock/rak4631/rak4631.png
keywords:
  - rak4631
  - rak4631 module
  - sx1262 lora transceiver
  - nrf52840 mcu
  - lorawan module for iot
  - nrf52840 lorawan development board
  - lorawan ble module
  - low power mcu
  - lora p2p communication
  - lora wireless module
  - low power consumption modules
  - long range communication
  - dual rf iot lorawan module
sidebar_label: Product Overview
download: true
date: 2020-09-18
---

# RAK4631 WisBlock LoRaWAN Module

Thank you for choosing **RAK4631 WisBlock LoRaWAN Module** in your awesome IoT Project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

* [RAK4631 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak4631/quickstart/)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak4631/sidewalk/)
* [WisBlock Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/quickstart/)
* [WisBlock Source Code Repository](https://github.com/RAKWireless/WisBlock/)
* [Arduino IDE BSP](https://learn.rakwireless.com/hc/en-us/articles/26687371039383-How-To-Perform-Installation-of-Board-Support-Package-in-Arduino-IDE)
* [PlatformIO BSP](https://learn.rakwireless.com/hc/en-us/articles/26687276346775-How-To-Perform-Installation-of-Board-Support-Package-in-PlatformIO)
* [Bootloader source code and ready to flash file](https://github.com/RAKWireless/WisBlock/tree/master/bootloader)
* [RAK4631 3D Model](https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK4631.stp)
* [40-Pin Male Connector 3D File](https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/M40S1003K6M.stp)

**Examples:**
* [RAK4631 example codes on folders **`RAK4630`** and **`common`**](https://github.com/RAKWireless/WisBlock/tree/master/examples)
* [Sample Code: LoRa](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK4630/communications/LoRa)
* [Sample Code: BLE](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK4630/communications/BLE)
* [Sample Code: Battery Level](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK4630/power/RAK4630_Battery_Level_Detect)

## Product Description

**RAK4631** is a **WisBlock Core** module for RAK **WisBlock**. It extends the **WisBlock** series with a powerful Nordic nRF52840 MCU that supports Bluetooth 5.0 (Bluetooth Low Energy) and the newest LoRa transceiver from Semtech, the SX1262. The Semtech SX1262 has compared to the older SX127x series a lower power consumption at the same TX power. This makes the **RAK4631** an ultra-low power communication solution.
**RAK4631** can be comfortably programmed with the Arduino™ IDE or the PlatformIO extension for other IDE's like Atom, MS Visual Code, or Clion.

Both LoRaWAN and LoRa point-to-point connections are supported by an Arduino™ library.

:::tip NOTE
The RAK4631 and RAK4631-R share common hardware and are 100% identical, but their firmware is different. **RAK4631** firmware is based on the Arduino BSP of the nRF52840 chip, whereas **RAK4631-R** firmware is based on RUI V3, giving you the flexibility to develop optimized firmware using the [RUI3 APIs](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/arduino-api/) or via [RUI3 AT commands](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/at-command-manual/).

You can [convert your RAK4631 to RAK4631-R](https://docs.rakwireless.com/product-categories/wisblock/rak4631-r/dfu/#updating-rak4631-to-rui3) if you prefer [RUI3](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/).
:::

## Product Features

* Nordic nRF52840 ultra-low power MCU
* 32-bit ARM® Cortex™-M4 CPU
* 64 MHz CPU clock
* 1 MB Flash, 256 KB RAM
* Semtech SX1262 low power high range LoRa transceiver
* LoRaWAN 1.0.2 protocol stack
* Bluetooth 5.0 protocol stack

* I2C, SPI, Analog inputs, Digital inputs, and outputs
* Low power consumption
* Chipset: Nordic nRF52840, Semtech SX1262

## Prerequisites

To use a **RAK4631**, you need at least a **WisBlock Base** to plug the module in. **WisBlock Base** is the power supply for the **RAK4631** module and has the programming/debug interface.

:::warning
- Make sure to fix the module with the screws to ensure a proper function.
- When using the LoRa or Bluetooth Low Energy transceivers, make sure that always an antenna is connected. Using these transceivers without an antenna can damage the system.
:::

