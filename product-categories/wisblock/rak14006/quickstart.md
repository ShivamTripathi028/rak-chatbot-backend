---
slug: /product-categories/wisblock/rak14006/quickstart/
title: RAK14006 WisBlock Rotary Encoder Module Quick Start Guide
description: This contains instructions and tutorials on installing and deploying your RAK14006. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: https://images.docs.rakwireless.com/wisblock/rak14006/rak14006.png
keywords:
  - quickstart
  - wisblock
  - RAK14006
sidebar_label: Quick Start Guide
---

# RAK14006 WisBlock Rotary Encoder Module Quick Start Guide

## Prerequisite

### Product Inclusions

Before going through each and every step on using the RAK14006 WisBlock Rotary Encoder module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK14006 WisBlock Rotary Encoder Module](https://store.rakwireless.com/products/rak14006-wisblock-rotary-input?utm_source=RAK14006&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [RAK19008 WisBlock IO Extension Cable](https://store.rakwireless.com/products/wisblock-io-extension-cable-rak19008?utm_source=RAK19008&utm_medium=Document&utm_campaign=BuyFromStore)
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install [ArduinoIDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino Boards Manager, install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

The RAK14006 is a rotary encoder module with PEC11L-4125F-S0020 from BOURNS. RAK14006 can detect user inputs such as rotation direction and rotation number of steps. Also, an independent push switch is provided. For more information about RAK14006, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak14006/datasheet/).

The RAK14006 WisBlock Rotary Encoder Module can be mounted on the IO slot of the WisBlock Base board, as shown in **Figure 1**. Also, always secure the connection of the WisBlock module by using compatible screws.

> **Image:** RAK14006 Connection to WisBlock Base

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 2**, the location for the IO slot is properly marked by silkscreen. Follow carefully the procedure defined in [RAK5005-O module assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with three pieces of M1.2 x 3 mm screws.

> **Image:** RAK14006 assembly to WisBlock Base

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
- Make sure the battery wires match the polarity on the RAK5005-O board. Not all batteries have the same wiring.
:::

### Software Configuration and Example

In this example, you will be getting the rotation position of the knob or if it is pressed to your Serial Monitor.

1. You need to select first the WisBlock Core you have, as shown in **Figure 6** to **Figure 8**.

> **Image:** Selecting RAK4631 as WisBlock Core

> **Image:** Selecting RAK11200 as WisBlock Core

> **Image:** Selecting RAK11300 as WisBlock Core

2. Copy the example code below.

```c
/**
   @file RAK14006_Rotary_Encoder.ino
   @author rakwireless.com
   @brief Rotary Encoder Example
   @version 0.1
   @date 2021-7-28
   @copyright Copyright (c) 2020
**/
#include <Wire.h>

#define ENCODER_A_PIN WB_IO6  //clockwise
#define ENCODER_B_PIN WB_IO4  //anticlockwise
#define SWITCH_PIN    WB_IO5  //press key

//position is 0 when start up
long position = 0;
bool press_flag = false;
bool clockwise_flag = false;
bool anticlockwise_flag = false;

void setup(){
  pinMode(WB_IO2, OUTPUT);
  digitalWrite(WB_IO2, HIGH);
  //setup our pins
  pinMode(ENCODER_A_PIN, INPUT);
  pinMode(ENCODER_B_PIN, INPUT);
  pinMode(SWITCH_PIN, INPUT);

  attachInterrupt(SWITCH_PIN, handle_1, FALLING);
  attachInterrupt(ENCODER_A_PIN, handle_2, RISING);
  attachInterrupt(ENCODER_B_PIN, handle_3, RISING);
  //setup our serial
  Serial.begin(115200);
  Serial.println("You can press and twist the button!!");
}

void loop(){
  if(press_flag==true)
  {
    press_flag = false;
    Serial.println("press key");
  }
  if(clockwise_flag==true)
  {
    clockwise_flag = false;
    position++;
    Serial.print("position step is ");
    Serial.println(position);
  }
  if(anticlockwise_flag==true)
  {
    anticlockwise_flag = false;
    position--;
    Serial.print("position step is ");
    Serial.println(position);
  }
}

void handle_1(){
  press_flag = true;
}
void handle_2(){
  clockwise_flag = true;
}
void handle_3(){
  anticlockwise_flag = true;
}
```

If you experience any error in compiling the example sketch, check the updated code for the RAK14006 WisBlock Rotary Encoder Module that can be found on the [RAK14006 WisBlock Example Code Repository](https://github.com/RAKWireless/WisBlock/blob/master/examples/common/IO/RAK14006_Rotary_Encoder/RAK14006_Rotary_Encoder.ino)

3. Select the right serial port and upload the code, as shown in **Figure 9** and **Figure 10**.

> **Image:** Selecting the correct Serial Port

> **Image:** Uploading the sample code

:::tip NOTE
RAK11200 requires the BOOT0 pin to be configured properly before uploading. If not done properly, uploading the source code to RAK11200 will fail. Check the full details on the [RAK11200 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/#uploading-to-wisblock).
:::

5. When you successfully upload the sample code, you may rotate or press the knob switch of RAK14006, as shown in **Figure 13**. Then, you can open up your serial monitor to get the rotary encoder reading, as shown in **Figure 14**.

> **Image:** Rotating the knob switch of RAK14006

> **Image:** Position step reading in Serial Monitor

