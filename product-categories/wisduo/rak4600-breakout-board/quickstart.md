---
title: RAK4600 WisDuo Breakout Board Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK4600 Breakout Board. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: "https://images.docs.rakwireless.com/wisduo/rak4600-breakout-board/rak4600-breakout.png"
keywords:
    - RAK4600 Breakout Board
    - wisduo
    - quickstart
sidebar_label: Quick Start Guide
slug: /product-categories/wisduo/rak4600-breakout-board/quickstart/
download: true
---

# RAK4600 Breakout Board Quick Start Guide

## Prerequisites

Before going through the steps in the installation guide of the RAK4600 Breakout Board, make sure to prepare the necessary items listed below:

### Hardware Tools

- <a href="https://store.rakwireless.com/products/rak4600-breakout-board?utm_source=RAK4600LPWANBreakoutModule&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">**RAK4600 Breakout Board**</a> (provided) – including **LoRa and BLE antenna**, **Dupont lines (9x)**, and **4-pin headers (2x)**
- Micro USB Cable (provided)
- LoRa Gateway in range, for testing (not provided)
- Windows PC (not provided)
- USB to UART adapter (not provided)
- <a href="https://store.rakwireless.com/products/daplink-tool?utm_source=RAKDAP1&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAKDAP1 Flash and Debug Tool</a> (not provided)

#### Software Tools

- <a href="https://downloads.rakwireless.com/#LoRa/Tools/" target="_blank">RAK Serial Port Tool</a>
- <a href="https://downloads.rakwireless.com/#LoRa/Tools/" target="_blank">CH340 Drivers</a>
- <a href="https://www.thethingsnetwork.org/get-started" target="_blank">The Things Network</a> account

#### Definition of Terms

##### List of acronyms

| ABP | Activation-By-Personalization |
| --- | --- |
| BLE | Bluetooth Low Energy |
| DFU | Device Firmware Upgrade |
| EUI | Extender Unique Identifier |
| LoRa | Long Range |
| OTAA | Over-The-Air-Activation |
| TTN | The Things Network |
| P2P | Peer to peer communication |
| SWD | Serial Wire Debug |
| RUI | RAKwireless Unified Interface |

## Product Configuration

### Interface with RAK4600 Breakout Board

To interface with the RAK4600 Breakout Board with your Windows PC, it is recommended to download and install the <a href="https://downloads.rakwireless.com/#LoRa/Tools/" target="_blank">**RAK Serial Port Tool**</a>.

:::warning
Before powering the RAK4600 Breakout Module, ensure that the included LoRa and BLE antennas are installed. Failure to do so may damage the board.
:::

Refer to **Figure 1** to connect the antennas.

> **Image:** RAK4600 Breakout Board antenna connection

Refer to **Figure 2** and **Figure 3** to identify the antennas.

> **Image:** RAK4600 Breakout Board BLE antenna

> **Image:** RAK4600 Breakout Board LoRa antenna

#### USB to UART

- Connect the USB-to-UART adapter to the pin header on the RAK4600 Breakout Board using a set of four Dupont lines. Refer to **Figure 4** for proper wiring.

> **Image:** Power up and interface with the board

- Open the RAK Serial Port Tool, select the COM port number noted in the previous step, and set the baud rate to **115200**. Click **OPEN** to connect to the board and begin sending commands.

> **Image:** Configure the RAK Serial Port Tool

#### BLE Interface

To configure the RAK4600 through BLE, execute the following steps.

1. Install the **nRF Connect** or **nRF Master Control Panel (BLE)** app provided by Nordic Semiconductor.
2. Open the app on the mobile device and scan for BLE devices.
3. Reset the RAK4600 board. After a few seconds, a list of BLE devices will be shown. The RAK4600 is listed as **RUI-XX: XX: XX**.

> **Image:** Nordic app scan for BLE devices

:::tip NOTE
Connect within 60 seconds after resetting the RAK4600. After that time, the BLE broadcast will be stopped.
:::

4. After pressing the **CONNECT** button, a list will be displayed, as shown in **Figure 7**.

> **Image:** Options to connect to the RAK4600

5. Select the service named **Nordic UART Service**.
6. To receive data from mobile, enable notification on TX Characteristic by clicking on the arrow.

> **Image:** Enable notifications from mobile phone

7. Write a value on RX Characteristic by clicking on the arrow.

