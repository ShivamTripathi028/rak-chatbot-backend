---
slug: /product-categories/meshtastic/wismesh-repeater-mini/quickstart/
title: WisMesh Repeater Mini Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your Meshtastic WisMesh Repeater Mini. For a full documentation, check the documentation of Meshtastic.org.
image: "https://images.docs.rakwireless.com/meshtastic/wismesh-repeater-mini.png"
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

# WisMesh Repeater Mini Quick Start Guide

WisMesh Repeater Mini is a solar-powered repeater that comes in a waterproof enclosure with a high-performance built-in antenna, making it deployable anywhere regardless of power availability or weather conditions.

This guide covers the basics for the RAKwireless Meshtastic devices that are not covered by the [Meshtastic documentation](https://meshtastic.org/docs/introduction).

For detailed instructions how to configure the devices for the Meshtastic network, follow the [Meshtastic Getting Started](https://meshtastic.org/docs/getting-started) guide.

You can also check the Meshtastic Basic Device Setup Guide:.

<div class="flex items-center flex-col align-center gap-2">
  [ Meshtastic Basic Device Setup ](https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/)
</div>

----

:::tip NOTE
To ensure you are running the latest version of the Meshtastic firmware, it is advised to download the latest [Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is autodetected. This use cases is covered in the stock firmware.

- All the base boards with RAK4631: **`firmware-rak4631-w.x.yy.zzzzzzz.uf2`**
:::

## Prerequisite

Before going through each and every step on using WisMesh Repeater Mini, make sure to prepare the necessary items listed below:

### Hardware

- [WisMesh Repeater Mini](https://store.rakwireless.com/products/wismesh-repeater-mini-a-solar-repeater-for-meshtastic?utm_source=wismesh_repeater_mini&utm_medium=Document&utm_campaign=BuyFromStore)

### Software

The WisBlock Core module of the WisMesh Repeater Mini comes pre-flashed with the Meshtastic firmware.

However, to connect the device to the Meshtastic network, you will have to configure it. The recommended way to configure the WisMesh Repeater Mini is using a mobile phone via a BLE connection with either of these configurations:
- [Android App](https://meshtastic.org/docs/category/android-app)
- [Apple App](https://meshtastic.org/docs/category/apple-apps)

Alternatively, the WisMesh Repeater Mini has an USB connector inside. With the USB connection, you can use either of these configurations:
- [Web Client](https://meshtastic.org/docs/software/web-client)
- [Python CLI](https://meshtastic.org/docs/software/python/cli)

:::tip NOTE
Make sure that you have installed one of these applications, as they are required for the configuration of the Meshtastic network.
:::

To access the USB port, follow these simple steps:

1. Remove the rubber plug on the side of the enclosure, as shown in **Figure 1**.

> **Image:** Remove the rubber plug

2. Access the USB port, as shown in **Figure 2**

> **Image:** Access the USB port

## Product Configuration

### Hardware Setup

The WisMesh Repeater Mini comes fully assembled. However, it is required to connect the battery to the WisBlock Base Board inside the enclosure.

:::warning IMPORTANT
The WisMesh Repeater Mini's internal battery is disconnect to avoid discharge of the battery during transportation.
:::

#### Connect the Battery

To connect the battery, open the enclosure lid and attach the battery cable to the battery connector on the WisBlock Base Board, as shown in **Figure 3**.

> **Image:** WisMesh Repeater Mini connect the battery

:::warning CAUTION
Make sure the cable of the battery is plugged in the correct orientation.
:::

To recharge the battery, mount the WisMesh Repeater Mini with its solar panel facing direct sunlight, ensuring there is no shadow. Alternatively, you can charge the battery through the USB port.

:::tip NOTE
For more details about the mounting options of the WisMesh Repeater, refer to the [Unify Enclosure mounting accessories](https://docs.rakwireless.com/product-categories/wisblock/rakbox-accessories/overview/).
:::

#### Antenna

The WisMesh Repeater Mini has an internal BLE antenna and an external LoRa antenna. Make sure that the LoRa antenna is plugged in properly before powering up the unit.

#### Assembling and Disassembling of WisMesh Repeater Mini

:::warning
It is strongly recommended to keep the WisMesh Repeater Mini closed at all times. If the devices are opened, make sure the assembly of the lid is properly done to avoid water intrusions into the enclosure.
:::

### Software Setup

To ensure you are running the latest version of the Meshtastic firmware, it is advised to download the latest [Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is autodetected. There's a special firmware if you have the RAK14000 WisBlock E-Ink Display connected. All other use cases are covered in the stock firmware.

- All the base boards with RAK4631: **`firmware-rak4631-w.x.yy.zzzzzzz.uf2`**

**Flashing the WisMesh Repeater Mini Firmware:**

The WisMesh Repeater Mini comes pre-flashed with the Meshtastic firmware. If problems occur, update the Meshtastic firmware to the latest version.

- [Guide to flash nRF52 devices](https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52).

To set up the WisMesh Repeater Mini for the Meshtastic network, follow the [configuration guide](https://meshtastic.org/docs/configuration/) in the Meshtastic documentation.

