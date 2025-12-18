---
slug: /product-categories/wisgate/rak10701-plus/datasheet/
title: RAK10701-Plus Field Tester for LoRaWAN Datasheet
description: Access the technical specifications, devices interfaces, and other features of the Field Tester Plus for LoRaWAN. 
image: https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/physical-interface.png
keywords:
    - lorawan
    - field tester
    - rak10701-plus
    - datasheet
sidebar_label: Datasheet
tags:
  - rak10701-plus
  - field tester plus
  - network coverage solution
  - datasheet
date: 2025-05-23
---

# RAK10701-Plus Field Tester for LoRaWAN Datasheet

<!-- Reference the technical specifications, hardware features, and operational parameters of the Field Tester Plus device. -->

## Overview

### Description

The **RAK10701-Plus LoRaWAN Field Tester** is an advanced, all-in-one solution for comprehensive indoor and outdoor LoRaWAN network analysis. This powerful device offers real-time insights for both uplink and downlink signal quality (RSSI and SNR), packet loss rates and distance information from gateways using its built-in GPS receiver, making it an indispensable tool for network deployment and optimization.

The device operates independently, allowing you to tag and label testing locations via a touch screen LCD and intuitive UI display. You can also configure different parameters (DR, frequency band, power) directly on the device without the need for external apps, making the Field Tester Plus a flexible tool for checking LoRaWAN coverage on site.

In addition, it integrates seamlessly with the **Field Test Data Processor Extension** on WisGateOS 2 to perform backend calculations and analysis. As a bonus, it also supports data export in CSV format.

### Product Features

- Compatible with **LoRaWAN 1.0.3** across multiple bands: RU864, IN865, EU868, US915, AU915, KR920, and AS923-1/2/3/4.
- Supports **TTN, ChirpStack, AWS IoT Core for LoRaWAN**, and private networks using **WisGateOS 2** built-in Network Server (no Internet required).
- Real-time graphical display of **RSSI** and **SNR** for signal monitoring.
- Proprietary **packet loss calculation** for accurate coverage evaluation.
- Supports **manual location labeling** and **structured CSV data export**.
- Powered by a **3200** **mAh** rechargeable battery (USB Type-C charging).
- **External LoRa antenna** for improved performance.
- **OTAA** activation and **Class A** device operation.
- **BLE support** for wireless configuration and firmware upgrades via **WisToolBox Mobile App**.

## Specifications

This section summarizes the core physical, electrical, and radio features of the Field Tester Plus to support reliable LoRaWAN® testing across diverse environments.

### Hardware

#### Interfaces

> **Image:** RAK10701-Plus Physical Interface

| Interface | Description |
| --- | --- |
| Touchscreen LCD | Main user interaction via TFT touchscreen. |
| LoRa Antenna Port (RP-SMA) | External antenna connection; comes with 2.0 dBi and 2.3 dBi antennas. |
| Side Button | Power On/Off, Sleep/Wake, Force Uplink. - Turn ON : Hold the button for 5 seconds. - Turn OFF : Hold the button for 5 seconds. - Sleep/Wake Display : Short press the button to toggle the display. - Force Uplink : Double press the button to trigger an uplink. |
| USB-C Port | Battery charging and device configuration. |

#### Main Display

The Field Tester Plus provides real-time network insights on its screen, allowing users to monitor signal conditions and track historical performance data at specific locations, making it an invaluable tool for field testing.

> **Image:** RAK10701-Plus Screen Interface

**Main Display Sections Overview**

