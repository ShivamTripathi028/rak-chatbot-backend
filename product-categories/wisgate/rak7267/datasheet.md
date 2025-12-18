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

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'


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
- Supports 9\~36&nbsp;V<sub>DC</sub> power supply and RAK Solar Battery Kit
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

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7267/datasheet/block_diagram.png"
  width="100%"
  caption="RAK7267 Block Diagram"
/>


#### Main Specifications

<table>
    <thead>
        <tr>
            <th>Feature</th>
            <th>Specifications</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Computing</td>
            <td>MT7628, DDR2 RAM 128&nbsp;MB</td>
        </tr>
        <tr>
            <td rowSpan="5">LoRa Feature</td>
            <td>SX1303 On Board</td>
        </tr>
        <tr>
            <td>8 Channels</td>
        </tr>
        <tr>
            <td>Frequency: EU868/IN865/RU864/US915/AU915/KR920/AS923-1/2/3/4</td>
        </tr>
        <tr>
            <td>Listen Before Talk</td>
        </tr>
        <tr>
            <td>LoRa Radio: Refer to the <a href="#lora-radio-specifications">LoRa Radio Specifications</a>  section for detailed information.</td>
        </tr>
         <tr>
            <td rowSpan="4">Wi-Fi Feature</td>
            <td>Frequency: 2.4&nbsp;GHz (802.11 b / g / n)</td>
        </tr>
         <tr>
            <td>Channels: 1-13</td>
        </tr>
        <tr>
            <td>2x2 MIMO</td>
        </tr>
        <tr>
            <td>Wi-Fi Radio: Refer to the <a href="#wi-fi-radio-specifications">Wi-Fi Radio Specifications</a>  section for detailed information.</td>
        </tr>
        <tr>
            <td>Cellular Feature</td>
            <td><b>Nano SIM Card:</b> 12&nbsp;mm x 9&nbsp;mm x 0.67&nbsp;mm<br/>Supports Quectel EG915U-EU / EG915U-LA / EG915Q-NA (IoT / M2M -LTE Cat 1 module)<br/>LTE Radio: Refer to the <a href="#lte-radio-specifications">LTE Radio Specifications</a> section for detailed information.</td>
        </tr>
        <tr>
            <td>Power Supply</td>
            <td>9\~36&nbsp;V<sub>DC</sub><br/>Compatible with RAK Solar Battery Kit</td>
        </tr>
        <tr>
            <td rowSpan="9">Antenna</td>
            <td>LoRa / LTE / Wi-Fi / GPS: Internal antenna</td>
        </tr>
        <tr>
            <td><b>LoRa</b></td>
        </tr>
        <tr>
            <td>Frequency Range: 863&nbsp;MHz\~928&nbsp;MHz<br/>Peak Gain: 2.5&nbsp;dBi<br/>VSWR: ≤ 1.5<br/>Efficiency: &gt;85%<br/>Polarization: Vertical</td>
        </tr>
         <tr>
            <td><b>LTE</b></td>
        </tr>
        <tr>
            <td>Frequency Range: 700&nbsp;MHz\~960&nbsp;MHz/1710&nbsp;MHz\~21700&nbsp;MHz<br/>Peak Gain: 3&nbsp;dBi<br/>VSWR: ≤ 3<br/>Efficiency: &gt;60%<br/>Polarization: Vertical</td>
        </tr>
        <tr>
            <td><b>Wi-Fi</b></td>
        </tr>
        <tr>
            <td>Frequency Range: 2400&nbsp;MHz\~2500&nbsp;MHz <br/>Peak Gain: 2&nbsp;dBi<br/>VSWR: ≤ 2.5<br/>Efficiency: &gt;75%<br/>Polarization: Vertical</td>
        </tr>
         <tr>
            <td><b>GPS</b></td>
        </tr>
        <tr>
            <td>Frequency Range: 1575&nbsp;MHz\~1602&nbsp;MHz <br/>Peak Gain: 28&nbsp;dBi<br/>VSWR: &lt;2<br/>Polarization: RHCP</td>
        </tr>
        <tr>
            <td>Ingress Protection</td>
            <td>IP67</td>
        </tr>
        <tr>
            <td>Weight</td>
            <td>0.66&nbsp;kg</td>
        </tr>
        <tr>
            <td>Dimension</td>
            <td>180&nbsp;mm x 130&nbsp;mm x 60&nbsp;mm</td>
        </tr>
        <tr>
            <td>Enclosure Material</td>
            <td>UV stabilized ABS</td>
        </tr>
        <tr>
            <td>Operating Temperature</td>
            <td>﹣30˚&nbsp;C to ﹢55˚&nbsp;C</td>
        </tr>
        <tr>
            <td>Storage Temperature</td>
            <td>﹣40˚&nbsp;C to ﹢85˚&nbsp;C</td>
        </tr>
        <tr>
            <td>Operating Humidity</td>
            <td>0\~95%&nbsp;RH non-condensing</td>
        </tr>
        <tr>
            <td>Storage Humidity</td>
            <td>0\~95%&nbsp;RH non-condensing</td>
        </tr>
        <tr>
            <td>Installation Method</td>
            <td>Pole mounting (other options available per request)</td>
        </tr>
    </tbody>
