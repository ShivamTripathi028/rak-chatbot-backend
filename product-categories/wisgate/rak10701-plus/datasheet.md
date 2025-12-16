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

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

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
- Powered by a **3200**&nbsp;**mAh** rechargeable battery (USB Type-C charging).
- **External LoRa antenna** for improved performance.
- **OTAA** activation and **Class A** device operation.
- **BLE support** for wireless configuration and firmware upgrades via **WisToolBox Mobile App**.


## Specifications

This section summarizes the core physical, electrical, and radio features of the Field Tester Plus to support reliable LoRaWAN® testing across diverse environments.

### Hardware

#### Interfaces

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/datasheet/rak10701-plus-physical-interface.png"
  width="80%"
  caption="RAK10701-Plus Physical Interface"
/>

<table>
  <thead>
    <tr>
      <th>Interface</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Touchscreen LCD</b></td>
      <td>Main user interaction via TFT touchscreen.</td>
    </tr>
    <tr>
      <td><b>LoRa Antenna Port (RP-SMA)</b></td>
      <td>External antenna connection; comes with 2.0&nbsp;dBi and 2.3&nbsp;dBi antennas.</td>
    </tr>
    <tr>
      <td><b>Side Button</b></td>
      <td>Power On/Off, Sleep/Wake, Force Uplink.<br/>- <b>Turn ON</b>: Hold the button for 5 seconds.<br/>- <b>Turn OFF</b>: Hold the button for 5 seconds.<br/>- <b>Sleep/Wake Display</b>: Short press the button to toggle the display.<br/>- <b>Force Uplink</b>: Double press the button to trigger an uplink.</td>
    </tr>
    <tr>
      <td><b>USB-C Port</b></td>
      <td>Battery charging and device configuration.</td>
    </tr>
  </tbody>
</table>


#### Main Display

The Field Tester Plus provides real-time network insights on its screen, allowing users to monitor signal conditions and track historical performance data at specific locations, making it an invaluable tool for field testing.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/datasheet/rak10701-plus-screen-interface.png"
  width="80%"
  caption="RAK10701-Plus Screen Interface"
/>

**Main Display Sections Overview**

<table>
  <thead>
    <tr>
      <th>Section</th>
      <th>Name</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>1</b></td>
      <td>Device Status</td>
      <td>Displays the current connection status of the Field Tester Plus with the LoRaWAN network. Possible states include:<br/>- <b>Joining</b>: Attempting to connect to the network.<br/>- <b>Joined</b>: Successfully connected to the network.<br/>- <b>Sending</b>: Actively sending uplink packets.<br/>- <b>Failed</b>: Failed to connect or send; check device registration and gateway coverage.<br/>- <b>Idle</b>: Device is not actively communicating.<br/>Additional Info:<br/>- <b>Sent 4s ago</b>: Time elapsed since last uplink.<br/>- <b>Green text</b>: Last uplink was successful.<br/>- <b>Red text</b>: Last uplink failed.</td>
    </tr>
    <tr>
      <td><b>2</b></td>
      <td>Battery Level</td>
      <td>Displays the current battery percentage of the device. It helps monitor the battery status for timely recharging.</td>
    </tr>
    <tr>
      <td><b>3</b></td>
      <td>Uplink RF Parameters</td>
      <td>Displays radio signal quality metrics from the device to the gateway:<br/>- <b>RSSI</b> (Received Signal Strength Indicator)<br/>- <b>SNR</b> (Signal-to-Noise Ratio)<br/>- <b>Packet Loss</b> (uplink packet success rate).</td>
    </tr>
    <tr>
      <td><b>4</b></td>
      <td>Downlink RF Parameters</td>
      <td>Displays radio signal quality metrics from the gateway to the device via LinkCheck mode:<br/>- <b>RSSI</b><br/>- <b>SNR</b><br/>- <b>Packet Loss</b> (downlink packet success rate).</td>
    </tr>
    <tr>
      <td><b>5</b></td>
      <td>Gateway Distance (GPS required)</td>
      <td>Shows the estimated distance to the nearest and farthest gateways based on GPS location:<br/>- <b>Max Distance</b>: Farthest gateway (minimum unit 250&nbsp;meters).<br/>- <b>Min Distance</b>: Nearest gateway (minimum unit 250&nbsp;meters).<br/><b>Note</b>: GPS must be available for distance calculation.</td>
    </tr>
    <tr>
      <td><b>6</b></td>
      <td>Gateway Info</td>
      <td>Displays the number of gateways that received the uplink.<br/><b>Gateway EUI</b>: Shows part of the EUI (unique ID) of the nearest gateway to help identify it easily.<br/><b>Last Refresh</b>: Time since the last successfully processed uplink packet.</td>
    </tr>
    <tr>
      <td><b>7</b></td>
      <td>GPS Location</td>
      <td>Displays the real-time GPS coordinates of the device when outdoor signal is available.
