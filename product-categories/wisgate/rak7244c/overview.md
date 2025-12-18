---
title: RAK7244C WisGate Developer D4+
description: RAK7244C features RAK2245, Raspberry Pi 4, GPS, and heat sink for enhanced performance, with RAK2013 enabling LTE connectivity to forward data to the Cloud. Read the full documentation for more information.
keywords:
    - RAK7244C documentation
    - WisGate Developer D4+
    - lorawan gateway raspberry pi 4
image: https://images.docs.rakwireless.com/wisgate/rak7244c/RAK7244C.png
sidebar_label: Product Overview
---

    

# RAK7244C WisGate Developer D4+
Thank you for choosing **RAK7244C WisGate Developer D4+ Gateway** in your awesome IoT Project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

* [Quick Start Guide](https://docs.rakwireless.com/product-categories/wisgate/rak7244c/quickstart/)
* [LoRaWAN Network Server Guide](https://docs.rakwireless.com/product-categories/wisgate/rak7244c/lorawan-network-server-guide/)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisgate/rak7244c/datasheet/)
* [Environment Test Report](test-report)
* [Source Code Repository](https://github.com/RAKWireless/rak_common_for_gateway)
* [WisGate Developer Gateway Firmware Setup](https://learn.rakwireless.com/hc/en-us/articles/26744073850775-How-To-Set-Up-WisGate-Developer-Gateway-Firmware)
* [RAK7244C ready to flash Firmware](https://downloads.rakwireless.com/LoRa/Developer-LoRaWAN-Gateway-RAK7244C/Firmware/RAK7244C_Latest_Firmware.zip)
* [RAK7244C Outdoor Case Assembly Guide](https://docs.rakwireless.com/product-categories/accessories/outdoor-enclosure-kit/overview/#wisgate-developer-d4-rak7244c-outdoor-case)

## Product Background

The **RAK7244C WisGate Developer D4+ Gateway** is a device that consists of Raspberry Pi 4, RAK2245 Pi HAT which includes a GPS module and a Heat Sink for better performance and thermal heat dissipation management, and a RAK2013 Cellular Pi HAT and its housing is built with an aluminum casing.

For the built-in RAK2245 Pi HAT, the SX1301 chip from Semtech is used, which is a built-in LPWAN concentrator IP core, a powerful digital signal processing engine. It can receive up to 8 LoRa packets simultaneously sent with different spreading factors on different channels and is available in multiple options so it can be used for international standard bands. This unique capability allows for the implementation of innovative network architectures advantageous over other short-range systems. For the build-in RAK2013 Cellular Pi HAT, it supports optional QUECTEL BG96 / EG91 / EG95 which can support NB-IoT / CAT-M / CAT1 LTE / CAT4 LTE. It follows Raspberry Pi specifications and is easy to mount with Raspberry Pi and RAK2245 Pi HAT module.

Pilot Gateway Pro is ideal for prototyping, proof-of-concept demonstration, or evaluation. It includes a ready-to-use gateway OS that can be connected to a LoRaWan server. Also, it is developer-friendly and easy even for not-so-techy users to set up the LoRaWan system. It has to be the best value and function for connectivity to address a variety of applications like Smart Grid, Intelligent Farm, and other IoT enterprise applications.

## Product Features

- Preassembled, fully functioning gateway
- **SX1301 baseband processor**, emulates 49 x LoRa demodulators 10 programmable parallel demodulation paths, supports 8 uplinks channels and 1 downlink channel
- Support optional cellular module (Quectel BG96 or EG91 or EG95) for NB-IOT/CAT-M/CAT1 LTE/CAT4 LTE
- Built-in **Ublox MAX-7Q GPS Module**
- Built-in heat sink for thermal heat dissipation management
- Supports 5 V / 2.5 A power supply
- TX power up to 27 dBm, RX sensitivity down to -139 dBm@SF12, BW 125 kHz
- Frequency band support: EU433, CN470, RU864, IN865, EU868, US915, AU915, KR920, AS923
- Housing with top cover, body, bottom cover with riveted motherboard standoff
- Includes Pi ready **ID EEPROM**, **GPIO** setup, and a device tree that  can be automatically configured from vendor information
- Supports fully open-source code connected to a LoRaWAN server