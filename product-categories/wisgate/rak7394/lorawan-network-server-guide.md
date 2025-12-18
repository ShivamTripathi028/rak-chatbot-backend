---
title: RAK7394 WisGate Developer CM4 LoRaWAN Network Server Guide
description: Comprehensive guide for configuring the RAK7394 WisGate Developer CM4 gateway with LoRaWAN network servers, including integration with The Things Network (TTNv3) and ChirpStack.
image: https://images.docs.rakwireless.com/wisgate/rak7394/rak7394.png
keywords:
    - RAK7394
    - WisGate Developer CM4
    - LoRaWAN gateway
    - LoRaWAN Network Server Guide
    - gateway configuration
    - IoT gateway setup
sidebar_label: LoRaWAN Network Server Guide
---

# RAK7394 WisGate Developer CM4 LoRaWAN Network Server Guide

## Connecting to The Things Stack (TTNv3)

The Things Network is enabling low-power devices to use long-range gateways to connect to an open-source, decentralized network to exchange data through an Application. Learn more about the Things Network through their [documentation](https://www.thethingsnetwork.org/docs/).

In this section, you will learn how to connect RAK7394/RAK7394C/RAK7394P WisGate Developer CM4 gateway to TTNv3.

1. To log in to TTNv3, visit the [TTN site](https://www.thethingsnetwork.org/). If you already have a TTN account, use your The Things ID credentials to log in.

2. Connect your gateway to the internet via the router using the method outlined in the [**Accessing the Internet**](https://docs.rakwireless.com/product-categories/wisgate/rak7394/quickstart/#accessing-the-gateway) section of the Quick Start Guide.

3. Configure the gateway by selecting TTN as the LoRa Server and setting the correct frequency, following the instructions provided in the **Configuring the Gateway** section.

4. Click **Start Building** and select the cluster that is geographically closest to your region.

> **Image:** Choose the cluster

5. Select **Register a Gateway** if you are a new user without a previously registered gateway, or navigate to **Gateways > + Add Gateway** if you have registered gateways before.

> **Image:** The Things Network console page

6. All registered gateways will be displayed. To register a new gateway, click **+ Add gateway**.

> **Image:** Add a new gateway

7. Fill in the required information and click **Create gateway**.

> **Image:** Register your gateway

- **Owner**: Automatically filled by The Things Stack, based on your account or created Organization.
- **Gateway ID**: This will be the unique ID of your gateway in the Network. Note that the ID must contain only lowercase letters, numbers, and dashes (-).
- **Gateway EUI**: A 64-bit extended unique identifier for your gateway. The gateway's EUI can be found by running either one of the following commands in the CLI of the gateway:

```
gateway-version
```

```
sudo gateway-config
```

- **Gateway description (optional)**: Optional gateway description; can also be used to save notes about the gateway.

- **Gateway Server address**: The address of the gateway server to connect to.

:::tip NOTE
- This tutorial uses the EU868 frequency band, so the server address should be set to: **eu1.cloud.thethings.network**.
- The **Europe 863-870 MHz (SF12 for RX2)** frequency plan is used.
:::

- **Frequency plan**: The frequency plan used by the gateway.

- The other settings are optional and can be adjusted to meet your specific requirements.

Once the gateway is configured for TTN and successfully registered in the console, its status will show as online.

> **Image:** Gateway connected successfully to TTN

## Connecting the Gateway with ChirpStack

The ChirpStack is an open-source LoRaWAN Network Server. For more information, visit the [ChirpStack site](https://www.chirpstack.io/).

For the RAK7394/RAK7394C/RAK7394P WisGate Developer CM4 Gateway, there are two ways to use ChirpStack:

### Using the Built-in ChirpStack

There is a built-in ChirpStack in every RAK Developer gateway if you use the latest firmware or the `rak_common_for_gateway` repository.

- When using the gateway for the first time after burning the latest firmware, it will operate in the **EU868 Band** and use the built-in ChirpStack as its default LoRa Server. If you do not wish to change the frequency or LoRa Server, no additional configuration is required, as this setup is automatically applied when the gateway boots.

- If it is not your first time using the gateway and you want to use the built-in ChirpStack as the LoRa Server, follow the steps outlined in the **Configuring the Gateway** section.

- **Optional**: If you have disabled **AP Mode** and connected the gateway to your Wi-Fi network (**Client Mode**), you can locate your gateway’s IP address using tools like [Advanced IP Scanner](https://www.advanced-ip-scanner.com/).

- The ChirpStack instance includes a **Web-based UI**. To access it, open a browser and use the following credentials:

  - **Browser Address**: `<Gateway IP address>:8080` (Example: `http://192.168.0.100:8080`)
  - **Username**: `admin`
  - **Password**: `admin`

:::warning
It is recommended to **change your password** to enhance the security of your account. You can do this by clicking the **Change Password** option under the user icon.
:::

> **Image:** ChirpStack web-based UI

- Everything is pre-configured, including **Device Profiles**, and the gateway is already registered with the server. To view the details, go to the **Gateways** tab and click on **rak_gateway** to access the gateway details page.

> **Image:** Available gateway in Chirpstack

- Navigate to the **Gateways** tab and check the **Last seen** status. It should show as a few seconds ago, indicating that the gateway is visible to the ChirpStack server.

> **Image:** Last seen status

### Using an Independent ChirpStack

You can set up an independent ChirpStack instance or deploy one on AWS. For instructions on using ChirpStack with AWS, refer to the [AWS guide](https://learn.rakwireless.com/hc/en-us/articles/26743884863767-How-To-Use-Amazon-Web-Services-with-LoRaWAN/). If you prefer to run ChirpStack on a different host or cloud service, follow the [Debian/Ubuntu guide](https://www.chirpstack.io/guides/debian-ubuntu/) on the ChirpStack site.

:::warning
Run the `sudo gateway-config` command in the CLI and configure the gateway to point to the IP address of the machine where you installed ChirpStack. This can be done by selecting **Setup RAK Gateway LoRa concentrator** (item 2 in the menu).
:::

- Assuming the setup is correct, log in to your ChirpStack instance to register your gateway by opening ChirpStack's web page in a browser and entering the appropriate URL.

    - **Browser Address**: `<IP Address of ChirpStack>:8080`
    - **Username**: `admin`
    - **Password**: `admin`

> **Image:** ChirpStack login page

- Click **Gateways** and select **+ CREATE** to register your gateway

> **Image:** ChirpStack registered gateways

- Fill in the necessary information.

> **Image:** Fill in the details

- Fill in the gateway ID that you got from the **Configuring the Gateway** section, also called gateway EUI.

- If your gateway is properly configured and a network connection is established between the external ChirpStack and your gateway, you should see the same page and status as depicted in **Figure 12**.

> **Image:** Successfully registered a gateway

## AWS IoT Core for LoRaWAN

Execute the following steps to set up your AWS account and permissions.

### Set Up Your AWS Account and Permissions

If you don't have an AWS account, refer to the instructions in the guide here. The relevant sections are **Sign up for an AWS account** and **Create a user and grant permissions**.

#### Overview

The high-level steps to get started with AWS IoT Core for LoRaWAN are as follows:

1. Set up Roles and Policies in IAM
2. Add a Gateway (see section [Add the Gateway to AWS IoT](#add-the-gateway-to-aws-iot))
3. Add Device(s) (see section [Add a LoRaWAN Device to AWS IoT](#add-a-lorawan-device-to-aws-iot))
    - Verify device and service profiles
    - Set up a Destination to which device traffic will be routed and processed by a rule.

These steps are outlined throughout this guide. For additional information, refer to the [AWS LoRaWAN Developer Guide.](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-lorawan.html)
#### Add the Gateway to AWS IoT

##### Preparation

Refer to the [online guide](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-onboard-gateways.html) for steps required before onboarding your gateway. For more details, check the software section of the [datasheet](https://docs.rakwireless.com/product-categories/wisgate/rak7248/datasheet/#software).

##### Frequency Band Selection and Role Setup

Refer to the [online guide](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-rfregion-permissions.html) for information on selecting an appropriate frequency band.

:::tip NOTE
The LoRa frequency bands supported by the RAK7248 include:
- RU864
- IN865
- EU868
- US915
- AU915
- KR920
- AS923
- CN470

You can choose the appropriate frequency band of your device from the options available on the [RAK Store](https://store.rakwireless.com/products/rak7248).
:::

##### Add the LoRaWAN Gateway

To register the gateway with AWS IoT Core for LoRaWAN, follow the steps in the [online guide](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-onboard-gateway-add.html) under the **Add a gateway using the console** section.

#### Add a LoRaWAN Device to AWS IoT

##### Preparation

- Go to the datasheet to learn more about the [RAK4631 WisBlock LPWAN Module](https://docs.rakwireless.com/product-categories/wisblock/rak4631/datasheet/#rak4631-wisblock-lpwan-module-datasheet).
- Follow the steps in the [online guide](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-onboard-end-devices.html) under the **Before onboarding your wireless device** section, then proceed to the [Add your wireless device to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-end-devices-add.html) section.

##### Verify Profiles

AWS IoT Core for LoRaWAN supports device profiles and service profiles.  Device profiles contain the communication and protocol parameter values the device needs to communicate with the network server. Service profiles describe the communication parameters the device needs to communicate with the application server.

Some pre-defined profiles are available for device and service profiles.  Before proceeding, verify that these profile settings match the devices you will be setting up to work with AWS IoT Core for LoRaWAN. For more details, refer to the [online guide](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-define-profiles.html) under the **Add profiles to AWS IoT Core for LoRaWAN** section.

:::tip NOTE
Proceed only if you have a device and service profile that meets your requirements.
:::

##### Set Up a Destination for Device Traffic

Most LoRaWAN devices do not send data to AWS IoT Core for LoRaWAN in a format directly usable by AWS services. Therefore, the data must first be routed to a **Destination**. A **Destination** represents an AWS IoT rule that processes the device's data for AWS services. This rule includes an SQL statement to select the device's data and topic rule actions to forward the SQL query results to the intended AWS services.

For more information, refer to the [online guide](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-create-destinations.html) under sections **Add a destination using the console** and **Create an IAM role for your destinations**. Also, refer to **Create rules to process LoRaWAN device messages** section in the [online guide](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-create-destinations.html).

### Set Up the Gateway

- [Set Up the Gateway Hardware](https://docs.rakwireless.com/product-categories/wisgate/rak7394/quickstart/#power-the-gateway)
- [Set Up the Gateway Software](https://docs.rakwireless.com/product-categories/wisgate/rak7394/quickstart/#access-the-gateway)

For additional software references, check the following link:

- [Community forum](https://forum.rakwireless.com/?utm_source=Docs&utm_medium=Docsheader&utm_campaign=RAKDocs)

#### Configure the Gateway Device

1. To connect to AWS IoT Core for LoRaWAN, you need to download and compile **Basics Station**.

Assuming you have successfully accessed the gateway via SSH, it is recommended to update and upgrade the system. This will ensure all packages are up-to-date. Use the following commands:  

```bash
sudo apt update
sudo apt upgrade -y
```

2. To register the gateway in AWS IoT Core for LoRaWAN, you need the device’s EUI. To locate the gateway’s EUI, use the following command to open the graphical user interface (GUI). The EUI will be displayed at the top of the GUI:  

```bash
sudo gateway-config
```

> **Image:** RAK7248 Configuration Options

You can also run the following command:

```
pi@rak-gateway:~ $ sudo gateway-version
Raspberry Pi 4 Model B Rev 1.1, OS "10 (buster)", 5.4.79-v7l+.
RAKwireless gateway RAK7248 no LTE version 4.2.7R install from firmware
Gateway ID: DCA632FFFE366417
```

3. To configure Basics Station, clone the repository and navigate to the downloaded folder using the following commands:  

```bash
git clone https://github.com/lorabasics/basicstation.git
cd basicstation
```

:::tip NOTE
Run the following commands in the **Basics Station** directory.
:::

4. Install all the dependencies by running the following command:

```
make platform=corecell variant=std
```

5. Replace the file `loragw_stts751.c`.

```
sudo cp -f /opt/ttn-gateway/sx1302_hal/libloragw/src/loragw_stts751.c deps/lgw1302/platform-corecell/libloragw/src/loragw_stts751.c
```

6. To build Basics Station, navigate to the directory, clean the build environment, and then run `make` to install all dependencies. Use the following commands:

```
make clean
make platform=corecell variant=std
```

7. After completing the installation, you need to configure the Basics Station protocol. Navigate to the folder containing the examples provided by Semtech, and then enter the **corecell** folder (specific to SX1302 builds):  

```bash
cd examples/corecell
```

8. To successfully start the concentrator, edit the reset_gw.sh script and change the reset pin to **17**.

```
#!/bin/sh

# This script is intended to be used on the SX1302 CoreCell platform, it performs the following actions:
#        - export/unexport GPI023 and GPI018 used to reset the SX1302 chip and to enable the LDOs
#
# Usage examples:
#       ./reset_lgw.sh stop
#       ./reset_lgw.sh start
#
# GPIO mapping has to be adopted with HW
#

SX1302_RESET_PIN=17
SX1302_POWER_EN_PIN=18

WAIT_GPIO() {
    sleep 0.1
}
```

9. To organize the configuration files for Basics Station to connect to AWS IoT Core for LoRaWAN, create a new folder:

```
mkdir lns-aws
```

10. Copy `station.conf` into this folder.

```
cp lns-ttn/station.conf lns-aws/
```

11. Add the certificates that you downloaded earlier to **lns-aws**. (Refer to [Add the LoRaWAN Gateway](#add-the-lorawan-gateway).)

> **Image:** Gateway Certificate

> **Image:** Enter the credentials

12.  All the configurations for the Basics Stations are ready. You should now have the files as follows:

```
pi@rak-gateway:~/basicstation/examples/corecell/lns-aws $ ls -al
total 28
drwxr-xr-x 2 pi pi 4096 Oct 28 17:57 .
drwxr-xr-x 4 pi pi 4096 Oct 28 17:44 ..
-rw-r--r-- 1 pi pi 1225 Oct 28 17:57 cups.crt
-rw-r--r-- 1 pi pi 1680 Oct 28 17:57 cups.key
-rw-r--r-- 1 pi pi 1607 Oct 28 17:57 cups.trust
-rw-r--r-- 1 pi pi   69 Oct 28 17:57 cups.uri
-rw-r--r-- 1 pi pi 2460 Oct 28 17:46 station.conf
```

13. Before you start using the Basics Station, disable the packet forwarder.
Use the command `sudo systemctl edit ttn-gateway.service` to edit the service of the packet forwarder, and add the following codes to the file.

:::tip NOTE
To re-activate the packet forwarder, edit the service file and set the value of **Restart** to **always**.
:::

```
[Unit]
Description=The Things Network Gateway

[Service]
WorkingDirectory=/opt/ttn-gateway/packet_forwarder/lora_pkt_fwd/
ExecStart=/opt/ttn-gateway/packet_forwarder/lora_pkt_fwd/start.sh
SyslogIdentifier=ttn-gateway
Restart=no
RestartSec=5

[Install]
WantedBy=multi-user.target
```

14. To apply the changes made to the unit, execute the following command:

```
sudo systemctl daemon-reload
```

15. Restart the ttn-gateway service to load the new service configuration. The unit file must be restated if you modify the running unit file.

```
sudo systemctl restart ttn-gateway.service
```

16. Find the ttn-gateway process PID and `kill` this process:

```
pi@rak-gateway:~/basicstation/example/corecell/lns-aws $ ps aux | grep ttn-gateway
pi      28165   0.2     0.1     7680        2780    pts/0   S+  18:20   0:00 /bin/bash/opt/ttn-gateway/packet_forwarder/lora_pkt_fwd/start.sh
pi      28236   0.0     0.0     7348         488    pts/1   S+  18:20   0:00 grep --color=auto ttn-gateway
pi@rak-gateway:~/basicstation/example/corecell/lns-aws $ sudo kill 28165
```

17. Now, you can start Basics Station. Exit the configuration folder and start Basics Station.

```
cd ..
./start-station.sh –l lns-aws/
```

> **Image:** Configure the Basics Station

If everything is configured properly, your gateway should be online in the AWS IoT Core for LoRaWAN console:

> **Image:** Connected Status in the LoRaWAN Console

### Add End-Devices

Refer to [RAK4631 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak4631/quickstart/) to enable communication with the gateway.

#### Connect the Device and Verify the Connection Status

Follow the instructions in the [online guide](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-device-connection-status.html) to connect your device to AWS IoT Core for LoRaWAN. To verify the connection status, refer to the instructions in the **Check device connection status using the console** section. You can also check [View format of uplink messages sent from LoRaWAN devices](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-uplink-metadata-format.html).

### Verifying Operation

Once the setup is complete, provisioned OTAA devices can join the network and begin sending messages. These messages will be received by AWS IoT Core for LoRaWAN and routed to the IoT Rules Engine for further processing.

Instructions for a sample *Hello World* application are provided in **Figure 18**, assuming the device has successfully joined the network and is capable of sending uplink traffic.

> **Image:** Send uplink architecture

#### Create a Lambda Function for Destination Rule

Create the lambda function to process device messages processed by the destination rule.

1. Go to the [AWS Lambda console](http://console.aws.amazon.com/lambda).
2. In the navigation pane, click **Functions**, then **Create function**.
3. Select **Author from scratch**.
4. Under **Basic Information**, enter the function name and choose _**Runtime Python 3.8**_. from the drop-down under **Runtime**.
5. Click on **Create function**.
6. Under **Function code**, paste the copied code into the editor under the _**lambda_function.py**_ tab.

```

  import base64 import json import logging import ctypes import boto3

  # define function name FUNCTION_NAME = 'RAK-HelloWorld'
  # Second Byte in Payload represents Data Types
  # Low Power Payload Reference: https://developers.mydevices.com/cayenne/docs/lora/ DATA_TYPES = 1
  # Type Temperature TYPE_TEMP = 0x67
  # setup iot-data client for boto3 client = boto3.client('iot-data') # setup logger
  logger = logging.getLogger(FUNCTION_NAME) logger.setLevel(logging.INFO)

  def decode(event):
  data_base64 = event.get('PayloadData') data_decoded = base64.b64decode(data_base64) result = {
  'devEui': event.get('WirelessMetadata').get('LoRaWAN'
  ).get('DevEui'),
  'fPort': event.get('WirelessMetadata').get('LoRaWAN'
  ).get('FPort'),
  'freq': event.get('WirelessMetadata').get('LoRaWAN'
  ).get('Frequency'),
  'timestamp': event.get('WirelessMetadata').get('LoRaWAN'
  ).get('Timestamp'),
  }

  if data_decoded[DATA_TYPES] == TYPE_TEMP: temp = data_decoded[DATA_TYPES + 1] << 8 \
  | data_decoded[DATA_TYPES + 2] temp = ctypes.c_int16(temp).value result['temperature'] = temp / 10

  return result

  def lambda_handler(event, context): data = decode(event)
  logger.info('Data: %s' % json.dumps(data))
  response = client.publish(topic=event.get('WirelessMetadata'
  ).get('LoRaWAN').get('DevEui')
  + '/project/sensor/decoded', qos=0, payload=json.dumps(data))
  return response

```

7. Once the code has been pasted, choose to **Deploy** to deploy the lambda code.
8. Click on the **Configuration** tab and choose **Permissions** menu of the lambda function.
9. Change the **Lambda Role Policy** permission.
  - Under **Execution role**, click on the hyperlink under **Role name**.
  - On the **Permissions tab**, find the **Policy name** and select it.
  - Choose **Edit policy**, and choose the **JSON** tab.
  - Append the following to the Statement section of the policy to allow publishing to AWS IoT.

```json
{
  "Effect":"Allow",
  "Action":[
    "iot:Publish"
  ],
  "Resource":[
    "*"
  ]
}
```

10.  Choose **Review Policy**, then **Save changes**.
11.  Go back to the Lambda code and create a test event that will allow you to test the functionality of the lambda function.
  - Click **Test** and the **Configure test event** window will pop up.
  - Enter a name for the test event under the **Event name**.
  - Paste the following sample payload in the area under **Event Json**:

```json
    {
    "WirelessDeviceId": "65d128ab-90dd-4668-9556-fe47c589610b",
    "PayloadData": "AWf/1w==",
    "WirelessMetadata": {
    "LoRaWAN": {
    "DataRate": "4",
    "DevEui": "0000000000000088",
    "FPort": 1,
    "Frequency": "868100000",
    "Gateways": [
            {
    "GatewayEui": "80029cffXXXXXXXX",
    "Rssi": -109,
    "Snr": 5
            }
        ],
    "Timestamp": "2021-02-08T04:00:40Z"
        }
    }
    }
```

12. Choose **Create** to save the event.
13. Navigate to the AWS IoT console, choose **Test** on the navigation pane, and select **MQTT client**.
14. Configure the MQTT client to subscribe to "**#**" (all topics).
15. Click **Test** on the Lambda function page to generate the test event you just created.
16. Verify the published data in the AWS IoT Core MQTT Test client:
    - Open another window. Go to **AWS IoT Console**, select **Test** under Subscription Topic, **enter #** and select **Subscribe to topic**.
    - The output should look similar to this:

        ```json
            000000000000000088/project/sensor/decoded      February 09, 2021, 14:45:29 (UTC+0800)
            {
                "devEui": "000000000000000088",
                "fPort": 1,
                "freq": "868100000",
                "timestamp": "2021-02-08T04:00:40Z",
                "temperature": -4.1
            }
        ```

#### Create the Destination Rule

In this section, you create the IoT rule that forwards the device payload to your application. This rule is associated with the destination created earlier in the [Set up a Destination for Device Traffic](#set-up-a-destination-for-device-traffic) section.

1. Navigate to the [AWS IoT console](http://console.aws.amazon.com/iot).
2. In the navigation pane, choose **Act**, then select **Rules**.
3. On the Rules page, choose **Create**.
4. On the Create a rule page, enter as follows:
      - Name: **LoRaWANRouting**
      - Description: **Any description of your choice**.

    :::tip NOTE
    The **Name of your Rule** is the information needed when you provision devices to run on AWS IoT Core for LoRaWAN.
    :::

5. Leave the default Rule query statement **'SELECT * FROM 'iot/topic'** unchanged. This query has no effect at this time, as traffic is currently forwarded to the rules engine based on the destination.
6. Under **Set one or more actions**, choose **Add action**.
7. On the Select an action page, choose **Republish a message to an AWS IoT topic**. Scroll down, and choose **Configure action**.
8. On the Configure action page, for Topic, enter **_project/sensor/decoded_**. The AWS IoT Rules Engine will forward messages to this topic.
9. Under **Choose or create a role to grant AWS IoT access to perform this action**, select **Create Role**.
10. For Name, enter a name of your choice.
11. Choose **Create role** to complete the role creation. You will see a **Policy Attached** tag next to the role name, indicating that the Rules Engine has been permitted to execute the action.
12. Choose **Add action**.
13. Add one more action to invoke the Lambda function. Under **Set one or more actions**, choose **Add action**.
14. Choose **Send a message to a Lambda function**.
15. Choose **Configure action**.
16. Select the Lambda function created earlier, and choose **Add action**.
17. Then, choose **Create rule**.
18. A **Success** message will be displayed at the top of the panel, and the destination has a rule-bound to it.

You can now check that the decoded data is received and republished by AWS by triggering a condition or event on the device itself.

- Go to the AWS IoT console. In the navigation pane, select **Test**, and choose **MQTT test client**.
- Subscribe to the wildcard topic **#** to receive messages from all topics.
- Wait for an uplink from the end device.
- You should see the traffic similar as shown below:

    ```json
        393331375d387505/project/sensor/decoded           February 09, 2021, 14:47:21 (UTC+0800)
        {
        "devEui": "393331375d387505",
        "fPort": 1,
        "freq": "867100000",
        "timestamp": "2021-02-09T06:47:20Z",
        "temperature": 27.2
        }
    ```

    ```json
    project/sensor/decoded    February 09, 2021, 14:47:21 (UTC+0800)
        {
            "WirelessDeviceID": "6477ec22-9570-31d5981da021",
            "PayloadData": "AWcBEA==",
            "WirelessMetadata": {
                "LoRaWAN": {
                    "DataRate": "4",
                    "DevEui": "393331375d387505",
                    "FPort": 1,
                    "Frequency": "867100000",
                    "Gateways": [
                        {
                            "GatewayEui": "ac1ff09fffe014bd5",
                            "Rssi": -103,
                            "Snr": 8.5
                        }
                    ],
                    "Timestamp": "2021-02-09T06:47:20Z"
                }
            }
        }
    ```

#### Configuring Amazon SNS

You will be using the Amazon Simple Notification Service to send text messages (SMS) when certain conditions are met.

1. Go to the [Amazon SNS console](http://console.aws.amazon.com/sns).
2. Click on the menu to open the navigation pane.
3. Select **Text Messaging** (SMS) and choose **Publish text message**.
4. Under the Message type, select **Promotional**.
5. Enter your phone number (phone number that will receive text alerts).
6. Enter **Test message** for the Message and choose **Publish** message.
7. If the phone number you entered is valid, you will receive a text message and your phone number will be confirmed.
8. Create an Amazon SNS Topic as follows:
      - In the navigation pane, choose **Topics**.
      - Select **Create topic**.
      - Under Details, select **Standard**.
      - Enter a name of your choice. Here, you will use "**_text_topic_**".
      - Choose **Create topic**.
9. Create a subscription for this topic:
      - On the page for the newly created text_topic, choose the **Subscriptions** tab.
      - Choose **Create subscription**.
      - Select **Protocol** as SMS from the drop-down.
      - Under Endpoint, enter the previously validated phone number to receive the SMS alerts.
      - Choose **Create subscription**. You should see a "_**Subscription to text_topic created successfully**_" message.

##### Add a Rule for Amazon SNS Notification

Now, add a new rule to send an Amazon SNS notification when certain conditions are met in a decoded message.

1. Navigate to the [AWS IoT console](http://console.aws.amazon.com/iot).
2. In the navigation pane, choose **Act**, then **Rules**.
3. On the Rules page, choose **Create**.
4. Enter the Name as _text_alert_ and provide an appropriate **Description**.
5. Under the **Rule query statement**, enter the following query:

  ```sql
      SELECT devEui as device_id, "Temperature exceeded 25" as message, temperature as temp, timestamp as time FROM '+/project/sensor/decoded' where temperature > 25
  ```

6. Choose **Add action**.
7. Choose **Send a message as an SNS push notification**.
8. Choose **Configure action**.
9. Under SNS target, select _text_topic_ from the drop-down.
10. Select **RAW** under **Message format**.
11. Under **Choose or create a role to grant AWS IoT access to perform this action**, choose **Create role**.
12. Enter a name for the role, and choose **Add action**.
13. Select **Create rule**.  You should see a **Success** message, indicating that the rule has been created.

##### Test the Rule for Amazon SNS Notification

After adding the rule for Amazon SNS notification, you should receive a text message when hitting the event.

Send message from end-device using AT command: `at+send:lora:1:01670110`. Here is the message from mobile after sending an uplink message:

```json
    {
        "device_id": "393331375d387505",
        "message": "Temperature exceeded 25",
        "temp": 27.2,
        "time": "2021-02-22T07:58:54Z"
    }
```

### Send Downlink Payload

This section shows how to send a downlink payload from AWS IoT LoRaWAN Server to the end device.

##### Install the AWS SAM CLI

Follow the instruction in the [online guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) to install the [AWS SAM CLI.

##### Deploy the SAM Template to AWS

Follow the instruction in the Deploy [SAM template to AWS](https://github.com/aws-samples/aws-iot-core-lorawan/tree/main/send_downlink_payload) GitHub.

##### Send Payload to End-Device

1. Send Payload to End-device.
    - Go to the AWS IoT console.
    - In the navigation pane, select **Test**, and choose **MQTT test client**.
    - Subscribe to the wildcard topic **#** to receive messages from all topics.
    - Specify the topic to `cmd/downlink/{WirelessDeviceId}` and a base64-encoded message.

> **Image:** Specifying a topic

2. You should see traffic on AWS similar to what is shown below:

    ```json
        downlink/status/6477ec22-9570-4fea-9668-31d5981da021   February 09, 2021, 15:09:29 (UTC+0800)
        {
            "sendresult": {
                "status": 200,
                "RequestId": "4f1d36e1-8316-4436-8e9d-2207e3711755",
                "MessageId": "60223529-0011d9f5-0095-0008",
                "ParameterTrace": {
                    "PayloadDate": "QQ==",
                    "WirelessDeviceId": "6477ec22-9570-4fea-9668-31d5981da021",
                    "Fport": 1,
                    "TransmitMode": 1
                }
            }
        }
    ```

> **Image:** Traffic on AWS

3. You should see traffic on your console of the end device similar to what is shown below:

```
SYSLOG:4:LoRa rX : 41 - 14
SYSLOG:4:LoRa Tx :
```

##### IoT Analytics

You will use IoT Analytics to visually display data via graphs if there is a need in the future to do further analysis.

###### Create an IoT Analytics Rule

** Create a Rule First **

1. Navigate to the [AWS IoT console](http://console.aws.amazon.com/iot).
2. In the navigation pane, choose **Act** and then, choose **Rules**.
3. On the Rules page, choose **Create**.
4. Enter the Name as **Visualize** and provide an appropriate **Description**.
5. Under the Rule query statement, enter the following query:

    ```sql
    SELECT * FROM 'project/sensor/decoded'
    ```

6. Choose **Add action**.
7. Select **Send a message to IoT Analytics**.
8. Choose **Configure Action**.
9. Choose **Quick Create IoT Analytics Resources**.
10. Under **Resource Prefix**, enter an appropriate prefix for your resources, such as _LoRa Choose Quick Create_.
11. Once the Quick Create Finished message is displayed, choose **Add action**.
12. Choose **Create rule**. You should see a Success message, indicating that the rule has been created.

###### Configure AWS IoT Analytics

** Set Up AWS IoT Analytics **

1. Go to the [AWS IoT Analytics console](http://console.aws.amazon.com/iotanalytics).
2. In the navigation panel, choose **Data sets**.
3. Select the data set generated by the Quick Create in [**Create an IoT Analytics Rule**](#create-an-iot-analytics-rule).
4. In the Details section, edit the **SQL query**.
5. Replace the query with as follows:

    ```sql
    SELECT devEui as device_id, temperature as temp, timestamp as time FROM LoRa_datastore
    ```

6. Under Schedule, choose **Add schedule**.
7. Under Frequency, choose **Every 1 minute**, and then click **Save**.

###### Configure Amazon QuickSight

Amazon QuickSight lets you easily create and publish interactive BI dashboards that include Machine Learning-powered insights.

1. Go to [AWS Management console](http://console.aws.amazon.com/).
2. From the management console, enter **QuickSight** in the "_Search for services, features.._" search box.
3. Click **QuickSight** in the search results.
4. If you haven't signed up for the service before, go ahead and sign up, as there is a free trial period.
5. Select the **Standard Edition**, and choose **Continue**.
6. Enter a unique name in the field **QuickSight account name**.
7. Fill in the **Notification email address**.
8. Review the other checkbox options and change them as necessary. The **AWS IoT Analytics** option must be selected.
9. Choose **Finish**. You will see a confirmation message.
10. Choose **Go to Amazon QuickSight**.
11. Select **Datasets**.
12. Select **New dataset**.
13. Select **AWS IoT Analytics**.
14. Under Select an AWS IoT Analytics data set to import, choose the data set created in [Create an IoT Analytics Rule](#create-an-iot-analytics-rule).
15. Choose **Create data source**, and then choose **Visualize**.
16. Select the dataset created, then select **Refresh** or **Schedule Refresh** for a periodic refresh of the dataset.

### Testing Your "Hello Word" Application

Using your device, create a condition to generate an event such as a high-temperature condition. If the temperature is above the configured threshold, then you will receive a text alert on your phone. This alert will include key parameters about the alert.

#### Testing Your "Hello World" Application

Using your device, create a condition to generate an event such as a high-temperature condition. If the temperature is above the configured threshold, then you will receive a text alert on your phone. This alert will include key parameters about the alert.

You can also visualize the data set as follows:

1. Go to the [AWS IoT Analytics console](http://console.aws.amazon.com/iotanalytics).
2. Choose **Data sets**.
3. Select the dataset created earlier.
4. Select **Content** and ensure there are at least a few uplink entries available in the data set.
5. Go to the [QuickSight console](http://quicksight.aws.amazon.com/).
6. Choose **New analysis**.
7. Choose the dataset created in [Create an IoT Analytics Rule](#create-an-iot-analytics-rule).
8. To see a chart of your dataset, select the following values:
    - **Time** on the X-axis
    - **Value** as temp (Average)
    - **Color** as device_id

### Debugging

If you experience any issues, you can check the logs located in the `/var/log/` directory.

### Troubleshooting

Unable to see the web login:
  - Check that your wifi is connected to **RAK7Wireless_XXXX**.
  - Try ping **192.168.230.1**.

