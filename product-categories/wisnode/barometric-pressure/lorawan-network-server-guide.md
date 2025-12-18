---
slug: /product-categories/wisnode/barometric-pressure/lorawan-network-server-guide/
title: Barometric Pressure Monitoring Solution LoRaWAN Network Server
description: Provides comprehensive information to connect he Sensor Hub Barometric Pressure Monitoring to various LoRaWAN network servers and display data on IoT platforms.
image: "https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/barometric-pressure-sensor.png"
keywords:
    - wisnode
    - Sensor Hub
    - TTN
    - Datacake
    - LoRaWAN
    - Barometric Pressure
sidebar_label: LoRaWAN Network Server
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# Barometric Pressure Monitoring Solution LoRaWAN Network Server

## Network Server and Visualization Configuration

This section outlines the operational steps for connecting the device to the network server in both the LoRaWAN and NB-IoT application scenarios.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f1application_scenarios.png"
  width="100%"
  caption="Application Scenarios"
/>

### LoRaWAN Application

#### Cloud Network Server Setup

The cloud network server deployment scenario involves connecting the gateway and devices to third-party cloud network servers. This server integrates visualization applications to manage real-time barometric pressure data.

This section provides instructions on creating a Datacake visualization application using the TTN v3 cloud network server.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f2cloudnetworkserver.png"
  width="100%"
  caption="Cloud network server deployment solution"
/>

##### Connect Gateway to TTN

For this example, you will use the TTNv3 cloud server and RAK7289 V2 WisGate Edge Lite 2 to demonstrate how to connect the RAK business gateway to a cloud server.

- **Register the Gateway**

1. Register an account and log in to the <a href="https://eu1.cloud.thethings.network/console/" target="_blank">TTN v3 website</a>. If you already have a TTN account, you can log in using your **The Things ID** credentials.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f3barpressolution_lns_ttn1.png"
  width="70%"
  caption="Log in to the TTN website"
/>

2. Once logged into the site, click on **Register a gateway** to begin the registration process for a new gateway.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f4barpressolution_lns_ttn2.png"
  width="70%"
  caption="TTN home page"
/>

3. Input the Gateway EUI and then click on **Confirm** to proceed.

The Gateway EUI serves as a distinct 64-bit extended identifier for the gateway. It is accessible from the Overview page of the gateway management platform or the label situated behind the gateway.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f5barpressolution_lns_ttn3.png"
  width="100%"
  caption="Enter the Gateway EUI"
/>

4. Choose the appropriate frequency plan used by the gateway, and click **Register gateway** to complete the registration process of the gateway.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f6barpressolution_lns_ttn4.png"
  width="100%"
  caption="Configure the gateway frequency"
/>

Your gateway dashboard should look the same with **Figure 7**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f7barpressolution_lns_ttn5.png"
  width="100%"
  caption="Successfully registered the gateway"
/>

**Generate a Token**

TTNv3 supports TLS server authentication and client tokens, which require trust files and keys to configure the gateway and successfully connect to the network. 

1. To generate a key file, navigate to **API keys** from the **Overview** page of the registered gateway, then click **Add API key**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f8barpressolution_lns_ttn6.png"
  width="100%"
  caption="Add API keys"
/>

2. In the **Add API key** page, set the **Name** field, tick off the checkboxes, then click **Create API key**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f9barpressolution_lns_ttn7.png"
  width="100%"
  caption="Configure the API Key"
/>

3. A new window pops up with the generated key. Copy the new API key by clicking the icon and then the **I have copied the key** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f10barpressolution_lns_ttn8.png"
  width="70%"
  caption="Copy and save the API Key"
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
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f11barpressolution_lns_ttn9.png"
  width="100%"
  caption="Configure the gateway"
/>

2. After saving the changes, return to the TTN gateway interface, and navigate to the **Gateways** tab to confirm that the gateway is now connected to TTNv3 as a Basics Station.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f12barpressolution_lns_ttn10.png"
  width="100%"
  caption="Gateway connected successfully"
/>

##### Connect Sensor Hub to TTN

1. Return to the TTNv3 homepage and select **Create an application** to add a node.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f13barpressolution_lns_ttn11.png"
  width="70%"
  caption="Select Create application"
/>

2. Click **+ Create application** to initiate the creation of a node.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f14barpressolution_lns_ttn12.png"
  width="100%"
  caption="Create a new application"
/>

3. Enter the desired **Application ID** in the provided field, then click on **Create application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f15barpressolution_lns_ttn13.png"
  width="100%"
  caption="Enter the application ID"
/>
4. Click on the **+ Register end device** button to add a new end device to the application.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f16barpressolution_lns_ttn14.png"
  width="100%"
  caption="Add the end device"
/>