Shows empty if GPS signal is unavailable.</td>
    </tr>
    <tr>
      <td><b>8</b></td>
      <td>Label</td>
      <td>Allows the user to tag and label the test location.<br/>- A test cycle (typically 50 packets) starts after labeling.<br/>- Labels are included in exported CSV reports for post-analysis.</td>
    </tr>
    <tr>
      <td><b>9</b></td>
      <td>Settings & Interval Control</td>
      <td>Allows control over uplink sending behavior and basic parameter configuration:<br/>- <b>Pause Icon</b>: Start or stop automatic uplinks.<br/>- <b>Gear Icon</b>: Open settings page to configure device parameters.<br/>- <b>Click RF metrics</b>: View the latest 15 historical values in a graph for trend observation. Metrics must be in green to be clickable</td>
    </tr>
  </tbody>
</table>

#### Basic Operation

This table outlines the user interactions with the device's side button and touchscreen interface.

<table>
  <thead>
    <tr>
      <th>Action</th>
      <th>Behavior</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Single Press</b></td>
      <td>Short press the side button to sleep/wake the screen.</td>
    </tr>
    <tr>
      <td><b>Double Press</b></td>
      <td>Double press the side button to force an uplink.</td>
    </tr>
    <tr>
      <td><b>Long Press</b></td>
      <td>Hold the side button to display the power-off option.</td>
    </tr>
    <tr>
      <td><b>Touch Green Text</b></td>
      <td>Tap the green text to view historical RF data for the selected metric.</td>
    </tr>
    <tr>
      <td><b>Touch Settings</b></td>
      <td>Tap to open settings and configure parameters or input labels.</td>
    </tr>
  </tbody>
</table>

#### RF Characteristics

**LoRaWAN Operating Frequencies​**

The RAK10701-Plus Field Tester for LoRaWAN supports the regional bands shown in the table below. When purchasing this device, pay attention to specifying the correct variant for your region.

<table>
  <thead>
    <tr>
      <th>Region</th>
      <th>Frequency Band</th>
      <th>Field Tester Plus Frequency (MHz)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Russia</b></td>
      <td>RU864</td>
      <th>8xx&nbsp;MHz version</th>
    </tr>
    <tr>
    <td><b>India</b></td>
      <td>IN865</td>
      <th>8xx&nbsp;MHz version</th>
      </tr>
      <tr>
    <td><b>Europe</b></td>
      <td>EU868</td>
      <th>8xx&nbsp;MHz version</th>
      </tr>
      <tr>
    <td><b>North America</b></td>
      <td>US915</td>
      <th>9xx&nbsp;MHz version</th>
      </tr>
      <tr>
    <td><b>Canada</b></td>
      <td>US915</td>
      <th>9xx&nbsp;MHz version</th>
      </tr>
      <tr>
    <td><b>Australia</b></td>
      <td>AU915</td>
      <th>9xx&nbsp;MHz version</th>
      </tr>
      <tr>
    <td><b>Korea</b></td>
      <td>KR920</td>
      <th>9xx&nbsp;MHz version</th>
      </tr>
      <tr>
    <td><b>Asia</b></td>
      <td>AS923-1/2/3/4</td>
      <th>9xx&nbsp;MHz version</th>
      </tr>
  </tbody>
</table>
**GPS Antenna**

<table>
  <thead>
    <tr>
      <th>Items</th>
      <th>Parameter</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Frequency</b></td>
      <td>1575.42&nbsp;MHz</td>
    </tr>
  </tbody>
</table>

#### Electrical Characteristics

<table>
  <thead>
    <tr>
      <th>Mode</th>
      <th>Condition</th>
      <th>Power Consumption</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Idle (LCD On)</b></td>
      <td>LCD is on</td>
      <td>120&nbsp;mA</td>
    </tr>
    <tr>
      <td><b>Idle (LCD Off)</b></td>
      <td>LCD is off</td>
      <td>60&nbsp;mA</td>
    </tr>
    <tr>
      <td><b>Battery</b></td>
      <td>3.7&nbsp;V, 3200&nbsp;mAh Li-ion rechargeable</td>
      <td>-</td>
    </tr>
    <tr>
      <td><b>Charging</b></td>
      <td>USB Type-C</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

#### Environmental Characteristics​
The table below lists the operation and storage temperature requirements.

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Min.</th>
      <th>Typical</th>
      <th>Max.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Storage Temp. Range</b></td>
      <td>-40°&nbsp;C</td>
      <td>+25°&nbsp;C</td>
      <td>+80°&nbsp;C</td>
    </tr>
    <tr>
      <td><b>Operation Temp. Range</b></td>
      <td>-10°&nbsp;C</td>
      <td>+25°&nbsp;C</td>
      <td>+60°&nbsp;C</td>
    </tr>
  </tbody>
</table>

#### Mechanical Characteristics

- Dimensions: 100&nbsp;mm x 75&nbsp;mm x 38&nbsp;mm
- Weight: approximately 8.6&nbsp;oz (244&nbsp;g) without battery

### Firmware

Download the latest <a href="https://downloads.rakwireless.com/#LoRa/RAK10701-Plus" target="_blank">firmware of RAK10701-Plus.</a>

<RkBottomNav/>