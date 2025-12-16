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

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK7285/RAK7285C WisGate Edge Ultra Datasheet

## Overview

### Descriptions

**RAK7285 WisGate Edge Ultra** is the latest version of the RAK WisGate Edge series, designed to overcome the limitations of half-duplex communication. It's tailored to meet the demands of high-density network deployments, particularly for smart city infrastructure, metering applications, and other scenarios requiring reliable two-way communication at scale.

This gateway supports up to 8 LoRa channels in full-duplex (a 16-channel variant is coming soon), with multi-backhaul options including Ethernet, Wi-Fi, and Cellular connectivity. Its integrated advanced cavity diplexers not only provide exceptional out-of-band interference suppression but also provide lightning protection for the LoRa antennas, ensuring uninterrupted and secure full-duplex communication.

In addition, RAK7285 operates under <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/" target="_blank">WisGateOS 2</a>, which is built on the latest OpenWrt kernel. The OS Web UI features a new design and supports multiple extension installations, enabling remote management using <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/overview/" target="_blank">WisDM</a> for personalized gateway customization.

### Features

#### Hardware

- IP67 industrial-grade enclosure with cable glands
- PoE (802.3at) + Surge Protection
- 8 LoRa channels in full-duplex (16 channels variant is coming soon)
- Built-in cavity diplexers for out-of-band interference suspension
- Backhaul: Wi-Fi, Ethernet, and LTE (available with RAK7285C)
- GPS
- Supports 9~36&nbsp;V<sub>DC</sub> and RAK Solar Battery Kit
- External antennas for GPS and LoRa
- Dying Gasp (optional)


#### Software

- <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/" target="_blank">WisGateOS 2</a>
- **WisGateOS 2 Extensions**: Adds support for features such as OpenVPN, WireGuard VPN, and more. Use the appropriate installation guide based on your WisGateOS 2 version:
    - <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/" target="_blank">For WisGateOS 2 version 2.2.x or later</a>
    - <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/" target="_blank">For WisGateOS 2 versions 2.0.x and 2.1.x</a>
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

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7285/datasheet/1.rak7285-block-diagram.png"
  width="100%"
  caption="RAK7285 Block Diagram"
/>

:::tip NOTE
+ The LTE module (RAK8213) is optional. Only RAK7285C integrates the LTE module.
+ The LoRa module 2 is optional. Only 16-channel gateway is available.
:::

#### Main Specifications

