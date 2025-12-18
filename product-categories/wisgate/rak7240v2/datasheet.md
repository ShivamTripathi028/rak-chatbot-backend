---
slug: /product-categories/wisgate/rak7240v2/datasheet/
title: RAK7240V2 / RAK7240CV2 WisGate Edge Prime Datasheet
description: Learn the comprehensive datasheet for RAK7240V2 WisGate Edge Prime, detailing its IP65-rated enclosure, 8 or 16-channel LoRaWAN support, multi-backhaul options, and advanced features for large-scale LPWAN deployments.
image: "https://images.docs.rakwireless.com/wisgate/rak7240-v2/rak7240v2.png"
keywords:
    - RAK7240V2
    - WisGate Edge Prime
    - LoRaWAN gateway
    - 8 channel gateway
    - 16 channel gateway
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK7240V2/RAK7240CV2 WisGate Edge Prime Datasheet

## Overview

### Description

The **RAK7240V2 WisGate Edge Prime** is ideal for large-scale LPWAN deployments where cost is essential, without compromising quality. The gateway is available in 8 or 16-channel versions to help you utilize the maximum number of available LoRaWAN channels in your region. It supports multi-backhaul with Ethernet, Wi-Fi, and cellular connectivity.

This gateway operates on <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#overview" target="_blank">WisGateOS 2</a>, a secure and flexible operating system based on the latest OpenWrt kernel. It supports extension modules for enhanced customization, and offers centralized remote management and configuration via <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/" target="_blank">WisDM</a>—making it an ideal choice for managing large networks of gateways.

Its wide range of customization options allows for flexibility when deploying a solution. It is suited for any use-case scenario, whether it's rapid deployment or customization regarding UI and functionality. The flat surface of the full-metal enclosure allows your logo to be added for brand customization and recognition.

### Features

#### Hardware

- IP65 industrial-grade enclosure with cable glands
- PoE (802.3af) + Surge Protection
- Up to two (2) LoRa concentrators for 8 or 16-channel options
- Multi-backhaul options: Ethernet, Wi-Fi, and LTE (*LTE available on 8-channel RAK7240CV2 only*)
- GPS
- Power variants:
  + PoE-only version
  + DC-input version (supports 9\~24&nbsp;V<sub>DC</sub>, RAK Battery Plus)
- External antennas for Wi-Fi, GPS, LTE (optional, available with RAK7240CV2), and LoRa

#### Software

- <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/" target="_blank">WisGateOS 2</a>: The OS for configuring and managing RAK gateways
- **WisGateOS 2 Extensions**: Adds support for features such as OpenVPN, WireGuard VPN, and more. Use the appropriate installation guide based on your WisGateOS 2 version:
    - <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/" target="_blank">For WisGateOS 2 version 2.2.x or later</a>
    - <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/" target="_blank">For WisGateOS 2 versions 2.0.x and 2.1.x</a>
- Remote management with <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/" target="_blank">WisDM</a> Fleet Management
- Built-in Network Server (LoRaWAN support v1.0.3)
- LoRaWAN Stack support with Semtech SX1303
- LoRa Frame filtering (node whitelisting in Packet Forwarder mode)
- MQTT v3.1 bridging with TLS encryption
- Fine timestamping (optional)
- Buffering of LoRa frames in Packet Forwarder mode in case of NS outage (no data loss)

## Specifications

### Overview

#### Block Diagram

The block diagram of RAK7240V2/RAK7240CV2 shows the internal architecture of the hardware.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7240-v2/datasheet/1.rak7240v2-block-diagram.png"
  width="100%"
  caption="RAK7240V2 Block Diagram"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7240-v2/datasheet/2.rak7240cv2-block-diagram.png"
  width="100%"
  caption="RAK7240CV2 Block Diagram"
/>

### Main Specifications

