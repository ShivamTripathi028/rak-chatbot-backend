---
slug: /product-categories/wisblock/rak18060/quickstart/
title: RAK18060 WisBlock Audio Stereo Amplifier Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK18060. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak18060/rak18060.png"
keywords:
  - quickstart
  - wisblock audio
  - RAK18060
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK18060 Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step on using the RAK18060 WisBlock module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK18060 WisBlock Audio Stereo Amplifier Module](https://store.rakwireless.com/products/5-6w-stereo-amplifier-texas-instruments-tas2560-rak18060?utm_source=RAK18060&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base) with IO slot
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [Li-Ion/LiPo battery (required)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- Speakers (required)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install the [Arduino IDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino board, install the RAKwireless Arduino BSP. Follow the steps in the [GitHub repo](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

RAK18060 is a stereo amplifier module, part of the **WisBlock Audio Series**.

For more information about RAK18060, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak18060/datasheet/).

RAK18060 module can be connected to the IO slot of the WisBlock Base to communicate with the WisBlock Core. Always secure the connection of the WisBlock module by using compatible screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18060/quickstart/rak18060_assembly.png"
  width="60%"
  caption="RAK18060 connection to WisBlock Base"
/>

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 2**, the location for the IO slot is properly marked by silkscreen. Follow carefully the procedure defined in [WisBlock Base board assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3&nbsp;mm screws depending on the module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18060/quickstart/rak18060_mounting.png"
  width="70%"
  caption="RAK18060 connection to WisBlock Base"
/>


##### Disassembling

The procedure in disassembling any type of WisBlock module is the same.

1. First, remove the screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18060/quickstart/16.removing-screws.png"
  width="70%"
  caption="Removing screws from the WisBlock module"
/>

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18060/quickstart/17.detaching-silkscreen.png"
  width="70%"
  caption="Detaching silkscreen on the WisBlock module"
/>

3. Apply force to the module at the position of the connector, as shown in **Figure 5**, to detach the module from the baseboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18060/quickstart/18.detaching-module.png"
  width="70%"
  caption="Applying even forces on the proper location of a WisBlock module"
/>

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts. RAK18060 uses I2C communication lines, and it can cause possible conflict, especially on other WisBlock Modules connected to Slot A to F of the WisBlock Base.
:::

After all this setup, you can now connect the battery and USB cable to start programming your WisBlock Core.

:::warning
- Batteries can cause harm if not handled properly.
- Only 3.7-4.2&nbsp;V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5&nbsp;V solar panels are supported. Do not use 12&nbsp;V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires match the polarity on the WisBlock Base board. Not all batteries have the same wiring.
:::

4. You need to connect the LoRa and BLE antennas to the **RAK4631** module to avoid damage to this module during operation.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18060/quickstart/arduino_example_13.png"
  width="50%"
  caption="LoRa and BLE antennas connection to RAK4631 module"
/>

5. There are different power sources possible for the RAK18060. By default, the power source is the battery on the WisBlock Base board. You should see a solder blob on SB2 on the circuit board of RAK18060.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18060/quickstart/arduino_example_11.png"
  width="60%"
  caption="Power Select Diagram for RAK18060"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18060/quickstart/arduino_example_10.png"
  width="60%"
  caption="Solder portion for SB2 of RAK18060"
/>

6. Then you can now connect the speaker on either output of the **RAK18060** module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18060/quickstart/arduino_example_12.png"
  width="60%"
  caption="Speaker output portions of RAK18060 module"
/>

### Software Configuration and Example

**RAK18060** is a stereo amplifier module, part of the **WisBlock Audio Series**. The RAK18060 is designed based on the TAS2560 from TI. The TAS2560 features an ultra low-noise audio DAC and Class-D audio amplifier which incorporates speaker voltage and current sensing feedback for use with speaker protection algorithms. The RAK18060 can drive the speaker to play audio through the input I2S signals. With other WisBlock modules, it can achieve rich applications, such as recording and voice control functions.

#### Sample Code Test of the RAK18060 WisBlock Module

1. Install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index) for WisBlock by using the `package_rakwireless_index.json` board installation package. The WisBlock Core should now be available on the Arduino IDE.

2. Plug in your integrated module (**RAK4631** + **RAK18060**) into your PC through the USB cable.

3. Install the latest [RAKwireless Audio Library](https://github.com/RAKWireless/RAKwireless-Audio-library) using the Library Manager of Arduino IDE.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18060/quickstart/rakwireless_audio_library.png"
  width="100%"
  caption="RAKwireless Audio Library"
/>

4. Then open your Arduino IDE and open the **PlayBack48K** sample code for **RAK18060**, as shown in **Figures 11 to 13**.

:::tip NOTE
The example codes of RAKwireless Audio Library are compatible with different WisBlock Core. You have to select the correct WisBlock Core based on what core you used in your application.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18060/quickstart/arduino_example_1.png"
  width="100%"
  caption="Arduino IDE"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18060/quickstart/arduino_example_2.png"
  width="100%"
  caption="Selecting the PlayBack48K Sample Code"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18060/quickstart/arduino_example_3.png"
  width="100%"
  caption="PlayBack48K Sample Code"
/>

5. Then select your WisBlock Core **RAK4631**, as shown in **Figure 14**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18060/quickstart/arduino_example_4.png"
  width="100%"
  caption="Selecting the RAK4631 WisBlock Core board"
/>

6. Once done, select the corresponding port of your WisBlock Core **RAK4631**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18060/quickstart/arduino_example_5.png"
  width="100%"
  caption="Selecting the port of RAK4631"
/>

7. Once done, it should look the same with **Figure 16**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18060/quickstart/arduino_example_6.png"
  width="100%"
  caption="Selected board and port of RAK4631"
/>

8. Then tick the right arrow at the top leftmost part of the Arduino IDE to upload the sample code to your **RAK4631** module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18060/quickstart/arduino_example_7.png"
  width="100%"
  caption="Uploading the PlayBack48K sample code to your RAK4631"
/>

9. Once done uploading, it should look the same with **Figure 18**. At this moment, you will hear **Train 52 from Amsterdam is now arriving** from your speaker playing repetitively.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18060/quickstart/arduino_example_9.png"
  width="100%"
  caption="Programmed RAK4631"
/>

<RkBottomNav/>