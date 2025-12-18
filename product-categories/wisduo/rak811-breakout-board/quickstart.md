---
title: RAK811 WisDuo Breakout Board Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK811 Breakout Board. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: "https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/rak811-breakout.png"
keywords:
    - RAK811 Breakout Board
    - wisduo
    - Quickstart
sidebar_label: Quick Start Guide
slug: /product-categories/wisduo/rak811-breakout-board/quickstart/
download: true
---


import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK811 Breakout Board Quick Start Guide

## Prerequisites

Before proceeding with the installation and setup guide for the RAK811 Breakout Board, ensure you have the following necessary items prepared:

### Hardware Tools

1. <a href="https://store.rakwireless.com/products/rak811-lpwan-breakout-module?utm_source=RAK811BreakoutModule&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">**RAK811 Breakout Board**</a>
2. <a href="https://store.rakwireless.com/products/daplink-tool?utm_source=RAKDAP1&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAKDAP1 Flash and Debug Tool</a>
3. Gateway in Range for Testing
4. Jumper Wires
5. 3.3 V Battery Power Supply
6. A Windows/Mac OS/Linux Computer

### Software Tools
1. <a href="https://downloads.rakwireless.com/#LoRa/Tools" target="_blank">RAK Serial Port Tool</a>
2. <a href="https://docs.rakwireless.com/product-categories/wisduo/rak811-breakout-board/datasheet/#firmwareos" target="_blank">RAK811 Breakout Board Firmware</a>
3. <a href="https://downloads.rakwireless.com/#LoRa/Tools/RAK_Device_Firmware_Upgrade_tool/" target="_blank">RAK Device Firmware Upgrade (DFU) Tool</a>


:::tip NOTE
The bootloader for the RAK811 Breakout Board is pre-installed during manufacturing, so flashing the bootloader is not required. If you find the bootloader of your RAK811 Breakout Board to be damaged, contact our support team through the <a href="https://forum.rakwireless.com/" target="_blank">RAKwireless forum</a>. For instructions on how to <a href="https://docs.rakwireless.com/product-categories/wisduo/rak811-breakout-board/quickstart/#upgrading-the-firmware" target="_blank">upgrade the firmware</a> of the device, refer to the miscellaneous section of this document.
:::

## Package Inclusions

- 1 pc - RAK811 Breakout Board (chipset pre-soldered on the board)
- 1 pc - LoRa Antenna

## Product Configuration

### Connect the RAK811 Breakout Board

The RAK811 Breakout Board can be configured using AT commands via the UART interface. To connect the RAK811 to a PC's USB port, you need a **USB to UART TTL adapter** and a serial terminal tool. It is highly recommended to use the <a href="https://downloads.rakwireless.com/#LoRa/Tools" target="_blank">RAK Serial Port Tool</a>, which allows you to easily send AT commands and view the corresponding replies from the console output.


:::warning
Before powering the RAK811 Breakout Board, install the LoRa antenna first. Failure to do so may result in damage to the board.
:::

- **Figure 1** shows the Pinout Diagram of the Board and **Figure 2** shows how to connect the RAK811 Breakout Board to the RAKDAP1.

<RkImage
 src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/interfacing-with-rak811-breakout/pinout_diagram.png"
  width="50%"
  caption="RAK811(H) Breakout Board Pinout Diagram"
  zoomMode={true}
/>

<RkImage
 src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/interfacing-with-rak811-breakout/rak811_diagram.svg"
  width="70%"
  caption="RAKDAP1 to RAK811 Breakout Board Connection"
  zoomMode={true}
/>

- Connect your **RAKDAP1 Flash and Debug Tool** to your Windows machine. Then, open the **RAK Serial Port Tool** and select the correct **COM port**.

<RkImage
 src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/interfacing-with-rak811-breakout/correct-port-correct-baud-rate.png"
  width="80%"
  caption="Correct Port Number and Correct Baud rate"
  zoomMode={true}
/>


### Connecting to The Things Stack (TTN V3)

This section will show how to connect the RAK811 Breakout Board to The Things Stack (TTN V3) platform.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/4.ttn-context.png"
  width="95%"
  caption="The Things Stack diagram"
  zoomMode={true}
/>

