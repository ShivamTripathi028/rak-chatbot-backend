---
title: RAK7289 WisGate Edge Pro Datasheet
description: Read more the comprehensive information about RAK7289, including technical specifications, characteristics, requirements, and a discussion of the device components.
keywords:
    - RAK7289 Datasheet
    - RAK7289 guides
    - WisGate Edge Pro Datasheet
image: https://images.docs.rakwireless.com/wisgate/rak7289/RAK7289.png
sidebar_label: Datasheet
---    

# RAK7289 WisGate Edge Pro Datasheet

## Overview

### Description

**RAK7289 WisGate Edge Pro** is an ideal product for IoT commercial deployment. With its industrial-grade components, it achieves a high standard of reliability.

Supports up to 16 LoRa channels, multi-backhaul with Ethernet, Wi-Fi, and Cellular connectivity. Optionally there is a dedicated port for different power options, solar panels, and batteries. With its new enclosure design, it allows the LTE, Wi-Fi, and GPS antennas to be inside the enclosure.

The gateway provides a solid out-of-the-box experience for quick deployment. Additionally, since its software and UI sits on top of OpenWRT it is perfect for the development of custom applications (via the open SDK).

Thus, the RAK7289 is suited for any use case scenario, be it rapid deployment or customization with regards to UI and functionality.

### Product Features

#### Hardware

- **IP67/NEMA-6** industrial-grade enclosure with cable glands
- **PoE (802.3af)** + Surge Protection
- Dual LoRa Concentrators for up to **16 channels**
- **Backhaul:** Wi-Fi, LTE, and Ethernet
- GPS
- Supports DC 12 V or Solar power supply with Electricity monitoring (Solar Kit optional)
- Internal antenna for Wi-Fi, GPS, and LTE, External antenna for LoRa
- Dying-Gasp (optional)

#### Software

- Built-in Network Server
- OpenVPN
- Software and UI sit on top of **OpenWRT**
- LoRaWAN 1.0.3
- **LoRa Frame filtering** (node whitelisting)
- **MQTT v3.1** Bridging with **TLS** encryption
- **Buffering of LoRa frames in Packet Forwarder mode** in case of NS outage (no data loss)
- **Full duplex (optional)**
- **Listen Before Talk (optional)**
- **Fine timestamping (optional)**

## Specifications

### Overview

The overview presents the block diagram for the RAK7289 that shows the internal architecture of the board.

#### Block Diagram

> **Image:** RAK7289 WisGate Edge Pro Block Diagram

#### Main Specifications

| Feature | Specifications |
| --- | --- |
| Computing | MT7628, DDR2 RAM 128 MB |
| Wi-Fi feature | Frequency: 2.4 GHz (802.11 b/g/b/) |
| Wi-Fi feature | 2x2 MIMO |
| Wi-Fi feature | RX Sensitivity: -95 dBm (Min) |
| Wi-Fi feature | TX Power: 20 dBm (Max) |
| Wi-Fi feature | Operation channels: 2.4 GHz: 1-13 |
| LoRa feature | SX1303 mPCIe card (connects maximum of two) |
| LoRa feature | 8 Channels (16 channels optional) |
| LoRa feature | RX Sensitivity: -139 dBm (Min) |
| LoRa feature | TX Power: 27 dBm (Max) |
| LoRa feature | Listen Before Talk |
| Frequency | EU433/CN470/EU868/US915/AS923/AU915/IN865/KR920 |
| Cellular feature | Supports Quectel EG95-E/EG95-NA (IoT/M2M -optimized LTE Cat 4 Module) |
| Cellular feature | EG95-E for EMEA Region |
| Cellular feature | - LTE FDD: B1/B3/B7/B8/B20/B28A |
| Cellular feature | - WCDMA: B1/B8 |
| Cellular feature | - GSM/EDGE: B3/B8 |
| Cellular feature | EG95-NA for North America Region |
| Cellular feature | - LTE FDD: B2/B4/B5/B12/B13 |
| Cellular feature | - WCDMA: B2/B4/B5 |
| Power supply | PoE (IEEE 802.3 af), 37~57 VDC |
| ETH | RJ45 (10/100 Mbps) |
| Antenna | LoRa: 1 or 2 N-Type connectors |
| Antenna | LTE: Internal antenna |
| Antenna | Wi-Fi: Internal antenna |
| Ingress protection | IP67 |
| Enclosure material | Aluminum and plastic |
| Operating temperature | -30˚ C to +55˚ C |
| Operating humidity | 0-95% RH non-condensing |
| Installation method | Pole or wall mounting |

### Hardware

The hardware specification covers the interfacing of the RAK7289 and its corresponding functionalities. It also presents the parameters and the standard values of the board.

#### RF Specifications

##### Wi-Fi Radio Specifications