</table>



### Hardware

This section provides an overview of the hardware specifications for the RAK7267 gateway, including its interfaces, core functions, and key board parameters.

#### Interfaces

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7267/datasheet/3.interfaces.png"
  width="60%"
  caption="RAK7267 Interfaces"
/>

##### Interface Description

| Interfaces     | Description           | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **DC 9-36 V**  | Power Input           | Provides power supply for the gateway.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Console**    | Type-C USB            | Used for debugging.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Reset**      | Reset Key             | **Short press**: Reboot the gateway. <br />**Long press** (5&nbsp;sec and above): Restore factory settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **NanoSIM**    | NanoSIM Card Slot     | Slot for a NanoSIM card, enabling cellular connectivity.<br /><div style={{ borderLeft: '6px solid #f4b400', backgroundColor: '#fff8e1', padding: '12px', borderRadius: '6px', color: '#5f370e', fontFamily: 'sans-serif' }}><strong style={{ display: 'inline-flex', alignItems: 'center', fontSize: '16px' }}>⚠️ WARNING</strong><br/><span style={{ display: 'block', marginTop: '4px' }}> The SIM card slot of the cellular versions is not hot-swappable. Make sure the gateway is switched off before inserting or ejecting the SIM card.</span></div>                                                                                                |
| **TF Card**    | SD Card Slot          | A 16 GB SD card is pre-installed in the gateway for data logging, system configurations, and other use cases that require local storage.<br /><div style={{ borderLeft: '6px solid #f4b400', backgroundColor: '#fff8e1', padding: '12px', borderRadius: '6px', color: '#5f370e', fontFamily: 'sans-serif' }}><strong style={{ display: 'inline-flex', alignItems: 'center', fontSize: '16px' }}>⚠️ WARNING</strong> <br /> <span style={{ display: 'block', marginTop: '4px' }}><strong>Do not</strong> eject the SD card located in the SD card slot during installation, as it stores logs and data essential for the device's performance. </span></div> |
| **Ground Pad** | Grounding Terminal    | Provides an earth grounding point for surge protection and EMI shielding. It is recommended to connect this to a reliable ground during installation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **LEDs**       | Status Indicator LEDs | PWR<br />LoRa<br />WLAN<br />LTE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |



##### LED Indicator Details

The status of the LEDs is described below. Refer to the LED printing on the main board.

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
            <td>Disconnected from Wi-Fi network</td>
        </tr>
        <tr>
            <td>On</td>
            <td>Connected to Wi-Fi network</td>
        </tr>
        <tr>
            <td>Flashing</td>
            <td>Data transmitting or receiving</td>
        </tr>
        <tr>
            <td rowspan="3">LTE</td>
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
    </tbody>
</table>



#### RF Specifications

##### LoRa Radio Specifications

<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Specifications</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Operating Frequency</td>
            <td><ul><li>EU868</li><li>IN865</li><li>RU864</li><li>US915</li><li>AU915</li><li>KR920</li><li>AS923-1/2/3/4</li></ul></td>
        </tr>
        <tr>
            <td>Transmit Power</td>
            <td>27&nbsp;dBm (Max)</td>
        </tr>
        <tr>
            <td>Receiver Sensitivity</td>
            <td>-140&nbsp;dBm (Min)</td>
        </tr>
    </tbody>