> **Image:** Send AT command

8. A small input window will appear, where AT commands can be entered.

> **Image:** nRF app AT command input window

9. Send AT commands to RAK4600 in this dialog.

    * For example, to check the current firmware version, type `at+version` then click on the **SEND** button.

> **Image:** nRF app, send at command over BLE

The console output shall be read on the TX Characteristic of the App.

> **Image:** AT response over BLE

### Connecting to The Things Stack (TTN V3)

This section will show how to connect the RAK4600 Breakout Board to The Things Stack (TTN V3) platform.

> **Image:** The Things Stack diagram

As shown in **Figure 13**, The Things Stack is an open-source LoRaWAN Network Server suitable for global, geo-distributed public and private deployments as well as for small, local networks. The architecture follows the LoRaWAN Network Reference Model for standards compliancy and interoperability. This project is actively maintained by <a href="https://www.thethingsindustries.com/" target="_blank">The Things Industries</a>.

LoRaWAN is a protocol for low-power wide-area networks. It allows for large-scale Internet of Things deployments where low-powered devices efficiently communicate with Internet-connected applications over long-range wireless connections.

The RAK4600 board can function as a device within this ecosystem. This section demonstrates how simple it is to send data to The Things Stack using the LoRaWAN protocol. To accomplish this, the RAK4600 must be within the coverage area of a LoRaWAN gateway connected to The Things Stack server.

#### Registration to TTN and Creating LoRaWAN Applications

Before starting, visit the<a href="https://console.cloud.thethings.network/" target="_blank">The Things Network platform</a> and select a cluster, as shown in **Figure 14**. The Things Industries periodically adds new clusters, so choose the one closest to your location. In this guide, the Europe 1 cluster is selected.

> **Image:** Select Cluster in TTN V3

Use the same login credentials as on TTN V2, if applicable. If you do not have an account, create one.

1. To register as a new user to TTN, click on **Login with The Things ID**, then select **register** on the next page, as shown in **Figure 6** and **Figure 7**. Fill in all the necessary details and activate.

> **Image:** Log in using TTN account

> **Image:** Registration of new account

2. Log in on the platform using your username/email and password then click **Submit**, as shown in **Figure 17**.

> **Image:** Log in to TTN platform

4. Click **Authorize** to proceed.

> **Image:** Authorization to TTN

4. Click **Create an application**.

> **Image:** Create TTN application for your LoRaWAN devices

5. To register an application, first enter the required details and information about your application, then click **Create application**.

> **Image:** Details of the TTN application

The next step is to add end-devices to your The Things Stack application. LoRaWAN specification enforces that each end device has to be personalized and activated. Activation can be done either via Over-The-Air-Activation (OTAA) or Activation-By-Personalization (ABP).

:::tip NOTE

- Ensure that you are within the coverage of a LoRaWAN gateway registered with **The Things Stack (TTN V3)**. Without coverage from such a gateway, you will not be able to activate any device registered in your application.

- If no LoRaWAN gateway coverage is available in your location, RAKwireless offers <a href="https://store.rakwireless.com/collections/wisgate" target="_blank">LoRaWAN gateways</a> that can be connected to **The Things Stack (TTN V3)**.

:::

#### The Things Stack OTAA Device Registration

1. Go to your application console to register a device. To start adding an OTAA end-device, click **+ Add end device**, as shown in **Figure 21**.

> **Image:** Add end device

2. To register the module, start by clicking **Manually**, as shown in **Figure 22**.

> **Image:** Manually register device to The Things Stack

3. Configure the activation method by selecting **Over the air activation (OTAA)** and compatible **LoRaWAN version**. Afterwards, click on the **Start** button, as shown in **Figure 23**.

> **Image:** Device activation configuration

4. Enter a unique **End Device ID** and the EUIs (**DevEUI** and **AppEUI**), as shown in **Figure 15**. Check if your module has a **DevEUI** on a sticker or a QR code that you can scan, and use this as the unique **DevEUI** for the device.

:::tip NOTE
Optionally, add a more descriptive **End device name** and **End device description** about your device.
:::

5. After entering all the details, click **Network layer settings** to proceed to the next step.

:::tip NOTE

It is advisable to use a meaningful **End device ID**, **End device name**, and **End device description** that will match your device purpose. The End device ID `rak-device` is for illustration purposes only.

:::

> **Image:** OTAA Device Information

