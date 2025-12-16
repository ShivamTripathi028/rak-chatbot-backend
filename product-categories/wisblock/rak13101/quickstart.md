---
slug: /product-categories/wisblock/rak13101/quickstart/
title: RAK13101 WisBlock GSM/GPRS Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK13101. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak13101/rak13101.png"
keywords:
  - quickstart
  - wisblock
  - RAK13101
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK13101 WisBlock GSM/GPRS Module Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step on using the RAK13101 WisBlock module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK13101](https://store.rakwireless.com/products/wisblock-gsm-module-rak13101?utm_source=RAK13101&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- GNSS and GSM Antennas
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)


#### Software

- Download and install [Arduino IDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino board, install the RAKwireless Arduino BSP. Follow the steps in the [GitHub repo](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

You can integrate the RAK13101 module on your WisBlock project to extend its functionality and have GSM/GPRS/GNSS capability. This is ideal for tracking applications with GSM/GPSR cellular connectivity in the area. For more information about RAK13101, refer to its [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak13101/datasheet/).

RAK13101 module can be mounted to the IO slot of the WisBlock Base and communicates to the WisBlock Core via UART. The module is activated via `WB_IO5` pin of the WisBlock Core. Two antennas must be connected to the module as well, one for the GNSS antenna port and one for the GSM antenna port. An external battery (Li-Ion/LiPo 3.7-4.2V) is also required to power up the module properly.

:::warning

- Batteries can cause harm if not handled properly.
- Only 3.7-4.2&nbsp;V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5&nbsp;V solar panels are supported. Do not use 12&nbsp;V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires match the polarity on the WisBlock Base board. Not all batteries have the same wiring.

:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13101/quickstart/rak13101_assembly.png" 
  figureCount="1"
  caption="RAK13101 connection to WisBlock Base" 
   width="80%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13101/quickstart/battery-connection.gif" 
  figureCount="2"
  caption="WisBlock Base RAK5005-O battery polarity and connection" 
   width="35%"
/>


#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 3**, the location for Slot A, B, C, and D are properly marked by silkscreen. Follow carefully the procedure defined in [RAK5005-O module assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3&nbsp;mm screws depending on the module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13101/quickstart/rak13101_mounting.png" 
  figureCount="3"
  caption="RAK13101 connection to WisBlock Base" 
   width="70%"
/>

##### Disassembling

The procedure in disassembling any type of WisBlock modules is the same.

1. Remove the screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13101/quickstart/16.removing-screws.png" 
  figureCount="4"
  caption="Removing screws from the WisBlock module" 
   width="70%"
/>

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13101/quickstart/17.detaching-silkscreen.png" 
  figureCount="5"
  caption="Detaching silkscreen on the WisBlock module" 
   width="70%"
/>

3. Apply force to the module at the position of the connector, as shown in **Figure 6**, to detach the module from the baseboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13101/quickstart/18.detaching-module.png" 
  figureCount="6"
  caption="Applying even forces on the proper location of a WisBlock module" 
   width="70%"
/>

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts. RAK13101 uses UART communication lines, and it can cause possible conflict especially on some modules that also use UART.
:::

### Software Configuration and Example

The RAK13101 WisBlock GSM/GPRS Module uses UART serial communication lines. In this example code, you will be able to send AT commands to the RAK13101 module. This will ensure that your RAK13101 is functional and ready for your IoT project.

#### Initial Test of the RAK13101 WisBlock Module

If you already installed the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index), the WisBlock Core and example code should now be available on the Arduino IDE.

1. You need to select first the WisBlock Core you have, as shown in **Figure 7** to **Figure 9**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13101/quickstart/rak4631_board.png" 
  figureCount="7"
  caption="Selecting RAK4631 as WisBlock Core" 
   width="100%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13101/quickstart/rak11200_board.png" 
  figureCount="8"
  caption="Selecting RAK11200 as WisBlock Core" 
   width="100%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13101/quickstart/rak11300_board.png" 
  figureCount="9"
  caption="Selecting RAK11300 as WisBlock Core" 
   width="100%"
/>

2. Next, copy the following sample code into your Arduino IDE:


<details>
<summary> Click to view the example </summary>

```c
/**
   @file Unvarnished_Transmission.ino
   @author rakwireless.com
   @brief unvarnished transmission via USB
   @version 0.1
   @date 2021-6-28
   @copyright Copyright (c) 2020
**/

#include <Wire.h>

#define POWER_KEY WB_IO5

void setup()
{
	time_t serial_timeout = millis();
	Serial.begin(115200);

	while (!Serial)
	{
		if ((millis() - serial_timeout) < 5000)
		{
            delay(100);
        }
        else
        {
            break;
        }
	}

	Serial.println("AT CMD TEST!");
	// Check if the modem is already awake
	time_t timeout = millis();
	bool moduleSleeps = true;
	Serial1.begin(9600);
	delay(1000);
	Serial1.println("ATI");
	//MC20 init
	while ((millis() - timeout) < 6000)
	{
		if (Serial1.available())
		{
			String result = Serial1.readString();
			Serial.println("Modem response after start:");
			Serial.println(result);
			moduleSleeps = false;
		}
	}
	if (moduleSleeps)
	{
		// Module slept, wake it up
    pinMode(POWER_KEY, OUTPUT);
		digitalWrite(POWER_KEY, 0);
		delay(200);
		digitalWrite(POWER_KEY, 1);
		delay(2000);
		digitalWrite(POWER_KEY, 0);
		delay(1000);
	}
	Serial.println("MC20 power up!");
}

void loop()
{
	int timeout = 100;
	String resp = "";
	String snd = "";
	char cArr[128] = {0};
	while (timeout--)
	{
		if (Serial1.available() > 0)
		{
			resp += char(Serial1.read());
		}
		if (Serial.available() > 0)
		{
			snd += char(Serial.read());
		}
		delay(1);
	}
	if (resp.length() > 0)
	{
		Serial.print(resp);
	}
	if (snd.length() > 0)
	{
		memset(cArr, 0, 128);
		snd.toCharArray(cArr, snd.length() + 1);
		Serial1.write(cArr);
		delay(10);
	}
	resp = "";
	snd = "";
}
```

</details>

3. You can now select the right serial port and upload the code, as shown in **Figure 10** and **Figure 11**.

:::tip NOTE
If you are using RAK11200 as WisBlock Core, you need to configure the BOOT0 pin before uploading. You need to short it to the ground then press the reset button of the WisBlock Base before releasing the BOOT0 pin. If not done properly, uploading the source code to RAK11200 will fail. Check the full details on the [RAK11200 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/#uploading-to-wisblock).
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13101/quickstart/select_port.png" 
  figureCount="10"
  caption="Selecting the correct Serial Port" 
   width="100%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13101/quickstart/upload.png" 
  figureCount="11"
  caption="Uploading the RAK13101 example code" 
   width="100%"
/>

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated code for the RAK13101 Module that can be found on the [WisBlock Example Code Repository](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/communications/Cellular/RAK13101_MC20_Module/Unvarnished_Transmission).
:::

4. When you successfully uploaded the example sketch, open the Serial Monitor of the Arduino IDE to see the initial logs, as shown in **Figure 12**. If you do not see any logs, you can try to disconnect the USB cable and battery, then reconnect again with the battery first. If you see that the LED of the RAK13101 is blinking after a few seconds, the module is now initialized properly.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13101/quickstart/basic_log.png" 
  figureCount="12"
  caption="RAK13101 initial logs" 
   width="100%"
/>

5. There are times that you might not see the initial logs if you open the Serial Monitor. The best way to test if the module is working is by sending actual AT commands, as shown in **Figure 13**. You can try to send the basic commands, `AT` and `ATI`.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13101/quickstart/at_logs.png" 
  figureCount="13"
  caption="RAK13101 AT and ATI command" 
   width="100%"
/>

<RkBottomNav/>

