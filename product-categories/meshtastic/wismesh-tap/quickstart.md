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

This guide covers the basics for the RAKwireless Meshtastic devices that are not covered by the [Meshtastic documentation](https://meshtastic.org/docs/introduction). 

For detailed instructions on how to configure the devices for the Meshtastic network, follow the [Meshtastic Getting Started](https://meshtastic.org/docs/getting-started) guide.

You can also check the Meshtastic Basic Device Setup Guide:.

<div class="flex items-center flex-col align-center gap-2">
  [ Meshtastic Basic Device Setup ](https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/)
</div>    

----

:::tip NOTE
To be sure to run the latest version of the Meshtastic firmware, we advice you to download the latest [Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device to make it compatible with the Meshtastic network.    

This device requires a specific Meshtastic firmware that supports the TFT display and the touch screen.

- WisMesh TAP - The firmware for this device is not yet released in the official Meshtastic Channel. Check with Meshtastic for the **`firmware-rak10701-w.x.yy.zzzzzzz.uf2`**
:::

## Prerequisite

Before going through each and every step on using WisMesh TAP, make sure to prepare the necessary items listed below:

### Hardware

- [WisMesh TAP](https://store.rakwireless.com/products/wismesh-tap)
- USB Cable

### Software

The WisBlock Core module of the WisMesh TAP comes pre-flashed with the Meshtastic firmware.

To connect the device to the Meshtastic network, you will have to configure it. Listed below are several applications for the configuration:
- [Android App](https://meshtastic.org/docs/category/android-app)
- [Apple App](https://meshtastic.org/docs/category/apple-apps)
- [Web Client](https://meshtastic.org/docs/software/web-client)
- [Python CLI](https://meshtastic.org/docs/software/python/cli)

:::tip NOTE
Make sure that you have installed one of these applications, as they are required for the configuration of the Meshtastic network.
::::

## Product Configuration

### Hardware Setup

The WisMesh TAP comes fully assembled with an internal battery. However, it is recommended to fully recharge the battery before switching the device on. It supports Li-Ion batteries, 5 V (e.g. from solar panel) supply, a 320x240 TFT touchscreen, and an on-screen keyboard.

WisMesh TAP also includes all GPIOs on pin headers, and an integrated GNSS location chip.

The WisMesh TAP is based on the RAKwireless RAK10701 Field Tester. Technical details of the RAKwireless RAK10701 Field Tester can be found in the [RAK10701 Field Tester](https://docs.rakwireless.com/product-categories/wisnode/rak10701-l/datasheet/#rak10701-l-field-tester-for-lorawan-datasheet) documentation.

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

To be sure to run the latest version of the Meshtastic firmware, we advice you to download the latest [Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

The firmware for this device is not yet released in the official Meshtastic Channel. Check with Meshtastic for the **`firmware-rak10701-w.x.yy.zzzzzzz.uf2`**

**Flashing the WisMesh TAP firmware:**

The WisMesh TAP comes pre-flashed with the Meshtastic firmware. If you encounter problems, update the Meshtastic firmware to the latest version.

- [Guide to flash nRF52 devices](https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52). (link goes to Meshtastic.org)

For the setup of the WisMesh TAP for the Meshtastic network, follow the [configuration guide](https://meshtastic.org/docs/configuration) in the Meshtastic documentation.

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

