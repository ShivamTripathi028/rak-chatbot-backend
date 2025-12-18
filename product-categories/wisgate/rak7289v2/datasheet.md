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

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK7289V2/RAK7289CV2 WisGate Edge Pro V2 Datasheet

## Overview

### Description

The RAK7289V2 WisGate Edge Pro is the flagship product of the RAK Edge Series. Featuring industrial-grade components, it ensures a high level of reliability.

It supports up to 16 LoRa channels and offers multi-backhaul options with Ethernet, Wi-Fi, and cellular connectivity. Additionally, it provides a dedicated port for various power options, including solar panels and batteries. Its redesigned enclosure accommodates LTE, Wi-Fi, and GPS antennas internally for enhanced aesthetics and functionality.

In addition, RAK7289V2 operates under <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#overview" target="_blank">WisGateOS 2</a>, which is built on the latest OpenWrt kernel. The OS Web UI features a new design and supports multiple extension installations, enabling remote management using <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview" target="_blank">WisDM</a> for personalized gateway customization.

:::warning
This product is intended to be powered by 12&nbsp;V<sub>DC</sub> through a designated power port. The use of solar chargers is not recommended, as they may supply overvoltage, potentially damaging the device. We strongly discourage the use of such chargers with this product, and any damage incurred as a result will void the warranty.
:::

### Features

#### Hardware

- IP67/NEMA-6 industrial-grade enclosure with cable glands
- PoE (802.3af) + Surge Protection
- Dual LoRa Concentrators for up to 16 channels
- Backhaul: Wi-Fi, Ethernet, LTE (optional, available with RAK7289CV2)
- GPS
- Supports 12&nbsp;V<sub>DC</sub> or solar power supply with electricity monitoring (Solar Kit optional)
- Internal antennas for Wi-Fi, GPS, and LTE
- External antenna for LoRa
- Dying-gasp (optional)

#### Software

- <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/" target="_blank">WisGateOS 2</a>
- **WisGateOS 2 Extensions**: Adds support for features such as OpenVPN, WireGuard VPN, and more. Use the appropriate installation guide based on your WisGateOS 2 version:
    - <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/" target="_blank">For WisGateOS 2 version 2.2.x or later</a>
    - <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/" target="_blank">For WisGateOS 2 versions 2.0.x and 2.1.x</a>
- Remote management with <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/" target="_blank">WisDM</a> Fleet Management
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

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/datasheet/2.without-lte.png"
  width="70%"
  caption="RAK7289V2 Block Diagram"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/datasheet/1.with-lte.png"
  width="70%"
  caption="RAK7289CV2 Block Diagram"
/>


#### Main Specifications

<table>
    <thead><tr><th>Feature</th><th>Specifications</th></tr></thead>
    <tbody>
        <tr><td>Computing</td><td>MT7628, 128&nbsp;MB DDR2 RAM</td></tr>
        <tr><td rowSpan="5">LoRa Features</td><td>SX1303 mPCIe card (connects maximum of two)</td></tr>
        <tr><td>8 Channels (16 channels optional)</td></tr>
        <tr><td>Frequency: EU868 / IN865 / US915 / AU915 / KR920 / AS923-1/2/3/4 / EU433 / CN470</td></tr>
        <tr><td>Listen Before Talk</td></tr>
        <tr><td>LoRa Radio: Refer to the <a href="#lora-radio-specifications">LoRa Radio Specifications</a> section for detailed information.</td></tr>
        <tr><td rowSpan="4">Wi-Fi Features</td><td>Frequency: 2.4&nbsp;GHz (802.11b / g / n)</td></tr>
        <tr><td>Operation Channels: 1-13 (2.4&nbsp;GHz)</td></tr>
        <tr><td>2x2 MIMO</td></tr>
        <tr><td>Wi-Fi Radio: Refer to the <a href="#wi-fi-radio-specifications">Wi-Fi Radio Specifications</a> section for detailed information.</td></tr>
        <tr><td rowSpan="2">Cellular Features (available with RAK7289CV2)</td><td><b>Nano SIM Card:</b>12 x 9 x 0.67&nbsp;mm<br/>Supports Quectel EG95-E / EG95-NA / EC25-J / EC25-AU(IoT / M2M -optimized LTE Cat 4 Module)</td></tr>
        <tr><td>LTE Radio: Refer to the <a href="#lte-radio-specifications-optional-available-with-rak7289cv2">LTE Radio Specifications</a> section for detailed information.</td></tr>
        <tr><td>Power Supply</td><td>PoE (IEEE 802.3af) - 37~57&nbsp;V<sub>DC</sub><br/>12&nbsp;V<sub>DC</sub><br/>Compatible with RAK Battery Plus</td></tr>
        <tr><td rowSpan="2">Antenna</td><td>LoRa: N-Type connector (one for the 8-channel gateway and two for the 16-channel gateway)</td></tr>
        <tr><td>Wi-Fi / GPS / LTE: Internal antenna</td></tr>
        <tr><td>Ingress protection</td><td>IP67</td></tr>
        <tr><td>Enclosure material</td><td>Aluminium and plastic</td></tr>
        <tr><td>Dimensions</td><td>240&nbsp;mm x 240&nbsp;mm x 89.5&nbsp;mm</td></tr>
        <tr><td>Weight</td><td>4.6&nbsp;kg gateway only</td></tr>
        <tr><td rowSpan="5">Operating Conditions</td><td>Operating temperature: ﹣40˚&nbsp;C to ﹢70˚&nbsp;C</td></tr>
        <tr><td>Storage Temperature: ﹣40˚&nbsp;C to ﹢85˚&nbsp;C</td></tr>
        <tr><td>Operating humidity: 0% to 95% (non-condensing)</td></tr>
        <tr><td>Storage Humidity: 0% to 95% (non-condensing)</td></tr>
        <tr><td>For environmental reliability test details: <a href="https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289CV2%20Environmental%20Reliability%20Tests(no%20watermark).pdf" target="_blank">WisGate Edge Pro RAK7289V2/CV2 Environmental Reliability Test.</a></td></tr>
        <tr><td>Installation Method</td><td>Pole or wall mounting</td></tr>
