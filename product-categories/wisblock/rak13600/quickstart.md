---
slug: /product-categories/wisblock/rak13600/quickstart/
title: RAK13600 WisBlock NFC Reader Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK13600. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak13600/rak13600.png"
keywords:
    - RAK13600
    - wisblock
    - quickstart
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK13600 WisBlock NFC Reader Module Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step on using the RAK13600 WisBlock NFC Reader Module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK13600 Wisblock Interface Extension Board with Coil Antenna](https://store.rakwireless.com/products/rak13600-wisblock-nfc-reader?utm_source=RAK13600&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install the [ArduinoIDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino Boards Manager, install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

The RAK13600 module is designed as wireless module that allows you to scan NFC and RFID tags and devices. It includes an antenna coil that transmits and receives RF signals from the object being scanned. Without the antenna coil shown in **Figure 1**, you will not be able to scan NFC/RFID devices. The antenna coil has adhesive transfer tape on it. You can remove the 3M patch film so you stick the antenna coil on the ideal location in your enclosure. The enclosure must be plastic and not metal, since metal enclosures introduce attenuation on RF signals.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13600/quickstart/nfc_coil.png" 
  figureCount="1"
  caption="NFC Coil Antenna" 
   width="35%"
/>

The RAK13600 module can be mounted on the IO slot of any WisBlock Base board, as shown in **Figure 2**. Also, always secure the connection of the WisBlock module by using compatible screws. For more information about RAK13600, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak13600/datasheet/).

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13600/quickstart/rak13600-assembly.png" 
  figureCount="2"
  caption="RAK13600 on WisBlock Base with WisBlock Core" 
   width="95%"
