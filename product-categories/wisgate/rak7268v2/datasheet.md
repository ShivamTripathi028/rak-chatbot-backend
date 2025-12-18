---
slug: /product-categories/wisgate/rak7268v2/datasheet/
title: RAK7268V2/RAK7268CV2 Datasheet | LoRaWAN Gateway Specs & Features
description: Explore the RAK7268V2 datasheet for detailed LoRaWAN gateway specs. Ideal for engineers and designers evaluating RF components. Learn more today.
image: "https://images.docs.rakwireless.com/wisgate/rak7268-v2/rak7268v2.png"
keywords:
  - rak7268v2 
  - rak7268cv2
  - rak7268v2 datasheet
  - lorawan gateway datasheet
  - indoor lora gateway specs
  - lorawan edge gateway datasheet
  - wisgate edge gateway
  - 8 channel lorawan gateway
  - low power lorawan gateway
  - multi-channel packet forwarder
  - lorawan network gateway
  - long range rf communication
  - low power consumption design
  - built-in mqtt bridge
  - long range iot gateway
sidebar_label: Datasheet
date: 2022-09-26
tags:
    - rak7268v2
    - rak7268cv2
    - wisgate
    - datasheet
---

# RAK7268V2/RAK7268CV2 WisGate Edge Lite 2 Datasheet

## Overview

### Description

The **RAK7268V2 / RAK7268CV2 WisGate Edge Lite 2** is part of the **RAK Edge Series**, offering flexible connectivity options to meet the needs of a wide range of IoT applications. Designed for **indoor use**, this gateway simplifies deployment with built-in Ethernet connectivity and onboard **2.4 GHz WiFi** for easy configuration through the default WiFi AP mode. The **RAK7268CV2** version additionally supports LTE uplink communication, offering optional cellular backhaul for remote deployments or environments requiring LTE connectivity.

The gateway operates on **[WisGateOS 2](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/)**, a powerful platform that ensures enhanced security, robust functionality, and flexibility for customizations via extensions. Furthermore, the **RAK7268V2 / RAK7268CV2** integrates seamlessly with **[WisDM](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/)**, enabling fleet management and remote monitoring of multiple devices, making it an ideal choice for managing large networks of gateways.

Designed for versatile indoor deployments, this gateway supports flexible power input options—including PoE, 12 V<sub>DC</sub>, and 9–24 V<sub>DC</sub>—as well as multiple LTE configurations with either built-in antennas or external antennas.

**Product Variants Overview**

| **Gateway  Model** | **Configuration  Type** | **LTE  Module**           | **Power  Input**         |
|--------------------|-------------------------|---------------------------|--------------------------|
| RAK7268CV2         | LTE (Internal Antennas) | Built-in LTE Cat 4 module | 12 V<sub>DC</sub>   |
| RAK7268CV2         | LTE (External Antennas) | Built-in LTE Cat 4 module | 12 V<sub>DC</sub>   |
| RAK7268CV2         | LTE (Internal Antennas) | Built-in LTE Cat 4 module | 9–24 V<sub>DC</sub> |
| RAK7268V2          | Non-LTE                 | Not included              | 12 V<sub>DC</sub>   |
| RAK7268V2          | Non-LTE                 | Not included              | 9–24 V<sub>DC</sub> |

### Features

#### Hardware

- **8 LoRa channels**
- Supports **2.4 GHz WiFi AP** for easy configuration
- **100M Base-T Ethernet** with **PoE** (Power over Ethernet)
- **RP-SMA** LoRa antenna connector
- **Multi-backhaul options** with Ethernet, WiFi, and **Cellular** (only in **RAK7268CV2**)
- **SD card** for log backup and LoRa frame buffering (in case of backhaul failover)
- Optional **LTE Cat 4** network (only in **RAK7268CV2**)
- **Breathing light** for visual monitoring the gateway’s status

#### Software

- **[WisGateOS 2](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/)** for enhanced security and functionality
- **Extension add-ons** for customized gateway functionality:
  - [Compatible with WisGateOS 2 version 2.2.x or later](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/)
  - [Compatible with WisGateOS 2 versions 2.0.x and 2.1.x](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/)
- **[WisDM](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/)** for remote management and monitoring
- Built-in **Network Server**
- **Basic Station** and **Packet Forwarder** modes
- **LoRa Frame Filtering** (node whitelisting in Packet Forwarder mode)
- **MQTT v3.1 Bridging** with **TLS encryption** (compatible with ChirpStack LNS)
- LoRa frame buffering in **Packet Forwarder mode** in case of NS outage, ensuring **no data loss**

