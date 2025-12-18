---
slug: /product-categories/wisblock/rak12037/quickstart/
title: RAK12037 WisBlock CO2 Sensor Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK12037. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: https://images.docs.rakwireless.com/wisblock/rak12037/rak12037.png
keywords:
    - RAK12037
    - wisblock
    - quickstart
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK12037 WisBlock CO2 Sensor Module Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step on using the RAK12037 WisBlock CO2 Sensor Module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK12037 WisBlock CO2 Sensor Module](https://store.rakwireless.com/products/co2-sensor-sensirion-scd30-rak12037?utm_source=RAK12037&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base) with IO slot
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [RAK19008 WisBlock IO Extension Cable (optional)](https://store.rakwireless.com/products/wisblock-io-extension-cable-rak19008?utm_source=RAK19008&utm_medium=Document&utm_campaign=BuyFromStore)
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install the [Arduino IDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino board, install the RAKwireless Arduino BSP. Follow the steps in the [GitHub repo](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

RAK12037 is a WisBlock Sensor that extends the WisBlock system based on the SCD30 module. This module uses NDIR CO2 sensor technology to sense CO2 and has an integrated temperature and humidity sensor. Ambient humidity and temperature can be measured by monitoring and compensating for external heat sources without the need for additional components. The small module height allows easy integration into different applications. The SCD30 features dual-channel detection for superior stability and ±30&nbsp;ppm + 3% accuracy.

For more information about RAK12037, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak12037/datasheet/).

RAK12037 module can be connected to the IO slot of [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) to communicate with the WisBlock Core, as shown in **Figure 1**. Also, always secure the connection of the WisBlock module by using compatible screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12037/quickstart/rak12037-assembly.png"
  figureCount="1"
  caption="RAK12037 connection to WisBlock Base" 
   width="70%"
/>


#### Assembling and Disassembling of WisBlock Modules

##### Assembling

The RAK12037 module can be mounted on the IO slot of the WisBlock Base Board, as shown in **Figure 2**. Also, always secure the connection of the WisBlock module by using compatible screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12037/datasheet/rak12037-mount.png"
  figureCount="2"
  caption="RAK12037 mounting connection to WisBlock Base module" 
   width="60%"
/>

##### Disassembling

The procedure in disassembling any type of WisBlock module is the same.

1. First, remove the screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12037/quickstart/removing_screw.png"
  figureCount="3"
  caption="Removing screws from the WisBlock module" 
   width="70%"
/>

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12037/quickstart/detaching-silkscreen.png"
  figureCount="4"
  caption="Detaching silkscreen on the WisBlock module" 
   width="70%"
/>

3. Apply force to the module at the position of the connector, as shown in **Figure 5**, to detach the module from the baseboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12037/quickstart/detach_module.png"
  figureCount="5"
  caption="Applying even forces on the proper location of a WisBlock module" 
   width="70%"
/>

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts.
:::

After all this setup, you can now connect the battery (optional) and USB cable to start programming your WisBlock Core.

:::warning 
- Batteries can cause harm if not handled properly.
- Only 3.7-4.2&nbsp;V rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5&nbsp;V solar panels are supported. Do not use 12&nbsp;V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires match the polarity on the WisBlock Base board. Not all batteries have the same wiring.
:::

### Software Configuration and Example

#### Initial Test of the RAK12037 WisBlock Module

1. Install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index) for WisBlock by using the `package_rakwireless_index.json` board installation package. The WisBlock Core should now be available on the Arduino IDE.

2. You need to select first the WisBlock Core you have.

**RAK4631 Board**

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12037/quickstart/rak4631-board.png"
  figureCount="6"
  caption="Selecting RAK4631 as WisBlock Core" 
   width="100%"
/>

**RAK11200 Board**

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12037/quickstart/rak11200-board.png"
  figureCount="7"
  caption="Selecting RAK11200 as WisBlock Core" 
   width="100%"
/>

**RAK11310 Board**

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12037/quickstart/rak11310-board.png"
  figureCount="8"
  caption="Selecting RAK11310 as WisBlock Core" 
   width="100%"
/>

3. Next, copy the following sample code into your Arduino IDE:

<details>
<summary> Click to view the code </summary>

```c
/**
   @file RAK12037_BasicReadings_SCD30.ino
   @author rakwireless.com
   @brief  Example of reading SCD30 sensor and displaying data through serial port.
   @version 0.1
   @date 2022-1-18
   @copyright Copyright (c) 2022
**/

#include <Wire.h>

#include "SparkFun_SCD30_Arduino_Library.h" // Click here to get the library: http://librarymanager/All#SparkFun_SCD30

SCD30 airSensor;

void setup()
{
  pinMode(WB_IO2, OUTPUT);
  digitalWrite(WB_IO2, HIGH);

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

  Serial.println("SCD30 Basic Readings Example.");

  Wire.begin();

  delay(500);

  if (airSensor.begin() == false)
  {
    Serial.println("Air sensor not detected. Please check wiring. Freezing...");
		while (1)
		{
			delay(10);
		}
  }
}

void loop()
{
  if (airSensor.dataAvailable())
  {
    Serial.print("co2(ppm):");
    Serial.print(airSensor.getCO2());

    Serial.print(" temp(C):");
    Serial.print(airSensor.getTemperature(), 1);

    Serial.print(" humidity(%):");
    Serial.print(airSensor.getHumidity(), 1);

    Serial.println();
  }
  else
    Serial.println("Waiting for new data");

  delay(3000);
}
```
</details>

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated code for your WisBlock Core Module that can be found on the [RAK12037 WisBlock Example Code Repository](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/IO/RAK12037_CO2_SCD30) and this sample code in GitHub will work on all WisBlock Core.
:::

4. Once the example code is open, install the [SparkFun_SCD30](https://github.com/sparkfun/SparkFun_SCD30_Arduino_Library) library by clicking the yellow highlighted link, as shown in **Figure 9** and **Figure 10**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12037/quickstart/rak12037-lib.png"
  figureCount="9"
  caption="Accessing the library used for RAK12037 Module" 
   width="100%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12037/quickstart/rak12037-libinstall.png"
  figureCount="10"
  caption="Installing the compatible library for RAK12037 Module" 
   width="100%"
/>

5. After the successful installation of the library, you can now select the right serial port and upload the code, as shown in **Figure 11** and **Figure 12**.

:::tip NOTE
If you're using the RAK11200 as your WisBlock Core, the RAK11200 requires the **Boot0** pin to be configured properly first before uploading. If not done properly, uploading the source code to RAK11200 will fail. Check the full details on the [RAK11200 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/#uploading-to-wisblock).
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12037/quickstart/select-port.png"
  figureCount="11"
  caption="Selecting the correct Serial Port" 
   width="100%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12037/quickstart/upload.png"
  figureCount="12"
  caption="Uploading the RAK12037 example code" 
   width="100%"
/>

6. When you have successfully uploaded the example sketch, open the serial monitor of the Arduino IDE and set the baud rate correctly. You will then see the sensor's output, as shown in **Figure 13**. Therefore, your RAK12037 is properly communicating with the WisBlock core.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12037/quickstart/rak12037-data.png"
  figureCount="13"
  caption="RAK12037 CO2 Sensor Serial Readings" 
   width="100%"
/>

<RkBottomNav/>