5. Set the parameters of the end device, as shown in **Figure 17**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f17barpressolution_lns_ttn15.png"
  width="100%"
  caption="End device parameters"
/>

- **JoinEUI**, **DevEUI**, and **AppKey** can be automatically generated by clicking **Generate** on the TTN web page or customized by the user.

:::tip NOTE
Ensure that the three parameters - **JoinEUI**, **DevEUI**, and **AppKey** - are consistent with the parameters set in the WisToolBox application.
:::

6. After completing the settings, return to the WisToolBox app, and click **JOIN NETWORK** to send the end device network join request.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f18barpressolution_lns_ttn16.png"
  width="25%"
  caption="Sending end device network join request"
/>

7. As shown in **Figure 19**, the Sensor Hub has successfully joined the TTNv3 network server.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f19barpressolution_lns_ttn17.png"
  width="100%"
  caption="Successfully joined the TTNv3 network server"
/>

##### Visualize Data Through Datacake

Datacake is a versatile IoT platform. It offers a range of features tailored for effective data visualization and management, making it a preferred choice for IoT projects requiring efficient monitoring and analysis.

**Create Datacake Integration**

1. In the TTN console, navigate to **Integrations** on the sidebar, proceed to the **Webhooks** section, and then click **+Add webhooks** to set up an integration.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f20barpressolution_lns_ttn18.png"
  width="100%"
  caption="Adding an integration"
/>

2. From the list of webhook templates, select the **Datacake** template.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f21barpressolution_lns_ttn19.png"
  width="100%"
  caption="Select the Datacake template"
/>

3. Generate an API key on Datacake to enable webhook authentication. To get started, register a <a href="https://datacake.co/" target="_blank">Datacake</a> account, and then log in.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f22barpressolution_lns_dc1.png"
  width="100%"
  caption="Log in to the Datacake IoT platform"
/>

4. Navigate to the Datacake workspace. Select **Members** on the sidebar, switch to the **API Users** tab, then click the **Add API User** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f23barpressolution_lns_dc2.png"
  width="100%"
  caption="Add API User"
/>

5. Enter the name of the API User, for instance, **TTS API**. Set the relevant parameters accordingly and click  **Save** to finalize the creation process.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f24barpressolution_lns_dc3.png"
  width="70%"
  caption="Set Parameters"
/>

6. Click the **Copy** button to copy the generated Datacake API Token.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f25barpressolution_lns_dc4.png"
  width="100%"
  caption="Copy the generated Datacake API Token"
/>

7. Back on the TTN website, enter **sensorhub** in the **Webhook ID** field (as an example), and paste the Datacake API Token you previously copied into the **Token** field. Click the **Create Datacake Webhook** button to generate the Datacake Webhook.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f26barpressolution_lns_dc5.png"
  width="100%"
  caption="Create the Datacake Webhook"
/>

**Add Sensor Hub to Datacake**

1. To add a new device, select **Devices** in the sidebar and click the **+Add Device** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f27barpressolution_lns_dc6.png"
  width="100%"
  caption="Add a Device"
/>

2. Choose **LoRaWAN** from the options and click **Next** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f28barpressolution_lns_dc7.png"
  width="70%"
  caption="Choose LoRaWAN connectivity"
/>

3. As the Sensor Hub is a new device, there is no pre-existing template. Create a template by clicking **New Product**, enter the **Product Name**, and click **Next** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f29barpressolution_lns_dc8.png"
  width="70%"
  caption="Create a New Product"
/>

4. Choose a network server for your device. In this guide, select **The Things Stack V3**, then click **Next** to continue.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f30barpressolution_lns_dc9.png"
  width="70%"
  caption="Select the Things Stack V3"
/>

5. In the **STEP 3 Devices** tab, enter the device **DEVEUI** and **NAME** fields, and click **Next** to continue.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f31barpressolution_lns_dc10.png"
  width="70%"
  caption="Add DEVEUI and Name"
/>

6. In **Step 4 Plan**, select the preferred subscription plan, and click **Add 1 device** to add the device. For this example, choose **Free**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f32barpressolution_lns_dc11.png"
  width="70%"
  caption="Select a subscription plan"
/>

7. The registered device can now be viewed on the **Devices** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f33barpressolution_lns_dc12.png"
  width="100%"
  caption="Registered device"
/>

**Create a Payload Decoder**

1. Click the successfully registered device and go to the **Configuration** tab. Scroll down to the **Payload Decoder** field, then copy and save the decoder code.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f34barpressolution_lns_dc13.png"
  width="100%"
  caption="Configuration tab"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f35barpressolution_lns_dc14.png"
  width="100%"
  caption="Decoder code"
/>

<details>
<summary> Click to view the code </summary>

