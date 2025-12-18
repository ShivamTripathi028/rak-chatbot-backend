---
title: RAK3172 WisDuo Evaluation Board AT Command Manual
description: For an easier experience with your LoRaWAN Module, a comprehensive list of commands for the LoRa P2P and LoRaWAN communication is provided. A serial communication interface is also presented for the two-way communication of the RAK3172 Evaluation Board.
image: "https://images.docs.rakwireless.com/wisduo/rak3172-evaluation-board/rak3172-evaluation.png"
keywords:
    - RAK3172 Evaluation Board
    - wisduo
    - AT Command Manual
sidebar_label: AT Command Manual
slug: /product-categories/wisduo/rak3172-evaluation-board/at-command-manual/
download: true
---

# RAK3172 Evaluation Board AT Command Manual

## Introduction

The RAK3172 Evaluation WisDuo Board is based on the STM32WLE5CCU6 chip and it is designed to simplify LoRaWAN and LoRa point-to-point (P2P) communication. To integrate LoRa technology into your projects, we implemented an easy-to-use USB interface, through which you can send AT commands. Through these AT commands, you can set the parameters needed for LoRa P2P and LoRaWAN communication.

The RAK3172 Evaluation Board consists of two modules:
- RAK3372 WisBlock Core module
   The RAK3372 is a module built with the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-evaluation-board/overview/" target="_blank">RAK3172 WisDuo Stamp Module</a> on a WisBlock Core-compatible PCB.
- RAK5005-O Base Board
   The RAK5005-O is a WisBlock Base Board that provides a power supply, battery connector, solar panel charging connector, one IO-Slot, and four small extension slots to use WisBlock modules with the evaluation board. You can find detailed information in the <a href="https://docs.rakwireless.com/product-categories/wisblock/rak5005-o/overview/" target="_blank">RAK5005-O Documentation</a>.

The USB serial communication is exposed on the USB connector or the RAK5005-O base board. The default parameters of the UART2 communication are **115200 / 8-N-1**. Firmware upgrade is also possible through this port. To get familiar with the pin distribution of this module and find a schematic circuit of a reference application, refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-evaluation-board/datasheet/" target="_blank">RAK3172-E Module Datasheet</a>.

### Links to Quick Start Guide

For AT commands example usage, you can check these sections of the quick start guide:

- <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-evaluation-board/quickstart/#ttn-otaa-device-registration" target="_blank">TTN OTAA Guide</a> - How to add OTAA device on TTN and what AT commands to use on RAK3172-E OTAA activation.
- <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-evaluation-board/quickstart/#ttn-abp-device-registration" target="_blank">TTN ABP Guide</a> - How to add ABP device on TTN and what AT commands to use on RAK3172-E ABP activation.
- <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-evaluation-board/quickstart/#chirpstack-otaa-device-registration" target="_blank">Chirpstack OTAA Guide</a> - How to add OTAA device to Chirpstack and what AT commands to use on RAK3172-E OTAA activation.
- <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-evaluation-board/quickstart/#chirpstack-abp-device-registration" target="_blank">Chirpstack ABP Guide</a> - How to add ABP device on Chirpstack and what AT commands to use on RAK3172-E ABP activation.
- <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-evaluation-board/quickstart/#lora-p2p-mode" target="_blank">LoRa P2P</a> - Point to point communication between two RAK3172-E modules.

## AT Commands List

There are two AT Commands set for RAK3172-E depending on the firmware uploaded on the device.

1. <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/at-command-manual/" target="_blank">RUI3 AT Commands</a>

:::tip NOTE
In addition, aside on UART2 that is connected to USB-UART converter, AT commands can also be interfaced via **TX1/RX1** on the WisBlock Base board. It is not configured to accept AT command by default. To configure TX1/RX1 interfaces, refer to <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/#rak-unified-interface-v3-rui3-serial-operating-modes" target="_blank">RUI3 Serial Operating Modes</a>.
:::

2. <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-evaluation-board/deprecated-at-command/" target="_blank">AT Commands (DEPRECATED) - FW version 1.0.4 and below</a>

:::warning
- There are RAK3172 devices loaded with old firmware versions which are not based on RUI3 (RAKwireless Unified Interface V3). These devices have v1.0.4 and below.
- If the host microcontroller code is based on this old firmware, we have a <a href="https://learn.rakwireless.com/hc/en-us/articles/26687498449559-AT-Command-Migration-Guide-of-RAK3172-to-RUI3-RAKwireless-Unified-Interface-V3" target="_blank">RAK3172 AT Command migration guide</a> that explain in detail the few differences between the two AT commands set.
:::

