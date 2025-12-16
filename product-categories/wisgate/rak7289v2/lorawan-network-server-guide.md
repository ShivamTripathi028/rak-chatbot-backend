---
title: RAK7289V2 RAK7289CV2 LoRaWAN Network Server Guide | Setup & Deployment
description: Learn how to set up and manage the RAK7289V2 LoRaWAN Network Server. Get expert guidance on LoRaWAN deployment, device management, and seamless integration.
image: https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/rak7289v2.png
keywords:
  - rak7289v2
  - rak7289cv2
  - lorawan base station
  - outdoor lorawan gateway
  - rak7289v2 setup guide
  - lora basics station
  - lorawan network server
  - lorawan gateway lte
  - mqtt integration
  - chirpstack lorawan integration
date: 2022-09-26
sidebar_label: LNS Guide
download: true
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK7289V2/RAK7289CV2 WisGate Edge Pro V2 LoRaWAN Network Server Guide

This manual provides you with operation guidance for connecting the gateway to different LoRaWAN network servers.

## Built-In Network Server

This section is an example demonstration on how to interconnect your RAK commercial gateway with its built-in LoRa network server and make an application for the node.

### Requirements

- Your node module (In this section, RAK3172 will be used as an example module)
- Your RAK gateway is connected to the Internet

### Set the Gateway Work Mode

1. Configure **Work mode** to **Built-in network server**. Navigate to **LoRa** > **Configuration**. For **Work mode**, select **Built-in network server**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/built-in-ns/set-the-gateway-work-mode.png"
  width="100%"
  caption="Set the gateway work mode"
/>

2. Select the log level and frequency band.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/built-in-ns/configure-log-level-and-frequency-band.png"
  width="100%"
  caption="Configure log level and frequency band"
/>

:::tip NOTE
You can expand the **View detailed regional parameters of the frequency plan** option to configure detailed regional parameters.
:::

### Create an Application

1. Navigate to **LoRa > Applications** tab.
2. Click the **Add application** button or the **add one now** link to add a new application.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/built-in-ns/add-application.png"
  width="100%"
  caption="Add an application"
/>

3. After the page jumps, configure the following information.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/built-in-ns/set-application-parameters.png"
  width="100%"
  caption="Set parameters"
/>

- **Application name**: Name of the application

- **Application description**: Description of the application, optional

- **Application Type**

  - **Unified Application key**: All devices will use the same application key. Selecting this option, then the application key field will pop up, where you can type in an application key or click the **Autogenerate** button to generate a key. This value needs to be consistent with the value from the end device, so either obtain it by querying the end device, or auto-generate it and synchronously change the corresponding value of the device.

  <RkImage
    src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/built-in-ns/unified-application-key.png"
    width="50%"
    caption="Configure unified application key"
  />

  After enabling the **Auto Add Device** option, you need to configure the **Application EUI** option. This value needs to be consistent with the value from the end device, so either obtain it by querying the end device, or auto-generate it and synchronously change the corresponding value of the device. After the application EUI and key verification, the device will be automatically added to the application.

  <RkImage
    src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/built-in-ns/auto-add-device.png"
    width="50%"
    caption="Enable auto add device"
  />

  - **Separate Application keys**: Each device has its own application key. Add the key when registering the device.

4. Click **Save Application** to add the new application.

### Add End Devices

1. Navigate to **LoRa > Applications** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/built-in-ns/application-list.png"
  width="100%"
  caption="Application list"
/>

2. In the application list, click the newly created application and choose the **End devices** tab.

:::tip NOTE
If you have enabled **Auto Add Device**, the device will be automatically registered with the adding request. Otherwise, you need to refer to the next step.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/built-in-ns/device-list.png"
  width="100%"
  caption="Device list"
/>

3. Click the **Add end device** button.
4. In the **End device information** interface, enter the following information.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/built-in-ns/add-new-device.png"
  width="100%"
  caption="Add new device"
/>

- **Activation Mode**: OTAA or ABP. This value needs to be consistent with the value from the end device. The ABP mode will pop up two additional fields, **Application Session Key** and **Network Session Key**.
- **End device (group) name**: Name of the end device (group).
- **End device description (optional)**: A description of the end device, optional.
- **Class**: This value needs to be consistent with the value from the end device.
- **Frame Counter Width**: Keep the default value.

5. Click **Add end devices** to enter the device adding page.
6. In the **Adding end devices** interface, enter the device EUI in the **End Device EUI (main)** field and click the **Add to End Devices list** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/built-in-ns/add-to-devicelist.png"
  width="100%"
  caption="Add new device to End Devices list"
/>

:::tip NOTE

+ The device EUI needs to be consistent with the end device EUI.
+ If the EUI is correct, the device will appear in the “End devices list”.
+ If the EUI is duplicate, the device will be displayed in the “End devices with an error”.

