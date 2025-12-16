---
slug: /product-categories/wisnode/water-conductivity-monitoring/quickstart/
title: Water Conductivity Monitoring Solution Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your Water Conductivity Solution. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device.
keywords:
  - Sensor Hub
  - Sensor Hub Solutions
  - quickstart
  - wisnode
  - Water Conductivity
image: https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/water-conductivity-monitoring.png
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# Water Conductivity Monitoring Solution Quick Start Guide

## Prerequisites

Before proceeding with each step for using the Water Conductivity Solution, ensure that you have the necessary items.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/water-conductivity-package-inclusion.png"
  width="80%"
  caption="Water Conductivity Solution Package Inclusion"
/>

### Hardware Tools

- Sensor Hub Water Conductivity Monitoring Solution
- <a href="https://store.rakwireless.com/products/rak-battery-lite-solar-power-solution-rak9154?utm_source=RAK9154SolarBattery&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">Solar Battery Lite for Sensor Hub</a> (optional)
- Additional accessories: Probe Cable, Probe Splitter, Power Supply, and others (numbers and variations depending on the use case)
- An Android or iOS mobile device with Bluetooth and NFC


### Software

<a href="https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/wistoolbox-mobile/" target="_blank">WisToolBox</a>

## Solution Configuration

### Sensor Hub Setup

#### SIM Card Installation

If the selected solution uses the NB-IoT/LTE CAT-M wireless communication, follow these steps to insert a SIM card. If you choose the LoRaWAN wireless communication mode, skip this section, as a SIM card is not required.

1. Remove the back cover by unscrewing the four screws with a cross screwdriver.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/1.sim-card-insertion.png"
  width="20%"
  caption="Remove the back cover"
/>

2. Insert the SIM card in the groove, then gently push it into the card slot.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/2.sim-card-insertion.png"
  width="35%"
  caption="Insert the SIM card"
/>

#### Sensor Hub Mounting

##### Wall Mounting

1. Use a 5&nbsp;mm drill bit to drill holes in the wall, then insert the screw anchors into the holes.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/3.sensor-hub-installation.png"
  width="80%"
  caption="Installation preparation"
/>

2. Secure the mounting bracket to the wall by using self-tapping screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/4.sensor-hub-installation.png"
  width="30%"
  caption="Secure the mounting bracket"
/>

3. Align the device's hanging tab with the slots on the bracket, then insert the tab into the slots. Pull the device downwards until it snaps into place.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/5.sensor-hub-installation.png"
  width="35%"
  caption="Align the device with the hanging tabs"
/>

##### Pole Mounting

1. Fix the mounting bracket to the pole using a steel strip.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/6.pole-mounting.png"
  width="20%"
  caption="Fix the mounting bracket"
/>

:::tip NOTE
Mount the bracket on a pole with a 50-80&nbsp;mm diameter. For larger poles, use a bigger steel strap. The standard kit does not include a larger steel strap. Purchase separately if needed.
:::

2. Align the hanging tab of the device with the slots on the bracket, then insert the tab into the slots. Gently pull the device downwards until it securely snaps in place.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/7.pole-mounting.png"
  width="35%"
  caption="Device installation"
/>

3. Insert a security screw at the top to fasten the device and the bracket together.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/8.pole-mounting.png"
  width="20%"
  caption="Fasten the device and the bracket"
/>

## RAK2560 WisNode Sensor Hub + Water Conductivity Sensor Setup

### Sensor Probe IO + Water Conductivity Sensor Installation

The Water Conductivity Sensor comes pre-assembled with the Sensor Probe IO by default at the factory. Therefore, no additional assembly is necessary.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/9.installation-of-water-conductivity sensor.png"
  width="35%"
  caption="Insert the Cable Connector into the Sensor Connector"
/>

#### Sensor Hub + Sensor Probe IO + Water Conductivity Sensor Installation.

1. Connect the Sensor Probe IO to the SensorHub using the SP11 connector.

2. Align the white dot mark on the Sensor Probe IO SP11 connector plug with the white dot mark on the Sensor Hub SP11 connector socket and push the plug firmly into the socket.

