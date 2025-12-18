---
title: WisDuo RAK4200 Breakout Board Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK4200 Breakout Board. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: "https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/rak4200-breakout.png"
keywords:
  - quickstart
  - RAK4200 Breakout Board
  - wisduo
sidebar_label: Quick Start Guide
slug: /product-categories/wisduo/rak4200-breakout-board/quickstart/
download: true
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK4200 WisDuo Breakout Board Quick Start Guide

## Prerequisites

Before going through the steps in the installation guide of the RAK4200 Breakout Board, make sure to prepare the necessary items listed below:

### Hardware

- <a href="https://store.rakwireless.com/products/rak4200-breakout-board?utm_source=RAK4200BreakoutModule&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAK4200 Breakout Board</a> (provided) – including LoRa antenna, Dupont lines (13x)
- USB to UART adapter – CH340 for example (not provided)
- Gateway in range, for testing (not provided)
- <a href="https://store.rakwireless.com/products/daplink-tool?utm_source=RAKDAP1&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAKDAP1 DAPLink Tool</a> (not provided)

### Software

- RAK Serial Port Tool
- CH340 Drivers
- <a href="https://www.thethingsnetwork.org/get-started" target="_blank">The Things Network</a> account

## Package Inclusions

- RAK4200 Breakout Board
- LoRa antenna
- Dupont lines (18x)


## Product Configuration

### Interface with RAK4200 Breakout Board

1. To interface with the RAK4200 Breakout Board with a Windows Machine, download the <a href="https://downloads.rakwireless.com/#LoRa/Tools/" target="_blank">**RAK Serial Port Tool**</a>.

:::warning
Before powering the RAK4200 Breakout Board, ensure the included LoRa antenna is properly installed. Failure to do so could damage the board.
:::

2. Connect the USB-to-UART adapter to the pin header on the RAK4200 using 4 DuPont lines. Refer to **Figure 1** for proper wiring instructions.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/connection.png"
  width="100%"
  caption="Power up and interface with the board"
  zoomMode={true}
/>

3. Open the Device Manager by pressing `Windows` + `R`, typing `devmgmt.msc`, and pressing Enter. Alternatively, you can search for `devmgmt.msc` in the **Start Menu**.

:::tip NOTE
Windows 10 should recognize the board and automatically install drivers. However, if it is missing in the COM and LPT ports list, you need to manually install the CH340 Drivers.
:::

4. Look for **Ports (COM & LPT)** and locate the entry named **USB-SERIAL CH340**. Note the COM port number, as you will need it to connect to the board. If you have a different model, the name should still include **USB-SERIAL** in some form.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/select-port.png"
  width="70%"
  caption="COM Port settings"
  zoomMode={true}
/>

5. Open the RAK Serial Port Tool. Select the COM Port number (the one you noted in the previous step) and set the **Baud Rate to 115200**. Click **OPEN**, and you should be connected to the board and be able to send commands.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/conect-device.png"
  width="80%"
  caption="Configure the RAK Serial Port Tool"
  zoomMode={true}
/>

### Connect with The Things Network (TTN)

The Things Network enables low-power devices to connect to long-range gateways, forming an open-source, decentralized network to exchange data with applications. Learn more at <a href="https://www.thethingsnetwork.org/docs/" target="_blank">**The Things Network**</a>.

In this section, you will connect the RAK4200 Breakout Board to **The Things Network (TTN)**.

1. If you don't have an account yet, head on to the <a href="https://www.thethingsnetwork.org/" target="_blank">TTN site</a> and create one. Once done, log in to your account and go to the console. See the highlighted box in **Figure 4**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/ttn-homepage.png"
  width="100%"
  caption="The Things Network Home Page"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/ttn-console.png"
  width="100%"
  caption="TTN Console Page"
  zoomMode={true}
/>

2. Choose **APPLICATIONS**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/add-application.png"
  width="100%"
  caption="Application Page"
  zoomMode={true}
/>

#### Add an Application

3. Click the **add application** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/application-input.png"
  width="100%"
  caption="Add an Application"
  zoomMode={true}
/>

:::tip NOTE
Here are the key points to consider when adding an application to TTN:

1. **Application ID**: A unique identifier on the TTN network, written in lowercase with no spaces.
2. **Description**: A short and concise human-readable description of your application.
3. **Application EUI**: Automatically generated by TTN.
4. **Handler Registration**: Select the handler to which you want to register this application.
:::

4. After filling in the necessary information, press the **Add application**. If the page is the same as shown in **Figure 8**, then you have successfully registered your application.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/app-overview.png"
  width="100%"
  caption="Application Overview"
  zoomMode={true}
/>

##### Register Device

4. Scroll down to the **Devices** section, or click the **Devices** button at the top.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/dev-section.png"
  width="100%"
  caption="Device Section"
  zoomMode={true}
/>

6. Click **Register device**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/add-device.png"
  width="100%"
  caption="Add your Device"
  zoomMode={true}
/>

:::tip NOTE
Here are the key points to remember when registering your device:

1. **Device ID**: A unique identifier for your RAK4200 Breakout Board within your application. This must be entered manually.
2. **Device EUI**: A unique identifier for your device on the network. You can modify this later if needed.
:::

7. Fill in the **Device ID** and **Device EUI** fields (you can generate a random Device EUI by clicking the arrows). Leave the other fields unchanged and click **Register**. Your device will now be registered under the corresponding application.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/dev-overview2.png"
  width="100%"
  caption="Device Overview"
  zoomMode={true}
/>

Depending on the authentication method you are using, proceed to either the **OTAA Mode** or **ABP Mode** section.



