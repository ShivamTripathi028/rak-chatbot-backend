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

# RAK9105U PowerLink - Remote Reboot Switch for LoRaWAN Datasheet

## Overview

### Description

The **RAK9105U PowerLink - Remote Reboot Switch for LoRaWAN** is a LoRaWAN-based remote power controller designed for managing power supply to devices such as gateways, LTE CPEs, WiFi routers, and IP cameras, especially in remote or hard-to-reach deployment environments.

- **Remote Power Switching**

By placing the RAK9105U between the power source and the target device, users can send **LoRaWAN downlink commands** to remotely toggle the power on or off.
- **Remote Device Reboot**

Ideal for scenarios where devices freeze or require periodic reboots, such as LoRaWAN gateways or LTE CPEs in field installations.

### Features

- Integrated RAK3172 LoRa module for long-range, low-power wireless control
- Supports LoRaWAN 1.0.3 Class C protocol
- Multi-band compatibility for global deployment
- Onboard LoRa antenna (Optional external antenna via IPEX connector)
- Remote power switching and rebooting via LoRaWAN downlink commands
- Plug-and-play integration available with Datacake platform
- Wide-range DC power input: 9–24 V via terminal block or DC jack (Compatible with RAK Battery Plus system for solar-powered deployments)
- Triple output design:
    - 1 always-on 12 V<sub>DC</sub> output
    - 2 controllable outputs (12 V + 5 V USB-C)

## Specifications

### Overview

> **Image:** RAK9105U overview

#### Block Diagram

> **Image:** RAK9105U block diagram

#### LoRa Connectivity

| Parameters | Specifications |
| --- | --- |
| Chipset | RAK3172 (STM32-based) |
| LoRaWAN Version | v1.0.3 Class C |
| Activation | OTAA (Over-The-Air Activation) |
| Frequency Bands | EU868, IN865, RU864, AU915, US915, KR920, AS923-1/2/3/4, EU433, and CN470 |

### Hardware

The hardware specifications are categorized into six parts. The section discusses the interfacing and corresponding functions, electrical, environmental characteristics, and antennas.

#### Interface

##### DC Input Interface

> **Image:** DC input interface

| Interfaces | Description | Remark |
| --- | --- | --- |
| 12 V DC Input | DC power jack for external power supply | Supports 9-24 V DC input |
| 12 V DC Input (RS485) | 4-pin terminal block for DC power input and optional RS485 communication | **DC Power input**: **+**: Connect to the positive output terminal of Battery Plus **-**: Connect to the negative output terminal of Battery Plus **RS485 communication** (Optional): **A**: Connect to RS485+ of Battery Plus **B**: Connect to RS485- of Battery Plus Compatible with RAK Battery Plus or other RS485-enabled systems |

##### DC Output Interface

> **Image:** DC output interface

| Interfaces | Description | Specifications |
| --- | --- | --- |
| Output1 | 12 V DC power jack (always on) | Voutput1 = Vinput -0.6 V Maximum Current 2 A |
| Output2 | 12 V DC power jack (MCU-controlled) | Voutput2 = Vinput -0.6 V Maximum Current 2 A |
| Output3 | 5 V USB Type-C (MCU-controlled) | Voutput3 = 5 V / 3 A Maximum Current 3 A |

##### Console

The Console interface is a USB Type-C port used to configure the onboard RAK3172 MCU or upgrade firmware via WisToolBox.

#### Antenna

| Parameter    | Value      |
| ------------ | ---------- |
| Peak gain    | 2 dBi |
| Efficiency   | > 70%      |
| Polarization | Vertical   |

#### Environmental Characteristics

| Feature               | Specifications             |
| --------------------- | -------------------------- |
| Type of use           | Indoor environment         |
| Operating temperature | -30° C to +75° C |
| Storage temperature   | -40° C to +85° C |
| Operating humidity    | 0-95%RH non-condensing     |
| Storage humidity      | 0-95%RH non-condensing     |

#### Mechanical Characteristics

> **Image:** RAK9105U dimensions

- **Dimensions**: 105.5 mm × 74.4 mm × 37.2 mm
- **Enclosure Material**: PMMA

#### Battery Plus Information

RAK9105U uses the RAK3172 module to read and report the battery data over LoRaWAN. By default, it uses the integrated PCB antenna on the PCB. An optional i-PEX connector option can be requested.

### Software

The firmware is based on RUI3 and comes pre-flashed.
It includes default LoRaWAN keys, which are provided on a label on the device’s casing.

