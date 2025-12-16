---
title: RAK3244 BastWAN Breakout Board Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK3244. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: https://images.docs.rakwireless.com/wisduo/bastwan/bastwan.png
keywords:
  - BastWAN
  - RAK3244
  - quickstart
  - wisduo
sidebar_label: Quick Start Guide
slug: /product-categories/wisduo/bastwan/quickstart/
download: true
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK3244 BastWAN Breakout Board Quick Start Guide

## Description

The **RAK3244 BastWAN** adapts the RAK4260 module into a Feather-compatible format, developed by <a href="http://www.electroniccats.com/" target="_blank">ElectronicCats</a>. At its core, the RAK4260 LPWAN Module is based on Microchip’s SAM R34 (R34J18B), a SiP device that integrates a 32-bit ARM Cortex-M0+ MCU with a LoRa transceiver. It provides full coding support through the Arduino™ IDE.

For more information about the board, check the [ElectronicCats RAK3244 BastWAN repository](https://github.com/ElectronicCats/Bast-WAN).

## Hardware Setup

The BastWAN is a Feather breakout board with everything you need to get started on your project.

:::warning
Before powering the Feather Board, ensure that the included LoRa antenna is connected. Failure to do so may damage the board.
:::

## Software Setup

### Burn the Bootloader

RAK3244 BastWAN board comes with a pre-flashed bootloader upon purchase. However, if it is necessary to replace the bootloader, you can burn the <a href="https://github.com/RAKWireless/Evaluation_Boards/tree/master/RAK4260/Arduino" target="_blank">bootloader-bast-wan-v3.4.0.bin</a> with Jlink as demonstrated below:

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/download.png"
  width="60%"
  caption="Flash the bootloader"
  zoomMode={true}
/>

You can also flash the bootloader by using the <a href="https://docs.rakwireless.com/product-categories/accessories/rakdap1/overview/" target="_blank">RAKDAP1 Flash and Debug Tool</a>. The guide on how to connect RAK3244 to RAKDAP1 can be found on <a href="https://docs.rakwireless.com/product-categories/wisduo/bastwan/datasheet/#interfaces" target="_blank">SWD Programming Interface section of RAK3244 datasheet</a>.

After ensuring the correct wiring connection, flash the bootloader using the `pyocd` command. If you do not have pyocd installed on your system, check the <a href="https://docs.rakwireless.com/product-categories/accessories/rakdap1/quickstart/#pyocd-installation" target="_blank">pyocd installation guide</a>.

```
pyocd flash -t atsaml21j18a bootloader-bast-wan-v3.4.0.bin
```

Once the command is executed, the bootloader should be flashed successfully. You can now connect the RAK3244 BastWan to your PC.

### Configure The Things Network (TTN)

This section covers **The Things Network (TTN)** and the procedure for setting up the platform to connect with the RAK3244 BastWAN.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/3.ttn-context.png"
  width="65%"
  caption="RAK3244 BastWAN in the context of the TTN"
  zoomMode={true}
/>

As depicted in **Figure 2**, the RAK3244 BastWAN is one of the devices positioned on the left side. In an IoT solution, its purpose is to sense relevant process variables and transmit the data to backend servers in the cloud. The processed data is then integrated into a larger solution to enable efficiency, traceability, predictability, and other capabilities.

The RAK3244 BastWAN can be part of this ecosystem, and this section aims to demonstrate how easy it is to send data to TTN using the LoRaWAN protocol. To accomplish this, the RAK3244 BastWAN must be within the coverage of a LoRaWAN gateway.

:::tip NOTE
The device name used for this setup is **"RAK4260"**, as it is the core of the RAK3244 BastWAN. However, you can assign any device name you prefer for your setup.
:::

<b>Sign up and Login</b>

If you don’t have an account yet, visit the <a href="https://www.thethingsnetwork.org/" target="_blank">TTN website</a> to create one. After completing the registration, log in to your account and navigate to the **Console**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/4.ttn-home.png"
  width="100%"
  caption="The Things Network Home Page"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/5.ttn_console.png"
  width="100%"
  caption="TTN Console Page"
  zoomMode={true}
/>

#### Create a New Application

1. Choose **APPLICATIONS**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/6.application_section.png"
  width="100%"
  caption="Application Section"
  zoomMode={true}
/>

2. Click the **add application** button.


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/7.adding_application.png"
  width="100%"
  caption="Add an Application"
  zoomMode={true}
/>

* Here are the key points to remember when adding an application:

  - **Application ID**: A unique identifier for your application in the network. It must be in lowercase with no spaces.
  - **Description**: A brief, human-readable summary of your application.
  - **Application EUI**: Automatically generated by The Things Network for your convenience.
  - **Handler Registration**: The handler to which you want to register this application.

3. After entering the required information, click the **Add Application** button. If a page similar to **Figure 8** appears, your application has been successfully registered.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/8.application_overview.png"
  width="100%"
  caption="Application Overview"
  zoomMode={true}
/>

<b>Register a New Device</b>

1. Scroll down until you see the Devices section or click the **Devices** button at the top.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/9.devices.png"
  width="100%"
  caption="Register a New Device"
  zoomMode={true}
/>

2. Then, register a new device by clicking on **register devices**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/10.adding_device.png"
  width="100%"
  caption="Add your Device"
  zoomMode={true}
/>

In this form, the **Device ID** must be unique within the application and consist of lowercase, alphanumeric characters. The other parameters in the form are crucial for the proper functioning of the LoRaWAN protocol:

* Device EUI
* Application Key
* Application EUI

The TTN platform can generate these parameters randomly by leaving those fields empty, or you can enter already existing values.

3. Click the **Register** button at the bottom of this page to finish the process.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/11.device_overview.png"
  width="100%"
  caption="Device Overview"
  zoomMode={true}
/>

Now that the Device EUI, Application EUI, and Application Key are defined, proceed with the setup of RAK3244 BastWAN LoRa configurations.

## Modify and Flash Firmware Using Arduino IDE
This section introduces how to use the RAK3244 BastWAN with the Arduino™ IDE.

### BSP Installation

1. After successfully flashing the bootloader, install the BSP library to add board support for the RAK3244 BastWAN. Open the Arduino IDE and navigate to **File > Preferences**. Copy and paste the following URL into the **Additional Boards Manager URLs** input field:

`https://electroniccats.github.io/Arduino_Boards_Index/package_electroniccats_index.json`

2. Click **OK**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/additional-board-support.png"
  width="60%"
  caption="Arduino additional board support"
  zoomMode={true}
/>

:::tip NOTE
If there is already an existing URL on the textbox, click the button at the right end of the field. This will open an editing window, allowing you to paste the above URL onto a new line as demonstrated in **Figure 12**.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/support-board-add-url.png"
  width="60%"
  caption="Alternative method for additional board support"
  zoomMode={true}
/>

2. Open the **Boards Manager** by navigating through **Tools > Board > Boards Manager**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/boards-manager.png"
  width="60%"
  caption="Arduino boards manager"
  zoomMode={true}
/>

3. In the Boards Manager search bar, look for **Electronic Cats SAMD Boards**. Click **Install** next to **Electronic Cats SAMD Boards**, and wait for the installation to complete before closing the window.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/electronic-cats-samd-boards.png"
  width="60%"
  caption="Install Electronic Cats SAMD Boards"
  zoomMode={true}
/>

4. RAK3244 BastWAN should now be on the list of Boards by navigating through **Tools > Board > Electronic Cats SAMD(L)(C) Core for Arduino**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/bastwan-in-boards.png"
  width="85%"
  caption="RAK3244 BastWAN available in Boards list"
  zoomMode={true}
/>

### LoRaWAN Library Installation

RAK3244 BastWAN board uses the Beelan-LoRaWAN library, which supports LoRaWAN Class A and Class C implementations operating in EU-868, AS-923, US-915, and AU-915 bands. You can recognize this library as the `<lorawan.h>` on the sample code.

To ensure the sample code works, install the **Beelan-LoRaWAN** library. In the Arduino IDE, go to **Tools > Manage Libraries**. Search for **Beelan LoRaWAN** and install the latest version of the library. The window will indicate when the library is successfully installed, as shown in **Figure 15**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/library-installed.png"
  width="70%"
  caption="Beelan LoRaWAN library installed"
  zoomMode={true}
/>

Visit the <a href="https://github.com/BeelanMX/Beelan-LoRaWAN" target="_blank">Beelan-LoRaWAN official GitHub repository</a> for more information.

## First Test

For a quick test, a sample source code is provided for a LoRaWAN Class A node with OTAA support. Download the source code and open it with Arduino IDE.

- <a href="https://github.com/RAKWireless/Evaluation_Boards/tree/master/RAK4260/Arduino/send-class-A-OTAA" target="_blank">Example source code for RAK3244 BastWAN</a>

The following sections will demonstrate how to modify LoRaWAN parameters to establish a connection with The Things Network (TTN).

### Modify LoRaWAN Parameters

For the RAK3244 BastWAN to successfully connect to a LoRaWAN Platform, several parameters must be properly configured. Not doing so will result in connection failure.

The most volatile parameters on LoRaWAN configuration are the Device EUI, Application EUI, and Application Keys. These data must match with the ones on The Thing Network (TTN) platform. Copy the EUIs and Keys from the TTN platform and paste them on the sample source code. **Figure 17** shows the lines of codes that should be modified:

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/dev_app_eui.png"
  width="60%"
  caption="Device EUI, Application EUI, and Application Keys"
  zoomMode={true}
/>

### Compile and Flash the Firmware

Now that the LoRaWAN parameters are set, run the sample program.

Click the **Verify** button on the upper left of Arduino IDE to compile the code. Before uploading the sample firmware, make sure that the RAK3244 BastWAN is connected and recognized by your PC. To verify this, there must be an assigned port on the **Tools** toolbar of Arduino IDE. It should not be grayed out.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/compilation.png"
  width="100%"
  caption="Compilation of sample source code"
  zoomMode={true}
/>

If everything is well, click the **Upload** button and the firmware should be flashed to your RAK3244 BastWAN.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/bastwan/quickstart/uploading.png"
  width="100%"
  caption="Upload the sample source code"
  zoomMode={true}
/>

The RAK3244 BastWAN will try to join the LoRaWAN network server, and if it is successful, it will send a string to verify its presence. You can find more details of the operation by examining the sample source code and opening the serial monitor.

Feel free to experiment with your own and explore the capabilities of RAK3244 BastWAN.


<RkBottomNav/>