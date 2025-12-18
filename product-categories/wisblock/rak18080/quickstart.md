---
slug: /product-categories/wisblock/rak18080/quickstart/
title: RAK18080 WisBlock Wireless Charge Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK18080. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak18080/rak18080.png"
keywords:
  - Quickstart
  - wisblock
  - RAK18080
sidebar_label: Quick Start Guide
---

# RAK18080 WisBlock Wireless Charge Module Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step on using the RAK18080 WisBlock module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK18080 WisBlock Audio DSP Board Module](https://store.rakwireless.com/products/wisblock-voice-processing-kit-audio-kit-3c?utm_source=RAK18080AudioKit&utm_medium=Document&utm_campaign=BuyFromStore)
- [WisBlock Audio Modules - Interposer, Microphones, and Amplifiers](https://store.rakwireless.com/collections/wisblock-audio)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base) with IO slot
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install the [Arduino IDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino board, install the RAKwireless Arduino BSP. Follow the steps in the [GitHub repo](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

RAK18080 is a professional audio processing module, part of the **WisBlock Audio Series**.

For more information about RAK18080, refer to the [Datasheet](datasheet.md).

RAK18080 module can be connected to the IO slot of the WisBlock Base to communicate with the WisBlock Core. Always secure the connection of the WisBlock module by using compatible screws.

> **Image:** RAK18080 connection to WisBlock Base

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 2**, the location for the IO slot is properly marked by silkscreen. Follow carefully the procedure defined in [WisBlock Base board assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3 mm screws depending on the module.

> **Image:** RAK18080 connection to WisBlock Base

When using the **RAK4631** board, connect the LoRa and BLE antennas to avoid damage to the board.

> **Image:** LoRa and BLE antennas of RAK4631

##### Disassembling

The procedure in disassembling any type of WisBlock module is the same.

1. First, remove the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

> **Image:** Detaching silkscreen on the WisBlock module

3. Apply force to the module at the position of the connector, as shown in **Figure 6**, to detach the module from the baseboard.

> **Image:** Applying even forces on the proper location of a WisBlock module

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts. RAK18080 uses I2C communication lines, and it can cause possible conflict, especially on other WisBlock Modules connected to Slot A to D of the WisBlock Base.
:::

After all this setup, you can now connect the battery (optional) and USB cable to start programming your WisBlock Core.

:::warning
- Batteries can cause harm if not handled properly.
- Only 3.7-4.2 V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5 V solar panels are supported. Do not use 12 V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires match the polarity on the WisBlock Base board. Not all batteries have the same wiring.
:::

### Software Configuration and Example

RAK18080 design is based on DBM10L by Synaptics. The DBM10L is an Artificial Intelligence (AI) and Machine Learning (ML) SoC based on a digital processor (DSP) optimized for voice and sensor processing. DBM10L can enable AI/ML, voice, and sensor applications, including Voice Trigger (VT), Voice Authentication (VA), Voice Command (VC), Noise Reduction (NR), Acoustic Echo Cancellation (AEC), and Sound Event Detection (SED). When used with **WisBlock Audio Stack**, RAK18080 can do VT and provide I2S data to the speaker. For this example, you will be using the **RAK4631** as your WisBlock Core.

#### Initial Test of the RAK18080 WisBlock Module

For this example, you need to use the **RAK18080 (DSP chip)**, **RAK18003 (Audio Interposer)**, **RAK18030 (PDM Microphone)** and **RAK18061 (Mono Amplifier)** modules. This example code is for a voice processing application. Also, you will need the following:
  - Li-Ion/LiPo battery
  - Speaker

1.  The **RAK18061** module is powered via **SB2 (battery)** by default. If you wish to use other DC power source, refer to the figures below.

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

2. Then in **RAK18003**, you need to connect **RAK18030** module using FPC cable.

> **Image:** Connecting together the RAK18003 and RAK18030 using FPC cable

3. Assemble the modules, as shown in the figure below. In this configuration, here's how the boards are stacked up:
   - RAK18061 (top)
   - RAK18080
   - RAK18003 + RAK18030
   - WisBlock Base board (bottom)

> **Image:** Overall Assembly

4. You can now connect the battery and speaker to the integrated module.

> **Image:** Connection of the battery and speaker into the integrated module

5. Install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index) for WisBlock by using the `package_rakwireless_index.json` board installation package. The WisBlock Core should now be available on the Arduino IDE.

6. Then install the latest [RAKwireless Audio Library](https://github.com/RAKWireless/RAKwireless-Audio-library) using the Library Manager of Arduino IDE.

> **Image:** RAKwireless Audio Library

> **Image:** RAKwireless Audio Library

7. Once done, connect the integrated module to the PC through a USB cable.

8. Open the sample code **DSPG_PlayBack** which is designed demonstrated **RAK18080** powerful features.

> **Image:** Selecting the sample code for RAK18080

> **Image:** Sample code for RAK18080

:::tip NOTE
The example codes of RAKwireless Audio Library are compatible with specific WisBlock Core. You have to select the correct WisBlock Core based on what core you used in your application.
:::

9. Select the **RAK4631** board and its serial port, as shown in **Figure 18** and **Figure 19**.

> **Image:** Selecting RAK4631 board as the WisBlock Core

> **Image:** Selecting the serial port of RAK4631 WisBlock Core

10. Then upload the code as shown in **Figure 20** and **Figure 21**.

> **Image:** Uploading the RAK18080 code

> **Image:** Uploading the RAK18080 code

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated example code for your WisBlock Core Module that can be found on the RAKwireless Audio Library.
:::

11. When you successfully uploaded the sample code, open the **Serial Monitor** of the Arduino IDE.

> **Image:** Sample code successfully uploaded to RAK4631

> **Image:** Opening the Serial Monitor

12. Once done, start speaking next to your PDM microphone **Hey RAK Star**. **RAK18080** module will recognize your voice and it will play a prompt sound via the speaker. Also, you will notice that **Hey RAK Star** will be logged in the Serial Monitor.

> **Image:** Hey RAK Star logged in the Serial Monitor