6. Configure the **Frequency plan**, compatible **Regional Parameter version**, and the supported **LoRaWAN class**. Then, click **Join settings** to continue.

> **Image:** OTAA Configuration

7. To generate the **AppKey**, click the **Generate button**. Then, click **Add end device** to complete the device registration process.

> **Image:** OTAA AppKey generation and device registration

You should now be able to see the device on The Things Stack console, as shown in **Figure 27**.

:::tip NOTE

- The **AppEUI**, **DevEUI**, and **AppKey** are required parameters to activate your LoRaWAN end device using OTAA. For security reasons, the **AppKey** is hidden by default but can be revealed by clicking the **Show** button. You can also quickly copy these parameters using the **Copy** button.

- The three OTAA parameters on The Things Stack device console are MSB by default.

- These parameters are always accessible on the device console page, as shown in **Figure 27**.
:::

> **Image:** OTAA device successfully registered to The Things Stack

#### RAK4600 OTAA Configuration for The Things Stack

The RAK4600 Breakout Board supports a series of AT commands to configure its internal parameters and control the functionalities of the module. To set up the RAK4600 board to join The Things Stack using OTAA, start by connecting the RAK4600 board to the computer (see **Figure 1**), open the RAK Serial Port Tool, and then wait for the communication to start. It is recommended to test the serial communication and verify the current configuration by sending either of these two AT commands:

```
at+set_config=device:restart
```

```
at+version
```

> **Image:** AT Command response

As an example, these are the list of the parameters you need to configure in RAK4600:

- LoRa join mode: **OTAA**
- LoRa class: **Class A**
- LoRa region: **EU868**
- Device EUI: **1133557799224466**
- Application EUI: **1000000000000009**
- Application Key: **04FA4E626EF5CF227C969601176275C2**

1. Set the LoRa join mode to **OTAA**.

```
at+set_config=lora:join_mode:0
```

2. Set the LoRa class to **Class A**.

```
at+set_config=lora:class:0
```

3. Set the frequency/region to **EU868**.

* Refer in the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4600-module/datasheet/#rf-characteristics" target="_blank">RAK4600 Datasheet</a> for the list of supported frequencies.

```
at+set_config=lora:region:EU868
```

4. Set the Device **EUI**.

```
at+set_config=lora:dev_eui:1133557799224466
```

5. Set the **Application EUI**.

:::tip NOTE
All zero value Application EUI `at+set_config=lora:app_eui:0000000000000000` is **not supported** and will return error.
:::

```
at+set_config=lora:app_eui:1000000000000009
```

6. Set the **Application Key**.

```
at+set_config=lora:app_key:04FA4E626EF5CF227C969601176275C2
```

> **Image:** Configure LoRa Parameters

:::tip NOTE

After configuring all the parameters, reset your RAK4600 Module to save parameters.

:::

7. Join in OTAA mode.

```
at+join
```

After 5 or 6 seconds, if the request was successfully received by a LoRa gateway, then you should see the messages shown in **Figure 30**.

8. Try to send a message from the RAK4600 board.

```
at+send=lora:2:1234567890
```

> **Image:** OTAA Test Sample Data Sent via RAK Serial Port Tool

You can see the data sent from the RAK4600 board on The Things Stack platform, as shown in **Figure 31**.

> **Image:** OTAA Test Sample Data Sent Viewed in The Things Stack

#### The Things Stack ABP Device Registration

1. To register an **ABP** device, open your application console and select the application to which you want to add the device. Then, click **+ Add end device**, as shown in **Figure 32**.

> **Image:** Add end device

2. To register the module, start by clicking **Manually**.

> **Image:** Add end device

3. Configure the activation method by selecting **Activation by personalization (ABP)** and compatible **LoRaWAN version**. Afterwards, click on the **Start** button, as shown **Figure 34**.

> **Image:** Manually register device to The Things Stack

4. Enter a unique **End Device ID** and **DevEUI**, as shown in **Figure 35**. Check if your module has a **DevEUI** on a sticker or a QR code that you can scan, and use this as the unique **DevEUI** for the device.

:::tip NOTE
Optionally, add a descriptive **End device name** and **End device description** about your device.
:::

5. After entering all the details, click **Network layer settings** to proceed to the next step.

:::tip NOTE

