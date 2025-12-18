---
title: WisMesh Repeater Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your Meshtastic WisMesh Repeater. For a full documentation check the documentation of Meshtastic.org
image: "https://images.docs.rakwireless.com/meshtastic/wismesh-repeater.png"
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

# WisMesh Repeater Quick Start Guide

WisMesh Repeater is a solar-powered repeater that comes in a waterproof enclosure with a high-performance built-in antenna, making it deployable anywhere regardless of power availability or weather conditions.

This guide covers the basics for the RAKwireless Meshtastic devices that are not covered by the [Meshtastic documentation](https://meshtastic.org/docs/introduction).

For detailed instructions how to configure the devices for the Meshtastic network, follow the [Meshtastic Getting Started](https://meshtastic.org/docs/getting-started) guide.

You can also check the Meshtastic Basic Device Setup Guide:.

<div class="flex items-center flex-col align-center gap-2">
  [ Meshtastic Basic Device Setup ](https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/)
</div>

----

:::tip NOTE
To be sure to run the latest version of the Meshtastic firmware, we advice you to download the latest [Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

Use Meshtastic RAK2560 firmware for this device.

- WisMesh Repeater - **`firmware-rak2560-w.x.yy.zzzzzzz.uf2`**
:::

## Prerequisite

Before going through each and every step on using WisMesh Repeater, make sure to prepare the necessary items listed below:

### Hardware

- [WisMesh Repeater](https://store.rakwireless.com/products/wismesh-repeater?variant=44413994172614?utm_source=wismesh_repeater&utm_medium=Document&utm_campaign=BuyFromStore)

### Software

The WisBlock Core module of the WisMesh Repeater comes pre-flashed with the Meshtastic firmware.

However to connect the device to the Meshtastic network you will have to configure it. The preferred method for the configuration of the WisMesh Repeater is from a mobile phone through a BLE connection with the following:
- [Android App](https://meshtastic.org/docs/category/android-app)
- [Apple App](https://meshtastic.org/docs/category/apple-apps)

Alternatively, the WisMesh Repeater has an USB connector in its unused battery cabinet. To access it, you have to open the battery lid. With the USB connection you can use either of these configurations:
- [Web Client](https://meshtastic.org/docs/software/web-client)
- [Python CLI](https://meshtastic.org/docs/software/python/cli)

The location of the USB connector is shown in **Figure 5**

> **Image:** WisMesh Repeater USB access

Make sure that you have installed one of these applications, as they are required for the configuration of the Meshtastic network.

## Product Configuration

### Hardware Setup

The WisMesh Repeater comes fully assembled. However, it is required to connect it to the Solar Battery Lite to power it up. The WisMesh Repeater itself has no internal battery.

:::warning
The WisMesh Repeater has the option to power the device with four LiSoCl2 batteries. But due to the power consumption of the Meshtastic LoRa network, it is not recommended to power the device with these non-rechargeable batteries. The lifespan of these batteries will be very limited.
:::

#### Connect the battery

Connect the Solar Battery Lite to the WisMesh Repeater as shown in **Figure 6**

> **Image:** WisMesh Repeater connection to the Solar Battery

:::tip NOTE
The cable from the Solar Battery Lite can be plugged into any of the two connectors of the WisMesh Repeater.
:::

To recharge the battery, mount the Solar Battery Lite in direct sun light without any shadowing.

:::tip NOTE
For more details about the mounting options of the solar battery lite, refer to the [Solar Battery Lite Installation Guide](https://docs.rakwireless.com/product-categories/accessories/rak9154/installation-guide#rak9154-solar-battery-installation-guide).
:::

#### Antenna

The WisMesh Repeater has internal LoRa and BLE antennas and does not require the assembly or connection of any external antenna.

#### Assembling and Disassembling of WisMesh Repeater

:::warning
It is strongly recommended to keep both the WisMesh Repeater and the Solar Battery Lite closed at all times. If the devices are opened, the devices might not be waterproof anymore and can be easily damaged.
:::

### Software Setup

To be sure to run the latest version of the Meshtastic firmware, we advice you to download the latest [Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is autodetected. This device works with the stock firmware.

- All the base boards with WisMesh Repeater: **`firmware-rak2560-w.x.yy.zzzzzzz.uf2`**
- For WisMesh Repeater:  _**DO NOT USE**_ - **`firmware-rak4631_eink-w.x.yy.zzzzzzz.uf2`**

**Flashing the WisMesh Repeater firmware:**

The WisMesh Repeater comes pre-flashed with the Meshtastic firmware. If you encounter problems, update the Meshtastic firmware to the latest version.

- [Guide to flash nRF52 devices](https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52). (link goes to Meshtastic.org)

For the setup of the WisMesh Repeater for the Meshtastic network, follow the [configuration guide](https://meshtastic.org/docs/configuration) in the Meshtastic documentation.