| Section | Name | Description |
| --- | --- | --- |
| 1 | Device Status | Displays the current connection status of the Field Tester Plus with the LoRaWAN network. Possible states include: - Joining : Attempting to connect to the network. - Joined : Successfully connected to the network. - Sending : Actively sending uplink packets. - Failed : Failed to connect or send; check device registration and gateway coverage. - Idle : Device is not actively communicating. Additional Info: - Sent 4s ago : Time elapsed since last uplink. - Green text : Last uplink was successful. - Red text : Last uplink failed. |
| 2 | Battery Level | Displays the current battery percentage of the device. It helps monitor the battery status for timely recharging. |
| 3 | Uplink RF Parameters | Displays radio signal quality metrics from the device to the gateway: - RSSI (Received Signal Strength Indicator) - SNR (Signal-to-Noise Ratio) - Packet Loss (uplink packet success rate). |
| 4 | Downlink RF Parameters | Displays radio signal quality metrics from the gateway to the device via LinkCheck mode: - RSSI - SNR - Packet Loss (downlink packet success rate). |
| 5 | Gateway Distance (GPS required) | Shows the estimated distance to the nearest and farthest gateways based on GPS location: - Max Distance : Farthest gateway (minimum unit 250 meters). - Min Distance : Nearest gateway (minimum unit 250 meters). Note : GPS must be available for distance calculation. |
| 6 | Gateway Info | Displays the number of gateways that received the uplink. Gateway EUI : Shows part of the EUI (unique ID) of the nearest gateway to help identify it easily. Last Refresh : Time since the last successfully processed uplink packet. |
| 7 | GPS Location | Displays the real-time GPS coordinates of the device when outdoor signal is available. Shows empty if GPS signal is unavailable. |
| 8 | Label | Allows the user to tag and label the test location. - A test cycle (typically 50 packets) starts after labeling. - Labels are included in exported CSV reports for post-analysis. |
| 9 | Settings & Interval Control | Allows control over uplink sending behavior and basic parameter configuration: - Pause Icon : Start or stop automatic uplinks. - Gear Icon : Open settings page to configure device parameters. - Click RF metrics : View the latest 15 historical values in a graph for trend observation. Metrics must be in green to be clickable |

#### Basic Operation

This table outlines the user interactions with the device's side button and touchscreen interface.

| Action | Behavior |
| --- | --- |
| Single Press | Short press the side button to sleep/wake the screen. |
| Double Press | Double press the side button to force an uplink. |
| Long Press | Hold the side button to display the power-off option. |
| Touch Green Text | Tap the green text to view historical RF data for the selected metric. |
| Touch Settings | Tap to open settings and configure parameters or input labels. |

#### RF Characteristics

**LoRaWAN Operating Frequencies​**

The RAK10701-Plus Field Tester for LoRaWAN supports the regional bands shown in the table below. When purchasing this device, pay attention to specifying the correct variant for your region.

| Region | Frequency Band | Field Tester Plus Frequency (MHz) |
| --- | --- | --- |
| Russia | RU864 | 8xx MHz version |
| India | IN865 | 8xx MHz version |
| Europe | EU868 | 8xx MHz version |
| North America | US915 | 9xx MHz version |
| Canada | US915 | 9xx MHz version |
| Australia | AU915 | 9xx MHz version |
| Korea | KR920 | 9xx MHz version |
| Asia | AS923-1/2/3/4 | 9xx MHz version |

**GPS Antenna**

| Items | Parameter |
| --- | --- |
| Frequency | 1575.42 MHz |

#### Electrical Characteristics

| Mode | Condition | Power Consumption |
| --- | --- | --- |
| Idle (LCD On) | LCD is on | 120 mA |
| Idle (LCD Off) | LCD is off | 60 mA |
| Battery | 3.7 V, 3200 mAh Li-ion rechargeable | - |
| Charging | USB Type-C | - |

#### Environmental Characteristics​
The table below lists the operation and storage temperature requirements.

| Parameter | Min. | Typical | Max. |
| --- | --- | --- | --- |
| Storage Temp. Range | -40° C | +25° C | +80° C |
| Operation Temp. Range | -10° C | +25° C | +60° C |

#### Mechanical Characteristics

- Dimensions: 100 mm x 75 mm x 38 mm
- Weight: approximately 8.6 oz (244 g) without battery

### Firmware

Download the latest [firmware of RAK10701-Plus.](https://downloads.rakwireless.com/#LoRa/RAK10701-Plus)

