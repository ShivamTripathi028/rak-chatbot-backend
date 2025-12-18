---
title: RAK11160 WisDuo LoRaWAN BLE WiFi Module | ESP8684 MCU
description: Discover the RAK11160, a low-power, long-range LoRaWAN module with STM32WLE5 MCU, ESP8684 WiFi/BLE, and ultra-low power consumption for IoT applications.
image: https://images.docs.rakwireless.com/wisduo/rak11160-module/rak11160-module.png
keywords:
  - rak11160
  - wisduo
  - lorawan module
  - lorawan ble wifi module
  - espressif esp8684
  - stm32wle5 lora module with ble and wifi
  - ble 5 lora module
  - long range low power mcu
  - rak11160 lorawan module
  - rak11160 iot module
tags:
  - rak11160
  - overview
  - wisduo
sidebar_label: Product Overview
slug: /product-categories/wisduo/rak11160-module/overview/
date: 2025-04-24
---

# RAK11160 WisDuo LoRaWAN + BLE + WiFi Module

Thank you for choosing **RAK11160 WisDuo LoRaWAN + BLE + WiFi Module** for your awesome IoT project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

* <a href="https://docs.rakwireless.com/product-categories/wisduo/rak11160-module/quickstart/" target="_blank">Quick Start Guide</a>
* <a href="https://docs.rakwireless.com/product-categories/wisduo/rak11160-module/at-command-manual/" target="_blank">AT Command Manual</a>
* <a href="https://docs.rakwireless.com/product-categories/wisduo/rak11160-module/datasheet/" target="_blank">Datasheet</a>
* <a href="https://downloads.rakwireless.com/3D_File/WisDuo/3D_RAK11160.step" target="_blank">RAK11160 3D Model</a>

## Product Description

The RAK11160 is a low-power, long-range LoRaWAN module based on the STM32WLE5 MCU with integrated LoRa transceiver. It uses an Espressif ESP8684 co-processor to support Bluetooth 5.0 (Bluetooth Low Energy) and WiFi connectivity. Compliant with LoRaWAN 1.0.4 specifications (Classes A, B, and C), the module also supports LoRa point-to-point (P2P) communication, facilitating the quick implementation of customized LoRa networks. With its three RF communication capabilities—LoRa, BLE, and WiFi—this module is well-suited for various IoT applications, including home automation, sensor networks, building automation, and other IoT network applications.

By default, RAK11160 runs on RUI3 (RAKwireless Unified Interface) firmware, allowing standalone operation with custom firmware development via Arduino-compatible RUI3 APIs. Sensors and other external peripherals can be interfaced directly, eliminating the need for an additional MCU. Alternatively, the RAK11160 can be interfaced with an external host MCU using AT commands via UART.

:::tip NOTE
There are two variants available for the RAK11160 Module:
1. Equipped with an MHF4 IPEX connector for external antenna integration
2. No IPEX connector, but includes an RF pinout for connecting a custom antenna
:::

## Product Features

- Based on **STM32WLE5**
	- ARM 32-bit Cortex – M4
	- 256 kB Flash and 64 kB SRAM
- WiFi/BLE modem processor based on **Espressif ESP8684**
	- RISC-V Single-Core CPU
	- 2 MB Flash and 272 kB SRAM
- **LoRaWAN 1.0.4** specification compliant
- **Supported bands**: EU433, CN470, IN865, EU868, AU915, US915, KR920, RU864, and AS923-1/2/3/4
- LoRaWAN Activation by OTAA/ABP
- LoRa Point-to-Point (P2P) communication
- BLE 5.0 support
- WiFi support
- Custom firmware using Arduino via RUI3 API
- Easy-to-use AT Command set STM32WLE5 and LoRa settings via UART interface.
- Espressif AT command to set ESP8684 WiFi and BLE settings via UART interface (same as for STM32WLE5)
- I/O ports: UART/I2C/SPI/ADC/GPIO
- Long-range: greater than 10 km with optimized antenna
- Ultra-low-power consumption of ~6 μA in sleep mode (ESP8684 powered down)
- **Supply Voltage**: 3.0 V ~ 3.6 V
- **Temperature range**: -40° C ~ 85° C

:::tip Note
For CE and FCC certifications we provide an AT command guide.    
You can find it in our <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/certification-guide" target="_blank">RUI3 documentation</a> or get it from our <a href="https://downloads.rakwireless.com/#RUI/RUI3/Certification%20Guide/" target="_blank">Download Center</a>.    
::: 

