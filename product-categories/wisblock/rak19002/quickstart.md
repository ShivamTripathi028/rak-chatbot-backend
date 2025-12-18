---
slug: /product-categories/wisblock/rak19002/quickstart/
title: RAK19002 WisBlock Boost Module Quick Start Guide
description: ontains instructions and tutorials for installing and deploying your RAK19002. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak19002/rak19002.png"
keywords:
  - Quickstart
  - wisblock
  - RAK19002
sidebar_label: Quick Start Guide
---

# RAK19002 WisBlock Boost Module Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step on using RAK19002 WisBlock module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK19002 WisBlock Boost Board](https://store.rakwireless.com/products/wisblock-boost-module-rak19002?utm_source=WisBlockRAK19002&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install [Arduino IDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino Boards Manager, install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

The RAK19002 is a step-up boost regulator module, part of the RAKwireless WisBlock Series. The module can supply 12 V / 50 mA and could be mounted on WisSensor slot of RAK5005-O. The output voltage of the module is controlled by WisBlock Core IO pin.

For more information about RAK19002, refer to the [Datasheet](datasheet.md).

RAK19002 module can be connected to **Slot A, B, C, or D** of WisBlock Base to communicate with the WisBlock Core. It will work on any of those slots, but you need to consider the specific pin assigned on that slot to use the RAK19002. The table below shows the default IO pins used:

| SLOT A | SLOT B | SLOT C | SLOT D |
| :----: | :----: | :----: | :----: |
|  IO1   |  IO2   |  IO3   |  IO5   |

Also, always secure the connection of the WisBlock module by using the compatible screws, as shown in **Figure 1**.

> **Image:** RAK19002 connection to WisBlock Base

> **Image:** RAK19002 Supply Pins

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 3**, the location for Slot A, B, C, and D are properly marked by silkscreen. Follow carefully the procedure defined in [RAK5005-O module assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3 mm screws depending on the module.

> **Image:** Module connection to WisBlock Base

##### Disassembling

The procedure in disassembling any type of WisBlock modules is the same.

1. First, remove the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

> **Image:** Detaching silkscreen on the WisBlock module

3. Apply force to the module at the position of the connector, as shown in **Figure 6**, to detach the module from the baseboard.

> **Image:** Applying even forces on the proper location of a WisBlock module

:::tip NOTE
If you will connect other modules to remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts.
:::

After all this setup, you can now connect the battery (optional) and USB cable to start programming your WisBlock Core.

:::warning
- Batteries can cause harm if not handled properly.
- Only 3.7-4.2 V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5 V solar panels are supported. Do not use 12 V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires are matching the polarity on the WisBlock Base board. Not all batteries have the same wiring.
:::

### Software Configuration and Example

For RAK19002, the default accessible IO pin assignments are defined as follows which are used on different connection slots:

- `WB_IO1` for IO1 on **SLOT A**
- `WB_IO2` for IO2 on **SLOT B**
- `WB_IO3` for IO3 on **SLOT C**
- `WB_IO5` for IO5 on **SLOT D**

:::tip NOTE
- The IO pin MUST be set to **HIGH** to enable the RAK19002 Boost module.
- The **SLOT B** is not recommended because the IO2 pin is used to control power supply 3V3_S on RAK5005-O WisBase.
- The maximum recommended current is 50 mA  ( V<sub>IN</sub>=3.3 V ).
:::

- [RAK19002 in RAK4631 WisBlock Core Guide](https://docs.rakwireless.com/product-categories/wisblock/rak19002/quickstart/#rak19002-in-rak4631-wisblock-core-guide)
- [RAK19002 in RAK11200 WisBlock Core Guide](https://docs.rakwireless.com/product-categories/wisblock/rak19002/quickstart/#rak19002-in-rak11200-wisblock-core-guide)
- [RAK19002 in RAK11310 WisBlock Core Guide](https://docs.rakwireless.com/product-categories/wisblock/rak19002/quickstart/#rak19002-in-rak11310-wisblock-core-guide)

#### RAK19002 in RAK4631 WisBlock Core Guide

If you already installed the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index), the WisBlock Core and example code should now be available on the Arduino IDE.

1. First, you need to select the RAK4631 WisBlock Core.

> **Image:** Selecting RAK4631 as WisBlock Core

2. The [Basic Sample Code for RAK19002](https://github.com/RAKWireless/WisBlock/blob/master/examples/common/sensors/RAK19002_Boost_TPS61046/RAK19002_Boost_TPS61046.ino) in Github will work on all WisBlock Core. You can open the example codes depending on your WisBlock Core, as shown in **Figure 8**.

> **Image:** Opening RAK19002 example code for RAK4631 WisBlock Core

3. Once the example code is open, you can now select the right serial port and upload the code, as shown in **Figure 9** and **Figure 10**.

> **Image:** Selecting the correct Serial Port

> **Image:** Uploading the RAK19002 example code

4. When you successfully uploaded the example sketch, you can now use the RAK19002 Boost module to power-up your external sensors, modules, or devices. You can use any devices as long as it operates at 12 V and up to 50 mA.

#### RAK19002 in RAK11200 WisBlock Core Guide

If you already installed the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index), the WisBlock Core and example code should now be available on the Arduino IDE.

1. First, you need to select the RAK11200 WisBlock Core.

> **Image:** Selecting RAK11200 as WisBlock Core

2. The [Basic Sample Code for RAK19002](https://github.com/RAKWireless/WisBlock/blob/master/examples/common/sensors/RAK19002_Boost_TPS61046/RAK19002_Boost_TPS61046.ino) in Github will work on all WisBlock Core. You can open the example codes depending on your WisBlock Core, as shown in **Figure 12**.

> **Image:** Opening RAK19002 example code for RAK11200 WisBlock Core

3. Once the example code is open, you can now select the right serial port and upload the code, as shown in **Figure 13** and **Figure 14**.

:::tip NOTE
RAK11200 requires **Boot0** pin to be configured properly first before uploading. If not done properly, uploading the source code to RAK11200 will fail. Check the full details on the [RAK11200 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/#uploading-to-wisblock).
:::

> **Image:** Selecting the correct Serial Port

> **Image:** Uploading the RAK19002 example code

4. When you successfully uploaded the example sketch, you can now use the RAK19002 Boost module to power-up your external sensors, modules, or devices. You can use any devices as long as it operates at 12 V and up to 50 mA.

#### RAK19002 in RAK11310 WisBlock Core Guide

If you already installed the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index), the WisBlock Core and example code should now be available on the Arduino IDE.

1. First, you need to select the RAK11310 WisBlock Core.

> **Image:** Selecting RAK11310 as WisBlock Core

2. The [Basic Sample Code for RAK19002](https://github.com/RAKWireless/WisBlock/blob/master/examples/common/sensors/RAK19002_Boost_TPS61046/RAK19002_Boost_TPS61046.ino) in Github will work on all WisBlock Core. You can open the example codes depending on your WisBlock Core, as shown in **Figure 16**.

> **Image:** Opening RAK19002 example code for RAK11310 WisBlock Core

3. Once the example code is open, you can now select the right serial port and upload the code, as shown in **Figure 17** and **Figure 18**.

> **Image:** Selecting the correct Serial Port

> **Image:** Uploading the RAK19002 example code

4. When you successfully uploaded the example sketch, you can now use the RAK19002 Boost module to power-up your external sensors, modules, or devices. You can use any devices as long as it operates at 12 V and up to 50 mA.