<table>
    <thead>
        <tr>
             <th>Feature</th><th>Specifications</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Computing</td>
            <td>MT7628, DDR2 RAM 128&nbsp;MB</td>
        </tr>
        <tr>
            <td>Frequency</td>
            <td><ul><li>US915</li><li>AU915</li></ul></td>
        </tr>
        <tr>
            <td rowspan="5">Wi-Fi Feature</td>
            <td>Frequency: 2.4&nbsp;GHz (802.11b / g / n)</td>
        </tr>
        <tr>
            <td>2x2 MIMO</td>
        </tr>
        <tr>
            <td>RX Sensitivity:-95&nbsp;dBm (Min)</td>
        </tr>
        <tr>
            <td>TX Power: 20&nbsp;dBm (Max)</td>
        </tr>
        <tr>
            <td>Operation channels: 2.4&nbsp;GHz, 1-13</td>
        </tr>
        <tr>
            <td rowspan="5">LoRa Feature</td>
            <td>SX1303 On Board</td>
        </tr>
        <tr>
            <td>8 LoRa channels in full-duplex (16 channels variant is coming soon)</td>
        </tr>
        <tr>
            <td>RX Sensitivity:-139&nbsp;dBm (Min)</td>
        </tr>
        <tr>
            <td>TX Power: 30&nbsp;dBm (Max)</td>
        </tr>
        <tr>
            <td>Listen Before Talk</td>
        </tr>
        <tr>
            <td rowspan="7">Cellular Feature (available with RAK7285C)</td>
            <td><b>Nano SIM Card: 12.30&nbsp;mm x 8.80&nbsp;mm x 0.67&nbsp;mm</b><br />Supports Quectel EG95-E / EG95-NA / EC25-AU (IoT / M2M -optimized LTE Cat 4 Module)</td>
        </tr>
        <tr>
            <td><b>EG95-E for EMEA Region (Europe, Middle East and Africa)</b></td>
        </tr>
        <tr>
            <td>LTE FDD: B1 / B3 / B7 / B8 / B20 / B28A<br />WCDMA: B1 / B8<br />GSM/EDGE: B3 / B8</td>
        </tr>
        <tr>
            <td><b>EG95-NA for North America Region</b></td>
        </tr>
        <tr>
            <td>LTE FDD: B2 / B4 / B5 / B12 / B13<br />WCDMA: B2 / B4 / B5</td>
        </tr>
        <tr>
            <td><b>EC25-AU for Latin America, Australia, and New Zealand Region</b></td>
        </tr>
        <tr>
            <td>LTE-FDD: B1 / B2 / B3 / B4 / B5 / B7 / B8 / B28<br />LTE-TDD: B40<br />WCDMA: B1/B2/B5/B8<br />GSM/EDGE: B2 / B3 / B5 / B8</td>
        </tr>
        <tr>
            <td>Power Supply</td>
            <td>PoE (IEEE 802.3at): 42\~57&nbsp;VDC<br />9~36&nbsp;VDC<br />Compatible with RAK Battery Plus</td>
        </tr>
        <tr>
            <td>ETH</td>
            <td>RJ45 (10/100 M)</td>
        </tr>
        <tr>
            <td rowspan="4">Antenna</td>
            <td>LoRa: N-Type connector (one for the 8-channel gateway and two for the 16-channel gateway)</td>
        </tr>
        <tr>
            <td>GPS: One N-Type connector</td>
        </tr>
        <tr>
            <td>Wi-Fi: Two N-Type connectors</td>
        </tr>
        <tr>
            <td>LTE: Two N-Type connectors( only for RAK7285C)</td>
        </tr>
        <tr>
            <td rowspan="2">Diplexer</td>
            <td><b>AU915:</b><br/>Frequency:<br/> - Rx: 915 ~ 920&nbsp;MHz<br/> - Tx: 923 ~ 928&nbsp;MHz<br/>Insertion loss:<br/> - Rx: 2.6 (Typical) / 4.0 (Maximum)  <br/>- Tx: 2.6 (Typical) / 3.8 (Maximum)<br/>Isolation between Rx and Tx: &gt; 80&nbsp;dB<br/>Return loss: &lt;-18&nbsp;dB<br/>Impedance: 50&nbsp;Ω</td>
        </tr>
        <tr>
            <td><b>US915:</b><br/>Frequency: <br/>- Rx: 902 ~ 915&nbsp;MHz<br/>- Tx: 923 ~ 928&nbsp;MHz<br/>Insertion loss:<br/>- Rx: 1.3 (Typical) / 1.6 (Maximum) <br/>- Tx: 1.8 (Typical) / 2.0 (Maximum)<br/>Isolation between Rx and Tx: &gt; 90&nbsp;dB<br/>Return loss: &lt;-18&nbsp;dB<br/>Impedance: 50&nbsp;Ω</td>
        </tr>
        <tr>
            <td>Ingress Protection</td>
            <td>IP67</td>
        </tr>
        <tr>
            <td>Enclosure Material</td>
            <td>Aluminum</td>
        </tr>
        <tr>
            <td>Dimensions</td>
            <td>310&nbsp;mm x 290&nbsp;mm x 146&nbsp;mm</td>
        </tr>
        <tr>
            <td>Operating Temperature</td>
            <td>-30˚&nbsp;C to +55˚&nbsp;C</td>
        </tr>
        <tr>
            <td>Storage Temperature</td>
            <td>-40˚&nbsp;C to ﹢85˚&nbsp;C</td>
        </tr>
        <tr>
            <td>Operating Humidity</td>
            <td>0~95%&nbsp;RH non-condensing</td>
        </tr>
        <tr>
            <td>Storage Humidity</td>
            <td>0~95%&nbsp;RH non-condensing</td>
        </tr>
        <tr>
            <td>Installation Method</td>
            <td>Pole or wall mounting</td>
        </tr>