</tbody>
</table>



### Hardware

The hardware specification details the interfacing of the RAK7289V2/RAK7289CV2 and its corresponding functionalities. It also outlines the parameters and standard values of the gateway.

#### Interfaces

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/datasheet/rak7289v2-interfaces.png"
  width="80%"
  caption="RAK7289V2/RAK7289CV2 Interfaces"
/>

##### Interface Description

| **Interface**              | **Description**                        | **Function**                                                                                                                                             |
| -------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **LoRa1 / LoRa2**          | LoRa Antenna Connectors                | N-Type connectors for external LoRa antennas. Required for LoRaWAN data transmission and reception.                                                      |
| **ETH (PoE)**              | Ethernet Port (RJ45, 10/100&nbsp;Mbps) | Provides network backhaul via Ethernet. **PoE (Power over Ethernet)** allows the gateway to receive both power and data through a single Ethernet cable. |
| **Additional Power Input** | Power Input                            | Accepts **12 V DC input**. <br />It is fully compatible with the **RAK Battery Plus**.                                                                   |
| **Reserved**               | Sealed Port (no function by default)   | Reserved for future use.                                                                                                                                 |
| **Console**                | USB Type-C Port                        | Used for serial console access during debugging and firmware flashing.                                                                                   |
| **Reset**                  | Reset Key                              | - **Short press**: Reboot the device.   <br />- **Long press (≥5 sec)**: Factory reset.                                                                  |
| **NanoSIM**                | NanoSIM Slot                           | Used for LTE connectivity. Required when using cellular backhaul. Included in all versions, even if LTE is not supported.                                |
| **TF Card**                | MicroSD (TF) Card Slot                 | Includes a **16 GB pre-installed SD card** used for log storage and configuration. <br />**Do not remove during operation** to avoid data loss.          |
| **LED Indicators**         | Status LEDs                            | - Power (PWR)   <br />- Ethernet (ETH)   <br />- LoRa1 & LoRa2   <br />- WLAN   <br />- LTE *(for LTE version)*   <br />                                 |

##### LED Indicators Details

<table>
    <thead><tr><th>LEDs</th><th>Status Indication Description</th></tr></thead>
    <tbody>
        <tr><td>LED 1 (PWR)</td><td>Power indicator: The LED is on when device power is on</td></tr>
        <tr><td rowSpan="4">LED 2 (ETH)</td></tr>
        <tr><td>ON: Link is up</td></tr>
        <tr><td>OFF: Link is down</td></tr>
        <tr><td>Flicker: Data transmitting and receiving</td></tr>
        <tr><td rowSpan="4">LED 3 (LoRa 1)</td></tr>
        <tr><td>ON: LoRa 1 is working</td></tr>
        <tr><td>OFF: LoRa 1 is not working</td></tr>
        <tr><td>Flicker: Indicate LoRa 1 Packet receiving and sending</td></tr>
        <tr><td rowSpan="3">LED 4 (WLAN)</td></tr>
        <tr><td>AP Mode:<ul><li>ON: The AP is up</li><li>Flicker: Data receiving and sending</li></ul></td></tr>
        <tr><td>STA Mode:<ul><li>Slow flicker (1&nbsp;Hz): Disconnected</li><li>ON: Connected</li><li>Flicker: Data receiving and sending</li></ul></td></tr>
        <tr><td rowSpan="3">LED 5 (LTE)</td></tr>
        <tr><td>Slow Flicker (1800&nbsp;ms bright / 200&nbsp;ms  dark): Network searching</td></tr>
        <tr><td>Slow flicker (200&nbsp;ms bright / 1800&nbsp;ms dark): Idle</td></tr>
        <tr><td rowSpan="4">LED 6 (LoRa 2 for 16 channel)</td></tr>
        <tr><td>ON: LoRa 2 is working</td></tr>
        <tr><td>OFF: LoRa 2 is not working</td></tr>
        <tr><td>Flicker: Indicate LoRa 2 Packet receiving and sending</td></tr>
 </tbody>
