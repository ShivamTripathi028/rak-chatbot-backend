---
title: RAK7285 WisGate Edge Ultra Datasheet
description: Access the RAK7285/RAK7285C WisGate Edge Ultra datasheet, featuring IP67 enclosure, 8-channel LoRaWAN, and multi-backhaul options for IoT deployments.
image: "https://images.docs.rakwireless.com/wisgate/rak7285/rak7285.png"
keywords:
 - RAK7285
 - WisGate Edge Ultra
 - LoRaWAN gateway
 - 8 channel gateway
 - multi-backhaul gateway
sidebar_label: Datasheet
---

# RAK7285/RAK7285C WisGate Edge Ultra Datasheet

## Overview

### Descriptions

**RAK7285 WisGate Edge Ultra** is the latest version of the RAK WisGate Edge series, designed to overcome the limitations of half-duplex communication. It's tailored to meet the demands of high-density network deployments, particularly for smart city infrastructure, metering applications, and other scenarios requiring reliable two-way communication at scale.

This gateway supports up to 8 LoRa channels in full-duplex (a 16-channel variant is coming soon), with multi-backhaul options including Ethernet, Wi-Fi, and Cellular connectivity. Its integrated advanced cavity diplexers not only provide exceptional out-of-band interference suppression but also provide lightning protection for the LoRa antennas, ensuring uninterrupted and secure full-duplex communication.

In addition, RAK7285 operates under [WisGateOS 2](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/), which is built on the latest OpenWrt kernel. The OS Web UI features a new design and supports multiple extension installations, enabling remote management using [WisDM](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/) for personalized gateway customization.

### Features

#### Hardware

- IP67 industrial-grade enclosure with cable glands
- PoE (802.3at) + Surge Protection
- 8 LoRa channels in full-duplex (16 channels variant is coming soon)
- Built-in cavity diplexers for out-of-band interference suspension
- Backhaul: Wi-Fi, Ethernet, and LTE (available with RAK7285C)
- GPS
- Supports 9~36 V<sub>DC</sub> and RAK Solar Battery Kit
- External antennas for GPS and LoRa
- Dying Gasp (optional)

#### Software

- [WisGateOS 2](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/)
- **WisGateOS 2 Extensions**: Adds support for features such as OpenVPN, WireGuard VPN, and more. Use the appropriate installation guide based on your WisGateOS 2 version:
    - [For WisGateOS 2 version 2.2.x or later](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/)
    - [For WisGateOS 2 versions 2.0.x and 2.1.x](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/)
- Remote management with WisDM Fleet Management
- Built-in Network Server (LoRaWAN support v1.0.3)
- LoRaWAN Stack support with Semtech SX1303
- LoRa Frame filtering (node whitelisting)
- MQTT v3.1 bridging with TLS encryption
- Buffering of LoRa frames in Packet Forwarder mode in case of NS outage (automatic data recovery)
- Full-duplex
- Listen Before Talk
- Fine timestamping

## Specifications

### Overview
#### Block Diagram

The block diagram of RAK7285/RAK7285C shows the internal architecture of the hardware.

> **Image:** RAK7285 Block Diagram

:::tip NOTE
+ The LTE module (RAK8213) is optional. Only RAK7285C integrates the LTE module.
+ The LoRa module 2 is optional. Only 16-channel gateway is available.
:::

#### Main Specifications

