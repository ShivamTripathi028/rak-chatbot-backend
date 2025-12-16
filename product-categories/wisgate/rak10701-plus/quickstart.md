---
slug: /product-categories/wisgate/rak10701-plus/quickstart/
title: RAK10701-Plus Field Tester for LoRaWAN Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK10701-Plus Field Tester for LoRaWAN. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/physical-interface.png.png
keywords:
    - lorawan
    - field tester
    - RAK10701-Plus
    - quickstart
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK10701-Plus Field Tester for LoRaWAN Quick Start Guide

## Prerequisites

Before going through each and every step in the installation guide of the RAK10701-Plus Field Tester for LoRaWAN, make sure to prepare the necessary items listed below:

### Hardware Tools

- <a href="https://store.rakwireless.com/products/field-tester-plus-for-lorawan-rak10701-plus?utm_source=field-tester&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAK10701-Plus Field Tester for LoRaWAN</a>
- LoRa Sub-GHz Antenna with RP-SMA connector
- USB Type-C Cable
- PC (Windows/Linux/macOS) or mobile (iOS/Android)
- RAK Gateway running WisGateOS 2 with Field Test Extension installed<br/>
  Example models include:
  - <a href="https://store.rakwireless.com/products/wisgate-edge-lite-2-rak7268v2-rak7268cv2?utm_source=WisGateRAK7268V2&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAK7268V2</a>
  - <a href="https://store.rakwireless.com/products/wisgate-edge-pro-rak7289v2-rak7289cv2?utm_source=WisGateRAK7289V2&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAK7289V2</a>
  - <a href="https://store.rakwireless.com/products/wisgate-edge-prime-rak7240v2-rak7240cv2?utm_source=WisGateRAK7240CV2&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAK7240V2</a>

  For the full list of compatible gateways, refer to the official WisGate Edge product series.

  :::tip NOTE
  If you purchased the Field Tester Plus Bundle, the RAK7268V2 comes pre-installed with the required extension.
  :::

### Software Tools

  - **Field Test Data Processor Extension for WisGateOS 2**<br/>
    To install the extension, see the guide: <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/#field-test-data-processor" target="_blank">How to Add an Extension</a>
  - <a href="https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/overview/" target="_blank"><b>WisToolBox</b></a>
      - Required for configuring OTAA parameters (DevEUI, AppEUI, and AppKey)
      - Used to register the Field Tester Plus on your LoRaWAN Network Server
      - Also supports firmware updates and device-level configuration

:::tip NOTE
The RAK10701-Plus must be fully charged and within the coverage area of the LoRaWAN Gateway of the network you are attempting to join. Without coverage, the field tester will not function properly.
:::

## Product Configuration

Before configuring the Field Tester Plus, it’s important to understand the physical interfaces, display layout, and basic operations of the device. For detailed specifications, refer to the <a href="https://docs.rakwireless.com/product-categories/wisnode/rak10701-plus/datasheet/" target="_blank">Field Tester Plus Datasheet</a>.

1. Connect the LoRa Sub-GHz antenna (RP-SMA connector) to the device.
2. Press and hold the side button for 5&nbsp;seconds to turn on the Field Tester Plus.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/button.png"
  width="55%"
  caption="RAK10701-Plus button to turn on"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/rak10701-plus-power-up-successful.png"
  width="55%"
  caption="RAK10701-Plus power up successful"
/>

3. Once powered on, the **main screen** will appear.

:::tip NOTE
No data will be shown on first boot until a valid uplink occurs.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/quickstart/rak10701-plus-first-boot.png"
  width="55%"
  caption="RAK10701-Plus first boot"
/>

4. Tap the **gear icon** on the screen to open the **Settings** menu.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/quickstart/rak10701-plus-settings-menu​.png"
  width="55%"
  caption="RAK10701-Plus Settings menu"
/>

