---
slug: /product-categories/wisgate/rak10701-plus/network-setup/
title: RAK10701-Plus Field Tester for LoRaWAN Network Setup
description: Learn how to conduct field tests with RAK10701-Plus Field Tester for LoRaWAN. Setup and perform field test, analyze real-time metrics, and export structured reports!
image: https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/physical-interface.png
keywords:
    - lorawan
    - field tester plus
    - rak10701-plus
    - field tester plus network setup
sidebar_label: Pre-Test Network Setup
tags:
  - rak10701-plus
  - field tester plus
  - network coverage solution
  - network setup
date: 2025-05-23
---

import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkImage from '@site/src/components/Image'

# RAK10701-Plus Field Tester for LoRaWAN Network Setup

Before conducting any field tests, it’s essential to set up the Field Tester Plus, configure your LoRaWAN gateway, and ensure all system components are properly connected.

## Prerequisites

Ensure that the following hardware and software components are ready:

### Hardware Requirements

- **RAK10701-Plus Field Tester** (LoRaWAN end device)
- **LoRa Sub-GHz Antenna** (RP-SMA connector)
- **USB Type-C** Cable (for charging and optional advanced configuration)
- **RAK Gateway running WisGateOS 2 with Field Test Data Processor Extension installed**

:::tip NOTE
If you purchased the Field Tester Plus Bundle, the included gateway comes pre-installed with the required Field Test Data Processor Extension.
:::

### Software Requirements

- **Field Test Data Processor Extension for WisGateOS 2**: To install the extension, see the guide:
  - <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later#field-test-data-processor" target="_blank">How to Add an Extension</a>
- **WisToolBox**: Used for configuring OTAA parameters (DevEUI, AppEUI, and AppKey) and supporting firmware updates.
  - [Download and installation guide](https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/overview)

## Field Tester Plus Configuration

Before configuring the Field Tester Plus, it’s important to understand the physical interfaces, display layout, and basic operations of the device. For detailed specifications, refer to the <a href="https://docs.rakwireless.com/product-categories/wisgate/rak10701-plus/datasheet/" target="_blank">Field Tester Plus Datasheet</a>.

### Device Configuration

This section describes the basic parameter settings that can be configured directly on the device via the touchscreen.

1. Connect the **LoRa Sub-GHz antenna** (RP-SMA connector) to the device.
2. Press and hold the **side button for 5 seconds** to turn on the Field Tester Plus.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/power-on-screen.png"
  width="50%"
  caption="Power On Screen"
/>

3. Once powered on, the main screen will appear.

:::tip NOTE
No data will be shown on first boot until a valid uplink occurs.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/field-tester-main-screen.png"
  width="50%"
  caption="Field Tester Main Screen"
/>

4. Tap the gear icon on the screen to open the **SETTINGS** menu.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/field-tester-settings.png"
  width="50%"
  caption="Field Tester Settings"
/>

5. Use the touch controls to adjust LoRa parameters (e.g., Band, DR, TX Power).

- Tap the ![right arrow icon](https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/right-arrow.png) **icon** to **cycle through available parameters** (e.g., Band, DR, TX Power). The selected parameter will blink, indicating it is active.

- Tap the ![up arrow icon](https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/up-arrow.png) **icon** or ![down arrow icon](https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/down-arrow.png) **icon** to **adjust and confirm** the parameter’s value.

  **Editable Parameters:**

  <table>
    <thead>
      <tr>
        <th>Setting</th>
        <th>Description</th>
        <th>Values / Notes</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><h3>Location Labeling</h3></td>
        <td>Set a test point label (important for CSV export)</td>
        <td><b>Default</b>: NULL<br/><b>Max Length</b>: 6 characters</td>
      </tr>
      <tr>
        <td><h3>Band</h3></td>
        <td>LoRaWAN regional frequency band</td>
        <td>RU864, IN865, EU868, US915, AU915, KR920, AS923-1/2/3/4</td>
      </tr>
      <tr>
        <td><h3>DR (Data Rate)</h3></td>
        <td>Affects signal range (lower DR = longer range)</td>
        <td>The available DR options vary by LoRaWAN regional frequency band.</td>
      </tr>
      <tr>
        <td><h3>TX Power</h3></td>
        <td>Transmission power level</td>
        <td>The available TX Power options vary by LoRaWAN regional frequency band.</td>
      </tr>
      <tr>
        <td><h3>TX Interval</h3></td>
        <td>Time between uplinks</td>
        <td>6-3600&nbsp;s</td>
      </tr>
      <tr>
        <td><h3>Backlight</h3></td>
        <td>Screen brightness</td>
        <td>0-10</td>
      </tr>
      <tr>
        <td><h3>ADR</h3></td>
        <td>Enable/disable Adaptive Data Rate</td>
        <td>ON/OFF</td>
      </tr>
    </tbody>
  </table>

