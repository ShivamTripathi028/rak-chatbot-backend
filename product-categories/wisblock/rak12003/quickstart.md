---
slug: /product-categories/wisblock/rak12003/quickstart/
title: RAK12003 WisBlock Infrared Temperature Sensor Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK12003. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak12003/rak12003.png"
keywords:
    - RAK12003
    - wisblock
    - quickstart
sidebar_label: Quick Start Guide
---

# RAK12003 WisBlock Infrared Temperature Sensor Module Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step on using the RAK12003 WisBlock module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK12003 WisBlock Infrared Temperature Sensor Module](https://store.rakwireless.com/products/infrared-temperature-sensor-rak12003?utm_source=WisBlockRAK12003&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install [Arduino IDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino board, install the RAKwireless Arduino BSP. Follow the steps in the [GitHub repo](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

WisBlock can integrate this module which extends the WisBlock system with an infrared temperature sensor.

For more information about RAK12003, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak12003/datasheet/).

The RAK12003 module gives us information about:

- Object temperatures between -20 °C and 100 °C
- Accuracy ±0.2 °C within the narrow object temperature range from 35 °C to 42 °C (medical applications)

RAK12003 module can be connected to the sensor's slot of [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) to communicate with the WisBlock Core, as shown in **Figure 1**. It will work on **SLOT A, C to F**. Also, always secure the connection of the WisBlock module by using compatible screws.

> **Image:** RAK12003 connection to WisBlock Base

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 2**, the location for Slot A, B, C, and D are properly marked by silkscreen. Follow carefully the procedure defined in [WisBlock Base board assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3 mm screws depending on the module.

> **Image:** RAK12003 connection to WisBlock Base

##### Disassembling

The procedure in disassembling any type of WisBlock modules is the same.

1. First, remove the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

> **Image:** Detaching silkscreen on the WisBlock module

3. Apply force to the module at the position of the connector, as shown in **Figure 5**, to detach the module from the baseboard.

> **Image:** Applying even forces on the proper location of a WisBlock module

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts. RAK12003 uses I2C communication lines, and it can cause possible conflict especially on some IO modules.
:::

After all this setup, you can now connect the battery and USB cable to start programming your WisBlock Core.

### Software Configuration and Example

The RAK12003 WisBlock Infrared Temperature Sensor Module is part of the RAKwireless WisBlock Series. It can be used for an accurate contactless thermal measurement for applications such as General purpose industry, temperature control of moving and hard to reach parts, body temperature measurement, non-contact thermometer for mobile and IoT application, with digital I2C/SPI serial interface standard output.

#### Initial Test of the RAK12003 WisBlock Module

1. Install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index) for WisBlock by using the `package_rakwireless_index.json` board installation package. The WisBlock Core should now be available on the Arduino IDE.

2. You need to select first the WisBlock Core you have, as shown in **Figure 6** to **Figure 8**.

> **Image:** Selecting RAK4631 as WisBlock Core

> **Image:** Selecting RAK11200 as WisBlock Core

> **Image:** Selecting RAK11300 as WisBlock Core

3. Next, copy the following sample code into your Arduino IDE:

<details>
<summary> Click to view the example </summary>
```c
/**
 * @file RAK12003_FIR_MLX90632.ino
 * @author rakwireless
 * @brief This example shows how to read both the remote object temperature and the local sensor temperature.
 * and prints out the temperature data to the Serial console.
 * @version 0.1
 * @date 2021-01-20
 *
 * @copyright Copyright (c) 2021
 */

#include <Wire.h>

#include "SparkFun_MLX90632_Arduino_Library.h"   // Click here to get the library: http://librarymanager/AllSparkFun_MLX90632_Arduino_Library
#define MLX90632_ADDRESS 0x3A
MLX90632 RAK_TempSensor;

void setup()
{
  TwoWire &wirePort = Wire;
  MLX90632::status returnError;
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
  Serial.println("MLX90632 Read Example");

  Wire.begin(); //I2C init

  if (RAK_TempSensor.begin(MLX90632_ADDRESS, wirePort, returnError) == true) //MLX90632 init
  {
     Serial.println("MLX90632 Init Succeed");
  }
  else
  {
     Serial.println("MLX90632 Init Failed");
  }
}

void loop()
{
  float object_temp = 0;
  object_temp = RAK_TempSensor.getObjectTempF(); //Get the temperature of the object we're looking at
  Serial.print("Object temperature: ");
  Serial.print(object_temp, 2);
  Serial.print(" F");

  float sensor_temp = 0;
  sensor_temp = RAK_TempSensor.getSensorTemp(); //Get the temperature of the sensor
  Serial.print(" Sensor temperature: ");
  Serial.print(sensor_temp, 2);
  Serial.print(" C");

  Serial.println();
}

```
</details>

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated code for your WisBlock Core Module that can be found on the [RAK12003 WisBlock Example Code Repository](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK12003_FIR_MLX90632). This sample code in Github will work on all WisBlock Core.
:::

4. Once the example code is open, install the [SparkFun MLX90632](https://github.com/sparkfun/SparkFun_MLX90632_Arduino_Library) library by clicking the yellow highlighted link, as shown in **Figure 9** and **Figure 10**.

> **Image:** Accessing the library used for RAK12003 Module

> **Image:** Installing the compatible library for RAK12003 Module

5. After successful installation of the library, you can now select the right serial port and upload the code, as shown in **Figure 11** and **Figure 12**.

:::tip NOTE
If you are using the RAK11200 as your WisBlock Core, the RAK11200 requires the **Boot0** pin to be configured properly first before uploading. If not done properly, uploading the source code to RAK11200 will fail. Check the full details on the [RAK11200 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/#uploading-to-wisblock).
:::

> **Image:** Selecting the correct Serial Port

> **Image:** Uploading the RAK12003 example code

6. When you successfully uploaded the example sketch, open the Serial Monitor of the Arduino IDE to see the sensor's reading logs. If you see the logs, as shown in **Figure 13**, then your RAK12003 is properly communicating to the WisBlock core.

> **Image:** RAK12003 sensor data logs