<b>Parameter Selection & Adjustment:</b>
- Tap the <img src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/quickstart/right-arrow-icon.png" alt="Edit" width="2%"/> **icon** to **cycle through available parameters** (e.g., Band, DR, TX Power).
The selected parameter will **blink**, indicating it is active.
- Tap the <img src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/quickstart/up-arrow-icon.png" alt="Edit" width="2%"/> **icon** or <img src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/quickstart/down-arrow-icon.png" alt="Edit" width="2%"/> **icon** to adjust and confirm the parameter’s value.

<b>Editable Parameters:</b>
| Setting           | Description                                       | Values / Notes                                                          |
|-------------------|---------------------------------------------------|-------------------------------------------------------------------------|
| Location Labeling | Set a test point label (important for CSV export) | Default: NULL Max Length: 6 characters                                  |
| Band              | LoRaWAN regional frequency band                   | RU864, IN865, EU868, US915, AU915, KR920, AS923-1/2/3/4                 |
| DR (Data Rate)    | Affects signal range (lower DR = longer range)    | The available DR options vary by LoRaWAN regional frequency band.       |
| TX Power          | Transmission power level                          | The available TX Power options vary by LoRaWAN regional frequency band. |
| TX Interval       | Time between uplinks                              | 6~3600&nbsp;s                                                           |
| Backlight         | Screen brightness                                 | 0~10                                                                    |
| ADR               | Enable/disable Adaptive Data Rate                 | <ul><li>ON</li><li>OFF</li></ul>                                        |

5. After adjusting the parameters, tap **OK**. In the confirmation screen, tap **OK** again to save your settings and exit the configuration interface.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/quickstart/rak10701-plus-save-settings​.png"
  width="55%"
  caption="RAK10701-Plus save settings"
/>

6. (Optional) Set DevEUI, AppEUI, AppKey via WisToolBox.

a. Connect the Field Tester Plus to your PC using a USB Type-C cable.<br/>
b. Launch the WisToolBox for Desktop.<br/>
c. Click **CONNECT** to establish a connection with the device.<br/>

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/quickstart/wistoolbox-connection-settings.png"
  width="100%"
  caption="WisToolBox connection settings"
/>

:::tip NOTE
If the connection fails, refer to the <a href="https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/wistoolbox-desktop/#wistoolbox-dashboard" target="_blank">WisToolBox for Desktop | Installation and Setup Guide</a>.
:::

d. Select the device and navigate to the **ADVANCED** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak10701-plus/quickstart/wistoolbox-advanced-tab.png"
  width="100%"
  caption="WisToolBox ADVANCED tab"
/>

e. Click **OPEN CONSOLE**, then enter the following AT commands:

| Command      | Value Format                                       |
|--------------|----------------------------------------------------|
| `AT+DEVEUI=` | 8&nbsp;bytes (64-bit hex, e.g. `70B3D57ED0012345`) |
| `AT+APPEUI=` | 8&nbsp;bytes (64-bit hex)                          |
| `AT+APPKEY=` | 16&nbsp;bytes (128-bit hex)                        |

### RAK10701-Plus Field Tester Physical Interface

The user interface of the RAK10701-Plus Field Tester for LoRaWAN consists of a TFT touchscreen LCD and a side push button. Additionally, it features an external LoRa antenna port with an RP-SMA connector and a USB-C port for charging and configuration when connected to a PC.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/physical-interface.png"
  width="55%"
  caption="Parts of RAK10701-Plus"
/>

:::tip NOTE
Make sure that the LoRa antenna is attached before turning on the device.
:::

1. To turn on the device, press and hold the button for at least five seconds.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/button.png"
  width="55%"
  caption="RAK10701-Plus button to turn on"
/>

:::tip NOTE
The same button can also be used to power off the device. To do so, hold it for at least five seconds.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/power_off.png"
  width="55%"
  caption="RAK10701-Plus power off"
/>

:::

2. When the device initializes, it will show the RAK logo on the screen. If there is any initialization error, it will be shown on the upper right section of the screen as well. A properly working device should not have any errors shown.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/rak10701-plus-power-up-successful.png"
  width="55%"
  caption="RAK10701-Plus power up successful"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/gps-error-on-boot-up-sequence.png"
  width="55%"
  caption="GPS error on boot up sequence"
