---
title: RAK4270 WisDuo Breakout Board Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK4270 Breakout Board. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: "https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/rak4270-breakout.png"
keywords:
  - quickstart
  - RAK4270 Breakout Board
  - wisduo
sidebar_label: Quick Start Guide
slug: /product-categories/wisduo/rak4270-breakout-board/quickstart/
download: true
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK4270 WisDuo Breakout Board Quick Start Guide

## Prerequisites

Before proceeding with the installation and setup of the RAK4270 Breakout Board, ensure you have the following necessary items prepared:

### Hardware Tools

1. <a href="https://store.rakwireless.com/products/rak4270-breakout-board?utm_source=RAK4270BreakoutBoard&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">**RAK4270 Breakout Board**</a>
2. USB-UART Module <a href="https://store.rakwireless.com/products/daplink-tool?utm_source=RAKDAP1&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">(RAKDAP1 Tool)</a>
3. Gateway in Range for Testing
4. Jumper Wires
5. 3.3&nbsp;V Battery Power Supply
6. A Windows/Mac OS/Linux Computer

### Software Tools
1. <a href="https://downloads.rakwireless.com/#LoRa/Tools" target="_blank">RAK Serial Port Tool</a>
2. <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4270-breakout-board/datasheet/#firmware" target="_blank">RAK4270 Firmware</a>
3. <a href="https://downloads.rakwireless.com/#LoRa/Tools/RAK_Device_Firmware_Upgrade_tool/" target="_blank">RAK Device Firmware Upgrade (DFU) Tool</a>


