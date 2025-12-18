---
slug: /product-categories/wisnode/water-ph-monitoring/lorawan-network-server-guide/
title: Water pH Sensor LoRaWAN Network Server Guide
description: Provides comprehensive information to connect it to various LoRaWAN network servers and display data on IoT platforms.
keywords:
  - wisnode
  - Sensor Hub
  - TTN
  - Datacake
  - LoRaWAN
  - Water pH
image: https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/waterphsolution.png
sidebar_label: LoRaWAN Network Server
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# Water pH Sensor LoRaWAN Network Server Guide

## Network Server and Visualization Configuration

This section outlines the operational steps for connecting the device to the network server in both the LoRaWAN and NB-IoT application scenarios.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f1application_scenarios.png"
  width="80%"
  caption="LoRaWAN Application Scenarios"
/>

### LoRaWAN Application

#### Cloud Network Server Setup

The cloud network server deployment scenario involves connecting the gateway and devices to third-party cloud network servers. This setup integrates visualization applications to manage real-time Water pH data.

This section provides instructions on creating a Datacake visualization application using the TTN v3 cloud network server.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f2cloudnetworkserver.png"
  width="80%"
  caption="Cloud network server deployment solution"
/>

##### Connect Gateway to TTN

For this example, you will use the TTNv3 cloud server and RAK7289V2 WisGate Edge Lite 2 to demonstrate how to connect the RAK business gateway to a cloud server.

- **Register the Gateway**

