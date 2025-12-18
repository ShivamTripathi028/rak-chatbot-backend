---
slug: /product-categories/wisgate/rak7240v2/lorawan-network-server-guide/
title: RAK7240V2/RAK7240CV2 WisGate Edge Prime Guide
description: A comprehensive guide for setting up both your RAK7240 V2 and Amazon Web Services account and permissions. It also includes instructions on connecting and configuring your LoRaWAN Gateway to The Things Network and LORIOT.
image: "https://images.docs.rakwireless.com/wisgate/rak7240-v2/rak7240v2.png"
keywords:
    - WisGate Edge Prime
    - LoRaWAN Network Server Guide
    - LoRaWAN Gateway
    - Outdoor Gateway
    - LoRaWAN Gateway setup
sidebar_label: LNS Guide
---

# RAK7240V2/RAK7240CV2 WisGate Edge Prime LoRaWAN Network Server Guide

This manual provides you with operation guidance for connecting the gateway to different LoRaWAN network servers.

## Built-In Network Server

This section is an example demonstration on how to interconnect your RAK commercial gateway with its built-in LoRa network server and make an application for the node.

### Requirements

- Your node module (In this section, RAK3172 will be used as an example module)
- Your RAK gateway is connected to the Internet

### Set the Gateway Work Mode

1. Configure **Work mode** to **Built-in network server**. Navigate to **LoRa** > **Configuration**. For **Work mode**, select **Built-in network server**.

> **Image:** Set the gateway work mode

2. Select the log level and frequency band.

> **Image:** Configure log level and frequency band

:::tip NOTE
You can expand the **View detailed regional parameters of the frequency plan** option to configure detailed regional parameters.
:::

### Create an Application

1. Navigate to **LoRa** > **Applications** tab.
2. Click the **Add application** button or the **add one now** link to add a new application.

> **Image:** Add an application

3. After the page jumps, configure the following information.

> **Image:** Set parameters

+ **Application name**: Name of the application
+ **Application description**: Description of the application, optional
+ **Application Type**
  + **Unified Application key**: All devices will use the same application key. Selecting this option, then the application key field will pop up, where you can type in an application key or click the **Autogenerate** button to generate a key. This value needs to be consistent with the value from the end device, so either obtain it by querying the end device, or auto-generate it and synchronously change the corresponding value of the device.

    
> **Image:** Configure unified application key

    After enabling the **Auto Add Device** option, configure the **Application EUI** option. This value needs to be consistent with the value from the end device, so either obtain it by querying the end device, or auto-generate it and synchronously change the corresponding value of the device. After the application EUI and key verification, the device will be automatically added to the application.

    
> **Image:** Enable auto add device

  - **Separate Application keys**: Each device has its own application key. Add the key when registering the device.

4. Click **Save Application** to add the new application.

### Add End Devices

1. Navigate to **LoRa > Applications** tab.

> **Image:** Application list

2. In the application list, click the newly created application and choose the **End devices** tab.

:::tip NOTE
If you have enabled **Auto Add Device**, the device will be automatically registered with the adding request. Otherwise, refer to the next step.
:::

> **Image:** Device list

3. Click the **Add end device** button.
4. In the **End device information** interface, enter the following information.

> **Image:** Add new device

- **Activation Mode**: OTAA or ABP. This value needs to be consistent with the value from the end device. The ABP mode will pop up two additional fields, **Application Session Key** and **Network Session Key**.
- **End device (group) name**: Name of the end device (group).
- **End device description (optional)**: A description of the end device, optional.
- **Class**: This value needs to be consistent with the value from the end device.
- **Frame Counter Width**: Keep the default value.

5. Click **Add end devices** to enter the device adding page.
6. In the **Adding end devices** interface, enter the device EUI in the **End Device EUI (main)** field and click the **Add to End Devices list** button.

> **Image:** Add new device to End Devices list

:::tip NOTE

+ The device EUI needs to be consistent with the end device EUI.
+ If the EUI is correct, the device will appear in the “End devices list”.
+ If the EUI is duplicate, the device will be displayed in the “End devices with an error”.

:::

7. Click **Add end devices** to add the device to the application. Execute join request on the node side.

> **Image:** Device online

By following the steps in the previous sections, you should now have your device registered. If you click on the **Device EUI**, you will go to the corresponding **Configuration** tab. Click the **Packet capture** button. Here you can monitor the data that the application is exchanging in real time.

> **Image:** End Device Packet Capture

## AWS IoT Core for LoRaWAN

Execute the following steps to set up your AWS account and permissions:

### Set up Roles and Policies in IAM

#### Add an IAM Role for CUPS Server

Adding an IAM role will allow the Configuration and Update Server (CUPS) to handle the wireless gateway credentials.

This procedure needs to be done only once, but must be performed before a LoRaWAN gateway tries to connect with AWS IoT Core for LoRaWAN.

1. Go to the <a href="https://console.aws.amazon.com/iam/home#/roles" target="_blank">IAM Roles</a> page on the IAM console.
2. Choose **Create role**.
3. On the Create Role page, choose **AWS account** > **Another AWS account**.
4. Enter your **Account ID**, then select **Next**.
5. In the search box next to the filter policies, type ***AWSIoTWirelessGatewayCertManager***.
   - If the search results show the policy named ***AWSIoTWirelessGatewayCertManager***, select it by clicking the checkbox.
   - If the policy does not exist, create one.
     - Go to the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html" target="_blank">IAM Policies</a> page. Choose **Create Policy**, then select the **JSON** tab to open the policy editor.
     - Replace the existing template with a trust policy document.

     ```json
     {
     "Version": "2012-10-17",
     "Statement": [
     {
     "Sid": "IoTWirelessGatewayCertManager",
     "Effect": "Allow",
     "Action": [
     "iot:CreateKeysAndCertificate",
     "iot:DescribeCertificate",
     "iot:ListCertificates",
     "iot:RegisterCertificate"
              ],
     "Resource": "*"
               }
           ]
     }
     ```

      - Click **Next**.
      - On the Review and create page. For the **Name**, type **_AWSIoTWirelessGatewayCertManager_**.

      :::tip NOTE
      You must enter the name as **_AWSIoTWirelessGatewayCertManager_** and must not use a different name. This is for consistency with future releases.
      :::

      - For the **Description**, enter a description of your choice.
      - Then choose **Create policy**. You will see a confirmation message showing the policy has been created.

