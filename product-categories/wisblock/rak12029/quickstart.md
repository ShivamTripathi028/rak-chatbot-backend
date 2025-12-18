---
slug: /product-categories/wisblock/rak12029/quickstart/
title: RAK12029 WisBlock Inductive Sensor Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK12029. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: https://images.docs.rakwireless.com/wisblock/rak12029/rak12029.png
keywords:
  - quickstart
  - wisblock
  - RAK12029
sidebar_label: Quick Start Guide
---

# RAK12029 WisBlock Inductive Sensor Module Quick Start Guide

## Prerequisite

### Package Inclusions

Before going through each and every step on using the RAK12029 WisBlock Inductive Sensor Module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK12029 WisBlock Inductive Sensor Module](https://store.rakwireless.com/products/rak12029-wisblock-inductive-sensor?utm_source=RAK12029&utm_medium=Document&utm_campaign=BuyFromStore)
- [RAK19008 WisBlock IO Extension Cable (optional)](https://store.rakwireless.com/products/wisblock-io-extension-cable-rak19008?utm_source=RAK19008&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base) with IO slot
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)
#### Software

- Download and install the [Arduino IDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards to your Arduino project, install the RAKwireless Arduino BSP. Follow the steps in the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

RAK12029 module is part of the WisBlock Sensor category and extends the WisBlock system with an inductive sensor module. The RAK12029 connects to the WisBlock Base Board through the IO slot. **Figure 1** shows the assembly of a [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core) highlighted in green and the RAK12029 module highlighted in red.

Also, always secure the connection of the WisBlock module by using compatible screws. For more information about RAK12029, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak12029/datasheet/).

> **Image:** RAK12029 connection to WisBlock Base Board

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 2**, the location for the IO slot is properly marked by silkscreen. Follow carefully the procedure defined in [WisBlock Base board assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3 mm screws depending on the module.

> **Image:** RAK12029 connection to WisBlock Base Board

##### Disassembling

The procedure in disassembling any type of WisBlock module is the same.

1. First, remove the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

> **Image:** Detaching silkscreen on the WisBlock module

3. Apply force to the module at the position of the connector, as shown in **Figure 5**, to detach the module from the baseboard.

> **Image:** Applying even forces on the proper location of a WisBlock module

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts. RAK12029 uses I2C and IO pins that can cause possible conflict with other modules.
:::

After all this setup, you can now connect the battery(optional) and USB cable to start programming your WisBlock Core.

:::warning
- Batteries can cause harm if not handled properly.
- Only 3.7-4.2 V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5 V solar panels are supported. Do not use 12 V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires match the polarity on the WisBlock Base board. Not all batteries have the same wiring.
:::

### Software Configuration and Example

RAK12029 is a metal detection sensor module based on the LDC1614 from Texas Instruments. The LDC1614 is an inductance-to-digital converter (LDC) that measures the oscillation frequency of four LC resonators. It outputs a digital value, that is, proportional to frequency, with 28 bits of measurement resolution. With this digital value, you can detect the presence of metallic objects.

#### Initial Test of the RAK12029 WisBlock Inductive Sensor Module

1. Install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index) for WisBlock by using the `package_rakwireless_index.json` board installation package. The WisBlock Core should now be available on the Arduino IDE.

2. You need to select first the WisBlock Core you have, as shown in **Figure 6** to **Figure 8**.

**RAK4631 Board**

> **Image:** Selecting RAK4631 as WisBlock Core

**RAK11200 Board**

> **Image:** Selecting RAK11200 as WisBlock Core

**RAK11310 Board**

> **Image:** Selecting RAK11300 as WisBlock Core

3. Copy the example code below:

<details>
<summary> Click to view the code </summary>
```c
/**
   @file Single_channel_detection.ino
   @author rakwireless.com
   @brief  Metallic object detected
   @version 1.0
   @date 2021-11-17
   @copyright Copyright (c) 2021
**/
#include "RAK12029_LDC1614.h"  // Click to install library: http://librarymanager/All#RAK12029_LDC1614

#define INDUCTANCE   13.000
#define CAPATANCE    100.0
#define GETCHANNEL   LDC1614_CHANNEL_0 //LDC1614_CHANNEL_(0~3)
RAK12029_LDC1614_Inductive ldc;

void setup()
{
  pinMode(LED_BLUE, OUTPUT);
  digitalWrite(LED_BLUE, LOW);

  //Sensor power switch
  pinMode(WB_IO2, OUTPUT);
  digitalWrite(WB_IO2, HIGH);
  delay(300);

  //control chip switch
  pinMode(WB_IO5, OUTPUT);
  digitalWrite(WB_IO5, LOW);
  // Initialize Serial for debug output
  time_t timeout = millis();
  Serial.begin(115200);
  while (!Serial)
  {
    if ((millis() - timeout) < 5000)
    {
      delay(100);
    }
    else
    {
      break;
    }
  }
  Serial.println("RAK12029 TEST");
  delay(1000);
  ldc.LDC1614_init();
  /*single channel use case configuration.*/
  if (ldc.LDC1614_single_channel_config(GETCHANNEL, INDUCTANCE, CAPATANCE))
  {
    Serial.println("can't detect sensor!");
    while (1) delay(100);
  }
}

void loop()
{
  u16 value = 0;
  ldc.IIC_read_16bit(LDC1614_READ_DEVICE_ID, &value);
  if (value == 0x3055)
  {
    u32 ChannelData = 0;
    /*Get channel 0 result and parse it.*/
    delay(100);
    if (ldc.LDC1614_get_channel_result(GETCHANNEL, &ChannelData) == 0)
    {
      /*sensor result value.you can make a lot of application according to its changes.*/
      if (0 != ChannelData)
      {
        Serial.printf("The result channel%d is:%d\r\n", 4 - GETCHANNEL, ChannelData);
        digitalWrite(LED_BLUE, HIGH);
      }
      delay(1000);
      digitalWrite(LED_BLUE, LOW);
    }
  }
  else
  {
    Serial.println("The IIC communication fails,please reset the sensor!");
    delay(500);
  }
}

```
</details>

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated code for your WisBlock Core Module that can be found on the [RAK12029 WisBlock Example Code Repository](https://github.com/RAKWireless/RAK12029-LDC1614/tree/main/examples) and this sample code in Github will work on all WisBlock Core.
:::

4. Install the [RAKwireless Inductive Sensor Module Library](https://github.com/RAKWireless/RAK12029-LDC1614)library by clicking the red-highlighted link then click install, as shown in **Figure 9** and **Figure 10**.

> **Image:** Getting the library of RAK12029

> **Image:** Installing the library of RAK12029

5. Then select the right serial port and upload the code, as shown in **Figure 11** and **Figure 12**.

:::tip NOTE
If you are using the RAK11200 as your WisBlock Core, the RAK11200 requires the **Boot0** pin to be configured properly first before uploading. If not done properly, uploading the source code to RAK11200 will fail. Check the full details on the [RAK11200 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/#uploading-to-wisblock).
:::

> **Image:** Selecting the correct serial port

> **Image:** Uploading the sample code

6. When you have successfully uploaded the sample code, place any metal or coin in the sensor, as shown in **Figure 13**. Then, you can open up your serial monitor to get the sensor readings, as shown in **Figure 14**.

> **Image:** Testing the RAK12029 Inductive Sensor Module

> **Image:** RAK12029 Inductive Sensor Module readings in the serial monitor