As shown in **Figure 4**, The Things Stack is an open source LoRaWAN Network Server suitable for global, geo-distributed public and private deployments as well as for small, local networks. The architecture follows the LoRaWAN Network Reference Model for standards compliancy and interoperability. This project is actively maintained by<a href="https://www.thethingsindustries.com/" target="_blank">The Things Industries</a>.

LoRaWAN is a protocol for low-power wide-area networks. It allows for large scale Internet of Things deployments where low-powered devices efficiently communicate with Internet-connected applications over long range wireless connections.

The RAK811 Board can be part of this ecosystem as a device, and the objective of this section is to demonstrate how simple it is to send data to The Things Stack using the LoRaWAN protocol. To achieve this, the RAK811 Board must be located inside the coverage of a LoRaWAN gateway connected to The Things Stack server.


#### Registration to TTN and Creating LoRaWAN Applications

1. Visit the <a href="https://console.cloud.thethings.network/" target="_blank">The Things Network platform</a> and choose a cluster, as shown in **Figure 5**. The Things Industries periodically adds more clusters, so select the one closest to your location. For this guide, **Europe 1** is selected.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/selecting-cluster.png"
  width="100%"
  caption="Select Cluster in TTN V3"
  zoomMode={true}
/>

2. Log in using your existing TTN V2 credentials. If you don’t have an account, create one.

To register as a new user on TTN, click on **Login with The Things ID**, then select **Register** on the next page, as shown in **Figures 6** and **7**. Fill in all the required details and activate your account.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/login-ttn.png"
  width="100%"
  caption="Log in using TTN account"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/register-new-account.png"
  width="100%"
  caption="Registration of new account"
  zoomMode={true}
/>


3. After creating an account, log in to the platform using your username/email and password, then click **Submit**, as shown in **Figure 8**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/login-to-ttn.png"
  width="100%"
  caption="Log in to TTN platform"
  zoomMode={true}
/>

4. Click **Authorize** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/authorization-to-ttn.png"
  width="100%"
  caption="Authorization to TTN"
  zoomMode={true}
/>

5. Click **Create an application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/creating-ttn-app.png"
  width="100%"
  caption="Create TTN application for your LoRaWAN devices"
  zoomMode={true}
/>

6. To register an application, first input the specific details and required information about your application, then click **Create application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/details-ttn-app.png"
  width="100%"
  caption="Details of the TTN application"
  zoomMode={true}
/>

7. Add end devices to your **The Things Stack** application. The LoRaWAN specification requires that each end device be personalized and activated. Activation can be done through either **Over-The-Air Activation (OTAA)** or **Activation By Personalization (ABP)**.

:::tip NOTE

Ensure that you are within the coverage of a **LoRaWAN gateway** registered to **The Things Stack (TTN V3)**. Without coverage from a registered LoRaWAN gateway, you will not be able to activate any devices that you register in your application.

RAKwireless offers <a href="https://store.rakwireless.com/collections/wisgate" target="_blank">LoRaWAN gateways</a> that can be connected to **The Things Stack (TTN V3)** if there is no LoRaWAN gateway coverage available in your location.

:::

#### The Things Stack OTAA Device Registration

1. To start adding an OTAA end device, click **+ Add end device**, as shown in **Figure 12**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/add-end-device.png"
  width="100%"
  caption="Add end device"
  zoomMode={true}
/>

2.    Click **Manually**, then configure the activation method by selecting **Over The Air Activation (OTAA)** and a compatible **LoRaWAN version**. Finally, click the **Start** button, as shown in **Figure 13** and **Figure 14**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/manual-register.png"
  width="100%"
  caption="Manually register device to The Things Stack"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/device-activation.png"
  width="100%"
  caption="Device activation configuration"
  zoomMode={true}
/>

3. Enter a unique **End Device ID** and EUIs (**DevEUI** and **AppEUI**). Optionally, provide an **End Device Name** and **End Device Description**. Finally, click **Network Layer Settings** to proceed to the next step.

:::tip NOTE
- Check if your module has a **DevEUI** on a sticker or a QR code that you can scan. Use this as the unique DevEUI for the device.

- It is recommended to use meaningful **End Device ID**, **End Device Name**, and **End Device Description** that align with your device's purpose. The **End Device ID** `rak-device` is used for illustration purposes only.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/otaa-device-info.png"
  width="100%"
  caption="OTAA Device Information"
  zoomMode={true}
