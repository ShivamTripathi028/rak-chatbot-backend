---
slug: /product-categories/wisblock/rak18000/quickstart/
title: RAK18000 WisBlock PDM Stereo Microphone Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK18000. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak18000/rak18000.png"
keywords:
  - quickstart
  - wisblock
  - RAK18000
sidebar_label: Quick Start Guide
---

# RAK18000 WisBlock PDM Stereo Microphone Module Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step on using the RAK18000 WisBlock module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK18000 WisBlock PDM Stereo Microphone Module](https://store.rakwireless.com/products/wisblock-microphone-module-rak18000?utm_source=WisBlockRAK18000&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base) with IO slot
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install [ArduinoIDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino board, install the RAKwireless Arduino BSP. Follow the steps in the [GitHub repo](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

RAK18000 is a WisBlock Sensor module that extends the WisBlock system with sound sensing capability.

For more information about RAK18000, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak18000/datasheet/).

RAK18000 module can be connected to the IO slot of WisBlock Base to communicate with the WisBlock Core. Also, always secure the connection of the WisBlock module by using compatible screws.

> **Image:** RAK18000 connection to WisBlock Base

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 2**, the location for the IO slot is properly marked by silkscreen. Follow carefully the procedure defined in [WisBlock Base board assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3 mm screws depending on the module.

> **Image:** RAK18000 connection to WisBlock Base

##### Disassembling

The procedure in disassembling any type of WisBlock modules is the same.

1. Remove the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

> **Image:** Detaching silkscreen on the WisBlock module

3. Apply force to the module at the position of the connector, as shown in **Figure 5**, to detach the module from the baseboard.

> **Image:** Applying even forces on the proper location of a WisBlock module

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts. RAK18000 uses the IOx signals as PDM communication lines, and it can cause possible conflict especially on other WisBlock Modules connected to Slot A to D of the WisBlock Base.
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

The RAK18000 is based on two MP34DT06J microphone modules. The RAK18000 is a digital microphone module that is designed to detect sounds and to support left and right channels. It is also capable of changing microphone orientation on the left or right channel through the switch resistor.

#### Initial Test of the RAK18000 WisBlock Module

1. Install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index) for WisBlock by using the `package_rakwireless_index.json` board installation package. The WisBlock Core should now be available on the Arduino IDE.

2. You need to select first the WisBlock Core you have, as shown in **Figure 6** to **Figure 8**.

**RAK4631 Board**

> **Image:** Selecting RAK4631 as the WisBlock Core

**RAK11200 Board**

> **Image:** Selecting RAK11200 as the WisBlock Core

**RAK11310 Board**

> **Image:** Selecting RAK11300 as the WisBlock Core

3. The Basic Sample Code for RAK18000 in Github will work depending on your WisBlock Core. You can open the example codes as shown in **Figure 9** to **Figure 11**.

**Using RAK4631 WisBlock Core**

- [RAK18000 Sample code](https://github.com/RAKWireless/WisBlock/tree/6a8b314f979f6a0c316b38b309d9fc6cd5c9a077/examples/RAK4630/sensors/RAK18000_Stereo) for RAK4631

> **Image:** Opening the RAK18000 example code for the RAK4631 WisBlock Core

**Using RAK11200 WisBlock Core**

- [RAK18000 Sample code](https://github.com/RAKWireless/WisBlock/tree/6a8b314f979f6a0c316b38b309d9fc6cd5c9a077/examples/RAK11200/IO/RAK18000_Stereo) for RAK11200

> **Image:** Opening RAK18000 example code for RAK11200 WisBlock Core

**Using RAK11300 WisBlock Core**

- [RAK18000 Sample code](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK11300/IO/RAK18000_Stereo) for RAK11300

> **Image:** Opening RAK18000 example code for RAK11300 WisBlock Core

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated code for your WisBlock Core Module that can be found on the **RAK18000 WisBlock Example Code Repository** and this sample code in Github will work depending on your WisBlock Core.

- [RAK18000 for RAK4631](https://github.com/RAKWireless/WisBlock/tree/6a8b314f979f6a0c316b38b309d9fc6cd5c9a077/examples/RAK4630/sensors/RAK18000_Stereo)
- [RAK18000 for RAK11200](https://github.com/RAKWireless/WisBlock/tree/6a8b314f979f6a0c316b38b309d9fc6cd5c9a077/examples/RAK11200/IO/RAK18000_Stereo)
- [RAK18000 for RAK11310](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK11300/IO/RAK18000_Stereo)
:::

4. After opening the sample sketch, choose your WisBlock Core then select the right serial port and upload the code, as shown in **Figure 12** and **Figure 13**.

:::tip NOTE
If you are using the RAK11200 as your WisBlock Core, the RAK11200 requires the **Boot0** pin to be configured properly first before uploading. If not done properly, uploading the source code to RAK11200 will fail. Check the full details on the [RAK11200 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/#uploading-to-wisblock).
:::

> **Image:** Selecting the correct Serial Port

> **Image:** Uploading the RAK18000 example code

5. When you successfully uploaded the example sketch, open the Serial Plotter of the Arduino IDE to see the sensor's reading logs. To test the sound detection, you can download a sound generating app on your smartphone and sweep frequencies from 1000 Hz to 10000 Hz. If you see the logs, as shown in **Figure 14**, then your RAK18000 is properly communicating to the WisBlock core.

> **Image:** RAK18000 audio data logs