</tbody>
</table>



### Hardware

The hardware specification covers the interfacing of the RAK7285/RAK7285C and its corresponding functionalities. It also presents the parameters and the standard values of the board.

#### Interfaces

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7285/datasheet/2.interfaces1.png"
  width="100%"
  caption="RAK7285/RAK7285C Interfaces"
/>

:::tip NOTE
+ The SD card in the SD card slot must not be ejected. Doing so might affect the device's performance, as various logs and data are stored on it.
+ The SIM card slot of the cellular versions is not hot-swappable. Ensure the gateway is switched off before inserting or ejecting the SIM card.
+ The available antenna interfaces vary between variants. For example, two N-type LTE interfaces are available on the RAK7285C, but not on the RAK7285.
:::

##### Reset Key Functions

The functions of the Reset key are as follows:

- **Short press**: Restart the gateway.
- **Long press** (5&nbsp;seconds or more): Restore factory settings.

##### LED Indicators

The status of the LEDs is described below. Refer to the LED printing on the main board.

<table>
    <thead>
        <tr><th>LEDs</th><th>Status Indication Description</th></tr>
    </thead>
    <tbody>
        <tr><td>LED 1 (PWR)</td><td>Power indicator: The LED is on when device power is on.</td></tr>
        <tr><td rowSpan="3">LED 2 (ETH)</td><td>ON: Linkup</td></tr>
        <tr><td>OFF: Linkdown</td></tr>
        <tr><td>Flicker: Data transmitting and receiving</td></tr>
        <tr><td rowSpan="3">LED 3 (LoRa 1)</td><td>ON: LoRa 1 is working</td></tr>
        <tr><td>OFF: LoRa 1 is not working</td></tr>
        <tr><td>Flicker: Indicate LoRa 1 Packet receiving and sending</td></tr>
        <tr><td rowSpan="7">LED 4 (WLAN)</td><td>AP Mode: </td></tr>
        <tr><td>&nbsp;&nbsp;&nbsp;ON: The AP is up</td></tr>
        <tr><td>&nbsp;&nbsp;&nbsp;Flicker: Data receiving and sending</td></tr>
        <tr><td>STA Mode: </td></tr>
        <tr><td>&nbsp;&nbsp;&nbsp;Slow flicker (1&nbsp;Hz): Disconnected</td></tr>
        <tr><td>&nbsp;&nbsp;&nbsp;ON: Connected</td></tr>
        <tr><td>&nbsp;&nbsp;&nbsp;Flicker: Data receiving and sending</td></tr>
        <tr><td rowSpan="4">LED 5 (LTE)</td><td>Slow Flicker (200&nbsp;ms Bright / 1800&nbsp;ms Dark): Network searching</td></tr>
        <tr><td>Slow flicker (200&nbsp;ms Dark / 1800&nbsp;ms Bright): Idle</td></tr>
        <tr><td>Fast flicker (125&nbsp;ms Bright / 125&nbsp;ms Dark): Ongoing data transfer</td></tr>
        <tr><td>ON: Voice is working</td></tr>
        <tr><td rowSpan="3">LED 6 (LoRa 2 for 16 channel)</td><td>ON: LoRa 2 is working</td></tr>
        <tr><td>OFF: LoRa 2 is not working</td></tr>
        <tr><td>Flicker: Indicate LoRa 2 Packet receiving and sending</td></tr>
    </tbody>
</table>



#### RF Specifications

##### Wi-Fi Radio Specifications

