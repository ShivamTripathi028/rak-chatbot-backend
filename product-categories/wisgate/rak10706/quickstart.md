---
slug: /product-categories/wisgate/rak10706/quickstart/
title: RAK10706 Field Tester for LoRa Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK10706 Signal Meter for LoRa. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: https://images.docs.rakwireless.com/wisnode/rak10706/rak10706.png
keywords:
    - lorawan
    - lora p2p
    - signal meter
    - rak10706
    - wisnode
    - coverage tester
sidebar_label: Quick Start Guide
download: true
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK10706 Signal Meter for LoRa Quick Start Guide

## Prerequisites

Before going through each and every step in the installation guide of the RAK10706 Signal Meter for LoRa, make sure to prepare the necessary items listed below:

### Hardware Tools

- <a href="https://store.rakwireless.com/products/signal-meter-for-lora?utm_source=RAK10706&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAK10706 Signal Meter for LoRa</a>
- LoRa SubGHz Antenna with RP-SMA connector
- USB Type-C Cable
- PC (Windows/Linux/macOS) or mobile (iOS/Android)

### Software Tools

Serial Terminal Application, for example <a href="https://freeware.the-meiers.org/" target="_blank"> Cool Term </a> for configuration.
<a href="https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/overview" target="_blank"> WisToolBox </a> for configuration and firmware update.

:::tip NOTE
- For LoRaWAN test mode, the device must be registered with an LNS and within range of a LoRaWAN gateway on the network you are attempting to join. Without coverage, the Signal Meter will not function.
- For LoRa P2P test mode, it is mandatory that other LoRa P2P end nodes are available and configured with the same frequency, SF, CR, BW, and Preamble Length.
:::

## Difference Between the RAK10706 Signal Meter and the RAK10701 Field Tester

One of the advantages of the RAK10706 Signal Meter is that there is no backend installations required on LoRaWAN servers (e.g., Helium, TTN, Chirpstack) in LinkCheck Packet mode. It works with any LoRaWAN server, such as AWS IoT Core or Actility.

The RAK10706 uses LinkCheckReq to gather information about the connection to the gateway(s). This helps monitor connectivity. With LinkCheck, the LoRaWAN server reports the number of gateways and the demodulation margin. The demodulation margin is calculated by the LoRaWAN server. It provides insights into the received signal quality. A higher margin indicates better signal quality.<br/>
Extract from the LoRaWAN 1.0.3 Specification:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/lorawan-linkcheck.png"
  width="80%"
  caption="LinkCheck explanation"
/>

## Typical Test Scenarios

In all scenarios, tests can be performed in three ways:

- **Automatic sending in a specified interval**: The interval can be set either through the built-in UI or with an AT command.
- **Forced sending**: Push the button three (3) times trigger transmission of a single packet using the pre-defined settings.
- **Forced sending with DR sweep (only in LoRaWAN test modes)**: Push the button four (4) times to trigger transmission of multiple packets. The sending starts at the lowest possible data rate and increases each packet until the highest possible data rate is reached.

### Outdoor Testing

In this scenario, location tracking should be enabled to include the tester's location in the test results. The log files will contain the location of the tester at the time the test was performed. If no location is found, the location will be set to Lat 0, Long 0.

### Indoor Testing

In this scenario the location tracking should be disabled, as the GNSS chip cannot acquire a valid location inside buildings. The log files will not contain the location of the tester.

### LinkCheck Testing

If it is not possible to connect the backend server to the LoRaWAN server to process the received packet data, the LinkCheck method is used. It provides basic information about connection quality and indicates whether the tester is within the coverage range of gateways.

### LoRa P2P Testing
This is a very basic test that only shows whether the device is in range from another LoRa P2P device that is sending out packets. In this mode, the device is listening and displaying information if it has received a data packet. It will as well send out data packets in the send interval that is setup on the device.

## Product Configuration

### RAK10706 Signal Meter Physical Interface

The user interface of the RAK10706 Signal Meter for LoRa is via OLED display and one pushbutton at the side. There is also an external LoRA antenna port via RP-SMA connector and USB-C port for charging and configuration if connected to a PC.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/physical-interface.png"
  width="40%"
  caption="RAK10706 view"
/>

:::tip NOTE
You have to ensure that the LoRa antenna is attached before turning the device on.
:::

1. To turn on the device, move the switch to the **ON** position (**ON** is marked with a circle above the switch).

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/power-switch.png"
  width="40%"
  caption="RAK10706 switch to turn on and off"
/>

2. When the device initializes, it will show the initialization info on the screen.

:::tip NOTE
If there is any initialization error, it will be shown. A properly working device should not have any errors shown.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/rak10706_boot.png"
  width="35%"
  caption="RAK10706 power up"
