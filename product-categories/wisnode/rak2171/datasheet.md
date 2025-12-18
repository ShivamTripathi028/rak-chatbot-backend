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

# RAK2171 WisNode TrackIt Datasheet

## Overview

> **Image:** RAK2171 WisNode TrackIt

### Description

**RAK2171 WisNode TrackIt** is RAKwireless’ latest LoRaWAN GPS tracking device. It comes in a small form factor with rechargeable battery and tracking and configuration application, available for iOS and Android devices.

RAK2171 supports multiple working modes and notification options. When used with RAK WisGate Edge gateways and in P2P mode, you can monitor your tracker on the application map, create geofences, and receive SOS and movement notifications. You can also configure the WisNode TrackIt to work with any third-party LoRaWAN network using the TrackIt application as a configuration tool.

### Features

- MT2523 with built-in Bluetooth and GPS
- SX1262 LoRa chip
- Built-in accelerometer
- Built-in battery: 400 mAh
- Charger with a magnetic plate
- Small size: 42 x 42 x 18 mm
- Low weight: 25 g
- Operating temperature: -20° C to +60° C
- IP65 rating
- Android and iOS application for easy management, configuration, and location tracking

## Specifications

### Overview

#### Board Overview

> **Image:** RAK2171 WisNode TrackIt Dimensions

| Parameter             | Value                                                                  |
| --------------------- | ---------------------------------------------------------------------- |
| Dimensions            | 42 x 42 x 18 mm                                                   |
| Weight                | 25 g                                                              |
| Operating temperature | -20° C to +60° C                                             |
| Battery capacity      | 400 mAh                                                           |
| Color                 | Tracker: White / Dark Grey 
 Charger: Black                       |
| Charger               | 5-pin Magnetic Plate 
 USB Type-A 
 Cable Length: 50 cm |

### Hardware

The hardware specification is categorized into five (5) parts. It covers the interfacing and the standard values and requirements, such as the RF, electrical, and environmental of the RAK2171 WisNode TrackIt.

#### Interfaces

> **Image:** RAK2171 WisNode TrackIt Interfaces

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
| Communication | Bluetooth V4.2 (for configuration) 
 LoRa (data transmission) |

#### Antennas

The RAK2171 WisNode TrackIt has built-in LoRaWAN, GPS, and Bluetooth antennas.

#### Electrical Characteristics

| Parameter        | Value              |
| ---------------- | ------------------ |
| Battery Type     | Lithium            |
| Battery Capacity | 400 mAh       |
| Charging         | 5 V, 1 A |

#### Environmental Requirements

| Parameter             | Value                      |
| --------------------- | -------------------------- |
| Charging temperature  | +10° C to +45° C |
| Operating temperature | -20° C to +60° C |

### Software

#### Mobile Application

- For Android
- For iOS

### Certification

### Certifications
- **REACH:** https://downloads.rakwireless.com/LoRa/RAK2171/Certification/RAK2171_REACH_Report.pdf
- **ROHS:** https://downloads.rakwireless.com/LoRa/RAK2171/Certification/RAK2171_RoHS_Report.pdf
- **FCC:** https://downloads.rakwireless.com/LoRa/RAK2171/Certification/RAK2171_FCC_Certification.pdf
- **ISED:** https://downloads.rakwireless.com/LoRa/RAK2171/Certification/RAK2171_ISED_Certification.pdf