3. Once connected, tighten the locking nut to secure the SP11 connector. The Sensor Probe IO can be linked to any Sensor Hub SP11 connector port. Refer to the actual use and connect to the appropriate port as illustrated in
 **Figure 11**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/10.connect-sensor-probe-IO-and-sensor-hub.png"
  width="45%"
  caption="Connect the Sensor Probe IO"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/11.connect-sensor-probe-IO-and-sensor-hub.png"
  width="35%"
  caption="Installation completed"
/>

## Power Supply Setup

The Sensor Hub relies on the Sensor Probe IO for connectivity to the water conductivity monitoring sensors. Consequently, it cannot be powered by batteries alone and requires a connection to either a solar panel or a 12&nbsp;V<sub>DC</sub> power supply for operation.

### RAK9154 Solar Battery Installation

:::tip NOTE
Mount the bracket on a pole with a 50-80&nbsp;mm diameter. For larger poles, use a bigger steel strap. The standard kit does not include a larger steel strap. Purchase separately if needed.
:::

1. Secure the mounting bracket to the pole using two steel straps.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/12.connect-solar-panel-system.png"
  width="20%"
  caption="Secure the mounting bracket"
/>

2. Attach the mounting plate to RAK9154 using two (2) M3 screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/13.connect-solar-panel-system.png"
  width="35%"
  caption="Attach the mounting plate"
/>

3. Secure RAK9154 onto the back of the solar panel using four (4) screws and nuts..

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/14.connect-solar-panel-system.png"
  width="35%"
  caption="Attach RAK9154 to solar panel"
/>

4. Connect the cable of the solar panel to the **PV Input** connector of RAK9154. Install two (2) M6 screws to the mounting plate and leave a gap of about 3&nbsp;mm.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/15.connect-solar-panel-system.png"
  width="35%"
  caption="Connector the RAK9154"
/>

5. Suspend the solar panel on the mounting bracket, adjust its angle and direction, and then tighten the two (2) M6 screws along with the remaining two screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/16.connect-solar-panel-system.png"
  width="35%"
  caption="Install the solar panel combination"
/>

6. Connect the Sensor Hub to the RAK9154. Use a cable to link the remaining connection ports of the Sensor Hub to the lithium battery Output 1 SP11 connection port of the RAK9154.

:::tip NOTE
When connecting to RAK9154, ensure that the Sensor Hub is connected to the Output 1 connection port.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/17.connect-solar-panel-system.png"
  width="60%"
  caption="Connect the Sensor Hub and RAK9154"
/>

7. Once the connection is complete, Sensor Hub is ready to be powered up.

### 12&nbsp;V<sub>DC</sub> Power Supply Installation

1. Connect the power adapter and the external power cable of the Sensor Hub through the circular DC interface.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/18.connect-the-12-vdc-power-supply.png"
  width="35%"
  caption="Power Adapter Connection"
/>

2. Connect the external power cable to the Sensor Hub through the SP11 connector.

3. Align the white dot symbol on the SP11 connector plug of the external power cable with the white dot mark on the Sensor Hub SP11 connector socket and push the plug firmly into the socket.

4. After the plug and socket are connected, tighten the locking nut to secure the SP11 connector. The external power cable can connect to any Sensor Hub connection port.


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/19.connect-the-12-vdc-power-supply.png"
  width="35%"
  caption="Connect the external power cable"
/>

## Software Configuration Guide

### Sensor Hub Configuration

#### Power Up Sensor Hub

After installing all hardware, connect the power supply. If the power supply consists of a solar panel and a battery, the device will power on automatically once all hardware has been installed.

:::warning
To prevent damage to the device, avoid powering up the Sensor Hub before connecting it to the sensor. For optimal performance, use the 12&nbsp;V<sub>DC</sub> adapter provided with the Sensor Hub.
:::

#### Connect Sensor Hub to WisToolBox

1. Download and install the WisToolBox app on your smart mobile device. The WisToolBox app is available for download from the Apple App Store and the Android Google Play Store.

2. Initiate the app and confirm that NFC and Bluetooth are enabled on your mobile device. Click on **START**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/1.start-app.png"
  width="35%"
  caption="Start App"
/>

