---
slug: /product-categories/wisblock/rak3401/quickstart/
title: RAK3401 WisBlock BLE Module Quick Start Guide | Setup & Configuration
description: Set up your RAK3401 BLE module with this quick start guide. Learn firmware flashing, low-power modes, and sensor integration.
image: https://images.docs.rakwireless.com/wisblock/rak3401/rak3401.png
keywords:
  - rak3401
  - rak3401 module
  - nrf52840 mcu
  - ble module guide
  - rak3401 setup
  - low power mcu
  - low power consumption modules
  - rf iot ble module
date: 2020-09-18
sidebar_label: Quick Start Guide
download: true
---

# RAK3401 WisBlock BLE Module Quick Start Guide

This guide introduces the RAK3401 WisBlock Core BLE Module and how to use it. RAK3401 consists of an nRF52840 MCU making it ideal for various IoT projects.

## Prerequisite

Before going through each and every step on using RAK3401 WisBlock Core, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK3401 WisBlock Core BLE Module](https://store.rakwireless.com/products/rak3401-ble-node)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base)
- Your choice of [WisBlock Modules](https://store.rakwireless.com/pages/wisblock)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

RAK3401 is also included in various WisBlock kits in the RAKwireless store:

- [WisMesh RAK3401 Starter Kit](https://docs.rakwireless.com/product-categories/meshtastic/wismesh-starter-kit-rak3401/overview/) - includes the RAK3401 with RAK19007 WisBlock Base Board and a 1W (30dBm) LoRa transceiver RAK13302. This kit is ideal to get started immediately with Meshtastic.

#### Software

:::tip NOTE
This software guide is based on the RAK4631 Arduino BSP; even the RAk3401 is not listed as board, it is compatible with the RAK4631 WisBlock Board. The only difference is that the RAK3401 does not have the LoRa transceiver.
:::

You can choose Arduino IDE or Platform IO in coding the RAK3401 WisBlock Core.

**Programming RAK3401 via Arduino IDE:**

- Download and install the [Arduino IDE](https://www.arduino.cc/en/Main/Software).

:::warning
_**If you are using Windows 10**_.
Do _**NOT**_ install the Arduino IDE from the Microsoft App Store. Instead, install the original Arduino IDE from the Arduino official website. The Arduino app from the Microsoft App Store has problems using third-party Board Support Packages.
:::

- To add the WisBlock Core boards on your Arduino board, you need to install the RAKwireless Arduino BSP. You can follow this complete guide on [adding the BSP in Arduino IDE](https://learn.rakwireless.com/hc/en-us/articles/26687371039383-How-To-Perform-Installation-of-Board-Support-Package-in-Arduino-IDE). You can also have a look at the RAKwireless Arduino BSP [GitHub repository](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

In Arduino IDE, once you installed the BSP, some examples for RAK4631 will be automatically included on the list of examples when you select WisBlock Core RAK4631 Board in the Board Manager.

**Programming RAK3401 via Platform IO:**

- [Platform IO for RAK3401 complete setup guide](https://learn.rakwireless.com/hc/en-us/articles/26687276346775-How-To-Perform-Installation-of-Board-Support-Package-in-PlatformIO)

:::tip NOTE
Updated and complete WisBlock examples can be found in the [WisBlock Examples](https://github.com/RAKWireless/WisBlock/tree/master/examples) repository which contains source codes that you can copy-paste and upload.

Aside from that, each WisBlock Modules has its own quick start guide to help you in your WisBlock journey.
:::

## Product Configuration

### Hardware Setup

#### RAK3401 to WisBlock Base

The RAK3401 will not work without a WisBlock Base board. The WisBlock Base provides a USB connection for programming the RAK3401. It also provides a power source and various interfaces to RAK3401 so that it can be connected to other WisBlock modules via different module slots.

RAKwireless offers many [WisBlock Base Boards](https://store.rakwireless.com/collections/wisblock-base) compatible with WisBlock Core. It is highly recommended for you to look on these WisBlock Base boards to see what matches your requirements in terms of available module slots, power supply options, and overall size.

To illustrate, RAK3401 can be connected to RAK19007 WisBlock Base, as shown in **Figure 1**.

> **Image:** RAK3401 Connection to WisBlock Base RAK19007

There are few pins that are exposed on RAK19007-O, and you can easily use them via header pins. The labels are at the back, as shown in **Figure 2**.

> **Image:** WisBlock Base exposed pins

More information can be found on the [official documentation of the specific WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) you used in your project.

For RAK19007 WisBlock Base with RAK3401 WisBlock Core, the accessible GPIO pins are defined as follows in the Arduino IDE and Platform IO:

- `WB_IO1` for IO1 pin
- `WB_IO2` for IO2 pin (Also used to control the 3.3 V supply of some WisBlock Modules to achieve low-power IoT devices.)
- `WB_A0` for AIN

There are usable LEDs as well that can be controlled by the RAK4631 on the WisBlock Base board:

- `LED_GREEN`
- `LED_BLUE`

UART1 and I2C_1 are also exposed on the header of the WisBlock Base board.

- RAK3401 has a native USB peripheral onboard (Serial), which is used for programming and Serial debugging and two usable hardware **UART1** and **UART2** (Serial 1 and Serial 2). **UART1** is accessible to WisBlock Slot A, WisBlock IO slot, and the exposed header pins. **UART2** is accessible only on the WisBlock IO slot.
- The **I2C_1** header pins are as well shared to the WisBlock Base Slots A to D. The second **I2C_2** is available only on the WisBlock IO slot.

#### RAK3401 to WisBlock Modules

RAK3401 WisBlock Core is designed to be interfaced with other [WisBlock Modules](https://store.rakwireless.com/pages/wisblock) like sensors, displays, and other interfaces. You need to connect these modules to the compatible slots on the WisBlock Base.

Each WisBlock Modules that will be used with RAK3401 WisBlock Core have a dedicated quick start guide you can follow on how to connect to the WisBlock Base.

Listed are the quick start guide of some [WisBlock modules you can buy from our store](https://store.rakwireless.com/pages/wisblock):

:::tip NOTE
The listed links are just examples. **All WisBlock Modules** have their own quick start guide that you can use as a reference to get started on specific modules.
:::

- [RAK1901 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak1901/quickstart/)
- [RAK1902 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak1902/quickstart/)
- [RAK1903 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak1903/quickstart/)

**Figure 3** shows an illustration on how you can combine various WisBlock Modules with the RAK3401 WisBlock Core via the WisBlock Base board.

> **Image:** RAK3401 Connection to WisBlock Base and other WisBlock Modules

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

**Figure 4** shows how to mount the RAK3401 module on top of a WisBlock Base board (RAK19007). Follow carefully the procedure defined in [WisBlock module assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard) in order to secure the connection safely. Once attached, carefully fix the module with one or more pieces of M1.2 x 3 mm screws depending on the module.

> **Image:** RAK3401 Mounting Sketch

##### Disassembling

The procedure in disassembling any type of WisBlock modules is the same.

1. First, remove the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

> **Image:** Detaching silkscreen on the WisBlock module

3. Apply force to the module at the position of the connector, as shown in **Figure 7,** to detach the module from the baseboard.

> **Image:** Applying even forces on the proper location of a WisBlock module

#### BLE Antenna

Another important part component of RAK3401 is the antenna.

> **Image:** BLE Antenna

You need to ensure that the antenna is properly connected to have a good BLE signal. Do not power the module without an antenna connected to the IPEX connector to avoid damage to the RF section of the chip.

:::warning
When using the Bluetooth Low Energy transceiver, make sure that an antenna is always connected. Using this transceiver without an antenna can damage the system. Make sure to fix the module with the screws to ensure a proper function.
:::

#### Battery and Solar Connection

RAK3401 can be powered via the USB cable or Li-Ion/LiPo battery via the dedicated connectors, as shown in **Figure 11**. The matching connector for the battery wires is an [JST PHR-2 2 mm pitch female](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable).

This illustration uses RAK19007 as WisBlock Base. There are other [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base) boards available and you need to check the datasheet of the specific WisBlock Base board for the right polarity and other parameters.

:::warning

- Batteries can cause harm if not handled properly.
- Only 3.7-4.2 V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5 V solar panels are supported. Do not use 12 V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires match the polarity on the WisBlock Base board. Not all batteries have the same wiring.

:::

> **Image:** WisBlock Base Connection

> **Image:** Battery Connection

The battery can be recharged as well via small solar panel, as shown in **Figure 13**. The matching connector for the solar panel wires is an [JST ZHR-2 1.5 mm pitch female](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable).

> **Image:** Solar Panel Connection

Specification of the battery and solar panel can be found on the datasheet of the WisBlock Base.

### Software Setup

RAK3401 WisBlock Core is designed to be interfaced with other WisBlock Modules like sensors, displays, and other interfaces. To make useful devices, you need to upload a source code to the RAK3401. Before you continue, you should have the [Arduino BSP or Platform IO already setup](https://docs.rakwireless.com/product-categories/wisblock/rak4631/quickstart/#software).

#### RAK3401 Example Repository

To quickly build your IoT device with less friction, example codes for RAK4631 can be used with the RAK3401, which can be used on all WisBlock Modules are provided.

You can access the codes on the [WisBlock Example code repository](https://github.com/RAKWireless/WisBlock/tree/master/examples). The example codes compatible only with RAK3401 are in the folders `RAK4631`. The shared examples of the WisBlock Core are in the `common` folder.

:::tip NOTE
All examples for the RAK4631 will work on the RAK3401, with exception of the LoRa and LoRaWAN examples.
:::

To use these examples, you have two options: **Arduino IDE** or **Platform IO**.

##### RAK3401 on Arduino IDE

Some example codes of various WisBlock Modules like the RAK1901 and RAK1902 are available in the Arduino IDE once you install the [BSP for the Arduino IDE](https://docs.rakwireless.com/product-categories/wisblock/rak4631/quickstart/#software), as shown in Figure 14. The updated and complete WisBlock examples are still in the [WisBlock Examples](https://github.com/RAKWireless/WisBlock/tree/master/examples).

> **Image:** RAK3401 WisBlock Core Examples

It is highly recommended to also check the dedicated quick start guide that you can follow on various WisBlock Modules. Each quick start guide of these modules contains the detailed steps on how to open the example codes and upload them to the RAK3401.

Listed are the examples where you can check the Software Setup on the quick start guide of the following WisBlock Modules:

:::tip NOTE
The listed links are just examples. **All WisBlock Modules** have their own quick start guide that you can use as a reference to get started on specific modules.
:::

- [RAK1901 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak1901/quickstart/)
- [RAK1902 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak1902/quickstart/)
- [RAK1903 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak1903/quickstart/)

##### RAK3401 on Platform IO

For the Platform IO, get the example codes on the [WisBlock Example code repository](https://github.com/RAKWireless/WisBlock/tree/master/examples) and add the necessary libraries individually. Then you can compile the example code.

:::tip NOTE
To use the RAK3401, use the RAK4631 board in the platformio.ini file. The RAK3401 is compatible with the RAK4631, only the LoRa transceiver is not available.
:::

## Miscellaneous

### How to Check If You Have the Updated RAK3401 Bootloader

:::tip NOTE
The RAK3401 and the RAK4631 are using the same bootloader. The following guide is for the RAK4631, but can be used as well for the RAK3401.
:::

You need to connect the RAK3401 to the PC via USB cable and double click the reset button on the WisBlock Base.

There will be a new drive named `RAK4631` that will be shown on your folder explorer. Inside this drive, there will be a text file named `INFO_UF2.TXT`, as shown in **Figure 18**.

> **Image:** RAK3401 drive content

If you open `INFO_UF2.TXT`, you'll see `Date: Dec  1 2021`, as shown in **Figure 19**.

> **Image:** INFO_UF2.TXT content

If you have a different drive name or folder date, it means you do not have the updated RAK3401 Bootloader and you need to update it.

### Updating the Bootloader

RAK3401 WisBlock Core is programmed with a USB bootloader so that you can upload application firmware to it without using any external tools like Jlink and other programmers/debuggers. However, there are situations that you need to update the bootloader when there is an updated version that supports new features, improvements, and bug fixes.

There are various ways to update the bootloader like via USB, Bluetooth, and Jlink. The procedure for these methods is explained in this guide.

#### Bootloader Update via USB

In this method, you need two things that must be in the same directory:

1. Adafruit-nrfutil utility program
2. RAK4631 Bootloader FW

##### For Windows

Download the [adafruit-nrfutil.exe (you need to unzip the downloaded file)](https://github.com/adafruit/Adafruit_nRF52_nrfutil/releases/download/0.5.3.post17/adafruit-nrfutil--0.5.3.post17-win.zip) and the latest [RAK4631 bootloader firmware](https://github.com/RAKWireless/WisBlock/releases).

:::tip NOTE
Detailed information about the RAK4631 Bootloader can be found on the [bootloader repository](https://github.com/RAKWireless/WisBlock/blob/master/bootloader/RAK4630).
:::

Once you downloaded these files, you need to put them in the same directory/folder on your computer.

For simplicity, this guide will assume the files are in C: drive.

> **Image:** Adafruit-nrfutil and RAK4631 Bootloader file in C: drive

When the files are ready, you need to open the Windows Command Prompt application. Then you need to change the location to C:\.

`cd C:\`

After that, you can now execute the update using this command:

`adafruit-nrfutil.exe --verbose dfu serial --package WisCore_RAK4631_Board_Bootloader.zip --port COM19 -b 115200 --singlebank --touch 1200`

> **Image:** RAK4631 Bootloader Updated Successfully

You need to determine the right COM port number of your device. COM19 on the command above is only for illustration. You will get an error if you are not connected to the right COM port number.

##### For Linux

You can get and install adafruit-nrfutil via pip3.

`sudo pip3 install adafruit-nrfutil`

or

`pip3 install --user adafruit-nrfutil`

Then download the latest [RAK4631 bootloader firmware](https://github.com/RAKWireless/WisBlock/releases).

Open a new terminal window and connect the RAK3401 to the PC via USB. Now use the `dmesg` command to display system information and check if the USB device has been recognized by Linux.

If the RAK3401 USB device is recognized, a listing for the device similar to the one below will be displayed.
```
usb 1-1: New USB device found, idVendor=239a, idProduct=0029, bcdDevice= 1.00
usb 1-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
usb 1-1: Product: WisBlock RAK4631
usb 1-1: Manufacturer: RAKWireless
usb 1-1: SerialNumber: XXXXXXXXXXXXXXXX
usb-storage 1-1:1.2: USB Mass Storage device detected
scsi host1: usb-storage 1-1:1.2
usbcore: registered new interface driver usb-storage
cdc_acm 1-1:1.0: ttyACM0: USB ACM device
usbcore: registered new interface driver cdc_acm
```
The line `cdc_acm 1-1:1.0: ttyACM0: USB ACM device` indicates that the port **/dev/ttyACM0** has been allocated for RAK4631.

After determining the port name, go to the directory where the bootloader FW file `WisCore_RAK4631_Board_Bootloader.zip` is located.

Then execute the following command:

`adafruit-nrfutil --verbose dfu serial --package WisCore_RAK4631_Board_Bootloader.zip -p /dev/ttyACM0 -b 115200 --singlebank --touch 1200`

##### For macOS

The same with Windows and Linux procedures, download the latest [RAK4631 bootloader firmware](https://github.com/RAKWireless/WisBlock/releases).

There are two ways to update the RAK3401 bootloader in macOS:

- If you have Python installed, you can follow the same steps for Linux.

- Another way is by creating a macOS executable. To do this method, download [adafruit-nrfutil-macos](https://github.com/adafruit/Adafruit_nRF52_nrfutil/releases/download/%24(APPVEYOR_REPO_TAG_NAME)/adafruit-nrfutil-macos) and make it executable.

Usually, the `adafruit-nrfutil-macos` file will go to the downloads folder.

The next step after downloading the file is to open the terminal and go to the downloads directory or the location where you put the downloaded file. It will be the change directory command where the **username** will depend on your macbook `cd /Users/username/Downloads` or you can directly try `cd Downloads`.

And then execute this command:

`chmod +x adafruit-nrfutil-macos`

> **Image:** Executable adafruit-nrfutil-macos

You also need to determine the port name of the RAK4631 using the command:

`ls /dev/cu.*`.

> **Image:** Checking the RAK4631 USB port connection

After all these steps, you can now upload the latest RAK4631 Bootloader Firmware by executing this command:

`./adafruit-nrfutil-macos --verbose dfu serial --package WisCore_RAK4631_Board_Bootloader.zip -p /dev/cu.usbmodem411 -b 115200 --singlebank --touch 1200`

> **Image:** Updated RAK4631 Bootloader

Your RAK3401 will now have the updated Bootloader Firmware.

#### Bootloader Update via Bluetooth

Updating the firmware via BLE is also possible.

The complete guide is on the [RAK4631 Bootloader repository using BLE](https://github.com/RAKWireless/WisBlock/tree/master/bootloader/RAK4630#update-over-ble).

#### Bootloader Update via Jlink

Updating the firmware via Jlink is possible as well.

The complete guide is on the [RAK4631 Bootloader repository using Jlink](https://github.com/RAKWireless/WisBlock/tree/master/bootloader/RAK4630#update-over-jlink).

