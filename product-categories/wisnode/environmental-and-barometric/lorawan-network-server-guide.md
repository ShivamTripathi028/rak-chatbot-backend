---
slug: /product-categories/wisnode/environmental-and-barometric/lorawan-network-server-guide/
title: Environmental and Barometric Solution LoRaWAN Network Server
description: Contains a comprehensive guide in setting up your Environmental and Barometric Monitoring Solution to the LoRaWAN and the NB-IoT platforms. It also includes instructions in connecting and configuring your LoRaWAN Gateway TTN and Datacake.
image: "https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/environmental-and-barometric-solution.png"
keywords:
  - WisNode
  - TTN
  - Datacake
  - Sensor Hub Solutions
  - Environmental and Barometric
sidebar_label: LoRaWAN Network Server
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# Environmental and Barometric Solution LoRaWAN Network Server

## Network Server and Visualization Configuration

This section outlines the operational steps for connecting the device to the network server in both the LoRaWAN and  LTE-M application scenarios, respectively.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/1.lorawan-application-scenario.png"
  width="100%"
  caption="LoRaWAN application scenario"
/>

### LoRaWAN Application

#### Cloud Network Server Setup

The cloud network server deployment scenario involves connecting the gateway and devices to third-party cloud network servers. This server integrates visualization applications to manage real-time temperature, humidity and pressure sensor data.

This section provides instructions on creating a Datacake visualization application using the TTN v3 cloud network server.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/2.cloud-network-server-deployment-solution.png"
  width="100%"
  caption="Cloud network server deployment solution"
/>

##### Connect Gateway to TTN

For this example, you will use the TTNv3 cloud server and RAK7289 V2 WisGate Edge Lite 2 to demonstrate how to connect the RAK business gateway to a cloud server.

- <b>Register the Gateway</b>

1. Register an account and log in to the <a href="https://eu1.cloud.thethings.network/console/" target="_blank">TTN v3 website</a>. If you already have a TTN account, you can log in using your **The Things ID** credentials.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/3.log-in-to-the-ttn-website.png"
  width="70%"
  caption="Log in to the TTN website"
/>

2. Once logged into the site, click on **Register a gateway** to begin the registration process for a new gateway.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/4.ttn-home-page.png"
  width="60%"
  caption="TTN home page"
/>

3. Input the Gateway EUI and then click on **Confirm** to proceed.

The Gateway EUI serves as a distinct 64-bit extended identifier for the gateway. It is accessible from the Overview page of the gateway management platform or the label situated behind the gateway.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/5.enter-the-gateway-eui.png"
  width="100%"
  caption="Enter the Gateway EUI"
/>

4. Choose the appropriate frequency plan used by the gateway, and click **Register gateway** to complete the registration process of the gateway.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/6.configure-the-gateway-frequency.png"
  width="100%"
  caption="Configure the gateway frequency"
/>

Your gateway dashboard should look the same with **Figure 7**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/7.adding-api-keys.png"
  width="100%"
  caption="Successfully registered the gateway"
/>

- <b> Generate a Token </b>

TTNv3 supports TLS server authentication and client tokens, which require trust files and keys to configure the gateway and successfully connect to the network. 

1. To generate a key file, navigate to **API keys** from the **Overview** page of the registered gateway, then click **Add API key**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/8.add-api-keys.png"
  width="100%"
  caption="Add API keys"
/>

2. In the **Add API key** page, set the **Name** field, tick off the checkboxes, then click **Create API key**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/9.configure-the-api-key.png"
  width="100%"
  caption="Configure the API Key"
/>

3. A new window pops up with the generated key. Copy the new API key by clicking the icon and then the **I have copied the key** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/10.copy-and-save-the-api-key.png"
  width="60%"
  caption="Copy and save the API Key"
/>

<b>Configure the Gateway</b>

1. Navigate back to the gateway management platform Web UI. Click on the left navigation bar to access the **LoRa > Configuration** tab. Complete the following settings and save them.
    - **Basics Station Server Type**: LNS Server
    - **Server URL**: `wss://eu1.cloud.thethings.network`
    - **Server Port**: `8887`
    - **Authentication Mode**: TLS server & Client Token - Authentication
    - **Trust (CA Certificate)**: Click the <a href="https://letsencrypt.org/certs/isrgrootx1.pem" target="_blank">link</a> to download.
    - **Client Token**: Copied API Keys

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/11.configure-the-gateway.png"
  width="100%"
  caption="Configure the gateway"
/>

2. After saving the changes, return to the TTN gateway interface, and navigate to the **Gateways** tab to confirm that the gateway is now connected to TTNv3 as a Basics Station.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/12.gateway-online.png"
  width="100%"
  caption="Gateway connected successfully"
/>

##### Connect Sensor Hub to TTN

1. Return to the TTNv3 homepage and select **Create an application** to add a node.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/13.ttnv3-home-page.png"
  width="60%"
  caption="Select Create an application"
/>

2. Click **+ Create application** to initiate the creation of a node.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/14.create-a-node.png"
  width="100%"
  caption="Create a new application"
/>

3. Enter the desired **Application ID** in the provided field, then click on **Create application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/15.fill-in-the-application-id-field.png"
  width="100%"
  caption="Fill in the Application ID field"
/>

4. Click on the **+ Register end device** button to add a new end device to the application.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/16.add-the-end-device.png"
  width="100%"
  caption="Add the end device"
/>