:::tip NOTE
A 9~24 V<sub>DC</sub> power input version of RAK7268V2 or RAK7268CV2 WisGate  Edge Lite 2 is available upon request. For more information or to make a  purchase, kindly contact [inquiry@rakwireless.com](mailto:inquiry@rakwireless.com).
:::

## Specifications

### Overview

#### Block Diagram

The block diagram of RAK7268V2/RAK7268CV2 shows the internal architecture of the hardware.

> **Image:** RAK7268V2 Block Diagram

> **Image:** RAK7268CV2 Block Diagram

:::tip NOTE

+ The internal block diagram applies to all models of the RAK7268V2 / RAK7268CV2 series, including both LTE and non-LTE versions.
+ The only variant-level difference is the **DC input range**, which is either **12 V fixed** or **9–24 V wide range**, depending on the model.
+ For LTE versions, the antenna type (internal or external) does not affect the internal layout—both use the same dual-antenna LTE module .

:::

#### Main Specifications

| Feature | Specifications |
| --- | --- |
| Computing | MT7628, 128 MB DDR2 RAM |
| LoRa Feature | SX1302 Mini PCIe card |
| LoRa Feature | 8 Channels |
| LoRa Feature | Frequency: EU868/IN865/RU864/US915/AU915/KR920/AS923-1/2/3/4/EU433/CN470 |
| LoRa Feature | LoRa Radio: Refer to the LoRa Radio Specifications section for detailed information. |
| WiFi Feature | Frequency: 2.4 GHz (802.11b/g/n) |
| WiFi Feature | Channels: 1-13 (2.4 GHz) |
| WiFi Feature | WiFi Radio: Refer to the WiFi Radio Specifications section for detailed information. |
| Cellular (Optional) | Nano SIM Card: 12 mm x 9 mm x 0.67 mm Supports Quectel EG95-E/EG95-NA/EC25-J/EC25-AU/EC25-E (IoT/M2M -optimized LTE Cat 4 Module) LTE Radio: Refer to the LTE Radio Specifications section for detailed information. |
| Power Supply | PoE (IEEE 802.3 af), 36-57 V DC — supported by all models |
| Power Supply | 12 V DC - 1 A – available on selected models |
| Power Supply | 9-24 V DC – available on selected models |
| Power Supply | Power consumption: 3 W (typical) |
| Antenna | LoRa: External antenna / RP-SMA connector |
| Antenna | WiFi: Internal antenna |
| Antenna | LTE: Internal antenna or External antenna / RP-SMA connector (depending on version) |
| Ingress Protection | IP30 |
| Enclosure Material | Plastic (PC+ABS) |
| Weight | 0.3 kg |
| Dimensions | 166 mm x 127.5 mm x 36 mm Gateway only (no antenna, no bracket) |
| Operating Conditions | Operating Temperature: -10˚ C to ﹢55˚ C Storage Temperature: -40˚ C to ﹢85˚ C |
| Operating Conditions | Operating Humidity: 0-95% RH non-condensing Storage Humidity: 0-95% RH non-condensing |
| Installation Method | Desktop mounting Wall mounting (via included bracket) Rail mounting (via included bracket) |

### Hardware

This section provides an overview of the hardware specifications for the RAK7268V2 / RAK7268CV2 gateway, including its interfaces, core functions, and key board parameters.

#### Interfaces

The RAK7268V2/RAK7268CV2 gateway provides several hardware interfaces, enabling various connectivity options and functionalities. The following diagrams illustrate the gateway interfaces for each configuration:

+ **12 V Power Supply**

> **Image:** RAK7268V2/RAK7268CV2 12 V power interfaces

+ **12 V Power Supply, With External LTE Antennas**

> **Image:** RAK7268CV2 power and antenna interfaces

+ **9-24 V Power Supply**

> **Image:** RAK7268V2/RAK7268CV2 9-24 V power interfaces

##### Interface Description

| Interfaces                        | Description             | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **DC 12 V / DC 9-24 V** | Power Input             | Provides power supply for the gateway.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **ETH (PoE)**                     | RJ45 (10/100 Mbps) | 10/100 Mbps Ethernet interface for wired network connectivity. 
 **PoE (Power over Ethernet)** allows the gateway to receive both power and data through a single Ethernet cable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Console**                       | Type-C USB              | Used for debugging.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Reset**                         | Reset Key               | **Short press**: Reboot the gateway. 