6. Click **Next**.
7. In **Role** name, enter **_IoTWirelessGatewayCertManagerRole_**, and then choose to **Create role**.

:::tip NOTE
You must not use a different name.  This is for consistency with future releases.
:::

8. In the confirmation message, choose ***IoTWirelessGatewayCertManagerRole*** to edit the new role.
9. In the **Summary**, choose the **Trust relationships** tab, and then choose **Edit trust relationship**.
10. In the **Policy Document**, change the **Principal** property to represent the IoT Wireless service:

```json
"Principal": {
"Service": "iotwireless.amazonaws.com"
},
```

- After changing the Principal property, the complete policy document should look like the following:

```json
{
"Version": "2012-10-17",
"Statement": [
    {
"Effect": "Allow",
"Principal": {
"Service": "iotwireless.amazonaws.com"
        },
"Action": "sts:AssumeRole",
"Condition": {}
    }
    ]
}
```

11.  Choose **Update Trust Policy** to save your changes and exit. At this point, you have created the ***IoTWirelessGatewayCertManagerRole*** and you won't need to do this again.

:::tip NOTE
The examples in this document are intended only for dev environments. All devices in your fleet must have credentials with privileges that authorize only intended actions on specific resources. The specific permission policies can vary for your use case. Identify the permission policies that best meet your business and security requirements. For more information, refer to <a href="https://docs.aws.amazon.com/iot/latest/developerguide/example-iot-policies.html">**Example Policies**</a> and <a href="https://docs.aws.amazon.com/iot/latest/developerguide/security-best-practices.html">**Security Best Practices**</a>.
:::

#### Add IAM Role for Destination to AWS IoT Core for LoRaWAN

** Creating a Policy **

Creating a policy gives the role permissions to describe the IoT endpoint and publish messages to AWS IoT.

1. Go to the <a href="http://console.aws.amazon.com/iam" target="_blank">IAM console</a>.
2. Choose **Policies** from the navigation pane.
3. Choose **Create Policy**, then choose the **JSON** tab to open the policy editor. Replace the existing template with this trust policy document:

```json
{
"Version": "2012-10-17",
"Statement": [
   {
"Effect": "Allow",
"Action":
[
"iot:DescribeEndpoint",
"iot:Publish"
],
"Resource": "*"
   }
   ]
}
```

4. Click **Next**.
5. On the Review and create page. For the **Name**, enter a name of your choice.
6. For **Description**, enter a description of your choice.
7. Choose **Create policy**. You will see a confirmation message indicating that the policy has been created.

** Creating the Role **

1. In the <a href="http://console.aws.amazon.com/iam" target="_blank">IAM console</a>, choose **Roles** from the navigation pane to open the Roles page.
2. Choose **Create Role**.
3. On the Create Role page, choose **AWS account** > **Another AWS account**.
4. Enter your **Account ID**, then select **Next**.
5. Search for the IAM policy you just created by entering the policy name in the search bar.
6. In the search results, select the checkbox corresponding to the policy.
7. Click **Next**.
8. For **Role name**, enter an appropriate name of your choice.
9. For **Description**, enter a description of your choice.
10. Choose **Create role**. You will see a confirmation message indicating that your role has been created.

** Updating your Trust Policy**

Update your role's trust relationship to grant AWS IoT Core for LoRaWAN permission to assume this IAM role when delivering messages from devices to your account.

1. In the <a href="http://console.aws.amazon.com/iam" target="_blank">IAM console</a>, choose **Roles** from the navigation pane to open the Roles page.
2. Enter the name of the role you created earlier in the search window, and click on the role name in the search results. This opens up the **Summary** page.
3. Choose the **Trust relationships** tab to navigate to the Trust relationships page.
4. Click **Edit trust policy**. The principal AWS role in your trust policy document defaults to root and must be changed. Replace the existing policy with this:

```json
{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "",
"Effect": "Allow",
"Principal": {
"Service": "iotwireless.amazonaws.com"
},
"Action": "sts:AssumeRole",
"Condition": {}
   }
   ]
}
```
5. Choose **Update Policy**.

### Add the Gateway to AWS IoT

#### Requirements

To complete setting up your gateway, you need the following:

- **LoRaWAN region**. For example, if the gateway is deployed in a US region, the gateway must support LoRaWAN region US915.
- **Gateway LNS-protocols**. Currently, the LoRa Basics Station protocol is supported.
- **Gateway ID (GatewayEUI)** or **serial number**. This is used to establish the connection between the LNS and the gateway. Consult the documentation for your gateway to locate this value.
- **Add minimum software versions** required, including Basics Station 2.0.5.

#### Add the LoRaWAN Gateway

To register the gateway with AWS IoT Core for LoRaWAN, execute these steps:

1. Go to the <a href="http://console.aws.amazon.com/iot" target="_blank">AWS IoT console</a>.
2. Select **LPWAN devices** in the navigation panel on the left.
3. Choose **Gateways**, and then click **Add gateway**.
4. In the **Add gateway** section, fill in the **Gateway's EUI** and **Frequency band (RF Region)** fields.
5. Enter a descriptive name in the **Name**: optional field. It is recommended that you use the GatewayEUI as the name.
6. Click **Add gateway**.
7. On the **Configure your gateway** page, find the section titled **Gateway certificate**.
8. Select **Create certificate**.
9. Once the **Certificate created and associated with your gateway** message is shown, select **Download certificate files** to download the certificate (*xxxxx.cert.pem*) and private key (*xxxxxx.private.key*).
10. In the section **Provisioning credentials**, choose **Download server trust certificates** to download the **CUPS (cups.trust)** and **LNS (lns.trust)** server trust certificates.
11. Copy the CUPS and LNS endpoints and save them in a `.txt` file for use while configuring the gateway.
12. Choose **Submit** to add the gateway.

### Set Up the Gateway

1. Using your preferred Web browser, access the gateway. To access the gateway, see the <a href="https://docs.rakwireless.com/product-categories/wisgate/rak7240v2/quickstart/" target="_blank">Quick Start Guide</a>.

> **Image:** Web User Interface Log-in

2. Configure **Network Mode** to **Basics Station**. Navigate to **LoRa**.
3. For **Work mode**, select **Basics station** and click **Configure Basics Station server setup** to expand the Basics Station settings.

> **Image:** Basics Station Work Mode

4. Select **LNS Server** from Server, then choose **TLS Server and Client Authentication** from Authentication Mode.

> **Image:** Configuring Network Mode to Basics Station

5. Configure URI, Port, and Authentication Mode.

