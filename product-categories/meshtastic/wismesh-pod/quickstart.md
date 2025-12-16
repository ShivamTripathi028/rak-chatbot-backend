---
title: Meshtastic WisMesh Pod Quick Start Guide
description: Get started with the WisMesh Pod! This quick start guide covers setup, features, and Meshtastic firmware for seamless IoT connectivity.
image: "https://images.docs.rakwireless.com/meshtastic/wismesh-pod.png"
keywords:
  - wismesh pod setup guide
  - u-blox zoe m8q
  - meshtastic
  - ble connectivity
  - rak4631
  - wisblock
  - nordic
  - nrf52840
  - semtech
  - sx1262
sidebar_label: Quick Start Guide
tags:
  - wismesh pod
  - meshtastic
  - quickstart
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# WisMesh Pod Quick Start Guide

The WisMesh Pod is your go-to device for ready-to-use and long-lasting connectivity, ideal for users seeking a hassle-free Meshtastic node. This device is powered by the efficient WisDuo module based on the nRF52840, a top performer on the Meshtastic Community Approval list.

Its integrated location tracking and acceleration sensors can provide accurate location data while hiking or traveling. The unique slim enclosure with a rubber-style protection makes it weatherproof.

## Product Features

- Robust 1000&nbsp;mAh built-in battery
- Antenna: Internal antennas for LoRa, BLE, and GNSS
- Efficiency: Utilizes the most power-efficient solution in the Meshtastic community
- Integrated acceleration sensor based on the ST LIS3DH
- Integrated location sensor based on the u-blox ZOE M8Q
- One button for on/off, reset, and boot mode functionality

This guide covers the basics for the RAKwireless Meshtastic devices that are not covered by the <a href="https://meshtastic.org/docs/introduction" target="_blank">Meshtastic documentation</a>.

You can also check the Meshtastic Basic Device Setup Guide:

<div class="flex items-center flex-col align-center gap-2">
  <a target="_blank" href="https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/?intsource=docs_center&intmedium=organic&intcampaign=wismesh_pod_documentation_quickstart_page&intterm=meshtastic_basic_device_setup&intcontent=documentation_link " class="no-underline text-white bg-rak-primary px-[15px] py-[5px] rounded-[20px] border-solid border hover:no-underline hover:text-rak-primary hover:bg-white  hover:border-rak-primary no-icon" > Meshtastic Basic Device Setup </a>
</div>

----

To be sure to run the latest version of the Meshtastic firmware, it's recommended to download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisMesh device is autodetected. This device works with the stock firmware.

- For WisMesh Pod: - **`firmware-rak4631-w.x.yy.zzzzzzz.uf2`**

## Prerequisite

Before going through each and every step of using the WisMesh Pod, make sure to prepare the necessary items listed below:

### Hardware

- <a href="https://store.rakwireless.com/products/wismesh-pod?utm_source=docs_center&utm_medium=organic&utm_campaign=wismesh-pod-documentation-quickstart-page&utm_term=wismesh-pod&utm_content_store-link" target="_blank">WisMesh Pod</a>
- USB Cable

### Software

The WisDuo module of the WisMesh Pod comes pre-flashed with the Meshtastic firmware.

However, to connect the device to the Meshtastic network, you will have to configure it. Listed below are several applications for the configuration:
- <a href="https://meshtastic.org/docs/category/android-app" target="_blank">Android App</a>
- <a href="https://meshtastic.org/docs/category/apple-apps" target="_blank">Apple App</a>
- <a href="https://meshtastic.org/docs/software/web-client" target="_blank">Web Client</a>
- <a href="https://meshtastic.org/docs/software/python/cli" target="_blank">Python CLI</a>

:::tip NOTE
Make sure that you have installed one of these applications, as they are required for configuring the Meshtastic network.
::::


## Hardware Details

The WisMesh Pod comes fully assembled with an internal battery. However, it is recommended to fully recharge the battery before switching the device on. It is powered by its internal 1000&nbsp;mAh battery and features a multi-function button, three LEDs and a USB-C connector for recharging.

:::info
The enclosure cannot be opened without damaging the device.
:::

### LED Indicators

The device has 3 colored LEDs, each indicating a different status:
- 🔴 RED LED: The charging indicator. It lights up when the USB connector is plugged in.
:::info
The device can be charged even if it is switched off.
:::
- 🟢 GREEN LED: Shows different states depending on the device's mode:
    - Solid: Powered on
    - Breathing: BLE DFU mode
    - Blinking: MCU activity
- 🔵 BLUE LED: The message indicator. It lights up when a message is received.

### Button

The side button on the device is multifunctional:
- Long press (> 3&nbsp;seconds): Powers the device on or off The green heartbeat LED indicates power status.
- Short press to reset the device.
- Double short press to switch into bootloader/DFU mode to enable firmware updates over the USB connector.

:::note
This button is _**not**_ a user button. It is only for the above mentioned functions.
:::

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/wismesh-pod-button.png"
  width="50%"
  caption="WisMesh Pod On/Off button"
/>

### USB port

The USB port is a USB-C connector for recharging the battery, flashing, and debugging the Meshtastic firmware.
It is recommended to use a 5&nbsp;V 0.5&nbsp;A USB charger to recharge the battery.

### Antenna

LoRa, BLE, and GNSS antennas are inside the enclosure.

### Dimensions

The device is built with a hard shell that cannot be opened and an additional rubber casing for protection.

Enclosure dimensions without rubber casing:

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/wismesh-pod-enclosure.png"
  width="50%"
  caption="WisMesh Pod dimensions of hard shell"
/>

Enclosure dimensions with rubber casing:

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/wismesh-pod-rubber.png"
  width="50%"
  caption="WisMesh Pod dimensions with rubber enclosure"
/>

## Software Setup

:::tip NOTE
To be sure to run the latest version of the Meshtastic firmware, it's recommended to download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisMesh Pod is autodetected.
- For WisMesh Pod **`firmware-rak4631-w.x.yy.zzzzzzz.uf2`**
:::

<b>Flashing the WisMesh Pod Firmware:</b>

The WisMesh Pod comes pre-flashed with the Meshtastic firmware. If you encounter problems, update the Meshtastic firmware to the latest version.
- <a href="https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52" target="_blank">Guide to flash nRF52 devices</a> (link goes to Meshtastic.org)

For the setup of the WisMesh Pod for the Meshtastic network, follow the <a href="https://meshtastic.org/docs/configuration/" target="_blank">configuration guide</a> in the Meshtastic documentation.

<RkBottomNav/>