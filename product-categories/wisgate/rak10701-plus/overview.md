---
slug: /product-categories/wisgate/rak10701-plus/overview/
title: RAK10701-Plus Field Tester for LoRaWAN
description: RAK10701-Plus Field Tester for LoRaWAN is an advanced, all-in-one solution for comprehensive indoor and outdoor LoRaWAN network analysis. This powerful device offers real-time insights for both uplink and downlink signal quality (RSSI and SNR), packet loss rates and distance information from gateways using its built-in GPS/GNSS receiver.
image: https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/physical-interface.png
keywords:
    - lorawan
    - field tester plus
    - rak10701-plus
sidebar_label: Field Tester Plus Overview
tags:
  - rak10701-plus
  - field tester plus
  - network coverage solution
date: 2025-05-23
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK10701-Plus Field Tester for LoRaWAN

**Quick Navigation**

This section introduces the Field Tester Plus device, its key features, system components, and how it integrates into LoRaWAN testing workflows. Here's the list of guides to help you quickly find the information you need:

<table>
  <thead>
    <tr>
      <th>Guide</th>
      <th>Definition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b><a href="https://docs.rakwireless.com/product-categories/wisgate/rak10701-plus/network-setup/" target="_blank">Pre-Test Network Setup</a></b></td>
      <td>Step-by-step instructions to set up the Field Tester Plus device, gateway, and network environment before testing.</td>
    </tr>
    <tr>
      <td><b><a href="https://docs.rakwireless.com/product-categories/wisgate/rak10701-plus/field-test/" target="_blank">Conduct Field Tests with Field Tester Plus</a></b></td>
      <td>Detailed workflows for performing field tests, analyzing real-time metrics, and exporting structured reports.</td>
    </tr>
    <tr>
      <td><b><a href="https://docs.rakwireless.com/product-categories/wisgate/rak10701-plus/firmware-update/" target="_blank">Firmware Update</a></b></td>
      <td>How to upgrade the device firmware via USB or Bluetooth to access new features and performance improvements.</td>
    </tr>
    <tr>
      <td><b><a href="https://docs.rakwireless.com/product-categories/wisgate/rak10701-plus/datasheet/" target="_blank">Datasheet</a></b></td>
      <td>Technical specifications, device interfaces, electrical characteristics, and environmental parameters.</td>
    </tr>
    <tr>
      <td><b><a href="https://docs.rakwireless.com/product-categories/wisgate/rak10701-plus/faqs-troubleshooting/" target="_blank">FAQs & Troubleshooting</a></b></td>
      <td>Solutions to common issues, explanations of key concepts, and guidance for optimizing test results.</td>
    </tr>
    <tr>
      <td><b><a href="https://docs.rakwireless.com/product-categories/wisgate/rak10701-plus/glossary/" target="_blank">Glossary of Key Terms</a></b></td>
      <td>Quick reference for important terms and metrics used throughout the guide.</td>
    </tr>
  </tbody>
</table>



## What is Field Tester Plus？

The **RAK10701-Plus LoRaWAN Field Tester** is an advanced, all-in-one solution for comprehensive indoor and outdoor LoRaWAN network analysis. This powerful device offers real-time insights for both uplink and downlink signal quality (RSSI and SNR), packet loss rates and distance information from gateways using its built-in GPS receiver, making it an indispensable tool for network deployment and optimization.

The device operates independently, allowing you to tag and label testing locations via a touch screen LCD and intuitive UI display. You can also configure different parameters (DR, frequency band, power) directly on the device without the need for external apps, making the Field Tester Plus a flexible tool for checking LoRaWAN coverage on site.

In addition, it integrates seamlessly with the **Field Test Data Processor Extension** on WisGateOS 2 to perform backend calculations and analysis. As a bonus, it also supports data export in CSV format.

### Key Features

- Compatible with **LoRaWAN 1.0.3** across multiple bands: RU864, IN865, EU868, US915, AU915, KR920, and AS923-1/2/3/4.
- Supports **TTN, ChirpStack, AWS IoT Core for LoRaWAN**, and private networks using **WisGateOS 2** built-in Network Server (no Internet required).
- Real-time graphical display of **RSSI** and **SNR** for signal monitoring.
- Proprietary **packet loss calculation** for accurate coverage evaluation.
- Supports **manual location labeling** and **structured CSV data export**.
- Powered by a **3200&nbsp;mAh** rechargeable battery (USB Type-C charging).
- **External LoRa antenna** for improved performance.
- **OTAA** activation and **Class A** device operation.
- **BLE support** for wireless configuration and firmware upgrades via **WisToolBox Mobile App**.


