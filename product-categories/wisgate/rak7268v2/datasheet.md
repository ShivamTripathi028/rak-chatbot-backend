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

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK7268V2/RAK7268CV2 WisGate Edge Lite 2 Datasheet


## Overview

### Description

The **RAK7268V2 / RAK7268CV2 WisGate Edge Lite 2** is part of the **RAK Edge Series**, offering flexible connectivity options to meet the needs of a wide range of IoT applications. Designed for **indoor use**, this gateway simplifies deployment with built-in Ethernet connectivity and onboard **2.4&nbsp;GHz WiFi** for easy configuration through the default WiFi AP mode. The **RAK7268CV2** version additionally supports LTE uplink communication, offering optional cellular backhaul for remote deployments or environments requiring LTE connectivity.

The gateway operates on **[WisGateOS 2](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/)**, a powerful platform that ensures enhanced security, robust functionality, and flexibility for customizations via extensions. Furthermore, the **RAK7268V2 / RAK7268CV2** integrates seamlessly with **[WisDM](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/)**, enabling fleet management and remote monitoring of multiple devices, making it an ideal choice for managing large networks of gateways.

Designed for versatile indoor deployments, this gateway supports flexible power input options—including PoE, 12&nbsp;V<sub>DC</sub>, and 9–24&nbsp;V<sub>DC</sub>—as well as multiple LTE configurations with either built-in antennas or external antennas.

**Product Variants Overview**

| **Gateway  Model** | **Configuration  Type** | **LTE  Module**           | **Power  Input**         |
|--------------------|-------------------------|---------------------------|--------------------------|
| RAK7268CV2         | LTE (Internal Antennas) | Built-in LTE Cat 4 module | 12&nbsp;V<sub>DC</sub>   |
| RAK7268CV2         | LTE (External Antennas) | Built-in LTE Cat 4 module | 12&nbsp;V<sub>DC</sub>   |
| RAK7268CV2         | LTE (Internal Antennas) | Built-in LTE Cat 4 module | 9–24&nbsp;V<sub>DC</sub> |
| RAK7268V2          | Non-LTE                 | Not included              | 12&nbsp;V<sub>DC</sub>   |
| RAK7268V2          | Non-LTE                 | Not included              | 9–24&nbsp;V<sub>DC</sub> |

### Features

#### Hardware

- **8 LoRa channels**
- Supports **2.4&nbsp;GHz WiFi AP** for easy configuration
- **100M Base-T Ethernet** with **PoE** (Power over Ethernet)
- **RP-SMA** LoRa antenna connector
- **Multi-backhaul options** with Ethernet, WiFi, and **Cellular** (only in **RAK7268CV2**)
- **SD card** for log backup and LoRa frame buffering (in case of backhaul failover)
- Optional **LTE Cat 4** network (only in **RAK7268CV2**)
- **Breathing light** for visual monitoring the gateway’s status

#### Software

- **[WisGateOS 2](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/)** for enhanced security and functionality
- **Extension add-ons** for customized gateway functionality:
  - <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/" target="_blank">Compatible with WisGateOS 2 version 2.2.x or later</a>
  - <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/" target="_blank">Compatible with WisGateOS 2 versions 2.0.x and 2.1.x</a>
- **[WisDM](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/)** for remote management and monitoring
- Built-in **Network Server**
- **Basic Station** and **Packet Forwarder** modes
- **LoRa Frame Filtering** (node whitelisting in Packet Forwarder mode)
- **MQTT v3.1 Bridging** with **TLS encryption** (compatible with ChirpStack LNS)
- LoRa frame buffering in **Packet Forwarder mode** in case of NS outage, ensuring **no data loss**

:::tip NOTE
A 9~24&nbsp;V<sub>DC</sub> power input version of RAK7268V2 or RAK7268CV2 WisGate  Edge Lite 2 is available upon request. For more information or to make a  purchase, kindly contact [inquiry@rakwireless.com](mailto:inquiry@rakwireless.com).
:::


## Specifications

### Overview

#### Block Diagram

