---
title: RAK7289V2/RAK7289CV2 WisGate Edge Pro V2
description: Discover the RAK7289V2 WisGate Edge Pro V2 – a 16-channel industrial LoRaWAN gateway with multi-backhaul, WisGateOS 2, and SX1303 support for scalable IoT.
image: "https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/rak7289v2.png"
keywords:
    - 16-channel LoRaWAN gateway
    - WisGate Edge Pro
    - SX1303 LoRa
    - LoRA gateway
    - OpenWrt
    - outdoor LoRaWAN gateway
sidebar_label: Overview
download: true
---

#  RAK7289V2/RAK7289CV2 WisGate Edge Pro V2

Thank you for choosing **RAK7289V2/RAK7289CV2 WisGate Edge Pro** in your awesome IoT Project! 🎉 To help you get started, we have provided you with all the necessary  information for your product.

**Product documentation**

* [Quick Start Guide](https://docs.rakwireless.com/product-categories/wisgate/rak7289v2/quickstart/)
* [LoRaWAN Network Server Guide](https://docs.rakwireless.com/product-categories/wisgate/rak7289v2/lorawan-network-server-guide/)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisgate/rak7289v2/datasheet/)
* [RAK7289V2/RAK7289CV2 Power Consumption Summary](https://learn.rakwireless.com/hc/en-us/articles/31641941368727-Power-Consumption-Summary-for-RAK7289V2-RAK7289CV2-WisGate-Edge-Pro)

For more related tutorials, you can refer to [Quick Start Guide >Tutorials](https://docs.rakwireless.com/product-categories/wisgate/rak7289v2/quickstart/#tutorials).

**Resources**

- For more information, check the [Frequently Asked Questions](https://learn.rakwireless.com/hc/en-us/articles/28700873891223-Essential-IoT-Gateway-Setup-A-Q-A-Guide-for-WisGate-Edge-Series-of-Gateways) for WisGate Edge.
- Visit the [RAKwireless Forum](https://forum.rakwireless.com/) for specialized assistance from the RAKstars community and RAKwireless experts.
- Check our extensive collection of [Applications & Tutorials](https://news.rakwireless.com/applications-tutorials/) to get inspiration on exciting new use cases.
- Need more specialized product assistance? Contact [RAKwireless Support](https://www.rakwireless.com/en-us/contact-us).

:::tip NOTE

The new RAK7289V2/RAK7289CV2 gateway now replaces the RAK7289. You can still browse the product information of [RAK7289](https://docs.rakwireless.com/product-categories/wisgate/rak7289/overview/)

:::

## Product Description

The RAK7289V2 WisGate Edge Pro is the flagship product of the RAK Edge Series. Featuring industrial-grade components, it ensures a high level of reliability.

It supports up to 16 LoRa channels and offers multi-backhaul options with Ethernet, Wi-Fi, and cellular connectivity. Additionally, it provides a dedicated port for various power options, including solar panels and batteries. Its redesigned enclosure accommodates LTE, Wi-Fi, and GPS antennas internally for enhanced aesthetics and functionality.

In addition, RAK7289V2 operates under [WisGateOS 2](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#overview), which is built on the latest OpenWrt kernel. The OS Web UI features a new design and supports multiple extension installations, enabling remote management using [WisDM](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview) for personalized gateway customization.

:::warning
This product is intended to be powered by 12 V<sub>DC</sub> through a designated power port. The use of solar chargers is not recommended, as they may supply overvoltage, potentially damaging the device. We strongly discourage the use of such chargers with this product, and any damage incurred as a result will void the warranty.
:::

## Product Features

### Hardware

- IP67/NEMA-6 industrial-grade enclosure with cable glands
- PoE (802.3af) + Surge Protection
- Dual LoRa Concentrators for up to 16-channel options
- Backhaul: Wi-Fi, Ethernet, and LTE (optional, available with RAK7289CV2)
- GPS
- Supports 12 V<sub>DC</sub> or solar power supply with electricity monitoring (Solar Kit optional)
- Internal antennas for Wi-Fi, GPS, and LTE, external antenna for LoRa
- Dying-gasp (optional)

### Software

- [WisGateOS 2](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/)
- **WisGateOS 2 Extensions**: Adds support for features such as OpenVPN, WireGuard VPN, and more. Use the appropriate installation guide based on your WisGateOS 2 version:
    - [For WisGateOS 2 version 2.2.x or later](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/)
    - [For WisGateOS 2 versions 2.0.x and 2.1.x](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/)
- Remote management with [WisDM](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview) Fleet Management
- Built-in Network Server (full LoRaWAN support v1.0.3)
- Full LoRaWAN Stack support with Semtech SX1303
- LoRa Frame filtering (node whitelisting in Packet Forwarder mode)
- MQTT v3.1 bridging with TLS encryption
- Fine timestamping (optional)
- Buffering of LoRa frames in Packet Forwarder mode in case of NS outage (no data loss)
- Listen Before Talk (optional)

## Field Applications

As the Internet of Things (IoT) technology gradually penetrates into various industries and all aspects of life, the application scenarios of LoRaWAN gateways have become very extensive. This section highlights field applications of the RAK7289V2/RAK7289CV2 WisGate Edge Prime outdoor gateways, aiming to provide inspiration for your solutions.

:::tip NOTE
The following scenarios and applications are only examples. The field applications of the LoRaWAN gateway are very extensive, including but not limited to these examples.
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

The latest unified operating system for RAK gateways offers a feature-rich environment to access and configure the LoRaWAN gateway. WisGateOS 2 is built on the latest OpenWrt kernel for enhanced security. It employs a simplified user interface that improves usability and programmability. Integrated with WisDM, it enables remote management of gateways and firmware. With its extensibility, you can add additional features and functions to your gateways. For more information, refer to [WisGateOS 2 User Manual](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/).

### WisGateOS 2 Extensions

WisGateOS 2 features an extension functionality, that allows features and functions be added, removed, or updated based on your needs. For more information, refer to [WisGateOS 2 Extensions](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/overview/).

### WisDM

WisDM is a RAKwireless cloud-based device management platform designed to help you optimize the ways of controlling your gateways. The WisDM device management software supports IoT networks of any scale built around commercial-grade LoRaWAN Edge gateways from RAKwireless. Additionally, the WisDM platform offers you remote configuration, OTAA updates, and scalable management. For more information, refer to [WisDM](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview).

<!-- ## Product Comparison

The following table provides a comparative summary of RAK commercial gateways. It highlights key specification differences to assist your selection.

|                                  | RAK7268V2/RAK7268CV2                                                                                                                                                                                                                                                        | RAK7240V2/RAK7240CV2                                                                                                                                                                                                                                                        | RAK7267                                                                                                                                                                                                                                                                     | RAK7285/RAK7285C                                                                                                                                                                                                                                                            | RAK7289V2/RAK7289CV2                                                                                                                                                                                                                                                        |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Product Image**                | <img src="https://images.docs.rakwireless.com/wisgate/rak7268-v2/rak7268v2.png" alt="RAK7268V2" width="75%"/>                                                                                                                                                               | <img src="https://images.docs.rakwireless.com/wisgate/rak7240-v2/rak7240v2.png" alt="RAK7240V2" width="85%"/>                                                                                                                                                               | <img src="https://images.docs.rakwireless.com/wisgate/rak7267/rak7267.png" alt="RAK7267" width="85%"/>                                                                                                                                                                      | <img src="https://images.docs.rakwireless.com/wisgate/rak7285/rak7285.png" alt="RAK7285" width="85%"/>                                                                                                                                                                      | <img src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/rak7289v2.png" alt="RAK7289V2" width="70%"/>                                                                                                                                                     |
| **Gateway Category**             | Indoor LoRaWAN Gateway                                                                                                                                                                                                                                                      | Outdoor LoRaWAN Gateway                                                                                                                                                                                                                                                     | Outdoor LoRaWAN Gateway                                                                                                                                                                                                                                                     | Outdoor LoRaWAN Gateway                                                                                                                                                                                                                                                     | Outdoor LoRaWAN Gateway                                                                                                                                                                                                                                                     |
| **Cellular Feature**             | Available with RAK7268CV2
IoT/M2M-optimized LTE Cat 4 Module
Supports:
EG95-E
EG95-NA
EC25-J
EC25-AU
EC25-E                                                                                                                                     | Available with RAK7240CV2
(for the 8-channel variant)
IoT/M2M-optimized LTE Cat 4 Module
Supports:
EG95-E
EG95-NA                                                                                                                                       | IoT/M2M -LTE Cat 1 Module
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
2.4 GHz: 1-13</li></ul>                                                                                                                                                         | <ul><li>Frequency:
2.4 GHz (802.11b/g/n)
</li><li>Operation Channels:
2.4 GHz: 1-13</li></ul>                                                                                                                                                         | <ul><li>Frequency:
2.4 GHz (802.11b/g/n)
</li><li>Operation Channels:
2.4 GHz: 1-13</li></ul>                                                                                                                                                         | <ul><li>Frequency:
2.4 GHz (802.11b/g/n)
</li><li>Operation Channels:
2.4 GHz: 1-13</li></ul>                                                                                                                                                         | <ul><li>Frequency:
2.4 GHz (802.11b/g/n)
</li><li>Operation Channels:
2.4 GHz: 1-13</li></ul>                                                                                                                                                         |
| **Frequency Band**               | EU868
IN865
US915
AU915
KR920
AS923-1/2/3/4
EU433
CN470                                                                                                                                                                                         | EU868
IN865
RU864
US915
AU915
KR920
AS923-1/2/3/4
EU433
CN470                                                                                                                                                                               | EU868
IN865
RU864
US915
AU915
KR920
AS923-1/2/3/4                                                                                                                                                                                                   | US915
AU915                                                                                                                                                                                                                                                             | EU868
IN865
US915
AU915
KR920
AS923-1/2/3/4
EU433
CN470                                                                                                                                                                                         |
| **Network Connectivity**         | Ethernet
Wi-Fi
LTE                                                                                                                                                                                                                                                  | Ethernet
Wi-Fi
LTE                                                                                                                                                                                                                                                  | Wi-Fi
LTE                                                                                                                                                                                                                                                               | Ethernet
Wi-Fi
LTE                                                                                                                                                                                                                                                  | Ethernet
Wi-Fi
LTE                                                                                                                                                                                                                                                  |
| **GPS**                          | -                                                                                                                                                                                                                                                                           | Supports GPS                                                                                                                                                                                                                                                                | Supports GPS                                                                                                                                                                                                                                                                | Supports GPS                                                                                                                                                                                                                                                                | Supports GPS                                                                                                                                                                                                                                                                |
| **Antenna**                      | **LoRa**:
External antenna
RP-SMA female connector
**WiFi/LTE**:
Internal antenna                                                                                                                                                                           | **LoRa/Wi-Fi/LTE/GPS**:
External antenna
N-Type connector                                                                                                                                                                                                           | **LoRa/WiFi/LTE/GPS**: Internal antenna                                                                                                                                                                                                                                     | **LoRa/WiFi/LTE/GPS**:
External antenna
N-Type connector                                                                                                                                                                                                            | **LoRa**:
External antenna
N-Type connector
**WiFi/LTE/GPS**:
Internal antenna                                                                                                                                                                              |
| **Power Pupply**                 | PoE (IEEE 802.3 af): 36\~57 V<sub>DC</sub>
DC 12 V - 1 A
(Optional) 9-24 V<sub>DC</sub> input upon request.                                                                                                                                     | PoE (IEEE 802.3af) : 42\~57 V<sub>DC</sub>
9\~24 V<sub>DC</sub>
Compatible with [RAK Solar Battery Kit](https://docs.rakwireless.com/product-categories/accessories/rak9155/overview/)                                                                    | 9\~36 V<sub>DC</sub>
Compatible with [RAK Solar Battery Kit](https://docs.rakwireless.com/product-categories/accessories/rak9155/overview/)                                                                                                                        | PoE (IEEE 802.3at): 42\~57 V<sub>DC</sub>
9\~36 V<sub>DC</sub>
Compatible with [RAK Solar Battery Kit](https://docs.rakwireless.com/product-categories/accessories/rak9155/overview/)                                                                     | PoE (IEEE 802.3af): 37\~57 V<sub>DC</sub>
DC 12 V
Compatible with [RAK Solar Battery Kit](https://docs.rakwireless.com/product-categories/accessories/rak9155/overview/)                                                                                  |
| **Ingress Protection**           | IP30                                                                                                                                                                                                                                                                        | IP65                                                                                                                                                                                                                                                                        | IP67                                                                                                                                                                                                                                                                        | IP67                                                                                                                                                                                                                                                                        | IP67                                                                                                                                                                                                                                                                        |
| **Enclosure Material**           | Plastic                                                                                                                                                                                                                                                                     | Aluminum                                                                                                                                                                                                                                                                    | ABS plastic                                                                                                                                                                                                                                                                 | Aluminum                                                                                                                                                                                                                                                                    | Aluminium and plastic                                                                                                                                                                                                                                                       |
| **Dimension**
(Gateway only) | 166 mm x 127.5 mm x 36 mm                                                                                                                                                                                                                                    | 224 mm x 121 mm x 42 mm                                                                                                                                                                                                                                      | 180 mm x 130 mm x 60 mm                                                                                                                                                                                                                                      | 310 mm x 290 mm x 146 mm                                                                                                                                                                                                                                     | 240 mm x 240 mm x 89.5 mm                                                                                                                                                                                                                                    |
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
﹣40° C to ﹢70° C
</li><li>Storage Temperature:
﹣40° C to ﹢85° C
</li><li>Operating Humidity:
0\~95% RH non-condensing
</li><li>Storage Humidity:
0~95% RH non-condensing</li></ul> |
| **Installation Method**          | Desktop mounting
Wall mounting (via included bracket)
Rail mounting (via included bracket)                                                                                                                                                                          | Pole or wall mounting                                                                                                                                                                                                                                                       | Pole mounting (other options available per request)                                                                                                                                                                                                                         | Pole or wall mounting                                                                                                                                                                                                                                                       | Pole or wall mounting                                                                                                                                                                                                                                                       | -->

