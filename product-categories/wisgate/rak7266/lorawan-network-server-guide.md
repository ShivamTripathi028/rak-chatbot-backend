---
slug: /product-categories/wisgate/rak7266/lorawan-network-server-guide/
title: RAK7266 LoRaWAN Network Server Guide | Setup & Configuration
description: Easily set up the RAK7266 WisGate Soho Lite with LTE backhaul, built-in LoRaWAN server, and secure MQTT bridging for reliable IoT network integration.
image: "https://images.docs.rakwireless.com/wisgate/rak7266/rak7266.svg"
keywords:
  - rak7266
  - rak7266 lns guide
  - setup lorawan gateway server
  - lorawan configuration
  - configure indoor lora gateway
  - lorawan edge gateway
  - lora settings configuration
  - wisgate edge gateway
  - 8 channel lorawan gateway
  - low power lorawan gateway
  - multi-channel packet forwarder
  - lorawan network gateway
  - long range rf communication
  - low power consumption design
  - built-in server setup
  - long range iot gateway
tags:
  - rak7266
  - wisgate
  - lns guide
sidebar_label: LNS Guide
date: 2026-06-26
---

# RAK7266 WisGate Soho Lite LoRaWAN Network Server Guide

This manual provides operational guidance for connecting the gateway to different LoRaWAN network servers.

## Built-In Network Server

This section provides a practical overview of how to use the **Built-in LoRa Network Server** on a RAK gateway.

For complete setup instructions—including configuring the server, adding end devices, and managing applications, refer to the <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/?intsource=docs_center&intmedium=organic&intcampaign=rak7266_documentation_lns_guide_page&intterm=wisgateos2_user_manual&intcontent=documentation_link#built-in-network-server" target="_blank">WisGateOS 2 User Manual.</a>

:::tip NOTE

The referenced manual may feature different gateway models, but the configuration process and user interface are consistent across all **WisGateOS 2**-based devices.

:::

## AWS IoT Core for LoRaWAN

### Set Up Roles and Policies in IAM

Before you can connect your LoRaWAN gateways and devices to **AWS IoT Core**, you must first set up the required **IAM roles and policies**.

These roles enable AWS services to:

- Provision and manage gateway credentials through the **Configuration and Update Server (CUPS)**
- Forward device data to AWS IoT services via defined **Destinations**

:::tip NOTE
The examples in this document are intended only for dev environments. All devices in your fleet must have credentials with privileges that authorize only intended actions on specific resources. The specific permission policies can vary for your use case. Identify the permission policies that best meet your business and security requirements. For more information, refer to <a href="https://docs.aws.amazon.com/iot/latest/developerguide/example-iot-policies.html">**Example Policies**</a> and <a href="https://docs.aws.amazon.com/iot/latest/developerguide/security-best-practices.html">**Security Best Practices**.</a>
:::

#### Add an IAM Role for CUPS Server

To allow **AWS IoT Core for LoRaWAN** to securely manage gateway certificates, you must assign an IAM **role and policy** that authorizes the **Configuration and Update Server (CUPS)** to:

- Create and register gateway certificates
- Manage gateway credentials automatically

This setup is required to enable gateways to authenticate and connect successfully with AWS IoT Core for LoRaWAN.

