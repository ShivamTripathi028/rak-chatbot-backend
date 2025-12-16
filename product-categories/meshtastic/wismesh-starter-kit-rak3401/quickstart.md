---
slug: /product-categories/meshtastic/wismesh-starter-kit-rak3401/quickstart/
title: Meshtastic Booster Starter Kit Quick Start Guide | RAK3401 LoRa Setup
description: Step-by-step guide to set up your Meshtastic Booster Starter Kit using RAK3401 and RAK13302. Learn firmware flashing, antenna setup, and LoRa mesh configuration.
image: "https://images.docs.rakwireless.com/meshtastic/wismesh-starter-kit-rak3401.png"
keywords:
  - Meshtastic Booster Starter Kit Quick Start
  - RAK3401 Setup Guide
  - RAK13302 LoRa Module Configuration
  - Flash nRF52 Firmware
  - Meshtastic LoRa Mesh Setup
  - WisBlock Meshtastic Device
  - LoRa Antenna Setup
  - DIY Meshtastic Node Guide
sidebar_label: Quick Start Guide
download: true
date: 2025-10-01
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'


# Meshtastic Booster Starter Kit Quick Start Guide

WisMesh Booster Starter Kit is a versatile DIY kit, ideal for DIY enthusiasts who wants a hassle-free Meshtastic node. This guide covers the basics for the Meshtastic Starter Kit that are not handled by the <a href="https://meshtastic.org/docs/introduction" target="_blank">Meshtastic documentation</a>.

For detailed instructions how to configure the devices for the Meshtastic network, follow the <a href="https://meshtastic.org/docs/getting-started" target="_blank">Meshtastic Getting Started</a> guide. You can also check the Meshtastic Basic Device Setup Guide:

<div class="flex items-center flex-col align-center gap-2">
  <a target="_blank" href="https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/?intsource=docs_center&intmedium=organic&intcampaign=meshtastic_booster_starter_documentation_kit_quick_start_guide_page&intterm=meshtastic_basic_device_setup&intcontent=documentation_link" class="no-underline text-white bg-rak-primary px-[15px] py-[5px] rounded-[20px] border-solid border hover:no-underline hover:text-rak-primary hover:bg-white  hover:border-rak-primary no-icon" > Meshtastic Basic Device Setup </a>
</div>

:::warning IMPORTANT
Due to the high power consumption during the 1&nbsp;W LoRa transmission, the device has to be powered either by a battery or by an external 5&nbsp;V supply to work correctly.
:::

----

:::tip NOTE
To ensure you are running the latest version of the Meshtastic firmware, download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

- All base boards with RAK3401 and the RAK13302 1&nbsp;W (30&nbsp;dBm) LoRa module use: **`firmware-rak3401-w.x.yy.zzzzzzz.uf2`**
:::

## Prerequisite

Before going through each and every step on using Meshtastic Starter Kit, make sure to prepare the necessary items listed below:

### Hardware

Meshtastic Basic Device Setup

### Software

The WisBlock Core module of the Meshtastic Starter Kit comes pre-flashed with the Meshtastic firmware. However, to connect the device to the Meshtastic network, it must first be configured using one of several available applications:
- <a href="https://meshtastic.org/docs/category/android-app" target="_blank">Android App</a>
- <a href="https://meshtastic.org/docs/category/apple-apps" target="_blank">Apple App</a>
- <a href="https://meshtastic.org/docs/software/web-client" target="_blank">Web Client</a>
- <a href="https://meshtastic.org/docs/software/python/cli" target="_blank">Python CLI</a>

:::tip NOTE
Make sure that you have installed one of these applications, as they are required for the configuration of the Meshtastic network.
::::

## Product Configuration

### Hardware Setup

#### RAK3401 to WisBlock Base

The Meshtastic Booster Starter Kit comes with the RAK3401 module already assembled on the WisBlock Base board. The WisBlock Base provides a USB connection for programming the RAK4631. It also provides a power source and various interfaces to RAK4631 so that it can be connected to other WisBlock modules via different module slots.

In case you need to change the RAK3401 or install additional modules, this guide illustrates how the RAK3401 can be connected to RAK5005-O WisBlock Base, as shown in **Figure 1**.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/rak3401-connection-to-wisblock-base-rak5005-o.png"
  width="80%"
  caption="RAK3401 Connection to WisBlock Base RAK5005-O"