</table>


#### RF Specifications

##### LoRa Radio Specifications

<table>
    <thead><tr><th>Feature</th><th>Specifications</th></tr></thead>
    <tbody>
        <tr><td>Operating Frequency</td><td>EU868 / IN865 / US915 / AU915 / KR920 / AS923-1/2/3/4 / EU433 / CN470</td></tr>
        <tr><td>Transmit Power</td><td>27&nbsp;dBm (Max)</td></tr>
        <tr><td>Receiver Sensitivity</td><td>-141&nbsp;dBm (Min)@SF12</td></tr>
</tbody>
</table>



##### Wi-Fi Radio Specifications

<table>
    <thead><tr><th>Feature</th><th>Specifications</th></tr></thead>
    <tbody>
        <tr><td>Wireless Standard</td><td>IEEE 802.11b / g / n</td></tr>
        <tr><td>Operating Frequency</td><td>ISM band: 2.412~2.472&nbsp;GHz</td></tr>
        <tr><td>Operation Channels</td><td>2.4&nbsp;GHz: 1-13</td></tr>
        <tr><td rowSpan="11">Transmit Power (The max power maybe different depending on local regulations) - per chain</td><td>802.11b</td></tr>
        <tr><td>  19&nbsp;dBm @1&nbsp;Mbps</td></tr>
        <tr><td>  19&nbsp;dBm @11&nbsp;Mbps</td></tr>
        <tr><td>802.11g</td></tr>
        <tr><td>  18&nbsp;dBm @6&nbsp;Mbps</td></tr>
        <tr><td>  16&nbsp;dBm @54&nbsp;Mbps</td></tr>
        <tr><td>  802.11n (2.4&nbsp;GHz)</td></tr>
        <tr><td>  18&nbsp;dBm @MCS0 (HT20)</td></tr>
        <tr><td>  16&nbsp;dBm @MCS7 (HT20)</td></tr>
        <tr><td>  17&nbsp;dBm @MCS0 (HT40)</td></tr>
        <tr><td>  15&nbsp;dBm @MCS7 (HT40)</td></tr>
        <tr><td rowSpan="11">Receiver Sensitivity (Typical)</td><td>802.11b</td></tr>
        <tr><td>  -95&nbsp;dBm @1&nbsp;Mbps</td></tr>
        <tr><td>  -88&nbsp;dBm @11&nbsp;Mbps</td></tr>
        <tr><td>802.11g</td></tr>
        <tr><td>  -90&nbsp;dBm @6&nbsp;Mbps</td></tr>
        <tr><td>  -75&nbsp;dBm @54&nbsp;Mbps</td></tr>
        <tr><td>  802.11n (2.4&nbsp;GHz)</td></tr>
        <tr><td>  -89&nbsp;dBm @MCS0 (HT20)</td></tr>
        <tr><td>  -72&nbsp;dBm @MCS7 (HT20)</td></tr>
        <tr><td>  -86&nbsp;dBm @MCS0 (HT40)</td></tr>
        <tr><td> -68&nbsp;dBm @MCS7 (HT40)</td></tr>
 </tbody>
</table>


##### LTE Radio Specifications (Optional, Available with RAK7289CV2)

<table>
    <thead><tr><th>Feature</th><th>Specifications</th></tr></thead>
    <tbody>
    <tr><td rowSpan="3">EG95-E for EMEA Region (Europe, Middle East, and Africa)</td><td>LTE FDD: B1/B3/B7/B8/B20/B28A</td></tr>
    <tr><td>WCDMA: B1/B8</td></tr>
    <tr><td>GSM/EDGE: B3/B8</td></tr>
    <tr><td rowSpan="2">EG95-NA for North America Region</td><td>LTE FDD: B2/B4/B5/B12/B13</td></tr>
    <tr><td>WCDMA: B2/B4/B5</td></tr>
    <tr><td rowSpan="3">EC25-J for Japan Region</td><td>LTE FDD: B1 / B3 / B8 / B18 / B19 / B26</td></tr>
    <tr><td>LTE TDD: B41</td></tr>
    <tr><td>WCDMA: B1 / B6 / B8 /B19</td></tr>
    <tr><td rowSpan="4">EC25-AU for Brazil Region</td><td>LTE-FDD: B1 / B2 / B3 / B4 / B5 / B7 / B8 / B28</td></tr>
    <tr><td>LTE-TDD: B40</td></tr>
    <tr><td>WCDMA: B1 / B2 / B5 / B8</td></tr>
    <tr><td>GSM/EDGE: B2 / B3 / B5 / B8</td></tr>
