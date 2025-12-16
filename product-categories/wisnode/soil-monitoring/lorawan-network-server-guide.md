---
slug: /product-categories/wisnode/soil-monitoring/lorawan-network-server-guide/
title: Soil Moisture, Temperature, and Electrical Conductivity Solution LoRaWAN Network Server Guide
description: Contains a comprehensive guide in setting up your Soil Moisture, Temperature, and Electrical Conductivity Solution to the LoRaWAN and the NB-IoT platforms. It also includes instructions in connecting and configuring your LoRaWAN Gateway with TTN and ChirpStack.
keywords:
- LoRaWAN Network Server Guide
- Sensor Hub
- Soil Monitoring
- TTN
- Datacake
- WisNode
image: https://images.docs.rakwireless.com/wisnode/soil-monitoring/soil-moisture.png
sidebar_label: LoRaWAN Network Server
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# Soil Moisture, Temperature, and Electrical Conductivity Solution LoRaWAN Network Server Guide

## Network Server and Visualization Configuration

This section outlines the operational steps for connecting the device to the network server in both the LoRaWAN and NB-IoT application scenarios.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/1-application-scenarios.png"
  width="80%"
  caption="Application scenarios"
/>

### LoRaWAN Application

#### Cloud Network Server Setup

The cloud network server deployment scenario involves connecting the gateway and devices to third-party cloud network servers. This server integrates visualization applications to manage real-time soil moisture, temperature, and EC data.

This section provides instructions on creating a Datacake visualization application using the TTN v3 cloud network server.


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/2-cloud-network-server-application-flow.png"
  width="80%"
  caption="Cloud Network Server Application Flow"
/>

##### Connect Gateway to TTN

For this example, you will use the TTNv3 cloud server and RAK7289 V2 WisGate Edge Lite 2 to demonstrate how to connect the RAK business gateway to a cloud server.

- **Register the Gateway**

1. Register an account and log in to the <a href="https://eu1.cloud.thethings.network/console/" target="_blank">TTN v3 website</a>. If you already have a TTN account, you can log in using your **The Things ID** credentials.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/3-the-things-stack-page.png"
  width="50%"
  caption="Log in to the TTN website"
/>

2. Once logged into the site, click on **Register a gateway** to begin the registration process for a new gateway.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/4-ttn-console-homepage.png"
  width="60%"
  caption="TTN home page"
/>

3. Input the Gateway EUI and then click on **Confirm** to proceed.

The Gateway EUI serves as a distinct 64-bit extended identifier for the gateway. It is accessible from the Overview page of the gateway management platform or the label situated behind the gateway.


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/5-gateway-eui.png"
  width="100%"
  caption="Enter the Gateway EUI"
/>

4. Choose the appropriate frequency plan used by the gateway, and click **Register gateway** to complete the registration process of the gateway.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/6-select-the-frequency-plan.png"
  width="100%"
  caption="Configure the Gateway frequency"
/>

Your gateway dashboard should look the same with **Figure 7**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/8-successfully-registered-the-gateway.png"
  width="100%"
  caption="Successfully registered the gateway"
/>

- **Generate a Token**

TTNv3 supports TLS server authentication and client tokens, which require trust files and keys to configure the gateway and successfully connect to the network. 

1. To generate a key file, navigate to **API keys** from the **Overview** page of the registered gateway, then click **Add API key**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/7-api-keys.png"
  width="100%"
  caption="Add API keys"
/>

2. In the **Add API key** page, set the **Name** field, tick off the checkboxes, then click **Create API key**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/9-add-api-key.png"
  width="100%"
  caption="Configure the API key"
/>

3. A new window pops up with the generated key. Copy the new API key by clicking the icon and then the **I have copied the key** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/10-enter-the-name-of-the-key.png"
  width="60%"
  caption="Copy and save the API key"
/>

**Configure the Gateway**

1. Navigate back to the gateway management platform Web UI. Click on the left navigation bar to access the **LoRa > Configuration** tab. Complete the following settings and save them.

