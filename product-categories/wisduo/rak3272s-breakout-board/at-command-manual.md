---
title: RAK3272S WisDuo Breakout Board AT Command Manual
description: Contains instructions and tutorials in installing and deploying your RAK3272S Breakout Board. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: "https://images.docs.rakwireless.com/wisduo/rak3272s-breakout-board/rak3272s-breakout.png"
keywords:
  - RAK3272S  Breakout Board
  - wisduo
  -  AT Command Manual
sidebar_label: AT Command Manual
slug: /product-categories/wisduo/rak3272s-breakout-board/at-command-manual/
download: true
---

# RAK3272S Breakout Board AT Command Manual

## Introduction

The **RAK3272S Breakout Board** is built around the STM32WLE5CC chip and is designed to simplify LoRaWAN and LoRa point-to-point (P2P) communication.

To integrate LoRa technology into your projects, the RAK3272S provides an easy-to-use UART communication interface, allowing you to send AT commands. These commands enable you to configure parameters for both LoRa P2P and LoRaWAN communication. Additionally, any microcontroller with a UART interface can be used to control the RAK3272S board.

The UART serial communication interface is available on **UART2 (also identified as the LPUART1 port)**, accessible via **Pin 7 (TX2)** and **Pin 8 (RX2)**. The default UART2 communication settings are **115200 baud rate, 8 data bits, no parity, and 1 stop bit (8-N-1)**. Firmware upgrades can also be performed through this port. For details on the pin distribution and a reference application schematic, consult the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3272s-breakout-board/datasheet/" target="_blank">RAK3272S Breakout Board Datasheet</a>.

## AT Commands List

There are two AT Commands set for RAK3272S depending on the firmware uploaded on the device.

1. <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/at-command-manual/" target="_blank">RUI3 AT Commands</a>

:::tip NOTE
In addition, aside on UART2 pins, AT commands can also be interfaced via UART1_TX **Pin 5** and UART1_RX **Pin 6** on J5 Header. You can configure the settings of UART1 interfaces via<a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/#rak-unified-interface-v3-rui3-serial-operating-modes" target="_blank">RUI3 Serial Operating Modes</a>.
:::

1. <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3272s-breakout-board/deprecated-at-command/" target="_blank">AT Commands (DEPRECATED) - FW version 1.0.4 and below.</a>

:::warning
- Some RAK3172 devices come with older firmware versions (v1.0.4 and below) that are not based on RUI3 (RAKwireless Unified Interface V3).
- If the host microcontroller code is based on older firmware, the <a href="https://learn.rakwireless.com/hc/en-us/articles/26687498449559-AT-Command-Migration-Guide-of-RAK3172-to-RUI3-RAKwireless-Unified-Interface-V3/" target="_blank">RAK3172 AT Command Migration Guide</a> provides a detailed explanation of the key differences between the two AT command sets.
:::

