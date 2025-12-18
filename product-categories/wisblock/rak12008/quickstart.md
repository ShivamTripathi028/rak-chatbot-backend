---
slug: /product-categories/wisblock/rak12008/quickstart/
title: RAK12008 WisBlock CO2 Sensor Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK12008. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak12008/rak12008.png"
keywords:
  - quickstart
  - RAK12008
  - wisblock
sidebar_label: Quick Start Guide
---

# RAK12008 WisBlock CO2 Sensor Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step on using the RAK12008 WisBlock Module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK12008 WisBlock CO2 Sensor Module](https://store.rakwireless.com/products/wisblock-co2-sensor-rak12008?utm_source=RAK12008&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base?utm_source=WisBlockBase&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core?utm_source=WisBlockCore&utm_medium=Document&utm_campaign=BuyFromStore)
- USB Cable
- [Li-Ion/LiPo Battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar Charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install [Arduino IDE.](https://www.arduino.cc/en/Main/Software)
- To add the RAKwireless Core boards to your Arduino Boards Manager, install the [RAKwireless Arduino BSP.](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index)

## Product Configuration

### Hardware Setup

WisBlock can integrate this module, which makes it easy to build up an ambient light data acquisition system.

For more information about RAK12008, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak12008/datasheet/).

RAK12008 module can be connected to any sensor slots of [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) to communicate with the WisBlock Core, as shown in **Figure 1**. It will work on **SLOT A to F**. Also, always secure the connection of the WisBlock module by using compatible screws.

> **Image:** RAK12008 connection to WisBlock Base

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 2**, the locations for Slots A to F are properly marked by silkscreen. Follow carefully the procedure defined in [WisBlock Base board assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3 mm screws, depending on the module.

> **Image:** RAK12008 connection to WisBlock Base

##### Disassembling

The procedure for disassembling any type of WisBlock module is the same.

1. To begin disassembling, remove the screws.

> **Image:** Removing screws from the WisBlock module

2. After removing the screws, check the silkscreen of the module to find the correct location where force can be applied.

> **Image:** Detaching silkscreen on the WisBlock module

3. Detach the module from the base board by applying forcer to the module at the position of the connector, as shown in **Figure 5**.

> **Image:** Applying even forces on the proper location of a WisBlock module

:::tip NOTE
- If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool). This tool finds possible pin conflicts.
- RAK12008 uses I2C communication lines, which can cause possible conflict, especially on some IO modules.
:::

After all this setup, you can now connect the battery (optional) and USB cable to start programming your WisBlock Core.

:::warning
- Batteries can cause harm if not handled properly.
- Only 3.7-4.2 V rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5 V solar panels are supported. Do not use 12 V solar panels. It will destroy the charging unit and, eventually, other electronic parts.
- Make sure the battery wires match the polarity on the WisBlock Base board. Not all batteries have the same wiring.
:::

### Software Configuration and Example

#### Initial Test of the RAK12008 WisBlock Module

1. Install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index) for WisBlock by using the `package_rakwireless_index.json` board installation package. The WisBlock Core should now be available on the Arduino IDE.

2. After that, you need to select the WisBlock Core you have, as shown in **Figure 6** to **Figure 8**.

**RAK4631 Board**

> **Image:** Selecting RAK4631 as WisBlock Core

**RAK11200 Board**

> **Image:** Selecting RAK11200 as WisBlock Core

**RAK11310 Board**

> **Image:** Selecting RAK11310 as WisBlock Core

3. Next, copy the following sample code into your Arduino IDE:

<details>
<summary> Click to view the example </summary>
```c
/**
   @file RAK12008_CO2_BasicReadings_STC31.ino
   @author rakwireless.com
   @brief Read CO2 and temperature data of STC31, and output data through serial port.
   @version 0.1
   @date 2022-02-21
   @copyright Copyright (c) 2022
**/
#include <Wire.h>
#include "SparkFun_STC3x_Arduino_Library.h" // Click here to get the library: http://librarymanager/All#SparkFun_STC3x

#define STC31_ADDRESS     0x2C

STC3x mySensor;

void setup()
{
  pinMode(WB_IO2,OUTPUT);
  digitalWrite(WB_IO2,HIGH);  //power on RAK12008.

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
  Serial.println(F("STC31 Basic Readings Example."));
  Wire.begin();

  //mySensor.enableDebugging(); // Uncomment this line to get helpful debug messages on Serial.

  if (mySensor.begin(STC31_ADDRESS,Wire) == false)
  {
    while (1)
    {
      Serial.println("Sensor not detected. Please check wiring. Freezing...");
      delay(5000);
    }
  }

  /*
   * We need to tell the sensor what binary gas and full range we are using
   * Possible values are:
   * STC3X_BINARY_GAS_CO2_N2_100   : Set binary gas to CO2 in N2.  Range: 0 to 100 vol%
   * STC3X_BINARY_GAS_CO2_AIR_100  : Set binary gas to CO2 in Air. Range: 0 to 100 vol%
   * STC3X_BINARY_GAS_CO2_N2_25    : Set binary gas to CO2 in N2.  Range: 0 to 25 vol%
   * STC3X_BINARY_GAS_CO2_AIR_25   : Set binary gas to CO2 in Air. Range: 0 to 25 vol%
   */
  if (mySensor.setBinaryGas(STC3X_BINARY_GAS_CO2_AIR_25) == false)
  {
    while (1)
    {
      Serial.println("Could not set the binary gas! Freezing...");
      delay(5000);
    }
  }
}

void loop()
{
  if (mySensor.measureGasConcentration()) // measureGasConcentration will return true when fresh data is available.
  {
    Serial.print(F("CO2(%):"));
    Serial.print(mySensor.getCO2(), 2);

    Serial.print(F("\tTemperature(C):"));
    Serial.print(mySensor.getTemperature(), 2);

    Serial.println();
  }
  else
  {
    Serial.print(F("."));
  }

  delay(1000);
}
```
</details>

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated code for your WisBlock Core Module. You can find it on the [RAK12008 WisBlock Example Code Repository](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK12008). The sample code on GitHub will work on all WisBlock Core.
:::

4. Once the example code is open, install the [SparkFun STC3x](https://github.com/sparkfun/SparkFun_STC3x_Arduino_Library/tree/main) library. Click the highlighted link, as shown in **Figure 9** and **Figure 10**.

> **Image:** Accessing the library used for RAK12008 Module

> **Image:** Installing the compatible library for RAK12008 Module

5. After successful installation of the library, you can now select the right serial port and upload the code, as shown in **Figure 11** and **Figure 12**.

:::tip NOTE
If you're using the RAK11200 as your WisBlock Core, the RAK11200 requires the **Boot0** pin to be configured properly first before uploading. If not done properly, uploading the source code to RAK11200 will fail. Check the full details on the [RAK11200 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/#install-rakwireless-esp32-bsp-on-arduino-boards-manager).
:::

> **Image:** Selecting the correct Serial Port

> **Image:** Uploading the RAK12008 example code

6. When you have successfully uploaded the example sketch, open the serial monitor of the Arduino IDE to see the sensor's reading logs. If you see the logs, as shown in **Figure 13**, then your RAK12008 is properly communicating to the WisBlock core. In this example code, you will see CO2 concentration and temperature readings.

:::tip NOTE
RAK12008 is developed for high-concentration CO2 applications and not for common ambient air.
:::

> **Image:** RAK12008 Ambient Light data logs

