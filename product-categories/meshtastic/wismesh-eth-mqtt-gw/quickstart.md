---
slug: /product-categories/meshtastic/wismesh-eth-mqtt-gw/quickstart/
title: WisMesh Ethernet MQTT Gateway
description: Contains instructions and tutorials for installing and deploying your Meshtastic WisMesh Ethernet MQTT Gateway. For a full documentation check the documentation of Meshtastic.org
image: "https://images.docs.rakwireless.com/meshtastic/wismesh-ethernet-gateway.png"
keywords:
  - RAK4631
  - wisblock
  - Meshtastic
  - Nordic
  - nRF52840
  - Semtech
  - SX1262
  - Ethernet
  - PoE
sidebar_label: Quick Start Guide
---

# WisMesh Ethernet MQTT Gateway

The WisMesh MQTT Ethernet Gateway connects your Meshtastic devices to the Cloud, enabling communication with the Meshtastic or your own MQTT Broker. It supports sending sensor data, location information, and text messages.

Besides LoRa connectivity, the device is integrated with the RAK13800 Ethernet module to connect to the internet, all mounted on the RAK19007 Base Board.

Pre-assembled and pre-flashed with the original Meshtastic `firmware-rak4631_eth_gw`, the WisMesh Ethernet MQTT Gateway supports JSON over MQTT for efficient communication.

For added option, the gateway can be powered via the Ethernet cable using the optional RAK19018 PoE module.

> **Image:** WisMesh Ethernet MQTT Gateway

This guide covers the basics for the RAKwireless Meshtastic devices that are not covered by the <a href="https://meshtastic.org/docs/introduction" target="_blank">Meshtastic documentation</a>.

For detailed instructions how to configure the devices for the Meshtastic network, follow the <a href="https://meshtastic.org/docs/getting-started" target="_blank">Meshtastic Getting Started</a> guide.

You can also check the following guides:

<div class="flex items-center flex-col align-center gap-2">
  <a target="_blank" href="https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/" class="no-underline text-white bg-rak-primary px-[15px] py-[5px] rounded-[20px] border-solid border hover:no-underline hover:text-rak-primary hover:bg-white  hover:border-rak-primary no-icon" > Meshtastic Basic Device Setup </a>
</div>

<div class="flex items-center flex-col align-center gap-2">
  <a target="_blank" href="https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-gateway-setup/" class="no-underline text-white bg-rak-primary px-[25px] py-[5px] rounded-[20px] border-solid border hover:no-underline hover:text-rak-primary hover:bg-white  hover:border-rak-primary no-icon" > Meshtastic Gateway Setup </a>
</div>

----

:::tip NOTE
To ensure you are running the latest version of the Meshtastic firmware, it is advised to download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is autodetected. Besides JSON output to the MQTT broker, there's a special firmware for the WisMesh Ethernet MQTT Gateway. Make sure to update the device with this Meshtastic firmware.

- Meshtastic Ethernet MQTT Gateway with RAK4631: **`firmware-rak4631_eth_gw-w.x.yy.zzzzzzz.uf2`**
:::

## Prerequisite

Before going through each and every step on using WisMesh Ethernet MQTT Gateway, make sure to prepare the necessary items listed below:

### Hardware

- <a href="https://store.rakwireless.com/products/wismesh-ethernet-gateway?variant=44413995385030?utm_source=wismesh_eth_gateway&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">WisMesh Ethernet MQTT Gateway</a>

### Software

The WisBlock Core module of the WisMesh Ethernet MQTT Gateway comes pre-flashed with the Meshtastic firmware.

However, to connect the device to the Meshtastic network, you will have to configure it. The recommended way to configure the WisMesh Ethernet MQTT Gateway is using a mobile phone via a BLE connection with either of these configurations:
- <a href="https://meshtastic.org/docs/category/android-app" target="_blank">Android App</a>
- <a href="https://meshtastic.org/docs/category/apple-apps" target="_blank">Apple App</a>

Alternatively, the WisMesh Ethernet MQTT Gateway has an USB connector inside. With the USB connection, you can use either of these configurations:
- <a href="https://meshtastic.org/docs/software/web-client" target="_blank">Web Client</a>
- <a href="https://meshtastic.org/docs/software/python/cli" target="_blank">Python CLI</a>

:::tip NOTE
Make sure that you have installed one of these applications, as they are required for the configuration of the Meshtastic network.
:::

To access the connector, unscrew the mounting plate inside the enclosure and lift it until you gain access to the USB connector.

## Product Configuration

### Hardware Setup

