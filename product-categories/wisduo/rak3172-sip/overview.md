---
title: RAK3172-SiP WisDuo LPWAN SiP
image: https://images.docs.rakwireless.com/wisduo/rak3172-sip/rak3172-sip.png
description: The RAK3172-SiP is a low-power, long-range transceiver based on the STM32WLE5JC SoC in a system-in-package form factor.  It provides an easy-to-use, small, low-power solution for long-range wireless data applications.
keywords:
    - RAK3172-SiP
    - wisduo
sidebar_label: Product Overview
slug: /product-categories/wisduo/rak3172-sip/overview/
download: true
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK3172-SiP WisDuo LPWAN SiP

Thank you for choosing **RAK3172-SiP WisDuo LPWAN SiP** in your awesome IoT project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

* <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-sip/quickstart/" target="_blank">Quick Start Guide</a>
* <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-sip/at-command-manual/" target="_blank">AT Command Manual</a>
* <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-sip/datasheet/" target="_blank">Datasheet</a>
* <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-sip/application-note/" target="_blank">Application Note</a>
* <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3272-sip-breakout-board/datasheet/#schematic-diagram" target="_blank">Reference Design</a>

## Product Description

The RAK3172-SiP (and RAK3172LP-SiP variant) are low-power, long-range transceivers based on the STM32WLE5JC SoC in a system-in-package form factor.  These two modules use different RF output paths to optimize current consumption depending on the application. The RAK3172-SiP uses RFO_HP, while the RAK3172LP-SiP uses the RFO_LP of the STM32WL SoC transceiver.

WisDuo SiP LoRa modules provide a small, easy-to-use, low-power solution for long-range wireless data applications. These modules comply with Classes A, B, and C of the LoRaWAN 1.0.3 specifications. They can easily connect to different LoRaWAN server platforms such as The Things Network (TTN), Helium, Chirpstack, and Actility. They also support LoRa point-to-point (P2P) communication mode, which facilitates the implementation of customized long-range LoRa networks.

The RAK3172-SiP/RAK3172LP-SiP can be configured using AT commands via a UART interface or custom firmware using the RUI3 API.  The RAK3172-SiP/RAK3172LP-SiP are very small and offer low-power features suitable for battery-powered applications.

:::warning
The RAK3172-SiP does not have pre-flashed LoRaWAN credentials and you have to define and setup your own unique credentials for the SiP's.
:::

## Product Features

- Based on **STM32WLE5JC**
- Two variants available
    - RAK3172-SiP (uses RFO_HP)
    - RAK3172LP-SiP (uses RFO_LP)
- System-in-Package form factor
- RUI3 API compatible
- **LoRaWAN 1.0.3** specification compliant
- **Supported bands**: IN865, EU868, AU915, US915, KR920, RU864, and AS923
- LoRaWAN Activation by OTAA/ABP
- LoRa Point-to-Point (P2P) communication
- Custom firmware using Arduino via RUI3 API
- Easy-to-use AT Command set via UART interface
- Long-range - up to 15&nbsp;km with optimized antenna
- ARM Cortex-M4 32-bit
- 256&nbsp;kbytes flash memory with ECC
- 64&nbsp;kbytes RAM
- Ultra-low power consumption of less than 2&nbsp;μA in sleep mode
- **Supply voltage**: 2.0&nbsp;V ~ 3.6&nbsp;V
- **Temperature range**: -40°&nbsp;C ~ 85°&nbsp;C
- **Size**: 12&nbsp;mm x 12&nbsp;mm x 1.22&nbsp;mm
- **Package**: LGA73 type

:::tip Note
For CE and FCC certifications we provide an AT command guide.    
You can find it in our <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/certification-guide" target="_blank">RUI3 documentation</a> or get it from our <a href="https://downloads.rakwireless.com/#RUI/RUI3/Certification%20Guide/" target="_blank">Download Center</a>.    
::: 

<RkBottomNav/>