---
slug: /product-categories/wisblock/rak12007/quickstart/
title: RAK12007 WisBlock Ultrasonic Sensor Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK12007. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak12007/rak12007.png"
keywords:
  - quickstart
  - wisblock
  - RAK12007
sidebar_label: Quick Start Guide
---

# RAK12007 WisBlock Ultrasonic Sensor Module Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step on using the RAK12007 WisBlock Ultrasonic Sensor Module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK12007 WisBlock Ultrasonic Sensor Module](https://store.rakwireless.com/products/ultrasonic-sensor-module-rak12007?utm_source=RAK12007&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base) with IO slot
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [RAK1921 WisBlock OLED Display](https://store.rakwireless.com/products/rak1921-oled-display-panel?utm_source=RAK1921&utm_medium=Document&utm_campaign=BuyFromStore)
- [RAK19008 WisBlock IO Extension Cable (optional)](https://store.rakwireless.com/products/wisblock-io-extension-cable-rak19008?utm_source=RAK19008&utm_medium=Document&utm_campaign=BuyFromStore)
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install [ArduinoIDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino Boards Manager, install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

The RAK12007, a part of WisBlock Sensor, is an ultrasonic sensor module based on the CS100, an industrial-grade ultrasonic distance measurement chip. This chip integrates an ultrasonic transmitter, ultrasonic receiver, and digital processing circuits. The distance measurement result output is in the form of the pulse width. For more information about RAK12007, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak12007/datasheet/).

The RAK12007 WisBlock Ultrasonic Sensor Module can be mounted on the IO slot of the WisBlock Base board, as shown in **Figure 1**. Also, always secure the connection of the WisBlock module by using compatible screws.

> **Image:** RAK12007 Connection to WisBlock Base

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 2**, the location for the IO slot is properly marked by silkscreen. Follow carefully the procedure defined in [WisBlock Base board assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard) to attach a WisBlock module. Once attached, carefully fix the module with three pieces of M1.2 x 3 mm screws.

> **Image:** RAK12007 assembly to WisBlock Base

##### Disassembling

The procedure in disassembling any type of WisBlock modules is the same.

1. First, remove the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

> **Image:** Detaching silkscreen on the WisBlock module

3. Apply force to the module at the position of the connector, as shown in **Figure 5**, to detach the module from the baseboard.

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

In this example, you will monitor the distance of the object in front of your RAK12007 WisBlock Ultrasonic Sensor Module and display it via RAK1921 WisBlock OLED Display.

#### Initial Test of the RAK12007 WisBlock Module

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
<summary> Click to view the example </summary>
```c
/**
 * @file RAK12007_OLED_Show_Distance.ino
 * @author rakwireless.com
 * @brief use ultrasonic measure distance and display the distance value on OLED example
 * velocity of sound =331.6+0.6T(m/s),(T is the Celsius temperature,331.6 m/sIs the speed of sound waves
 * traveling through air at a temperature of 0 degrees Celsius).
 * @version 0.1
 * @date 2021-06-17
 * @copyright Copyright (c) 2021
 */

#include <Wire.h>
#include <Adafruit_GFX.h>   //Click here to get the library: http://librarymanager/All#Adafruit_GFX
#include <Adafruit_SSD1306.h>   //Click here to get the library: http://librarymanager/All#Adafruit_SSD1306

#ifdef RAK4630
  #define BOARD "RAK4631 "
  #define  RAK4631_BOARD true
#else
  #define  RAK4631_BOARD false
#endif

#define SCREEN_WIDTH 128 // set OLED width,unit:pixel
#define SCREEN_HEIGHT 64 // set OLED height,unit:pixel

#define OLED_RESET -1
Adafruit_SSD1306 oled(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#define TRIG WB_IO6
#define ECHO WB_IO4
#define PD   WB_IO5   //power done control （=1 power done，=0 power on）

#define TIME_OUT  24125 //max measure distance is 4m,the velocity of sound is 331.6m/s in 0℃,TIME_OUT=4*2/331.6*1000000=24215us

float ratio = 346.6/1000/2;   //velocity of sound =331.6+0.6*25℃(m/s),(Indoor temperature about 25℃)

long int duration_time();  //measure high level time
void oled_init();

void setup()
{
   Serial.begin(115200);
   time_t timeout = millis();
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

   pinMode(ECHO, INPUT);   // Echo Pin of Ultrasonic Sensor is an Input
   pinMode(TRIG, OUTPUT);  // Trigger Pin of Ultrasonic Sensor is an Output
   pinMode(PD, OUTPUT);    // power done control pin is an Output
   digitalWrite(TRIG,LOW);
   digitalWrite(PD,LOW);
   pinMode(LED_BLUE, OUTPUT);   // The LED is an Output
   oled_init();
   Serial.println("========================");
   Serial.println("    RAK12007 test");
   Serial.println("========================");
}
void loop()
{
   long int duration, mm;
   digitalWrite(LED_BLUE,HIGH);
   duration = duration_time();
   if(duration > 0)
   {
     mm = duration*ratio; //Test distance = (high level time×velocity of sound (340M/S) / 2,
     digitalWrite(LED_BLUE,LOW);
     Serial.print(mm);
     Serial.print("mm");
     Serial.println();

     oled.clearDisplay();
     oled.setTextColor(WHITE);
     oled.setTextSize(2.5);
     oled.setCursor(20, 10);
     oled.printf("Distance:");
     oled.setCursor(30, 40);
     oled.printf("%d mm",mm);
     oled.display();
   }
   else
   {
     Serial.println("Out of range");
     oled.clearDisplay();
     oled.setTextColor(WHITE);
     oled.setTextSize(2);
     oled.setCursor(0, 20);
     oled.printf("over range");
     oled.display();
   }
  delay(100);
}
long int duration_time()
{
   long int respondTime;
   pinMode(TRIG, OUTPUT);
   digitalWrite(TRIG, HIGH);
   delayMicroseconds(12);   //pull high time need over 10us
   digitalWrite(TRIG, LOW);
   pinMode(ECHO, INPUT);
   respondTime = pulseIn(ECHO, HIGH); // microseconds
   delay(33);
   if(RAK4631_BOARD)
   {
     respondTime = respondTime*0.7726; // Time calibration factor is 0.7726,to get real time microseconds for 4631board
   }
   Serial.printf("respond time is %d\r\n",respondTime);

   if((respondTime>0)&&(respondTime < TIME_OUT))  //ECHO pin max timeout is 33000us according it's datasheet
   {
    return respondTime;
   }
   else
   {
     return -1;
   }
}
void oled_init()
{
  oled.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  oled.clearDisplay();
  oled.display();
}
```
</details>

:::tip NOTE
- The example code is the same for all WisBlock Core Modules.
- If you experience any error in compiling the example sketch, check the updated code for the RAK12007 WisBlock Ultrasonic Sensor Module that can be found on the [RAK12007 WisBlock Example Code Repository](https://github.com/RAKWireless/WisBlock/blob/master/examples/common/IO/RAK12007_OLED_Show_Distance/RAK12007_OLED_Show_Distance.ino).
:::

4. Install the required libraries by pressing `Ctrl` and clicking each highlighted link, as shown in **Figure 9** to **Figure 11**.

> **Image:** Links for required libraries

> **Image:** Installation of Adafruit GFX Library and Companion Library

> **Image:** Installation of Adafruit SSD1306 Library

5. Then select the right Serial Port and upload the code, as shown in **Figure 12** and **Figure 13**.

:::tip NOTE
RAK11200 requires the BOOT0 pin to be configured properly before uploading. If not done properly, uploading the source code to RAK11200 will fail. Check the full details on the [RAK11200 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/#install-rakwireless-esp32-bsp-on-arduino-boards-manager).
:::

> **Image:** Selecting the correct Serial Port

> **Image:** Uploading the sample code

6. When you have successfully uploaded the sample code, you should see the distance displayed on the RAK1921 WisBlock OLED Display, as shown in **Figure 14**. Then, you can open up your serial monitor to get the sensor reading, as shown in **Figure 15**.

> **Image:** Distance shown in RAK1921 WisBlock OLED Display

> **Image:** RAK12007 WisBlock Ultrasonic Module reading in Serial Monitor

You can try to point the sensor on any surface to detect the distance or put an object in front of the sensor.

