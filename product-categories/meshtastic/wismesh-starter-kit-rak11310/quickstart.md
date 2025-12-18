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

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'


# WisMesh RP2040 Starter Kit Quick Start Guide

WisMesh RP2040 Starter Kit is a versatile DIY Kit, ideal for DIY enthusiasts. Ideal for users looking for a hassle-free Meshtastic node.

This guide covers the basics for the RAKwireless Meshtastic devices that are not covered by the <a href="https://meshtastic.org/docs/introduction" target="_blank">Meshtastic documentation</a>.

For detailed instructions how to configure the devices for the Meshtastic network, follow the <a href="https://meshtastic.org/docs/getting-started" target="_blank">Meshtastic Getting Started</a> guide.

You can also check the Meshtastic Basic Device Setup Guide:.

<div class="flex items-center flex-col align-center gap-2">
  <a target="_blank" href="https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/" class="no-underline text-white bg-rak-primary px-[15px] py-[5px] rounded-[20px] border-solid border hover:no-underline hover:text-rak-primary hover:bg-white  hover:border-rak-primary no-icon">Meshtastic Basic Device Setup</a>
</div>

----

:::tip NOTE
To ensure you are running the latest version of the Meshtastic firmware, it is advised to download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is autodetected. This device works with the stock firmware.

- All the base boards with RAK11310: **`firmware-rak11310-w.x.yy.zzzzzzz.uf2`**
:::

## Prerequisite

Before going through each and every step on using WisMesh RP2040 Starter Kit, make sure to prepare the necessary items listed below:

### Hardware

- <a href="https://store.rakwireless.com/products/wisblock-rp2040-starter-kit-for-meshtastic" target="_blank">WisMesh RP2040 Starter Kit</a>
- USB Cable
- <a href="https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">Li-ion/LiPo battery</a> (optional)
- <a href="https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">Solar charger</a> (optional)

### Software

The WisBlock Core module of the WisMesh RP2040 Starter Kit comes pre-flashed with the Meshtastic firmware.

However, to connect the device to the Meshtastic network, you will have to configure it. There are several applications for the configuration:
- <a href="https://meshtastic.org/docs/category/android-app" target="_blank">Android App</a>
- <a href="https://meshtastic.org/docs/category/apple-apps" target="_blank">Apple App</a>
- <a href="https://meshtastic.org/docs/software/web-client" target="_blank">Web Client</a>
- <a href="https://meshtastic.org/docs/software/python/cli" target="_blank">Python CLI</a>

:::tip NOTE
Make sure that you have installed one of these applications, as they are required for the configuration of the Meshtastic network.
::::

## Product Configuration

### Hardware Setup

#### RAK11310 to WisBlock Base

The WisMesh RP2040 Starter Kit comes with the RAK11310 module pre-assembled on the WisBlock Base Board. The WisBlock Base provides a USB connection for programming the RAK11310. Additionally, it provides a power source and various interfaces to RAK11310, allowing it to connect to other WisBlock modules via different module slots.

In case you need to change the RAK11310 or install additional modules, this guide illustrates how the RAK11310 can be connected to RAK19007 WisBlock Base, as shown in **Figure 1**.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wisblock/rak4631/quickstart/rak5005-connect.png"
  width="80%"
  caption="RAK11310 Connection to WisBlock Base RAK19007"
/>

:::tip NOTE
- Assembly of the RAK11310 on other Base Boards is performed in the same way.
- Assembly guides for other modules can be found in their **Quick Start Guides**.
:::


#### Assembling and Disassembling of WisBlock Modules

##### Assembling

**Figure 2** shows how to mount the RAK11310 module on top of a WisBlock Base board (RAK19007). Follow carefully the procedure defined in <a href="https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard" target="_blank">WisBlock module assembly/disassembly instructions</a> to secure the connection safely. Once attached, carefully fix the module with one or more pieces of M1.2 x 3&nbsp;mm screws depending on the module.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wisblock/rak4631/datasheet/mounting-sketch.png"
  width="50%"
  caption="RAK11310 Mounting Sketch"
/>

##### Disassembling

The procedure in disassembling any type of WisBlock modules is the same.

1. Start by removing the screws.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wisblock/rak1910/quickstart/16.removing-screws.png"
  width="70%"
  caption="Removing screws from the WisBlock module"
/>

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wisblock/rak1910/quickstart/17.detaching-silkscreen.png"
  width="70%"
  caption="Detaching silkscreen on the WisBlock module"
/>

3. Apply force to the module at the position of the connector, as shown in **Figure 3,** to detach the module from the baseboard.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wisblock/rak1910/quickstart/18.detaching-module.png"
  width="70%"
  caption="Applying even forces on the proper location of a WisBlock module"
/>

#### LoRa and BLE Antenna

Another important part component of WisMesh RP2040 Starter Kit are the antennas.

For LoRa, two antennas are included.
- 2&nbsp;dBi rubber antenna: Comes with a SMA connector and an IPEX-to-SMA pigtail cable.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/meshtastic/rubber-antenna.png"
  width="30%"
  caption="LoRa Antenna"
/>

- LoRa PCB antenna: Can be connected directly to the RAK11310

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/meshtastic/lora-pcb-antenna.png"
  width="40%"
  caption="LoRa PCB Antenna"
/>

:::tip NOTE
- Make sure that the antenna is properly connected to have a good LoRa signal. Do not power the module without an antenna connected to the IPEX connector to avoid damage to the RF section of the chip.
- Detailed information about the RAK11310 LoRa antenna can be found on the <a href="https://downloads.rakwireless.com/LoRa/WisBlock/Accessories/RAK_PCB_Antenna_for_LoRa_863-870_MHz_(RAKARB04)_Datasheet.pdf" target="_blank">863-870&nbsp;MHz antenna datasheet</a>.
:::

:::warning
When using the LoRa transceivers, make sure that an antenna is always connected. Using these transceivers without an antenna can damage the system. Make sure to fix the module with the screws to ensure a proper function.
:::

### Software Setup

To ensure you are running the latest version of the Meshtastic firmware, it is advised to download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is autodetected. This device works with the stock firmware.

- All the base boards with RAK11310: **`firmware-rak11310-w.x.yy.zzzzzzz.uf2`**

<b>Flashing the Meshtastic Starter Kit Firmware:</b>

The Meshtastic Starter Kit comes pre-flashed with the Meshtastic firmware. If problems occur, update the Meshtastic firmware to the latest version.

- <a href="https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52" target="_blank">Guide to flash RP2040 devices</a>.

To set up the WisMesh RP2040 Starter Kit for the Meshtastic network, follow the <a href="https://meshtastic.org/docs/configuration/" target="_blank">configuration guide</a> in the Meshtastic documentation.

### RAK11310 and WisBlock Base Boards

Detailed information and datasheets for the different modules can be found in the following documentations:

- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak11310/overview/" target="_blank">RAK11310 Core Module</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak19007/overview/" target="_blank">RAK19007 Base Board</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak19003/overview/" target="_blank">RAK19003 Base Board</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak19001/overview/" target="_blank">RAK19001 Base Board</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak1921/overview/" target="_blank">RAK1921 OLED Display</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak12500/overview/" target="_blank">RAK12500 GNSS Location Module</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak1904/overview/" target="_blank">RAK1904 Acceleration Sensor</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak13800/overview/" target="_blank">RAK13800 Ethernet Module</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak19018/overview/" target="_blank">RAK19018 Ethernet PoE Module</a>


<RkBottomNav/>