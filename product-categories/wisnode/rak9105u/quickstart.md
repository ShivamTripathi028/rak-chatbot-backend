---
slug: /product-categories/wisnode/rak9105u/quickstart/
title: RAK9105U Remote Reboot Switch for LoRaWAN Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK9105U. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: "https://images.docs.rakwireless.com/wisnode/rak9105u/1.rak9105u.png"
keywords:
  - quickstart
  - RAK9105U
  - wisnode
tags:
    - rak9105u
    - wisnode
    - quickstart
sidebar_label: Quick Start Guide
date: 2025-07-10
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK9105U PowerLink - Remote Reboot Switch for LoRaWAN Quick Start Guide

The **RAK9105U PowerLink** offers 2 typical setup paths to accommodate different deployment needs from rapid evaluation to full-scale integration.
- [**Plug-and-Play Solution Kit**](#plug-and-play-solution-kit)<br/>
Ideal for fast evaluation, testing, or small-scale deployments. This option uses a pre-configured RAK9105U and LoRaWAN gateway connected to the Datacake platform. No manual setup is required.
- [**Custom Setup (Advanced Integration)**](#custom-setup-advanced-integration)<br/>
Designed for users who wish to integrate the RAK9105U into their own LoRaWAN infrastructure. This setup requires manual configuration via the USB console and tools such as WisToolBox or AT commands.

In the following sections, you’ll find step-by-step instructions for each setup path, including hardware installation, configuration, and LoRaWAN network onboarding.

## Plug-and-Play Solution Kit

This section guides you through the fastest way to get your RAK9105U Solution Kit up and running, verify remote power control, and experience the reboot functionality using the Datacake app.

### Prerequisites

Before you proceed, make sure you have the following items:
- 1 RAK9105U PowerLink
- 1 RAK7268V2 LoRaWAN Gateway Kit (pre-configured)
- 1 USB Type-C Cable
- 2 DC Power Cables
- 1 4-Pin Terminal Block

<b>Required External Items</b>

- **9-24&nbsp;V<sub>DC</sub> power source**
- A **mobile device** with the **Datacake App** installed (available on iOS and Android)

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/rak9105u-solution-kit-package-inclusions.png"
  caption="RAK9105U Advanced Integration Package Inclusions"
  width="80%"
/>

### Solution Kit Hardware Installation

1. **Connect to the target device**<br/>
Use the provided cables to connect the device (e.g., IP camera or LTE router) to one of the following output ports on the RAK9105U:
    - **Output 2 (Barrel Jack)** – remotely controllable
    - **Output 3 (USB Type-C)** – remotely controllable
2. **Power the RAK9105U**<br/>
Connect a 9-24&nbsp;V<sub>DC</sub> power source to the DC input port. You can use either the included 4-pin terminal block or the standard barrel jack.<br/>
**Recommended input**: 12&nbsp;V<sub>DC</sub>.
3. **Set up the gateway**<br/>
To enable LoRaWAN communication, the included RAK7268V2 gateway must be powered on and connected to the internet.
  - **Ensure Internet Connectivity**<br/>
      For plug-and-play operation, it is recommend to use **Ethernet**. Simply connect the cable to the gateway and router. No configuration needed.
      :::tip NOTE
      If you prefer to use Wi-Fi, **follow the gateway power-on steps first** (see the **Power On the Gateway** section), ensuring the antenna is installed and the device is mounted properly. Then, configure the wireless settings through the gateway’s web interface.
      For detailed instructions, refer to the <a href="https://docs.rakwireless.com/product-categories/wisgate/rak7268v2/quickstart/#access-the-internet?intsource=docs_center&intmedium=organic&intcampaign=rak9105u_documentation_quickstart_page&intterm=rak7268v2-quickstart-guide&intcontent=documentation_link" target="_blank">RAK7268V2 Quick Start Guide</a>.
      :::
  - **Power On the Gateway**<br/>
    Before powering on the gateway, ensure the LoRa antenna is properly installed and the device is securely mounted. For detailed setup steps, refer to the <a href="https://docs.rakwireless.com/product-categories/wisgate/rak7268v2/quickstart/#gateway-installation-guide?intsource=docs_center&intmedium=organic&intcampaign=rak9105u_documentation_quickstart_page&intterm=rak7268v2_installation_guide&intcontent=documentation_link" target="_blank">RAK7268V2 installation guide</a>.
    Connect the power adapter to the gateway and plug it into a power outlet.
  - **Check Gateway Status**<br/>
    After powering on the gateway, wait up to **2&nbsp;minutes** and observe the LED indicators to verify normal operation:

| LED                                | Expected Status After Power-On | Description                                                                                                                                  |
|------------------------------------|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| PWR LED                            | ON (solid)                     | Power is connected; the gateway is powered on.                                                                                               |
| Breathing LED                      | Blue (slow blinking)           | **Red** indicates the gateway is not yet connected to the internet.<br/>**Blue** (slow blinking) indicates a successful internet connection. |
| ETH LED (if Ethernet is connected) | ON / Flickering                | Ethernet port is active; data transmission may be occurring.                                                                                 |
| WLAN LED                           | ON / Flickering                | WiFi AP mode is active and functional.                                                                                                       |
| LoRa LED                           | ON / Flickering                | Indicates the LoRa transceiver is operational and handling packets.                                                                          |


:::warning IMPORTANT
- If the **blue LED** is not on, the gateway is not connected to the internet and cannot forward LoRaWAN traffic.
- **Do not press the reset button** unless instructed. It will erase factory provisioning and disconnect the gateway from the solution kit.
:::

### Add Your Device to the Datacake App

1. Install the **Datacake App** on your **iOS or Android** device.
2. Open the app on your phone.
3. Tap the **+** icon on the top-right corner of the home screen.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/add-device-in-datacake-app.png"
  caption="Add Device in the Datacake App"
  width="35%"
/>

4. Select **Scan QR Code**, grant camera access if prompted, and scan the QR code on the RAK9105U label.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/scan-qr-code.png"
  caption="Scan QR code"
  width="35%"
/>

5. The app will detect the device automatically. You can rename it if needed (e.g., **Camera Power** or **Router Switch**).

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/rename-device.png"
  caption="Rename the Device"
  width="35%"
/>

6. Tap **Save** to add the device to the **Devices** list.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/save-device-to-datacake.png"
  caption="Save the Device on DataCake"
  width="35%"
/>

7. Select the device entry to access the pre-configured control dashboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/preconfigured-control-dashboard.png"
  caption="Pre-configured Control Dashboard"
  width="35%"
/>

### Control Power Outputs

The Datacake dashboard allows you to remotely monitor and control the 2 output channels of the RAK9105U PowerLink.
As shown in the screenshot:
- The dashboard displays 2 device tiles representing the controllable outputs:
  - **Device A** → corresponds to **Output 3** (5&nbsp;V USB Type-C)
  - **Device B** → corresponds to **Output 2** (12&nbsp;V<sub>DC</sub> Barrel Jack)
- Each device block includes:
  - Status indicator (e.g., **On** in green when powered)
  - Timestamp of the last update (e.g., **8 seconds ago**)
  - Two control buttons:
    - Power on **Device A/B**: Sends a downlink to enable output
    - Power off **Device A/B**: Sends a downlink to disable output

## Custom Setup (Advanced Integration)

Designed for users who wish to integrate the RAK9105U into their own LoRaWAN infrastructure. This setup requires manual configuration via the USB console and tools such as WisToolBox.

This guide assumes you have an existing LoRaWAN infrastructure in place (i.e., a functioning gateway and network server). The following steps will show how to configure and register the RAK9105U to your own LNS.

### Prerequisites

Before starting, make sure to have the following items:
  - 1 RAK9105U PowerLink
  - 1 USB Type-C Cable
  - 2 DC Power Cables
  - 1 4-Pin Terminal Block

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/rak9105u-custom-setup-package-inclusion.png"
  caption="RAK9105U Custom Setup Package Inclusions"
  width="80%"
/>

<b>Required External Items</b>
- 9–24&nbsp;V<sub>DC</sub> power source
- Access to a functioning LoRaWAN Network Server (e.g., ChirpStack, The Things Stack, etc.)
- Computer with WisToolBox installed (desktop version)
- Deployed and internet-connected LoRaWAN gateway. (Must be located within radio range of the RAK9105U, and properly configured to forward packets to your chosen network server)

### Configure RAK9105U with WisToolBox

#### Connect to the PC

1. Download and install WisToolBox for the operating system.
2. Use a USB Type-C cable to connect the **Console port** of the RAK9105U to the computer.
3. Open WisToolBox and click **START** to detect connected devices.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/wistoolbox-click-start.png"
  caption="Click START on WisToolBox"
  width="100%"
/>

4. Once the device is recognized (as a RAK3172-based module), click **CONNECT**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/wistoolbox-click-connect.png"
  caption="Connect Device via WisToolBox"
  width="100%"
/>

5. Click the device icon to open the **Device Information** and begin configuration.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/wistoolbox-open-device-information.png"
  caption="Open Device information"
  width="100%"
/>

#### LoRaWAN Configuration

1. In the **PARAMETERS** tab, go to **Global Settings** and configure:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/wistoolbox-global-settings.png"
  caption="WisToolBox Global Settings"
  width="100%"
/>

  - **Network mode**: Select LoRaWAN
  - **Join mode**: Select OTAA (Only OTAA is supported)
  - **Active region**: Choose the appropriate frequency band (e.g., EU868, US915, AS923), consistent with your LoRaWAN network’s gateway region.

2. Navigate to **LoRaWAN Keys, ID, EUI**, and configure the following:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/wistoolbox-lorawan-keys-id-eui.png"
  caption="LoRaWAN Keys, ID, and EUI Configuration"
  width="100%"
/>

  - **Application EUI**: Modify as needed
  - **Application key**: Enter manually or click the key icon to generate one automatically
  - **Device EUI**: Modify if required

:::warning IMPORTANT
These credentials must match the parameters used when adding the device to the target LoRaWAN Network Server (LNS). Mismatched credentials will cause join failures.
:::

3. Go to **Data on LoRaWAN® Network** and adjust the following:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/wistoolbox-adjust-network-parameters.png"
  caption="Adjust LoRaWAN Network Settings"
  width="50%"
/>

  - **Confirm Mode**: Enable or disable confirmed messages
  - **Enable Join Process**: Set to Enabled
  - **Automatic Access**: Enable this option to allow the device to automatically join the LoRaWAN network upon power-up.
  - **Reattempt Period (s)**: Retry interval (default: 8 seconds)
  - **Max Number of Reattempts**: Retry limit (default: 0 = unlimited)

Optional:
  - **JOIN NETWORK**: Click this button to manually start join process if auto-join is disabled
  - **Network Status**: Displays join result
  - **Last Received Data**: Shows most recent received data
  - **Send Data**: Use to test uplink payload transmission

4. Click **APPLY COMMAND** in the confirmation pop-up window.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/click-apply-command.png"
  caption="Click APPLY COMMAND"
  width="100%"
/>

5. Wait for the device to complete configuration and respond with a success status.

Once LoRaWAN parameters are configured, the RAK9105U is prepared to join the network.
After registering the device on the LoRaWAN Network Server (LNS) using the same credentials, it will be ready to receive downlink commands for remote power control.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/join-configuration-success.png"
  caption="Success Join Configuration"
  width="100%"
/>

:::warning IMPORTANT
<b>Deployment Note (Pre-Installation)</b>

At this stage, the RAK9105U PowerLink is powered temporarily via USB for configuration only. Do not connect the device to any power-controlled equipment or deploy it on-site yet.

This approach ensures:
- The LoRaWAN configuration is completed correctly
- The device can be successfully registered and joined to the network server
- Risk is minimized when later connecting to actual loads (e.g., routers, cameras)

Hardware wiring and physical installation will be covered in the [Hardware Installation](#hardware-installation) section, after confirming successful network integration.
:::


### Connect to a LoRaWAN Network Server

This section shows how to connect RAK9105U to different LoRaWAN network servers.

The RAK9105U supports standard OTAA activation and is compatible with common LNS platforms.

Supported Platforms:
- RAK Built-in LNS (WisGateOS2)
- The Things Stack (TTN v3)
- ChirpStack v4
- Other standards-compliant private or cloud-based LNS


#### Connect to RAK Built-in LNS (WisGateOS 2)

Follow these steps to register the RAK9105U PowerLink to a RAK gateway running WisGateOS2 in Built-in Network Server mode.

This guide assumes that the RAK gateway has already been deployed and configured for your target region.

##### Set Work Mode to Built-in Network Server
1. Log in to the WisGateOS 2 web interface. Refer to the RAK Gateway User Manual for instructions on accessing the UI.

Start by accessing the gateway. Refer to the <a href="https://docs.rakwireless.com/product-categories/wisgate/?intsource=docs_center&intmedium=organic&intcampaign=rak9105u__documentation_quickstart_page&intterm=rak_gateway_user_manual&intcontent=documentation_link" target="_blank">RAK Gateway User Manual</a> for instructions on accessing the UI.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/bins1-home-page.png"
  caption="Login Page"
  width="100%"

/>

2. Once logged in, navigate to the **LoRa** menu and set the gateway's **Work Mode** to **Built-in Network Server**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/bins2-work-mode.png"
  caption="Configure the Work Mode"
  width="100%"

/>

##### Create an Application

1. Head to the **Applications** tab. Click **Add application** or **Add one now** to create a new application.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/wisgate-add-application.png"
  caption="Add WisGate application"
  width="100%"
/>

2. Fill in the following fields:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/bins4-add-app.png"
  caption="Add Application"
  width="100%"
/>

- **Application Name**: Enter a name for the application.
- **Application Description**: Optionally, provide a brief description of the application.
- **Application Type**: Select the appropriate type from the drop-down menu.
  - **Unified Application Key**: All devices will use the same application key. Enter your App Key (must match the key set in RAK9105U), or click **Autogenerate**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/bins5-autogenerate.png"
  caption="Autogenerate Option"
  width="50%"

/>

- **Separate Application keys**: Each device uses its own App Key (entered during device registration)

:::tip NOTE
- If using **Auto Add Device**, also configure the Application EUI. This must match the EUI set on the RAK9105U. You can either manually enter it or synchronize it based on device. Once both App EUI and App Key match, the device will auto-register when it joins.


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/bins6-auto-add.png"
  caption="Auto Add Device Option"
  width="50%"

/>
:::

3. Click **Save application** to add the application

##### Register the Device

**If Auto Add Device is Enabled**, the RAK9105U will automatically register in the End devices list once it sends a join request.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/bins7-add-end-dev.png"
  caption="Device Added"
  width="100%"

/>

**If Auto Add Device is Disabled**, refer to the following steps to manually add devices.

1. Go to the **End devices** tab and click **Add end device**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/bins8-add-dev-manually.png"
  caption="End Devices Tab"
  width="100%"
/>

2. Fill in the required information:

- **Activation Mode**: Select **OTAA**.
- **End Device (Group) Name**: Enter the name of the device for identification.
- **End Device Description (Optional)**: Optionally, add a description for the device.
- **Class**: Select the appropriate device class.
- **Frame Counter Width**: Use the default setting.
- **LoRaWAN MAC Version**: Select the correct LoRaWAN MAC version for the device.


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/bins9-end-dev-info.png"
  caption="Add Device Manually"
  width="100%"
/>

3. In the next step, enter the **End Device EUI (Main)** (must match the one set in WisToolBox) and click **Add to “End Devices List”**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/enter-the-end-device-eui.png"
  width="100%"
  caption="Enter the End Device EUI"
/>

4. Click **Add end devices**. Confirm and complete the device addition.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/click-add-end-devices.png"
  width="50%"
  caption="Click Add end devices"
/>

Once the device is registered, it will appear in the **End Devices** list.
A successful network join can be confirmed by checking that the “**LAST SEEN**” field shows a recent timestamp, indicating that the server has received uplink data from the device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/end-devices-list.png"
  width="100%"
  caption="End Devices list"
/>

#### Connect to The Things Network (TTN v3)

This section explains how to register the RAK9105U PowerLink on **The Things Stack (TTN v3)** using LoRaWAN OTAA activation, assuming the gateway is already deployed and connected to your TTN environment.

##### Create an Application in TTN v3

1. Log in to the TTN Console. Go to **Applications** and click **+ Add Application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/ttn-add-application.png"
  caption="Add TTN application"
  width="100%"
/>

2. Fill in the required details (e.g., Application ID: **smart-plugin**)

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/ttn-add-application-id.png"
  caption="Add application ID on TTN"
  width="100%"
/>

3. Click **Create Application**.

##### Register the Device in TTN v3

1. Inside the newly created application, click **+ Register end device**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/ttn-register-end-device.png"
  caption="Register end device on TTN"
  width="100%"
/>

2. Configure General Parameters
- **Input Method**: Select **Enter end device specifics manually**.
- **Frequency Plan**: Match your gateway’s region (e.g., EU868)
- **LoRaWAN Version**: Select 1.0.3
- **JoinEUI**: Enter the value that matches your RAK9105U configuration

3. After confirming the JoinEUI, proceed to fill in:
- **DevEUI**: Same as configured on the RAK9105U
- **AppKey**: Must match the value set on the RAK9105U (or auto-generated during setup)
- **End device ID**: Enter a unique identifier (e.g., my-device)

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/ttn15-gateway-conn.png"
  caption="End Device Parameters"
  width="100%"
/>


4. Click **Register end device** to complete.

Once the RAK9105U has successfully joined the network, you will see the Last activity timestamp in the TTN Console device overview.

The activity counter (e.g., 1 up / n/a down) indicates that uplink and downlink communication is working as expected.


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/ttn-activity-timestamp.png"
  caption="TTN activity timestamp"
  width="100%"
/>

#### Connect to ChirpStack v4

This section explains how to register the RAK9105U PowerLink on ChirpStack v4 using OTAA activation, assuming that your LoRaWAN gateway is already deployed and connected to a functioning ChirpStack server.

##### Create an Application in ChirpStack v4

1. In ChirpStack UI, go to **Applications** and click **Add application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/chirpstack-add-application.png"
  caption="Add ChirpStack application"
  width="100%"
/>

2. Fill in the following fields:
    - **Name**: Enter an application name
    - **Description**: Add a description or tags if needed

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/chirpstack-add-application-details.png"
  caption="Add ChirpStack application details"
  width="100%"
/>

3. Click **Submit** to create the application.

##### Create a Device Profile in ChirpStack v4

Before adding a device in ChirpStack v4, you need to create a **Device Profile**, which defines key configuration parameters for your LoRaWAN device.

The **Device Profile** ensures that ChirpStack correctly interprets how the device communicates with the network.

1. Navigate to **Device Profiles** and click **Add device profile**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/chirpstack-add-device-profile.png"
  caption="Add ChirpStack device profile"
  width="100%"
/>

2. Under the General tab:
- **Name**: Enter a profile name (e.g., US915-OTAA-ClassC)
- **Description**: Add notes if needed (e.g., RAK9105U Remote Reboot Switch)
- **Region**: Select the region matching your gateway (e.g., US915, EU868)
- **MAC version**: Select LoRaWAN 1.0.3
- **Regional parameters revision**: Choose RP002-1.0.3
- **ADR algorithm**: Default ADR algorithm (LoRa only)


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/chirpstack-add-device-profile-details.png"
  caption="Add ChirpStack device profile details"
  width="100%"
/>

3. Under the **Class-C** tab, enable **Device supports Class-C** and click **Submit**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/chirpstack-device-supports-class-c.png"
  caption="ChirpStack device supports class C"
  width="100%"
/>

##### Register the Device in ChirpStack v4

1. Return to the **Applications** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/chirpstack-register-device-in-applications.png"
  caption="Register ChirpStack device in Applications"
  width="100%"
/>

2. Select the application you created and click **Add device**.
3. Fill in the following fields:
- **Name**: Enter a name for your device
- **Description**: (Optional) Add a description to help identify the device
- **Device EUI (EUI64)**: Same as configured on the RAK9105U
- **Join EUI (EUI64)**: Same as configured on the RAK9105U
- **Device profile**: Select the one you just created

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/chirpstack-register-device-details.png"
  caption="Register ChirpStack device details"
  width="100%"
/>


4. In the **OTAA Keys** section. Enter the **Application key** (must match the key configured on the RAK9105U)

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/chirpstack-register-device-otaa-keys.png"
  caption="Register ChirpStack device OTAA keys"
  width="100%"
/>

5. Click **Submit** to complete registration.

When the join is successful, the device will appear in the **ChirpStack UI** with a valid “**Last seen**” timestamp, indicating that the server has received uplink data and the device is ready to receive downlink commands.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/chirpstack-submit-device-registeration.png"
  caption="Submit ChirpStack device registeration"
  width="100%"
/>

### Hardware Installation

Before proceeding with the physical installation of the RAK9105U, it is important to ensure that all network configuration steps have been completed and that the device has successfully joined your LoRaWAN Network Server (LNS).

This approach helps avoid unnecessary redeployment or troubleshooting in the field, especially in remote or elevated locations.

Once the device has been verified to work correctly through USB-based configuration and has appeared in the LNS with a valid join status, you can safely proceed with installation and wiring to the target device.

1. **Connect to Your Target Device**
Use the provided cables to connect your device (e.g., IP camera or LTE router) to one of the following output ports on the RAK9105U:

- **Output 2 (Barrel Jack)** – remotely controllable
- **Output 3 (USB Type-C)** – remotely controllable

2. **Power the RAK9105U**
Connect a 9–24&nbsp;V<sub>DC</sub> power source to the DC input port.
You can use either the included 4-pin terminal block or the standard barrel jack.

Once hardware installation is complete and the device is powered on via DC input, the RAK9105U will operate based on the previously configured LoRaWAN settings.

Since the device has already been registered and verified during initial USB-based setup, no additional network join action is required. The device is now ready for actual deployment and remote control.

### Application Integration

This section will walk you through how to integrate **RAK9105U PowerLink** with **Datacake** using **The Things Stack (TTN v3)**.

#### Set Up Datacake Integration in TTN (Webhook)

1. In the TTN Console, navigate to your application and go to the **Webhooks** section.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/ttn-datacake-integration.png"
  caption="TTN Datacake integration"
  width="100%"
/>

2. Click **+ Add Webhook** and select the **Datacake** template from the list.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/ttn-datacake-add-webhook.png"
  caption="Add Webhook TTN Datacake"
  width="100%"
/>


3. Log in to your **Datacake** account and go to **Members** > **API Users**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/datacake-api-users.png"
  caption="API users on Datacake"
  width="100%"
/>

4. Click **Add API User**, enter a name (e.g., tts-api-user), and configure the necessary permissions.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/datacake-add-api-users.png"
  caption="Add API users on Datacake"
  width="60%"
/>

5. Click **Save** to create the API user, and then click **Copy** to copy the generated **API Token** to your clipboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/datacake-copy-api-token.png"
  caption="Copy API token Datacake"
  width="100%"
/>

6. Go back to the **TTN Console**, enter the following details, and then click **Create Datacake Webhook**.
- **Webhook ID**: For this guide, enter `rak9105u`
- **Token**: Paste the token copied from Datacake

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/ttn-paste-token-from-datacake.png"
  caption="Paste token from Datacake on TTN"
  width="100%"
/>

#### Add the Device to Datacake

1. In Datacake, navigate to **Devices** and click **+ Add Device**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/datacake-add-device.png"
  caption="Add device on Datacake"
  width="100%"
/>

2. Select **LoRaWAN** as the device type and click **Next**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/datacake-lorawan-connectivity.png"
  caption="LoRaWAN connectivity on Datacake"
  width="60%"
/>

3. Choose **New Product**, enter a name for the product (e.g., RAK9105U), then click **Next**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/datacake-add-lorawan-device.png"
  caption="Add LoRaWAN device on Datacake"
  width="60%"
/>

4. Select **The Things Stack V3** as the network server, then click **Next**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/datacake-choose-ttn-lns.png"
  caption="Choose Datacake TTN LNS"
  width="60%"
/>

5. Enter the following information and click **Next**.
- **DEVEUI**: Must match the value configured in TTN
- **NAME**: Enter a custom name for your device

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/datacake-add-device-info.png"
  caption="Add device info on Datacake"
  width="60%"
/>

6. Choose a subscription plan (e.g., **Free**) and click **Add 1 Device** to complete the setup.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/datacake-choose-subscription.png"
  caption="Choose Datacake subscription"
  width="60%"
/>


#### Configure Payload Decoder

1. Open your device in **Datacake**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/datacake-configure-payload-decoder.png"
  caption="Configure Datacake payload decoder"
  width="100%"
/>

2. Navigate to the **Configuration** tab and scroll down to the **Payload Decoder** section.
3. Paste the provided JavaScript decoder into the editor and click **Save** to apply the decoder and activate data parsing.

<details>
<summary>Click to view the code</summary>

```js
function Decoder(bytes, port) {
var decoded = {};
var str = bin2HexStr(bytes);

switch (port) {
  case 1:
    var outputStatus = parseOutputStatus(bytes[0]); // Power output status
    decoded.output5V = outputStatus.output5V;
    decoded.output12V = outputStatus.output12V;
    decoded.swversion = parseSWVersion(bytes[1]); // Software version
  break;

  case 2:
    decoded.curvoltage = parseCurVoltage(bytes[0]) + ' V'; // Current voltage
    decoded.curcurrent = parseCurCurrent(bytes[2]) + ' A'; // Current
    decoded.cycletimes = bytes[4] + ' cycles'; // Cycle times
    decoded.remaincapacity = Math.floor(parseRemainCapacity(bytes.slice(6, 8))) + ' mAh'; // Remaining capacity
    decoded.cursoc = parseCurSOC(bytes[8]) + ' %'; // Current state of charge
  break;

  case 3:
    decoded.fullcapacity = Math.floor(parseFullCapacity((bytes[0] << 8) | bytes[1])) + ' mAh'; // Full capacity
    decoded.custfaultstatush = parseFaultStatusHigh(bytes[2], bytes[3]); // High fault status
    decoded.custfaultstatusl = parseFaultStatusLow(bytes[4], bytes[5]); // Low fault status
    decoded.custwarnstatush = parseWarningStatusHigh(bytes[6], bytes[7]); // High warning status
    decoded.batterymode = parseBatteryMode(bytes[8]); // Battery mode
  break;

  case 4:
    decoded.avgtemp = bytes[0] + ' °C'; // Average temperature
    decoded.maxtemp = bytes[1] + ' °C'; // Maximum temperature
    decoded.mintemp = bytes[2] + ' °C'; // Minimum temperature
    decoded.cursoh = bytes[3] + ' %'; // Current state of health
    var batteryStatus = parseBatteryStatus(bytes[4]); // Battery status
    decoded.chargeMos = batteryStatus.chargeMos;
    decoded.dischargeMos = batteryStatus.dischargeMos;
    decoded.fullyCharged = batteryStatus.fullyCharged;
    decoded.outputstatus = parseOutputStatus(bytes[5]); // Output status
    decoded.swversion = parseSWVersion(bytes[6]); // Software version
    decoded.bmsbootversion = parseBMSBootVersion(bytes[7], bytes[8]); // BMS Boot version
  break;

  default:
    decoded.result = "Port not recognized"; // Handle unknown ports
  break;
}

// Get LoRaWAN metadata
  try {
    decoded.lorawanrssi = (port && port.metadata && port.metadata.rssi) || 0;
    decoded.lorawansnr = (port && port.metadata && port.metadata.snr) || 0;
    decoded.lorawandatarate = (port && port.metadata && port.metadata.datarate) || '';
  } catch (e) {
    console.log('Failed to read gateway metadata');
  }

return decoded;
}

  function bin2HexStr(bytesArr) {
    var str = '';
      for (var i = 0; i < bytesArr.length; i++) {
    var tmp = (bytesArr[i] & 0xff).toString(16);
      if (tmp.length === 1) {
      tmp = '0' + tmp;
    }
      str += tmp;
    }
    return str;
  }

  function parseShort(str, base) {
    var n = parseInt(str, base);
    return (n << 16) >> 16;
  }

  // Helper functions
  function parseOutputStatus(byte) {
    var statusBits = manualPadStart(byte.toString(2), 8, '0'); // Convert byte to binary string
    return {
      output5V: statusBits[7] === '1' ? "True" : "False", // Control 5V output
      output12V: statusBits[6] === '1' ? "True" : "False" // Control 12V output
    };
  }

  function parseSWVersion(byte) {
    var majorVersion = Math.floor(byte / 100); // Calculate major version
    var minorVersion = Math.floor((byte % 100) / 10); // Calculate minor version
    var patchVersion = byte % 10; // Calculate patch version
  return majorVersion + '.' + minorVersion + '.' + patchVersion; // Format as x.y.z
  }

  function parseCurVoltage(byte) {
  return (byte * 0.01).toFixed(2); // Convert U8 to voltage (0.01 V)
  }

  function parseCurCurrent(byte) {
    var current = (byte & 0xFF) - 256; // Handle signed values
  return (current * 0.01).toFixed(2); // Convert U8 to current (0.01 A)
  }

  function parseRemainCapacity(bytes) {
   var capacity = bytesToInt(bytes);
  return (capacity * 10).toFixed(2); // Convert U16 to mAh
  }

  function parseCurSOC(byte) {
  return byte; // Direct percentage
  }

  function parseFullCapacity(byte) {
  return (byte * 10).toFixed(2); // Full capacity in mAh
  }

  function parseFaultStatusHigh(highByte, lowByte) {
    if (highByte === 0 && lowByte === 0) {
    return "Normal"; // Return Normal if both are 0
    }
  return "Fault"; // Return fault otherwise
  }

  function parseFaultStatusLow(lowByte) {
    if (lowByte === 0) {
    return "Normal"; // Return Normal if lowByte is 0
    }
  return "Fault"; // Return fault otherwise
  }

  function parseWarningStatusHigh(highByte, lowByte) {
    if (highByte === 0 && lowByte === 0) {
    return "Normal"; // Return Normal if both are 0
    }
  return "Fault"; // Return fault otherwise
  }

  function parseBatteryMode(byte) {
    var modes = {
    0: "Null",
    1: "Charging",
    2: "Discharging",
    3: "Fully Charged",
    4: "Fully Discharged",
    5: "Protect",
    6: "Permanent Fail",
    7: "Null",
    };
  return modes[byte] || "Unknown"; // Return mode or Unknown
  }

  function parseBatteryStatus(byte) {
    var statusBits = manualPadStart(byte.toString(2), 8, '0'); // Fill with leading zeros
      return {
        chargeMos: statusBits[7] === '0' ? "On" : "Off", // Charge MOS state
        dischargeMos: statusBits[6] === '0' ? "On" : "Off", // Discharge MOS state
        fullyCharged: statusBits[4] === '1' ? "Full" : "Normal" // Full charge status
      };
  }

  function parseBMSBootVersion(bootMajorByte, bootMinorByte) {
    var majorVersion = bootMajorByte; // Use the input major version byte
    var minorVersion = Math.floor(bootMinorByte / 10); // Calculate minor version
    var patchVersion = bootMinorByte % 10; // Calculate patch version
  return majorVersion + '.' + minorVersion + '.' + patchVersion; // Format as x.y.z
  }

  function bytesToInt(bytes) {
    var result = 0;
     for (var i = 0; i < bytes.length; i++) {
        result = (result << 8) | bytes[i];
       }
  // Handle signed integers if needed
    var byteLength = bytes.length;
     if (result >= Math.pow(2, byteLength * 8 - 1)) {
        result -= Math.pow(2, byteLength * 8); // Convert to negative
      }
  return result;
  }

  // Manual padStart implementation
  function manualPadStart(str, targetLength, padString) {
    str = String(str);
      while (str.length < targetLength) {
        str = padString + str;
      }
    return str;
}

```
</details>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/datacake-paste-javascript-decoder.png"
  caption="Paste Datacake Javascript decoder"
  width="100%"
/>


#### Create a Configuration Field

1. Navigate to the **Configuration** tab and scroll down to the **Fields** section.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/datacake-fields-section.png"
  caption="Fields section on Datacake"
  width="100%"
/>

2. Click **+ Add Field** and define the field schema:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/datacake-add-field.png"
  caption="Add field on Datacake"
  width="60%"
/>

3. Repeat this process to add all required fields that correspond to your decoder output.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/datacake-add-all-field.png"
  caption="Add all field on Datacake"
  width="100%"
/>


#### Enable Downlink Control

To control outputs remotely via LoRaWAN downlinks, configure your TTN connection in the Downlink Configuration section.

1. In the **Configuration** tab, scroll to **Downlink Configuration** and click **Change**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/downlink-configuration.png"
  caption="Downlink configuration"
  width="100%"
/>

2. Fill in the following fields:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/downlink-fields.png"
  caption="Downlink details"
  width="60%"
/>

- **TTS Device ID**: Found in **TTN** > **Device overview** > **End device ID**

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/downlink-tts-device-id.png"
  caption="Downlink TTS device ID"
  width="100%"
/>

- **TTI Server URL**: e.g., *eu1.cloud.thethings.network*
- **TTI App ID**: Found in **TTN** > **Application overview** > **ID**

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/downlink-tti-app-id.png"
  caption="Downlink TTI app ID"
  width="100%"
/>

- **TTI API Key**: See instructions below to create one.

  - In the **TTN Console**, navigate to the application’s **API keys** tab.

    <RkImage
      src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/ttn-console-api-keys-tab.png"
      width="100%"
      caption="TTN Console API keys tab"
    />

  - Click **+ Add API key**. Set a name and enable permission to write downlink messages

    <RkImage
      src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/tti-add-api-keys.png"
      caption="TTI add API keys"
      width="100%"
    />

  - Click **Create API key**.

    <RkImage
      src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/tti-create-api-keys.png"
      caption="TTI create API keys"
      width="60%"
    />

   - Copy the generated key immediately (it will only be shown once).
   - Paste the key into the **TTI API key** field in Datacake.

3. Click **Update** to save the configuration.


#### Send Downlinks

This section explains how to configure and send **LoRaWAN downlink commands** from **Datacake** to the RAK9105U device, enabling remote control of power outputs via TTN.

1. Open your device in Datacake and navigate to the **Downlinks** tab using the top navigation bar.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/downlink-tab.png"
  caption="Downlink tab"
  width="100%"
/>

2. Click **+ Add Downlink**, then fill in the downlink details:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/downlink-details.png"
  caption="Downlink details 1"
  width="60%"
/>

- **Name**: Enter a descriptive name for the downlink (e.g., "DeviceA-on")
- **Description**: Optionally, add information about what the command does
- **Port**: Specify the LoRaWAN port (FPort) the command will use
- **Payload Encoder**: Input the payload encoding logic in JavaScript. For example, to turn on Output 3 (5&nbsp;V).

```js

function Encoder(measurements, port) {
    // Return a byte array here
    return [0x00, 0x01];
}
```

**Command Reference**:

| Hex Payload | Description            |
|-------------|------------------------|
| 0000        | 5&nbsp;V Output 3 OFF  |
| 0001        | 5&nbsp;V Output 3 ON   |
| 0100        | 12&nbsp;V Output 2 OFF |
| 0101        | 12&nbsp;V Output 2 ON  |

3. Repeat the above steps to add other downlink commands as needed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/downlink-add-other-dl-commands.png"
  caption="Add other Downlink commands"
  width="100%"
/>


4. On the **Downlink** list, find the command and click **Configure and send downlink**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/configure-and-send-downlink.png"
  caption="Configure and send downlink"
  width="100%"
/>

5. Click **Save measurements and send downlink** to queue the command.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/save-measurements-and-send-downlink.png"
  caption="Save measurements and send downlink"
  width="60%"
/>

6. After sending, a green message will appear confirming: **The downlink was queued successfully**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/downlink-queued-successfully.png"
  caption="Downlink queued successfully"
  width="100%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/downlink-data-preview.png"
  caption="Downlink data preview"
  width="100%"
/>

:::tip NOTE

The status of the device shown in the dashboard is based on **uplink reports**.
After sending a downlink, the actual device state (e.g., Output On/Off) will be updated only when the next **uplink payload** is received.
:::

#### Build Your Dashboard

Follow these steps to visualize your device data using widgets in the Datacake dashboard:

1. In Datacake, open your device and navigate to the **Dashboard** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/dashboard-datacake.png"
  caption="Datacake dashboard"
  width="100%"
/>

2. Click **Edit Mode** icon, then select **+ Add Widget**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/dashboard-add-widget.png"
  caption="Dashboard widget"
  width="100%"
/>

3. Choose a widget type based on the data you want to display.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/dashboard-choose-widget-type.png"
  caption="Choose dashboard widget type"
  width="60%"
/>

4. Configure the widget:
- **Title**: Set a clear title (e.g., "Device A").

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/dashboard-widget-title.png"
  caption="Dashboard widget title"
  width="60%"
/>

- **Data**: Select the corresponding field (e.g., output5V).

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/dashboard-data.png"
  caption="Dashboard data"
  width="60%"
/>

- **Appearance**: Customize color, units, size, and any display logic.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/dashboard-appearance.png"
  caption="Dashboard appearance"
  width="60%"
/>

5. Repeat the above steps for each field you want to **monitor** (e.g., Device A status). Additionally, you can add **control buttons** to send downlink commands directly from the dashboard, such as **Power on Device A**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/quickstart/dashboard-add-other-widget.png"
  caption="Add other dashboard widget"
  width="100%"
/>

6. Once set up, you can remotely control the 12&nbsp;V and 5&nbsp;V outputs of the RAK9105U through Datacake, enabling real-time reboot or power management of connected devices.


<RkBottomNav/>