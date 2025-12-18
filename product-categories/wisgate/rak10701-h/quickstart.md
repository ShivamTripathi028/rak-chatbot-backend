---
slug: /product-categories/wisgate/rak10701-h/quickstart/
title: RAK10701-H Field Mapper for Helium Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK10701-H Field Mapper for Helium Network. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: https://images.docs.rakwireless.com/wisnode/rak10701/rak10701-h.png
keywords:
  - field mapper
  - helium network
  - quickstart
sidebar_label: Quick Start Guide
download: true
---

# RAK10701-H Field Mapper for Helium Quick Start Guide

## Prerequisites

### What Do You Need?

Before going through each and every step in the installation guide of the RAK10701-H Field Mapper for Helium Network, make sure to prepare the necessary items listed below:

#### Hardware Tools

1. [RAK10701-H Field Mapper for Helium Network](https://store.rakwireless.com/products/field-mapper-for-helium-with-plug-play-and-3rd-party-mode-rak10701-h?variant=42437640782022?utm_source=RAK10701H&utm_medium=Document&utm_campaign=BuyFromStore)
2. LoRa SubGhz Antenna with RP-SMA connector
3. USB Type-C Cable
4. Windows/Linux/macOS for PC or iOS/Android for mobile

#### Software Tools

[WisToolBox](https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/overview/) for configuration and firmware update.

## Product Configuration

### RAK10701-H Field Mapper Physical Interface

The user interface of the RAK10701-H Field Mapper for LoRaWAN is via TFT Touchscreen LCD and one push button at the side. There is also an external LoRA antenna port via RP-SMA connector and USB-C port for charging and configuration if connected to a PC.

> **Image:** Parts of RAK10701-H

:::tip NOTE
You have to ensure that the LoRa antenna is attached before turning on the device.
:::

1. To turn on the device, you have to press and hold the button for at least five seconds.

> **Image:** RAK10701-H button to turn on

:::tip NOTE
The same button can be used to power off. You have to hold it as well for at least five seconds.

> **Image:** RAK10701-H power off

:::

2. When the device initializes, it will show the RAK logo on the screen. If there is any initialization error, it will be shown on the upper right section of the screen as well. A properly working device should not have any errors shown.

> **Image:** RAK10701-H power up successful

> **Image:** GPS error on boot up sequence

3. After the successful boot up, the main home screen will be shown. Take note, that there will be no data at the first start of the device.

:::tip NOTE
The field mapper must be outside and has a clear view of the sky to get GPS coordinates. The GPS antenna is located on top of the device beside the RP-SMA connector of the LoRa Antenna.

If you are indoors, there will be no reception of the GPS signal. The latitude and longitude data will be empty.
:::

> **Image:** RAK10701-H Main Page waiting for valid data

4. Once fully powered on, the external button at the side can sleep or wake up the display on the LCD screen via a single press on it.

5. If the device is connected via USB-C to a computer, then the button is pressed, it will not remove the display but will lock the screen (touch screen behavior is disabled).

> **Image:** RAK10701-H locked screen

### Field Mapper Operating Modes

The Field Mapper can operate in different modes.

- [Plug and Play Mode](https://docs.rakwireless.com/product-categories/wisgate/rak10701-h/quickstart/#plug-and-play-mode)
- [Custom Mode](https://docs.rakwireless.com/product-categories/wisgate/rak10701-h/quickstart/#custom-mode)
- [Discovery Mode](https://docs.rakwireless.com/product-categories/wisgate/rak10701-h/quickstart/#discovery-mode)

Additional information:

- [Packet Frame Format](https://docs.rakwireless.com/product-categories/wisgate/rak10701-h/quickstart/#packet-frame-format)

:::tip NOTE
All these modes require you to be within Helium network coverage. Otherwise, the device will not be able to join the Helium network. The Helium network converge can be found on [Helium Explorer webpage](https://explorer.helium.com/).
:::

The active work mode (Plug-and-Play or Custom) of the Field Mapper can be found under settings. You have to click the settings icon to check the current mode.

> **Image:** RAK10701-H settings button

> **Image:** RAK10701-H word modes - Custom and Plug and Play

You can change the mode anytime using the navigation keys on the touchscreen LCD and the device will restart to activate the new mode.

> **Image:** RAK10701-H restart notification

The third mode (Discovery mode), can be enabled without going to settings. The Discovery mode runs by clicking the discovery mode icon.

> **Image:** RAK10701-H Discovery mode

#### Plug and Play Mode

On Plug and Play mode, the RAK10701-H Field Mapper automatically sends the uplink payload to the Helium network as long as it was able to join the network.

There is no EUI and KEY configuration needed since it is already on-boarded to the Helium network with the included data credits (DC). The only parameter that is critical to set is the regional band. This is dependent on your location. For example, if you are in Europe, it must be EU868 as shown in this guide. The complete regional frequency plans per country can be found on [Helium documentation on frequency plans](https://docs.helium.com/lorawan-on-helium/frequency-plans/#frequency-plans-by-country).

> **Image:** RAK10701-H band settings

The Field Mapper must get a GPS fix to get valid data. The number of hotspots count will only update once the device sent a successful uplink and received a downlink coming from the server. If you are indoors, the device will not be able to get the satellite signals and won't have latitude and longitude coordinates.

> **Image:** RAK10701-H GPS fix

You can also force an uplink even without a GPS fix by double-clicking on the external button at the side of RAK10701-H.

> **Image:** RAK10701-H force uplink

In plug-and-play mode, the Field Mapper is **automatically configured** to work on [Helium Cargo](https://cargo.helium.com/), [Coverage Map](https://coveragemap.net/heatmap) and [Helium Mapper](https://mappers.helium.com/). This allows you to quickly check your device by using its device name in real-time.

**Helium Cargo** - You can check your device by search input and it will filter all devices automatically. You can click on the name of your device and get more information.

> **Image:** RAK10701 in Helium Cargo

**Coverage Map** - Under the `Advance maps`, you can directly check your device and see it on the coverage map.

> **Image:** Coverage Map - Advance maps

> **Image:** RAK10701 in Coverage Map

**Helium Mapper** - The RAK10701-H contributes automatically to the coverage mapping collected by the Helium Mapper. You can go to your area and see if the hex coverage is updated.

> **Image:** RAK10701 in Helium Mapper

#### Custom Mode

In Custom Mode, the RAK10701 can be manually registered to [Helium Console](https://console.helium.com/). This is a public LoRaWAN network server that you can use for your LoRaWAN end-devices. This guide shows each detail of how to prepare the Helium Console for your RAK10701 field mapper. There will be two dedicated on this mode - [Setting up of Helium Console](https://docs.rakwireless.com/product-categories/wisgate/rak10701-h/quickstart/#setting-up-of-the-helium-console) and [Configuration of RAK10701 via WisToolBox](https://docs.rakwireless.com/product-categories/wisgate/rak10701-h/quickstart/#configuration-of-rak10701-h-using-wistoolbox).

##### Setting up of the Helium Console

:::tip NOTE
This guide is based on [disk19 guide for the Field Mapper](https://github.com/disk91/WioLoRaWANFieldTester/blob/master/doc/ConfigureHelium.md) configuration for the Helium Console.
:::

1. You need to register an account and then purchase data credits (DC) to use the network. If you are a new user, there are free data credits (DC) included in your new account to get you started quickly.

> **Image:** Heluim Console

> **Image:** Console Home Page

2. Once you are logged in, you can start adding your device. You have two ways to add a device as shown in the image.

> **Image:** Adding Device

3. The newly added device parameters will be shown. You have to put a device name and click save.

:::tip NOTE
The DEVEUI, APPEUI, and APPKEY are important in this step. These values must be configured on your RAK1071-H device using WisToolBox which will be covered later in this guide.
:::

> **Image:** Configuring Device Name

4. The device will be added to the blockchain and it will show pending beside its name.

> **Image:** Pending Device Status

5. While waiting for the device to be added to the blockchain, you can create a `Label`. This will allow you to group your device to have a common setting. This will be needed to attach the needed integrations to the backend server of `dev.disk91.com`. You have to click the folder with the + icon add a `Label` name then click Save Label. The newly created label should now be shown in the `Devices` console.

> **Image:** Add Label icon

> **Image:** Add Label Name

> **Image:** Label created successfully

6. Once the `Label` is created you have to associate it on the RAK10701 device. You can attach the `Label` on the device by clicking the Add Label button.

> **Image:** Attach the label to the device

7. A pop-up will be shown and you have to select the correct `Label` created for RAK10701 then click **Add Label**.

> **Image:** Drop-down on label selection

8. After successful attachment of `Label` on the devices, it should show one (1) device is under that `Label`. The device is properly labeled which is needed for the next steps - `Integrations` and `Flow`.

> **Image:** Label added on the RAK10701 device

9. To connect the backend server, you have to create an `Integration`.

> **Image:** Add integration

> **Image:** HTTP integration

10. Then you must proceed to steps 2 and 3 sections of the `Integration` settings. You have to select `POST` then on the Endpoint URL, you must put `https://dev.disk91.com/fieldtester/helium/v3`. It is also needed to put the integration name before the clicking the **Add integration** button.

> **Image:** Details of HTTP Integration

11. After preparing the device and the integration, you can now proceed with creating the flow to connect them. You have to click `Flows` and then the `+` icon on `NODES`.

> **Image:** Setting up the Flows

12. You must select `Labels` and `Integrations` and then drag the correct blocks on the flows canvas.

> **Image:** Drag the rak10701-devices label

> **Image:** Drag the RAK1070x_Integration

13. You then have to connect the `Label` block to the `Integration` block via the tiny connector indicated by the red arrows by using your mouse cursor and dragging the line connector.

:::tip NOTE
There is no need to save the changes created on the flows canvas since it is automatically saved as you do changes.
:::

> **Image:** Connecting Labels to Integrations

14. The final step in the setting up of the Helium Console for RAK10701 is the setting up of packets. You have to click on `Packets` and then the `Add New Packet Config` icon.

> **Image:** Creating Packets

15. You must also input a name on the `Packet Config Name`, select `Multiple Packets` and drag the slider, so it will show `All Available Packets`. Once done, you can now click on `+ Create Packet Config`.

> **Image:** Multiple packets configuration

> **Image:** Successful packets creation

16. You must associate the multiple packet setup with the `rak10701-devices` label. To do this, you have to go back on `Flows`, double-click on the `rak10701-devices` label, choose the `Pakets` tab under rak10701-devices settings then enable the `ALL Packets` slide switch. After this, you can now proceed with the configuration of RAK10701.

> **Image:** Attaching multiple packets to the rak10701-devices label

##### Configuration of RAK10701-H Using WisToolBox

The Field Mapper should have the correct credentials to connect to the Helium Console. This can be done using WisToolBox and also with the help of the touchscreen LCD user interface.

1. Connect the RAK10701-H to the PC via USB Type-C cable and open the WisToolBox application. You can find more info on how to install and use the [WisToolbox from its documentation](https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/overview/).

2. Click the **CONNECT DEVICE** button to launch WisToolBox Dashboard.

> **Image:** WisToolBox Desktop splash screen

3. Review the **Connection settings** parameters on the dashboard, then click on the **CONNECT** button.

> **Image:** WisToolBox Desktop connection settings

4. On the WisToolBox Dashboard screen, select the RAK4630 module. This is the module inside the RAK10701-H Field Mapper device.

> **Image:** Detected module by WisToolBox

5. You can now update the APPEUI, DEVEUI, and APPKEY. It must be the same as the parameters you have in the [Setting up of Helium Console](https://docs.rakwireless.com/product-categories/wisgate/rak10701-h/quickstart/#setting-up-of-the-helium-console) as shown in step 3. Then you can click **APPLY COMMANDS**.

> **Image:** Changing device parameters

:::tip NOTE
These are the only parameters that you need to change via WisToolBox. Other configurations like frequency plan, the interval of uplinks, TX power, and data rate can be done on the touchscreen of RAK10701.

For the frequency plan change, the device has to restart to activate this newly configured frequency band. There will be a notification on the UI touchscreen LCD. If you use WisToolBox to configure the band, you have to restart the device manually, and there will be no notification from the UI of the LCD.
:::

6. You will see the summary of commands that was applied successfully. If the update is unsuccessful, just resend the needed changes. After the successful update, click the **CLOSE** button to return to Dashboard.

> **Image:** Successful update of parameters

7. You can now remove the USB Type-C cable and proceed to the screen of RAK10701. You can click the settings icon and then update the frequency plan, the interval of uplinks, TX power, and data rate as needed. You can use the arrows for navigation and click `OK` to save changes.

> **Image:** RAK10701-H settings button

> **Image:** Configurable parameters

#### Discovery Mode

1. Click the **Discovery Mode** button on the RAK10701-H screen to enter Discovery Mode.

:::tip NOTE
You need to be able to join the Helium network as well as a good GPS fix to enable Discovery Mode.
:::

> **Image:** Discovery mode button

2. Wait for a while, and after the progress bar of sending 10 groups of data packets on the screen is completed, the page will automatically jump to generate a QR code.

> **Image:** Discovery mode joining

> **Image:** Discovery mode scanning

3. Scan the QR code using your smartphone to view the map between the RAK10701-H and the hotspot.

> **Image:** QR Generated after Discovery Mode

4. The QR code is a link that will direct you to disk19.com URL with mapbox.

> **Image:** Map provided on the QR link

### Miscellaneous

This part of the guide shows the Field Mapper interface and how to update the firmware.

- [User Interface](https://docs.rakwireless.com/product-categories/wisgate/rak10701-h/quickstart/#field-mapper-display-interface)
- [Firmware Update](https://docs.rakwireless.com/product-categories/wisgate/rak10701-h/quickstart/#upgrading-the-firmware)

#### Field Mapper Display Interface

This section discusses the interfaces on the LCD of the device as well as its pages.

##### Display Status and Indicator

The RAK10701-H Field Mapper for Helium has status indicators that show the current state of the device.

> **Image:** Device status and indicator

> **Image:** Different device status

**Status:**

- **IDLE**: RAK10701-H Field Mapper state is in between the previous uplink and the next uplink. The duration of IDLE depends on the interval configured on the device.
- **JOINING**: RAK10701-H Field Mapper is trying to join the network. This status is triggered when a Join request is sent.
- **JOINED**: RAK10701-H Field Mapper successfully received the Join accept the packet. This status will be displayed until refreshed when new data is sent.
- **FAILED**: RAK10701-H Field Mapper failed to join the network. Triggered by receive timeout. There might be no available gateway reachable by the Field Mapper.
- **SENDING**: RAK10701-H Field Mapper's data such as GPS is being uploaded via an uplink. It will be displayed until the reception is completed or timed out.

##### Settings

The field mapper has configurable parameters: Band, TX power, TX interval, backlight intensity, and DR. You can navigate the settings using the arrow widgets plus the back and ok buttons.
The OTAA parameters APPEUI, DEVEUI, and APPKEY are also displayed but can't be changed on the touchscreen. WisToolBox or another Serial Port terminal tool is needed to send the AT commands to update the EUIs and key.

> **Image:** Settings button

> **Image:** Settings page

##### Data Plots

There are four different data plots on the field mapper: **number of gateways**, **RSSI**, **SNR**, and **approximate distance**. These graphs are accessible by touching the respective icons assigned to the parameter.

> **Image:** Accessing different data plots

> **Image:** Distance plot

> **Image:** RSSI plot

> **Image:** SNR plot

##### GPS Data

The main page shows the last GPS data captured by the device.

> **Image:** GPS display

> **Image:** GPS data

#### Packet Frame Format

The Uplink packet format send on Fport 1:
| Byte  | Usage                                                  |
| ----- | ------------------------------------------------------ |
| 0 - 5 | GSP position see here for details. Decoding see below  |
| 6 - 7 | Altitude in meters + 1000 m ( 1100 = 100 m ) |
| 8     | HDOP * 10 (11 = 1.1)                                   |
| 9     | Sats in view                                           |

When the GPS position is invalid of GPS is disable, the frame is fill with 0's.

The downlink response format send on Fport 2:
| Byte | Usage                               |
| ---- | ----------------------------------- |
| 0    | Sequence ID % 255                   |
| 1    | Min Rssi + 200 (160 = -40 dBm) |
| 2    | Max Rssi + 200 (160 = -40 dBm) |
| 3    | Min Distance step 250 m        |
| 4    | Max Distance step 250 m        |
| 5    | Seen hotspot                        |

The distance is calculated from the GPS position and the gateways position returned by LoRaWAN server meta-data. Under 250 m value is 250 m, over 32 km value is 32 km. 0 is considered as invalid response.

The following integration and payload transformation allows to decode the gps position and report is to mapper.

Dicovery uplink format send on Fport 3 (no ack):
| Byte  | Usage                                                                                              |
| ----- | -------------------------------------------------------------------------------------------------- |
| 0 - 5 | [GPS position](https://www.disk91.com/2015/technology/sigfox/telecom-design-sdk-decode-gps-frame/) |

Discovery is sending 10 messages SF10 on every 40 seconds. All the other information comes from the metadata provided by the network server.

#### Upgrading the Firmware

It is recommended to update to the latest version of the firmware. To do this, download the latest [RAK10701-H Field Mapper for Helium firmware](https://docs.rakwireless.com/product-categories/wisgate/rak10701-h/datasheet/#software) and use the WisToolBox to update the custom firmware.

1. Drag the downloaded firmware to the WisToolBox custom firmware section.

> **Image:** WisToolBox firmware

2. After the firmware file is uploaded to the application, you can now select **UPGRADE DEVICE**.

> **Image:** Upload the latest firmware

> **Image:** Confirm upgrading of firmware

3. If all proceed with no error, you should see `Firmware update successful` notification, and the RAK10701-H will restart automatically.

> **Image:** Ongoing upgrading of firmware

> **Image:** Successful upload of latest firmware