```js
function lppDecode (bytes) {
var sensor_types = {
	0: { 'size': 1, 'name': ' digital_in ', 'signed': false, 'divisor': 1 },
	1: { 'size': 1, 'name': ' digital_out ', 'signed': false, 'divisor': 1 },
	2: { 'size': 2, 'name': ' analog_in ', 'signed': true, 'divisor': 100 },
	3: { 'size': 2, 'name': ' analog_out ', 'signed': true, 'divisor': 100 },
	100: { 'size': 4, 'name': 'generic', 'signed': false, 'divisor': 1 },
	101: { 'size': 2, 'name': 'illuminance', 'signed': false, 'divisor': 1 },
	102: { 'size': 1, 'name': 'presence', 'signed': false, 'divisor': 1 },
	103: { 'size': 2, 'name': 'temperature', 'signed': true, 'divisor': 10 },
	104: { 'size': 1, 'name': 'humidity', 'signed': false, 'divisor': 1 },
	112: { 'size': 2, 'name': ' humidity_prec ', 'signed': true, 'divisor': 10 },
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
	134: { 'size': 6, 'name': ' gyrometer ', 'signed': true, 'divisor': 100 },
	135: { 'size': 3, 'name': ' colour ', 'signed': false, 'divisor': 1 },
	136: { 'size': 9, 'name': ' gps ', 'signed': true, 'divisor': [10000, 10000, 100] },
	137: { 'size': 11, 'name': ' gps ', 'signed': true, 'divisor': [1000000, 1000000, 100] },
	138: { 'size': 2, 'name': ' voc ', 'signed': false, 'divisor': 1 },
	142: { 'size': 1, 'name': 'switch', 'signed': false, 'divisor': 1 },
	188: { 'size': 2, 'name': ' soil_moist ', 'signed': false, 'divisor': 10 },
	190: { 'size': 2, 'name': ' wind_speed ', 'signed': false, 'divisor': 100 },
	191: { 'size': 2, 'name': ' wind_direction ', 'signed': false, 'divisor': 1 },
	192: { 'size': 2, 'name': ' soil_ec ', 'signed': false, 'divisor': 1000 },
	193: { 'size': 2, 'name': ' soil_ph_h ', 'signed': false, 'divisor': 100 },
	194: { 'size': 2, 'name': ' soil_ph_l ', 'signed': false, 'divisor': 10 },
	195: { 'size': 2, 'name': 'pyranometer', 'signed': false, 'divisor': 1 },
	203: { 'size': 1, 'name': 'light', 'signed': false, 'divisor': 1 },
};


function arrayToDecimal (stream, is_signed , divisor) {
	var value = 0;
	for (var i = 0; i < stream.length ; i ++) {
		if (stream[ i ] > 0xFF)
			throw 'Byte value overflow!';
		value = (value << 8) | stream[ i ];
	}
	if ( is_signed ) {
		var edge = 1 << ( stream.length ) * 8; // 0x1000..
		var max = (edge - 1) >> 1; // 0x0FFF.. >> 1
		value = (value > max) ? value - edge : value;
	}
	value /= divisor;
	return value;
}

var sensors = [];
var i = 0;
while ( i < bytes.length ) {
	var s_no = bytes[ i ++];
	var s_type = bytes[ i ++];
	if ( typeof sensor_types [ s_type ] == 'undefined') {
		throw 'Sensor type error!: ' + s_type ;
	}

	var s_value = 0;
	var type = sensor_types [ s_type ];
	switch ( s_type ) {
		case 113: //Accelerometer
		case 134: // Gyrometer
			s_value = {
				'x': arrayToDecimal ( bytes.slice ( i + 0, i + 2), type.signed , type.divisor ),
				'y': arrayToDecimal ( bytes.slice ( i + 2, i + 4), type.signed , type.divisor ),
				'z': arrayToDecimal ( bytes.slice ( i + 4, i + 6), type.signed , type.divisor )
			};
			break;
		case 136: // GPS Location
			s_value = {
				'latitude': arrayToDecimal ( bytes.slice ( i + 0, i + 3), type.signed , type.divisor [0]),
				'longitude': arrayToDecimal ( bytes.slice ( i + 3, i + 6), type.signed , type.divisor [1]),
				'altitude': arrayToDecimal ( bytes.slice ( i + 6, i + 9), type.signed , type.divisor [2])
			};
			break;
		case 137: // Precise GPS Location
			s_value = {
				'latitude': arrayToDecimal ( bytes.slice ( i + 0, i + 4), type.signed , type.divisor [0]),
				'longitude': arrayToDecimal ( bytes.slice ( i + 4, i + 8), type.signed , type.divisor [1]),
				'altitude': arrayToDecimal ( bytes.slice ( i + 8, i + 11), type.signed , type.divisor [2])
			};
			sensors.push ({
				'channel': s_no ,
				'type': s_type ,
				'name': 'location',
				'value': "(" + s_value.latitude + "," + s_value.longitude + ")"
			});
			sensors.push ({
				'channel': s_no ,
				'type': s_type ,
				'name': 'altitude',
				'value': s_value.altitude
			});
			break;
		case 135: // Color
			s_value = {
				'r': arrayToDecimal ( bytes.slice ( i + 0, i + 1), type.signed , type.divisor ),
				'g': arrayToDecimal ( bytes.slice ( i + 1, i + 2), type.signed , type.divisor ),
				'b': arrayToDecimal ( bytes.slice ( i + 2, i + 3), type.signed , type.divisor )
			};
			break;

		default: // All the rest
			s_value = arrayToDecimal ( bytes.slice ( i , i + type.size ), type.signed , type.divisor );
			break;
	}

	sensors.push ({
		'channel': s_no ,
		'type': s_type ,
		'name': type.name,
		'value': s_value
	});

	i += type.size ;
}

return sensors;
}

// For TTN, Helium and Datacake
function Decoder(bytes, fport ) {
// bytes = input.bytes ;
// fPort = input.fPort ;

// flat output (like original decoder):
var response = {};
lppDecode (bytes, 1). forEach (function (field) {
	response[field['name'] + '_' + field['channel']] = field['value'];
});

// Enable only for Datacake
response['LORA_RSSI'] = (!! normalizedPayload.gateways && !! normalizedPayload.gateways [0] && normalizedPayload.gateways [0]. rssi ) || 0;
response['LORA_SNR'] = (!! normalizedPayload.gateways && !! normalizedPayload.gateways [0] && normalizedPayload.gateways [0].snr) || 0;
response['LORA_DATARATE'] = normalizedPayload.data_rate ;

return response;
}
```
</details>


