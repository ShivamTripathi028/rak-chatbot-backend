---
slug: /product-categories/wislink/lx200v20/datasheet/
title: LX200V20 WisLink 200 Mbps PLC Module + EVB Datasheet
description: Provides comprehensive information about your LX200V20 WisLink 200 Mbps PLC Module + EVB to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wislink-plc/lx200v20/lx200v20.png"
keywords:
  - datasheet
  - wislink
  - lx200v20
sidebar_label: Datasheet
---

# LX200V20 WisLink 200 Mbps PLC Module + EVB Datasheet

## Overview

### Description

**LX200V20** is a Power Line Communication (PLC) product supporting IEEE 1901 and Homeplug AV standards. It features a standard MII interface for communication. The small footprint is ideal for embedded design applications. Connectors allow easy integration into target devices. This module accelerates design cycles and speeds up time to market. Measuring 40 x 21 mm, it operates on a single 3.3 V<sub>DC</sub> rail with an integrated power management unit. The module supports robust OFDM mode modulation 200 Mbps PHY rate. It can be integrated into smart meters and is ideal for energy, surveillance, and smart home applications.

### Features

- 200 Mbps PHY rate
- 128-bit encryption
- MAx Range: 
  - Power Lines: 300 m 
  - Telephone Lines: 600 m 
  - Cable Lines: 2000 m
- Compliant with Homeplug AV specification and IEEE1901 standards
- Single chip solution with integrated analog front end and line driver
- MII communication interface for communication with any Ethernet-based device
- Data transmission via two-wired lines, telephone line, and a power line
- Working frequency range 2-30 MHz
- Dimensions: 60 x 30 mm

:::warning
For optimal performance and extended device lifespan, use active or passive cooling such as fans or heatsinks to regulate chip temperature during operation.
:::

## Specifications

#### Parameters

| Parameter                     | Value              |
|-------------------------------|--------------------|
| Max. data rate                | 200 Mbps      |
| DC interface                  | 7 V~28 V |

### Applications

- Smart meters
- Energy management systems
- Programmable controlled thermostats
- Remote meter devices
- Surveillance
- Industry
- Solar panels

### Hardware

The hardware specification is categorized into five parts. It shows the interfacing and the pinouts of the board and their corresponding functions and diagrams. It also covers the electrical and mechanical parameters of the LX200V30 WisLink 500 Mbps Broadband PLC Module + EVB.

#### Interfaces

##### Evaluation Board (EVB)

The EVB provides all the external interfaces required by the PLC module, which include 7V-28 V DCDC, 3.3 V BUCK, DC power Jack, RJ45 Ethernet, and a PLC coupling transformer. The board is suitable for any embedded design that needs a different power circuit. You can easily use the board to evaluate the PLC performance. 

> **Image:** Baseplate interfaces and top view

#### Pin Definition

Module connector J2 is a single row of 2.0 mm pins, responsible for drawing out the corresponding interface, including the Ethernet interface of connecting RJ45, PLC coupling TX and RX interface, power supply, LED, and so on. Тhe order from right to left from 1 to 20. The specific definitions are as follows.

> **Image:** Pin definition

| Pin No. | Definition | Description                                                                                                           |
|---------|------------|-----------------------------------------------------------------------------------------------------------------------|
| 1       | GND        | Ground                                                                                                                |
| 2       | TX+        | Powerline Tx signal                                                                                                   |
| 3       | TX-        | Powerline Tx signal                                                                                                   |
| 4       | GND        | Ground                                                                                                                |
| 5       | RX+        | Powerline Rx signal                                                                                                   |
| 6       | RX-        | Powerline Rx signal                                                                                                   |
| 7       | GND        | Ground                                                                                                                |
| 8       | ZC_IN_EX   | Zero cross input
Minimum: 100 mVpp, AC coupled
Maximum: 3.3 Vpp, AC coupled                                     |
| 9       | GPIO[0]    | PLC Link LED, light when the PLC is connected (Blue LED on EVB board)                                                 |
| 10      | GPIO[1]    | System self-check LED, light after power up (Green LED on EVB board RJ45)                                             |
| 11      | GND        | Ground                                                                                                                |
| 12      | GPIO[2]    | Ethernet LED, light when the Ethernet is connected, blink when data is in transmission (Yellow LED on EVB board RJ45) |
| 13      | GPIO[3]    | Factory default                                                                                                       |
| 14      | VDD2P0     | Ethernet 2.0 V                                                                                                   |
| 15      | PERX_P     | Differential in, positive differential input from bandpass filter                                                     |
| 16      | PERX_N     | Differential in, negative differential input from bandpass filter                                                     |
| 17      | GND        | Ground                                                                                                                |
| 18      | PETX_P     | Differential out, positive differential output of the TX PGA                                                          |
| 19      | PETX_N     | Differential out, negative differential output of the TX PGA                                                          |
| 20      | 3.3 V | 3.3 V working voltage                                                                                            |

#### Electrical Characteristics

| Parameter       | Min  | Typical | Max  | Unit |
|-----------------|------|---------|------|------|
| Working voltage | 3.15 | 3.3     | 3.45 | V    |
| Working current | -    | 700     | -    | mA   |

#### Mechanical Characteristics

#### Schematic Diagram

> **Image:** Connector pin map

> **Image:** Ethernet port diagram

> **Image:** Signal Tx and Rx diagram

> **Image:** LED diagram

> **Image:** Reset and power regulator diagram

#### Installation Guide

##### Assembly

The LX200V20 module is connected to the EVB via the pin connector. Simply slide the pins of the module in the connector of the board. Pin 1 is on the right side of the module and pin 20 on the left.

> **Image:** Assembly

:::tip NOTE

1. RX+ and RX-, TX+ and Tx-, PERX_P and PERX_N, PETX_P and PETX_N are all the differential available signals. Follow the differential signal rules when designing your hardware.

2. The width of RX+ and RX-, TX+ and TX- should be no less than 20 mm. The length of the lines must not be more than 15 cm.

:::

