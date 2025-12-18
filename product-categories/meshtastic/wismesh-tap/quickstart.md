---
title: Meshtastic WisMesh TAP  Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your Meshtastic WisMesh TAP. For a full documentation check the documentation of Meshtastic.org
image: "https://images.docs.rakwireless.com/meshtastic/wismesh-tap.png"
keywords:
  - RAK4631
  - wisblock
  - Meshtastic
  - Nordic
  - nRF52840
  - Semtech
  - SX1262
sidebar_label: Quick Start Guide
---

# WisMesh TAP Quick Start Guide

WisMesh TAP is an all-in-one Meshtastic node with on-screen keyboard that allows you to send messages over Meshtastic without your phone.

This guide covers the basics for the RAKwireless Meshtastic devices that are not covered by the <a href="https://meshtastic.org/docs/introduction" target="_blank">Meshtastic documentation</a>. 

For detailed instructions on how to configure the devices for the Meshtastic network, follow the <a href="https://meshtastic.org/docs/getting-started" target="_blank">Meshtastic Getting Started</a> guide.

You can also check the Meshtastic Basic Device Setup Guide:.

<div class="flex items-center flex-col align-center gap-2">
  <a target="_blank" href="https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/" class="no-underline text-white bg-rak-primary px-[15px] py-[5px] rounded-[20px] border-solid border hover:no-underline hover:text-rak-primary hover:bg-white  hover:border-rak-primary no-icon" > Meshtastic Basic Device Setup </a>
</div>    

----

:::tip NOTE
To be sure to run the latest version of the Meshtastic firmware, we advice you to download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to your RAKwireless device to make it compatible with the Meshtastic network.    

This device requires a specific Meshtastic firmware that supports the TFT display and the touch screen.

- WisMesh TAP - The firmware for this device is not yet released in the official Meshtastic Channel. Check with Meshtastic for the **`firmware-rak10701-w.x.yy.zzzzzzz.uf2`**
:::

## Prerequisite

Before going through each and every step on using WisMesh TAP, make sure to prepare the necessary items listed below:

### Hardware

- <a href="https://store.rakwireless.com/products/wismesh-tap" target="_blank">WisMesh TAP</a>
- USB Cable

### Software

The WisBlock Core module of the WisMesh TAP comes pre-flashed with the Meshtastic firmware.

To connect the device to the Meshtastic network, you will have to configure it. Listed below are several applications for the configuration:
- <a href="https://meshtastic.org/docs/category/android-app" target="_blank">Android App</a>
- <a href="https://meshtastic.org/docs/category/apple-apps" target="_blank">Apple App</a>
- <a href="https://meshtastic.org/docs/software/web-client" target="_blank">Web Client</a>
- <a href="https://meshtastic.org/docs/software/python/cli" target="_blank">Python CLI</a>

:::tip NOTE
Make sure that you have installed one of these applications, as they are required for the configuration of the Meshtastic network.
::::

## Product Configuration

### Hardware Setup

The WisMesh TAP comes fully assembled with an internal battery. However, it is recommended to fully recharge the battery before switching the device on. It supports Li-Ion batteries, 5 V (e.g. from solar panel) supply, a 320x240 TFT touchscreen, and an on-screen keyboard.

WisMesh TAP also includes all GPIOs on pin headers, and an integrated GNSS location chip.

The WisMesh TAP is based on the RAKwireless RAK10701 Field Tester. Technical details of the RAKwireless RAK10701 Field Tester can be found in the <a href="https://docs.rakwireless.com/product-categories/wisnode/rak10701-l/datasheet/#rak10701-l-field-tester-for-lorawan-datasheet" target="_blank">RAK10701 Field Tester</a> documentation.

#### Charging and Debugging via USB-C

The WisMesh TAP has a USB-C connector for recharging the device.

#### Recharge the Battery

To recharge the device, plug a USB-C cable into the device and connected it to a 5 V 2 A USB wall charger. Recharging the battery via a USB port on your computer is not recommended due to the potential low current output.

#### Antenna

The LoRa antenna needs to be plugged into the RP-SMA connector of the WisMesh TAP. Make sure the connector is screwed in correct and is secured by tightening the connection.

:::tip NOTE
The BLE antenna and GNSS antenna are inside the enclosure and already connected.
:::

### Software Setup

To be sure to run the latest version of the Meshtastic firmware, we advice you to download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

The firmware for this device is not yet released in the official Meshtastic Channel. Check with Meshtastic for the **`firmware-rak10701-w.x.yy.zzzzzzz.uf2`**

**Flashing the WisMesh TAP firmware:**

The WisMesh TAP comes pre-flashed with the Meshtastic firmware. If you encounter problems, update the Meshtastic firmware to the latest version.

- <a href="https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52" target="_blank">Guide to flash nRF52 devices</a>. (link goes to Meshtastic.org)

For the setup of the WisMesh TAP for the Meshtastic network, follow the <a href="https://meshtastic.org/docs/configuration" target="_blank">configuration guide</a> in the Meshtastic documentation.

### Using the Touch Screen

- You can navigate through the usual Meshtastic screens by swiping on the display to the left or right:    

> **Image:** WisMesh TAP Slide through

- To send messages, swipe up on the screen:

> **Image:** WisMesh TAP Slide through

- Double tap on **Broadcast** or select one of the preset receivers:

> **Image:** WisMesh TAP Slide through

- Start typing the message:

> **Image:** WisMesh TAP Slide through

- Send the message with the RETURN key on the screen.