/>

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 3**, the location for the IO slot is properly marked by silkscreen. Follow carefully the procedure defined in [WisBlock Base module assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with three M1.2 x 3&nbsp;mm screws compatible with the module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13600/quickstart/mounting.png" 
  figureCount="3"
  caption="RAK13600 connection to WisBlock Base Board" 
   width="60%"
/>

##### Disassembling

The procedure in disassembling any type of WisBlock modules is the same.

1. First, remove the screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13600/quickstart/16.removing-screws.png" 
  figureCount="4"
  caption="Removing screws from the WisBlock module" 
   width="70%"
/>

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13600/quickstart/17.detaching-silkscreen.png" 
  figureCount="5"
  caption="Detaching silkscreen on the WisBlock module" 
   width="70%"
/>

3. Apply force to the module at the position of the connector, as shown in **Figure 6**, to detach the module from the baseboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13600/quickstart/18.detaching-module.png" 
  figureCount="6"
  caption="Applying even forces on the proper location of a WisBlock module" 
   width="70%"
/>

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts. RAK13600 uses I2C and IO pins. It can cause possible conflict, especially on some IO modules.
:::

After all this setup, you can now connect the battery (optional) and USB cable to start programming your WisBlock Core.

:::warning 

- Battery can cause harm if not handled properly.
- Only 3.7-4.2&nbsp;V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Make sure the battery wires match the polarity on the RAK WisBlock Base Board. Not all batteries have the same wiring.
- Only 5&nbsp;V solar panels are supported. Do not use 12&nbsp;V solar panels. It will destroy the charging unit and eventually other electronic parts.
:::

### Software Configuration and Example

The RAK13600 is based on the popular NFC/RFID chip PN532. You need to install the RAK13600-PN532 library to use the module. By default, the module communicates via I2C to the WisBlock Core module. The following guide shows how to test your RAK13600 module using a standard RFID card, as shown in **Figure 7**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13600/quickstart/module_coil_card.png" 
  figureCount="7"
  caption="RAK13600 with Coil and RFID Card" 
   width="50%"
/>

1. Open the Arduino IDE and select the WisBlock Core you use, as shown in **Figure 8** to **Figure 10**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13600/quickstart/selectboard4631.png" 
  figureCount="8"
  caption="Selecting RAK4631 as WisBlock Core" 
   width="100%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13600/quickstart/selectboard11200.png" 
  figureCount="9"
  caption="Selecting RAK11200 as WisBlock Core" 
   width="100%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13600/quickstart/selectboard11300.png" 
  figureCount="10"
  caption="Selecting RAK11300 as WisBlock Core" 
   width="100%"
/>

2. Copy the example code below and paste it on the Arduino IDE:

<details>
<summary> Click to view the example </summary>

```c
/**
   @file readMifareClassic.ino
   @author rakwireless.com
   @brief  This example will wait for any ISO14443A card or tag, and depending on the size of the UID will attempt to read from it.
   @version 0.1
   @date 2021-10-14
   @copyright Copyright (c) 2021
**/

#include <Wire.h>
#include <SPI.h>
#include <RAK13600-PN532.h> // Click here to get the library: http://librarymanager/All#RAK13600-PN532

// If using the breakout or shield with I2C, define just the pins connected
#define PN532_IRQ   (WB_IO6)
#define PN532_RESET (WB_IO5)  // Not connected by default on the NFC Shield

// Or use this line for a breakout or shield with an I2C connection:
NFC_PN532 nfc(PN532_IRQ, PN532_RESET);

void setup(void) {
  Serial.begin(115200);
  pinMode(WB_IO2, OUTPUT);
  digitalWrite(WB_IO2, HIGH);
  delay(300);
  while (!Serial) delay(10); // for Leonardo/Micro/Zero

  Serial.println("Hello!");

  nfc.begin();

  uint32_t versiondata = nfc.getFirmwareVersion();
  if (! versiondata) {
    Serial.print("Didn't find PN53x board");
    while (1); // halt
  }
  // Got ok data, print it out!
  Serial.print("Found chip PN5"); Serial.println((versiondata>>24) & 0xFF, HEX);
  Serial.print("Firmware ver. "); Serial.print((versiondata>>16) & 0xFF, DEC);
  Serial.print('.'); Serial.println((versiondata>>8) & 0xFF, DEC);

  // configure board to read RFID tags
  nfc.SAMConfig();

  Serial.println("Waiting for an ISO14443A Card ...");
}

void loop(void) {
  uint8_t success;
  uint8_t uid[] = { 0, 0, 0, 0, 0, 0, 0 };  // Buffer to store the returned UID
  uint8_t uidLength;                        // Length of the UID (4 or 7 bytes depending on ISO14443A card type)

  // Wait for an ISO14443A type cards (Mifare, etc.).  When one is found
  // 'uid' will be populated with the UID, and uidLength will indicate
  // if the uid is 4 bytes (Mifare Classic) or 7 bytes (Mifare Ultralight)
  success = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A, uid, &uidLength);

  if (success) {
    // Display some basic information about the card
    Serial.println("Found an ISO14443A card");
    Serial.print("  UID Length: ");Serial.print(uidLength, DEC);Serial.println(" bytes");
    Serial.print("  UID Value: ");
    nfc.PrintHex(uid, uidLength);

    if (uidLength == 4)
    {
      // We probably have a Mifare Classic card ...
      uint32_t cardid = uid[0];
      cardid <<= 8;
      cardid |= uid[1];
      cardid <<= 8;
      cardid |= uid[2];
      cardid <<= 8;
      cardid |= uid[3];
      Serial.print("Seems to be a Mifare Classic card #");
      Serial.println(cardid);
    }
    Serial.println("");
  }
  delay(2000);
}
```
</details>

3. Install the RAK13600-PN532 library by clicking the link highlighted by red box, as shown in **Figure 11**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13600/quickstart/example_code.png" 
  figureCount="11"
  caption="Getting the RAK13600-PN532 Library" 
   width="100%"
/>

4. You will be directed to the **Library Manager** then you have to click install.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13600/quickstart/library_install.png" 
  figureCount="12"
  caption="Installing RAK13600-PN532 Library" 
   width="100%"
/>

5. Next, you need to install an additional library from Adafruit. You need to type on the library search box `adafruit busio` then install it by clicking install. After the successful installation of the two libraries, you can now close the **Library Manager** window.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13600/quickstart/library_adafruitbusio.png" 
  figureCount="13"
  caption="Installing Adafruit BusIO Library" 
   width="100%"
/>

6. Select the right Serial Port and upload the code, as shown in **Figure 14** and **Figure 15**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13600/quickstart/select_port.png" 
  figureCount="14"
  caption="Selecting the correct Serial Port" 
   width="100%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13600/quickstart/done_upload.png" 
  figureCount="15"
  caption="Uploading the sample code" 
   width="100%"
/>

If you experience any error in compiling the demo sketch, check the updated code for the [RAK13600 readMifareClassic example](https://github.com/RAKWireless/WisBlock/blob/master/examples/common/IO/RAK13600_PN530_NFC/readMifareClassic/readMifareClassic.ino). Other example codes for RAK13600 are also available on the [RAK13600 WisBlock Example Code Repository](https://github.com/RAKWireless/WisBlock/blob/master/examples/common/IO/RAK13600_PN530_NFC).

:::tip NOTE
If you are using RAK11200 as the WisBlock Core, it requires the BOOT0 pin to be configured properly before uploading. If not done properly, uploading the source code to RAK11200 will fail. Check the full details on the [RAK11200 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/#uploading-to-wisblock).
:::

7. When you have successfully uploaded the example code, open the serial monitor by clicking the magnifying glass icon on the upper right of the Arduino IDE then place the RFID card on top of the antenna coil. You should see the details of the card, as shown in **Figure 16**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13600/quickstart/serial_output.png" 
  figureCount="16"
  caption="RFID Card Information Read by the RAK13600" 
   width="100%"
/>

<RkBottomNav/>