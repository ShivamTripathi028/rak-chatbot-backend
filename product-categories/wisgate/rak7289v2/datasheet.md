---
title: RAK7289V2/RAK7289CV2 WisGate Edge Pro V2 Datasheet
description: Learn about the RAK7289V2 WisGate Edge Pro V2 datasheet. Explore specs for this 16-channel LoRaWAN gateway with SX1303, WisGateOS 2, and multi-backhaul support.
image: "https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/rak7289v2.png"
keywords:
  - RAK7289V2 datasheet
  - WisGate Edge Pro V2
  - LoRaWAN gateway
  - 16-channel gateway
  - industrial gateway
sidebar_label: Datasheet
---

# RAK7289V2/RAK7289CV2 WisGate Edge Pro V2 Datasheet

## Overview

### Description

The RAK7289V2 WisGate Edge Pro is the flagship product of the RAK Edge Series. Featuring industrial-grade components, it ensures a high level of reliability.

It supports up to 16 LoRa channels and offers multi-backhaul options with Ethernet, Wi-Fi, and cellular connectivity. Additionally, it provides a dedicated port for various power options, including solar panels and batteries. Its redesigned enclosure accommodates LTE, Wi-Fi, and GPS antennas internally for enhanced aesthetics and functionality.

In addition, RAK7289V2 operates under [WisGateOS 2](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#overview), which is built on the latest OpenWrt kernel. The OS Web UI features a new design and supports multiple extension installations, enabling remote management using [WisDM](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview) for personalized gateway customization.

:::warning
This product is intended to be powered by 12 V<sub>DC</sub> through a designated power port. The use of solar chargers is not recommended, as they may supply overvoltage, potentially damaging the device. We strongly discourage the use of such chargers with this product, and any damage incurred as a result will void the warranty.
:::

### Features

#### Hardware

- IP67/NEMA-6 industrial-grade enclosure with cable glands
- PoE (802.3af) + Surge Protection
- Dual LoRa Concentrators for up to 16 channels
- Backhaul: Wi-Fi, Ethernet, LTE (optional, available with RAK7289CV2)
- GPS
- Supports 12 V<sub>DC</sub> or solar power supply with electricity monitoring (Solar Kit optional)
- Internal antennas for Wi-Fi, GPS, and LTE
- External antenna for LoRa
- Dying-gasp (optional)

#### Software

- [WisGateOS 2](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/)
- **WisGateOS 2 Extensions**: Adds support for features such as OpenVPN, WireGuard VPN, and more. Use the appropriate installation guide based on your WisGateOS 2 version:
    - [For WisGateOS 2 version 2.2.x or later](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/)
    - [For WisGateOS 2 versions 2.0.x and 2.1.x](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/)
- Remote management with [WisDM](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/) Fleet Management
- Built-in Network Server (full LoRaWAN support v1.0.3)
- Full LoRaWAN Stack support with Semtech SX1303
- LoRa Frame filtering (node whitelisting in Packet Forwarder mode)
- MQTT v3.1 bridging with TLS encryption
- Fine timestamping (optional)
- Buffering of LoRa frames in Packet Forwarder mode in case of NS outage (no data loss)
- Listen Before Talk (optional)

## Specifications

### Overview

The overview presents the block diagram for the RAK7289V2/RAK7289CV2 that shows the internal architecture of the hardware.

#### Block Diagram

> **Image:** RAK7289V2 Block Diagram

> **Image:** RAK7289CV2 Block Diagram

#### Main Specifications

| Feature | Specifications |
| --- | --- |
| Computing | MT7628, 128 MB DDR2 RAM |
| LoRa Features | SX1303 mPCIe card (connects maximum of two) |
| LoRa Features | 8 Channels (16 channels optional) |
| LoRa Features | Frequency: EU868 / IN865 / US915 / AU915 / KR920 / AS923-1/2/3/4 / EU433 / CN470 |
| LoRa Features | Listen Before Talk |
| LoRa Features | LoRa Radio: Refer to the LoRa Radio Specifications section for detailed information. |
| Wi-Fi Features | Frequency: 2.4 GHz (802.11b / g / n) |
| Wi-Fi Features | Operation Channels: 1-13 (2.4 GHz) |
| Wi-Fi Features | 2x2 MIMO |
| Wi-Fi Features | Wi-Fi Radio: Refer to the Wi-Fi Radio Specifications section for detailed information. |
| Cellular Features (available with RAK7289CV2) | Nano SIM Card: 12 x 9 x 0.67 mm Supports Quectel EG95-E / EG95-NA / EC25-J / EC25-AU(IoT / M2M -optimized LTE Cat 4 Module) |
| Cellular Features (available with RAK7289CV2) | LTE Radio: Refer to the LTE Radio Specifications section for detailed information. |
| Power Supply | PoE (IEEE 802.3af) - 37~57 V DC 12 V DC Compatible with RAK Battery Plus |
| Antenna | LoRa: N-Type connector (one for the 8-channel gateway and two for the 16-channel gateway) |
| Antenna | Wi-Fi / GPS / LTE: Internal antenna |
| Ingress protection | IP67 |
| Enclosure material | Aluminium and plastic |
| Dimensions | 240 mm x 240 mm x 89.5 mm |
| Weight | 4.6 kg gateway only |
| Operating Conditions | Operating temperature: ﹣40˚ C to ﹢70˚ C |
| Operating Conditions | Storage Temperature: ﹣40˚ C to ﹢85˚ C |
| Operating Conditions | Operating humidity: 0% to 95% (non-condensing) |
| Operating Conditions | Storage Humidity: 0% to 95% (non-condensing) |
| Operating Conditions | For environmental reliability test details: WisGate Edge Pro RAK7289V2/CV2 Environmental Reliability Test. |
| Installation Method | Pole or wall mounting |

### Hardware

The hardware specification details the interfacing of the RAK7289V2/RAK7289CV2 and its corresponding functionalities. It also outlines the parameters and standard values of the gateway.

#### Interfaces

> **Image:** RAK7289V2/RAK7289CV2 Interfaces

##### Interface Description

| **Interface**              | **Description**                        | **Function**                                                                                                                                             |
| -------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **LoRa1 / LoRa2**          | LoRa Antenna Connectors                | N-Type connectors for external LoRa antennas. Required for LoRaWAN data transmission and reception.                                                      |
| **ETH (PoE)**              | Ethernet Port (RJ45, 10/100 Mbps) | Provides network backhaul via Ethernet. **PoE (Power over Ethernet)** allows the gateway to receive both power and data through a single Ethernet cable. |
| **Additional Power Input** | Power Input                            | Accepts **12 V DC input**. 
It is fully compatible with the **RAK Battery Plus**.                                                                   |
| **Reserved**               | Sealed Port (no function by default)   | Reserved for future use.                                                                                                                                 |
| **Console**                | USB Type-C Port                        | Used for serial console access during debugging and firmware flashing.                                                                                   |
| **Reset**                  | Reset Key                              | - **Short press**: Reboot the device.   
- **Long press (≥5 sec)**: Factory reset.                                                                  |
| **NanoSIM**                | NanoSIM Slot                           | Used for LTE connectivity. Required when using cellular backhaul. Included in all versions, even if LTE is not supported.                                |
| **TF Card**                | MicroSD (TF) Card Slot                 | Includes a **16 GB pre-installed SD card** used for log storage and configuration. 
**Do not remove during operation** to avoid data loss.          |
| **LED Indicators**         | Status LEDs                            | - Power (PWR)   
- Ethernet (ETH)   
- LoRa1 & LoRa2   
- WLAN   
- LTE *(for LTE version)*   
                                 |

##### LED Indicators Details

| LEDs | Status Indication Description |
| --- | --- |
| LED 1 (PWR) | Power indicator: The LED is on when device power is on |
| LED 2 (ETH) | ON: Link is up |
| LED 2 (ETH) | OFF: Link is down |
| LED 2 (ETH) | Flicker: Data transmitting and receiving |
| LED 3 (LoRa 1) | ON: LoRa 1 is working |
| LED 3 (LoRa 1) | OFF: LoRa 1 is not working |
| LED 3 (LoRa 1) | Flicker: Indicate LoRa 1 Packet receiving and sending |
| LED 4 (WLAN) | AP Mode: ON: The AP is up Flicker: Data receiving and sending |
| LED 4 (WLAN) | STA Mode: Slow flicker (1 Hz): Disconnected ON: Connected Flicker: Data receiving and sending |
| LED 5 (LTE) | Slow Flicker (1800 ms bright / 200 ms dark): Network searching |
| LED 5 (LTE) | Slow flicker (200 ms bright / 1800 ms dark): Idle |
| LED 6 (LoRa 2 for 16 channel) | ON: LoRa 2 is working |
| LED 6 (LoRa 2 for 16 channel) | OFF: LoRa 2 is not working |
| LED 6 (LoRa 2 for 16 channel) | Flicker: Indicate LoRa 2 Packet receiving and sending |

#### RF Specifications

##### LoRa Radio Specifications

| Feature | Specifications |
| --- | --- |
| Operating Frequency | EU868 / IN865 / US915 / AU915 / KR920 / AS923-1/2/3/4 / EU433 / CN470 |
| Transmit Power | 27 dBm (Max) |
| Receiver Sensitivity | -141 dBm (Min)@SF12 |

##### Wi-Fi Radio Specifications

| Feature | Specifications |
| --- | --- |
| Wireless Standard | IEEE 802.11b / g / n |
| Operating Frequency | ISM band: 2.412~2.472 GHz |
| Operation Channels | 2.4 GHz: 1-13 |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 802.11b |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 19 dBm @1 Mbps |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 19 dBm @11 Mbps |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 802.11g |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 18 dBm @6 Mbps |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 16 dBm @54 Mbps |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 802.11n (2.4 GHz) |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 18 dBm @MCS0 (HT20) |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 16 dBm @MCS7 (HT20) |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 17 dBm @MCS0 (HT40) |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 15 dBm @MCS7 (HT40) |
| Receiver Sensitivity (Typical) | 802.11b |
| Receiver Sensitivity (Typical) | -95 dBm @1 Mbps |
| Receiver Sensitivity (Typical) | -88 dBm @11 Mbps |
| Receiver Sensitivity (Typical) | 802.11g |
| Receiver Sensitivity (Typical) | -90 dBm @6 Mbps |
| Receiver Sensitivity (Typical) | -75 dBm @54 Mbps |
| Receiver Sensitivity (Typical) | 802.11n (2.4 GHz) |
| Receiver Sensitivity (Typical) | -89 dBm @MCS0 (HT20) |
| Receiver Sensitivity (Typical) | -72 dBm @MCS7 (HT20) |
| Receiver Sensitivity (Typical) | -86 dBm @MCS0 (HT40) |
| Receiver Sensitivity (Typical) | -68 dBm @MCS7 (HT40) |

##### LTE Radio Specifications (Optional, Available with RAK7289CV2)

| Feature | Specifications |
| --- | --- |
| EG95-E for EMEA Region (Europe, Middle East, and Africa) | LTE FDD: B1/B3/B7/B8/B20/B28A |
| EG95-E for EMEA Region (Europe, Middle East, and Africa) | WCDMA: B1/B8 |
| EG95-E for EMEA Region (Europe, Middle East, and Africa) | GSM/EDGE: B3/B8 |
| EG95-NA for North America Region | LTE FDD: B2/B4/B5/B12/B13 |
| EG95-NA for North America Region | WCDMA: B2/B4/B5 |
| EC25-J for Japan Region | LTE FDD: B1 / B3 / B8 / B18 / B19 / B26 |
| EC25-J for Japan Region | LTE TDD: B41 |
| EC25-J for Japan Region | WCDMA: B1 / B6 / B8 /B19 |
| EC25-AU for Brazil Region | LTE-FDD: B1 / B2 / B3 / B4 / B5 / B7 / B8 / B28 |
| EC25-AU for Brazil Region | LTE-TDD: B40 |
| EC25-AU for Brazil Region | WCDMA: B1 / B2 / B5 / B8 |
| EC25-AU for Brazil Region | GSM/EDGE: B2 / B3 / B5 / B8 |

#### Power Supply Options

The RAK7289V2/RAK7289CV2 supports the following power supply methods:

- **PoE (Power over Ethernet):**
   Via included PoE injector, supports IEEE 802.3af standard (input: 37–57 V DC).

- **12 V DC Input:**
   Through the waterproof power connector, accepts 12 V regulated DC from an external power supply.

  :::warning

  **Only use regulated 12 V DC power sources.** Do not use solar chargers or non-certified adapters, as improper voltage may damage the device and void the warranty.

  :::

- **[RAK9155 Battery Plus](https://store.rakwireless.com/products/rak-battery-plus-rak9155?variant=42309251563718) (Optional):**
   Provides regulated 12 V DC output and is designed for off-grid or solar-powered deployments. Purchased separately.

:::tip NOTE

Only **one** power input should be used at a time.

:::

### Software

The RAK7289V2/RAK7289V2 gateway runs on WisGateOS 2, a robust software platform designed for efficient network management and integration. Below are the key software features and capabilities:

For more detailed information on software configurations and usage, refer to the [WisGateOS 2 User Guide](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/).

| **Category**                          | **Feature**                          | **Description**                                                                                                                       |
| ------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **LoRaWAN and Network Management**    | LoRaWAN Packet Forwarding            | Supports Packet Forwarder and Basic Station configurations                                                                            |
|                                       | Built-in Server                      | Local LoRaWAN Network Server (LNS) integrated into the gateway for network management                                                 |
|                                       | Frequency Band Setup                 | Configurable with different LoRaWAN frequency bands based on deployment region                                                        |
|                                       | TX Power Setup                       | Adjustable transmit power for optimal network performance                                                                             |
|                                       | Automatic Data Recovery              | Ensures reliable data transmission even during network disruptions                                                                    |
|                                       | Server Address and Port Setup        | Custom configuration for LoRaWAN Network Server communication                                                                         |
|                                       | Supports LoRaWAN Classes A, B, and C | Fully compatible with LoRaWAN devices operating in Class A, B, and C                                                                  |
|                                       | Uplink Backup                        | Enables automatic switchover to a backup uplink (e.g., LTE or Wi-Fi) when the primary uplink fails. Requires Multi-WAN configuration. |
|                                       | Location Setup                       | Manual or automatic setup of gateway location (e.g., GPS coordinates)                                                                 |
| **Connectivity and Network Services** | Wi-Fi Client/AP Mode                 | Connect to existing network or act as an access point                                                                                 |
|                                       | DHCP Server/Client                   | Dynamic IP address allocation for both server and client roles                                                                        |
|                                       | NAT and Router Module                | Enables router functionality with Network Address Translation                                                                         |
|                                       | WireGuard / OpenVPN                  | Secure communication tunnel for remote access and management                                                                          |
|                                       | LTE APN Setup                        | Configures Access Point Name for LTE connectivity                                                                                     |
| **Monitoring and Security**           | Statistics and Data Logger           | Tracks performance metrics and logs operational data                                                                                  |
|                                       | Firewall                             | Provides basic firewall functions for traffic control and security                                                                    |
|                                       | SSH2                                 | Secure Shell access for remote troubleshooting and management                                                                         |
|                                       | Ping Watchdog                        | Monitors connectivity and triggers recovery if the connection fails                                                                   |
| **User Interface and Management**     | Web UI                               | Web-based interface for configuration and monitoring                                                                                  |
|                                       | WisDM                                | Cloud platform for remote management and monitoring                                                                                   |
|                                       | Gateway OTA management               | Over-the-air firmware management for seamless updates                                                                                 |
|                                       | MQTT Bridge                          | Integration with IoT platforms using MQTT protocol                                                                                    |
|                                       | Firmware Updates                     | Over-the-air updates for easy firmware upgrades                                                                                       |
|                                       | NTP                                  | Synchronizes the gateway system time for accurate timestamp recording                                                                 |

### Firmware

|                 Model                 |                                            Source                                            |
| :-----------------------------------: | :------------------------------------------------------------------------------------------: |
| RAK7289V2/RAK7289CV2 WisGate Edge Pro | [Download](https://downloads.rakwireless.com/LoRa/WisGateOS2/WisGateOS2_Latest_Firmware.zip) |

## Models/Bundles

| Part Number | 8 Channel SX1303 | 16 Channel SX1303 | Cat4 Cellular | GPS | Wi-Fi | Dying gasp |
| --- | --- | --- | --- | --- | --- | --- |
| RAK7289CV2-XYZ | √ |  | √ | √ | √ |  |
| RAK7289CV2-XYZ | √ |  | √ | √ | √ | √ |
| RAK7289CV2-XYZ |  | √ | √ | √ | √ | √ |
| RAK7289V2-XYZ | √ |  |  | √ | √ |  |
| RAK7289V2-XYZ | √ |  |  | √ | √ | √ |
| RAK7289V2-XYZ |  | √ |  | √ | √ | √ |

## Certification

### Certifications
- **CE:** https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289_RAK7289V2_CE_Certification.pdf
- **FCC:** https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289_FCC_Certification.pdf
- **ISED:** https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289_ISED_Certification.zip
- **JRL:** https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289CV2_RAK7289V2_JRL_certification.pdf
- **JTBL:** https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289CV2_JTBL_Certification.pdf
- **KC:** https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289_RAK7289C_RAK7289V2_RAK7289CV2_KC_Certification.pdf
- **MA:** https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289V2_MA_Certification.pdf
- **NBTC:** https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289CV2_NBTC_Certification.pdf
- **REACH:** https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289C_RAK7289_RAK7289CV2_RAK7289V2_REACH_Report.pdf
- **RED:** https://downloads.rakwireless.com/LoRa/WisGate/Certification/WisGate_RED_Verification.pdf
- **ROHS:** https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289C_RAK7289_RAK7289CV2_RAK7289V2_RoHS_Report.pdf
- **RCM:** https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289_RAK7289V2_RCM_Certification.pdf
- **RSM:** https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289C_RAK7289CV2_RSM_Certification.pdf
- **TDRA:** https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289CV2_TDRA_Certification.pdf
- **UKCA:** https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289C_RAK7289CV2_UKCA_Certification.pdf
- **WPC:** https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289CV2_WPC_Certification.pdf