2. Displace the menu bar to the **+Add Field** section, and click **+Add Field**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f36barpressolution_lns_dc15.png"
  width="100%"
  caption="Add Field"
/>

3. The **Add Field** window appears. Fill out the fields shown in **Figure 37** to configure the stored data in the device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f37barpressolution_lns_dc16.png"
  width="70%"
  caption="Configuration fields"
/>

:::tip NOTE
- Enter a suitable name in the **Name** field.
- The **Identifier** field will be automatically filled in based on the name.
- When an uplink is received, refresh the page, and the **CURRENT VALUE** field will be updated.
- Leave everything else as default, and click **Add Field** to complete the setup.
:::

3. Repeat the above steps to add the **Temperature** field. Once completed, it should look like the example shown in **Figure 38**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f38barpressolution_lns_dc17.png"
  width="100%"
  caption="Successfully added fields"
/>

**Create a Dashboard**

1. To create a dashboard, toggle the **edit mode** switch on the device **Dashboard** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f39barpressolution_lns_dc18.png"
  width="100%"
  caption="Turn on the edit mode switch"
/>

2. Click **+Add Widget** to add a visualization widget.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f40barpressolution_lns_dc19.png"
  width="100%"
  caption="Add visualization widget"
/>

3. Select **Value** from the menu to create a new dashboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f41barpressolution_lns_dc20.png"
  width="70%"
  caption="Select Value to create a new dashboard"
/>

:::tip NOTE
You can select different types of widgets to accommodate various data formats.
:::

4. In the **Title** field under the **Basics** tab, name the widget, for example, **Barometric Pressure**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f43barpressolution_lns_dc22.png"
  width="70%"
  caption="Name the Widget"
/>

5. Under the **Data** tab, pull down the **Field** tab bar, select **Barometric Pressure**, and set the unit to **hPa**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f42barpressolution_lns_dc21.png"
  width="70%"
  caption="Setting Parameters"
/>

6. Under the **Gauge** tab, select the gauge type and color, set the range of values for the widget, and then click **Save**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f44barpressolution_lns_dc23.png"
  width="70%"
  caption="Set Gauge"
/>

7. When you finish adding the widgets, turn off the **edit mode** switch to save the edits.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f45barpressolution_lns_dc24.png"
  width="100%"
  caption="Added Widget"
/>

#### Built-In Network Server Setup

The RAK gateway comes with a built-in NS, which eliminates the need to deploy NS in the cloud or locally. This gateway is suitable for small-sized industrial application scenarios and offers various advantages such as cost savings, reduced R&D investment, high execution efficiency, and shorter delays.

The built-in network server of the RAK gateway provides MQTT and HTTP integration that allows for post-processing data and implementing solutions based on the needs.

This section will use the public MQTT broker integration as an example to demonstrate how to use the built-in network server to create a visualization application on ThingsBoard.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f46built_inserveapplicationflow.png"
  width="100%"
  caption="Gateway built-in NS application scenario"
