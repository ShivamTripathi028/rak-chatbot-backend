---
slug: /product-categories/wisblock/rak14012/quickstart/
title: RAK14012 WisBlock LED Matrix Quick Start Guide
description: This contains instructions and tutorials on installing and deploying your RAK14012. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak14012/rak14012.png"
keywords:
  - quickstart
  - wisblock
  - RAK14012
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'


# RAK14012 WisBlock LED Matrix Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step on using the RAK14012 WisBlock LED Matrix, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK14012 WisBlock LED Matrix](https://store.rakwireless.com/products/rak14012-wisblock-16x16-rgb-led-matrix?utm_source=WisBlockRAK14012&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [RAK19008 WisBlock IO Extension Cable](https://store.rakwireless.com/products/wisblock-io-extension-cable-rak19008?utm_source=RAK19008&utm_medium=Document&utm_campaign=BuyFromStore)
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install the [ArduinoIDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino Boards Manager, install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

The RAK14012 is an LED matrix driver module for WS2812B LEDs, which has a control circuit and RGB chip.  For more information about RAK14012, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak14012/datasheet/).

The RAK14012 WisBlock LED Matrix can be mounted on the IO slot of the WisBlock Base board, as shown in **Figure 1**. Also, always secure the connection of the WisBlock module by using compatible screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14012/quickstart/module-connection.png"
  figureCount="1"
  width="95%"
  caption="RAK14012 Connection to WisBlock Base"