3. On the **Select connection mode** menu, choose **NFC Activation**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/2.select-nfc-activation.png"
  width="35%"
  caption="Select NFC Activation"
/>

4. Select the **Sensor HUB** option in the device selection interface to establish a connection.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/3.select-sensor-hub.png"
  width="35%"
  caption="Select Sensor Hub"
/>

5. Click the **CONNECT** button to initiate the scanning process for devices.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/4.click-on-the-connect-button.png"
  width="35%"
  caption="Click on the CONNECT button"
/>

6. Hold your mobile device close to the **N** symbol on the Sensor Hub device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/5.scanning-in-progress.png"
  width="35%"
  caption="Scanning in progress"
/>

:::tip NOTE
The detection of the Sensor Hub device indicates that the device has been successfully powered up.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/6.scan-successful.png"
  width="35%"
  caption="Scan Successful"
/>

7. After the connection is established, there will be a synchronization of device data. This process may take some time.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/7.sync-device.png"
  width="35%"
  caption="Sync Device"
/>

:::tip NOTE
- By default, if no connection is established within 30 seconds, the BLE broadcast of the Sensor Hub will automatically shut down. To establish a connection, connect the RAK device immediately after turning on the power or restart the power.

- Certain Android smartphones may necessitate enabling GPS to connect to BLE. Enabling GPS does not involve the use or sharing of sensitive information with the app.
:::

8. Upon completion of data synchronization, the app will automatically transition to the **SENSOR HUB INFO** page.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/8.sensor-hub-info-page.png"
  width="35%"
  caption="SENSOR HUB INFO page"
/>

9. While on the **SENSOR HUB INFO** page, configure the Uplink Settings according to the selected network.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/9.uplink-settings-option.png"
  width="35%"
  caption="Uplink Settings option"
/>

10. Once configured, click **SAVE SELECTION**, and then the **APPLY** to implement the configuration options.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/10.apply-the-configuration-options.png"
  width="35%"
  caption="Apply the configuration options"
/>

After a few seconds, the synchronization progress will be completed, concluding this process.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/11.commands-applied-successfully.png"
  width="35%"
  caption="Commands applied successfully"
/>

### Sensor Hub Network Configuration

#### LoRaWAN Configuration

This section focuses on configuring the LoRaWAN parameters and joining the network. Before proceeding with the following steps, ensure that the gateway and Sensor Hub are connected to the server.

Refer to the <a target="_blank" href="https://docs.rakwireless.com/product-categories/wisnode/water-conductivity-monitoring/lorawan-network-server-guide#connect-gateway-to-ttn">Connect Gateway to TTN</a> and <a target="_blank" href="https://docs.rakwireless.com/product-categories/wisnode/water-conductivity-monitoring/lorawan-network-server-guide#connect-sensor-hub-to-ttn">Connect Sensor Hub to TTN</a> sections for detailed instructions.

1. Click the **LORA & LORAWAN PARAMETERS** tab. Configure the following parameters:

- <b>Global settings</b>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/12.global-settings.png"
  width="35%"
  caption="Global Settings"
/>

- **Join mode**: Configure the Join mode based on the device's network access mode: **Over-The-Air Activation (OTAA)** or **Activation By Personalization (ABP)**. Make sure it matches the join mode registered on the network server.

- **Active region**: Set the Active region to the device's frequency plan. Ensure that it is consistent with the gateway and device frequency plan registered on the network server. <br/>Supported frequency bands:  CN470, RU864, IN865, EU868, US915, AU915, KR920, AS923-1/2/3/4.

<b>LoRaWAN keys, ID, EUI</b>

- For the **OTAA join mode**, configure the following parameters: **Application EUI**, **Application key**, and **Device EUI**.

  <RkImage
    src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/13.otaa-join-mode-configuration.png"
    width="35%"
    caption="OTAA join mode configuration"
  />

  - **Application EUI**: Confirm that it matches the device's Application EUI as registered in the network server.
  - **Application key**: Verify its alignment with the device's Application key registered in the network server. Click **GENERATE KEY** to create a new key if needed.
  - **Device EUI**: Confirm that it matches the Device EUI registered in the network server.

