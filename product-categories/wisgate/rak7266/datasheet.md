---
slug: /product-categories/wisgate/RAK7266/datasheet/
title: RAK7266 Datasheet | LoRaWAN Gateway Specs & Features
description: Explore the RAK7266 datasheet for detailed LoRaWAN gateway specs. Ideal for engineers and designers evaluating RF components. Learn more today.
image: "https://images.docs.rakwireless.com/wisgate/rak7266/RAK7266.png"
keywords:
  - rak7266 datasheet
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
tags:
  - rak7266
  - wisgate
  - datasheet
sidebar_label: Datasheet
date: 2026-06-26
---

# RAK7266 WisGate Soho Lite Datasheet

## Overview

### Description

The **RAK7266 WisGate Soho Lite** is an indoor LoRaWAN gateway from the **RAK Soho Series**, designed for versatile and compact IoT deployments. It comes with an **integrated LTE Cat 1 module** and offers **multiple backhaul options**, including **cellular (LTE)**, **WiFi**, and **Ethernet**, ensuring versatile deployment options in environments with or without wired internet access.

This gateway supports **8 LoRa channels** and onboards **2.4 GHz WiFi** for easy configuration through the default WiFi AP mode. An **Ethernet port** is available for wired network access when needed. The device is powered via a **stable 12V DC input**, making it well-suited for controlled indoor environments such as smart panels, utility cabinets, or fixed installations.

Depending on the variant, LTE antennas may be **internal** or **externally connected via RP-SMA connectors**, allowing users to select the best option for signal conditions and installation constraints.

The RAK7266 runs on **WisGateOS 2**, a secure, modular firmware based on OpenWrt developed by RAK. It provides access to a wide range of features, including extension modules, a built-in LoRaWAN Network Server, and advanced system diagnostics. Additionally, it supports integration with **WisDM** for centralized management and fleet monitoring, making it a powerful and practical solution for LTE-based indoor deployments.

### Features

#### Hardware

- **8 LoRa channels**
- Supports **2.4 GHz WiFi**, with **AP mode enabled by default** for easy configuration
- **100M Base-T Ethernet port** (for network access, no PoE)
- **RP-SMA** LoRa antenna connector
- An integrated **LTE Cat 1 module** for cellular backhaul
- Multi backhaul options with **Ethernet, WiFi, and Cellular**
- **Breathing light** for visual status indication

#### Software

- **[WisGateOS 2](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/?intsource=docs_center&intmedium=organic&intcampaign=rak7266_documentation_datasheet_page&intterm=wisgate_os2&intcontent=documentation_link)** – A secure, OpenWrt-based OS developed by RAK for enhanced stability and flexibility.
- **Extension add-ons** for customized gateway functionality:
  - [Compatible with WisGateOS 2 version 2.2.x or later](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/)
  - [Compatible with WisGateOS 2 versions 2.0.x and 2.1.x](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/)
- **[WisDM](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/?intsource=docs_center&intmedium=organic&intcampaign=rak7266_documentation_datasheet_page&intterm=wisdm&intcontent=documentation_link)** for remote management and monitoring
- Built-in **Network Server**
- **Basic Station** and **Packet Forwarder** modes
- **LoRa Frame Filtering** (node whitelisting in Packet Forwarder mode)
- **MQTT v3.1 Bridging** with **TLS encryption**
- LoRa frame buffering in **Packet Forwarder mode** in case of NS outage, ensuring **no data loss**

## Specifications

### Overview

#### Block Diagram

The block diagram of RAK7266 shows the internal architecture of the hardware.

> **Image:** RAK7266 Block Diagram

#### Main Specifications

