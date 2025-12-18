---
slug: /product-categories/meshtastic/wismesh-wifi-mqtt-gw/quickstart/
title: WisMesh WiFi MQTT Gateway
description: Contains instructions and tutorials for installing and deploying your Meshtastic WisMesh WiFi MQTT Gateway. For a full documentation, check the documentation of Meshtastic.org.
image: "https://images.docs.rakwireless.com/meshtastic/wismesh-ethernet-gateway.png"
keywords:
 - RAK11200
  - RAK13300
  - RAK3312
  - wisblock
  - Meshtastic
  - Espressif
  - ESP32
  - ESP32-S3
  - Semtech
  - SX1262
  - WiFi
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# WisMesh WiFi MQTT Gateway

The WisMesh WiFi MQTT Gateway connects your Meshtastic devices to the cloud, enabling communication with either the Meshtastic MQTT broker or your own MQTT broker. It supports sending sensor data, location information, and text messages.

:::tip NOTE
The **WisMesh WiFi MQTT Gateway** was updated to **WisMesh WiFi MQTT Gateway V2** by replacing the ESP32 Wroover MCU with an ESP32-S3 MCU. This update does not affect the functionality.
:::

The original device featured the WisBlock RAK11200 Core module with Meshtastic firmware, integrated WiFi and BLE, and the RAK13300 LoRa module, all mounted on the RAK19007 Base Board.

With the update to **WisMesh WiFi MQTT Gateway V2**, the device uses the WisBlock RAK3312 Core module with Meshtastic firmware, integrated WiFi, BLE and a LoRa transceiver. 

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/meshtastic/wismesh-wifi-gateway.png"
  width="50%"
  caption="WisMesh WiFi MQTT Gateway V2"
/>

The device comes in a Unify 100x75x38&nbsp;mm enclosure, offering a variety of mounting options.

:::tip NOTE
For more details about the mounting options of the WisMesh WiFi MQTT Gateway, refer to the <a href="https://docs.rakwireless.com/product-categories/wisblock/rakbox-accessories/overview/" target="_blank">Unify Enclosure mounting accessories</a>.
:::

This guide covers the basics for RAKwireless Meshtastic devices that are not covered by the <a href="https://meshtastic.org/docs/introduction" target="_blank">Meshtastic documentation</a>.

For detailed instructions on how to configure the devices for the Meshtastic network, follow the <a href="https://meshtastic.org/docs/getting-started" target="_blank">Meshtastic Getting Started</a> guide.

You can also refer to the following guides:

<div class="flex items-center flex-col align-center gap-2">
  <a target="_blank" href="https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/" class="no-underline text-white bg-rak-primary px-[15px] py-[5px] rounded-[20px] border-solid border hover:no-underline hover:text-rak-primary hover:bg-white  hover:border-rak-primary no-icon" > Meshtastic Basic Device Setup </a>
</div>

<br/>

<div class="flex items-center flex-col align-center gap-2">
  <a target="_blank" href="https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-gateway-setup/" class="no-underline text-white bg-rak-primary px-[25px] py-[5px] rounded-[20px] border-solid border hover:no-underline hover:text-rak-primary hover:bg-white  hover:border-rak-primary no-icon" > Meshtastic Gateway Setup </a>
</div>

----

:::tip NOTE
To ensure you are running the latest version of the Meshtastic firmware, it is advised to download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> version and upload it to your RAKwireless device. This ensures compatibility with the Meshtastic network.

For firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is auto-detected. A special firmware version is required for the WisMesh WiFi MQTT Gateway. Make sure to update the device with the appropriate Meshtastic firmware:
- Meshtastic WiFi MQTT Gateway with RAK11200: **`firmware-rak11200-w.x.yy.zzzzzzz.bin`**
- Meshtastic WiFi MQTT Gateway V2 with RAK3312: **`firmware-rak3312-w.x.yy.zzzzzzz.bin`**
:::

## Prerequisite

Before going through each and every step on using WisMesh WiFi MQTT Gateway, make sure to prepare the necessary items listed below:

### Hardware

- <a href="https://store.rakwireless.com/products/wismesh-wifi-gateway?utm_source=wismesh_wifi_gateway&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">WisMesh WiFi MQTT Gateway</a>

### Software

The WisBlock Core module of the WisMesh WiFi MQTT Gateway comes pre-flashed with the Meshtastic firmware.

However, to connect the device to the Meshtastic network, it must be configure. The recommended method is using a mobile device via BLE, with one of the following apps:
- <a href="https://meshtastic.org/docs/category/android-app" target="_blank">Android App</a>
- <a href="https://meshtastic.org/docs/category/apple-apps" target="_blank">Apple App</a>

Alternatively, the WisMesh WiFi MQTT Gateway has an USB connector inside. With the USB connection, you can use either of these configurations:
- <a href="https://meshtastic.org/docs/software/web-client" target="_blank">Web Client</a>
- <a href="https://meshtastic.org/docs/software/python/cli" target="_blank">Python CLI</a>

:::tip NOTE
Make sure to install one of these applications. They are required to configure the device for the Meshtastic network.
:::

To access the USB connector, unscrew the mounting plate inside the enclosure and lift it to reveal the connector.