:::

7. Click **Add end devices** to add the device to the application. Execute join request on the node side.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/built-in-ns/device-online.png"
  width="100%"
  caption="Device online"
/>

By following the steps in the previous sections, you should now have your device registered. If you click on the **Device EUI**, you will go to the corresponding **Configuration** tab. Click the **Packet capture** button. Here you can monitor the data that the application is exchanging in real time.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/built-in-ns/data-packet.png"
  width="100%"
  caption="End Device Packet Capture"
/>

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
     - On the Review and create page. For the **Name**, type ***AWSIoTWirelessGatewayCertManager***.

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
The examples in this document are intended only for dev environments. All devices in your fleet must have credentials with privileges that authorize only intended actions on specific resources. The specific permission policies can vary for your use case. Identify the permission policies that best meet your business and security requirements. For more information, refer to <a href="https://docs.aws.amazon.com/iot/latest/developerguide/example-iot-policies.html"><b>Example Policies</b></a> and <a href="https://docs.aws.amazon.com/iot/latest/developerguide/security-best-practices.html"><b>Security Best Practices</b></a>
:::

#### Add IAM Role for Destination to AWS IoT Core for LoRaWAN


<b> Creating a Policy </b>

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

<b> Creating the Role </b>

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

<b> Updating your Trust Policy</b>

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

1. Using your preferred Web browser, access the gateway. To access the gateway, see the <a href="https://docs.rakwireless.com/product-categories/wisgate/rak7289v2/quickstart/" target="_blank">Quick Start Guide</a>.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/aws/web-user-interface-log-in.png"
  width="100%"
  caption="Web User Interface Log-in"
/>

2. Configure **Network Mode** to **Basics Station**. Navigate to **LoRa**.
3. For **Work mode**, select **Basics station** and click **Configure Basics Station server setup** to expand the Basics Station settings.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/aws/basics-station-work-mode.png"
  width="100%"
  caption="Basics Station Work Mode"
/>

4. Select **LNS Server** from Server, then choose **TLS Server and Client Authentication** from Authentication Mode.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/aws/configure-network-mode-to-basics-station.png"
  width="80%"
  caption="Configuring Network Mode to Basics Station"
/>

5. Configure URI, Port, and Authentication Mode.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/aws/configure-uri-port-authentication-mode.png"
  width="100%"
  caption="Configuring URI, Port, and Authentication Mode"
/>

6. Click **Save**. Check if the gateway is online in AWS IoT console.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/aws/verify-operation.png"
  width="90%"
  caption="Verifying Operation"
/>

### Add a LoRaWAN Device to AWS IoT

In this section we use RAK3172 as an example device.

#### Requirements

- Locate and note the following specifications about your endpoint device.
  - **LoRaWAN Region**: This must match the gateway LoRaWAN region.
  - **MAC Version**: This must be one of the following:
    - V1.0.2
    - v1.0.3
    - v1.0.4
    - v1.1
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

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/aws/add-the-device-profile.png"
  width="60%"
  caption="Adding the Device Profile"
/>

4. Click **Add device profile** once you have set a device profile that will work for you.

5. In the **Service Profiles** section, click **Add service profile** and set up the parameters as needed. As an example, the default service profile parameters are shown below. However, only the **_AddGwMetadata_** setting can be changed at this time.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/aws/add-the-service-profile.png"
  width="60%"
  caption="Adding the Service Profile"
/>

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

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/aws/add-destination.png"
  width="60%"
  caption="Adding Destination"
/>

6. Choose **Add Destination**.  You will see a message **_Destination added_**, indicating the destination has been successfully added.

#### Register the Device

Now, register an endpoint device with AWS IoT Core for LoRaWAN as follows. Before adding a device to AWS IoT, retrieve the **DevEUI**, **AppEUI**, and **AppKey** from the end Device's console. The RAK3172 device used in this example needs to query device information through <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/at-command-manual/" target="+blank">AT commands</a>.

1. Go to the <a href="http://console.aws.amazon.com/iot" target="_blank">AWS IoT console</a>.
2. Select **LPWAN devices** in the navigation panel on the left.
3. Select **Devices**, then choose **Add wireless device**.
4. On the **Add device** page, select the LoRaWAN specification version in the drop-down under **Wireless device specification**.
5. Enter the **DevEUI**.
6. Enter the remaining fields as per the OTAA/ABP choice you made above.
7. Enter a name for your device in the **Wireless device name – optional field**.
8. In the **Profiles** section, under **Wireless device profile**, from the drop-down option find the device profile you have created or the one that corresponds to your device and region.

