---
title: RAK11161 WisDuo LoRaWAN+BLE+WiFi Breakout Board AT Command Manual
description: Learn how to use AT commands for the RAK11161 WisDuo LoRaWAN BLE WiFi module with STM32WLE5 & Espressif ESP8684. Full command list inside.
image: https://images.docs.rakwireless.com/wisduo/rak11161-breakout-board/rak11161.png
keywords:
  - rak111610
  - wisduo
  - lorawan module
  - lorawan ble wifi module
  - espressif esp8684
  - stm32wle5 lora module with ble and wifi
  - rak11161 at commands
tags:
  - rak11161
  - at command
  - wisduo
sidebar_label: AT Command Manual
slug: /product-categories/wisduo/rak11161-breakout-board/at-command-manual/
date: 2025-08-05
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK11161 WisDuo LoRaWAN + BLE + WiFi Module AT Command Manual

## Overview

The RAK11161 is based on the STM32WLE5 MCU and the Espressif ESP8684 co-processor. It is designed to simplify LoRaWAN and LoRa point-to-point (P2P) communication.

To integrate LoRa technology into your projects, the RAK11161 uses a simple serial port communication interface for sending AT commands. Through these AT commands, you can set the parameters required for LoRa P2P and LoRaWAN communication on the STM32WLE5. Using the same UART, the ESP8684's Espressif AT commands for WiFi and BLE can be configured.

## RUI3 AT Command List

The RAK11161's default firmware is based on <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/overview/" target="_blank">RUI3 (RAKwireless Unified Interface) V3.</a> By default, AT commands are accessed via UART2.

The complete list of commands can be found in <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/at-command-manual/" target="_blank">RUI3 AT Commands Documentation.</a>

The Espressif AT command manual can be found on Espressif's website in the <a href="https://docs.espressif.com/projects/esp-at/en/latest/esp32/AT_Command_Set/index.html" target="_blank">ESP-AT User Guide.</a>

<RkBottomNav/>