It is advisable to use a meaningful **End device ID**, **End device name**, and **End device description** that will match your device purpose. The End device ID `rak-device-abp` is for illustration purposes only.

:::

> **Image:** Device Information

6. Configure the **Frequency plan**, compatible **Regional Parameter version**, and supported **LoRaWAN class**. For an **ABP** device, generate the **Device Address** and **NwkSKey** (Network Session Key). Then, click **Application layer settings** to proceed.

> **Image:** ABP Configuration in The Things Stack

7. To generate the **AppSKey**, click the **Generate** button. Then, click **Add end device** to complete the device registration process.

> **Image:** ABP Configuration in The Things Stack

8. You should now be able to see the device on The Things Stack console, as shown in **Figure 38**.

> **Image:** RAK4600 registered at The Things Stack

#### RAK4600 ABP Configuration for The Things Stack

To set up the RAK4600 Breakout Board to join The Things Stack using ABP, start by connecting the RAK4600 board to the computer (see **Figure 1**) and open the RAK Serial Port Tool. It is recommended to test the serial communication by sending either of these two AT commands:

```
at+set_config=device:restart
```

```
at+version
```

> **Image:** AT Command response

As an example, these are the list of the parameters you need to configure in RAK4600:

- LoRa join mode: **ABP**
- LoRa class: **Class A**
- LoRa region: **EU868**
- Device address: **260BDE80**
- Network Session Key: **433C7A924F7F6947778FE821525F183A**
- Application Session Key: **A585653A949C2B2D44B55E99E94CB533**

1. Set the LoRa join mode to **ABP**.

```
at+set_config=lora:join_mode:1
```
2. Set the LoRa class to **Class A**.

```
at+set_config=lora:class:0
```

3. Set the frequency/region to **EU868**.

- Refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4600-breakout-board/datasheet/#rf-characteristics" target="_blank">RAK4600 Breakout Board Datasheet</a> for the list of supported frequencies.

```
at+set_config=lora:region:EU868
```

4. Set the **Device Address**.

```
at+set_config=lora:dev_addr:260BDE80
```

5. Set the **LoRa Network Session Key**.

```
at+set_config=lora:nwks_key:433C7A924F7F6947778FE821525F183A
```

6. Set the **LoRa Application Session Key**.

```
at+set_config=lora:apps_key:A585653A949C2B2D44B55E99E94CB533
```

> **Image:** AT Command for ABP LoRa parameters via RAK Serial Port Tool

:::tip NOTE

After configuring all the parameters, reset the RAK4600 Module to save the parameters.

:::

7. Join in ABP mode.

```
at+join
```

:::tip NOTE

In **ABP mode**, LoRaWAN does not require the device to join a network before sending a LoRaWAN packet. However, to maintain the consistency of the internal states of the RAK4270 board's firmware, the `at+join` command must still be sent. In this case, the firmware will respond almost immediately with **OK**.

:::

8. Try to send data from the RAK4600 to The Things Network in ABP mode.

```
at+send=lora:2:1234567890
```

> **Image:** ABP Test Sample Data Sent via RAK Serial Port Tool

You can see the data sent by the RAK4600 board on The Things Stack device console *Live data* section and the *Last seen* info should be a few seconds ago.

> **Image:** OTAA Test Sample Data Sent Viewed in The Things Stack

### Connecting with ChirpStack

This section shows how to connect the RAK4600 Breakout Board to the ChirpStack platform. As described in the ChirpStack website:

“ChirpStack provides open-source components for LoRaWAN networks. Together they form a ready-to-use solution including a user-friendly web interface for device management and APIs for integration. The modular architecture makes it possible to integrate within existing infrastructures. All components are licensed under the MIT license and can be used for commercial purposes.”

> **Image:** RAK4600 Breakout Board in the context of the ChirpStack platform

The architecture of the ChirpStack platform is shown in **Figure 43**. Similar to the case of TTN, the RAK4600 Breakout Board is located in the periphery and will transmit the data to the backend servers through a LoRa gateway. For a more technical understanding of the ChirpStack components, refer to its <a href="https://www.chirpstack.io/project/architecture/" target="_blank">Architecture</a> page.

* This document assumes that you are using a **RAK Gateway** with its built-in **ChirpStack** or the **RAK Cloud Testing ChirpStack**. Additionally, ensure that the RAK Gateway with ChirpStack is successfully configured. For detailed guidance, refer to the relevant **RAK documentation**.