- **Basics Station Server Type**: LNS Server
- **Server URL**: `wss://eu1.cloud.thethings.network`
- **Server Port**: `8887`
- **Authentication Mode**: TLS server & Client Token - Authentication
- **Trust (CA Certificate)**: Click the <a href="https://letsencrypt.org/certs/isrgrootx1.pem" target="_blank">link</a> to download.
- **Client Token**: Copied API Keys

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/12-configure-the-gateway.png"
  width="100%"
  caption="Configure the Gateway"
/>

2. After saving the changes, return to the TTN gateway interface, and navigate to the **Gateways** tab to confirm that the gateway is now connected to TTNv3 as a Basics Station.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/13-gateway-connected.png"
  width="100%"
  caption="Gateway connected Successfully"
/>

##### Connect Sensor Hub to TTN

1. Return to the TTNv3 homepage and select **Create an application** to add a node.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/14-create-an-application.png"
  width="60%"
  caption="Select create an application"
/>

2. Click **+ Create application** to initiate the creation of a node.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/15-create-application.png"
  width="100%"
  caption="Create a new application"
/>

3. Enter the desired **Application ID** in the provided field, then click on **Create application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/16-fill-in-the-application-id-field.png"
  width="100%"
  caption="Fill in the Application ID field"
/>

4. Click on the **+ Register end device** button to add a new end device to the application.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/17-register-end-device.png"
  width="100%"
  caption="Add the end device"
/>

5. Set the parameters of the end device, as shown in **Figure 17**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/18-set-the-parameters-of-the-end-device.png"
  width="100%"
  caption="End device parameters"
/>

- **JoinEUI**, **DevEUI**, and **AppKey** can be automatically generated by clicking **Generate** on the TTN web page. These parameters are customizable as well.

:::tip NOTE
Ensure that the three parameters - **JoinEUI**, **DevEUI**, and **AppKey** - are consistent with the parameters set in the WisToolBox application.
:::

6. After completing the settings, return to the WisToolBox app, and click **JOIN NETWORK** to send the end device network join request.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/19-send-network-access-request.png"
  width="35%"
  caption="Sending end device network join request"
/>

7. As shown in **Figure 19**, the Sensor Hub has successfully joined the TTNv3 network server.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/20-successfully-joined.png"
  width="100%"
  caption="Successfully joined the TTNv3 networks server"
/>

##### Visualize Data Through Datacake

Datacake is a versatile IoT platform. It offers a range of features tailored for effective data visualization and management, making it a preferred choice for IoT projects requiring efficient monitoring and analysis.

**Create Datacake Integration**

1. In the TTN console, navigate to **Integrations** on the sidebar, proceed to the **Webhooks** section, and then click **+Add webhooks** to set up an integration.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/21-add-webhooks.png"
  width="100%"
  caption="Adding an integration"
/>

2. From the list of webhook templates, select the **Datacake** template.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/22-select-the-datacake-template.png"
  width="100%"
  caption="Select the Datacake template"
/>

3. Generate an API key on Datacake to enable webhook authentication. To get started, register a <a href="https://datacake.co/" target="_blank">Datacake</a> account, and then log in.


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/23-datacake.png"
  width="100%"
  caption="Datacake IoT platform main page"
/>

4. Navigate to the Datacake workspace. Select **Members** on the sidebar, switch to the **API Users** tab, then click the **Add API User** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/24-add-api-user.png"
  width="100%"
  caption="Add API User"
/>

5. Enter the name of the API User, for instance, **TTS API**. Set the relevant parameters accordingly and click **Save** to finalize the creation process.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/25-set-the-relevant-parameters.png"
  width="80%"
  caption="Set parameters"
/>

6. Click the **Copy** button to copy the generated Datacake API Token.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/26-copy-the-generated-datacake-api-token.png"
  width="100%"
  caption="Copy the generated Datacake API Token"
/>

7. Back on the TTN website, enter **sensorhub** in the **Webhook ID** field (as an example), and paste the Datacake API Token you previously copied into the **Token** field. Click the **Create Datacake Webhook** button to generate the Datacake Webhook.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/27-create-datacake-webhook.png"
  width="100%"
  caption="Create Datacake Webhook"
/>

**Add Sensor Hub to Datacake**

