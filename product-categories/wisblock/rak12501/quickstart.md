---
slug: /product-categories/wisblock/rak12501/quickstart/
title: RAK12501 WisBlock GNSS Location Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK12501. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak12501/rak12501.png"
keywords:
    - rak12501
    - wisblock
    - quickstart
    - quectel l76k
sidebar_label: Quick Start Guide
---
import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK12501 WisBlock GNSS Location Module Quick Start Guide

## Prerequisites

Before going through each and every step on using the RAK12501 GNSS Location WisBlock module, make sure to prepare the necessary items listed below:

### Hardware

- [RAK12501 WisBlock GNSS Location Module](https://store.rakwireless.com/products/wisblock-gnss-location-module-rak12501?utm_source=WisBlockRAK12501&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

### Software

- Download and install [ArduinoIDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino board, install the RAKwireless Arduino BSP. Follow the steps in the [GitHub repo](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

The RAK12501 uses the Quectel L76K module. It supports a wide variety of satellite data protocols such as GPS, GLONASS, QZSS, and BeiDou. This ensures the retrieval of precise location data.

For more information about RAK12501, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak12501/datasheet/).

This module gives information about:

- GPS coordinate (latitude, longitude, altitude)
- Ground speed
- Direction (heading)
- SIV (Satellite-in-View)

Connected to the sensor's slot of the [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base), the RAK12500 enables communication with the WisBlock Core, as shown in **Figure 1**. It functions on **SLOT A or SLOT D**. Additionally, always secure the WisBlock module connection using compatible screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12501/quickstart/rak12501-assembly.png"
  caption="RAK12501 connection to the WisBlock Base"
  width="100%"
/>

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 2**, the location for Slot A and D are properly marked by silkscreen. Follow carefully the procedure defined in [WisBlock Base board assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3&nbsp;mm screws depending on the module.
<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12500/quickstart/rak12500-mounting.png"
  caption="Attach RAK12501 to the WisBlock Base"
  width="60%"
/>

##### Disassembling

The procedure in disassembling any type of WisBlock modules is the same.

1. First, remove the screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12500/quickstart/16.removing-screws.png"
  caption="Remove screws from the WisBlock module"
  width="80%"
/>

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12500/quickstart/17.detaching-silkscreen.png"
  caption="Detach silkscreen on the WisBlock module"
  width="70%"
/>

3. Apply force to the module at the position of the connector, as shown in **Figure 5**, to detach the module from the baseboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12500/quickstart/18.detaching-module.png"
  caption="Apply even forces on the proper location of a WisBlock module"
  width="70%"
/>

#### GPS Antenna

Another important part component of RAK12501 is the GPS antenna. Make sure that it is properly connected to have a good GPS signal.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12501/quickstart/rak12501-gps-antenna.png"
  caption="GPS antenna"
  width="70%"
/>

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts. RAK12501 uses UART communication lines, and it can cause possible conflict especially on some IO modules.
:::

After all this setup, connect the battery and USB cable to start programming your WisBlock Core.

:::warning
- Batteries can cause harm if not handled properly.
- Only 3.7-4.2&nbsp;V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5&nbsp;V solar panels are supported. Do not use 12&nbsp;V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires match the polarity on the WisBlock Base board. Not all batteries have the same wiring.
:::

### Software Configuration and Example

The RAK12501 is a very accurate GNSS Module that contains a Quectel L76K chip. The L76K features exceptional performance, high sensitivity, and minimal acquisition time, with digital serial interface standard output.

#### Initial Test of the RAK12501 WisBlock Module

1. Install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index) for WisBlock by using the `package_rakwireless_index.json` board installation package. The WisBlock Core should now be available on the Arduino IDE.

2. Choose the WisBlock Core that you have, as shown in **Figure 7** to **Figure 9**.

**RAK4631 Board**
<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12501/quickstart/rak4631-board.png"
  caption="Select RAK4631 as the WisBlock Core"
  width="100%"
/>

**RAK11200 Board**
<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12501/quickstart/rak11200-board.png"
  caption="Select RAK11200 as the WisBlock Core"
  width="100%"
/>

**RAK11310 Board**
<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12501/quickstart/rak11300-board.png"
  caption="Select RAK11300 as the WisBlock Core"
  width="100%"
/>

3. The [Basic Sample Code for RAK12501](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK12501_GPS_L76K) in GitHub will work on all WisBlock Core. Download the source code from the GitHub repository and open the `RAK12501_GPS_L76K.ino` file with Arduino IDE.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12501/quickstart/open-rak12501-example.png"
  caption="Open the RAK12501 example code"
  width="100%"
/>

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated code for your WisBlock Core Module that can be found on the [RAK12501 WisBlock Example Code Repository](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK12501_GPS_L76K).
:::

4. Once the example code is open, install the [TinyGPS](https://github.com/neosarchizo/TinyGPS) library by clicking the highlighted link, as shown in **Figure 11** and **Figure 12**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12501/quickstart/rak12501-code.png"
  caption="Access the library used for the RAK12501 Module"
  width="100%"
/>
<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12501/quickstart/rak12501-library.png"
  caption="Install the compatible library for the RAK12501 Module"
  width="45%"
/>


5. After installing the library, select the correct serial port and upload the code, as shown in **Figure 13** and **Figure 14**.

:::tip NOTE
If you are using the RAK11200 as your WisBlock Core, the RAK11200 requires the **Boot0** pin to be configured properly first before uploading. If not done properly, uploading the source code to RAK11200 will fail. Check the full details on the [RAK11200 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/#uploading-to-wisblock).
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12500/quickstart/rak12500_port.png"
  caption="Select the correct Serial Port"
  width="100%"
/>
<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12500/quickstart/rak12500_upload.png"
  caption="Upload the RAK12501 example code"
  width="100%"
/>

6. When the example sketch is uploaded, open the Serial Monitor of the Arduino IDE to see the sensor's reading logs. If you see the logs, as shown in **Figure 15**, then your RAK12501 is properly communicating to the WisBlock core.

:::tip NOTE
The GPS antenna must have an unobstructed view of the sky to be able to receive satellite signals. For the example to work, you should test it outside of a building.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12500/quickstart/rak12500_log.png"
  caption="RAK12501 sensor data logs"
  width="100%"
/>

<RkBottomNav/>