<table>
    <thead><tr><th>Feature</th><th>Specifications</th></tr></thead>
    <tbody>
        <tr>
            <td>Wireless Standard</td>
            <td>IEEE 802.11b / g / n</td>
        </tr>
        <tr>
            <td>Operating Frequency</td>
            <td>ISM band: 2.412 ~ 2.472&nbsp;GHz</td>
        </tr>
        <tr>
            <td>Operation Channels</td>
            <td>2.4&nbsp;GHz: 1-13</td>
        </tr>
        <tr>
            <td rowspan="11">Transmit Power<br />(The max power maybe different<br />depending on local regulations): per chain</td>
            <td>802.11b</td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;19&nbsp;dBm @1&nbsp;Mbps</td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;19&nbsp;dBm @11&nbsp;Mbps</td>
        </tr>
        <tr>
            <td>802.11g</td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;18&nbsp;dBm @6&nbsp;Mbps</td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;16 dBm @54&nbsp;Mbps</td>
        </tr>
        <tr>
            <td>802.11n (2.4&nbsp;GHz)</td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;18&nbsp;dBm @MCS0 (HT20)</td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;16&nbsp;dBm @MCS7 (HT20)</td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;17&nbsp;dBm @MCS0 (HT40) </td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;15&nbsp;dBm @MCS7 (HT40)</td>
        </tr>
        <tr>
            <td rowspan="11">Receiver Sensitivity<br />(Typical)</td>
            <td>802.11b</td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;-95&nbsp;dBm @1&nbsp;Mbps</td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;-88&nbsp;dBm @11&nbsp;Mbps</td>
        </tr>
        <tr>
            <td>802.11g</td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;-90&nbsp;dBm @6&nbsp;Mbps</td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;-75&nbsp;dBm @54&nbsp;Mbps</td>
        </tr>
        <tr>
            <td>802.11n (2.4&nbsp;GHz)</td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;-89&nbsp;dBm @MCS0 (HT20)</td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;-72&nbsp;dBm @MCS7 (HT20)</td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;-86&nbsp;dBm @MCS0 (HT40)</td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;-68&nbsp;dBm @MCS7 (HT40)</td>
        </tr>
    </tbody>
</table>



##### LoRa Radio Specifications

<table>
    <thead>
        <tr>
            <th>Feature</th>
            <th>Specifications</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Operating Frequency</td>
            <td>US915/AU915</td>
        </tr>
        <tr>
            <td>Transmit Power</td>
            <td>30&nbsp;dBm (Max)</td>
        </tr>
        <tr>
            <td>Receiver Sensitivity</td>
            <td>-139&nbsp;dBm (Min)</td>
        </tr>
</tbody>
</table>


#### Mechanical Characteristics

| Parameter          | Value                                                                             |
|--------------------|-----------------------------------------------------------------------------------|
| Dimensions         | 310&nbsp;mm x 290&nbsp;mm x 146&nbsp;mm Gateway only (no antenna, no bracket) |
| Ingress protection | IP67                                                                              |

#### Environmental Requirements

<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Value</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Operating Conditions</td>
             <td>Operating Temperature:-30˚&nbsp;C to ﹢55˚&nbsp;C<br />Storage Temperature:-40˚&nbsp;C to ﹢85˚&nbsp;C<br />Operating Humidity: 0 ~ 95%&nbsp;RH non-condensing<br />Storage Humidity: 0 ~ 95%&nbsp;RH non-condensing</td>
        </tr>
    </tbody>
</table>



### Software