/>

##### Configure ThingsBoard

1. Log in to <a href="https://thingsboard.cloud/login" target="_blank">ThingsBoard</a>. If you don't have an account, <a href="https://thingsboard.cloud/signup" target="_blank">create one</a> before proceeding.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f47barpressolution_bins_tb1.png"
  width="70%"
  caption="ThingsBoard authentication page"
/>

2. After successfully logging in, you will be directed to the ThingsBoard homepage.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f48barpressolution_bins_tb2.png"
  width="100%"
  caption="ThingsBoard Homepage"
/>

3. Navigate through **Integration center > Integrations > Data converters** in the left navigation tree to create a data converter for the uplink.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f49barpressolution-bins-tb3.png"
  width="100%"
  caption="Create a Data Converter"
/>

4. Click the **Add Data Converter** icon and choose the **Create new converter** option.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f50barpressolution_bins_tb4.png"
  width="70%"
  caption="Create a new Converter"
/>

5. Enter the name of the decoder in the **Name** field (for example, *Uplink decoder*), leave the **Type** field as **Uplink**, and select the **JavaScript** option.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f51barpressolution_bins_tb5.png"
  width="70%"
  caption="Add the decoder code"
/>

6. Edit the decoder code by copying the following code into the edit box, then click **Add** to include the uplink decoder.

<details>
<summary> Click to view the code </summary>

```js

/** Decoder **/
//decode payload to string
var payloadStr = decodeToString (payload);
var data = JSON.parse ( payloadStr ).data;
var bytes = atob (data).split('').map(function (c) {
return c.charCodeAt (0);
});

var values = {};
let i = 0;
while ( i < bytes.length ) {
var channelId = (bytes[ i ] << 8) | bytes[ i + 1];
var value;
switch ( channelId ) {
case 0x0367:
value = (bytes[ i + 2] << 8) | bytes[ i + 3];
      values.temperature = value / 10.0;
      i += 4;
break;
case 0x0473:
value = (bytes[ i + 2] << 8) | bytes[ i + 3];
      values.pressure = value / 10.0;
      i += 4;
break;
default:
break;
}
}

var integrationName = 'MQTT Integration';
var deviceName = ' rak1902 ';
var result = {
  deviceName : deviceName ,
attributes: {
    integrationName : metadata[' integrationName '],
	temperature: values.temperature ,
	pressure: values.pressure ,
},
};

/** Helper functions **/
function decodeToString (payload) {
return String.fromCharCode.apply (String, payload);
}
return result;

/** Helper functions **/
function decodeToString (payload) {
return String. fromCharCode. apply (String, payload);
}
return result;
```
</details>

:::tip NOTE
In the above code, the word `rak1902` marked is the device ID, which is the device name. This parameter must match the device name added in section **Configure the Gateway**. In this example, it is *rak1902*.
:::

7. Navigate to the **Integration Center > Integrations** menu and click the **Add Integration** icon to add the MQTT integration.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f52barpressolution_bins_tb6.png"
  width="100%"
  caption="Add the MQTT Integration"
/>

8. Enter the name of the integration (for example, *MQTT Integration*) in the **Name** field and select **MQTT** in the Type drop-down menu. Click **Next** to continue.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f53barpressolution_bins_tb7.png"
  width="70%"
  caption="Basic Settings"
/>

9. In the **Uplink data converter** options, click **Select existing** to choose the previously created decoder (**Uplink Decoder**), then click **Next**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f54barpressolution_bins_tb8.png"
  width="70%"
  caption="Select the created decoder"
/>

10. In the **Downlink data converter** interface, no configuration is necessary and just click **Skip** to bypass this setup.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f55barpressolution_bins_tb9.png"
  width="70%"
  caption="WisGate OS Web Management Platform"
/>

11. Configure connection options. **Host** is the MQTT broker address used for messages. The Host of the external MQTT broker used in this example is `broker.hivemq.com`. You can choose to use other brokers with a different Host.


12. Enter the address `broker.hivemq.com` in the **Host** field, with the port number `1883`. Click the **Add topic filter** button to configure the subscription topic.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f55-1barpressolution_bins_tb9.png"
  width="70%"
  caption="Configure the connection options
"
/>

**Configure the subscription topic**

````
application/{{application_name}}/device/{{ device_EUI }}/join
application/{{application_name}}/device/{{ device_EUI }}/ rx
application/{{application_name}}/device/{{ device_EUI }}/ tx
application/{{application_name}}/device/{{ device_EUI }}/ack
application/{{application_name}}/device/{{ device_EUI }}/status
````

   - **application_name**: The application ID created in the gateway.
   - **device_EUI**: The device EUI of the end device.

13. Modify the parameter values corresponding to the topics based on the actual application created and the device used.