| Feature | Specifications |
| --- | --- |
| Computing | MT7628, DDR2 RAM 128 MB |
| Frequency | US915 AU915 |
| Wi-Fi Feature | Frequency: 2.4 GHz (802.11b / g / n) |
| Wi-Fi Feature | 2x2 MIMO |
| Wi-Fi Feature | RX Sensitivity:-95 dBm (Min) |
| Wi-Fi Feature | TX Power: 20 dBm (Max) |
| Wi-Fi Feature | Operation channels: 2.4 GHz, 1-13 |
| LoRa Feature | SX1303 On Board |
| LoRa Feature | 8 LoRa channels in full-duplex (16 channels variant is coming soon) |
| LoRa Feature | RX Sensitivity:-139 dBm (Min) |
| LoRa Feature | TX Power: 30 dBm (Max) |
| LoRa Feature | Listen Before Talk |
| Cellular Feature (available with RAK7285C) | Nano SIM Card: 12.30 mm x 8.80 mm x 0.67 mm Supports Quectel EG95-E / EG95-NA / EC25-AU (IoT / M2M -optimized LTE Cat 4 Module) |
| Cellular Feature (available with RAK7285C) | EG95-E for EMEA Region (Europe, Middle East and Africa) |
| Cellular Feature (available with RAK7285C) | LTE FDD: B1 / B3 / B7 / B8 / B20 / B28A WCDMA: B1 / B8 GSM/EDGE: B3 / B8 |
| Cellular Feature (available with RAK7285C) | EG95-NA for North America Region |
| Cellular Feature (available with RAK7285C) | LTE FDD: B2 / B4 / B5 / B12 / B13 WCDMA: B2 / B4 / B5 |
| Cellular Feature (available with RAK7285C) | EC25-AU for Latin America, Australia, and New Zealand Region |
| Cellular Feature (available with RAK7285C) | LTE-FDD: B1 / B2 / B3 / B4 / B5 / B7 / B8 / B28 LTE-TDD: B40 WCDMA: B1/B2/B5/B8 GSM/EDGE: B2 / B3 / B5 / B8 |
| Power Supply | PoE (IEEE 802.3at): 42\~57 VDC 9~36 VDC Compatible with RAK Battery Plus |
| ETH | RJ45 (10/100 M) |
| Antenna | LoRa: N-Type connector (one for the 8-channel gateway and two for the 16-channel gateway) |
| Antenna | GPS: One N-Type connector |
| Antenna | Wi-Fi: Two N-Type connectors |
| Antenna | LTE: Two N-Type connectors( only for RAK7285C) |
| Diplexer | AU915: Frequency: - Rx: 915 ~ 920 MHz - Tx: 923 ~ 928 MHz Insertion loss: - Rx: 2.6 (Typical) / 4.0 (Maximum) - Tx: 2.6 (Typical) / 3.8 (Maximum) Isolation between Rx and Tx: > 80 dB Return loss: <-18 dB Impedance: 50 Ω |
| Diplexer | US915: Frequency: - Rx: 902 ~ 915 MHz - Tx: 923 ~ 928 MHz Insertion loss: - Rx: 1.3 (Typical) / 1.6 (Maximum) - Tx: 1.8 (Typical) / 2.0 (Maximum) Isolation between Rx and Tx: > 90 dB Return loss: <-18 dB Impedance: 50 Ω |
| Ingress Protection | IP67 |
| Enclosure Material | Aluminum |
| Dimensions | 310 mm x 290 mm x 146 mm |
| Operating Temperature | -30˚ C to +55˚ C |
| Storage Temperature | -40˚ C to ﹢85˚ C |
| Operating Humidity | 0~95% RH non-condensing |
| Storage Humidity | 0~95% RH non-condensing |
| Installation Method | Pole or wall mounting |

### Hardware

The hardware specification covers the interfacing of the RAK7285/RAK7285C and its corresponding functionalities. It also presents the parameters and the standard values of the board.

#### Interfaces

> **Image:** RAK7285/RAK7285C Interfaces

:::tip NOTE
+ The SD card in the SD card slot must not be ejected. Doing so might affect the device's performance, as various logs and data are stored on it.
+ The SIM card slot of the cellular versions is not hot-swappable. Ensure the gateway is switched off before inserting or ejecting the SIM card.
+ The available antenna interfaces vary between variants. For example, two N-type LTE interfaces are available on the RAK7285C, but not on the RAK7285.
:::

##### Reset Key Functions

The functions of the Reset key are as follows:

- **Short press**: Restart the gateway.
- **Long press** (5 seconds or more): Restore factory settings.

##### LED Indicators

The status of the LEDs is described below. Refer to the LED printing on the main board.

| LEDs | Status Indication Description |
| --- | --- |
| LED 1 (PWR) | Power indicator: The LED is on when device power is on. |
| LED 2 (ETH) | ON: Linkup |
| LED 2 (ETH) | OFF: Linkdown |
| LED 2 (ETH) | Flicker: Data transmitting and receiving |
| LED 3 (LoRa 1) | ON: LoRa 1 is working |
| LED 3 (LoRa 1) | OFF: LoRa 1 is not working |
| LED 3 (LoRa 1) | Flicker: Indicate LoRa 1 Packet receiving and sending |
| LED 4 (WLAN) | AP Mode: |
| LED 4 (WLAN) | ON: The AP is up |
| LED 4 (WLAN) | Flicker: Data receiving and sending |
| LED 4 (WLAN) | STA Mode: |
| LED 4 (WLAN) | Slow flicker (1 Hz): Disconnected |
| LED 4 (WLAN) | ON: Connected |
| LED 4 (WLAN) | Flicker: Data receiving and sending |
| LED 5 (LTE) | Slow Flicker (200 ms Bright / 1800 ms Dark): Network searching |
| LED 5 (LTE) | Slow flicker (200 ms Dark / 1800 ms Bright): Idle |
| LED 5 (LTE) | Fast flicker (125 ms Bright / 125 ms Dark): Ongoing data transfer |
| LED 5 (LTE) | ON: Voice is working |
| LED 6 (LoRa 2 for 16 channel) | ON: LoRa 2 is working |
| LED 6 (LoRa 2 for 16 channel) | OFF: LoRa 2 is not working |
| LED 6 (LoRa 2 for 16 channel) | Flicker: Indicate LoRa 2 Packet receiving and sending |