| Feature | Specifications |
| --- | --- |
| Wireless Standard | IEEE 802.11 b/g/n |
| Operating Frequency | ISM band: 2.412~2.472 (GHz) |
| Operation Channels | 2.4 GHz: 1-13 |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 802.11b |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 19 dBm @1 Mbps |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 19 dBm @11 Mbps |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 802.11g |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 18 dBm @6 Mbps |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 16 dBm @54 Mbps |
| Transmit Power (The max power maybe different depending on local regulations) - per chain | 802.11n (2.4G) |
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
| Receiver Sensitivity (Typical) | 802.11n (2.4G) |
| Receiver Sensitivity (Typical) | -89 dBm @MCS0 (HT20) |
| Receiver Sensitivity (Typical) | -72 dBm @MCS7 (HT20) |
| Receiver Sensitivity (Typical) | -86 dBm @MCS0 (HT40) |
| Receiver Sensitivity (Typical) | -68 dBm @MCS7 (HT40) |

##### LoRa Radio Specifications

| Feature              | Specifications                                  |
| -------------------- | ----------------------------------------------- |
| Operating Frequency  | EU433/CN470/EU868/US915/AS923/AU915/IN865/KR920 |
| Transmit Power       | 27 dBm (Max)                                    |
| Receiver Sensitivity | -139 dBm (Min)                                  |

#### Interfaces

> **Image:** RAK7289 WisGate Edge Pro Interfaces

- The function of the Reset key is as follows:
  - **Short press:** Restart the gateway.
  - **Long press** (5s and above): Restore factory settings.

- LEDs status description:

| LEDs | Status Indication Description |
| --- | --- |
| LED 1 (PWR) | Power indicator - The LED is on when device power is on |
| LED 2 (ETH) | ON - Linkup |
| LED 2 (ETH) | OFF - Linkdown |
| LED 2 (ETH) | Flicker - Data transmitting and receiving |
| LED 3 (LoRa 1) | ON - LoRa 1 is working |
| LED 3 (LoRa 1) | OFF - LoRa 1 is not working |
| LED 3 (LoRa 1) | Flicker - Indicate LoRa 1 Packet receiving and sending |
| LED 4 (WLAN) | AP Mode: |
| LED 4 (WLAN) | -ON - The AP is up |
| LED 4 (WLAN) | -Flicker - Data receiving and sending |
| LED 4 (WLAN) | STA Mode: |
| LED 4 (WLAN) | -Slow flicker (1 Hz) - Disconnected |
| LED 4 (WLAN) | -ON - Connected |
| LED 4 (WLAN) | -Flicker - Data receiving and sending |
| LED 5 (LTE) | Slow Flicker (1800 ms High / 200 ms Low) - Network searching |
| LED 5 (LTE) | Slow flicker (200 ms High / 1800 ms Low) - Idle |
| LED 5 (LTE) | Fast flicker (125 ms High / 125 ms Low) - Ongoing data transfer |
| LED 5 (LTE) | ON - Voice is working |
| LED 6 (LoRa 2 for 16 channel) | ON - LoRa 2 is working |
| LED 6 (LoRa 2 for 16 channel) | OFF - LoRa 2 is not working |
| LED 6 (LoRa 2 for 16 channel) | Flicker - Indicate LoRa 2 Packet receiving and sending |

### Firmware

The firmware sits on OpenWRT, which makes it possible to customize it. There is a Web UI for easy configuration and management of the device, as well as the possibility for SSH2 management.

| Model                       | Firmware Version | Source                                                                                     |
| --------------------------- | ---------------- | ------------------------------------------------------------------------------------------ |
| RAK7289 WisGate Edge Pro    | WisGateOS V1.3.9 | [Download](https://downloads.rakwireless.com/LoRa/WisGateOS/WisGateOS_Latest_Firmware.zip) |

### Software

#### Software Features

| LoRaWAN                       | Network            | Managеment              |
| ----------------------------- | ------------------ | ----------------------- |
| Supports class A, B, C        | Wi-Fi AP mode      | WEB UI                  |
| LoRa package forward          | Wi-Fi Client mode  | SSH2, NTP               |
| Frequency band setup          | LTE APN setup      | Firmware update         |
| TX power setup                | Uplink backup      | LoRa packet forwarder   |
| Data logger                   | Support 802.1q     | Built-In Network Server |
| Statistic                     | DHCP Server/Client | OpenVPN, Ping Watch Dog |
| Location setup                | Firewall           | MQTT Bridge             |
| Server address and port setup |                    |                         |

## Models/Bundles

| Part Number | 8 Channel SX1303 | 16 Channel SX1303 | Cat4 Cellular | GPS  | Wi-Fi | Dying gasp |
| ----------- | :--------------: | :---------------: | :-----------: | :--: | :---: | :--------: |
| RAK7289-XYZ |        √         |                   |       √       |  √   |   √   |            |
| RAK7289-XYZ |                  |         √         |       √       |  √   |   √   |            |
| RAK7289-XYZ |        √         |                   |       √       |  √   |   √   |     √      |
| RAK7289-XYZ |                  |         √         |       √       |  √   |   √   |     √      |
| RAK7289-XYZ |        √         |                   |               |  √   |   √   |            |
| RAK7289-XYZ |                  |         √         |               |  √   |   √   |            |
| RAK7289-XYZ |        √         |                   |               |  √   |   √   |     √      |
| RAK7289-XYZ |                  |         √         |               |  √   |   √   |     √      |

<!-- ## Certification -->