/>

3. After a successful boot-up, the main home screen will be displayed. Note that no data will be shown upon the device's first start.

:::tip NOTE
- The field tester must be outside and have a clear view of the sky to get GPS coordinates. The GPS antenna is located on top of the device beside the RP-SMA connector of the LoRa Antenna.
- If you are indoors, there will be no reception of the GPS signal. The distances, latitude, and longitude data will be empty.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/rak10701-plus-main-page-waiting-for-valid-data.png"
  width="55%"
  caption="RAK10701-Plus Main Page waiting for valid data"
/>

4. Once fully powered on, the external button at the side can sleep or wake up the display on the LCD screen via a single press on it.
5. If the device is connected via USB-C to a computer and the button is pressed, the display won't be removed but the screen will be locked (disabling touch functionality).

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/rak10701-plus-locked-screen.png"
  width="55%"
  caption="RAK10701-Plus locked screen"
/>

The complete data readings on the RAK10701-Plus Field Tester.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/complete-rf-data-information.png"
  width="55%"
  caption="Complete RF data information"
/>

### RAK10701-PLUS Configuration via Settings and AT command

By clicking the settings (gear icon) on the lower right corner of the main screen, you will have access to the settings. This will allow you to change the following parameters:

- **Regional band**: Must be the same with your LoRaWAN network server and gateway.
- **DR**: Data rate allowed on the specific band.
- **TX power**: Represent RF transmission power index. Lower index value has higher power.
- **TX interval**: The regular uplinks configured when field tester is running.
- **Backlight**: Higher value will drain the battery faster.
- **ADR**: Adaptive Data Rate that overrides configured DR.
- **Location Labeling/Tagging**: Initially set to NULL but can be changed by pressing up/down button widget in LCD.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/rak10701-plus-settings-page.png"
  width="55%"
  caption="RAK10701-Plus Settings Page"
/>

The Field Tester Plus must be registered on the LoRaWAN Network Server and successfully joined to function. This requires configuring the device's OTAA parameters, which can be done via AT commands. The required parameters are DEVEUI, APPEUI (also called JOINEUI), and APPKEY.

Use WisToolBox or another serial terminal tool to send the necessary AT commands. These OTAA parameters must match those in the LoRaWAN Network Server (refer to the specific LNS guide in the next section); otherwise, the device will fail to join. To view the AT commands you input instead of just the plain `OK` reply, input the command `ATE`.

```
AT+DEVEUI=BE0FA6C0D5C8407C
AT+APPEUI=31B8B21614DA729B
AT+APPKEY=905DE3EF436DE3A59F095F256D4E8B09
```

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/at-commands-for-otaa-configuration.png"
  width="100%"
  caption="AT Commands for OTAA configuration"
/>

### Installation of the Field Tester Extension on WisGateOS 2

Field Tester Extension is an extension app installed on RAKwireless WisGate Edge LoRaWAN Gateway with WisGateOS 2. It is designed to provide background computing services for Field Tester Plus. The application communicates with LoRaWAN network servers through MQTT subscribe/publish methods, supporting both the built-in LoRaWAN network server in the RAK gateway and third-party LoRaWAN network servers.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/field-tester-extension-using-built-in-lns.png"
  width="85%"
  caption="Field Tester Extension using Built-in LNS"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/field-tester-extension-using-3rd-party-lns.png"
  width="85%"
  caption="Field Tester Extension using 3rd party LNS"
/>