| Feature                     | Specifications                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Computing                   | MT7628, DDR2RAM 128&nbsp;MB                                                                                                                                                                                                                                                                                                                                                         |
| LoRa Feature                | SX1303 mPCIe card (connects a maximum of two)<br/>8 Channels (16 channels optional)<br/>Frequency:<ul><li>EU868</li><li>IN865</li><li>RU864</li><li>US915</li><li>AU915</li><li>KR920</li><li>AS923-1/2/3/4</li><li>EU433</li><li>CN470</li></ul><br />LoRa Radio: Refer to the <a href="#lora-radio-specifications">LoRa Radio Specifications</a> section for detailed information |
| Wi-Fi Feature               | Frequency: 2.400-2.4835&nbsp;GHz (802.11b/g/n)<br/>Operation Channels: 1-13<br />Wi-Fi Radio: Refer to the <a href="#wifi-radio-specifications">Wi-Fi Radio Specifications</a> section for detailed information                                                                                                                                                                     |
| Cellular Feature (optional) | **Nano SIM Card:** 12&nbsp;mm x 9&nbsp;mm x 0.67&nbsp;mm<br/>Supports Quectel EG95-E / EG95-NA (IoT / M2M -optimized LTE Cat 4 Module)<br/>LTE Radio: Refer to the <a href="#lte-radio-specifications">LTE Radio Specifications</a> section for detailed information<br />Available only on RAK7240CV2 8-channel variant<br />                                                      |
| Power Supply                | PoE (IEEE 802.3af) , 42\~57&nbsp;V<sub>DC</sub><br/>9\~24&nbsp;V<sub>DC</sub> from dedicated DC port (available on DC-input models only)<br/>Compatible with RAK Solar Battery Kit (available on DC-input models only)                                                                                                                                                              |
| Power Consumption           | 12&nbsp;W (typical)                                                                                                                                                                                                                                                                                                                                                                 |
| Antenna                     | External antennas for LoRa®, Wi-Fi, GPS, and LTE                                                                                                                                                                                                                                                                                                                                    |
| Ingress Protection          | IP65                                                                                                                                                                                                                                                                                                                                                                                |
| Enclosure Material          | Aluminum                                                                                                                                                                                                                                                                                                                                                                            |
| Weight                      | 1.3&nbsp;kg                                                                                                                                                                                                                                                                                                                                                                         |
| Dimension                   | 224&nbsp;mm x 121&nbsp;mm x 42&nbsp;mm Gateway only (no antenna, no bracket)                                                                                                                                                                                                                                                                                                        |
| Operating Temperature       | -30˚&nbsp;C to ﹢55˚&nbsp;C                                                                                                                                                                                                                                                                                                                                                          |
| Storage Temperature         | -40˚&nbsp;C to ﹢85˚&nbsp;C                                                                                                                                                                                                                                                                                                                                                          |
| Operating Humidity          | 0% to 95% (non-condensing)                                                                                                                                                                                                                                                                                                                                                          |
| Storage Humidity            | 0% to 95% (non-condensing)                                                                                                                                                                                                                                                                                                                                                          |
| Installation Method         | Pole or wall mounting                                                                                                                                                                                                                                                                                                                                                               |

### Hardware

The hardware specification is categorized into four sections. It discusses the interfaces and parameters of the RAK7240V2/RAK7240CV2.

#### Interfaces

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7240-v2/datasheet/3.interface.png"
  width="100%"
  caption="RAK7240V2/RAK7240CV2 Interfaces"
/>

##### Interface Description

| **Interface**         | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Wi-Fi                 | External Wi-Fi antenna connector                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ETH (PoE)             | 10/100&nbsp;Mbps Ethernet port with IEEE 802.3af PoE input support                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Console               | USB Type-C port for debugging and maintenance   <br />Reset:  <br /><ul><li>**Short press**: Reboot the gateway</li><li>**Long press (5 sec and above)**: Restores factory settings  </li></ul>                                                                                                                                                                                                                                                                                                                                                                                              |
| TF Card               | Pre-installed 16 GB microSD card for log storage and uplink frame buffering <br /> <div style={{ borderLeft: '6px solid #f4b400', backgroundColor: '#fff8e1', padding: '12px', borderRadius: '6px', color: '#5f370e', fontFamily: 'sans-serif' }}><strong style={{ display: 'inline-flex', alignItems: 'center', fontSize: '16px' }}>⚠️ WARNING</strong><br/><span style={{ display: 'block', marginTop: '4px' }}><strong>Do not</strong> eject the SD card located in the SD card slot during installation, as it stores logs and data essential for the device's performance.</span></div> |
| NanoSIM               | Available only on LTE-enabled models (RAK7240CV2); slot is present on all models for hardware  compatibility                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| LED Indicators        | WLAN, STAT, ACT, LoRa, ETH, PWR indicators for device and module status                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| GPS                   | GPS antenna connector                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Ground Pad            | Grounding point for ESD and lightning protection                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DC Input *(Optional)* | 9\~24&nbsp;V<sub>DC</sub> power input  (only on DC-input models)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| LoRa                  | LoRa® antenna connector                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| LTE-DIV / LoRa2       | LTE diversity antenna or LoRa2 antenna connector *(used as LoRa2 on 16-channel)*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| LTE-MAIN              | LTE main antenna connector *(available only on RAK7240CV2 LTE models)*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

##### LED Indicators

The status of the LEDs is described below.

