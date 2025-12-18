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

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK7266 WisGate Soho Lite Datasheet


## Overview

### Description

The **RAK7266 WisGate Soho Lite** is an indoor LoRaWAN gateway from the **RAK Soho Series**, designed for versatile and compact IoT deployments. It comes with an **integrated LTE Cat 1 module** and offers **multiple backhaul options**, including **cellular (LTE)**, **WiFi**, and **Ethernet**, ensuring versatile deployment options in environments with or without wired internet access.

This gateway supports **8 LoRa channels** and onboards **2.4&nbsp;GHz WiFi** for easy configuration through the default WiFi AP mode. An **Ethernet port** is available for wired network access when needed. The device is powered via a **stable 12V DC input**, making it well-suited for controlled indoor environments such as smart panels, utility cabinets, or fixed installations.

Depending on the variant, LTE antennas may be **internal** or **externally connected via RP-SMA connectors**, allowing users to select the best option for signal conditions and installation constraints.

The RAK7266 runs on **WisGateOS 2**, a secure, modular firmware based on OpenWrt developed by RAK. It provides access to a wide range of features, including extension modules, a built-in LoRaWAN Network Server, and advanced system diagnostics. Additionally, it supports integration with **WisDM** for centralized management and fleet monitoring, making it a powerful and practical solution for LTE-based indoor deployments.

### Features

#### Hardware

- **8 LoRa channels**
- Supports **2.4&nbsp;GHz WiFi**, with **AP mode enabled by default** for easy configuration
- **100M Base-T Ethernet port** (for network access, no PoE)
- **RP-SMA** LoRa antenna connector
- An integrated **LTE Cat 1 module** for cellular backhaul
- Multi backhaul options with **Ethernet, WiFi, and Cellular**
- **Breathing light** for visual status indication

#### Software

- **[WisGateOS 2](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/?intsource=docs_center&intmedium=organic&intcampaign=rak7266_documentation_datasheet_page&intterm=wisgate_os2&intcontent=documentation_link)** – A secure, OpenWrt-based OS developed by RAK for enhanced stability and flexibility.
- **Extension add-ons** for customized gateway functionality:
  - <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/" target="_blank">Compatible with WisGateOS 2 version 2.2.x or later</a>
  - <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/" target="_blank">Compatible with WisGateOS 2 versions 2.0.x and 2.1.x</a>
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

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7266/datasheet/block-diagram.png"
  width="100%"
  caption="RAK7266 Block Diagram"
/>

#### Main Specifications