- For the **ABP** join mode, configure the required parameters: **Application session key**, **Device address**, and **Network session key**. 

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/14.abp-join-mode.jpg"
  width="35%"
  caption="ABP join mode"
/>

- <b>Data on LoRa® network</b>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/15.data-on-lora-network.png"
  width="35%"
  caption="Data on LoRa® network"
/>

  * **Confirm mode**: Message confirmation mode.
  * **Enable auto join**: Determine whether to activate automatic network access. When enabled, the device will join the network automatically upon powering up.
  * **Network status**: Indicates the status of the network connection. It will activate automatically once connected to the network.
  * **ADR**: The Adaptive Data Rate optimizes the data rates in the network. Toggle the button to enable and disable it.
  * **JOIN NETWORK**: After completing the network parameter configuration, click the **JOIN NETWORK** button to run the join network command.

2. After clicking **JOIN NETWORK**, a **Message sent** message will appear, indicating that the join network command has been sent.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/16.join-the-network.png"
  width="35%"
  caption="Join the Network"
/>

#### NB-IoT/LTE CAT-M1 Configuration

This section primarily introduces the configuration of LTE-M network parameters. If you are using the NB-IoT/LTE CAT-M1 network, after connecting the device, select **LTE-M** in the **Uplink Settings** options on the **SENSOR HUB INFO** interface to display the **LTE-M PARAMETERS** configuration tab.

1. Click the **LTE-M PARAMETERS** tab and check the following parameters to ensure that the network is working properly.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/17.view-the-lte-m-parameters-tab.png"
  width="35%"
  caption="View the LTE-M Parameters tab"
/>

<b>LTE-M Network</b>

- **OPERATOR**: shows the Network operator. If the operator's name is displayed (for example, *CHINAMOBILE*), it indicates that the device has recognized the SIM card.

<b>IP Network</b>

- **STATUS**: if the status is **Activated**, it signifies that the network of the SIM card is functioning normally.

2. Select the **Application** option to configure the cellular network parameters.
 
<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/18.configure-the-cellular-network-parameters.png"
  width="60%"
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
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/19.apply-the-modified-configuration.png"
  width="70%"
  caption="Apply the modified configuration"
/>

4. When configured correctly and successfully connected to the server, the **Connection Status** will display as **connected**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/20. successfully-connected-to-the-server.png"
  width="35%"
  caption="Successfully connected to the server"
/>

### Sensor Configuration

This section details the configuration process of the water conductivity sensor. It shows how to access the monitoring data and device details of the water conductivity sensor. Additionally, there’s an option to configure other information for each monitoring parameter, such as the uplink data sending period and threshold.

1. To start with, click the **SENSOR PROBE** tab to display the connected water conductivity sensor.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/21.water-conductivity-sensor.png"
  width="35%"
  caption="Water Conductivity sensor"
/>

2. Click the dropdown to expand the details of the water conductivity sensor.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/22.sensor-details.png"
  width="35%"
  caption="Sensor details"
/>

- **Temperature**
- **Electrical Conductivity**
- **FETCH DATA**: Update the monitoring data from the sensor.
- **Device details**


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/23.sensor-details.png"
  width="35%"
  caption="Sensor details"
/>

3. Set the payload sensing interval of the water conductivity sensor.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/24.set-the-payload-sensing-interval.png"
  width="35%"
  caption="Set the payload sensing interval"
/>

- **Sensor interval(s)**: The payload sending interval in seconds. It determines how often the sensor sends uplink data to the server, with a range interval from 60 ~ 86,400 seconds.

4. After completing the modifications, a message **Commands in queue** will appear at the bottom of the interface. Click **APPLY** to send the parameter update commands.

5. When the message **All commands applied successfully** appears on the interface, it indicates that the parameter update commands have been successfully sent.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-conductivity-monitoring/quickstart/25.commands-applied-successfully.png"
  width="35%"
  caption="Commands applied successfully"
/>

<b>Other Operations</b>

- **IMPORT SETTINGS**
- **REMOVE SENSOR PROBE**: Detach the sensor.
- **RESTORE TO DEFAULT SETTINGS**: Reset the Sensor Probe to its default settings.
- **UPGRADE SENSOR PROBE**: Update the firmware of the Sensor Probe.

<RkBottomNav/>