> **Image:** Configuring URI, Port, and Authentication Mode

6. Click **Save**. Check if the gateway is online in AWS IoT console.

> **Image:** Verifying Operation

### Add a LoRaWAN Device to AWS IoT

In this section we use RAK4200 as an example device.

#### Requirements

- Locate and note the following specifications about your endpoint device.
    - **LoRaWAN Region**: This must match the gateway LoRaWAN region.
    - **MAC Version**: This must be one of the following:
        + V1.0.2
        + v1.0.3
        + v1.0.4
        + v1.1
    - OTAA v1.0.x and OTAA v1.1 are supported.
    - ABP v1.0.x and ABP v1.1 are supported.
- Locate and note the following information from your device manufacturer:
    - For OTAA v1.0x devices: **DevEUI**, **AppKey**, **AppEUI**
    - For OTAA v1.1 devices: **DevEUI**, **AppKey**, **NwkKey**, **JoinEUI**
    - For ABP v1.0x devices: **DevEUI**, **DevAddr**, **NwkSkey**, **AppSkey**
    - For ABP v1.1 devices: **DevEUI**, **DevAddr**, **NwkSEnckey**, **FNwkSIntKey**, **SNwkSIntKey**, **AppSKey**

#### Verify Profiles

AWS IoT Core for LoRaWAN supports device profiles and service profiles. Device profiles contain the communication and protocol parameter values the device needs to communicate with the network server. Service profiles describe the communication parameters the device needs to communicate with the application server.

Some pre-defined profiles are available for device and service profiles. Before proceeding, verify that these profile settings match the devices you will be setting up to work with AWS IoT Core for LoRaWAN.

1. Navigate to the <a href="http://console.aws.amazon.com/iot" target="_blank">AWS IoT console</a>. In the navigation pane, choose **LPWAN devices**, then click **Profiles**.
2. In the **Device Profiles** section, there are some pre-defined profiles listed.
3. Check each of the profiles to determine if one of them will work for you. If not, select **Add device profile** and set up the parameters as needed. For US915 as an example:

> **Image:** Adding the Device Profile

4. Click **Add device profile** once you have set a device profile that will work for you.
5. In the **Service Profiles** section, click **Add service profile** and set up the parameters as needed. As an example, the default service profile parameters are shown below. However, only the ***Add gateway meta data*** setting can be changed at this time.

> **Image:** Adding the Service Profile

6. Proceed only if you have a device and service profile that will work for you.

#### Set Up a Destination for Device Traffic

Because most LoRaWAN devices don't send data to AWS IoT Core for LoRaWAN in a format that can be consumed by AWS services, traffic must first be sent to a Destination. A Destination represents the AWS IoT rule that processes a device's data for use by AWS services. This AWS IoT rule contains the SQL statement that selects the device's data and the topic rule actions that send the result of the SQL statement to the services that will use it.

For more information on Destinations, refer to the AWS <a href="https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html" target="_blank">LoRaWAN Developer Guide</a>.

A destination consists of a Rule and a Role. To set up the destination, execute the following steps:

1. Navigate to the <a href="http://console.aws.amazon.com/iot" target="_blank">AWS IoT console</a>. In the navigation pane, choose **LPWAN devices**, and then **Destinations**.
2. Choose **Add Destination**.
3. For the **Destination name**, enter **_ProcessLoRa_**, and then add an appropriate description under **Destination description – optional**.

:::tip NOTE
The Destination name can be anything. For getting started and consistency, choose **ProcessLoRa** for the first integration with AWS IoT Core for LoRaWAN.
:::

4. For **Rule name**, enter **_LoRaWANRouting_**. Ignore the section **Rules configuration – Optional** for now.  The Rule will be set up later in the "Hello World" sample application. See Create the IoT Rule for the destination.
5. In the **Permissions** section, choose **Select an existing service role** and select the IAM role you had created earlier, from the drop-down.

> **Image:** Adding Destination

6. Choose **Add Destination**.  You will see a message **_Destination added_**, indicating the destination has been successfully added.

#### Register the Device

Now, register an endpoint device with AWS IoT Core for LoRaWAN as follows. Before adding a device to AWS IoT, retrieve the **DevEUI**, **AppEUI**, and **AppKey** from the end Device's console. You can use AT command `at+get_config=lora:status` to obtain the information.

For more AT commands, refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4200-breakout-board/at-command-manual/" target="_blank">RAK4200 AT Command Manual</a>.

```
at+get_config=lora:status\r\n
OK Work Mode: LoRaWAN
Region: EU868
Send_interval: 600s
Auto send status: false.
MulticastEnable: true.
Multi_Dev_Addr: 260XXXXX
Multi_Apps_Key: F13DDFA2619B10411F02XXXXXXXXXXXX
Multi_Nwks_Key: 1D1991F5377C675879C3XXXXXXXXXXXX
Join_mode: OTAA
DevEui: 70B3XXXXXXXXXXXX
AppEui: F573D2XXXXXXXXXX
AppKey: 70B3DXXXXXXXXXXXXXXXXXXXXXXXXXXX
Class: C
Joined Network:false
IsConfirm: unconfirm
AdrEnable: true
EnableRepeaterSupport: false
RX2_CHANNEL_FREQUENCY: 869525000, RX2_CHANNEL_DR:0
RX_WINDOW_DURATION: 3000ms
RECEIVE_DELAY_1: 1000ms
RECEIVE_DELAY_2: 2000ms
JOIN_ACCEPT_DELAY_1: 5000ms
JOIN_ACCEPT_DELAY_2: 6000ms
Current Datarate: 4
Primeval Datarate: 4
ChannelsTxPower: 0
UpLinkCounter: 0
DownLinkCounter: 0

```
1. Go to the <a href="http://console.aws.amazon.com/iot" target="_blank">AWS IoT console</a>.
2. Select **LPWAN devices** in the navigation panel on the left.
3. Select **Devices**, then choose **Add wireless device**.
4. On the **Add device** page, select the LoRaWAN specification version in the drop-down under **Wireless device specification**.
5. Under **LoRaWAN specification and wireless device configuration**, enter the **DevEUI**.
6. Enter the remaining fields as per the OTAA/ABP choice you made above.
7. Enter a name for your device in the **Wireless device name – optional field**.
8. In the **Profiles** section, under **Wireless device profile**, from the drop-down option find the device profile you have created or the one that corresponds to your device and region.