/>

3. After the successful boot-up, the main home screen will be shown. Take note, that there will be no data at the first start of the device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/rak10706_home.png"
  width="35%"
  caption="RAK10706 power up successful"
/>

:::tip NOTE
By default, the Signal Meter is in LoRaWAN LinkCheck test mode. Follow the steps below to register the device on a LoRaWAN server.
:::

### LoRaWAN Network Servers Guide for RAK10706 Signal Meter for LoRa

The Signal Meter is compatible with any network server. By default, the device operates in LoRaWAN mode with OTAA join. The following steps outline how to use OTAA join mode.

#### Device Configuration of RAK10706 via WisToolBox

1. Start by connecting the device to a Serial Terminal app (e.g., CoolTerm) or WisToolBox via the USB cable.

:::tip NOTE
With WisToolBox connected, it will show the device as a RAK4630 module.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/wistoolbox-connect.png"
  width="100%"
  caption="RAK10706 on WisToolBox"
/>

2. Go to **Parameters** to retrieve the LoRaWAN credentials from **LoRaWAN keys, ID, EUI** dropdown.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/wistoolbox-credentials.png"
  width="100%"
  caption="RAK10706 on WisToolBox"
/>

3. Take note of the Application EUI, Application Key, and Device EUI. These are later required for registering the device on a LoRaWAN server.

4. Open the **Global Settings** dropdown and set the LoRaWAN region you want to use with the device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/wistoolbox-region.png"
  width="100%"
  caption="RAK10706 on WisToolBox"
/>

#### Device Configuration of RAK10706 via Serial Terminal Application

When using a Serial Terminal application like CoolTerm, connect the terminal to the device. Serial parameters are 115200 Baud 8N1.

1. Send the command `AT+BAND?` to get a list of available LoRaWAN regions.

2. Set the LoRaWAN region with `AT+BAND=10` (example for AS923-3).

3. Send the command `ATC+STATUS=?` to get the **DevEUI**, **AppEUI** and **AppKey** for later use.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/coolterm-credentials.png"
  width="100%"
  caption="RAK10706 on Serial Terminal Application"
/>

#### LoRaWAN Server Configuration for RAK10706 Signal Meter

You can check each guide on how to use the RAK10706 Signal Meter for LoRa in the following network servers.

