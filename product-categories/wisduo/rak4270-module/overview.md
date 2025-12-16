---
title: RAK4270 WisDuo LPWAN Module
description: The RAK4270 module is designed to simplify LoRa peer-to-peer and LoRaWAN communication. the module is suitable for various applications that require long-range data acquisition and low power consumption, such as smart meters, agricultural sensors, and smart cities.
keywords:
- RAK4270
- wisduo
image: https://images.docs.rakwireless.com/wisduo/rak4270-module/RAK4270-Module.png
sidebar_label: Product Overview
---

    
import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK4270 WisDuo LPWAN Module

Thank you for choosing **RAK4270 WisDuo LPWAN Module** in your awesome IoT Project! 🎉 To help you get started, we have provided you all the necessary documentation for your product.

- [Quick Start Guide](https://docs.rakwireless.com/product-categories/wisduo/rak4270-module/quickstart/)
- [AT Command Manual](https://docs.rakwireless.com/product-categories/wisduo/rak4270-module/at-command-manual/)
- <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui" target="_blank">RUI Customized Development</a> - RAK4270 module supports RUI (RAKwireless Unified Interface) Customized Development.
- [Low Level Development](https://docs.rakwireless.com/product-categories/wisduo/rak4270-module/low-level-development/)
- [Datasheet](https://docs.rakwireless.com/product-categories/wisduo/rak4270-module/datasheet/)
- [RAK4270 Module 3D Model](https://downloads.rakwireless.com/3D_File/WisDuo/PWB-RAK4270.stp)
- [Reference Design](https://docs.rakwireless.com/product-categories/wisduo/rak4270-breakout-board/datasheet/#schematic-diagram)

## Product Description

The RAK4270 LoRa Module includes an **STM32L071 MCU** and an **SX1262** LoRa chip, which supports eight spreading factors (SF5 ~ SF12) and signals bandwidth that can be adjusted between 7.8&nbsp;kHz to 500&nbsp;kHz. It has Ultra-Low Power Consumption of 2.31&nbsp;μA (down to 1.61&nbsp;μA @ 2.0&nbsp;V) in sleep mode, but during the Transmit Mode, it can reach the maximum output power of 22&nbsp;dBm. As a receiver, it can achieve a sensitivity of -148&nbsp;dBm.

The module complies with Class A and C of LoRaWAN 1.0.2 specifications, and it also supports LoRa Point-to-Point (P2P) communications. The module is suitable for various applications that require long-range data acquisition and low power consumption, such as smart meters, supply chain and logistics tracking, agricultural sensors, and smart cities.

You can configure the mode and operation of the RAK4270 module using the [AT Commands](https://docs.rakwireless.com/product-categories/wisduo/rak4270-module/at-command-manual/) via a UART interface. Also, it offers low-power features that are very suitable for battery-powered applications.

## Features

- LoRa module is suitable for applications in Smart City, Smart Agriculture, Smart Industry
- Compact form factor: **15 x 15.5 x 2.5&nbsp;mm** (LxWxH)
- 20 pin stamp pad for PCB SMT board-to-board soldering
- I/O ports: **UART/I2C/GPIO/ADC**
- AT commands control interface
- Temperature range: **-30&nbsp;°C to +85&nbsp;°C**
- Supply voltage: **2.0 to 3.6&nbsp;V**
- **Supported bands**: (EU433, CN470, IN865, EU868, AU915, US915, KR920, and AS923-1/2/3/4)
- LoRa bandwidth range of 7.8&nbsp;kHz to 500&nbsp;kHz, SF5 to SF12, BR=0.018~62.5&nbsp;kb/s
- Ultra-Low Power Consumption of 2.31&nbsp;μA (down to 1.61&nbsp;μA @ 2.0V&nbsp;) in sleep mode
- ARM Cortex-M0+ 32-bit RISC core
- 128&nbsp;kbytes flash memory with ECC
- 20&nbsp;kbytes RAM
- 6&nbsp;kbytes of data EEPROM with ECC
- Compliance with TBC
