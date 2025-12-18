---
title: RAK4630 WisDuo LoRaWAN+BLE Module AT Command Manual
description: For easier use of your LoRaWAN module, a comprehensive list of commands for LoRa P2P and LoRaWAN communication is provided.  A serial communication interface is also presented for two-way communication with the RAK4630 WisDuo LoRaWAN module.
image: https://images.docs.rakwireless.com/wisduo/rak4630-module/rak4630-module.png
keywords:
  - RAK4630
  - AT Command Manual
sidebar_label: AT Command Manual
slug: /product-categories/wisduo/rak4630-module/at-command-manual/
download: true
---

# RAK4630 WisDuo LoRaWAN+BLE Module AT Command Manual

## Overview

The RAK4630 is built on the nRF52840 chip and incorporates the LoRa transceiver SX1262.  Its purpose is to streamline LoRaWAN and LoRa point-to-point (P2P) communication.  It also leverages the BLE functionality of the nRF52840 chip. To integrate LoRa technology into your projects, the RAK4630 offers a user-friendly serial port communication interface for sending AT commands. These AT commands enable configuration of the parameters required for LoRa P2P and LoRaWAN communication.

## RUI3 AT Command List

The RAK4630's default firmware is based on [RUI3 (RAKwireless Unified Interface V3)](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/overview/).  AT commands are accessible via USB and BLE by default.

A complete list of commands is available in the [RUI3 AT Commands Documentation](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/at-command-manual/).

:::tip NOTE
Apart from USB and BLE, AT commands can also be interfaced via UART1 (pins 9 and 10) and UART2 (pins 6 and 7—no AT command functionality by default).  For details on the pin distribution of this module, refer to the [RAK4630 Datasheet](https://docs.rakwireless.com/product-categories/wisduo/rak4630-module/datasheet/#pin-definition). The basic circuit setup can be found in the [RAK4630 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisduo/rak4630-module/quickstart/#hardware-setup). You can configure the settings of each interface through the [RUI3 Serial Operating Modes](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/#rak-unified-interface-v3-rui3-serial-operating-modes).
:::

