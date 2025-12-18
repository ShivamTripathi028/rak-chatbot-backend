---
slug: /product-categories/wisnode/rak2470/datasheet/
title: RAK2470 WisNode Bridge Serial Prime Datasheet
description: Provides comprehensive information about your RAK2470 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisnode/rak2470/datasheet/rak2470.png"
keywords:
  - datasheet
  - RAK2470
  - wisnode
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK2470 WisNode Bridge Serial Prime Datasheet

## Overview

### Description

The **RAK2470 WisNode Bridge Serial Prime** is an RS485 to LoRaWAN converter designed for outdoor industrial applications. Utilizing the LoRaWAN network, RAK2470 wirelessly transmits RS485 data to and from end devices.

Additionally, RAK2470 WisNode Bridge Serial Prime comes with a T-type conversion cable, enabling it to link up with any RS485 equipped sensors. Both the RAK2470 and connected sensors can be powered via the DC power port.

RAK2470's default interface, the M12-4 circular connector, permits direct connection to MPPT Solar Charge Controllers, Inverters, or Inverter Integrated Machines.

Together with a RAK WisGate Gateway and LoRa Server products, RAK2470 can quickly and easily build a wireless industrial field control system. It is designed with industrial-grade protection, accommodates a wide range of voltage supplies, supports pole mounting, and facilitates field installation and use.

### Features

- **Regional Parameters Version**: RP001-1.0.3
- **LoRaWAN 1.0.3** protocol stack, supports **Class C**
- **Input range:** 5 ~ 12&nbsp;V<sub>DC</sub>
- **Mounting:** Pole
- IP67 weatherproof

## Specifications

### Main Specifications

| Parameter           | Specifications                                                                                                                                                 |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LoRa Feature        | Protocol stack: LoRaWAN 1.0.3<br/>Frequency: EU868 / IN865 / RU864 / US915 / AU915 / KR920 / AS923 / CN470<br/>LoRaWAN mode: Class C<br/>Tx power: 22&nbsp;dBm |
| RS485 Feature       | Data rate: 9600, 115200<br/>Carrying capacity: Up to 32 devices                                                                                                |
| Power Supply        | 5-12&nbsp;V<sub>DC</sub> input                                                                                                                                 |
| Antenna             | LoRa: Built-in fiberglass antenna<br/>Frequency: 863 ~ 928&nbsp;MHz<br/>VSWR: &lt; 2<br/>Efficiency: &gt; 80%<br/>Max Gain: 3&nbsp;dBi                         |
| Enclosure Material  | Fiberglass                                                                                                                                                     |
| Dimensions          | 30&nbsp;mm × 215&nbsp;mm                                                                                                                                       |
| Protection Grade    | IP67                                                                                                                                                           |
| Working Temperature | -40°&nbsp;C ~ +85°&nbsp;C                                                                                                                                      |
| Storage Temperature | -40°&nbsp;C ~ +85°&nbsp;C                                                                                                                                      |
| Installation method | Pole                                                                                                                                                           |

### Hardware

The hardware specification describes the device's interfaces and parameters.

#### Interfaces

The **RAK2470 WisNode Bridge Serial Prime** comes with an M12-4 circular connector (including power and RS485 data interfaces). 

The power interface needs to be powered by a DC power supply (5 ~ 12&nbsp;V), and the voltage must be stable.

In addition, the RS485 host baud rate supports 9600 and 115200, and up to 32 devices can be connected.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/datasheet/3.m12-4-connector-pin-definition-new.png"
  caption="M12-4 connector pin definition"
  width="60%"
/>

| Pin | Circular Connector | Description                              | Type               |
|-----|--------------------|------------------------------------------|--------------------|
| 1   | VCC                | Power input (5 ~ 12&nbsp;V<sub>DC</sub>) | PI (Power input)   |
| 2   | RS485_A            | RS485 A+                                 | IO (Bidirectional) |
| 3   | RS485_B            | RS485 B-                                 | IO (Bidirectional) |
| 4   | GND                | Ground                                   | PI (Power input)   |



#### T-Type Conversion Cable

The RAK2470 comes with a 1&nbsp;m T-type conversion cable for each branch. Using this conversion cable, the RAK2470 can be connected to any RS485 equipped sensors, and power can be supplied to both the RAK2470 and the connected sensor via the DC power port.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2470/datasheet/4.t-type-conversion-cable-new.png"
  caption="T-type conversion cable"
  width="70%"
/>

:::tip NOTE

The standard length of the T-type conversion cable is 1&nbsp;m. If you need to customize the cable length, kindly contact [inquiry@rakwireless.com](mailto:inquiry@rakwireless.com).

:::


<table>
  <thead>
    <tr>
      <th>Interface</th>
      <th>Pin</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowSpan="4">L20-4 Four-core Straight-through Port</td>
      <td>Pin1</td>
      <td>Connect to the positive terminal of the sensor power cord.</td>
    </tr>
    <tr>
      <td>Pin2</td>
      <td>Connect to RS485-A of the sensor.</td>
    </tr>
    <tr>
      <td>Pin3</td>
      <td>Connect to RS485-B of the sensor.</td>
    </tr>
    <tr>
      <td>Pin4</td>
      <td>Connect to the negative terminal of the sensor power cord.</td>
    </tr>
    <tr>
      <td rowSpan="4">M12-4 Female-pin Port</td>
      <td>Pin1</td>
      <td>Power input (5 ~ 12&nbsp;V<sub>DC</sub>)</td>
    </tr>
    <tr>
      <td>Pin2</td>
      <td>RS485 A+</td>
    </tr>
    <tr>
      <td>Pin3</td>
      <td>RS485 B-</td>
    </tr>
    <tr>
      <td>Pin4</td>
      <td>GND</td>
    </tr>
    <tr>
      <td>DC port</td>
      <td></td>
      <td>Power input port</td>
    </tr>
  </tbody>
</table>


## Certification

<RkCertificationIcons certifications={[
    {
        'ce': 'https://downloads.rakwireless.com/LoRa/RAK2470/Certification/RAK2470_CE_Certification.pdf',
    },
    {
        'rohs': 'https://downloads.rakwireless.com/LoRa/RAK2470/Certification/RAK2470_ROHS_Report.pdf',
    },
    {
        'fcc': 'https://downloads.rakwireless.com/LoRa/RAK2470/Certification/RAK2470_FCC_Certification.pdf',
    },
    {
        'ised': 'https://downloads.rakwireless.com/LoRa/RAK2470/Certification/RAK2470_ISED_Certification.pdf',
    }

]} />


<RkBottomNav/>
