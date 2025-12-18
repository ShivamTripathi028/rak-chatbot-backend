---
slug: /product-categories/wisblock/rak18061/quickstart/
title: RAK18061 WisBlock Audio Mono Amplifier Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK18061. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak18061/rak18061.png"
keywords:
  - quickstart
  - wisblock
  - RAK18061
sidebar_label: Quick Start Guide
---

# RAK18061 WisBlock Audio Mono Amplifier Module Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step on using the RAK18061 WisBlock module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK18061 WisBlock Audio Mono Amplifier Module](https://store.rakwireless.com/products/5-6w-amplifier-texas-instruments-tas2560-rak18061?utm_source=RAK18061&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base) with IO slot
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- Speaker
- [Li-Ion/LiPo battery](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install the [Arduino IDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino board, install the RAKwireless Arduino BSP. Follow the steps in the [GitHub repo](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

RAK18061 is a mono amplifier module, part of the **WisBlock Audio Series**.

For more information about RAK18061, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak18061/datasheet/).

RAK18061 module can be connected to the IO slot of the WisBlock Base to communicate with the WisBlock Core. Always secure the connection of the WisBlock module by using compatible screws.

> **Image:** RAK18061 connection to WisBlock Base

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 2**, the location for the IO slot is properly marked by silkscreen. Follow carefully the procedure defined in [WisBlock Base board assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3 mm screws depending on the module.

> **Image:** RAK18061 connection to WisBlock Base

You need to connect the LoRa and BLE antennas to the **RAK4631** module to avoid damage to this module during operation.

> **Image:** LoRa and BLE antennas connection to RAK4631 module

The **RAK18061** module is powered via **SB2 (battery)** by default. If you wish to use other DC power source, refer to **Figure 4**.

> **Image:** Power Select Diagram for RAK18061 with SB2 as default

   **3V3**

   If you want to use 3V3, desolder SB2 and solder SB1.

> **Image:** Solder portion for SB1

   **VBUS**

   If you want to use VBUS, desolder SB2 and solder SB3.

> **Image:** Solder portion for SB3

   **EX_POWER**

   If you want to use EX_POWER, desolder SB2 and solder SB4.

> **Image:** Solder portion for SB4

Then you can now connect the speaker to the speaker output of the **RAK18061** module.

> **Image:** Speaker output of RAK18061 module

##### Disassembling

The procedure in disassembling any type of WisBlock module is the same.

1. First, remove the screws.

> **Image:** Removing screws from the WisBlock module

1. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

> **Image:** Detaching silkscreen on the WisBlock module

1. Apply force to the module at the position of the connector, as shown in **Figure 11**, to detach the module from the baseboard.

> **Image:** Applying even forces on the proper location of a WisBlock module

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts. RAK18061 uses I2C communication lines, and it can cause possible conflict, especially on other WisBlock Modules connected to Slot A to D of the WisBlock Base.
:::

After all this setup, you can now connect the battery and USB cable to start programming your WisBlock Core.

:::warning
- Batteries can cause harm if not handled properly.
- Only 3.7-4.2 V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5 V solar panels are supported. Do not use 12 V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires match the polarity on the WisBlock Base board. Not all batteries have the same wiring.
:::

### Software Configuration and Example

**RAK18061** is a mono amplifier module, part of the **WisBlock Audio Series**. The RAK18061 is designed based on the TAS2560 from TI. The TAS2560 features an ultra low-noise audio DAC and Class-D audio amplifier which incorporates speaker voltage and current sensing feedback for use with speaker protection algorithms. The RAK18061 can drive the speaker to play audio through the input I2S signals. With other WisBlock modules, it can achieve rich applications, such as recording and voice control functions.

#### Sample Code Test of the RAK18061 WisBlock Module

1. Install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index) for WisBlock by using the `package_rakwireless_index.json` board installation package. The WisBlock Core should now be available on the Arduino IDE.

2. Then install the latest [RAKwireless Audio Library](https://github.com/RAKWireless/RAKwireless-Audio-library) using the Library Manager of Arduino IDE.

> **Image:** RAKwireless Audio Library

> **Image:** RAKwireless Audio Library

3. Plug in your integrated module (**RAK4631** + **RAK18061**) into your PC through the USB cable.

4. Then open your Arduino IDE and open the **PlayBack48K** sample code for **RAK18061**, as shown in **Figures 14 to 16**.

> **Image:** Arduino IDE

> **Image:** Selecting the PlayBack48K Sample Code

> **Image:** PlayBack48K Sample Code

:::tip NOTE
The example codes of RAKwireless Audio Library are compatible with specific WisBlock Core. You have to select the correct WisBlock Core based on what core you used in your application.
:::

5. Select your WisBlock Core **RAK4631**, as shown in **Figure 17**.

> **Image:** Selecting the RAK4631 WisBlock Core board

6. Once done, select the corresponding port of your WisBlock Core **RAK4631**.

> **Image:** Selecting the port of RAK4631

7. Once done, it should look the same with **Figure 19**.

> **Image:** Selected board and port of RAK4631

8. Then tick the right arrow at the top leftmost part of the Arduino IDE to upload the sample code to your **RAK4631** module.

> **Image:** Uploading the PlayBack48K sample code to your RAK4631

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated example code for your WisBlock Core Module that can be found on the [RAKwireless Audio Library](https://github.com/RAKWireless/RAKwireless-Audio-library/tree/main/examples).
:::

9. Once done uploading, it should look like the same with **Figure 21**. At this moment, you will hear "**Train 32 from Amsterdam is now arriving**" from your speaker playing repetitively.

> **Image:** Programmed RAK4631