/>

4. Set up the **Frequency Plan**, compatible **Regional Parameter Version**, and supported **LoRaWAN Class**. Then, click **Join Settings** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/otaa-configuration.png"
  width="100%"
  caption="OTAA Configuration"
  zoomMode={true}
/>

5. To obtain an **AppKey**, click the **Generate** button. Then, click **Add End Device** to complete the registration of your new device.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/otaa-appkey.png"
  width="100%"
  caption="OTAA AppKey generation and device registration"
  zoomMode={true}
/>

You should now be able to see the device on The Things Stack console after you fully registered your device, **as shown in Figure 18**.

:::tip NOTE

- The **AppEUI**, **DevEUI**, and **AppKey** are the parameters required to activate your LoRaWAN end device via OTAA. For security reasons, the **AppKey** is hidden by default, but you can reveal it by clicking the **Show** button. You can also quickly copy these parameters using the **Copy** button.

- The three OTAA parameters on The Things Stack device console are MSB by default.

- These parameters are always accessible on the device console page, as shown in Figure 18.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/otaa-sucessfull-register.png"
  width="100%"
  caption="OTAA device successfully registered to The Things Stack"
  zoomMode={true}
/>


#### RAK811 OTAA Configuration for The Things Stack

The RAK811 Board supports a series of AT commands to configure its internal parameters and control the functionalities of the module. To set up the RAK811 Board to join The Things Stack using OTAA, start by connecting the RAK811 Board to the Computer (see **Figure 1**) and open the RAK Serial Port Tool. Wait for the communication to start. It is recommended to test the serial communication and verify the current configuration by sending either of these two AT commands:

```
at+set_config=device:restart
```

```
at+version
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/3.command-response.png"
  width="90%"
  caption="AT Command response"
  zoomMode={true}
/>

As an example, these are the list of the parameters you need to configure in RAK811:

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

* Refer in the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak811-breakout-board/datasheet/#rf-characteristics" target="_blank">RAK811 Breakout Board Datasheet</a> for the list of supported frequencies.


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
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/14.lora-parameters.png"
  width="90%"
  caption="Configure LoRa Parameters"
  zoomMode={true}
/>

:::tip NOTE

After configuring all the parameters, reset your RAK811 Board for saving the parameters.

:::

7. Join in OTAA mode.

```
at+join
```

After 5 or 6 seconds, if the request is successfully received by a LoRa gateway, then you should see the messages shown in **Figure 21**.

8. Try to send a message from the RAK811 Board.

```
at+send=lora:2:1234567890
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/15.send-message.png"
  width="90%"
  caption="OTAA Test Sample Data Sent via RAK Serial Port Tool"
  zoomMode={true}
/>

You will see the data sent by the RAK811 Board on The Things Stack platform, as shown in **Figure 22**.


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/otaasend.png"
  width="100%"
  caption="OTAA Test Sample Data Sent Viewed in The Things Stack"
  zoomMode={true}
/>


#### The Things Stack ABP Device Registration

1. To register an ABP device, navigate to your application console and select the application where you want to add the device. Then, click **+ Add end device**, as shown in **Figure 23**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/add-end-device.png"
  width="100%"
  caption="Add end device"
  zoomMode={true}
/>

2. To register the module, click **Manually**, then configure the activation method by selecting **Activation By Personalization (ABP)** and a compatible **LoRaWAN version**. Finally, click the **Start** button, as shown in **Figure 24** and **Figure 25**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/manual-register.png"
  width="100%"
  caption="Add end device"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/manual-register-ttn.png"
  width="100%"
  caption="Manually register device to The Things Stack"
  zoomMode={true}
/>

3. Enter a unique **End Device ID** and **DevEUI**. Optionally, provide an **End Device Name** and **End Device Description** for your device. Then, click **Network Layer Settings** to proceed to the next step.

:::tip NOTE
- Check if your module has a **DevEUI** on a sticker or QR code that you can scan. Use this as the device's unique **DevEUI**.

- It is recommended to use meaningful **End Device ID**, **End Device Name**, and **End Device Description** that align with your device's purpose. The **End Device ID** `rak-device-abp` is used for illustration purposes only.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/device-information.png"
  width="100%"
  caption="Device Information"
  zoomMode={true}
/>

