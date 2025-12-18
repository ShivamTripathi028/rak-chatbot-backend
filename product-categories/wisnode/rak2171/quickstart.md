---
slug: /product-categories/wisnode/rak2171/quickstart/
title: RAK2171 WisNode TrackIt Helium Integration
description: Contains instructions and tutorials for installing and deploying your RAK2171. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: https://images.docs.rakwireless.com/wisnode/rak2171/rak2171.png
keywords:
    - lorawan
    - tracker
    - rak2171
    - quickstart
    - wisnode
sidebar_label: Quick Start Guide
---

# RAK2171 Quick Start Guide

## Prerequisites

### What Do You Need?

Before going through each and every step in the guide of the RAK2171 WisNode TrackIt, make sure to prepare the necessary items listed below:

- <a href="https://store.rakwireless.com/products/wisnode-trackit-set-rak2171?utm_source=RAK2171WisNodeTrackIt&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAK2171 WisNode TrackIt</a>
- WisGate Edge gateway
- An Android or iOS device with Bluetooth

### What’s Included in the Package?

- 2 pcs RAK2171 WisNode TrackIt
- 2 pcs Charging cable with magnetic plate
- 2 pcs Protective silicone case

> **Image:** Inclusion list

## Product Configuration

WisNode TrackIt supports three working modes:
1. [LoRaWAN Mode](#lorawan-mode)
2. [P2P Mode](#lora-peer-to-peer-p2p-mode)
3. [Third-party LNS](#third-party-lorawan-network-server-lns-mode)

### LoRaWAN Mode

To fully utilize the WisNode TrackIt and the TrackIt App in this mode, you need to use RAK WisGate Edge gateway/s.

In this mode, the WisNode TrackIt is configured via the TrackIt application on your phone. The TrackIt application automatically registers the RAK2171 trackers in the WisGate Edge gateways' Built-in Network Server.

> **Image:** LoRaWAN mode

1. Download and install the [**TrackIt App**](https://play.google.com/store/apps/details?id=com.rak.wisnodetrackit&hl=en_US&gl=US) on your smartphone.
2. Turn on the Bluetooth on tour smartphone.
3. Start the **TrackIt App**. Location permission may be requested, allow it.
4. Agree with the **Terms and Conditions** and the **Privacy Policy**, and press the **Sign in with RAK ID** button.

> **Image:** Welcome screen

5. Sign in with your RAK ID or sign up for a new RAK ID if you don’t have an account. If you do not have a RAK ID, press the **Create new** link and fill the needed information.

> **Image:** Sign in screen

6. After you log in, the App will prompt you to add a tracker. To start the pairing process, press the **+ ADD TRACKER** button.

> **Image:** Add tracker and Start Pairing screen

7. Hold the **Power button** of your RAK2171 for 3 seconds to turn it on. If the device was turned on previously, you may need to restart it, as the Bluetooth is available for pairing for 3 minutes.

8. Press the **Start Pairing** in the app. An information screen will be displayed to inform you of the process.

> **Image:** Pairing screen

If the tracker is turned off or the Bluetooth pair period has expired, you will see a **Tracker not found** message. Restart the tracker and try again.

> **Image:** Pairing screen

9. After successful pairing, you will see a configuration screen, where you will be able to change the tracker's default name and the working mode. This section is for the LoRaWAN mode, so press the LoRaWAN button to change the mode from LoRa P2P to LoRaWAN.

> **Image:** Set up screen

10. You will see two options: **RAK Embedded NS** and **Third Party NS**. For this mode, press **RAK Embedded NS**.

11. Confirm that the gateway is powered and ready by pressing the **GATEWAY ON** button.

> **Image:** Gateway on confirmation

12. You will be prompted to connect to the Wi-Fi AP of your RAK gateway. Press the **GO TO WI-FI SETTINGS** button. You will be redirected to your phone's Wi-Fi settings, where you need to find the RAK WisGate Edge gateway Wi Fi AP and connect to it. You will be promoted for the gateway's login credentials.

- By default,
  - Username: **root**
  - Password: **root**

> **Image:** Connect to the gateway's Wi-Fi screen

13. After successful login, the TrackIt app will create an application in the gateway's built-In NS and will register the TrackIt device automatically. Once you are done, press the **VIEW ON MAP** button to see the WisNode TrackIt location on the application map.

> **Image:** Successful connection screen

### LoRa Peer-to-Peer (P2P) Mode

In this mode, no LoRaWAN gateway is needed, but you need at least two RAK2171 devices. One of the trackers is permanently connected via Bluetooth to the TrackIt App on your smartphone and acts a **Host**. The other tracker/s is/are registered as **Client** and send their data to the Host tracker.

> **Image:** P2P mode

1. Download and install the [**TrackIt App**](https://play.google.com/store/apps/details?id=com.rak.wisnodetrackit&hl=en_US&gl=US) on your smartphone.
2. Turn on the Bluetooth on tour smartphone.
3. Start the **TrackIt App**. Location permission may be requested, allow it.
4. Agree with the **Terms and Conditions** and the **Privacy Policy**, and press the **Sign in with RAK ID** button.

> **Image:** Welcome screen

5. Sign in with your RAK ID or sign up for a new RAK ID if you don’t have an account. If you do not have a RAK ID, press the **Create new** link and fill the needed information.

> **Image:** Sign in screen

6. After you log in, the App will prompt you to add a tracker. To start the pairing process, press the **+ ADD TRACKER** button.

> **Image:** Add tracker and Start Pairing screen

7. Hold the **Power button** of your RAK2171 for 3 seconds to turn it on. If the device was turned on previously, you may need to restart it, as the Bluetooth is available for pairing for 3 minutes.

8. Press the **Start Pairing** in the app. An information screen will be displayed to inform you of the process.

> **Image:** Pairing screen

If the tracker is turned off or the Bluetooth pair period has expired, you will see a **Tracker not found** message. Restart the tracker and try again.

> **Image:** Pairing screen

10. After successful pairing, you will see a configuration screen, where you will be able to change the tracker's default name and the working mode.

> **Image:** Set up screen

11. Select the LoRa P2P mode and press **ADD**. Your tracker is now added as a **Host**, then press the **VIEW ON MAP** button to see its location. As the Host should be always connected to your smartphone, this is also your position.

:::tip NOTE
The first Tracker you add will act as a **Host**. All other trackers added will be **Clients**.
:::

> **Image:** Host tracker is added

12. To add a **Client** tracker, press the **+** button on the map. The adding process is the same as for the **Host**.  If you go to the map and slide up the menu at the bottom, you will see the registered trackers, their role, and battery status.

> **Image:** Client tracker is added and Registered Trackers List

### Third-Party LoRaWAN Network Server (LNS) Mode

In this mode, any LoRaWAN NS can be used (TTN, Helium, or other). The RAK TrackIt App acts only as a configuration tool for the trackers, no map or location data is available in the App.

> **Image:** Client tracker is added and Registered Trackers List

1. Download and install the [**TrackIt App**](https://play.google.com/store/apps/details?id=com.rak.wisnodetrackit&hl=en_US&gl=US) on your smartphone.
2. Turn on the Bluetooth on tour smartphone.
3. Start the **TrackIt App**. Location permission may be requested, allow it.
4. Agree with the **Terms and Conditions** and the **Privacy Policy**, and press the **Sign in with RAK ID** button.

> **Image:** Welcome screen

5. Sign in with your RAK ID or sign up for a new RAK ID if you don’t have an account. If you do not have a RAK ID, press the **Create new** link and fill the needed information.

> **Image:** Sign in screen

6. After you log in, the App will prompt you to add a tracker. To start the pairing process, press the **+ ADD TRACKER** button.

> **Image:** Add tracker and Start Pairing screen

7. Hold the **Power button** of your RAK2171 for 3 seconds to turn it on. If the device was turned on previously, you may need to restart it, as the Bluetooth is available for pairing for 3 minutes.

8. Press the **Start Pairing** in the app. An information screen will be displayed to inform you of the process.

> **Image:** Pairing screen

If the tracker is turned off or the Bluetooth pair period has expired, you will see a **Tracker not found** message. Restart the tracker and try again.

> **Image:** Pairing screen

9. After successful pairing, you will see a configuration screen, where you will be able to change the tracker's default name and the working mode. Press the LoRaWAN button to change the mode from LoRa P2P to LoRaWAN.

> **Image:** Set up screen

10. You will see two options: **RAK Embedded NS** and **Third Party NS**. For this mode, press **Third Party NS**.

11. You can see the RAK2171 **Device EUI**, **Application EUI**, **Application Key**, **Class**, and **Join mode**. From the **Region** menu, you can select the LoRaWAN band to be used.

:::tip NOTE
* For now, the Class and Join mode can't be changed.
* All LoRaWAN bands will be added with next firmware updates.
:::

> **Image:** Third Party NS Set up screen

12. Press **CONFIRM** to choose the selected LoRaWAN region. Then, press **CONTINUE**.
13. A notification will be displayed, that in Third-party LNS mode the device's position data will be not available on the TrackIt App's map as the data will be sent to the Third-party Network Server directly.

> **Image:** Third Party NS Confirmation

## TrackIt LoRaWAN Payload

TrackIt is the latest GPS LoRaWAN tracker by RAKwireless. The name hints what is the device’s purpose – to track something, whether it is a person, an asset, an animal, or anything else. In addition to the tracking application, the device can be used to send SOS or a 6-level alarm signal, based on movement, vibration, fall, etc. The different payloads of the device are explained in this section.

### Header/Payload Type/Message ID

| 1 byte | 1 byte |  |  |
| --- | --- | --- | --- |
| HEADER | Payload time | Reserved | Message ID |
| 2 bits | 6 bits | 3 bits | 5 bits |

- **Header** - by default, the Header is 11.
- **Payload type** – different payload types are explained in this table above.
- **Message ID** – an internal counter for the message. The first 5 bits are for the message ID. The other 3 are reserved.

### Header/Payload Type

The different payload types that TrackIt can send are explained below. If the GPS has a fix, it will send data of the location. If a 6-level alarm is activated in the application, the device will send a message when the working pattern is activated.

With 5 clicks on the power button, the device will start sending SOS messages. When the SOS is canceled, a message will also be sent.

| 0b’1100 1010 | No Location | 0xCA |
| --- | --- | --- |
| 0b’1100 1011 | Location | 0xCB |
| 0b’1100 1100 | Send SOS | 0xCC |
| 0b’1100 1101 | Cancel SOS | 0xCD |
| 0b’1100 1110 | 6-level alarm | 0xCE |

#### Working Patterns in 6-level Alarm

1. Mild Vibration
2. Violent Vibration
3. Movement
4. Mild Shaking
5. Violent Shaking
6. Fall

### No Location Payload

The device will send **No location payload** when the GPS has no fix.

| 1 byte              | 2 byte     | 3-6 byte       | 7-10 byte | 11 byte       | 12-16 byte |
|---------------------|------------|----------------|-----------|---------------|------------|
| Header/Payload Type | Message ID | Application ID | Device ID | Battery Level | Time       |

1. Header/Payload Type: 1 byte
2. Message ID: 1 byte (3 reserved bits + 5 bits to be used for the ID)
3. Application ID: 4 bytes
4. Device ID: 4 bytes
5. Battery: 1 byte
6. Time: 4 bytes
7. Status: 1 byte – 8 bits
- Bit 0 – shows if Extended Prediction Orbit (EPO) worked. This allows the device to predict where satellites will be in the sky.
- Bit 1 – shows if the device is charging.
- Bit 2 and 3 show if there is GPS fix:
  * 00: Open the GPS fix
  * 01: Locating
  * 10: Successful
  * 11: Failed

### Location Payload

The device will send **Location payload** when the GPS has a fix.

 | 1 byte              | 2 byte     | 3-6 byte       | 7-10 byte | 11-14 byte | 15-18 byte | 19 byte          | 20 byte | 21 byte | 22-25 byte |
 |---------------------|------------|----------------|-----------|------------|------------|------------------|---------|---------|------------|
 | Header/Payload Type | Message ID | Application ID | Device ID | Longitude  | Accuracy   | GPS Start Number | Battery | Time    | Status     |

1. Header/Payload Type: 1 byte
2. Message ID: 1 byte (3 reserved bits + 5 bits to be used for the ID)
3. Application ID: 4 bytes
4. Device ID: 4 bytes
5. Longitude: 4 bytes
6. Latitude: 4 bytes
7. Accuracy: 1 byte
8. GPS Start Number: 1 byte
9. Battery: 1 byte
10. Time: 4 bytes
11. Status: 1 byte
- Bit 0 – shows if Extended Prediction Orbit (EPO) worked. This allows the device to predict where satellites will be in the sky.
- Bit 1 – shows if the device is charging
- Bit 2 and 3 show if there is a GPS fix:
  * 00: Open the GPS fix
  * 01: Locating
  * 10: Successful
  * 11: Failed

### Send SOS Payload

SOS type payload has two subtypes of payload – SOS without user data and SOS with user data. The user has the option to set information about themselves via the application in the payload – **Name**, **Phone Number**, and **Country code**. To activate the SOS, the user needs to press 5 times the power button of the TrackIt.

#### Payload Without User's Data

| 1 byte              | 2 byte     | 3-6 byte       | 7-10 byte | 11-14 byte | 15-18 byte |
|---------------------|------------|----------------|-----------|------------|------------|
| Header/Payload Type | Message ID | Application ID | Device ID | Longitude  | Latitude   |

#### Payload With User Data

| 1 byte              | 2 byte     | 3-6 byte       | 7-10 byte | 11-14 byte | 15-18 byte | 19-28 byte   | 29-39 byte   | 40-50 byte   |
|---------------------|------------|----------------|-----------|------------|------------|--------------|--------------|--------------|
| Header/Payload Type | Message ID | Application ID | Device ID | Longitude  | Latitude   | Contact Name | Country Code | Phone Number |

1. Header/Payload Type: 1 byte
2. Message ID: 1 byte (3 reserved bits + 5 bits to be used for the ID)
3. Application ID: 4 bytes
4. Device ID: 4 bytes
5. Longitude: 4 bytes
6. Latitude: 4 bytes
7. User’s name: max length is 10 bytes
8. Country code: max length is 11 bytes
9. Phone number: max length is 11 bytes

### Cancel SOS Payload

This payload will be sent when the SOS is canceled. To cancel the SOS, the user needs to press 5 times the power button of the TrackIt.

 | 1 byte              | 2 byte     | 3-6 byte       | 7-10 byte |
 |---------------------|------------|----------------|-----------|
 | Header/Payload Type | Message ID | Application ID | Device ID |

1. Header/Payload Type: 1 byte
2. Message ID: 1 byte (3 reserved bits + 5 bits to be used for the ID)
3. Application ID: 4 bytes
4. Device ID: 4 bytes

### 6-level Sensitivity Alarm Payload

The 6-level sensitivity alarm is configured in the application of the TrackIt. The device will send data only when a chosen **Working Pattern** is activated. These are the different **Working Patterns** in 6-level alarm:

1. Mild Vibration
2. Violent Vibration
3. Movement
4. Mild Shaking
5. Violent Shaking
6. Fall

 | 1 byte              | 2 byte     | 3-6 byte       | 7-10 byte | 11 byte |
 |---------------------|------------|----------------|-----------|---------|
 | Header/Payload Type | Message ID | Application ID | Device ID | Level   |

1. Header/Payload Type: 1 byte
2. Message ID: 1 byte (3 reserved bits + 5 bits to be used for the ID)
3. Application ID: 4 bytes
4. Device ID: 4 bytes
5. Level: 1 byte

