---
title: Meshtastic WisMesh Tag Quick Start Guide 
description: Learn to set up the WisMesh Tag, explore its GNSS and sensor features, and discover how to flash firmware and connect to the Meshtastic network.
image: "https://images.docs.rakwireless.com/meshtastic/wismesh-pod.png"
keywords:
  - wismesh tag setup guide
  - meshtastic
  - st lis2dh
  - ultra-low-power connectivity
  - mesh network
  - rak4631
  - wisblock
  - nordic
  - nrf52840
  - semtech
  - sx1262
sidebar_label: Quick Start Guide
tags:
  - wismesh tag
  - meshtastic
  - quickstart
---

# WisMesh Tag Quick Start Guide

The WisMesh Tag is your super-slim go-to device for ready-to-use and long-lasting connectivity. It is ideal for users seeking a hassle-free Meshtastic node. This device is powered by the efficient MCU Nordic nRF52840, a top performer on the Meshtastic Community Approval list.

Its integrated location tracking and acceleration sensors can provide accurate location data while hiking or traveling. The unique slim enclosure with rubber-style protection makes it weatherproof.

## Product Features

- Robust 1000 mAh built-in battery
- Low Power Nordic nRF52840 MCU
- Semtech SX1262 LoRa transceiver
- Supports 8xx and 9xx MHz LoRa bands
- Antenna: Internal antennas for LoRa, BLE, and GNSS
- Efficiency: Utilizes the most power-efficient solution in the Meshtastic community
- Integrated acceleration sensor based on the ST LIS2DH
- Integrated location sensor based on the AT6558R
- One button for reset, and boot mode functionality
- User button

This guide covers the basics for the RAKwireless Meshtastic devices that are not covered by the [Meshtastic documentation](https://meshtastic.org/docs/introduction).

You can also check the Meshtastic Basic Device Setup Guide:

<div class="flex items-center flex-col align-center gap-2">
  [ Meshtastic Basic Device Setup ](https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/?intsource=docs_center&intmedium=organic&intcampaign=wismesh_tag_documentation_quickstart_page&intterm=meshtastic_basic_device_setup&intcontent=documentation_link)
</div>

----

To be sure to run the latest version of the Meshtastic firmware, we advise you to download the latest [Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisMesh device is auto-detected. This device works with the stock firmware.
- For WisMesh Tag: - **`firmware-wismesh-tag-w.x.yy.zzzzzzz.uf2`**

## Prerequisite

Before going through each step of using the WisMesh Tag, make sure to prepare the necessary items listed below:

### Hardware

- [WisMesh Tag](https://store.rakwireless.com/products/wismesh-tag-meshtastic-gps-lora-tracker-ip66?utm_source=docs_center&utm_medium=organic&utm_campaign=wismesh_tag_documentation_quickstart_page&utm_term=buy_now&utm_content=store_link)
- USB Cable

### Software

The nRF52840 MCU of the WisMesh Tag comes pre-flashed with the Meshtastic firmware.

However, to connect the device to the Meshtastic network, you will have to configure it. Listed below are several applications for the configuration:
- [Android App](https://meshtastic.org/docs/category/android-app)
- [Apple App](https://meshtastic.org/docs/category/apple-apps)
- [Web Client](https://meshtastic.org/docs/software/web-client)
- [Python CLI](https://meshtastic.org/docs/software/python/cli)

:::tip NOTE
Make sure that you have installed one of these applications, as they are required for the configuration of the Meshtastic network.
::::

## Product Configuration

### Hardware Description

The WisMesh Tag comes fully assembled with an internal battery. However, it is recommended to fully recharge the battery before switching the device on. It is powered by its internal 1000 mAh battery and features a multi-function button, three LEDs and a 4-pin connector for recharging.

:::info
The enclosure cannot be opened without damaging the device.
:::

#### LED Indicators

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

#### Button

##### Front Button

The front button, positioned on the top of the device, operates under the control of the Meshtastic firmware. Its functions vary based on the press pattern:
- **Single press**: Dismisses notifications
- **Double press**: Sends the device's position
- **Triple press**: Toggles GPS on or off
- **Long press**: Shuts down the device

> **Image:** WisMesh Tag User button

##### Back Button

The back button is located at the bottom of the device. It is recommended to function as a reset button and does not support long-pressing to power off the device. It performs the following actions:
- **Single press**: Resets the device
- **Double press**: Puts the device into DFU mode

> **Image:** WisMesh Tag Power Button

#### Recharging Port

The 4-pin connector on the top of the device is for recharging the device and also serves as a USB interface to flash new firmware or debug the Meshtastic firmware.
It is recommended to use a 5 V 0.5 A USB charger to recharge the battery.

> **Image:** WisMesh Tag On/Off button

A matching magnetic connector cable with a USB connector is included in the WisMesh Tag package.

#### Antenna

LoRa, BLE and GNSS antennas are inside the enclosure.

#### Dimensions

Enclosure dimensions:

> **Image:** WisMesh Tag dimensions

### Software Setup

:::tip NOTE
To be sure to run the latest version of the Meshtastic firmware, it's recommended to download the latest [Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisMesh Tag is autodetected.

- For WisMesh Tag **`firmware-wismesh-tag-w.x.yy.zzzzzzz.uf2`**
:::

**Flashing the WisMesh Tag Firmware:**

The WisMesh Tag comes pre-flashed with the Meshtastic firmware. If you encounter problems, update the Meshtastic firmware to the latest version.
- [Guide to flash nRF52 devices](https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52) (link goes to Meshtastic.org)

For the setup of the WisMesh Tag for the Meshtastic network, follow the [configuration guide](https://meshtastic.org/docs/configuration/) in the Meshtastic documentation.