#### OTAA Mode

When setting up a new device in TTN, the default join mode is **OTAA**. For configuration, you will need the following three parameters: **Device EUI**, **Application EUI**, and **App Key**. These can be obtained from the **Overview page**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/ttn-dev-overview.png"
  width="100%"
  caption="Device Overview Parameters"
  zoomMode={true}
/>

:::tip NOTE
- As an example, join in **OTAA mode**, using the **EU868 frequency**, with the default LoRa class set to **Class A**.

- Execute the following commands one by one, in the given order.
:::

1. Set the LoRa join mode to **OTAA**.

```sh
at+set_config=lora:join_mode:0
```

2. Set the LoRa class to **Class A**:

```sh
at+set_config=lora:class:0
```

3. Set the frequency/region to **EU868**:

```sh
at+set_config=lora:region:EU868
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/otaa-serial1.png"
  width="45%"
  caption="AT Command for OTAA Join Mode, Class and Region"
  zoomMode={true}
/>

:::tip NOTE
Execute the following commands one by one, in the given order.
:::

4. Set the **Device EUI**:

```sh
at+set_config=lora:dev_eui:XXXX
```

5. Set the **Application EUI**:

:::tip NOTE
All zero value Application EUI `at+set_config=lora:app_eui:0000000000000000` is **not supported** and will return error.
:::

```sh
at+set_config=lora:app_eui:XXXX
```

6. Set the **Application Key**:

```sh
at+set_config=lora:app_key:XXXX
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/otaa-serial2.png"
  width="45%"
  caption="AT Command for OTAA Device EUI, Application EUI and Application Key"
  zoomMode={true}
/>

7. Reboot the RAK4200 Breakout Board to save the parameters.

```sh
at+set_config=device:restart
```

8. Then join in OTAA mode:

```sh
at+join
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/otaa-join.png"
  width="45%"
  caption="AT Command for OTAA LoRa Join via RAK Serial Port Tool"
  zoomMode={true}
/>

9. After joining in OTAA mode successfully, try to send data from the RAK4200 Breakout Board to TTN:

```sh
at+send=lora:2:1234567890
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/otaa-send-data.jpg"
  width="45%"
  caption="OTAA Test Sample Data Sent via RAK Serial Port Tool"
  zoomMode={true}
/>

You will see the data sent from the RAK4200 Breakout Board on the TTN website, as shown in **Figure 17**:

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/ttn-traffic.png"
  width="100%"
  caption="OTAA Test Sample Data Sent Viewed in The Things Network"
  zoomMode={true}
/>

## Miscellaneous

### Firmware Update

Before you start working with the RAK4200, it is recommended to keep the RAK4200 module updated to the latest version of the firmware.

:::tip NOTE

For RAK4200 modules with firmware version **V3.0.0.12 and below**, use the <a href="https://www.st.com/en/development-tools/stm32cubeprog.html" target="_blank">STM32CubeProgrammer</a> to upgrade the firmware by uploading the **`.hex` file** (not the `.bin` file) from the [latest RAK4200 firmware](https://downloads.rakwireless.com/#LoRa/RAK4200/Firmware/). Firmware versions below V3.0.0.12 have a different bootloader code and are incompatible with the RAK DFU Tool.

:::

In the following sections, two (2) options for flashing new firmware in a RAK4200 module are shown: **Firmware Upgrade through DAPLink** and **Firmware Upgrade through UART1**.

#### Firmware Upgrade Through DAPLink

Refer to <a href="https://docs.rakwireless.com/product-categories/accessories/rakdap1/quickstart/" target="_blank">RAKDAP1 Flash and Debug Tool Quickstart Guide</a>.


#### Firmware Upgrade Through UART1

##### Minimum Hardware and Software Requirements

| Hardware/Software | Requirements                              |
| :---------------: | :---------------------------------------: |
| Computer          | A Windows/Linux/Mac computer              |
| Firmware File     | Bin firmware downloaded from the website. |
| Others            | A USB to TTL adapter.                     |

##### Firmware Upgrade Procedure

Follow this procedure to upgrade the firmware in Device Firmware Upgrade (DFU) mode through the UART1 interface.

1. Download the latest application firmware of the <a href="https://downloads.rakwireless.com/#LoRa/RAK4200/Firmware/" target="_blank">RAK4200 module</a>.
2. Download the RAK Device Firmware Upgrade (DFU) tool. In this folder are the different DFU tools depending on your machine's OS.
    - <a href="https://downloads.rakwireless.com/#LoRa/Tools/RAK_Device_Firmware_Upgrade_tool/" target="_blank">RAK Device Firmware Upgrade (DFU) Tool</a>
3. Connect the RAK4200 module with a computer through USB to TTL adapter, as shown in **Figure 18**:

4. Open the RAK Device Firmware Upgrade (DFU) tool. Select the serial port and baud rate of the module, and then click on the **Select Port** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/device-firmware-tool.png"
  width="70%"
  caption="Device Firmware Upgrade Tool"
  zoomMode={true}
/>

5. Click on the **Select Firmware** button and choose the application firmware file of the module with the suffix `. bin`.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/select-firmware.png"
  width="70%"
  caption="Select firmware"
  zoomMode={true}
/>

6. Click on the **Upgrade** button to upgrade the device. After the upgrade is complete, the RAK4200 module is now ready to work with the new firmware.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/firmware-upgrading.png"
  width="70%"
  caption="Firmware upgrade"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4200-breakout-board/quickstart/upgrade-success.png"
  width="70%"
  caption="Upgrade successful"
  zoomMode={true}
/>

<RkBottomNav/>