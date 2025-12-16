---
slug: /product-categories/wisblock/rak12005/overview/
title: RAK12005 WisBlock Rain Sensor Module
description: RAK12005 is a WisBlock Sensor that contains a sensing pad used for detecting water like rain and other electroconductive liquids.
image: "https://images.docs.rakwireless.com/wisblock/rak12005/rak12005.png"
keywords:
  - Microchip
  - MCP606
  - RAK12005
  - wisblock
sidebar_label: Product Overview
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'


# RAK12005 WisBlock Rain Sensor Module

Thank you for choosing **RAK12005 WisBlock Rain Sensor Module** in your awesome IoT Project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

* [RAK12005 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak12005/quickstart/)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak12005/datasheet/)
* <a href="https://docs.rakwireless.com/product-categories/wisblock/quickstart/" target="_blank">WisBlock Quick Start Guide</a>
* [WisBlock Source Code Repository](https://github.com/RAKWireless/WisBlock/)
* [RAK12005 3D Model](https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK12005.step)
* [40-Pin Male Connector 3D file](https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/M40S1003K6M.stp)
* [WisBlock IO Tutorial](https://learn.rakwireless.com/hc/en-us/articles/26743881131927-How-To-Make-Your-Own-WisBlock-IO-Board)

**Examples**

* [Sample Code: RAK12005](https://github.com/RAKWireless/WisBlock/blob/master/examples/common/IO/RAK12005_WaterDetector/RAK12005_WaterDetector.ino)

## Product Description

The RAK12005, a part of WisBlock Sensor, is an electroconductive-liquid detect module used for detecting water and other electroconductive liquids. If the detection area is wet, the output of Microchip's MCP606 CMOS op-amp will go positive, signaling the presence of liquid.

RAK12005 WisBlock Rain Sensor Module also has a separate sensor PCB, the RAK12030. This sensor PCB is connected to the RAK12005 with a cable so that you can place the sensor under the open sky and keep your WisBlock solution in a dry place or inside a waterproof enclosure.

## Product Features

* **Sensor specifications**
    * 3.3&nbsp;V Power supply (disconnect option to save power)
    * Chipset: Microchip MCP606
    * Digital output
    * Configurable detection threshold via trimmer
    * Separate sensor PCB RAK12030, size 25 x 35&nbsp;mm

* **Size**
    * 15 x 25&nbsp;mm

## Prerequisites

To use a **RAK12005**, you need at least a **RAK12030 Rain Sensing Pad** and a **WisBlock Base** to plug the module in. **WisBlock Base** provides power supply to the **RAK12005** module. Furthermore, you need a **WisBlock Core** module to use the sensor.

:::warning
Make sure to fix the module with the screws to ensure a proper function.
:::

<RkBottomNav/>