1. To add a new device, select **Devices** in the sidebar and click the **+Add Device** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/28-add-device.png"
  width="100%"
  caption="Add Device"
/>

2. Choose **LoRaWAN** from the options and click **Next** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/29-select-lorawan.png"
  width="60%"
  caption="Select LoRaWAN"
/>

3. As the Sensor Hub is a new device, there is no pre-existing template. Create a template by clicking **New Product**, enter the **Product Name**, and click **Next** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/30-step-1.png"
  width="80%"
  caption="Create a new product"
/>

4. Choose a network server for your device. In this guide, select **The Things Stack V3**, then click **Next** to continue.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/31-step-2.png"
  width="80%"
  caption="Select the Things Stack V3"
/>

5. In the **STEP 3 Devices** tab, enter the device **DEVEUI** and **NAME** fields, and click **Next** to continue.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/32-step-3.png"
  width="80%"
  caption="Add DEVEUI and Name"
/>

6. In **Step 4 Plan**, select the preferred subscription plan, and click **Add 1 device** to add the device. For this example, choose **Free**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/33-step-4.png"
  width="80%"
  caption="Select a subscription plan"
/>

7. The registered device can now be viewed on the **Devices** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/34-device-registered.png"
  width="100%"
  caption="Registered Device"
/>

**Create a Payload Decoder**

1. Click the successfully registered device and go to the **Configuration** tab. Scroll down to the **Payload Decoder** field, then copy and save the decoder code.


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/35-create-payload-decoder-1.png"
  width="100%"
  caption="Configuration tab"
/>


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/36-create-payload-decoder-2.png"
  width="100%"
  caption="Decoder Code"
/>

<details>
<summary> Click to view the code </summary>

```js
function Decoder(bytes, port) {  
    var decoded = {};  
    var str = bin2HexStr(bytes);  
    var i = 0;  
    while (i < str.length) {  
        var channelId = parseShort(str.slice(i, i + 4), 16);  
        var value = parseShort(str.slice(i + 4, i + 8), 16);  
        i += 8;  
        switch (channelId) { 
            case 0x0167:  
                decoded.temperature = value / 10.0;  
                break;  
            case 0x0270:  
                decoded.humidity = value / 10.0;  
                break;  
            case 0x03C0:  
                decoded.electric_conductivity = value / 1000.0;  
                break;  
            default:  
                break;  
        }  
    }  
  
    try {  
        decoded.lorawan_rssi = (port && port.metadata && port.metadata.rssi) || 0;  
        decoded.lorawan_snr = (port && port.metadata && port.metadata.snr) || 0;  
        decoded.lorawan_datarate = (port && port.metadata && port.metadata.data_rate) || '';  
    } catch (e) {  
        console.log('Failed to read gateway metadata');  
    }  
  
    return decoded;  
}  
  
function bin2HexStr(bytesArr) {  
    var str = '';  
    for (var i = 0; i < bytesArr.length; i++) {  
        var tmp = (bytesArr[i] & 0xff).toString(16);  
        if (tmp.length == 1) {  
            tmp = '0' + tmp;  
        }  
        str += tmp;  
    }  
    return str;  
}  
  
// convert string to short integer  
function parseShort(str, base) {  
    var n = parseInt(str, base);  
    return (n << 16) >> 16;  
}  
  
// convert string to triple bytes integer  
function parseTriple (str, base) {
var n = parseInt (str, base);
    return (n << 8) >> 8;
}
```
</details>

2. Displace the menu bar to the **+Add Field** section, and click **+Add Field**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/37-add-field.png"
  width="100%"
  caption="Add Field"
/>

3. The **Add Field** window appears. Fill out the fields shown in **Figure 37** to configure the stored data in the device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/38-the-following-settings.png"
  width="60%"
  caption="Configuration fields"
/>


:::tip NOTE
- Enter a suitable name in the **Name** field.
- The **Identifier** field will be automatically filled in based on the name.
- When an uplink is received, refresh the page, and the **CURRENT VALUE** field will be updated.
- Leave everything else as default, and click **Add Field** to complete the setup.
:::