| LEDs                          | Status Indication Description                                                                                                                                                                                                                                                    |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PWR                           | ON: Gateway is powered on<br/>OFF: Gateway is powered on                                                                                                                                                                                                                         |
| ETH                           | ON: Link is up<br/>OFF: Link is down<br/>Flicker: Data transmitting or receiving                                                                                                                                                                                                 |
| LoRa                          | ON: LoRa1 module active<br/>OFF: LoRa1 module inactive<br/>Flicker: Indicate that LoRa1 packet transmitting or receiving                                                                                                                                                         |
| ACT (LTE)                     | Slow flicker (1800&nbsp;ms bright / 200&nbsp;ms dark): Searching for network<br/>Slow flicker (200&nbsp;ms bright / 1800&nbsp;ms dark): Idle status (online)<br/>Fast flicker: Data transmitting or receiving                                                                    |
| STAT<br/>_(16 channels only)_ | ON: LoRa2 module active<br/>OFF: LoRa2 module inactive<br/>Flashing: Data transmitting or receiving                                                                                                                                                                              |
| WLAN                          | **AP Mode**<ul><li>ON: AP is active</li><li>Flicker: Data transmitting or receiving</li></ul><br/>**STA Mode**<ul><li>Slow flicker (1&nbsp;Hz): Disconnected from Wi-Fi network</li><li>ON: Connected to Wi-Fi network</li><li>Flicker: Data transmitting or receiving</li></ul> |

#### RF Specifications

##### LoRa Radio Specifications

| Feature              | Specifications                                                                                                                                                                                             |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operating frequency  | <ul><li>EU868</li><li>IN865</li><li>RU864</li><li>US915</li><li>AU915</li><li>KR920</li><li>AS923-1/2/3/4</li><li>EU433</li><li>CN470</li></ul><br />*(Supported frequency depends on the model selected)* |
| Transmit power       | 27&nbsp;dBm (Max)                                                                                                                                                                                          |
| Receiver sensitivity | -139&nbsp;dBm (Min)                                                                                                                                                                                        |

##### Wi-Fi Radio Specifications

| Feature                                                                                    | Specifications                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Wireless Standard                                                                          | IEEE 802.11b/g/n                                                                                                                                                                                                                                                                                             |
| Operating frequency                                                                        | ISM band: 2.412~2.472 (GHz)                                                                                                                                                                                                                                                                                  |
| Operation channels                                                                         | 2.4&nbsp;GHz: 1-13                                                                                                                                                                                                                                                                                           |
| Transmit power: per chain (The max. power may be different depending on local regulations) | **802.11b**<br/> 1&nbsp;Mbps: 19&nbsp;dBm<br/> 11&nbsp;Mbps: 19&nbsp;dBm<br/>**802.11g**<br/> 6&nbsp;Mbps: 18&nbsp;dBm<br/> 54&nbsp;Mbps: 16&nbsp;dBm<br/> **802.11n (2.4&nbsp;GHz)**<br/> MCS0 (HT20): 18&nbsp;dBm<br/> MCS7 (HT20): 16&nbsp;dBm<br/> MCS0 (HT40): 17 dBm<br/> MCS7 (HT40): 15dBm           |
| Receiver sensitivity (Typical)                                                             | **802.11b**<br/> 1&nbsp;Mbps: 95&nbsp;dBm<br/> 11&nbsp;Mbps: 88&nbsp;dBm<br/>**802.11g**<br/> 6&nbsp;Mbps: 90&nbsp;dBm<br/> 54&nbsp;Mbps: 75&nbsp;dBm<br/>**802.11n (2.4&nbsp;GHz)**<br/> MCS0 (HT20): 89&nbsp;dBm<br/> MCS7 (HT20): 72&nbsp;dBm<br/> MCS0 (HT40): 86&nbsp;dBm<br/> MCS7 (HT40): 68&nbsp;dBm |

##### LTE Radio Specifications

| Feature                          | Specifications                                                                            |
|----------------------------------|-------------------------------------------------------------------------------------------|
| EG95-E for EMEA Region           | LTE FDD: B1 / B3 / B7 / B8 / B20 / B28A<br/> WCDMA: B1 / B8<br/> GSM: 900 / 1800&nbsp;MHz |
| EG95-NA for North America Region | LTE FDD: B2 / B4 / B5 / B12 / B13<br/> WCDMA: B2 / B4 / B5                                |




### Software