:::tip NOTE
The values in the subscription topic must be all lowercase. For example, `application/1/device/0123456789abcdef/join`. 
:::


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f56barpressolution_bins_tb10.png"
  width="60%"
  caption="Configure and add the subscription topics"
/>

14. After configuring the details, click on **Add** to save and complete the settings.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f56-1barpressolution_bins_tb10-1.png"
  width="100%"
  caption="Configuration completed"
/>

##### Configure the Gateway

This section will use the <a href="https://store.rakwireless.com/products/rak7268-8-channel-indoor-lorawan-gateway?variant=42316475924678" target="_blank">RAK7268 V2 WisGate Edge Lite 2</a> as an example.

1. To access the gateway web management platform, refer to the <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#overview" target="_blank">WisGateOS V2 user manual</a> for details.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f57barpressolution_bins_tb11.png"
  width="100%"
  caption="WisGate OS Web Management Platform"
/>

2. After successfully logging in, navigate to the **LoRa®** menu in the left navigation tree and set the **Work mode** of the gateway to the **Built-in network server**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f58barpressolution_bins_tb12.png"
  width="100%"
  caption="Set the Work mode of the gateway"
/>

3. Once done with the setting, click the **Applications** tab, then the **Add application** button. You can also click **add one now** text link to add a new application.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f59barpressolution_bins_tb13.png"
  width="100%"
  caption="Applications Tab"
/>

4. Configure the following information: **Application name**, **Application description**, and **Application Type**.

- **Unified Application key**: Choose this option if all devices will use the same application key. Once selected, a field for the application key appears, where you can manually type in an application key or click the **Autogenerate** button to generate one.


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f60barpressolution_bins_tb14.png"
  width="70%"
  caption="Configure the Application key"
/>

- After enabling the **Auto Add Device** option, configure the **Application EUI option**. The value needs to be consistent with the node value. Once you have verified the application EUI and key, the device will be added automatically to the application.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f61barpressolution_bins_tb15.png"
  width="70%"
  caption="Auto Add Device"
/>

:::tip NOTE
You can obtain the values by either querying the end device or generating it automatically and modifying the corresponding value of the device synchronously.  
:::

- **Separate Application keys**: Each device has its own application key. Add the key when registering the device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f62barpressolution_bins_tb16.png"
  width="70%"
  caption="Add Application Key"
/>

5. Once you've completed the configuration, click on **Save Application** to add the new application.

6. In the application list, locate the newly created application and navigate to the **End devices** tab. If you've enabled the **Auto Add Device** function, the device will be automatically registered upon the addition request.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f63barpressolution_bins_tb17.png"
  width="100%"
  caption="End Devices Tab"
/>

7. Click the **Add end device** button. In the **End device information** interface, fill in the following information:

- **Activation Mode**: Select the activation mode of the device: OTAA or ABP. 
  - Choosing ABP mode creates two additional fields: **Application Session Key** and **Network Session Key**. 
  - In this example, use OTAA activation mode.
- **End device (group) name**: Enter the name of the end device or the group it belongs to.
- **End device description (optional)**: Optionally provide a description for the end device.
- **Class**: Select **Class A** for device’s operating mode.
- **Frame Counter Width**: Keep the default value.
- **LoRaWAN MAC Version**: The protocol version (v1.0.3) of the end device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f64barpressolution_bins_tb18.png"
  width="70%"
  caption="Add new end devices"
/>

8. After completing, click **Add end devices** to proceed to the next step.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f64-1barpressolution_bins_tb18-1.png"
  width="70%"
  caption="Add the device to the device list"
/>

9. In the **Adding end devices** interface, enter the device EUI in the **End Device EUI (Main)** field and select the **Add to End Devices list** button. Then click **Add end devices** to complete adding the end device.

:::tip NOTE
- The device EUI configured here must match the end device. You can either obtain it by querying the end device or entering one (1) EUI and synchronously updating the corresponding value of the end device.
- If the EUI is correct, the device will be displayed in the **End devices list**.
- If the EUI is incorrect, the device will be displayed in the **End devices with an error**.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f65barpressolution_bins_tb19.png"
  width="70%"
  caption="Complete the end device addition"
/>

10. Click the **Add** button to confirm adding the device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f66barpressolution_bins_tb20.png"
  width="70%"
  caption="Confirm to add the end device"
/>

11. When finished, enter the **End devices** interface, where you can see the created end device.

##### Connect the Sensor Hub to the Built-In Network Server

For specific configuration on how to connect SensorHub to the server, refer to **SensorHub Network Configuration > LoRaWAN Application Scenario**.

Once completed, the device will join the network. As shown in **Figure 70**, the end device **SensorHub** has successfully connected to the gateway's built-in server.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f67barpressolution_bins_tb21.png"
  width="100%"
  caption="End device  SensoHub has been connected"