6.  After configuration, tap **OK** twice to save and exit.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/field-tester-apply-changes.png"
  width="50%"
  caption="Field Tester Apply Changes"
/>

### LoRaWAN OTAA Credentials Setup

The Field Tester Plus comes pre-configured with default **DevEUI**, **AppEUI**, and **AppKey**, so you can start testing immediately.

This setup step is **optional** and only required if you want to change the device credentials or register it to a different LoRaWAN® network.

The Field Tester Plus supports two configuration methods for setting DevEUI, AppEUI, and AppKey:

#### Mobile Configuration via WisToolBox App

**Preparation**

- Install **WisToolBox** from the App Store or Google Play.
- Power on your **Field Tester Plus**.
- Ensure Bluetooth is enabled on your phone and that it is placed near the device.

1. Launch the **WisToolBox App**, then tap **SATRT**.
2. Select **BLE Pairing** as the connection mode and tap **CONNECT**.
3. Once the device appears on your phone (e.g., `RAK10701.004474`), tap the green link button to complete pairing.
4. After pairing, the app will display **DEVICE INFO** and **PARAMETERS** tabs. Go to the **PARAMETERS** tab and expand **LoRaWAN® keys, ID, EUI**.
5. You can edit the following:
   + **Application EUI**
   + **Application Key**
   + **Device EUI**
6. After entering the credentials, tap **APPLY**.
7. When completed, the device restarts and syncs automatically.

#### PC Configuration via USB (Desktop WisToolBox)

1. Connect the Field Tester Plus to your PC using a USB Type-C cable.
2. Launch **WisToolBox for Desktop** and click **CONNECT** to establish a connection with the Field Tester Plus.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/wistoolbox-connection-settings.png"
  width="100%"
  caption="WisToolBox Connection Settings"
/>

:::tip NOTE
If the connection fails, refer to the <a href="https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/wistoolbox-desktop/#wistoolbox-dashboard" target="_blank">WisToolBox for Desktop | Installation and Setup Guide</a>.
:::

3. Select the device and navigate to the **ADVANCED** tab.


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/field-tester-connected-to-wistoolbox.png"
  width="100%"
  caption="Field Tester Connected To WisToolBox"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/field-tester-advanced-commands.png"
  width="100%"
  caption="Field Tester Advanced Commands"
/>

4. Click **OPEN CONSOLE**, then enter the following AT commands:

<table>
  <thead>
    <tr>
      <th>Command</th>
      <th>Value Format</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><h3>AT+DEVEUI=</h3></td>
      <td>8 bytes (64-bit hex, e.g. 70B3D57ED0012345)</td>
    </tr>
    <tr>
      <td><h3>AT+APPEUI=</h3></td>
      <td>8 bytes (64-bit hex)</td>
    </tr>
    <tr>
      <td><h3>AT+APPKEY=</h3></td>
      <td>16 bytes (128-bit hex)</td>
    </tr>
    </tbody>
</table>
<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/wistoolbox-at-command-console.png"
  width="100%"
  caption="WisToolBox AT Command Console"
/>


## Field Test Data Processor Extension Installation

The Field Test Data Processor Extension is an optional application that runs on RAK WisGate Edge gateways powered by WisGateOS 2. It enables local signal analysis, CSV report generation, and heatmap visualization for data collected by the Field Tester Plus.

The extension communicates with LoRaWAN Network Servers via **MQTT (subscribe/publish)**, and supports both Built-In and External LNS:

1. **RAK Gateways Built-in LNS**

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/built-in-lns-setup.png"
  width="80%"
  caption="Built-in LNS Setup"
/>

In this setup:

- Uplinks from the Field Tester are forwarded to the built-in LNS on the RAK Gateway.
- The extension subscribes to the MQTT Broker within the gateway to receive packets.
- This allows fully local processing, even **without an external network**. Best for **offline**, **indoor,** or **portable testing setups**.

2. **External LNS** (e.g., ChirpStack, TTN, AWS IoT Core)

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/external-lns-setup.png"
  width="80%"
  caption="External LNS Setup"
/>

In this setup:

- The RAK Gateway uses **Packet Forwarder** or **Basic Station** mode to connect to an external LNS (e.g., **ChirpStack, TTN, AWS IoT Core**).
- The extension remains installed locally on the gateway and connects to the external MQTT broker of the LNS to receive packet metadata for analysis.
- Ideal for **production deployments** with cloud LNS platforms.

**Installation Scenarios**

- **Field Tester Plus Bundle**: The included gateway comes pre-installed with the Field Test Data Processor Extension.
- **Other RAK WisGateOS 2 gateways**: Manually install the extension via the WisGateOS 2 web interface. See: <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later#how-to-add-an-extension" target="_blank">How to Add an Extension</a>.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/wisgateos-2-extensions-menu.png"
  width="100%"
  caption="WisGateOS 2 Extensions Menu"
/>

## Set Up the Gateway and the Field Tester Plus for Your LNS