4. Set up the **Frequency Plan**, compatible **Regional Parameter Version**, and supported **LoRaWAN Class**. For an ABP device, generate the **Device Address** and **NwkSKey** (Network Session Key). Then, click **Application Layer Settings** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/abp-configuration.png"
  width="100%"
  caption="ABP Configuration in The Things Stack"
  zoomMode={true}
/>

5. To obtain the **AppSKey**, click the **Generate** button. Then, click **Add End Device** to complete your new device registration.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/abp-configuration-ttn.png"
  width="100%"
  caption="ABP Configuration in The Things Stack"
  zoomMode={true}
/>

You should now be able to see the device on The Things Stack console, as shown in **`Figure 29`**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/rak811-registered-ttn.png"
  width="100%"
  caption="RAK811 registered at The Things Stack"
  zoomMode={true}
/>

#### RAK811 ABP Configuration for The Things Stack

To set up the RAK811 Board to join The Things Stack using ABP, start by connecting the RAK811 Board to the Computer (see **Figure 1**) and open the RAK Serial Port  Tool. It is recommended to test the serial communication by sending either of these two AT commands:

```
at+set_config=device:restart
```

```
at+version
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/3.command-response.png"
  width="90%"
  caption="AT Command response"
  zoomMode={true}
/>

As an example, here is the list of parameters you need to configure in the RAK811:

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

- Refer in the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak811-breakout-board/datasheet/#rf-characteristics" target="_blank">RAK811 Breakout Board Datasheet</a> for the list of supported frequencies.

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
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/21.abp-at-commands.png"
  width="90%"
  caption="AT Command for ABP LoRa parameters via RAK Serial Port Tool"
  zoomMode={true}
/>

:::tip NOTE

After configuring all the parameters, reset RAK811 Board for saving the parameters.

:::

7. Join in ABP mode.

```
at+join
```

:::tip NOTE

In **ABP mode** of LoRaWAN, a device does not need to join a network before sending a LoRaWAN package. However, to maintain the consistency of the internal states of the RAK811 Board's firmware, it is still necessary to send the **`at+join`** command. In ABP mode, the firmware will reply almost immediately with an **"OK"**.

:::

8. Try to send a data from the RAK811 to The Things Network in ABP mode.

```
at+send=lora:2:1234567890
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/15.send-message.png"
  width="90%"
  caption="ABP Test Sample Data Sent via RAK Serial Port Tool"
  zoomMode={true}
/>

You can see the data sent by the RAK811 Board on the The Things Stack device console *Live data* section and the *Last seen* info should be a few seconds ago.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/abpsend.png"
  width="100%"
  caption="OTAA Test Sample Data Sent Viewed in The Things Stack"
  zoomMode={true}
/>

### Connecting to ChirpStack

The ChirpStack or previously known as LoRaServer project provides open-source components for building LoRaWAN networks. To learn more about ChirpStack, visit their <a href="https://www.chirpstack.io/" target="_blank">**website**</a>.

You can use RAK811 Breakout Board to connect with ChirpStack according to the following steps:


:::tip NOTE

In this document, it is assumed that you are using RAK Gateway and its built-in ChirpStack or RAK cloud testing ChirpStack. Also, the <a href="https://docs.rakwireless.com/product-categories/wisgate/rak7243/quickstart/#server-is-chirpstack" target="_blank">RAK Gateway with Chirpstack</a> must be configured successfully.

:::

1. Open the **ChirpStack** web interface that you want to connect to and log in with your credentials.

2. By default, there is already one or more items in this page. You can either use it or create a new item, but for this, create a new item by clicking the “**CREATE**” button.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/connecting-to-chirpstack/chirpstack-app.png"
  width="100%"
  caption="ChirpStack Applications"
  zoomMode={true}
/>

3. Fill up the necessary information then Click **CREATE APPLICATION**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/connecting-to-chirpstack/creating-the-app.png"
  width="100%"
  caption="Create the Application"
  zoomMode={true}
/>

4. Click the new item name **RAKwireless_Test_Application**:

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/connecting-to-chirpstack/applications-page.png"
  width="100%"
  caption="Applications page in ChirpStack"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/connecting-to-chirpstack/rak811-application.png"
  width="100%"
  caption="RAK811 Breakout Board Application"
  zoomMode={true}
/>

