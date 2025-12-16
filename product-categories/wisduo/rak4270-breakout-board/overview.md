---
title: RAK4270 WisDuo Breakout Board
description: The RAK4270 Breakout Board is designed to facilitate the external connection of RAK4270 pins making it easier to debug the said module.
image: "https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/rak4270-breakout.png"
keywords:
  - RAK4270 Breakout Board
  - wisduo
sidebar_label: Product Overview
slug: /product-categories/wisduo/rak4270-breakout-board/overview/
download: true
---

import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK4270 WisDuo Breakout Board
Thank you for choosing **RAK4270 Breakout Board** in your awesome IoT Project! 🎉 To help you get started, we have provided you all the necessary documentation for your product.

* <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4270-breakout-board/quickstart/" target="_blank">Quick Start Guide</a>
* <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4270-breakout-board/at-command-manual/" target="_blank">AT Command Manual</a>
* <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4270-breakout-board/datasheet/" target="_blank">Datasheet</a>
* <a href="https://downloads.rakwireless.com/3D_File/WisDuo/PWB-RAK4270%20Breakout%20Board.stp" target="_blank">RAK4270 Breakout Board 3D Model</a>


## Product Description

The **RAK4270 Breakout Board** is a compact board specifically designed to simplify external connections to the RAK4270 pins. Its primary purpose is to provide access to the stamp module's pins via two rows of 2.54&nbsp;mm headers, making it convenient for debugging.

The RAK4270 LoRa Module includes an **STM32L071 MCU** and an **SX1262 LoRa chip**, which supports eight (8) spreading factors (**SF5 ~ SF12**) and signal bandwidth that can be adjusted between **7.8&nbsp;kHz** to **500&nbsp;kHz**. It has Ultra-Low Power Consumption of 2.31&nbsp;μA (down to 1.61&nbsp;μA @ 2.0&nbsp;V) in sleep mode, but during the Transmit mode, it can reach the maximum output power of **22&nbsp;dBm**. As a receiver, it can achieve a sensitivity of **-148&nbsp;dBm**.

The module complies with the LoRaWAN 1.0.2 protocol, so it can be used for implementing LoRa networks or Lora point-to-point communications. The module is suitable for various applications that require long-range data acquisition and low power consumption, like smart meters, supply chain and logistics tracking, agricultural sensors, smart cities, etc.

This module is expected to be controlled by an external controller through its UART interface by sending a set of AT commands. These AT commands control not only the state of this module but also set the LoRaWan communication parameters and payloads (see RAK <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4270-breakout-board/at-command-manual/" target="_blank">AT Command Manualt</a>).


## Product Features

- LoRa module for Smart City, Smart Agriculture, Smart Industry
- I/O ports: **UART/I2C/GPIO**
- Temperature range: **-30&nbsp;°C** to **+85&nbsp;°C**
- Supply voltage: **2.0 ~ 3.6&nbsp;V**
- Supported bands: EU433, CN470, IN865, EU868, AU915, US915, KR920, and AS923-1/2/3/4
- Low-Power Wireless Systems with 7.8&nbsp;kHz to 500&nbsp;kHz bandwidth
- Ultra-Low Power Consumption of 2.31&nbsp;μA (down to 1.61&nbsp;μA @ 2.0&nbsp;V) in sleep mode
- Core: ARM 32-bit Cortex – M0+ with MPU
- Up to 128&nbsp;KB flash memory with ECC
- 20&nbsp;KB RAM
- 6&nbsp;KB of data EEPROM with ECC

<RkBottomNav/>