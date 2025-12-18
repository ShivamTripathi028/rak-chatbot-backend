---
title: RAK3272-SiP WisDuo Breakout Board
description: The RAK3272-SiP Breakout Board is made to quickly evaluate the RAK3272-SiP module. The form factor board allows access to most GPIOs.
image: "https://images.docs.rakwireless.com/wisduo/rak3272-sip-breakout-board/rak3272-sip.png"
keywords:
  - RAK3272-SiP Breakout Board
  - wisduo
sidebar_label: Product Overview
slug: /product-categories/wisduo/rak3272-sip-breakout-board/overview/
download: true
---

# RAK3272-SiP Breakout Board

Thank you for choosing **RAK3272-SiP Breakout Board** in your awesome IoT project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

* [Quick Start Guide](https://docs.rakwireless.com/product-categories/wisduo/rak3272-sip-breakout-board/quickstart/)
* [AT Command Manual](https://docs.rakwireless.com/product-categories/wisduo/rak3272-sip-breakout-board/at-command-manual/)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisduo/rak3272-sip-breakout-board/datasheet/)
* [RAK3272-SiP 3D Model](https://downloads.rakwireless.com/3D_File/WisDuo/3D_RAK3272-SiP.step)

## Product Description

The RAK3272-SiP and RAK3272LP-SiP Breakout Boards were designed to allow easy access to the [RAK3172-SiP/RAK3172LP-SiP](https://docs.rakwireless.com/product-categories/wisduo/rak3172-sip/overview/) module pins to simplify development and testing. The two SiP module variants use different RF output paths to optimize current consumption depending on the application. RAK3172-SiP uses RFO_HP while RAK3172LP-SiP uses the RFO_LP on the STM32WL SoC transceiver.

The microcontroller's GPIO pins are accessible through 2.54 mm headers. The breakout board is powered by either the RAK3172-SiP or the RAK3172LP-SiP, both of which are based on the STM32WLE5JC. The STM32WLE5JC belongs to the [STM32WLE5x](https://www.st.com/en/microcontrollers-microprocessors/stm32wlex.html) family. It features an Arm® Cortex®-M4 core operating at 48 MHz and includes a sub-GHz radio based on the Semtech SX126x.

The board complies with Class A, B, & C of LoRaWAN 1.0.3 specifications and also features LoRa Point-to-Point (P2P) communication mode, which helps you in implementing your own customized long-range LoRa network quickly. It is also RUI3 compatible which allows you to create custom firmware using RUI3 APIs.

## Product Features

- 32-bit Arm® Cortex®‐M4 48 MHz MCU and sub-GHz Semtech SX126x radio
- Chipset STM32WLE5JC (single-core)
- Two variants available
    - RAK3272-SiP (uses RFO_HP)
    - RAK3272LP-SiP (uses RFO_LP)
- I/O ports: UART/I2C/GPIO/SPI
- 32 MHz TCXO and 32 kHz xtal
- RUI3 API compatible
- Custom firmware using Arduino via RUI3 API
- Easy to use AT Command set via UART interface
- Serial Wire Debug (SWD) interface
- **LoRaWAN 1.0.3** specification compliant
- **Supported bands**: IN865, EU868, AU915, US915, KR920, RU864, and AS923
- Supply voltage: 1.8 V ~ 3.6 V
- Temperature range: -40° C ~ 85° C
- Size: 25.4 mm x 41.8 mm

:::tip Note
For CE and FCC certifications we provide an AT command guide.    
You can find it in our [RUI3 documentation](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/certification-guide) or get it from our [Download Center](https://downloads.rakwireless.com/#RUI/RUI3/Certification%20Guide/).    
::: 