:::tip NOTE
Compare your device details to ensure the device profile is correct. If there are no valid default options, you will have to create a new profile. See the [Verify Profiles](#verify-profiles) section.
:::

9. Choose the destination you created earlier (_ProcessLoRa_) from the drop-down under **Choose destination**.

> **Image:** LoRaWAN specifications and wireless device configuration

10. Click **Next**.
11. Choose **Add device**. You will see a message saying "*Wireless device added*", indicating that your device has been set up successfully.
12. Restart the end device, and it should join the AWS IoT LoRaWAN server.

```
EVENT:0:STARTUP
SYSLOG:4:OTAA Join Request
SYSLOG:4:OTAA Join Success
EVENT:1:JOIN_NETWORK
SYSLOG:4:LoRa Tx :
```

> **Image:** Joined Device

### Verifying Operation

Once setup is completed, provisioned OTAA devices can join the network and start to send messages. Messages from devices can then be received by AWS IoT Core for LoRaWAN and forwarded to the IoT Rules Engine.

Instructions for a sample Hello World application are given below, assuming that the device has joined and is capable of sending uplink traffic.

> **Image:** Sending Uplink Architecture

#### Create a Lambda Function for Destination Rule

Create the lambda function to process device messages processed by the destination rule.

1. Go to the <a href="http://console.aws.amazon.com/lambda" target="_blank">AWS Lambda console</a>.
2. Select **Functions** in the navigation pane.
3. Choose **Create function**.
4. Select **Author** from scratch.
5. Under **Basic Information**, enter the function name and choose **_Runtime Python 3.8_**. from the drop-down under **Runtime**.
6. Click **Create function**.
7. Under **Code source**, paste the copied code into the editor under the **_lambda_function.py_** tab.

<details>
<summary> Click to view the code</summary>

```python
import base64
import json
import logging
import ctypes
import boto3

# define function name

FUNCTION_NAME = 'RAK-HelloWorld'

# Second Byte in Payload represents Data Types
# Low Power Payload Reference: https://developers.mydevices.com/cayenne/docs/lora/

DATA_TYPES = 1

# Type Temperature

TYPE_TEMP = 0x67

# setup iot-data client for boto3

client = boto3.client('iot-data')

# setup logger

logger = logging.getLogger(FUNCTION_NAME)
logger.setLevel(logging.INFO)

def decode(event):
    data_base64 = event.get('PayloadData')
    data_decoded = base64.b64decode(data_base64)
    result = {
        'devEui': event.get('WirelessMetadata').get('LoRaWAN'
                ).get('DevEui'),
        'fPort': event.get('WirelessMetadata').get('LoRaWAN'
                ).get('FPort'),
        'freq': event.get('WirelessMetadata').get('LoRaWAN'
                ).get('Frequency'),
        'timestamp': event.get('WirelessMetadata').get('LoRaWAN'
                ).get('Timestamp'),
        }

    if data_decoded[DATA_TYPES] == TYPE_TEMP:
        temp = data_decoded[DATA_TYPES + 1] << 8 \
            | data_decoded[DATA_TYPES + 2]
        temp = ctypes.c_int16(temp).value
        result['temperature'] = temp / 10

    return result

def lambda_handler(event, context):
    data = decode(event)
    logger.info('Data: %s' % json.dumps(data))
    response = client.publish(topic=event.get('WirelessMetadata'
                              ).get('LoRaWAN').get('DevEui')
                              + '/project/sensor/decoded', qos=0,
                              payload=json.dumps(data))
    return response

```
</details>

8. Once the code has been pasted, choose **Deploy** to deploy the lambda code.
9. Click the **Configuration** tab of the lambda function and select **Permissions**.
10. Change the **Lambda Role Policy** permission.
    -  Under **Execution role**, click the hyperlink under **Role name**.
    -  On the **Permissions** tab, find the policy name and select it.
    -  Choose **Edit policy**, and choose the **JSON** tab.
    -  Append the following to the **Statement** section of the policy to allow publishing to AWS IoT.

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

    - After the change, the code should look like this:

    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
            "Effect":"Allow",
            "Action":[
                 "iot:Publish"
            ],
             "Resource":[
              "*"
             ]
            }
        ]
    }
    ```

    -  Choose **Review Policy**, then Save changes.

11. Go back to the Lambda function **Code source** and create a test event that will allow you to test the functionality of the lambda function.
    + Click **Test** next to **Deploy**.
    + In the **Configure test event**, enter a name for the test event in the **Event name** field.
    + Paste the following sample payload in the area under **Event JSON** field:

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

12.	Choose **Save** to save the event.
13. In a new window, navigate to the AWS IoT console, choose **Test** on the navigation pane, and select **MQTT test client**.
14. In **Subscription topic** field type **#** (all topics) and click **Subscribe to topic**. The MQTT will subscribe to all topics.
15. Click on **Test** in the Lambda function page to generate the test event you just created.
16. Verify the published data in the AWS IoT Core MQTT Test client. The output should look similar to this:

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

In this section, create the IoT rule that forwards the device payload to your application.  This rule is associated with the destination created earlier in **Set up a Destination for Device Traffic** section.

1. Navigate to the <a href="http://console.aws.amazon.com/iot" target="_blank">AWS IoT console</a>.
2. In the navigation pane, choose **Message routing**, then select **Rules**.
3. On the Rules page, choose **Create rule**.
4. On the Create a rule page, enter as follows:
      - Name: **LoRaWANRouting**
      - Description: **Any description of your choice**.

    :::tip NOTE
    The **Name of your Rule** is the information needed when you provision devices to run on AWS IoT Core for LoRaWAN.
    :::

5. Click **Next**.
6. Leave the default Rule query statement: '**SELECT * FROM 'iot/topic**' unchanged. This query has no effect at this time, as traffic is currently forwarded to the rules engine based on the destination. Click **Next**.
7. On the **Attach rule actions** page, choose **Republish to AWS IoT topic**.
8. For Topic, enter ***project/sensor/decoded***. The AWS IoT Rules Engine will forward messages to this topic.
9. Under **IAM role**, select **Create new role**.
10. For **Name**, enter a name of your choice. Click **Create**.
11. Add one more action to invoke the Lambda function. Choose **Add rule action**.
12. Choose **Lambda**.
13. Select the Lambda function created earlier and choose **Next**.
14. Then choose **Create**.
15. A "**Success**" message will be displayed at the top of the panel, and the destination has a rule bound to it.

You can now check that the decoded data is received and republished by AWS by triggering a condition or event on the device itself.

- Go to the AWS IoT console. In the navigation pane, select **Test**, and choose **MQTT client**.
- Subscribe to the wildcard topic '**#**' to receive messages from all topics.
- Send message from endDevice using AT command: `at+send:lora:1:01670110`.
- You should see traffic similar to that shown below.

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
       "WirelessDeviceID": "3eff83dd-9159-XXXX-XXXX-XXXXXXXXXXXX",
       "PayloadData": "AWcBEA==",
       "WirelessMetadata": {
           "LoRaWAN": {
               "DataRate": "4",
               "DevEui": "3933XXXXXXXXXXXX ",
               "FPort": 1,
               "Frequency": "867100000",
               "Gateways": [
                  {
                       "GatewayEui": "ac1ff09ffXXXXXXXX",
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

1. Go to the <a href="http://console.aws.amazon.com/sns" target="_blank">Amazon SNS console</a>.
2. Select **Text Messaging** (SMS) and choose **Publish text message**.
3. Under **Message type**, select **Promotional**.
4. Enter your phone number (phone number that will receive text alerts).
5. Enter "*Test message*" for the **Message** and choose **Publish** message.
6. If the phone number you entered is valid, you will receive a text message and your phone number will be confirmed.
7. Create an Amazon SNS Topic as follows:
      - In the navigation pane, choose **Topics**.
      - Select **Create topic**.
      - Under **Type**, select **Standard**.
      - Enter a name of your choice. Here, you will use "*text_topic*".
      - Select **Create topic**.
8. Create a subscription for this topic:
      - On the newly created *text_topic* page, choose the **Subscriptions** tab.
      - Choose **Create subscription**.
      - In **Topic ARN**, choose the topic you have created earlier.
      - Select **Protocol** as **SMS** from the drop-down.
      - Under **Endpoint**, enter the previously validated phone number to receive the SMS alerts.
      - Choose **Create subscription**. You should see a **_Subscription to text_topic created successfully_** message.

##### Add a Rule for Amazon SNS Notification

Now, add a new rule to send an Amazon SNS notification when certain conditions are met in a decoded message.

1. Navigate to the <a href="http://console.aws.amazon.com/iot" target="_blank">AWS IoT console</a>.
2. In the navigation pane, choose **Act**. Then, choose **Rules**.
3. On the Rules page, choose **Create**.
4. Enter the **Name** as "*text_alert*" and provide an appropriate Description.
5. Under the **Rule query statement**, enter the following query:
  ```sql
      SELECT devEui as device_id, "Temperature exceeded 25" as message, temperature as temp, timestamp as time FROM '+/project/sensor/decoded' where temperature > 25
  ```
6. Under **Set one or more actions**, choose **Add action**.
7. Choose **Send a message as an SNS push notification**.
8. Choose **Configure action**.
9. Under SNS target, select *text_topic* from the drop-down.
10. Select **RAW** under **Message format**.
11. Under **Choose or create a role to grant AWS IoT access to perform this action**, choose **Create role**.
12. Enter a name for the role and choose **Add action**.
13. Choose **Create rule**. You should see a "**Success**" message, indicating that the rule has been created.

##### Test the Rule for Amazon SNS Notification

After adding the rule for Amazon SNS notification, you should receive a text message when hitting the event.

Wait for an uplink from the device. Here is the message from the mobile device after sending an uplink message.

```json
  {
       "device_id": "3933XXXXXXXXXXXX",
       "message": "Temperature exceeded 25",
       "temp": 27.2,
       "time": "2021-02-22T07:58:54Z"
  }