This section provides step-by-step instructions to:

- Connect your LoRaWAN gateway to your chosen LNS platform.
- Register the Field Tester Plus device to the network.
- Install and configure the Field Test Data Processor Extension to enable local data analysis and reporting.

### Built-in LNS (WisGateOS 2)

#### Set Gateway to the Built-in Network Server

This section demonstrates how to connect your RAK gateway to a LoRaWAN Network Server (LNS).

1. Log into the WisGateOS 2 web UI. Navigate to **LoRa > Configuration**.
2. In the **Work Mode** section, select **Built-in Network Server**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/lora-configuration-work-mode.png"
  width="55%"
  caption="LoRa Configuration Work Mode"
/>

3. Select the log level and frequency band.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/log-frequency-band-configuration.png"
  width="100%"
  caption="Log And Frequency Band Configuration"
/>

:::tip NOTE
Make sure the frequency band configured on the gateway matches the **LoRaWAN Band setting** of your **Field Tester Plus**.
:::

#### Register the Field Tester Plus

1. Ensure your gateway is configured to use the **Built-in LNS**. Navigate to **LoRa** > **Applications** tab.
2. Click the **Add application** button (or the **add one now** link).

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/built-lns-application-menu.png"
  width="100%"
  caption="Built LNS Application Menu"
/>

3. You will be redirected to the application configuration page. Fill in the following fields:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/new-application-fields.png"
  width="100%"
  caption="New Application Data Fields"
/>

- **Application name**: Name of the application.
- **Application description**: Description of the application (optional).
- **Application Type**
    - **Unified Application key**: All devices will use the same application key.
    - **Separate Application keys**: Each device or group of devices has a unique key.
- **Auto Add Device**: When enabled, devices with matching AppKey and Application EUI will be added automatically after a successful join request.
- **Application Key**: Required for Unified Application Key setup.
- **Application EUI**: Required for automatic device registration when Auto Add Device is enabled.

:::tip NOTE
Refer to the  <a href="https://docs.rakwireless.com/product-categories/wisgate/rak10701-plus/network-setup/#field-tester-plus-configuration" target="_blank">Field Tester Plus Configuration</a> section for matching AppKey and AppEUI setup.
:::


4. Click **Save Application** to complete the creation.
5. Once the application is saved, navigate to: **Your Application** > **Configuration**. Click **End Devices** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/application-end-devices-menu.png"
  width="100%"
  caption="Application End Devices Menu"
/>

6. In the End device information interface, fill in the following information.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/end-device-otaa-configuration.png"
  width="100%"
  caption="End Device OTAA Configuration"
/>

- **Activation Mode**: Select OTAA. This value needs to be consistent with the value from the end device.
- **End device (group) name**: Name of the end device (group).
- **End device description (optional)** A description of the end device, optional.
- **Class**: Class A
- **Frame Counter Width**: Keep the default value.

7. Click **Add end devices** to enter the device adding page.

8. In the **Adding end devices** interface, enter the device EUI in the **End Device EUI (main)** field and click the **Add to End Devices list** button.

- Correct devices will appear under the **End devices list.**
- Duplicate devices will appear under **End devices with error** for correction.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/adding-new-end-device.png"
  width="100%"
  caption="Add New End Device"
/>

9. Click **Add end devices** to add the Field Tester Plus to the application.

Once registered, the Field Tester Plus will begin sending periodic uplinks to the Built-in LNS.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/end-device-field-tester-added.png"
  width="100%"
  caption="End Device Field Tester Added"
/>

The device is currently operating in **LinkCheck Mode**, as the Field Test Data Processor Extension has not yet been configured.
In this mode, the device screen will only display:

- **Downlink RSSI/SNR**
- **Number of responding gateways**

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/field-tester-linkcheck-mode.png"
  width="60%"
  caption="Field Tester LinkCheck Mode"
/>

Next, install and configure the Field Test Data Processor Extension to enable full metric reporting (uplinks, packet loss, CSV export).


#### Configure Field Test Data Processor Extension for Built-in LNS

For detailed steps on configuring the Field Test Data Processor Extension for the Built-in LNS, the <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/#built-in-network-server" target="_blank">WisGateOS 2 Extension > Field Test > Built-in Network Server</a>.

### The Things Network (TTN)

#### Connect Gateway to TTN

This section explains how to connect and configure a RAK gateway with The Things Network (TTN), using the RAK7289V2 model as a reference.

:::tip NOTE
Make sure the frequency band configured on the gateway matches the LoRaWAN Band setting of your Field Tester Plus.
:::

To complete the TTN gateway setup, follow the instructions in <a href="https://docs.rakwireless.com/product-categories/wisgate/rak7289v2/lorawan-network-server-guide/#the-things-network-ttn" target="_blank">RAK7289V2 LoRaWAN Network Server Guide |  The Things Network (TTN)</a>.


#### Register Field Tester Plus on TTN

