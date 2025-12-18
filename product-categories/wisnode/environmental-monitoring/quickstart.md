---
slug: /product-categories/wisnode/environmental-monitoring/quickstart/
title: Environmental Monitoring Solution Quick Start Guide
description: Provides comprehensive information on your Environmental Monitoring Solution to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
keywords:
- quickstart
- Sensor Hub
- Sensor Hub Solutions
- Environmental Monitoring
- WisNode
image: "https://images.docs.rakwireless.com/wisnode/environmental-monitoring/environmental-monitoring.png"
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# Environmental Monitoring Solution Quick Start Guide

## Prerequisites

Before proceeding with each step for using the Environmental Monitoring Solutions, ensure you have the necessary items.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/1-device-list.png"
  width="75%"
  caption="Solutions package inclusion"
/>

### Hardware

- <a href="https://store.rakwireless.com/products/environmental-monitoring?variant=42510931329222?utm_source=solarpower&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">Sensor Hub Environmental Monitoring Solution</a>
- <a href="https://store.rakwireless.com/products/rak-battery-lite-solar-power-solution-rak9154?utm_source=RAK9154SolarBattery&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">Solar Battery Lite for Sensor Hub</a> (optional)
- Additional accessories: Probe Cable, Probe Splitter, Power Supply, and others (numbers and variations depending on the use case)
- An Android or iOS mobile device with Bluetooth and NFC 


### Software

<a href="https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/wistoolbox-mobile/" target="_blank">WisToolBox</a>

## Solution Configuration

### Sensor Hub Setup

#### SIM Card Installation

If the selected solution utilizes the NB-IoT/LTE CAT-M wireless communication mode, follow these steps to insert a SIM card. If you opt for the LoRaWAN wireless communication mode, skip this section, as a SIM card is not required.

1. Remove the back cover by unscrewing the four screws with a cross screwdriver.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/2-remove-the-back-cover.png"
  width="30%"
  caption="Remove the back cover"
/>

2. Insert the SIM card into the groove, then gently push it into the card slot.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/3-put-the-sim-card.png"
  width="50%"
  caption="Insert the SIM card"
/>

#### Sensor Hub Mounting

##### Wall Mounting

1. Use a 5&nbsp;mm drill bit to drill holes in the wall, then insert the screw anchors into the holes.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/4-wall-mounting.png"
  width="75%"
  caption="Installation preparation"
/>

2. Secure the mounting bracket to the wall by using tapping screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/5-attach-the-mounting-bracket.png"
  width="40%"
  caption="Secure the mounting bracket"
/>

3. Align the device's hanging tab with the slots on the bracket, and then insert the tab into the slots. Pull the device downwards until it snaps into place.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/6-installation-of-equipment.png"
  width="50%"
  caption="Align the device with the hanging tabs"
/>

##### Pole Mounting

1. Secure the mounting bracket to the pole using a steel strap.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/7-fix-the-mounting-bracket.png"
  width="20%"
  caption="Fix the mounting bracket"
/>

:::tip NOTE
- Mount the bracket on a pole with a 50-80&nbsp;mm diameter. For larger poles, use a bigger steel strap.
- The standard kit does not include a larger steel strap. Purchase separately if needed.
:::

2. Align the hanging tab of the device with the slots on the bracket, then insert the tab into the slots. Gently pull the device downwards until it securely snaps in place.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/8-installation-of-equipment1.png"
  width="35%"
  caption="Device installation"
/>

3. Insert a security screw at the top to fasten the device and the bracket together.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/9-lock-the-device-and-the-bracket.png"
  width="30%"
  caption="Fasten the device and the bracket"
/>

## RAK2560 WisNode Sensor Hub + Temperature & Humidity Sensor Setup

### Sensor Hub + Temperature & Humidity Sensor Installation

The RAK1901 Temperature and Humidity sensor comes pre-assembled with Sensor Hub by default at the factory. No additional assembly is required; simply connect the Temperature & Humidity Sensor and Sensor Hub. 


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/12-installation-completed.png"
  width="50%"
  caption="Installation completed"
/>

## Power Supply Setup

The Sensor Hub Environmental Monitoring Solution supports a battery, solar panel, or 12&nbsp;V<sub>DC</sub> power supply.

### RAK9154 Solar Battery Installation

:::tip NOTE
- Mount the bracket on a pole with a 50-80&nbsp;mm diameter. For larger poles, use a bigger steel strap.
- The standard kit does not include a larger steel strap. Purchase separately if needed.
:::

