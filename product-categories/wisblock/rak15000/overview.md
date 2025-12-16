---
slug: /product-categories/wisblock/rak15000/overview/
title: RAK15000 WisBlock EEPROM Module
description: Provides comprehensive information about your RAK15000 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak15000/rak15000.png"
keywords:
  - wisblock
  - RAK15000
  - Microchip
  - AT24CM02
sidebar_label: Product Overview
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'


# RAK15000 WisBlock EEPROM Module

Thank you for choosing **RAK15000 WisBlock EEPROM Module** in your awesome IoT Project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

* [RAK15000 Quick Start Guide](quickstart.md)
* [Datasheet](datasheet.md)
* <a href="https://docs.rakwireless.com/product-categories/wisblock/quickstart/" target="_blank">WisBlock Quick Start Guide</a>
* [WisBlock Source Code Repository](https://github.com/RAKWireless/WisBlock/)
* [RAK15000 3D Model](https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK15000.stp)
* [24-Pin Male Connector 3D File](https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/M24S1003K6M.stp)
* [WisBlock Sensor Tutorial](https://learn.rakwireless.com/hc/en-us/articles/26687819464343-How-To-Make-Your-Own-WisBlock-Sensor-Board)

**Example**

For All WisBlock Core Modules:

* [Sample Code: RAK15000 WisBlock EEPROM Module](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK15000_EEPROM_AT24C02)

## Product Description

The RAK15000 WisBlock EEPROM module, part of the RAKwireless Wisblock series, is a serial EEPROM module with an I2C interface. Designed to work at low-power mode, the standby average consumption is lower than 3&nbsp;µA (VCC = 5.5&nbsp;V). The RAK15000 uses Microchip AT24CM02, which provides 2,097,152 bits of Serial Electrically Erasable and Programmable Read-Only Memory (EEPROM), organized as 262,144 words of 8 bits each.

## Product Features

* 3.3&nbsp;V input voltage, on/off control by the WisBlock Core module
* **Temperature range:** -40&nbsp;°C to +85&nbsp;°C
* Internally organized as 262,144 x 8&nbsp;bit (2&nbsp;Mbit)
* I2C-Compatible (2-wire) Serial Interface
    - 100&nbsp;kHz Standard mode
    - 400&nbsp;kHz Fast Mode
* High Reliability
    - Endurance: 1,000,000 write cycles
    - Data retention: 100 years
* Built in error detection and correction
* 256-byte Page Write Mode
* Random and Sequential Read Modes
* Standby current less than 3&nbsp;µA
* Chipset: Microchip AT24CM02
* **Module size**: 10 x 10&nbsp;mm

## Prerequisites

To use a **RAK15000**, you need at least a **WisBlock Base** to plug the module in. **WisBlock Base** is the power supply for the **RAK15000** module. Furthermore, you need a **WisBlock Core** module to access the EEPROM memory.

:::warning
Make sure to fix the module with the screws to ensure a proper function.
:::

<RkBottomNav/>