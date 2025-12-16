---
title: Meshtastic WisMesh Pocket V2 Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your Meshtastic WisMesh Pocket V2. For a full documentation, check the documentation of Meshtastic.org
image: "https://images.docs.rakwireless.com/meshtastic/wismesh-pocket-v2.png"
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

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# WisMesh Pocket V2 Quick Start Guide

:::info
WisMesh Pocket V2 is an updated version of the WisMesh Pocket. It has an improved voltage regulator and battery circuit to comply with the European CE requirements. To comply with FCC regulations, it uses an SMA antenna connector.
:::

WisMesh Pocket V2 is a go-to device for ready-to-use and long-lasting connectivity. Ideal for users seeking a hassle-free Meshtastic node.

This guide covers the basics for the RAKwireless Meshtastic devices that are not covered by the <a href="https://meshtastic.org/docs/introduction" target="_blank">Meshtastic documentation</a>.

You can also check the Meshtastic Basic Device Setup Guide:.

<div class="flex items-center flex-col align-center gap-2">
  <a target="_blank" href="https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/" class="no-underline text-white bg-rak-primary px-[15px] py-[5px] rounded-[20px] border-solid border hover:no-underline hover:text-rak-primary hover:bg-white  hover:border-rak-primary no-icon" > Meshtastic Basic Device Setup </a>
</div>

----

To be sure to run the latest version of the Meshtastic firmware, we advice you to download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is autodetected. This device works with the stock firmware.

- All the base boards with RAK4631/RAK4630: - **`firmware-rak4631-w.x.yy.zzzzzzz.uf2`**
- For WisMesh Pocket V2:  _**DO NOT USE**_ - **`firmware-rak4631_eink-w.x.yy.zzzzzzz.uf2`**


## Prerequisite

Before going through each and every step on using WisMesh Pocket V2, make sure to prepare the necessary items listed below:

### Hardware

- <a href="https://store.rakwireless.com/products/wismesh-pocket?variant=43640511365318?utm_source=wismesh_tap&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">WisMesh Pocket V2</a>
- USB Cable

### Software

The WisBlock Core module of the WisMesh Pocket V2 comes pre-flashed with the Meshtastic firmware.

However, to connect the device to the Meshtastic network, you will have to configure it. Listed below are several applications for the configuration:
- <a href="https://meshtastic.org/docs/category/android-app" target="_blank">Android App</a>
- <a href="https://meshtastic.org/docs/category/apple-apps" target="_blank">Apple App</a>
- <a href="https://meshtastic.org/docs/software/web-client" target="_blank">Web Client</a>
- <a href="https://meshtastic.org/docs/software/python/cli" target="_blank">Python CLI</a>

:::tip NOTE
Make sure that you have installed one of these applications, as they are required for the configuration of the Meshtastic network.
::::

## Product Configuration

### Hardware Setup

The WisMesh Pocket V2 comes fully assembled with an internal battery. However, it is recommended to fully recharge the battery before switching the device on. It supports Li-ion batteries, 5&nbsp;V (e.g. from solar panel) supply, integrated user button, battery disconnect switch, and a dedicated connector for a 1.3-inch OLED display.

Additionally, the WisMesh Pocket V2 also includes all GPIOs on pin headers, two WisBlock Sensor Slots, one WisBlock IO slot, and an integrated GNSS location chip on the Base Board.

It is based on the WisMesh Base board version VC, which is specifically designed for the Meshtastic usage. Technical details of the WisMesh Base Board can be found in the <a href="https://docs.rakwireless.com/product-categories/meshtastic/wismesh-base/datasheet-vc/" target="_blank">WisMesh Base Board</a> documentation.

#### Battery and Solar Panel / 5V Connection

The WisMesh Pocket V2 has an internal connector for a Li-ion battery. Make sure to double-check the battery cable polarity during replacement. The compatible connector for the battery wires depends on the board variant:
- For EU/UK (CE & UKCA certification): <a href="https://www.jst-mfg.com/product/detail_e.php?series=199" target="_blank">JST PHR-3 2&nbsp;mm pitch female</a>.
- For other markets: <a href="https://www.jst-mfg.com/product/detail_e.php?series=199" target="_blank">JST PHR-2 2&nbsp;mm pitch female</a>.