1. Secure the mounting bracket on the pole with two steel straps.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/13-fix-the-mounting-bracket1.png"
  width="20%"
  caption="Secure the mounting bracket"
/>

2. Attach the mounting plate to the RAK9154 with two (2) M3 screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/14-secure-the-mounting-plate.png"
  width="35%"
  caption="Secure the mounting plate"
/>

3. Install the RAK9154 to the back of the solar panel with four (4) screws and nuts.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/15-attach-rak9154-to-solar-panel.png"
  width="40%"
  caption="Attach RAK9154 to solar panel"
/>

4. Connect the cable of the solar panel to the **PV input** connector of RAK9154. Install two (2) M6 screws to the mounting plate with a clearance of about 3&nbsp;mm.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/16-connector-the-rak9154.png"
  width="40%"
  caption="RAK9154 and Solar Panel Connection"
/>

5. Suspend the solar panel on the mounting bracket, adjust its angle and direction, and then tighten the two (2) M6 screws along with the remaining two screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/17-adjust-the-solar-panel.png"
  width="40%"
  caption="Install the solar panel combination"
/>

6. Connect Sensor Hub and RAK9154. Use a cable to link the remaining connection port of the Sensor Hub to the lithium battery Output 1 SP11 connection port of RAK9154.

:::tip NOTE
When connecting to RAK9154, ensure that the Sensor Hub is connected to the Output 1 connection port.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/18-connect-sensor-hub-and-rak9154-1.png"
  width="60%"
  caption="Connect Sensor Hub and RAK9154"
/>

7. Once the connection is complete, the Sensor Hub is ready to be powered up.

### 12&nbsp;V<sub>DC</sub> Power Supply Installation

1. Connect the power adapter to the external power cable of the Sensor Hub using a circular DC connector. 

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/20-connect-the-power-adapter.png"
  width="40%"
  caption="Power adapter connection"
/>

2. Connect the external power cable to the Sensor Hub using the SP11 connector.
3. Align the white dot symbol on the SP11 connector plug of the external power cable with the white dot symbol on the Sensor Hub SP11 connector socket and push the plug firmly into the socket.
4. After the plug and socket are connected, tighten the locking nut to secure the connection of the SP11 connector. The external power cable can connect to any Sensor Hub connection port.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/21-connect-the-external-power.png"
  width="35%"
  caption="Connect the external power cable"
/>

## Software Configuration Guide

### Sensor Hub Configuration

#### Power Up Sensor Hub

After installing all hardware components, connect the power supply. If the power supply consists of a solar panel and a battery, the device will power on automatically once all hardware has been installed.

:::warning
To prevent damage to the device, refrain from powering up the Sensor Hub before connecting it to the sensor. It is advisable to use the 12&nbsp;V<sub>DC</sub> adapter provided with the Sensor Hub for optimal performance.
:::

#### Connect Sensor Hub to WisToolBox

1. Download and install the WisToolBox app on your smart mobile device. The WisToolBox app is available for download from the Apple <a target="_blank" href="https://apps.apple.com/us/app/wistoolbox/id1575891664">App Store</a> and the Android <a target="_blank" href="https://play.google.com/store/apps/details?id=com.rak.wistoolbox&hl=en_US&gl=US">Google Play Store</a>.
2. Initiate the app and confirm that NFC and Bluetooth are enabled on your mobile device. Click on **START**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/22-select-device.png"
  width="35%"
  caption="Start the app"
/>

3. On the **Select connection mode** menu, choose **NFC Activation**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/23-select-sensor-hub.png"
  width="35%"
  caption="Select NFC Activation"
/>

4. Select the **Sensor HUB** option in the device selection interface to establish a connection.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/24-scan-device.png"
  width="35%"
  caption="Select Sensor Hub"
/>

5. Click the **CONNECT** button to initiate the scanning process for devices.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/25-synchronization-of-device-data.png"
  width="35%"
  caption="Click on the CONNECT button"
/>

6. Hold your mobile device close to the **N** symbol on the Sensor Hub device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/26-scanning-in-progess.png"
  width="35%"
  caption="Scanning in progress"
/>

:::tip NOTE
The detection of the Sensor Hub device indicates that the device has been successfully powered up.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/27-scan-successful.png"
  width="35%"
  caption="Scan Successful"
/>

7. After the connection is established, there will be a synchronization of device data. This process may take some time.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/28-sync-device.png"
  width="35%"
  caption="Sync Device"
/>