1. Register an account and log in to the [TTN v3 website.](https://eu1.cloud.thethings.network/console/) If you already have a TTN account, you can log in with your **The Things ID** credentials.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f3waterphsolution_lns_ttn1.png"
  width="50%"
  caption="Log in to the TTN website"
/>

2. Once logged into the site, click on **Register a gateway** to begin the registration process for a new gateway. 

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f4waterphsolution_lns_ttn2.png"
  width="50%"
  caption="TTN home page"
/>

3. Input the Gateway EUI and then click on **Confirm** to proceed. 

The Gateway EUI serves as a distinct 64-bit extended identifier for the gateway, accessible from the Overview page of the gateway management platform or from the label situated behind the gateway.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f5waterphsolution_lns_ttn3.png"
  width="100%"
  caption="Enter the Gateway EUI"
/>

4. Choose the appropriate frequency plan used by the gateway, and click **Register gateway** to complete the registration process of the gateway.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f6waterphsolution_lns_ttn4.png"
  width="100%"
  caption="Configure the gateway frequency"
/>

**Generate Token**

TTNv3 supports TLS server authentication and client tokens, which require trust files and keys to configure the gateway and successfully connect to the network. 

1. To generate a key file, navigate to **API keys** from the **Overview** page of the registered gateway, then click on **Add API key**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f8waterphsolution_lns_ttn6.png"
  width="100%"
  caption="Add API keys"
/>

2. In the **Add API key** page, set the **Name** field, tick of the checkboxes shown in **Figure 8**, then click **Create API key**. 

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f9waterphsolution_lns_ttn7.png"
  width="100%"
  caption="Configure the API Key"
/>

3. A new window pops up with the generated key. Copy the new API key by clicking the icon and then the **I have copied the key** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f10waterphsolution_lns_ttn8.png"
  width="60%"
  caption="Copy and save the API Key"
/>

**Register the Gateway**

1. Navigate back to the gateway management platform Web UI. Click on the left navigation bar to access the **LoRa > Configuration** tab. Complete the following settings and save them.

- **Basics Station Server Type**: LNS Server
- **Server URL**: `wss://eu1.cloud.thethings.network`
- **Server Port**: `8887`
- **Authentication Mode**: TLS server & Client Token Authentication
- **Trust (CA Certificate)**: Download the [certificate](https://letsencrypt.org/certs/isrgrootx1.pem)
- **Client Token**: Copied API Keys

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f11waterphsolution_lns_ttn9.png"
  width="100%"
  caption="Configure the gateway"
/>

2. After saving the changes, return to the TTN gateway interface, and navigate to the **Gateways** tab to confirm that the gateway is now connected to TTNv3 as a Basics Station.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f12waterphsolution_lns_ttn10.png"
  width="100%"
  caption="Gateway connected successfully"
/>

##### Connect Sensor Hub to TTN

1. Return to the TTNv3 homepage and select **Create an application** to add a node.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f13waterphsolution_lns_ttn11.png"
  width="70%"
  caption="Select Create An Application"
/>

2. Click **+ Create application** to initiate the creation of a node.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f14waterphsolution_lns_ttn12.png"
  width="100%"
  caption="Create a new application"
/>

3. Enter the desired **Application ID** in the provided field, then click on **Create application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f15waterphsolution_lns_ttn13.png"
  width="100%"
  caption="Enter the application ID"
/>

4. Click on the **+Register end device** button to add a new end device to the application.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f16waterphsolution_lns_ttn14.png"
  width="100%"
  caption="Add the end device"
/>

5. Set the parameters of the end device, as shown in **Figure 16**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f17waterphsolution_lns_ttn15.png"
  width="100%"
  caption="End device parameters"
/>

- **JoinEUI**, **DevEUI**, and **AppKey** can be automatically generated by clicking **Generate** on the TTN web page or customized by the user.

:::tip NOTE
Ensure that the three parameters - **JoinEUI**, **DevEUI**, and **AppKey** - are consistent with the parameters set in the WisToolBox application.
:::

6. After completing the settings, return to the WisToolBox app, and click **JOIN NETWORK** to send the end device network access request.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f18waterphsolution_lns_ttn16.png"
  width="25%"
  caption="Sending end device network join request"
/>

7. As shown in **Figure 18**, the Sensor Hub has successfully joined the TTNv3 network server.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f19waterphsolution_lns_ttn17.png"
  width="100%"
  caption="Successfully joined the TTNv3 network server"
/>

##### Visualize Data Through Datacake

Datacake is a versatile IoT platform. It offers a range of features tailored for effective data visualization and management, making it a preferred choice for IoT projects requiring efficient monitoring and analysis.

**Create Datacake Integration**

1. In the TTN console, navigate to **Integrations** on the sidebar, proceed to the **Webhooks** section, and then click **+Add Webhooks** to set up an integration.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f20waterphsolution_lns_ttn18.png"
  width="100%"
  caption="Adding an integration"
/>

2. From the list of webhook templates, select the **Datacake** template.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f21waterphsolution_lns_ttn19.png"
  width="100%"
  caption="Select the Datacake template"
/>

3. Generate an API key for webhook authentication on Datacake. To get started, register a [Datacake](https://datacake.co/) account, and then log in.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f22waterphsolution_lns_dc1.png"
  width="100%"
  caption="Log in to the Datacake IoT platform"
/>

4. Navigate to the Datacake workspace. Select **Members** on the sidebar, and switch to the **API Users** tab, then click the **Add API User** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f23waterphsolution_lns_dc2.png"
  width="100%"
  caption="Add API User"
/>

5. Enter the name of the API User, for instance, **TTS API**. Set the relevant parameters accordingly and click **Save** to finalize the creation process.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f24waterphsolution_lns_dc3.png"
  width="50%"
  caption="Set Parameters"
/>

6. Click the **Copy** button to copy the generated Datacake API Token.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f25waterphsolution_lns_dc4.png"
  width="100%"
  caption="Copy the generated Datacake API Token"
/>

7. Back on the TTN website, enter **sensorhub** in the **Webhook ID** field (as an example), and paste the Datacake API Token you previously copied into the **Token** field. Click the **Create Datacake Webhook** button to generate the Datacake Webhook.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f26waterphsolution_lns_dc5.png"
  width="100%"
  caption="Create the Datacake Webhook"
/>

**Add Sensor Hub to Datacake**

1. To add a new device, select **Devices** in the sidebar and click the **+Add Device** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f27waterphsolution_lns_dc6.png"
  width="100%"
  caption="Add a Device"
/>

2. Choose **LoRaWAN** from the options and click **Next** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f28waterphsolution_lns_dc7.png"
  width="50%"
  caption="Choose LoRaWAN connectivity"
/>

3. As the Sensor Hub is a new device, there is no pre-existing template. Create a template by clicking **New Product**, enter the **Product Name**, and click **Next** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f29waterphsolution_lns_dc8.png"
  width="50%"
  caption="Create a New Product"
/>

4. Choose a network server for your device. In this guide, select **The Things Stack V3**, then click **Next** to continue.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f30waterphsolution_lns_dc9.png"
  width="50%"
  caption="Select the Things Stack V3"
/>

5. In the **Step 3 Devices** tab, enter the device **DEVEUI** and **NAME** fields, and click **Next** to continue.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f31waterphsolution_lns_dc10.png"
  width="50%"
  caption="Add DEVEUI and Name"
/>

6. In **Step 4 Plan**, select the preferred subscription plan, and click **Add 1 device** to add the device. For this example, choose **Free**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f32waterphsolution_lns_dc11.png"
  width="50%"
  caption="Select a subscription plan"
/>

7. The registered devices can now be viewed on the **Devices** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f33waterphsolution_lns_dc12.png"
  width="100%"
  caption="Registered device"
/>

**Create a Payloader Decoder**

1. Click the successfully registered device and go to the **Configuration** tab. Scroll down to the **Payload Decoder** field, then copy and save the decoder code.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f34pwaterphsolution_lns_dc13.png"
  width="100%"
  caption="Configuration tab"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f35waterphsolution_lns_dc14.png"
  width="100%"
  caption="Decoder code"
/>

<details>
<summary> Click to view the example </summary>
````js
function Decoder(bytes, port) {
var decoded = {};


function value(bytes) {
var value = (bytes[1] << 8) | bytes[0];
value = twosComplement (value, 16);
return value;
}


  var offset = 0;
  while (offset < bytes.length) {
    var channel_id = bytes[offset++];
    var channel_type = bytes[offset++];
    if (channel_id === 0x15 && channel_type === 0xC1) {
      var PH = (bytes[offset++] * 256 + bytes[offset++]) / 100;
      decoded.PH = PH.toFixed(1);
    } else {
      break;
    }
  }


  return decoded;
}
````

</details>

2. Displace the menu bar to the **+Add Field** section and click **+Add Field**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f36waterphsolution_lns_dc15.png"
  width="100%"
  caption="Add Field"
/>

3. The **Add Field** window appears. Fill out the fields shown in **Figure 36** to configure the stored data in the device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f37waterphsolution_lns_dc16.png"
  width="50%"
  caption="Configuration fields"
/>

:::tip NOTE
- Enter an appropriate name in the Name field.
- The **Identifier** field will be automatically filled based on the name.
- When an uplink is received, refresh the page, and the **CURRENT VALUE** field will be updated.
- Leave everything else as default, and click **Add Field** to complete the setup.
:::

3. When completed, it will look the same, as shown in **Figure 37**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f38waterphsolution_lns_dc17.png"
  width="100%"
  caption="Successfully added fields"
/>

**Create a Dashboard**

1. To create a dashboard, toggle the **edit mode** switch on the **Dashboard** tab of the device in Datacake.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f39waterphsolution_lns_dc18.png"
  width="100%"
  caption="Turn on the edit mode switch"
/>

2. Click **+Add Widget** to include a visualization widget.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f40waterphsolution_lns_dc19.png"
  width="100%"
  caption="Add visualization widget"
/>

3. Select **Value** from the menu to create a new dashboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f41waterphsolution_lns_dc20.png"
  width="50%"
  caption="Select Value to create a new dashboard"
/>

:::tip NOTE
You can select various types of widgets to accommodate different data formats.
:::

4. In the **Title** field under the **Basics** tab, name the widget, for example, *PH*.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f43waterphsolution_lns_dc22.png"
  width="50%"
  caption="Name the Widget"
/>

5. Under the **Data** tab, click the Field dropdown arrow, select **Water pH**, and set the unit to **pH**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f42waterphsolution_lns_dc21.png"
  width="50%"
  caption="Setting Parameters"
/>

6. Under the **Gauge** tab, select the gauge type and color, set the range of values for the widget, and then click **Save**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f44waterphsolution_lns_dc23.png"
  width="50%"
  caption="Set Gauge"
/>

7. When you finish adding the widgets, turn off the **edit mode** switch to save the edits.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f45waterphsolution_lns_dc24.png"
  width="100%"
  caption="Added Widget"
/>

#### Built-In Network Server Setup

The RAK gateway comes with a built-in NS, which eliminates the need to deploy NS in the cloud or locally. This gateway is suitable for small-sized industrial application scenarios and offers various advantages such as cost savings, reduced R&D investment, high execution efficiency, and shorter delays.

The built-in network server of the RAK gateway provides MQTT and HTTP integration that allows for post-processing data and implementing solutions based on the needs.

This section will use the public MQTT broker integration as an example to demonstrate how to use the built-in network server to create a visualization application on ThingsBoard.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f46built-inserve applicationflow.png"
  width="80%"
  caption="Gateway built-in NS application scenario"
/>

##### Configure the ThingsBoard

1. Log in to [ThingsBoard.](https://thingsboard.cloud/login) If you don't have an account yet, [create one](https://thingsboard.cloud/signup) before proceeding.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f47waterphsolution_lns_tb1.png"
  width="40%"
  caption="ThingsBoard authentication page"
/>

2. After successfully logging in, you will be directed to the ThingsBoard homepage.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f48waterphsolution_lns_tb2.png"
  width="100%"
  caption="ThingsBoard Homepage"
/>

3. Navigate to the **Integration center > Data converter** menu bar to create a data converter for the uplink.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f49waterphsolution_lns_tb3.png"
  width="100%"
  caption="Create a Data Converter"
/>

4. Click on the **Add Data Converter** icon and choose the **Create new converter** option.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f50waterphsolution_lns_tb4.png"
  width="40%"
  caption="Create a new Converter"
/>

5. Enter the name of the decoder in the **Name** field (for example, *Uplink decoder*), leave the **Type** field as **Uplink**, and select the **JavaScript** option.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f51waterphsolution_lns_tb5.png"
  width="50%"
  caption="Add the decoder code"
/>

6. Edit the decoder code by copying the following code into the edit box. Then, click **Add** to include the uplink decoder.

<details>
<summary> Click to view the example </summary>
````js

/** Decoder **/
// decode payload to string
var payloadStr = decodeToString (payload);
var data = JSON.parse ( payloadStr ).data;
var bytes = atob (data).split('').map(function(c) {
return c.charCodeAt (0);
});


var values = {};
let i = 0;
  while (i < bytes.length) {
    var channelId = (bytes[i] << 8) | bytes[i + 1];
    var value;
    if (channelId === 0x15C1) {
      value = (bytes[i + 2] * 256 + bytes[i + 3]) / 100;
      i += 4;
      values.ph = value;
    }  else {
      break;
    }
  }


  var integrationName = 'MQTT Integration';
  var deviceName = 'sensorhub_ph';
  var result = {
    deviceName: deviceName,
    attributes: {
      integrationName: metadata['integrationName'],
      ph: values.ph,},
  };


  /** Helper functions **/


  function decodeToString(payload) {
return String.fromCharCode.apply (String, payload);
}


return result;
````

</details>

7. Navigate to the **Integration Center > Integrations** menu and click the **Add Integration** icon to add the MQTT integration.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f52waterphsolution_lns_tb6.png"
  width="100%"
  caption="Add the MQTT Integration"
/>

8. Enter the name of the integration (for example, *MQTT Integration*) in the **Name** field and select **MQTT** in the Type drop-down menu. Click **Next** to continue.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f53waterphsolution_lns_tb7.png"
  width="50%"
  caption="Basic Settings"
/>

9. In the **Uplink data converter** options, click **Select existing** to choose the previously created decoder (**Uplink Decoder**), then click **Next**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f54waterphsolution_lns_tb8.png"
  width="50%"
  caption="Select the created decoder"
/>

10. In the **Downlink data converter** interface, no configuration is necessary. Simply click **Skip** to bypass this setup.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f55waterphsolution_lns_tb9.png"
  width="50%"
  caption="WisGate OS Web Management Platform"
/>

11. Configure connection options. **Host** is the MQTT broker address used for messages. The Host of the external MQTT broker used in this example is `broker.hivemq.com`. You can choose to use other brokers with a different Host.


12. Enter the address `broker.hivemq.com` in the **Host** field, with the port number `1883`. Click the **Add topic filter** button to configure the subscription topic:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f56waterphsolution_lns_tb10.png"
  width="50%"
  caption="WisGate OS Web Management Platform"
/>

````
application/{{ application_name }}/device/{{ device_EUI }}/join
application/{{ application_name }}/device/{{ device_EUI }}/ rx
application/{{ application_name }}/device/{{ device_EUI }}/ tx
application/{{ application_name }}/device/{{ device_EUI }}/ack
application/{{ application_name }}/device/{{ device_EUI }}/status
````

- **application_name**: the aapplication ID created in the gateway.
- **device_EUI**: the device EUI of the end device.

Modify the parameter values corresponding to the topics based on the actual application created and the device used.

:::tip NOTE
The values in the subscription topic must be all lowercase. For example, *application/1/device/0123456789abcdef/join*. 
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f56-1waterphsolution_lns_tb10-1.png"
  width="50%"
  caption="WisGate OS Web Management Platform"
/>

13.  After configuring the details, click on **Add** to save and complete the settings.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f56-2waterphsolution_lns_tb10-2.png"
  width="100%"
  caption="WisGate OS Web Management Platform"
/>

##### Configure the Gateway

This section will use [RAK7268 V2 WisGate Edge Lite 2](https://store.rakwireless.com/products/rak7268-8-channel-indoor-lorawan-gateway?variant=42316475924678) as an example.

1. To access the gateway web management platform, refer to the [WisGateOS V2 User Manual](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/) for details.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f57waterphsolution_lns_tb11.png"
  width="80%"
  caption="WisGate OS Web Management Platform"
/>

2. After successfully logging in, navigate to the **LoRa®** menu in the left navigation tree. Set the **Work mode** of the gateway to **Built-in network server**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f58waterphsolution_lns_tb12.png"
  width="100%"
  caption="Set the Work mode of the gateway"
/>

3. Once done with the setting, click the **Applications** tab, then the **Add application** button. You can also click **add one now** text link to add a new application.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f59waterphsolution_lns_tb13.png"
  width="100%"
  caption="Applications Tab"
/>

4. Configure the following information: **Application name**, **Application Description**, and **Application Type**.

- **Unified Application key**: Choose this option if all devices will use the same application key. Once selected, a field for the application key appears, where you can manually type in an application key or click the **Autogenerate** button to generate one.


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f60waterphsolution_lns_tb14.png"
  width="60%"
  caption="Unified Application Key"
/>

- After enabling the Auto Add Device option, configure the **Application EUI option**. The value needs to be consistent with the node value. Once you have verified the application EUI and key, the device will be added automatically to the application.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f61waterphsolution_lns_tb15.png"
  width="60%"
  caption="Auto Add Device"
/>

:::tip NOTE
You can obtain the values by either querying the end device or generating it automatically and modifying the corresponding value of the device synchronously.  
:::

- **Separate Application keys**: Each device has its own application key. Add the key when registering the device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f62waterphsolution_lns_tb16.png"
  width="60%"
  caption="Add Application Key"
/>

5. Once you've completed the configuration, click on **Save Application** to add the new application.

6. In the application list, locate the newly created application and navigate to the **End devices** tab. If you've enabled the **Auto Add Device** function, the device will be automatically registered upon the addition request.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f63waterphsolution_lns_tb17.png"
  width="100%"
  caption="End Devices Tab"
/>

7. Click the **Add end device** button. In the **End device information** interface, fill in the following information:

- **Activation Mode:** Select the activation mode of the device: OTAA or ABP. 
  - Choosing ABP mode creates two additional fields: **Application Session Key** and **Network Session Key**. 
  In this example, you’re using OTAA activation mode.
- **End device (group) name**: Enter the name of the end device or the group it belongs to.
- **End device description (optional)**: Optionally provide a description for the end device.
- **Class:** Select **Class A** for the device's operating mode.
- **Frame Counter Width:** Maintain the default value.
- **LoRaWAN MAC Version:** The protocol version (V1.0.3) of the node.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f64waterphsolution_lns_tb18.png"
  width="60%"
  caption="Add new end devices"
/>

8. After completing, click **Add end devices** to proceed to the next step.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f64-1waterphsolution_lns_tb18-1.png"
  width="70%"
  caption="Add the device to the device list"
/>

9. In the **Adding end devices** interface, enter the device EUI in the **End Device EUI (main)** field and select the **Add to End Devices list** button. Then click **Add end devices** to complete adding the end device.

:::tip NOTE
- The device EUI configured here must match the end device. You can either obtain it by querying the end device or entering one (1) EUI and synchronously updating the corresponding value of the end device.
- If the EUI is correct, the device will be displayed in the **End devices list**.
- If the EUI is incorrect, the device will be displayed in the **End devices with an error**.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f65waterphsolution_lns_tb19.png"
  width="70%"
  caption="Complete the end device addition"
/>

10. Click the Add button to confirm adding the device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f66waterphsolution_lns_tb20.png"
  width="50%"
  caption="Confirm to add the end device"
/>

11. When finished, you will enter the **End devices interface**, where you can see the created end device.

##### Connect Sensor Hub to Built-In Network Server

For specific configuration on how to connect SensorHub to the server, please refer to **SensorHub Network Configuration > LoRaWAN Application Scenario**. Once completed, the device will join the network. As shown in **Figure 69**, the end device SensorHub has successfully connected to the gateway's built-in server.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f67waterphsolution_lns_tb21.png"
  width="80%"
  caption="End device  SensoHub has been connected"
/>

##### Configure MQTT Integration

1. Navigate to the **LoRa® > Configuration > Integration Interface Parameters** section.

2. Enable the **Enable Integration Interface** option and select **Generic MQTT** as the **Integration mode**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f68waterphsolution_lns_tb22.png"
  width="50%"
  caption="Set up MQTT integration"
/>

3. In the **MQTT Broker Address** option, enter `broker.hivemq.com` then click **Save changes**.

4. After the device has joined and has been sending uplink data, check the uplink data in **ThingsBoard > Integrations > Your Integration > Events**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f69waterphsolution_lns_tb23.png"
  width="100%"
  caption="View the gateway uplink data"
/>

##### Visualize Data Through ThingsBoard

1. After creating the data converter, integrating, and obtaining some data in the **Event** tab, check the automatically created devices based on the decoder in the **Entities > Devices > Groups** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f70waterphsolution_lns_tb24.png"
  width="100%"
  caption="Check the device"
/>

2. Click the group named **All** in the **Device groups** menu to automatically create a decoder device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f71waterphsolution_lns_tb25.png"
  width="100%"
  caption="Automatically created decoder device"
/>

3. Click the device, and navigate to the **Attributes** tab, and check on the node data.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f72waterphsolution_lns_tb26.png"
  width="100%"
  caption="Node data"
/>

4. To visualize the data, simply select the values you wish to display, then click the **Show on widget** button.

5. On the next page, choose the desired widget for your data from the **Current bundle** drop-down menu. In this example, select **Outdoor Environment**, and then select the appropriate visualization chart for the **Water pH** by clicking the slide icon .

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f74waterphsolution_lns_tb28.png"
  width="100%"
  caption="Select Widget"
/>

6. After selecting the widget, click **Add to dashboard**.

By default, the profile does not have a dashboard, so you need to select **Create new dashboard** and enter a name for the dashboard in the **New dashboard title** field, for example, **SensorHub_ph**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f76waterphsolution_lns_tb30.png"
  width="100%"
  caption="Add data to Dashboard"
/>

7. After setting the name of the dashboard, click the **Add** button to add more widgets. Alternatively, check the **Open dashboard** option to automatically open the created dashboard after adding the widget.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f75waterphsolution_lns_tb29.png"
  width="100%"
  caption="Enter the dashboard name"
/>

:::tip NOTE
If the **Open** dashboard option is not selected, users can still easily view the added widgets via **Dashboard groups > All > [Group Name]**.
:::

8. Click the Edit mode icon <img src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/icon1.png" alt="Edit" width="10%"/> to set the appropriate name and unit for the Water pH Sensor. 

9. Click the Edit widget icon <img src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/icon2.png" alt="Edit" width="4%"/> and complete the following setup steps:

- Select the Water pH unit in the **Value** drop-down menu; in this example, it's pH.
- Click the **Apply** button to apply the settings.
- Click the exit icon <img src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/icon3.png" alt="Edit" width="3%"/> , and then click the save icon <img src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/icon4.png" alt="Edit" width="7%"/> to save the settings.

:::tip NOTE
- The parameter values will be automatically rounded based on the type of widget selected for the data. If needed, adjust the number of decimal places in the icon edit mode.
- The ThingsBoard visualization dashboard editor allows you to adjust the size and shape of widgets by dragging the edges of the widgets in the Edit mode.
:::

If the above settings are correct, the final visualization widget on the Dashboard should resemble **Figure 78**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f77waterphsolution_lns_tb31.png"
  width="100%"
  caption="Dashboard created"
/>

### NB-IoT/LTE CAT-M1 Application

#### Connect Sensor Hub to MQTT Server

In the **Network Server and Visualization Configuration** section, the server in the example has been set as a public MQTT broker: `broker.hivemq.com`. Refer to the corresponding section for details. Users can also choose other brokers or servers, such as AWS IoT Core (optional), according to actual usage scenarios.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f79nb-iotlte-cat-m1-application-scenari.png"
  width="100%"
  caption="NB-IoT/LTE CAT-M1 application scenario"
/>

#### Visualize Data Through Datacake

In this example, we will utilize Datacake as the visualization platform. Datacake is a versatile IoT platform designed to visualize data from nodes in a user-friendly manner. 

To get started, create an account on the [official website](https://datacake.co/) and log in.

##### Add Sensor Hub to Datacake

1. After logging in to your account, navigate to the **Devices** tab and click **+ Add Device** to proceed with adding the Sensor Hub end device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f80waterphsolution_nbi1.png"
  width="100%"
  caption="Devices Page"
/>

2. Select the **API** option and click **Next** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f82waterphsolution_nbi3.png"
  width="50%"
  caption="Select API"
/>

3. As the device is new and there's no ready-made template, choose **New Product** from the **Datacake Product** options. Enter the device name in the **Product Name** field, then click **Next** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f83waterphsolution_nbi4.png"
  width="50%"
  caption="Select New Product"
/>

4. The **SERIAL NUMBER** field can be left blank. Datacake will randomly generate a serial number for the device, then click **Next**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f84waterphsolution_nbi5.png"
  width="50%"
  caption="Add Devices"
/>

5. Select the preferred subscription plan, then click **Add 1 device**. For this example, choose **Free**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f85waterphsolution_nbi6.png"
  width="50%"
  caption="Select a subscription plan"
/>

6. The registered device can now be viewed on the **Devices** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f86waterphsolution_nbi7.png"
  width="100%"
  caption="Registered device"
/>

##### MQTT Configuration

1. Click the name of the device you just created in the list to enter the interface, then select the **Configuration** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f88waterphsolution_nbi9.png"
  width="100%"
  caption="Configuration tab"
/>

2. Scroll down to the **API Configuration** option and copy the **Serial number**. Save it locally for later use.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f89waterphsolution_nbi10.png"
  width="100%"
  caption="Copy the serial number"
/>

3. Continue scrolling down to the **MQTT Configuration** option and configure the external MQTT Broker.
4. Click **+Add new MQTT server** and configure the relevant parameters. 

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f90waterphsolution_nbi11.png"
  width="100%"
  caption="Configure the external MQTT Broker"
/>

5. Fill in the relevant information based on the actual server used, then click **Test Connection** to verify whether Datacake can successfully connect to the **MQTT Broker**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f91waterphsolution_nbi12.png"
  width="50%"
  caption="Configure the relevant parameters"
/>

:::tip NOTE
If SSL/TLS encryption and authentication are set for more secure communication, ensure to configure them accordingly in this section. However, for this example, you can skip this option.
:::

 6. If the connection is successful, you will see the message **Connection successful**. Click **Add MQTT Server** to complete the addition of the MQTT server.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f92waterphsolution_nbi13.png"
  width="100%"
  caption="Connection established successfully"
/>

7. After successfully adding the MQTT server, click on **+Add Uplink Decoder** to add a decoder.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f93waterphsolution_nbi14.png"
  width="100%"
  caption="Add MQTT Server"
/>

8. A new window will appear, and fill in the fields according to your project.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f94waterphsolution_nbi15.png"
  width="50%"
  caption="Add Uplink Decoder"
/>

- **Subscribe to topics**: Configure the subscription topics, that is, the value of the **Publish Topic** configured in the **Network Server and Visualization Configuration** section.
- **Decoder function**: Copy the following decoding code and paste it into the **Decoder function** space.

````js
function Decoder(topic, payload) {
var decoded = [];
var data = JSON.parse ( payload.replace (/\s*/g,""));
   
for (var key in data) {
    
   decoded.push (
{
device: "1ca52561-0252-4d9c-b277-6f684270bfb1",
field: key,
value: data[key]
}
)
}
    
return decoded;

````
:::tip NOTE
In the above code, make sure that the parameter **serial_number** (device: `1ca52561-0252-4d9c-b277-6f684270bfb1`) matches the serial number saved locally earlier.
:::

9. Once completed, click **Add uplink decoder**.
10. In the **Fields** option, click **+Add Field** to show the monitoring values of the devices. Each device can create a certain number of fields, also known as a **_data points_**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f95waterphsolution_nbi16.png"
  width="100%"
  caption="Set the related parameters of the field"
/>

11. Set the necessary parameters of the Fields. For **Fields** with multiple data points, add them one by one. Once done, click **Add Field**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f95waterphsolution_nbi17.png"
  width="50%"
  caption="Set the related parameters of the field"
/>

:::tip NOTE
The **Identifier** field will be automatically filled based on the name.
:::

12. Once the uplink data is received, the **Current value** column in the **Fields** list will display the current monitoring value from the sensor.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f96waterphsolution_nbi18.png"
  width="100%"
  caption="Added sensor monitoring values"
/>

##### **Create a Dashboard to Visualize Data**

**Dashboards** can be customized depending on the specific needs and preferences of a project. Follow the steps below to add widgets and visualize the data.

1. On the device details page, navigate to the **Dashboard** tab, then toggle on the edit mode switch.
2. Click on the **+ Add Widget** button to add a widget for visualizing data.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f97waterphsolution_nbi19.png"
  width="100%"
  caption="Open the edit mode"
/>

3. Choose what type of widgets you want to display. For this example, select **Value** to visualize the Water pH values. 

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f98waterphsolution_nbi20.png"
  width="50%"
  caption="Select and add widgets for visualizing data"
/>

4. Click on the **Data** tab. Choose the field for visualization from the **Field** options and set the unit of the field, which is **pH** in this example.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f99waterphsolution_nbi21.png"
  width="50%"
  caption="Select the visualization data field"
/>

5. After configuring the widget, click **Save**. Once done with the dashboard configuration, turn off the **edit mode** switch to save the settings.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/lorawan-network-server/f100waterphsolution_nbi22.png"
  width="100%"
  caption="Water pH data visualization"
/>

<RkBottomNav/>