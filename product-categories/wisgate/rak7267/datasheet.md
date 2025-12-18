---
title: RAK7267 WisGate Soho Pro Datasheet
description: Comprehensive datasheet for RAK7267 WisGate Soho Pro, an 8-channel outdoor LoRaWAN gateway with IP67-rated enclosure, supporting Wi-Fi and LTE backhaul, GPS, and internal antennas for LoRa, LTE, Wi-Fi, and GPS.
image: https://images.docs.rakwireless.com/wisgate/rak7267/rak7267.png
keywords:
    - RAK7267
    - WisGate Soho guides
    - LoRaWAN gateway
    - 8 channel gateway
sidebar_label: Datasheet
---

# RAK7267 WisGate Soho Pro Datasheet

## Overview

### Description

The RAK7267 WisGate Soho Pro is an innovative 8-channel LoRaWAN® gateway designed for outdoor deployments. It supports Wi-Fi and cellular connectivity.

This gateway uses an IP67-rated Unify Enclosure, a weatherproof and flame-retardant enclosure made of UV stabilized ABS plastic that protects internal components from dust and water. The new enclosure is designed to allow the LoRa, LTE, Wi-Fi, and GPS antennas to be inside the enclosure.

In addition, RAK7267 operates under <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#overview" target="_blank">WisGateOS 2</a>, which is built on the latest OpenWrt kernel. The OS Web UI features a new design and supports multiple extension installations, enabling remote management using <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/" target="_blank">WisDM</a> for personalized gateway customization.

### Features

#### Hardware

- IP67 Unify enclosure
- LoRa Concentrator for up to **8 channels**
- Backhaul: Wi-Fi and LTE
- GPS
- Supports 9\~36 V<sub>DC</sub> power supply and RAK Solar Battery Kit
- Internal antenna for LoRa, LTE, Wi-Fi, and GPS

#### Software

- <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#overview" target="_blank">WisGateOS 2</a>
- **WisGateOS 2 Extensions**: Adds support for features such as OpenVPN, WireGuard VPN, and more. Use the appropriate installation guide based on your WisGateOS 2 version:
    - <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/" target="_blank">For WisGateOS 2 version 2.2.x or later</a>
    - <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/" target="_blank">For WisGateOS 2 versions 2.0.x and 2.1.x</a>
- Remote management with <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/" target="_blank">WisDM</a> Fleet Management
- Built-in Network Server (LoRaWAN support V 1.0.3)
- LoRaWAN Stack support with Semtech SX1303
- LoRa Frame filtering (node whitelisting in Packet Forwarder mode)
- MQTT v3.1 bridging with TLS encryption
- Buffering of LoRa frames in Packet Forwarder mode in case of NS outage (no data loss)
- Listen Before Talk
- Fine timestamping

## Specifications

### Overview

This section presents the block diagram for the RAK7267 that shows the internal architecture of the hardware.

#### Block Diagram

> **Image:** RAK7267 Block Diagram

#### Main Specifications

| Feature | Specifications |
| --- | --- |
| Computing | MT7628, DDR2 RAM 128 MB |
| LoRa Feature | SX1303 On Board |
| LoRa Feature | 8 Channels |
| LoRa Feature | Frequency: EU868/IN865/RU864/US915/AU915/KR920/AS923-1/2/3/4 |
| LoRa Feature | Listen Before Talk |
| LoRa Feature | LoRa Radio: Refer to theLoRa Radio Specificationssection for detailed information. |
| Wi-Fi Feature | Frequency: 2.4 GHz (802.11 b / g / n) |
| Wi-Fi Feature | Channels: 1-13 |
| Wi-Fi Feature | 2x2 MIMO |
| Wi-Fi Feature | Wi-Fi Radio: Refer to theWi-Fi Radio Specificationssection for detailed information. |
| Cellular Feature | Nano SIM Card:12 mm x 9 mm x 0.67 mmSupports Quectel EG915U-EU / EG915U-LA / EG915Q-NA (IoT / M2M -LTE Cat 1 module)LTE Radio: Refer to theLTE Radio Specificationssection for detailed information. |
| Power Supply | 9\~36 VDCCompatible with RAK Solar Battery Kit |
| Antenna | LoRa / LTE / Wi-Fi / GPS: Internal antenna |
| Antenna | LoRa |
| Antenna | Frequency Range: 863 MHz\~928 MHzPeak Gain: 2.5 dBiVSWR: ≤ 1.5Efficiency: >85%Polarization: Vertical |
| Antenna | LTE |
| Antenna | Frequency Range: 700 MHz\~960 MHz/1710 MHz\~21700 MHzPeak Gain: 3 dBiVSWR: ≤ 3Efficiency: >60%Polarization: Vertical |
| Antenna | Wi-Fi |
| Antenna | Frequency Range: 2400 MHz\~2500 MHzPeak Gain: 2 dBiVSWR: ≤ 2.5Efficiency: >75%Polarization: Vertical |
| Antenna | GPS |
| Antenna | Frequency Range: 1575 MHz\~1602 MHzPeak Gain: 28 dBiVSWR: <2Polarization: RHCP |
| Ingress Protection | IP67 |
| Weight | 0.66 kg |
| Dimension | 180 mm x 130 mm x 60 mm |
| Enclosure Material | UV stabilized ABS |
| Operating Temperature | ﹣30˚ C to ﹢55˚ C |
| Storage Temperature | ﹣40˚ C to ﹢85˚ C |
| Operating Humidity | 0\~95% RH non-condensing |
| Storage Humidity | 0\~95% RH non-condensing |
| Installation Method | Pole mounting (other options available per request) |