</table>



##### Wi-Fi Radio Specifications

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
            <td>IEEE 802.11 b / g / n</td>
        </tr>
        <tr>
            <td>Frequency</td>
            <td>ISM band: 2.412\~2.472&nbsp;GHz</td>
        </tr>
        <tr>
            <td>Channels</td>
            <td>1-13</td>
        </tr>
        <tr>
            <td rowSpan="11">Transmit Power (The max power maybe different depending on local regulations) - per chain</td>
            <td>**802.11b**</td>
        </tr>
        <tr>
            <td>  19&nbsp;dBm @1&nbsp;Mbps</td>
        </tr>
        <tr>
            <td>  19&nbsp;dBm @11&nbsp;Mbps</td>
        </tr>
        <tr>
            <td>**802.11g**</td>
        </tr>
        <tr>
            <td>  18&nbsp;dBm @6&nbsp;Mbps</td>
        </tr>
        <tr>
            <td>  16&nbsp;dBm @54&nbsp;Mbps</td>
        </tr>
        <tr>
            <td>  **802.11n (2.4&nbsp;GHz)**</td>
        </tr>
        <tr>
            <td>  18&nbsp;dBm @MCS0 (HT20)</td>
        </tr>
        <tr>
            <td>  16&nbsp;dBm @MCS7 (HT20)</td>
        </tr>
        <tr>
            <td>  17&nbsp;dBm @MCS0 (HT40)</td>
        </tr>
        <tr>
            <td>  15&nbsp;dBm @MCS7 (HT40)</td>
        </tr>
        <tr>
            <td rowSpan="11">Receiver Sensitivity (Typical)</td>
            <td>**802.11b**</td>
        </tr>
        <tr>
            <td>﹣95&nbsp;dBm @1&nbsp;Mbps</td>
        </tr>
        <tr>
            <td>﹣88&nbsp;dBm @11&nbsp;Mbps</td>
        </tr>
        <tr>
            <td>**802.11g**</td>
        </tr>
        <tr>
            <td>﹣90&nbsp;dBm @6&nbsp;Mbps</td>
        </tr>
        <tr>
            <td>﹣75&nbsp;dBm @54&nbsp;Mbps</td>
        </tr>
        <tr>
            <td>  **802.11n (2.4&nbsp;GHz)**</td>
        </tr>
        <tr>
            <td>﹣89&nbsp;dBm @MCS0 (HT20)</td>
        </tr>
        <tr>
            <td>﹣72&nbsp;dBm @MCS7 (HT20)</td>
        </tr>
        <tr>
            <td>﹣86&nbsp;dBm @MCS0 (HT40)</td>
        </tr>
        <tr>
            <td>﹣68&nbsp;dBm @MCS7 (HT40)</td>
        </tr>
    </tbody>
</table>



##### LTE Radio Specifications

<table>
  <thead>
    <tr>
      <th>Module / Region</th>
      <th>Supported Bands</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowSpan="2">EG915U-EU for EMEA/Brazil/Australia/New Zealand Region</td>
      <td>LTE FDD: B1 / B3 / B5 / B7 / B8 / B20 / B28</td>
    </tr>
    <tr>
      <td>GSM: B2 / B3 / B5 / B8</td>
    </tr>
    <tr>
      <td rowSpan="2">EG915U-LA for Latin America Region</td>
      <td>LTE FDD: B2 / B3 / B4 / B5 / B7 / B8 / B28 / B66</td>
    </tr>
    <tr>
      <td>GSM: B2 / B3 / B5 / B8</td>
    </tr>
    <tr>
      <td>EG915Q-NA for North America Region</td>
      <td>LTE FDD: B2 / B4 / B5 / B12 / B13 / B66 / B71</td>
    </tr>
  </tbody>
</table>

#### Electrical Characteristics

The RAK7267 WisGate Soho Pro supports multiple power input methods. Choose the option that best fits your deployment scenario.

- **DC Adapter + Cable**<br/>
  Recommended for indoor use. Use the provided power adapter and cable to supply power to the gateway.

