---
slug: /product-categories/wisnode/rak9105u/datasheet/
title: RAK9105U Remote Reboot Switch for LoRaWAN
description: Provides comprehensive information about your RAK9105U Power Controller to help you use it. This information includes technical specifications, characteristics, and requirements.
image: "https://images.docs.rakwireless.com/wisnode/rak9105u/1.rak9105u.png"
keywords:
  - RAK9105U
  - power supply
  - accessories
  - datasheet
sidebar_label: Datasheet
tags:
    - rak9105u
    - wisnode
    - datasheet
date: 2025-07-10
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK9105U PowerLink - Remote Reboot Switch for LoRaWAN Datasheet

## Overview

### Description

The **RAK9105U PowerLink - Remote Reboot Switch for LoRaWAN** is a LoRaWAN-based remote power controller designed for managing power supply to devices such as gateways, LTE CPEs, WiFi routers, and IP cameras, especially in remote or hard-to-reach deployment environments.

- <b>Remote Power Switching</b><br/>
By placing the RAK9105U between the power source and the target device, users can send **LoRaWAN downlink commands** to remotely toggle the power on or off.
- <b>Remote Device Reboot</b><br/>
Ideal for scenarios where devices freeze or require periodic reboots, such as LoRaWAN gateways or LTE CPEs in field installations.

### Features

- Integrated RAK3172 LoRa module for long-range, low-power wireless control
- Supports LoRaWAN 1.0.3 Class C protocol
- Multi-band compatibility for global deployment
- Onboard LoRa antenna (Optional external antenna via IPEX connector)
- Remote power switching and rebooting via LoRaWAN downlink commands
- Plug-and-play integration available with Datacake platform
- Wide-range DC power input: 9–24&nbsp;V via terminal block or DC jack (Compatible with RAK Battery Plus system for solar-powered deployments)
- Triple output design:
    - 1 always-on 12&nbsp;V<sub>DC</sub> output
    - 2 controllable outputs (12&nbsp;V + 5&nbsp;V USB-C)


## Specifications

### Overview

<RkImage
  src="https://images.docs.rakwireless.com/accessories/rak9105u/1.rak9105u.png"
  width="70%"
  caption="RAK9105U overview"
/>

#### Block Diagram

<RkImage
  src="https://images.docs.rakwireless.com/accessories/rak9105u/2.block-diagram.png"
  width="80%"
  caption="RAK9105U block diagram"
/>


#### LoRa Connectivity

<table>
  <thead>
    <tr>
      <th>Parameters</th>
      <th>Specifications</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Chipset</td>
      <td>RAK3172 (STM32-based)</td>
    </tr>
    <tr>
      <td>LoRaWAN Version</td>
      <td>v1.0.3<br/>Class C </td>
    </tr>
    <tr>
      <td>Activation</td>
      <td>OTAA (Over-The-Air Activation)</td>
    </tr>
    <tr>
      <td>Frequency Bands</td>
      <td>EU868, IN865, RU864, AU915, US915, KR920, AS923-1/2/3/4, EU433, and CN470</td>
    </tr>
  </tbody>
</table>

### Hardware

The hardware specifications are categorized into six parts. The section discusses the interfacing and corresponding functions, electrical, environmental characteristics, and antennas.

#### Interface

##### DC Input Interface

<RkImage
  src="https://images.docs.rakwireless.com/accessories/rak9105u/5.in-interface.png"
  width="50%"
  caption="DC input interface"
/>

<table>
  <thead>
    <tr>
      <th>Interfaces</th>
      <th>Description</th>
      <th>Remark</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>12&nbsp;V<sub>DC</sub> Input</td>
      <td>DC power jack for external power supply</td>
      <td>Supports 9-24&nbsp;V<sub>DC</sub> input</td>
    </tr>
    <tr>
      <td>12&nbsp;V<sub>DC</sub> Input (RS485)</td>
      <td>4-pin terminal block for DC power input and optional RS485 communication</td>
      <td>**DC Power input**:<br/><ul><li>**+**: Connect to the positive output terminal of Battery Plus</li><li>**-**: Connect to the negative output terminal of Battery Plus</li></ul><br/>**RS485 communication** (Optional):<br/><ul><li>**A**: Connect to RS485+ of Battery Plus</li><li>**B**: Connect to RS485- of Battery Plus</li></ul><br/> Compatible with RAK Battery Plus or other RS485-enabled systems</td>
    </tr>
  </tbody>
</table>

##### DC Output Interface

<RkImage
  src="https://images.docs.rakwireless.com/accessories/rak9105u/4.out-interface.png"
  width="45%"
  caption="DC output interface"
/>

<table>
  <thead>
    <tr>
      <th>Interfaces</th>
      <th>Description</th>
      <th>Specifications</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Output1</td>
      <td>12&nbsp;V<sub>DC</sub> power jack (always on)</td>
      <td>Voutput1 = Vinput -0.6&nbsp;V<br/>Maximum Current 2&nbsp;A</td>
    </tr>
    <tr>
      <td>Output2</td>
      <td>12&nbsp;V<sub>DC</sub> power jack (MCU-controlled)</td>
      <td>Voutput2 = Vinput -0.6&nbsp;V<br/>Maximum Current 2&nbsp;A</td>
    </tr>
    <tr>
      <td>Output3</td>
      <td>5&nbsp;V USB Type-C (MCU-controlled)</td>
      <td>Voutput3 = 5&nbsp;V / 3&nbsp;A <br/>Maximum Current 3&nbsp;A</td>
    </tr>
  </tbody>
</table>

##### Console

The Console interface is a USB Type-C port used to configure the onboard RAK3172 MCU or upgrade firmware via WisToolBox.

#### Antenna

| Parameter    | Value      |
| ------------ | ---------- |
| Peak gain    | 2&nbsp;dBi |
| Efficiency   | > 70%      |
| Polarization | Vertical   |


#### Environmental Characteristics

| Feature               | Specifications             |
| --------------------- | -------------------------- |
| Type of use           | Indoor environment         |
| Operating temperature | -30°&nbsp;C to +75°&nbsp;C |
| Storage temperature   | -40°&nbsp;C to +85°&nbsp;C |
| Operating humidity    | 0-95%RH non-condensing     |
| Storage humidity      | 0-95%RH non-condensing     |


#### Mechanical Characteristics

<RkImage
  src="https://images.docs.rakwireless.com/accessories/rak9105u/3.dimensions.png"
  width="50%"
  caption="RAK9105U dimensions"
/>

- **Dimensions**: 105.5&nbsp;mm × 74.4&nbsp;mm × 37.2&nbsp;mm
- **Enclosure Material**: PMMA

#### Battery Plus Information

RAK9105U uses the RAK3172 module to read and report the battery data over LoRaWAN. By default, it uses the integrated PCB antenna on the PCB. An optional i-PEX connector option can be requested.

### Software

The firmware is based on RUI3 and comes pre-flashed.
It includes default LoRaWAN keys, which are provided on a label on the device’s casing.

<RkBottomNav/>