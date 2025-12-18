---
slug: /product-categories/wisnode/water-ph-monitoring/quickstart/
title: Water pH Monitoring Sensor Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your Sensor Hub Water pH solution. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
keywords:
- quickstart
- wisnode
- Power Supply
- Installation
- Water pH
image: https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/waterphsolution.png
sidebar_label: Quick Start Guide
---

# Water pH Monitoring Sensor Quick Start Guide

## Prerequisites

Before proceeding with each step for using the Water pH Monitoring Solution, ensure that you have the necessary items listed below:

> **Image:** Solutions package inclusion

### Hardware Tools

- Sensor Hub Water pH Monitoring Solution
- [Solar Battery Lite for Sensor Hub](https://store.rakwireless.com/products/rak-battery-lite-solar-power-solution-rak9154?m=9&h=power-supplies-accessories) (Optional)
- Additional accessories: Probe Cable, Probe Splitter, power supply, and others (numbers and variations depending on the use case)
- An Android or iOS mobile device with Bluetooth and NFC

### Software

- [WisToolBox](https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/wistoolbox-mobile/)

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

> **Image:** Installation Preparation

2. Secure the mounting bracket to the wall by using self-tapping screws.

> **Image:** Secure the mounting bracket

3. Align the device's hanging tab with the slots on the bracket, and then insert the tab into the slots. Pull the device downwards until it snaps into place.

> **Image:** Align the device with the hanging tabs

##### Pole Mounting

1. Fix the mounting bracket to the pole using a steel strap.

> **Image:** Fix the Mounting Bracket

:::tip NOTE
Mount the bracket on a pole with a 50-80 mm diameter. For larger poles, use a bigger steel strap. The standard kit does not include a larger steel strap. Purchase separately if needed.
:::

2. Align the hanging tabs of the device with the slots on the bracket, then insert the tabs into the slots. Gently pull the device downwards until it securely snaps into place.

> **Image:** Device installation

3. Insert a security screw at the top to fasten the device and the bracket together.

> **Image:** Fasten the device and the bracket

### RAK2560 WisNode Sensor Hub + Water pH Sensor Setup

#### Sensor Probe IO + Water pH Sensor Installation

The Water pH Sensor comes pre-assembled with the Sensor Probe IO by default at the factory, so no additional assembly is required.

> **Image:** Water pH Sensor

#### Sensor Hub + Sensor Probe IO + Water pH Sensor Installation

1. Connect the Sensor Probe IO to the SensorHub using the SP11 connector. 
2. Align the white dot mark on the Sensor Probe IO SP11 connector plug with the white dot mark on the SensorHub SP11 connector socket, and push the plug firmly into the socket. 
3. Once connected, tighten the locking nut to secure the SP11 connector. The Sensor Probe IO can be linked to any Sensor Hub SP11 connector port. Refer to the actual use and connect to the appropriate port as illustrated in **Figure 11**.

> **Image:** Connect the Sensor Probe IO

> **Image:** Installation complete

#### Water pH Sensor Installation

The water pH sensor (JXBS-4001-PH) transmitter instrument panel is designed for wall mounting. Mount it at a 90-degree angle, perpendicular to the ground. 
The mounting holes are located in the center on both sides of the device, with a diameter of less than 4mm and a spacing of 105 mm. Use 3 mm self-tapping screws for installation. Additionally, mount the device in a location that is sheltered from wind, rain, and direct sunlight.

Ensure the area is well-ventilated to prevent the internal temperature from rising. Do not tilt the instrument to the left or right during installation; aim to keep it as horizontal as possible.

> **Image:** Water pH sensor Mounting Holes

The water pH sensor (JXBS-4001-PH) probe is a highly precise component and must be installed correctly to avoid damage to the electrode or irreversible harm. The electrode can be installed using one of the following methods: pipeline installation, submersible installation, or flange installation.

> **Image:** Probe installation diagram

:::tip NOTE
- Do not immerse the probe directly into the water; use a mounting bracket or a flow cup to secure it. Before installation, apply thread seal tape (at the 3/4 thread) to ensure a waterproof seal, preventing water from entering the electrode and causing a short circuit in the electrode cable.

- During a water outage, ensure the probe remains immersed in the measured liquid or is covered with a protective cap filled with protective liquid. In winter, when the water temperature is low or if the water is out for an extended period, add an antifreeze device or bring the probe indoors and store it in water. Failure to do so may shorten the probe's service life.
:::

### Power Supply Setup

The Sensor Hub relies on the Sensor Probe IO for connectivity to the Water pH combo sensors. Consequently, it cannot be powered by batteries alone and requires a connection to either a solar panel or a 12 V<sub>DC</sub> power supply for operation.

#### RAK9154 Solar Battery Installation

:::tip NOTE
Mount the bracket on a pole with a 50-80 mm diameter. For larger poles, use a bigger steel strap. The standard kit does not include a larger steel strap. Purchase separately if needed.
:::

1. Secure the mounting bracket to the pole using two steel straps.

> **Image:** Secure the mounting bracket

2. Attach the mounting plate to RAK9154 using two (2) M3 screws.

> **Image:** Secure the mounting plate

3. Install the RAK9154 to the back of the solar panel using four (4) screws and nuts.

> **Image:** Attach the RAK9154 to solar panel

4. Connect the cable from the solar panel to the PV Input connector of RAK9154. Install two M6 screws on the mounting plate with a clearance of about 3 mm.

> **Image:** RAK9154 and Solar Panel Connection

5. Suspend the solar panel on the mounting bracket, adjust its angle and direction, and then secure it by tightening the two (2) M6 screws along with the remaining two screws.

> **Image:** Install the solar panel combination

6. Connect the Sensor Hub to the RAK9154. Use a cable to link the remaining connection ports of the Sensor Hub to the Output 1 SP11 connection port of the RAK9154.

:::tip NOTE
When connecting to RAK9154, ensure that the Sensor Hub is connected to the Output 1 connection port.
:::

> **Image:** Connect Sensor Hub and RAK9154

7. Once the connection is complete, the Sensor Hub is ready to be powered up.

#### 12 V<sub>DC</sub> Power Supply Installation

1. Connect the power adapter and the external power cable of the Sensor Hub through the circular DC interface.

> **Image:** Power adapter connection

2. Connect the external power cable to the Sensor Hub through the SP11 connector.  
3. Align the white dot mark on the SP11 connector plug of the external power cable with the white dot mark on the Sensor Hub SP11 connector socket, and push the plug in firmly into the socket. 
4. After the plug and socket are connected, tighten the locking nut to secure the SP11 connector. The external power cable can connect to any Sensor Hub connection port.

> **Image:** Connect external power supply

> **Image:** Connection complete

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

> **Image:** Start the App

3. On the **Select connection mode** menu, choose **NFC Activation**.

> **Image:** Select NFC Activation

4. Select the **Sensor HUB** option in the device selection interface to establish a connection.

> **Image:** Select Sensor Hub

5. Click the **CONNECT** button to initiate the scanning process for devices.

> **Image:** Click on the CONNECT button

6. Hold your mobile device close to the **N** symbol on the SensorHub device.

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

10. Once configured, click **SAVE SELECTION** and then the **APPLY** button to implement the configuration options.

> **Image:** Apply the configuration options

After a few seconds, the synchronization progress will be completed, concluding this process.

> **Image:** Commands applied successfully

#### Sensor Hub Network Configuration

##### LoRaWAN Configuration

This section focuses on configuring LoRaWAN parameters and joining the network. Before proceeding with the following steps, ensure that both the gateway and Sensor Hub are successfully connected to the server.

Refer to the **Connect the Gateway to the Server** and **Connect Sensor Hub to the Server** sections for detailed instructions.

1. Click on the **LORA & LORAWAN PARAMETERS** tab. Configure the following parameters:

**Global Settings**

> **Image:** Global Settings

- **Join Mode:** Configure the Join mode based on the device's network access mode: **Over-The-Air Activation (OTAA)** or **Activation By Personalization (ABP)**. Make sure it matches the join mode registered on the network server.
- **Active Region:** Set the Active region to the device's frequency plan. Ensure that it is consistent with the gateway and device frequency plan registered on the network server.

Supported frequency bands include CN470, RU864, IN865, EU868, US915, AU915, KR920, AS923-1/2/3/4.

**LoRaWAN keys, ID, EUI**

* For the **OTAA join mode**, configure the following parameters: **Application EUI**, **Application key**, and **Device EUI**.

> **Image:** LoRaWAN parameters
  
  * **Application EUI**: Confirm that it matches the device's Application EUI as registered in the network server.
  * **Application key**: Verify its alignment with the device's Application key registered in the network server. Click **GENERATE KEY** to create a new key if needed.
  * **Device EUI**: Confirm that it matches the device's EUI as registered in the network server.

* For the **ABP join mode**, configure the following parameters: **Application session key**, **Device address**, **Network session key**.

**Data on LoRa® Network**

> **Image:** Data on LoRa® Network

* **Confirm mode**: Message confirmation mode.
* **Enable auto join**: Determine whether to activate automatic network access. When enabled, the device will join the network automatically upon powering up.
* **Network status**: Indicates the status of the network connection. It will be activated automatically once successfully connected to the network.
* **ADR**: The Adaptive Data Rate optimizes data rates in the network. Toggle the button to enable or disable it.
* **JOIN NETWORK**: After completing the network parameter, click the **JOIN NETWORK** button to run the join network command.

2. After clicking **JOIN NETWORK**, a message **Message sent** will appear, indicating that the join network command has been sent.

> **Image:** Join the network

##### NB-IoT/LTE CAT-M1 Configuration

This section primarily introduces the configuration of LTE-M network parameters. If you are using the NB-IoT/LTE CAT-M1 network, after connecting the device, select **LTE-M** in the **Uplink Settings** options on the **SENSOR HUB INFO** interface to display the **LTE-M PARAMETERS** configuration tab.

1. Click the **LTE-M PARAMETERS** tab. Check the following parameters to ensure the normal use of the network.

> **Image:** View the NB-IOT PARAMETERS tab parameters

**NB-IoT Network**

- **OPERATOR**: shows the Network operator. If the operator's name is displayed, it indicates that the device has recognized the SIM card. 
For example, *T-Mobile*.

**IP Network**

- **STATUS**: If the status is **Activated**, it signifies that the network of the SIM card is functioning normally.

2. Select the **Application** option to set up the cellular network parameters.

> **Image:** Configure the cellular network parameters

- **Service**: choose a service, either AWS IoT Core or Generic MQTT. Let's take Generic MQTT as an example.
- **Server address**: input the server address. Using the external MQTT broker as an example, enter `broker.hivemq.com`. Enter the address based on your specific use case.
- **Server Port**: specify the server port according to your configuration.
- **Client ID**: set the client ID for your device.
- **Enable user auth**: decide whether to activate user authentication for your device.
- **Enable SSL**: decide whether to activate SSL (Secure Sockets Layer) for secure communication.

> **Image:** Configure the Subscription Topics

- **Publish Topic**: specify the topic for publishing messages.
- **Data Format**: select **JSON** as the preferred format for data transmission.
- **Subscribe Topic**: subscribe to the topic for receiving incoming messages, as illustrated in this example.

3. Following the configuration, click **APPLY** in the command list at the bottom of the interface to implement the changes. If the message **All commands applied successfully** appears, it indicates a successful configuration modification.

> **Image:** Apply the modified configuration

4. When the configuration is accurate and the connection to the server is successful, the **Connection Status** will display as **connected**.

> **Image:** Successfully connected to the server

#### Sensor Configuration

This section details the configuration process of the Water pH sensor. It shows how to access the monitoring data and device details of the Water pH sensor. Additionally, there’s an option to configure other information for each monitoring parameter, such as the uplink data sending period and threshold.

1. To start with, click the **SENSOR PROBE** tab to display the connected Water pH sensor. 

> **Image:** Water pH Sensor

2. Click the dropdown arrow to expand the details of the Water pH sensor.

> **Image:** Sensor Information

- **pH**: Water pH value.
- **FETCH DATA**: Update the monitoring data from the sensor.
- **Device details**: Information of the Water pH sensor.

> **Image:** Sensor Details

3. Set the payload transmission interval for the water pH sensor.

> **Image:** Set the sensor parameters

- **Sensor interval(s):** The payload sending interval in seconds. It determines how often the sensor sends uplink data to the server, with a range interval from 60~86,400 seconds. Set this parameter when the Send periodic uplink is enabled.

4. After completing the modifications, a message **Commands in queue** will appear at the bottom of the interface. Click **APPLY** to send the parameter update commands.

5. When the message **All commands applied successfully**, appears on the interface, it indicates that the parameter update commands have been successfully sent.

> **Image:** Apply commands

**Other Operations**

- **IMPORT SETTINGS:** Import settings of previous configurations
- **REMOVE SENSOR PROBE:** Detach the sensor.
- **RESTORE TO DEFAULT SETTINGS:** Reset the Sensor Probe to its default settings.
- **UPGRADE SENSOR PROBE:** Update the firmware of the Sensor Probe.