- **Custom DC Power (9~36&nbsp;V<sub>DC</sub>)**<br/> 
  Suitable for industrial or flexible power environments. Use the DC cable to connect an external DC power source within the 9~36&nbsp;V<sub>DC</sub> range.

- **RAK9155 Battery Plus System**<br/> 
  Recommended for outdoor installations. Use the dedicated power cable designed for RAK9155 Battery Plus to connect and supply power to the gateway.

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
            <td>LoRa package forward (packet forwarder, Basics Station)</td>
            <td>LTE APN Setup</td>
            <td>SSH2, NTP</td>
        </tr>
        <tr>
            <td>Frequency Band Setup</td>
            <td>Support 802.1q</td>
            <td>Firmware update</td>
        </tr>
        <tr>
            <td>Country Code setup</td>
            <td>Uplink backup</td>
            <td>LoRa Packet Forwarder</td>
        </tr>
        <tr>
            <td>Server Address and Port Setup</td>
            <td>Firewall</td>
            <td>Built-in Network Server</td>
        </tr>
        <tr>
            <td>TX Power Setup</td>
            <td>DHCP Server/Client</td>
            <td>MQTT Bridge</td>
        </tr>
        <tr>
            <td>Data logger</td>
            <td>Wi-Fi AP mode</td>
            <td>OpenVPN, Ping Watch Dog</td>
        </tr>
        <tr>
            <td>Location setup</td>
            <td> </td>
            <td>WEB UI</td>
        </tr>
        <tr>
            <td>Statistic</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Supports class A, B, C</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Server address and Port setup</td>
            <td> </td>
            <td> </td>
        </tr>
</tbody>
</table>

### Firmware


|          Model           |                                                         Source                                                          |
|:------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| RAK7267 WisGate Soho Pro | <a href="https://downloads.rakwireless.com/LoRa/WisGateOS2/WisGateOS2_Latest_Firmware.zip" target="_blank">Download</a> |

## Models/Bundles

<table class="q-table">
    <thead>
        <tr>
            <th>Part Number</th>
            <th style={{ textAlign: 'center' }}>8 Channel SX1303</th>
            <th style={{ textAlign: 'center' }}>Cat1 Cellular</th>
            <th style={{ textAlign: 'center' }}>GPS</th>
            <th style={{ textAlign: 'center' }}>Wi-Fi</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>RAK7267-XYZ</td>
            <td style={{ textAlign: 'center' }}>√</td>
            <td style={{ textAlign: 'center' }}>√</td>
            <td style={{ textAlign: 'center' }}>√</td>
            <td style={{ textAlign: 'center' }}>√</td>
        </tr>
    </tbody>
</table>


## Certification


<RkCertificationIcons certifications={[
    {
        'anatel': 'https://downloads.rakwireless.com/LoRa/RAK7267/Certification/RAK7267_ANATEL_Certification.pdf',
    },
    {
        'ce': 'https://downloads.rakwireless.com/LoRa/RAK7267/Certification/RAK7267_CE_Certification.pdf',
    },
    {
        'fcc': 'https://downloads.rakwireless.com/LoRa/RAK7267/Certification/RAK7267_FCC_Certification.pdf',
    },
    {
        'ised': 'https://downloads.rakwireless.com/LoRa/RAK7267/Certification/RAK7267_ISED_Certification.pdf',
    },
    {
        'rcm': 'https://downloads.rakwireless.com/LoRa/RAK7267/Certification/RAK7267_RCM_Certification.pdf',
    },
    {
        'rohs': 'https://downloads.rakwireless.com/LoRa/RAK7267/Certification/RAK7267_ROHS_Report.pdf',
    },
    {
        'rsm': 'https://downloads.rakwireless.com/LoRa/RAK7267/Certification/RAK7267_RSM_Certification.pdf',
    },
    {
        'red': 'https://downloads.rakwireless.com/LoRa/WisGate/Certification/WisGate_RED_Verification.pdf'
    },
    {
        'ukca': 'https://downloads.rakwireless.com/LoRa/RAK7267/Certification/RAK7267_UKCA_Certification.pdf',
    },
]} />


<RkBottomNav/>