To connect your Field Tester Plus to **The Things Network (TTN)**, a community-based LoRaWAN Network Server (LNS), visit the TTN Console at: https://console.cloud.thethings.network/

1. Choose the appropriate **cluster** for your region. You can either select your country or manually choose the nearest TTN cluster.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/the-things-network-cluster-selection.png"
  width="100%"
  caption="The Things Network Cluster Selection"
/>

2. On the homepage, click **Applications** > **+ Add application**

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/the-things-network-add-application.png"
  width="100%"
  caption="The Things Network Add Application"
/>

3. Add **Application ID**, **Application name**, and **Description** then click **Create application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/the-things-network-create-application.png"
  width="100%"
  caption="The Things Network Create Application"
/>

4. Click **Register end device** within your newly created application.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/the-things-network-register-end-device.png"
  width="100%"
  caption="The Things Network Register End Device"
/>

5. Choose **Enter end device specifics manually**. This will allow you to add the **Frequency plan, LoRaWAN version, Regional Parameters version**, and **JoinEUI**. The values of these parameters depend on the hardware you use. If your device has a preconfigured **JoinEUI**, you must use it. Click **Confirm** after putting all the details.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/the-things-network-joineui-and-parameters.png"
  width="100%"
  caption="The Things Network JoinEUI and Parameters"
/>

6. After confirming the **JoinEUI**, you can proceed on adding other OTAA parameters—**DevEUI** and **AppKey**. Use the **Generate** button if these parameters are not available with the device. Otherwise, use the OTAA parameters provided with the device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/the-things-network-deveui-and-appkey.png"
  width="100%"
  caption="The Things Network DevEUI and AppKey"
/>

7. After you register the device, it will be added to the LoRaWAN application.


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/the-things-network-device-added-succesfully.png"
  width="100%"
  caption="The Things Network Device Added Successfully"
/>

8. Restart the Field Tester Plus. Once registered and connected, it will begin sending periodic uplinks to the TTN LNS.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/the-things-network-live-data.png"
  width="100%"
  caption="The Things Network Live Data"
/>

The device is currently operating in **LinkCheck Mode**, as the Field Test Data Processor Extension has not yet been configured.
In this mode, the device screen will only display:
- **Downlink RSSI/SNR**
- **Number of responding gateways**

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/field-tester-uncomplete-menu.png"
  width="60%"
  caption="Field Tester Uncomplete Menu"
/>

Next, install and configure the Field Test Data Processor Extension to enable full metric reporting (uplinks, packet loss, CSV export).

#### Configure the Field Test Data Processor Extension for TTN

For detailed steps on configuring the Field Test Data Processor Extension for the TTN, refer to the <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/#the-things-network" target="_blank">WisGateOS 2 Extension > Field Test Data Processor > TTN</a>


### ChirpStack v3

#### Connect Gateway to ChirpStack v3

This section explains how to connect and configure a RAK gateway with ChirpStack v3.

:::warning
Make sure the frequency band configured on the gateway matches the LoRaWAN Band setting of your Field Tester Plus.
:::

1. To register the gateway in the ChirpStack Network server, access the ChirpStack UI. To do that, open a web browser and type the server address of the ChirpStack with port 8080.
IP address of ChirpStack: `8080`
2. Login using the following credentials:
- **Username/email:** admin
- **Password:** admin

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/33.png"
  width="55%"
  caption="ChirpStack Login page"
/>

3. Create a Service Profile (Required Before Gateway Registration). In the left sidebar, go to Service-profiles.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/34.png"
  width="100%"
  caption="Create a Service Profile"
/>

4. Click **+ CREATE** and fill in the following parameters:

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/35.png"
  width="100%"
  caption="Fill in Service Profile"
/>

- **Service-profile name:** Provide a descriptive name
- **Network-server:** build_in_ns
- **Add gateway meta-data:** Check this option
- **Minimum allowed data-rate** Set based on your region
- **Maximum allowed data-rate**：Set based on your region

5. Once completed, click **CREATE SERVICE PROFILE**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/36.png"
  width="100%"
  caption="Create Service Profile"
/>

6. In the left sidebar, go to **Gateways**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/37.png"
  width="100%"
  caption="ChirpStack Application Dashboard"
/>

7. Click **+ CREATE**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/38.png"
  width="100%"
  caption="Connect gateway on ChirpStack"
/>

8. Under the **General** section, fill in the following fields:

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/39.png"
  width="100%"
  caption="Fill in the gateway details"
/>

- **Gateway name:** A unique name for the gateway
- **Gateway Description:** A short description for identification
- **Gateway ID:** The gateway's EUI (found on the physical label or in the gateway’s Web UI under Dashboard > Overview)
- **Network-server:** build_in_ns
- **Service-profile:** Select the service profile you just created
9. Click **CREATE GATEWAY** to finish the registration.
10. Open your browser and go to the IP address of the gateway.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/40.png"
  width="100%"
  caption="WisGate Login Interface"
