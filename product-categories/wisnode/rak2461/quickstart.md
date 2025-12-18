---
slug: /product-categories/wisnode/rak2461/quickstart/
title: RAK2461 WisNode Bridge IO Lite Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK7201. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: "https://images.docs.rakwireless.com/wisnode/rak2461/datasheet/rak2461.png"
keywords:
  - quickstart
  - RAK2461
  - wisnode
sidebar_label: Quick Start Guide
---

# RAK2461 WisNode Bridge IO Lite Quick Start Guide

## Prerequisite

Before going through each and every step in the installation guide of the WisNode Bridge IO Lite, make sure to prepare the necessary items listed below:

### Hardware

1. [RAK2461 WisNode Bridge IO Lite](https://store.rakwireless.com/products/rak2461-wisnode-bridge-io-lite?utm_source=rak2461&utm_medium=Document&utm_campaign=BuyFromStore)
2. USB Type-C configuration cable
3. Gateway in range
4. A Windows/macOS/Linux Computer

### Software

IO.Box Desktop is a software application that will allow you to configure the devices from the RAK24XX series. You can download the application from here: 

- [Windows](https://apps.microsoft.com/detail/9nbxvlt622bs?hl=en-US&gl=US)
- [Linux](https://downloads.rakwireless.com/#IO.Box/) (coming soon)
- [Mac](https://downloads.rakwireless.com/#IO.Box/) (coming soon)

## Package Inclusions

### Variant for Wall Mounting

> **Image:** RAK2461 Package Inclusions 1

+ One (1) RAK2461 WisNode Bridge IO Lite (RS485-DIx4-DOx1 or RS485-DOx4)
+ One (1) Screw Kit
+ One (1) LoRa Antenna
+ One (1) Power Adapter
+ One (1) USB Cable (Type C to Type A)
+ One (1) 4-Pin Terminal Block 
+ Two (2) 8-Pin Terminal Block

### Variant for DIN Rail Mounting

> **Image:** RAK2461 Package Inclusions 2

+ One (1) RAK2461 WisNode Bridge IO Lite (RS485-DIx4-DOx1 or RS485-DOx4)
+ One (1) DIN rail Mounting Kit
+ One (1) LoRa Antenna
+ One (1) Power Adapter
+ One (1) USB Cable (Type C to Type A)
+ One (1) 4-Pin Terminal Block 
+ Two (2) 8-Pin Terminal Block

## Installation

RAK2461 allows for two installation methods: wall mounting and DIN rail installation.

### Wall Mounting

1. Drill the wall corresponding to the device dimensions and insert the anchors in the holes.

> **Image:** Hole drilling

2. Fix the device to the wall with two tapping screws.

> **Image:** Wall mounting

### DIN Rail Mounting

1. Attach the DIN rail mounting clip on the device with two M3*6 countersink screws.

> **Image:** Attaching the clip

2. Mount the device to the DIN rail.

> **Image:** DIN rail mounting

## Connect the RAK2461 to the Device

In this section, we will demonstrate how to use different interfaces on the RAK2461 to connect devices. 

:::tip NOTE

For connecting to other devices, read their specific documentation carefully and connect accordingly.
:::

### RS485 Sensor Application

In this section, the RK520-02 Soil Moisture, Temperature and Electrical Conductivity Sensor will be used as an example.

1. Connect the sensor device to the RAK2461.

> **Image:** Data interface connection

   Here are the basic communication parameters of the RK520-02 sensor:

| Parameter      | Definition   |
| -------------- | ------------ |
| Format         | 8-bit binary |
| Data bit       | 8-bit        |
| Parity         | No           |
| Stop bit       | 1            |
| Error checking | CRC          |
| Baud rate      | 9600         |

### Digital Input Sensor Application

 In this section, the DH-ARD631-50 Outdoor Active PIR sensor will be used as an example.

1. Have two devices, one transmitter and one receiver.
2. The transmitter's POWER(1/2) is connected to the Vout and GND of the bridge.
3. The receiver's POWER(2/3) is connected to the 12V_Out and GND of the bridge.
4. The receiver's ALARM(5/6) is connected to the DI4 COM and DI4 IN of the bridge.

> **Image:** Sensor to Bridge wiring

### Digital Output for Switching Application

1. You can connect any module or device to the port of the Digital Output as long as it operates on the recommended voltage rating.

> **Image:** Wiring

## Power On the RAK2461

1. The RAK2461 device can be powered either by:

- 9-24 V<sub>DC</sub> input
- USB type-C

The USB type-C port of the device can be used for configuration. Powering the device from the type-C port will not provide power to the sensor connected to Vout but only to the device itself. To power the device and sensor, you should use the 9-24 V<sub>DC</sub> input of the RAK2461.

> **Image:** Power interface connection

## Connect the RAK2461 to the IO.Box

1. Download and open the [IO.Box](https://downloads.rakwireless.com/#IO.Box/) application.

2. Connect the RAK2461 to a computer using the USB type-C cable. 

   :::tip NOTE

   + Note that this will work for the LoRaWAN configuration, but when configuring the sensor you would need to connect the 9-24 V<sub>DC</sub> power supply in order to provide power to the sensor itself. 
   + Make sure that the USB type-C cable that you are using supports data transfer and no other serial software is connected to the COM port that RAK2461 uses.

   :::

3. Click **Connect Device** in the IO.Box console.

> **Image:** IOBox get started

If an error occurs that shows no device detected, here are some possible causes for that and how to fix it:

- Double-check the quality of the USB cable and if the correct COM port is used.
- Check if other terminal software is active and still connected to the RAK2461.

> **Image:** No device error

4. On the IO.Box dashboard screen, you can see information about the devices connected to the PC in the form of a list of connected devices with device models and EUIs. Choose the device that you wish to configure via the **Connect** button next to it.

5. On the main menu to the left, choose **LoRaWAN** to configure the LoRaWAN settings as needed. Do not forget to click **Save** below the changes.

- **Device EUI**: This is the unique identifier provided by RAKwireless.
- **Region**: The LoRaWAN region/band.
- **Class**: Choose LoRaWAN class C.
- **Join Mode**: Choose between OTAA and ABP according to LoRaWAN protocol.
- **Application EUI**: Enter the unique identifier for your application.
- **Application Key**: Enter the unique secure key for your application.
- **Confirm Mode**: Activate to receive confirmation messages from the network server for each uplink.
- **ADR**: Enable Adaptive Data Rate allowing the network server to control the data rate for your device.
  + **DataRate**: Manually set the data transmission rate. Lower rates extend coverage but increase transmission time and power usage. Choose based on the distance and signal quality to the gateway.
  + **TX Power Level**: Adjust the transmission power level. The lower the number the higher the power. 0 is the maximum allowed in the selected region and each incrementation of 1 to the number reduces the power by 2 dBm.
- **Data Collection Period**: Set up the global data report period of the device. Range: 60–86400 in seconds.
- **LoRaWAN Status**: Indicates the activity of the device in the LoRaWAN network.

> **Image:** LoRaWAN tab

## Interface Configuration

This section shows the interface configuration references for different applications.
### RS485 Interface

#### RS485 Interface Configuration

1. Go to the **System** tab from the main menu. Enable the **DC12 V Output**. Note that the power output interface connected to the example sensor is enabled here. Please enable the power output interface that your sensor is actually connected to.

> **Image:** Enable the power output

2. Go to the **RS485** tab from the main menu and configure the interface according to the sensor/device you are connecting to. Do not forget to save your changes. In this tab you will find:

- **Baudrate**: Select the communication speed for the RS485 interface, measured in bits per second. Choose a rate that matches your device's requirements.
- **Databits**: Select the number of data bits for each character in the RS485 communication. Typically, options include 7 or 8 bits, depending on your device's protocol requirements.
- **Stopbits**: Select the number of stop bits used in the RS485 communication. Common options are 1 or 2, depending on your device's data transmission protocol.
- **Parity**: Select the parity setting for the RS485 interface. Options typically include **None** for no parity, **Even** for even parity, or **Odd** for odd parity. Choose based on your device's communication requirements.

> **Image:** RS485 interface configuration

#### Add Modbus Poll Task

This section shows how to create a polling task with an integer data type. If you need to create a polling task with a raw binary data type, refer to [(Optional) Add a Raw Data in Binary Poll Task](#optional-add-a-raw-data-in-binary-poll-task).
1. In the **Modbus Poll Task** menu click **+Add** for a new poll. You will see the **Polling Task parameters** that need to be configured.

> **Image:** Add poll task

2. Fill in the relevant fields according to the specific sensor's datasheet. Here we create a temperature polling task as an example.

> **Image:** Add temperature polling task

- **Channel ID**: Enter the identifier for the polling task. This ID is included in the device’s uplink data to indicate the task.
- **Name**: Custom name, length: 4-15.
- **Device Address**: The Modbus slave address in decimal format. Range: 1-254.
- **Function Code**: The Modbus function code defines this poll's operation.
- **Register Address**: The address of the register that you wish to access in hexadecimal format.
- **Quantity**: The number of register addresses that you want to access.
- **Data Type**: The data type of the Modbus response.
- **Scale**: To adjust the raw data from the Modbus response to the desired units. For example, to convert kilograms to grams set the scale to X1000.
- **Sensor Type**: Choose the unit of the data obtained from the Modbus slave device. 
- **Enable**: Enable or disable this polling task.
- **Request**: Displays the Modbus command generated based on the settings you've selected above. This command will be used to communicate with the Modbus device.
- **Response**: Displays the response received from the Modbus slave device.
- **Value**: This shows the data extracted from the Modbus Response is parsed according to the above configuration.
- **Uplink Data**: Displays the data payload format that will be sent to the server, based on the configuration above.

3. Before saving the task click **Check** for automatic validation.
4. Save the polling task.
5. Create moisture and EC polling tasks in the same way.

> **Image:** Add moisture polling task

> **Image:** Add EC polling task

> **Image:** Created polling tasks

#### (Optional) Add a Raw Data in Binary Poll Task

1. In the **Modbus Poll Task** menu click **+Add** for a new poll. You will see the **Polling Task parameters** that need to be configured.

> **Image:** Add poll task

2. Fill in the relevant fields according to the specific sensor's datasheet. Here we create a temperature polling task as an example.

> **Image:** Add temperature polling task

- **Channel ID**: Enter the identifier for the polling task. This ID is included in the device’s uplink data to indicate the task.
- **Name**: Custom name, length: 4-15.
- **Device Address**: The Modbus slave address in decimal format. Range: 1-254.
- **Function Code**: The Modbus function code defines this poll's operation.
- **Register Address**: The address of the register that you wish to access in hexadecimal format.
- **Quantity**: The number of register addresses that you want to access.
- **Data Type**: The data type of the Modbus response.
- **Sensor Type**: Choose the unit of the data obtained from the Modbus slave device. 
- **Enable**: Enable or disable this polling task.
- **Request**: Displays the Modbus command generated based on the settings you've selected above. This command will be used to communicate with the Modbus device.
- **Response**: Displays the response received from the Modbus slave device.
- **Value**: This shows the data extracted from the Modbus Response is parsed according to the above configuration.
- **Uplink Data**: Displays the data payload format that will be sent to the server, based on the configuration above.

3. Before saving the task click **Check** for automatic validation.
4. Save the polling task.
5. Create moisture and EC polling tasks in the same way.

> **Image:** Add moisture polling task

> **Image:** Add EC polling task

> **Image:** Created polling tasks

### Digital Input Interface

1. Go to the **System** tab from the main menu.

2. Enable the **DC Vout Output** and the **DC 12 V Output** power outputs. Note that the power output interface connected to the example sensor is enabled here. Please enable the power output interface that your sensor is actually connected to.

> **Image:** Enable the power outputs

3. Go to the **DI/DO** tab. After enabling DI4 and reloading, you will see the input state enabled.

+ **Port ID**: The identifier of the digital input port. You can find the port ID on the device’s enclosure label.
+ **Channel ID**: An identifier of the polling task. The ID will be included in the uplink data to indicate the source of the data.
+ **Debounce**: Set a delay (Range: 50-2000 ms) to stabilize the signal from a switch or button, ensuring only a single action is registered and eliminating false triggers due to contact bounce.
+ **Input State**: Displays this digital input port's status (active or inactive).
+ **Enable**: Toggle to activate the polling task for this port, allowing it to report the port’s state.

> **Image:** Enable DI4

### Digital Output Interface

1. Go to the **DI/DO** tab from the main menu.

+ **Port ID**: The identifier of the digital input port. You can find the port ID on the device’s enclosure label.
+ **Channel ID**: An identifier of the polling task. The ID will be included in the uplink data to indicate the source of the data.

+ **Output State**: Toggle to change this digital output port's current state (active or inactive).
+ **Enable**: Toggle to activate the polling task for this port, allowing it to report the port’s state.

2. When the output state is enable, the left bulb is supplied, when it is disabled, the right bulb is supplied.

> **Image:** Output state

3. Enable the **Enable** button to activate the polling task for this digital output port and report the current state of the port.

## Connect the RAK2461 to LoRa Network Server

This section provides you with operation guidance for connecting the RAK2461 to different LoRaWAN network servers.

### Built-in Network Server

In this section, the RAK2461 Bridge Lite IO will be connected to an RAKwireless gateway. For the gateway, the built-in LNS will be used. 

####  Set-up the Built-in Network Server

1. Start by accessing the gateway. You can see how to do it on the [WisGateOS V2 user manual](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/).

> **Image:** WisGateOS 2 login page

2. Once logged in, head to the **LoRa** menu.

> **Image:** LoRa page

3. By default, the gateway works as a Built-In Network Server. If not, switch the **Work mode** to **Built-in network server**.

#### Adding Application

1. Once the gateway is in Built-in network server mode, head to the **Applications** tab.

> **Image:** Create Application in the Built-In Network Server

2. Click the **Add application** button or **add one now** link to add a new application. On the new page, fill in the following information:

> **Image:** Adding application

- **Application name**: type a name for the application.
- **Application description**: optionally you can write a description of the application.
- **Application Type**: from the drop-down menu select the type of application.
- **Unified Application key**: all devices will use the same application key. Selecting this option pops up an **Application Key** field. This value needs to be consistent with the value from the end device. You can type your application key there or use the **Autogenerate** button to generate one.

> **Image:** Unified application key

The **Auto Add Device** switch activates the **Application EUI** field. The device will be automatically added to the application after the application EUI and key verification.

> **Image:** Auto add device

- **Separate Application keys**: each device will have its own application key. The key is added when registering the device.
- **Payload type**: from the drop-down, select **CayenneLPP** payload type and turn on the **Only forward data object** feature.

3. Once set, click **Save application** to add the application.
4. After the application is added, head to the **End devices** tab. The devices should automatically register upon join request if you are using the Auto Add Device feature.
If that’s not the case, click the **Add end device** button. On the **End device information** page fill in the following information:

> **Image:** Successfully created application

- **Activation Mode**: choose the activation mode of your device.
  - **OTAA**
  - **ABP**: This mode pops up two additional fields:
    - **Application Session Key**
    - **Network Session Key**
- **End device (group) name**: the name of the device.
- **End device description (optional)**: optionally, you can add a description for the device.
- **Class**: the class of the device.
- **Frame Counter width**: the width of the frame counter. Leave it as default.
- **LoRaWAN MAC Version**: the LoRaWAN MAC version. 

#### Adding the Device

1. Once everything is set, click **Add end devices** to go to the page and add the device.

2. On the **Adding end devices** page, type the device EUI at the **End Device EUI (main)** and click **Add to “End Devices list”**.

> **Image:** Adding end device

- If the EUI is correct, the device will show in the **End devices list**.
- If the EUI is not correct, the devices will show in the **End devices with an error**.

3. Once the device is added to the **End devices list** click **Add end devices**. Confirm you are adding the device.

> **Image:** Confirmation message for adding a device

4. After the device has successfully joined the LNS, you will see the LoRaWAN status in the IO.Box console toggles as activated. You might need to refresh the page.

> **Image:** Device is online

> **Image:** LoRaWAN status

Wait a while and you will see the uplink data from the LoRaWAN network. 

The following is an example of RS485 application uplink data. The format of the uplink message would be as follows: 

`01 + 67(tem) + 00e1(Hex) 22.5(Dec) 22.5℃     02 + 70(RH) + 01d5(Hex) 469(Dec) 46.9%`

`03 + 7f(EC) + 000128e0(Hex) 76000(Dec) 76.000us/cm`

> **Image:** Uplink data

### The Things Network (TTN)

#### Gateway Configuration

##### Registering the Gateway

1. Log in first and head on to [TTNv3 website ](https://eu1.cloud.thethings.network/console). If you already have a TTN account, you can use your The Things ID credentials to log in.

> **Image:** Login in

2. To register a commercial gateway, choose **Gateways** tab. Click **+Register gateway**.

> **Image:** Add a gateway

3. In the **Gateway EUI** field, type the EUI of the gateway. Click on **Confirm**. The gateway's EUI can be found either on the sticker on the casing or by going to the **Dashboard** > **Overview** page via the Web UI. Instructions on how to access your gateway via Web UI can be found in the product's [Quick Start Guide ](https://docs.rakwireless.com/product-categories/wisgate/).

> **Image:** Add gateway EUI

4. After typing the EUI, click on **Confirm**. Additional fields will pop up. Fill in the following information:

- **Gateway ID**: This will be the unique ID of your gateway in the Network. An ID based on the EUI is automatically generated. You can change it if you need. Note that the ID must contain only lowercase letters, numbers, and dashes (-).
- **Gateway name**: Optionally, you can type a name for your gateway.
- **Frequency plan**: The frequency plan used by the gateway.

> **Image:** Configure parameters

5. To register your gateway, click **Register gateway**.

> **Image:** Successfully added a gateway

##### Generating the Token

1. To generate a key file, , click **API keys** in the left navigation of the registered gateway.

2. On the **API keys page**, choose **+Add API key**.

> **Image:** API key page

3. In the **Name field**, type the name of your key (for example - mykey). Choose **Grant individual rights** and select **Link as Gateway to a Gateway for traffic exchange, i.e. write uplink and read downlink**.

> **Image:** Generate an API key

4. To generate the key, choose **Create API key**. The following window will pop up, telling you to copy the key you just generated.

> **Image:** Copying the generated key

:::warning

Copy the key and save it in a `.txt` file (or other), because you won’t be able to view or copy your key after that.

:::

5. Click **I have copied the key** to proceed.

##### Configuring the Gateway

1. To configure the gateway, access it via the Web UI. To learn how to do that, refer to the [Quick Start Guide ](https://docs.rakwireless.com/product-categories/wisgate/).
2. Navigate to **LoRa** > **Configuration**. Configure the following parameters and save.

> **Image:** Configure the gateway parameters

- **Basics Station Server Type**: For server type, choose **LNS Server**.
- **Server URL**: This is the link to The Things Stack server. Note that, for this tutorial, the gateway is connected to the European cluster. For Europe fill in the following:

```text
wss://eu1.cloud.thethings.network
```

- **Server Port**: The LNS Server uses port 8887. Type in **8887**.
- **Authentication Mode**: Choose **TLS server authentication and Client token**. When selected, the **Trust (CA Certificate)** and **Client token** fields will show up.
- **Trust (CA Certificate)**: For trust, upload the **Let’s Encrypt ISRG ROOT X1 Trust** certificate by clicking **choose file**. The file with the certificate can be downloaded [directly ](https://letsencrypt.org/certs/isrgrootx1.pem).
- **Client Token**: This is the generated API key.

3. To save the changes, click **Save Changes**. If everything is set correctly, you can see the gateway is connected to TTNv3.

> **Image:** Successful connection

#### RAK2461 Configuration

##### Creating Application

1. Click the **Application** tab at the top of the left navigation to enter the application interface.

> **Image:** Application list

2. Click **+Add application** to create an application.

> **Image:** Create an application

3. After filling the application details, click **Create application** to save the configuration.

##### Adding the device

IO.Box supports automatically adding node device to the TTN network server.

1. Navigate to the **Integration tab** > **Onboard to TheThings Stack Server** to create a device profile, then click **OK**.

> **Image:** Create a device profile

2. Click **Create New** to create a TheThingsStack Server and configure the following parameters.

> **Image:** Create a TheThingsStack Server

+ **Name**: The name of TheThingsStack Server.

+ **Server Address**: The ThingsStack Server address. In this case, it is `eu1.cloud.thethings.network`. The default port is 1884.

+ **User ID**: Your User ID, which can be obtained from **Profile settings** > **Edit profile**. 

+ **API Key**: Your personal API key. You can create one by following the steps below.

  1. To create a personal API key, go to **Home** > **User settings** > **API keys** in the left-hand sidebar and click **+Add API key**.

  2. Enter a **Name** for your key, set the **Expiry date**, select rights that you want to grant and then press **Create API Key**.

     
> **Image:** Create API key

  3. You will see a screen that shows your newly created API Key. You now can copy it in your clipboard by pressing the copy button. After saving the key in a safe place, press **I have copied the key**. You will not be able to see this key again in the future, and if you lose it, you can create a new one by following this same procedure.

     
> **Image:** Copy API key

3. Click **Create** to save the configuration.

> **Image:** Created server

4. Click the created server and select the application created previously in the TTN.

> **Image:** Select the created application

5. Click **OK** to confirm the registered node device information. 

> **Image:** Register the device

6. After the device is created successfully, you can view the added device in the TTN.

> **Image:** Added device in the TTN

7. To activate the device, click **Apply**.

> **Image:** Active the device

8. After a successful **Apply**, the device in the TTN is activated and receives data as shown in **Figure 62** and **Figure 63**. 

> **Image:** Device is online

> **Image:** Data details

You will also see the LoRaWAN activation status in the IO.Box console enabled. 

> **Image:** LoRaWAN status

### ChirpStack

This guide will show you how to connect the RAK2461 to a ChirpStack network server. In this tutorial, the ChirpStack v4 network server is used as an example.

#### Gateway configuration

##### Registering the Gateway

1. To register the gateway in the ChirpStack network server, access the ChirpStack UI. To do that, open a web browser and type the server address of the ChirpStack with port 8080.

```text
<IP address of ChirpStack>:8080 
```

2. Login using the following credentials:

   + Username/email: **admin**

   + Password: **admin**

> **Image:** ChirpStack login page

3. On the left pane, head to **Gateways**.

> **Image:** Gateway list

4. To register one, click **Add gateway**.

5. In the **General** menu, you need to set the gateway parameters.

> **Image:** Registering the gateway

- **Name**: Unique name for the gateway on the network server. The name may only contain words, numbers, and dashes.
- **Description**: A brief description of the gateway.
- **Gateway ID (EUI64)**: The Extended Unique Identifier (EUI) of the gateway. The EUI is in the **Dashboard** > **Overview** of the gateway Web UI.
- **Stats interval (secs)**: The expected interval in seconds in which the gateway sends its statistics.

6. Click **Submit**. You will see the registered gateway in the **Gateway list**.

> **Image:** Registered gateway

##### Configuring the Gateway

In this section, you will configure the gateway’s packet forwarder to send data to the ChirpStack Gateway Bridge. 

1. To configure the gateway, access it via the Web UI. To learn how to do that, refer to the [Quick Start Guide ](https://docs.rakwireless.com/product-categories/wisgate/).
2. Navigate to **LoRa** > **Configuration**. Configure the following parameters and save.

> **Image:** Configure gateway parameters

- **Work mode**: Packet forwarder.
- **Protocol**: Semtech UDP GWMP Protocol.
- **Server address**: Your ChirpStack server IP address.

- **Server Port**: The default port is 1700. If the UDP port enabled on your ChirpStack server is not 1700, this value should be consistent with the UDP port enabled on the server.

3. Click **Save changes** to save the changes.

4. If everything is set correctly, the gateway will display as online. You can click the gateway name to inspect the gateway traffic.

> **Image:** Registered gateway

#### RAK2461 Configuration

##### Creating Application

1. On the left pane, head to **Application**. 

> **Image:** Application list

2. Click **Add application** and configure the parameters.

> **Image:** Create application

3. Click **Submit**.

> **Image:** Added application

##### Adding the device

IO.Box supports automatically adding node device to the ChirpStack server.

1. Navigate to the **Integration** tab and choose the **Onboard to ChirpStack Server** to create a device profile. Click **OK**.

> **Image:** Create a device profile

2. Click **Create New** to create a ChirpStack Server and configure the following parameters.

> **Image:** Create a ChirpStack Server

+ **Name**: The name of ChirpStack server.

+ **Server Address**: The ChirpStack server address. The default port is 8080.

+ **Auth Method**: Password or API Key. Here we use API key.

+ **API Key**: ChirpStack server API key. You can create one by following the steps below.

  1. To create a personal API key, go to **Network Server** > **API keys** in the left-hand sidebar and click **Add API key**.

  2. Enter a **Name** for your key and then press **Submit**.

     
> **Image:** Create API key

  3. You will see the newly created API Key. Copy the key and save it in a safe place, press **Back**. You will not be able to see this key again in the future, and if you lose it, you can create a new one by following this same procedure.

     
> **Image:** Copy API key

+ **Tenant**: ChirpStack.

3. Click **Create** to save the configuration.

> **Image:** Created server

4. Click the created server and select the application created previously in the ChirpStack.

> **Image:** Select the created application

5. Click **OK** to confirm the registered node device information. 

> **Image:** Register the device

6. After the device is created successfully, you can view the added device in the ChirpStack.

> **Image:** Added device in the ChirpStack

7. To activate the device, click **Apply**.

> **Image:** Active the device

8. After a successful **Apply**, the device in the ChirpStack is activated and receives data.

> **Image:** Device is online

> **Image:** Data details

You will also see the LoRaWAN activation status in the IO.Box console enabled. 

> **Image:** LoRaWAN status

### System 

From the main menu of IO.Box, go to the **System** tab to find device information for the RAK2461 as well as power output toggles and firmware update options. 

#### Device Version Information

> **Image:** Device version information

- **Hardware Version**: Displays the specific version of the device’s hardware.
- **Firmware Version**: Displays the device's firmware version.
- **Device EUI**: Displays the unique identifier assigned by the manufacturer.
- **Device Model**: Displays the specific model name or number of the device.
- **Serial Number**: Displays the device’s serial number of the device.
- **Device Type**: Indicates the category or classification of the device, defining its interface types and functionalities. For detailed specifications refer to the device’s model information.
- **Frequency Band**: The device’s frequency band.

#### Power Output

> **Image:** Power output

- **DC Vout Output**: Toggle to enable or disable the Vout power output. When enabled, Vout passes through the same voltage as the Vin input. 
- **DC 12V Output**: Toggle to enable or disable the 12V_Out power output. When enabled, it provides a 12 V / 0.5 A power output. 
- **DC 5V Output**: Toggle to enable or disable the 5V_Out power output. When enabled, it provides a 5 V / 0.5 A power output. 

#### System Reset & Firmware Upgrade

> **Image:** System reset & firmware upgrade

##### Reboot

1. Simply press the **Reboot** button.

> **Image:** Reboot button

2. After clicking **OK**, the device will reboot and disconnect from the IO.Box application.

##### Factory Reset 

1. To restore the device to factory settings, press the **Reset to Factory** button.

> **Image:** Reset Button

2. After clicking **OK**, the device will restore to factory setting.

##### Firmware Update

1. Download the latest firmware.
2. Click **Firmware Upgrade** and select the firmware file.
3. Confirm the firmware information and then click **Upgrade**. Wait for the procedure to finish.

> **Image:** Confirm the firmware information

> **Image:** Upgrading procedure

> **Image:** Successful upgrade

