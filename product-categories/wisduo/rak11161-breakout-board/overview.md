---
title: RAK11161 WisDuo LoRaWAN BLE WiFi Breakout Board | ESP8684 MCU
description: Discover the RAK11161 Breakout Board, a low-power, long-range LoRaWAN board with STM32WLE5 MCU, ESP8684 WiFi/BLE, and ultra-low power consumption for IoT applications.
image: https://images.docs.rakwireless.com/wisduo/rak11161-breakout-board/rak11161.png
keywords:
  - rak11161
  - wisduo
  - lorawan module
  - lorawan ble wifi module
  - espressif esp8684
  - stm32wle5 lora module with ble and wifi
  - ble 5 lora module
  - long range low power mcu
  - rak11161 lorawan module
  - rak11161 iot module
tags:
  - rak11161
  - overview
  - wisduo
sidebar_label: Product Overview
slug: /product-categories/wisduo/rak11161-breakout-board/overview/
date: 2025-08-14
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK11161 WisDuo LoRaWAN + BLE + WiFi Breakout Board

Thank you for choosing **RAK11161 WisDuo LoRaWAN + BLE + WiFi Breakout Board** for your awesome IoT project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

* <a href="https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/" target="_blank">Quick Start Guide</a>
* <a href="https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/at-command-manual/" target="_blank">AT Command Manual</a>
* <a href="https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/datasheet/" target="_blank">Datasheet</a>
* <a href="https://downloads.rakwireless.com/3D_File/WisDuo/3D_RAK11161.step" target="_blank">RAK11161 3D Model</a>

## Product Description

The **RAK11161** is a breakout board for the low-power, long-range LoRaWAN module RAK11160 based on the STM32WLE5 MCU with integrated LoRa transceiver. It uses an Espressif ESP8684 co-processor to support Bluetooth 5.0 (with Bluetooth Low Energy support) and WiFi connectivity.

Compliant with LoRaWAN 1.0.4 specifications (Classes A, B, and C), the module also supports LoRa point-to-point (P2P) communication, facilitating quick implementation of customized LoRa networks. Additionally, RAK11161 offers three RF communication capabilities (LoRa, BLE, and WiFi), making it well-suited for various IoT applications, such as home automation, sensor networks, building automation, and other IoT network applications.

By default, RAK11161 runs on the RUI3 (RAKwireless Unified Interface) firmware, allowing standalone operation with custom firmware development via Arduino-compatible RUI3 APIs. Sensors and other external peripherals can connect directly, eliminating the need for an additional MCU. Alternatively, the RAK11161 can be interfaced with an external host MCU using AT commands via UART.

## Product Features

- Based on RAK11160
- Provides all RAK11160 pins via a pin header
- Includes Serial Wire Debug (SWD) interface for the STM32WLE5CC
- UART interface for ESP8684 debug
- UART interface for AT command interface
- Based on **STM32WLE5**
	- Arm 32-bit Cortex-M4
	- 256&nbsp;kB Flash and 64&nbsp;kB SRAM
- WiFi/BLE modem processor based on **Espressif ESP8684**
	- RISC-V Single-Core CPU
	- 2&nbsp;MB Flash and 272&nbsp;kB SRAM
- **LoRaWAN 1.0.4** specification compliant
- **Supported bands**: IN865, EU868, AU915, US915, KR920, RU864, and AS923-1/2/3/4
- LoRaWAN Activation by OTAA/ABP
- LoRa Point-to-Point (P2P) communication
- BLE 5.0 support
- WiFi support
- Custom firmware using Arduino via RUI3 API
- Easy-to-use AT command set for STM32WLE5 and LoRa settings via the UART interface
- Espressif AT commands for configuring ESP8684 WiFi and BLE settings via the UART interface (similar to STM32WLE5 commands)
- I/O ports: UART/I2C/SPI/ADC/GPIO
- Long-range: greater than 10&nbsp;km with optimized antenna
- Consumes ~6&nbsp;μA with ESP8684 powered down and STM32WLE5 in deep sleep
- **Supply Voltage**: 3.0&nbsp;V\~3.6&nbsp;V
- **Temperature range**: -40°&nbsp;C\~85°&nbsp;C
- Dimensions: 29&nbsp;mm x 40&nbsp;mm

:::tip Note
For CE and FCC certifications we provide an AT command guide.    
You can find it in our <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/certification-guide" target="_blank">RUI3 documentation</a> or get it from our <a href="https://downloads.rakwireless.com/#RUI/RUI3/Certification%20Guide/" target="_blank">Download Center</a>.    
::: 

<RkBottomNav/>