/>

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 2**, the location for the IO slot is properly marked by silkscreen. Follow carefully the procedure defined in [RAK5005-O module assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with three pieces of M1.2 x 3&nbsp;mm screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14012/quickstart/mounting.png"
  figureCount="2"
  width="70%"
  caption="RAK14012 assembly to WisBlock Base"
/>

##### Disassembling

The procedure in disassembling any type of WisBlock modules is the same.

1. Remove the screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14012/quickstart/removing_screw.png"
  figureCount="3"
  width="70%"
  caption="Removing screws from the WisBlock module"
/>

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14012/quickstart/detach_silkscreen.png"
  figureCount="4"
  width="70%"
  caption="Detaching silkscreen on the WisBlock module"
/>

3. Apply force to the module at the position of the connector, as shown in **Figure 5**, to detach the module from the baseboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14012/quickstart/detach_module.png"
  figureCount="5"
  width="70%"
  caption="Applying even forces on the proper location of a WisBlock module"
/>

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts.
:::

After all this setup, you can now connect the battery (optional) and USB cable to start programming your WisBlock Core.

:::warning

- Batteries can cause harm if not handled properly.
- Only 3.7-4.2&nbsp;V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5&nbsp;V solar panels are supported. Do not use 12&nbsp;V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires match the polarity on the RAK5005-O board. Not all batteries have the same wiring.
:::

### Software Configuration and Example

In this example, you will be seeing multiple LED Matrix display patterns and colors. Follow the setup in **Figure 6** and **Figure 7** to follow the connection.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14012/quickstart/module-connection.png"
  figureCount="6"
  width="100%"
  caption="Setting up RAK14012 to WisBlock Base board and WisBlock Core"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14012/quickstart/matrix-connection.png"
  figureCount="7"
  width="100%"
  caption="Connecting the RAK14012 to the 16x16 LED Matrix"
/>

:::warning
- The allowable voltage range from the external power supply is 3.7&nbsp;V to 5.3&nbsp;V. Do not go beyond that limit.
- Make sure that the jumper from 5V_OUT of RAK14012 WisBlock LED Matrix is disconnected when connecting to an external power supply.
- LED Matrix DIN should be connected to RAK14012 DOUT.
- LED Matrix GND should be connected to RAK14012 GND.
:::

1. Select the WisBlock Core you have, as shown in **Figure 8** to **Figure 10**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14012/quickstart/selectboard4631.png"
  figureCount="8"
  width="100%"
  caption="Selecting RAK4631 as WisBlock Core"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14012/quickstart/selectboard11200.png"
  figureCount="9"
  width="100%"
  caption="Selecting RAK11200 as WisBlock Core"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14012/quickstart/selectboard11300.png"
  figureCount="10"
  width="100%"
  caption="Selecting RAK11300 as WisBlock Core"
/>

2. Copy the example code below:

```c
//**
   @file RAK14012_RGB_Matrix_Disco.ino
   @author rakwireless.com
   @brief Light up the RGB mixed color screen as your Disco atmosphere light.
   @version 0.1
   @date 2021-11-29
   @copyright Copyright (c) 2021
**/

#include <Rak_RGB_Matrix.h>  // Click to install library: http://librarymanager/All#RAK14012-LED-Matrix
#include "Wire.h"

#define NUMPIXELS       256
#define PIN             WB_IO5

// Parameter 1 = number of pixels in strip
// Parameter 2 = Arduino pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
//   NEO_RGBW    Pixels are wired for RGBW bitstream (NeoPixel RGBW products)
RAK_RGB_Matrix strip = RAK_RGB_Matrix(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

// IMPORTANT: To reduce NeoPixel burnout risk, add 1000 uF capacitor across
// pixel power leads, add 300 - 500 Ohm resistor on first pixel's data input
// and minimize distance between Arduino and first pixel.  Avoid connecting
// on a live circuit...if you must, connect GND first.

void setup()
{
  // Enable 5v power supply on the board.
  // An external battery is required.
  pinMode(WB_IO6, OUTPUT);
  digitalWrite(WB_IO6, HIGH);

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

  strip.begin();
  strip.setBrightness(25);
  strip.show(); // Initialize all pixels to 'off'
}

void loop()
{
  // Some example procedures showing how to display to the pixels:
  colorWipe(strip.Color(255, 0, 0), 50); // Red
  colorWipe(strip.Color(0, 255, 0), 50); // Green
  colorWipe(strip.Color(0, 0, 255), 50); // Blue
  // ColorWipe(strip.Color(0, 0, 0, 255), 50); // White RGBW
  // Send a theater pixel chase in...
  theaterChase(strip.Color(127, 127, 127), 50); // White
  theaterChase(strip.Color(127, 0, 0), 50); // Red
  theaterChase(strip.Color(0, 0, 127), 50); // Blue

  rainbow(20);
  rainbowCycle(20);
  theaterChaseRainbow(50);
}

/**
 * @brief Fill the dots one after the other with a color.
 */
void colorWipe(uint32_t c, uint8_t wait)
{
  for(uint16_t i=0; i<strip.numPixels(); i++)
  {
    strip.setPixelColor(i, c);
    strip.show();
    delay(wait);
  }
}

void rainbow(uint8_t wait)
{
  uint16_t i, j;

  for(j=0; j<256; j++)
  {
    for(i=0; i<strip.numPixels(); i++)
  {
      strip.setPixelColor(i, Wheel((i+j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

/**
 * @brief Slightly different, this makes the rainbow equally distributed throughout.
 */
void rainbowCycle(uint8_t wait)
{
  uint16_t i, j;

  for(j=0; j<256*5; j++)
  {
    // 5 cycles of all colors on wheel
    for(i=0; i< strip.numPixels(); i++)
    {
      strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

/**
 * @brief Theatre-style crawling lights.
 */
void theaterChase(uint32_t c, uint8_t wait)
{
  for (int j=0; j<10; j++)
  {
    //do 10 cycles of chasing
    for (int q=0; q < 3; q++)
    {
      for (uint16_t i=0; i < strip.numPixels(); i=i+3)
      {
        strip.setPixelColor(i+q, c);    //turn every third pixel on
      }
      strip.show();

      delay(wait);

      for (uint16_t i=0; i < strip.numPixels(); i=i+3)
      {
        strip.setPixelColor(i+q, 0);        //turn every third pixel off
      }
    }
  }
}

/**
 * @brief Theatre-style crawling lights with rainbow effect.
 */
void theaterChaseRainbow(uint8_t wait)
{
  for (int j=0; j < 256; j++)
  {
    // cycle all 256 colors in the wheel
    for (int q=0; q < 3; q++)
    {
      for (uint16_t i=0; i < strip.numPixels(); i=i+3)
      {
        strip.setPixelColor(i+q, Wheel( (i+j) % 255));    //turn every third pixel on
      }
      strip.show();

      delay(wait);

      for (uint16_t i=0; i < strip.numPixels(); i=i+3)
      {
        strip.setPixelColor(i+q, 0);        //turn every third pixel off
      }
    }
  }
}

/**
 * @brief Input a value 0 to 255 to get a color value.
 * The colours are a transition r - g - b - back to r.
 */
uint32_t Wheel(byte WheelPos)
{
  WheelPos = 255 - WheelPos;
  if(WheelPos < 85)
  {
    return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  }
  if(WheelPos < 170)
  {
    WheelPos -= 85;
    return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
  WheelPos -= 170;
  return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
}

```

If you experience any error in compiling the example sketch, check the updated code for the RAK14012 WisBlock LED Matrix that can be found on the [RAK14012 WisBlock Example Code Repository](https://github.com/RAKWireless/RAK14012-LED-Matrix/tree/main/examples).

3. Download the required library by clicking the highlighted text, as shown in **Figure 11**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14012/quickstart/getting-library.png"
  figureCount="11"
  width="100%"
  caption="Accessing the library"
/>

4. Select the right serial port and upload the code, as shown in **Figure 12** and **Figure 13**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14012/quickstart/select_port.png"
  figureCount="12"
  width="100%"
  caption="Selecting the correct Serial Port"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14012/quickstart/upload.png"
  figureCount="13"
  width="100%"
  caption="Uploading the sample code"
/>

:::tip NOTE
RAK11200 requires the BOOT0 pin to be configured properly before uploading. If not done properly, uploading the source code to RAK11200 will fail. Check the full details on the [RAK11200 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/#uploading-to-wisblock).
:::

5. When you successfully upload the sample code, you can see that the LED Matrix is turned on and displaying lighting patterns.


<RkBottomNav/>