/>

:::tip NOTE
- The RAK3401 can be assembled on other base boards in the same way.
- Assembly guides for additional modules are available in their respective Quick Start Guides.
:::


#### Assembling and Disassembling of WisBlock Modules

##### Assembling

**Figure 2** shows how to mount the RAK3401 module onto a WisBlock Base board (RAK5005-O). Follow the steps in the <a href="https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard?utm_source=docs_center&utm_medium=organic&utm_campaign=meshtastic_booster_starter_documentation_kit_quick_start_guide_page&utm_term=wisblock_module_assembly/disassembly_instructions&utm_content=learn_link" target="_blank">WisBlock module assembly/disassembly guide</a> to ensure a secure connection. Once mounted, fasten the module with one or more M1.2x3&nbsp;mm screws, depending on the module type.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/rak3401-mounting-sketch.png"
  width="50%"
  caption="RAK3401 Mounting Sketch"
/>

##### Disassembling

The procedure in disassembling any type of WisBlock modules is the same.

1. Start by removing the screws.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/removing-screws-from-the-wisblock-module.png"
  width="70%"
  caption="Removing screws from the WisBlock module"
/>

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/detaching-silkscreen-on-the-wisblock-module.png"
  width="70%"
  caption="Detaching silkscreen on the WisBlock module"
/>

3. Apply force to the module at the position of the connector, as shown in **Figure 5**, to detach the module from the baseboard.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/applying-even-forces-on-the-proper-location-of-a-wisblock-module.png"
  width="70%"
  caption="Applying even forces on the proper location of a WisBlock module"
/>

#### LoRa and BLE Antenna

Antennas are an essential part of the Meshtastic Starter Kit. The kit includes the following:

1. **LoRa Rubber Antenna**: A 2&nbsp;dBi rubber antenna with a SMA connector and an IPEX-to-SMA pigtail cable.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/lora-rubber-antenna.png"
  width="30%"
  caption="LoRa Rubber Antenna"
/>

:::tip NOTE
Detailed information about the 2&nbsp;dBi rubber antennas can be found on the <a href="https://downloads.rakwireless.com/Accessories/Antenna/Rubber-Antenna/2701C042_Sunnyway_LoRa%20Antenna_SWE047-ZT_20240411.pdf" target="_target">antenna datasheet</a>.
:::

2. **LoRa PCB Antenna**: A compact PCB antenna for LoRa.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/lora-pcb-antenna.png"
  width="40%"
  caption="LoRa PCB Antenna"
/>

:::tip NOTE
- Connect the LoRa antenna to the IPEX connector on the RAK13302 LoRa transceiver module.
- Detailed information about the LoRa antennas can be found in the <a href="https://downloads.rakwireless.com/LoRa/WisBlock/Accessories/RAK_PCB_Antenna_for_LoRa_863-870_MHz_(RAKARB04)_Datasheet.pdf" target="_blank">863-870&nbsp;MHz antenna datasheet</a> or the <a href="https://downloads.rakwireless.com/LoRa/WisBlock/Accessories/RAK_PCB_Antenna_for_LoRa_902-928_MHz_(RAKARB03)_Datasheet.pdf" target="_blank">902-928&nbsp;MHz antenna datasheet</a>.
:::

3. **BLE PCB Antenna**: A PCB antenna for Bluetooth Low Energy that connects directly to the RAK3401.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/ble-pcb-antenna.png"
  width="40%"
  caption="BLE PCB Antenna"
/>


:::warning
- Never power the module without an antenna connected to the IPEX connector. Doing so may damage the RF section of the chip.
- Always ensure the correct antenna is attached when using LoRa or Bluetooth Low Energy transceivers.
:::

#### Power Supply Setup

Due to the high power consumption of the 1&nbsp;W transceiver during the LoRa transmission, the device has to be powered either by battery or by an external 5&nbsp;V supply.

Depending on the selected power supply, make sure the jumper on the RAK13302 is set in the correct position:

The 3-pin jumper header is to select the supply source for the booster chip.