:::tip NOTE
Compare your device details to ensure the device profile is correct. If there are no valid default options, you will have to create a new profile. See the [Verify Profiles](#verify-profiles) section.
:::

9. Choose the destination you created earlier (*ProcessLoRa*) from the drop-down under **Choose destination**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/aws/lorawan-specifications-and-wireless-device-configuration.png"
  width="80%"
  caption="LoRaWAN specifications and wireless device configuration"
/>

10. Click **Next**.
11. Choose **Add device**. You will see a message saying "*Wireless device added*", indicating that your device has been set up successfully.
12. Restart the end device, and it should join the AWS IoT LoRaWAN server.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/aws/joined-device.png"
  width="80%"
  caption="Joined Device"
/>

### Verifying Operation

Once setup is completed, provisioned OTAA devices can join the network and start to send messages. Messages from devices can then be received by AWS IoT Core for LoRaWAN and forwarded to the IoT Rules Engine.

Instructions for a sample Hello World application are given below, assuming that the device has joined and is capable of sending uplink traffic.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/aws/send-uplink-architecture.png"
  width="100%"
  caption="Sending Uplink Architecture"
/>

#### Create a Lambda Function for Destination Rule

Create the lambda function to process device messages processed by the destination rule.

1. Go to the <a href="http://console.aws.amazon.com/lambda" target="_blank">AWS Lambda console</a>.
2. Select **Functions** in the navigation pane.
3. Choose **Create function**.
4. Select **Author** from scratch.
5. Under **Basic Information**, enter the function name and choose **_Runtime Python 3.8_**. from the drop-down under **Runtime**.
6. Click **Create function**.
7. Under **Function code**, paste the copied code into the editor under the **_lambda_function.py_** tab.

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
        'devEui': event.get('WirelessMetadata').get('LoRaWAN')
                .get('DevEui'),
        'fPort': event.get('WirelessMetadata').get('LoRaWAN')
                .get('FPort'),
        'freq': event.get('WirelessMetadata').get('LoRaWAN')
                .get('Frequency'),
        'timestamp': event.get('WirelessMetadata').get('LoRaWAN')
                .get('Timestamp'),
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
    response = client.publish(topic=event.get('WirelessMetadata')
                              .get('LoRaWAN').get('DevEui')
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

- Choose **Review Policy**, then Save changes.

11. Go back to the Lambda function **Code source** and create a test event that will allow you to test the functionality of the lambda function.

  - Click **Test** next to **Deploy**.

  - In the **Configure test event**, enter a name for the test event in the **Event name** field.

  - Paste the following sample payload in the area under **Event JSON** field:

    :::tip NOTE
    The device information in the following code must be consistent with the device information you are using.
    :::

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

1. Navigate to the <a href="http://console.aws.amazon.com/iot" target="_blank">AWS IoT console</a>
2. In the navigation pane, choose **Act**, then select **Rules**.
3. On the Rules page, choose **Create rule**.
4. On the Create a rule page, enter as follows:
   - Name: **LoRaWANRouting**
   - Description: **Any description of your choice**.

     :::tip NOTE
     The **Name of your Rule** is the information needed when you provision devices to run on AWS IoT Core for LoRaWAN.
     :::
5. Leave the default Rule query statement: `SELECT * FROM 'iot/topic'` unchanged. This query has no effect at this time, as traffic is currently forwarded to the rules engine based on the destination.
6. Under **Set one or more actions**, click **Add action**.
7. On the **Select an action page**, select **Republish a message to an AWS IoT topic**. Scroll down and choose **Configure action**.
8. On the **Configure action page**, for Topic, enter **_project/sensor/decoded_**. The AWS IoT Rules Engine will forward messages to this topic.
9. Under **Choose or create a role to grant AWS IoT access to perform this action**, click on **Create Role**.
10. For **Name**, enter a name of your choice.
11. Select **Create role** to complete the role creation. You will see a "**Policy Attached**" tag next to the role name, indicating that the Rules Engine has been permitted to execute the action.
12. Choose **Add action**.
13. Add one more action to invoke the Lambda function. Under **Set one or more actions**, click **Add action**.
14. Select **Send a message to a Lambda function**.
15. Choose **Configure action**.
16. Click the Lambda function created earlier and choose **Add action**.
17. Then select **Create rule**.
18. A "**Success**" message will be displayed at the top of the panel, and the destination has a rule bound to it.

You can now check that the decoded data is received and republished by AWS by triggering a condition or event on the device itself.

- Go to the AWS IoT console. In the navigation pane, select **Test**, and choose **MQTT client**.
- Subscribe to the wildcard topic '**#**' to receive messages from all topics.
- Send message from endDevice using AT command
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
12. Enter a name for the role and choose **Create role**.
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

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/aws/specify-a-topic.png"
  width="100%"
  caption="Specifying a Topic"
/>

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

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/aws/traffic-on-aws.png"
  width="100%"
  caption="Traffic on AWS"
/>

5. You should see traffic on your console of end device similar as shown below.

```
SYSLOG:4:LoRa rX : 41 - 14
SYSLOG:4:LoRa Tx :
```

##### IoT Analytics

You will use IoT Analytics to visually display data via graphs if there is a need in the future to do further analysis.

###### Create an IoT Analytics Rule

<b> Create a Rule First </b>

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

<b> Set up AWS IoT Analytics </b>

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

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/aws/system-log.png"
  width="100%"
  caption="System Log"
/>

### Troubleshooting

1. Unable to see the web login:
   - Check that your Wi-Fi is connected to **RAK7289V2_XXXX** or **RAK7289CV2_XXXX**.
   - Try ping **192.168.230.1**.
2. Lost password to login to the web login.
   - Hold the reset button for 10 seconds to factory reset the device.

## AWS IoT Core Integration

AWS IoT Core Integration is a software service that enables your LoRaWAN gateway to work with AWS IoT Core. The <a href="https://learn.rakwireless.com/hc/en-us/articles/26475924574103-How-To-Implement-AWS-Integration-for-WisGate-Edge-V2" target="_blank">AWS Integration for WisGate Edge V2</a> tutorial will show you how to set up a LoRaWAN end-node and view its data on the AWS IoT Console. In addition, it’ll show you how to send a message from AWS IoT Console to the end-node as well.

## The Things Network (TTN)

This tutorial illustrates how to configure and connect your RAK Gateway with <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/" target="_blank">WisGateOS 2</a> to a LoRaWAN Network Server by using the Basics Station protocol. For this example, we will show you how to connect the gateway to TTNv3.


:::tip NOTE

LoRa Basics Station is an implementation of a LoRa packet forwarder. This protocol simplifies the management of large-scale LoRaWAN Networks. More information about the Basics Station protocol can be found in the <a href="https://blog.semtech.com/expert-series-5-things-you-need-to-know-about-lorawan-based-gateways" target="_blank">explanatory document</a> provided by Semtech.
:::

### Register the Gateway

1. First, log in and navigate to the [TTNv3 website](https://id.thethingsnetwork.org/). If you already have a TTN account, you can use your credentials to log in.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/ttn/the-things-stack-login-page.png"
  width="100%"
  caption="The Things Stack Login Page"
/>


2. To register a commercial gateway, choose **Register a gateway** (for new users that do not already have a registered gateway) or go to **Gateways** > **+ Register gateway** (for users that have registered gateways before).

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/ttn/console-page-after-a-successful-login.png"
  width="100%"
  caption="Console Page After a Successful Login"
/>


3. You will be redirected to the **Register gateway** page.
4. In the **Gateway EUI** field, type the EUI of the gateway. The gateway's EUI can be found either on the sticker on the casing or by going to the **Dashboard > Overview** page via the Web UI. Instructions on how to access your gateway via Web UI can be found in the product's [Quick Start Guide](https://docs.rakwireless.com/product-categories/wisgate/rak7289v2/quickstart/#access-the-gateway).

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/ttn/register-gateway.png"
  width="100%"
  caption="Register gateway"
/>


5. After entering the EUI, click on **Confirm**. Additional fields will appear. Fill in the following information:

- **Gateway ID**: This will be the unique ID of your gateway in the Network. An ID based on the EUI is automatically generated. You can change it if you needed. Note that the ID must contain only lowercase letters, numbers, and dashes (-).
- **Gateway name**: Optionally, you can type a name for your gateway.
- **Frequency plan**: The frequency plan used by the gateway.


:::tip NOTE
- The other settings are optional and can be adjusted to meet your specific requirements.
- This tutorial is for the EU868 Frequency band.
  :::

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/ttn/add-a-gateway.png"
  width="80%"
  caption="Adding a gateway"
/>


6. To register your gateway, click **Register gateway**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/ttn/successfully-added-a-gateway.png"
  width="100%"
  caption="Successfully added a gateway"
/>

### Generate the Token

TTNv3 supports TLS server authentication and client tokens, which require a trust file and a key file to configure the gateway to successfully connect it to the network.

1. To generate a key file, from the **Overview page** of the registered gateway navigate to **API keys**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/ttn/overview-page.png"
  width="100%"
  caption="Overview page"
/>


2. On the **API keys page**, choose **+ Add API key**.


<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/ttn/api-key-page.png"
  width="100%"
  caption="API key page"
/>


3. In the **Name field**, type the name of your key (for example: *mykey*). Choose **Grant individual rights** and select the **Link as Gateway to a Gateway for traffic exchange, i.e. read uplink and write downlink** option.


<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/ttn/generate-an-api-key.png"
  width="100%"
  caption="Generating an API key"
/>


4. To generate the key, choose **Create API key**. The following window will pop up, instructing you to copy the generated key.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/ttn/copy-the-generated-key.png"
  width="60%"
  caption="Copying the generated key"
/>

:::warning
Copy the key and save it in a `.txt` file (or another format), as you won’t be able to view or copy your key later.
:::

5. Click **I have copied the key** to proceed.

### Configure the Gateway

1. To configure the gateway, access it via the Web UI. Refer to the [Quick Start Guide](https://docs.rakwireless.com/product-categories/wisgate/rak7289v2/quickstart/) for specific instructions.

2. Navigate to **LoRa** > **Configuration** > **Work mode** and select **Basics station**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/ttn/change-the-work-mode.png"
  width="100%"
  caption="Changing the working mode"
/>


3. Expand the Basics Station settings by clicking **Configure Basics Station server setup**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/ttn/expanded-basics-station-settings.png"
  width="100%"
  caption="Expanded Basics Station settings"
/>


4. To connect the gateway to TTNv3, configure the following parameters:

- **Basics Station Server Type**: For server type, choose **LNS Server**.
- **Server URL**: This is the link to The Things Stack server. For this tutorial, the gateway is connected to the European cluster. Fill in the following for Europe:

```
wss://eu1.cloud.thethings.network
```

- **Server Port**: The LNS Server uses port `8887`. Type in **`8887`**.
- **Authentication Mode**: Choose **TLS server authentication and Client token**. When selected, the **Trust (CA Certificate)** and **Client token** fields will show up.
- **Trust (CA Certificate)**: For **Trust**, upload the **Let’s Encrypt ISRG ROOT X1 Trust** certificate by clicking **choose file**. The file with the certificate can be downloaded <a href="https://letsencrypt.org/certs/isrgrootx1.pem" target="_blank">directly</a>.
- **Client Token**: This is the generated API key.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/ttn/basics-station-settings.png"
  width="100%"
  caption="Basics Station settings"
/>


5. To save the changes, click **Save Changes**. If everything is set correctly, you can see the gateway is connected to TTNv3.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/ttn/successful-connection.png"
  width="100%"
  caption="Successful connection"
/>



## ChirpStack

This guide will show you how to connect the RAKWireless Commercial gateway running WisGateOS 2 to a ChirpStack Network Server. Whether it is a local or external ChirpStack Network Server, the steps to add a gateway are the same. The guide is not about how to install ChirpStack, but how to configure the gateway to send data to it. In this tutorial, an external ChirpStack v4 Network Server is used as an example.

For external ChirpStack, RAK provides instructions for installing the ChirpStack Network Server on the AWS cloud. You can refer to the <a href="https://learn.rakwireless.com/hc/en-us/articles/26743884863767-How-To-Use-Amazon-Web-Services-with-LoRaWAN/#installing-chirpstack)" target="_blank">Learn Site</a>.

### Requirements

- Your RAK gateway is connected to the Internet.
- Connect to ChirpStack v4, the firmware of gateway is WisGateOS 2 2.2.x or above.
- ChirpStack v4 Network server is ready.

To access the ChirpStack web UI, you need to enable **TCP port 8080** and to make the gateway to communicate with the Network server you need to enable the following ports in the inbound rules of the instance:

- The Semtech Packet Forwarder needs UDP port `1700`.
- MQTT Bridge (unsecured) needs TCP port `1883`.
- MQTT Bridge (secured) needs TCP port `8883`.
- Basics Station needs TCP port `3001`.

:::tip NOTE
Instructions for opening the ports mentioned above are provided in the <a href="https://learn.rakwireless.com/hc/en-us/articles/26743884863767-How-To-Use-Amazon-Web-Services-with-LoRaWAN/#installing-chirpstack" target="_blank">installing ChirpStack on AWS</a> guide.
:::

### Registering the Gateway

1. To register the gateway in the ChirpStack Network server, access the ChirpStack UI. To do that, open a web browser and type the server address of the ChirpStack with port `8080`.

```
<IP address of ChirpStack>:8080
```

2. In this case, the ChirpStack is installed on the AWS cloud with the public IP address `18.156.176.220.`

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/chirpstack-login-page.png"
  width="100%"
  caption="ChirpStack login page"
/>

3. Login using the following credentials:

- Username/email: **admin**
- Password: **admin**

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/chirpstack-dashboard.png"
  width="100%"
  caption="ChirpStack dashboard"
/>

4. On the left pane, head to **Gateways**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/gateway-list.png"
  width="100%"
  caption="Gateway list"
/>

5. By default, no gateways are registered. To register one, click **Add gateway**.
6. In the **General** menu, you need to set the gateway parameters.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/register-the-gateway.png"
  width="100%"
  caption="Registering the gateway"
/>

- **Name**: unique name for the gateway on the Network server. The name may only contain words, numbers, and dashes.
- **Description**: a brief description of the gateway.
- **Gateway ID (EUI64)**: the Extended Unique Identifier (EUI) of the gateway. The EUI is in the Overview menu of the Dashboard page of the web UI of the gateway.
- **Stats interval (secs)**: The expected interval in seconds in which the gateway sends its statistics.

7. Click **Submit**. You will see the registered gateway in the Gateway list.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/registered-gateway.png"
  width="100%"
  caption="Registered gateway"
/>

### Configuring the Gateway

Three options will be considered here, and you can choose one of the connection options as needed.

- [Connecting the Gateway via Packet Forwarder](#connecting-the-gateway-via-packet-forwarder)
- [Connecting the Gateway via MQTT Bridge](#connecting-the-gateway-via-mqtt-bridge)
- [Connecting the Gateway via Basics Station](#connecting-the-gateway-via-basics-station)

#### Connecting the Gateway via Packet Forwarder

In this method, you will configure the gateway’s packet forwarder to send data to the ChirpStack Gateway Bridge.

:::tip NOTE
When connecting the gateway to the ChirpStack, you will need to open ports 1700 and 8080 to enable the communication between the gateway and the server and be able to access the ChirpStack.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/opened-1700-udp-port.png"
  width="100%"
  caption="Opened 1700 UDP port"
/>

1. Start by accessing the gateway.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/wisgate-login-interface.png"
  width="100%"
  caption="Login page"
/>


2. Login using the set credentials you have set in the <a href="https://docs.rakwireless.com/product-categories/wisgate/rak7289v2/quickstart/#access-the-gateway" target="_blank">Access the Gateway</a> section.
3. On the left side, head to **LoRa**. By default, the gateway is configured to work as a Built-in network server.
4. From **Work Mode**, select **Packet forwarder**. Click **Choose from the available protocols** to expand the Packet forwarder settings.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/set-packet-forwarder-mode.png"
  width="100%"
  caption="Setting Packet Forwarder Mode"
/>

When Packet Forwarder mode is chosen, the **Semtech UDP GWMP Protocol** is selected by default.

In this case, the ChirpStack is installed on the AWS cloud instance with public IP **18.156.176.220** (yours will be different). The default ports that the packet forwarder is using are 1700.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/configure-udp-protocol-parameters-on-chirpstack.png"
  width="90%"
  caption="Configuring UDP Protocol parameters on ChirpStack"
/>

5. Click **Save changes** to save the changes.
6. If everything is set correctly, the gateway will display as online. You can click the gateway name to inspect the gateway traffic.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/registered-gateway.png"
  width="100%"
  caption="Registered gateway"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/gateway-details.png"
  width="100%"
  caption="Gateway details"
/>

#### Connecting the Gateway via MQTT Bridge

In this method, you will configure the gateway’s built-in bridge to publish the data to the ChirpStack MQTT broker.

:::tip NOTE
When connecting the gateway to the ChirpStack, you will need to open ports 1883 and 8080 to enable the communication between the gateway and the server and be able to access the ChirpStack.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/chirpstack-enable-ports.png"
  width="100%"
  caption="ChirpStack enable ports"
/>

1. Start by accessing the gateway.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/wisgate-login-interface.png"
  width="100%"
  caption="Login page"
/>

2. Login using the set credentials you have set in the <a href="https://docs.rakwireless.com/product-categories/wisgate/rak7289v2/quickstart/#access-the-gateway" target="_blank">Access the Gateway</a> section.
3. On the left side, head to **LoRa**. By default, the gateway is configured to work as **Built-in network server**.
4. From **Work Mode**, select **Packet forwarder**. Click **Choose from the available protocols** to expand the Packet forwarder settings.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/set-packet-forwarder-mode.png"
  width="100%"
  caption="Setting packet forwarder mode"
/>

5. To use the built-in gateway bridge, from the **Protocol** select **LoRa Gateway MQTT Bridge**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/lora-gateway-mqtt-bridge.png"
  width="90%"
  caption="LoRa Gateway MQTT bridge"
/>

6. Choose **MQTT for ChirpStack 4.x (PROTOBUF)** as the MQTT protocol.

:::tip NOTE
+ The ChirpStack v3 supports both **MQTT for ChirpStack 3.x (JSON)** and **MQTT for ChirpStack 3.x (PROTOBUF)**. If you are using an earlier version of ChirpStack (v3), you need to choose one of the MQTT protocols to use.
+ If you want to use the JSON protocol, you need to change the payload marshaler in the gateway bridge `.toml` file to `.json`. By default, the marshaler is protobuf. To configure the payload marshaler, you will use the SSH client PuTTY to access the configuration files. How to do this is explained in the <a href="https://learn.rakwireless.com/hc/en-us/articles/26743884863767-How-To-Use-Amazon-Web-Services-with-LoRaWAN/#accessing-instance-via-ssh" target="_blank">Learn Site</a>.
  :::

By default, the built-in gateway bridge is pointed to the local broker (127.0.0.1). To point the gateway to the ChirpStack network, you need to set the ChirpStack Broker address in the **MQTT Broker Address** field.

In this case, the ChirpStack is installed on an AWS cloud instance with public IP `18.156.176.220` (yours will be different). The default port that the MQTT Broker uses is 1883.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/configure-mqtt-bridge-parameters-on-chirpstack.png"
  width="85%"
  caption="Configure MQTT Bridge parameters on ChirpStack"
/>

7. Click **Save changes** to save the changes.

If everything is set correctly, the gateway will display as online. You can click the gateway name to inspect the gateway traffic.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/registered-gateway.png"
  width="100%"
  caption="Registered gateway"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/gateway-details.png"
  width="100%"
  caption="Gateway details"
/>

#### Connecting the Gateway via Basics Station

In this method, you will connect the gateway to the ChirpStack via Basics Station. The LoRa Basics™ Station is an implementation of a LoRa packet forwarder.

:::tip NOTE
When connecting the gateway to the ChirpStack, you will need to open TCP ports `3001` and `8080` to enable the communication between the gateway and the server and be able to access the ChirpStack.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/chirpstack-enable-ports.png"
  width="100%"
  caption="ChirpStack enable ports"
/>

1. Start by accessing the gateway.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/wisgate-login-interface.png"
  width="100%"
  caption="Login interface"
/>

2. Login using the set credentials you have set in the <a href="https://docs.rakwireless.com/product-categories/wisgate/rak7289v2/quickstart/#access-the-gateway" target="_blank">Access the Gateway</a> section.

3. On the left side, head to **LoRa**. By default, the gateway is configured to work as **Built-in network server**.

4. For **Work Mode**, select **Basics station** and click **Configure Basics Station** server setup to expand the Basics Station settings.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/configuring-basics-sation.png"
  width="100%"
  caption="Setting Basics Station mode"
/>

- **Basics Station Server Type**: For server, choose LNS Server.
- **Server URL**: the address of the ChirpStack v4 server. In this case, the ChirpStack v4 is installed on an AWS cloud instance with public IP `18.156.176.220` (yours will be different). The URL will be: `ws://18.156.176.220`.

:::tip NOTE
The URL starts with `ws://` in case a plain text connection is used. Using the `wss://` scheme will trigger a TLS connection based on the `tc.{cert,key,trust}`credentials set.
:::

- **Server Port**: the port to which the Websocket listens. The port is `3001`.
- **Authentication Mode**: Authentication for the ChirpStack server. For this case, you will use no authentication.

5. Click **Save changes** to save the changes.

Now, your gateway is configured to work as a Basics Station and is pointed to the ChirpStack gateway bridge. The default installation of the ChirpStack sets up the backend of the ChirpStack gateway bridge as `semtech_udp`.

To configure the backend of the ChirpStack gateway bridge, you need to access the configuration file of the bridge. To access it, you will need an SSH terminal. In this case, you will use the PuTTY client.

To access the ChirpStack configuration files, you need to access the instance. How to do this is explained in the <a href="https://learn.rakwireless.com/hc/en-us/articles/26743884863767-How-To-Use-Amazon-Web-Services-with-LoRaWAN/#accessing-instance-via-ssh" target="_blank">Learn Site</a>.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/putty-client.png"
  width="50%"
  caption="PuTTY client"
/>

6. Go to the `/etc/chirpstack-gateway-bridge/` file path and open the `chirpstack-gateway-bridge.toml` file.

7. In the file, find the gateway backend configuration paragraph and replace the type with `basic_station`.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/configure-gateway-bridge.png"
  width="100%"
  caption="Configure gateway bridge type"
/>

8. Now scroll down until you find the **Concentrator configuration** paragraph and uncomment the following text as shown below.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/configuring-gateway-bridge-backend.png"
  width="100%"
  caption="Configuring gateway bridge backend"
/>

:::tip NOTE
The example uses US915. The frequency band setting needs to be consistent with the frequency band of the gateway used.
:::

9. Save and exit the `.toml` file and restart the gateway bridge service to apply the changes by restarting the gateway bridge service with the following command:

```text
sudo systemctl restart chirpstack-gateway-bridge.service
```

Now, the ChirpStack backend configuration is set to the Basics station.

If everything is set correctly, the gateway will display as online. You can click the gateway name to inspect the gateway traffic.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/registered-gateway.png"
  width="100%"
  caption="Registered gateway"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpstack/gateway-details.png"
  width="100%"
  caption="Gateway details"
/>

## ThingPark by Actility

In this section, you will learn how to add the RAK7289V2/RAK7289CV2 WisGate Edge Pro to **ThingPark**.

ThingPark is Actility’s platform, in which you can register your LoRaWAN® gateway and end devices. ThingPark offers a user-friendly dashboard where you can monitor various information about the gateway/end device, such as status, radio traffic, statistics, and more. Together with HTTPS integration, you can send the data received from the end nodes to an application server for post-processing and visualization.

For the complete step-by-step tutorial, refer to the <a href="https://learn.rakwireless.com/hc/en-us/articles/26476191725207-How-To-Add-RAK-WisGate-Edge-Gateway-V2-in-ThingPark-Actility-ThingPark-Guide" target="_blank">How to Add RAK WisGate Edge Gateway V2 in ThingPark - Actility ThingPark Guide</a>.



## Chirp Network

<a href="https://chirpwireless.io/" target="_blank">Chirp Wireless</a> is a leading global wireless network provider, offering reliable and extensive IoT connectivity solutions for outdoor and indoor use. Chirp's main objective is to simplify IoT deployments for its clients.

By providing multiple connectivity options, including 2.4&nbsp;GHz LoRa, and offering white-label business-specific modules, Chirp eliminates the need for multiple networks, platforms, and billing systems. Chirp offers its visualization platform, empowering clients to effortlessly implement IoT devices and visualize data with a simple click.

In this guide, you will learn how to connect a WisGate Edge V2 gateway to the LNS solution provided by Chirp Wireless.

### Adding the Gateway

1. Log in to your account at the <a href="https://app.chirpwireless.io/" target="_blank">Chirp Wireless login page</a>. If you don't have an account, create one.

<RkImage
src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpwireless/chirps-login-page.png"
width="100%"
caption="Chirp's login page"
/>

2. Once logged in, navigate to **Gateways** > **+Add gateway** > **3rd Party Gateway**.

<RkImage
src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpwireless/add-a-gateway.png"
width="100%"
caption="Adding a gateway"
/>

3. Fill in the needed data and click **Next**.
- **Name**: Enter a name for the gateway that will help you identify it easily.
- **Region**: This is the LoRaWAN region of the gateway. For this example, we will be using the EU868.
- **Gateway EUI**: This is the EUI of the gateway. You can find it either on a sticker at the back of the device or in the **Web UI** > **Dashboard** > **Overview**.

<RkImage
src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpwireless/gateway-information.png"
width="100%"
caption="Gateway information"
/>

4. After confirmation, download the `certs.zip` containing the needed certificates and copy the LNS address to the clipboard. Click **Continue**.

<RkImage
src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpwireless/certificates-and-address-generation.png"
width="100%"
caption="Certificates and address generation"
/>

5. Now, your gateway is successfully added to the Chirp platform. Click **Continue** to view your gateway list.

<RkImage
src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpwireless/gateway-successfully-added.png"
width="100%"
caption="Gateway successfully added"
/>

:::tip NOTE
If you didn't save the certificates or LNS address, you can navigate to the gateway's **Settings** tab.
:::

<RkImage
src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpwireless/gateway-settings.png"
width="100%"
caption="Gateway settings"
/>

### Configuring the Gateway

1. To configure the gateway, access it via the Web UI. To learn how to do that, refer to the Quick Start Guide for each gateway.
2. Navigate to **LoRa** > **Configuration** > **Work mode** and select **Basics station**.
- **Server URL**: Put the LNS Address you copied from Chirp's dashboard.
- **Server Port**: Enter the port number `443`.
-  **Authentication Mode**: Select *TLS Server & Client Authentication*.

<RkImage
src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpwireless/gateway-configuration.png"
width="100%"
caption="Gateway configuration"
/>

3. Unzip the certificates.

<RkImage
src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpwireless/gateway-certificates.png"
width="50%"
caption="Certificates"
/>

4. Upload each certificate to the corresponding field in the Web UI and click **Save changes**.

| Field                  | Certificate |
| :--------------------: | :---------: |
| Trust (CA Certificate) | `tc.trust`  |
| Client certificate     | `tc.crt`    |
| Client key             | `tc.key`    |

<RkImage
src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpwireless/upload-certificates.png"
width="100%"
caption="Uploading certificates"
/>

5. If set up correctly, the status of the gateway on the Chirp's dashboard will show as online. It may take a couple of minutes, so wait till the dashboard appears.

<RkImage
src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpwireless/gateway-is-online.png"
width="100%"
caption="Gateway is online"
/>

<RkImage
src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/lorawan-network-server-guide/chirpwireless/gateway-overview.png"
width="100%"
caption="Gateway overview"
/>

<RkBottomNav/>