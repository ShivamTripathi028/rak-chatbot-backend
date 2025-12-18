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

# WisMesh Pod Quick Start Guide

The WisMesh Pod is your go-to device for ready-to-use and long-lasting connectivity, ideal for users seeking a hassle-free Meshtastic node. This device is powered by the efficient WisDuo module based on the nRF52840, a top performer on the Meshtastic Community Approval list.

Its integrated location tracking and acceleration sensors can provide accurate location data while hiking or traveling. The unique slim enclosure with a rubber-style protection makes it weatherproof.

## Product Features

- Robust 1000 mAh built-in battery
- Antenna: Internal antennas for LoRa, BLE, and GNSS
- Efficiency: Utilizes the most power-efficient solution in the Meshtastic community
- Integrated acceleration sensor based on the ST LIS3DH
- Integrated location sensor based on the u-blox ZOE M8Q
- One button for on/off, reset, and boot mode functionality

This guide covers the basics for the RAKwireless Meshtastic devices that are not covered by the [Meshtastic documentation](https://meshtastic.org/docs/introduction).

You can also check the Meshtastic Basic Device Setup Guide:

<div class="flex items-center flex-col align-center gap-2">
  [ Meshtastic Basic Device Setup ](https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/?intsource=docs_center&intmedium=organic&intcampaign=wismesh_pod_documentation_quickstart_page&intterm=meshtastic_basic_device_setup&intcontent=documentation_link )
</div>

----

To be sure to run the latest version of the Meshtastic firmware, it's recommended to download the latest [Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisMesh device is autodetected. This device works with the stock firmware.

- For WisMesh Pod: - **`firmware-rak4631-w.x.yy.zzzzzzz.uf2`**

## Prerequisite

Before going through each and every step of using the WisMesh Pod, make sure to prepare the necessary items listed below:

### Hardware

- [WisMesh Pod](https://store.rakwireless.com/products/wismesh-pod?utm_source=docs_center&utm_medium=organic&utm_campaign=wismesh-pod-documentation-quickstart-page&utm_term=wismesh-pod&utm_content_store-link)
- USB Cable

### Software

The WisDuo module of the WisMesh Pod comes pre-flashed with the Meshtastic firmware.

However, to connect the device to the Meshtastic network, you will have to configure it. Listed below are several applications for the configuration:
- [Android App](https://meshtastic.org/docs/category/android-app)
- [Apple App](https://meshtastic.org/docs/category/apple-apps)
- [Web Client](https://meshtastic.org/docs/software/web-client)
- [Python CLI](https://meshtastic.org/docs/software/python/cli)

:::tip NOTE
Make sure that you have installed one of these applications, as they are required for configuring the Meshtastic network.
::::

## Hardware Details

The WisMesh Pod comes fully assembled with an internal battery. However, it is recommended to fully recharge the battery before switching the device on. It is powered by its internal 1000 mAh battery and features a multi-function button, three LEDs and a USB-C connector for recharging.

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
- Long press (> 3 seconds): Powers the device on or off The green heartbeat LED indicates power status.
- Short press to reset the device.
- Double short press to switch into bootloader/DFU mode to enable firmware updates over the USB connector.

:::note
This button is _**not**_ a user button. It is only for the above mentioned functions.
:::

> **Image:** WisMesh Pod On/Off button

### USB port

The USB port is a USB-C connector for recharging the battery, flashing, and debugging the Meshtastic firmware.
It is recommended to use a 5 V 0.5 A USB charger to recharge the battery.

### Antenna

LoRa, BLE, and GNSS antennas are inside the enclosure.

### Dimensions

The device is built with a hard shell that cannot be opened and an additional rubber casing for protection.

Enclosure dimensions without rubber casing:

> **Image:** WisMesh Pod dimensions of hard shell

Enclosure dimensions with rubber casing:

> **Image:** WisMesh Pod dimensions with rubber enclosure

## Software Setup

:::tip NOTE
To be sure to run the latest version of the Meshtastic firmware, it's recommended to download the latest [Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisMesh Pod is autodetected.
- For WisMesh Pod **`firmware-rak4631-w.x.yy.zzzzzzz.uf2`**
:::

**Flashing the WisMesh Pod Firmware:**

The WisMesh Pod comes pre-flashed with the Meshtastic firmware. If you encounter problems, update the Meshtastic firmware to the latest version.
- [Guide to flash nRF52 devices](https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52) (link goes to Meshtastic.org)

For the setup of the WisMesh Pod for the Meshtastic network, follow the [configuration guide](https://meshtastic.org/docs/configuration/) in the Meshtastic documentation.

