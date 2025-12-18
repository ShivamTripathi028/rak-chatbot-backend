---
title: RAK7391 WisGate Connect
description: Discover RAK7391 WisGate Connect documentation, a Raspberry Pi CM4-based gateway supporting multiple radio and WisBlock modules, with flexible power options, heat management, and LoRaWAN capabilities.
image: "https://images.docs.rakwireless.com/wisgate/rak7391/rak7391.png"
keywords:
    - RAK7391
    - WisGate Connect
    - Raspberry Pi CM4
    - LoRaWAN gateway Raspberry Pi 4
sidebar_label: Product Overview
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK7391 WisGate Connect

Thank you for choosing **RAK7391 WisGate Connect** in your awesome IoT project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

* [Quick Start Guide](https://docs.rakwireless.com/product-categories/wisgate/rak7391/quickstart/)
* [Assembly Guide](https://docs.rakwireless.com/product-categories/wisgate/rak7391/assembly-guide/)
* [Compatible Hardware](https://docs.rakwireless.com/product-categories/wisgate/rak7391/compatible-hardware/)
* [Services](https://docs.rakwireless.com/product-categories/wisgate/rak7391/services/)
* [Connecting to WisBlock](https://docs.rakwireless.com/product-categories/wisgate/rak7391/connecting-to-wisblock/)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisgate/rak7391/datasheet/)


## Product Description

The RAK7391 WisGate Connect is a Raspberry Pi CM4-based gateway designed to support various radio and WisBlock modules. It features multiple interfaces to accommodate the diverse needs of developers, including HDMI, Ethernet, USB, mPCIe, CSI, DSI, M.2, WisBlock, PoE, and Raspberry Pi HAT. Additionally, it can serve as a basic LoRaWAN gateway, supporting up to four (4) separate modules. This allows for configurations such as a 16-channel sub-GHz LoRaWAN gateway and a 2.4&nbsp;GHz LoRaWAN gateway operating on the same device.

The RAK7391 provides flexible power supply options, including a DC terminal, a Phoenix terminal, and optional PoE support. It features a fan interface for CPU cooling, with control based on the CPU temperature. The device also monitors its power supply, and its ultracapacitors ensure backup power during a failure. This enables the system to send notifications or handle brief power interruptions seamlessly.

## Product Features

### Hardware

- Accepts the complete range of CM4 modules
- Flexible power supply modes such as DC terminal, Phoenix terminal, and POE (optional)
- HDMI 2.0 connector
- 1&nbsp;GB Ethernet with PoE support (optional)
- 2.5&nbsp;GB Ethernet without PoE support (optional)
- USB2.0 + 2x USB3.0
- Type-C USB socket for updating the CM4
- Micro SD card socket for CM4 Lite modules
- Standard fan connector, compatible with 5&nbsp;V and 12&nbsp;V fans (jumper cap configuration)
- External power connector (+5&nbsp;V, +12&nbsp;V with PoE)
- MIPI DSI display FPC connectors (22 pins 0.5&nbsp;mm pitch cable)
- 2x MIPI CSI-2 camera FPC connectors (22 pins 0.5&nbsp;mm pitch cable)
- Raspberry Pi HAT connector
- PoE support via an optional module
- Debug UART port
- 2x WisBlock IO connectors
- 3x mPCIe slots
- 1x M.2 B-Key interface
- RTC with battery socket and ability to wake up CM4
- Configuration jumpers (WiFi and BLE enabling/disabling, EEPROM write enable, buzzer enabling)

### Software

A custom distribution for the WisGate Connect, called RAKPiOS, has been developed. RAKPiOS is a fork of the Raspberry Pi OS, featuring all the necessary drivers for the device, security enhancements, helper scripts, and Docker preinstalled.

You can easily deploy several IoT services from a curated list of Docker containers available from the device.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7391/1.software-structures.png"
  width="70%"
  caption="Software structure"
/>

### Typical Application

- LoRaWAN gateway (multichannel and multiband)
- Industrial gateway leveraging existing WisBlock modules (ModBUS, 4-20&nbsp;mA, 0-5&nbsp;V, and general IO)
- Edge gateway or standalone gateway
- Development platform for new products

<RkBottomNav/>