---
title: RAK4260 WisDuo Breakout Board Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK4260 Breakout Board. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: "https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/rak4260-breakout.png"
keywords:
  - quickstart
  - RAK4260 Breakout Board
  - wisduo
sidebar_label: Quick Start Guide
slug: /product-categories/wisduo/rak4260-breakout-board/quickstart/
download: true
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK4260 WisDuo Breakout Board Quick Start Guide

## Prerequisites

The next two sections list the components and tools required to get started with the development board. While some components are included in the package, others need to be provided separately.

Before going through the steps in the installation guide of the RAK4260 Breakout Board, make sure to prepare the necessary items listed below:

### Hardware Tools

- <a href="https://store.rakwireless.com/products/rak4260-breakout-board?utm_source=RAK4260BreakoutModule&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">**RAK4260 Breakout Board**</a> (provided) – including LoRa antenna, Dupont lines (13x)
- USB to UART adapter – CH340 for example (not provided)
- <a href="https://store.rakwireless.com/products/daplink-tool?utm_source=RAKDAP1&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAKDAP1 DAPLink Tool</a> (not provided)
- Gateway in range, for testing (not provided)
- Windows PC (not provided)

### Software Tools

- <a href="https://www.microchip.com/mplab/microchip-studio" target="_blank">Microchip Studio</a>
- <a href="https://downloads.rakwireless.com/#LoRa/Tools/" target="_blank">RAK Serial Tool</a>
- <a href="https://www.driverscape.com/download/usb-serial-ch340" target="_blank">CH340 Drivers</a>
- <a href="https://www.thethingsnetwork.org/get-started" target="_blank">The Things Network</a> account
- <a href="https://github.com/RAKWireless/RAK4260-LoRaNode-demo" target="_blank">Sample Code</a>

## Package Inclusions

- RAK4260 Breakout Board
- LoRa antenna
- Dupont lines (24x)


## Product Configuration

### Interface with RAK4260 Breakout Board

:::warning
Before powering the **RAK4260 Breakout Board**, ensure the included LoRa antenna is installed. Failure to do so may damage the board.
:::

#### USB to UART

1. Connect the USB-to-UART adapter to the pin header on the RAK4260 using a set of 4 DuPont lines. Refer to **Figure 1** for proper wiring guidance.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/powering-and-interfacing-with-the-board.png"
  width="100%"
  caption="Powering up and interfacing with the board"
  zoomMode={true}
/>

2. Open the Device Manager by pressing `Windows` + `R`, typing `devmgmt.msc`, and pressing Enter. Alternatively, you can search for `devmgmt.msc` in the **Start Menu**.

3. Look for **Ports (COM & LPT)** and locate the entry named **USB-SERIAL CH340**. Note the COM port number, as you will need it to connect to the board. If you have a different model, the name should still include **USB-SERIAL** in some form.

:::tip NOTE
Windows 10 should recognize the board and automatically install drivers.
If you didn't find any port with the name USB-Serial CH340, make sure to install the CH340 Drivers in your Windows PC.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/com-port-settings.png"
  width="100%"
  caption="COM Port settings"
  zoomMode={true}
/>

4. Open the RAK Serial Port Tool. Select the COM Port number (the one you noted in the previous step) and set the **Baud Rate to 115200**. Click **OPEN**, and you should be connected to the board and be able to send commands.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/configuring-the-rak-serial-port-tool.png"
  width="90%"
  caption="Configure the RAK Serial Port Tool"
  zoomMode={true}
/>

#### DAPLink Connection

Connect the tool as shown in **Figure 4** and **Figure 5**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/connection.png"
  width="75%"
  caption="DAPLink to RAK4260 Breakout Board"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/pin.png"
  width="60%"
  caption="DAPLink connection"
  zoomMode={true}
/>


### Connect with The Things Network (TTN)

The Things Network enables low-power devices to connect to long-range gateways, facilitating data exchange with applications over an open-source, decentralized network. Learn more about it on the <a href="https://www.thethingsnetwork.org/docs/" target="_blank">**The Things Network** </a>website.

This section will guide you through connecting the **RAK4260 Breakout Board** to **The Things Network (TTN)**.