```

##### Send Downlink Payload

This section shows how to send downlink payload from AWS IoT LoRaWAN Server to the end Device.

1. Install the <a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html" target="_blank">AWS SAM CLI</a>.
2. Deploy <a href="https://github.com/aws-samples/aws-iot-core-lorawan/tree/main/send_downlink_payload" target="_blank">SAM template to AWS</a>.
3. Send Payload to End Device.
    - Go to the AWS IoT console.
    - In the navigation pane, select **Test**, and choose **MQTT client**.
    - Subscribe to the wildcard topic '**#**' to receive messages from all topics.
    - Specify the topic to **_cmd/downlink/\{WirelessDeviceId\}_** and a base64-encoded message.

> **Image:** Specifying a Topic

4. You should see traffic on AWS similar as shown below:

    ```json
    downlink/status/3eff83dd-9159-XXXX-XXXX-XXXXXXXXXXXX  February 09, 2021, 15:09:29 (UTC+0800)
    {
        "sendresult": {
            "status": 200,
            "RequestId": "4f1d36e1-8316-4436-8e9d-2207e3711755",
            "MessageId": "60223529-0011d9f5-0095-0008",
            "ParameterTrace": {
                "PayloadDate": "QQ==",
                "WirelessDeviceId": "3eff83dd-9159-XXXX-XXXX-XXXXXXXXXXXX",
                "Fport": 1,
                "TransmitMode": 1
            }
        }
    }
    ```

> **Image:** Traffic on AWS

5. You should see traffic on your console of end device similar as shown below.

```
SYSLOG:4:LoRa rX : 41 - 14
SYSLOG:4:LoRa Tx :
```

##### IoT Analytics

You will use IoT Analytics to visually display data via graphs if there is a need in the future to do further analysis.

###### Create an IoT Analytics Rule

** Create a Rule First **

1. Navigate to the <a href="http://console.aws.amazon.com/iot" target="_blank">AWS IoT console</a>.
2. In the navigation pane, choose **Act** and then, choose **Rules**.
3. On the Rules page, choose **Create**.
4. Enter the Name as **Visualize**, and provide an appropriate Description.
5. Under the Rule query statement, enter the following query:
```sql
SELECT * FROM 'project/sensor/decoded'
```
6. Choose **Add action**.
7. Select **Send a message to IoT Analytics**.
8. Choose **Configure Action**.
9. Choose **Quick Create IoT Analytics Resources**.
10. Under **Resource Prefix**, enter an appropriate prefix for your resources, such as _LoRa_.
11. Choose **Quick Create**.
12. Once the Quick Create Finished message is displayed, choose **Add action**.
13. Choose **Create rule**. You should see a Success message, indicating that the rule has been created.

###### Configure AWS IoT Analytics

1. Go to the <a href="http://console.aws.amazon.com/iotanalytics" target="_blank">AWS IoT Analytics console</a>.
2. In the navigation panel, choose **Data sets**.
3. Select the data set generated by the Quick Create in **Create an IoT Analytics Rule**.
4. In the Details section, click **Edit** in the **SQL query**.
5. Replace the query with as follows:
```sql
SELECT devEui as device_id, temperature as temp, timestamp as time FROM LoRa_datastore
```
6. Click **Update**.
7. Navigate to **Schedule**, and click **Edit**.
8. Under **Frequency**, choose **Every 1 minute**, and then click **Update**.

###### Configure Amazon QuickSight

Amazon QuickSight lets you easily create and publish interactive business intelligence (BI) dashboards that include machine learning-powered insights.

1. Go to <a href="http://console.aws.amazon.com/" target="_blank">AWS Management console</a>.
2. From the management console, enter **QuickSight** in the "_Search for services, features.._" search box.
3. Click on **QuickSight** in the search results.
4. If you haven't signed up for the service before, go ahead and sign up, as there is a free trial period.
5. Select the **Standard Edition**, and choose **Continue**.
6. Enter a unique name in the field QuickSight account name.
7. Fill in the Notification email address.
8. Review the other checkbox options and change them as necessary. The **AWS IoT Analytics** option must be selected.
9. Choose **Finish**. You will see a confirmation message.
10. Choose **Go to Amazon QuickSight**.
11. Select **Datasets**.
12. Select **New dataset**.
13. Select **AWS IoT Analytics**.
14. Under Select an AWS IoT Analytics data set to import, choose the data set created in **Create an IoT Analytics Rule**.
15. Choose **Create data source**, and then choose **Visualize**.
16. Select the dataset created, then select **Refresh** or **Schedule Refresh** for a periodic refresh of the dataset.

###### Testing Your "Hello Word" Application

Using your device, create a condition to generate an event, such as a high-temperature condition. If the temperature is above the configured threshold, you will receive a text alert on your phone. This alert will include key parameters about the alert.

You can also visualize the data set as follows:

1. Go to the <a href="http://console.aws.amazon.com/iotanalytics" target="_blank">AWS IoT Analytics console</a>.
2. Choose **Data sets**.
3. Select the dataset created earlier.
4. Select **Content** and ensure there are at least few uplink entries available in the data set.
5. Go to the <a href="http://quicksight.aws.amazon.com/" target="_blank">**QuickSight console**</a>.
6. Choose **New analysis**.
7. Choose the dataset created in **Create an IoT Analytics Rule**.
8. Select time on the X-axis, Value as temp (Average), and Color as device_id to see a chart of your dataset.

### Debugging

After logging in to the device using the web browser, the system log can be viewed from **Diagnostics** > **System Log**.

> **Image:** System Log

### Troubleshooting

1. Unable to see the web login:
    - Check that your Wi-Fi is connected to **RAK7240V2_XXXX** or **RAK7240CV2_XXXX**.
    - Try ping **192.168.230.1**.
2. Lost password to login to the web login.
   - Hold the reset button for 10 seconds to factory reset the device.

## AWS IoT Core Integration

AWS IoT Core Integration is a software service that enables your LoRaWAN gateway to work with AWS IoT Core. The <a href="https://learn.rakwireless.com/hc/en-us/articles/26475924574103-How-To-Implement-AWS-Integration-for-WisGate-Edge-V2" target="_blank">AWS Integration for WisGate Edge V2</a> tutorial will show you how to set up a LoRaWAN end-node and view its data on the AWS IoT Console. In addition, it'll show you how to send a message from AWS IoT Console to the end-node as well.

## The Things Network (TTN)

This tutorial illustrates how to configure and connect your RAK Gateway with WisGateOS 2 to a LoRaWAN Network Server by using the Basics Station protocol. For this example, it will be shown how to connect the gateway to TTNv3.

:::tip NOTE
LoRa Basics Station is an implementation of a LoRa packet forwarder. This protocol simplifies the management of large-scale LoRaWAN Networks. More information about the Basics Station protocol can be found in the <a href="https://blog.semtech.com/expert-series-5-things-you-need-to-know-about-lorawan-based-gateways" target="_blank">explanatory document</a> provided by Semtech.
:::

#### Registering the Gateway

1. Log in first and head on to [TTNv3 website](https://eu1.cloud.thethings.network/console). If you already have a TTN account, use your The Things ID credentials to log in.

> **Image:** The Things Stack Login Page

2. To register a commercial gateway, choose **Register a gateway** (for new users that do not already have a registered gateway) or go to **Gateways** > **+ Register gateway** (for users that have registered gateways before).

> **Image:** Console Page After a Successful Login

3. You will be redirected to the **Register gateway** page.
4. In the **Gateway EUI** field, type the EUI of the gateway. The gateway's EUI can be found either on the sticker on the casing or by going to the **Dashboard** > **Overview** page via the Web UI. Instructions on how to access your gateway via Web UI can be found in the product's <a href="https://docs.rakwireless.com/product-categories/wisgate/rak7240v2/quickstart#access-the-gateway" target="_blank">Quick Start Guide</a>.

> **Image:** Register Gateway

5. After typing the EUI, click on **Confirm**. Additional fields will pop up. Fill in the following information:
- **Gateway ID**: This will be the unique ID of your gateway in the Network. An ID based on the EUI is automatically generated. You can change it if you need. Note that the ID must contain only lowercase letters, numbers, and dashes (-).
- **Gateway name**: Optionally, you can type a name for your gateway.
- **Frequency plan**: The frequency plan used by the gateway.

:::tip NOTE
- The other settings are optional and can be changed to satisfy your requirements.
- For this tutorial, we will use Europe 863-870 MHz (SF12 for RX2).
:::

> **Image:** Adding a gateway

6. To register your gateway, click **Register gateway**.

> **Image:** Successfully added a gateway

#### Generating the Token

TTNv3 supports TLS server authentication and Client token, which requires a trust file and a key file to configure the gateway to successfully connect it to the network.

1. To generate a key file, from the **Overview page** of the registered gateway navigate to **API keys**.

> **Image:** Overview page

2. On the **API keys page**, choose **+Add API key**.

> **Image:** API key page

3. In the **Name field**, type the name of your key (for example - mykey). Choose **Grant individual rights**, and select **Link as Gateway to a Gateway for traffic exchange, i.e. write uplink and read downlink**.

> **Image:** Generating an API key

4. To generate the key, choose **Create API key**. The following window will pop up, telling you to copy the key you just generated.

> **Image:** Copying the generated key

:::warning
Copy the key and save it in a `.txt` file (or other), because you won't be able to view or copy your key after that.
:::

5. Click **I have copied the key** to proceed.

### Configuring the Gateway

1. To configure the gateway, access it via the Web UI. To learn how to do that, refer to the <a href="https://docs.rakwireless.com/product-categories/wisgate/rak7240v2/quickstart#access-the-gateway" target="_blank">Quick Start Guide</a>.
2. Navigate to **LoRa** > **Configuration** > **Work mode**, and select **Basics station**.

> **Image:** Changing the working mode

3. Expand the Basics Station settings by clicking **Configure Basics Station server setup**.

> **Image:** Expanded Basics Station settings

4. To connect the gateway to TTNv3, configure the following parameters:

- **Basics Station Server Type**: For server type, choose **LNS Server**.
- **Server URL**: This is the link to The Things Stack server. Note that, for this tutorial, the gateway is connected to the European cluster. For Europe fill in the following:

```
wss://eu1.cloud.thethings.network
```

- **Server Port**: The LNS Server uses port `8887`. Type in **`8887`**.
- **Authentication Mode**: Choose **TLS server authentication and Client token**. When selected, the **Trust (CA Certificate)** and **Client token** fields will show up.
- **Trust (CA Certificate)**: For **Trust**, upload the **Let's Encrypt ISRG ROOT X1 Trust** certificate by clicking **choose file**. The file with the certificate can be downloaded <a href="https://letsencrypt.org/certs/isrgrootx1.pem" target="_blank">directly</a>.
- **Client Token**: This is the generated API key.

> **Image:** Basics Station settings

5. To save the changes, click **Save Changes**. If everything is set correctly, you will be able to see the gateway is connected to TTNv3.

> **Image:** Successful connection

## ChirpStack

This guide will show you how to connect the RAKWireless Commercial gateway running WisGateOS 2 to a ChirpStack Network Server. Whether it is a local or external ChirpStack Network Server, the steps to add a gateway are the same. The guide is not about how to install ChirpStack, but how to configure the gateway to send data to it. In this tutorial, an external ChirpStack v4 Network Server is used as an example.

For external ChirpStack, RAK provides instructions for installing the ChirpStack Network Server on the AWS cloud. You can refer to the <a href="https://learn.rakwireless.com/hc/en-us/articles/26743884863767-How-To-Use-Amazon-Web-Services-with-LoRaWAN/#installing-chirpstack)" target="_blank">Learn Site</a>.

### Requirements

- Your RAK gateway is connected to the Internet.
- Connect to ChirpStack v4, the firmware of gateway is WisGateOS 2 2.2.x or above.
- ChirpStack v4 Network server is ready.

To access the ChirpStack web UI, enable **TCP port 8080** and to make the gateway to communicate with the Network server you need to enable the following ports in the inbound rules of the instance:

- The Semtech Packet Forwarder needs UDP port `1700`.
- MQTT Bridge (unsecured) needs TCP port `1883`.
- MQTT Bridge (secured) needs TCP port `8883`.
- Basics Station needs TCP port `3001`.

:::tip NOTE
A guide on how to open the above ports can be found in the <a href="https://learn.rakwireless.com/hc/en-us/articles/26743884863767-How-To-Use-Amazon-Web-Services-with-LoRaWAN/#installing-chirpstack" target="_blank">guide</a> on how to install ChirpStack on AWS.
:::

### Registering the Gateway

1. To register the gateway in the ChirpStack Network server, access the ChirpStack UI. To do that, open a web browser and type the server address of the ChirpStack with port `8080`.

```
<IP address of ChirpStack>:8080
```

2. In this case, the ChirpStack is installed on the AWS cloud with the public IP address `18.156.176.220.`

> **Image:** ChirpStack login page

3. Login using the following credentials:

- Username/email: **admin**
- Password: **admin**

> **Image:** ChirpStack dashboard

4. On the left pane, head to **Gateways**.

> **Image:** Gateway list

5. By default, no gateways are registered. To register one, click **Add gateway**.
6. In the **General** menu, set the gateway parameters.

> **Image:** Registering the gateway

- **Name**: unique name for the gateway on the Network server. The name may only contain words, numbers, and dashes.
- **Description**: a brief description of the gateway.
- **Gateway ID (EUI64)**: the Extended Unique Identifier (EUI) of the gateway. The EUI is in the Overview menu of the Dashboard page of the web UI of the gateway.
- **Stats interval (secs)**: The expected interval in seconds in which the gateway sends its statistics.

7. Click **Submit**. You will see the registered gateway in the Gateway list.

> **Image:** Registered gateway

### Configuring the Gateway

Three options will be considered here, and you can choose one of the connection options as needed.

- [Connecting the Gateway via Packet Forwarder](#connecting-the-gateway-via-packet-forwarder)
- [Connecting the Gateway via MQTT Bridge](#connecting-the-gateway-via-mqtt-bridge)
- [Connecting the Gateway via Basics Station](#connecting-the-gateway-via-basics-station)

#### Connecting the Gateway via Packet Forwarder

In this method, you will configure the gateway's packet forwarder to send data to the ChirpStack Gateway Bridge.

:::tip NOTE
When connecting the gateway to the ChirpStack, you will need to open ports 1700 and 8080 to enable the communication between the gateway and the server and be able to access the ChirpStack.
:::

> **Image:** Opened 1700 UDP port

1. Start by accessing the gateway.

> **Image:** Login page

2. Login using the set credentials you have set in the <a href="https://docs.rakwireless.com/product-categories/wisgate/rak7240v2/quickstart#access-the-gateway" target="_blank">Access the Gateway</a> section.
3. On the left side, head to **LoRa**. By default, the gateway is configured to work as a **Built-in network server**.
4. From **Work Mode**, select **Packet forwarder**. Click **Choose from the available protocols** to expand the Packet forwarder settings.

> **Image:** Setting Packet Forwarder Mode

When Packet Forwarder mode is chosen, the **Semtech UDP GWMP Protocol** is selected by default.

In this case, the ChirpStack is installed on the AWS cloud instance with public IP **18.156.176.220** (yours will be different). The default ports that the packet forwarder is using are 1700.

> **Image:** Configuring Packet Forwarder to ChirpStack

5. Click **Save changes** to save the changes.
6. If everything is set correctly, the gateway will display as online. You can click the gateway name to inspect the gateway traffic.

> **Image:** Registered gateway

> **Image:** Gateway details

#### Connecting the Gateway via MQTT Bridge

In this method, you will configure the gateway's built-in bridge to publish the data to the ChirpStack MQTT broker.

:::tip NOTE
When connecting the gateway to the ChirpStack, you will need to open ports 1883 and 8080 to enable the communication between the gateway and the server and be able to access the ChirpStack.
:::

> **Image:** ChirpStack enable ports

1. Start by accessing the gateway.

> **Image:** Login page

2. Login using the set credentials you have set in the <a href="https://docs.rakwireless.com/product-categories/wisgate/rak7240v2/quickstart#access-the-gateway" target="_blank">Access the Gateway</a> section.
3. On the left side, head to **LoRa**. By default, the gateway is configured to work as **Built-in network server**.
4. From **Work Mode**, select **Packet forwarder**. Click **Choose from the available protocols** to expand the Packet forwarder settings.

> **Image:** Setting packet forwarder mode

5. To use the built-in gateway bridge, from the **Protocol** select **LoRa Gateway MQTT Bridge**.

> **Image:** LoRa Gateway MQTT bridge

6. Choose **MQTT for ChirpStack 4.x (PROTOBUF)** as the MQTT protocol.

:::tip NOTE
+ The ChirpStack v3 supports both **MQTT for ChirpStack 3.x (JSON)** and **MQTT for ChirpStack 3.x (PROTOBUF)**. If you are using an earlier version of ChirpStack (v3), choose one of the MQTT protocols to use.
+ If you want to use the JSON protocol, change the payload marshaler in the gateway bridge `.toml` file to `.json`. By default, the marshaler is protobuf. To configure the payload marshaler, you will use the SSH client PuTTY to access the configuration files. How to do this is explained in the <a href="https://learn.rakwireless.com/hc/en-us/articles/26743884863767-How-To-Use-Amazon-Web-Services-with-LoRaWAN/#accessing-instance-via-ssh" target="_blank">Learn Site</a>.
:::

By default, the built-in gateway bridge is pointed to the local broker (127.0.0.1). To point the gateway to the ChirpStack network, set the ChirpStack Broker address in the **MQTT Broker Address** field.

In this case, the ChirpStack is installed on an AWS cloud instance with public IP `18.156.176.220` (yours will be different). The default port that the MQTT Broker uses is 1883.

> **Image:** Configuring packet forwarder to ChirpStack

7. Click **Save changes** to save the changes.

If everything is set correctly, the gateway will display as online. You can click the gateway name to inspect the gateway traffic.

> **Image:** Registered gateway

> **Image:** Gateway details

#### Connecting the Gateway via Basics Station

In this method, you will connect the gateway to the ChirpStack via Basics Station. The LoRa Basics™ Station is an implementation of a LoRa packet forwarder.

:::tip NOTE
When connecting the gateway to the ChirpStack, you will need to open TCP ports `3001` and `8080` to enable the communication between the gateway and the server and be able to access the ChirpStack.
:::

> **Image:** ChirpStack enable ports

1. Start by accessing the gateway.

> **Image:** Login page

2. Login using the set credentials you have set in the <a href="https://docs.rakwireless.com/product-categories/wisgate/rak7240v2/quickstart#access-the-gateway" target="_blank">Access the Gateway</a> section.
3. On the left side, head to **LoRa**. By default, the gateway is configured to work as **Built-in network server**.

4. For **Work Mode**, select **Basics station** and click **Configure Basics Station** server setup to expand the Basics Station settings.

> **Image:** Setting Basics Station mode

- **Basics Station Server Type**: For server, choose LNS Server.
- **Server URL**: the address of the ChirpStack v4 server. In this case, the ChirpStack v4 is installed on an AWS cloud instance with public IP `18.156.176.220` (yours will be different). The URL will be: `ws://18.156.176.220`.

