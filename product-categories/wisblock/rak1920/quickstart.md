---
slug: /product-categories/wisblock/rak1920/quickstart/
title: RAK1920 WisBlock Sensor Adapter Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK1920. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak1920/rak1920.png"
keywords:
  - quickstart
  - wisblock
  - RAK1920
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK1920 WisBlock Sensor Adapter Module Quick Start Guide



## Prerequisite

### What Do You Need?

Before going through each and every step on using the RAK1920 WisBlock module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK1920 WisBlock Interface Module](https://store.rakwireless.com/products/rak1920-sensor-adapter-module?utm_source=RAK1920&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- Grove PIR Motion Sensor (AS312)

#### Software

- Download and install [Arduino IDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino board, install the RAKwireless Arduino BSP. Follow the steps in the [GitHub repo](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

RAK1920 is a WisBlock Interface module, which extends the WisBlock system with an adapter board to connect Click Boards (MikroElektronika), QWICC (Sparkfun) based, and Grove (Seeed) based sensors to WisBlock.

For more information about the RAK1920, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak1920/datasheet/).

RAK1920 module is part of the WisBlock Interface category, which connects to the base board through the IO slot. Also, always secure the connection of the WisBlock module by using the compatible screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1920/quickstart/rak1920_assembly.png"
    caption="RAK1920 connection to WisBlock Base" 
   width="70%"
/>

#### Assembling and Disassembling of WisBlock Modules
##### Assembling

As shown in **Figure 2**, the location for IO slot is properly marked by silkscreen. Follow carefully the procedure defined in [RAK5005-O module assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3&nbsp;mm screws depending on the module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1920/quickstart/rak1920_mounting.png"
    caption="RAK1920 connection to WisBlock Base" 
   width="70%"
/>

##### Disassembling

The procedure in disassembling any type of WisBlock modules is the same.

1. Remove the screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1920/quickstart/16.removing-screws.png"
  caption="Removing screws from the WisBlock module" 
   width="70%"
/>

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1920/quickstart/17.detaching-silkscreen.png"
    caption="Detaching silkscreen on the WisBlock module" 
   width="70%"
/>

3. Apply force to the module at the position of the connector, as shown in **Figure 5**, to detach the module from the baseboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1920/quickstart/18.detaching-module.png"
    caption="Applying even forces on the proper location of a WisBlock module" 
   width="70%"
/>

:::tip NOTE
If you will connect other modules to remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts. RAK1920 uses UART and I2C communication lines, and it can cause possible conflict especially on other WisBlock Modules connected to Slot A to D of the WisBlock Base.
:::

After all this setup, you can now connect the battery (optional) and USB cable to start programming your WisBlock Core.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1920/quickstart/battery-connection.gif"
    caption="Battery connection to WisBlock Base Board" 
   width="50%"
/>

:::warning

- Batteries can cause harm if not handled properly.
- Only 3.7-4.2&nbsp;V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5&nbsp;V solar panels are supported. Do not use 12&nbsp;V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires are matching the polarity on the WisBlock Base board. Not all batteries have the same wiring.

:::


### Software Configuration and Example

The RAK1920 module is a sensor extension module, it supports several defacto-standard interfaces in the IoT market and allows customers to integrate sensors manufactured by Mikroe, SparkFun, SeeedStudio, and others. For example, the RAK1920 supports the Click Boards™ series of modules provided by Mikroe, Qwiic Connect™ sensor interface designed by SparkFun, and it supports all kinds of I2C module digital I/O, UART and ADC sensors with a Grove™ interface.


#### Initial Test of the RAK1920 WisBlock Module

If you already installed the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index), the WisBlock Core and example code should now be available on the Arduino IDE.

1. You need to select first the WisBlock Core you have, as shown in **Figure 7**, **Figure 8** and **Figure 9**.

**Using RAK4631 WisBlock Core**

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1920/quickstart/rak4631_board.png"
    caption="Selecting RAK4631 as WisBlock Core" 
   width="100%"
/>

**Using RAK11200 WisBlock Core**

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1920/quickstart/rak11200_board.png"
    caption="Selecting RAK11200 as WisBlock Core" 
   width="100%"
/>

**Using RAK11300 WisBlock Core**

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1920/quickstart/rak11300_board.png"
    caption="Selecting RAK11300 as WisBlock Core" 
   width="100%"
/>

2. The Basic Sample Code for RAK1920 in Github will work on all WisBlock Core. You can open the the example codes depending on your WisBlock Core, as shown in **Figure 10**, **Figure 11** and **Figure 12**. For this guide we will be using [Grove PIR AS312](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK1920_Grove_PIR_AS312)

**Sample code for RAK4631**

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1920/quickstart/rak4631_example.png"
  figureCount="10"
  caption="Opening RAK1920 example code for RAK4631 WisBlock Core" 
   width="100%"
/>

**Sample code for RAK11200**

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1920/quickstart/rak11200_example.png"
  figureCount="11"
  caption="Opening RAK1920 example code for RAK11200 WisBlock Core" 
   width="100%"
/>

**Sample code for RAK11300**

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1920/quickstart/rak11300_example.png"
  figureCount="12"
  caption="Opening RAK1920 example code for RAK11300 WisBlock Core" 
   width="100%"
/>

3. Once the example code is open, you can now select the right serial port and upload the code, as shown in **Figure 13** and **Figure 14**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1920/quickstart/select_port.png"
  figureCount="13"
  caption="Selecting the correct Serial Port" 
   width="100%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1920/quickstart/upload.png"
  figureCount="14"
  caption="Uploading the RAK1920 example code" 
   width="100%"
/>

5. When you successfully uploaded the example sketch, open the Serial Monitor of the Arduino IDE to see the sensor's reading logs. If you see the logs, as shown in **Figure 15**, then your RAK1920 is properly communicating to the WisBlock core.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1920/quickstart/pir_logs.png"
  figureCount="15"
  caption="RAK1920 sensor data logs" 
   width="100%"
/>

**Sample code for other sensors**

- [Grove Color TCS3472](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK1920_Grove_Color_TCS3472)
- [MikroBUS Temperature TMP102](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK1920_MikroBUS_Temperature_TMP102)
- [QWIIC AirQuality SGP30](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK1920_QWIIC_AirQuality_SGP30)




<RkBottomNav/>