/>

11. Login using the credentials you set during the initial setup.
12. In the left sidebar, go to **LoRa**.
13. Under **Work Mode**, select **Packet forwarder**.
14. Click **Choose from the available protocols** to expand the protocol options. Change the **Protocol** to **LoRa Gateway MQTT Bridge**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/41.png"
  width="100%"
  caption="Choose LoRa Gateway MQTT Bridge"
/>

15. Set the following parameters:

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/42.png"
  width="100%"
  caption="Set LoRa Gateway MQTT Bridge Parameters"
/>

- **MQTT Protocol:** (Choose either of the following)
    - **MQTT for ChirpStack 3.x (JSON)**
    - **MQTT for ChirpStack 3.x (Protobuf)**. Based on your ChirpStack server configuration
- **MQTT Broker Address:** Enter the IP address where ChirpStack is deployed
- **MQTT Broker Port:** `1883`

16. Click **Save changes** to save the changes.

If everything is set correctly, the gateway will display as online. You can click the gateway name to inspect the gateway traffic.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/43.png"
  width="100%"
  caption="Save changed on ChirpStack"
/>

#### Register Field Tester Plus on ChirpStack v3

1. Log in to your Chirpstack account and on the main dashboard page click **Device-profiles**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/44.png"
  width="100%"
  caption="Device profile"
/>

2. Click **+ CREATE** and fill in the following parameters:

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/45.png"
  width="100%"
  caption="Add Device profile information"
/>

- **Device-profile name:** Provide a descriptive name
- **Network-server:** build_in_ns
- **LoRaWAN MAC version:** Select the appropriate version supported by your device
- **LoRaWAN Regional Parameters revision:** Choose the revision that matches your region
- **ADR algorithm:** Select Default ADR algorithm (LoRa only)
- **Max EIRP:** Enter the maximum EIRP supported by the device
- **Uplink interval (seconds):** Set the desired uplink interval (e.g., 300 seconds or 5 minutes)

3. Go to the **Join (OTAA / ABP)** tab. Check the option: **Device supports OTAA**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/46.png"
  width="100%"
  caption="Check Device supports OTAA*"
/>

4. Click **CREATE DEVICE PROFILE**.
5. In the left sidebar, go to **Applications**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/47.png"
  width="100%"
  caption="ChirpStack Application"
/>

6. Click **+ CREATE**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/48.png"
  width="100%"
  caption="Add Application information"
/>

7. Fill in the application parameters, then click **CREATE APPLICATION**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/49.png"
  width="100%"
  caption="Fill in the application parameters"
/>

8. Click the name of the application you just created.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/50.png"
  width="100%"
  caption="Click the name of the application"
/>

9. Click **+ CREATE** to register a new device, and fill in the device parameters:

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/51.png"
  width="100%"
  caption="Register a new device"
/>

- **Device name:** A unique name for the device
- **Device description:** A short description
- **Device EUI:** Must match the EUI of your Field Tester Plus
- **Device-profile:** Select the device profile you created earlier
10. After saving by clicking **CREATE**, go to the **KEYS (OTAA)** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/52.png"
  width="100%"
  caption="ChirpStack OTAA key"
/>

11. Enter the **Application Key** associated with your Field Tester Plus device, then click **SET DEVICE KEYS**.

Once registered, the Field Tester Plus will begin sending periodic uplinks to the Chirpstack v3 LNS.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/53.png"
  width="100%"
  caption="Enter Application Key"
/>

The device is currently operating in **LinkCheck Mode**, as the Field Test Data Processor Extension has not yet been configured.
In this mode, the device screen will only display:
- **Downlink RSSI/SNR**
- **Number of responding gateways**

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/network-setup/ft-linkcheck-mode.png"
  width="55%"
  caption="Field Tester LinkCheck Mode"
/>

Next, install and configure the Field Test Data Processor Extension to enable full metric reporting (uplinks, packet loss, CSV export).

#### Configure Field Test Data Processor Extension for ChirpStack v3

For detailed steps on configuring the Field Test Data Processor Extension for the ChirpStack v4, refer to the <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/#chirpstack-v3" target="_blank">WisGateOS 2 Extension > Field Test Data Processor > ChirpStack v3</a>.

### ChirpStack v4

#### Connect Gateway to ChirpStack v4

This section explains how to connect and configure a RAK gateway with ChirpStack v4, using the RAK7289V2 model as a reference.

:::tip NOTE
Make sure the frequency band configured on the gateway matches the LoRaWAN Band setting of your Field Tester Plus.
:::


To complete the ChirpStack v4 gateway setup, follow the instructions in <a href="https://docs.rakwireless.com/product-categories/wisgate/rak7289v2/lorawan-network-server-guide/#chirpstack" target="_blank">RAK7289V2 LoRaWAN Network Server Guide |  ChirpStack v4.</a>

