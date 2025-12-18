---
title: Meshtastic Starter Kit Quick Start Guide
description: Step-by-step instructions to set up your Meshtastic WisMesh Starter Kit, including hardware assembly, firmware updates, and network configuration for seamless DIY mesh networking.
image: "https://images.docs.rakwireless.com/meshtastic/wismesh-starter-kit.png"
keywords:
    - RAK4631
    - Meshtastic
    - Meshtastic device
    - Meshtastic kits
    - LoRa mesh
    - SX1262
sidebar_label: Quick Start Guide
---

# Meshtastic WisMesh Starter Kit Quick Start Guide

WisMesh Starter Kit is a versatile DIY Kit, ideal for DIY enthusiasts. Ideal for users looking for a hassle-free Meshtastic node.

This guide covers the basics for the Meshtastic Starter Kit that are not handled by the [Meshtastic documentation](https://meshtastic.org/docs/introduction).

For detailed instructions how to configure the devices for the Meshtastic network, follow the [Meshtastic Getting Started](https://meshtastic.org/docs/getting-started) guide.

You can also check the Meshtastic Basic Device Setup Guide:.

<div class="flex items-center flex-col align-center gap-2">
  [ Meshtastic Basic Device Setup ](https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/)
</div>

----

:::tip NOTE
To be sure to run the latest version of the Meshtastic firmware, we advice you to download the [latest Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is autodetected. There's a special firmware if you have the [RAK14000 WisBlock E-Ink Display](https://store.rakwireless.com/products/wisblock-epd-module-rak14000) connected. All other use cases are covered in the stock firmware.

- All the base boards with RAK4631 - **`firmware-rak4631-w.x.yy.zzzzzzz.uf2`**
- RAK4631 with RAK14000 - **`firmware-rak4631_eink-w.x.yy.zzzzzzz.uf2`**
:::

## Prerequisite

Before going through each and every step on using Meshtastic Starter Kit, make sure to prepare the necessary items listed below:

### Hardware

- [RAK4631 WisBlock Core LPWAN Module](https://store.rakwireless.com/products/rak4631-lpwan-node?utm_source=RAK4631WisBlockLPWANModule&utm_medium=Document&utm_campaign=BuyFromStore)
- [RAK19007 WisBlock Base](https://store.rakwireless.com/collections/wisblock-base)
- [Your choice of WisBlock Modules](https://store.rakwireless.com/pages/wisblock)
- [USB Cable]()
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

### Software

The WisBlock Core module of the Meshtastic Starter Kit comes pre-flashed with the Meshtastic firmware.

However to connect the device to the Meshtastic network you will have to configure it. There are several applications for the configuration:
- [Android App](https://meshtastic.org/docs/category/android-app)
- [Apple App](https://meshtastic.org/docs/category/apple-apps)
- [Web Client](https://meshtastic.org/docs/software/web-client)
- [Python CLI](https://meshtastic.org/docs/software/python/cli)

:::tip NOTE
Make sure that you have installed one of these applications, as they are required for the configuration of the Meshtastic network.
::::

## Product Configuration

### Hardware Setup

#### RAK4631 to WisBlock Base

The Meshtastic Starter Kit comes with the RAK4631 module already assembled on the WisBlock Base board. The WisBlock Base provides a USB connection for programming the RAK4631. It also provides a power source and various interfaces to RAK4631 so that it can be connected to other WisBlock modules via different module slots.

In case you need to change the RAK4631 or install additional modules, this guide illustrates how the RAK4631 can be connected to RAK19007 WisBlock Base, as shown in **Figure 1**.

> **Image:** RAK4631 Connection to WisBlock Base RAK5005-O

:::tip NOTE
Assembly of the RAK4631 on other Base Boards is performed in the same way.
Assembly guides for other modules can be found in the Quick Start Guides of these modules.
:::

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

**Figure 2** shows how to mount the RAK4631 module on top of a WisBlock Base board (RAK19007). Follow carefully the procedure defined in [WisBlock module assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard) in order to secure the connection safely. Once attached, carefully fix the module with one or more pieces of M1.2 x 3 mm screws depending on the module.

> **Image:** RAK4631 Mounting Sketch

##### Disassembling

The procedure in disassembling any type of WisBlock modules is the same.

1. Start by removing the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

> **Image:** Detaching silkscreen on the WisBlock module

3. Apply force to the module at the position of the connector, as shown in **Figure 3,** to detach the module from the baseboard.

> **Image:** Applying even forces on the proper location of a WisBlock module

#### LoRa and BLE Antenna

Another important part component of Meshtastic Starter kit are the antennas.

For LoRa, two antennas are included.
1. A 2 dBi rubber antenna with a SMA connector and an IPEX-to-SMA pigtail cable.

> **Image:** LoRa Antenna

:::tip NOTE
Detailed information about the 2 dBi rubber antenna can be found on the [antenna datasheet](https://downloads.rakwireless.com/Accessories/Antenna/Rubber-Antenna/2701C042_Sunnyway_LoRa%20Antenna_SWE047-ZT_20240411.pdf).
:::

2. A LoRa PCB antenna that can be connected directly to the RAK4631

> **Image:** LoRa PCB Antenna

3. A BLE PCB antenna that can be connected directly to the RAK4631

> **Image:** BLE PCB Antenna

You need to ensure that the antenna is properly connected to have a good LoRa signal. Do not power the module without an antenna connected to the IPEX connector to avoid damage to the RF section of the chip.

RAK4631 has a label on its sticker where to connect the antennas, as shown in **Figure 9**.

> **Image:** RAK4631 Antenna Label

:::tip NOTE
Detailed information about the RAK4631 BLE and LoRa antenna can be found on the [863-870 MHz antenna datasheet](https://downloads.rakwireless.com/LoRa/WisBlock/Accessories/RAK_PCB_Antenna_for_LoRa_863-870_MHz_(RAKARB04)_Datasheet.pdf) or the [902-928 MHz antenna datasheet](https://downloads.rakwireless.com/LoRa/WisBlock/Accessories/RAK_PCB_Antenna_for_LoRa_902-928_MHz_(RAKARB03)_Datasheet.pdf).
:::

:::warning
When using the LoRa or Bluetooth Low Energy transceivers, make sure that an antenna is always connected. Using these transceivers without an antenna can damage the system. Make sure to fix the module with the screws to ensure a proper function.
:::

### Software Setup

To be sure to run the latest version of the Meshtastic firmware, we advice you to download the latest [Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is autodetected. There's a special firmware if you have the [RAK14000 WisBlock E-Ink Display](https://store.rakwireless.com/products/wisblock-epd-module-rak14000) connected. All other use cases are covered in the stock firmware.

- All the base boards with RAK4631 - **`firmware-rak4631-w.x.yy.zzzzzzz.uf2`**
- RAK4631 with RAK14000 - **`firmware-rak4631_eink-w.x.yy.zzzzzzz.uf2`**

**Flashing the Meshtastic Starter Kit firmware:**

The Meshtastic Starter Kits come pre-flashed with the Meshtastic firmware. If you encounter problems, update the Meshtastic firmware to the latest version.

- [Guide to flash nRF52 devices](https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52). (link goes to Meshtastic.org)

For the setup of the Meshtastic Starter Kit for the Meshtastic network, follow the [configuration guide](https://meshtastic.org/docs/configuration) in the Meshtastic documentation.

### RAK4631 and WisBlock Base Boards

Detailed information and datasheets can be found in the documentation for the different modules:

- [RAK4631 Core Module](https://docs.rakwireless.com/product-categories/wisblock/rak4631)
- [RAK19007 Base Board](https://docs.rakwireless.com/product-categories/wisblock/rak19007)
- [RAK19003 Base Board](https://docs.rakwireless.com/product-categories/wisblock/rak19003)
- [RAK19001 Base Board](https://docs.rakwireless.com/product-categories/wisblock/rak19001)
- [RAK1921 OLED Display](https://docs.rakwireless.com/product-categories/wisblock/rak1921)
- [RAK12500 GNSS Location Module](https://docs.rakwireless.com/product-categories/wisblock/rak12500)
- [RAK1904 Acceleration Sensor](https://docs.rakwireless.com/product-categories/wisblock/rak1904)
- [RAK13800 Ethernet Module](https://docs.rakwireless.com/product-categories/wisblock/rak13800)
- [RAK19018 Ethernet PoE Module](https://docs.rakwireless.com/product-categories/wisblock/rak19018)

