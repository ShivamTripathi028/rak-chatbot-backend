---
title: Meshtastic WisMesh Pocket Mini Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your Meshtastic WisMesh Pocket Mini. For a full documentation, check the documentation of Meshtastic.org.
image: "https://images.docs.rakwireless.com/meshtastic/wismesh-pocket-mini.png"
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

# WisMesh Pocket Mini Quick Start Guide

WisMesh Pocket Mini is a go-to device for ready-to-use and long-lasting connectivity. Ideal for users seeking a hassle-free Meshtastic node.

This guide covers the basics for the RAKwireless Meshtastic devices that are not covered by the <a href="https://meshtastic.org/docs/introduction" target="_blank">Meshtastic documentation</a>.

For detailed instructions how to configure the devices for the Meshtastic network, follow the <a href="https://meshtastic.org/docs/getting-started" target="_blank">Meshtastic Getting Started</a> guide.

You can also check the Meshtastic Basic Device Setup Guide:.

<div class="flex items-center flex-col align-center gap-2">
  <a target="_blank" href="https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/" class="no-underline text-white bg-rak-primary px-[15px] py-[5px] rounded-[20px] border-solid border hover:no-underline hover:text-rak-primary hover:bg-white  hover:border-rak-primary no-icon" > Meshtastic Basic Device Setup </a>
</div> 

----

:::tip NOTE
To ensure you are running the latest version of the Meshtastic firmware, it is advised to download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is autodetected. This device works with the stock firmware.

- All the base boards with RAK4631/RAK4630: **`firmware-rak4631-w.x.yy.zzzzzzz.uf2`**
- For WisMesh Pocket Mini:  _**DO NOT USE**_ **`firmware-rak4631_eink-w.x.yy.zzzzzzz.uf2`**
:::

## Prerequisite

Before going through each and every step on using WisMesh Pocket Mini, make sure to prepare the necessary items listed below:

### Hardware

- <a href="https://store.rakwireless.com/products/wismesh-pocket-mini?variant=44253549461702" target="_blank">WisMesh Pocket Mini</a>
- USB Cable

### Software

The WisBlock Core module of the WisMesh Pocket Mini comes pre-flashed with the Meshtastic firmware.

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

The WisMesh Pocket Mini comes fully assembled with an internal battery and a battery disconnect switch. However, it is recommended to fully recharge the battery before using the device on. It supports Li-ion batteries and 5 V (e.g. from solar panel) supply.

:::tip NOTE
The battery can only be charged with the ON/OFF switch in _**ON**_ position!
:::

| 
> **Image:** WisMesh Pocket Mini USB
 | 
> **Image:** WisMesh Pocket Mini Switch
 |
| -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |

WisMesh Pocket Mini also includes two WisBlock Sensor Slots.

The WisMesh Pocket Mini is based on the WisBlock RAK19003 Base Board, which is the smallest Base Board version. Technical details of the WisBlock RAK19003 Base Board can be found in the <a href="https://docs.rakwireless.com/product-categories/wisblock/rak19003/datasheet" target="_blank">WisBlock RAK19003 Base Board</a> documentation.

#### Battery Connector and Solar Panel (5 V) Connector

The WisMesh Pocket Mini has an internal connector for a Li-ion battery. Double-check the battery cable polarity when replacing. The matching connector for the battery wires is a <a href="https://www.jst-mfg.com/product/detail_e.php?series=199" target="_blank">JST PHR-2 2 mm pitch female</a>.

WisMesh Pocket Mini also has an internal connector for 5 V supply or solar panel connection. When using this connector, double-check the polarity of the supply cable.

The matching connector for the solar panel wires is an <a href="https://www.jst-mfg.com/product/detail_e.php?series=287" target="_blank">JST ZHR-2 1.5 mm pitch female</a>.

> **Image:** WisMesh Pocket Mini Battery

> **Image:** WisMesh Pocket Mini Solar Panel

#### Recharge the Battery

To recharge the device, plug a USB-C cable into the device and connected it to a 5 V/2 A USB wall charger. Recharging the battery via a USB port on your computer is not recommended due to the potential low current output.

#### Antenna

The BLE antenna and GNSS antenna are both inside the enclosure and have already been connected.

#### Assembling and Disassembling of WisMesh Pocket Mini 

If you want to add more WisBlock modules, simply open the device and plug the modules into their sensor slots.

<!--
##### Disassembling

1. Unscrew the four screws on the corners of the enclosure with a screwdriver.

> **Image:** WisMesh Pocket Mini Disassembly Enclosure Screws

2. Open the enclosure carefully, as there are battery cables between the top and bottom part, do not use force to pull the cables. Then separate three IPEX connectors from PCBA.

> **Image:** WisMesh Pocket Mini Disassembly Opening - Disconnect antenna cables

3. Unscrew four screws that hold the Base Board in the enclosure. Then you can remove the Base Board from the enclosure

> **Image:** WisMesh Pocket Mini Disassembly Base Board removal

4. Separate the battery cable from the Base Board.

> **Image:** WisMesh Pocket Mini Disassembly Battery disconnect

##### Assembling

1. Plug the battery cable into the Base Board.

> **Image:** WisMesh Pocket Mini Assembly Battery connection

2. Put the Base Board into the enclosure and fix it with four screws.

> **Image:** WisMesh Pocket Mini Assembly Mount Base Board

3. Plug the IPEX connectors on the sockets on the Base Board. Make sure to connect each antenna to the correct socket, and then close the enclosure.

> **Image:** WisMesh Pocket Mini Assembly Connect antennas

4. Put the four nuts into the slots on the bottom of the enclosure, then fix the screws.

> **Image:** WisMesh Pocket Mini Assembly Fix enclosure

-->

### Software Setup

To ensure you are running the latest version of the Meshtastic firmware, it is advised to download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is autodetected. This device works with the stock firmware.

- All the base boards with RAK4631/RAK4630: **`firmware-rak4631-w.x.yy.zzzzzzz.uf2`**
- For WisMesh Pocket Mini:  _**DO NOT USE**_ **`firmware-rak4631_eink-w.x.yy.zzzzzzz.uf2`**

**Flashing the WisMesh Pocket Mini firmware:**

The WisMesh Pocket Mini comes pre-flashed with the Meshtastic firmware. If problems occur, update the Meshtastic firmware to the latest version.

- <a href="https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52" target="_blank">Guide to flash nRF52 devices</a>. 

To set up the WisMesh Pocket Mini for the Meshtastic network, follow the <a href="https://meshtastic.org/docs/configuration/" target="_blank">configuration guide</a> in the Meshtastic documentation.

