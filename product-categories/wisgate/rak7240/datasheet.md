---
title: RAK7240 WisGate Edge Prime Datasheet
description: Provides comprehensive information about your RAK7240 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
keywords:
- datasheet
- wisgate
- RAK7240
image: https://images.docs.rakwireless.com/wisgate/rak7240/quickstart/RAK7240.png
sidebar_label: Datasheet
---

    

# RAK7240 WisGate Edge Prime Datasheet

## Overview

### Description

The **RAK7240 WisGate Edge Prime** is an ideal product for large scale LPWAN deployment where cost is essential, however, there is no compromises to be made on quality. Its wide range of customization options allows for flexibility when deploying a solution. With its industrial-grade components and high class of ingress protection, it achieves a high standard of reliability.

The Gateway provides for a solid out of the box experience where quick deployment is required. Additionally, since its software and User Interface sit on top of OpenWRT, it is perfect for the development of custom applications (**via the open SDK**).

Thus, the **RAK7240 WisGate Edge Prime**, is suited for any use case scenario, be it rapid deployment or customization with regards to User Interface and functionality.

### Features

#### Hardware

- **IP65** industrial-grade enclosure with cable glands
- **PoE** + Surge Protection
- Dual LoRa Concentrators for up to **16 channels**
- Backhaul: **Wi-Fi**, **LTE**, and **Ethernet**
- **GPS**
- SD Card slot

#### Software

- Built-in LoRa Server
- OpenVPN
- Software and UI sit on top of **OpenWRT**
- LoRaWAN 1.0.3
- **LoRa Frame filtering** (node whitelisting)
- **MQTT v3.1** Bridging with **TLS** encryption
- **Buffering of LoRa frames** in case of NS outage (no data loss)

## Specifications

### Overview

The overview presents the RAK7240 circuit board and its block diagram that shows how the module's components work.

#### Circuit Board (Board Overview)

> **Image:** RAK7240 WisGate Edge Prime Circuit Board

#### Block Diagram

> **Image:** RAK7240 WisGate Edge Prime Block Diagram

### Hardware

The hardware specification is categorized into four parts. It discusses the interfaces and the parameters of the RAK7240. It also covers the LoRa and Wi-Fi specifications of the board.

#### Interfaces (Hardware Interfaces)

The hardware interfaces of **RAK7240 WisGate Edge Prime** include five (5) antenna ports (LoRa, LTE-DIV/LoRa2, LTE-MAIN, WiFi, and GPS), six (6) status indicator LEDs, TF Card and nano-SIM sockets, a console port, an Ethernet Port (PoE), and a ground pad, as shown in the following figure:

> **Image:** RAK7240 WisGate Edge Prime Hardware Interfaces

##### LED Indicators

The status of the LEDs is described as below. Please refer to the printing of the LEDs on the mainboard.

| **LEDs**                          | **Status Indication Description**                                                                                                                                                                                                  |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PWR**                           | Power Indicator, LED is **ON** when the device is powered                                                                                                                                                                          |
| **ETH**                           | • **ON** – link is up 
• **OFF** – link is down 
• **Flashing** – Data is being transferred                                                                                                                                  |
| **LoRa**®                         | • **ON** - LoRa module 1 status is up 
• **OFF** – LoRa module 1 status is down 
• **Flashing** – LoRa module 1 data is being transferred                                                                                 |
| **ACT** _(LTE)_                   | • **Slow Flashing** (_200ms Bright/1800ms Dark)_ - searching for network 
• **Slow Flashing** (200ms Dark/1800ms Bright) - idle status (online) 
• **Fast Flashing** - Data is being transferred                             |
| **STAT** 
_(16 channels only)_ | • **ON** - LoRa module 2 status is up 
• **OFF** – LoRa module 2 status is down 
• **Flashing** – LoRa module 2 data is being transferred                                                                                 |
| **WLAN**                          | **AP Mode** 
• **ON** - WLAN status is up 
• **Flashing** - Data is being transferred 
 **STA Mode** 
• **Slow Flashing**(1Hz) - Disconnected 
• **ON** - Connected 
• **Flashing** - Data is being transferred |

#### Main Specifications

| Feature                   | Specifications                                                                                                                                                                                                                                                                     |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Computing**             | MT7628, DDR2RAM 128MB                                                                                                                                                                                                                                                              |
| **Wi-Fi Feature**         | • **Frequency**: 2.400-2.4835GHz (802.11b/g/n)
• **RX Sensitivity**: -95dBm (Min)
• **TX Power**: 20dBm (Max)
• **Operation Channels**: 2.4GHz: 1-13                                                                                                                      |
| **LoRa Feature**          | • **Card**: SX1301 Mini PCIe card (connects maximum of two),
• **Channels**: 8 Channels (Optional: 16 channels)
• **RX Sensitivity**: -139dBm (Min)
• **TX Power**: 27dBm (Max)
• **Frequency**: EU433 / CN470 / RU864 / IN865 / EU868 / US915 / AU915 / KR920 / AS923 |
| **Cellular Feature**      | **Variant for Europe** 
• LTE FDD: B1/B3/B7/B8/B20/B28A 
• WCDMA: B1/B8 
• GSM: 900/1800MHz  
 **Variant for North America** 