5. Set the parameters of the end device, as shown in **Figure 17**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/17.end-device-parameters.png"
  width="100%"
  caption="End device parameters"
/>

- **JoinEUI**, **DevEUI**, and **AppKey** can be automatically generated by clicking **Generate** on the TTN web page or customized by the user.

:::tip NOTE
Ensure that the three parameters - **JoinEUI**, **DevEUI**, and **AppKey** - are consistent with the parameters set in the WisToolBox application.
:::

6. After completing the settings, return to the WisToolBox app, and click **JOIN NETWORK** to send the end device network join request.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/18.sending-end-device-network-join-request.png"
  width="40%"
  caption="Sending end device network join request"
/>

7. As shown in **Figure 19**, the Sensor Hub has successfully joined the TTNv3 network server.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/19.successfully-joined-the-ttnv3-network-server.png"
  width="100%"
  caption="Successfully joined the TTNv3 network server"
/>

##### Visualize Data Through Datacake

Datacake is a versatile IoT platform. It offers a range of features tailored for effective data visualization and management, making it a preferred choice for IoT projects requiring efficient monitoring and analysis.

<b>Create Datacake Integration</b>

1. In the TTN console, navigate to **Integrations** on the sidebar, proceed to the **Webhooks** section, and then click **+Add webhooks** to set up an integration.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/20.adding-an-integration.png"
  width="100%"
  caption="Adding an integration"
/>

2. From the list of webhook templates, select the **Datacake** template.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/21.select-the-datacake-template.png"
  width="100%"
  caption="Select the Datacake template"
/>

3. Generate an API key on Datacake to enable webhook authentication. To get started, register a <a href="https://datacake.co/" target="_blank">Datacake</a> account, and then log in.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/22.log-in-to-the-datacake-iot-platform.png"
  width="100%"
  caption="Datacake IoT platform main page"
/>

4. Navigate to the Datacake workspace. Select **Members** on the sidebar, switch to the **API Users** tab, then click the **Add API User** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/23.add-api-user.png"
  width="100%"
  caption="Add API User"
/>

5. Enter the name of the API User, for instance, **TTS API**. Set the relevant parameters accordingly and click **Save** to finalize the creation process.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/24.set-parameters.png"
  width="70%"
  caption="Set Parameters"
/>

6. Click the **Copy** button to copy the generated Datacake API Token.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/25.copy-the-generated-datacake-api-token.png"
  width="100%"
  caption="Copy the generated Datacake API Token"
/>

7. Back on the TTN website, enter **sensorhub** in the **Webhook ID** field (as an example), and paste the Datacake API Token you previously copied into the **Token** field. Click the **Create Datacake Webhook** button to generate the Datacake Webhook.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/26.create-the-datacake-webhook.png"
  width="100%"
  caption="Create the Datacake Webhook"
/>

<b>Add Sensor Hub to Datacake</b>

1. To add a new device, select **Devices** in the sidebar and click the **+Add Device** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/27.add-a-device.png"
  width="100%"
  caption="Add a device"
/>

2. Choose **LoRaWAN** from the options and click **Next** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/28.select-lorawan.png"
  width="70%"
  caption="Select LoRaWAN"
/>

3. As the Sensor Hub is a new device, there is no pre-existing template. Create a template by clicking **New Product**, enter the **Product Name**, and click **Next** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/29.create-a-new-product.png"
  width="70%"
  caption="Create a New Product"
/>

4. Choose a network server for your device. In this guide, select **The Things Stack V3**, then click **Next** to continue.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/30.select-the-things-stack-v3.png"
  width="70%"
  caption="Select the Things Stack V3"
/>

5. In the **STEP 3 Devices** tab, enter the device **DEVEUI** and **NAME** fields, and click **Next** to continue.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/31.add-deveui-and-name.png"
  width="70%"
  caption="Add DEVEUI and Name"
/>

6. In **Step 4 Plan**, select the preferred subscription plan, and click **Add 1 device** to add the device. For this example, choose **Free**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/32.select-a-subscription-plan.png"
  width="70%"
  caption="Select a subscription plan"
/>

7. The registered device can now be viewed on the **Devices** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/33.registered-device.png"
  width="100%"
  caption="Registered device"
/>

<b>Create a Payload Decoder</b>

1. Click the successfully registered device and go to the **Configuration** tab. Scroll down to the **Payload Decoder** field, then copy and save the decoder code.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/34.configuration-tab.png"
  width="100%"
  caption="Configuration tab"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/35.decoder-code.png"
  width="100%"
  caption="Decoder code"
/>

<details>
<summary> Click to view the code </summary>

