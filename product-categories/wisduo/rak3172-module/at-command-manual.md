---
title: RAK3172 WisDuo AT Command Manual | LoRaWAN & P2P Commands Guide
description: Master LoRaWAN AT commands with the RAK3172 module, powered by STM32WLE5CCU6. Configure LoRa P2P, UART, and low-power settings for seamless communication.
image: https://images.docs.rakwireless.com/wisduo/rak3172-module/rak3172-module.png
keywords: 
  - stm32wle5ccu5
  - rak3172
  - stm32 lorawan
  - lora development module
  - lora transceiver
  - low-power lora module
  - lora wireless module
  - lora at commands
  - lorawan at command
  - lora p2p at command
date: 2021-04-12
sidebar_label: AT Command Manual
slug: /product-categories/wisduo/rak3172-module/at-command-manual/
download: true
---

# RAK3172 WisDuo LoRaWAN Module AT Command Manual

## Introduction

The RAK3172 WisDuo module is based on the STM32WLE5CC chip and is designed to simplify LoRaWAN and LoRa point-to-point (P2P) communication. To integrate LoRa technology into your projects, the RAK3172 is implemented with an easy-to-use UART communication interface where you can send AT commands. Through these AT commands, you can set the parameters needed for LoRa P2P and LoRaWAN communication. You can also use any microcontroller with a UART interface to control the RAK3172 module.

The UART serial communication is exposed on the UART2 (also identified as the **LPUART1 port**), through **Pin 2 (TX2)** and **Pin 1 (RX2)**. The default parameters of the UART2 communication are **115200 / 8-N-1**. The firmware upgrade is also possible through this port. To familiarize yourself with the pin distribution of this module and find a schematic circuit of a reference application, refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/datasheet/#rak3172-wisduo-lpwan-module-datasheet" target="_blank">RAK3172 Module Datasheet</a>.

### Links to Quick Start Guide

For AT commands example usage, you can check these sections of the quick start guide:

- <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/quickstart/#ttn-otaa-device-registration" target="_blank">RAK3172 TTN OTAA Guide</a> - How to add OTAA device on TTN and what AT commands to use on RAK3172 OTAA activation.
- <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/quickstart/#ttn-abp-device-registration" target="_blank">RAK3172 TTN ABP Guide</a> - How to add ABP device on TTN and what AT commands to use on RAK3172 ABP activation.
- <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/quickstart/#chirpstack-otaa-device-registration" target="_blank">RAK3172 Chirpstack OTAA Guide</a> - How to add OTAA device to Chirpstack and what AT commands to use on RAK3172 OTAA activation.
- <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/quickstart/#chirpstack-abp-device-registration" target="_blank">RAK3172 Chirpstack ABP Guide</a> - How to add ABP device on Chirpstack and what AT commands to use on RAK3172 ABP activation.
- <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/quickstart/#lora-p2p-mode" target="_blank">LoRa P2P</a> - Point to point communication between two RAK3172 modules.

## AT Commands List

There are two AT command sets for RAK3172, depending on the firmware uploaded to the device.

1. <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/at-command-manual/" target="_blank">RUI3 AT Commands</a>

:::tip NOTE
In addition, aside on UART2, AT commands can also be interfaced via UART1 **Pin 4 (TX1)** and **Pin 5 (RX1)**. You can configure the settings of UART1 and UART2 interfaces via <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/#rak-unified-interface-v3-rui3-serial-operating-modes" target="_blank">RUI3 Serial Operating Modes</a>.
:::

2. <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/at-command-manual/" target="_blank">AT Commands (DEPRECATED) - FW version 1.0.4 and below</a>

:::warning
- There are RAK3172 devices loaded with old firmware versions which are not based on RUI3 (RAKwireless Unified Interface V3). These devices have v1.0.4 and below.
- If the host microcontroller code is based on this old firmware, we have a <a href="https://learn.rakwireless.com/hc/en-us/articles/26687498449559-AT-Command-Migration-Guide-of-RAK3172-to-RUI3-RAKwireless-Unified-Interface-V3" target="_blank">RAK3172 AT Command migration guide</a> that explain in detail the few differences between the two AT commands set.
:::