:::tip NOTE
To comply with CE regulations, the European board versions have a 3-pin battery connector and can only be used with Li-ion batteries that include an NTC temperature sensor and a 3-wire connector.

Other board versions are equipped with a 2-pin battery connector. An NTC temperature sensor is integrated on the main board.
:::

WisMesh Pocket V2 also has an internal connector for 5&nbsp;V supply or solar panel connection. When using this connector, double-check the polarity of the supply cable.

The matching connector for the solar panel wires is a <a href="https://www.jst-mfg.com/product/detail_e.php?series=287" target="_blank">JST ZHR-2 1.5&nbsp;mm pitch female</a>.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/rak19026_vc_batt_solar.png"
  width="50%"
  caption="WisMesh Pocket V2 Battery and 5 V/Solar Panel"
/>

#### Recharge the Battery

To recharge the device, plug a USB-C cable into the device and connected it to a 5&nbsp;V/2&nbsp;A USB wall charger. Recharging the battery via a USB port on your computer is not recommended due to the potential low current output.

:::tip NOTE
Charge the WisMesh Pocket V2 faster by keeping it off with the ON/OFF switch in the off position.
:::

#### Antenna

The LoRa antenna needs to be plugged into the SMA connector of the WisMesh Pocket. Make sure the connector is properly screwed in and securely tightened.

:::tip NOTE
The BLE antenna and GNSS antenna are inside the enclosure and already connected.
:::

#### Assembling and Disassembling of WisMesh Pocket

If you want to add additional WisBlock modules, you can do so by opening the device and plugging the modules into their sensor or IO slots.

##### Disassembling

1. Unscrew the four screws on the corners of the enclosure with a screwdriver.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/install-01.png"
  width="50%"
  caption="Disassemble screws"
/>

2. Carefully open the enclosure, as there are battery cables between the top and bottom parts. Do not use force to pull the cables. Next, detach the three IPEX connectors from the PCBA.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/install-02.png"
  width="50%"
  caption="Disconnect antenna cables"
/>

3. Unscrew the four screws that secure the Base Board in the enclosure, then take out the Base Board from the enclosure.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/install-03.png"
  width="50%"
  caption="Detach base board"
/>

4. Separate the battery cable from the Base Board.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/install-04.png"
  width="50%"
  caption="Disconnect battery"
/>

##### Assembling

1. Plug the battery cable into the Base Board.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/install-05.png"
  width="50%"
  caption="Connect battery"
/>

2. Put the Base Board into the enclosure and fix it with four screws.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/install-06.png"
  width="50%"
  caption="Mount base board"
/>

3. Plug the IPEX connectors on the sockets on the Base Board. Make sure to connect each antenna to the correct socket, and then close the enclosure.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/install-07.png"
  width="50%"
  caption="Connect antennas"
/>

4. Put the four nuts into the slots on the bottom of the enclosure, then fix the screws.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/install-08.png"
  width="50%"
  caption="Align enclosure and fix screws"
/>


### Software Setup

:::tip NOTE
To be sure to run the latest version of the Meshtastic firmware, we advice you to download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base Board is autodetected. There's a special firmware if you have the <a href="https://store.rakwireless.com/products/wisblock-epd-module-rak14000" target="_blank">RAK14000 WisBlock E-Ink Display</a> connected. All other use cases are covered in the stock firmware.

- All the base boards with RAK4631: **`firmware-rak4631-w.x.yy.zzzzzzz.uf2`**
- For WisMesh Pocket V2:  _**DO NOT USE**_ - **`firmware-rak4631_eink-w.x.yy.zzzzzzz.uf2`**
:::

<b>Flashing the WisMesh Pocket V2 firmware:</b>

The WisMesh Pocket V2 comes pre-flashed with the Meshtastic firmware. If you encounter problems, update the Meshtastic firmware to the latest version.

- <a href="https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52" target="_blank">Guide to flash nRF52 devices</a>. (link goes to Meshtastic.org)

For the setup of the WisMesh Pocket V2 for the Meshtastic network, follow the <a href="https://meshtastic.org/docs/configuration/" target="_blank">configuration guide</a> in the Meshtastic documentation.

<RkBottomNav/>