1. If you don't have an account yet, head on to the <a href="https://www.thethingsnetwork.org/" target="_blank">TTN site</a> and create one. Once done, log in to your account and go to the console.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/ttn-home-page.png"
  width="100%"
  caption="The Things Network Home Page"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/ttn-console-page.png"
  width="100%"
  caption="TTN Console Page"
  zoomMode={true}
/>

2. Choose **APPLICATIONS**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/application-page.png"
  width="100%"
  caption="Application Page"
  zoomMode={true}
/>

#### Add an Application

3. Click the **add application** button

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/adding-an-application.png"
  width="100%"
  caption="Add an Application"
  zoomMode={true}
/>

Here are the key points to consider when adding an application to TTN:

  - **Application ID**: A unique identifier on the TTN network, written in lowercase with no spaces.
  - **Description**: A short and concise human-readable description of your application.
  - **Application EUI**: Automatically generated by TTN.
  - **Handler Registration**: Select the handler to which you want to register this application.


4. After filling in the necessary information, press the **Add application**. If the page is the same as shown in **Figure 10**, then you have successfully registered the application.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/application-overview.png"
  width="100%"
  caption="Application Overview"
  zoomMode={true}
/>

#### Register the Device

5. Scroll down to the **Devices** section, or click the **Devices** button at the top.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/device-section.png"
  width="100%"
  caption="Device Section"
  zoomMode={true}
/>

6. Click **Register device**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/add-your-device.png"
  width="100%"
  caption="Add your Device"
  zoomMode={true}
/>

Here are the key details to note when registering your device:

- **Device ID**: A unique identifier for your RAK4260 Breakout Board within your application, which you must enter manually.
- **Device EUI**: A unique identifier for your device within the network, which can be changed later if needed.
- **App Key**: Used to secure communication between the device and the network.
- **App EUI**: A unique identifier for the application in which you are registering the device.


7. Fill in the **Device ID** field and generate a random **Device EUI** by clicking the arrows. Leave the remaining fields unchanged, then click **Register**. Your device will now be registered under the corresponding application.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/device-overview.png"
  width="100%"
  caption="Device Overview"
  zoomMode={true}
/>

In the Device Overview, there are two options for the **Activation Method**: **OTAA** and **ABP**. The default option is **OTAA** as shown above.


#### OTAA Mode

**OTAA** stands for **Over-The-Air Activation**. While detailed information about OTAA is beyond the scope of this document, it is essential to understand that a device requires three parameters: **Device EUI**, **Application EUI**, and **App Key**. These parameters, as briefly explained in the previous section, must be set correctly for the LoRa Server to grant network access.

These parameters can be obtained from the **Device Overview page**, where they are conveniently grouped together.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/device-overview-parameters.png"
  width="100%"
  caption="Device Overview Parameters"
  zoomMode={true}
/>

Since these values are randomly generated by TTN, you need to update your **RAK4260 Breakout Board** with them to register it on the network. As previously mentioned, this must be done directly in the source code, followed by compiling and flashing it to the device.

The next section will guide you through this process using **Atmel Studio**.

##### Parameter and Firmware Setup

Execute the following steps to connect your device with the TTN. Register and then fill in the parameters obtained upon registering.

###### Edit OTAA Parameters in the Code

1. Open your Atmel Studio and navigate to the demo firmware you downloaded from the <a href="https://github.com/RAKWireless/RAK4260-LoRaNode-demo" target="_blank">RAKwireless GitHub repository</a>.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/atmel-studio-main-page.png"
  width="100%"
  caption="Atmel Studio main page"
  zoomMode={true}
/>

2 Go to **File** > **Open** > **Project/Solution**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/open-the-sample-project.png"
  width="100%"
  caption="Open the sample project"
  zoomMode={true}
/>

3. Go to the folder where you downloaded the GitHub repository and select the **APPS_ENDDEVICE_DEMO1** project file (it is in the directory with the same name as the file). Then click **Open**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/demo-firmware-project-file.png"
  width="100%"
  caption="Demo firmware project file"
  zoomMode={true}
/>

4. Once your project is loaded, you will see a file structure containing folders and files that you can edit. Copy the values of the three (3) parameters shown in **Figure 14** and paste them into the **`conf_app.h`** file. This file is located in the **`src`** config folder, accessible through the Solution Explorer tree.

Here are the required parameters:
- **Device EUI**
- **Application EUI**
- **Application Key**

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/otaa_atmel_studio.png"
  width="100%"
  caption="Device configuration file (OTAA parameters)"
  zoomMode={true}