### Hardware

This section provides an overview of the hardware specifications for the RAK7267 gateway, including its interfaces, core functions, and key board parameters.

#### Interfaces

> **Image:** RAK7267 Interfaces

##### Interface Description

| Interfaces     | Description           | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **DC 9-36 V**  | Power Input           | Provides power supply for the gateway.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Console**    | Type-C USB            | Used for debugging.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Reset**      | Reset Key             | **Short press**: Reboot the gateway. 
**Long press** (5 sec and above): Restore factory settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **NanoSIM**    | NanoSIM Card Slot     | Slot for a NanoSIM card, enabling cellular connectivity.
<div style={{ borderLeft: '6px solid #f4b400', backgroundColor: '#fff8e1', padding: '12px', borderRadius: '6px', color: '#5f370e', fontFamily: 'sans-serif' }}><strong style={{ display: 'inline-flex', alignItems: 'center', fontSize: '16px' }}>⚠️ WARNING</strong>
<span style={{ display: 'block', marginTop: '4px' }}> The SIM card slot of the cellular versions is not hot-swappable. Make sure the gateway is switched off before inserting or ejecting the SIM card.</span></div>                                                                                                |
| **TF Card**    | SD Card Slot          | A 16 GB SD card is pre-installed in the gateway for data logging, system configurations, and other use cases that require local storage.
<div style={{ borderLeft: '6px solid #f4b400', backgroundColor: '#fff8e1', padding: '12px', borderRadius: '6px', color: '#5f370e', fontFamily: 'sans-serif' }}><strong style={{ display: 'inline-flex', alignItems: 'center', fontSize: '16px' }}>⚠️ WARNING</strong> 
 <span style={{ display: 'block', marginTop: '4px' }}>**Do not** eject the SD card located in the SD card slot during installation, as it stores logs and data essential for the device's performance. </span></div> |
| **Ground Pad** | Grounding Terminal    | Provides an earth grounding point for surge protection and EMI shielding. It is recommended to connect this to a reliable ground during installation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **LEDs**       | Status Indicator LEDs | PWR
LoRa
WLAN
LTE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

##### LED Indicator Details

The status of the LEDs is described below. Refer to the LED printing on the main board.

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
| WLAN | Slow Flash (1 Hz) | Disconnected from Wi-Fi network |
| WLAN | On | Connected to Wi-Fi network |
| WLAN | Flashing | Data transmitting or receiving |
| LTE | Slow Flash 1(1800 ms bright / 200 ms dark) | Searching for network (unregistered) |
| LTE | Slow Flash 2(200 ms bright / 1800 ms dark) | Idle (registered to network) |
| LTE | Quick Flash(125 ms bright / 125 ms dark) | Data transmitting or receiving |

#### RF Specifications

##### LoRa Radio Specifications

| Parameter | Specifications |
| --- | --- |
| Operating Frequency | EU868IN865RU864US915AU915KR920AS923-1/2/3/4 |
| Transmit Power | 27 dBm (Max) |
| Receiver Sensitivity | -140 dBm (Min) |

##### Wi-Fi Radio Specifications