4. When completed, it will look the same, as shown in **Figure 38**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/39-added-fields.png"
  width="100%"
  caption="Successfully added fields"
/>

**Create a Dashboard**

1. To create a dashboard, click the **edit mode** switch on the **Dashboard** tab of the device on Datacake.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/40-create-a-dashboard.png"
  width="100%"
  caption="Turn on the edit mode switch"
/>

2. Click **+Add Widget** to add a visualization widget.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/41-add-widget.png"
  width="100%"
  caption="Add Visualization Widget"
/>

3. Select **Value** from the menu to create a new dashboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/42-select-value.png"
  width="80%"
  caption="Select Value to create a new dashboard"
/>

:::tip NOTE
You can select different types of widgets to accommodate various data formats.
:::

4. In the **Title** field under the **Basics** tab, name the widget as **Temperature**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/43-name-the-widget-in-the-title-field.png"
  width="60%"
  caption="Name the widget"
/>

5. Under the **Data** tab, click the **Field** tab dropdown arrow, select **Temperature**, and set the unit to **°C**.


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/44-setting-parameters.png"
  width="60%"
  caption="Set the unit"
/>

6. Under the **Gauge** tab, select the gauge type and color, set the range of values for the widget, and then click **Save**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/45-set-gauge.png"
  width="60%"
  caption="Set the widget type"
/>

7. To add another widget, ensure the **edit mode** switch is **ON**, then click the **+Add Widget** button again.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/46-added-widget.png"
  width="100%"
  caption="Added Widget"
/>

8. When you finish adding the widgets, turn off the **edit mode** switch to save the edits.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/48-save-the-edits.png"
  width="100%"
  caption="Save the edits"
/>

9. Return to the WisToolBox APP, and click **JOIN NETWORK** to send the end device network access request. Once the request is successfully returned, the data will be uploaded within 60 seconds.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/47-send-the-end-device-network-access-request.png"
  width="35%"
  caption="Send the end device network access request"
/>

#### Built-In Network Server Setup

The RAK gateway comes with a built-in NS, which eliminates the need to deploy NS in the cloud or locally. This gateway is suitable for small-sized industrial application scenarios and offers various advantages such as cost savings, reduced R&D investment, high execution efficiency, and shorter delays.

The built-in network server of the RAK gateway provides MQTT and HTTP integration that allows for post-processing data and implementing solutions based on the needs.

This section will use the public MQTT broker integration as an example to demonstrate how to use the built-in network server to create a visualization application on ThingsBoard.


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/49-gateway-built-in-server-application-flow.png"
  width="80%"
  caption="Gateway Built-in Server Application Flow"
/>

##### Configure the ThingsBoard

1. Log in to <a href="https://thingsboard.cloud/login" target="_blank">ThingsBoard</a>. If you don't have an account, <a href="https://thingsboard.cloud/signup" target="_blank">create one</a> before proceeding.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/50-sign-up-thingsboard.png"
  width="45%"
  caption="Sign up ThingsBoard"
/>

2. After successfully logging in, you will be directed to the ThingsBoard homepage.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/51-thingsboard-homepage.png"
  width="100%"
  caption="ThingsBoard homepage"
/>

3. Navigate through **Integration center > Integrations > Data converters** in the left navigation tree to create a data converter for the uplink.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/52-create-a-data-converter-for-the-uplink.png"
  width="100%"
  caption="Create a data converter for the uplink"
/>

4. Click the **Add Data Converter** icon and choose the **Create new converter** option.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/53-select-create-new-converter.png"
  width="35%"
  caption="Select Create new converter"
/>


5. Enter the name of the decoder in the **Name** field (for example, *Uplink decoder*), leave the **Type** field as **Uplink**, and select the **JavaScript** option.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/54-add-data-converter.png"
  width="45%"
  caption="Add Data Converter"
/>

6. Edit the decoder code by copying the following code into the edit box, then click **Add** to include the uplink decoder.

<details>
<summary> Click to view the code </summary>