|     Jumper Position     | Supply Source                           |
|:-----------------------:|-----------------------------------------|
| IN_5&nbsp;V to 5&nbsp;V | Supply from WisBlock Base Board Battery |
| EX_5&nbsp;V to 5&nbsp;V | Supply from Jx connector                |

:::tip NOTE
If the supply is through EX_5&nbsp;V, the whole WisBlock Base Board can be supplied through this source.
:::

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/rak13302-5-v-supply-selection.png"
  width="80%"
  caption="RAK13302 5&nbsp;V supply selection"
/>

**External power supply cable connections:**

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/rak13302-5-v-supply-cable.png"
  width="80%"
  caption="RAK13302 5&nbsp;V supply cable"
/>

### Software Setup

To ensure you are running the latest version of the Meshtastic firmware, download the latest <a href="https://meshtastic.org/downloads" target="_blank">Meshtastic firmware</a> and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

- All the base boards with RAK3401 - **`firmware-rak3401-w.x.yy.zzzzzzz.uf2`**

<b>Flashing the Meshtastic Starter Kit firmware:</b>

The Meshtastic Starter Kits come pre-flashed with the Meshtastic firmware. If you encounter problems, update the Meshtastic firmware to the latest version.

- <a href="https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52" target="_blank">Guide to flash nRF52 devices</a>. (link goes to Meshtastic.org)

For the setup of the Meshtastic Starter Kit for the Meshtastic network, follow the <a href="https://meshtastic.org/docs/configuration" target="_blank">configuration guide</a> in the Meshtastic documentation.

### RAK3401 and WisBlock Base Boards

Detailed information can be found in the documentation for the different modules:

- <a href="https://docs.rakwireless.com/product-categories/meshtastic/wismesh-starter-kit-rak3401/overview/?intsource=docs_center&intmedium=organic&intcampaign=meshtastic_booster_starter_documentation_kit_quick_start_guide_page&intterm=rak3401_core_module&intcontent=documentation_link" target="_blank">RAK3401 Core Module</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak19007/overview/?intsource=docs_center&intmedium=organic&intcampaign=meshtastic_booster_starter_documentation_kit_quick_start_guide_page&intterm=rak19007_base_board&intcontent=documentation_link" target="_blank">RAK19007 Base Board</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak19003/overview/?intsource=docs_center&intmedium=organic&intcampaign=meshtastic_booster_starter_documentation_kit_quick_start_guide_page&intterm=rak19003_base_board&intcontent=documentation_link" target="_blank">RAK19003 Base Board</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak19001/overview/?intsource=docs_center&intmedium=organic&intcampaign=meshtastic_booster_starter_documentation_kit_quick_start_guide_page&intterm=rak19001_base_board&intcontent=documentation_link" target="_blank">RAK19001 Base Board</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak1921/overview/?intsource=docs_center&intmedium=organic&intcampaign=meshtastic_booster_starter_documentation_kit_quick_start_guide_page&intterm=rak1921_oled_display&intcontent=documentation_link" target="_blank">RAK1921 OLED Display</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak12500/overview/?intsource=docs_center&intmedium=organic&intcampaign=meshtastic_booster_starter_documentation_kit_quick_start_guide_page&intterm=rak12500_gnss_location_module&intcontent=documentation_link" target="_blank">RAK12500 GNSS Location Module</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak1904/overview/?intsource=docs_center&intmedium=organic&intcampaign=meshtastic_booster_starter_documentation_kit_quick_start_guide_page&intterm=rak1904_acceleration_sensor&intcontent=documentation_link" target="_blank">RAK1904 Acceleration Sensor</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak13800/overview/?intsource=docs_center&intmedium=organic&intcampaign=meshtastic_booster_starter_documentation_kit_quick_start_guide_page&intterm=rak13800_ethernet_module&intcontent=documentation_link" target="_blank">RAK13800 Ethernet Module</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak19018/overview/?intsource=docs_center&intmedium=organic&intcampaign=meshtastic_booster_starter_documentation_kit_quick_start_guide_page&intterm=rak19018_ethernet_poe_module&intcontent=documentation_link" target="_blank">RAK19018 Ethernet PoE Module</a>

<RkBottomNav/>