- [The Things Network](#rak10706-signal-meter-guide-for-the-things-network)
- [Chirpstack](#rak10706-signal-meter-guide-for-chirpstack)
- [Loriot](#rak10706-signal-meter-guide-for-loriot)



:::tip NOTE
- For other network servers the procedure is very similar.
- This section will focus on the configuration of each network server. The procedure of [Device Configuration of RAK10706 via WisToolBox](#configuration-of-rak10706-using-wistoolbox) is the same for all network server and will be covered in a separate section of the guide.
:::

#### RAK10706 Signal Meter Guide for The Things Network

This section shows how to use the RAK10706 Signal Meter for LoRa with The Things Stack.

1. Log in to TTNv3 by visiting the TTNv3 [site](https://console.cloud.thethings.network/) and selecting your cluster. If you already have a TTN account, you can use your The Things ID credentials to log in.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/image001.png"
  width="100%"
  caption="The Things Stack home page"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/image002.png"
  width="100%"
  caption="Console page after a successful login"
/>


:::tip NOTE
To connect RAK10706 Signal Meter to TTNv3, you should already have connected a gateway in range to TTNv3. Or, you have to be sure that you are in the range of a public gateway.
:::


2. After logging in to the platform, create an application by clicking **Create an application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/rak4631-ttnv3-1.png"
  width="100%"
  caption="Create an application"
/>

3. To register an application, input specific details and necessary information about your application, and then click **Create application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/rak4631-ttnv3-2.png"
  width="100%"
  caption="Creating an Application"
/>

:::tip NOTE
If you had no error during the previous step, you should now be on the application console page.
:::

4. Next is to add end-devices to your TTN application, then click **+Add end device**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/rak4631-ttnv3-3.png"
  width="100%"
  caption="Add end-devices to your TTN application"
/>

5. Register the RAK10706 Signal Meter by clicking the **Manually** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/rak4631-ttnv3-4.png"
  width="100%"
  caption="Adding end devices manually"
/>

6. Choose the following configurations in adding the end devices. You must choose the correct Frequency Plan, and the LoRaWAN version must be 1.0.3.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/rak4631-ttnv3-5.png"
  width="100%"
  caption="Configurations for adding end devices"
/>

7. Click **Show advanced activation, LoRaWAN class, and cluster settings**, then select **Over the air action (OTAA)**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/rak4631-ttnv3-6.png"
  width="100%"
  caption="OTAA settings"
/>

8. Then input the LoRaWAN OTAA parameters you retrieved before from the device. Finally, click **Register End Device**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/rak4631-ttnv3-7.png"
  width="100%"
  caption="Registering the end device"
/>

9. You should now be able to see the device on the TTN console after you fully register your device.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/rak4631-ttnv3-8.png"
  width="100%"
  caption="OTAA device successfully registered to TTN"
/>

10. After adding the application and device, you should see the join request/accept, uplinks, and downlinks in The Things Stack console.

#### RAK10706 Signal Meter Guide for Chirpstack

To use Chirpstack for RAK10706, you must have a working installation of the Chirpstack LoRaWAN network server. It can be on a dedicated machine such as **Raspberry Pi**, or in a cloud VPS instance.

1. To start with Chirpstack, you must create a device profile for your RAK10706 Signal Meter device. Select **LoRaWAN MAC version 1.0.4**, the version supported by the RAK10706 Signal Meter.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/3_device_profile.png"
  width="95%"
  caption="Creating Device Profile in Chirpstack"
/>

2. Next, go to the **JOIN (OTAA / ABP)** tab, and enable **Device supports OTAA**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/4_device_profile.png"
  width="95%"
  caption="Enable support for OTAA"
/>

3. After creating the device profile, you can now create an application and add the RAK10706 device. And then attached the `Device-profile` you created. Use the DevEUI and AppEUI you have retrieved from the RAK10706 before.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/6_create_application.png"
  width="95%"
  caption="Create application in Chirpstack"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/7_create_device.png"
  width="95%"
  caption="Create device in Chirpstack."
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/8_create_device_appkey.png"
  width="95%"
  caption="Device APPKEY"
/>

5. You also need to secure that you have a Gateway registered in Chirpstack and with the correct Network Server profile.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/9_gateway.png"
  width="95%"
  caption="Gateways registered in Chripstack"
/>

#### RAK10706 Signal Meter Guide for LORIOT

This section provides a step-by-step guide for performing a field mapping test using LORIOT network management system and Datacake's platform to visualize your results. This solution supports network planning, ensuring data-driven decisions tailored to your specific environment.

##### Prerequisites

- [RAK10706 Signal Meter for LoRa](https://store.rakwireless.com/products/signal-meter-for-lora?variant=42437595726022)
- [LORIOT Account](https://www.loriot.io/login.html)
- Gateway

##### Setting LORIOT as the LNS

1. Forward a gateway to LORIOT, which will be the LNS (LoRa Network Server) for this use case. To register the gateway to LORIOT, you will need the gateway’s MAC and EUI, which can be found on the [WisGateOS 2 Overview page](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/).

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/1. wisgate edges web ui.png"
width="100%"
caption="WisGate Edges web UI"
/>

2. Go to your LORIOT profile. From the menu on the left, navigate through **Networks** > **your_network** > **+Add Gateway**.

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/2. loriot console.png"
width="100%"
caption="LORIOT console"
/>

:::tip NOTE
The LORIOT platform provides you with a **Sample Network** at the point of your profile creation. You can use it for free. If you wish to create a new one, or delete the provided one, you will need a paid plan to continue.
:::

3. For the base platform, select **Basics Station Semtech**. You will be asked to provide eth0 MAC address and EUI, which you obtained in **step 1**. After filling in these values, press the **Register Basics Station Semtech gateway** at the bottom of the page.

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/3. registering the gateway to loriot.png"
width="100%"
caption="Registering The Gateway To LORIOT"
/>

4. The last thing you need to do to connect your gateway with LORIOT LNS is to provide the Basics Station configuration to the gateway. Navigate to **LoRa** > **Configuration**, click **Basics station**, and then complete the **Basic Station server setup**.

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/4. gateway configuration page.png"
width="100%"
caption="Gateway Configuration Page"
/>

You can find the Trust (CA Certificate), Server URL, and Server port in LORIOT under the **Gateway** > **Certificate**. Use the configuration provided by LORIOT, as it may differ based on your region.

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/5. certificate.png"
width="100%"
caption="Certificate"
/>

:::tip NOTE
If the steps are followed correctly, the gateway should show a **Connected** status.
:::


##### Adding the Device to LORIOT

1. Add the device to LORIOT. In the LORIOT platform, navigate to **Applications** > **your_application** and use the **Enroll Device** utility from the menu on the left. Fill out your Device EUI, Join (APP) EUI, and Application Key.

<RkImage
src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/6. adding the device to the loriot platform.png"
width="100%"
caption="Adding The Device To The LORIOT Platform"
/>

:::tip NOTE
The LORIOT platform provides you with a **Sample Application** at the point of your profile creation. You can use it for free. If you wish to create a new one or delete the provided one, you will need a paid plan to continue.
:::

### RAK10706 Signal Meter Built-In UI

#### RAK10706 Button Functions

The button on the side of the RAK10706 has different functions, depending on the status of the device.

- <b>Inactive UI Settings</b>

Generic function of the button if the Settings UI is not active

<table>
  <tbody>
    <tr>
      <td>Long Press</td>
      <td>switch off / on the display for power savings</td>
    </tr>
    <tr>
      <td>Single click</td>
      <td>no function</td>
    </tr>
    <tr>
      <td>Double click</td>
      <td>enter the Settings UI (stops the testing mode, no more test packets are sent and received packets are ignored)</td>
    </tr>
    <tr>
      <td>3 clicks</td>
      <td>Force a downlink packet to be sent</td>
    </tr>
    <tr>
      <td>4 clicks</td>
      <td>Force multiple downlink packets with DR sweep. Sending starts with the lowest possible data rate and increases the data rate with each packet until the highest possible data rate has been reached.</td>
    </tr>
    <tr>
      <td>5 clicks</td>
      <td>no function (to avoid accidental reset of device)</td>
    </tr>
    <tr>
      <td>6 clicks</td>
      <td>Reset the device</td>
    </tr>
    <tr>
      <td>7 clicks</td>
      <td>Enter Bootloader Mode for firmware upgrades</td>
    </tr>
  </tbody>
</table>

- <b>Active UI Settings</b>

When the UI is active, the button change to different functions.

<table>
  <tbody>
    <tr>
      <td>Single click</td>
      <td>go up one level in the UI. If the top level is reached, the UI will be closed, and if required, changes are saved on the device.</td>
      <td></td>
    </tr>
    <tr>
      <td>Double click</td>
      <td>change or select the second menu item.</td>
      <td>select the next item from a list of options</td>
    </tr>
    <tr>
      <td>3 clicks</td>
      <td>change or select the third menu item.</td>
      <td>select the previous item from a list of options</td>
    </tr>
    <tr>
      <td>4 clicks</td>
      <td>change or select the forth menu item.</td>
      <td></td>
    </tr>
    <tr>
      <td>5 clicks</td>
      <td>change or select the fifth menu item.</td>
      <td></td>
    </tr>
    <tr>
      <td>6 clicks</td>
      <td>change or select the sixth menu item.</td>
      <td></td>
    </tr>
    <tr>
      <td>7 clicks</td>
      <td>change or select the seventh menu item.</td>
      <td></td>
    </tr>
  </tbody>
</table>

#### Change Settings On-the-Fly

Double-clicking the button opens the settings UI, allowing you to change settings without connecting the PC via USB.

- The button function in the Settings UI changes based on the settings level. A single click moves up one level.
- For other items, the number before an item indicates the clicks required to activate that level.
- If a level has selectable items, the selected item is marked with _**`==>`**_ instead of its number.
- If a level has items than can be toggled on/off, its status is shown after the item name.

Overview of all settings levels:

##### Top Level

- (2) Get the test settings info (mode, send interval, location status, display saver status)
- (3) Change the device settings (Change send interval, enable/disable location, enable/disable display saver)
- (4) Change test mode (LoRaWAN, LoRa P2P, Field Tester and Field Tester V2)
- (5) Change LoRa P2P or LoRaWAN settings

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/ui-top.png"
  width="25%"
  caption="Top Level"
/>

:::tip NOTE
The device may reset when leaving the settings if the test mode has been changed.
:::

##### Test Settings Info

- Current test settings

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/ui-top-info.png"
  width="25%"
  caption="Current test settings"
/>

##### Device Settings

- (2) Change send interval
- (3) Enable/Disable location tracking (toggle)
  - Location On keeps the GNSS module powered for faster location acquisition (resulting in faster battery drain).
- (4) Enable/Disable display saver (toggle)
  - Display Saver On turns off the display after 1 minute. The display can be reactivated with a single button click.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/ui-dev-setting-top.png"
  width="25%"
  caption="Device settings"
/>


###### Send Interval

- (2) 10 seconds more
- (3) 10 seconds less

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/ui-dev-setting-interval.png"
  width="25%"
  caption="Send interval"
/>

##### Test Mode

- (2) LinkCheck test mode (no back-end required)
- (3) LoRa P2P test mode
- (4) Field Tester compatible test mode. Has limited functionality and requires back-end. For details, see [RAK10701 Field Tester Quick Start Guide](https://docs.rakwireless.com/product-categories/wisgate/rak10701-l/quickstart/).
- (5) Field Tester Plus compatible test mode. Has limited functionality and requires back-end. For details, see [RAK10701 Field Tester Plus Quick Start Guide](https://docs.rakwireless.com/product-categories/wisgate/rak10701-plus/quickstart/).

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/ui-mode-top.png"
  width="25%"
  caption="Test Mode"
/>

##### LoRaWAN Setting for LoRaWAN Test Modes

- (2) Enable/Disable ADR
- (3) Change ADR
- (4) Change TX power
- (5) Change LoRaWAN region

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/ui-lorawan-top.png"
  width="25%"
  caption="LoRaWAN settings"
/>

###### ADR

- (2) ADR on/off (toggle)

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/ui-lorawan-adr.png"
  width="25%"
  caption="ADR settings"
/>

###### DR

- (2) Select next higher data rate
- (3) Select next lower data rate

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/ui-lorawan-dr.png"
  width="25%"
  caption="DR settings"
/>

###### TX

- (2) Select next lower TX power
- (3) Select next higher TX power

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/ui-lorawan-tx.png"
  width="25%"
  caption="DR settings"
/>

###### Region

- (2) Select next region
- (3) Select previous

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/ui-lorawan-region.png"
  width="25%"
  caption="LoRaWAN region selection"
/>

##### LoRa P2P Setting for LoRa P2P Test Modes

- (2) Change send frequency
- (3) Change spreading factor
- (4) Change bandwidth
- (5) Change coding rate
- (6) Change TX power

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/ui-lora-top.png"
  width="25%"
  caption="LoRa P2P settings"
/>

###### Send Frequency

- (2) 0.1&nbsp;MHz up
- (3) 0.1&nbsp;MHz down

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/ui-lora-freq.png"
  width="25%"
  caption="Send frequency"
/>

###### Spreading Factor
- (2) Select next higher SF
- (3) Select next lower SF

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/ui-lora-sf.png"
  width="25%"
  caption="SF settings"
/>

###### Bandwidth
- (2) Select next higher BW
- (3) Select next lower BW

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/ui-lora-bw.png"
  width="25%"
  caption="BW settings"
/>

###### Coding Rate
- (2) Select next higher CR
- (3) Select next lower CR

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/ui-lora-cr.png"
  width="25%"
  caption="CR settings"
/>

###### TX Power
- (2) Select next higher TX power
- (3) Select next lower TX power

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/ui-lora-tx.png"
  width="25%"
  caption="TX power settings"
/>

### Custom AT Commands

The RAK10706 application includes multiple custom AT commands:

- `ATC+SENDINT` to set the send interval time or heart beat time. The device will send a payload with this interval. The time is set in seconds, e.g. `AT+SENDINT=600` sets the send interval to 600 seconds or 10 minutes.
- `ATC+MODE` to set the test mode. 0 using LPWAN LinkCheck, 1 using LoRa P2P, 2 using FieldTester protocol, 3 using FieldTester PLUS protocol.
- `ATC+STATUS` to get status information from the device.
- `ATC+PCKG` to setup a custom payload that is used in the uplink packets (only Linkcheck test mode and LoRa P2P test mode).
- `ATC+LOGS` to retrieve or erase saved log files from the SD card (if SD card is present). See [AT commands for log files](#at-commands-for-log-files).
- `ATC+RTC` to set or get time of RTC (if RTC module is present). Set format = [yyyy:mm:dd:hh:MM] (discard leading zeros)

### Setup with AT Commands

#### LoRa P2P Setup

To use the device in LoRa P2P mode, it has to be set into this mode with:
```
AT+NWM=0
```
The device might reboot after this command, if it was not already in P2P mode.

Next, the LoRa P2P parameters need to be set up. In this example, the device is being set to the following:

<table>
  <tbody>
    <tr>
      <td>Frequency</td>
      <td>916100000&nbsp;Hz</td>
    </tr>
    <tr>
      <td>Bandwidth</td>
      <td>125&nbsp;kHz</td>
    </tr>
    <tr>
      <td>Spreading Factor</td>
      <td>7</td>
    </tr>
    <tr>
      <td>Coding Rate</td>
      <td>45387</td>
    </tr>
    <tr>
      <td>Preamble Length</td>
      <td>8</td>
    </tr>
    <tr>
      <td>TX power</td>
      <td>5&nbsp;dBm</td>
    </tr>
  </tbody>
</table>


```
AT+PRECV=0
AT+P2P=916000000:7:0:1:8:5
ATC+MODE=2
```
:::tip NOTE
If the credentials were set already (they are saved in the flash of the device), the switch to P2P testing can as well be done with:
`ATC+MODE=2`

The device might reboot after this command, if it was not already in LoRa P2P mode.

The command AT+PRECV=0 is required to stop the device from listening. While in RX mode, parameters cannot be changed.
:::

To be able to receive packets from other devices, they have to be setup to exactly the same parameters.

#### LoRaWAN LinkCheck Setup

To use the device in LoRaWAN mode, it has to be set into this mode with:
```
AT+NWM=1
```
The device might reboot after this command, if it was not already in LoRaWAN mode.
Then the LoRaWAN parameters and credentials have to be setup. In this example, I am setting the device to AS923-3, OTAA join mode, unconfirmed packet mode, enable link check and then reset the device to perform a LoRaWAN JOIN sequence:
```
AT+BAND=10
AT+NJM=1
AT+CFM=0
AT+LINKCHECK=2
AT+DEVEUI=AC1F09FFFE000000
AT+APPEUI=AC1F09FFFE000000
AT+APPKEY=AC1F09FFFE000000AC1F09FFFE000000
ATC+MODE=0
ATZ
```

:::tip NOTE
- If the credentials have already been set (they are saved in the device's flash), the switch to LinkCheck testing can also be performed with:
`ATC+MODE=0`
  - The device might reboot after this command, if it was not already in LoRaWAN mode.

- The device must be registered with a LoRaWAN server using these credentials, and a gateway within range must be connected to the server. Otherwise, the device cannot join the network, and no tests can be performed. If the device fails to join, an error will be displayed on the screen: **LoRaWAN Join Failed**
  - In this case, double check all settings on the device and LoRaWAN server, and check if a gateway is in range and connected to the LoRaWAN server.
:::

#### LoRaWAN FieldTester & FieldTester Pro Setup

:::tip NOTE
These test modes do not offer the complete functionality of the RAK10701-L and RAK10701-PLUS Field Testers.
:::

To use the device in LoRaWAN mode, it has to be set into this mode with
```
AT+NWM=1
```
The device might reboot after this command, if it was not already in LoRaWAN mode.
Then the LoRaWAN parameters and credentials have to be setup. In this example, I am setting the device to AS923-3, OTAA join mode, confirmed packet mode, disable link check and then reset the device to perform a LoRaWAN JOIN sequence:
```
AT+BAND=10
AT+NJM=1
AT+CFM=1
AT+LINKCHECK=0
AT+DEVEUI=AC1F09FFFE000000
AT+APPEUI=AC1F09FFFE000000
AT+APPKEY=AC1F09FFFE000000AC1F09FFFE000000
ATC+MODE=3
ATZ
```

:::tip NOTE
- If the credentials have already been set (they are saved in the device's flash), the switch to FieldTester testing can also be performed with:
`ATC+MODE=3`
  - The device might reboot after this command, if it was not already in LoRaWAN mode.

- In FieldTester Mode a backend server has to be set up as integration in the LoRaWAN server. Without this backend server, the FieldTester Mode will not work.
  - More information about available backend solutions can be found in the [RAK10701-L documentation](https://docs.rakwireless.com/product-categories/wisgate/rak10701-l/quickstart/).

- The device has to be registered in a LoRaWAN server with these credentials and a gateway in range has to be connected to the LoRaWAN server. Otherwise, the device cannot join and there are no tests possible. If the device cannot join the network, it will show an error on the display: **LoRaWAN Join Failed**
  - In this case, double check all settings on the device and LoRaWAN server, and check if a gateway is in range and connected to the LoRaWAN server.
:::

### Usage
The principle usage for all modes is similar. After selecting the mode and setting the correct parameters and credentials, the device will send uplink packets in the selected send interval.

:::warning Important
When using FieldTester mode, the device requires a valid location fix from its built-in GNSS module. Otherwise, it will not send any uplink packets.
:::

#### LoRa P2P

If the setup of all devices is the same and a packet is received, the display will show the received LoRa P2P packets:

- P2P received packet number
- Frequency, spreading factor and bandwidth
- RSSI
- SNR

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/lora-p2p-rx.png"
  width="35%"
  caption="LoRa P2P RX"
/>

:::tip NOTE
An uplink can be manually triggered by pushing the button three times.
:::

After a packet is sent, the display shown in **Figure 49** will appear.:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/lora-p2p-tx.png"
  width="35%"
  caption="LoRa P2P RX"
/>

#### LoRaWAN LinkCheck

After the device has joined the network, it will send confirmed packets with LinkCheck request enabled to the LoRaWAN server. The LoRaWAN server will answer to the LinkCheck request. The display will show the following:
- Linkcheck result
- Demodulation Margin from the LoRaWAN server
- DR of the sent packet
- Number of gateways
- Number of sent and lost packets
- RSSI and SNR of the received packet


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/lpw-linkcheck-ok.png"
  width="35%"
  caption="LoRaWAN LinkCheckAns"
/>

If the device is out of range of the gateways (after having previously joined), it will show an error message if the LoRaWAN server did respond to the LinkCheck request:
- Linkcheck result
- Number of sent and lost packets
- Error value
- DR of the sent packet

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/lpw-linkcheck-nok.png"
  width="35%"
  caption="LoRaWAN no LinkCheckAns"
/>

:::tip NOTE
- An uplink can be manually triggered by pushing the button three times.
- To check all possible data rates, multiple uplinks can be triggered by pressing the button four times. The packets will be sent starting with the lowest possible DR, and with each packet, the DR will increase until the highest possible rate is reached.
:::

#### LoRaWAN FieldTester

After the device has joined the network, it will send confirmed packets with location information to the LoRaWAN server. The LoRaWAN server will forward this information together with gateway information to the backend server. The backend server will create and send a downlink packet to the tester. The display will show the following:
- RSSI and SNR level of the received downlink packet
- Number of gateways that received the packet
- Min and Max RSSI levels seen by the gateways
- Min and Max calculated distance between the tester and the gateways
- Number of sent packets and number of lost packets

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/fieldtester-ok.png"
  width="35%"
  caption="Fieldtester display"
/>

Before sending an uplink packet, the tester will try to acquire a location.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/fieldtester-get-location.png"
  width="35%"
  caption="Fieldtester location acquisition"
/>

If a location fix can be acquired, an uplink packet will be sent, followed by waiting for the downlink packet from the backend server. The display's headline will show an _**O**_ to indicate that a location was acquired.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/fieldtester-ok.png"
  width="35%"
  caption="Fieldtester location fix"
/>

If no location fix can be acquired, an error will be displayed and no packet will be sent. The display's headline will show an _**X**_ to indicate that no location was acquired.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/fieldtester-no-location.png"
  width="35%"
  caption="Fieldtester location failure"
/>

:::tip NOTE
- An uplink can be manually triggered by pushing the button three times.
- To check all possible data rates, multiple uplinks can be triggered by pressing the button four times. The packets will be sent starting with the lowest possible DR, and with each packet, the DR will increase until the highest possible rate is reached.
:::

:::warning Important
- In FieldTester Mode a backend server must be set up as integration in the LoRaWAN server. Without this backend server, the FieldTester Mode will not work.
- More information about available backend solutions can be found in the [RAK10701 documentation](https://docs.rakwireless.com/product-categories/wisgate/rak10701-p/quickstart/#lorawan-network-servers-guide-for-rak10701-p-field-tester-pro/)
:::

### Log Files (If SD Card is Present)

If an SD card is present, the results of the coverage tests are written in CSV format to the SD card. The files start from `0000-log.csv`, and on each restart, a new file with an incrementing number is created.

#### AT commands for Log Files

_**`ATC+LOGS=?`**_ is used to retrieve the log files over the USB port. This makes it possible to read the log files without removing the SD card from the device.

_**`ATC+LOGS=e`**_ is used to erase all log files from the SD card.

----

#### Linkcheck Mode Log Format

When in Linkcheck mode for LoRaWAN, the log file has the following format:

##### If Location is Enabled

`time;Mode;Gw;Lat;Lng;RX RSSI;RX SNR;Demod;TX DR;Lost`

##### If Location is Disabled

`time;Mode;Gw;RX RSSI;RX SNR;Demod;TX DR;Lost`

<table>
  <thead>
    <tr>
      <th>PARAMETER</th>
      <th>DECSRIPTION</th>
      <th>VALUES</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>`time`</td>
      <td>Time stamp (available if LNS has provided the time or if a RTC module is attached)</td>
      <td>2024-10-07 14:35:204</td>
    </tr>
    <tr>
      <td>`Mode`</td>
      <td>0 for LinkCheck mode</td>
      <td>0</td>
    </tr>
    <tr>
      <td>`Gw`</td>
      <td>Number of gateways</td>
      <td>1</td>
    </tr>
    <tr>
      <td>`Lat`</td>
      <td>Latitude (if location is active and location fix)</td>
      <td>14.521355</td>
    </tr>
    <tr>
      <td>`Lng`</td>
      <td>Longitude (if location is active and location fix)</td>
      <td>121.10688</td>
    </tr>
    <tr>
      <td>`RX RSSI`</td>
      <td>RSSI of downlink</td>
      <td>-91</td>
    </tr>
    <tr>
      <td>`RX SNR`</td>
      <td>SNR of downlink</td>
      <td>8</td>
    </tr>
    <tr>
      <td>`Demod`</td>
      <td>Demodulation value</td>
      <td>29</td>
    </tr>
    <tr>
      <td>`TX DR`</td>
      <td>TX datarate</td>
      <td>3</td>
    </tr>
    <tr>
      <td>`Lost`</td>
      <td>Number of lost packets</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

----

#### FieldTester Mode Log Format

When in FieldTester mode for LoRaWAN, the log file has the following format:

`time;Mode;Gw;Lat;Lng;min RSSI;max RSSI;RX RSSI;RX SNR;min Dist;max Dist;TX DR`

<table>
  <thead>
    <tr>
      <th>PARAMETER</th>
      <th>DECSRIPTION</th>
      <th>VALUES</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>`time`</td>
      <td>Time stamp (available if LNS has provided the time or if a RTC module is attached)</td>
      <td>2024-10-07 14:39:00</td>
    </tr>
    <tr>
      <td>`Mode`</td>
      <td>2 for FieldTester mode</td>
      <td>2</td>
    </tr>
    <tr>
      <td>`Gw`</td>
      <td>Number of gateways</td>
      <td>1</td>
    </tr>
    <tr>
      <td>`Lat`</td>
      <td>Latitude (can be 0.0 if no location fix, e.g. indoor testing)</td>
      <td>14.521355</td>
    </tr>
    <tr>
      <td>`Lng`</td>
      <td>Longitude (can be 0.0 if no location fix, e.g. indoor testing)</td>
      <td>121.10688</td>
    </tr>
    <tr>
      <td>`min RSSI`</td>
      <td>Minimum RSSI seen by gateways</td>
      <td>-50</td>
    </tr>
    <tr>
      <td>`max RSSI`</td>
      <td>Maximum RSSI seen by gateways</td>
      <td>-50</td>
    </tr>
    <tr>
      <td>`RX RSSI`</td>
      <td>RSSI of downlink</td>
      <td>-59</td>
    </tr>
    <tr>
      <td>`RX SNR`</td>
      <td>SNR of downlink</td>
      <td>7</td>
    </tr>
    <tr>
      <td>`min Dist`</td>
      <td>Minimum distance to gateway(s)</td>
      <td>250</td>
    </tr>
    <tr>
      <td>`max Dist`</td>
      <td>Maximum distance to gateway(s)</td>
      <td>250</td>
    </tr>
    <tr>
      <td>`TX DR`</td>
      <td>TX datarate</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
----

#### P2P Mode Log Format

When in Linkcheck mode for LoRaWAN, the log file has the following format:

##### If Location is Enabled

`time;Mode;Lat;Lng;RX RSSI;RX SNR`

##### If Location is Disabled

`time;Mode;RX RSSI;RX SNR`

<table>
  <thead>
    <tr>
      <th>PARAMETER</th>
      <th>DECSRIPTION</th>
      <th>VALUES</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>`time`</td>
      <td>Time stamp (available if LNS has provided the time or if a RTC module is attached)</td>
      <td>2024-10-07 14:51:21</td>
    </tr>
    <tr>
      <td>`Mode`</td>
      <td>1 for LinkCheck mode</td>
      <td>1</td>
    </tr>
    <tr>
      <td>`Lat`</td>
      <td>Latitude (if location is active and location fix)</td>
      <td>14.521355</td>
    </tr>
    <tr>
      <td>`Lng`</td>
      <td>Longitude (if location is active and location fix)</td>
      <td>121.10688</td>
    </tr>
    <tr>
      <td>`RX RSSI`</td>
      <td>RSSI of downlink</td>
      <td>-38</td>
    </tr>
    <tr>
      <td>`RX SNR`</td>
      <td>SNR of downlink</td>
      <td>12</td>
    </tr>
  </tbody>
</table>

### Miscellaneous

#### Upgrading the Firmware

It is recommended to update to the latest version of the firmware. To do this, download the latest [RAK10706 WisNode Signal Meter firmware](https://docs.rakwireless.com/product-categories/wisgate/rak10706/datasheet#firmware/) and use the WisToolBox to update the custom firmware.

1. Drag the downloaded firmware to the WisToolBox custom firmware section.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/wistoolbox-firmware.png"
  width="85%"
  caption="WisToolBox firmware"
/>

2. After the firmware file is uploaded to the application, you can now select **UPGRADE DEVICE**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/wistoolbox-firmware-upgrade.png"
  width="85%"
  caption="Upload the latest firmware"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/wistoolbox-firmware-upgrade2.png"
  width="85%"
  caption="Confirm upgrading of firmware"
/>

:::tip NOTE
If all proceed with no error, you should see a **Firmware update successful** notification, and the RAK10706 device will restart automatically.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/wistoolbox-firmware-upgrade3.png"
  width="85%"
  caption="Ongoing upgrading of firmware"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/wistoolbox-firmware-success.png"
  width="85%"
  caption="Successful upload of latest firmware"
/>

<RkBottomNav/>