```js
/** Decoder **/
// decode payload to string
var payloadStr = decodeToString (payload);
var data = JSON.parse(payloadStr).data;
var bytes = atob(data).split('').map(function (c) {
return c.charCodeAt(0);
});

var values = {};
let i = 0;
while (i < bytes.length) {
var channelId = (bytes[i] << 8) | bytes[i + 1];
var value = (bytes[i + 2] << 8) | bytes[i + 3];
i += 4;
switch (channelId) {
case 0x0167:
values.temperature = value / 10.0;
break;
case 0x0270:
values.humidity = value / 10.0;
break;
case 0x03C0:
values.electric_conductivity = value / 1000;
break;
default:
break;
}
}
var integrationName = 'MQTT Integration';
var deviceName = 'dev_ac1f09fffe0903ec';
var result = {
deviceName: deviceName,
attributes: {
integrationName: metadata['integrationName'],
temperature: values.temperature,
humidity: values.humidity,
pressure: values.electric_conductivity,
},
};

/** Helper functions **/

function decodeToString(payload) {
return String.fromCharCode.apply(String, payload);
}

return result;
```
</details>

7. Navigate to the **Integration Center > Integrations** menu and click the **Add Integration** icon to add the MQTT integration.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/55-add-the-mqtt-integration.png"
  width="100%"
  caption="Add the MQTT integration"
/>

8. Enter the name of the integration (for example, *MQTT Integration*) in the **Name** field and select **MQTT** in the Type drop-down menu. Click **Next** to continue.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/56-basic-settings.png"
  width="60%"
  caption="Fill in the integration name"
/>

9. In the **Uplink data converter** options, click **Select existing** to choose the previously created decoder (**Uplink Decoder**), then click **Next**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/57-select-the-created-decoder.png"
  width="60%"
  caption="Select the created decoder"
/>

10. In the **Downlink data converter** interface, no configuration is necessary and just click **Skip** to bypass this setup.
11. Configure connection options. **Host** is the MQTT broker address used for messages. The Host of the external MQTT broker used in this example is `broker.hivemq.com`. You can choose to use other brokers with a different Host.
12. Enter the address `broker.hivemq.com` in the **Host** field, with the port number `1883`. Click the **Add topic filter** button to configure the subscription topic.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/58-configure-the-connection-options.png"
  width="60%"
  caption="Configure the connection options"
/>

**Configure the subscription topic**

```
application/{{application_name}}/device/{{ device_EUI }}/join
application/{{application_name}}/device/{{device_EUI}}/rx
application/{{application_name}}/device/{{device_EUI}}/tx
application/{{application_name}}/device/{{device_EUI}}/ack
application/{{application_name}}/device/{{device_EUI}}/status
```

- **application_name**: The application ID created in the gateway.
- **device_EUI**: The device EUI of the end device.

13. Modify the parameter values corresponding to the topics based on the actual application created and the device used. After configuring the details, click the **Add** button to save and complete the settings.

:::tip NOTE
The values in the subscription topic must be all lowercase. For example, `application/1/device/0123456789abcdef/join`. 
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/59-configure-and-add-the-subscription-topics.png"
  width="60%"
  caption="Configure and add the subscription topics"
/>

##### Configure the Gateway

This section will use the <a href="https://store.rakwireless.com/products/rak7268-8-channel-indoor-lorawan-gateway?variant=42316475924678" target="_blank">RAK7268 V2 WisGate Edge Lite 2</a> as an example.

1. To access the gateway web management platform, refer to the <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#overview" target="_blank">WisGateOS V2 user manual</a> for details.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/60-web-ui.png"
  width="100%"
  caption="WisGate OS Web Management Platform"
/>

2. After successfully logging in, navigate to the **LoRa®** menu in the left navigation tree and set the **Work mode** of the gateway to the **Built-in network server**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/61-set-work-mode.png"
  width="100%"
  caption="Set the Work mode"
/>

3. Once done with the setting, click the **Applications** tab, then the **Add application** button. You can also click **add one now** text link to add a new application.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/62-applications-tab.png"
  width="100%"
  caption="Applications tab"
/>

4. Configure the following information: **Application name**, **Application description**, and **Application Type**.

- **Unified Application key**: Choose this option if all devices will use the same application key. Once selected, a field for the application key appears, where you can manually type in an application key or click the **Autogenerate** button to generate one.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/63-configure-the-application.png"
  width="100%"
  caption="Configure the Application"