#### Register Field Tester Plus on ChirpStack v4

1. Log in to your Chirpstack account and on the main dashboard page click **Applications.**

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/chirpstack-application-dashboard.png"
  width="100%"
  caption="ChirpStack Application Dashboard"
/>

2. Click **Add application** and fill in the required fields:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/chirpstack-add-application.png"
  width="100%"
  caption="ChirpStack Add Application"
/>

3. Click **Submit** to create the application.

4. Go to **Device Profiles** and click **Add device profile.**

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/chirpstack-add-device-profile.png"
  width="100%"
  caption="ChirpStack Add Device Profile"
/>

5. Configure the profile to match your device's specifications:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/chirpstack-match-device-specifications.png"
  width="100%"
  caption="ChirpStack Match Device Specifications"
/>

6. In the device profile configuration, go to the **Join (OTAA / ABP)** tab.
7. Enable the **Device supports OTAA** option and click **Submit** to save the device profile.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/chirpstack-enable-support-otaa.png"
  width="100%"
  caption="ChirpStack Enable Support OTAA"
/>

8. Navigate to the **Applications > your application** and click **Add device**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/chirpstack-add-device-on-applications.png"
  width="100%"
  caption="ChirpStack Add Device on Applications"
/>

9. On the Add Device page, you must enter the device details, including **Name, Description, Device EUI, Join EUI**, and **Device Profile**. You can use the **Generate** button for the **Device EUI** and **Join EUI** if these values are not available with the device. Otherwise, use the OTAA parameters provided by the device. After entering all required information, click **Submit** to complete the process.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/chirpstack-fill-device-information.png"
  width="100%"
  caption="ChirpStack Fill Device Information"
/>

10. The next step is to provide the **Application Key**. Use the key provided with the device, if available; otherwise, click the Generate button to create one. After entering the **Application Key**, click **Submit** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/chirpstack-add-application-key.png"
  width="100%"
  caption="ChirpStack Add Application Key"
/>

Once registered, the Field Tester Plus will begin sending periodic uplinks to the Chirpstack v4 LNS.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/sending-periodic-uplinks-to-chripstack.png"
  width="100%"
  caption="Sending Periodic Uplinks to ChripStack"
/>

The device is currently operating in **LinkCheck Mode**, as the Field Test Data Processor Extension has not yet been configured.
In this mode, the device screen will only display:
- **Downlink RSSI/SNR**
- **Number of responding gateways**

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/field-tester-only-displays-rssi-and-snr.png"
  width="60%"
  caption="Field Tester Only Displays RSSI and SNR"
/>

Next, install and configure the Field Test Data Processor Extension to enable full metric reporting (uplinks, packet loss, CSV export).

#### Configure Field Test Data Processor Extension for ChirpStack v4

For detailed steps on configuring the Field Test Data Processor Extension for the ChirpStack v4, refer to the
<a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/#chirpstack-v4" target="_blank">WisGateOS 2 Extension > Field Test Data Processor > ChirpStack v4.</a>

### AWS IoT Core for LoRaWAN

#### Connect Gateway to AWS IoT Core for LoRaWAN

This section explains how to connect and configure WisGateOS 2 with AWS IoT Core, using the RAK7289V2 model as a reference.

:::tip NOTE
Make sure the frequency band configured on the gateway matches the LoRaWAN Band setting of your Field Tester Plus.
:::

To complete the AWS IoT Core gateway setup, follow the instructions in <a href="https://docs.rakwireless.com/product-categories/wisgate/rak7289v2/lorawan-network-server-guide/#aws-iot-core-for-lorawan" target="_blank">RAK7289V2 LoRaWAN Network Server Guide |  AWS IoT Core .</a>

#### Register Field Tester Plus on AWS IoT Core for LoRaWAN

##### **Create a destination role for AWS IoT Core for LoRaWAN**

To allow **AWS IoT Core for LoRaWAN** to forward device data to AWS services (via **Destinations**), you must assign an IAM role and policy that authorizes the service to publish messages on your behalf. If you've already created this IAM role during gateway setup, there's no need to create it again. Otherwise, follow the official AWS instructions below to set it up:  <a href="https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-create-destinations.html#lorawan-create-destinations-roles" target="_blank">Create a destination role for AWS IoT Core for LoRaWAN</a>

##### Verify Profiles

1. Navigate to the <a href="http://console.aws.amazon.com/iot" target="_blank">AWS IoT console.</a>
2. In the navigation pane, go to **LPWAN Devices > Profiles.**
3. Under **Device Profiles**, review the pre-defined options.
    - If none fit your device or region, click Add device profile and configure custom parameters.
    - Example: For AS923-1, set parameters accordingly.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/aws-add-device-profile.png"
  width="100%"
  caption="AWS Add Device Profile"
/>