:::tip NOTE
The frequency band used in this example is EU868 which is supported by the high-frequency version of the RAK4600 Breakout Board.
:::

* These are the steps needed to send data to the ChirpStack platform from a RAK4600 Breakout Board:

  1. Create a new Application
  2. Register a new device on the platform:
  3. Configure the Join Mode:
      * OTAA mode on the platform
      * OTAA mode on the RAK4600
      * ABP mode on the platform
      * ABP mode on the RAK4600 Breakout Board
  4. Send data from the RAK4600 Breakout Board and receive it at the platform

The following section provides details for each of the aforementioned steps. Before starting, decide whether to use ABP or OTAA mode to register the device with the network server.

#### Create a new Application

1. Go to the Application section, then click on the **+ CREATE** button.

> **Image:** Application Section

2. For this setup, create a new Application by clicking on the **CREATE APPLICATION** button.

> **Image:** Create a New Application

3. Create an Application named **rak_node_test**. Fill in the required parameters, as shown in **Figure 46**. To finish, click on the **CREATE APPLICATION** button.

* **Application Name**: rak_node_test
* **Application Description**: test
* **Service profile**: field is to select the system profile.

The **Application Description** field is just a descriptive text.

> **Image:** Fill in Parameters of an Application

**Register a new Device**

4. Click on the Application **rak_node_test** created in the previous step.

> **Image:** List of Applications Created

5. Select the **DEVICES** tab, as shown in **Figure 48**.

> **Image:** Devices Tab of an Application

6. Inside of the **DEVICES** tab, create a new device (LoRa node) by clicking on the **+ CREATE** button.

> **Image:** Add a New Device

> **Image:** New Device Registration Form

7. Generate a Device EUI automatically by clicking the icon highlighted in **Figure 51**. Or, you can write a correct Device EUI in the edit box.

Fill in the parameters requested:

* **Device name** and **Device description**: These are just descriptive texts.
* **Device EUI**: This interface allows you to generate a Device EUI automatically by clicking the icon highlighted in red in **Figure 51**. You can also add a specific Device EUI directly in the form.
* **Device-profile**: To join in OTAA mode, select **device_profile_otaa** or **device_profile_abp** to join in ABP mode.

8. To finish, click on the **CREATE DEVICE** button.

:::tip NOTE
ChirpStack doesn’t support AS923 in ABP mode.
:::

> **Image:** Generate a new Device EUI in the device registration form

#### LoRaWAN Join Mode

In LoRaWAN, a node can connect to the network using one of two methods, collectively referred to as **Join Mode**. The two supported modes are **OTAA (Over the Air Activation)** and **ABP (Activation by Personalization)**. This section explains the configuration process for both modes, covering both the platform side and the node side.

##### OTAA Mode

###### Configure the OTAA Mode on the Platform

1. If **DeviceProfile_OTAA** is selected, an **Application Key** must be created for the device after it is successfully created.

> **Image:** Chirpstack OTAA Activation

2. A previously created Application key can be entered here, or a new one can be generated automatically by clicking on the icon highlighted in red in **Figure 53**.

> **Image:** Chirpstack OTAA Set Device Keys

3. Once the **Application key** is added in the form, the process can be finalized by clicking on the **SET DEVICE-KEYS** button.

* As shown in **Figure 54**, a new device should be listed in the **DEVICES** tab. The most important parameters, such as the **Device EUI**, are shown in the summary.

> **Image:** Chirpstack OTAA List of Device in the Device Tab

4. To end the process, it is a good practice to review that the **Application key** is properly associated with this device. The **Application key** can be verified in the **KEYS(OTAA)** tab.

> **Image:** Application Key associated to the new device

:::tip NOTE
Standard **OTAA mode** requires the **Device EUI**, **Application Key**, and the **Application EUI**. However, in ChirpStack’s implementation, only the **Device EUI** and **Application Key** are mandatory; the **Application EUI** is not required or recorded in the Application tab. Despite this, the **Application EUI** is a mandatory parameter in the RAK4270 Breakout Board firmware. To resolve this mismatch, you can reuse the **Device EUI** as the **Application EUI** when configuring the node.
:::

###### Configure the OTAA Mode on the RAK4600 Breakout Board

RAK4600 Breakout Board complies with the LoRaWAN 1.0.2 specification. By default, the LoRa join mode is **OTAA** and the LoRa Class is **Class A**.

