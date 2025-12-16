---
title: RAK7248 WisGate Developer D4H
description: The RAK7248 WisGate Developer D4H is a LoRaWAN Gateway that consists of Raspberry Pi 4, RAK2287 Concentrator, and RAK2287 Pi HAT. The RAK2287 includes a GPS module and a heat sink for improved performance and thermal dissipation management.
keywords:
    - RAK7248
    - WisGate Developer D4H
    - LoRaWAN gateway
    - LoRaWAN gateway Raspberry Pi
image: https://images.docs.rakwireless.com/wisgate/rak7248/RAK7248.png
sidebar_label: Product Overview
---

    
import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK7248 WisGate Developer D4H

Thank you for choosing **RAK7248 WisGate Developer D4H** in your awesome IoT Project 🎉! To help you get started, we have provided you with all the necessary documentation for your product.

* [Quick Start Guide](https://docs.rakwireless.com/product-categories/wisgate/rak7248/quickstart/)
* [LoRaWAN Network Server Guide](https://docs.rakwireless.com/product-categories/wisgate/rak7248/lorawan-network-server-guide/)
* [AWS Greengrass V2](aws-greengrass)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisgate/rak7248/datasheet/)
* [WisGate Developer Gateway Firmware Setup](https://learn.rakwireless.com/hc/en-us/articles/26744073850775-How-To-Set-Up-WisGate-Developer-Gateway-Firmware)
* [RAK7248 Latest Firmware](https://downloads.rakwireless.com/LoRa/RAK7248/Firmware/RAK7248_Latest_Firmware.zip)

## Product Background

The **RAK7248 WisGate Developer D4H** is a LoRaWAN® Gateway that consists of Raspberry Pi4, RAK2287 Concentrator, and RAK2287 Pi HAT.

The **RAK7248C D4H** has a cellular and a PoE variant.

The **RAK7248C WisGate Developer D4H** is the cellular variant, consisting of Raspberry Pi4, RAK2287 Concentrator, RAK2013 Cellular Pi HAT for the cellular connectivity, and RAK2287 Pi HAT.

The **RAK7248P D4H** is the PoE variant that consists of Raspberry Pi4, RAK2287 Concentrator, RAK 9003 for the PoE support, and RAK2287 Pi HAT.

**RAK2287** includes a GPS module and a heat sink for better performance and thermal heat dissipation management, and its housing is built with an aluminum casing.

For the build-in **RAK2287**, uses the **SX1302** chip from Semtech which built-in LoRa concentrator IP core is a powerful digital signal processing engine. It can receive up to **8 LoRa packets** with different spreading factors on different channels and is available in multiple variants so it can be used for international standard bands. This unique capability allows implementing innovative network architectures advantageous over other short-range systems. **RAK2287 Pi HAT** is a converter board a with Raspberry Pi form factor that enables the RAK2287 module to be mounted on top of the Raspberry Pi. It integrates one (1) 40-pin female Pi HAT connector and one mPCIe connector to connect RAK2287 (RAK9003 in PoE variant/RAK2013 in Cellular variant) to the Raspberry Pi 4.

RAK7248 is ideal for prototyping, proof-of-concept demonstrations, or evaluation. It includes a ready-to-use LoRaWAN Gateway OS that can be connected to a LoRaWAN server. Also, it is developer-friendly and simple even for not-so-tech users to set up a LoRaWAN system. It has to be the best value and function for connectivity to address a variety of applications like Smart Grid, Intelligent Farm, and other IoT enterprise applications.

## Product Features

- Computing with Raspberry Pi4 (Linux).
- Based on the LoRa Concentrator Engine: Semtech® SX1302.
- Supports Cellular module (Quectel BG96 or EG95) for NB-IOT / LTE CAT-M1 / LTE CAT1 / LTE CAT4 (only in Cellular variant).
- Built-in Ublox ZOE-M8Q GPS Module.
- Built-in Heat Sink for thermal heat dissipation management.
- Supports 5V/3A and Power-Over-Ethernet (only in PoE variant) power supply.
- IP30 housing.
- TX power up to 27dBm, RX sensitivity down to -139 dBm @SF12, BW 125 KHz.
- LoRa Frequency band support: RU864, IN865, EU868, US915, AU915, KR920, AS923.
- Includes Pi-ready 'ID EEPROM', GPIO setup, and device tree can be automatically configured from vendor information.
- Supports a fully open source LoRaWAN server.