| Parameter | Specifications |
| --- | --- |
| Wireless Standard | IEEE 802.11 b / g / n |
| Frequency | ISM band: 2.412\~2.472 GHz |
| Channels | 1-13 |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | **802.11b** |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 19 dBm @1 Mbps |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 19 dBm @11 Mbps |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | **802.11g** |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 18 dBm @6 Mbps |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 16 dBm @54 Mbps |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | **802.11n (2.4 GHz)** |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 18 dBm @MCS0 (HT20) |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 16 dBm @MCS7 (HT20) |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 17 dBm @MCS0 (HT40) |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 15 dBm @MCS7 (HT40) |
| Receiver Sensitivity (Typical) | **802.11b** |
| Receiver Sensitivity (Typical) | ﹣95 dBm @1 Mbps |
| Receiver Sensitivity (Typical) | ﹣88 dBm @11 Mbps |
| Receiver Sensitivity (Typical) | **802.11g** |
| Receiver Sensitivity (Typical) | ﹣90 dBm @6 Mbps |
| Receiver Sensitivity (Typical) | ﹣75 dBm @54 Mbps |
| Receiver Sensitivity (Typical) | **802.11n (2.4 GHz)** |
| Receiver Sensitivity (Typical) | ﹣89 dBm @MCS0 (HT20) |
| Receiver Sensitivity (Typical) | ﹣72 dBm @MCS7 (HT20) |
| Receiver Sensitivity (Typical) | ﹣86 dBm @MCS0 (HT40) |
| Receiver Sensitivity (Typical) | ﹣68 dBm @MCS7 (HT40) |

##### LTE Radio Specifications

| Module / Region | Supported Bands |
| --- | --- |
| EG915U-EU for EMEA/Brazil/Australia/New Zealand Region | LTE FDD: B1 / B3 / B5 / B7 / B8 / B20 / B28 |
| EG915U-EU for EMEA/Brazil/Australia/New Zealand Region | GSM: B2 / B3 / B5 / B8 |
| EG915U-LA for Latin America Region | LTE FDD: B2 / B3 / B4 / B5 / B7 / B8 / B28 / B66 |
| EG915U-LA for Latin America Region | GSM: B2 / B3 / B5 / B8 |
| EG915Q-NA for North America Region | LTE FDD: B2 / B4 / B5 / B12 / B13 / B66 / B71 |

#### Electrical Characteristics

The RAK7267 WisGate Soho Pro supports multiple power input methods. Choose the option that best fits your deployment scenario.

- **DC Adapter + Cable**

  Recommended for indoor use. Use the provided power adapter and cable to supply power to the gateway.

- **Custom DC Power (9~36 V<sub>DC</sub>)**
 
  Suitable for industrial or flexible power environments. Use the DC cable to connect an external DC power source within the 9~36 V<sub>DC</sub> range.

- **RAK9155 Battery Plus System**
 
  Recommended for outdoor installations. Use the dedicated power cable designed for RAK9155 Battery Plus to connect and supply power to the gateway.

### Software

| LoRa | Network | Management |
| --- | --- | --- |
| Gateway OTA management | Wi-Fi Client mode | WisDM |
| LoRa package forward (packet forwarder, Basics Station) | LTE APN Setup | SSH2, NTP |
| Frequency Band Setup | Support 802.1q | Firmware update |
| Country Code setup | Uplink backup | LoRa Packet Forwarder |
| Server Address and Port Setup | Firewall | Built-in Network Server |
| TX Power Setup | DHCP Server/Client | MQTT Bridge |
| Data logger | Wi-Fi AP mode | OpenVPN, Ping Watch Dog |
| Location setup |  | WEB UI |
| Statistic |  |  |
| Supports class A, B, C |  |  |
| Server address and Port setup |  |  |

### Firmware

|          Model           |                                                         Source                                                          |
|:------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| RAK7267 WisGate Soho Pro | <a href="https://downloads.rakwireless.com/LoRa/WisGateOS2/WisGateOS2_Latest_Firmware.zip" target="_blank">Download</a> |

## Models/Bundles

| Part Number | 8 Channel SX1303 | Cat1 Cellular | GPS | Wi-Fi |
| --- | --- | --- | --- | --- |
| RAK7267-XYZ | √ | √ | √ | √ |

## Certification

### Certifications
- **ANATEL:** https://downloads.rakwireless.com/LoRa/RAK7267/Certification/RAK7267_ANATEL_Certification.pdf
- **CE:** https://downloads.rakwireless.com/LoRa/RAK7267/Certification/RAK7267_CE_Certification.pdf
- **FCC:** https://downloads.rakwireless.com/LoRa/RAK7267/Certification/RAK7267_FCC_Certification.pdf
- **ISED:** https://downloads.rakwireless.com/LoRa/RAK7267/Certification/RAK7267_ISED_Certification.pdf
- **RCM:** https://downloads.rakwireless.com/LoRa/RAK7267/Certification/RAK7267_RCM_Certification.pdf
- **ROHS:** https://downloads.rakwireless.com/LoRa/RAK7267/Certification/RAK7267_ROHS_Report.pdf
- **RSM:** https://downloads.rakwireless.com/LoRa/RAK7267/Certification/RAK7267_RSM_Certification.pdf
- **RED:** https://downloads.rakwireless.com/LoRa/WisGate/Certification/WisGate_RED_Verification.pdf
- **UKCA:** https://downloads.rakwireless.com/LoRa/RAK7267/Certification/RAK7267_UKCA_Certification.pdf

