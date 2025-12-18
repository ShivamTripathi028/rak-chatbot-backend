---
slug: /product-categories/wislink/lx200v30/datasheet/
title: LX200V30 WisLink 500 Mbps Broadband PLC Module + EVB Datasheet
description: Provides comprehensive information about your LX200V30 WisLink 1000 Mbps PLC Module + EVB to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wislink-plc/lx200v30/1.lx200v30.png"
keywords:
  - datasheet
  - wislink
  - lx200v30
sidebar_label: Datasheet
---

# LX200V30 WisLink 500 Mbps Broadband PLC Module + EVB Datasheet

## Overview

### Description

LX200V30 is a new type of data transmission product based on OFDM (Orthogonal Frequency Division Multiplexing). The maximum transmission rate of power lines can reach 500 Mbps. Standard Ethernet ports, as well as the two interfaces of twisted pair and coaxial cable, are provided. The module supports 128-bit AES encryption and communicates via a frequency band of 2-68 MHz, and the existing CATV signal or wired broadcasting is not affected. It can be put into work after the wiring is completed without any user configuration. This will advance the product's time-to-market and increase the flexibility of product functionality.

### Features

- 500 Mbps PHY rate
- 128-bit encryption
- Range:
  - Power line: up to 300 m
  - Twisted pair: up to 600 m
  - Coaxial cable: up to 2000 m
- Compliant with Homeplug AV specification and IEEE1901 standards
- MII communication interface for communication with any Ethernet-based device
- Data transmission via a coaxial cable, twisted pair, or a power line
- Working frequency range 2-68 MHz
- Dimensions: 40 x 30 mm

:::warning
For optimal performance and extended device lifespan, use active or passive cooling such as fans or heatsinks to regulate chip temperature during operation.
:::

### Applications

- Smart monitoring instruments
- Energy management systems
- Smart home
- Medical systems
- Automobile electronics charging pile
- Industry

## Specifications

#### Block Diagram

> **Image:** LX200V30 block diagram

#### Parameters

| Parameter                     | Value                 |
| ----------------------------- | --------------------- |
| Max. data rate                | 1000 Mbps        |
| DC interface                  | 4.75 V~36 V |
| V50 supported unit connection | 6~8                   |

### Hardware

The hardware specification is categorized into five parts. It shows the interfacing and the pinouts of the board and their corresponding functions and diagrams. It also covers the electrical and mechanical parameters of the LX200V30 WisLink 500 Mbps Broadband PLC Module + EVB.

#### Interfaces

##### Evaluation Board (EVB)

The external interface circuits required by the LX200V30 backplane include 7 ~ 28 V, 3.3V BUCK, DC power connector, Ethernet RJ45, PLC coupling transmission transformer, and other coupling parts and their interfaces. The auxiliary interface test board is designed to be convenient for testing. When customers design products, changes will be made according to different structure of products.

> **Image:** Baseplate interfaces and top view

#### Pin Definition

> **Image:** Pin definition

| Pin No. | Definition    | Description                                          |
| ------- | ------------- | ---------------------------------------------------- |
| 1       | NC1           | NC                                                   |
| 2       | TR1-          | Coupling signal sending, negative                    |
| 3       | NC2           | NC                                                   |
| 4       | NC3           | NC                                                   |
| 5       | TR1+          | Coupling signal receiving, positive                  |
| 6       | NC4           | NC                                                   |
| 7       | GND           | Ground                                               |
| 8       | IN 12 V  | 12 V input operating voltage                    |
| 9       | GND           | Ground                                               |
| 10      | IN 3.3 V | 3.3 V input operating voltage                   |
| 11      | PWR           | Power indicator                                      |
| 12      | ETH           | Net-port ACT light, flashing when there is data flow |
| 13      | PLC           | Signal transmission indicator light                  |
| 14      | RST           | Reset                                                |
| 15      | ETX+          | Network sending signal, positive                     |
| 16      | ETX-          | Network sending signal, negative                     |
| 17      | ERX+          | Network receiving signal, positive                   |
| 18      | ERX-          | Network receiving signal, negative                   |
| 19      | NC5           | NC                                                   |
| 20      | NC6           | NC                                                   |

#### Electrical Characteristics

| Parameter                    | Min   | Typical | Max   | Unit |
| ---------------------------- | ----- | ------- | ----- | ---- |
| 12 V operating voltage  | 11.15 | 12      | 12.85 | V    |
| 3.3 V operating voltage | 3.15  | 3.3     | 3.45  | V    |
| Operating current            | 125   | 130     | 145   | mA   |

#### Mechanical Characteristics

#### Schematic Diagram

> **Image:** Connector pin map

> **Image:** Ethernet port diagram

> **Image:** Signal receiving diagram

> **Image:** Signal indicators, factory parameter restoring circuit, and all kinds of filter circuits

#### Installation Guide

##### Assembly

The LX200V30 module is connected to the EVB via the pin connector. Simply slide the pins of the module in the connector of the board.

> **Image:** Assemble the module

:::tip NOTE

1. The signals RX+ and RX-, TX+ and TX-, PERX_P and PERX_N, PETX_P and PETX_N all use differential signal lines, and the cabling should follow the rules for differential signal.
2. The width of RX+ and RX-, TX+ and TX- should be no less than 20  mm. The length of the lines must not be more than 15 cm.