/>



- After enabling the **Auto Add Device** option, configure the **Application EUI option**. The value needs to be consistent with the node value. Once you have verified the application EUI and key, the device will be added automatically to the application.


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/64-auto-add-device.png"
  width="60%"
  caption="Auto Add Device"
/>

:::tip NOTE
You can obtain the values by either querying the end device or generating it automatically and modifying the corresponding value of the device synchronously.
:::

5. Once you've completed the configuration, click on **Save Application** to add the new application.

6. In the application list, locate the newly created application and navigate to the **End devices** tab. If you've enabled the **Auto Add Device** function, the device will be automatically registered upon the addition request.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/65-end-devices-tab.png"
  width="100%"
  caption="End Device Tab"
/>

7. Click the **Add end device** button. In the **End device information** interface, fill in the following information:

- **Activation Mode**: Select the activation mode of the device, OTAA or ABP.
  - Choosing ABP mode creates two additional fields: **Application Session Key** and **Network Session Key**. 
  - In this example, use OTAA activation mode.
- **End device (group) name**: Enter the name of the end device or the group it belongs to.
- **End device description (optional)**: Optionally provide a description for the end device.
- **Class**: Select **Class A** for device’s operating mode.
- **Frame Counter Width**: Keep the default value.
- **LoRaWAN MAC Version**: The protocol version (v1.0.3) of the end device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/66-add-new-end-device.png"
  width="80%"
  caption="Add new end devices"
/>

8. After completing, click **Add end devices** to proceed to the next step.

9. In the **Adding end devices** interface, enter the device EUI in the **End Device EUI (Main)** field and select the **Add to End Devices list** button. Then click **Add end devices** to complete adding the end device.

:::tip NOTE
- The device EUI configured here must match the end device. You can either obtain it by querying the end device or entering one (1) EUI and synchronously updating the corresponding value of the end device.
- If the EUI is correct, the device will be displayed in the **End devices list**.
- If the EUI is incorrect, the device will be displayed in the **End devices with an error**.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/67-device-adding-page.png"
  width="80%"
  caption="Add the device to the device list"
/>

10. Click the **Add** button to confirm adding the device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/68-add-end-device-to-application.png"
  width="45%"
  caption="Confirm to add the end device"
/>

11. When finished, enter the **End devices** interface, where you can see the created end device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/69-connected-to-gateway-built-in-server.png"
  width="80%"
  caption="End Device Created"
/>

##### Connect the Sensor Hub to the Built-In Network Server

For specific configuration on how to connect SensorHub to the server, refer to **SensorHub Network Configuration > LoRaWAN Application Scenario**. 

Once completed, the device will join the network. As shown in Figure below, the end device **SensorHub** has successfully connected to the gateway's built-in server.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/65-end-devices-tab.png"
  width="100%"
  caption="End Device SensorHub has been connected"
/>

##### Configure the MQTT Integration

1. Go to the **LoRa® > Configuration > Integration Interface Parameters** section.
2. Toggle the **Enable Integration Interface** option and select **Generic MQTT** as the **Integration mode**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/70-set-up-mqtt-integration.png"
  width="60%"
  caption="Set Up MQTT Integration"
/>

3. In the **MQTT Broker Address** option, enter `broker.hivemq.com` then click **Save changes**.

4. After the device has joined and has been sending uplink data, check the uplink data in **ThingsBoard > Integrations > Your Integration > Events**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/71-uplink-data.png"
  width="100%"
  caption="View the gateway uplink data"
/>

##### Visualize Data Through ThingsBoard

1. After creating the data converter, integrating, and obtaining some data in the **Event** tab, check the automatically created devices based on the decoder in the **Entities** > **Devices** > **Groups** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/72-decoder-based-device.png"
  width="100%"
  caption="Check the device"
/>

2. Click the group named **All** in the **Device groups** menu to automatically create a decoder device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/73-decoder-based-device1.png"
  width="100%"
  caption="Automatically created decoder device" 
/>