:::tip NOTE
The URL starts with `ws://` in case a plain text connection is used. Using the `wss://` scheme will trigger a TLS connection based on the `tc.{cert,key,trust}`credentials set.
:::

- **Server Port**: the port to which the Websocket listens. The port is `3001`.
- **Authentication Mode**: Authentication for the ChirpStack server. For this case, you will use no authentication.

5. Click **Save changes** to save the changes.

Now that the gateway is configured to operate as a Basics Station and is pointing to the ChirpStack gateway bridge, note that the default ChirpStack installation sets up the backend of the ChirpStack gateway bridge as `semtech_udp`.

To configure the backend of the ChirpStack Gateway Bridge, open its configuration file using an SSH terminal. In this guide, the PuTTY client is used to establish the SSH connection.

Instructions for accessing the instance via SSH are available on the <a href="https://learn.rakwireless.com/hc/en-us/articles/26743884863767-How-To-Use-Amazon-Web-Services-with-LoRaWAN/#accessing-instance-via-ssh" target="_blank">Learn Site</a>.

> **Image:** PuTTY client

6. Go to the `/etc/chirpstack-gateway-bridge/` file path and open the `chirpstack-gateway-bridge.toml` file.
7. In the file, find the gateway backend configuration paragraph and replace the type with `basic_station`.