```js
function lppDecode (bytes) {
var sensor_types = {
	0: { 'size': 1, 'name': 'digital_in', 'signed': false, 'divisor': 1 },
	1: { 'size': 1, 'name': 'digital_out', 'signed': false, 'divisor': 1 },
	2: { 'size': 2, 'name': 'analog_in', 'signed': true, 'divisor': 100 },
	3: { 'size': 2, 'name': 'analog_out', 'signed': true, 'divisor': 100 },
	100: { 'size': 4, 'name': 'generic', 'signed': false, 'divisor': 1 },
	101: { 'size': 2, 'name': 'illuminance', 'signed': false, 'divisor': 1 },
	102: { 'size': 1, 'name': 'presence', 'signed': false, 'divisor': 1 },
	103: { 'size': 2, 'name': 'temperature', 'signed': true, 'divisor': 10 },
	104: { 'size': 1, 'name': 'humidity', 'signed': false, 'divisor': 1 },
	112: { 'size': 2, 'name': 'humidity_prec', 'signed': true, 'divisor': 10 },
	113: { 'size': 6, 'name': 'accelerometer', 'signed': true, 'divisor': 1000 },
	115: { 'size': 2, 'name': 'barometer', 'signed': false, 'divisor': 10 },
	116: { 'size': 2, 'name': 'voltage', 'signed': false, 'divisor': 100 },
	117: { 'size': 2, 'name': 'current', 'signed': false, 'divisor': 1000 },
	118: { 'size': 4, 'name': 'frequency', 'signed': false, 'divisor': 1 },
	120: { 'size': 1, 'name': 'percentage', 'signed': false, 'divisor': 1 },
	121: { 'size': 2, 'name': 'altitude', 'signed': true, 'divisor': 1 },
	125: { 'size': 2, 'name': 'concentration', 'signed': false, 'divisor': 1 },
	128: { 'size': 2, 'name': 'power', 'signed': false, 'divisor': 1 },
	130: { 'size': 4, 'name': 'distance', 'signed': false, 'divisor': 1000 },
	131: { 'size': 4, 'name': 'energy', 'signed': false, 'divisor': 1000 },
	132: { 'size': 2, 'name': 'direction', 'signed': false, 'divisor': 1 },
	133: { 'size': 4, 'name': 'time', 'signed': false, 'divisor': 1 },
	134: { 'size': 6, 'name': 'gyrometer', 'signed': true, 'divisor': 100 },
	135: { 'size': 3, 'name': 'colour', 'signed': false, 'divisor': 1 },
	136: { 'size': 9, 'name': 'gps', 'signed': true, 'divisor': [10000, 10000, 100] },
	137: { 'size': 11, 'name': 'gps', 'signed': true, 'divisor': [1000000, 1000000, 100] },
	138: { 'size': 2, 'name': 'voc', 'signed': false, 'divisor': 1 },
	142: { 'size': 1, 'name': 'switch', 'signed': false, 'divisor': 1 },
	188: { 'size': 2, 'name': 'soil_moist', 'signed': false, 'divisor': 10 },
	190: { 'size': 2, 'name': 'wind_speed', 'signed': false, 'divisor': 100 },
	191: { 'size': 2, 'name': 'wind_direction', 'signed': false, 'divisor': 1 },
	192: { 'size': 2, 'name': 'soil_ec', 'signed': false, 'divisor': 1000 },
	193: { 'size': 2, 'name': 'soil_ph_h', 'signed': false, 'divisor': 100 },
	194: { 'size': 2, 'name': 'soil_ph_l', 'signed': false, 'divisor': 10 },
	195: { 'size': 2, 'name': 'pyranometer', 'signed': false, 'divisor': 1 },
	203: { 'size': 1, 'name': 'light', 'signed': false, 'divisor': 1 },
};


function arrayToDecimal(stream, is_signed, divisor) {


	var value = 0;
	for (var i = 0; i < stream.length; i++) {
		if (stream[i] > 0xFF)
			throw 'Byte value overflow!';
		value = (value << 8) | stream[i];
	}


	if (is_signed) {
		var edge = 1 << (stream.length) * 8;  // 0x1000..
		var max = (edge - 1) >> 1;             // 0x0FFF.. >> 1
		value = (value > max) ? value - edge : value;
	}


	value /= divisor;


	return value;


}


var sensors = [];
var i = 0;
while (i < bytes.length) {


	var s_no = bytes[i++];
	var s_type = bytes[i++];
	if (typeof sensor_types[s_type] == 'undefined') {
		throw 'Sensor type error!: ' + s_type;
	}


	var s_value = 0;
	var type = sensor_types[s_type];
	switch (s_type) {


		case 113:   // Accelerometer
		case 134:   // Gyrometer
			s_value = {
				'x': arrayToDecimal(bytes.slice(i + 0, i + 2), type.signed, type.divisor),
				'y': arrayToDecimal(bytes.slice(i + 2, i + 4), type.signed, type.divisor),
				'z': arrayToDecimal(bytes.slice(i + 4, i + 6), type.signed, type.divisor)
			};
			break;
		case 136:   // GPS Location
			s_value = {
				'latitude': arrayToDecimal(bytes.slice(i + 0, i + 3), type.signed, type.divisor[0]),
				'longitude': arrayToDecimal(bytes.slice(i + 3, i + 6), type.signed, type.divisor[1]),
				'altitude': arrayToDecimal(bytes.slice(i + 6, i + 9), type.signed, type.divisor[2])
			};
			break;
		case 137:   // Precise GPS Location
			s_value = {
				'latitude': arrayToDecimal(bytes.slice(i + 0, i + 4), type.signed, type.divisor[0]),
				'longitude': arrayToDecimal(bytes.slice(i + 4, i + 8), type.signed, type.divisor[1]),
				'altitude': arrayToDecimal(bytes.slice(i + 8, i + 11), type.signed, type.divisor[2])
			};
			sensors.push({
				'channel': s_no,
				'type': s_type,
				'name': 'location',
				'value': "(" + s_value.latitude + "," + s_value.longitude + ")"
			});
			sensors.push({
				'channel': s_no,
				'type': s_type,
				'name': 'altitude',
				'value': s_value.altitude
			});
			break;
		case 135:   // Colour
			s_value = {
				'r': arrayToDecimal(bytes.slice(i + 0, i + 1), type.signed, type.divisor),
				'g': arrayToDecimal(bytes.slice(i + 1, i + 2), type.signed, type.divisor),
				'b': arrayToDecimal(bytes.slice(i + 2, i + 3), type.signed, type.divisor)
			};
			break;


		default:    // All the rest
			s_value = arrayToDecimal(bytes.slice(i, i + type.size), type.signed, type.divisor);
			break;
	}


	sensors.push({
		'channel': s_no,
		'type': s_type,
		'name': type.name,
		'value': s_value
	});


	i += type.size;


}


return sensors;
}


// For TTN, Helium and Datacake
function Decoder(bytes, fport) {
// bytes = input.bytes;
// fPort = input.fPort;


// flat output (like original decoder):
var response = {};
lppDecode(bytes, 1).forEach(function (field) {
	response[field['name'] + '_' + field['channel']] = field['value'];
});


// Enable only for Datacake
 response['LORA_RSSI'] = (!!normalizedPayload.gateways && !!normalizedPayload.gateways[0] && normalizedPayload.gateways[0].rssi) || 0;
 response['LORA_SNR'] = (!!normalizedPayload.gateways && !!normalizedPayload.gateways[0] && normalizedPayload.gateways[0].snr) || 0;
 response['LORA_DATARATE'] = normalizedPayload.data_rate;


return response;
}  

```
</details>

