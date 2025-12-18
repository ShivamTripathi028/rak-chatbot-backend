---
slug: /product-categories/wisnode/barometric-pressure/quickstart/
title: Barometric Pressure Monitoring Sensor Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your Sensor Hub Barometric Pressure solution. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: "https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/barometric-pressure-sensor.png"
keywords:
  - quickstart
  - wisnode
  - Power Supply
  - Installation
  - Barometric Pressure
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# Barometric Pressure Monitoring Sensor Quick Start Guide

## Prerequisites

### What Do You Need?

Before proceeding with each step for using the RAK2560 WisNode Sensor Hub module, ensure that you have the necessary items listed below:

#### Hardware Tools

- [Sensor Hub Barometric Pressure Monitoring Solution](https://store.rakwireless.com/products/atmosBarPresere-monitoring?m=3&h=sensorhub-solution&variant=42510932508870)
- [Solar Battery Lite for Sensor Hub](https://store.rakwireless.com/products/rak-battery-lite-solar-power-solution-rak9154?m=9&h=power-supplies-accessories) (Optional)
- Additional accessories: Probe Cable, Probe Splitter, power supply, and others (numbers and variations depending on the use case)
- An Android or iOS mobile device with Bluetooth and NFC

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f1barpressolution_accesories.png"
  width="80%"
  caption="Sensor Hub Solar Radiation Solution Accesories"
/>

#### Software

- [WisToolBox](https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/wistoolbox-mobile/)

## Solution Configuration

### Sensor Hub Setup

#### SIM Card Installation

If the selected solution utilizes the NB-IoT/LTE CAT-M wireless communication mode, follow these steps to insert a SIM card. If you opt for the LoRaWAN wireless communication mode, skip this section, as a SIM card is not required.

1. Remove the back cover by unscrewing the four screws with a cross screwdriver.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f2barpressolution_siminstall1.png"
  width="40%"
  caption="Remove the back cover"
/>

2. Insert the SIM card into the groove, then gently push it into the card slot.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f3barpressolution_siminstall2.png"
  width="50%"
  caption="Insert the SIM card"
/>

#### Sensor Hub Mounting

##### Wall Mounting

1. Use a 5&nbsp;mm drill bit to drill holes in the wall, then insert the screw anchors into the holes.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f4barpressolution_wallmount1.png"
  width="50%"
  caption="Installation preparation"
/>

2. Secure the mounting bracket to the wall by using self-tapping screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f5barpressolution_wallmount2.png"
  width="30%"
  caption="Secure the mounting bracket"
/>

3. Align the device's hanging tab with the slots on the bracket, and then insert the tab into the slots. Pull the device downwards until it snaps into place.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f6barpressolution_wallmount3.png"
  width="50%"
  caption="Align the device with the hanging tabs"
/>


##### Pole Mounting

1. Secure the mounting bracket to the pole using a steel strap.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f7barpressolution_polemount1.png"
  width="20%"
  caption="Fix the Mounting Bracket"
/>

:::tip NOTE
Mount the bracket on a pole with a 50-80&nbsp;mm diameter. For larger poles, use a bigger steel strap. The standard kit does not include a larger steel strap. Purchase separately if needed.
:::

2. Align the hanging tab of the device with the slots on the bracket, then insert the tab into the slots. Gently pull the device downwards until it securely snaps in place.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f8barpressolution_polemount2.png"
  width="50%"
  caption="Device installation"
/>

3. Insert a security screw at the top to fasten the device and the bracket together.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f9barpressolution_polemount3.png"
  width="30%"
  caption="Fasten the device and the bracket"
/>

###  Install the Barometric Pressure Sensor 

The RAK1902 Barometric Pressure monitoring Sensor is pre-connected to the Sensor Hub at the factory, eliminating the need for any additional assembly by the user.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f10barpressolution_sensor.png"
  width="50%"
  caption="Sensor Probe Installation"
/>

## Power Supply Setup

The SensorHub Barometric Pressure Monitoring Sensor RAK1902 supports three power supply methods: battery-powered, connected to a solar panel, or a 12&nbsp;V<sub>DC</sub> power supply.

### RAK9154 Solar Battery Installation

:::tip NOTE
- Mount the bracket on a pole with a 50-80&nbsp;mm diameter. For larger poles, use a bigger steel strap. The standard kit does not include a larger steel strap. Purchase separately if needed.
- The Sensor Hub supports a power supply using 2 to 4 ER18505 non-rechargeable batteries, which should be purchased separately if needed. For more information on compatible batteries, refer to the [Sensor Hub user manual.](https://docs.rakwireless.com/product-categories/wisnode/rak2560/overview/)
- The Sensor Hub has two models based on the communication mode: LoRaWAN only and LoRaWAN+NB-IoT. The Sensor Hub's NB-IoT module supports two LTE (Long-Term Evolution) categories: CAT M1 and CAT NB2. CAT M1 offers higher data transfer rates and lower latency, while CAT NB2 provides ultra-low power consumption and a larger coverage range, making it ideal for battery-powered devices requiring long-term connectivity.
:::

1. Secure the mounting bracket on the pole with two steel straps.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f13barpressolution_batteryins1.png"
  width="30%"
  caption="Secure the mounting bracket"
/>

2. Attach the mounting plate to the RAK9154 with two (2) M3 screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f14barpressolution_batteryins2.png"
  width="40%"
  caption="Attach the mounting plate"
/>

3. Install the RAK9154 to the back of the solar panel with four (4) screws and nuts.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f15barpressolution_batteryins3.png"
  width="50%"
  caption="Attach the RAK9154 to solar panel"
/>

4. Connect the cable of the solar panel to the **PV input** connector of RAK9154. Install two (2) M6 screws to the mounting plate with a clearance of about 3&nbsp;mm.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f16barpressolution_batteryins4.png"
  width="50%"
  caption="RAK9154 and Solar Panel Connection"
/>

5. Suspend the solar panel on the mounting bracket, adjust its angle and direction, and then tighten the two (2) M6 screws along with the remaining two screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f17barpressolution_batteryins5.png"
  width="40%"
  caption="Install the solar panel combination"
/>

6. Connect Sensor Hub and RAK9154. Use a cable to link the remaining connection port of the Sensor Hub to the lithium battery Output 1 SP11 connection port of RAK9154.

:::tip NOTE
When connecting to RAK9154, ensure that the Sensor Hub is connected to the Output 1 connection port.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f18barpressolution_batteryins6.png"
  width="60%"
  caption="Connect the Sensor Hub and RAK9154"
/>

7. Once the connection is complete, the Sensor Hub is ready to be powered up.

### 12&nbsp;V<sub>DC</sub> Power Supply Installation

1. Connect the power adapter to the external power cable of Sensor Hub using a circular DC connector.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f19barpressolution_powersupply.png"
  width="50%"
  caption="Power adapter connection"
/>

2. Connect the external power cable to the Sensor Hub using the SP11 connector.
3. Align the white dot mark on the SP11 connector plug of the external power cable with the white dot mark on the Sensor Hub SP11 connector socket, and push the plug firmly into the socket.
4. After the plug and socket are connected, tighten the locking nut to secure the connection of the SP11 connector. The external power cable can connect to any Sensor Hub connection port.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f20barpressolution_probeinstall1.png"
  width="50%"
  caption="Connect external power supply"
/>

## Software Configuration Guide

### Sensor Hub Configuration

#### Power Up Sensor Hub

After installing all hardware components, connect the power supply. If the power supply consists of a solar panel and a battery, the device will power on automatically once all hardware has been installed.

:::warning
To prevent damage to the device, refrain from powering up the Sensor Hub before connecting it to the sensor. It is advisable to use the 12&nbsp;V<sub>DC</sub> adapter provided with the Sensor Hub for optimal performance.
:::

#### Connect Sensor Hub to WisToolBox

1. Download and install the WisToolBox app on your smart mobile device. The WisToolBox app is available for download from the Apple App Store and the Android Google Play Store.

2. Initiate the app and confirm that NFC and Bluetooth are enabled on your mobile device. Click on **START**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f21barpressolution_wtb_start.png"
  width="40%"
  caption="Start App"
/>

3. On the **Select connection mode** menu, choose **NFC Activation**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f22barpressolution_wtb_seldevice1.png"
  width="40%"
  caption="Select NFC Activation"
/>

4. Select the **Sensor HUB** option in the device selection interface to establish a connection.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f23barpressolution_wtb_seldevice2.png"
  width="40%"
  caption="Select Sensor Hub"
/>

5. Click the **CONNECT** button to initiate the scanning process for devices.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f24barpressolution_wtb_nfcconn.png"
  width="40%"
  caption="Click on the CONNECT button"
/>

6. Hold your mobile device close to the **N** symbol on the Sensor Hub device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f25barpressolution_wtb_scandevices.png"
  width="40%"
  caption="Scanning in progress"
/>

:::tip NOTE
The detection of the Sensor Hub device indicates that the device has been successfully powered up.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f26barpressolution_wtb_scansuccess.png"
  width="40%"
  caption="Scan Successful"
/>

7. After the connection is established, there will be a synchronization of device data. This process may take some time.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f27barpressolution_wtb_getdevinfo.png"
  width="40%"
  caption="Sync Device"
/>

:::tip NOTE
- By default, if no connection is established within 30 seconds, the BLE broadcast of the Sensor Hub will automatically shut down. To establish a connection, connect the RAK device immediately after turning on the power or restart the power.
- Certain Android smartphones may necessitate enabling GPS to connect to BLE. Enabling GPS does not involve the use or sharing of sensitive information with the app.

:::

8. Upon completion of data synchronization, the app will automatically transition to the **SENSOR HUB INFO** page.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f28barpressolution_wtb_shinfo.png"
  width="40%"
  caption="SENSOR HUB INFO page"
/>

9. While on the **SENSOR HUB INFO** page, configure the Uplink Settings according to the selected network.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f29barpressolution_wtb_lorasel.png"
  width="40%"
  caption="Uplink Settings option"
/>

10. Once configured, click **SAVE SELECTION**, and then the **APPLY** button to implement the configuration options.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f30barpressolution_wtb_queue.png"
  width="40%"
  caption="Apply the configuration options"
/>

After a few seconds, the synchronization progress will be completed, concluding this process.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f31barpressolution_wtb_cmndsapld.png"
  width="40%"
  caption="Commands applied successfully"
/>

### Sensor Hub Network Configuration

#### LoRaWAN Configuration

This section focuses on configuring the LoRaWAN parameters and joining the network. Before proceeding with the following steps, ensure that the gateway and Sensor Hub are connected to the server.

Refer to the **Connect the Gateway to the Server** and **Connect Sensor Hub to the Server** sections for detailed instructions.

1. Click the **LORA & LORAWAN PARAMETERS** tab. Configure the following parameters:

- <b>Global settings</b>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f32barpressolution_wtb_loraconf1.png"
  width="50%"
  caption="Global Settings"
/>

- **Join mode**: Configure the Join mode based on the device's network access mode: **Over-The-Air Activation (OTAA)** or **Activation By Personalization (ABP)**. Make sure it matches the join mode registered on the network server.
- **Active region**: Set the Active region to the device's frequency plan. Ensure that it is consistent with the gateway and device frequency plan registered on the network server.
Supported frequency bands include CN470, RU864, IN865, EU868, US915, AU915, KR920, AS923-1/2/3/4.

<b>LoRaWAN keys, ID, EUI</b>

- For the **OTAA join mode**, configure the following parameters: **Application EUI**, **Application key**, and **Device EUI**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f33barpressolution_wtb_loraconf2.png"
  width="40%"
  caption="LoRaWAN parameters"
/>  

   * **Application EUI**: Confirm that it matches the device's Application EUI as registered in the network server.
   * **Application key**: Verify its alignment with the device's Application key registered in the network server. Click **GENERATE KEY** to create a new key if needed.
   * **Device EUI**: Confirm that it matches the device's EUI as registered in the network server. 

* For the ABP join mode, configure the following parameters: **Application session key**, **Device address**, and **Network session key**.

**Data on LoRa® Network**

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f34barpressolution_wtb_loraconf3.png"
  width="40%"
  caption="Data on LoRa® Network"
/>

  * **Confirm mode**: Message confirmation mode.
  * **Enable auto join**: Determine whether to activate automatic network access. When enabled, the device will join the network automatically upon powering up.
  * **Network status**: Indicates the status of the network connection. It will be activated automatically once successfully connected to the network.
  * **ADR**: The Adaptive Data Rate optimizes data rates in the network. Toggle the button to enable or disable it.
  * **JOIN NETWORK**: After completing the network parameter, click the **JOIN NETWORK** button to run the join network command.

2. After clicking **JOIN NETWORK**, a message **Message sent** will appear, indicating that the join network command has been sent.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f35barpressolution_wtb_loraconf4.png"
  width="40%"
  caption="Join the network"
/>

#### NB-IoT/LTE CAT-M1 Configuration

This section primarily introduces the configuration of LTE-M network parameters. If you are using the NB-IoT/LTE CAT-M1 network, after connecting the device, select **LTE-M** in the **Uplink Settings** options on the **SENSOR HUB INFO** interface to display the **LTE-M PARAMETERS** configuration tab.

1. Click the **LTE-M PARAMETERS** tab and check the following parameters to ensure that the network is working properly.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f36barpressolution_wtb_nbconf1.png"
  width="40%"
  caption="View the NB-IOT PARAMETERS tab parameters"
/>

**LTE-M Network**

- **OPERATOR**: Shows the Network operator. If the operator's name is displayed, it indicates that the device has recognized the SIM card. 
For example, *T-Mobile*.

**IP Network**

- **STATUS**: If the status is **Activated**, it signifies that the network of the SIM card is functioning normally.

2. Select the **Application** option to configure the cellular network parameters.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f37barpressolution_wtb_nbconf2.png"
  width="40%"
  caption="Configure the cellular network parameters"
/>

- **Service**: Choose a service, either AWS IoT Core or Generic MQTT. For this guide, use Generic MQTT as an example.
- **Server address**: Input the server address. Using the external MQTT broker as an example, enter `broker.hivemq.com`. Enter the address based on your specific use case.
- **Server Port**: Specify the server port according to your configuration.
- **Client ID**: Set the client ID for your device.
- **Enable user auth**: Decide whether to activate user authentication for your device.
- **Enable SSL**: Decide whether to activate SSL (Secure Sockets Layer) for secure communication.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f38barpressolution_wtb_nbconf3.png"
  width="40%"
  caption="Configure the Subscription Topics"
/>

- **Publish Topic**: Specify the topic for publishing messages.
- **Data Format**: Select **JSON** as the preferred format for data transmission.
- **Subscribe Topic**: Subscribe to the topic for receiving incoming messages, as illustrated in this example.

3. Following the configuration, click **APPLY** in the command list at the bottom of the interface to implement the changes. If the message **All commands applied successfully** appears, it indicates a successful configuration modification.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f39pbarpressolution_wtb_nbconf4.png"
  width="40%"
  caption="Apply the modified configuration"
/>

4. When configured correctly and successfully connected to the server, the **Connection Status** will display as **connected**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f40barpressolution_wtb_nbconf5.png"
  width="50%"
  caption="Successfully connected to the server"
/>

### Sensor Configuration

This section details the configuration process of the RAK1902 Barometric Pressure sensor. It shows how to access the monitoring data and device details of the Barometric Pressure sensor. Additionally, there’s an option to configure other information for each monitoring parameter, such as the uplink data sending period and threshold.

1. To start with, click the **SENSOR PROBE** tab to display the connected Barometric Pressure sensor. 

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f41barpressolution_wtb_shconf1.png"
  width="40%"
  caption="Barometric Pressure Sensor"
/>

2. Click the dropdown arrow to expand the details of the sensor.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f42barpressolution_wtb_shconf2.png"
  width="40%"
  caption="Sensor Information"
/>

- **Temperature**: Temperature value.
- **Pressure**: Pressure value.
- **FETCH DATA**: Update the monitoring data from the sensor.
- **Device details**

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f43barpressolution_wtb_shconf3.png"
  width="30%"
  caption="Sensor Details"
/>

3. Click the downward arrow in the **Pressure** tab bar to set the periodic uplink sending of the pressure parameters, thresholds, and other related information.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f44barpressolution_wtb_shconf4.png"
  width="40%"
  caption="Sensor details"
/>

- **Sensor data**: Data provided by the sensor.
- **FETCH DATA**: Update the latest sensor data.
- **Send uplink if value changes**: Send uplink data if the sensor data changes.
- **Sensor interval(s)**: The payload sending interval in seconds. It determines how often the sensor sends uplink data to the server, with a range interval from 60~86,400 seconds. Set this parameter when the Send periodic uplink is enabled.
- **Send periodic uplink**: Send uplink data periodically based on the sensor interval.
- **Lower threshold, hPa**: Specifies the minimum acceptable barometric pressure value.
- **Send uplink if below threshold**: Trigger the transmission of uplink data if the value falls below the lower threshold.
- **Upper threshold, hPa**: Maximum acceptable barometric presure value.
- **Send uplink if above threshold**: Send uplink data if the value exceeds the upper threshold.
- **Threshold, hPa**: Range of acceptable values.
- **Send uplink if between threshold**: Send uplink data if the value falls within the specified threshold range.

4. Click the downward arrow in the **Temperature** tab bar to set the periodic uplink sending, thresholds, and other information, in the same way you configured the pressure values in the previous step.

5. After completing the modifications, a message **Commands in queue** will appear at the bottom of the interface. Click **APPLY** to send the parameter update commands.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f45barpressolution_wtb_shconf5.png"
  width="40%"
  caption="Set the sensor parameters"
/>

5. When the message **All commands applied successfully**, appears on the interface, it indicates that the parameter update commands have been successfully sent.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/quickstart/f46barpressolution_wtb_shconf6.png"
  width="40%"
  caption="Apply commands"
/>

**Other Operations**

- **REMOVE SENSOR PROBE**: Detach the sensor.
- **RESTORE TO DEFAULT SETTINGS**: Reset the Sensor Probe to its default settings.
- **UPGRADE SENSOR PROBE**: Upgrade the firmware of the Sensor Probe.

<RkBottomNav/>