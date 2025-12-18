---
slug: /product-categories/wisblock/rak3372/overview/
title: RAK3372 WisBlock LPWAN Module
description: RAK3372 is a WisBlock Core module for RAKwireless WisBlock. It extends the WisBlock series with a very efficient core based on STM32WL LoRa SoC which supports LoRa P2P and LoRaWAN functionality.
image: https://images.docs.rakwireless.com/wisblock/rak3372/rak3372.png
keywords:
    - RAK3372
    - wisblock
    - STM32WL
    - STM32WLE5CCU6
    - STMicroelectronics

sidebar_label: Product Overview
---

import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK3372 WisBlock LPWAN Module

Thank you for choosing **RAK3372 WisBlock LPWAN Module** in your awesome IoT project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak3372/quickstart/" target="_blank">RAK3372 Quick Start Guide</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak3372/at-command-manual/" target="_blank">AT Command Manual</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak3372/datasheet/" target="_blank">Datasheet</a>
- <a href="https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK3372.step" target="_blank">RAK3372 3D Model</a>
- <a href="https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/M40S1003K6M.stp" target="_blank">40-Pin Male Connector 3D File</a>

## Product Description

The RAK3372 WisBlock Core module is a <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/datasheet/" target="_blank">RAK3172 LoRa module</a> with an expansion PCB and connectors compatible with the WisBlock Base. It allows an easy way to access the pins of the RAK3172 module, simplifying development and testing processes.

The module itself comprises a RAK3172 as its main component. The RAK3372 is based on the STM32WLE5CCU6 LoRa SoC transceiver chip. It features ultra-low power consumption of less than 2.0&nbsp;uA during sleep mode with configurable high LoRa output RF power up to 22&nbsp;dBm during transmission mode.

Additionally, RAK3372 complies with LoRaWAN 1.0.3 protocols and supports LoRa point-to-point communication.


## Product Features

- Based on <a href="https://www.st.com/resource/en/datasheet/stm32wle5cc.pdf" target="_blank">STM32WLE5CCU6</a>
- **I/O ports**: UART/I2C/GPIO
- **Temperature range**: -70°&nbsp;C to +85°&nbsp;C
- **Supply voltage**: 2.0 ~ 3.6&nbsp;V
- Low-Power Wireless Systems with 7.8&nbsp;kHz to 500&nbsp;kHz Bandwidth
- Ultra-Low Power Consumption of less than 2.0&nbsp;uA in sleep mode
- LoRa PA Boost mode with 22&nbsp;dBm output power
- Serial Wire Debug (SWD) interface
- **Module size**: 20&nbsp;mm x 30&nbsp;mm

:::warning
- RAK3372 WB_IO3 (WisBlock IO Pin 3) is connected to PB12 of the RAK3172 module. This pin is internally connected to a 10&nbsp;kΩ resistor as mentioned on the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/datasheet/#pin-definition" target="_blank">pin definition table of the RAK3172 datasheet</a>. Other WisBlock modules that use this pin will have possible conflict.
:::

## Prerequisites

To use a **RAK3372**, you need at least a **WisBlock Base** to plug the module in. **WisBlock Base** is the power supply for the **RAK3372** module and has the programming/debug interface.

:::warning
- When using the LoRa transceiver, make sure that it is connected to an antenna. Using the transceiver chip without an antenna can damage the system.
- Make sure to fix the module with screws to ensure proper function.
:::

:::tip Note
For CE and FCC certifications we provide an AT command guide.    
You can find it in our <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/certification-guide" target="_blank">RUI3 documentation</a> or get it from our <a href="https://downloads.rakwireless.com/#RUI/RUI3/Certification%20Guide/" target="_blank">Download Center</a>.    
::: 

<RkBottomNav/>