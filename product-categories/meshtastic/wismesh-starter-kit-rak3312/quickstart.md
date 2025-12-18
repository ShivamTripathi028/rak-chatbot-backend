---
slug: /product-categories/meshtastic/wismesh-starter-kit-rak3312/quickstart/
title: Meshtastic RAK3312 Starter Kit Quick Start Guide
description: Step-by-step instructions to set up your Meshtastic WisMesh Starter Kit, including hardware assembly, firmware updates, and network configuration for seamless DIY mesh networking.
image: "https://images.docs.rakwireless.com/meshtastic/rak3312-starter-kit-2.png"
keywords:
    - RAK3312
    - Meshtastic
    - Meshtastic device
    - Meshtastic kits
    - LoRa mesh
    - SX1262
sidebar_label: Quick Start Guide
download: true
---

# Meshtastic WisMesh RAK3312 Starter Kit Quick Start Guide

The WisMesh RAK3312 Starter Kit is a versatile DIY kit designed for users who want a simple and reliable Meshtastic node. It is ideal for beginners and hobbyists looking for a hassle-free way to begin building with Meshtastic.

This guide covers the basics for the Meshtastic RAK3312 Starter Kit that are not handled by the [Meshtastic documentation](https://meshtastic.org/docs/introduction).

For detailed instructions how to configure the devices for the Meshtastic network, follow the [Meshtastic Getting Started](https://meshtastic.org/docs/getting-started) guide.

You can also check the Meshtastic Basic Device Setup Guide:.

<div class="flex items-center flex-col align-center gap-2">
  [ Meshtastic Basic Device Setup ](https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup?intsource=docs_center&intmedium=organic&intcampaign=meshtastic_wismesh_rak3312_starter_kit_documentation_quick_start_guide_page&intterm=meshtastic_basic_device_setup&intcontent=documentation_link)
</div>

----

:::tip NOTE
To make sure that your device runs the latest Meshtastic firmware, download the most recent version of the [ Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device. This ensures compatibility with the Meshtastic network.

- Meshtastic firmware for RAK3312 - **`firmware-rak3312-w.x.yy.zzzzzzz.bin`**
:::

## Prerequisite

Before going through each and every step on using Meshtastic Starter Kit, make sure to prepare the necessary items listed below:

### Hardware

- [WisMesh RAK3312 Starter Kit](https://store.rakwireless.com/products/wismesh-rak3312-starter-kit?utm_source=docs_center&utm_medium=organic&utm_campaign=meshtastic_wismesh_rak3312_starter_kit_documentation_quick_start_guide_page&utm_term=wismesh_rak3312_starter_kit&utm_content=store_link)
- [Your choice of WisBlock Modules](https://store.rakwireless.com/pages/wisblock?utm_source=docs_center&utm_medium=organic&utm_campaign=meshtastic_wismesh_rak3312_starter_kit_documentation_quick_start_guide_page&utm_term=your_choice_of_wisblock_modules&utm_content=store_link)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=docs_center&utm_medium=organic&utm_campaign=meshtastic_wismesh_rak3312_starter_kit_documentation_quick_start_guide_page&utm_term=li-ion_lipo_battery&utm_content=store_link)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=docs_center&utm_medium=organic&utm_campaign=meshtastic_wismesh_rak3312_starter_kit_documentation_quick_start_guide_page&utm_term=solar_charger&utm_content=store_link)

### Software

The WisBlock Core module of the Meshtastic RAK3312 Starter Kit comes pre-flashed with the Meshtastic firmware.

To connect the device to the Meshtastic network, you will need one of the following configuration tools:
- [Android App](https://meshtastic.org/docs/category/android-app)
- [Apple App](https://meshtastic.org/docs/category/apple-apps)
- [Web Client](https://meshtastic.org/docs/software/web-client)
- [Python CLI](https://meshtastic.org/docs/software/python/cli)

:::tip NOTE
Make sure that you have installed one of these applications, you will need it to configure the Meshtastic network.
::::

## Product Configuration

### Hardware Setup

#### RAK3312 to WisBlock Base

The Meshtastic RAK3312 Starter Kit comes with the RAK3312 module already assembled on the WisBlock Base board. The base board provides the USB interface for programming the RAK3312, a power source, and multiple module slots for adding WisBlock components.

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

**Figure 1** shows how to mount the RAK3312 module on top of a WisBlock Base board (RAK19007). Follow the assembly instructions in the [WisBlock module assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard?utm_source=docs_center&utm_medium=organic&utm_campaign=meshtastic_wismesh_rak3312_starter_kit_documentation_quick_start_guide_page&utm_term=wisblock_module_assembly/disassembly_instructions&utm_content=store_link) carefully to secure the connection safely. Once attached, secure the module with M1.2 x 3 mm screws.

:::tip NOTE
Assembly of the RAK3312 on other base boards follows the same procedure. You can find assembly guides for other modules in their respective **Quick Start Guides**.
:::

> **Image:** RAK3312 Mounting Sketch

##### Disassembling

To remove any WisBlock module, follow these steps:

1. Remove the screws.

> **Image:** Removing screws from the WisBlock module

2. Check the module silkscreen for the correct point where force can be applied.

> **Image:** Detaching silkscreen on the WisBlock module

3. Apply gentle upward pressure at the connector area as shown in **Figure 4,** to detach the module from the base board.

> **Image:** Applying even forces on the proper location of a WisBlock module

#### LoRa and WiFi/BLE Antenna

The Meshtastic Starter Kit includes several antennas:

- A **2 dBi rubber LoRa antenna** with a SMA connector and an IPEX-to-SMA pigtail cable.

> **Image:** LoRa Antenna

:::tip NOTE
Detailed information about the 2 dBi rubber antenna can be found on the [antenna datasheet](https://downloads.rakwireless.com/Accessories/Antenna/Rubber-Antenna/2701C042_Sunnyway_LoRa%20Antenna_SWE047-ZT_20240411.pdf).
:::

- A **LoRa PCB antenna** that can be connected directly to the RAK3312

> **Image:** LoRa PCB Antenna

- A **WiFi/BLE PCB antenna** that can be connected directly to the RAK3312

> **Image:** WiFi/BLE PCB Antenna

:::warning
Make sure the antenna is securely connected to ensure proper LoRa signal performance. Avoid powering the module without an antenna attached to the IPEX connector, as this can damage the RF section of the chip.
:::

RAK3312 has clear labels showing where each antenna connects, as shown in **Figure 8**.

> **Image:** RAK3312 Antenna Label

:::tip NOTE
Detailed information about the RAK3312 WiFi/BLE and LoRa antenna can be found on the [863-870 MHz antenna datasheet](https://downloads.rakwireless.com/LoRa/WisBlock/Accessories/RAK_PCB_Antenna_for_LoRa_863-870_MHz_(RAKARB04)_Datasheet.pdf) or the [902-928 MHz antenna datasheet](https://downloads.rakwireless.com/LoRa/WisBlock/Accessories/RAK_PCB_Antenna_for_LoRa_902-928_MHz_(RAKARB03)_Datasheet.pdf).
:::

:::warning
When using the LoRa, WiFi, or BLE transceivers, make sure that an antenna is always connected. Using these transceivers without an antenna can damage the system. Make sure to fix the module with the screws to ensure a proper function.
:::

### Software Setup

To make sure that your device runs the latest Meshtastic firmware, download the most recent version of the [Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device. This ensures compatibility with the Meshtastic network.

- Meshtastic firmware - **`firmware-rak3312-w.x.yy.zzzzzzz.bin`**

**Flashing the Meshtastic Starter Kit Firmware:**

The Meshtastic Starter Kits come pre-flashed with the Meshtastic firmware. If you encounter problems, update the Meshtastic firmware to the latest version.

- [Flash ESP32 devices](https://meshtastic.org/docs/getting-started/flashing-firmware/esp32/). (link goes to Meshtastic.org)

To configure your device for the Meshtastic network, follow the [Meshtastic Configuration Guide](https://meshtastic.org/docs/configuration).

### RAK3312 and WisBlock Base Boards

Detailed information and datasheets can be found in the documentation for the different modules:

- [RAK3312 Core Module](https://docs.rakwireless.com/product-categories/wisblock/rak3312?intsource=docs_center&intmedium=organic&intcampaign=meshtastic_wismesh_rak3312_starter_kit_documentation_quick_start_guide_page&intterm=rak3312_core_module&intcontent=documentation_link)
- [RAK19007 Base Board](https://docs.rakwireless.com/product-categories/wisblock/rak19007?intsource=docs_center&intmedium=organic&intcampaign=meshtastic_wismesh_rak3312_starter_kit_documentation_quick_start_guide_page&intterm=rak19007_base_board&intcontent=documentation_link)