4. Click **Add device profile** to save.
5. In the **Service Profiles** section, click **Add service profile** and configure service parameters (default values are generally acceptable).

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/aws-add-service-profile.png"
  width="100%"
  caption="AWS Add Service Profile"
/>

6. Once you have created appropriate Device and Service Profiles, proceed to set up a destination for device traffic.

##### Set Up a Destination for Device Traffic

To use the Field Tester Extension with AWS IoT Core for LoRaWAN, you must associate your device with a **Destination**—this defines where your uplink data will be sent.
1. Navigate to the <a href="http://console.aws.amazon.com/iot" target="_blank">AWS IoT console</a>.
2. In the navigation pane, choose **LPWAN devices**, and then **Destinations**.
3. Choose **Add Destination**.
4. Fill in the Destination details:
  - For the **Destination name**, enter ***ProcessFieldTesterUplink***. The name can be customized.
  - **Destination description** *(optional)*: Provide a helpful description.
5. Select **Publish to AWS IoT Core message broker**. This allows the uplink messages to be published to an MQTT topic for other applications or services to consume.
6. Enter a topic such as ***RecvFieldTesterUplink***.
7. In the **Permissions** section, choose **Select an existing service role** and select the <a href="https://docs.google.com/document/d/1-rhXw2Zwb8cTQPsnSTE_mpa5e3dalNT6/edit#heading=h.5uqr7h5v8y76" target="_blank">IAM role</a> you had created earlier, from the drop-down.
8. Choose **Add Destination**. You will see a message ***Destination added***, indicating the destination has been successfully added.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/aws-add-destination.png"
  width="70%"
  caption="AWS Add Destination"
/>

##### Register Device

1. In the navigation pane, go to **LPWAN Devices > Devices**.
2. Click **Add wireless device**.
3. On the **Add Device** page:
4. Select the LoRaWAN specification version in the drop-down under **Wireless device specification**.
5. Enter the **DevEUI**.
6. Fill in the **AppEUI/JoinEUI** and **AppKey** as per your OTAA settings.
7. Provide a wireless **Device name**.
8. Under Profiles, select the **Device Profile** and **Service Profile** you created earlier.
9. Under **Destination**, choose the one previously created.


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/aws-configure-lorawan-device.png"
  width="100%"
  caption="AWS Configure LoRaWAN Device"
/>

10. Click **Next**, then **Add device** to complete registration.

Once registered, the Field Tester Plus will begin sending periodic uplinks to the AWS IoT Core.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/aws-field-tester-configuration-completed.png"
  width="100%"
  caption="AWS Field Tester Configuration Completed"
/>

The device is currently operating in **LinkCheck Mode**, as the Field Test Data Processor Extension has not yet been configured.
In this mode, the device screen will only display:
- **Downlink RSSI/SNR**
- **Number of responding gateways**

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/field-tester-only-displays-rssi-and-snr.png"
  width="60%"
  caption="Field Tester Only Displays RSSI and SNR"
/>

Next, install and configure the Field Test Data Processor Extension to enable full metric reporting (uplinks, packet loss, CSV export).

#### Configure Field Test Data Processor Extension for AWS

For detailed steps on configuring the Field Test Data Processor Extension for the AWS IoT Core, refer to the <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/#aws-iot" target="_blank">WisGateOS 2 Extension > Field Test > AWS IoT.</a>

### The Things Industries (TTI)

#### Connect Gateway to TTI

This section explains how to connect and configure a RAK gateway with The Things Industries (TTI), using the RAK7289V2 model as a reference.

:::warning IMPORTANT
Make sure the frequency band configured on the gateway matches the LoRaWAN Band setting of your Field Tester Plus.
:::

1. Log in to your organization’s TTS Console.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-login-page.png"
  width="100%"
  caption="TTI Login page"
/>

2. To register a gateway, go to **Gateways** > **+ Register gateway**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-register-gateway.png"
  width="100%"
  caption="Register gateway on TTI"
/>

3. You will be redirected to the Register gateway page.
4. In the Gateway EUI field, type the EUI of the gateway.

:::tip NOTE
- Check the label on the device casing marked as GWEUI.
- Optionally, log in to the gateway's Web UI and navigate to **Dashboard** > **Overview**.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-gateway-eui-field.png"
  width="100%"
  caption="Type EUI of the gateway on TTI"
/>

5. After typing the EUI, click on **Confirm**. Additional fields will pop up. Fill in the following information:

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-confirm-eui.png"
  width="100%"
  caption="Confirm EUI"
/>

- **Gateway ID:** The unique ID of your gateway in the Network.  The ID must contain only lowercase letters, numbers, and dashes (-).
- **Gateway name:** Optionally, you can type a name for your gateway.
- **Frequency plan:** The frequency plan used by the gateway.

:::tip NOTE
The other settings are optional and can be changed to satisfy your requirements. For this tutorial, we will use Australia 915-928&nbsp;MHz, FSB 2 (used by TTN).
:::