/>

5. After replacing the default values with those for the device registered with TTN, you can proceed to compile the project.

:::tip NOTE
There is no need to edit anything else in order to compile the firmware that will allow you to connect to the TTN network.
:::

###### Compile the Code

6. Compile the code by going to the **Build** > **Build Solution**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/build_solution.png"
  width="100%"
  caption="Compile the code"
  zoomMode={true}
/>

7. The output should have no errors, as shown in **Figure 20**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/successful-compiling-of-the-code.png"
  width="100%"
  caption="Compile the code"
  zoomMode={true}
/>

###### Flash the Firmware

8. Find the output file in the **Debug** folder of the directory where you downloaded the firmware. Refer to **Figure 21** for guidance.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/firmware-hex-file.png"
  width="100%"
  caption="Firmware .hex file"
  zoomMode={true}
/>

9. With the firmware now ready, proceed to flash it using the **RAKDAP1** hardware tool and the **pyOCD** software tool.

###### Flash the Firmware Using RAKDAP1

Refer to the <a href="https://docs.rakwireless.com/product-categories/accessories/rakdap1/overview/" target="_blank">RAKDAP1 Flash and Debug Tool</a>.

##### Connect to TTN

Connect the USB to the UART adapter to the pin header on the RAK4260 via a set of four (4) DuPont lines. Refer to the [Interfacing with RAK4260 Breakout Board](#interfacing-with-rak4260-breakout-board) section for more details.

###### Regional Band and Join Network Setup

1. When you open the **RAK Serial Port Tool**, it should display the details shown in **Figure 22**, provided it has been less than 5 seconds since the board was powered on. The firmware is designed to initialize with default settings 5 seconds after powering up.

:::tip NOTE
EU868 is used for the region as an example. This section shows how to change the default region and connect with the network.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/startup-default-output.png"
  width="45%"
  caption="Start up default output"
  zoomMode={true}
/>

2. After the 5-second period has elapsed, the current configurations will be reported. These configurations include:
  - **Class A**
  - **OTAA**
  - **Unconfirmed LoRa Frames**
  - **Fport - 1**

:::tip NOTE
These settings are not adjustable at this stage. If you want to change them, you need to start over at the stage where you modify the firmware files before compiling them.
:::

3. Using **Figure 23** as a reference, you will see a list of four (4) options. To navigate to the **Main Menu**, send the number **4**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/configuration-menu.png"
  width="45%"
  caption="Configuration menu"
  zoomMode={true}
/>

4. Send the number **1** to select the **EU868 Regional Band**. Alternatively, you can choose a different number based on your specific requirements.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/band-selection-menu.png"
  width="45%"
  caption="Band selection menu"
  zoomMode={true}
/>

5. The device will automatically attempt to join the LoRaWAN network using the **Device EUI**, **Application EUI**, and **Application Key** configured in the firmware file.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/network-join-parameters-set.png"
  width="45%"
  caption="Network join parameters set"
  zoomMode={true}
/>

6. If the device successfully joins the network, it will report the assigned **Device Address**, along with the parameters (e.g., Class A, OTAA). The **Configuration Menu** will then be displayed again, allowing you to send another command.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/successful-network-join.png"
  width="45%"
  caption="Successful network join"
  zoomMode={true}
/>

###### Uplink LoRa Frame Testing

6. In the main menu, select **Option 2** to send an uplink LoRa Frame.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/sending-data-to-the-server.png"
  width="45%"
  caption="Send data to the server"
  zoomMode={true}
/>

:::tip NOTE
The firmware uploaded into the RAK4260 Breakout Board is just an example. Thus, the data sent are just dummy temperature readings (the original Microchip code was for a board with an actual temperature sensor). It will be reported as output together with the transmission is successful, as shown in **Figure 28**.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4260-breakout-board/quickstart/sending-data-successful.png"
  width="45%"
  caption="Send data to the server (successful)"
  zoomMode={true}
/>

This should be sufficient to prove that the board functions as intended, and it can send data over the network after successfully joining it. As this module is intended for development, the example firmware is limited to this functionality.

You can use this project as a base to develop a more complex firmware using the Microchip LoRaWAN Stack (MLS).

<RkBottomNav/>