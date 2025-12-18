---
slug: /product-categories/wisblock/rak15001/quickstart/
title: RAK15001 WisBlock Flash Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK15001. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak15001/rak15001.png"
keywords:
  - quickstart
  - wisblock
  - RAK15001
sidebar_label: Quick Start Guide
---

# RAK15001 WisBlock Flash Module Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step on using the RAK15001 WisBlock module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK15001 WisBlock Flash module](https://store.rakwireless.com/products/wisblock-flash-module-rak15001?utm_source=WisBlock15001&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install [ArduinoIDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino Boards Manager, install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

WisBlock can integrate this module which makes it easy for you to save big data on such applications that you need to access frequently, like conversion tables, lookup tables or images, and even sound files. But compared to the EEPROM module, the RAK15001 Flash Memory module has fewer write/erase cycles, so it is not an ideal storage for constantly changing data like for sensor readings.

For more information about RAK15001, please refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak15001/datasheet/).

RAK15001 module can be connected to any slot of WisBlock Base to communicate with the WisBlock Core. It will work on **SLOT A, B, C, or D**. Also, always secure the connection of the WisBlock module by using compatible screws.

> **Image:** RAK15001 connection to WisBlock Base

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 2**, the location for Slot A, B, C, and D are properly marked by silkscreen. Follow carefully the procedure defined in [RAK5005-O module assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3 mm screws depending on the module.

> **Image:** Sensor connection to WisBlock Base

##### Disassembling

The procedure in disassembling any type of WisBlock modules is the same.

1. First, remove the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

> **Image:** Detaching silkscreen on the WisBlock module

3. Apply force to the module at the position of the connector, as shown in **Figure 5**, to detach the module from the baseboard.

> **Image:** Applying even forces on the proper location of a WisBlock module

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts. RAK15001 uses SPI communication lines, and it can cause possible conflict especially on some IO modules.
:::

After all this setup, you can now connect the battery (optional) and USB cable to start programming your WisBlock Core.

### Software Configuration and Example

The RAK15001 is a NOR flash module with a 16 MBit (2 MByte) nonvolatile memory. It uses GD25Q16CNIG (16 Mbit) from GigaDevice with a standard SPI interface.
#### RAK15001 in RAK4631 WisBlock Core Guide

If you already installed the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index), the WisBlock Core and example code should now be available on the Arduino IDE.

1. First, you need to select the RAK4631 WisBlock Core.

> **Image:** Selecting RAK4631 as WisBlock Core

2. The [Basic Sample Code for RAK15001](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK15001_Flash_GD25Q16C) in Github will work on ALL WisBlock Core. You can open the example codes depending on your WisBlock Core, as shown in **Figure 7**.

> **Image:** Opening RAK15001 example code for RAK4631 WisBlock Core

3. Once the example code is open, install the [Adafruit_SPIFlash](https://github.com/adafruit/Adafruit_SPIFlash) library by clicking the link highlighted in yellow, as shown in **Figure 8** and **Figure 9**.

> **Image:** Accessing the library used for RAK15001 Module

> **Image:** Installing the compatible library for RAK15001 Module

4. After successful installation of the library, you can now select the right serial port and upload the code.

> **Image:** Selecting the correct Serial Port

5. When you successfully uploaded the example sketch, open the Serial Monitor of the Arduino IDE to see if it read the content, wrote new data, and erased the data from the Flash module. If you see the logs, as shown in **Figure 11**, then your RAK15001 is properly communicating to the WisBlock core.

> **Image:** RAK15001 Read, Write, and Erase data

#### RAK15001 in RAK11200 WisBlock Core Guide

If you already installed the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index), the WisBlock Core and example code should now be available on the Arduino IDE.

1. First, you need to select the RAK11200 WisBlock Core.

> **Image:** Selecting RAK11200 as WisBlock Core

2. The [Basic Sample Code for RAK15001](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK15001_Flash_GD25Q16C) in Github will work on ALL WisBlock Core. You can open the example codes depending on your WisBlock Core, as shown in **Figure 13**.

> **Image:** Opening RAK15001 example code for RAK11200 WisBlock Core

3. Once the example code is open, install the [Adafruit_SPIFlash](https://github.com/adafruit/Adafruit_SPIFlash) library by clicking the link highlighted in yellow, as shown in **Figure 14** and **Figure 15**.

> **Image:** Accessing the library used for RAK15001 Module

> **Image:** Installing the compatible library for RAK15001 Module

4. After successful installation of the library, you can now select the right serial port and upload the code.

:::tip NOTE
RAK11200 requires the **Boot0** pin to be configured properly first before uploading. If not done properly, uploading the source code to RAK11200 will fail. Check the full details on the [RAK11200 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/).
:::

> **Image:** Selecting the correct Serial Port

5. When you successfully uploaded the example sketch, open the Serial Monitor of the Arduino IDE to see if it read the content, wrote new data, and erased the data from the Flash module. If you see the logs, as shown in **Figure 17**, then your RAK15001 is properly communicating to the WisBlock core.

> **Image:** RAK15001 Read, Write, and Erase data

#### RAK15001 in RAK11310 WisBlock Core Guide

If you already installed the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index), the WisBlock Core and example code should now be available on the Arduino IDE.

1. First, you need to select the RAK11310 WisBlock Core.

> **Image:** Selecting RAK11310 as WisBlock Core

2. The [Basic Sample Code for RAK15001](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK15001_Flash_GD25Q16C) in Github will work on ALL WisBlock Core. You can open the example codes depending on your WisBlock Core, as shown in **Figure 19**.

> **Image:** Opening RAK15001 example code for RAK11310 WisBlock Core

3. Once the example code is open, install the [Adafruit_SPIFlash](https://github.com/adafruit/Adafruit_SPIFlash) library by clicking the link highlighted in yellow, as shown in **Figure 20** and **Figure 21**.

> **Image:** Accessing the library used for RAK15001 Module

> **Image:** Installing the compatible library for RAK15001 Module

4. After successful installation of the library, you can now select the right serial port and upload the code.

> **Image:** Selecting the correct Serial Port

5. When you successfully uploaded the example sketch, open the Serial Monitor of the Arduino IDE to see if it read the content, wrote new data, and erased the data from the Flash module. If you see the logs, as shown in **Figure 23**, then your RAK15001 is properly communicating to the WisBlock core.

> **Image:** RAK15001 Read, Write, and Erase data