To install, login to the WisGateOS 2 web console of your WisGate Edge LoRaWAN Gateway and proceed to [extensions](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#extensions). Look for **Field Test** extension and click **Install**. Once installed, configure the application and device (Field Tester Plus) to the LoRaWAN network server you use in your network deployment.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/field-tester-extension-installation.png"
  width="75%"
  caption="Field Tester Extension Installation"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/field-tester-extension-overview.png"
  width="100%"
  caption="Field Tester Extension Overview"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/field-tester-extension-configuration.png"
  width="75%"
  caption="Field Tester Extension Configuration"
/>

### LoRaWAN Network Servers Guide for RAK10701-Plus Field Tester

The field tester plus supports different network servers. Check the following guide on how to use the RAK10701-Plus Field Tester for LoRaWAN in the following network servers. If the LNS you use is not listed, the field tester plus will only work in LinkCheck mode.

- [WisGate Built-in LNS](#rak10701-plus-field-tester-guide-using-built-in-lns-of-wisgateos2)
- [The Things Network](#rak10701-plus-field-tester-guide-using-the-things-network-or-the-things-industries)
- [Chirpstack](#rak10701-plus-field-tester-guide-using-chirpstack)
- [AWS IoT Core for LoRaWAN](#rak10701-plus-field-tester-guide-using-aws-iot-core-for-lorawan)

#### RAK10701-Plus Field Tester Guide Using Built-in LNS of WisGateOS 2

One unique feature of Field Tester Plus is that it allows you to have coverage testing without the need of internet. This is made possible by using the Built-in LNS of the WisGateOS 2. This guide will provide you step by step procedure how to setup the Built-in LNS to work on Field Tester Plus.

##### Set the Gateway Work Mode to Built-in Network Server

1.	Configure Work mode to Built-in network server. **Navigate to LoRa** > **Configuration**. For Work mode, select Built-in network server.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/wisgateos2-built-in-lns.png"
  width="100%"
  caption="WisGateOS 2 Built-in LNS"
/>

2.	Select the log level and frequency band.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/configure-log-level-and-frequency-band.png"
  width="100%"
  caption="Configure log level and frequency band"
/>

##### Create an Application on Built-in LNS

1.	Navigate to **LoRa** > **Applications** tab.

2.	Click the **Add application** button or the **add one now** link to create a new application.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/wisgateos2-applications-page.png"
  width="100%"
  caption="WisGateOS 2 Applications Page"
/>

3.	After the page jumps, configure the following information:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/wisgateos2-applications-configuration.png"
  width="100%"
  caption="WisGateOS 2 Applications Configuration"
/>

- **Application name**: Name of the application
- **Application description**: Description of the application (optional)

- **Application Type**

  - **Unified Application key**: Choose this option if all devices will use the same application key. Once selected, a field for the application key appears, where you can manually type in an application key or click the **Autogenerate** button to generate one.

    :::tip NOTE
    The Unified Application Key must match the value from the Field Tester Plus. You can either obtain it by querying the Field Tester Plus or auto-generate it and then update the corresponding value on the Field Tester Plus accordingly
    :::

    After enabling the Auto Add Device option, configure the Application EUI option. This value needs to be consistent with the value from the Field Tester Plus, so either obtain it by querying the Field Tester Plus, or auto-generate it and synchronously change the corresponding value of the Field Tester Plus. After the application EUI and key verification, the device will be automatically added to the application.

  <RkImage
      src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/wisgateos2-application-key.png"
    width="50%"
    caption="WisGateOS 2 Application Key"
  />

  - **Separate Application key**: Each device has its own application key. Add the key when registering the device.

  <RkImage
      src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/wisgateos2-application-eui.png"
    width="50%"
    caption="WisGateOS 2 Application EUI"
  />

4.	Click **Save Application** to add the new application.

:::tip NOTE
The DEVEUI, APPEUI, and APPKEY are important in this step. These values must be configured on your RAK10701-Plus device [via AT commands as mentioned in the previous section](#rak10701-plus-configuration-via-settings-and-at-command).

:::

##### Add End-Device on Built-in LNS

1.	Navigate to **LoRa** > **Applications** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/wisgateos2-application-tab.png"
  width="100%"
  caption="WisGateOS 2 Application tab"
/>

2.	In the application list, click the newly created application and go to the **End devices** tab. If the **Auto Add Device** feature is used, the device will be automatically registered with the adding request. Otherwise, refer to the next step.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/add-end-device1.png"
  width="100%"
  caption="Add End Device"
/>

3.	Click the **Add end device** button.

4.	In the End device information interface, fill in the following information:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/setting-up-otaa-parameters.png"
  width="100%"
  caption="Set up OTAA parameters"
/>

- **Activation Mode**: OTAA. This value needs to be consistent with the value from the end device.
- **End device (group) name**: Name of the end device (group).
- **End device description** (optional): A description of the end device, optional.
- **Class**: Class A
- **Frame Counter Width**: Keep the default value.

5.	Click **Add end devices** to enter the device adding page.

6.	In the **Adding end devices** interface, enter the device **EUI** in the End Device EUI (main) field and click the **Add to End Devices** list button.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/setting-up-device-parameters.png"
  width="100%"
  caption="Set up device parameters"
/>

:::tip NOTE
- The device EUI needs to be consistent with the end device EUI.
- If the EUI is correct, the device will appear in the **End devices list**.
- If the EUI is duplicate, the device will be displayed in the **End devices with an error**.

:::

7.	Click **Add end devices** to add the Field Tester Plus to the application.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/adding-end-device2.png"
  width="100%"
  caption="Add end device"
/>

##### Set Up Mapper Extension Using Built-in LNS

By following the steps in the previous sections, you should now have your device registered. Follow these steps to set up a mapper extension using the built-in LNS:

1. Navigate to **Device EUI**, and go to the corresponding **Configuration** tab.

2. Click the **Packet capture** button. Here you can monitor data that the application is exchanging in real time.

3. Restart to join the network and start sending uplinks, provided the join is successful and interval sending is enabled (indicated by the pause widget next to the settings icon in the lower-right corner of the LCD screen).

    :::tip NOTE
    You can also force an uplink by double clicking the user button on the side of the field tester. Make sure your field tester is within the LoRaWAN Gateway's coverage area, otherwise it will keep attempting to join but will fail.
    :::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/packet-capture.png"
  width="100%"
  caption="Packet capture"
/>

After successful join and initial uplinks, you will only see Downlink information since the integration of Built-in LNS and Field Tester Extension on WisGateOS 2 is not yet done.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/downlink-data-displayed.png"
  width="55%"
  caption="Downlink data displayed"
/>

4. To complete the process, go to the **Field Tester** Extension on your WisGateOS 2 and select the **Built-in Server**.

    :::tip NOTE
    No authentication method is required to connect to the internal MQTT broker, you just need to set the MQTT broker server address to localhost. The default uplink topic is `application/{appName}/device/{devEui}/rx`, which means subscribing uplink message from all Field Tester devices. While for downlink, it is `application/{appName}/device/{devEui}/tx`.
    :::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/mapper-extension-configuration.png"
  width="85%"
  caption="Mapper Extension configuration"
/>

After the successful integration, you should be able to see complete information of Uplink and Downlink RF strength and signal quality.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/complete-rf-data-information.png"
  width="55%"
  caption="Complete RF data information"
/>

#### RAK10701-Plus Field Tester Guide Using The Things Network or The Things Industries

:::tip NOTE
This guide doesn't cover registration of the LoRaWAN Gateway to TTN/TTI. For the registration of LoRaWAN Gateway on the TTN/TTI server, you can [follow this guide](https://docs.rakwireless.com/product-categories/wisgate/rak7268v2/lorawan-network-server-guide#the-things-network-ttn).
:::

For community LoRaWAN Network Server (LNS) The Things Network Sandbox, go to https://console.cloud.thethings.network/. If you use The Things Industries Cloud, go to your account URL.

1. Under the **Existing clusters**, select the cluster where your device or gateway is located. Alternatively, choose the country or region of the device or gateway from the dropdown menu. Then, click on the recommended cluster.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/tti-ttn-cluster-selection.png"
  width="100%"
  caption="TTI/TTN Cluster Selection"
/>

2. On the home page, create an application to register the device.

:::tip NOTE
You can also register the device on any application that is already in your account.
:::

3. Navigate on **Home** > **Dashboard**, then click **Add application** to create an application.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/add-application1.png"
  width="100%"
  caption="Add Application"
/>

4. Click on the **Application** tab. Under the **Create application** page, enter the **Application ID**, **Application name**, and **Description**, then click **Create application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/create-application.png"
  width="100%"
  caption="Create Application"
/>

5. Newly created applications have no end-devices yet. On the **Application overview** > **LoRaWAN end-devices** page, click **+Register end device** to add the end-devices.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/register-end-device.png"
  width="100%"
  caption="Register End Device"
/>

6. Choose **Enter end device specifics manually** as the input method.

:::tip NOTE
Clicking **Enter end device specifics manually** allows you to add the **Frequency plan**, **LoRaWAN version**, **Regional Parameters version** and **JoinEUI**. The values of these parameters depend on the hardware you use. If your device has a preconfigured JoinEUI, use it.
:::

7. Register the end device. Enter the device details, such as the **Frequency plan**, **LoRaWAN version**, and **Regional Parameters version**, then click **Confirm**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/add-end-device-details1.png"
  width="100%"
  caption="Add End Device Details"
/>

8. Once the JoinEUI is confirmed, add the other OTAA parameters—**DevEUI**, **AppKey**, and **End device ID**. Then, under **After registration**, choose **View registered end device** and click on **Register end device**.

    :::tip NOTE
    - If these parameters are not provided in the device, click the **Generate** button.
    - Alternatively, use the OTAA parameters provided in the device.
    :::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/add-end-device-details2.png"
  width="100%"
  caption="Add End Device Details"
/>

9. After you register the device, it will be added to the LoRaWAN Application. Restart the Field Tester Plus and it will join the network and start sending uplinks, provided the join is successful and interval sending is enabled (indicated by the pause widget next to the settings icon in the lower-right corner of the LCD screen).

    :::tip NOTE
    You can also force an uplink by double clicking the user button on the side of the field tester. Make sure your field tester is within the LoRaWAN Gateway's coverage area, otherwise it will keep attempting to join but will fail.
    :::

After successful join and initial uplinks, you will only see Downlink information since the integration of TTI and Field Tester Extension on WisGateOS 2 is not yet done.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/downlink-data-displayed.png"
  width="55%"
  caption="Linkcheck Mode Data"
/>

10. To complete the process, go to the **Field Tester** Extension on your WisGateOS 2 and select **The Things Network**. Input the required parameters, which you can obtain from your TTN or TTI LNS (see [Figure 39](#create-mqtt-integration-in-tti-ttn)). Ensure you add the correct configuration.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/set-extension-to-tti-ttn.png"
  width="90%"
  caption="Set Extension to TTI/TTN"
/>

11. The integration between The Things Network and the Field Tester Extension is via MQTT. You need to <a href="https://www.thethingsindustries.com/docs/api/concepts/auth/#creating-user-api-keys)" target="_blank">generate API key on TTN/TTI</a> console which you will use as the password on the extension.

12. Set up the uplink and downlink topics. The uplink topic is `v3/{application id}@{tenant id}/devices/{device id}/up` and the downlink topic is `v3/{application id}@{tenant id}/devices/{device id}/down/sent`. For example, uplink topic is `v3/xk-mapper@ttn/devices/field-tester-extension/up` while downlink topic is `v3/xk-mapper@ttn/devices/field-tester-extension/down/sent`

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/create-mqtt-integration-in-tti-ttn.png"
  width="100%"
  caption="Create MQTT Integration in TTI/TTN"
/>

After the successful integration, you should be able to see complete information of Uplink and Downlink RF strength and signal quality.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/complete-rf-data-information.png"
  width="55%"
  caption="Complete RF data information"
/>

#### RAK10701-Plus Field Tester Guide Using Chirpstack

1. Log in to your Chirpstack account and on the main dashboard page click Applications.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/chirpstack-dashboard1.png"
  width="100%"
  caption="Chirpstack Dashboard"
/>

:::tip NOTE
This guide doesn't cover registration of the LoRaWAN Gateway to Chirpstack. For registration of the LoRaWAN Gateway on Chirpstack, you can [follow this guide](https://docs.rakwireless.com/product-categories/wisgate/rak7268v2/lorawan-network-server-guide/#chirpstack).
:::

2. On the application page, create new application by clicking **Add application** or select an existing application you have.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/add-application2.png"
  width="100%"
  caption="Add Application"
/>

3. If you choose to add new application, add details of the application which includes **Name** and **Description**. After putting the details, click **Submit**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/add-device.png"
  width="100%"
  caption="Add Device"
/>

4. Add the device by clicking **Add device**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/add-device-information1.png"
  width="100%"
  caption="Add Device Information"
/>

5. On the **Add device** page, add the details of the device including Name, Description, Device EUI, Join EUI, and  Device profile. After providing the details, click **Submit**.

    :::tip NOTE
    Alternatively, use the **Generate** button for **Device EUI** and **Join EUI** if these parameters are not provided in the device. Else, use OTAA parameters are provided in the device.
    :::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/add-device-information2.png"
  width="100%"
  caption="Add Device Information"
/>

6. Once the details are added, add the **Application key**. Use the one provided in the device if any or use the **Generate** button. After inputting the **Application key**, click **Submit**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/add-device-information3.png"
  width="100%"
  caption="Add Device Information"
/>

If all is successful, your device will be registered in the Chirpstack application.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/chirpstack-dashboard2.png"
  width="100%"
  caption="Chirpstack Dashboard"
/>

7. After you register the device, it will be added on the LoRaWAN Application. Restart the Field Tester Plus and it will join the network and start sending uplinks, provided the join is successful and interval sending is enabled (indicated by the pause widget next to the settings icon in the lower-right corner of the LCD screen).

    :::tip NOTE
    You can also force an uplink by double clicking the user button on the side of the field tester. Make sure your field tester is within the LoRaWAN Gateway's coverage area, otherwise it will keep attempting to join but will fail.
    :::

After successful join and initial uplinks, you will only see Downlink information since the integration of Chirpstack and Field Tester Extension on WisGateOS 2 is not yet done.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/downlink-data-displayed.png"
  width="55%"
  caption="Linkcheck Mode Data"
/>

8. To complete the process, go to the **Field Tester** Extension on your WisGateOS 2 and select **ChirpStack**. Input the required parameters, which you can obtain from your ChirpStack LNS.

9. Set up MQTT broker address to the server where you deploy ChirpStack as well as the authentication if needed.
For Chirpstack, the uplink topic is `application/{applicationId}/device/{devEui}/event/up` and the downlink topic is `application/{applicationId}/device/{devEui}/command/down`.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/set-extension-to-chirpstack.png"
  width="55%"
  caption="Set Extension to Chirpstack"
/>

10. After the successful integration, you should be able to see complete information of Uplink and Downlink RF strength and signal quality.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/complete-rf-data-information.png"
  width="55%"
  caption="Complete RF data information"
/>

#### RAK10701-Plus Field Tester Guide Using AWS IoT Core for LoRaWAN

:::tip NOTE
This guide doesn't cover registration of the LoRaWAN Gateway to AWS IoT. For registration of the LoRaWAN Gateway on AWS IoT, you can [follow this guide](https://docs.rakwireless.com/product-categories/wisgate/rak7268v2/lorawan-network-server-guide/#add-a-lorawan-device-to-aws-iot).
:::

Since AWS IoT has an internal MQTT broker but lacks an integrated MQTT for LoRaWAN, additional configurations on the AWS IoT side are required after configuring the extension. Below are the AWS IoT workflow steps followed by the instructions:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/aws-uplink-message-flow.png"
  width="85%"
  caption="AWS Uplink Message Flow"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/aws-downlink-message-flow.png"
  width="85%"
  caption="AWS Downlink Message Flow"
/>

1. To connect to the MQTT broker, retrieve the MQTT broker address from the AWS IoT settings.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/get-the-mqtt-broker.png"
  width="85%"
  caption="Get the MQTT Broker"
/>

2. Since TLS is used to ensure the confidentiality of the MQTT broker, create a certificate in the AWS IoT security.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/creation-of-x509-certificates.png"
  width="85%"
  caption="Creation of X.509 Certificates"
/>

3. Download the device certificate, including the private key and CA certificate, then upload them to the extension configuration page.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/download-the-certificates1.png"
  width="85%"
  caption="Download the certificates"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/download-the-certificates2.png"
  width="85%"
  caption="Download the certificates"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/update-field-tester-extension-with-mqtt-broker-and-certificate.png"
  width="85%"
  caption="Update Field Tester Extension with MQTT Broker and Certificate"
/>

4. Create a destination to process the uplink data by subscribing to the uplink topic, enabling it to receive the uplink data from AWS IoT.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/set-up-uplink-data-destination.png"
  width="85%"
  caption="Set up Uplink Data Destination"
/>

:::tip NOTE
When you have a wireless device for the Field Tester, assign the destination to the wireless device. For more detailed information, see Onboard your devices to AWS IoT Core for LoRaWAN - AWS IoT Wireless.
:::

5. Send downlink message to Field Tester by creating a Lambda Function named ***FieldTester***. The Runtime should be ***Python 3.10***.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/creation-of-lambda-function-of-the-downlink.png"
  width="85%"
  caption="Creation of Lambda Function of the Downlink"
/>

6. Replace the lambda function code with the following python code:

``` python
import json
import boto3
import base64
import codecs
import binascii
client = boto3.client("iotwireless")
def lambda_handler(event, context):
    device_id = event["deviceID"]
    data = event["data"]
    fPort = event["fPort"]
    client.send_data_to_wireless_device(TransmitMode=0,
                                        Id=device_id,
                                        WirelessMetadata={
                                            "LoRaWAN": {"FPort": fPort}},
                                        PayloadData=data)
    return {
        'statusCode': 200,
        'body': json.dumps('Send Downlink from Lambda!')
    }
```

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/add-the-python-script-for-lambda.png"
  width="85%"
  caption="Add the Python Script for Lambda"
/>

7. Create a message routing rule in AWS IoT to subscribe the downlink topic **SendFieldTesterDownlink** and invoke this Lambda Function to process the downlink message.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/set-up-rules-for-the-lambda-function1.png"
  width="85%"
  caption="Set up Rules for the Lambda Function"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/set-up-rules-for-the-lambda-function2.png"
  width="85%"
  caption="Set up Rules for the Lambda Function"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/set-up-rules-for-the-lambda-function3.png"
  width="85%"
  caption="Set up Rules for the Lambda Function"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/set-up-rules-for-the-lambda-function4.png"
  width="85%"
  caption="Set up Rules for the Lambda Function"
/>

### Report Generation of Field Testing Result

Report generation of test logs can be done on the Field Tester Extension in WisGateOS 2. There is a Export button that will generate the CSV file.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/export-on-field-tester-extension-mapper.png"
  width="85%"
  caption="Export on Field Tester Extension Mapper"
/>

Labeling and tagging of locations must be done on the setting interface. Navigate the label tag showing NULL as default and change it using the built-in keyboard. Remember to change the **NULL** setting if you want to log data; otherwise, no readings will be recorded.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/set-location-label-name.png"
  width="45%"
  caption="Set location label/name"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/built-in-keyboard.png"
  width="55%"
  caption="Built-In Keyboard"
/>

After your field testing and generation of report, you can have the CSV output containing all the information of your testing. Click on the sheet showing the field tester DEVEUI.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/quickstart/csv-exported-data.png"
  width="100%"
  caption="CSV Exported Data"
/>

<RkBottomNav/>