2. Complete the fields for the configuration shown in **Figure 36**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/36.configuration-fields.png"
  width="60%"
  caption="Configuration fields"
/>

:::tip NOTE
- Add the field type under the **Type** input box. Select **Integer** for RAK1901, and **Float** for RAK1902.
- Enter an appropriate name in the **Name** field.
- The **Identifier** field will be automatically filled in based on the name.
- When an uplink is received, refresh the page and the **CURRENT VALUE** field will be updated.
- Leave everything else as default and click **Add Field** to complete the setup.
:::

3. Repeat the above steps to add the Humidity/Temperature (RAK1902)/ Pressure fields, as shown is **Figure 38** when completed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/37.successfully-added-fields.png"
  width="100%"
  caption="Successfully added fields"
/>

<b>Create a Dashboard</b>

1. To create a dashboard, click the **edit mode** switch (<img src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/0.edit-off.png" alt="Edit off" height="20px"/>) on the **Dashboard** tab of the device on Datacake.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/38.turn-on-the-edit-mode-switch.png"
  width="100%"
  caption="Turn on the edit mode switch"
/>

2. Click **+Add Widget** to add a visualization widget.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/39.add-visualization-widget.png"
  width="100%"
  caption="Add visualization widget"
/>

3. Select **Value** from the menu to create a new dashboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/40.select-value-to-create-a-new-dashboard.png"
  width="70%"
  caption="Select Value to create a new dashboard"
/>

:::tip NOTE
You can select different types of widgets to accommodate various data formats.
:::

4. In the **Title** field under the **Basics** tab, name the widget. As an example, the temperature widget of RAK1901 is used, so name it as **RAK1901_Temperature**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/41.name-the-widget.png"
  width="70%"
  caption="Name the widget"
/>

5. Under the **Data** tab, pull down the **Field** tab bar, select **Temperature** (for **RAK1901**), and set the unit to **° C**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/42.set-the-unit.png"
  width="70%"
  caption="Set the unit"
/>

6. Under the **Gauge** tab, select the gauge type and color, set the range of values for the widget, and then click **Save**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/43.set-the-widget-type.png"
  width="70%"
  caption="Set the widget type"
/>

7. To add another widget, ensure the **edit mode** switch is **ON**, then repeat from **Step 2-6** for the **Humidity**, **Temperature (RAK1902)**, and **Pressure** fields.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/44.added-widget.png"
  width="100%"
  caption="Added Widget"
/>

8. When you finish adding the widgets, turn off the **edit mode** switch to save the edits.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/45.save-the-edits.png"
  width="100%"
  caption="Save the edits"
/>


#### Built-In Network Server Setup

The RAK gateway comes with a built-in NS, which eliminates the need to deploy NS in the cloud or locally. This gateway is suitable for small-sized industrial application scenarios and offers various advantages such as cost savings, reduced R&D investment, high execution efficiency, and shorter delays.

The built-in network server of the RAK gateway provides MQTT and HTTP integration that allows for post-processing data and implementing solutions based on the needs.

This section will use the public MQTT broker integration as an example to demonstrate how to use the built-in network server to create a visualization application on ThingsBoard.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/46.gateway-built-in-ns-application-scenario.png"
  width="100%"
  caption="Gateway built-in NS application scenario"
/>

##### Configure the ThingsBoard

1. Log in to <a href="https://thingsboard.cloud/login" target="_blank">ThingsBoard</a>. If you don't have an account, <a href="https://thingsboard.cloud/signup" target="_blank">create one</a> before proceeding.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/47.thingsboard-authentication-page.png"
  width="50%"
  caption="ThingsBoard authentication page"
/>

2. After successfully logging in, you will be directed to the ThingsBoard homepage.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/48.thingsboard-homepage.png"
  width="100%"
  caption="ThingsBoard homepage"
/>

3. Navigate through **Integration center > Integrations > Data converters** in the left navigation tree to create a data converter for the uplink.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/49.create-a-data-converter.png"
  width="100%"
  caption="Create a data converter"
/>

4. Click the **Add Data Converter** icon (<img src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/0.add-button.png" alt="Add Button" height="20px"/>) and choose the **Create new converter** option.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/50.create-a-data-converter.png"
  width="100%"
  caption="Create a data converter"
/>

5. Enter the name of the decoder in the **Name** field (for example, *Uplink decoder*), leave the **Type** field as **Uplink**, and select the **JavaScript** option.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/51.add-the-decoder-code.png"
  width="50%"
  caption="Add the decoder code"
/>

6. Edit the decoder code by copying the following code into the edit box, then click **Add** to include the uplink decoder.

<details>
<summary> Click to view the code </summary>

```js
/** Decoder **/
//decode payload to string
var payloadStr = decodeToString(payload);
var data = JSON.parse(payloadStr).data;
var bytes = atob(data).split('').map(function (c) {
  return c.charCodeAt(0);
});


var values = {};
let i = 0;
while (i < bytes.length) {
  var channelId = (bytes[i] << 8) | bytes[i + 1];
  var value;
  switch (channelId) {
    case 0x0167:
      value = (bytes[i + 2] << 8) | bytes[i + 3];
      values.temperature1 = value / 10.0;
      i += 4;
      break;
    case 0x0268:
      value = bytes[i + 2];
      values.humidity = value;
      i += 3;
      break;
    case 0x0367:
      value = (bytes[i + 2] << 8) | bytes[i + 3];
      values.temperature2 = value / 10.0;
      i += 4;
      break;
case 0x0473:
      value = (bytes[i + 2] << 8) | bytes[i + 3];
      values.pressure = value / 10.0;
      i += 4;
      break;
    default:
      break;
  }
}


var integrationName = 'MQTT Integration';
var deviceName = ' rak19012';
var result = {
  deviceName: deviceName,
  attributes: {
    integrationName: metadata['integrationName'],
    temperature1: values.temperature1,
    humidity: values.humidity,
	temperature2: values.temperature2,
	pressure: values.pressure,
  },
};


/** Helper functions **/


function decodeToString (payload) {
return String.fromCharCode.apply (String, payload);
}


return result;

```
</details>

:::tip NOTE
In the above code, the marked word **rak19012** is the device ID, i.e., the device name. This parameter must be consistent with the device name added in **Configure the Gateway**. In this example, it is **rak19012**.
:::

7. Navigate to the **Integration Center > Integrations** menu and click the **Add Integration** icon (<img src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/0.add-button.png" alt="Add Button" height="20px"/>) to add the MQTT integration.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/52.add-the-mqtt-integration.png"
  width="100%"
  caption="Add the MQTT integration"
/>

8. Enter the name of the integration (for example, *MQTT Integration*) in the **Name** field and select **MQTT** in the Type drop-down menu. Click **Next** to continue.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/53.fill-in-the-integration-name.png"
  width="60%"
  caption="Fill in the integration name"
/>

9. In the **Uplink data converter** options, click **Select existing** to choose the previously created decoder (**Uplink Decoder**), then click **Next**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/54.select-the-created-decoder.png"
  width="60%"
  caption="Select the created decoder"
/>

10. In the **Downlink data converter** interface, no configuration is necessary and just click **Skip** to bypass this setup.
11. Configure connection options. **Host** is the MQTT broker address used for messages. The Host of the external MQTT broker used in this example is `broker.hivemq.com`. You can choose to use other brokers with a different Host.
12. Enter the address `broker.hivemq.com` in the **Host** field, with the port number `1883`. Click the **Add topic filter** button to configure the subscription topic.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/55.configure-the-connection-options.png"
  width="60%"
  caption="Configure the connection options"
/>

<b>Configure the subscription topic</b>

```
application/{{application_name}}/device/{{device_EUI}}/join
application/{{application_name}}/device/{{device_EUI}}/rx
application/{{application_name}}/device/{{device_EUI}}/tx
application/{{application_name}}/device/{{device_EUI}}/ack
application/{{application_name}}/device/{{device_EUI}}/status
```

- **application_name**: The application ID created in the gateway.
- **device_EUI**: The device EUI of the end device.

13. Modify the parameter values corresponding to the topics based on the actual application created and the device used. After configuring the details, click the **Add** button to save and complete the settings.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/56.configure-the-subscription-topics.png"
  width="60%"
  caption="Configure and add the subscription topics"
/>

14. After clicking **Add**, the settings are saved and completed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/57.configuration-completed.png"
  width="100%"
  caption="Configuration completed"
/>

##### Configure the Gateway

This section will use the <a href="https://store.rakwireless.com/products/rak7268-8-channel-indoor-lorawan-gateway?variant=42316475924678" target="_blank">RAK7268 V2 WisGate Edge Lite 2</a> as an example.

1. To access the gateway web management platform, refer to the <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#overview" target="_blank">WisGateOS V2 user manual</a> for details.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/58.gateway-web-management-platform.png"
  width="100%"
  caption="WisGate OS Web Management Platform"
/>

2. After successfully logging in, navigate to the **LoRa®** menu in the left navigation tree and set the **Work mode** of the gateway to the **Built-in network server**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/59.set-the-work-mode-of-the-gateway.png"
  width="100%"
  caption="Set the Work mode of the gateway"
/>

3. Once done with the setting, click the **Applications** tab, then the **Add application** button. You can also click **add one now** text link to add a new application.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/60.applications-tab.png"
  width="100%"
  caption="Applications tab"
/>

4. Configure the following information: **Application name**, **Application description**, and **Application Type**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/61.configure-the-application.png"
  width="100%"
  caption="Configure the Application key"
/>

- **Unified Application key**: Choose this option if all devices will use the same application key. Once selected, a field for the application key appears, where you can manually type in an application key or click the **Autogenerate** button to generate one.

:::tip NOTE
- After enabling the **Auto Add Device** option, configure the **Application EUI option**. The value needs to be consistent with the node value. Once you have verified the application EUI and key, the device will be added automatically to the application.

<div class="text-center">
<img src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/61-a.auto-add-device.png" alt="Auto add device" class="img-fluid"/>
</div>
:::

5. Once you've completed the configuration, click on **Save Application** to add the new application.

6. In the application list, locate the newly created application and navigate to the **End devices** tab. If you've enabled the **Auto Add Device** function, the device will be automatically registered upon the addition request.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/62.end-devices-tab.png"
  width="100%"
  caption="End devices tab"
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
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/63.add-new-end-devices.png"
  width="100%"
  caption="Add new end devices"
/>

8. After completing, click **Add end devices** to proceed to the next step.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/64.add-the-device-to-the-device-list.png"
  width="100%"
  caption="Add the device to the device list"
/>

9. In the **Adding end devices** interface, enter the device EUI in the **End Device EUI (Main)** field and select the **Add to End Devices list** button. Then click **Add end devices** to complete adding the end device. Then click **Add end devices** to complete adding the end device.

:::tip NOTE
- The device EUI configured here must match the end device. You can either obtain it by querying the end device or entering one (1) EUI and synchronously updating the corresponding value of the end device.
- If the EUI is correct, the device will be displayed in the **End devices list**.
- If the EUI is incorrect, the device will be displayed in the **End devices with an error**.
:::

10. After selecting the device in the **End devices list** at the bottom left, click **Add end devices** to complete adding the end device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/65.complete-the-end-device-addition.png"
  width="100%"
  caption="Complete the end device addition"
/>

11. Click the **Add** button to confirm adding the device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/66.confirm-to-add-the-end-device.png"
  width="70%"
  caption="Confirm to add the end device"
/>

12. When finished, enter the **End devices** interface, where you can see the created end device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/67.end-device-created.png"
  width="100%"
  caption="End device created"
/>

##### Connect the Sensor Hub to the Built-In Network Server

For specific configuration on how to connect SensorHub to the server, refer to **SensorHub Network Configuration > LoRaWAN Application Scenario**.

Once completed, the device will join the network. As shown in **Figure 70**, the end device **SensorHub** has successfully connected to the gateway's built-in server.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/68.end-device--sensohub-has-been-connected.png"
  width="100%"
  caption="Connected to Gateway Built-In Server"
/>

##### Configure the MQTT Integration

1. Go to the **LoRa® > Configuration > Integration Interface Parameters** section.

2. Toggle the **Enable Integration Interface** option and select **Generic MQTT** as the **Integration mode**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/69.set-up-mqtt-integration.png"
  width="100%"
  caption="Set up MQTT integration"
/>

3. In the **MQTT Broker Address** option, enter `broker.hivemq.com` then click **Save changes**.

4. After the device has joined and has been sending uplink data, check the uplink data in **ThingsBoard** > **Integrations** > **Your Integration** > **Events**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/70.view-the-gateway-uplink-data.png"
  width="100%"
  caption="View the gateway uplink data"
/>

##### Visualize Data Through ThingsBoard

1. After creating the data converter, integrating, and obtaining some data in the **Event** tab, check the automatically created devices based on the decoder in the **Entities** > **Devices** > **Groups** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/71.check-the-device.png"
  width="100%"
  caption="Check the device"
/>

2. Click the group named **All** in the **Device groups** menu to automatically create a decoder device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/72.automatically-created-decoder-device.png"
  width="100%"
  caption="Automatically created decoder device"
/>

3. Click the device and go to the **Attributes** tab, where you will see the node data.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/73.node-data.png"
  width="100%"
  caption="Node data"
/>

4. To visualize the data, simply select the values you wish to display, then click the **Show on widget** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/74.data-visualization.png"
  width="100%"
  caption="Data visualization"
/>

5. On the next page, select the required widget from the **Current bundle** dropdown menu. In this example, choose **Outdoor Environment**, and select the appropriate visualization chart for Humidity by clicking the slide icon (<img src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/0.slide-icon.png" alt="Slide icon" height="20px"/>).

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/75.choose-an-appropriate-visualization-chart.png"
  width="100%"
  caption="Choose an appropriate visualization chart"
/>

6. After selecting the widget, click **Add to dashboard** to proceed.

7. The **Add widget to dashboard** window will appear. By default, there is no dashboard in the profile, so you need to select **Create new dashboard** and enter a name for the dashboard in the **new dashboard title** field. Additionally, in this dashboard, the user can add more widgets for the device.


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/76.enter-the-dashboard-name.png"
  width="100%"
  caption="Enter the dashboard name"
/>

8. After setting the dashboard name, click the **Add** button to add more widgets. Alternatively, check the **Open dashboard** option to automatically open the created dashboard after adding the widget.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/77.dashboard-created.png"
  width="100%"
  caption="Dashboard created"
/>

:::tip NOTE
If the **Open** dashboard option is not selected, you can still easily view the added widgets via **Dashboard groups** > **All** > [**Group Name**].
:::

9. To set the appropriate name and unit of Humidity, click on **Edit mode** (<img src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/0-a.edit-mode.png" alt="Edit mode" height="20px"/>) > **Edit widget** (<img src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/0-b.edit-mode.png" alt="Edit switch" height="20px"/>) and complete the steps below:
    - Select the humidity unit in the **Value** column, **%RH** in this example;
    - Click the **Apply** button to apply the settings;
    - Click the exit icon (<img src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/0.exit.png" alt="Exit" height="20px"/>) in the upper right corner, and click on **Save** (<img src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/0.save.png" alt="Save" height="20px"/>).
    
<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/78.edit-dashboard.png"
  width="100%"
  caption="Edit Dashboard"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/79.set-appropriate-name-and-unit-of-humidity.png"
  width="100%"
  caption="Set appropriate name and unit of Humidity"
/>

:::tip NOTE
ThingsBoard visualization dashboard editor supports adjusting the size and shape of widgets by dragging the edges of the widgets in the **Edit mode**.
:::

10. If the above settings are correct, the final **Dashboard** visualization widget should look like **Figure 110**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/80.visualization-widget-settings-completed.png"
  width="100%"
  caption="Visualization widget settings completed"
/>

11. After repeating the above steps to complete the visualization of the remaining parameters, the results are as follows:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/81.visualization-completed.png"
  width="100%"
  caption="Visualization completed"
/>

:::tip NOTE

- When adding the visualizations of the remaining parameters, in the Add widget to dashboard step, you should click Select existing dashboard to select the previously created dashboard SensorHub_RAK1901&2.

<div class="text-center">
<img src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/81-a.select-existing-dashboard.png" alt="Select existing dashboard" class="img-fluid" width="70%"/>
</div>

- The visualization parameter values of the RAK1902 barometric pressure sensor (Temperature2 and Barometer) will be automatically rounded due to the different types of widgets selected for the data. If needed, please set the decimals in the icon edit mode.

<div class="text-center">
<img src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/81-b.icon-edit-mode.png" alt="Icon edit mode" class="img-fluid" width="100%"/>
</div>

:::

### NB-IoT/LTE CAT-M1 Application

#### Connect Sensor Hub to MQTT Server

In the **Network Server and Visualization Configuration** section, the server has been set as a public MQTT broker: `broker.hivemq.com`. You can also choose other brokers or servers, such as AWS IoT Core (optional), according to the actual usage scenario. 

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/82.nb-iot-lte-cat-m1-application-scenario.png"
  width="100%"
  caption="NB-IoT/LTE CAT-M1 Application Scenario"
/>

#### Visualize Data Through Datacake

In this example, you will use Datacake as the visualization platform. Datacake is a versatile IoT platform designed to visualize data from nodes in a user-friendly manner.

To get started, create an account on the <a href="https://datacake.co/" target="_blank">official website</a> and log in.

##### Add Sensor Hub to Datacake

1. After logging in to your account, navigate to the **Devices** tab and click **+ Add Device** to proceed with adding the Sensor Hub end device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/83.add-the-end-device,-sensorhub.png"
  width="100%"
  caption="Add the end device, SensorHub"
/>

2. Select the **API** option and click **Next** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/84.select-api.png"
  width="60%"
  caption="Select API"
/>

3. As the device is new and there's no ready-made template, choose **New Product** from the **Datacake Product** options. Enter the device name in the **Product Name** field, then click **Next** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/85.select-new-product.png"
  width="60%"
  caption="Select New Product"
/>

4. The **SERIAL NUMBER** field can be left blank. Datacake will randomly generate a serial number for the device, then click **Next**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/86.keep-the-serial-number.png"
  width="60%"
  caption="Keep the serial number"
/>

5. Select the preferred subscription plan, then click **Add 1 device**. For this example, choose **Free**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/87.select-a-subscription-plan.png"
  width="60%"
  caption="Select a subscription plan"
/>

6. The registered device can now be viewed on the **Devices** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/88.registered-device.png"
  width="100%"
  caption="Registered device"
/>

##### MQTT Configuration

1. Click the name of the device you just created in the list to enter the interface, then select the **Configuration** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/90.configuration-tab.png"
  width="100%"
  caption="Copy the serial number"
/>

2. Scroll down to the **API Configuration** option and copy the **Serial number**. Save it locally for later use.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/91.copy-the-serial-number.png"
  width="100%"
  caption="Copy the serial number"
/>

3. Continue scrolling down to the **MQTT Configuration** option and configure the external MQTT Broker.

4. Click **+Add new MQTT server** and configure the relevant parameters.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/92.configure-the-external-mqtt-broker.png"
  width="100%"
  caption="Configure the external MQTT Broker"
/>

5. Fill in the relevant information based on the actual server used, then click **Test Connection** to verify whether Datacake can successfully connect to the **MQTT Broker**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/93.configure-the-relevant-parameters.png"
  width="70%"
  caption="Configure the relevant parameters"
/>

:::tip NOTE
If SSL/TLS encryption and authentication are set for more secure communication, ensure to configure them accordingly in this section. However, for this example, you can skip this option.
:::

6. If the connection is successful, you will see the message **Connection successful**. Click **Add MQTT Server** to complete the addition of the MQTT server.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/94.configure-the-relevant-parameters.png"
  width="100%"
  caption="Configure the relevant parameters"
/>

7. After successfully adding the MQTT server, click on **+Add Uplink Decoder** to add a decoder.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/95.configure-the-relevant-parameters.png"
  width="100%"
  caption="Configure the relevant parameters"
/>

8. A new window will appear, and fill in the fields according to your project.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/96.add-uplink-decoder.png"
  width="70%"
  caption="Add Uplink Decoder"
/>

- **Subscribe to topics**: Configure the subscription topics, that is, the value of the **Publish Topic** configured in the **Network Server and Visualization Configuration** section.
- **Decoder function**: Copy the following decoding code and paste it into the **Decoder function** space.

<details>
<summary> Click to view the code </summary>

```js
function decodeToString (payload) {
return payload
.match(/.{2}/g)
.map(function (hex) {
return parseInt (hex, 16);
})
.map(function ( charCode ) {
      return String.fromCharCode(charCode);
    })
    .join("");
}


function Decoder(topic, payload) {
  var decoded = [];
  var payloadStr = decodeToString(payload);
  var data = payloadStr;
  var bytes = Array.prototype.map.call(data, function (char) {
    return char.charCodeAt(0);
  });
  console.log(bytes);


  var values = {};
  var i = 0;
  while (i < bytes.length) {
    var channelId = (bytes[i] << 8) | bytes[i + 1];
    var value;
    switch (channelId) {
      case 0x0167:
        value = (bytes[i + 2] << 8) | bytes[i + 3];
        values.temperature1 = value / 10.0;
        i += 4;
        break;
      case 0x0268:
        value = bytes[i + 2];
        values.humidity = value;
        i += 3;
        break;
      case 0x0367:
        value = (bytes[i + 2] << 8) | bytes[i + 3];
        values.temperature2 = value / 10.0;
        i += 4;
        break;
      case 0x0473:
        value = (bytes[i + 2] << 8) | bytes[i + 3];
        values.barmoeter = value / 10.0;
        i += 4;
        break;
      default:
        break;
    }
  }


  var data = {
    temperature1: values.temperature1,
    humidity: values.humidity,
    temperature2: values.temperature2,
    barmoeter: values.barmoeter,
  };


  for (var key in data) {
    if (data.hasOwnProperty(key)) {
      decoded.push ({
        device: "53f86e9f-24e6-4dd3-bc8b-07c4b7e6feb8" ,
field: key,
value: data[key],
});
}
}
return decoded;
}

```
</details>


:::tip NOTE
In the above code, make sure that the parameter **serial_number** (device: ```53f86e9f-24e6-4dd3-bc8b-07c4b7e6feb8```) matches the serial number saved locally earlier.
:::

9. Once completed, click **Add uplink decoder**.
10. In the **Fields** option, click **+ Add Field** to show the monitoring values of the devices. Each device can create a certain number of fields, also known as a **<i>data point</i>**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/97.add-field.png"
  width="100%"
  caption="Add Field"
/>

11. Set the necessary parameters of the **Field**. For **Fields** with multiple data points, add them one by one. Once done, click **Add Field**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/98.set-the-related-parameters-of-the-field.png"
  width="70%"
  caption="Set the related parameters of the field"
/>

:::tip NOTE
The **Identifier** field will be automatically filled based on the name.
:::

12. Once the uplink data is received, the **Current value** column in the **Fields** list will display the current monitoring value from the sensor.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/99.added-sensor-monitoring-values.png"
  width="100%"
  caption="Added sensor monitoring values"
/>

13. Follow **Steps 11-12** to add other monitoring parameters. 

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/100.add-other-monitoring-parameters-individually.png"
  width="100%"
  caption="Add other monitoring parameters individually"
/>

:::tip NOTE
Due to the different precision of the RAK1901 and RAK1902 sensors when creating fields, select **Integer** for RAK1901, and **Float** for RAK1902.
:::

##### Create a Dashboard to Visualize Data

**Dashboards** can be customized depending on the specific needs and preferences of a project. Follow the steps below to add widgets and visualize the data.

1. On the device details page, navigate to the **Dashboard** tab, then toggle on the edit mode switch (<img src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/0.edit-off.png" alt="Edit off" height="20px"/>).

2. Click on the **+ Add Widget** button to add a widget for visualizing data.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/101.open-the-edit-mode.png"
  width="50%"
  caption="Open the edit mode"
/>

3. Choose what type of widgets you want to display. For this example, select **Value** to visualize temperature monitoring values.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/102.add-widgets-for-visualizing-data.png"
  width="70%"
  caption="Add widgets for visualizing data"
/>

4. Click on the **Data** tab. Choose the field for visualization from the **Field** options (for example, Temperature) and set the unit of the field, which is **° C**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/103.select-the-visualization-data-field.png"
  width="70%"
  caption="Select the visualization data field"
/>

5. After configuring the widget, click **Save**. You should now see the successfully created widget on the Dashboard interface.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/104.successfully-created-solar-radiation-widget.png"
  width="100%"
  caption="Successfully created solar radiation widget"
/>

6. To add more parameter widgets, click the **+Add Widget** button again with the edit mode toggle switch ON (<img src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/0.edit-on.png" alt="Edit on" height="20px"/>), then repeat **Steps 4-6**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/105.close-edit-mode-to-save-the-settings.png"
  width="100%"
  caption="Close edit mode to save the settings"
/>

7. Once done with the dashboard configuration, turn OFF (<img src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/0.edit-off.png" alt="Edit off" height="20px"/>) the **edit mode** switch to save the settings.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/lorawan-network-server/128.visualization-completed1.png"
  width="100%"
  caption="Visualization completed1"
/>

<RkBottomNav/>