---
slug: /product-categories/wisnode/weather-station/quickstart/
title: Weather Station Monitoring Solution Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your Weather Station Solution. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device.
keywords:
  - Sensor Hub
  - Sensor Hub Solutions
  - quickstart
  - wisnode
  - Weather Station
image: https://images.docs.rakwireless.com/wisnode/environmental-monitoring/environmental-monitoring.png
sidebar_label: Quick Start Guide
---

# Weather Station Monitoring Solution Quick Start Guide

## Prerequisites

Before proceeding with each step for using the Weather Station Monitoring Solution, make sure to have all the necessary items listed below:

> **Image:** Weather Station Solution Package Inclusion

### Hardware Tools

- [Weather Station Monitoring Solution](https://store.rakwireless.com/products/weather-station-monitoring?variant=42505214427334?utm_source=W&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar Battery Lite for Sensor Hub](https://store.rakwireless.com/products/rak-battery-lite-solar-power-solution-rak9154?utm_source=RAK9154SolarBattery&utm_medium=Document&utm_campaign=BuyFromStore) (optional)
- Additional accessories: Probe Cable, Probe Splitter, power supply, and others (numbers and variations depending on the use case)
- An Android or iOS mobile device with Bluetooth and NFC 

### Software

[WisToolBox](https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/wistoolbox-mobile/)

## Solution Configuration

### Sensor Hub Setup

#### SIM Card Installation

If the selected solution utilizes the NB-IoT/LTE CAT-M wireless communication mode, follow these steps to insert a SIM card. If you opt for the LoRaWAN wireless communication mode, skip this section, as a SIM card is not required.

1. Remove the back cover by unscrewing the four screws with a cross screwdriver.

> **Image:** Remove the back cover

2. Insert the SIM card into the groove, then gently push it into the card slot.

> **Image:** Insert the SIM card

#### Sensor Hub Mounting

##### Wall Mounting

1. Use a 5 mm drill bit to drill holes in the wall, then insert the screw anchors into the holes.

> **Image:** Installation preparation

2. Secure the mounting bracket to the wall by using self-tapping screws.

> **Image:** Secure the mounting bracket

3. Align the device's hanging tab with the slots on the bracket, and then insert the tab into the slots. Pull the device downwards until it snaps into place.

> **Image:** Align the device with the hanging tabs

##### Pole Mounting

1. Secure the mounting bracket to the pole using a steel strap.

> **Image:** Fix the mounting bracket

:::tip NOTE
Mount the bracket on a pole with a 50-80 mm diameter. For larger poles, use a bigger steel strap. The standard kit does not include a larger steel strap. Purchase separately if needed.
:::

2. Align the hanging tab of the device with the slots on the bracket, then insert the tab into the slots. Gently pull the device downwards until it securely snaps in place.

> **Image:** Device installation

3. Insert a security screw at the top to fasten the device and the bracket together.

> **Image:** Fasten the device and the bracket

## RAK2560 WisNode Sensor Hub + Micro Weather Sensor Setup

### Sensor Probe IO + Micro Weather Sensor Installation

1. Pass the communication cable connector of the micro weather sensor through the circular hole in the provided mounting bracket.

2. Connect the micro weather sensor and the communication cable. Align the grooves of the connectors and insert the cable connector into the sensor connector.

> **Image:** Insert the Cable Connector into the Sensor Connector

3. After inserting, tighten the locking nut.

4. Fix the sensor to the mounting bracket using the provided wing screws. When installing the sensor, ensure that the indicator on the sensor corresponds to the geographical north.

> **Image:** Fix the Sensor to the Mounting Bracket

> **Image:** Indicator

5. Fix the mounting bracket to the pole.

:::tip NOTE
**Precautions during mounting:**
- Check regularly to ensure that the sensor is not disturbed by other running equipment that may not fully comply with the general standards, such as radio/radar transmitters, ship engines, and motors.
- Do not mount the sensor on the same plane as any radar scanning devices, and keep a distance of at least 2 meters between them.
- When mounting the sensor, keep it at a certain distance from the radio receiving antennas around.
- Avoid nearby structures, such as trees, utility poles, and tall buildings, which can generate an eddying flow that affects the accuracy of the ultrasonic sensor.
- When mounting the sensor on a building, the ideal mounting height should be 1.5 times the height of the building.
- When mounting the sensor on the boom of a mast, the boom needs to be on the prevailing wind side.
:::

#### Sensor Hub + Sensor Probe IO + Micro Weather Sensor Installation

The micro weather sensor comes pre-assembled with Sensor Probe IO by default at the factory. No additional assembly is required; simply connect Sensor Probe IO and Sensor Hub.

1. Connect Sensor Probe IO with Sensor Hub via the SP11 connector.
2. Align the white dot symbol on the Sensor Probe IO SP11 connector plug with the white dot symbol on the Sensor Hub SP11 connector socket and push the plug firmly into the socket.
3. Once connected, tighten the locking nut to secure the SPI connection. The Sensor Probe IO can connect to any Sensor Hub SP11 connector port. Refer to the actual use and connect to the appropriate port, as shown in **Figure 13**.

> **Image:** Connect the Sensor Probe IO

> **Image:** Installation completed

## Power Supply Setup

The Sensor Hub relies on the Sensor Probe IO for connectivity to the micro weather sensors. Consequently, it cannot be powered by batteries alone and requires a connection to either a solar panel or a 12 V<sub>DC</sub> power supply for operation.

### RAK9154 Solar Battery Installation

:::tip NOTE
Mount the bracket on a pole with a 50-80 mm diameter. For larger poles, use a bigger steel strap. The standard kit does not include a larger steel strap. Purchase separately if needed.
:::

1. Secure the mounting bracket on the pole with two steel straps.

> **Image:** Secure the mounting bracket

2. Attach the mounting plate to the RAK9154 with two (2) M3 screws.

> **Image:** Attach the mounting plate

3. Install the RAK9154 to the back of the solar panel with four (4) screws and nuts.

> **Image:** Attach RAK9154 to solar panel

4. Connect the cable of the solar panel to the **PV input** connector of RAK9154. Install two (2) M6 screws to the mounting plate with a clearance of about 3 mm.

> **Image:** Connector the RAK9154

5. Suspend the solar panel on the mounting bracket, adjust its angle and direction, and then tighten the two (2) M6 screws along with the remaining two screws.

> **Image:** Install the solar panel combination

6. Connect Sensor Hub and RAK9154. Use a cable to link the remaining connection port of the Sensor Hub to the lithium battery Output 1 SP11 connection port of RAK9154.

:::tip NOTE
When connecting to RAK9154, ensure that the Sensor Hub is connected to the Output 1 connection port.
:::

> **Image:** Connect the Sensor Hub and RAK9154

7. Once the connection is complete, the Sensor Hub is ready to be powered up.

### 12 V<sub>DC</sub> Power Supply Installation

1. Connect the power adapter to the external power cable of Sensor Hub using a circular DC connector.

> **Image:** Power Adapter Connection

2. Connect the external power cable to the Sensor Hub using the SP11 connector.
3. Align the white dot mark on the SP11 connector plug of the external power cable with the white dot mark on the Sensor Hub SP11 connector socket, and push the plug firmly into the socket.
4. After the plug and socket are connected, tighten the locking nut to secure the connection of the SP11 connector. The external power cable can connect to any Sensor Hub connection port.

> **Image:** Connect the external power cable

## Software Configuration Guide

### Sensor Hub Configuration

#### Power Up Sensor Hub

After installing all hardware components, connect the power supply. If the power supply consists of a solar panel and a battery, the device will power on automatically once all hardware has been installed.

:::warning
To prevent damage to the device, refrain from powering up the Sensor Hub before connecting it to the sensor. It is advisable to use the 12 V<sub>DC</sub> adapter provided with the Sensor Hub for optimal performance.
:::

#### Connect Sensor Hub to WisToolBox

1. Download and install the WisToolBox app on your smart mobile device. The WisToolBox app is available for download from the Apple App Store and the Android Google Play Store.

2. Initiate the app and confirm that NFC and Bluetooth are enabled on your mobile device. Click on **START**.

> **Image:** Start App

3. On the **Select connection mode** menu, choose **NFC Activation**.

> **Image:** Select NFC Activation

4. Select the **Sensor HUB** option in the device selection interface to establish a connection.

> **Image:** Select Sensor Hub

5. Click the **CONNECT** button to initiate the scanning process for devices.

> **Image:** Click on the CONNECT button

6. Hold your mobile device close to the **N** symbol on the Sensor Hub device.

> **Image:** Scanning in progress

:::tip NOTE
The detection of the Sensor Hub device indicates that the device has been successfully powered up.
:::

> **Image:** Scan Successful

7. After the connection is established, there will be a synchronization of device data. This process may take some time.

> **Image:** Sync Device

:::tip NOTE
- By default, if no connection is established within 30 seconds, the BLE broadcast of the Sensor Hub will automatically shut down. To establish a connection, connect the RAK device immediately after turning on the power or restart the power.
- Certain Android smartphones may necessitate enabling GPS to connect to BLE. Enabling GPS does not involve the use or sharing of sensitive information with the app.
:::

8. Upon completion of data synchronization, the app will automatically transition to the **SENSOR HUB INFO** page.

> **Image:** SENSOR HUB INFO page

9. While on the **SENSOR HUB INFO** page, configure the Uplink Settings according to the selected network.

> **Image:** Uplink Settings option

10. Once configured, click **SAVE SELECTION**, and then the **APPLY** button to implement the configuration options.

> **Image:** Apply the configuration options

After a few seconds, the synchronization progress will be completed, concluding this process.

> **Image:** Commands applied successfully

### Sensor Hub Network Configuration

#### LoRaWAN Configuration

This section focuses on configuring the LoRaWAN parameters and joining the network. Before proceeding with the following steps, ensure that the gateway and Sensor Hub are connected to the server.

Refer to the **Connect the Gateway to the Server** and **Connect Sensor Hub to the Server** sections for detailed instructions.

1. Click the **LORA & LORAWAN PARAMETERS** tab. Configure the following parameters:

- **Global settings**

> **Image:** Global Settings

- **Join mode**: Configure the Join mode based on the device's network access mode: **Over-The-Air Activation (OTAA)** or **Activation By Personalization (ABP)**. Make sure it matches the join mode registered on the network server.
- **Active region**: Set the Active region to the device's frequency plan. Ensure that it is consistent with the gateway and device frequency plan registered on the network server.

Supported frequency bands include CN470, RU864, IN865, EU868, US915, AU915, KR920, AS923-1/2/3/4.

**LoRaWAN keys, ID, EUI**

- For the **OTAA join mode**, configure the following parameters: **Application EUI**, **Application key**, and **Device EUI**.

  
> **Image:** OTAA join mode configuration

  - **Application EUI**: Confirm that it matches the device's Application EUI as registered in the network server.
  - **Application key**: Verify its alignment with the device's Application key registered in the network server. Click **GENERATE KEY** to create a new key if needed.
  - **Device EUI**: Confirm that it matches the Device EUI registered in the network server. 

- For the ABP join mode, configure the required parameters: **Application session key**, **Device address**, and **Network session key**. 

> **Image:** ABP join mode

- **Data on LoRa® network**

> **Image:** Data on LoRa® network

  * **Confirm mode**: Message confirmation mode.
  * **Enable auto join**: Determine whether to activate automatic network access. When enabled, the device will join the network automatically upon powering up.
  * **Network status**: Indicates the status of the network connection. It will be activated automatically once successfully connected to the network.
  * **ADR**: The Adaptive Data Rate optimizes data rates in the network. Toggle the button to enable or disable it.
  * **JOIN NETWORK**: After completing the network parameter, click the **JOIN NETWORK** button to run the join network command.

2. After clicking **JOIN NETWORK**, a **Message sent** message will appear, indicating that the join network command has been sent.

> **Image:** Join the Network

#### NB-IoT/LTE CAT-M1 Configuration

This section primarily introduces the configuration of LTE-M network parameters. If you are using the NB-IoT/LTE CAT-M1 network, after connecting the device, select **LTE-M** in the **Uplink Settings** options on the **SENSOR HUB INFO** interface to display the **LTE-M PARAMETERS** configuration tab.

1. Click the **LTE-M PARAMETERS** tab and check the following parameters to ensure that the network is working properly.

> **Image:** View the LTE-M Parameters tab

**LTE-M Network**

- **OPERATOR**: Shows the Network operator. If the operator's name is displayed, it indicates that the device has recognized the SIM card.
For example, *CHINAMOBILE*.

**IP Network**

- **STATUS**: If the status is **Activated**, it signifies that the network of the SIM card is functioning normally.

2. Select the **Application** option to configure the cellular network parameters.
 
 
> **Image:** Configure the cellular network parameters

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
 

> **Image:** Apply the modified configuration

4. When configured correctly and successfully connected to the server, the **Connection Status** will display as **connected**.

> **Image:** Successfully connected to the server

### Sensor Configuration

This section details the configuration process of the weather sensor. It shows how to access the monitoring data and device details of the weather station solution. Additionally, there’s an option to configure other information for each monitoring parameter, such as the uplink data sending period and threshold.

1. To start with, click the **SENSOR PROBE** tab to display the connected weather stations on the interface. 

> **Image:** Weather Station sensor

2. Click the dropdown arrow to expand the details of the weather station sensor.

> **Image:** Sensor details

- **Wind speed**
- **Wind direction**
- **Temperature**
- **Humidity**
- **Pressure**: The atmospheric pressure.
- **FETCH DATA**: Update the monitoring data from the sensor.
- **Device details**

> **Image:** Sensor details

For this example, fetch the data of the Wind speed and set the parameters by then choosing the Wind speed feature. 

3. Configure the periodic uplink data sending, thresholds, and other relevant information for the sensor.

> **Image:** Set the sensor parameters

- **Sensor data**: Data provided by the sensor.
- **FETCH DATA**: Update the latest sensor data.
- **Send uplink if value changes**: Send uplink data if the sensor data changes.
- **Sensor interval(s)**: The payload sending interval in seconds. It determines how often the sensor sends uplink data to the server, with a range interval from 60~86,400 seconds. Set this parameter when the **Send periodic uplink** is enabled.
- **Send periodic uplink**: Send uplink data periodically based on the sensor interval.
- **Lower threshold**: Specifies the minimum acceptable value.
- **Send uplink if below threshold**: Trigger the transmission of uplink data if the value falls below the lower threshold.
- **Upper threshold**: Maximum acceptable value.
- **Send uplink if above threshold**: Send uplink data if the value exceeds the upper threshold.
- **Threshold, m/s**: Range of acceptable values.
- **Send uplink if between thresholds**: Send uplink data if the value falls within the specified threshold range.

4. After completing the modifications, a message **Commands in queue** will appear at the bottom of the interface. Click **APPLY** to send the parameter update commands.

> **Image:** Apply commands

5. When the message **All commands applied successfully**, appears on the interface, it indicates that the parameter update commands have been successfully sent.

> **Image:** Commands applied successfully

**Other Operations**

- **REMOVE SENSOR PROBE**: Detach the sensor.
- **RESTORE TO DEFAULT SETTINGS**: Reset the Sensor Probe to its default settings.
- **UPGRADE SENSOR PROBE**: Upgrade the firmware of the Sensor Probe.

