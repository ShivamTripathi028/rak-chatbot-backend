---
slug: /product-categories/wisnode/rak7431/firmware-upgrade-guide/
title: RAK7431 WisNode Bridge Serial Firmware Update Guide
description: A step-by-step guide in installing and upgrading the latest firmware of your RAK7201. With this guide, you can ensure that your LoRaWAN Module is always updated, and you can also use this to upload your custom firmware.
image: "https://images.docs.rakwireless.com/wisnode/rak7431/datasheet/rak7431.png"
keywords:
  - Firmware Upgrade
  - RAK7431
  - wisnode
sidebar_label: Firmware Upgrade Guide
---

# RAK7431 WisNode Bridge Serial Firmware Upgrade Guide

For the RAK7201 to work properly, the latest firmware must be installed.

## Overview

To upgrade the firmware of the RAK7431 WisNode Bridge Serial the following will be needed:

- [RAK7431 WisNode Bridge Serial](https://store.rakwireless.com/products/rak7431?utm_source=RAK7431WisNodeBridge&utm_medium=Document&utm_campaign=BuyFromStore)
- [RAK DFU (Device Firmware Upgrade)](https://downloads.rakwireless.com/#LoRa/Tools/RAK_Device_Firmware_Upgrade_tool/)
- Micro USB cable
- [Latest firmware](https://downloads.rakwireless.com/LoRa/RAK7431/Firmware/RAK7431_Latest_Firmware.zip)

## Upgrade Process

1. Download the RAK DFU Tool for your Operating System.

> **Image:** RAK DFU Tool download

2. Download the latest Firmware.

:::tip NOTE
The Latest_Fiirmware.zip file has tree **.bin** files which are for the High, Middle, and Low bands:
- **HB** - high band firmware – supports US915, AS923, AU915, and KR920 LoRaWAN bands.
- **MB** - middle band firmware – supports EU868, IN865, and RU864 LoRaWAN bands.
- **LB** - low band firmware – supports EU433 and CN470 LoRaWAN bands.

Select the correct file corresponding to the LoRaWAN band that your device is working on.
:::

3. Connect RAK7431 to your computer via a micro-USB cable. Check what COM port is the device connected to.

- Under Windows you should see it like this:

> **Image:** COM port check

- Under MacOS and Linux you can check by running the `lsusb` command in the terminal.

4. Start the RAK DFU Tool.
5. Select the correct COM port and Firmware version (HB, MB, or LB).
6. Click the **Upgrade** button to start the process. Wait until the flash is complete. Do not interrupt the process.

> **Image:** RAK DFU Tool

