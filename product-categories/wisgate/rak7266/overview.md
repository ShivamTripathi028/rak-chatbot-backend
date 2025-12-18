---
slug: /product-categories/wisgate/rak7266/overview/
title: RAK7266 WisGate Soho Lite
description: RAK7266 WisGate Soho Lite features 8 LoRa channels, integrated LTE Cat 1 connectivity with an external antenna, WiFi AP mode, and WisGateOS 2 based on OpenWrt — ideal for compact indoor deployments.
image: "https://images.docs.rakwireless.com/wisgate/rak7266/rak7266.png"
keywords:
    - Indoor gateway
    - lorawan gateway
    - WisGate Soho Lite
    - Indoor LoRaWAN gateway
    - SX1302
tags:
  - rak7266
  - wisgate
  - overview
sidebar_label: Product Overview
date: 2026-06-26
---

# RAK7266 WisGate Soho Lite

Thank you for choosing **RAK7266 WisGate Soho Lite** in your awesome IoT Project! 🎉 To help you get started, we have provided you with all the necessary information for your product.

**Product documentation**

* [Quick Start Guide](/product-categories/wisgate/rak7266/quickstart/)
* [LoRaWAN Network Server Guide](/product-categories/wisgate/rak7266/lorawan-network-server-guide/)
* [Datasheet](/product-categories/wisgate/rak7266/datasheet/)

**Resources**

- For more information, check the <a href="https://learn.rakwireless.com/hc/en-us/articles/28700873891223-Essential-IoT-Gateway-Setup-A-Q-A-Guide-for-WisGate-Edge-Series-of-Gateways" target="_blank">Frequently Asked Questions for WisGate Edge</a>.
- Check out the extensive collection of <a href="https://learn.rakwireless.com/hc/en-us?utm_source=docs_center&utm_medium=organic&utm_campaign=rak7266-documentation-overview-page&utm_term=applications-and-tutorials&utm_content_learn-link" target="_blank">Applications & Tutorials</a> to get inspiration on new use cases.
- Visit the <a href="https://forum.rakwireless.com/?utm_source=docs_center&utm_medium=organic&utm_campaign=rak7266-documentation-overview-page&utm_term=rakwireless-forum&utm_content_forum-link" target="_blank">RAKwireless Forum</a> for a specialized assistance from the RAKstars community and RAKwireless experts.
- For a more specialized product assistance, contact <a href="https://www.rakwireless.com/en-us/contact-us?utm_source=docs_center&utm_medium=organic&utm_campaign=rak7266-documentation-overview-page&utm_term=rakwireless-support&utm_content_text-link" target="_blank">RAKwireless Support</a>.

## Product Description

The **RAK7266 WisGate Soho Lite** is an indoor LoRaWAN gateway from the **RAK Soho Series**, designed for versatile and compact IoT deployments. It comes with an **integrated LTE Cat 1 module** and offers **multiple backhaul options**, including **cellular (LTE)**, **WiFi**, and **Ethernet**, ensuring versatile deployment options in environments with or without wired internet access.

This gateway supports **8 LoRa channels** and onboards **2.4 GHz WiFi** for easy configuration through the default WiFi AP mode. An **Ethernet port** is available for wired network access when needed. The device is powered via a **stable 12 V DC input**, making it well-suited for controlled indoor environments such as smart panels, utility cabinets, or fixed installations.

Depending on the variant, LTE antennas may be **internal** or **externally connected via RP-SMA connectors**, allowing users to select the best option for signal conditions and installation constraints.

The RAK7266 runs on **WisGateOS 2**, a secure, modular firmware based on OpenWrt developed by RAK. It provides access to a wide range of features, including extension modules, a built-in LoRaWAN Network Server, and advanced system diagnostics. Additionally, it supports integration with **WisDM** for centralized management and fleet monitoring, making it a powerful and practical solution for LTE-based indoor deployments.

## Product Features

### Hardware

