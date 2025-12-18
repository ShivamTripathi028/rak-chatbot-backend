---
slug: /product-categories/wisblock/rak15000/quickstart/
title: RAK15000 WisBlock EEPROM Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK15000. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak15000/rak15000.png"
keywords:
  - quickstart
  - wisblock
  - RAK15000
sidebar_label: Quick Start Guide
---

# RAK15000 WisBlock EEPROM Module Quick Start Guide

## Prerequisite

Before going through each and every step on using the RAK15000 WisBlock module, make sure to prepare the necessary items listed below:

### Hardware

- [RAK15000 WisBlock EEPROM Module](https://store.rakwireless.com/products/wisblock-eeprom-module-rak15000?utm_source=WisBlockRAK15000&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

### Software

- Download and install [Arduino IDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino Boards Manager, install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

WisBlock can integrate this module which makes it easy for you to save a lot of data, making it readily available to applications that need to access it frequently. The RAK15000 EEPROM Memory module has 1,000,000 write cycles, so it can be used to store constantly changing data.

For more information about RAK15000, refer to the [Datasheet](datasheet.md).

The RAK15000 module can be connected to any slot of WisBlock Base to communicate with the WisBlock Core. It will work on **SLOT A, B, C, or D**. Also, always secure the connection of the WisBlock module by using compatible screws.

> **Image:** RAK15000 connection to WisBlock Base

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 2**, the location for Slot A, B, C, and D are properly marked by silkscreen. Follow carefully the procedure defined in [RAK5005-O module assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with one or more M1.2 x 3 mm screws, depending on the module.

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
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts. RAK15000 uses I2C communication lines, and it can cause possible conflict especially on some IO modules. For instance, if you are planning to use it in conjunction with the [EPD module](https://store.rakwireless.com/products/wisblock-epd-module-rak14000?utm_source=WisBlockRAK14000&utm_medium=Document&utm_campaign=BuyFromStore), which uses all IO pins, you would have to forego the 3-key keypad (uses IO 3, 5 and 6) and put the EEPROM module on slot D (has IO 5 & 6).
:::

After all this setup, you can now connect the battery (optional) and USB cable to start programming your WisBlock Core.

### Software Configuration and Example

The RAK15000 EEPROM has an I2C-Compatible (Two-Wire) Serial Interface. Furthermore, the EEPROM is organized in so-called pages. One page holds 256-byte and there are 1024 pages. Having insight into how the memory cells are organized is important for write and erase operations.

These are the quick links that go directly to the software guide for the specific WisBlock Core module you use:

- [RAK15000 WisBlock EEPROM Module Quick Start Guide](#rak15000-wisblock-eeprom-module-quick-start-guide)
  - [Prerequisite](#prerequisite)
    - [Hardware](#hardware)
    - [Software](#software)
  - [Product Configuration](#product-configuration)
    - [Hardware Setup](#hardware-setup)
      - [Assembling and Disassembling of WisBlock Modules](#assembling-and-disassembling-of-wisblock-modules)
        - [Assembling](#assembling)
        - [Disassembling](#disassembling)
    - [Software Configuration and Example](#software-configuration-and-example)
      - [RAK15000 in RAK4631 WisBlock Core Guide](#rak15000-in-rak4631-wisblock-core-guide)
      - [RAK15000 in RAK11200 WisBlock Core Guide](#rak15000-in-rak11200-wisblock-core-guide)
      - [RAK15000 in RAK11310 WisBlock Core Guide](#rak15000-in-rak11310-wisblock-core-guide)

#### RAK15000 in RAK4631 WisBlock Core Guide

Install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

1. Now, select the RAK4631 WisBlock Core, as shown in **Figure 6**.

> **Image:** Selecting RAK4631 as the WisBlock Core

2. Open the RAK15000 sample code.

You can open the example code for RAK4631 WisBlock Core, as shown in **Figure 7**.

> **Image:** Opening the RAK15000 example code for the RAK4631 WisBlock Core

3. Install **Adafruit FRAM_I2C** Library.

Once the example code is opened, install the latest version of [Adafruit FRAM_I2C](https://github.com/adafruit/Adafruit_FRAM_I2C) library by clicking the link highlighted in yellow, as shown in **Figure 8**.

> **Image:** Opening Adafruit EEPROM library

To finish the library installation, click on the **Install** button highlighted in yellow, as shown in **Figure 9**.

> **Image:** Installing the Adafruit EEPROM library

4. After successful installation of the library, you can now select the right serial port and upload the code, as shown in **Figure 10** and **Figure 11**.

> **Image:** Selecting the correct Serial Port

> **Image:** Uploading the RAK15000 example code

The sketch writes a value to a random address. Then it checks the read value and compares it with the written value.

After successful upload, a random number will be written and read to a random address five times.

> **Image:** RAK15000 example code logs

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated code for the RAK4630 WisBlock Core Module that can be found on the [RAK4630 WisBlock Example Code Repository](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK15000_EEPROM_AT24C02).
:::

#### RAK15000 in RAK11200 WisBlock Core Guide

Install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

1. Now, select the RAK11200 WisBlock Core, as shown in **Figure 13**.

> **Image:** Selecting RAK11200 as the WisBlock Core

2. Open the RAK15000 sample code.

You can open the example code for RAK11200 WisBlock Core, as shown in **Figure 14**.

> **Image:** Opening the RAK15000 example code for the RAK4631 WisBlock Core

3. Install **Adafruit FRAM_I2C** Library.

Once the example code is open, install the latest version of [Adafruit FRAM_I2C](https://github.com/adafruit/Adafruit_FRAM_I2C) library by clicking the link highlighted in yellow, as shown in **Figure 15**.

> **Image:** Opening the Adafruit EEPROM library

To finish the library installation, click on the **Install** button highlighted in yellow, as shown in **Figure 16**.

> **Image:** Installing the Adafruit EEPROM library

4. After successful installation of the library, you can now select the right serial port and upload the code, as shown in **Figure 17** and **Figure 19**.

> **Image:** Selecting the correct Serial Port

Before uploading your sketch, short circuit BOOT0 and GND pin, and press the reset button. Then click the Upload button as shown below.

> **Image:** Force ESP32 Download mode

> **Image:** Uploading the RAK15000 example code

The sketch writes a value to a random address. Then it checks the read value and compares it with the written value.

After successful upload, a random number will be written and read to a random address five times.

> **Image:** RAK15000 example code logs

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated code for the RAK11200 WisBlock Core Module that can be found on the [RAK11200 WisBlock Example Code Repository](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK15000_EEPROM_AT24C02).
:::

#### RAK15000 in RAK11310 WisBlock Core Guide

Install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

1. Now, select the RAK11310 WisBlock Core, as shown in **Figure 21**.

> **Image:** Selecting RAK11310 as the WisBlock Core

2. Open the RAK15000 sample code.

You can open the example code for RAK11200 WisBlock Core, as shown in **Figure 22**.

> **Image:** Opening the RAK15000 example code for the RAK4631 WisBlock Core

3. Install **Adafruit FRAM_I2C** Library.

Once the example code is open, install the latest version of [Adafruit FRAM_I2C](https://github.com/adafruit/Adafruit_FRAM_I2C) library by clicking the link highlighted in yellow, as shown in **Figure 23**.

> **Image:** Opening the Adafruit EEPROM library

To finish the library installation, click on the **Install** button highlighted in yellow, as shown in **Figure 24**.

> **Image:** Installing the Adafruit EEPROM library

4. After successful installation of the library, you can now select the right serial port and upload the code, as shown in **Figure 25** and **Figure 26**.

> **Image:** Selecting the correct Serial Port

> **Image:** Uploading the RAK15000 example code

The sketch writes a value to a random address. Then it checks the read value and compares it with the written value.

After successful upload, a random number will be written and read to a random address five times.

> **Image:** RAK15000 example code logs

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated code for the RAK11300 WisBlock Core Module that can be found on the [RAK11300 WisBlock Example Code Repository](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK15000_EEPROM_AT24C02).
:::