| LoRa                                                    | Network            | Management              |
|---------------------------------------------------------|--------------------|-------------------------|
| Gateway OTA management                                  | Wi-Fi AP mode      | WisDM                   |
| LoRa package forward (packet forwarder, Basics Station) | Wi-Fi Client mode  | SSH2, NTP               |
| Frequency Band Setup                                    | LTE APN Setup      | Firmware update         |
| Country code setup                                      | 802.1q             | LoRa Packet Forwarder   |
| TX Power Setup                                          | Uplink backup      | Built-in Network Server |
| Data logger                                             | Firewall           | MQTT Bridge             |
| Location setup                                          | DHCP Server/Client | OpenVPN, Ping Watch Dog |
| Statistic                                               |                    | WEB UI                  |
| Supports class A, B, and C                              |                    |                         |
| Server address and Port setup                           |                    |                         |

### Firmware

| Model                                   | Source                                                                                                                  |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| RAK7240V2/RAK7240CV2 WisGate Edge Prime | <a href="https://downloads.rakwireless.com/LoRa/WisGateOS2/WisGateOS2_Latest_Firmware.zip" target="_blank">Download</a> |

## Models/Bundles

<table>
    <thead>
        <tr><th>Models</th><th>Variants</th><th>Packing list</th></tr>
    </thead>
    <tbody>
        <tr><td rowSpan="2">RAK7240V2</td><td>8 Channels without 4G</td><td>1 x 8-channel device<br/>1 x GPS Antenna<br/>1 x 2.4G Wi-Fi Antenna<br/>1 x PoE Injector<br/>1 x Mounting Kit<br/>1 x Manual</td></tr>
        <tr><td>8 Channels without 4G<br/>DC and Battery Plus support</td><td>1 x 8-channel device with DC Input interface<br/>1 x GPS Antenna<br/>1 x 2.4G Wi-Fi Antenna<br/>1 x PoE Injector<br/>1 x Mounting Kit<br/>1 x Cable for RAK Battery Plus<br/>1 x Manual</td></tr>
        <tr><td rowSpan="2">RAK7240V2</td><td>16 Channels without 4G</td><td>1 x 16-channel device<br/>1 x GPS Antenna<br/>1 x 2.4G Wi-Fi Antenna<br/>1 x PoE Injector<br/>1 x Mounting Kit<br/>1 x Manual</td></tr>
        <tr><td>16 Channels without 4G<br/>DC and Battery Plus support</td><td>1 x 16-channel device with DC Input interface<br/>1 x GPS Antenna<br/>1 x 2.4G Wi-Fi Antenna<br/>1 x PoE Injector<br/>1 x Mounting Kit<br/>1 x Cable for RAK Battery Plus<br/>1 x Manual</td></tr>
         <tr><td rowSpan="2">RAK7240CV2</td><td>8 Channels with 4G</td><td>1 x 8-channel device with LTE module<br/>2 x LTE Antenna<br/>1 x GPS Antenna<br/>1 x 2.4G Wi-Fi Antenna<br/>1 x PoE Injector<br/>1 x Mounting Kit<br/>1 x Manual</td></tr>
        <tr><td>8 Channels with 4G<br/>DC and Battery Plus support</td><td>1 x 8-channel device with LTE module and DC Input interface<br/>2 x LTE Antenna<br/>1 x GPS Antenna<br/>1 x 2.4G Wi-Fi Antenna<br/>1 x PoE Injector<br/>1 x Mounting Kit<br/>1 x Cable for RAK Battery Plus<br/>1 x Manual</td></tr>
    </tbody>
</table>

## Certification

<RkCertificationIcons certifications={[
    {
        'anatel': 'https://downloads.rakwireless.com/LoRa/RAK7240V2/Certification/RAK7240V2_ANATEL_Certification.pdf',
    },
    {
        'anatel': 'https://downloads.rakwireless.com/LoRa/RAK7240V2/Certification/RAK7240CV2_ANATEL_Certification.pdf',
    },
    {
        'fcc': 'https://downloads.rakwireless.com/LoRa/RAK7240V2/Certification/RAK7240V2_FCC_Certification.pdf',
    },
    {
        'fcc': 'https://downloads.rakwireless.com/LoRa/RAK7240V2/Certification/RAK7240CV2_FCC_Certification.pdf',
    },
    {
        'ised': 'https://downloads.rakwireless.com/LoRa/RAK7240V2/Certification/RAK7240V2_ISED_Certification.pdf',
    },
    {
        'ised': 'https://downloads.rakwireless.com/LoRa/RAK7240V2/Certification/RAK7240CV2_ISED_Certification.pdf',
    },
    {
        'ce': 'https://downloads.rakwireless.com/LoRa/RAK7240V2/Certification/RAK7240V2_RAK7240CV2_CE_Certification.pdf',
    },
    {
        'red': 'https://downloads.rakwireless.com/LoRa/WisGate/Certification/WisGate_RED_Verification.pdf'
    },

]} />

<RkBottomNav/>