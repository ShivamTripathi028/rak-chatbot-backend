---
slug: /product-categories/meshtastic/wismesh-b1/quickstart/
title: Meshtastic WisMesh Board ONE Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your Meshtastic WisMesh Board ONE. For a full documentation, check the documentation of Meshtastic.org.
image: "https://images.docs.rakwireless.com/meshtastic/wismesh-board-one.png"
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

# WisMesh Board ONE Quick Start Guide

The WisMesh Board ONE is available in both as a development board and a ready-to-use device with an enclosure, built-in 1000 mAh battery, and an SMA connector for LoRa antenna. Its BLE antenna is integrated on the board to save space.

This guide covers the basics for the RAKwireless Meshtastic devices that are not covered by the [Meshtastic documentation](https://meshtastic.org/docs/introduction).

For detailed instructions how to configure the devices for the Meshtastic network, follow the [Meshtastic Getting Started](https://meshtastic.org/docs/getting-started) guide.

You can also check the Meshtastic Basic Device Setup Guide:.

<div class="flex items-center flex-col align-center gap-2">
  [ Meshtastic Basic Device Setup ](https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/)
</div>

----

:::tip NOTE
To ensure you are running the latest version of the Meshtastic firmware, it is advised to download the latest [Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is autodetected. The WisMesh Board ONE works with the stock firmware.

- For the WisMesh Board ONE: use **`firmware-rak4631-w.x.yy.zzzzzzz.uf2`**
- For the WisMesh Board ONE:  _**DO NOT USE**_ **`firmware-rak4631_eink-w.x.yy.zzzzzzz.uf2`**
:::

## Prerequisite

Before going through each and every step on using WisMesh Board ONE, make sure to prepare the necessary items listed below:

### Hardware

- [WisMesh Board ONE](https://store.rakwireless.com/products/wismesh-board-one?variant=44413994434758&utm_medium=Document&utm_campaign=BuyFromStore)
- USB Cable

### Software

The WisBlock Core module of the WisMesh Board ONE comes pre-flashed with the Meshtastic firmware.

However, to connect the device to the Meshtastic network, you will have to configure it. Listed below are several applications for the configuration:
- [Android App](https://meshtastic.org/docs/category/android-app)
- [Apple App](https://meshtastic.org/docs/category/apple-apps)
- [Web Client](https://meshtastic.org/docs/software/web-client)
- [Python CLI](https://meshtastic.org/docs/software/python/cli)

:::tip NOTE
Make sure that you have installed one of these applications, as they are required for the configuration of the Meshtastic network.
::::

## Product Configuration

### Hardware Setup

The WisMesh Board ONE comes in two variants:
- Fully assembled with an internal battery and a battery disconnect switch. However, it is recommended to fully recharge the battery before using the device on. It supports Li-ion batteries and 5 V (e.g. from solar panel) supply.
- As a board without enclosure. In addition to the battery and solar panel connector, it has options to add other modules through the pin headers that provide access to all GPIOs and system buses.

:::tip NOTE
The battery can only be charged when the switch is _**ON**_.
:::

> **Image:** WisMesh Board ONE Top

WisMesh Board ONE also includes one WisBlock Sensor Slot as shown in **Figure 2**.

> **Image:** WisMesh Board ONE Bottom

The WisMesh Board ONE is designed as a special Base Board. Technical details of the WisMesh Board ONE Board can be found in the [WisMesh Board ONE Datasheet](https://docs.rakwireless.com/product-categories/meshtastic/wismesh-b1/datasheet/).

#### Battery Connector and Solar Panel (5 V) Connector

The WisMesh Board ONE has an internal connector for a Li-ion battery. Double-check the battery cable polarity when replacing. The matching connector for the battery wires is a [JST PHR-2 2 mm pitch female](https://www.jst-mfg.com/product/detail_e.php?series=199).

:::tip NOTE
Depending on the regional requirements, the WisMesh Board ONE can have a 2-pin (US) or a 3-pin (EU) battery connector. If the 3-pin connector is present on the board, only batteries with an integrated NTC temperature sensor and a 3-wire cable can be connected and charged.
:::

WisMesh Board ONE also has an internal connector for 5 V supply or solar panel connection. When using this connector, double-check the polarity of the supply cable.

The matching connector for the solar panel wires is an [JST ZHR-2 1.5 mm pitch female](https://www.jst-mfg.com/product/detail_e.php?series=287).

> **Image:** WisMesh Board ONE Battery and Solar Panel connector polarity

#### Recharge the Battery

To recharge the device, plug a USB-C cable into the device and connected it to a 5 V/2 A USB wall charger. Recharging the battery via a USB port on your computer is not recommended due to the potential low current output.

#### Antenna

- The BLE antenna is integrated on the PCB of the WisMesh Board ONE.
- The LoRa antenna is connected through an IPEX connector. It can be a PCB antenna inside the enclosure or an SMA antenna connector to attach an external antenna.

#### Assembling and Disassembling of WisMesh Board ONE

If you want to add more WisBlock modules, simply open the device and plug the modules into their sensor slots.

<!--
##### Disassembling

1. Unscrew the four screws on the corners of the enclosure with a screwdriver.

> **Image:** WisMesh Board ONE Disassembly Enclosure Screws

2. Open the enclosure carefully, as there are battery cables between the top and bottom part, do not use force to pull the cables. Then separate three IPEX connectors from PCBA.

> **Image:** WisMesh Board ONE Disassembly Opening - Disconnect antenna cables

3. Unscrew four screws that hold the Base Board in the enclosure. Then you can remove the Base Board from the enclosure

> **Image:** WisMesh Board ONE Disassembly Base Board removal

4. Separate the battery cable from the Base Board.

> **Image:** WisMesh Board ONE Disassembly Battery disconnect

##### Assembling

1. Plug the battery cable into the Base Board.

> **Image:** WisMesh Board ONE Assembly Battery connection

2. Put the Base Board into the enclosure and fix it with four screws.

> **Image:** WisMesh Board ONE Assembly Mount Base Board

3. Plug the IPEX connectors on the sockets on the Base Board. Make sure to connect each antenna to the correct socket, and then close the enclosure.

> **Image:** WisMesh Board ONE Assembly Connect antennas

4. Put the four nuts into the slots on the bottom of the enclosure, then fix the screws.

> **Image:** WisMesh Board ONE Assembly Fix enclosure

-->

### Software Setup

To ensure you are running the latest version of the Meshtastic firmware, it is advised to download the latest [Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is autodetected. The WisMesh Board ONE is using the stock firmware.

- For the WisMesh Board ONE: use **`firmware-rak4631-w.x.yy.zzzzzzz.uf2`**
- For the WisMesh Board ONE:  _**DO NOT USE**_ **`firmware-rak4631_eink-w.x.yy.zzzzzzz.uf2`**

**Flashing the WisMesh Board ONE Firmware:**

The WisMesh Board ONE comes pre-flashed with the Meshtastic firmware. If problems occur, update the Meshtastic firmware to the latest version.

- [Guide to flash nRF52 devices](https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52).

To set up the WisMesh Board ONE for the Meshtastic network, follow the [configuration guide](https://meshtastic.org/docs/configuration/) in the Meshtastic documentation.