### System Components

<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Field Tester Plus</b></td>
      <td>A handheld LoRaWAN end device that sends uplinks and displays real-time metrics like RSSI and SNR.</td>
    </tr>
    <tr>
      <td><b>LoRaWAN Gateway</b></td>
      <td>Receives uplinks and forwarders them to the configured LoRaWAN Network Server (LNS).<br/><b>Supported LNS options include:</b><ul><li>Built-in LNS (on RAK WisGateOS 2)</li><li>The Things Network (TTN) / The Things Industries (TTI)</li><li>ChirpStack v3 / v4</li><li>AWS IoT Core for LoRaWAN</li></ul></td>
    </tr>
    <tr>
      <td><b>Field Test Data Processor Extension</b></td>
      <td>Installs on your RAK gateway to enable <b>local signal processing</b>. It computes key quality metrics—such as RSSI, SNR, and packet loss—and exports structured test reports (e.g., CSV), <b>without relying on any cloud integration.</b></td>
    </tr>
    </tbody>
</table>


## How It Works?

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/overview/field-tester-roadmap.png"
  width="100%"
  caption="Field Tester Roadmap"
/>

1. **Field Testing**<br/>The Field Tester Plus sends uplinks at regular intervals, containing GPS or manually labeled location data.

2. **Network Server Forwarding**<br/>Nearby LoRaWAN gateways receive the uplinks and forward them to the configured LNS (e.g., TTN, ChirpStack, AWS IoT Core, or the built-in LNS in RAK gateways).

3. **Data Processing with Extension**<br/>If the gateway is a RAK model running **WisGateOS 2** and has the **Field Test Data Processor Extension** installed, it will subscribe to uplink messages via MQTT and perform local analysis. This enables:
   
    <ul><li>Real-time metric calculation for both uplink and downlink (RSSI, SNR, packet loss, gateway info)</li><li>Exportable CSV reports</li><li>Heatmap visualization of signal metrics (RSSI, SNR)</li></ul>

:::tip NOTE
Without the Extension, signal analysis is limited to basic downlink responses only (see **Work Modes** below).
:::

4. **Data Viewing**<br/>Depending on your configuration, test results can be:
   
    <ul><li>Realtime display directly on the device screen</li><li>Exported as structured CSV logs (with Extension)</li><li>Visualized as heatmaps (with Extension)</li><li>Sent to external application servers (with LNS integration)</li></ul>

**Work Modes**

Field Tester Plus offers two operational modes, depending on whether the Field Test Data Processor Extension is installed and properly connected:

<table>
  <thead>
    <tr>
      <th>Mode</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Field Tester Mode</b></td>
      <td>Full-feature mode. The gateway runs the Field Test Data Processor Extension, which analyzes uplinks locally via MQTT and feeds results back to the device.<br/> Displays both <b>uplink and downlink metrics</b>, including <b>RSSI, SNR, packet loss</b>, distance (if GPS is available), and allows <b>CSV export</b> and heatmap generation.</td>
    </tr>
    <tr>
      <td><b>LinkCheck Mode</b></td>
      <td>Basic mode. The device has joined an LNS, but no Extension is installed or configured.<br/> Only basic downlink information is shown: <b>RSSI, SNR</b>, and <b>number of receiving gateways</b>, based on LinkCheck MAC responses. No uplink metrics or CSV export is available.</td>
    </tr>
    </tbody>
</table>


## Why Use Field Tester Plus?

Most LoRaWAN field testers depend on GPS and cloud processing, which often fail in indoor or GPS-denied environments.
**Field Tester Plus**, combined with the **Field Test Data Processor Extension** on a RAK gateway, solves this by enabling:

- **Real-time signal insights** **–** See RSSI, SNR, and packet loss as you test
- **Quickly check network health** **–** Evaluate coverage and performance on the spot
- **Standalone, no phone needed** **–** Works fully on its own with a touch screen
- **Durable and compact design** **–** Built for rugged outdoor and indoor environments
- **Plug-and-play compatibility** **–** Supports WisGateOS2 Built-in LNS, TTN/TTI, Chirpstack v3 / v4, and AWS IoT Core for LoRaWAN

### Typical Applications

Field Tester Plus is ideal for a variety of real-world LoRaWAN validation scenarios:

- **Field Deployments**: Measure and verify LoRaWAN coverage in open or remote outdoor environments.
- **Indoor Signal Validation**: Test network performance in buildings such as factories, offices, or underground areas where GPS is unavailable.
- **Pre-Deployment Testing**: Evaluate signal quality before installing a gateway to ensure proper placement and optimal coverage.

<RkBottomNav/>