---
slug: /product-categories/wisblock/rak11162/overview/
title: RAK11162 WisBlock LoRaWAN Module with Wi-Fi & BLE | Ultra-Low Power IoT MCU
description: Discover the RAK11162, a low-power, long-range WisBlock LoRaWAN module with STM32WLE5 MCU, ESP8684 Wi-Fi/BLE, and ultra-low power consumption for IoT applications.
image: https://images.docs.rakwireless.com/wisblock/rak11162/rak11162.png
keywords:
  - rak11162 module
  - stm32wle5 lora transceiver
  - esp32-c2 wifi ble
  - lorawan module for iot
  - stm32wle5 lorawan development board
  - esp32-c2 wifi ble development board
  - lorawan ble wifi module
  - low power mcu
  - lora p2p communication
  - lora wireless module
  - low power consumption modules
  - long range communication
  - trupple rf iot lorawan module
tags:
  - rak11162
  - wisblock
  - overview
date: 2025-05-23
sidebar_label: Product Overview
---

import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK11162 WisBlock LoRaWAN Module

Thank you for choosing **RAK11162 WisBlock LoRaWAN Module** in your awesome IoT Project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

* [RAK11162 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11162/quickstart/)
* [RAK11162 Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak11162/datasheet/)
* [RAK11160 Datasheet](https://docs.rakwireless.com/product-categories/wisduo/rak11160-module/datasheet/)
* <a href="https://docs.rakwireless.com/product-categories/wisblock/quickstart/" target="_blank">WisBlock Quick Start Guide</a>
* [RUI3 Best Practices](https://github.com/RAKWireless/RUI3-Best-Practice)
* [RUI3 Supported IDE's](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/supported-ide)
* [Bootloader and RUI3 AT command firmware](https://downloads.rakwireless.com/#RUI/RUI3/Image/)
* [RAK11162 3D Model](https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK11162.step)
* [40-Pin Male Connector 3D File](https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/M40S1003K6M.stp)

## Product Description

The **RAK11162** is a WisBlock Core module for RAK **WisBlock**. It extends the **WisBlock** series with a low power STM32WLE MCU that supports LoRa and a ESP8684 co-processor for Bluetooth 5.0 (Bluetooth Low Energy) and Wi-Fi. Compliant with LoRaWAN 1.0.4 specifications (Classes A, B, and C), the module also supports LoRa point-to-point (P2P) communication, facilitating the quick implementation of customized LoRa networks.

With its three RF communication capabilities (LoRa, BLE, and Wi-Fi), this module is well-suited for various IoT applications, including home automation, sensor networks, building automation, and other IoT network applications.

By default, RAK11162 runs on RUI3 (RAKwireless Unified Interface) firmware, allowing standalone operation with custom firmware development via Arduino-compatible RUI3 APIs. Sensors and other external peripherals can be interfaced directly, eliminating the need for an additional MCU.

## Product Features

- Based on **STM32WLE5**
	- ARM 32-bit Cortex – M4
	- 256&nbsp;kB Flash and 64&nbsp;kB SRAM
- Wi-Fi/BLE modem processor based on **Espressif ESP8684**
	- RISC-V Single-Core CPU
	- 2&nbsp;MB Flash and 272&nbsp;kB SRAM
- **LoRaWAN 1.0.4** specification compliant
- **Supported bands**: EU433, CN470, IN865, EU868, AU915, US915, KR920, RU864, and AS923-1/2/3/4
- LoRaWAN Activation by OTAA/ABP
- LoRa Point-to-Point (P2P) communication
- BLE 5.0 support
- Wi-Fi support
- Custom firmware using Arduino via RUI3 API
- Easy-to-use AT Command set STM32WLE5 and LoRa settings via UART interface.
- Espressif AT command to set ESP8684 Wi-Fi and BLE settings via UART interface (same with STM32WLE5)
- I/O ports: UART/I2C/SPI/ADC/GPIO
- Long-range: greater than 10&nbsp;km with optimized antenna
- Ultra-low-power consumption of ~5&nbsp;μA in sleep mode (ESP8684 powered down)
- **Supply Voltage**: 1.8&nbsp;V ~ 3.6&nbsp;V
- **Temperature range**: -40°&nbsp;C ~ 85°&nbsp;C

## Prerequisites

To use a **RAK11162**, you need at least a <a href="https://store.rakwireless.com/collections/wisblock-base?srsltid=AfmBOopZc6hiRouDzzO5q0m5oX1p821fsEmv8clcSIVJmJvtxjafHXqS" target="_blank">WisBlock Base</a> to plug the module in. The WisBlock Base provides power to the RAK11162 module and includes the programming and debugging interface.

:::warning
- Make sure to fix the module with the screws to ensure a proper function.
- When using the LoRa, Wi-Fi, or BLE transceivers, make sure that an antenna is always connected. Using these transceivers without an antenna can damage the system.
:::

:::tip Note
For CE and FCC certifications we provide an AT command guide.    
You can find it in our <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/certification-guide" target="_blank">RUI3 documentation</a> or get it from our <a href="https://downloads.rakwireless.com/#RUI/RUI3/Certification%20Guide/" target="_blank">Download Center</a>.    
::: 

<RkBottomNav/>