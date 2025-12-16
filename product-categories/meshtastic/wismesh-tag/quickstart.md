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

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# WisMesh Tag Quick Start Guide

The WisMesh Tag is your super-slim go-to device for ready-to-use and long-lasting connectivity. It is ideal for users seeking a hassle-free Meshtastic node. This device is powered by the efficient MCU Nordic nRF52840, a top performer on the Meshtastic Community Approval list.

Its integrated location tracking and acceleration sensors can provide accurate location data while hiking or traveling. The unique slim enclosure with rubber-style protection makes it weatherproof.

## Product Features

- Robust 1000&nbsp;mAh built-in battery
- Low Power Nordic nRF52840 MCU
- Semtech SX1262 LoRa transceiver
- Supports 8xx and 9xx MHz LoRa bands
- Antenna: Internal antennas for LoRa, BLE, and GNSS
- Efficiency: Utilizes the most power-efficient solution in the Meshtastic community
- Integrated acceleration sensor based on the ST LIS2DH
- Integrated location sensor based on the AT6558R
- One button for reset, and boot mode functionality
- User button

This guide covers the basics for the RAKwireless Meshtastic devices that are not covered by the <a href="https://meshtastic.org/docs/introduction" target="_blank">Meshtastic documentation</a>.

You can also check the Meshtastic Basic Device Setup Guide:

<div class="flex items-center flex-col align-center gap-2">
  <a target="_blank" href="https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/?intsource=docs_center&intmedium=organic&intcampaign=wismesh_tag_documentation_quickstart_page&intterm=meshtastic_basic_device_setup&intcontent=documentation_link" class="no-underline text-white bg-rak-primary px-[15px] py-[5px] rounded-[20px] border-solid border hover:no-underline hover:text-rak-primary hover:bg-white  hover:border-rak-primary no-icon" > Meshtastic Basic Device Setup </a>
</div>

----

To be sure to run the latest version of the Meshtastic firmware, we advise you to download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisMesh device is auto-detected. This device works with the stock firmware.
- For WisMesh Tag: - **`firmware-wismesh-tag-w.x.yy.zzzzzzz.uf2`**

## Prerequisite

Before going through each step of using the WisMesh Tag, make sure to prepare the necessary items listed below:

### Hardware

- <a href="https://store.rakwireless.com/products/wismesh-tag-meshtastic-gps-lora-tracker-ip66?utm_source=docs_center&utm_medium=organic&utm_campaign=wismesh_tag_documentation_quickstart_page&utm_term=buy_now&utm_content=store_link" target="_blank">WisMesh Tag</a>
- USB Cable


### Software

The nRF52840 MCU of the WisMesh Tag comes pre-flashed with the Meshtastic firmware.

However, to connect the device to the Meshtastic network, you will have to configure it. Listed below are several applications for the configuration:
- <a href="https://meshtastic.org/docs/category/android-app" target="_blank">Android App</a>
- <a href="https://meshtastic.org/docs/category/apple-apps" target="_blank">Apple App</a>
- <a href="https://meshtastic.org/docs/software/web-client" target="_blank">Web Client</a>
- <a href="https://meshtastic.org/docs/software/python/cli" target="_blank">Python CLI</a>

:::tip NOTE
Make sure that you have installed one of these applications, as they are required for the configuration of the Meshtastic network.
::::

## Product Configuration

### Hardware Description

The WisMesh Tag comes fully assembled with an internal battery. However, it is recommended to fully recharge the battery before switching the device on. It is powered by its internal 1000&nbsp;mAh battery and features a multi-function button, three LEDs and a 4-pin connector for recharging.

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

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/wismesh-tag-button.png"
  width="50%"
  caption="WisMesh Tag User button"
/>

##### Back Button

The back button is located at the bottom of the device. It is recommended to function as a reset button and does not support long-pressing to power off the device. It performs the following actions:
- **Single press**: Resets the device
- **Double press**: Puts the device into DFU mode

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/wismesh-tag-reset-button.png"
  width="50%"
  caption="WisMesh Tag Power Button"
/>

#### Recharging Port

The 4-pin connector on the top of the device is for recharging the device and also serves as a USB interface to flash new firmware or debug the Meshtastic firmware.
It is recommended to use a 5&nbsp;V 0.5&nbsp;A USB charger to recharge the battery.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/wismesh-tag-port.png"
  width="50%"
  caption="WisMesh Tag On/Off button"
/>

A matching magnetic connector cable with a USB connector is included in the WisMesh Tag package.

#### Antenna

LoRa, BLE and GNSS antennas are inside the enclosure.


#### Dimensions

Enclosure dimensions:

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/wismesh-tag-enclosure.png"
  width="50%"
  caption="WisMesh Tag dimensions"
/>

### Software Setup

:::tip NOTE
To be sure to run the latest version of the Meshtastic firmware, it's recommended to download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisMesh Tag is autodetected.

- For WisMesh Tag **`firmware-wismesh-tag-w.x.yy.zzzzzzz.uf2`**
:::

<b>Flashing the WisMesh Tag Firmware:</b>

The WisMesh Tag comes pre-flashed with the Meshtastic firmware. If you encounter problems, update the Meshtastic firmware to the latest version.
- <a href="https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52" target="_blank">Guide to flash nRF52 devices</a> (link goes to Meshtastic.org)

For the setup of the WisMesh Tag for the Meshtastic network, follow the <a href="https://meshtastic.org/docs/configuration/" target="_blank">configuration guide</a> in the Meshtastic documentation.

<RkBottomNav/>