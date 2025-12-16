---
slug: /product-categories/wisnode/rak2171/datasheet/
title: RAK2171 WisNode TrackIt Datasheet
description: Provides comprehensive information about your RAK2171 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisnode/rak2171/rak2171.png
keywords:
    - lorawan
    - tracker
    - rak2171
    - datasheet
    - wisnode
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'


# RAK2171 WisNode TrackIt Datasheet

## Overview

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2171/datasheet/rak2171.png"
  width="40%"
  caption="RAK2171 WisNode TrackIt"
/>

### Description

**RAK2171 WisNode TrackIt** is RAKwireless’ latest LoRaWAN GPS tracking device. It comes in a small form factor with rechargeable battery and tracking and configuration application, available for iOS and Android devices.

RAK2171 supports multiple working modes and notification options. When used with RAK WisGate Edge gateways and in P2P mode, you can monitor your tracker on the application map, create geofences, and receive SOS and movement notifications. You can also configure the WisNode TrackIt to work with any third-party LoRaWAN network using the TrackIt application as a configuration tool.

### Features

- MT2523 with built-in Bluetooth and GPS
- SX1262 LoRa chip
- Built-in accelerometer
- Built-in battery: 400&nbsp;mAh
- Charger with a magnetic plate
- Small size: 42 x 42 x 18&nbsp;mm
- Low weight: 25&nbsp;g
- Operating temperature: -20°&nbsp;C to +60°&nbsp;C
- IP65 rating
- Android and iOS application for easy management, configuration, and location tracking


## Specifications

### Overview

#### Board Overview

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2171/datasheet/dimensions.png"
  width="40%"
  caption="RAK2171 WisNode TrackIt Dimensions"
/>


| Parameter             | Value                                                                  |
| --------------------- | ---------------------------------------------------------------------- |
| Dimensions            | 42 x 42 x 18&nbsp;mm                                                   |
| Weight                | 25&nbsp;g                                                              |
| Operating temperature | -20°&nbsp;C to +60°&nbsp;C                                             |
| Battery capacity      | 400&nbsp;mAh                                                           |
| Color                 | Tracker: White / Dark Grey <br /> Charger: Black                       |
| Charger               | 5-pin Magnetic Plate <br /> USB Type-A <br /> Cable Length: 50&nbsp;cm |


### Hardware

The hardware specification is categorized into five (5) parts. It covers the interfacing and the standard values and requirements, such as the RF, electrical, and environmental of the RAK2171 WisNode TrackIt.

#### Interfaces
<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2171/helium-datacake/07.png"
  width="80%"
  caption="RAK2171 WisNode TrackIt Interfaces"
/>

##### Buttons and LED

* **Function Button** - Used for LED signalization.

| LED color           | Meaning                    |
| ------------------- | -------------------------- |
| 🔵 Blue breathing   | Charging                   |
| 🟢 Green steady     | Battery is full            |
| 🔴 Red signal blink | Low battery (20% and down) |

* **Power/SOS Button** - Used for powering on/off the device and sending SOS signals.

| Press Combination            | Function                     | LED Color               |
| ---------------------------- | ---------------------------- | ----------------------- |
| Press and hold for 3 seconds | Power on/off                 | Red light for 3 seconds |
| 5 consecutively clicks       | Sends SOS message to the app | Red flash on            |
| 5 consecutively clicks again | Cancel SOS message           | Red flash off           |

* **Charging Interface** - The device has 3 pins charging port on the back that connects to the magnetic charging plate.

:::tip NOTE
Use the original charging plate and cable only.
:::

#### RF Characteristics

| Parameter     | Value                                                              |
|---------------|--------------------------------------------------------------------|
| Positioning   | GPS & GLONASS                                                      |
| Communication | Bluetooth V4.2 (for configuration) <br /> LoRa (data transmission) |


#### Antennas

The RAK2171 WisNode TrackIt has built-in LoRaWAN, GPS, and Bluetooth antennas.

#### Electrical Characteristics

| Parameter        | Value              |
| ---------------- | ------------------ |
| Battery Type     | Lithium            |
| Battery Capacity | 400&nbsp;mAh       |
| Charging         | 5&nbsp;V, 1&nbsp;A |

#### Environmental Requirements

| Parameter             | Value                      |
| --------------------- | -------------------------- |
| Charging temperature  | +10°&nbsp;C to +45°&nbsp;C |
| Operating temperature | -20°&nbsp;C to +60°&nbsp;C |

### Software

#### Mobile Application

- For Android
- For iOS

### Certification

<RkCertificationIcons certifications={[
    {
        'reach': 'https://downloads.rakwireless.com/LoRa/RAK2171/Certification/RAK2171_REACH_Report.pdf',
    },
    {
        'rohs': 'https://downloads.rakwireless.com/LoRa/RAK2171/Certification/RAK2171_RoHS_Report.pdf',
    },
    {
        'fcc': 'https://downloads.rakwireless.com/LoRa/RAK2171/Certification/RAK2171_FCC_Certification.pdf',
    },
    {
        'ised': 'https://downloads.rakwireless.com/LoRa/RAK2171/Certification/RAK2171_ISED_Certification.pdf',
    },
]} />



<RkBottomNav/>