> **Image:** Configure gateway bridge type

8. Scroll down to the **Concentrator configuration** section and uncomment the following text shown in **Figure 63**.

> **Image:** Configuring gateway bridge backend

9. Save and exit the `.toml` file, then apply the changes by restarting the gateway bridge service using the following command:

```text
sudo systemctl restart chirpstack-gateway-bridge.service
```

This updates the ChirpStack backend configuration is support to the Basics station.

If everything is set correctly, the gateway should appear as online in the ChirpStack interface. Click the gateway name to view its traffic details.

> **Image:** Registered gateway

> **Image:** Gateway details

## ThingPark by Actility

In this section, you will learn how to add RAK7240V2/RAK7240CV2 WisGate Edge Pro in **ThingPark**.

ThingPark is Actility's platform, in which you can register your LoRaWAN® gateway and end devices. ThingPark offers a user-friendly dashboard where you can monitor various information about the gateway/end device, such as status, radio traffic, statistics, and more. Together with HTTPS integration, send the data received from the end nodes to an application server for post-processing and visualization.

For the complete step-by-step tutorial, refer to the <a href="https://learn.rakwireless.com/hc/en-us/articles/26476191725207-How-To-Add-RAK-WisGate-Edge-Gateway-V2-in-ThingPark-Actility-ThingPark-Guide" target="_blank">How to Add RAK WisGate Edge Gateway V2 in ThingPark - Actility ThingPark Guide</a>.

