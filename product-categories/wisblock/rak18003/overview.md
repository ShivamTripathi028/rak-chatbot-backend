---
slug: /product-categories/wisblock/rak18003/overview/
title: RAK18003 WisBlock Audio Interposer Module
description: RAK18003 WisBlock Audio module is an interposer module that allows you to use multiple WisBlock Audio boards in a single IO slot.
image: "https://images.docs.rakwireless.com/wisblock/rak18003/rak18003.png"
keywords:
  - RAK18003
  - wisblock
sidebar_label: Product Overview
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK18003 WisBlock Audio Interposer Module

Thank you for choosing **RAK18003 WisBlock Audio Interposer Module** in your awesome IoT project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

* [RAK18003 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak18003/quickstart/)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak18003/datasheet/)
* <a href="https://docs.rakwireless.com/product-categories/wisblock/quickstart/" target="_blank">WisBlock Quick Start Guide</a>
* [WisBlock Source Code Repository](https://github.com/RAKWireless/WisBlock/)
* [RAK18003 3D Model](https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK18003.stp)
* [40-Pin Male Connector 3D File](https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/M40S1003K6M.stp)
* [WisBlock IO Tutorial](https://learn.rakwireless.com/hc/en-us/articles/26743881131927-How-To-Make-Your-Own-WisBlock-IO-Board)

## Product Description

The RAK18003 is an interposer module, part of the WisBlock Audio Series. The RAK18003 is designed to allow multiple WisBlock Audio modules to be used together on a single IO slot. It consists of two IO expanders (TPT29555-TS5R), one signal switch (5223YWQ10/TR), and connectors where other WisBlock Audio modules can be interfaced. It also has a usable TF card slot.

:::tip NOTE
WisBlock Audio stack must have an interposer. The interposer board should be connected directly to WisBase. The PDM MIC connector connects to the interposer by the FPC connector and other modules connect to the interposer by the BTB connector.
:::

## Product Features

* **Module Specifications**
  - Interposer board
  - Extend IO for WisBlock Core to control other modules
  - FPC connector for connecting PDM MIC modules
  - TF-card connector
  - BTB connector for WisBlock Audio stack

* **Module Size**
  - 25 x 35&nbsp;mm

## Prerequisites

To use a **RAK18003**, you need at least a **WisBlock Base** to plug the module in. The **WisBlock Base** provides power supply to the **RAK18003** module. Furthermore, you need the **WisBlock Core** and the **WisBlock Audio** modules to use the **RAK18003** module.

:::warning
Make sure to fix the module with screws to ensure proper function.
:::

<RkBottomNav/>