/>

##### Configure the MQTT Integration

1. Go to the **LoRa® > Configuration > Integration Interface Parameters** section.

2. Toggle the **Enable Integration Interface** option and select **Generic MQTT** as the **Integration mode**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f68barpressolution_bins_tb22.png"
  width="70%"
  caption="Set up MQTT integration"
/>

3. In the **MQTT Broker Address** option, enter `broker.hivemq.com` then click **Save changes**.

4. After the device has joined and has been sending uplink data, check the uplink data in **ThingsBoard > Integrations > Your Integration > Events**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f69barpressolution_bins_tb23.png"
  width="100%"
  caption="View the gateway uplink data"
/>

##### Visualize Data Through ThingsBoard

1. After creating the data converter, integrating, and obtaining some data in the **Event** tab, check the automatically created devices based on the decoder in the **Entities** > **Devices** > **Groups** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f70barpressolution_bins_tb24.png"
  width="100%"
  caption="Check the device"
/>

2. Click the group named **All** in the **Device groups** menu to automatically create a decoder device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f71barpressolution_bins_tb25.png"
  width="100%"
  caption="Automatically created decoder device"
/>

3. Click the device and go to the **Attributes** tab, where you will see the node data.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f72barpressolution_bins_tb26.png"
  width="100%"
  caption="Node data"
/>

4. To visualize the data, simply select the values you wish to display, then click the **Show on widget** button.

5. On the next page, choose the desired widget for your data from the **Current bundle** drop-down menu. In this example, select **Outdoor Environment**, and then select the appropriate visualization chart for the **Barometer** by clicking the slide icon.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f74barpressolution_bins_tb28.png"
  width="100%"
  caption="Select Widget"
/>

6. After selecting the widget, click **Add to dashboard** to proceed.

By default, the profile does not have a dashboard, so you need to select **Create new dashboard** and enter a name for the dashboard in the **New dashboard title** field, for example, *Sensor Hub*.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f76barpressolution_bins_tb30.png"
  width="70%"
  caption="Enter the dashboard name"
/>

7. After setting the name of the dashboard, click the **Add** button to add more widgets. Alternatively, check the **Open dashboard** option to automatically open the created dashboard after adding the widget.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f77barpressolution_bins_tb31.png"
  width="100%"
  caption="Dashboard created"
/>

:::tip NOTE
- If the **Open** dashboard option is not selected, you can still easily view the added widgets via **Dashboard groups** > **All** > [**Group Name**].
- Click the **Edit mode** icon in the upper right corner to set the appropriate name and unit of Pressure.
- The ThingsBoard visualization dashboard editor allows you to adjust the size and shape of widgets by dragging the edges of the widgets in the **Edit mode**.
:::

8. If the above settings are correct, the final visualization widget on the Dashboard should resemble **Figure 79**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f77barpressolution_bins_tb31.png"
  width="100%"
  caption="Dashboard created"
/>

Follow the previous steps to add the **Temperature** data if you need to monitor this variable as well.

### NB-IoT/LTE CAT-M1 Application

#### Connect Sensor Hub to MQTT Server


In the **Network Server and Visualization Configuration** section, the server has been set as a public MQTT broker: `broker.hivemq.com`. You can also choose other brokers or servers, such as AWS IoT Core (optional), according to the actual usage scenario. 

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f79nb-iotlte-cat-m1-application-scenari.png"
  width="100%"
  caption="NB-IoT/LTE CAT-M1 application scenario"
/>

#### Visualize Data Through Datacake

In this example, you will use Datacake as the visualization platform. Datacake is a versatile IoT platform designed to visualize data from nodes in a user-friendly manner.

To get started, create an account on the <a href="https://datacake.co/" target="_blank">official website</a> and log in.

##### Add Sensor Hub to Datacake

1. After logging in to your account, navigate to the **Devices** tab and click **+ Add Device** to proceed with adding the Sensor Hub end device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f80barpressolution_nbi1.png"
  width="100%"
  caption="Devices Page"
/>

2. Select the **API** option and click **Next** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f82barpressolution_nbi3.png"
  width="70%"
  caption="Select API"
/>

3. As the device is new and there's no ready-made template, choose **New Product** from the **Datacake Product** options. Enter the device name in the **Product Name** field, then click **Next** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f83barpressolution_nbi4.png"
  width="70%"
  caption="Select New Product"
/>

4. The **SERIAL NUMBER** field can be left blank. Datacake will randomly generate a serial number for the device, then click **Next**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f84barpressolution_nbi5.png"
  width="70%"
  caption="Add Devices"
/>

