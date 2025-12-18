---
title: RAK3172-SiP WisDuo LPWAN SiP AT Command Manual
description: Contains instructions and tutorials for installing and deploying your RAK3172-SiP.  Instructions are detailed and step-by-step for easier setup of your LoRaWAN module.
image: https://images.docs.rakwireless.com/wisduo/rak3172-sip/rak3172-sip.png
keywords:
    - wisduo
    - AT Command Manual
    - RAK3172
sidebar_label: AT Command Manual
slug: /product-categories/wisduo/rak3172-sip/at-command-manual/
download: true
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK3172-SiP WisDuo LPWAN SiP AT Command Manual

## Overview

The RAK3172-SiP, based on the STM32WLE5 chip, simplifies LoRaWAN and LoRa point-to-point (P2P) communication.  To integrate LoRa technology into your projects, the RAK3172-SiP uses an easy-to-use UART communication interface for sending AT commands.  These AT commands set parameters for LoRa P2P and LoRaWAN communication. Any microcontroller with a UART interface can control the RAK3172-SiP.

The UART serial communication is exposed on the UART2 (also identified as **LPUART1 port**), through **Pin 29 (TX2)** and **Pin 30 (RX2)**. The default parameters of the UART2 communication are **115200 / 8-N-1**. Firmware upgrades are also possible through this port. To familiarize yourselft with the pin distribution of this module and find a schematic circuit of a reference application, refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-sip/datasheet/" target="_blank">RAK3172-SiP Datasheet</a>.

:::warning
The RAK3172-SiP does not have pre-flashed LoRaWAN credentials. In this case, you have to define and setup your own unique credentials for the SiP's.
:::

## RUI3 AT Command List

The RAK3172-SiP default firmware is based on <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/overview/" target="_blank">RUI3 (RAKwireless Unified Interface V3)</a>. You can access the AT command via UART2 by default.

The complete list of commands can be found in <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/at-command-manual/" target="_blank">RUI3 AT Commands Documentation.</a>


:::tip NOTE
In addition, aside on UART2, AT commands can also be interfaced via UART1 **Pin 17 (TX1)** and **Pin 18 (RX1)**. You can configure the settings of UART1 and UART2 interfaces via <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/#rak-unified-interface-v3-rui3-serial-operating-modes" target="_blank">RUI3 Serial Operating Modes</a>.
:::

<RkBottomNav/>