• LTE FDD: B2/B4/B5/B12/B13 
• WCDMA: B2/B4/B5                                                                                   |
| **Power Supply**          | PoE (IEEE 802.3af) - 42~57V DC                                                                                                                                                                                                                                                     |
| **Power Consumption**     | 12 W (typical)                                                                                                                                                                                                                                                                     |
| **Ethernet** (ETH)        | RJ45 (10/100M)                                                                                                                                                                                                                                                                     |
| **Console**               | RJ45 (RS232)                                                                                                                                                                                                                                                                       |
| **Antenna**               | 5 N-Type connectors                                                                                                                                                                                                                                                                |
| **LEDs**                  | LoRa LED (1), Cellular (2), POWER (1), ETH (1), WI-FI (1)                                                                                                                                                                                                                          |
| **Ingress Protection**    | IP65                                                                                                                                                                                                                                                                               |
| **Enclosure Material**    | Aluminum                                                                                                                                                                                                                                                                           |
| **Weight**                | 1.3 kg                                                                                                                                                                                                                                                                             |
| **Dimension**             | 224 mm x 121 mm x 42 mm                                                                                                                                                                                                                                                            |
| **Operating Temperature** | -30˚C to +55 ˚C                                                                                                                                                                                                                                                                    |
| **Storage Temperature**   | -40˚C to +85 ˚C                                                                                                                                                                                                                                                                    |
| **Operating Humidity**    | 0% to 95% (non-condensing)                                                                                                                                                                                                                                                         |
| **Storage Humidity**      | 0% to 95% (non-condensing)                                                                                                                                                                                                                                                         |
| **Installation Method**   | Pole or Wall mounting                                                                                                                                                                                                                                                              |

#### RF Specifications

##### LoRa Radio Specifications

| Feature                  | Specifications                                                        |
| ------------------------ | --------------------------------------------------------------------- |
| **Operating Frequency**  | EU433 / CN470 / RU864 / IN865 / RU864 / US915 / AU915 / KR920 / AS923 |
| **Transmit Power**       | 27dBm (Max)                                                           |
| **Receiver Sensitivity** | -139dBm (Min)                                                         |

##### Wi-Fi Radio Specifications

| Feature                                                                                           | Specifications                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Wireless Standard**                                                                             | IEEE 802.11b/g/n                                                                                                                                                                                                                              |
| **Operating Frequency**                                                                           | ISM band: 2.412~2.472(GHz)                                                                                                                                                                                                                    |
| **Operation Channels**                                                                            | 2.4GHz: 1-13                                                                                                                                                                                                                                  |
| **Transmit Power**
(The max. power may be different  
depending on local regulations) -per chain | **802.11b** 
• 1Mbps: 19dBm 
• 11Mbps: 19dBm  
 **802.11g** 
• 6Mbps: 18dBm 
• 54Mbps: 16dBm  
 **802.11n (2.4G)** 
• MCS0 (HT20): 18dBm 
• MCS7 (HT20): 16dBm 
• MCS0 (HT40): 17dBm 
• MCS7 (HT40): 15dBm  |
| **Receiver
Sensitivity** 
(Typical)                                                         | **802.11b** 
• 1Mbps: 95dBm 
• 11Mbps: 88dBm  
 **802.11g** 
• 6 Mbps: 90dBm 
• 54Mbps: 75dBm  
  **802.11n (2.4G)** 
• MCS0 (HT20): 89dBm
• MCS7 (HT20): 72dBm 
• MCS0 (HT40): 86dBm 
• MCS7 (HT40): 68dBm |

### Firmware

| Model                      | Firmware Version | Source                                                                                          |
| -------------------------- | ---------------- | ----------------------------------------------------------------------------------------------- |
| RAK7240 WisGate Edge Prime | WisGateOS V1.3.9 | [Download](https://downloads.rakwireless.com/LoRa/WisGateOS/WisGateOS_Latest_Firmware.zip)      |

### Software

RAK7240 supports different software features such as LoRa, Network, and Management.

#### Supported Software

| LoRa                          | Network                        | Management                                   |
| ----------------------------- | ------------------------------ | -------------------------------------------- |
| Supports class A, B, C        | CPE and AP mode                | WEB Management                               |
| Supports LoRaWAN protocol     | Bridge, WISP and router module | Supports SSH2                                |
| Country code setup            | Supports 802.1q backup         | Firmware update                              |
| TX power up setup             | DHCP Server/Client             | NTP                                          |
| Datalogger & statistic        | Router module NAT              | Supports configure the LoRa Packet Forwarder |
| Location setup                | Firewall                       | Build-in LoRa Server                         |
| Server address and port setup |                                | Supports OpenVPN                             |
|                               |                                | Supports Ping Watch Dog                      |
|                               |                                | Supports MQTT Bridge                         |

## Models / Bundles

| Part Number    | Package Content                                                                                                                                          |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RAK7240-0X-14X | 1x 8 channel device with LTE module, 1x LoRa Antenna, 2x LTE Antenna, 1x GPS Antenna, 1x 2.4G WiFi Antenna, 1x PoE Injector, 1x Mounting Kit, 1x Manual  |
| RAK7240-1X-14X | 1x 16 channel device with LTE module, 2x LoRa Antenna, 1x LTE Antenna, 1x GPS Antenna, 1x 2.4G WiFi Antenna, 1x PoE Injector, 1x Mounting Kit, 1x Manual |
| RAK7240-0X     | 1x 8 channel device, 1x LoRa Antenna, 1x GPS Antenna, 1x 2.4G WiFi Antenna, 1x PoE Injector, 1x Mounting Kit, 1x Manual                                  |
| RAK7240-1X     | 1x 16 channel device, 2x LoRa Antenna, 1x GPS Antenna, 1x 2.4G WiFi Antenna, 1x PoE Injector, 1x Mounting Kit, 1x Manual                                 |

<!-- ## Certification -->