The block diagram of RAK7268V2/RAK7268CV2 shows the internal architecture of the hardware.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7268-v2/datasheet/block-diagram-without-lte.png"
  width="100%"
  caption="RAK7268V2 Block Diagram"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7268-v2/datasheet/block-diagram-with-lte.png"
  width="100%"
  caption="RAK7268CV2 Block Diagram"
/>

:::tip NOTE

+ The internal block diagram applies to all models of the RAK7268V2 / RAK7268CV2 series, including both LTE and non-LTE versions.
+ The only variant-level difference is the **DC input range**, which is either **12&nbsp;V fixed** or **9–24&nbsp;V wide range**, depending on the model.
+ For LTE versions, the antenna type (internal or external) does not affect the internal layout—both use the same dual-antenna LTE module .

:::

#### Main Specifications

<table>
    <thead>
      <tr><th>Feature</th><th>Specifications</th></tr>
    </thead>
    <tbody>
        <tr><td>Computing</td><td>MT7628, 128&nbsp;MB DDR2 RAM</td></tr>
        <tr><td rowSpan="4">LoRa Feature</td><td>SX1302 Mini PCIe card</td></tr>
        <tr><td>8 Channels</td></tr>
        <tr><td>Frequency: EU868/IN865/RU864/US915/AU915/KR920/AS923-1/2/3/4/EU433/CN470</td></tr>
        <tr><td>LoRa Radio: Refer to the <a href="#lora-radio-specifications">LoRa Radio Specifications</a> section for detailed information.</td></tr>
        <tr><td rowSpan="3">WiFi Feature</td><td>Frequency: 2.4&nbsp;GHz (802.11b/g/n)</td></tr>
        <tr><td>Channels: 1-13 (2.4&nbsp;GHz)</td></tr>
        <tr><td>WiFi Radio: Refer to the <a href="#wifi-radio-specifications">WiFi Radio Specifications</a> section for detailed information.</td></tr>
        <tr><td>Cellular (Optional)</td><td><b>Nano SIM Card:</b> 12&nbsp;mm x 9&nbsp;mm x 0.67&nbsp;mm<br />Supports Quectel EG95-E/EG95-NA/EC25-J/EC25-AU/EC25-E (IoT/M2M -optimized LTE Cat 4 Module)<br />LTE Radio: Refer to the <a href="#lte-radio-specifications-optional-available-with-rak7268cv2">LTE Radio Specifications</a> section for detailed information.</td></tr>
        <tr><td rowSpan="4">Power Supply</td><td>PoE (IEEE 802.3 af), 36-57&nbsp;V<sub>DC</sub> — supported by all models</td></tr>
        <tr><td>12&nbsp;V<sub>DC</sub> - 1&nbsp;A – available on selected models</td></tr>
        <tr><td>9-24&nbsp;V<sub>DC</sub> – available on selected models</td></tr>
        <tr><td>Power consumption: 3&nbsp;W (typical)</td></tr>
        <tr><td rowSpan="3">Antenna</td><td>LoRa: External antenna / RP-SMA connector</td></tr>
        <tr><td>WiFi: Internal antenna</td></tr>
        <tr><td>LTE: Internal antenna or External antenna / RP-SMA connector (depending on version)</td></tr>
        <tr><td>Ingress Protection</td><td>IP30</td></tr>
        <tr><td>Enclosure Material</td><td>Plastic (PC+ABS)</td></tr>
        <tr><td>Weight</td><td>0.3&nbsp;kg</td></tr>
        <tr><td>Dimensions</td><td>166&nbsp;mm x 127.5&nbsp;mm x 36&nbsp;mm<br />Gateway only (no antenna, no bracket)</td></tr>
        <tr><td rowSpan="2">Operating Conditions</td><td>Operating Temperature: -10˚&nbsp;C to ﹢55˚&nbsp;C<br />Storage Temperature: -40˚&nbsp;C to ﹢85˚&nbsp;C</td></tr>
        <tr><td>Operating Humidity: 0-95%&nbsp;RH non-condensing<br />Storage Humidity: 0-95%&nbsp;RH non-condensing</td></tr>
        <tr><td>Installation Method</td><td>Desktop mounting<br />Wall mounting (via included bracket)<br />Rail mounting (via included bracket)</td></tr>
    </tbody>
