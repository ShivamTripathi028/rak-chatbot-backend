---
slug: /product-categories/wisblock/rak12052/quickstart/
title: RAK12052 WisBlock Thermal IR Array Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK12052. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: https://images.docs.rakwireless.com/wisblock/rak12052/rak12052.png
keywords:
    - RAK12052
    - wisblock
    - quickstart
sidebar_label: Quick Start Guide
---

# RAK12052 WisBlock Thermal IR Array Module Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step of using the RAK12052 WisBlock Thermal IR Array Module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK12052 WisBlock Thermal IR Array Module](https://store.rakwireless.com/collections/wisblock-sensor)
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

RAK12052 is a 32 x 24 thermal IR array module based on MLX90640 from Melexis. MLX90640 is a fully-calibrated 32 x 24 pixels thermal IR array in an industry-standard 4-lead TO39 package with a digital interface. The MLX90640 contains 768 FIR pixels.

For more information about RAK12052, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak12052/datasheet/).

RAK12052 module can be connected to the IO slot of the WisBlock Base to communicate with the WisBlock Core. Always secure the connection of the WisBlock module by using compatible screws.

> **Image:** RAK12052 connection to WisBlock Base

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 2**, the location for the IO slot is properly marked by silkscreen. Follow carefully the procedure defined in [WisBlock Base board assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3 mm screws depending on the module.

> **Image:** RAK12052 connection to WisBlock Base

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
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts. RAK12052 uses I2C communication lines, and it can cause possible conflicts, especially on other WisBlock Modules connected to Slot A to F of the WisBlock Base.
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

The RAK12052 design is based on **MLX90640** from Melexis. MLX90640 is a fully-calibrated 32 x 24 pixels thermal IR array in an industry-standard 4-lead TO39 package with a digital interface. The MLX90640 contains 768 FIR pixels. An ambient sensor is integrated to measure the ambient temperature of the chip and a supply sensor to measure the VDD. The outputs of all sensors (IR, Ta, and VDD) are stored in internal RAM and accessible through I2C. It is comparable to having a thermal camera (or Predator's vision) but in compact but usable low resolution. For this example, you will be using the **RAK4631** as your WisBlock Core.

#### Initial Test of the RAK12052 WisBlock Module

1. Install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index) for WisBlock by using the `package_rakwireless_index.json` board installation package. The WisBlock Core should now be available on the Arduino IDE.

> **Image:** Arduino IDE

> **Image:** WisBlock Cores inside the Arduino IDE

2. Then install the library of **RAK12052** into your Arduino IDE.

> **Image:** Managing libraries inside the Arduino IDE

> **Image:** RAK12052 Library

3. Then open the sample code for **RAK12052**.

> **Image:** Selecting the sample code for RAK12052

> **Image:** Sample code for RAK12052

4. Then select the **RAK4631** board and its serial port, as shown in **Figure 13** and **Figure 14**.

> **Image:** Selecting RAK4631 board as the WisBlock Core

> **Image:** Selecting the serial port of RAK4631 WisBlock Core

:::tip NOTE
If you are using the RAK11200 as your WisBlock Core, the RAK11200 requires the **Boot0** pin to be configured properly first before uploading. If not done properly, uploading the source code to RAK11200 will fail. Check the full details on the [RAK11200 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/#uploading-to-wisblock).
:::

1. Then upload the code as shown in **Figure 15** and **Figure 16**.

> **Image:** Uploading the RAK12052 sample code

> **Image:** Uploading the RAK12052 sample code

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated code for the RAK12052 WisBlock Thermal IR Array module that can be found on the [RAK12052 WisBlock Example Code Repository](https://github.com/RAKWireless/RAK12052-MLX90640).
:::

6. When you successfully uploaded the sample code, open the Serial Monitor of the Arduino IDE to monitor the thermal IR array module reading logs.

> **Image:** Sample code successfully uploaded to RAK4631

> **Image:** Readings from the Serial Monitor