<table>
  <thead>
    <tr><th>Feature</th><th>Specifications</th></tr>
  </thead>
  <tbody>
    <tr><td>Computing</td><td>MT7628, 128&nbsp;MB DDR2 RAM</td></tr>
    <tr><td rowSpan="4">LoRa Feature</td><td>SX1302 / SX1303 Mini PCIe card (<i>The default configuration uses the SX1302 Mini PCIe card, with an SX1303 version available upon request.</i>)</td></tr>
    <tr><td>8 Channels</td></tr>
    <tr><td>Frequency: EU868/IN865/RU864/US915/AU915/KR920/AS923-1-2-3-4/EU433/CN470</td></tr>
    <tr><td>LoRa Radio: Refer to the [LoRa Radio Specifications](#lora-radio-specifications) section for detailed information.</td></tr>
    <tr><td rowSpan="3">WiFi Feature</td><td>Frequency: 2.4&nbsp;GHz (802.11b/g/n)</td></tr>
    <tr><td>Channels: 1-13</td></tr>
    <tr><td>WiFi Radio: Refer to the [WiFi Radio Specifications](#wifi-radio-specifications) section for detailed information.</td></tr>
    <tr><td>Cellular</td><td><b>Nano SIM Card:</b> 12&nbsp;mm x 9&nbsp;mm x 0.67&nbsp;mm<br />Supports Quectel EG915U-EU / EG915U-LA / EG915Q-NA(IoT / M2M -LTE Cat 1 module)<br />LTE Radio: Refer to the [LTE Radio Specifications](#lte-radio-specifications) section for detailed information.</td></tr>
    <tr><td>Power Supply</td><td>12&nbsp;V<sub>DC</sub></td></tr>
    <tr><td rowSpan="3">Antenna</td><td>LoRa: External antenna / RP-SMA connector</td></tr>
    <tr><td>WiFi: Internal antenna</td></tr>
    <tr><td>LTE: Internal antenna or External antenna / RP-SMA connector</td></tr>
    <tr><td>Ingress Protection</td><td>IP30</td></tr>
    <tr><td>Enclosure Material</td><td>Plastic (PC+ABS)</td></tr>
    <tr><td>Weight</td><td>0.3 kg</td></tr>
    <tr><td>Dimensions</td><td>166&nbsp;mm x 127.5&nbsp;mm x 36&nbsp;mm Gateway only (no antenna, no bracket)</td></tr>
    <tr><td>Operating Conditions</td><td><ul><li>Operating Temperature: -10˚&nbsp;C to ﹢55˚&nbsp;C</li><li>Storage Temperature: -40˚&nbsp;C to ﹢85˚&nbsp;C</li><li>Operating Humidity: 0\~95%&nbsp;RH non-condensing</li><li>Storage Humidity: 0\~95%&nbsp;RH non-condensing</li></ul></td></tr>
    <tr><td>Installation Method</td><td><ul><li>Desktop mounting</li><li>Wall mounting (via included bracket)</li><li>Rail mounting (via included bracket)</li></ul></td></tr>
  </tbody>
</table>


### Hardware

The hardware specification covers the interfacing of the RAK7266 gateway and its corresponding functionalities, along with the parameters and standard values of the board.

#### Interfaces


The RAK7266 gateway provides several hardware interfaces, enabling various connectivity options and functionalities.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7266/datasheet/interfaces.png"
  width="100%"
  caption="RAK7266 interfaces"
/>

##### Interface Description

| Interfaces  | Description             | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **DC 12V**  | Power Input             | Provides power supply for the gateway.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **ETH**     | RJ45 (10/100&nbsp;Mbps) | 10/100&nbsp;Mbps Ethernet interface for wired network connectivity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Console** | Type-C USB              | Used for debugging.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Reset**   | Reset Key               | **Short press**: Reboot the gateway. <br />**Long press** (5&nbsp;sec and above): Restore factory settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **NanoSIM** | NanoSIM Card Slot       | Slot for a NanoSIM card, enabling cellular connectivity.<br /><div style={{ borderLeft: '6px solid #f4b400', backgroundColor: '#fff8e1', padding: '12px', borderRadius: '6px', color: '#5f370e', fontFamily: 'sans-serif' }}><strong style={{ display: 'inline-flex', alignItems: 'center', fontSize: '16px' }}>⚠️ WARNING</strong><br/><span style={{ display: 'block', marginTop: '4px' }}> The SIM card slot of the cellular versions is not hot-swappable. Make sure the gateway is switched off before inserting or ejecting the SIM card.</span></div>                                                                                                 |
| **TF Card** | SD Card Slot            | A 16&nbsp;GB SD card is pre-installed in the gateway for data logging, system configurations, and other use cases that require local storage.<br /><div style={{ borderLeft: '6px solid #f4b400', backgroundColor: '#fff8e1', padding: '12px', borderRadius: '6px', color: '#5f370e', fontFamily: 'sans-serif' }}><strong style={{ display: 'inline-flex', alignItems: 'center', fontSize: '16px' }}>⚠️ WARNING</strong><br/><span style={{ display: 'block', marginTop: '4px' }}><strong>Do not</strong> eject the SD card located in the SD card slot during installation, as it stores logs and data essential for the device's performance.</span></div> |
| **LEDs**    | Status Indicator LEDs   | <ul><li>PWR LED</li><li>LoRa LED</li><li>WLAN LED</li><li>LTE LED</li><li>Breathing LED</li><li>ETH LED</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **LoRa**    | LoRa Antenna Connector  | RP-SMA connector for external LoRa antenna, enabling LoRaWAN communication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **MAIN**    | LTE Antenna Connector   | RP-SMA connector for external LTE antenna.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **AUX**     | Reserve                 | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

##### LED Indicators Details

<table>
  <thead>
    <tr><th>LEDs</th><th>Status Indication Description</th></tr>
  </thead>
  <tbody>
     <tr>
        <td rowspan="2">PWR</td>
        <td>On</td>
        <td>Gateway is powered on</td>
     </tr>
     <tr>
        <td>Off</td>
        <td>Gateway is powered off</td>
     </tr>
     <tr>
            <td rowspan="3">LoRa</td>
            <td>On</td>
            <td>LoRa module active</td>
     </tr>
     <tr>
            <td>Off</td>
            <td>LoRa module inactive</td>
     </tr>
     <tr>
            <td>Flashing</td>
            <td>Indicates LoRa packet transmission/reception</td>
     </tr>
     <tr>
            <td rowspan="8">WLAN</td>
            <td colspan="2"><strong>AP Mode</strong></td>
     </tr>
     <tr>
            <td>On</td>
            <td>AP is up</td>
     </tr>
     <tr>
            <td>Off</td>
            <td>AP is down</td>
     </tr>
     <tr>
            <td>Flashing</td>
            <td>Data transmitting or receiving</td>
     </tr>
     <tr>
            <td colspan="2"><strong>STA Mode</strong></td>
     </tr>
     <tr>
            <td>Slow Flash (1 Hz)</td>
            <td>Disconnected from WiFi network</td>
     </tr>
     <tr>
            <td>On</td>
            <td>Connected to WiFi network</td>
     </tr>
     <tr>
            <td>Flashing</td>
            <td>Data transmitting or receiving</td>
     </tr>
     <tr>
            <td rowspan="3">LTE (functional only in RAK7268CV2)</td>
            <td>Slow Flash 1<br/>(1800&nbsp;ms bright / 200&nbsp;ms dark)</td>
            <td>Searching for network (unregistered)</td>
     </tr>
     <tr>
            <td>Slow Flash 2<br/>(200&nbsp;ms bright / 1800&nbsp;ms dark)</td>
            <td>Idle (registered to network)</td>
     </tr>
     <tr>
            <td>Quick Flash<br/>(125&nbsp;ms bright / 125&nbsp;ms dark)</td>
            <td>Data transmitting or receiving</td>
     </tr>
     <tr>
            <td rowspan="3">Breathing LED</td>
            <td>Red (fast blinking)</td>
            <td>Abnormal (e.g., no internet)</td>
     </tr>
     <tr>
            <td>Blue (slow blinking)</td>
            <td>Normal operation</td>
     </tr>
     <tr>
            <td colspan="2">The breathing light can be programmed for different statuses. For detailed instructions on how to program the breathing light, refer to the <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later#rak-breathing-light">RAK Breathing Light Extension</a>.</td>
     </tr>
     <tr>
            <td rowspan="3">ETH</td>
            <td>On</td>
            <td>Linkup</td>
     </tr>
     <tr>
            <td>Off</td>
            <td>Linkdown</td>
     </tr>
    <tr>
            <td>Flashing</td>
            <td>Data transmitting and receiving</td>
     </tr>
  </tbody>
</table>




#### RF Specifications

##### LoRa Radio Specifications

| Parameter            | Specifications                                                |
|----------------------|---------------------------------------------------------------|
| Operating Frequency  | EU868/IN865/RU864/US915/AU915/KR920/AS923-1/2/3/4/EU433/CN470 |
| Transmit Power       | 27&nbsp;dBm (Max)                                             |
| Receiver Sensitivity | -139&nbsp;dBm (Min)                                           |



##### WiFi Radio Specifications

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Specifications</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Wireless Standard</td>
      <td>IEEE 802.11b/g/n</td>
    </tr>
    <tr>
      <td>Operating Frequency</td>
      <td>ISM band: 2.412-2.472&nbsp;GHz</td>
    </tr>
    <tr>
      <td>Operation Channels</td>
      <td>2.4&nbsp;GHz: 1-13</td>
    </tr>
    <tr>
      <td rowSpan="3">Transmit Power: per chain <br /> (The max power differs depending on local regulations.)</td>
        <td><strong>802.11b</strong><ul><li>19&nbsp;dBm @ 1&nbsp;Mbps</li><li>19&nbsp;dBm @ 11&nbsp;Mbps</li></ul></td>
    </tr>
    <tr>
        <td><strong>802.11g</strong><ul><li>18&nbsp;dBm @ 6&nbsp;Mbps</li><li>16&nbsp;dBm @ 54&nbsp;Mbps</li></ul></td>
    </tr>
    <tr>
        <td><strong>802.11n (2.4&nbsp;GHz)</strong><ul><li>18&nbsp;dBm @ MCS0 (HT20)</li><li>16&nbsp;dBm @ MCS7 (HT20)</li><li>17&nbsp;dBm @ MCS0 (HT40)</li><li>15&nbsp;dBm @ MCS7 (HT40)</li></ul></td>
    </tr>
    <tr>
      <td rowSpan="3">Receiver Sensitivity (Typical)</td>
        <td><strong>802.11b</strong><ul><li>-95&nbsp;dBm @ 1&nbsp;Mbps</li><li>-88&nbsp;dBm @ 11&nbsp;Mbps</li></ul></td>
    </tr>
    <tr>
        <td><strong>802.11g</strong><ul><li>-90&nbsp;dBm @ 6&nbsp;Mbps</li><li>-75&nbsp;dBm @ 54&nbsp;Mbps</li></ul></td>
    </tr>
    <tr>
        <td><strong>802.11n (2.4&nbsp;GHz)</strong><ul><li>-89&nbsp;dBm @ MCS0 (HT20)</li><li>-72&nbsp;dBm @ MCS7 (HT20)</li><li>-86&nbsp;dBm @ MCS0 (HT40)</li><li>-68&nbsp;dBm @ MCS7 (HT40)</li></ul></td>
    </tr>
  </tbody>
</table>


##### LTE Radio Specifications

| Module / Region                                        | Supported Bands                                                              |
|--------------------------------------------------------|------------------------------------------------------------------------------|
| EG915U-EU for EMEA/Brazil/Australia/New Zealand Region | LTE FDD: B1 / B3 / B5 / B7 / B8 / B20 / B28<br />GSM: B2 / B3 / B5 / B8      |
| EG915U-LA for Latin America Region                     | LTE FDD: B2 / B3 / B4 / B5 / B7 / B8 / B28 / B66<br />GSM: B2 / B3 / B5 / B8 |
| EG915Q-NA for North America Region                     | LTE FDD: B2 / B4 / B5 / B12 / B13 / B66 / B71                                |



### Software

The RAK7266 gateway runs on WisGateOS 2, a robust software platform designed for efficient network management and integration. Below are the key software features and capabilities:

For more detailed information on software configurations and usage, refer to the [WisGateOS 2 User Guide](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/?intsource=docs_center&intmedium=organic&intcampaign=rak7266_documentation_overview_page&intterm=wisgate_os2&intcontent=documentation_link).

<table>
  <thead>
    <tr>
      <th>Category</th>
      <th>Feature</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td rowSpan="9"><strong>LoRaWAN and Network Management</strong></td>
      <td>LoRaWAN Packet Forwarding</td>
      <td>Supports Packet Forwarder and Basic Station configurations</td>
    </tr>
    <tr>
      <td>Built-in Server</td>
      <td>Local LoRaWAN Network Server (LNS) integrated into the gateway for network management</td>
    </tr>
    <tr>
      <td>Frequency Band Setup</td>
      <td>Configurable with different LoRaWAN frequency bands based on deployment region</td>
    </tr>
    <tr>
      <td>TX Power Setup</td>
      <td>Adjustable transmit power for optimal network performance</td>
    </tr>
    <tr>
      <td>Automatic Data Recovery</td>
      <td>Ensures reliable data transmission even during network disruptions</td>
    </tr>
    <tr>
      <td>Server Address and Port Setup</td>
      <td>Custom configuration for LoRaWAN Network Server communication</td>
    </tr>
    <tr>
      <td>Supports LoRaWAN Class A and C</td>
      <td>Fully compatible with LoRaWAN devices operating in Class A and C</td>
    </tr>
    <tr>
      <td>Uplink Backup</td>
      <td>Enables automatic switchover to a backup uplink (e.g., LTE or WiFi) when the primary uplink fails. Requires Multi-WAN configuration.</td>
    </tr>
    <tr>
      <td>Location Setup</td>
      <td>Manual or automatic setup of gateway location (e.g., GPS coordinates)</td>
    </tr>
    <tr>
        <td rowSpan="5"><strong>Connectivity and Network Services</strong></td>
      <td>WiFi Client/AP Mode</td>
      <td>Connect to existing network or act as an access point</td>
    </tr>
    <tr>
      <td>DHCP Server/Client</td>
      <td>Dynamic IP address allocation for both server and client roles</td>
    </tr>
    <tr>
      <td>NAT and Router Module</td>
      <td>Enables router functionality with Network Address Translation</td>
    </tr>
    <tr>
      <td>WireGuard / OpenVPN</td>
      <td>Secure communication tunnel for remote access and management</td>
    </tr>
    <tr>
      <td>LTE APN Setup</td>
      <td>Configures Access Point Name for LTE connectivity</td>
    </tr>
    <tr>
        <td rowSpan="4"><strong>Monitoring and Security</strong></td>
      <td>Statistics and Data Logger</td>
      <td>Tracks performance metrics and logs operational data</td>
    </tr>
    <tr>
      <td>Firewall</td>
      <td>Provides basic firewall functions for traffic control and security</td>
    </tr>
    <tr>
      <td>SSH2</td>
      <td>Secure Shell access for remote troubleshooting and management</td>
    </tr>
    <tr>
      <td>Ping Watchdog</td>
      <td>Monitors connectivity and triggers recovery if the connection fails</td>
    </tr>
    <tr>
        <td rowSpan="6"><strong>User Interface and Management</strong></td>
      <td>Web UI</td>
      <td>Web-based interface for configuration and monitoring</td>
    </tr>
    <tr>
      <td>WisDM</td>
      <td>Cloud platform for remote management and monitoring</td>
    </tr>
    <tr>
      <td>Gateway OTA management</td>
      <td>Over-the-air firmware management for seamless updates</td>
    </tr>
    <tr>
      <td>MQTT Bridge</td>
      <td>Integration with IoT platforms using MQTT protocol</td>
    </tr>
    <tr>
      <td>Firmware Updates</td>
      <td>Over-the-air updates for easy firmware upgrades</td>
    </tr>
    <tr>
      <td>NTP</td>
      <td>Synchronizes the gateway system time for accurate timestamp recording</td>
    </tr>
  </tbody>
</table>


### Firmware

The firmware is built on **OpenWrt**, providing a flexible and secure foundation for the gateway. It features an intuitive **web UI** for straightforward configuration and management, as well as **SSH2** support for remote management. **WisGateOS 2** also supports the installation of various extensions, including **OpenVPN**, **WireGuard**, and custom logo configurations. For more details on available extensions, refer to the [WisGateOS 2 Extensions Guide](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/overview/?intsource=docs_center&intmedium=organic&intcampaign=rak7266_documentation_overview_page&intterm=extension-add-ons&intcontent=documentation_link).

|           Model           |                                                                                                                        Source                                                                                                                         |
|:-------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| RAK7266 WisGate Soho Lite | [Download](https://downloads.rakwireless.com/LoRa/WisGateOS2/WisGateOS2_Latest_Firmware.zip?utm_source=docs_center&utm_medium=organic&utm_campaign=rak7266-documentation-datasheet-page&utm_term=rak7266-firmware-download&utm_content_download-link) |



## Certification

<RkCertificationIcons certifications={[
    {
      'fcc': 'https://downloads.rakwireless.com/LoRa/RAK7266/Certification/RAK7266_FCC_Certification.pdf'
    },
    {
      'ised': 'https://downloads.rakwireless.com/LoRa/RAK7266/Certification/RAK7266_ISED_Certification.pdf'
    },
    {
      'red': 'https://downloads.rakwireless.com/LoRa/WisGate/Certification/WisGate_RED_Verification.pdf'
    }

]} />

<RkBottomNav/>