Follow the official instructions:
[Add an IAM role to allow the Configuration and Update Server (CUPS) to manage gateway credentials](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-rfregion-permissions.html#lorawan-onboard-permissions)

:::tip NOTE
In some AWS accounts or regions, the managed policy `AWSIoTWirelessGatewayCertManager` may not appear by default.

If not available, go to the [IAM Policies](https://console.aws.amazon.com/iam/home#/policies) page and **manually create a policy** with the following definition **and name it exactly** `AWSIoTWirelessGatewayCertManager`:

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

:::

#### Add an IAM Role for Destination to AWS IoT Core for LoRaWAN

To allow AWS IoT Core for LoRaWAN to forward device data to AWS services (via **Destinations**, such as IoT Rules), you must assign an IAM **role and policy** that authorizes the service to publish messages on your behalf.

For detailed steps on how to create this IAM role, refer to the official AWS documentation:
[Create a destination role for AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-create-destinations.html#lorawan-create-destinations-roles)

### Add the Gateway to AWS IoT

To register the gateway with AWS IoT Core for LoRaWAN, execute these steps:

1. Navigate to the <a href="http://console.aws.amazon.com/iot" target="_blank">AWS IoT console.</a>
2. Select **LPWAN devices** from the navigation panel.
3. Choose **Gateways**, then click **Add gateway**.
4. In the **Add gateway** section, fill in the **Gateway's EUI** and **Frequency band (RF Region)** fields.
5. Enter a descriptive name in the **Name**: optional field. It is recommended that you use the GatewayEUI as the name.
6. Click **Add gateway**.
7. On the **Configure your gateway** page, find the section titled **Gateway certificate**.
8. Select **Create certificate**.
9. Once the **Certificate created and associated with your gateway** message appears, select **Download certificate files** to download the certificate (*xxxxx.cert.pem*) and private key (*xxxxxx.private.key*).
10. In the section **Provisioning credentials**, choose **Download server trust certificates** to download the **CUPS (cups.trust)** and **LNS (lns.trust)** server trust certificates.
11. Copy the **CUPS and LNS endpoints** and save them in a `.txt` file. You will need them later when configuring the gateway.
12. Choose **Submit** to add the gateway.

### Set Up the Gateway

1. Using your preferred Web browser, access the gateway. To access the gateway, see the <a href="https://docs.rakwireless.com/product-categories/wisgate/rak7266/quickstart/" target="_blank">Quick Start guide.</a>

> **Image:** Web User Interface Log-in

2. Configure **Network Mode** to **Basics Station**. Navigate to **LoRa**.
3. For **Work mode**, select **Basics station** and click **Configure Basics Station server setup** to expand the Basics Station settings.

> **Image:** Basics Station Work Mode

4. Select **LNS Server** from Server, then choose **TLS Server and Client Authentication** from Authentication Mode.

> **Image:** Configure Network Mode to Basics Station

5. Configure URI, Port, and Authentication Mode.

> **Image:** Configure URI, Port, and Authentication Mode

6. Click **Save changes**, then check whether the gateway appears online in the AWS IoT console.

> **Image:** Verify Operation

### Add a LoRaWAN Device to AWS IoT

This section demonstrates how to register a LoRaWAN device to **AWS IoT Core for LoRaWAN**, using a **RAK end device** as an example.

#### AWS IoT Requirements

Before registering your device, make sure you have the following information, based on your device's firmware and activation mode:

**Device specifications**:
- **LoRaWAN Region** – Must match the region configured on your gateway (e.g., EU868, US915)
- **MAC Version** – For example, 1.0.2 or 1.0.3

**Device credentials** *(provided by the device manufacturer or configured in firmware)*:
- **For OTAA v1.0.x**: `DevEUI`, `AppEUI`, `AppKey`
- **For OTAA v1.1**: `DevEUI`, `JoinEUI`, `AppKey`, `NwkKey`
- **For ABP v1.0.x**: `DevEUI`, `DevAddr`, `NwkSKey`, `AppSKey`
- **For ABP v1.1**: `DevEUI`, `DevAddr`, `NwkSEncKey`, `FNwkSIntKey`, `SNwkSIntKey`, `AppSKey`

#### Verify Profiles

Before adding a device, you need to create a **Device Profile** and a **Service Profile**.

- **Device Profile** defines how the device communicates with the **network server**, including its LoRaWAN version, region, and supported classes.
- **Service Profile** defines how the network server delivers messages to the **application server**, such as message frequency and delivery options.

You can use AWS-provided default profiles or create custom ones to match your device settings.

1. Navigate to the <a href="http://console.aws.amazon.com/iot" target="_blank">AWS IoT console.</a>
2. In the navigation pane, choose **LPWAN devices**, then click **Profiles**.
3. In the **Device Profiles** section, there are some pre-defined profiles listed.
4. Check each of the profiles to determine if one of them will work for you. If not, select **Add device profile** and set up the parameters as needed.

> **Image:** Add the Device Profile

5. Click **Add device profile** once you have set a device profile that will work for you.
6. In the **Service Profiles** section, click **Add service profile** and set up the parameters as needed. As an example, the default service profile parameters are shown below. However, only the ***Add gateway meta data*** setting can be changed at this time.

> **Image:** Add the Service Profile

7. Proceed only if you have a device and service profile that will work for you.

#### Set Up a Destination for Device Traffic

This guide uses a **RAK LoRaWAN device** as an example. In this scenario, the device is expected to send uplink data that will be **subscribed via MQTT** for visualization or processing. Therefore, we configure the destination to **publish to the AWS IoT Core message broker**.

However, if you're using a different device or application, you may need to configure your destination differently—such as routing data to an **IoT Rule**, **Lambda function**, or other AWS services.

1. Navigate to the **<a href="http://console.aws.amazon.com/iot" target="_blank">AWS IoT console</a>**.
2. In the navigation pane, choose **LPWAN devices**, and then **Destinations**.
3. Choose **Add Destination**.
4. Fill in the **Destination** details:
   - **Destination name**: `ProcessFieldTesterUplink` (or any name you prefer)
   - **Destination description - *optional:*** Provide a helpful description.
5. Select **Publish to AWS IoT Core message broker**. This allows the uplink messages to be published to an MQTT topic for other applications or services to consume.
6. Enter a topic such as ***RecvFieldTesterUplink*.** This option is required for MQTT-based tools such as the Field Tester Extension.
7. In the **Permissions** section, choose **Select an existing service role**, and pick the [IAM role](#add-iam-role-for-destination-to-aws-iot-core-for-lorawan) you created earlier.
8. Click **Add Destination**. A confirmation message will appear.

> **Image:** Add a Destination

#### Register the Device

Now, register an endpoint device with AWS IoT Core for LoRaWAN as follows.

1. In the navigation pane, go to **LPWAN Devices > Devices**.
2. Click **Add wireless device**.
3. On the **Add Device** page:
   - Select the LoRaWAN specification version in the drop-down under **Wireless device specification**.
   - Enter the **DevEUI**.
   - Fill in the **AppEUI/JoinEUI** and **AppKey** as per your OTAA settings.
   - Provide a wireless **Device name**.
   - Under Profiles, select the **Device Profile** and **Service Profile** you created earlier.
   - Under **Destination**, choose the one previously created.

> **Image:** Wireless device configuration

4. Click **Next**, then **Add device** to complete registration.

Once registered, the RAK device will begin sending periodic uplinks to the AWS IoT Core.

> **Image:** Joined Device

## The Things Network (TTN)

This tutorial illustrates how to configure and connect your RAK Gateway with WisGateOS 2 to a LoRaWAN Network Server by using the Basics Station protocol. For this example, it will be shown how to connect the gateway to TTNv3.

:::tip NOTE
LoRa Basics Station is an implementation of a LoRa packet forwarder. This protocol simplifies the management of large-scale LoRaWAN Networks. More information about the Basics Station protocol can be found in the <a href="https://blog.semtech.com/expert-series-5-things-you-need-to-know-about-lorawan-based-gateways" target="_blank">explanatory document</a> provided by Semtech.
:::

### Register the Gateway in TTN

1. Log in to the [TTNv3 website](https://id.thethingsnetwork.org/), then go to the [TTNv3 console](https://eu1.cloud.thethings.network/console). If you already have a TTN account, you can use your The Things ID credentials to log in.

> **Image:** The Things Stack Login Page

2. To register a commercial gateway, go to **Gateways** > **+ Register gateway**.

> **Image:** Go to register a gateway

3. You will be redirected to the **Register gateway** page.

4. In the **Gateway EUI** field, type the EUI of the gateway.

:::tip NOTE
- Check the label on the device casing marked as **GWEUI**.
- Or, log in to the gateway's Web UI and navigate to **Dashboard** > **Overview**.
:::

> **Image:** Register Gateway

5. After typing the EUI, click on **Confirm**. Additional fields will pop up. Fill in the following information:
- **Gateway ID**: This will be the unique ID of your gateway in the Network. An ID based on the EUI is automatically generated. You can change it if you need.

  :::tip NOTE
  The ID must contain only lowercase letters, numbers, and hyphens (-).
  :::

- **Gateway name**: Optionally, you can type a name for your gateway.

- **Frequency plan**: The frequency plan used by the gateway.

:::tip NOTE
- The other settings are optional and can be changed to satisfy your requirements.
- For this tutorial, we will use United States 902-928 MHz, FSB 2 (used by TTN).
:::

> **Image:** Add a gateway to TTN

6. To register your gateway, click **Register gateway**.

> **Image:** Successfully added a gateway

### Generate the Token in TTN

TTNv3 supports TLS server authentication and Client token, which requires a trust file and a key file to configure the gateway to successfully connect it to the network.

1. To generate a key file, from the **Overview** page of the registered gateway navigate to **API keys**.

2. On the **API keys page**, choose **+ Add API key**.

> **Image:** API key page

3. In the **Name** field, type the name of your key (for example - mykey). Choose **Grant individual rights** and select **Link as Gateway to a Gateway for traffic exchange, i.e. write uplink and read downlink**.

> **Image:** Configure the API key

4. To generate the key, choose **Create API key**. The following window will pop up, telling you to copy the key you just generated.

> **Image:** Copy the generated key

:::warning
Copy the key and save it in a `.txt` file (or other), because you won’t be able to view or copy your key after that.
:::

5. Click **I have copied the key** to proceed.

### Configure the Gateway for TTN

1. To configure the gateway, access it via the Web UI.
2. Navigate to **LoRa** > **Configuration** > **Work mode** and select **Basics station**.

> **Image:** Change the working mode

3. Expand the Basics Station settings by clicking **Configure Basics Station server setup** and configure the following parameters:

> **Image:** Expanded Basics Station settings

- **Basics Station Server Type**: For server type, choose **LNS Server**.
- **Server URL**: This is the link to The Things Stack server. Note that, for this tutorial, the gateway is connected to the European cluster. For Europe fill in the following:

```
wss://eu1.cloud.thethings.network
```

- **Server Port**: The LNS Server uses port `8887`.
- **Authentication Mode**: Choose **TLS server authentication and Client token**. When selected, the **Trust (CA Certificate)** and **Client token** fields will show up.
- **Trust (CA Certificate)**: For **Trust**, upload the **Let’s Encrypt ISRG ROOT X1 Trust** certificate by clicking **choose file**. The file with the certificate can be downloaded <a href="https://letsencrypt.org/certs/isrgrootx1.pem" target="_blank">directly.</a>
- **Client Token**: This is the generated API key.

4. To save the changes, click **Save Changes**.

If everything is set correctly, you can see the gateway is connected to TTNv3.

> **Image:** Successful connection

## ChirpStack

This guide shows you how to configure a **RAKwireless Commercial Gateway running WisGateOS 2** (e.g., RAK7266) to connect to a **ChirpStack Network Server**.

:::tip NOTE
+ This tutorial does **not cover** the installation or deployment of ChirpStack itself.
+ It assumes you already have a ChirpStack server deployed and accessible either locally or externally.
:::

The instructions here focus on configuring the gateway side to forward LoRaWAN data to ChirpStack. An **external ChirpStack v4 instance** is used as the example in this guide.

### ChirpStack Requirements

The firmware of your RAK gateway is WisGateOS 2 2.2.x or above

**Server-Side Port Configuration (Must Be Open on ChirpStack Server)**

| Port | Protocol | Required For                     | Notes                                 |
| ---- | -------- | -------------------------------- | ------------------------------------- |
| 1700 | UDP      | Semtech UDP Packet Forwarder     | Required for UDP mode gateways        |
| 1883 | TCP      | MQTT (unsecured)                 | If using MQTT Bridge                  |
| 8883 | TCP      | MQTT over TLS (secured)          | Recommended if using MQTT             |
| 3001 | TCP      | LoRa Basics Station (WebSocket) | Required only if using Basics Station |
| 8080 | TCP      | ChirpStack Web UI                | Required for browser-based access     |

:::tip NOTE
These ports must be **allowed in your firewall or cloud security group**, depending on your deployment method (e.g., AWS, DigitalOcean, local).
:::

### Register the Gateway in ChirpStack

1. To register the gateway in the ChirpStack Network server, access the ChirpStack UI. To do that, open a web browser and type the server address of the ChirpStack with port `8080`.

```
<IP address of ChirpStack>:8080
```

2. Login using the following credentials:
- Username/email: **admin**
- Password: **admin**

> **Image:** ChirpStack login page

3. On the left pane, head to **Gateways**.

> **Image:** Go to Gateways

4. To register one, click **Add gateway**.

> **Image:** Gateway list

5. In the **General** menu, you need to set the gateway parameters:

<!--
Broken image

> **Image:** Register the gateway
 -->

- **Name**: A unique identifier for the gateway within ChirpStack.
- **Description**: *(Optional)* A brief summary or label to help you recognize the gateway’s role or location.
- **Gateway ID (EUI64)**: The **Extended Unique Identifier** (EUI) of the gateway. You can find this value labeled as **GWEUI** on the physical sticker of the device or under **Dashboard > Overview** in the gateway’s Web UI.
- **Stats interval (secs)**:  The expected time interval (in seconds) at which the gateway reports its status and statistics to the server.

6. Click **Submit**. You will see the registered gateway in the gateway list.

> **Image:** Registered gateway

### Configure the Gateway for ChirpStack

The WisGateOS 2 gateway supports **three connection options** for connecting to ChirpStack. You may choose the method that best fits your deployment.
- Packet Forwarder (UDP)
- Packet Forwarder (MQTT Bridge)
- Basics Station (WebSocket)

#### Connect the Gateway via Packet Forwarder (UDP)

In this method, you will configure the gateway to use the **Semtech UDP Packet Forwarder** protocol to send uplink data to the **ChirpStack Gateway Bridge**.

:::tip NOTE
To enable communication between the gateway and the ChirpStack server, make sure the following ports are open on the ChirpStack host:

- **UDP port 1700**: Required for the Semtech Packet Forwarder protocol.
- **TCP port 8080**: Required to access the ChirpStack web interface.

Ensure these ports are allowed in your firewall or cloud security group.
:::

1. To configure the gateway, access it via the Web UI.

> **Image:** Login page

2. In the left sidebar, go to **LoRa**.
3. Under **Work Mode**, select **Packet forwarder**.
4. Then, under **Protocol**, click **Choose from the available protocols** to expand the settings.

> **Image:** Setting Packet Forwarder Mode

**Semtech UDP GWMP Protocol** is selected by default in Packet Forwarder mode.

5. Set the **Server Address** to your ChirpStack instance’s IP address or domain. In this case, the ChirpStack is installed on the AWS cloud instance with public IP **`18.156.176.220`** (yours will be different). The default ports that the packet forwarder is using are 1700.

> **Image:** Configure Packet Forwarder to ChirpStack

6. Click **Save changes** to save the changes.

If everything is set correctly, the gateway will display as online. You can click the gateway name to inspect the gateway traffic.

> **Image:** Registered gateway

> **Image:** Gateway details

#### Connect the Gateway via MQTT Bridge

In this method, you will configure the gateway’s built-in bridge to publish the data to the ChirpStack MQTT broker.

:::tip NOTE
To enable communication between the gateway and the ChirpStack server, ensure the following ports are open on the server:

- **TCP 1883**: Required for MQTT Broker communication.
- **TCP 8080**: Required to access the ChirpStack Web UI.
:::

1. To configure the gateway, access it via the Web UI.

> **Image:** Login page

2. In the left sidebar, go to **LoRa**.
3. Under **Work Mode**, select **Packet forwarder**.
4. Click **Choose from the available protocols** to expand the protocol options. Change the **Protocol** to **LoRa Gateway MQTT Bridge**.

> **Image:** LoRa Gateway MQTT bridge

5. Select **MQTT for ChirpStack 4.x (PROTOBUF)** as the MQTT protocol.

:::tip NOTE
+ The ChirpStack v3 supports both **MQTT for ChirpStack 3.x (JSON)** and **MQTT for ChirpStack 3.x (PROTOBUF)**. If you are using an earlier version of ChirpStack (v3), you need to choose one of the MQTT protocols to use.
+ If you want to use the JSON protocol, you need to change the payload marshaler in the gateway bridge `.toml` file to `.json`. By default, the marshaler is protobuf. To configure the payload marshaler, use the SSH client PuTTY to access the configuration files. How to do this is explained in the <a href="https://learn.rakwireless.com/hc/en-us/articles/26743884863767-How-To-Use-Amazon-Web-Services-with-LoRaWAN/?utm_source=docs_center&utm_medium=organic&utm_campaign=rak7266-documentation-lns-guide-page&utm_term=amazon-web-services-with-lorawan&utm_content=learn-link#accessing-instance-via-ssh" target="_blank">Amazon Web Services with LoRaWAN</a> guide on Learn site.
:::

6. To point the gateway to the ChirpStack network, you need to set the ChirpStack Broker address in the **MQTT Broker Address** field. In this case, the ChirpStack is installed on an AWS cloud instance with public IP `18.156.176.220` (yours will be different). The default port that the MQTT Broker uses is 1883.

> **Image:** Configure packet forwarder to ChirpStack

7. Click **Save changes** to save the changes.

If everything is set correctly, the gateway will display as online. You can click the gateway name to inspect the gateway traffic.

> **Image:** Registered gateway

> **Image:** Gateway details

#### Connect the Gateway via Basics Station

In this method, you will connect the gateway to the ChirpStack via Basics Station. The LoRa Basics Station is an implementation of a LoRa packet forwarder.

:::tip NOTE
To enable communication between the gateway and the ChirpStack server, make sure the following ports are open on the server:

- **TCP 3001**: Used for Basics Station WebSocket communication.
- **TCP 8080**: Used for accessing the ChirpStack Web UI.
:::

1. To configure the gateway, access it via the Web UI.

> **Image:** Login page

2. In the left sidebar, go to **LoRa**.
3. Under **Work Mode**, select **Basics Station**.
4. Click **Configure Basics Station server setup** to expand the server configuration panel.

> **Image:** Set Basics Station mode

- **Basics Station Server Type**: Choose **LNS Server**.
- **Server URL**: Enter the WebSocket address of your ChirpStack server. Example: `ws://18.156.176.220` *(replace with your actual IP)*

  :::tip NOTE
  + Use `ws://` for non-encrypted WebSocket connections.
  + Use `wss://` if you are using TLS, along with appropriate certificates (`tc.cert`, `tc.key`, `tc.trust`).
  :::

- **Server Port**: Enter `3001`.
- **Authentication Mode**: Select **No Authentication** for this setup.

> **Image:** Configure Basics Station to ChirpStack

5. Click **Save changes** to save the changes.
6. Configure ChirpStack Gateway Bridge for Basics Station.
   The default ChirpStack Gateway Bridge backend is configured for `semtech_udp`. You’ll need to update this to use `basic_station`.

  - Access the ChirpStack Server via SSH. Use an SSH terminal such as **PuTTY** to connect to your cloud instance. For guidance, refer to the <a href="https://learn.rakwireless.com/hc/en-us/articles/26743884863767-How-To-Use-Amazon-Web-Services-with-LoRaWAN/#accessing-instance-via-ssh" target="_blank">RAK Learn Site.</a>

      
> **Image:** PuTTY client

  - Go to the `/etc/chirpstack-gateway-bridge/` file path and open the `chirpstack-gateway-bridge.toml` file.
  - In the file, find the gateway backend configuration paragraph and replace the type with `basic_station`.

      
> **Image:** Configure gateway bridge type

  - Scroll down until you find the **Concentrator configuration** paragraph and uncomment the following text as shown below.

      
> **Image:** Configure gateway bridge backend

  - Save and exit the `.toml` file and restart the gateway bridge service to apply the changes by restarting the gateway bridge service with the following command:

      `sudo systemctl restart chirpstack-gateway-bridge.service`

Once everything is set up correctly, your gateway should show as **online** in the ChirpStack web interface.

> **Image:** Registered gateway

> **Image:** Gateway details