5. **Add** a Node device into ChirpStack by clicking the “**CREATE**” button.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/connecting-to-chirpstack/adding-node-device.png"
  width="100%"
  caption="Add a Node Device"
  zoomMode={true}
/>

6. Fill in the required fields. You can generate a **Device EUI** automatically by clicking the **Device EUI** icon, or manually enter the correct **Device EUI** in the edit box.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/connecting-to-chirpstack/filling-deive-parameters.png"
  width="100%"
  caption="Fill the Device Parameters"
  zoomMode={true}
/>

:::tip NOTE
- If you want to join in OTAA mode, select **DeviceProfile_OTAA** in the **Device-profile** item.
- If you want to join in ABP mode and CN470 frequency, select **DeviceProfile_ABP_CN470** in the **Device-Profile** item.
- If you want to join in ABP mode and other frequencies except AS923 and CN470, select **DeviceProfile_ABP** in the **Device-profile** item.
:::


#### OTAA Mode

1. To join ChirpStack in OTAA mode, select **DeviceProfile_OTAA**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-otaa-mode/selecting-otaa-activation.png"
  width="100%"
  caption="Select OTAA Activation Mode in ChirpStack"
  zoomMode={true}
/>

2. Press the **CREATE DEVICE** button. You can either manually enter the **Application Key** or generate it automatically by clicking the icon highlighted in **Figure 41**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-otaa-mode/app-key-generation.png"
  width="100%"
  caption="Application Key Generation"
  zoomMode={true}
/>

3. Click the **SET DEVICE KEYS** button to finalize the configuration on **ChirpStack**.

- The **Device EUI**, which was previously set on your **RAK811 Breakout Board** as `dev_eui`, matches the one highlighted in **Figure 42**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-otaa-mode/device-eui-code.png"
  width="100%"
  caption="Device EUI Code"
  zoomMode={true}
/>

- The **Application Key**, which was previously set as `app_key`, should match the one highlighted in **Figure 43**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-otaa-mode/application-key-lorawan.png"
  width="100%"
  caption="Application Key LoRaWAN"
  zoomMode={true}
/>

:::tip NOTE
The **Application EUI**, which was set in the RAK811 Breakout Board as **app_eui**, is not required for **ChirpStack**.
:::

4. Configure the **RAK811 Breakout Board** using AT commands. To do this, connect your RAK811 Breakout Board to a PC, power it on, and open the **RAK Serial Port Tool** on your computer.

```sh
at+version
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-otaa-mode/rak-serial-port-tool.png"
  width="45%"
  caption="RAK Serial Port Tool"
  zoomMode={true}
/>

5. If the join mode is not in OTAA, just set the LoRa join mode to **OTAA** and LoRa class to **Class A** by typing the AT commands shown in **Figure 45**.

```sh
at+set_config=lora:join_mode:0
```

```sh
at+set_config-lora:class:0
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-otaa-mode/settings-lorawan-mode.png"
  width="90%"
  caption="Set of LoRaWAN mode and class"
  zoomMode={true}
/>

6. Type the following AT command to set the **Frequency/Region**, **Device EUI**, **Application EUI**, and **Application Key**. Remember to replace "**XXX"** and "**XXXX"** with the parameters set in the previous steps.

```sh
at+set_config=lora:region:EU868
```

```sh
at+set_config=lora:dev_eui:XXXX
```

```sh
at+set_config=lora:app_eui:XXXX
```

```sh
at+set_config=lora:app_key:XXXX
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-otaa-mode/settings-frequency-eui.png"
  width="90%"
  caption="Setting of Frequency and Device EUI"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-otaa-mode/setting-app-eui-key.png"
  width="90%"
  caption="Setting of Application EUI and Key"
  zoomMode={true}
/>

7. Then, **join** in OTAA mode.

```sh
at+join
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-otaa-mode/joining-otaa.png"
  width="45%"
  caption="Join in OTAA"
  zoomMode={true}
/>

- **Joined Successfully!**

8. You should view the **JoinRequest** and **JoinAccept** on the ChirpStack page.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-otaa-mode/join-request-device.png"
  width="100%"
  caption="Join Request of the Device in the ChirpStack"
  zoomMode={true}
/>

9. Try sending data from the RAK811 Breakout Board to the ChirpStack by typing the command below in the serial port.

