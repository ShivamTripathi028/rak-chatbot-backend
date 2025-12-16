---
title: RAK3272-SiP WisDuo Breakout Board AT Command Manual
description: Contains instructions and tutorials in installing and deploying your RAK3272-SiP Breakout Board. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Breakout Board.
image: "https://images.docs.rakwireless.com/wisduo/rak3272-sip-breakout-board/rak3272-sip.png"
keywords:
  - RAK3272-SiP Breakout Board
  - wisduo
  - AT Command Manual
sidebar_label: AT Command Manual
slug: /product-categories/wisduo/rak3272-sip-breakout-board/at-command-manual/
download: true
---

import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK3272-SiP Breakout Board AT Command Manual

## Introduction

RAK3272-SiP Breakout Board is based on <a href="https://www.st.com/en/microcontrollers-microprocessors/stm32wlex.html" target="_blank">STM32WLE5x</a> single-core chip and it is designed to simplify LoRaWAN and LoRa point-to-point (P2P) communication. To integrate LoRa technology into your projects, the RAK3272-SiP firmware is implemented with an easy-to-use UART communication interface, based on AT commands. Through these AT commands, you can set the parameters needed for LoRa P2P and LoRaWAN communication. You can also use any microcontroller with a UART interface to control the RAK3272-SiP  board.

The UART serial communication is available on **UART2**, using **Pin 7 (UART2 TX)** and **Pin 8 (UART2 RX)** of the J3 header. The default UART2 communication settings are **115200 baud rate, 8 data bits, no parity, and 1 stop bit (8-N-1)**. Firmware upgrades can also be performed through this port. For details on the module's pin distribution and a reference application schematic, consult the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3272-sip-breakout-board/datasheet/" target="_blank">RAK3272-SiP Breakout Board Datasheet</a>.

## RUI3 AT Command List

The RAK3272-SiP Breakout Board default firmware is based on <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/#hardware-compatibility" target="_blank">RUI3 (RAKwireless Unified Interface V3)</a>. You can access the AT command via UART2 by default.

The complete list of commands can be found in <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/at-command-manual/" target="_blank">RUI3 AT Commands Documentation.</a>


:::tip NOTE
In addition, aside on UART2, AT commands can also be interfaced via UART1 in J4 header **Pin 5 (UART1_RX)** and **Pin 6 (UART1_TX)**. You can configure the settings of UART1 and UART2 interfaces via <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/#rak-unified-interface-v3-rui3-serial-operating-modes" target="_blank">RUI3 Serial Operating Modes</a>.
:::

<RkBottomNav/>