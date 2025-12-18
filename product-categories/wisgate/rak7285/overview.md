---
title: RAK7285 WisGate Edge Ultra
description: RAK7285 WisGate Edge Ultra is a full duplex IoT gateway with 8 LoRa channels, multi-backhaul options, and OpenWrt-based WisGateOS 2, ideal for IoT commercial deployment.
image: "https://images.docs.rakwireless.com/wisgate/rak7285/rak7285.png"
keywords:
    - WisGate Edge Ultra
    - Cavity Filter
    - openwrt LoRaWAN
    - LoRaWAN gateway
    - full duplex gateway
sidebar_label: Overview
download: true
---

#  RAK7285/RAK7285C WisGate Edge Ultra

Thank you for choosing **RAK7285/RAK7285C WisGate Edge Ultra** in your awesome IoT Project! 🎉 To help you get started, we have provided you with all the necessary information for your product.

**Product documentation**

* [Quick Start Guide](https://docs.rakwireless.com/product-categories/wisgate/rak7285/quickstart/)
* [LoRaWAN Network Server Guide](https://docs.rakwireless.com/product-categories/wisgate/rak7285/lorawan-network-server-guide/)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisgate/rak7285/datasheet/)

For more related tutorials, check the [Tutorials](https://docs.rakwireless.com/product-categories/wisgate/rak7285/quickstart/#tutorials) section of the Quick Start Guide.

**Resources**

- For more information, check the [Frequently Asked Questions](https://learn.rakwireless.com/hc/en-us/articles/28700873891223-Essential-IoT-Gateway-Setup-A-Q-A-Guide-for-WisGate-Edge-Series-of-Gateways) for WisGate Edge.
- Visit the [RAKwireless Forum](https://forum.rakwireless.com/)for specialized assistance from the RAKstars community and RAKwireless experts.
- Check our extensive collection of [Applications & Tutorials](https://news.rakwireless.com/applications-tutorials/)to get inspiration on exciting new use cases.
- Need more specialized product assistance? Contact [RAKwireless Support](https://www.rakwireless.com/en-us/contact-us).

## Product Description

**RAK7285 WisGate Edge Ultra** is the latest version of the RAK WisGate Edge series, designed to overcome the limitations of half-duplex communication. It's tailored to meet the demands of high-density network deployments, particularly for smart city infrastructure, metering applications, and other scenarios requiring reliable two-way communication at scale.

This gateway supports up to 8 LoRa channels in full-duplex (a 16-channel variant is coming soon), with multi-backhaul options including Ethernet, Wi-Fi, and cellular connectivity. Its integrated advanced cavity diplexers not only provide exceptional out-of-band interference suppression but also provide lightning protection for the LoRa antennas, ensuring uninterrupted and secure full-duplex communication.

In addition, RAK7285 operates under [WisGateOS 2](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/), which is built on the latest OpenWrt kernel. The OS Web UI features a new design and supports multiple extension installations, enabling remote management using [WisDM](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/) for personalized gateway customization.

## Product Features

### Hardware

- IP67 industrial-grade enclosure with cable glands
- PoE (802.3at) + Surge Protection
- 8 LoRa channels in full-duplex (16 channels variant is coming soon)
- Built-in cavity diplexers for out-of-band interference suspension
- Backhaul: Wi-Fi, Ethernet, and LTE (available with RAK7285C)
- GPS
- Supports 9~36 V<sub>DC</sub> and RAK Solar Battery Kit
- External antennas for GPS and LoRa
- Dying Gasp (optional)

### Software

- [WisGateOS 2](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#overview/)
- **WisGateOS 2 Extensions**: Adds support for features such as OpenVPN, WireGuard VPN, and more. Use the appropriate installation guide based on your WisGateOS 2 version:
    - [For WisGateOS 2 version 2.2.x or later](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/)
    - [For WisGateOS 2 versions 2.0.x and 2.1.x](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/)
- Remote management with WisDM Fleet Management
- Built-in Network Server (LoRaWAN support v1.0.3)
- LoRaWAN Stack support with Semtech SX1303
- LoRa Frame filtering (node whitelisting)
- MQTT v3.1 bridging with TLS encryption
- Fine timestamping
- **Buffering of LoRa frames in Packet Forwarder mode** in case of NS outage (automatic data recovery)
- **Full-duplex**
- **Listen Before Talk**

## Field Applications

As the Internet of Things (IoT) technology gradually penetrates into various industries and all aspects of life, the application scenarios of LoRaWAN gateways have become very extensive. This section highlights field applications of the RAK7285/RAK7285C WisGate Edge Ultra outdoor gateways, aiming to provide inspiration for your solutions.

:::tip NOTE
The following scenarios and applications are only examples. The field applications of LoRaWAN gateway are very extensive, including but not limited to these examples.
:::

### Agriculture

From measuring environmental conditions that influence crop production to tracking livestock health indicators, Internet of Things (IoT) technology for agriculture allows you to effectively measure all the parameters (soil quality, sunshine, precipitation, etc.) useful for efficient agriculture or livestock farming in real time, at a low cost, and with a very long range.

- Livestock monitoring
- Environmental monitoring
- Asset management
- Irrigation control
- Soil health

### Industry

The Industrial Internet of Things (IoT) is the foundation of Industry 4.0 and smart factories. The low power consumption of the LoRaWAN® network, as well as its range of several kilometers and its penetration in buildings, makes it feasible in various industrial fields such as automation, remote monitoring, and predictive maintenance.

- Supply chain robotics
- Solar and wind power
- Analysis of liquid flow in a pipe, valve or tank
- Smoke detection
- Equipment monitoring

### Smart City

Smart city leverages advanced LoRaWAN® technology and data-driven approaches to enhance city operations, services, and connectivity for its citizens.

- Infrastructure
- Urban traffic management
- Environmental protection
- Energy Management
- Public security

## Software and Services

### WisGateOS 2

The latest unified operating system for RAK gateways offers a feature-rich environment to access and configure the LoRaWAN gateway. WisGateOS 2 is built on the latest OpenWrt kernel for enhanced security. It employs a simplified user interface that improves usability and programmability. Integrated with WisDM, it enables remote management of gateways and firmware. With its extensibility, you can add additional features and functions to your gateways. For more information, refer to [WisGateOS 2 User Manual](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#overview).

### WisGateOS 2 Extensions

WisGateOS 2 includes an extension system that lets you add, remove, or update features based on your needs. Use the appropriate installation guide for your WisGateOS 2 version:
    - [For WisGateOS 2 version 2.2.x or later](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/)
    - [For WisGateOS 2 versions 2.0.x and 2.1.x](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/)

### WisDM

WisDM is a RAKwireless cloud-based device management platform designed to help you optimize the ways of controlling your gateways. The WisDM device management software supports IoT networks of any scale built around commercial-grade LoRaWAN Edge gateways from RAKwireless. Additionally, the WisDM platform offers you remote configuration, OTAA updates, and scalable management. For more information, refer to [WisDM](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/).

<!-- ## Product Comparison

The following table provides a comparative summary of RAK commercial gateways. It highlights key specification differences to assist your selection.

|                                  | RAK7268V2/RAK7268CV2                                                                                                                                                                                                                                                      | RAK7240V2/RAK7240CV2                                                                                                                                                                                                                                                      | RAK7267                                                                                                                                                                                                                                                                   | RAK7285/RAK7285C                                                                                                                                                                                                                                                          | RAK7289V2/RAK7289CV2                                                                                                                                                                                                                                                      |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Product Image**                | <img src="https://images.docs.rakwireless.com/wisgate/rak7268-v2/rak7268v2.png" alt="img " style={{zoom:'15%'}} />                                                                                                                                                        | <img src="https://images.docs.rakwireless.com/wisgate/rak7240-v2/rak7240v2.png" alt="img" style={{zoom:'15%'}} />                                                                                                                                                         | <img src="https://images.docs.rakwireless.com/wisgate/rak7267/rak7267.png" alt="img" style={{zoom:'15%'}} />                                                                                                                                                              | <img src="https://images.docs.rakwireless.com/wisgate/rak7285/rak7285.png" alt="img" style={{zoom:'15%'}} />                                                                                                                                                              | <img src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/rak7289v2.png" alt="img" style={{zoom:'15%'}} />                                                                                                                                               |
| **Gateway Category**             | Indoor LoRaWAN Gateway                                                                                                                                                                                                                                                    | Outdoor LoRaWAN Gateway                                                                                                                                                                                                                                                   | Outdoor LoRaWAN Gateway                                                                                                                                                                                                                                                   | Outdoor LoRaWAN Gateway                                                                                                                                                                                                                                                   | Outdoor LoRaWAN Gateway                                                                                                                                                                                                                                                   |
| **OS**                           | WisGateOS 2                                                                                                                                                                                                                                                                | WisGateOS 2                                                                                                                                                                                                                                                                | WisGateOS 2                                                                                                                                                                                                                                                                | WisGateOS 2                                                                                                                                                                                                                                                                | WisGateOS 2                                                                                                                                                                                                                                                                |
| **LoRa Feature**                 | <ul><li>SX1302 LoRa Core
8 Channels
</li><li>RX Sensitivity:
﹣139 dBm (Min)
</li><li>TX Power:
27 dBm (Max)</li></ul>                                                                                                                       | <ul><li>SX1303 LoRa Core
8 Channels /16 Channels
</li><li>RX Sensitivity:
﹣139 dBm (Min)
</li><li>TX Power:
27 dBm (Max)</li></ul>                                                                                                          | <ul><li>SX1303 LoRa Core
8 Channels
</li><li>RX Sensitivity:
﹣139 dBm (Min)
</li><li>TX Power:
27 dBm (Max)
Listen Before Talk</li></ul>                                                                                                | <ul><li>SX1303 LoRa Core
8 Channels in full-duplex
</li><li>RX Sensitivity:
﹣139 dBm (Min)
</li><li>TX Power:
30 dBm (Max)
Listen Before Talk</li></ul>                                                                                 | <ul><li>SX1303 LoRa Core
8 Channels /16 Channels
</li><li>RX Sensitivity:
﹣139 dBm (Min)
</li><li>TX Power:
27 dBm (Max)
Listen Before Talk</li></ul>                                                                                   |
| **Cellular Feature**             | Available with RAK7268CV2
IoT/M2M-optimized LTE Cat 4 Module
Supports:
EG95-E
EG95-NA
EC25-J
EC25-AU
EC25-E                                                                                                                                   | Available with RAK7240CV2
(for the 8-channel variant)
IoT/M2M-optimized LTE Cat 4 Module
Supports:
EG95-E
EG95-NA                                                                                                                                     | IoT/M2M -LTE Cat 1 Module
Supports:
EG915U-EU
EG915U-LA
EG915Q-NA
                                                                                                                                                                                    | Available with RAK7285C
IoT/M2M-optimized LTE Cat 4 Module
Supports:
EG95-E
EG95-NA
EC25-AU
                                                                                                                                                      | Available with RAK7289CV2
IoT/M2M-optimized LTE Cat 4 Module
Supports:
EG95-E
EG95-NA
EC25-J
EC25
                                                                                                                                            |
| **Wi-Fi Feature**                | <ul><li>Frequency:
2.4 GHz (802.11b/g/n)
</li><li>Operation Channels:
2.4 GHz: 1-13</li></ul>                                                                                                                                                       | <ul><li>Frequency:
2.4 GHz (802.11b/g/n)
</li><li>Operation Channels:
2.4 GHz: 1-13</li></ul>                                                                                                                                                       | <ul><li>Frequency:
2.4 GHz (802.11b/g/n)
</li><li>Operation Channels:
2.4 GHz: 1-13</li></ul>                                                                                                                                                       | <ul><li>Frequency:
2.4 GHz (802.11b/g/n)
</li><li>Operation Channels:
2.4 GHz: 1-13</li></ul>                                                                                                                                                       | <ul><li>Frequency:
2.4 GHz (802.11b/g/n)
</li><li>Operation Channels:
2.4 GHz: 1-13</li></ul>                                                                                                                                                       |
| **Frequency Band**               | EU868
IN865
US915
AU915
KR920
AS923-1/2/3/4
EU433
CN470                                                                                                                                                                                       | EU868
IN865
RU864
US915
AU915
KR920
AS923-1/2/3/4
EU433
CN470                                                                                                                                                                             | EU868
IN865
RU864
US915
AU915
KR920
AS923-1/2/3/4                                                                                                                                                                                                 | US915
AU915                                                                                                                                                                                                                                                           | EU868
IN865
US915
AU915
KR920
AS923-1/2/3/4
EU433
CN470                                                                                                                                                                                       |
| **Network Connectivity**         | Ethernet
Wi-Fi
LTE                                                                                                                                                                                                                                                | Ethernet
Wi-Fi
LTE                                                                                                                                                                                                                                                | Wi-Fi
LTE                                                                                                                                                                                                                                                             | Ethernet
Wi-Fi
LTE                                                                                                                                                                                                                                                | Ethernet
Wi-Fi
LTE                                                                                                                                                                                                                                                |
| **GPS**                          | -                                                                                                                                                                                                                                                                         | Supports GPS                                                                                                                                                                                                                                                              | Supports GPS                                                                                                                                                                                                                                                              | Supports GPS                                                                                                                                                                                                                                                              | Supports GPS                                                                                                                                                                                                                                                              |
| **Antenna**                      | **LoRa**:
External antenna
RP-SMA female connector
**WiFi/LTE**:
Internal antenna                                                                                                                                                                         | **LoRa/Wi-Fi/LTE/GPS**:
External antenna
N-Type connector                                                                                                                                                                                                         | **LoRa/WiFi/LTE/GPS**: Internal antenna                                                                                                                                                                                                                                   | **LoRa/WiFi/LTE/GPS**:
External antenna
N-Type connector                                                                                                                                                                                                          | **LoRa**:
External antenna
N-Type connector
**WiFi/LTE/GPS**:
Internal antenna                                                                                                                                                                            |
| **Power Pupply**                 | PoE (IEEE 802.3 af): 36\~57 V<sub>DC</sub>
DC 12 V - 1 A
(Optional) 9-24 V<sub>DC</sub> input upon request.                                                                                                                                   | PoE (IEEE 802.3af) : 42\~57 V<sub>DC</sub>
9\~24 V<sub>DC</sub>
Compatible with [RAK Solar Battery Kit](https://docs.rakwireless.com/product-categories/accessories/rak9155/overview/#product-description)                                              | 9\~36 V<sub>DC</sub>
Compatible with [RAK Solar Battery Kit](https://docs.rakwireless.com/product-categories/accessories/rak9155/overview/#product-description)                                                                                                  | PoE (IEEE 802.3at): 42\~57 V<sub>DC</sub>
9\~36 V<sub>DC</sub>
Compatible with [RAK Solar Battery Kit](https://docs.rakwireless.com/product-categories/accessories/rak9155/overview/#product-description)                                               | PoE (IEEE 802.3af): 37\~57 V<sub>DC</sub>
DC 12 V
Compatible with [RAK Solar Battery Kit](https://docs.rakwireless.com/product-categories/accessories/rak9155/overview/#product-description)                                                            |
| **Ingress Protection**           | IP30                                                                                                                                                                                                                                                                      | IP65                                                                                                                                                                                                                                                                      | IP67                                                                                                                                                                                                                                                                      | IP67                                                                                                                                                                                                                                                                      | IP67                                                                                                                                                                                                                                                                      |
| **Enclosure Material**           | Plastic                                                                                                                                                                                                                                                                   | Aluminum                                                                                                                                                                                                                                                                  | ABS plastic                                                                                                                                                                                                                                                               | Aluminum                                                                                                                                                                                                                                                                  | Aluminium and plastic                                                                                                                                                                                                                                                     |
| **Dimension**
(Gateway only) | 166 mm x 127.5 mm x 36 mm                                                                                                                                                                                                                                  | 224 mm x 121 mm x 42 mm                                                                                                                                                                                                                                    | 180 mm x 130 mm x 60 mm                                                                                                                                                                                                                                    | 310 mm x 290 mm x 146 mm                                                                                                                                                                                                                                   | 240 mm x 240 mm x 89.5 mm                                                                                                                                                                                                                                  |
| **Operating Condition**          | <ul><li>Operating Temperature:
﹣10° C to ﹢55° C
</li><li>Storage Temperature:
﹣40° C to ﹢85° C
</li><li>Operating Humidity:
0\~95% RH non-condensing
</li><li>Storage Humidity:
0~95% RH non-condensing</li></ul> | <ul><li>Operating Temperature:
﹣30° C to ﹢55° C
</li><li>Storage Temperature:
﹣40° C to ﹢85° C
</li><li>Operating Humidity:
0\~95% RH non-condensing
</li><li>Storage Humidity:
0~95% RH non-condensing</li></ul> | <ul><li>Operating Temperature:
﹣30° C to ﹢55° C
</li><li>Storage Temperature:
﹣40° C to ﹢85° C
</li><li>Operating Humidity:
0\~95% RH non-condensing
</li><li>Storage Humidity:
0~95% RH non-condensing</li></ul> | <ul><li>Operating Temperature:
﹣30° C to ﹢55° C
</li><li>Storage Temperature:
﹣40° C to ﹢85° C
</li><li>Operating Humidity:
0\~95% RH non-condensing
</li><li>Storage Humidity:
0~95% RH non-condensing</li></ul> | <ul><li>Operating Temperature:
﹣30° C to ﹢55° C
</li><li>Storage Temperature:
﹣40° C to ﹢85° C
</li><li>Operating Humidity:
0\~95% RH non-condensing
</li><li>Storage Humidity:
0~95% RH non-condensing</li></ul> |
| **Installation Method**          | Desktop mounting
Wall mounting (via included bracket)
Rail mounting (via included bracket)                                                                                                                                                                        | Pole or wall mounting                                                                                                                                                                                                                                                     | Pole mounting (other options available per request)                                                                                                                                                                                                                       | Pole or wall mounting                                                                                                                                                                                                                                                     | Pole or wall mounting                                                                                                                                                                                                                                                     | -->