:::tip NOTE
- By default, if no connection is established within 30 seconds, the BLE broadcast of the Sensor Hub will automatically shut down. To establish a connection, connect the RAK device immediately after turning on the power or restart the power.
- Certain Android smartphones may necessitate enabling GPS to connect to BLE. Enabling GPS does not involve the use or sharing of sensitive information with the app.
:::

8. Upon completion of data synchronization, the app will automatically transition to the **SENSOR HUB INFO** page.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/29-sensor-hub-info-page.png"
  width="35%"
  caption="SENSOR HUB INFO page"
/>

9. While on the **SENSOR HUB INFO** page, configure the Uplink Settings according to the selected network.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/31-uplink-settings-option.png"
  width="35%"
  caption="Uplink Settings option"
/>

10. Once configured, click **SAVE SELECTION**, and then the **APPLY** button to implement the configuration options.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/32-apply-the-configuration-options.png"
  width="35%"
  caption="Apply the configuration options"
/>

After a few seconds, the synchronization progress will be completed, concluding this process.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/33-commands-applied-successfully.png"
  width="35%"
  caption="Commands applied successfully"
/>

#### Sensor Hub Network Configuration

##### LoRaWAN Configuration

This section focuses on configuring the LoRaWAN parameters and joining the network. Before proceeding with the following steps, ensure that the gateway and Sensor Hub are connected to the server.

Refer to the <a href="https://docs.rakwireless.com/product-categories/wisnode/environmental-monitoring/lorawan-network-server-guide#connect-gateway-to-ttn" target="_blank">Connect Gateway to TTN</a> and <a href="https://docs.rakwireless.com/product-categories/wisnode/environmental-monitoring/lorawan-network-server-guide#connect-sensor-hub-to-ttn" target="_blank">Connect Sensor Hub to TTN</a> sections for detailed instructions.

1. Click on the **LORA & LORAWAN PARAMETERS** tab. Configure the following parameters:

- **Global Settings**

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/34-global-settings.png"
  width="35%"
  caption="Global Settings"
/>

- **Join Mode**: Configure the Join mode based on the device's network access mode: **Over-The-Air Activation (OTAA)** or **Activation By Personalization (ABP)**. Make sure it matches the join mode registered on the network server.
- **Active Region**: Set the Active region to the device's frequency plan. Ensure that it is consistent with the gateway and device frequency plan registered on the network server.

Supported frequency bands include CN470, RU864, IN865, EU868, US915, AU915, KR920, AS923-1/2/3/4.

<b>LoRaWAN keys, ID, EUI</b>

- For the **OTAA join mode**, configure the following parameters: **Application EUI**, **Application key**, and **Device EUI**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/30-lorawan-keys-id-eui.png"
  width="35%"
  caption="OTAA Join Mode Configuration"
/>

  - **Application EUI**: Confirm that it matches the device's Application EUI as registered in the network server.
  - **Application key**: Verify its alignment with the device's Application key registered in the network server. Click **GENERATE KEY** to create a new key if needed.
  - **Device EUI**: Confirm that it matches the Device EUI registered in the network server.

- For the **ABP** join mode, configure the required parameters: **Application session key, Device address**, and **Network session key**. 

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/35-abp-join-mode.png"
  width="35%"
  caption="ABP Join Mode"
/>

- **Data on LoRa® network**

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/36-data-on-lora-network.png"
  width="35%"
  caption="Data on LoRa® network"
/>

- **Confirm mode**: Message confirmation mode.
- **Enable Auto Join**: Determine whether to activate automatic network access. When enabled, the device will join the network automatically upon powering up.
- **Network Status**: Indicates the status of the network connection. It will activate automatically once connected to the network.
- **ADR**: The Adaptive Data Rate optimizes the data rates in the network. Toggle the button to enable and disable it.
- **JOIN NETWORK**: After completing the network parameter configuration, click the JOIN NETWORK button to run the join network command.

2. After clicking **JOIN NETWORK**, a message **Message sent** will appear, indicating that the join network command has been sent.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/37-join-the-network.png"
  width="35%"
  caption="Join the network"
/>

##### NB-IoT/LTE CAT-M1 Configuration

This section primarily introduces the configuration of LTE-M network parameters. If you are using the NB-IoT/LTE CAT-M1 network, after connecting the device, select **LTE-M** in the **Uplink Settings** options on the **SENSOR HUB INFO** interface to display the **LTE-M PARAMETERS** configuration tab.

1. Click the **LTE-M PARAMETERS** tab and check the following parameters to ensure that the network is working properly.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/38-view-the-lte-m-parameters-tab.png"
  width="35%"
  caption="View the LTE-M Parameters tab"
