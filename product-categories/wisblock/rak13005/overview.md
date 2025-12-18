---
slug: /product-categories/wisblock/rak13005/overview/
title: RAK13005 WisBlock LIN Module
description: RAK13005 is a WisBlock Interface module that extends the WisBlock system with a LIN module. It is designed for in-vehicle networks using data transmission rates up to 20 kBaud.
image: "https://images.docs.rakwireless.com/wisblock/rak13005/rak13005.png"
keywords:
  - RAK13005
  - wisblock
  - Infineon
  - TLE7259-3
sidebar_label: Product Overview
---

import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK13005 WisBlock LIN Module

Thank you for choosing **RAK13005 WisBlock LIN Module** in your awesome IoT Project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

* [RAK13005 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak13005/quickstart/)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak13005/datasheet/)
* <a href="https://docs.rakwireless.com/product-categories/wisblock/quickstart/" target="_blank">WisBlock Quick Start Guide</a>
* [WisBlock Source Code Repository](https://github.com/RAKWireless/WisBlock/)
* [RAK13005 3D Model](https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK13005.stp)
* [40-Pin Male Connector 3D File](https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/M40S1003K6M.stp)
* [WisBlock Interface Tutorial](https://learn.rakwireless.com/hc/en-us/articles/26743881131927-How-To-Make-Your-Own-WisBlock-IO-Board)


**Examples**:

* [Sample Code: RAK13005 LIN Data Transfer](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/IO/RAK13005_LIN_BUS/LINBusCommunication)
* [Sample Code: RAK13005 LIN LED Control](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/IO/RAK13005_LIN_BUS/LINBusControlLED)

## Product Description

The RAK13005 is a **Local Interconnect Network** (LIN) transceiver module, used in automatic technologies that can be mounted on the IO slot of the WisBlock Base board. It is designed for in-vehicle networks using data transmission rates from 2.4&nbsp;kBaud to 20&nbsp;kBaud, and it uses the TLE7259-3 chip from Infineon.

This module offers safe communication over up to 40&nbsp;m distance between the LIN bus nodes. Besides the use in an automotive environment, it can be implemented in home appliances and industrial automation. The LIN bus technology consists of Peripheral (Slave) and Controller (Master) Nodes which are both supported by RAK13005.

## Product Features

* **Module specifications**

    *   Single-wire LIN transceiver for transmission rates up to 20&nbsp;kBaud
    *   Supports both Controller(Master) and Peripheral(Slave) modes
    *   Compliant to ISO 17987-4 and LIN Specification 2.2A
    *   Very low current consumption in sleep mode with wake-up functions
    *   Support 12&nbsp;V and 24&nbsp;V LIN bus power supply
    *   Digital I/O levels compatible with 3.3&nbsp;V and 5&nbsp;V microcontrollers
    *   Chipset: Infineon TLE7259-3

* **Size**
    * 25 x 35&nbsp;mm

## Prerequisites

To use a **RAK13005**, you need at least a **WisBlock Base** to plug the module in. Furthermore, you need a **WisBlock Core** module to control the module.

:::warning
Make sure to fix the module with the screws to ensure a proper function.
:::

<RkBottomNav/>