| Feature | Specifications |
| --- | --- |
| Computing | MT7628, 128 MB DDR2 RAM |
| LoRa Feature | SX1302 / SX1303 Mini PCIe card ( The default configuration uses the SX1302 Mini PCIe card, with an SX1303 version available upon request. ) |
| LoRa Feature | 8 Channels |
| LoRa Feature | Frequency: EU868/IN865/RU864/US915/AU915/KR920/AS923-1-2-3-4/EU433/CN470 |
| LoRa Feature | LoRa Radio: Refer to the [LoRa Radio Specifications](#lora-radio-specifications) section for detailed information. |
| WiFi Feature | Frequency: 2.4 GHz (802.11b/g/n) |
| WiFi Feature | Channels: 1-13 |
| WiFi Feature | WiFi Radio: Refer to the [WiFi Radio Specifications](#wifi-radio-specifications) section for detailed information. |
| Cellular | Nano SIM Card: 12 mm x 9 mm x 0.67 mm Supports Quectel EG915U-EU / EG915U-LA / EG915Q-NA(IoT / M2M -LTE Cat 1 module) LTE Radio: Refer to the [LTE Radio Specifications](#lte-radio-specifications) section for detailed information. |
| Power Supply | 12 V DC |
| Antenna | LoRa: External antenna / RP-SMA connector |
| Antenna | WiFi: Internal antenna |
| Antenna | LTE: Internal antenna or External antenna / RP-SMA connector |
| Ingress Protection | IP30 |
| Enclosure Material | Plastic (PC+ABS) |
| Weight | 0.3 kg |
| Dimensions | 166 mm x 127.5 mm x 36 mm Gateway only (no antenna, no bracket) |
| Operating Conditions | Operating Temperature: -10˚ C to ﹢55˚ C Storage Temperature: -40˚ C to ﹢85˚ C Operating Humidity: 0\~95% RH non-condensing Storage Humidity: 0\~95% RH non-condensing |
| Installation Method | Desktop mounting Wall mounting (via included bracket) Rail mounting (via included bracket) |

### Hardware

The hardware specification covers the interfacing of the RAK7266 gateway and its corresponding functionalities, along with the parameters and standard values of the board.

#### Interfaces

The RAK7266 gateway provides several hardware interfaces, enabling various connectivity options and functionalities.

> **Image:** RAK7266 interfaces

##### Interface Description

| Interfaces  | Description             | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **DC 12V**  | Power Input             | Provides power supply for the gateway.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **ETH**     | RJ45 (10/100 Mbps) | 10/100 Mbps Ethernet interface for wired network connectivity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Console** | Type-C USB              | Used for debugging.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Reset**   | Reset Key               | **Short press**: Reboot the gateway. 
**Long press** (5 sec and above): Restore factory settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **NanoSIM** | NanoSIM Card Slot       | Slot for a NanoSIM card, enabling cellular connectivity.
<div style={{ borderLeft: '6px solid #f4b400', backgroundColor: '#fff8e1', padding: '12px', borderRadius: '6px', color: '#5f370e', fontFamily: 'sans-serif' }}><strong style={{ display: 'inline-flex', alignItems: 'center', fontSize: '16px' }}>⚠️ WARNING</strong>
<span style={{ display: 'block', marginTop: '4px' }}> The SIM card slot of the cellular versions is not hot-swappable. Make sure the gateway is switched off before inserting or ejecting the SIM card.</span></div>                                                                                                 |
| **TF Card** | SD Card Slot            | A 16 GB SD card is pre-installed in the gateway for data logging, system configurations, and other use cases that require local storage.
<div style={{ borderLeft: '6px solid #f4b400', backgroundColor: '#fff8e1', padding: '12px', borderRadius: '6px', color: '#5f370e', fontFamily: 'sans-serif' }}><strong style={{ display: 'inline-flex', alignItems: 'center', fontSize: '16px' }}>⚠️ WARNING</strong>
<span style={{ display: 'block', marginTop: '4px' }}>**Do not** eject the SD card located in the SD card slot during installation, as it stores logs and data essential for the device's performance.</span></div> |
| **LEDs**    | Status Indicator LEDs   | <ul><li>PWR LED</li><li>LoRa LED</li><li>WLAN LED</li><li>LTE LED</li><li>Breathing LED</li><li>ETH LED</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **LoRa**    | LoRa Antenna Connector  | RP-SMA connector for external LoRa antenna, enabling LoRaWAN communication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **MAIN**    | LTE Antenna Connector   | RP-SMA connector for external LTE antenna.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **AUX**     | Reserve                 | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

##### LED Indicators Details

| LEDs | Status Indication Description |  |
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
| Breathing LED | The breathing light can be programmed for different statuses. For detailed instructions on how to program the breathing light, refer to the RAK Breathing Light Extension . | The breathing light can be programmed for different statuses. For detailed instructions on how to program the breathing light, refer to the RAK Breathing Light Extension . |
| ETH | On | Linkup |
| ETH | Off | Linkdown |
| ETH | Flashing | Data transmitting and receiving |

#### RF Specifications

##### LoRa Radio Specifications

| Parameter            | Specifications                                                |
|----------------------|---------------------------------------------------------------|
| Operating Frequency  | EU868/IN865/RU864/US915/AU915/KR920/AS923-1/2/3/4/EU433/CN470 |
| Transmit Power       | 27 dBm (Max)                                             |
| Receiver Sensitivity | -139 dBm (Min)                                           |

##### WiFi Radio Specifications

| Parameter | Specifications |
| --- | --- |
| Wireless Standard | IEEE 802.11b/g/n |
| Operating Frequency | ISM band: 2.412-2.472 GHz |
| Operation Channels | 2.4 GHz: 1-13 |
| Transmit Power: per chain (The max power differs depending on local regulations.) | 802.11b 19 dBm @ 1 Mbps 19 dBm @ 11 Mbps |
| Transmit Power: per chain (The max power differs depending on local regulations.) | 802.11g 18 dBm @ 6 Mbps 16 dBm @ 54 Mbps |
| Transmit Power: per chain (The max power differs depending on local regulations.) | 802.11n (2.4 GHz) 18 dBm @ MCS0 (HT20) 16 dBm @ MCS7 (HT20) 17 dBm @ MCS0 (HT40) 15 dBm @ MCS7 (HT40) |
| Receiver Sensitivity (Typical) | 802.11b -95 dBm @ 1 Mbps -88 dBm @ 11 Mbps |
| Receiver Sensitivity (Typical) | 802.11g -90 dBm @ 6 Mbps -75 dBm @ 54 Mbps |
| Receiver Sensitivity (Typical) | 802.11n (2.4 GHz) -89 dBm @ MCS0 (HT20) -72 dBm @ MCS7 (HT20) -86 dBm @ MCS0 (HT40) -68 dBm @ MCS7 (HT40) |

##### LTE Radio Specifications

| Module / Region                                        | Supported Bands                                                              |
|--------------------------------------------------------|------------------------------------------------------------------------------|
| EG915U-EU for EMEA/Brazil/Australia/New Zealand Region | LTE FDD: B1 / B3 / B5 / B7 / B8 / B20 / B28
GSM: B2 / B3 / B5 / B8      |
| EG915U-LA for Latin America Region                     | LTE FDD: B2 / B3 / B4 / B5 / B7 / B8 / B28 / B66
GSM: B2 / B3 / B5 / B8 |
| EG915Q-NA for North America Region                     | LTE FDD: B2 / B4 / B5 / B12 / B13 / B66 / B71                                |

### Software

The RAK7266 gateway runs on WisGateOS 2, a robust software platform designed for efficient network management and integration. Below are the key software features and capabilities:

For more detailed information on software configurations and usage, refer to the [WisGateOS 2 User Guide](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/?intsource=docs_center&intmedium=organic&intcampaign=rak7266_documentation_overview_page&intterm=wisgate_os2&intcontent=documentation_link).

| Category | Feature | Description |
| --- | --- | --- |
| LoRaWAN and Network Management | LoRaWAN Packet Forwarding | Supports Packet Forwarder and Basic Station configurations |
| LoRaWAN and Network Management | Built-in Server | Local LoRaWAN Network Server (LNS) integrated into the gateway for network management |
| LoRaWAN and Network Management | Frequency Band Setup | Configurable with different LoRaWAN frequency bands based on deployment region |
| LoRaWAN and Network Management | TX Power Setup | Adjustable transmit power for optimal network performance |
| LoRaWAN and Network Management | Automatic Data Recovery | Ensures reliable data transmission even during network disruptions |
| LoRaWAN and Network Management | Server Address and Port Setup | Custom configuration for LoRaWAN Network Server communication |
| LoRaWAN and Network Management | Supports LoRaWAN Class A and C | Fully compatible with LoRaWAN devices operating in Class A and C |
| LoRaWAN and Network Management | Uplink Backup | Enables automatic switchover to a backup uplink (e.g., LTE or WiFi) when the primary uplink fails. Requires Multi-WAN configuration. |
| LoRaWAN and Network Management | Location Setup | Manual or automatic setup of gateway location (e.g., GPS coordinates) |
| Connectivity and Network Services | WiFi Client/AP Mode | Connect to existing network or act as an access point |
| Connectivity and Network Services | DHCP Server/Client | Dynamic IP address allocation for both server and client roles |
| Connectivity and Network Services | NAT and Router Module | Enables router functionality with Network Address Translation |
| Connectivity and Network Services | WireGuard / OpenVPN | Secure communication tunnel for remote access and management |
| Connectivity and Network Services | LTE APN Setup | Configures Access Point Name for LTE connectivity |
| Monitoring and Security | Statistics and Data Logger | Tracks performance metrics and logs operational data |
| Monitoring and Security | Firewall | Provides basic firewall functions for traffic control and security |
| Monitoring and Security | SSH2 | Secure Shell access for remote troubleshooting and management |
| Monitoring and Security | Ping Watchdog | Monitors connectivity and triggers recovery if the connection fails |
| User Interface and Management | Web UI | Web-based interface for configuration and monitoring |
| User Interface and Management | WisDM | Cloud platform for remote management and monitoring |
| User Interface and Management | Gateway OTA management | Over-the-air firmware management for seamless updates |
| User Interface and Management | MQTT Bridge | Integration with IoT platforms using MQTT protocol |
| User Interface and Management | Firmware Updates | Over-the-air updates for easy firmware upgrades |
| User Interface and Management | NTP | Synchronizes the gateway system time for accurate timestamp recording |

### Firmware

The firmware is built on **OpenWrt**, providing a flexible and secure foundation for the gateway. It features an intuitive **web UI** for straightforward configuration and management, as well as **SSH2** support for remote management. **WisGateOS 2** also supports the installation of various extensions, including **OpenVPN**, **WireGuard**, and custom logo configurations. For more details on available extensions, refer to the [WisGateOS 2 Extensions Guide](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/overview/?intsource=docs_center&intmedium=organic&intcampaign=rak7266_documentation_overview_page&intterm=extension-add-ons&intcontent=documentation_link).

|           Model           |                                                                                                                        Source                                                                                                                         |
|:-------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| RAK7266 WisGate Soho Lite | [Download](https://downloads.rakwireless.com/LoRa/WisGateOS2/WisGateOS2_Latest_Firmware.zip?utm_source=docs_center&utm_medium=organic&utm_campaign=rak7266-documentation-datasheet-page&utm_term=rak7266-firmware-download&utm_content_download-link) |

## Certification

### Certifications
- **FCC:** https://downloads.rakwireless.com/LoRa/RAK7266/Certification/RAK7266_FCC_Certification.pdf
- **ISED:** https://downloads.rakwireless.com/LoRa/RAK7266/Certification/RAK7266_ISED_Certification.pdf
- **RED:** https://downloads.rakwireless.com/LoRa/WisGate/Certification/WisGate_RED_Verification.pdf