</tbody>
</table>

#### Power Supply Options

The RAK7289V2/RAK7289CV2 supports the following power supply methods:

- **PoE (Power over Ethernet):**
   Via included PoE injector, supports IEEE 802.3af standard (input: 37–57&nbsp;V DC).

- **12&nbsp;V DC Input:**
   Through the waterproof power connector, accepts 12 V regulated DC from an external power supply.

  :::warning

  **Only use regulated 12&nbsp;V DC power sources.** Do not use solar chargers or non-certified adapters, as improper voltage may damage the device and void the warranty.

  :::

- **<a href="https://store.rakwireless.com/products/rak-battery-plus-rak9155?variant=42309251563718" target="_blank">RAK9155 Battery Plus</a> (Optional):**
   Provides regulated 12&nbsp;V DC output and is designed for off-grid or solar-powered deployments. Purchased separately.

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

<table class="q-table"><thead><tr><th>Part Number</th> <th >8 Channel SX1303</th> <th >16 Channel SX1303</th> <th >Cat4 Cellular</th> <th >GPS</th> <th >Wi-Fi</th> <th >Dying gasp</th></tr></thead> <tbody><tr><td>RAK7289CV2-XYZ</td> <td >√</td> <td ></td> <td >√</td> <td >√</td> <td >√</td> <td ></td></tr> <tr><td>RAK7289CV2-XYZ</td> <td ></td> <td >√</td> <td >√</td> <td >√</td> <td >√</td> <td ></td></tr> <tr><td>RAK7289CV2-XYZ</td> <td >√</td> <td ></td> <td >√</td> <td >√</td> <td >√</td> <td >√</td></tr> <tr><td>RAK7289CV2-XYZ</td> <td ></td> <td >√</td> <td >√</td> <td >√</td> <td >√</td> <td >√</td></tr> <tr><td>RAK7289V2-XYZ</td> <td >√</td> <td ></td> <td ></td> <td >√</td> <td >√</td> <td ></td></tr> <tr><td>RAK7289V2-XYZ</td> <td ></td> <td >√</td> <td ></td> <td >√</td> <td >√</td> <td ></td></tr> <tr><td>RAK7289V2-XYZ</td> <td >√</td> <td ></td> <td ></td> <td >√</td> <td >√</td> <td >√</td></tr> <tr><td>RAK7289V2-XYZ</td> <td ></td> <td >√</td> <td ></td> <td >√</td> <td >√</td> <td >√</td></tr></tbody></table>



## Certification

<RkCertificationIcons certifications={[
  {
'ce': 'https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289_RAK7289V2_CE_Certification.pdf'
},
{
'fcc': 'https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289_FCC_Certification.pdf'
},
{
'ised': 'https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289_ISED_Certification.zip'
},
{
'jrl': 'https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289CV2_RAK7289V2_JRL_certification.pdf'
},
{
'jtbl': 'https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289CV2_JTBL_Certification.pdf'
},
{
'kc': 'https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289_RAK7289C_RAK7289V2_RAK7289CV2_KC_Certification.pdf'
},
{
'ma': 'https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289V2_MA_Certification.pdf'
},
{
'nbtc': 'https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289CV2_NBTC_Certification.pdf'
},
{
'reach': 'https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289C_RAK7289_RAK7289CV2_RAK7289V2_REACH_Report.pdf'
},
{
'red': 'https://downloads.rakwireless.com/LoRa/WisGate/Certification/WisGate_RED_Verification.pdf'
},
{
'rohs': 'https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289C_RAK7289_RAK7289CV2_RAK7289V2_RoHS_Report.pdf'
},
{
'rcm': 'https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289_RAK7289V2_RCM_Certification.pdf'
},
{
'rsm': 'https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289C_RAK7289CV2_RSM_Certification.pdf'
},
{
'tdra': 'https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289CV2_TDRA_Certification.pdf'
},
{
'ukca': 'https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289C_RAK7289CV2_UKCA_Certification.pdf'
},
{
'wpc': 'https://downloads.rakwireless.com/LoRa/RAK7289V2/Certification/RAK7289CV2_WPC_Certification.pdf'
},
]} />



<RkBottomNav/>