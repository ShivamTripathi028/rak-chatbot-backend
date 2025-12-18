---
title: RAK7394 WisGate Developer CM4
description: Explore RAK7394 WisGate Developer CM4 documentation for a versatile LoRaWAN Gateway with cellular and PoE variants, powered by the Raspberry Pi CM4.
image: https://images.docs.rakwireless.com/wisgate/rak7394/rak7394.png
keywords:
    - Raspberry Pi CM4
    - LoRaWAN Gateway
    - lorawan gateway raspberry pi
    - RAK7394
    - RAK7394P
    - RAK7394C
sidebar_label: Product Overview
---

import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK7394 WisGate Developer CM4

Thank you for choosing **RAK7394 WisGate Developer CM4** in your awesome IoT project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

* [Quick Start Guide](https://docs.rakwireless.com/product-categories/wisgate/rak7394/quickstart/)
* [LoRaWAN Network Server Guide](https://docs.rakwireless.com/product-categories/wisgate/rak7394/lorawan-network-server-guide/)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisgate/rak7394/datasheet/)


## Product Description

The **RAK7394 WisGate Developer CM4** is a LoRaWAN Gateway that has a cellular and a PoE variant. This gateway consists of a RAKR314 CM4 Carrier Board + Raspberry Pi Compute Module 4 (CM4), RAK2287 Concentrator, and RAK2287 Pi HAT.

- **Cellular Variant**: The RAK7394C includes the RAKR314 CM4 Carrier Board with a Raspberry Pi CM4, a RAK2287 Concentrator, a RAK2013 Cellular Pi HAT for cellular connectivity, and a RAK2287 Pi HAT.

- **PoE Variant**: The RAK7394P includes the RAKR314 CM4 Carrier Board with a Raspberry Pi CM4, a RAK2287 Concentrator, a RAK9003 for PoE support, and a RAK2287 Pi HAT.

The **RAK2287 Concentrator** includes a GPS module and a heat sink for better performance and thermal heat dissipation management, and its housing is built with an aluminum casing. It also uses the **SX1302** chip from Semtech® whose built-in LoRa concentrator IP core is a powerful digital signal processing engine.

It can receive up to **8 LoRa packets** with different spreading factors on different channels and is available in multiple variants so it can be used for international standard bands. This unique capability allows the implementation of innovative network architectures advantageous over other short-range systems.

The **RAK2287 Pi HAT** is a converter board with a Raspberry Pi form factor that enables the RAK2287 module to be mounted on top of the RAKR314 CM4 Carrier Board. It integrates one (1) 40-pin female Pi HAT connector and one mPCIe connector to connect RAK2287 (RAK9003 in PoE variant/RAK2013 in Cellular variant) to the CM4 Carrier Board.

The **RAKR314 Carrier Board** is designed specifically for the Raspberry Compute Module CM4 following the Raspberry Pi4 form factor. This feature-packed board includes a standard 40 PIN GPIO and supports the RAK PoE HAT, making it an excellent choice for power-over-ethernet applications.

With two USB 2.0 ports, two USB 3.0 ports, two USB-type C ports (one for power and one for programming), and an Ethernet port, this board has all the connectivity options you need. The SD card slot also provides extra storage for the eMMC CM4 modules or serves as a main (boot) for non-eMMC modules. One of the best things about the RAKR314 is that it allows you to utilize the power of the CM4 module in the familiar Raspberry Pi form factor, so you can take advantage of all your existing HATs.

The **RAK7389** is designed for prototyping, proof-of-concept demonstrations, and evaluation. It features a ready-to-use LoRaWAN Gateway OS that connects seamlessly to a LoRaWAN server. With its developer-friendly design, it is easy to set up, even for users with limited technical expertise, making it an excellent choice for building LoRaWAN systems. Offering exceptional value and functionality, it supports a wide range of applications, including Smart Grid, Intelligent Farming, and other IoT enterprise solutions.

:::tip NOTE
By default, the CM4 comes with еMMC and the SD card can be used for additional storage. The SD card can be used for Boot only with CM4 Lite models.
:::

## Product Features

- Computing with Raspberry Pi Compute Module 4.
- Based on the LoRa Concentrator Engine: Semtech SX1302.
- Supports Cellular module (Quectel BG96 or EG95) for NB-IoT / LTE CAT-M1 / LTE CAT1 / LTE CAT4 (only in Cellular variant).
- Built-in Ublox ZOE-M8Q GPS Module.
- Built-in Heat Sink for thermal heat dissipation management.
- Supports 5&nbsp;V / 3&nbsp;A and Power-Over-Ethernet (only in PoE variant) power supply.
- IP30 housing.
- TX power up to 27&nbsp;dBm, RX sensitivity down to -139&nbsp;dBm @SF12, BW 125&nbsp;kHz.
- LoRa Frequency band support: RU864, IN865, EU868, US915, AU915, KR920, AS923.
- Includes Pi-ready 'ID EEPROM', GPIO setup, and device tree can be automatically configured from vendor information.
- Supports a fully open-source LoRaWAN server.


<RkBottomNav/>