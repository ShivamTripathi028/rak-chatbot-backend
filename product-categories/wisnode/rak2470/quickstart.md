---
slug: /product-categories/wisnode/rak2470/quickstart/
title: RAK2470 WisNode Bridge Serial Prime Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK2470. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: "https://images.docs.rakwireless.com/wisnode/rak2470/datasheet/rak2470.png"
keywords:
  - quickstart
  - RAK2470
  - wisnode
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'

import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK2470 WisNode Bridge Serial Prime Quick Start Guide

## Prerequisite

Before going through each and every step in the installation guide of the WisNode Bridge Serial Prime, make sure to prepare the necessary items listed below:

### Hardware

1. <a href="https://store.rakwireless.com/products/wisnode-bridge-serial-prime-rak2470?utm_source=rak2470&utm_medium=Document&utm_campaign=BuyFromStore&variant=43592626634950" target="_blank">RAK2470 WisNode Bridge Serial Prime</a>
2. [Configuration Cable for WisNode Bridge Serial Prime RAK2470](https://store.rakwireless.com/products/configuration-cable-for-wisnode-bridge-serial-prime-rak2470)
3. Gateway in range (for testing)
4. A Windows/macOS/Linux Computer

### Software

IO.Box Desktop is a software application that will allow you to configure the devices from the RAK24XX series. You can download the application from here:

- <a href="https://apps.microsoft.com/detail/9nbxvlt622bs?hl=en-US&gl=US" target="_blank">Windows</a>
- <a href="https://downloads.rakwireless.com/#IO.Box/" target="_blank">Linux</a> (coming soon)
- <a href="https://downloads.rakwireless.com/#IO.Box/" target="_blank">macOS</a> (coming soon)

## Package Inclusion

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/2.package-contents.png"
  caption="RAK2470 Package Inclusions"
  width="60%"
/>

- One (1) RAK2470 WisNode Bridge Serial Prime
- One (1) Mounting Kit
- One (1) T-Type Conversion Cable
- One (1) Power Adapter

## Installation

RAK2470 allows for pole mounting. Follow the provided installation steps to ensure secure mounting.

1. Fix the RAK2470 to the mounting kit with four (4) M4\*20 screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/5.fixing-the-device-to-the-mounting-kit.png"
  caption="Fixing the device to the mounting kit"
  width="30%"
/>

2. Using two (2) steel strips, fasten the RAK2470 on the pole.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/6.using-the-steel-strips.png"
  caption="Using the steel strips"
  width="45%"
/>

:::tip NOTE
The pole diameter supported by the included steel strips is 55 ~ 80&nbsp;mm.
:::

3. Link the connector of the RAK2470 to the corresponding port.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/7.adding-the-connector.png"
  caption="Adding the connector"
  width="45%"
/>



## Connect the RAK2470 to the Sensor

There are two ways to connect devices to RAK2470:

+ When the device has its own power source (e.g. a MPPT solar charge controller), it can be directly connected to the connector on the RAK2470.

+ When the device cannot provide power, it needs to be powered through the T-type conversion cable as follows.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/8.connecting-the-bridge-to-a-device.png"
  caption="Connecting the bridge to a device"
  width="70%"
/>

### Data Interface Connection

The connection to a sensor is via the L20-4 Port of the T-type conversion cable. In this section, the RK520-02 Soil Moisture, Temperature, and Electrical Conductivity sensors will be used as an example.
+ Pin 1: Connect to the positive terminal of the sensor's power cord.
+ Pin 2: Connect to RS485-A of the sensor.
+ Pin 3: Connect to RS485-B of the sensor.
+ Pin 4: Connect to the negative terminal of the sensor's power cord.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/connecting-the-sensor-to-the-t-type-conversion.png"
  caption="Data interface connection"
  width="70%"
/>

### RAK2470 Connection

If you are using the RAK2470 for the first time, you need to configure it. To do so, connect the RAK2470 to your PC using the USB configuration cable.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/rak2470-connection.png"
  caption="RAK2470 Connection"
  width="70%"
/>

## Power On the Device

The RAK2470 device can be powered with 5 ~ 12&nbsp;V<sub>DC</sub> wide-range input via a 12&nbsp;V<sub>DC</sub> adapter. Simply connect the adapter to the DC port of the T-type conversion cable.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/device-with-power-supply.png"
  caption="Power interface connection"
  width="60%"
/>

## Connect the RAK2470 to the IO.Box

1. Download and open the [IO.Box](https://downloads.rakwireless.com/#IO.Box/) application.

2. Connect the RAK2470 to a computer via the USB configuration cable.

3. Click **Connect Device** in the IO.Box console.

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/iobox-get-started.png"
width="100%"
caption="IOBox get started"
/>

:::tip NOTE
If an error occurs indicating that no device is detected, a common cause is that the RAK2470 has been connected to the PC for more than 30 seconds without any action. In this case, simply unplugging and re-plugging the device should resolve the issue.
:::

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/iobox-error.png"
width="100%"
caption="No device error"
/>

4. On the IO.Box dashboard screen, you can see information about the devices connected to the PC in the form of a list of connected devices with device models and EUIs. Choose the device that you wish to configure via the **Connect** button next to it.

5. On the main menu to the left, choose **LoRaWAN** to configure the LoRaWAN settings as needed. Do not forget to click **Save** below the changes.

- **Device EUI**: This is the unique identifier provided by RAKwireless.

- **Region**: The LoRaWAN region/band.

- **Join Mode**: Choose between OTAA and ABP according to LoRaWAN protocol.

- **Class**: The LoRaWAN Class (C).

- **Application EUI**: Enter the unique identifier for your application.

- **Application Key**: Enter the unique secure key for your application.

- **Confirm Mode**: Activate to receive confirmation messages from the network server for each uplink.

- **ADR**: Enable Adaptive Data Rate allowing the network server to control the data rate for your device.
  + **DataRate**: Manually set the data transmission rate. Lower rates extend coverage but increase transmission time and power usage. Choose based on the distance and signal quality to the gateway.
  + **TX Power Level**: Adjust the transmission power level. The lower the number the higher the power. 0 is the maximum allowed in the selected region and each incrementation of 1 to the number reduces the power by 2&nbsp;dBm.

- **Data Collection Period**: Set up the global data report period of the device. Range: 60–86400 in seconds.

- **LoRaWAN Status**: Indicates the activity of the device in the LoRaWAN network.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/lorawan-tab.png"
  width="100%"
  caption="LoRaWAN tab"
/>

## Interface Configuration

This section shows the interface configuration references for different applications.

#### RS485 Interface Configuration

1. Go to the **RS485** tab from the main menu and configure the interface according to the sensor/device you are connecting to. Do not forget to save your changes. In this tab you will find:

- **Baudrate**: Select the communication speed for the RS485 interface, measured in bits per second. The rate should match your device's requirements.
- **Databits**: Select the number of data bits for each character in the RS485 communication. Typically, options include 7 or 8 bits, depending on your device's protocol requirements.
- **Stopbits**: Select the number of stop bits used in the RS485 communication. Common options are 1 or 2, depending on your device's data transmission protocol.
- **Parity**: Select the parity setting for the RS485 interface. Options typically include **None** for no parity, **Even** for even parity, or **Odd** for odd parity. Choose based on your device's communication requirements.

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/interface-configuration.png"
width="100%"
caption="RS485 interface configuration"
/>

#### Add Modbus Poll Task

This section shows how to create a polling task with an integer data type. If you need to create a polling task with a raw binary data type, refer to [(Optional) Add a Raw Data in Binary Poll Task](#optional-add-a-raw-data-in-binary-poll-task).

1. In the **Modbus Poll Task** menu click **+ Add** for a new poll. You will see the **Polling Task parameters** that need to be configured.

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/add-poll-task.png"
width="100%"
caption="Modbus poll task"
/>

2. Fill in the relevant fields according to the specific sensor's datasheet. Here we create a temperature polling task as an example.

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/add_temperature_poll_task_int.png"
width="100%"
caption="Configure the polling task"
/>

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

5. Create the moisture and EC polling tasks in the same way.

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/add_moisture_poll_task_int.png"
width="100%"
caption="Add a moisture polling task"
/>

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/add_ec_poll_task_int.png"
width="100%"
caption="Add a EC polling task"
/>

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/lorawan-poll-tasks.png"
width="100%"
caption="Created polling tasks"
/>

:::tip NOTE
The RAK2470 WisNode Serial Prime has one channel used for both the RS485 communication with the sensor, and in the setup procedure. This is why you cannot see the requested data (polled data) from the sensor during setup.
:::


### (Optional) Add a **Raw Data in Binary** Poll Task

1. In the **Modbus Poll Task** menu click **+ Add** for a new poll. You will see the **Polling Task parameters** that need to be configured.

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/add-poll-task.png"
width="100%"
caption="Modbus poll task"
/>

2. Fill in the **register address** and other relevant fields according to the specific sensor's datasheet. Here we create a temperature polling task as an example.

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/add_temperature_poll_task_bin.png"
width="100%"
caption="Configure the polling task"
/>

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

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/add_moisture_poll_task_bin.png"
width="100%"
caption="Add a moisture polling task"
/>

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/add_ec_poll_task_bin.png"
width="100%"
caption="Add a EC polling task"
/>

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/lorawan-poll-tasks-bin.png"
width="100%"
caption="Created polling tasks"
/>

:::tip NOTE
The RAK2470 WisNode Serial Prime has one channel that is used both for the RS485 communication with the sensor and in the setup procedure. This is why you cannot see the requested data (polled data) from the sensor during setup.
:::

## Connect the RAK2470 to LoRa Network Server

This section provides you with operation guidance for connecting the RAK2470 to different LoRaWAN network servers.

### Built-in Network Server

In this section, the RAK2470 WisNode Bridge Serial Prime will be connected to a RAKwireless gateway. For the gateway, the built-in LNS will be used.

####  Set-up the Built-in Network Server

1. Start by accessing the gateway. You can see how to do it on the <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/" target="_blank">WisGateOS V2 user manual</a>.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/built-in-wisgateos-v2-login-page.png"
  caption="WisGateOS 2 login page"
  width="100%"
/>

2. Once logged in, head to the **LoRa** menu.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/built-in-lora-page.png"
  caption="LoRa page"
  width="100%"
/>

3. By default, the gateway works as a Built-In Network Server. If not, switch the **Work mode** to **Built-in network server**.

#### Adding Application

1. Once the gateway is in Built-in network server mode, head to the **Applications** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/built-in-application-page.png"
  caption="Create Application in the Built-In Network Server"
  width="100%"
/>

2. Click the **Add application** button or **add one now** link to add a new application. On the new page, fill in the following information:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/built-in-9.adding-application.png"
  caption="Adding application"
  width="100%"
/>

- **Application name**: type a name for the application.
- **Application description**: optionally you can write a description of the application.
- **Application Type**: from the drop-down menu select the type of application.
- **Unified Application key**: all devices will use the same application key. Selecting this option pops up an **Application Key** field. This value needs to be consistent with the value from the end device. You can type your application key there or use the **Autogenerate** button to generate one.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/built-in-7.unified-application-key.png"
  caption="Unified application key"
  width="45%"
/>

The **Auto Add Device** switch activates the **Application EUI** field. The device will be automatically added to the application after the application EUI and key verification.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/built-in-8.auto-add-device.png"
  caption="Auto add device"
  width="45%"
/>

- **Separate Application keys**: each device will have its own application key. The key is added when registering the device.
- **Payload type**: from the drop-down, select **CayenneLPP** payload type and turn on the **Only forward data object** feature.

3. Once set, click **Save application** to add the application.

4. After the application is added, head to the **End devices** tab. The devices should automatically register upon join request if you are using the Auto Add Device feature. <br/>
If that’s not the case, click the **Add end device** button. On the **End device information** page fill in the following information:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/built-in-11.adding-device.png"
  caption="Successfully created application"
  width="100%"
/>

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

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/built-in-13.adding-end-device.png"
  caption="Adding end device"
  width="100%"
/>

- If the EUI is correct, the device will show in the **End devices list**.
- If the EUI is not correct, the devices will show in the **End devices with an error**.

3. Once the device is added to the **End devices list** click **Add end devices**. Confirm you are adding the device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/built-in-confirm_add_device.png"
  caption="Confirmation message for adding a device"
  width="50%"
/>

4. After the device has successfully joined the LNS, you will see the LoRaWAN status in the IO.Box console toggles as activated. You might need to refresh the page.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/built-in-device-online.png"
  caption="Device is online"
  width="100%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/lorawan-status.png"
  caption="LoRaWAN status"
  width="60%"
/>

You have now completed the configuration of the RAK2470. However, the LoRa network server is not yet able to receive the uplink data because the RAK2470 currently has only one channel, which is being used both for RS485 communication with the sensor and during the setup process. To resolve this, remove the configuration cable to exit configuration mode. Then, connect the RAK2470 directly to the T-type conversion cable.

After disconnecting the device, wait for a while, and you'll see uplink data from the LoRaWAN network in the gateway Web UI. The figure below shows the uplink data from the example sensor.

- **Temperature**: `0167`
- **Data**: `00d9`

```
00d9 (hex) = 217 (dec)
217 x 0.1 (conversion factor) = 21.7° C
```

- **RH**: `02bc`
- **Data**: `028d`

```
028d (hex) = 653 (dec)
653 x 0.001 (conversion factor) = 65.3%
```

- **EC**: `037f`
- **Data**: `0002ee00`

```
0002ee00 (hex) = 192000 (dec)
192000 x 0.001 (conversion factor) = 192.000 us/cm
```

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/built-in-polling-task-parameters.png"
  caption="Uplink data"
  width="100%"
/>

### The Things Network (TTN)

#### Gateway Configuration

##### Registering the Gateway

1. Log in first and head on to [TTNv3 website ](https://eu1.cloud.thethings.network/console). If you already have a TTN account, you can use your The Things ID credentials to log in.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-login-ttn.png"
  caption="Login in"
  width="100%"
/>

2. To register a commercial gateway, choose **Gateways** tab. Click **+ Register gateway**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-register-gateway.png"
  caption="Add a gateway"
  width="100%"
/>

3. In the **Gateway EUI** field, type the EUI of the gateway. Click on **Confirm**. The gateway's EUI can be found either on the sticker on the casing or by going to the **Dashboard > Overview** page via the Web UI. Instructions on how to access your gateway via Web UI can be found in the product's [Quick Start Guide ](https://docs.rakwireless.com/product-categories/wisgate/).

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-add-gateway-eui.png"
  caption="Add gateway EUI"
  width="100%"
/>

4. After typing the EUI, click on **Confirm**. Additional fields will pop up. Fill in the following information:

- **Gateway ID**: This will be the unique ID of your gateway in the Network. An ID based on the EUI is automatically generated. You can change it if you need. Note that the ID must contain only lowercase letters, numbers, and dashes (-).
- **Gateway name**: Optionally, you can type a name for your gateway.
- **Frequency plan**: The frequency plan used by the gateway.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-configure-gateway-paras.png"
  caption="Configure parameters"
  width="100%"
/>

5. To register your gateway, click **Register gateway**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-add-gateway-successfully.png"
  caption="Successfully added a gateway"
  width="100%"
/>

##### Generating the Token

1. To generate a key file, , click **API keys** in the left navigation of the registered gateway.

2. On the **API keys page**, choose **+ Add API key**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-add-api-key.png"
  caption="API key page"
  width="100%"
/>

3. In the **Name field**, type the name of your key (for example - mykey). Choose **Grant individual rights** and select **Link as Gateway to a Gateway for traffic exchange, i.e. write uplink and read downlink**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-configure-api-key.png"
  caption="Generate an API key"
  width="100%"
/>

4. To generate the key, choose **Create API key**. The following window will pop up, telling you to copy the key you just generated.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-copy-api-key.png"
  caption="Copying the generated key"
  width="60%"
/>

:::warning

Copy the key and save it in a `.txt` file (or other), because you won’t be able to view or copy your key after that.

:::

5. Click **I have copied the key** to proceed.

##### Configuring the Gateway

1. To configure the gateway, access it via the Web UI. To learn how to do that, refer to the [Quick Start Guide ](https://docs.rakwireless.com/product-categories/wisgate/).
2. Navigate to **LoRa** > **Configuration**. Configure the following parameters and save.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-configure-gateway.png"
  caption="Configure the gateway parameters"
  width="100%"
/>

- **Basics Station Server Type**: For server type, choose **LNS Server**.
- **Server URL**: This is the link to The Things Stack server. Note that, for this tutorial, the gateway is connected to the European cluster. For Europe fill in the following:

```text
wss://eu1.cloud.thethings.network
```

- **Server Port**: The LNS Server uses port 8887. Type in **8887**.
- **Authentication Mode**: Choose **TLS server authentication and Client token**. When selected, the **Trust (CA Certificate)** and **Client token** fields will show up.
- **Trust (CA Certificate)**: For trust, upload the **Let’s Encrypt ISRG ROOT X1 Trust** certificate by clicking **choose file**. The file with the certificate can be downloaded [directly ](https://letsencrypt.org/certs/isrgrootx1.pem).
- **Client Token**: This is the generated API key.

3. To save the changes, click **Save Changes**. If everything is set correctly, you can see the gateway is connected to TTN.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-joined-ttn.png"
  caption="Successful connection"
  width="100%"
/>

#### RAK2470 Configuration

##### Creating Application

1. Click the **Application** tab at the top of the left navigation to enter the application interface.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-application-list.png"
  caption="Application list"
  width="100%"
/>

2. Click **+ Add application** to create an application.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-create-an-application.png"
  caption="Create an application"
  width="100%"
/>

3. Click **Create application** to save the configuration.

##### Adding the device

IO.Box supports automatically adding node device to the TTN network server.

1. Navigate to the **Integration** tab and choose the **Onboard to TheThings Stack Server** to create a device profile. Click **OK**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-onboard-to-ttn.png"
  caption="Create a device profile"
  width="100%"
/>

2. Click **Create New** to create a TheThingsStack Server and configure the following parameters.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-configure-ttnserver-paras.png"
  caption="Create a TheThingsStack Server"
  width="100%"
/>

+ **Name**: The name of TheThingsStack Server.

+ **Server Address**: The ThingsStack Server address. In this case, it is `eu1.cloud.thethings.network`. The default port is 1884.

+ **User ID**: Your User ID, which can be obtained from **Profile settings > Edit profile**.

+ **API Key**: Your personal API key. You can create one by following the steps below.

  1. To create a personal API key, go to **Home >  User settings > API keys** in the left-hand sidebar and click **+ Add API key**.

  2. Enter a **Name** for your key, set the **Expiry date**, select rights that you want to grant and then press **Create API Key**.

     <RkImage
       src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-create-api-key.png"
       caption="Create API key"
       width="100%"
     />

  3. You will see a screen that shows your newly created API Key. You now can copy it in your clipboard by pressing the copy button. After saving the key in a safe place, press **I have copied the key**. You will not be able to see this key again in the future, and if you lose it, you can create a new one by following this same procedure.

     <RkImage
       src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-copy-api-key-2.png"
       caption="Copy API key"
       width="60%"
     />

3. Click **Create** to save the configuration.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-created-server.png"
  caption="Created server"
  width="100%"
/>


4. Click the created server and select the application created previously in the TTN.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-select-application.png"
  caption="Select the created application"
  width="100%"
/>

5. Click **OK** to confirm the registered node device information.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-register-device.png"
  caption="Register the device"
  width="100%"
/>

6. After the device is created successfully, you can view the added device in the TTN.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-added-device.png"
  caption="Added device in the TTN"
  width="100%"
/>

7. To activate the device, click **Apply**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-active-device.png"
  caption="Active the device"
  width="100%"
/>

8. After a successful **Apply**, the device in the TTN is activated.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-device-online.png"
  caption="Device is online"
  width="100%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/lorawan-status.png"
  caption="LoRaWAN status"
  width="60%"
/>

You have now completed the configuration of the RAK2470. However, the LoRa network server is not yet able to receive the uplink data because the RAK2470 currently has only one channel, which is being used both for RS485 communication with the sensor and during the setup process. To resolve this, remove the configuration cable to exit configuration mode. Then, connect the RAK2470 directly to the T-type conversion cable.

After disconnecting the device, wait for a while, and you'll see uplink data from the LoRaWAN network in the TTN. The figure below shows the uplink data from the example sensor.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/ttn-data-details.png"
  caption="Data details"
  width="100%"
/>

### ChirpStack

This guide will show you how to connect the RAK2470 to a ChirpStack network server. In this tutorial, the ChirpStack v4 network server is used as an example.

#### Gateway configuration

##### Registering the Gateway

1. To register the gateway in the ChirpStack network server, access the ChirpStack UI. To do that, open a web browser and type the server address of the ChirpStack with port 8080.

```text
<IP address of ChirpStack>:8080
```

2. Login using the following credentials:

   + Username/email: **admin**

   + Password: **admin**

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-login-page.png"
  caption="ChirpStack login page"
  width="100%"
/>

3. On the left pane, head to **Gateways**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-gateway-list.png"
  caption="Gateway list"
  width="100%"
/>

4. To register one, click **Add gateway**.

5. In the **General** menu, you need to set the gateway parameters.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-register-gateway.png"
  caption="Registering the gateway"
  width="100%"
/>

- **Name**: Unique name for the gateway on the Network server. The name may only contain words, numbers, and dashes.
- **Description**: A brief description of the gateway.
- **Gateway ID (EUI64)**: The Extended Unique Identifier (EUI) of the gateway. The EUI is in the **Dashboard > Overview** of the gateway Web UI.
- **Stats interval (secs)**: The expected interval in seconds in which the gateway sends its statistics.

6. Click **Submit**. You will see the registered gateway in the **Gateway list**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-registered-gateway.png"
  caption="Registered gateway"
  width="100%"
/>

##### Configuring the Gateway

In this section, you will configure the gateway’s packet forwarder to send data to the ChirpStack Gateway Bridge.

1. To configure the gateway, access it via the Web UI. To learn how to do that, refer to the [Quick Start Guide ](https://docs.rakwireless.com/product-categories/wisgate/).
2. Navigate to **LoRa** > **Configuration**. Configure the following parameters and save.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-configure-gateway.png"
  caption="Configure gateway parameters"
  width="100%"
/>

- **Work mode**: Packet forwarder.
- **Protocol**: Semtech UDP GWMP Protocol.
- **Server address**: Your ChirpStack server IP address.

- **Server Port**: The default port is 1700. If the UDP port enabled on your ChirpStack server is not 1700, this value should be consistent with the UDP port enabled on the server.

3. Click **Save changes** to save the changes.

4. If everything is set correctly, the gateway will display as online. You can click the gateway name to inspect the gateway traffic.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-gateway-online.png"
  caption="Registered gateway"
  width="100%"
/>

#### RAK2470 Configuration

##### Creating Application

1. On the left pane, head to **Application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-application-list.png"
  caption="Application list"
  width="100%"
/>

2. Click **Add application** and configure the parameters.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-add-application.png"
  caption="Create application"
  width="100%"
/>

3. Click **Submit**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-added-application.png"
  caption="Added application"
  width="100%"
/>

##### Adding the device

IO.Box supports automatically adding node device to the ChirpStack server.

1. Navigate to the **Integration** tab and choose the **Onboard to ChirpStack Server** to create a device profile. Click **OK**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-onboard-to-chirpstack.png"
  caption="Create a device profile"
  width="100%"
/>

2. Click **Create New** to create a ChirpStack Server and configure the following parameters.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-configure-server-paras.png"
  caption="Create a ChirpStack Server"
  width="100%"
/>

+ **Name**: The name of ChirpStack Server.

+ **Server Address**: The ChirpStack Server address. The default port is 8080.

+ **Auth Method**: Password or API Key. Here we use API key.

+ **API Key**: ChirpStack server API key. You can create one by following the steps below.

  1. To create a personal API key, go to **Network Server > API keys** in the left-hand sidebar and click **Add API key**.

  2. Enter a **Name** for your key and then press **Submit**.

     <RkImage

       src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-create-api-key.png"
       caption="Create API key"
       width="100%"
     />

  3. You will see the newly created API Key. Copy the key and save it in a safe place, press **Back**. You will not be able to see this key again in the future, and if you lose it, you can create a new one by following this same procedure.

     <RkImage

       src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-copy-api-key-3.png"
       caption="Copy API key"
       width="100%"
     />

+ **Tenant**: ChirpStack.

3. Click **Create** to save the configuration.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-created-server.png"
  caption="Created server"
  width="100%"
/>



4. Click the created server and select the application created previously in the ChirpStack.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-select-application.png"
  caption="Select the created application"
  width="100%"
/>

5. Click **OK** to confirm the registered node device information.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-register-device.png"
  caption="Register the device"
  width="100%"
/>

6. After the device is created successfully, you can view the added device in the ChirpStack.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-added-device.png"
  caption="Added device in the ChirpStack"
  width="100%"
/>

7. To activate the device, click **Apply**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-active-device.png"
  caption="Active the device"
  width="100%"
/>

8. After a successful **Apply**, the device in the ChirpStack is activated.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-joined-chirpstack.png"
  caption="Active the device"
  width="100%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/lorawan-status.png"
  caption="LoRaWAN status"
  width="60%"
/>

You have now completed the configuration of the RAK2470. However, the LoRa network server is not yet able to receive the uplink data because the RAK2470 currently has only one channel, which is being used both for RS485 communication with the sensor and during the setup process. To resolve this, remove the configuration cable to exit configuration mode. Then, connect the RAK2470 directly to the T-type conversion cable.

After disconnecting the device, wait for a while, and you'll see uplink data from the LoRaWAN network in ChirpStack. The figure below shows the uplink data from the example sensor.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-device-online.png"
  caption="Device is online"
  width="100%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/chirpstack-data-details.png"
  caption="Data details"
  width="100%"
/>

### System

From the main menu of IO.Box, go to the **System** tab to find device information for the RAK2470 as well as power output toggles and firmware update options.

#### Device Version Information

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/device-info.png"
  caption="Device version information"
  width="80%"
/>

- **Hardware Version**: Displays the specific version of the device’s hardware.
- **Firmware Version**: Displays the device's firmware version.
- **Device EUI**: Displays the unique identifier assigned by the manufacturer.
- **Device Model**: Displays the specific model name or number of the device.
- **Serial Number**: Displays the device’s serial number of the device.
- **Device Type**: Indicates the category or classification of the device, defining its interface types and functionalities. For detailed specifications refer to the device’s model information.
- **Frequency Band**: The device’s frequency band.

#### System Reset & Firmware Upgrade

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/system.png"
  caption="System reset && firmware upgrade"
  width="80%"
/>

##### Reboot

1. Simply press the **Reboot** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/reboot.png"
  caption="Reboot button"
  width="80%"
/>

2. After clicking **OK**, the device will reboot and disconnect from the IO.Box application.

##### Factory Reset

1. To restore the device to factory settings, press the **Reset to Factory** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/reset.png"
  caption="Reset Button"
  width="80%"
/>

2. After clicking **OK**, the device will restore to factory setting.

##### Firmware Update

1. Download the latest firmware.
2. Click **Firmware Upgrade** and select the firmware file.
3. Confirm the firmware information and then click **Upgrade**. Wait for the procedure to finish.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/firmware-info.png"
  caption="Confirm the firmware information"
  width="80%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/upgrading.png"
  caption="Upgrading procedure"
  width="80%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/quickstart/upgrade-ok.png"
  caption="Successful upgrade"
  width="80%"
/>

<RkBottomNav/>