- **8 LoRa channels**
- Supports **2.4 GHz WiFi**, with **AP mode enabled by default** for easy configuration
- **100M Base-T Ethernet port** (for network access, no PoE)
- **RP-SMA** LoRa antenna connector
- An integrated **LTE Cat 1 module** for cellular backhaul
- Multi backhaul options with **Ethernet, WiFi, and Cellular**
- **Breathing light** for visual status indication

### Software

- **[WisGateOS 2](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/?intsource=docs_center&intmedium=organic&intcampaign=rak7266_documentation_overview_page&intterm=wisgate_os2&intcontent=documentation_link)**: A secure, OpenWrt-based OS developed by RAK for enhanced stability and flexibility.
- **Extension add-ons** for customized gateway functionality:
  - <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/" target="_blank">Compatible with WisGateOS 2 version 2.2.x or later</a>
  - <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/" target="_blank">Compatible with WisGateOS 2 versions 2.0.x and 2.1.x</a>
- **[WisDM](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/?intsource=docs_center&intmedium=organic&intcampaign=rak7266_documentation_overview_page&intterm=wisdm&intcontent=documentation_link)** for remote management and monitoring
- Built-in **Network Server**
- **Basic Station** and **Packet Forwarder** modes
- **LoRa Frame Filtering** (node whitelisting in Packet Forwarder mode)
- **MQTT v3.1 Bridging** with **TLS encryption**
- LoRa frame buffering in **Packet Forwarder mode** in case of NS outage, ensuring **no data loss**

## Field Applications

**The RAK7266 WisGate Soho Lite** is well-suited for a variety of indoor IoT applications that require reliable wireless connectivity and flexible backhaul options. Its compact form factor and multi-interface support—including LTE, WiFi, and Ethernet—make it ideal for deployment in residential, commercial, and utility environments.

:::tip NOTE
The following scenarios and applications are only examples. The field applications of LoRaWAN gateway are very extensive, including but not limited to these examples.
:::

### Smart Home
  Secure and connect devices beyond traditional wireless range:

  + Garage door control
  + Outdoor lighting
  + Leak detection
  + Pet geofencing

### Smart Buildings
  Enhance building management and operational efficiency with:

  + Temperature and humidity monitoring
  + Electricity consumption metering
  + Ventilation system monitoring

### Utilities
  Support infrastructure automation and real-time diagnostics through:

  + Water and electricity usage reporting
  + Leak detection in pipelines
  + Pressure and temperature monitoring in gas systems

## Software and Services

### WisGateOS 2

The latest unified operating system for RAK gateways offers a feature-rich environment to access and configure the LoRaWAN gateway. WisGateOS 2 is built on the latest OpenWrt kernel for enhanced security. It employs a simplified user interface that improves usability and programmability. Integrated with WisDM, it enables remote management of gateways and firmware. With its extensibility, you can add additional features and functions to your gateways. For more information, refer to <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/?intsource=docs_center&intmedium=organic&intcampaign=rak7266_documentation_overview_page&intterm=wisgate_os2&intcontent=documentation_link" target="_blank">WisGateOS 2 User Manual</a>.

### WisGateOS 2 Extensions

WisGateOS 2 features an extension functionality that allows features and functions be added, removed, or updated based on your needs. For more information, refer to <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/overview/?intsource=docs_center&intmedium=organic&intcampaign=rak7266_documentation_overview_page&intterm=extension-add-ons&intcontent=documentation_link" target="_blank">WisGateOS 2 Extensions</a>.

### WisDM

WisDM is a cloud-based device management platform specifically designed to help you optimize the ways of controlling your gateways. The WisDM device management software supports IoT networks of any scale built around commercial-grade LoRaWAN Edge gateways from RAKwireless. Additionally, the WisDM platform offers you remote configuration, OTAA updates, and scalable management. For more information, refer to <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/?intsource=docs_center&intmedium=organic&intcampaign=rak7266_documentation_overview_page&intterm=wisdm&intcontent=documentation_link" target="_blank">WisDM</a>.

## Indoor Gateway Family

RAK offers a diverse range of indoor gateways designed to meet various connectivity and deployment needs. These gateways provide reliable, high-performance solutions for different use cases, incorporating advanced connectivity options such as LTE, WiFi, and LoRa. Below is an overview of key indoor gateways in the RAK product family:

