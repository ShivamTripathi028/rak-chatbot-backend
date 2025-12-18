---
slug: /product-categories/wisblock/rak12031/quickstart/
title: RAK12031 WisBlock T-Beam-Fork Sensor Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK12031. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: https://images.docs.rakwireless.com/wisblock/rak12031/rak12031.png
keywords:
  - quickstart
  - wisblock
  - RAK12031
sidebar_label: Quick Start Guide
---

# RAK12031 WisBlock T-Beam-Fork Sensor Module Quick Start Guide

## Prerequisite

### Package Inclusions

Before going through each and every step on using the RAK12031 WisBlock module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK12031 WisBlock T-Beam-Fork Sensor Module](https://store.rakwireless.com/products/rak12028-rak12031-wisblock-through-beam-fork-sensor?utm_source=RAK12031&utm_medium=Document&utm_campaign=BuyFromStore)
- [RAK19005 FPC Sensor Extension Cable (optional)](https://store.rakwireless.com/products/fpc-extension-cable-for-slot-a-to-d-rak19005?utm_source=RAK19005&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install the [ArduinoIDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino board, install the RAKwireless Arduino BSP. Follow the steps in the [Github repo](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

RAK12031 is a WisBlock T-Beam-Fork (TBF) sensor module that is based on EE-SX1041 from Omron. It can detect the presence of small moving objects, measure the speed of rotation, linear motion, and more. RAK12031 is a separate TBF sensor and have two (2) connectors, which can be connected to the [RAK12028 TBF Connector module](https://docs.rakwireless.com/product-categories/wisblock/rak12028/overview/) or by using a [RAK19005 WisBlock Sensor Extension Cable](https://docs.rakwireless.com/product-categories/wisblock/rak19005/overview/) to connect it to the WisBlock Base.

For more information about RAK12031, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak12031/datasheet/).

RAK12031 module can be connected to the sensor's slot of [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) to communicate with the WisBlock Core, as shown in **Figure 1**. It will work on **SLOT A, C to F**. Also, always secure the connection of the WisBlock module by using compatible screws.

> **Image:** RAK12031 connection to WisBlock Base

> **Image:** RAK12031 connection to WisBlock Base using RAK19005 FPC Sensor Extension Cable

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 3**, the location for Slots A, B, C, and D are properly marked by silkscreen. Follow carefully the procedure defined in [WisBlock Base board assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3 mm screws depending on the module.

> **Image:** RAK12031 connection to WisBlock Base

##### Disassembling

The procedure in disassembling any type of WisBlock module is the same.

1. First, remove the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

> **Image:** Detaching silkscreen on the WisBlock module

3. Apply force to the module at the position of the connector, as shown in **Figure 6**, to detach the module from the baseboard.

> **Image:** Applying even forces on the proper location of a WisBlock module

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts.
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

#### Initial Test of the RAK12031 WisBlock Module

1. Install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index) for WisBlock by using the `package_rakwireless_index.json` board installation package. The WisBlock Core should now be available on the Arduino IDE.

2. You need to select first the WisBlock Core you have.

**RAK4631 Board**

> **Image:** Selecting RAK4631 as WisBlock Core

**RAK11200 Board**

> **Image:** Selecting RAK11200 as WisBlock Core

**RAK11310 Board**

> **Image:** Selecting RAK11310 as WisBlock Core

3. Next, copy the following sample code into your Arduino IDE:

<details>
<summary> Click to view the code </summary>

```c
/**
   @file RAK12031_T_Fork_SX1041.ino
   @author rakwireless.com
   @brief TBF example.
          Can detect presence of small objects.
          Can detect movement and rotation speed of a slot disk.
   @version 0.1
   @date 2021-10-18
   @copyright Copyright (c) 2020
**/

#include <Adafruit_TinyUSB.h>

// It use WB_IO2 to power up and is conflicting with singal pin, so better use in SlotA/SlotC/SlotD.
#define SINGAL_PIN          WB_IO1  // Connect with TBF out put pin.  Mount in SLOT A.
//#define SINGAL_PIN          WB_IO3  // Connect with TBF out put pin.  Mount in SLOT C.
//#define SINGAL_PIN          WB_IO5  // Connect with TBF out put pin.  Mount in SLOT D.

#define ROTATIONL_COUNT     20      // Adjust according to the code wheel used.

volatile uint32_t g_pulse_count=0;

void setup()
{
  pinMode(WB_IO2, OUTPUT);
  digitalWrite(WB_IO2, HIGH); // Enable power supply.

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
  Serial.println("TBF example.");

  pinMode(SINGAL_PIN,INPUT_PULLDOWN);  // Connect with TBF out put pin.
  attachInterrupt(digitalPinToInterrupt(SINGAL_PIN) ,pulse_INT_call_back ,FALLING);  // Enable interrupts.FALLING CHANGE

  Serial.println("Waiting for motion.");
}

void pulse_INT_call_back()
{
  g_pulse_count++;
}

void loop()
{
  float rotationl_speed = 0;
  Serial.print("Pulse count:");
  Serial.print(g_pulse_count);
  rotationl_speed = (float)g_pulse_count / (float)ROTATIONL_COUNT;
  g_pulse_count = 0;
  Serial.print("   ");
  Serial.print("Rotating speed:");
  Serial.print(rotationl_speed);
  Serial.print("[r/s]");
  Serial.print("   ");
  if( digitalRead(SINGAL_PIN) == LOW )
  {
    Serial.println("Object exists.");
  }
  else
  {
    Serial.println("Object not exists.");
  }
  delay(1000);
}

```
</details>

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated code for your WisBlock Core Module that can be found on the [RAK12031 WisBlock Example Code Repository](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/IO/RAK12031_T_Fork_SX1041) and this sample code in Github will work on all WisBlock Core.
:::

4. Once the example code is open, you can now select the right serial port and upload the code, as shown in **Figure 10** and **Figure 11**.

:::tip NOTE
If you are using the RAK11200 as your WisBlock Core, the RAK11200 requires the **Boot0** pin to be configured properly first before uploading. If not done properly, uploading the source code to RAK11200 will fail. Check the full details on the [RAK11200 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/#uploading-to-wisblock).
:::

> **Image:** Selecting the correct serial port

> **Image:** Uploading the RAK12031 example code

5. When you have successfully uploaded the example sketch, open the serial monitor of the Arduino IDE and set the baud rate correctly. You will be able to see the sensor's output, as shown in **Figure 12**. Try to place an object in the middle of the of T-Beam-Fork Sensor. If the presence of the object and the rotation speed, then your RAK12031 is properly communicating with the WisBlock core.

> **Image:** RAK12031 sensor serial readings