The WisMesh Ethernet MQTT Gateway comes fully assembled. Due to its dimensions, this WisBlock assembly is not compatible with the smaller Unify Enclosure. However, it can be mounted using a custom plate with the <a href="https://store.rakwireless.com/products/unify-enclosure-ip67-150-100-45mm" target="_blank">Unify Enclosure 150x100x45 mm</a>.

> **Image:** Suggested assembly in the Unify Enclosure 150x100x45mm

#### Connect the Ethernet Cable

Connect the Ethernet cable to the RAK13800 Ethernet module, as shown in **Figure 3**

> **Image:** Connect the Ethernet cable

#### Use PoE to Supply the Device

If you have an PoE injector connected to the Ethernet cable, the device can be power through it with the RAK19018 PoE module.

The RAK19018 is a Power-over-Ethernet module used together with the RAK13800 Ethernet Interface module to draw power from CAT5/CAT6 cables. This PoE module is based on the Silvertel Ag9905MT converter board and compatible with the IEEE 802.3af PoE standard.

:::tip NOTE
More details can be found in the <a href="https://docs.rakwireless.com/product-categories/wisblock/rak19018/datasheet" target="_blank">RAK19018 datasheet</a>.
:::

#### Antennas

:::tip NOTE
The WisMesh Ethernet MQTT Gateway comes with a PCB BLE antenna and a LoRa antenna. Make sure the antennas are plugged in properly before powering up the unit.
:::

### Software Setup

To ensure you are running the latest version of the Meshtastic firmware, it is advised to download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is autodetected. To support JSON output to the MQTT broker, there's a special firmware for the WisMesh Ethernet MQTT Gateway. Make sure to update the device with this Meshtastic firmware.

- Meshtastic Ethernet MQTT Gateway with RAK4631: **`firmware-rak4631_eth_gw-w.x.yy.zzzzzzz.uf2`**

**Flashing the WisMesh Ethernet MQTT Gateway Firmware:**

The WisMesh Ethernet MQTT Gateway comes pre-flashed with the Meshtastic firmware. If problems occur, update the Meshtastic firmware to the latest version.

- <a href="https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52" target="_blank">Guide to flash nRF52 devices</a>.

To set up the WisMesh Ethernet MQTT Gateway for the Meshtastic network, follow the <a href="https://meshtastic.org/docs/configuration/" target="_blank">configuration guide</a> in the Meshtastic documentation.

## Tutorial - Meshtastic MQTT Gateway Setup

### Device Setup

The Meshtastic MQTT Gateway comes pre-flashed with Meshtastic firmware, but its device setup differs from other Meshtastic nodes.

:::warning IMPORTANT
- If JSON over MQTT output is required, make sure to flash the **`firmware-rak4631_eth_gw-w.x.yy.zzzzzzz.uf2`** firmware.
- Other RAK4631 Meshtastic firmware do not support JSON over MQTT.
:::

To set up the device, connect the Meshtastic Gateway by selecting it on the Meshtastic app.

> **Image:** WisMesh devices in the Meshtastic Mobile App

:::tip NOTE
- Set all your devices to the same _**Region**_ and _**Channel**_.
- Because the Meshtastic gateway does NOT have a GNSS module, only a FIXED position can be set up.
- If required, a RAK12500 GNSS module can be added to sensor Slot A.
:::

> **Image:** Setup fixed location

### Gateway Connections

1. Connect the gateway to the internet. In this case, the RAK4631 with the RAK13800 Ethernet Module will be used.

> **Image:** Ethernet setup

:::warning IMPORTANT
Below are the options for connecting the gateway through Ethernet:
- For this setup, connect the device via BLE, then configure the Ethernet connection.
- Alternatively, configure the connection settings using the Meshtastic app, via USB, or through the Meshtastic Web GUI or command-line utility.
:::

2. Set up the connection to the MQTT broker.

> **Image:** MQTT setup

:::tip NOTE
- The MQTT broker used here is the free MQTT broker provided by Meshtastic. You can find the URL, address, username, and password in the <a href="https://meshtastic.org/docs" target="_blank">Meshtastic documentation</a>
- To make parsing of the data easier, enable the JSON output.
- To avoid too much traffic, create a custom root topic. If the root topic already existed, it will be more difficult to filter out the devices later at your end.
- If you prefer to see the devices on the public Meshtastic maps (e.g. <a href="https://meshmap.net/" target="_blank">MeshMap.net</a>), enable **Map reporting** and set a **Map reporting interval**.
:::

:::info
A more comprehensive guide for the Meshtastic Gateway can be found in the <a href="https://github.com/beegee-tokyo/Meshtastic-Sensor-Network" target="_blank">Meshtastic-Sensor-Network</a> PoC. This includes setting up multiple sensor nodes, retrieving the sensor data from the MQTT broker, and visualizing the data in Grafana.
:::