| Feature                        | RAK7268V2 / RAK7268CV2 
WisGate Edge Lite 2                                                                                                                                      | RAK7266
WisGate Soho Lite                                                                                                            |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **Product Image**              | <img src="https://images.docs.rakwireless.com/wisgate/rak7268-v2/rak7268v2.png" alt="RAK7268V2" width="50%" />                                                                        | <img src="https://images.docs.rakwireless.com/wisgate/rak7266/rak7266.png" alt="RAK7266" width="50%" />                                   |
| **LoRa Features**              | <ul><li>SX1302 with 8 channels</li><li>RX Sensitivity: −139 dBm (Min)</li><li>TX Power: 27 dBm (Max)</li></ul>                                                              | <ul><li>SX1302 with 8 channels</li><li>RX Sensitivity: −139 dBm (Min)</li><li>TX Power: 27 dBm (Max)</li></ul>                  |
| **Frequency Bands**            | EU868, IN865, US915, AU915, KR920, AS923-1/2/3/4, EU433, CN470                                                                                                                        | EU868, IN865, US915, AU915, KR920, AS923-1/2/3/4, EU433, CN470                                                                            |
| **Cellular Connectivity**      | <ul><li>Available with RAK7268CV2, LTE Cat 4 (IoT/M2M-optimized)</li><li>Supports EG95-E, EG95-NA, EC25-J, EC25-AU, EC25-E</li></ul>                                                  | <ul><li>LTE Cat 1 (IoT/M2M-optimized)</li><li>Supports EG915U-EU, EG915U-LA, EG915Q-NA</li></ul>                                          |
| **WiFi**                      | <ul><li>2.4 GHz (802.11b/g/n)</li><li>Operation Channels: 1-13</li></ul>                                                                                                         | <ul><li>2.4 GHz (802.11b/g/n)</li><li>Operation Channels: 1-13</li></ul>                                                             |
| **Multi-Network Connectivity** | Ethernet, WiFi, LTE                                                                                                                                                                  | Ethernet, WiFi, LTE                                                                                                                      |
| **Power Supply**               | PoE (IEEE 802.3 af):<ul><li>36-57 V<sub>DC</sub></li><li>12 V<sub>DC</sub> (depending on the version)</li><li>9-24 V<sub>DC</sub> (depending on the version)</li></ul> | 12 V<sub>DC</sub>                                                                                                                    |
| **GPS**                        | Not supported                                                                                                                                                                         | Not supported                                                                                                                             |
| **Antenna**                    | <ul><li>LoRa: External antenna</li><li>WiFi: Internal antenna</li><li>LTE: Internal or External antenna (depending on version)</li></ul>                                             | <ul><li>LoRa: External antenna</li><li>WiFi: Internal antenna</li><li>LTE: Internal or External antenna (depending on version)</li></ul> |
| **Ingress Protection**         | IP30                                                                                                                                                                                  | IP30                                                                                                                                      |
| **Enclosure Material**         | Plastic (PC+ABS)                                                                                                                                                                      | Plastic (PC+ABS)                                                                                                                          |
| **Dimensions (Gateway Only)**  | 166 mm x 127.5 mm x 36 mm                                                                                                                                              | 166 mm x 127.5 mm x 36 mm                                                                                                  |
| **Operating Temperature**      | −10˚ C to +55˚ C                                                                                                                                                            | −10˚ C to +55˚ C                                                                                                                |
| **Storage Temperature**        | −40˚ C to +85˚ C                                                                                                                                                            | −40˚ C to +85˚ C                                                                                                                |
| **Operating Humidity**         | 0-95% RH (non-condensing)                                                                                                                                                             | 0-95% RH (non-condensing)                                                                                                                 |
| **Storage Humidity**           | 0-95% RH (non-condensing)                                                                                                                                                             | 0-95% RH (non-condensing)                                                                                                                 |
| **Installation Methods**       | Desktop, Wall (via included bracket), Rail (via included bracket)                                                                                                                     | Desktop, Wall (via included bracket), Rail (via included bracket)                                                                         |

