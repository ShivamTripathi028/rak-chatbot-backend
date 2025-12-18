---
slug: /product-categories/meshtastic/wismesh-tap-v2/quickstart/
title: Meshtastic WisMesh TAP V2 Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your Meshtastic WisMesh TAP. For a full documentation check the documentation of Meshtastic.org
image: "https://images.docs.rakwireless.com/meshtastic/wismesh-tap-v2.png"
keywords:
  - RAK3312
  - wisblock
  - Meshtastic
  - Espressif
  - ESP32-S3
  - Semtech
  - SX1262
sidebar_label: Quick Start Guide
download: true
date: 2025-10-28
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# WisMesh TAP V2 Quick Start Guide

The **WisMesh TAP V2** is an all-in-one Meshtastic node with on-screen keyboard that allows sending messages over the Meshtastic network without using a phone. It supports the Meshtastic UI (MUI), includes an SD Card for the MUI's map function, and features a buzzer to announce incoming messages.

This guide covers the basic information for the RAKwireless Meshtastic devices that are not covered by the <a href="https://meshtastic.org/docs/introduction" target="_blank">Meshtastic documentation</a>.

To get familiar with the MUI, please check the <a href="https://meshtastic.org/docs/software/meshtastic-ui/" target = "_blank">MESHTASTIC UI documentation</a> provided by Meshtastic.

For detailed instructions on how to configure the devices for the Meshtastic network, follow the <a href="https://meshtastic.org/docs/getting-started" target="_blank">Meshtastic Getting Started</a> guide.

You may also check the Meshtastic Basic Device Setup Guide:

<div class="flex items-center flex-col align-center gap-2">
  <a target="_blank" href="https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/" class="no-underline text-white bg-rak-primary px-[15px] py-[5px] rounded-[20px] border-solid border hover:no-underline hover:text-rak-primary hover:bg-white  hover:border-rak-primary no-icon" > Meshtastic Basic Device Setup </a>
</div>

----

:::tip NOTE
To be sure to run the latest version of the Meshtastic firmware, it is recommended to download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to the RAKwireless device for compatibility with the Meshtastic network.

This device requires a specific Meshtastic firmware that supports the TFT display and the touchscreen.

- WisMesh TAP V2 - The firmware for this device has not yet been released in the official Meshtastic Channel. Check with Meshtastic for the correct file: **`firmware-rak_wismesh_tap_v2-tft-w.x.yy.zzzzzzz.bin`**
:::

## Prerequisite

Before going through each and every step on using WisMesh TAP V2, make sure to prepare the necessary items listed below:

### Hardware

- <a href="https://store.rakwireless.com/products/wismesh-tap-v2" target="_blank">WisMesh TAP V2</a>
- USB Cable

### Software

The WisBlock Core module of the WisMesh TAP V2 comes pre-flashed with the Meshtastic firmware.

The MUI offers the complete setup directly on the device using its touchscreen. Refer to the <a href="https://meshtastic.org/docs/software/meshtastic-ui/" target = "_blank">Meshtastic UI documentation</a> provided by Meshtastic for the setup details.


Alternative you can use the applications provided by Meshtastic to setup the device.
Listed below are several applications for the configuration:
- <a href="https://meshtastic.org/docs/category/android-app" target="_blank">Android App</a>
- <a href="https://meshtastic.org/docs/category/apple-apps" target="_blank">Apple App</a>
- <a href="https://meshtastic.org/docs/software/web-client" target="_blank">Web Client</a>
- <a href="https://meshtastic.org/docs/software/python/cli" target="_blank">Python CLI</a>

:::tip NOTE
These applications are optional. Device setup can be completed entirely through the MUI.
::::

## Product Configuration

### Hardware Setup

The WisMesh TAP V2 comes fully assembled with a internal battery. However, it is recommended to fully recharge the battery before switching the device on. It supports Li-Ion batteries, 5&nbsp;V (e.g. from solar panel) supply, a 320x240 TFT touchscreen, and an on-screen keyboard. Internally, it has a SD Card and a buzzer for notifications.

WisMesh TAP V2 also includes all GPIOs on pin headers, an integrated GNSS location chip, and a 3-axis acceleration sensor.

Based on the WisBlock Modular system, this device consists of:
- [RAK19007 WisBlock Base Board](https://docs.rakwireless.com/product-categories/wisblock/rak19007/datasheet/)
- [RAK3312 WisBlock Core](https://docs.rakwireless.com/product-categories/wisblock/rak3312/datasheet/) with Espressif ESP32-S3 and integrated Semtech SX1262 LoRa transceiver
- [RAK12501 WisBlock GNSS location sensor](https://docs.rakwireless.com/product-categories/wisblock/rak12501/datasheet/)
- [RAK1904 WisBlock 3-Axis acceleration sensor](https://docs.rakwireless.com/product-categories/wisblock/rak1904/datasheet/)
- RAK14017 WisBlock TFT LCD display module with integrated SD Card slot and buzzer (Not sold yet).

#### Charging and Debugging via USB-C

The WisMesh TAP V2 has a USB-C connector for recharging the device.

#### Recharge the Battery

To recharge the device, plug a USB-C cable to the WisMesh TAP V2 and plug it into a 5&nbsp;V / 2&nbsp;A USB wall charger. Charging via a computer USB port is not recommended due to the potential low current output.

#### Antenna Installation

Attach the LoRa antenna to the antenna connector on the WisMesh TAP V2. Make sure the connector is properly aligned and tightened securely.

:::tip NOTE
The BLE/WiFi antenna and GNSS antenna are already connected inside the enclosure.
:::

### Software Setup

To ensure you are running the latest version of the Meshtastic firmware, download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

The firmware for this device is not yet released in the official Meshtastic Channel. Check with Meshtastic for the **`firmware-rak_wismesh_tap_v2-tft-w.x.yy.zzzzzzz.bin`**

<b>Flashing the WisMesh TAP V2 firmware:</b>

The WisMesh TAP V2 comes pre-flashed with the Meshtastic firmware. If you encounter any issues, update the device with the latest Meshtastic firmware. For instructions, see: <a href="https://meshtastic.org/docs/getting-started/flashing-firmware/esp32/" target="_blank">Flash ESP32 devices</a> on **Meshtastic.org**.

To configure the WisMesh TAP V2 for the Meshtastic network, follow the <a href="https://meshtastic.org/docs/configuration" target="_blank">Meshtastic Configuration Guide</a>.

### Using the Touchscreen

### Using the Touch Screen

The Meshtastic UI includes a navigation panel on the left side of the screen. Each icon in this panel provides quick access to specific functions.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/wismesh-tap-v2-icons.png"
  width="50%"
  caption="WisMesh TAP V2 navigation"
/>

- **Messaging Icon**: Open the messaging screen.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/wismesh-tap-v2-chat.png"
  width="50%"
  caption="WisMesh TAP V2 chat"
/>

- **Map Icon**: Display the device location and nearby Meshtastic nodes.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/wismesh-tap-v2-map.png"
  width="50%"
  caption="WisMesh TAP V2 map"
/>

:::tip NOTE
For a detailed guide on using the Meshtastic UI, refer to the official <a href="https://meshtastic.org/docs/software/meshtastic-ui/" target = "_blank">MESHTASTIC UI documentation</a>.
:::

<RkBottomNav/>