6. To register your gateway, click **Register gateway**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-click-register-gateway.png"
  width="100%"
  caption="Register gateway"
/>

7. TTNv3 supports TLS server authentication and Client token, which requires a trust file and a key file to configure the gateway to successfully connect it to the network. To generate a key file, from the **Overview** page of the registered gateway navigate to API keys.https://console.cloud.thethings.network/

8. On the **API keys** page, choose **+ Add API key**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-add-api-key.png"
  width="100%"
  caption="Click Add API key"
/>

9. In the **Name** field, type the name of your key (for example - mykey). Choose **Grant individual rights** and select **Link as Gateway to a Gateway for traffic exchange, i.e. write uplink and read downlink**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-add-key-name.png"
  width="100%"
  caption="Choose Grant individual rights"
/>

10. To generate the key, choose **Create API key**. The following window will pop up, telling you to copy the key you just generated.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-create-api-key.png"
  width="55%"
  caption="Click on Create API key"
/>

:::warning
Copy the key and save it in a .txt file (or other), because you won’t be able to view or copy your key after that.
:::

11. Click **I have copied the key** to proceed.
12. To configure the gateway, access it via the Web UI. Navigate to **LoRa** > **Configuration** > **Work mode** and select **Basics station**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-configure-gateway.png"
  width="100%"
  caption="Configure gateway"
/>

13. Expand the Basics Station settings by clicking **Configure Basics Station server setup** and configure the following parameters:

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-configure-basic-station.png"
  width="100%"
  caption="Configure Basics Station server setup"
/>

- **Basics Station Server Type**: For server type, choose LNS Server.
- **Server URL**: You can find it in The Things Stack (TTS) Console, under your registered gateway’s **left-hand menu** > **General settings** > **Gateway Server address**.
    :::tip NOTE
    Make sure to add wss:// in front of the address when entering it into your gateway configuration.
    :::
- **Server Port:** The LNS Server uses port 8887.
- **Authentication Mode:** Choose TLS server authentication and Client token. When selected, the **Trust (CA Certificate)** and **Client token** fields will show up.
- **Trust (CA Certificate):** For **Trust**, upload the **Let’s Encrypt ISRG ROOT X1** Trust certificate by clicking **choose file**. The file with the certificate can be downloaded directly.
- **Client Token:** This is the generated API key.

14. To save the changes, click **Save Changes**.

If everything is set correctly, you can see the gateway is connected to TTNv3.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-save-changes.png"
  width="100%"
  caption="Save changes"
/>

#### Register Field Tester Plus on TTI

1. Log in to your organization’s TTS Console.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-login-page.png"
  width="100%"
  caption="The Things Stack Login page"
/>

2. To create an application, go to **Applications** > **+ Add application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-login-page.png"
  width="100%"
  caption="Create an application"
/>

3. Add **Application ID**, **Application name** and **Description** then click **Create application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-register-gateway.png"
  width="100%"
  caption="Register gateway"
/>

4. Click **Register end device** within your newly created application.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-gateway-eui-field.png"
  width="100%"
  caption="Register end device"
/>

5. Choose **Enter end device specifics manually**. This will allow you to add the **Frequency plan, LoRaWAN version, Regional Parameters version** and **JoinEUI**. The values of these parameters depend on the hardware you use. If your device has a preconfigured JoinEUI, you must use it. Click **Confirm** after putting all the details.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-register-end-device.png"
  width="100%"
  caption="Enter end device specifics"
/>

6. After confirming the **JoinEUI**, you can proceed on adding other OTAA parameters – **DevEUI** and **AppKey**. You can use the **Generate** button if these parameters are not provided in the device. Else, you must use OTAA parameters are provided in the device.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-add-otaa-parameters.png"
  width="100%"
  caption="Add OTAA parameters"
/>

7. After you register the device, it will be added on the LoRaWAN Application. Restart the Field Tester Plus and it will join the network and begin sending regular uplinks.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-send-regular-uplinks.png"
  width="100%"
  caption="Regular Uplinks"
/>

Once registered, the Field Tester Plus will begin sending periodic uplinks to the TTN LNS.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-send-periodinc-uplink.png"
  width="100%"
  caption="Periodic Uplinks"
/>

The device is currently operating in ****, as the Field Test Data Processor Extension has not yet been configured. In this mode, the device screen will only display:
- **Downlink RSSI/SNR**
- **Number of responding gateways**

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/tti/tti-linkcheck-mode.png"
  width="55%"
  caption="Field Tester LinkCheck Mode"
/>

Next, install and configure the Field Test Data Processor Extension to enable full metric reporting (uplinks, packet loss, CSV export).

#### Configure Field Test Data Processor Extension for TTI

For detailed steps on configuring the Field Test Data Processor Extension for the TTI, refer to the <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/#the-things-industries" target="_blank">WisGateOS 2 Extension > Field Test Data Processor > TTI</a>.

<RkBottomNav/>