3. Click the device and go to the **Attributes** tab, where you will see the node data.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/74-the-data-from the-end-device.png"
  width="100%"
  caption="Data Visualization"
/>

4. To visualize the data, simply select the values you wish to display, then click the **Show on widget** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/75-select-the-value.png"
  width="100%"
  caption="Select the value"
/>

5. On the next page, select the desired widget for the data from the **Current bundle** drop-down menu. In this example, select **Humidity**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/76-select-widget-for-data.png"
  width="100%"
  caption="Select widget for data"
/>

6. After selecting the widget, click **Add to dashboard** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/77-add-to-dashboard.png"
  width="100%"
  caption="Selecting a widget"
/>

7. The **Add widget to dashboard** window will appear. By default, there is no dashboard in the profile, so you need to select **Create new dashboard** and enter a name for the dashboard in the **new dashboard title** field. 

-  In this guide, name the dashboard ***sensorhub_soil_multparam***.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/78-create-new-dashboard.png"
  width="50%"
  caption="Enter the Dashboard name"
/>

8. After setting the dashboard name, click the **Add** button to add more widgets. Alternatively, check the **Open dashboard** option to automatically open the created dashboard after adding the widget.

:::tip NOTE
If the **Open** dashboard option is not selected, you can still easily view the added widgets via **Dashboard groups** > **All** > [**Group Name**].
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/79-dashboard.png"
  width="100%"
  caption="Dashboard created"
/>

9. You can visualize other data from the device following the same steps as above. The only difference is that when adding the widget, instead of **Create a new dashboard**, click **Select existing dashboard**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/80-visualization-completed.png"
  width="100%"
  caption="Adding widgets"
/>

### NB-IoT/LTE CAT-M1 Application

#### Connect Sensor Hub to MQTT Server

In the **Network Server and Visualization Configuration** section, the server has been set as a public MQTT broker: `broker.hivemq.com`. You can also choose other brokers or servers, such as AWS IoT Core (optional), according to the actual usage scenario. 

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/81-nb-iotlte-cat-m1-application-scenario.png"
  width="80%"
  caption="NB-IoT LTE CAT-M1 Application Scenario"
/>

#### Visualize Data Through Datacake

In this example, you will use Datacake as the visualization platform. Datacake is a versatile IoT platform designed to visualize data from nodes in a user-friendly manner.

To get started, create an account on the <a href="https://datacake.co/" target="_blank">official website</a> and log in.

##### Add Sensor Hub to Datacake

1. After logging in to your account, navigate to the **Devices** tab and click **+ Add Device** to proceed with adding the Sensor Hub end device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/82-log-into-the-datacake.png"
  width="100%"
  caption="Add the end device, SensorHub"
/>

2. Select the **API** option and click **Next** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/83-add-device-to-datacake.png"
  width="60%"
  caption="Select API"
/>

3. As the device is new and there's no ready-made template, choose **New Product** from the **Datacake Product** options. Enter the device name in the **Product Name** field, then click **Next** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/84-select-new-product.png"
  width="80%"
  caption="Select New Product"
/>

4. The **SERIAL NUMBER** field can be left blank. Datacake will randomly generate a serial number for the device, then click **Next**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/85-keep-the-serial-number.png"
  width="80%"
  caption="Keep the serial number"
/>

5. Select the preferred subscription plan, then click **Add 1 device**. For this example, choose **Free**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/86-select-a-subscription-plan.png"
  width="80%"
  caption="Select a subscription plan"
/>

6. The registered device can now be viewed on the **Devices** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/87-registered-device.png"
  width="100%"
  caption="Registered Device"
/>

##### MQTT Configuration

1. Click the name of the device you just created in the list to enter the interface, then select the **Configuration** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/88-dashboard-page.png"
  width="100%"
  caption="Configuration Tab"
/>

2. Scroll down to the **API Configuration** option and copy the **Serial number**. Save it locally for later use.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/89-copy-the-serial-number.png"
  width="100%"
  caption="Copy the serial number"
/>

3. Continue scrolling down to the **MQTT Configuration** option and configure the external MQTT Broker.