## Product Configuration

### Hardware Setup

The WisMesh WiFi MQTT Gateway comes fully assembled. It is also available in the <a href="https://store.rakwireless.com/products/unify-enclosure-ip65-100-75-38mm" target="_blank">Unify Enclosure IP67 100x75x38&nbsp;mm</a>.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/meshtastic/wifi-gw-enclosure.png"
  width="50%"
  caption="WisMesh WiFi MQTT Gateway in the Unify Enclosure 100x75x38mm"
/>

#### Power Supply

The WisMesh WiFi MQTT Gateway supports two power supply options:

**1. USB connector**    
To power the device via USB, connect it to a wall adapter or a similar power source using a USB-C cable. The power source must provide 5&nbsp;V and 1.5&nbsp;A.

:::tip NOTE
When using the USB connector for power supply, the enclosure is no longer waterproof.
:::

**2. 5-pin M8 connector**    
The enclosure features a waterproof 5-pin connector, allowing the device to be powered from any 5&nbsp;V, 1.5&nbsp;A power supply. To supply through the M8 connector, use the included cable stub and connect the red and black wires to the power source.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/meshtastic/wifi-gw-power.png"
  width="50%"
  caption="WisMesh WiFi MQTT Gateway M8 power supply connection"
/>

#### Antennas

The WisMesh WiFi MQTT Gateway comes with:
- A PCB BLE antenna
- An external LoRa antenna

:::warning
Ensure both antennas are properly connected before powering on the device.
:::

### Software Setup

To ensure you are running the latest version of the Meshtastic firmware, it is advised to download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is auto-detected. Besides JSON output to the MQTT broker, there's a special firmware for the WisMesh WiFi MQTT Gateway. Make sure to update the device with this specific Meshtastic firmware.

- Meshtastic WiFi MQTT Gateway with RAK11200: **`firmware-rak11200-w.x.yy.zzzzzzz.bin`**
- Meshtastic WiFi MQTT Gateway V2 with RAK3312: **`firmware-rak3312-w.x.yy.zzzzzzz.bin`**

<b>Flashing the WisMesh WiFi MQTT Gateway Firmware:</b>

The WisMesh WiFi MQTT Gateway comes pre-flashed with the Meshtastic firmware. If problems occur, update the Meshtastic firmware to the latest version.

- <a href="https://meshtastic.org/docs/getting-started/flashing-firmware/esp32/" target="_blank">Guide to flash ESP32 devices</a>. (link goes to Meshtastic.org)

To set up the WisMesh WiFi MQTT Gateway for the Meshtastic network, follow the <a href="https://meshtastic.org/docs/configuration/" target="_blank">configuration guide</a> in the Meshtastic documentation.


## Tutorial - Meshtastic MQTT Gateway Setup

### Device Setup

The Meshtastic MQTT Gateway comes pre-flashed with Meshtastic firmware, but its device setup differs from other Meshtastic nodes.

To set up the device, connect the Meshtastic Gateway by selecting it on the Meshtastic app.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/meshtastic/gw-device-list.png"
  width="30%"
  caption="WisMesh devices in the Meshtastic Mobile App"
/>

:::tip NOTE
- Set all devices to the same _**Region**_ and _**Channel**_.
- The gateway does not include a GNSS module, so only a FIXED position can be set.
- If required, a RAK12501 GNSS module can be added to sensor Slot A.
:::

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/meshtastic/gw-fixed-location.png"
  width="30%"
  caption="Setup fixed location"
/>

### Gateway Connections

1. Connect the gateway to the internet. In this case, the RAK3312 or RAK11200 with its built-in WiFi will be used.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/meshtastic/gw-wifi-network.png"
  width="30%"
  caption="WiFi setup"
/>

:::warning IMPORTANT
Below are the options for connecting the gateway through WiFi:
- For this setup, connect the device via BLE, then configure the WiFi credentials.
- Alternatively, configure via USB using the Meshtastic Web GUI or command-line utility.
:::

:::tip NOTE
Once connected to the WiFi network, the device's IP address will be shown in the device list.
:::

2. Set up the connection to the MQTT broker.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/meshtastic/gw-mqtt-settings.png"
  width="30%"
  caption="MQTT setup"
/>

:::tip NOTE
- The MQTT broker used here is the free MQTT broker provided by Meshtastic. You can find the URL, address, username, and password in the <a href="https://meshtastic.org/docs" target="_blank">Meshtastic documentation</a>.
- To make parsing of the data easier, enable the JSON output.
- To avoid too much traffic, create a custom root topic. If the root topic already existed, it will be more difficult to filter out the devices later at your end.
- If you prefer to see the devices on the public Meshtastic maps (e.g. <a href="https://meshmap.net/" target="_blank">MeshMap.net</a>), enable **Map reporting** and set a **Map reporting interval**.
:::

:::info
A more comprehensive guide for the Meshtastic Gateway can be found in the <a href="https://github.com/beegee-tokyo/Meshtastic-Sensor-Network" target="_blank">Meshtastic-Sensor-Network</a> PoC. This includes setting up multiple sensor nodes, retrieving the sensor data from the MQTT broker, and visualizing the data in Grafana.
:::


<RkBottomNav/>