#### RF Specifications

##### Wi-Fi Radio Specifications

| Feature | Specifications |
| --- | --- |
| Wireless Standard | IEEE 802.11b / g / n |
| Operating Frequency | ISM band: 2.412 ~ 2.472 GHz |
| Operation Channels | 2.4 GHz: 1-13 |
| Transmit Power (The max power maybe different depending on local regulations): per chain | 802.11b |
| Transmit Power (The max power maybe different depending on local regulations): per chain | 19 dBm @1 Mbps |
| Transmit Power (The max power maybe different depending on local regulations): per chain | 19 dBm @11 Mbps |
| Transmit Power (The max power maybe different depending on local regulations): per chain | 802.11g |
| Transmit Power (The max power maybe different depending on local regulations): per chain | 18 dBm @6 Mbps |
| Transmit Power (The max power maybe different depending on local regulations): per chain | 16 dBm @54 Mbps |
| Transmit Power (The max power maybe different depending on local regulations): per chain | 802.11n (2.4 GHz) |
| Transmit Power (The max power maybe different depending on local regulations): per chain | 18 dBm @MCS0 (HT20) |
| Transmit Power (The max power maybe different depending on local regulations): per chain | 16 dBm @MCS7 (HT20) |
| Transmit Power (The max power maybe different depending on local regulations): per chain | 17 dBm @MCS0 (HT40) |
| Transmit Power (The max power maybe different depending on local regulations): per chain | 15 dBm @MCS7 (HT40) |
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

##### LoRa Radio Specifications

| Feature | Specifications |
| --- | --- |
| Operating Frequency | US915/AU915 |
| Transmit Power | 30 dBm (Max) |
| Receiver Sensitivity | -139 dBm (Min) |

#### Mechanical Characteristics

| Parameter          | Value                                                                             |
|--------------------|-----------------------------------------------------------------------------------|
| Dimensions         | 310 mm x 290 mm x 146 mm Gateway only (no antenna, no bracket) |
| Ingress protection | IP67                                                                              |

#### Environmental Requirements

| Parameter | Value |
| --- | --- |
| Operating Conditions | Operating Temperature:-30˚ C to ﹢55˚ C Storage Temperature:-40˚ C to ﹢85˚ C Operating Humidity: 0 ~ 95% RH non-condensing Storage Humidity: 0 ~ 95% RH non-condensing |

### Software

| LoRa | Network | Management |
| --- | --- | --- |
| Gateway OTA management | Wi-Fi Client mode | WisDM |
| LoRa Package Forward (Packet Forwarder, Basics Station) | LTE APN Setup | SSH2, NTP |
| Frequency Band Setup | Support 802.1q | Firmware Update |
| Server Address and Port Setup | Uplink backup | LoRa Packet Forwarder |
| TX Power Setup | Firewall | Built-in Network Server |
| Data Logger | DHCP Server/Client | MQTT Bridge |
| Location Setup | Wi-Fi AP mode | OpenVPN, Ping Watch Dog |
| Statistic |  | WEB UI |
| Supports Class A, B, and C |  |  |
| Automatic Data Recovery |  |  |

### Firmware

The firmware is based on OpenWRT. It features a web UI that enables easy configuration and management of the device, as well as the option for SSH2 management. The WisGateOS V2 supports the installation of extensions (OpenVPN, WireGuard, Custom Logo, etc.).

Detailed information about the extensions can be found on the [WisGateOS 2 Extensions](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/overview/#supported-extensions).

|                Model                | Firmware Version |                                                         Source                                                          |
|:-----------------------------------:|:----------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| RAK7285/RAK7285C WisGate Edge Ultra |     v2.2.13      | [Download](https://downloads.rakwireless.com/LoRa/WisGateOS2/WisGateOS2_Latest_Firmware.zip) |

## Models/Bundles

| Part Number | 8 Channel SX1303 | 16 Channel SX1303 | Cat4 Cellular | GPS | Wi-Fi |
| --- | --- | --- | --- | --- | --- |
| RAK7285C-XYZ | √ |  | √ | √ | √ |
| RAK7285C-XYZ |  | √ | √ | √ | √ |
| RAK7285-XYZ | √ |  |  | √ | √ |
| RAK7285-XYZ |  | √ |  | √ | √ |

## Certification

### Certifications
- **ANATEL:** https://downloads.rakwireless.com/LoRa/RAK7285/Certification/RAK7285_RAK7285C_ANATEL_Certification.pdf