**Long press** (5 sec and above): Restore factory settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **NanoSIM**                       | NanoSIM Card Slot       | Slot for a NanoSIM card, enabling cellular connectivity. Available on all models; functional only with LTE-enabled versions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **TF Card**                       | SD Card Slot            | A 16 GB SD card is pre-installed in the gateway for data logging, system configurations, and other use cases that require local storage.
<div style={{ borderLeft: '6px solid #f4b400', backgroundColor: '#fff8e1', padding: '12px', borderRadius: '6px', color: '#5f370e', fontFamily: 'sans-serif' }}><strong style={{ display: 'inline-flex', alignItems: 'center', fontSize: '16px' }}>⚠️ WARNING</strong>
<span style={{ display: 'block', marginTop: '4px' }}>**Do not** eject the SD card located in the SD card slot during installation, as it stores logs and data essential for the device's performance.</span></div> |
| **LEDs**                          | Status Indicator LEDs   | PWR LED 
LoRa LED
WLAN LED 
LTE LED 
Breathing LED
LTE LED (only in RAK7268CV2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **LoRa**                          | LoRa Antenna Connector  | RP-SMA connector for external LoRa antenna, enabling LoRaWAN communication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **MAIN / AUX**                    | LTE Antenna Connectors  | Available only on models that support external LTE antennas. These versions include two RP-SMA connectors (MAIN and AUX) for connecting external LTE antennas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

##### LED Indicators Details

| LED | Status | Description |
| --- | --- | --- |
| PWR | On | Gateway is powered on |
| PWR | Off | Gateway is powered off |
| LoRa | On | LoRa module active |
| LoRa | Off | LoRa module inactive |
| LoRa | Flashing | Indicates LoRa packet transmission/reception |
| WLAN | AP Mode | AP Mode |
| WLAN | On | AP is up |
| WLAN | Off | AP is down |
| WLAN | Flashing | Data transmitting or receiving |
| WLAN | STA Mode | STA Mode |
| WLAN | Slow Flash (1 Hz) | Disconnected from WiFi network |
| WLAN | On | Connected to WiFi network |
| WLAN | Flashing | Data transmitting or receiving |
| LTE (functional only in RAK7268CV2) | Slow Flash 1 (1800 ms bright / 200 ms dark) | Searching for network (unregistered) |
| LTE (functional only in RAK7268CV2) | Slow Flash 2 (200 ms bright / 1800 ms dark) | Idle (registered to network) |
| LTE (functional only in RAK7268CV2) | Quick Flash (125 ms bright / 125 ms dark) | Data transmitting or receiving |
| Breathing LED | Red (fast blinking) | Abnormal (e.g., no internet) |
| Breathing LED | Blue (slow blinking) | Normal operation |
| Breathing LED | The breathing light can be programmed for different statuses. For detailed instructions on how to program the breathing light, refer to the appropriate installation guide based on your firmware version: Compatible with WisGateOS 2 version 2.2.x or later Compatible with WisGateOS 2 versions 2.0.x and 2.1.x | The breathing light can be programmed for different statuses. For detailed instructions on how to program the breathing light, refer to the appropriate installation guide based on your firmware version: Compatible with WisGateOS 2 version 2.2.x or later Compatible with WisGateOS 2 versions 2.0.x and 2.1.x |
| ETH | On | Linkup |
| ETH | Off | Linkdown |
| ETH | Flashing | Data transmitting and receiving |

#### RF Specifications

##### LoRa Radio Specifications

| Feature | Specifications |
| --- | --- |
| Operating Frequency | EU868/IN865/RU864/US915/AU915/KR920/AS923-1/2/3/4/EU433/CN470 |
| Transmit Power | 27 dBm (Max) |
| Receiver Sensitivity | -139 dBm (Min) |

##### WiFi Radio Specifications

| Parameter | Specifications |
| --- | --- |
| Wireless Standard | IEEE 802.11b/g/n |
| Frequency | ISM band: 2.412-2.472 GHz |
| Channels | 45670 |
| Transmit Power (The max power maybe different depending on local regulations): per chain | **802.11b** 19 dBm @1 Mbps 19 dBm @11 Mbps |
| Transmit Power (The max power maybe different depending on local regulations): per chain | **802.11g** 18 dBm @6 Mbps 16 dBm @54 Mbps |
| Transmit Power (The max power maybe different depending on local regulations): per chain | **802.11n (2.4 GHz)** 18 dBm @MCS0 (HT20) 16 dBm @MCS7 (HT20) 17 dBm @MCS0 (HT40) 15 dBm @MCS7 (HT40) |
| Receiver Sensitivity (Typical) | **802.11b** -95 dBm @1 Mbps -88 dBm @11 Mbps |
| Receiver Sensitivity (Typical) | **802.11g** -90 dBm @6 Mbps -75 dBm @54 Mbps |
| Receiver Sensitivity (Typical) | **802.11n (2.4 GHz)** -89 dBm @MCS0 (HT20) -72 dBm @MCS7 (HT20) -86 dBm @MCS0 (HT40) -68 dBm @MCS7 (HT40) |

##### LTE Radio Specifications (Optional, Available with RAK7268CV2)

| Module / Region | Supported Bands |
| --- | --- |
| EG95-E (EMEA Region) | LTE FDD: B1/B3/B7/B8/B20/B28A |
| EG95-E (EMEA Region) | WCDMA: B1/B8 |
| EG95-E (EMEA Region) | GSM/EDGE: B3/B8 |
| EG95-NA (North America) | LTE FDD: B2/B4/B5/B12/B13 |
| EG95-NA (North America) | WCDMA: B2/B4/B5 |
| EC25-J (Japan) | LTE FDD: B1/B3/B8/B18/B19/B26 |
| EC25-J (Japan) | WCDMA: B1/B6/B8/B19 |
| EC25-J (Japan) | LTE TDD: B41 |
| EC25-AU (LATAM / AU / NZ) | LTE FDD: B1/B2/B3/B4/B5/B7/B8/B28 |
| EC25-AU (LATAM / AU / NZ) | WCDMA: B1/B2/B5/B8 |
| EC25-AU (LATAM / AU / NZ) | LTE TDD: B40 |
| EC25-AU (LATAM / AU / NZ) | GSM: B2/B3/B5/B8 |
| EC25-E (Korea/India) | LTE FDD: B1/B3/B5/B7/B8/B20 |
| EC25-E (Korea/India) | WCDMA: B1/B5/B8 |
| EC25-E (Korea/India) | LTE TDD: B38/B40/B41 |
| EC25-E (Korea/India) | GSM: B3/B8 |
| Other PCIE LTE modules | Optional support for global bands (custom module) |

### Software

The RAK7268V2/RAK7268CV2 gateway runs on WisGateOS 2, a robust software platform designed for efficient network management and integration. Below are the key software features and capabilities:

For more detailed information on software configurations and usage, refer to the [WisGateOS 2 User Guide](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/).

| Category | Feature | Description |
| --- | --- | --- |
| **LoRaWAN and Network Management** | LoRaWAN Packet Forwarding | Supports Packet Forwarder and Basic Station configurations |
| **LoRaWAN and Network Management** | Built-in Server | Local LoRaWAN Network Server (LNS) integrated into the gateway for network management |
| **LoRaWAN and Network Management** | Frequency Band Setup | Configurable with different LoRaWAN frequency bands based on deployment region |
| **LoRaWAN and Network Management** | TX Power Setup | Adjustable transmit power for optimal network performance |
| **LoRaWAN and Network Management** | Automatic Data Recovery | Ensures reliable data transmission even during network disruptions |
| **LoRaWAN and Network Management** | Server Address and Port Setup | Custom configuration for LoRaWAN Network Server communication |
| **LoRaWAN and Network Management** | Supports LoRaWAN Class A and C | Fully compatible with LoRaWAN devices operating in Class A and C |
| **LoRaWAN and Network Management** | Uplink Backup | Enables automatic switchover to a backup uplink (e.g., LTE or WiFi) when the primary uplink fails. Requires Multi-WAN configuration. |
| **LoRaWAN and Network Management** | Location Setup | Manual or automatic setup of gateway location (e.g., GPS coordinates) |
| **Connectivity and Network Services** | WiFi Client/AP Mode | Connect to existing network or act as an access point |
| **Connectivity and Network Services** | DHCP Server/Client | Dynamic IP address allocation for both server and client roles |
| **Connectivity and Network Services** | NAT and Router Module | Enables router functionality with Network Address Translation |
| **Connectivity and Network Services** | WireGuard / OpenVPN | Secure communication tunnel for remote access and management |
| **Connectivity and Network Services** | LTE APN Setup | Configures Access Point Name for LTE connectivity |
| **Monitoring and Security** | Statistics and Data Logger | Tracks performance metrics and logs operational data |
| **Monitoring and Security** | Firewall | Provides basic firewall functions for traffic control and security |
| **Monitoring and Security** | SSH2 | Secure Shell access for remote troubleshooting and management |
| **Monitoring and Security** | Ping Watchdog | Monitors connectivity and triggers recovery if the connection fails |
| **User Interface and Management** | Web UI | Web-based interface for configuration and monitoring |
| **User Interface and Management** | WisDM | Cloud platform for remote management and monitoring |
| **User Interface and Management** | Gateway OTA management | Over-the-air firmware management for seamless updates |
| **User Interface and Management** | MQTT Bridge | Integration with IoT platforms using MQTT protocol |
| **User Interface and Management** | Firmware Updates | Over-the-air updates for easy firmware upgrades |
| **User Interface and Management** | NTP | Synchronizes the gateway system time for accurate timestamp recording |

### Firmware

The firmware is built on **OpenWrt**, providing a flexible and secure foundation for the gateway. It features an intuitive **web UI** for straightforward configuration and management, as well as **SSH2** support for remote management. **WisGateOS 2** also supports the installation of various extensions, including **OpenVPN**, **WireGuard**, and custom logo configurations.

For more details on available extensions, refer to the [WisGateOS 2 Extensions Guide](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/overview/#supported-extensions).

|                  Model                   |                                            Source                                            |
|:----------------------------------------:|:--------------------------------------------------------------------------------------------:|
| RAK7268V2/RAK7268CV2 WisGate Edge Lite 2 | [Download](https://downloads.rakwireless.com/LoRa/WisGateOS2/WisGateOS2_Latest_Firmware.zip) |

## Certification

### Certifications
- **ANATEL:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268V2_ANATEL_Certification.pdf
- **ANATEL:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268CV2_ANATEL_Certification.pdf
- **CE:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_RAK7268V2_RAK7268C_RAK7268CV2_CE_Certification.pdf
- **ISED:** https://downloads.rakwireless.com/LoRa/RAK7268V2/Certification/RAK7268_RAK7268V2_IC_Certification.pdf
- **ISED:** https://downloads.rakwireless.com/LoRa/RAK7268V2/Certification/RAK7268C_RAK7268CV2_IC_Certification.pdf
- **FCC:** https://downloads.rakwireless.com/LoRa/RAK7268V2/Certification/RAK7268_RAK7268V2_FCC_Certification.pdf
- **FCC:** https://downloads.rakwireless.com/LoRa/RAK7268V2/Certification/RAK7268C_RAK7268CV2_FCC_Certification.pdf
- **JRL:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_RAK7268V2_RAK7268C_RAK7268CV2_JRL_Certification.pdf
- **JTBL:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_RAK7268V2_JTBL_Certification.pdf
- **KC:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268V2_RAK7268CV2_KC_Certification.pdf
- **RCM:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_RAK7268V2_RAK7268C_RAK7268CV2_RCM_Certification.pdf
- **REACH:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268C_RAK7268CV2_RAK7268_RAK7268V2_REACH_Report.pdf
- **RED:** https://downloads.rakwireless.com/LoRa/WisGate/Certification/WisGate_RED_Verification.pdf
- **ROHS:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268C_RAK7268CV2_RAK7268_RAK7268V2_RoHS_Report.pdf
- **RSM:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_RAK7268V2_RAK7268C_RAK7268CV2_RSM_Certification.pdf
- **UKCA:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_RAK7268V2_RAK7268C_RAK7268CV2_UKCA_Certification.pdf

### FCC Caution

Any changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate the equipment.

This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

:::tip NOTE
This equipment has been tested and found to comply with the limits for a Class B digital device, according to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation. This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used according to the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:

1. Reorient or relocate the receiving antenna.
2. Increase the separation between the equipment and the receiver.
3. Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
4. Consult the dealer or an experienced radio/TV technician for help.
:::

### FCC Radiation Exposure Statement

This equipment complies with FCC radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 20 cm between the radiator and your body.