5. Select the preferred subscription plan, then click **Add 1 device**. For this example, choose **Free**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f85barpressolution_nbi6.png"
  width="70%"
  caption="Select a subscription plan"
/>

6. The registered device can now be viewed on the **Devices** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f86barpressolution_nbi7.png"
  width="100%"
  caption="Registered device"
/>

##### MQTT Configuration

1. Click the name of the device you just created in the list to enter the interface, then select the **Configuration** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f88barpressolution_nbi9.png"
  width="100%"
  caption="Configuration tab"
/>

2. Scroll down to the **API Configuration** option and copy the **Serial number**. Save it locally for later use.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f89barpressolution_nbi10.png"
  width="100%"
  caption="Copy the serial number"
/>

3. Continue scrolling down to the **MQTT Configuration** option and configure the external MQTT Broker.

4. Click **+Add new MQTT server** and configure the relevant parameters.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f90barpressolution_nbi11.png"
  width="100%"
  caption="Configure the external MQTT Broker"
/>

5. Fill in the relevant information based on the actual server used, then click **Test Connection** to verify whether Datacake can successfully connect to the **MQTT Broker**. The information shown in **Figure 89** is just an example.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f91barpressolution_nbi12.png"
  width="70%"
  caption="Configure the relevant parameters"
/>

:::tip NOTE
If SSL/TLS encryption and authentication are set for more secure communication, ensure to configure them accordingly in this section. However, for this example, you can skip this option.
:::

6. If the connection is successful, you will see the message **Connection successful**. Click **Add MQTT Server** to complete the addition of the MQTT server.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f92barpressolution_nbi13.png"
  width="100%"
  caption="Connection established successfully"
/>

7. After successfully adding the MQTT server, click on **+Add Uplink Decoder** to add a decoder.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f93barpressolution_nbi14.png"
  width="100%"
  caption="Add MQTT Server"
/>

8. A new window will appear, and fill in the fields according to your project.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f94barpressolution_nbi15.png"
  width="70%"
  caption="Add Uplink Decoder"
/>

- **Subscribe to topics**: Configure the subscription topics, that is, the value of the **Publish Topic** configured in the **Network Server and Visualization Configuration** section.
- **Decoder function**: Copy the following decoding code and paste it into the **Decoder function** space.

````js

var decoded = [];
var data = JSON.parse ( payload.replace (/\s*/g,""));
for (var key in data) {
        decoded.push (
{
device: "e2517219-bc32-482c-af3f-dbc95200adce" ,
field: key,
value: data[key]
}
)
}
return decoded;
}
````
:::tip NOTE
In the above code, make sure that the parameter **serial_number** (device: `e2517219-bc32-482c-af3f-dbc95200adce`) matches the serial number saved locally earlier.
:::

9. Once completed, click **Add uplink decoder**.
10. In the **Fields** option, click **+ Add Field** to show the monitoring values of the devices. Each device can create a certain number of fields, also known as a **_data point_**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f95barpressolution_nbi16.png"
  width="100%"
  caption="Add Field"
/>

11. Set the necessary parameters of the **Field**. For **Fields** with multiple data points, add them one by one. Once done, click **Add Field**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f95barpressolution_nbi17.png"
  width="70%"
  caption="Set the related parameters of the field"
/>

:::tip NOTE
The **Identifier** field will be automatically filled based on the name.
:::

12. Repeat the above steps to add the **Temperature** field. 
13. Once the uplink data is received, the **Current Value** column in the Fields list will display the current monitoring value from the sensor.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f96barpressolution_nbi18.png"
  width="100%"
  caption="Added sensor monitoring values"
/>

##### Create a Dashboard to Visualize Data

**Dashboards** can be customized depending on the specific needs and preferences of a project. Follow the steps below to add widgets and visualize the data.

1. On the device details page, navigate to the **Dashboard** tab, then toggle on the edit mode switch.
2. Click on the **+ Add Widget** button to add a widget for visualizing data.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f97barpressolution_nbi19.png"
  width="100%"
  caption="Open the edit mode"
/>

3. Choose what type of widgets you want to display. For this example, select **Value** to visualize the Barometric Pressure values. 

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f98barpressolution_nbi20.png"
  width="70%"
  caption="Select and add widgets for visualizing data"
/>

4. Click on the **Data** tab. Choose the field for visualization from the **Field** options and set the unit of the field, which is **hPa** in this example.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f99barpressolution_nbi21.png"
  width="70%"
  caption="Select the visualization data field"
/>

5. Repeat the above steps to add the **Temperature** field. After configuring the widgets, click **Save**. 

6. Once done with the dashboard configuration, turn off the **edit mode** switch to save the settings.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/lorawan-network-server/f100barpressolution_nbi22.png"
  width="100%"
  caption="Barometric Pressure data visualization"
/>

<RkBottomNav/>