<table>
    <thead>
        <tr>
            <th>LoRa</th>
            <th>Network</th>
            <th>Management</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Gateway OTA management</td>
            <td>Wi-Fi Client mode</td>
            <td>WisDM</td>
        </tr>
        <tr>
            <td>LoRa Package Forward (Packet Forwarder, Basics Station)</td>
            <td>LTE APN Setup</td>
            <td>SSH2, NTP</td>
        </tr>
        <tr>
            <td>Frequency Band Setup</td>
            <td>Support 802.1q</td>
            <td>Firmware Update</td>
        </tr>
        <tr>
            <td>Server Address and Port Setup</td>
            <td>Uplink backup</td>
            <td>LoRa Packet Forwarder</td>
        </tr>
        <tr>
            <td>TX Power Setup</td>
            <td>Firewall</td>
            <td>Built-in Network Server</td>
        </tr>
        <tr>
            <td>Data Logger</td>
            <td>DHCP Server/Client</td>
            <td>MQTT Bridge</td>
        </tr>
        <tr>
            <td>Location Setup</td>
            <td>Wi-Fi AP mode</td>
            <td>OpenVPN, Ping Watch Dog</td>
        </tr>
        <tr>
         <td>Statistic</td>
            <td> </td>
            <td>WEB UI</td>
        </tr>
        <tr>
            <td>Supports Class A, B, and C</td>
            <td> </td>
            <td> </td>
        </tr>
        <tr>
        <td>Automatic Data Recovery</td>
            <td> </td>
            <td> </td>
        </tr>
    </tbody>
</table>


### Firmware

The firmware is based on OpenWRT. It features a web UI that enables easy configuration and management of the device, as well as the option for SSH2 management. The WisGateOS V2 supports the installation of extensions (OpenVPN, WireGuard, Custom Logo, etc.).

Detailed information about the extensions can be found on the <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/overview/#supported-extensions" target="_blank">WisGateOS 2 Extensions</a>.




|                Model                | Firmware Version |                                                         Source                                                          |
|:-----------------------------------:|:----------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| RAK7285/RAK7285C WisGate Edge Ultra |     v2.2.13      | <a href="https://downloads.rakwireless.com/LoRa/WisGateOS2/WisGateOS2_Latest_Firmware.zip" target="_blank">Download</a> |


## Models/Bundles

<table class="q-table">
    <thead>
        <tr>
            <th>Part Number</th>
            <th style={{ textAlign: 'center' }}>8 Channel SX1303</th>
            <th style={{ textAlign: 'center' }}>16 Channel SX1303</th>
            <th style={{ textAlign: 'center' }}>Cat4 Cellular</th>
            <th style={{ textAlign: 'center' }}>GPS</th>
            <th style={{ textAlign: 'center' }}>Wi-Fi</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>RAK7285C-XYZ</td>
            <td style={{ textAlign: 'center' }}>√</td>
            <td style={{ textAlign: 'center' }}></td>
            <td style={{ textAlign: 'center' }}>√</td>
            <td style={{ textAlign: 'center' }}>√</td>
            <td style={{ textAlign: 'center' }}>√</td>
        </tr>
        <tr>
            <td>RAK7285C-XYZ</td>
            <td style={{ textAlign: 'center' }}></td>
            <td style={{ textAlign: 'center' }}>√</td>
            <td style={{ textAlign: 'center' }}>√</td>
            <td style={{ textAlign: 'center' }}>√</td>
            <td style={{ textAlign: 'center' }}>√</td>
        </tr>
        <tr>
            <td>RAK7285-XYZ</td>
            <td style={{ textAlign: 'center' }}>√</td>
            <td style={{ textAlign: 'center' }}></td>
            <td style={{ textAlign: 'center' }}></td>
            <td style={{ textAlign: 'center' }}>√</td>
            <td style={{ textAlign: 'center' }}>√</td>
        </tr>
        <tr>
            <td>RAK7285-XYZ</td>
            <td style={{ textAlign: 'center' }}></td>
            <td style={{ textAlign: 'center' }}>√</td>
            <td style={{ textAlign: 'center' }}></td>
            <td style={{ textAlign: 'center' }}>√</td>
            <td style={{ textAlign: 'center' }}>√</td>
        </tr>
    </tbody>
</table>

## Certification

<RkCertificationIcons certifications={[
    {
        'anatel': 'https://downloads.rakwireless.com/LoRa/RAK7285/Certification/RAK7285_RAK7285C_ANATEL_Certification.pdf',
    },
    
]} />

<RkBottomNav/>