```sh
at+send=lora:2:1234567890
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-otaa-mode/sending-data-chirpstack.png"
  width="45%"
  caption="Send Data to ChirpStack"
  zoomMode={true}
/>

The message will be displayed on ChirpStack page, as shown in **Figure 51**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-otaa-mode/message-recieved.png"
  width="100%"
  caption="Message Received in ChirpStack"
  zoomMode={true}
/>



#### ABP Mode

1. If you select **DeviceProfile_ABP** or **DeviceProfile_ABP_CN470**, it means you want to join ChirpStack in **ABP mode**.

:::warning
Frequency AS923 in ABP Mode is not supported in Chirpstack.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-abp-mode/abp-activation.png"
  width="100%"
  caption="Chirpstack ABP Activation"
  zoomMode={true}
/>

2. Save the parameters for ABP in the **ACTIVATION** item.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-abp-mode/chirpstack-abp-activation.png"
  width="100%"
  caption="Chirpstack ABP Activation Parameters Needed"
  zoomMode={true}
/>

3. Use the previously saved parameters to configure the RAK811 Breakout Board using AT commands. To set the **LoRa join** mode to **ABP**, type the following command:

```sh
at+set_config=lora:join_mode:1
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-abp-mode/abp-va-rak-serial-tool.png"
  width="45%"
  caption="Chirpstack ABP Join Mode via RAK Serial Port Tool"
  zoomMode={true}
/>

4. Set LoRa class to **Class A**.

```sh
at+set_config=lora:class:0
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-abp-mode/abp-set-class.png"
  width="45%"
  caption="Chirpstack ABP Set Class via RAK Serial Port Tool"
  zoomMode={true}
/>

5. Set the frequency/region to **EU868**.

```sh
at+set_config=lora:region:EU868
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-abp-mode/abp-set-region.png"
  width="45%"
  caption="Chirpstack ABP Set Region/Frequency via RAK Serial Port Tool"
  zoomMode={true}
/>

6. Set the **Device Address**.

```sh
at+set_config=lora:dev_addr:XXXX
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-abp-mode/set-device-adress.png"
  width="45%"
  caption="Chirpstack ABP Set Device Address via RAK Serial Port Tool"
  zoomMode={true}
/>

7. Set the **Network Session Key**.

```sh
at+set_config=lora:nwks_key:XXXX
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-abp-mode/abp-set-network-key.png"
  width="45%"
  caption="Chirpstack ABP Set Network Session Key via RAK Serial Port Tool"
  zoomMode={true}
/>

8. Set the **Application Session Key**.

```sh
at+set_config=lora:apps_key:XXXX
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-abp-mode/abp-set-key-via-rak-port-toll.png"
  width="45%"
  caption="Chirpstack ABP Set Application Session Key via RAK Serial Port Tool"
  zoomMode={true}
/>

:::tip NOTE
After configuring all the parameters, reset your RAK811 Breakout Board to save the parameters.
:::

9. Join in ABP mode.

```sh
at+join
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-abp-mode/abp-join-via-rak-port-tool.png"
  width="45%"
  caption="Chirpstack ABP Join via RAK Serial Port Tool"
  zoomMode={true}
/>

:::tip NOTE
Although joining is not required in **ABP mode**, you still need to set this AT command to validate the parameters configured for ABP mode.
:::

10. Try to send a data from RAK811 Breakout Board to ChirpStack.

```sh
at+send=lora:2:1234567890
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-abp-mode/sample-data-sent.png"
  width="45%"
  caption="Chirpstack Sample Data Sent via RAK Serial Port Tool"
  zoomMode={true}
/>

- You will see the data, which is just sent from RAK811 Breakout Board on ChirpStack page:

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/chirpstack-abp-mode/data-received.png"
  width="100%"
  caption="Chirpstack Data Received Preview"
  zoomMode={true}
/>


### LoRa P2P Mode

This section shows how to use LoRa P2P mode. You will be using EU868 as the frequency, although it is applicable to other standard bands.

1. First, find two RAK811 Breakout Board which can work on EU868 frequency and make sure their firmware version isn’t less than V3.0.0.1.

2. Next, connect these two RAK811 Breakout Board with PC through UART, and open two serial port tool on PC.

3. Set the RAK811 to work in LoRa P2P mode. Open the RAK Serial Port Tool and send the following command:

```sh
at+set_config=lora:work_mode:1
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/lora-p2p-mode/lora-p2p.png"
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

Refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak811-breakout-board/at-command-manual/" target="_blank">Configuring Using AT Commands</a> section to learn more about the definition of the parameters used.

:::

Hence, it is translated into the following RAK811 AT command and sent to both units.

```
at+set_config=lorap2p:869525000:7:0:1:5:5
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/lora-p2p-mode/configuring-p2p.png"
  width="45%"
  caption="Configure P2P in both RAK811 Breakout Board Nodes"
  zoomMode={true}
/>

5. Set the transmission mode of the module. Unit 1 is configured as the sender, and Unit 2 is set to the receiver by AT command.

```
at+set_config=lorap2p:transfer_mode:2

at+set_config=lorap2p:transfer_mode:1
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/lora-p2p-mode/mode-setting.png"
  width="90%"
  caption="Set Modes in both RAK811 Module"
  zoomMode={true}
/>

6. Try sending a message from Unit 1 to Unit 2.

```
at+send=lorap2p:1234567890
```

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/lora-p2p-mode/sending-message.png"
  width="90%"
  caption="Message sent and received status in the two modules"
  zoomMode={true}
/>

You have successfully finished your RAK811 Breakout Board set up.

## Miscellaneous

### Upgrading the Firmware

:::tip NOTE

For RAK811 modules with firmware version **V3.0.0.12 and below**, you need to use the <a href="https://www.st.com/en/development-tools/stm32cubeprog.html" target="_blank">STM32CubeProgrammer</a> to upgrade the firmware and upload the **.hex file** (not the .bin file) of the <a href="https://downloads.rakwireless.com/#LoRa/RAK811/Firmware/" target="_blank">latest RAK811 firmware</a>. Firmware versions below V3.0.0.12 have a different bootloader code and are incompatible with the RAK DFU Tool.

:::

Follow the steps below to upgrade the firmware in Device Firmware Upgrade (DFU) mode via the UART1 interface:

1.	Download the latest application firmware of the RAK811 that can be found on the datasheet.
    - <a href="https://docs.rakwireless.com/product-categories/wisduo/rak811-breakout-board/datasheet/#firmwareos" target="_blank">RAK811 Breakout Board Datasheet</a>

2. Download and open the RAK Device Firmware Upgrade (DFU) tool.
    - <a href="https://downloads.rakwireless.com/#LoRa/Tools/RAK_Device_Firmware_Upgrade_tool/" target="_blank">RAK Device Firmware Upgrade (DFU) Tool</a>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/upgrading-the-firmware/2.device-firmware.png"
  width="90%"
  caption="RAK Upgrade Tool"
  zoomMode={true}
/>

3. Click **Choose File** and choose the firmware you have downloaded for your desired frequency band.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/upgrading-the-firmware/3.select-firmware.png"
  width="90%"
  caption="Choose the Correct Upgrade file"
  zoomMode={true}
/>

4. Click **Start** to upgrade. This may take a minute.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/upgrading-the-firmware/4.firmware-upgrading.png"
  width="90%"
  caption="Firmware Upgrading in Process"
  zoomMode={true}
/>

5. You should see the same pop-up window, as shown in **Figure 62**, if everything was successful.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/quickstart/upgrading-the-firmware/5.upgrade-success.png"
  width="90%"
  caption="Successfully Upgraded Firmware"
  zoomMode={true}
/>

6. Close the upgrade tool and **OPEN** the serial port tool again.

- It is recommended to use the **RAK Serial Port Tool** as it includes ready-to-use AT commands that are very helpful. You can download it for free from the RAK website at this **<a href="https://downloads.rakwireless.com/LoRa/RAK811/Tools/RAK_SERIAL_PORT_TOOL_V1.2.1.zip" target="_blank">RAK directory</a>**.

7. Choose the correct **COM port** and set the baud rate to **115200**. Then, open the serial port and enter the AT command shown below to restart. Another option is to press the **RST** button on the RAK811 Breakout Board.

```sh
at+set_config=device:restart
```

If you want to configure your RAK811 Breakout Board using the available **AT commands**, check the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak811-breakout-board/at-command-manual/" target="_blank">AT Commands for RAK811 Breakout Board</a>.


<RkBottomNav/>