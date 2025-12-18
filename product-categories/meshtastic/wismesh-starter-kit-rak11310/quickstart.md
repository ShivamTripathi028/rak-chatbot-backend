---
slug: /product-categories/meshtastic/wismesh-starter-kit-rak11310/quickstart/
title: WisMesh RP2040 Starter Kit Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your WisMesh RP2040 Starter Kit. For a full documentation, check the documentation of Meshtastic.org.
image: "https://images.docs.rakwireless.com/meshtastic/wismesh-rp2040-starter-kit.png"
keywords:
  - RAK11310
  - wisblock
  - Meshtastic
  - Raspberry
  - RP2040
  - Semtech
  - SX1262
sidebar_label: Quick Start Guide
download: true
---

# WisMesh RP2040 Starter Kit Quick Start Guide

WisMesh RP2040 Starter Kit is a versatile DIY Kit, ideal for DIY enthusiasts. Ideal for users looking for a hassle-free Meshtastic node.

This guide covers the basics for the RAKwireless Meshtastic devices that are not covered by the [Meshtastic documentation](https://meshtastic.org/docs/introduction).

For detailed instructions how to configure the devices for the Meshtastic network, follow the [Meshtastic Getting Started](https://meshtastic.org/docs/getting-started) guide.

You can also check the Meshtastic Basic Device Setup Guide:.

<div class="flex items-center flex-col align-center gap-2">
  [Meshtastic Basic Device Setup](https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/)
</div>

----

:::tip NOTE
To ensure you are running the latest version of the Meshtastic firmware, it is advised to download the latest [Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is autodetected. This device works with the stock firmware.

- All the base boards with RAK11310: **`firmware-rak11310-w.x.yy.zzzzzzz.uf2`**
:::

## Prerequisite

Before going through each and every step on using WisMesh RP2040 Starter Kit, make sure to prepare the necessary items listed below:

### Hardware

- [WisMesh RP2040 Starter Kit](https://store.rakwireless.com/products/wisblock-rp2040-starter-kit-for-meshtastic)
- USB Cable
- [Li-ion/LiPo battery](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore) (optional)
- [Solar charger](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore) (optional)

### Software

The WisBlock Core module of the WisMesh RP2040 Starter Kit comes pre-flashed with the Meshtastic firmware.

However, to connect the device to the Meshtastic network, you will have to configure it. There are several applications for the configuration:
- [Android App](https://meshtastic.org/docs/category/android-app)
- [Apple App](https://meshtastic.org/docs/category/apple-apps)
- [Web Client](https://meshtastic.org/docs/software/web-client)
- [Python CLI](https://meshtastic.org/docs/software/python/cli)

:::tip NOTE
Make sure that you have installed one of these applications, as they are required for the configuration of the Meshtastic network.
::::

## Product Configuration

### Hardware Setup

#### RAK11310 to WisBlock Base

The WisMesh RP2040 Starter Kit comes with the RAK11310 module pre-assembled on the WisBlock Base Board. The WisBlock Base provides a USB connection for programming the RAK11310. Additionally, it provides a power source and various interfaces to RAK11310, allowing it to connect to other WisBlock modules via different module slots.

In case you need to change the RAK11310 or install additional modules, this guide illustrates how the RAK11310 can be connected to RAK19007 WisBlock Base, as shown in **Figure 1**.

> **Image:** RAK11310 Connection to WisBlock Base RAK19007

:::tip NOTE
- Assembly of the RAK11310 on other Base Boards is performed in the same way.
- Assembly guides for other modules can be found in their **Quick Start Guides**.
:::

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

**Figure 2** shows how to mount the RAK11310 module on top of a WisBlock Base board (RAK19007). Follow carefully the procedure defined in [WisBlock module assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard) to secure the connection safely. Once attached, carefully fix the module with one or more pieces of M1.2 x 3 mm screws depending on the module.

> **Image:** RAK11310 Mounting Sketch

##### Disassembling

The procedure in disassembling any type of WisBlock modules is the same.

1. Start by removing the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

> **Image:** Detaching silkscreen on the WisBlock module

3. Apply force to the module at the position of the connector, as shown in **Figure 3,** to detach the module from the baseboard.

> **Image:** Applying even forces on the proper location of a WisBlock module

#### LoRa and BLE Antenna

Another important part component of WisMesh RP2040 Starter Kit are the antennas.

For LoRa, two antennas are included.
- 2 dBi rubber antenna: Comes with a SMA connector and an IPEX-to-SMA pigtail cable.

> **Image:** LoRa Antenna

- LoRa PCB antenna: Can be connected directly to the RAK11310

> **Image:** LoRa PCB Antenna

:::tip NOTE
- Make sure that the antenna is properly connected to have a good LoRa signal. Do not power the module without an antenna connected to the IPEX connector to avoid damage to the RF section of the chip.
- Detailed information about the RAK11310 LoRa antenna can be found on the [863-870 MHz antenna datasheet](https://downloads.rakwireless.com/LoRa/WisBlock/Accessories/RAK_PCB_Antenna_for_LoRa_863-870_MHz_(RAKARB04)_Datasheet.pdf).
:::

:::warning
When using the LoRa transceivers, make sure that an antenna is always connected. Using these transceivers without an antenna can damage the system. Make sure to fix the module with the screws to ensure a proper function.
:::

### Software Setup

To ensure you are running the latest version of the Meshtastic firmware, it is advised to download the latest [Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is autodetected. This device works with the stock firmware.

- All the base boards with RAK11310: **`firmware-rak11310-w.x.yy.zzzzzzz.uf2`**

**Flashing the Meshtastic Starter Kit Firmware:**

The Meshtastic Starter Kit comes pre-flashed with the Meshtastic firmware. If problems occur, update the Meshtastic firmware to the latest version.

- [Guide to flash RP2040 devices](https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52).

To set up the WisMesh RP2040 Starter Kit for the Meshtastic network, follow the [configuration guide](https://meshtastic.org/docs/configuration/) in the Meshtastic documentation.

### RAK11310 and WisBlock Base Boards

Detailed information and datasheets for the different modules can be found in the following documentations:

- [RAK11310 Core Module](https://docs.rakwireless.com/product-categories/wisblock/rak11310/overview/)
- [RAK19007 Base Board](https://docs.rakwireless.com/product-categories/wisblock/rak19007/overview/)
- [RAK19003 Base Board](https://docs.rakwireless.com/product-categories/wisblock/rak19003/overview/)
- [RAK19001 Base Board](https://docs.rakwireless.com/product-categories/wisblock/rak19001/overview/)
- [RAK1921 OLED Display](https://docs.rakwireless.com/product-categories/wisblock/rak1921/overview/)
- [RAK12500 GNSS Location Module](https://docs.rakwireless.com/product-categories/wisblock/rak12500/overview/)
- [RAK1904 Acceleration Sensor](https://docs.rakwireless.com/product-categories/wisblock/rak1904/overview/)
- [RAK13800 Ethernet Module](https://docs.rakwireless.com/product-categories/wisblock/rak13800/overview/)
- [RAK19018 Ethernet PoE Module](https://docs.rakwireless.com/product-categories/wisblock/rak19018/overview/)