:::tip NOTE
The bootloader of the RAK4270 Breakout Board is pre-installed during manufacturing, so flashing it is not required. If you suspect that the bootloader on your RAK4270 Breakout Board is damaged, contact RAK support via the <a href="https://forum.rakwireless.com/" target="_blank">RAKwireless forum</a>. For instructions on [upgrading the firmware](#upgrading-the-firmware) of the device, refer to the miscellaneous section of this document.
:::

## Package Inclusions

- 1 pc - RAK4270 Breakout Board (chipset pre-soldered on the board)
- 1 pc - LoRa Antenna

### List of Acronyms

| Acronym | Definition                          |
| ------- | ----------------------------------- |
| DFU     | Device Firmware Upgrade             |
| JTAG    | Joint Test Action Group             |
| LoRa    | Long Range                          |
| OTAA    | Over-The-Air-Activation             |
| ABP     | Activation-By-Personalization (ABP) |
| TTN     | The Things Network                  |
| TTS     | The Things Stack                    |

## Product Configuration

### Interface with RAK4270 Breakout Board

RAK4270 Breakout Board can be configured using AT commands via the UART interface. You need a USB to UART TTL adapter to connect the RAK4270 board to the PC's USB port and a serial terminal tool.

Use the <a href="https://docs.rakwireless.com/product-categories/accessories/rakdap1/overview/" target="_blank">RAKDAP1</a> as the USB-to-UART interface device. The RAKDAP1 is compatible with other RAK modules and serves as both a debugging tool and firmware uploader. It is also highly recommended to use the <a href="https://downloads.rakwireless.com/#LoRa/Tools" target="_blank">RAK Serial Port Tool</a> for easily sending AT commands and viewing console output responses.


:::warning
Before powering on the RAK4270 Breakout Board, ensure that the LoRa antenna is properly installed. Failing to do so may result in damage to the board.
:::

#### USB to UART

1. Connect the RAK4270 Breakout Board to the USB-UART interface, as shown in **Figure 1** and **Figure 2**.

UART1 is used for AT commands input as well as a firmware update. Check the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4270-breakout-board/datasheet/#pin-definition" target="_blank">RAK4270 Breakout Board Pin Definition</a> on the datasheet for complete details.

<RkImage
 src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/interfacing-with-rak4270-breakout/rakdap1torak4270bb.jpg"
  width="80%"
  caption="RAK4270 Breakout Board Connected to RAKDAP1 USB-UART Interface"
  zoomMode={true}
/>

<RkImage
 src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/interfacing-with-rak4270-breakout/uart_conn.jpg"
  width="50%"
  caption="RAK4270 Breakout Board to USB Uart Module Connection"
  zoomMode={true}
/>

2. Connect the USB-UART module to your Windows PC, open the <a href="https://downloads.rakwireless.com/#LoRa/Tools" target="_blank">RAK Serial Port Tool</a>, and select the correct COM port and baud rate.

<RkImage
 src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/interfacing-with-rak4270-breakout/rib8pvikbtggt9xryvxp.png"
  width="80%"
  caption="Correct Port Number and Baud rate"
  zoomMode={true}
/>


### Connecting to The Things Stack (TTN V3)

This section will show how to connect the RAK4270 board to The Things Stack (TTN V3) platform.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/4.ttn-context.png"
  width="95%"
  caption="The Things Stack diagram"
  zoomMode={true}
/>

As shown in **Figure 4**, The Things Stack is an open-source LoRaWAN Network Server suitable for global, geo-distributed public and private deployments as well as for small, local networks. The architecture follows the LoRaWAN Network Reference Model for standards compliancy and interoperability. This project is actively maintained by <a href="https://www.thethingsindustries.com/" target="_blank">The Things Industries.</a>

LoRaWAN is a protocol for low-power wide-area networks. It allows large-scale Internet of Things deployments where low-powered devices efficiently communicate with Internet-connected applications over long-range wireless connections.

The RAK4270 Breakout Board can function as a device within this ecosystem. This section demonstrates how easily data can be sent to **The Things Stack** using the LoRaWAN protocol. To accomplish this, ensure the RAK4270 board is within the coverage area of a LoRaWAN gateway connected to **The Things Stack** server.


#### Register for TTN and Create LoRaWAN Applications

Before starting, navigate to the <a href="https://console.cloud.thethings.network/" target="_blank">The Things Network platform</a> and select a cluster, as shown in **Figure 5**. **The Things Industries** periodically adds new clusters, so choose the one closest to your location. In this guide, **Europe 1** is selected as an example.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/t_image_1.png"
  width="100%"
  caption="Select Cluster in TTN V3"
  zoomMode={true}
/>

Use your existing login credentials from **TTN V2** if you have an account. Otherwise, create a new account.

1. To register as a new user to TTN, click on **Login with The Things ID**, then select **register** on the next page, as shown in **Figure 6** and **Figure 7**. Fill in all the necessary details and activate.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/t_image_2.png"
  width="100%"
  caption="Log in using TTN account"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/t_image_3.png"
  width="100%"
  caption="Registration of new account"
  zoomMode={true}
/>

2. Log in on the platform using your username/email and password then click **Submit**, as shown in **Figure 8**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/t_image_4.png"
  width="100%"
  caption="Log in to TTN platform"
  zoomMode={true}
/>

3. Click **Authorize** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/t_image_5.png"
  width="100%"
  caption="Authorization to TTN"
  zoomMode={true}
/>

4. Click **Create an application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/t_image_6.png"
  width="100%"
  caption="Create TTN application for your LoRaWAN devices"
  zoomMode={true}
/>

5. To register an application, first enter the required details and information about your application, then click **Create application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/t_image_7.png"
  width="100%"
  caption="Details of the TTN application"
  zoomMode={true}
/>

The next step is to add end-devices to your The Things Stack application. LoRaWAN specification enforces that each end device has to be personalized and activated. Activation can be done either via Over-The-Air-Activation (OTAA) or Activation-By-Personalization (ABP).

:::tip NOTE

- Ensure that you are within the coverage of a LoRaWAN gateway registered with **The Things Stack (TTN V3)**. Without coverage from such a gateway, you will not be able to activate any device registered in your application.

- If no LoRaWAN gateway coverage is available in your location, RAKwireless offers <a href="https://store.rakwireless.com/collections/wisgate" target="_blank">LoRaWAN gateways</a> that can be connected to **The Things Stack (TTN V3)**.

:::

#### The Things Stack OTAA Device Registration

1. Go to your application console to register a device. To start adding an OTAA end-device, click **+ Add end device**, as shown in **Figure 12**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/t_image_8.png"
  width="100%"
  caption="Add end device"
  zoomMode={true}
/>

2. To register the module, first click **Manually**. Then, configure the activation method by selecting **Over the Air Activation (OTAA)** and a compatible **LoRaWAN version**. Finally, click the **Start** button, as shown in **Figure 13** and **Figure 14**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/t_image_9.png"
  width="100%"
  caption="Manually register device to The Things Stack"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/t_image_10.png"
  width="100%"
  caption="Device activation configuration"
  zoomMode={true}
/>

3. Enter a unique **End Device ID** and the EUIs (**DevEUI** and **AppEUI**), as shown in **Figure 15**. Check if your module has a **DevEUI** on a sticker or a QR code that you can scan, and use this as the unique **DevEUI** for the device.

Optionally, add a descriptive **End device name** and **End device description** about your device.

4. After entering all the details, click **Network layer settings** to proceed to the next step.

:::tip NOTE

It is advisable to use a meaningful End device ID, End device name, and End device description that will match your device purpose. The End device ID `rak-device` is for illustration purposes only.

:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/t_image_11.png"
  width="100%"
  caption="OTAA Device Information"
  zoomMode={true}
/>

5. Configure the **Frequency plan**, compatible **Regional Parameter version**, and the supported **LoRaWAN class**. Then, click **Join settings** to continue.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/t_image_12.png"
  width="100%"
  caption="OTAA Configuration"
  zoomMode={true}
/>

6. To generate the **AppKey**, click the **Generate button**. Then, click **Add end device** to complete the device registration process.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/t_image_13.png"
  width="100%"
  caption="OTAA AppKey generation and device registration"
  zoomMode={true}
/>

You should now be able to see the device on The Things Stack console, as shown in **Figure 18**.

:::tip NOTE

- The **AppEUI**, **DevEUI**, and **AppKey** are required parameters to activate your LoRaWAN end device using OTAA. For security reasons, the **AppKey** is hidden by default but can be revealed by clicking the **Show** button. You can also quickly copy these parameters using the **Copy** button.

- The three OTAA parameters on The Things Stack device console are MSB by default.

- These parameters are always accessible on the device console page, as shown in **Figure 18**.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/t_image_14.png"
  width="100%"
  caption="OTAA device successfully registered to The Things Stack"
  zoomMode={true}
/>


#### RAK4270 OTAA Configuration for The Things Stack

The RAK4270 Breakout Board supports a series of AT commands to configure its internal parameters and control the functionalities of the module. To set up the RAK4270 board to join The Things Stack using OTAA, start by connecting the RAK4270 board to the Computer (see **Figure 1**) and open the RAK Serial Port Tool. Wait for the communication to start. It is recommended to test the serial communication and verify the current configuration by sending either of these two AT commands:

```
at+set_config=device:restart
```

```
at+version
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/3.command-response.png"
  width="90%"
  caption="AT Command response"
  zoomMode={true}
/>

As an example, these are the list of the parameters you need to configure in RAK4270:

- LoRa join mode: **OTAA**
- LoRa class: **Class A**
- LoRa region: **EU868**
- Device EUI: **1133557799224466**
- Application EUI: **1000000000000009**
- Application Key: **04FA4E626EF5CF227C969601176275C2**

1. Set the LoRa join mode to OTAA.

```
at+set_config=lora:join_mode:0
```

2. Set the LoRa class to Class A.

```
at+set_config=lora:class:0
```

3. Set the frequency/region to EU868.

* Refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4270-breakout-board/datasheet/#rf-characteristics" target="_blank">RAK4270 Breakout Board Datasheet</a> for the list of supported frequencies.


```
at+set_config=lora:region:EU868
```

4. Set the Device EUI.

```
at+set_config=lora:dev_eui:1133557799224466
```

5. Set the Application EUI.

:::tip NOTE
All zero value Application EUI `at+set_config=lora:app_eui:0000000000000000` is **not supported** and will return error.
:::

```
at+set_config=lora:app_eui:1000000000000009
```

6. Set the Application Key.

```
at+set_config=lora:app_key:04FA4E626EF5CF227C969601176275C2
```


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/14.lora-parameters.png"
  width="90%"
  caption="Configure LoRa Parameters"
  zoomMode={true}
/>

:::tip NOTE

After configuring, reset your RAK4270 Breakout Board to save the parameters.

:::

7. Join in OTAA mode.

```
at+join
```

After 5 or 6 seconds, if the request is successfully received by a LoRa gateway, then you should see the messages shown in **Figure 21**.

8. Try to send a message from the RAK4270 board.

```
at+send=lora:2:1234567890
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/15.send-message.png"
  width="90%"
  caption="OTAA Test Sample Data Sent via RAK Serial Port Tool"
  zoomMode={true}
/>

You can see the data sent by the RAK4270 board on The Things Stack platform, as shown in **Figure 22**.


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/otaasend.png"
  width="100%"
  caption="OTAA Test Sample Data Sent Viewed in The Things Stack"
  zoomMode={true}
/>


#### The Things Stack ABP Device Registration

1. To register an **ABP** device, open your application console and select the application to which you want to add the device. Then, click **+ Add end device**, as shown in **Figure 23**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/t_image_8.png"
  width="100%"
  caption="Add end device"
  zoomMode={true}
/>

2. To register the module, click **Manually**, then configure the activation method by selecting **Activation by personalization (ABP)**, compatible **LoRaWAN version**, and click **Start** button, as shown in **Figure 24** and **Figure 25**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/t_image_9.png"
  width="100%"
  caption="Add end device"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/image_1_abp.png"
  width="100%"
  caption="Manually register device to The Things Stack"
  zoomMode={true}
/>

3. Enter a unique **End Device ID** and **DevEUI**, as shown in **Figure 26**. Check if your module has a **DevEUI** on a sticker or a QR code that you can scan, and use this as the unique **DevEUI** for the device.

Optionally, add a descriptive **End device name** and **End device description** about your device.

4. After entering all the details, click **Network layer settings** to proceed to the next step.

:::tip NOTE

It is advisable to use a meaningful End device ID, End device name, and End device description that will match your device purpose. The End device ID `rak-device-abp` is for illustration purposes only.

:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/image_2_abp.png"
  width="100%"
  caption="Device Information"
  zoomMode={true}
/>

5. Configure the **Frequency plan**, compatible **Regional Parameter version**, and supported **LoRaWAN class**. For an **ABP** device, generate the **Device Address** and **NwkSKey** (Network Session Key). Then, click **Application layer settings** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/image_3_abp.png"
  width="100%"
  caption="ABP Configuration in The Things Stack"
  zoomMode={true}
/>

6. To generate the **AppSKey**, click the **Generate** button. Then, click **Add end device** to complete the device registration process.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/image_4_abp.png"
  width="100%"
  caption="ABP Configuration in The Things Stack"
  zoomMode={true}
/>

You should now be able to see the device on The Things Stack console, as shown in **Figure 29**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/image_5_abp.png"
  width="100%"
  caption="RAK4270 registered at The Things Stack"
  zoomMode={true}
/>

#### RAK4270 ABP Configuration for The Things Stack

To set up the RAK4270 Breakout Board to join The Things Stack using ABP, start by connecting the RAK4270 board to the Computer (see Figure 1) and open the RAK Serial Port  Tool. It is recommended to test the serial communication by sending either of these two AT commands:

```
at+set_config=device:restart
```

```
at+version
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/3.command-response.png"
  width="90%"
  caption="AT Command response"
  zoomMode={true}
/>

As an example, these are the list of the parameters you need to configure in RAK4270:

- LoRa join mode: **ABP**
- LoRa class: **Class A**
- LoRa region: **EU868**
- Device address: **260BDE80**
- Network Session Key: **433C7A924F7F6947778FE821525F183A**
- Application Session Key: **A585653A949C2B2D44B55E99E94CB533**

1. Set the LoRa join mode to ABP.

```
at+set_config=lora:join_mode:1
```
2. Set the LoRa class to Class A.

```
at+set_config=lora:class:0
```

3. Set the frequency/region to EU868.

- Refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4270-breakout-board/datasheet/#rf-characteristics" target="_blank">RAK4270 Breakout Board Datasheet</a> for the list of supported frequencies.

```
at+set_config=lora:region:EU868
```

4. Set the Device Address.

```
at+set_config=lora:dev_addr:260BDE80
```

5. Set the LoRa Network Session Key.

```
at+set_config=lora:nwks_key:433C7A924F7F6947778FE821525F183A
```

6. Set the LoRa Application Session Key.

```
at+set_config=lora:apps_key:A585653A949C2B2D44B55E99E94CB533
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/21.abp-at-commands.png"
  width="90%"
  caption="AT Command for ABP LoRa parameters via RAK Serial Port Tool"
  zoomMode={true}
/>

:::tip NOTE

After configuring all the parameters, reset the RAK4270 Breakout Board to save the configuration

:::

7. Join in ABP mode.

```
at+join
```

:::tip NOTE

In **ABP mode**, LoRaWAN does not require the device to join a network before sending a LoRaWAN packet. However, to maintain the consistency of the internal states of the RAK4270 board's firmware, the `at+join` command must still be sent. In this case, the firmware will respond almost immediately with **OK**.

:::

8. Try to send data from the RAK4270 to The Things Network in ABP mode.

```
at+send=lora:2:1234567890
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/15.send-message.png"
  width="90%"
  caption="ABP Test Sample Data Sent via RAK Serial Port Tool"
  zoomMode={true}
/>

You can see the data sent by the RAK4270 board on The Things Stack device console *Live data* section and the *Last seen* info should be few seconds ago.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/abpsend.png"
  width="100%"
  caption="OTAA Test Sample Data Sent Viewed in The Things Stack"
  zoomMode={true}
/>


### Connect with ChirpStack

**ChirpStack**, formerly known as the **LoRaServer** project, offers open-source components for creating LoRaWAN networks. Similar to **The Things Network (TTN)**, the **RAK4270 Breakout Module** operates at the periphery, transmitting data to backend servers via a LoRa gateway. For more information, visit the<a href="https://www.chirpstack.io/" target="_blank">official ChirpStack website</a>.


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/22.chirpstack-platform.png"
  width="60%"
  caption="RAK4270 Breakout Board in the Context of the ChirpStack Platform"
  zoomMode={true}
/>


:::tip NOTE
This document assumes that you are using a **RAK Gateway** with its built-in **ChirpStack** or the **RAK Cloud Testing ChirpStack**. Additionally, ensure that the RAK Gateway with ChirpStack is successfully configured. For detailed guidance, refer to the relevant **RAK documentation**.
:::

In this section, you need the following requirements:

  1. Ensure that the ChirpStack online gateway is operational and that the frequency band of the nodes matches the frequency band of the gateway in use.
  2.  The RAK Serial Port Tool provided by RAK
  3.  RAK4270 Breakout Board

:::tip NOTE
The frequency band used in the test is EU868, use the high-frequency version of the RAK4270 Breakout Board.
:::

Before starting, decide whether to use **OTAA** or **ABP** mode to register the device with the network server.


<b>Sign up and login</b>

Log in to the ChirpStack server using your username and password.

#### Create a New Application

1. Go to the Application section, as shown in **Figure 35**.


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/23.chirpstack.png"
  width="100%"
  caption="Application Section"
  zoomMode={true}
/>

2. For this setup, create a new Application by clicking on the “**CREATE**” button, and filling the required parameters, as shown in **Figure 36** and **Figure 37**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/24.new-application.png"
  width="100%"
  caption="Creating a New Application"
  zoomMode={true}
/>

* For this setup, create an Application named “**rak_node_test**”.

ChirpStack LoraServer supports multiple system configurations, with only one by default.

* The **Service Profile** field is used to select the system profile.
* The **Payload Codec** Specifies the parsing method for processing payload data, such as parsing **LPP format data**.


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/25.filling-parameters.png"
  width="100%"
  caption="Fill in Parameters of an Application"
  zoomMode={true}
/>

<b>Register a New Device</b>

3. Choose the **Application** created in the previous step, then select the **DEVICES** tab, as shown in **Figure 38** and **Figure 39**.

4. Once done, click **CREATE APPLICATION**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/26.application-available.png"
  width="100%"
  caption="List of Applications Created"
  zoomMode={true}
/>


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/27.application-page.png"
  width="100%"
  caption="Device Tab of an Application"
  zoomMode={true}
/>

5. Once inside of the **DEVICE** tab, create a new device (LoRa node) by clicking on the **+ CREATE** button.


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/28.adding-node.png"
  width="100%"
  caption="Add a New Device"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/29.new-device-registration.png"
  width="100%"
  caption="New Device Registration Form"
  zoomMode={true}
/>

6. After creating the node, fill in the required details. You can either generate a **Device EUI** automatically by clicking the icon or manually enter a valid **Device EUI** in the edit box.

Fill in the parameters requested:

* **Device name and Device description**: These are descriptive texts about your device.
* **Device EUI**: This interface lets you generate a **Device EUI** automatically by clicking the red-highlighted icon in **Figure 42**. Alternatively, you can manually enter a specific **Device EUI** directly into the form.
* **Device Profile**:
  * If you want to join in OTAA mode, select **DeviceProfile_OTAA**.
  * If you want to join in ABP mode, select **DeviceProfile_ABP**.


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/30.adding-parameters.png"
  width="100%"
  caption="Generate a New Device EUI"
  zoomMode={true}
/>

#### LoRaWAN Join Mode

In LoRaWAN, a node can connect to the network using one of two methods, collectively referred to as **Join Mode**. The two supported modes are **OTAA (Over the Air Activation)** and **ABP (Activation by Personalization)**. This section explains the configuration process for both modes, covering both the platform side and the node side.


##### OTAA Mode

###### Configure the OTAA Mode on the Platform

1. If **DeviceProfile_OTAA** is selected, as shown in **Figure 43**, an **Application Key** must be created for the device after it is successfully created.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/31.otaa.png"
  width="100%"
  caption="Chirpstack OTAA Activation"
  zoomMode={true}
/>

2. A previously created Application Key can be entered here, or a new one can be generated automatically by clicking the icon highlighted in red in **Figure 44**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/32.otaa-set-device-keys.png"
  width="100%"
  caption="Chirpstack OTAA Set Device Keys"
  zoomMode={true}
/>

3. Once the Application Key is added to the form, the process can be finalized by clicking on the **SET DEVICE-KEYS** button.

* The newly created device will appear in the **DEVICES** tab. Key parameters, such as the **Device EUI**, will be displayed in the summary.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/33.list-device.png"
  width="100%"
  caption="Chirpstack OTAA List of Device in the Device Tab"
  zoomMode={true}
/>

4. To end the process, it is a good practice to review that the Application Key is properly associated with this device. The Application Key can be verified in the **KEYS(OTAA)** tab, as shown in **Figure 46**.


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/34.application-key.png"
  width="100%"
  caption="Application Key Associated with the New Device"
  zoomMode={true}
/>


:::tip NOTE

Standard **OTAA mode** requires the **Device EUI**, **Application Key**, and the **Application EUI**. However, in ChirpStack’s implementation, only the **Device EUI** and **Application Key** are mandatory; the **Application EUI** is not required or recorded in the Application tab. Despite this, the **Application EUI** is a mandatory parameter in the RAK4270 Breakout Board firmware. To resolve this mismatch, you can reuse the **Device EUI** as the **Application EUI** when configuring the node.

:::

###### Configure the OTAA mode on the RAK4270 Breakout Board

The RAK4270 Breakout Board supports a series of <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4270-breakout-board/at-command-manual/" target="_blank">AT commands</a> to configure its internal parameters and control the functionalities of the module.

To set up the RAK4270 Breakout to join ChirpStack using OTAA, start by connecting the board to the computer (see **Figure 2**) and open the RAK Serial Port Tool. Wait for the communication to start. It is recommended to test the serial communication by sending either of these two AT commands:


```
at+get_config=lora:status
```

```
at+version
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/3.command-response.png"
  width="90%"
  caption="at+version command response"
  zoomMode={true}
/>

As an example, these are the list of the parameters you need to configure in the RAK4270 Breakout Board:

- LoRa join mode: **OTAA**
- LoRa class: **Class A**
- LoRa region: **EU868**
- Device EUI: **5e9d1e0857cf25f1**
- Application EUI: **5e9d1e0857cf25f1**
- Application Key: **f921d50cd7d02ee3c5e6142154f274b2**

1. Set the LoRa join mode to OTAA.

```
at+set_config=lora:join_mode:0
```

2. Set the LoRa class to Class A.

```
at+set_config=lora:class:0
```

3. Set the frequency/region to EU868.

- Refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4270-breakout-board/datasheet/#rf-characteristics" target="_blank">RAK4270 Breakout Board Datasheet</a> for the list of supported frequencies.


```
at+set_config=lora:region:EU868
```

4. Set the Device EUI.

```
at+set_config=lora:dev_eui:5e9d1e0857cf25f1
```

5. Set the Application EUI.

```
at+set_config=lora:app_eui:5e9d1e0857cf25f1
```

:::tip NOTE

The App EUI parameter is not needed for the ChirpStack platform; therefore, you will use the same ID as the Device EUI. Otherwise, the firmware will fail to connect to the network server.


:::

6. Set the Application Key.

- Get the Application Key from the TTN register.


```
at+set_config=lora:app_key:f921d50cd7d02ee3c5e6142154f274b2
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/36.configure-lora-parameters.png"
  width="45%"
  caption="Chirpstack OTAA configuration via RAK Serial Port Tool"
  zoomMode={true}
/>


:::tip NOTE
After configuring all the parameters, reset your RAK4270 Breakout Board to save the parameters.
:::

7. Join the Network.

```
at+join
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/37.otaa-join-chirpstack.png"
  width="45%"
  caption="Chirpstack OTAA Join the Network via RAK Serial Port Tool"
  zoomMode={true}
/>

8. You will see the JoinRequest and JoinAccept on the ChirpStack page.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/38.chirpstack-console.png"
  width="100%"
  caption="Check LoRaWAN Joint Request in Chirpstack OTAA Console"
  zoomMode={true}
/>

9. Try to send data from the RAK4270 Breakout Board to ChirpStack.

```
at+send=lora:2:1234567890
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/39.send-message-chirpstack.png"
  width="45%"
  caption="Send a LoRaWAN Message via RAK Serial Port Tool"
  zoomMode={true}
/>

On the ChirpStack platform, you can view messages in the **LORAWAN FRAMES** tab, as shown in **Figure 52**. By convention:

- Messages sent from nodes to gateways are referred to as **Uplinks**.
- Messages sent from gateways to nodes are referred to as **Downlinks**.


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/40.message-received.png"
  width="100%"
  caption="Chirpstack Data Received Preview"
  zoomMode={true}
/>

This concludes the exercise to send data in the OTAA mode.


##### ABP Mode

###### Configure the ABP Mode on the Platform

When registering a new device, if you select **DeviceProfile_ABP**, as shown in **Figure 53**, the ChirpStack platform will assume that the device will connect to the LoRaWAN network using **ABP mode**.

:::tip NOTE

Enable the **Disable frame counting verification** option. During testing, restarting the module resets the frame counter to zero, which can cause a synchronization issue with the ChirpStack server, interpreting it as a replay attack. Disabling this feature is safe for testing purposes, but ensure it is reactivated in a production environment.

:::


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/41.configuring-device-abp.png"
  width="100%"
  caption="ChirpStack Console, Configuring a Device"
  zoomMode={true}
/>

After selecting the ABP mode, the following parameters appear in the Activation tab:

* **Device address**
* **Network Session Key**
* **Application Session Key**

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/42.abp-activation-parameters.png"
  width="100%"
  caption="Chirpstack ABP Activation Parameters Needed"
  zoomMode={true}
/>

* The parameters can be either randomly generated by the platform or manually set with user-defined values. Once all parameters are correctly filled in, complete the process by clicking the **ACTIVATE DEVICE** button.

###### Configure the ABP Mode on the RAK4270 Breakout Board

In the following steps, you will configure the RAK4270 Breakout Board to work in the ABP mode. To set up the RAK4270 Breakout Board to join ChirpStack using ABP, start by connecting the board to the computer (see **Figure 2**) and open the RAK Serial Port Tool. Wait for the communication to start. It is recommended to test the serial communication by sending either of these two AT commands:

```
at+get_config=lora:status
```

```
at+version
```


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/3.command-response.png"
  width="90%"
  caption="at+version command response"
  zoomMode={true}
/>

As an example, these are the list of the parameters you need to configure in the RAK4270 Breakout Board:

- LoRa join mode: **ABP**
- LoRa class: **Class A**
- LoRa region: **EU868**
- Device address: **26011af9**
- Network Session Key: **c280cb8d1df688bc18601a97025c5488**
- Application Session Key: **4d42ec5caf97f03d833cdaf5003f69e1**

1. Set LoRa join mode to ABP.

```
at+set_config=lora:join_mode:1
```

2. Set LoRa class to Class A.

```
at+set_config=lora:class:0
```

3. Set the frequency/region to EU868.

- Refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4270-breakout-board/datasheet/#rf-characteristics" target="_blank">RAK4270 Breakout Board Datasheet</a> for the list of supported frequencies.

```
at+set_config=lora:region:EU868
```

4. Set the Device Address.

```
at+set_config=lora:dev_addr:26011af9
```

5. Set the Network Session Key.

```
at+set_config=lora:nwks_key:c280cb8d1df688bc18601a97025c5488
```

6. Set the Application Session Key.

```
at+set_config=lora:apps_key:4d42ec5caf97f03d833cdaf5003f69e1
```


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/44.configure-abp-parameters.png"
  width="45%"
  caption="Chirpstack ABP Parameters Configuration via RAK Serial Port Tool"
  zoomMode={true}
/>

:::tip NOTE

After configuring all the parameters, reset your RAK4270 Breakout Board to save the parameters.

:::

7. Join in ABP mode.

```
at+join
```

:::tip NOTE

In **ABP mode**, the LoRaWAN protocol does not require the device to join a network before sending a LoRaWAN packet. However, to maintain the consistency of the internal states in the RAK4270 Breakout Board firmware, the `at+join` command must still be sent. The firmware will respond almost immediately with **OK**.

:::

8. Try to send data from the RAK4270 Breakout Board to ChirpStack.

```
at+send=lora:2:1234567890
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/45.data-sent-abp.png"
  width="45%"
  caption="Chirpstack Sample Data Sent via RAK Serial Port Tool"
  zoomMode={true}
/>

### LoRa P2P Mode

This section explains how to set up and connect two RAK4270 Breakout Board units to operate in **LoRa P2P mode** using **EU868** as the frequency. The steps are also applicable to other standard frequency bands. To begin this process, ensure you have the following requirements:

1. Both RAK4270 Breakout Board units must be configured to operate on the **EU868** frequency.

2. The setup of the RAK4270 Breakout Board units involves connecting them to a general-purpose computer via the UART port. Each board can be configured separately, but testing the **LoRa P2P mode** requires both units to be connected simultaneously to their respective UART ports. This setup can be achieved using:

- One computer with two available USB ports, or
- Two computers, each with one available USB port.

3. Set the RAK4270 Breakout Board to work in LoRa P2P mode. Open the RAK Serial Port Tool and send the following command:

```
at+set_config=lora:work_mode:1
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/46.lora-p2p.png"
  width="45%"
  caption="P2P Initialization"
  zoomMode={true}
/>

4. Configure LoRa P2P parameters for both of them.


```
at+set_config=lorap2p:XXX:Y:Z:A:B:C
```

For this example, the LoRa parameters are the following:

- Link frequency: **869525000&nbsp;Hz**
- Spreading factor: **7**
- Bandwidth: **125&nbsp;kHz**
- Coding Rate: **4/5**
- Preamble Length: **5**
- Power: **5&nbsp;dBm**

:::tip NOTE

Refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4270-breakout-board/at-command-manual/" target="_blank">Configuring Using AT Commands</a> section to learn more about the definition of the parameters used.

:::

Hence, it is translated into the following RAK4270 Breakout Board AT command and sent to both units.

```
at+set_config=lorap2p:869525000:7:0:1:5:5
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/48.configuring-p2p.png"
  width="45%"
  caption="Configure P2P in both RAK4270 Breakout Board"
  zoomMode={true}
/>

5. Set the transmission mode of the module. Unit 1 is configured as the sender, and Unit 2 is set to the receiver by AT command.

```
at+set_config=lorap2p:transfer_mode:2
```

```
at+set_config=lorap2p:transfer_mode:1
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/49.mode-setting.png"
  width="80%"
  caption="Set Modes in both RAK4270 Breakout Board"
  zoomMode={true}
/>

6. Try to send a message from Unit 1 to Unit 2.

```
at+send=lorap2p:1234567890
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/50.sending-message.png"
  width="80%"
  caption="Message sent and received status in the two modules"
  zoomMode={true}
/>


## Miscellaneous

### Upgrade the Firmware

Before you start working with the RAK4270 Breakout Board, it is recommended to keep the board updated to the latest version of the firmware. Download the latest <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4270-breakout-board/datasheet/#software" target="_blank">RAK4270 firmware</a>.

:::tip NOTE

For RAK4270 modules with firmware version **V3.0.0.12** or below, use the <a href="https://www.st.com/en/development-tools/stm32cubeprog.html" target="_blank">STM32CubeProgrammer</a> to upgrade the firmware. Upload the **.hex file** (not the .bin file) of the <a href="https://downloads.rakwireless.com/#LoRa/RAK4270/Firmware/" target="_blank">latest RAK4270 firmware</a>. Older firmware versions have a different bootloader code and are incompatible with the **RAK DFU Tool**.

:::

In the following sections, two (2) options for flashing new firmware in the RAK4270 Breakout Module are shown: **Upgrade through DAPLink** and **Upgrade through UART1**.

#### Firmware Upgrade Through DAPLink

Refer to the <a href="https://docs.rakwireless.com/product-categories/accessories/rakdap1/overview/" target="_blank">RAKDAP1 Flash and Debug Tool</a> guide in the Accessories Category.

#### Firmware Upgrade Through UART1

##### Minimum Hardware and Software Requirements

Refer to the table for the minimum hardware and software required to perform the firmware upgrade using J-Link.

| Hardware/Software | Requirement                                   |
| ----------------- | --------------------------------------------- |
| Computer          | A Windows/Ubuntu/Mac computer                 |
| Firmware File     | Bin firmware file downloaded from the website |
| Others            | A USB to TTL module                           |


##### Firmware Upgrade Procedure

Execute the following procedure to upgrade the firmware in Device Firmware Upgrade (DFU) mode through the UART1 interface.

1.  Download the latest application firmware of the RAK4270 Breakout Board.

    - <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4270-breakout-board/datasheet#software" target="_blank">RAK4270 Firmware</a>

2.  Download the RAK Device Firmware Upgrade (DFU) tool.
    - <a href="https://downloads.rakwireless.com/#LoRa/Tools/RAK_Device_Firmware_Upgrade_tool/" target="_blank">RAK Device Firmware Upgrade (DFU) Tool</a>

3.  Connect the RAK4270 Breakout Board with a computer through a USB to TTL.

4.  Open the Device Firmware Upgrade tool. Select the serial port and baud rate of the module and click the **Select Port** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/56.device-firmware.png"
  width="80%"
  caption="Device Firmware Upgrade Tool"
  zoomMode={true}
/>

5.  Select the application firmware file of the module with the suffix `.bin`.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/57.select-firmware.png"
  width="80%"
  caption="Select Firmware"
  zoomMode={true}
/>

6.  Click the **Upgrade** button to upgrade the device. After the upgrade is complete, the RAK4270 Breakout Board will be ready to work with the new firmware.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/58.firmware-upgrading.png"
  width="80%"
  caption="Firmware Upgrading"
  zoomMode={true}
/>


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4270-breakout-board/quickstart/59.upgrade-success.png"
  width="80%"
  caption="Upgrade Successful"
  zoomMode={true}
/>

<RkBottomNav/>