---
slug: /product-categories/wisblock/rak14000/quickstart/
title: RAK14000 WisBlock E-Ink Display Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK14000. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak14000/rak14000.png"
keywords:
  - quickstart
  - wisblock
  - RAK14000
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK14000 WisBlock E-Ink Display Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step on using RAK14000 WisBlock E-Ink Display, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK14000 WisBlock E-Ink Display](https://store.rakwireless.com/products/wisblock-epd-module-rak14000?utm_source=WisBlockRAK14000&utm_medium=Document&utm_campaign=BuyFromStore)
- [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base/)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

##### Arduino

- Download and install [Arduino IDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino Boards Manager, install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

The RAK14000 module is part of the WisBlock Display category and connects to the baseboard through the IO slot. It has an E-Paper and a three-pushbutton interface that is connected via an FPC connector, as shown in Figure 1.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/rak14000-parts.png"
  figureCount="1"
  width="40%"
  caption="RAK14000 E-Paper and Three-Pushbutton Interface"
/>

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 2**, the location for the IO slot is properly marked by silkscreen. Follow carefully the procedure defined in [RAK5005-O module assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3&nbsp;mm screws depending on the module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/rak14000-mounting.png"
  figureCount="2"
  width="60%"
  caption="RAK14000 connection to WisBlock Base"
/>

##### Disassembling

The procedure to disassemble any type of WisBlock modules is the same.

1. Remove the screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/removing_screw.png"
  figureCount="3"
  width="70%"
  caption="Removing screws from the WisBlock module"
/>

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/detach_silkscreen.png"
  figureCount="4"
  width="70%"
  caption="Detaching silkscreen on the WisBlock module"
/>

3. Apply force to the module at the position of the connector, as shown in **Figure 5**, to detach the module from the baseboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/detach_module.png"
  figureCount="5"
  width="70%"
  caption="Applying even forces on the proper location of a WisBlock module"
/>

##### Connecting the E-Paper and the Three-Pushbutton Switch

:::tip NOTE
Some illustrations are specific to the FPC connector of the Three-Pushbutton Switch, but it is also applicable to the E-Paper.
:::

1. The FPC connectors for the E-Paper and Pushbuttons are commonly set to close by default, as shown in **Figure 6**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/rak14000-fpc-close.svg"
  figureCount="6"
  width="50%"
  caption="RAK14000 FPC Connector Closed"
/>

2. You need to open the lock of the FPC connector by carefully pulling it up. Then insert fully and carefully the FPC cable of the E-Paper and the Three-Pushbutton Switch with the copper trace facing down to the connector, as shown in **Figure 7**.

:::tip NOTE
The E-Paper can be connected on either of the two FPC connectors. These are J2 and J3 in the RAK14000 board. This gives you flexibility on the orientation of the E-Paper display.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/rak14000-fpc-open.svg"
  figureCount="7"
  width="70%"
  caption="RAK14000 FPC Connectors Open"
/>

3. Once done, make sure to lock the FPC connection again by carefully pushing down the lock until the FPC cable tightens, as shown in **Figure 8**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/rak14000-copper-bottom.svg"
  figureCount="8"
  width="70%"
  caption="RAK14000 FPC Correct Connection"
/>

If the copper trace is on top, as shown in **Figure 9**, that is a **wrong connection**, and the E-Paper and Three-Pushbutton Switch will not work.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/rak14000-copper-top.png"
  figureCount="9"
  width="50%"
  caption="RAK14000 FPC Wrong Connection"
/>

:::tip NOTE
If you will connect other modules to remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts. For instance, if you are planning to use it in conjunction with the [EEPROM module](https://store.rakwireless.com/products/wisblock-eeprom-module-rak15000?utm_source=WisBlockRAK15000&utm_medium=Document&utm_campaign=BuyFromStore), since the EPD uses all IO pins, you would have to forego the Three-Pushbutton Switch (uses IO 3, 5 and 6) and put the EEPROM module on slot D (has IO 5 & 6).
:::

After all this setup, you can now connect the battery and USB cable to start programming your WisBlock Core.

### Software Configuration and Example

In this example, you will be using E-Paper and the Three-Pushbutton Switch to demonstrate functionality.

These are the quick links that go directly to the software guide for the specific WisBlock Core module you use:

- [RAK14000 in RAK4631 WisBlock Core Guide](#rak14000-in-rak4631-wisblock-core-guide)
- [RAK14000 in RAK11200 WisBlock Core Guide](#rak14000-in-rak11200-wisblock-core-guide)
- [RAK14000 in RAK11310 WisBlock Core Guide](#rak14000-in-rak11310-wisblock-core-guide)

#### RAK14000 in RAK4631 WisBlock Core Guide

##### Arduino Setup

If you already installed the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index), the WisBlock Core and example code should now be available on the Arduino IDE.

1. Select the RAK4631 WisBlock Core you have, as shown in **Figure 10**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/rak4631_board.png"
  figureCount="10"
  width="100%"
  caption="Selecting RAK4631 as WisBlock Core"
/>

2. Install the [Adafruit GFX Library](https://github.com/adafruit/Adafruit-GFX-Library).

- Open the Arduino IDE.
- On the Menu bar, click **Sketch** &gt; **Include Library** &gt; **Manage Libraries**.
- On the Library Manager text area, type **adafruit gfx**.
- To finish installation, click on the **Install** button highlighted in yellow, as shown in **Figure 11**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/adafruit_gfx.png"
  figureCount="11"
  width="100%"
  caption="Adafruit GFX Library Install"
/>

3. Install the [Adafruit EPD Library](https://github.com/adafruit/Adafruit_EPD).

- Open the Arduino IDE.
- On the Menu bar, click **Sketch** &gt; **Include Library** &gt; **Manage Libraries**.
- On the Library Manager text area, type **adafruit epd**.
- To finish installation, click on the **Install** button highlighted in yellow, as shown in **Figure 12**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/adafruit_epd.png"
  figureCount="12"
  width="100%"
  caption="Adafruit EPD Library Install"
/>

4. You can access the programming guide for the RAK14000 module by opening the example codes, as shown in **Figure 13**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/example_rak4631_rak14000.png"
  figureCount="13"
  width="100%"
  caption="Opening RAK14000 example for RAK4631 WisBlock Core"
/>

:::tip NOTE

You will need to change this section of the code if you are using an E-Paper with different resolution from another vendor.

```c
typedef struct  DEPG {
   int  width;
   int  height;
   int  position1_x;
   int  position1_y;
   int  position2_x;
   int  position2_y;
   int  position3_x;
   int  position3_y;
   int  position4_x;
   int  position4_y;
} DEPG;

// DEPG  DEPG_HP = {250,122,40,20,40,30,40,50,90,40};  //use this for white-black-red version
DEPG  DEPG_HP = {212,104,30,15,30,25,30,45,80,30};  //  use this for white-black version

Adafruit_SSD1680 display(DEPG_HP.width, DEPG_HP.height, EPD_MOSI,
                         EPD_SCK, EPD_DC, EPD_RESET,
                         EPD_CS, SRAM_CS, EPD_MISO,
                         EPD_BUSY);
```
:::

5. After opening the example code, you can now select the right port and upload the code, as shown in **Figure 14** and **Figure 15**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/rak4631_select_port.png"
  figureCount="14"
  width="100%"
  caption="Selecting the correct Serial Port"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/rak4631_upload.png"
  figureCount="15"
  width="100%"
  caption="Uploading the RAK14000 example code"
/>

6. Once you have successfully uploaded the example sketch, you should be able to see the image output on the E-Paper. You can also see the corresponding button pressed in the Serial Monitor.

#### RAK14000 in RAK11200 WisBlock Core Guide

##### Arduino Setup

If you already installed the [RAKwireless Arduino BSP](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/#arduino-ide-bsp-installation), the WisBlock Core and example code should now be available on the Arduino IDE.

1. Select the WisBlock Core you have, as shown in **Figure 16**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/rak11200_board.png"
  figureCount="16"
  width="100%"
  caption="Selecting RAK11200 as WisBlock Core"
/>

2. Install the [Adafruit GFX Library](https://github.com/adafruit/Adafruit-GFX-Library).

- Open the Arduino IDE.
- On the Menu bar, click **Sketch** &gt; **Include Library** &gt; **Manage Libraries**.
- On the Library Manager text area, type **adafruit gfx**.
- To finish installation, click on **Install** button highlighted in yellow, as shown in **Figure 17**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/adafruit_gfx.png"
  figureCount="17"
  width="100%"
  caption="Adafruit GFX Library Install"
/>

3. Install [Adafruit EPD Library](https://github.com/adafruit/Adafruit_EPD)

- Open the Arduino IDE.
- On the Menu bar, click **Sketch** &gt; **Include Library** &gt; **Manage Libraries**.
- On the Library Manager text area, type **adafruit epd**.
- To finish installation, click on **Install** button highlighted in yellow, as shown below in **Figure 18**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/adafruit_epd.png"
  figureCount="18"
  width="100%"
  caption="Adafruit EPD Library Install"
/>

4. You can access the programming guide for the RAK14000 module by opening the example codes depending on your WisBlock Core, as shown in **Figure 19**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/example_rak11200_rak14000.png"
  figureCount="19"
  width="100%"
  caption="Opening RAK14000 example for RAK11200 WisBlock Core"
/>

:::tip NOTE

You will need to change this section of the code depending on the E-Paper you are using.

```c
// 2.13" EPD with SSD1680, width=250 pixels, heigh=122 pixels
Adafruit_SSD1680 display(250, 122, EPD_MOSI,EPD_SCK, EPD_DC, EPD_RESET,EPD_CS, SRAM_CS, EPD_MISO,EPD_BUSY);
```

:::

5. After opening the example code, you can now select the right port and upload the code, as shown in **Figure 20** and **Figure 22**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/rak11200_port.png"
  figureCount="20"
  width="100%"
  caption="Selecting the correct Serial Port"
/>

Before uploading your sketch, short circuit **BOOT0** and **GND** pins and press the reset button as shown below.
<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/rak11200-boot0-for-flashing.png"
  figureCount="21"
  width="60%"
  caption="Force ESP32 Download mode"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/rak11200_upload.png"
  figureCount="22"
  width="100%"
  caption="Uploading the RAK14000 example code"
/>

6. Once you have successfully uploaded the example sketch, you should be able to see the image output on the E-Paper. You can also see the corresponding button pressed in the Serial Monitor.

#### RAK14000 in RAK11310 WisBlock Core Guide

##### Arduino Setup

If you already installed the [RAKwireless Arduino BSP](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/#arduino-ide-bsp-installation), the WisBlock Core and example code should now be available on the Arduino IDE.

1. Select the RAK11310 WisBlock Core you have, as shown in **Figure 23**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/rak11310_board.png"
  figureCount="23"
  width="100%"
  caption="Selecting RAK11310 as WisBlock Core"
/>

2. Install the [Adafruit GFX Library](https://github.com/adafruit/Adafruit-GFX-Library).

- Open the Arduino IDE.
- On the Menu bar, click **Sketch** &gt; **Include Library** &gt; **Manage Libraries**.
- On the Library Manager text area, type **adafruit gfx**.
- To finish installation, click on the **Install** button highlighted in yellow, as shown in **Figure 24**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/adafruit_gfx.png"
  figureCount="24"
  width="100%"
  caption="Adafruit GFX Library Install"
/>

3. Install the [Adafruit EPD Library](https://github.com/adafruit/Adafruit_EPD).

- Open the Arduino IDE.
- On the Menu bar, click **Sketch** &gt; **Include Library** &gt; **Manage Libraries**.
- On the Library Manager text area, type **adafruit epd**.
- To finish installation, click on the **Install** button highlighted in yellow, as shown in **Figure 25**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/adafruit_epd.png"
  figureCount="25"
  width="100%"
  caption="Adafruit EPD Library Install"
/>

4. You can access the programming guide for the RAK14000 module by opening the example codes, as shown in **Figure 26**.

:::tip NOTE

There are two versions of RAK14000 module for sale in the RAKwireless Store, the [white-black display panel](https://store.rakwireless.com/products/wisblock-epd-module-rak14000?variant=39534109655238) and [white-black-red display panel](https://store.rakwireless.com/products/wisblock-epd-module-rak14000?variant=39534109688006) version.

You will need to change this section of the code depending on the E-Paper you are using.

```c
typedef struct  DEPG {
   int  width;
   int  height;
   int  position1_x;
   int  position1_y;
   int  position2_x;
   int  position2_y;
   int  position3_x;
   int  position3_y;
   int  position4_x;
   int  position4_y;
} DEPG;

// DEPG  DEPG_HP = {250,122,40,20,40,30,40,50,90,40};  // use this for 250 x 122 white-black-red
DEPG  DEPG_HP = {212,104,30,15,30,25,30,45,80,30};  // use this for 212 x 104 white-black

Adafruit_SSD1680 display(DEPG_HP.width, DEPG_HP.height, EPD_MOSI,
                         EPD_SCK, EPD_DC, EPD_RESET,
                         EPD_CS, SRAM_CS, EPD_MISO,
                         EPD_BUSY);
```
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/example_rak11310_rak14000.png"
  figureCount="26"
  width="100%"
  caption="Opening RAK14000 example for RAK4631 WisBlock Core"
/>

5. After opening the example code, you can now select the right port and upload the code, as shown in **Figure 27** and **Figure 28**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/rak11310_select_port.png"
  figureCount="27"
  width="100%"
  caption="Selecting the correct Serial Port"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak14000/quickstart/rak11310_upload.png"
  figureCount="28"
  width="100%"
  caption="Uploading the RAK14000 example code"
/>

6. Once you have successfully uploaded the example sketch, you should be able to see the image output on the E-Paper. You can also see the corresponding button pressed in the Serial Monitor.


<RkBottomNav/>
