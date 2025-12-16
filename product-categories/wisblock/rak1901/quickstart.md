---
slug: /product-categories/wisblock/rak1901/quickstart/
title: RAK1901 WisBlock Temperature and Humidity Sensor Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK1901. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak1901/rak1901.png"
keywords:
  - quickstart
  - wisblock
  - RAK1901
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK1901 WisBlock Temperature and Humidity Sensor Quick Start Guide



## Prerequisite

### What Do You Need?

Before going through each and every step on using the RAK1901 WisBlock module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK1901 WisBlock Temperature & Humidity Sensor](https://store.rakwireless.com/products/rak1901-shtc3-temperature-humidity-sensor?utm_source=RAK1901&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [RAK19005 WisBlock Sensor Extension Cable (optional)](https://store.rakwireless.com/products/fpc-extension-cable-for-slot-a-to-d-rak19005?utm_source=RAK19005&utm_medium=Document&utm_campaign=BuyFromStore)
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

##### Arduino

- Download and install [ArduinoIDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino Boards Manager, install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

WisBlock can integrate this module which makes it easy to build up an environmental temperature and humidity data acquisition system.

For more information about the RAK1901, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak1901/datasheet/).

The RAK1901 module gives information about:

- Environment Temperature
- Environment Humidity

RAK1901 module can be connected to the sensor's slot of [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) to communicate with the WisBlock Core, as shown in **Figure 1**. It will work on **SLOT A to F**. Also, always secure the connection of the WisBlock module by using compatible screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1901/quickstart/rak1901_assembly.png"
  figureCount="1"
  caption="RAK1901 connection to WisBlock Base" 
   width="70%"
/>

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 2**, the location for Slot A, B, C, and D are properly marked by silkscreen. Follow carefully the procedure defined in [WisBlock Base board module assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3&nbsp;mm screws depending on the module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1901/quickstart/wisblock-sensor-silkscreen.png"
  figureCount="2"
  caption="RAK1901 connection to WisBlock Base" 
   width="70%"
/>

##### Disassembling

The procedure in disassembling any type of WisBlock modules is the same.

1. Remove the screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1901/quickstart/removing-screws.png"
  figureCount="3"
  caption="Removing screws from the WisBlock module" 
   width="70%"
/>

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1901/quickstart/detaching-silkscreen.png"
  figureCount="4"
  caption="Detaching silkscreen on the WisBlock module" 
   width="70%"
/>

3. Apply force to the module at the position of the connector, as shown in **Figure 5**, to detach the module from the baseboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1901/quickstart/detaching-module.png"
  figureCount="5"
  caption="Applying even forces on the proper location of a WisBlock module" 
   width="70%"
/>

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts. RAK1901 uses I2C communication lines, and it can cause possible conflict especially on some IO modules.
:::

After all this setup, you can now connect the battery (optional) and USB cable to start programming your WisBlock Core.

:::warning
- Batteries can cause harm if not handled properly.
- Only 3.7-4.2&nbsp;V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5&nbsp;V solar panels are supported. Do not use 12&nbsp;V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires match the polarity on the WisBlock Base board. Not all batteries have the same wiring.
:::

### Software Configuration and Example

The RAK1901 is a Temperature & Humidity sensor board that contains the SHTC3 chip. The SHTC3 is a digital temperature and humidity sensor designed especially for battery-driven high-volume consumer electronics applications. The device comprises a sensing element and an IC interface which communicates through I2C from the sensing element to the application.

#### Initial Test of the RAK1901 WisBlock Module

1. Install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index) for WisBlock by using the `package_rakwireless_index.json` board installation package. The WisBlock Core should now be available on the Arduino IDE.

2. You need to select first the WisBlock Core you have.

**RAK4631 Board**

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1901/quickstart/rak4631-board.png"
  figureCount="6"
  caption="Selecting RAK4631 as WisBlock Core" 
   width="100%"
/>

**RAK11200 Board**

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1901/quickstart/rak11200-board.png"
  figureCount="7"
  caption="Selecting RAK11200 as WisBlock Core" 
   width="100%"
/>

**RAK11310 Board**

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1901/quickstart/rak11310-board.png"
  figureCount="8"
  caption="Selecting RAK11310 as WisBlock Core" 
   width="100%"
/>

3. Copy the following sample code into your Arduino IDE:

<details>
<summary> Click to view the code</summary>

```c
/**
   @file RAK1901_Temperature_Humidity_SHTC3.ino
   @author rakwireless.com
   @brief Setup and read values from a SHTC3 temperature and humidity sensor
   @version 0.1
   @date 2020-12-28
   @copyright Copyright (c) 2020
**/


#include "SparkFun_SHTC3.h" 		//Click here to get the library: http://librarymanager/All#SparkFun_SHTC3

SHTC3 g_shtc3;						      // Declare an instance of the SHTC3 class

void errorDecoder(SHTC3_Status_TypeDef message)   // The errorDecoder function prints "SHTC3_Status_TypeDef" resultsin a human-friendly way
{
  switch (message)
  {
    case SHTC3_Status_Nominal:
      Serial.print("Nominal");
      break;
    case SHTC3_Status_Error:
      Serial.print("Error");
      break;
    case SHTC3_Status_CRC_Fail:
      Serial.print("CRC Fail");
      break;
    default:
      Serial.print("Unknown return code");
      break;
  }
}

void shtc3_read_data(void)
{
	float Temperature = 0;
	float Humidity = 0;

	g_shtc3.update();
	if (g_shtc3.lastStatus == SHTC3_Status_Nominal) // You can also assess the status of the last command by checking the ".lastStatus" member of the object
	{

		Temperature = g_shtc3.toDegC();			          // Packing LoRa data
		Humidity = g_shtc3.toPercent();

		Serial.print("RH = ");
		Serial.print(g_shtc3.toPercent()); 			      // "toPercent" returns the percent humidity as a floating point number
		Serial.print("% (checksum: ");

		if (g_shtc3.passRHcrc) 						            // Like "passIDcrc" this is true when the RH value is valid from the sensor (but not necessarily up-to-date in terms of time)
		{
			Serial.print("pass");
		}
		else
		{
			Serial.print("fail");
		}

		Serial.print("), T = ");
		Serial.print(g_shtc3.toDegC()); 			        // "toDegF" and "toDegC" return the temperature as a flaoting point number in deg F and deg C respectively
		Serial.print(" deg C (checksum: ");

		if (g_shtc3.passTcrc) 						            // Like "passIDcrc" this is true when the T value is valid from the sensor (but not necessarily up-to-date in terms of time)
		{
			Serial.print("pass");
		}
		else
		{
			Serial.print("fail");
		}
		Serial.println(")");
	}
	else
	{
    Serial.print("Update failed, error: ");
		errorDecoder(g_shtc3.lastStatus);
		Serial.println();
	}
}

void setup()
{
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

	Wire.begin();
	Serial.println("shtc3 init");
	Serial.print("Beginning sensor. Result = "); // Most SHTC3 functions return a variable of the type "SHTC3_Status_TypeDef" to indicate the status of their execution
	errorDecoder(g_shtc3.begin());              // To start the sensor you must call "begin()", the default settings use Wire (default Arduino I2C port)
	Wire.setClock(400000);						          // The sensor is listed to work up to 1 MHz I2C speed, but the I2C clock speed is global for all sensors on that bus so using 400kHz or 100kHz is recommended
	Serial.println();

	if (g_shtc3.passIDcrc)                      // Whenever data is received the associated checksum is calculated and verified so you can be sure the data is true
	{					   						                    // The checksum pass indicators are: passIDcrc, passRHcrc, and passTcrc for the ID, RH, and T readings respectively
		Serial.print("ID Passed Checksum. ");
		Serial.print("Device ID: 0b");
		Serial.println(g_shtc3.ID, BIN); 		      // The 16-bit device ID can be accessed as a member variable of the object
	}
	else
	{
		Serial.println("ID Checksum Failed. ");
	}
}

void loop()
{
	shtc3_read_data();
	delay(1000);
}
```
</details>

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated code for your WisBlock Core Module that can be found on the [RAK1901 WisBlock Example Code Repository](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK1901_Temperature_Humidity_SHTC3) and this sample code in Github will work on all WisBlock Core.
:::

3. Once the example code is open, install the [SparkFun SHTC3](https://github.com/sparkfun/SparkFun_SHTC3_Arduino_Library) library by clicking the yellow highlighted link, as shown in **Figure 9** and **Figure 10**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1901/quickstart/rak1901-lib.png"
  figureCount="9"
  caption="Accessing the library used for RAK1901 Module" 
   width="100%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1901/quickstart/lib-install.png"
  figureCount="10"
  caption="Installing the compatible library for RAK1901 Module" 
   width="70%"
/>

4. After successful installation of the library, you can now select the right serial port and upload the code, as shown in **Figure 11** and **Figure 12**.

:::tip NOTE
If you are using the RAK11200 as your WisBlock Core, the RAK11200 requires the **Boot0** pin to be configured properly first before uploading. If not done properly, uploading the source code to RAK11200 will fail. Check the full details on the [RAK11200 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/#uploading-to-wisblock).
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1901/quickstart/rak4631-selectport.png"
  figureCount="11"
  caption="Selecting the correct Serial Port" 
   width="100%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1901/quickstart/upload.png"
  figureCount="12"
  caption="Uploading the RAK1901 example code" 
   width="100%"
/>

5. When you successfully uploaded the example sketch, open the Serial Monitor of the Arduino IDE to see the sensor's reading logs. If you see the logs, as shown in **Figure 13**, then your RAK1901 is properly communicating to the WisBlock core.


<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1901/quickstart/sensor-logs.png"
  figureCount="13"
  caption="RAK1901 temperature and humidity data logs" 
   width="80%"
/>


<RkBottomNav/>