</table>




### Hardware

This section provides an overview of the hardware specifications for the RAK7268V2 / RAK7268CV2 gateway, including its interfaces, core functions, and key board parameters.

#### Interfaces


The RAK7268V2/RAK7268CV2 gateway provides several hardware interfaces, enabling various connectivity options and functionalities. The following diagrams illustrate the gateway interfaces for each configuration:

+ **12&nbsp;V Power Supply**

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7268-v2/datasheet/interfaces.png"
  width="100%"
  caption="RAK7268V2/RAK7268CV2 12&nbsp;V power interfaces"
/>

+ **12&nbsp;V Power Supply, With External LTE Antennas**

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7268-v2/datasheet/interfaces1.png"
  width="100%"
  caption="RAK7268CV2 power and antenna interfaces"
/>

+ **9-24&nbsp;V Power Supply**

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7268-v2/datasheet/interfaces2.png"
  width="100%"
  caption="RAK7268V2/RAK7268CV2 9-24&nbsp;V power interfaces"
/>

##### Interface Description

| Interfaces                        | Description             | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **DC 12&nbsp;V / DC 9-24&nbsp;V** | Power Input             | Provides power supply for the gateway.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **ETH (PoE)**                     | RJ45 (10/100&nbsp;Mbps) | 10/100&nbsp;Mbps Ethernet interface for wired network connectivity. <br /> **PoE (Power over Ethernet)** allows the gateway to receive both power and data through a single Ethernet cable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Console**                       | Type-C USB              | Used for debugging.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Reset**                         | Reset Key               | **Short press**: Reboot the gateway. <br />**Long press** (5&nbsp;sec and above): Restore factory settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **NanoSIM**                       | NanoSIM Card Slot       | Slot for a NanoSIM card, enabling cellular connectivity. Available on all models; functional only with LTE-enabled versions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **TF Card**                       | SD Card Slot            | A 16&nbsp;GB SD card is pre-installed in the gateway for data logging, system configurations, and other use cases that require local storage.<br /><div style={{ borderLeft: '6px solid #f4b400', backgroundColor: '#fff8e1', padding: '12px', borderRadius: '6px', color: '#5f370e', fontFamily: 'sans-serif' }}><strong style={{ display: 'inline-flex', alignItems: 'center', fontSize: '16px' }}>⚠️ WARNING</strong><br/><span style={{ display: 'block', marginTop: '4px' }}><strong>Do not</strong> eject the SD card located in the SD card slot during installation, as it stores logs and data essential for the device's performance.</span></div> |
| **LEDs**                          | Status Indicator LEDs   | PWR LED <br/>LoRa LED<br/>WLAN LED <br/>LTE LED <br/>Breathing LED<br />LTE LED (only in RAK7268CV2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **LoRa**                          | LoRa Antenna Connector  | RP-SMA connector for external LoRa antenna, enabling LoRaWAN communication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **MAIN / AUX**                    | LTE Antenna Connectors  | Available only on models that support external LTE antennas. These versions include two RP-SMA connectors (MAIN and AUX) for connecting external LTE antennas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |


##### LED Indicators Details



<table>
<thead>
        <tr>
            <th>LED</th>
            <th>Status</th>
            <th>Description</th>
        </tr>
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
            <td>Slow Flash (1&nbsp;Hz)</td>
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
            <td colspan="2">The breathing light can be programmed for different statuses. For detailed instructions on how to program the breathing light, refer to the appropriate installation guide based on your firmware version:<ul><li><a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/#rak-breathing-light" target="_blank">Compatible with WisGateOS 2 version 2.2.x or later</a></li><li><a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/#breathing-light" target="_blank">Compatible with WisGateOS 2 versions 2.0.x and 2.1.x</a></li></ul></td>
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

<table>
    <thead>
      <tr><th>Feature</th><th>Specifications</th></tr>
    </thead>
    <tbody>
        <tr><td>Operating Frequency</td><td>EU868/IN865/RU864/US915/AU915/KR920/AS923-1/2/3/4/EU433/CN470</td></tr>
        <tr><td>Transmit Power</td><td>27&nbsp;dBm (Max)</td></tr>
        <tr><td>Receiver Sensitivity</td><td>-139&nbsp;dBm (Min)</td></tr>
</tbody>
</table>



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
      <td>Frequency</td>
      <td>ISM band: 2.412-2.472&nbsp;GHz</td>
    </tr>
    <tr>
      <td>Channels</td>
      <td>45670</td>
    </tr>
    <tr>
      <td rowSpan="3">Transmit Power (The max power maybe different depending on local regulations): per chain</td>
      <td>**802.11b** <br /> 19&nbsp;dBm @1&nbsp;Mbps <br /> 19&nbsp;dBm @11&nbsp;Mbps</td>
    </tr>
    <tr>
      <td>**802.11g** <br /> 18&nbsp;dBm @6&nbsp;Mbps <br /> 16&nbsp;dBm @54&nbsp;Mbps</td>
    </tr>
    <tr>
      <td>**802.11n (2.4&nbsp;GHz)** <br /> 18&nbsp;dBm @MCS0 (HT20) <br /> 16&nbsp;dBm @MCS7 (HT20) <br /> 17&nbsp;dBm @MCS0 (HT40) <br /> 15&nbsp;dBm @MCS7 (HT40)</td>
    </tr>
    <tr>
      <td rowSpan="3">Receiver Sensitivity (Typical)</td>
      <td>**802.11b** <br /> -95&nbsp;dBm @1&nbsp;Mbps <br /> -88&nbsp;dBm @11&nbsp;Mbps</td>
    </tr>
    <tr>
      <td>**802.11g** <br /> -90&nbsp;dBm @6&nbsp;Mbps <br /> -75&nbsp;dBm @54&nbsp;Mbps</td>
    </tr>
    <tr>
      <td>**802.11n (2.4&nbsp;GHz)** <br /> -89&nbsp;dBm @MCS0 (HT20) <br /> -72&nbsp;dBm @MCS7 (HT20) <br /> -86&nbsp;dBm @MCS0 (HT40) <br /> -68&nbsp;dBm @MCS7 (HT40)</td>
    </tr>
  </tbody>
</table>

##### LTE Radio Specifications (Optional, Available with RAK7268CV2)

<table>
    <thead><tr><th>Module / Region</th><th>Supported Bands</th></tr></thead>
    <tbody>
    <tr><td rowSpan="3">EG95-E (EMEA Region)</td><td>LTE FDD: B1/B3/B7/B8/B20/B28A </td></tr>
    <tr><td>WCDMA: B1/B8</td></tr>
    <tr><td>GSM/EDGE: B3/B8</td></tr>
    <tr><td rowSpan="2">EG95-NA (North America)</td><td>LTE FDD: B2/B4/B5/B12/B13 </td></tr>
    <tr><td>WCDMA: B2/B4/B5</td></tr>
    <tr><td rowSpan="3">EC25-J (Japan)</td><td>LTE FDD: B1/B3/B8/B18/B19/B26 </td></tr>
    <tr><td>WCDMA: B1/B6/B8/B19</td></tr>
    <tr><td>LTE TDD: B41</td></tr>
    <tr><td rowSpan="4">EC25-AU (LATAM / AU / NZ)</td><td>LTE FDD: B1/B2/B3/B4/B5/B7/B8/B28 </td></tr>
    <tr><td>WCDMA: B1/B2/B5/B8</td></tr>
    <tr><td>LTE TDD: B40</td></tr>
    <tr><td>GSM: B2/B3/B5/B8</td></tr>
    <tr><td rowSpan="4">EC25-E (Korea/India)</td><td>LTE FDD: B1/B3/B5/B7/B8/B20 </td></tr>
    <tr><td>WCDMA: B1/B5/B8</td></tr>
    <tr><td>LTE TDD: B38/B40/B41</td></tr>
    <tr><td>GSM: B3/B8</td></tr>
    <tr><td rowSpan="2">Other PCIE LTE modules</td></tr>
    <tr><td>Optional support for global bands (custom module)</td></tr>
</tbody>
</table>



### Software

The RAK7268V2/RAK7268CV2 gateway runs on WisGateOS 2, a robust software platform designed for efficient network management and integration. Below are the key software features and capabilities:

For more detailed information on software configurations and usage, refer to the [WisGateOS 2 User Guide](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/).

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
      <td rowSpan="9">**LoRaWAN and Network Management**</td>
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
      <td rowSpan="5">**Connectivity and Network Services**</td>
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
      <td rowSpan="4">**Monitoring and Security**</td>
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
      <td rowSpan="6">**User Interface and Management**</td>
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

The firmware is built on **OpenWrt**, providing a flexible and secure foundation for the gateway. It features an intuitive **web UI** for straightforward configuration and management, as well as **SSH2** support for remote management. **WisGateOS 2** also supports the installation of various extensions, including **OpenVPN**, **WireGuard**, and custom logo configurations.

For more details on available extensions, refer to the [WisGateOS 2 Extensions Guide](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/overview/#supported-extensions).

|                  Model                   |                                            Source                                            |
|:----------------------------------------:|:--------------------------------------------------------------------------------------------:|
| RAK7268V2/RAK7268CV2 WisGate Edge Lite 2 | [Download](https://downloads.rakwireless.com/LoRa/WisGateOS2/WisGateOS2_Latest_Firmware.zip) |




## Certification

<RkCertificationIcons certifications={[
    {
        'anatel': 'https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268V2_ANATEL_Certification.pdf',
    },
    {
        'anatel': 'https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268CV2_ANATEL_Certification.pdf',
    },
    {
        'ce': 'https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_RAK7268V2_RAK7268C_RAK7268CV2_CE_Certification.pdf',
    },
    {
        'ised': 'https://downloads.rakwireless.com/LoRa/RAK7268V2/Certification/RAK7268_RAK7268V2_IC_Certification.pdf',
    },
    {
        'ised': 'https://downloads.rakwireless.com/LoRa/RAK7268V2/Certification/RAK7268C_RAK7268CV2_IC_Certification.pdf',
    },
    {
        'fcc': 'https://downloads.rakwireless.com/LoRa/RAK7268V2/Certification/RAK7268_RAK7268V2_FCC_Certification.pdf',
    },
    {
        'fcc': 'https://downloads.rakwireless.com/LoRa/RAK7268V2/Certification/RAK7268C_RAK7268CV2_FCC_Certification.pdf',
    },
    {
        'jrl': 'https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_RAK7268V2_RAK7268C_RAK7268CV2_JRL_Certification.pdf',
    },
    {
        'jtbl': 'https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_RAK7268V2_JTBL_Certification.pdf',
    },
    {
        'kc': 'https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268V2_RAK7268CV2_KC_Certification.pdf',
    },
    {
        'rcm': 'https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_RAK7268V2_RAK7268C_RAK7268CV2_RCM_Certification.pdf',
    },
    {
        'reach': 'https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268C_RAK7268CV2_RAK7268_RAK7268V2_REACH_Report.pdf',
    },
    {
        'red': 'https://downloads.rakwireless.com/LoRa/WisGate/Certification/WisGate_RED_Verification.pdf'
    },
    {
        'rohs': 'https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268C_RAK7268CV2_RAK7268_RAK7268V2_RoHS_Report.pdf',
    },
    {
        'rsm': 'https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_RAK7268V2_RAK7268C_RAK7268CV2_RSM_Certification.pdf',
    },
    {
        'ukca': 'https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_RAK7268V2_RAK7268C_RAK7268CV2_UKCA_Certification.pdf',
    },

]} />

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

This equipment complies with FCC radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 20&nbsp;cm between the radiator and your body.

<RkBottomNav/>