To set up the RAK4600 Breakout Board to join ChirpStack using OTAA, start by connecting the breakout board to the Windows PC, as shown in section [Interfacing with RAK4600 Breakout Board](#interface-with-rak4600-breakout-board), open the RAK Serial Port Tool, and then wait for the communication to start. It is recommended to test the serial communication by sending either of these two AT commands:

```
at+get_config=lora:status
```

```
at+version
```

> **Image:** at+version command response

As an example, the following parameters will be configured in the RAK4600 Breakout Board:

- LoRa join mode: **OTAA**
- LoRa class: **Class A**
- LoRa region: **EU868**
- Device EUI: **d045f054b2797f7c** (from ChirpStack registration)
- Application EUI: **d045f054b2797f7c** (from ChirpStack registration)
- Application Key: **2cb29aefe344c0d7b044e7a7d3afda6d** (from ChirpStack registration)

1. Set the LoRa join mode to **OTAA**.

```
at+set_config=lora:join_mode:0
```

2.  Set the LoRa Class to **Class A**.

```
at+set_config=lora:class:0
```
3.  Set the frequency/region to **EU868** (for Europe).

Refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4600-breakout-board/datasheet/#rf-characteristics" target="_blank">Datasheet</a> for the list of supported frequencies.

```
at+set_config=lora:region:EU868
```

:::tip NOTE
Remember that the device frequency shall be in the same frequency band as the gateway.
:::

4.  Set the Device **EUI**.

```
at+set_config=lora:dev_eui:d045f054b2797f7c
```

5. Set the **Application EUI**.

```
at+set_config=lora:app_eui:d045f054b2797f7c
```
:::tip NOTE
The App EUI parameter is not needed for the ChirpStack platform; therefore, use the same ID as the Device EUI. Otherwise, the firmware will fail to connect to the network server.
:::

6.  Set the **Application Key**.

```
at+set_config=lora:app_key:2cb29aefe344c0d7b044e7a7d3afda6d
```

> **Image:** Chirpstack OTAA configuration via RAK Serial Port Tool

:::tip NOTE
After configuring all the parameters, reset your RAK4600 Breakout Board to save the parameters.
:::

7. Join the network.

```
at+join
```

8. After 5 or 6 seconds, if the request is successfully received by a LoRa gateway, then the **OK Join Success** message will be shown.

> **Image:** Chirpstack OTAA Join the Network via RAK Serial Port Tool

9. The **JoinRequest** and **JoinAccept** messages are also displayed on the ChirpStack platform, specifically in the **LORAWAN FRAMES** tab.

> **Image:** Check LoRaWAN Joint Request in Chirpstack OTAA Console

9.  Try to send data from the RAK4600 Breakout Board to ChirpStack.

```
at+send=lora:2:1234567890
```

> **Image:** Send a LoRaWAN Message via RAK Serial Port Tool

- On the ChirpStack console, the messages shall appear in the **LORAWAN FRAMES** tab, as shown in **Figure 61**. By convention, messages sent from nodes to the gateway are considered as **UPLINK**, while messages sent by the gateway to nodes are considered as a **DOWNLINK**.

> **Image:** Chirpstack Data Received Preview

##### ABP Mode

###### Configure the ABP Mode on the Platform

During the registration of a new device, if **device_profile_abp** is selected, then the ChirpStack platform will assume that this device will join the LoRaWAN network using the ABP mode.

:::tip NOTE
Check **Disable frame-counter validation** to prevent issues during testing where the node-side frame counter resets to zero after the node is powered on. Without this setting, the server may fail to synchronize with the node-side counter, causing transmission errors.
:::

1. Fill the parameters requested, as appears in **Figure 62**:

* **Device name** and **Device description**: These are just descriptive texts.
* **Device EUI**: You can also add a specific Device EUI directly in the form.

> **Image:** Configure a Device in ABP Mode

2. Once these parameters are filled, click on the **CREATE DEVICE** button.

After selecting the ABP mode, the following parameters appear in the **ACTIVATION** tab:

* **Device address**
* **Network Session Key**
* **Application Session Key**

> **Image:** Chirpstack ABP Activation Parameters Needed

* The parameters can be either randomly generated by the platform or manually set with user-defined values. Once all parameters are correctly filled in, complete the process by clicking the **ACTIVATE DEVICE** button.

###### Configure the ABP mode on the RAK4600 Breakout Board

The RAK4600 Breakout Board complies with the LoRaWAN 1.0.2 specification. By default, the LoRa join mode is **OTAA**, and the LoRa Class is **Class A**.

To set up the RAK4600 Breakout Board to join ChirpStack using ABP, start by connecting the breakout board to the computer, as shown in section [Interface with RAK4600 Breakout Board](#interface-with-rak4600-breakout-board), open the RAK Serial Port Tool, and then wait for the communication to start. It is recommended to test the serial communication by sending either of these two AT commands:

```
at+get_config=lora:status
```

```
at+version
```

> **Image:** at+version command response

As an example, the following parameters will be configured in RAK4600:

- LoRa join mode: **ABP**
- LoRa class: **Class A**
- LoRa region: **EU868**
- Device address: **26011af9** (from ChirpStack registration)
- Network Session Key: **c280cb8d1df688bc18601a97025c5488** (from ChirpStack registration)
- Application Session Key: **4d42ec5caf97f03d833cdaf5003f69e1** (from ChirpStack registration)

1. Set the LoRa join mode to **ABP**.

```
at+set_config=lora:join_mode:1
```

2.  Set the LoRa Class to **Class A**.

```
at+set_config=lora:class:0
```

3.  Set the frequency/region to **EU868** (for Europe).

Refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4600-breakout-board/datasheet/#rf-characteristics" target="_blank">Datasheet</a> for the list of supported frequencies.

```
at+set_config=lora:region:EU868
```

4. Set the **Device Address**.

```
at+set_config=lora:dev_addr:26011af9
```

5. Set the **Network Session Key**.

```
at+set_config=lora:nwks_key:c280cb8d1df688bc18601a97025c5488
```

6.  Set the **Application Key**.

```
at+set_config=lora:apps_key:4d42ec5caf97f03d833cdaf5003f69e1
```

> **Image:** Chirpstack ABP Parameters Configuration via RAK Serial Port Tool

:::tip NOTE

After configuring all the parameters, reset your RAK4600 Breakout Board to save the parameters.

:::

7.  Join in ABP mode.

```
at+join
```

:::tip NOTE
The ABP mode in LoRaWAN doesn’t require to join a network before sending a LoRaWAN package. But, to keep the consistency of internal states of the firmware of the RAK4600, it is still required to send the `at+join` command in the ABP mode.
:::

> **Image:** RAK Serial Port Tool join LoRaWAN in ABP mode.

9. Try to send data from the RAK4600 Breakout Board to ChirpStack.

```
at+send=lora:2:1234567890
```
The console will feedback with an **OK** message.

> **Image:** Chirpstack Sample Data Sent via RAK Serial Port Tool

The sent data shall be displayed on the ChirpStack console on the **LORAWAN FRAMES** tab.

> **Image:** ChirpStack Console UPLINK LoRaWAN Frame in ABP mode.

### LoRa P2P
Refer to <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4600-module/quickstart/#lora-p2p-mode" target="_blank">LoRa P2P guide.</a>

## Miscellaneous

### Bluetooth Connection Modes

There are three BLE modes in the RAK4600 Breakout Board from the firmware V3.0.0.6: the **Peripheral Mode**, the **Central Mode**, and the **Beacon Scan Mode**. You can change the work mode of RAK4600 Breakout Board BLE using the AT command provided, which is defined. For further information, refer to RAK4600 Breakout Board <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4600-breakout-board/at-command-manual/#bluetooth-connection-modes" target="_blank">**AT Command Manual**</a>.

```
at+set_config=ble:work_mode:<mode>:<long_range>
```

**Description:** Set the work mode for BLE.
- **mode** - 0: BLE peripheral mode, 1: BLE central mode. 2: Beacon scan mode.
- **long_range** - 0: normal range. RAK4600 Breakout Board does not support BLE long-range.

#### BLE Peripheral Mode

Using the Peripheral Mode, you can scan RAK4600 Breakout Board BLE and connect it using your mobile device.

#### BLE Central Mode

Using the Central Mode, the RAK4600 Breakout Board BLE will not advertise, so your mobile device will not be able to scan it. This is very useful if you want to make the breakout board act as a BLE gateway wherein BLE Sensor Nodes (up to 20 devices) can send sensor data.

#### Beacon Scan Mode

Using the Beacon Scan mode, the RAK4600 Breakout Board can scan around for Beacon devices. It is useful to scan iBeacon and Eddystone.

#### RAK4600 Breakout Board BLE Default Settings

By default, the RAK4600 Breakout Board operates in **Peripheral Mode**. In this mode, you can easily configure the board through BLE, including performing DFU. Note that after resetting the breakout board, you have only 60 seconds to establish a BLE connection with your mobile device due to its power consumption settings.

If no connection is made within 60 seconds, the breakout board will stop BLE advertising and enter power-saving mode. However, once a BLE connection is established, there are no time limitations for using the RAK4600 Breakout Board BLE.

If the RAK4600 Breakout Board is set to operate in **Central Mode**, it will initially function in **Peripheral Mode** for 30 seconds. If no connection is established within this time, it will automatically switch to **Central Mode**. In this mode, the breakout board stops BLE advertising and will no longer be visible to your mobile device until you either change the mode back to Peripheral Mode or reset the RAK4600 Breakout Board.

### Upgrading the Firmware

Before you start working with the RAK44600 Breakout Board, it is recommended to keep the board updated to the latest version of the firmware. Download the latest <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4600-breakout-board/datasheet/#firmware" target="_blank">RAK4600 firmware</a>.

In the following sections, two (2) options for flashing new firmware in a RAK4600 Breakout Board are shown: **Upgrade through DAPLink** and **Upgrade through BLE**.

#### Firmware Upgrade Through DAPLink

Refer to the <a href="https://docs.rakwireless.com/product-categories/accessories/rakdap1/overview/#rakdap1-flash-and-debug-tool" target="_blank">RAKDAP1 Flash and Debug Tool</a> guide in the Accessories category.

#### Firmware Upgrade Through BLE

1. Install the **nRF Connect for Mobile**, developed by the Nordic Semiconductor company. This tool is available on Google Play Store and Apple App Store.

    - <a href="https://www.nordicsemi.com/Software-and-tools/Development-Tools/nRF-Connect-for-mobile" target="_blank">nRF Connect for Mobile</a>

2. Download the **DFU package** for the RAK4600 Breakout Board and save it on your mobile phone.

    - <a href="https://downloads.rakwireless.com/#LoRa/RAK4600/Firmware/History-Release-Version/DFU-Package/" target="_blank">**DFU package**</a>

3. Make sure the Bluetooth on your mobile is turned on. Open the **nRF Connect for Mobile** application, and you will see all BLE devices in range in the scan list:

> **Image:** Available Bluetooth Devices in the nRF Connect app

4. Turn on the RAK4600 Breakout Board and wait for a couple of seconds. Search for a BLE Device named **RUI-...** in the scan list of the app. Connect to this device and then click on **Secure DFU Service**.

:::tip NOTE
 The “**RUI-...**” BLE device is visible only for 60 seconds. For more information, see [**Bluetooth Connection Modes**](#bluetooth-connection-modes).
:::

> **Image:** Secure DFU Service in the nRF Connect App

5. In the “**Secure DFU Service**”, click the button highlighted in red in **Figure 71**.

> **Image:** Buttonless DFU

6. Click the arrow highlighted in **Figure 72**. A Write value pop-up window will appear and press “**Send**”.

> **Image:** Reset the Bootloader via Bluetooth

7. Now, the RAK4600 Breakout Board is now working in DFU Mode. In the application, you will see the default status of the breakout board, as shown in **Figure 73**.

> **Image:** RAK4600 Breakout Board Default Status Overview after Resetting

8. In the nRF Connect device list, search for a BLE device named **DfuTarg** and then, click on the **CONNECT** button.

> **Image:** RAK4600 Breakout Board Default Bluetooth ID after Resetting

9. After connecting, select the **DFU Icon**. In the file type selection, choose **Distribution packet (ZIP)** and press **OK**. You will then be prompted to select the ZIP file of the DFU package you previously downloaded.

> **Image:** Distribution Packet File Type under DFU

10. The DFU application will automatically begin upgrading the firmware of the RAK4600 Breakout Board via DFU over BLE. Once the upgrade is complete, the application will restart the breakout board, and DFU mode will be disabled. You can now use the RAK4600 Breakout Board with the latest firmware.

> **Image:** DFU Upgrading of RAK4600 Breakout Board Firmware via BLE

