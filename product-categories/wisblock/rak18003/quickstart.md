---
slug: /product-categories/wisblock/rak18003/quickstart/
title: RAK18003 WisBlock Audio Interposer Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK18003. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak18003/rak18003.png"
keywords:
  - quickstart
  - RAK18003
  - wisblock
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK18003 WisBlock Audio Interposer Module Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step on using the RAK18003 WisBlock module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK18003 WisBlock Audio Interposer Module](https://store.rakwireless.com/products/wisblock-audio-interposer-rak18003?utm_source=RAK18003&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base) with IO slot
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- Your choice of [WisBlock Audio Module compatible with Interposer](https://store.rakwireless.com/collections/wisblock-audio)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install the [Arduino IDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino Board Manager, install the RAKwireless Arduino BSP. Follow the steps in the [GitHub repo](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

RAK18003 is an interposer module, part of the **WisBlock Audio Series**.

For more information about RAK18003, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak18003/datasheet/).

RAK18003 module can be connected to the IO slot of the WisBlock Base to communicate with the WisBlock Core. Always secure the connection of the WisBlock module by using compatible screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/rak18003_assembly.png"
  width="80%"
  caption="RAK18003 connection to WisBlock Base"
/>

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 2**, the location for the IO slot is properly marked by silkscreen. Follow carefully the procedure defined in [WisBlock Base board assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3&nbsp;mm screws depending on the module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/rak18003_mounting.png"
  width="70%"
  caption="RAK18003 connection to WisBlock Base"
/>

When using the **RAK4631** board, connect the LoRa and BLE antennas to avoid damage to the board.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/arduino_example_13(2).png"
  width="70%"
  caption="LoRa and BLE antennas connection to RAK4631 module"
/>

##### Disassembling

The procedure in disassembling any type of WisBlock module is the same.

1. First, remove the screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/removing-screws.png"
  width="70%"
  caption="Removing screws from the WisBlock module"
/>

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/detaching-silkscreen.png"
  width="70%"
  caption="Detaching silkscreen on the WisBlock module"
/>

1. Apply force to the module at the position of the connector, as shown in **Figure 6**, to detach the module from the baseboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/detaching-module.png"
  width="70%"
  caption="Applying even forces on the proper location of a WisBlock module"
/>

:::tip NOTE
- If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts.
- RAK18003 uses I2C communication lines, and it can cause possible conflict, especially on other WisBlock Modules connected to Slot A to D of the WisBlock Base.
:::

After all this setup, you can now connect the battery and USB cable to start programming your WisBlock Core.

:::warning
- Batteries can cause harm if not handled properly.
- Only 3.7-4.2&nbsp;V rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5&nbsp;V solar panels are supported. Do not use 12&nbsp;V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires match the polarity on the WisBlock Base board. Not all batteries have the same wiring.
:::

### Software Configuration and Examples

**RAK18003** is an interposer module, part of the **WisBlock Audio Series**. Its design allows multiple WisBlock Audio modules to be used together on a single IO slot. It consists of two IO expanders (TPT29555-TS5R), one signal switch (5223YWQ10/TR), and connectors where other WisBlock Audio modules can be interfaced. It also has a usable TF card slot. **RAK18003** module can be used with **RAK18030 PDM Microphone** or **RAK18060 Amplifier Module**. Their sample applications are detailed below.

#### Sample Code Test of the RAK18030 Module with RAK18003 Interposer Module

1. To test the **RAK18003 (Audio Interposer)** with **RAK4631 (WisBlock Core)** and **RAK18030 (PDM Microphone)**, you need to assemble them first, as shown in **Figure 7**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/arduino_example_15a.png"
  width="100%"
  caption="Assembling together the RAK4631, RAK18030, and RAK18003"
/>

2. Then install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index) for WisBlock by using the `package_rakwireless_index.json` board installation package. The WisBlock Core should now be available on the Arduino IDE.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/rak18030_arduino_example_1.png"
  width="100%"
  caption="Arduino IDE"
/>

3. Install the latest [RAKwireless Audio Library](https://github.com/RAKWireless/RAKwireless-Audio-library) using the Library Manager of Arduino IDE.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/rakwireless_audio_library.png"
  width="100%"
  caption="RAKwireless Audio Library"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/rakwireless_audio_library2.png"
  width="100%"
  caption="RAKwireless Audio Library"
/>

4. Open the sample code for **RAK18003**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/rak18030_arduino_example_2a.png"
  width="100%"
  caption="Selecting the sample code for RAK18003"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/rak18030_arduino_example_3a.png"
  width="100%"
  caption="Sample code for RAK18003"
/>

:::tip NOTE
The example codes of RAKwireless Audio Library are compatible with specific WisBlock Core. You have to select the correct WisBlock Core based on what core you used in your application.
:::

5. Select the **RAK4631** board and its serial port, as shown in **Figure 13** and **Figure 14**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/rak18030_arduino_example_4a.png"
  width="100%"
  caption="Selecting RAK4631 board as the WisBlock Core"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/rak18030_arduino_example_5a.png"
  width="100%"
  caption="Selecting the serial port of RAK4631 WisBlock Core"
/>

6. Upload the code, as shown in **Figure 15** and **Figure 16**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/rak18030_arduino_example_6a.png"
  width="100%"
  caption="Uploading the RAK18030 code"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/rak18030_arduino_example_7a.png"
  width="100%"
  caption="Uploading the RAK18030 code"
/>

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated example code for your WisBlock Core Module that can be found on the [RAKwireless Audio Library.](https://github.com/RAKWireless/RAKwireless-Audio-library/tree/main/examples)
:::

7. When you successfully uploaded the sample code, open the **Serial Plotter** of the Arduino IDE to see the sensor's reading logs. To test the sound detection, you can download a sound-generating app on your smartphone and sweep frequencies starting from 1000&nbsp;Hz to 10000&nbsp;Hz. If you see the logs, then your RAK18030 and RAK18003 are communicating to the WisBlock core.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/rak18030_arduino_example_8a.png"
  width="100%"
  caption="Sample code successfully uploaded to RAK4631"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/rak18030_arduino_example_9a.png"
  width="100%"
  caption="Opening the Serial Plotter"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/rak18030_arduino_example_10a.png"
  width="100%"
  caption="FFT Plot of 10kHz sample signal"
/>

:::tip NOTE
If there is no serial plot graph shown in Arduino 2.0.x, you can try the serial plotter of the legacy Arduino 1.8.x IDE.
:::

#### Sample Code Test of the RAK18060 Module with RAK18003 Interposer Module

1. To test the **RAK18003 (Audio Interposer)** with **RAK4631 (WisBlock Core)** and **RAK18060 (Stereo Amplifier)**, you need to assemble them first as shown in **Figure 20**. Also, you'll be needing the following:
   - Li-Ion/LiPo battery
   - Speakers

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/arduino_example_14a.png"
  width="100%"
  caption="Assembling together the RAK4631, RAK18060, and RAK18003"
/>

2. The **RAK18060** module is powered via **SB2 (battery)** by default. If you wish to use another DC power source, refer to **Figures 21 to 24**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/arduino_example_11.png"
  width="60%"
  caption="Power Select Diagram for RAK18060 with SB2 as default"
/>

   **3V3**

   If you want to use 3V3, desolder SB2 and solder SB1.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/arduino_example_16.png"
  width="60%"
  caption="Solder portion for SB1"
/>

   **VBUS**

   If you want to use VBUS, desolder SB2 and solder SB3.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/arduino_example_17.png"
  width="60%"
  caption="Solder portion for SB3"
/>

   **EX_POWER**

   If you want to use EX_POWER, desolder SB2, and solder SB4.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/arduino_example_18.png"
  width="60%"
  caption="Solder portion for SB4"
/>


3. You can now connect the speaker on either output of the **RAK18060** module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/arduino_example_12.png"
  width="60%"
  caption="Speaker output portions of RAK18060 module"
/>

4. Install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index) for WisBlock by using the `package_rakwireless_index.json` board installation package. The WisBlock Core should now be available on the Arduino IDE.

5. Then install the latest [RAKwireless Audio Library](https://github.com/RAKWireless/RAKwireless-Audio-library) using the Library Manager of Arduino IDE.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/rakwireless_audio_library.png"
  width="100%"
  caption="RAKwireless Audio Library"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/rakwireless_audio_library2.png"
  width="100%"
  caption="RAKwireless Audio Library"
/>

6. Plug in your integrated module **RAK4631** + **RAK18003** + **RAK18060** into your PC through the USB cable.

7. Then open your Arduino IDE and open the **PlayBack48K** sample code for **RAK18060**, as shown in **Figures 28 to 30**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/arduino_example_1.png"
  width="100%"
  caption="Arduino IDE"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/arduino_example_2.png"
  width="100%"
  caption="Selecting the PlayBack48K Sample Code"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/arduino_example_3.png"
  width="100%"
  caption="PlayBack48K Sample Code"
/>

:::tip NOTE
The example codes of RAKwireless Audio Library are compatible with specific WisBlock Core. You have to select the correct WisBlock Core based on what core you used in your application.
:::

8. Select your WisBlock Core **RAK4631**, as shown in **Figure 31**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/arduino_example_4.png"
  width="100%"
  caption="Selecting the RAK4631 WisBlock Core board"
/>

9. Then select the corresponding port of your WisBlock Core **RAK4631**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/arduino_example_5.png"
  width="100%"
  caption="Selecting the serial port of RAK4631 WisBlock Core"
/>

10. Once done, it should look the same with **Figure 33**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/arduino_example_6.png"
  width="100%"
  caption="Selected board and port of RAK4631"
/>

11. Then tick the right arrow at the top leftmost part of the Arduino IDE to upload the sample code to your **RAK4631** module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/arduino_example_7.png"
  width="100%"
  caption="Uploading the PlayBack48K sample code to your RAK4631"
/>

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated example code for your WisBlock Core Module that can be found on the [RAKwireless Audio Library](https://github.com/RAKWireless/RAKwireless-Audio-library/tree/main/examples).
:::

12. Once done uploading, it should look the same with **Figure 35**. At this moment, you will hear "Train 52 from Amsterdam is now arriving" from your speaker playing repetitively.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18003/quickstart/arduino_example_9.png"
  width="100%"
  caption="Programmed RAK4631"
/>