/>

<b>LTE-M Network</b>

- **OPERATOR**: Shows the network operator. If the operator's name is displayed (for example, *T-Mobile*), it indicates that the device has recognized the SIM card.

<b>IP Network</b>

- **STATUS**: If the status is **Activated**, it signifies that the network of the SIM card is functioning normally.

2. Select the **Application** option to configure the cellular network parameters.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/39-configure-the-cellular-network-parameters.png"
  width="50%"
  caption="Configure the cellular network parameters"
/>

- **Service**: Choose a service, either AWS IoT Core or Generic MQTT. For this guide, use Generic MQTT as an example.
- **Server address**: Input the server address. Using the external MQTT broker as an example, enter `broker.hivemq.com`. Enter the address based on your specific use case.
- **Server Port**: Specify the server port according to your configuration.
- **Client ID**: Set the client ID for your device.
- **Enable user auth**: Decide whether to activate user authentication for your device.
- **Enable SSL**: Decide whether to activate SSL (Secure Sockets Layer) for secure communication.
- **Publish Topic**: Specify the topic for publishing messages.
- **Data Format**: Select **JSON** as the preferred format for data transmission.
- **Subscribe Topic**: Subscribe to the topic for receiving incoming messages, as illustrated in this example.

3. Following the configuration, click **APPLY** in the command list at the bottom of the interface to implement the changes. If the message **All commands applied successfully** appears, it indicates a successful configuration modification.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/40-apply-the-modified-configuration.png"
  width="50%"
  caption="Apply the modified configuration"
/>

4. When configured correctly and successfully connected to the server, the **Connection Status** will display as **connected**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/41-successfully-connected-to-the-server.png"
  width="50%"
  caption="Successfully connected to the server"
/>

#### Sensor Configuration

This section details the configuration process of the RAK1901 Temperature and Humidity Sensor. It shows how to access the monitoring data and device details of the sensor. Additionally, there’s an option to configure other information for each monitoring parameter, such as the uplink data sending period and threshold.

1. To start with, click the **SENSOR PROBE** tab to display the connected sensor on the interface. 

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/42-environment-sensor.png"
  width="35%"
  caption="Connected temperature and humidity sensor"
/>

2. Click the dropdown to expand the details of the environmental monitoring sensor.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/43-details-of-the-sensor.png"
  width="35%"
  caption="Sensor details"
/>

- **Temperature**
- **Humidity**
- **FETCH DATA**: Update the monitoring data from the sensor.
- **Device details**

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/44-device-details.png"
  width="35%"
  caption="Sensor details"
/>

3. Fetch the temperature data and configure the periodic uplink data sending, thresholds, and other relevant information for the sensor. 

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/45-set-the-sensor-parameters.png"
  width="35%"
  caption="Set the sensor parameters"
/>

- **Sensor data**: Data provided by the sensor.
- **FETCH DATA**: Update the latest sensor data.
- **Send uplink if value changes**: Send uplink data if the sensor data changes.
- **Sensor interval(s)**: The payload sending interval in seconds. It determines how often the sensor sends uplink data to the server, with a range interval from 60~86, 400&nbsp;seconds. Set this parameter when the Send periodic uplink is enabled.
- **Send periodic uplink**: Send uplink data periodically based on the sensor interval.
- **Lower threshold**: The minimum acceptable value.
- **Send uplink if below threshold**: Send uplink data if the value is below the lower threshold.
- **Upper threshold**: Maximum acceptable value.
- **Send uplink if above threshold**: Send uplink data if the value exceeds the upper threshold.
- **Threshold, m/s**: Range of acceptable values.
- **Send uplink if between threshold**: Send uplink data if the value falls within the threshold range.

4. After completing the modifications, a message **Commands in queue** will appear at the bottom of the interface. Click **APPLY** to send the parameter update commands.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/46-apply-commands.png"
  width="35%"
  caption="Apply commands"
/>

5. When the message **All commands applied successfully**, appears on the interface, it indicates that the parameter update commands have been successfully sent.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/environmental-monitoring/quickstart/47-applied-successfully.png"
  width="35%"
  caption="Commands applied successfully"
/>

<b>Other Operations</b>

- **REMOVE SENSOR PROBE**: Detach the sensor.
- **RESTORE TO DEFAULT SETTINGS**: Reset the Sensor Probe to its default settings.
- **UPGRADE SENSOR PROBE**: Upgrade the firmware of the Sensor Probe.

<RkBottomNav/>s