4. Click **+Add new MQTT server** and configure the relevant parameters.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/90-configure-the-external-mqtt-broker.png"
  width="100%"
  caption="Configure the external MQTT broker"
/>

5. Fill in the relevant information based on the actual server used, then click **Test Connection** to verify whether Datacake can successfully connect to the **MQTT Broker**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/91-configure-the-relevant-parameters.png"
  width="60%"
  caption="Configure the relevant parameters"
/>

:::tip NOTE
If SSL/TLS encryption and authentication are set for more secure communication, ensure to configure them accordingly in this section. However, for this example, you can skip this option.
:::

6. If the connection is successful, you will see the message **Connection successful**. Click **Add MQTT Server** to complete the addition of the MQTT server.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/92-configure-the-relevant-parameters.png"
  width="100%"
  caption="Configure the relevant parameters"
/>

7. After successfully adding the MQTT server, click on **+Add Uplink Decoder** to add a decoder.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/93-add-uplink-decoder.png"
  width="100%"
  caption="Add Uplink decoder"
/>

8. A new window will appear, and fill in the fields according to your project.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/94-add-uplink-decoder.png"
  width="60%"
  caption="Add Uplink Decoder"
/>

- **Subscribe to topics**: Configure the subscription topics, that is, the value of the **Publish Topic** configured in the **Network Server and Visualization Configuration** section.
- **Decoder function**: Copy the following decoding code and paste it into the **Decoder function** space.

```js
function Decoder(topic, payload) {
var decoded = [];
var data = JSON.parse ( payload .replace (/\s*/g,"") );
for (var key in data) {
        decoded. push (
{
device: "ddc5e012-30e4-4091-a050-b7318bacb209",
field: key,
value: data[key]
}
)
}
return decoded;
} 
```

:::tip NOTE
In the above code, make sure that the parameter **serial_number** (device: `9f05fd20-56b0-4eca-8549-fe544d783056`) matches the serial number saved locally earlier.
:::

9. Once completed, click **Add uplink decoder**.
10. In the **Fields** option, click **+Add Field** to show the monitoring values of the devices. Each device can create a certain number of fields, also known as a **data point**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/95-add-field1.png"
  width="100%"
  caption="Add Field"
/>

11. Set the necessary parameters of the **Field**. For **Fields** with multiple data points, add them one by one. Once done, click **Add Field**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/96-related-parameters.png"
  width="45%"
  caption="Set the related parameters of the field"
/>

:::tip NOTE
The **Identifier** field will be automatically filled based on the name.
:::

12. Once the uplink data is received, the **Current value** column in the **Fields** list will display the current monitoring value from the sensor.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/97-sensor-monitoring-values.png"
  width="100%"
  caption="Added sensor monitoring values"
/>


##### Create a Dashboard to Visualize Data

**Dashboards** can be customized depending on the specific needs and preferences of a project. Follow the steps below to add widgets and visualize the data.

1. On the device details page, navigate to the **Dashboard** tab, then toggle on the edit mode switch.
2. Click on the **+ Add Widget** button to add a widget for visualizing data.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/98-open-edit-mode.png"
  width="100%"
  caption="Open the edit mode"
/>

3. Choose what type of widgets you want to display. For this example, select **Value** to visualize temperature monitoring values.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/42-select-value.png"
  width="60%"
  caption="Select and add widgets for visualizing data"
/>

4. Go to the **Data** tab and choose the data you want to visualize from the available **Field** options. For this example, select **Temperature** and set the unit of the field to **°C**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/100-data-tab.png"
  width="45%"
  caption="Select the visualization data field"
/>

5. After configuring the widget, click **Save**. You should now see the successfully created **Temperature** widget on the Dashboard interface.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/101-created-widget.png"
  width="100%"
  caption="Successfully created Temperature widget"
/>

6. To add more parameter widgets, click the **+Add Widget** button again with the edit mode toggle switch **ON**, then repeat **Steps 3-5**.

7. Once done with the dashboard configuration, turn off the **edit mode** switch to save the settings.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/soil-monitoring/lorawan-network-server/102-save-the-settings.png"
  width="100%"
  caption="Weather Station data visualization"
/>

<RkBottomNav/>