---
slug: /product-categories/wisgate/rak7240v2/overview/
title: RAK7240V2/RAK7240CV2 WisGate Edge Prime
description: RAK7240V2 has a built-in GPS module and LoRa Server. This gateway supports multiple backhaul connectivity options such as WiFi, LTE, and Ethernet with an available SD card slot to back up the gathered data. The enclosure is IP rated, dustproof and waterproof, and with a built-in surge protection.
image: "https://images.docs.rakwireless.com/wisgate/rak7240-v2/rak7240v2.png"
keywords:
    - Outdoor Gateway
    - RAK7240CV2
    - wisgate
    - LoRaWAN gateway
    - Outdoor LoRaWAN Gateway
sidebar_label: Product Overview
---

# RAK7240V2/RAK7240CV2 WisGate Edge Prime

Thank you for choosing **RAK7240V2/RAK7240CV2 WisGate Edge Prime** in your awesome IoT Project! 🎉 To help you get started, we have provided you with all the necessary information for your product.

**Product documentation**

* [Quick Start Guide](/product-categories/wisgate/rak7240v2/quickstart/)
* [LoRaWAN Network Server Guide](/product-categories/wisgate/rak7240v2/lorawan-network-server-guide/)
* [Datasheet](/product-categories/wisgate/rak7240v2/datasheet/)

For more related tutorials, you can refer to [Quick Start Guide >Tutorials](https://docs.rakwireless.com/product-categories/wisgate/rak7240v2/quickstart/#tutorials).

**Resources**

- For more information, check the [Frequently Asked Questions for WisGate Edge](https://learn.rakwireless.com/hc/en-us/articles/28700873891223-Essential-IoT-Gateway-Setup-A-Q-A-Guide-for-WisGate-Edge-Series-of-Gateways).
- Visit the [RAKwireless Forum](https://forum.rakwireless.com/) for specialized assistance from the RAKstars community and RAKwireless experts.
- Check our extensive collection of [How-To Guides](https://learn.rakwireless.com/hc/en-us) to get inspiration on exciting new use cases.
- Need more specialized product assistance? Contact [RAKwireless Support](https://www.rakwireless.com/en-us/contact-us).

:::info IMPORTANT NOTE
The new RAK7240V2/RAK7240CV2 gateway now replaces the RAK7240. You can still browse the product information of [RAK7240](https://docs.rakwireless.com/product-categories/wisgate/rak7240/overview/).
:::

## Product Description

The **RAK7240V2 WisGate Edge Prime** is ideal for large-scale LPWAN deployments where cost is essential, without compromising quality. The gateway is available in 8 or 16-channel versions to help you utilize the maximum number of available LoRaWAN channels in your region. It supports multi-backhaul with Ethernet, WiFi, and cellular connectivity.

This gateway operates on [WisGateOS 2](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#overview), a secure and flexible operating system based on the latest OpenWrt kernel. It supports extension modules for enhanced customization, and offers centralized remote management and configuration via [WisDM,](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/) making it an ideal choice for managing large networks of gateways.

Its wide range of customization options allows for flexibility when deploying a solution. It is suited for any use-case scenario, whether it's rapid deployment or customization regarding UI and functionality. The flat surface of the full-metal enclosure allows your logo to be added for brand customization and recognition.

## Product Features

### Hardware

- IP65 industrial-grade enclosure with cable glands
- PoE (802.3af) + Surge Protection
- Up to two (2) LoRa concentrators for 8 or 16-channel options
- Multi-backhaul options:
  - Ethernet
  - Wi-Fi
  - LTE (*LTE available on 8-channel RAK7240CV2 only*)
- GPS
- Power variants:
  + PoE-only version
  + DC-input version (supports 9–24 V<sub>DC</sub>, RAK Battery Plus)
- External antennas for WiFi, GPS, LTE (optional, available with RAK7240CV2), and LoRa

### Software

- [WisGateOS 2](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#overview/): The OS for configuring and managing RAK gateways
- **WisGateOS 2 Extensions**: Adds support for features such as OpenVPN, WireGuard VPN, and more. Use the appropriate installation guide based on your WisGateOS 2 version:
    - [For WisGateOS 2 version 2.2.x or later](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/)
    - [For WisGateOS 2 versions 2.0.x and 2.1.x](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/)
- Remote management with [WisDM](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/) Fleet Management
- Built-in **Network Server** (LoRaWAN support v1.0.3)
- LoRaWAN Stack support with Semtech SX1303
- **LoRa Frame Filtering** (node whitelisting in Packet Forwarder mode)
- **MQTT v3.1 Bridging** with **TLS encryption**
- Fine timestamping (optional)
- LoRa frame buffering in **Packet Forwarder mode** in case of NS outage, ensuring **no data loss**

## Model Variants Overview

| **Gateway  Model** | **LoRa  Channels** | **Power  Option** | **Cellular**  |
|--------------------|--------------------|-------------------|---------------|
| RAK7240V2          | 8                  | PoE + DC Input    | Not supported |
| RAK7240V2          | 8                  | PoE only          | Not supported |
| RAK7240V2          | 16                 | PoE + DC Input    | Not supported |
| RAK7240V2          | 16                 | PoE only          | Not supported |
| RAK7240CV2         | 8                  | PoE + DC Input    | LTE-enabled   |
| RAK7240CV2         | 8                  | PoE only          | LTE-enabled   |

## Software and Services

### WisGateOS 2

The latest unified operating system for RAK gateways offers a feature-rich environment to access and configure the LoRaWAN gateway. WisGateOS 2 is built on the latest OpenWrt kernel for enhanced security. It employs a simplified user interface that improves usability and programmability. Integrated with WisDM, it enables remote management of gateways and firmware. With its extensibility, you can add additional features and functions to your gateways.

For more information, refer to [WisGateOS 2 User Manual](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#overview).

### WisGateOS 2 Extensions

WisGateOS 2 features an extension functionality, that allows features and functions be added, removed, or updated based on your needs. For more information, refer to [WisGateOS 2 Extensions](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/overview/#overview).

### WisDM

WisDM is a RAKwireless cloud-based device management platform designed to help you optimize the ways of controlling your gateways. The WisDM device management software supports IoT networks of any scale built around commercial-grade LoRaWAN Edge gateways from RAKwireless. Additionally, the WisDM platform offers you remote configuration, OTAA updates, and scalable management.

For more information, refer to [WisDM](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/).
