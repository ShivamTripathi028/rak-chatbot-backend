---
slug: /product-categories/wisblock/rak15006/overview/
title: RAK15006 WisBlock 512kByte FRAM Module
description: RAK15006 is a WisBlock 512kByte FRAM module that extends the WisBlock system with an MB85RS4MT memory module from Fujitsu.
image: "https://images.docs.rakwireless.com/wisblock/rak15006/rak15006.png"
keywords:
  - wisblock
  - RAK15006
  - Fujitsu
  - MB85RS4MT
sidebar_label: Product Overview
---

import RkBottomNav from '@site/src/components/Document/BottomNav'


# RAK15006 WisBlock 512kByte FRAM Module

Thank you for choosing **RAK15006 WisBlock 512kByte FRAM Module** in your awesome IoT Project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

* [RAK15006 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak15006/quickstart/)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak15006/datasheet/)
* <a href="https://docs.rakwireless.com/product-categories/wisblock/quickstart/" target="_blank">WisBlock Quick Start Guide</a>
* [WisBlock Source Code Repository](https://github.com/RAKWireless/WisBlock/)
* [RAK15006 3D Model](https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK15006.stp)
* [24-Pin Male Connector 3D File](https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/M24S1003K6M.stp)
* [WisBlock Sensor Tutorial](https://learn.rakwireless.com/hc/en-us/articles/26687819464343-How-To-Make-Your-Own-WisBlock-Sensor-Board)

**Examples**

- For All WisBlock Core Modules:
    - [RAK15006 Sample Code](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK15006-FRAM-4MBit-MB85RS4MT)

## Product Description

RAK15006 is a WisBlock 512kByte FRAM module that extends the WisBlock system with an MB85RS4MT memory module from Fujitsu. This module is interfaced via I2C. Additionally, it can be mounted to the sensor slot of the WisBlock Base board.

## Product Features

* **Sensor specifications**
    *  Temperature Range：-40&nbsp;°C to +85&nbsp;°C
    *  SPI compatible digital interface, supports 40&nbsp;MHz
    *  Operating power supply current: 2.6&nbsp;mA (Max @ 40&nbsp;MHz)
    *  Standby current: 50&nbsp;uA (Max)
    *  Sleep current: 8&nbsp;uA (Max)
    *  524,288 words x 8 bits
    *  High Reliability：
       - Read/write endurance：10,000,000,000,000/byte
       - Data retention：
           - 10 years(+85&nbsp;°C)
           - 95 years(+55&nbsp;°C)
           - Over 200 years（+35&nbsp;°C）

* **Size**
    * 10 x 10&nbsp;mm

## Prerequisites

To use a **RAK15006**, you need at least a **WisBlock Base** to plug the module in. **WisBlock Base** provides power supply to the **RAK15006** module. Furthermore, you need a **WisBlock Core** module to use the sensor.

:::warning
Make sure to fix the module with the screws to ensure a proper function.
:::

<RkBottomNav/>