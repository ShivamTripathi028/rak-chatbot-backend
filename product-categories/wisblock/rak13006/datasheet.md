---
slug: /product-categories/wisblock/rak13006/datasheet/
title: RAK13006 WisBlock CAN Module Datasheet
description: Provides comprehensive information about your RAK13006 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak13006/rak13006.png"
keywords:
  - datasheet
  - wisblock
  - RAK13006
sidebar_label: Datasheet
---

# RAK13006 WisBlock CAN Module Datasheet

## Overview

### Description

RAK13006 is a CAN Bus communication module based on the MCP2518FD CAN controller and ATA6563 CAN transceiver both from Microchip. The MCP2518FD is the CAN chip that communicates to WisBlock Core MCU via SPI up to 17 MHz SPI Clock Speed and ATA6563 is the low-level physical layer chip that provides a physical connection with the CAN bus communication lines. It supports both CAN 2.0B and CAN FD with an arbitration bit rate up to 1 Mbps. This WisBlock Interface module is ideal for industrial and automotive applications.

### Features

- Based on MCP2518FD and ATA6563
- Arbitration Bit Rate up to 1 Mbps
- ISO11898-2:2016 and SAEJ2962-2 Compliant
- Configurable terminal resistance on CANH and CANL lines via slide switch
- Operating temperature: **-40 °C ~ 85 °C**
- Size: 25 x 35 mm

## Specifications

### Overview

#### Mounting

The RAK13006 module can be mounted on the IO Slot of a WisBlock Base board. **Figure 1** shows the mounting mechanism of the RAK13006 on a WisBlock Base board, such as the RAK5005-O, and **Figure 2** shows the terminal crimp connector.

> **Image:** RAK13006 WisBlock CAN Module mounting

> **Image:** RAK13006 Crimp Terminal Connector and Terminal Resistance Switch

### Hardware

The hardware specification is categorized into five parts. It shows the chipset of the module and the pinouts and their corresponding functions and diagrams. It also presents the parameters and their standard values in terms of electrical and mechanical.

####  Chipset

| Vendor                          | Part Number |
| ------------------------------- | ----------- |
| Microchip (CAN Controller)      | MCP2518FD   |
| Microchip (CAN PHY Transceiver) | ATA6563     |

#### Pin Definition

The RAK13006 WisBlock CAN module comprises a standard 40-pin WisConnector. The WisBlock 40-pin connector allows the RAK13006 module to be mounted on a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 3**.

:::tip NOTE
- 3V3_S supply pin
- SPI-related pins
- IO5 connected to interrupt pin
:::

> **Image:** RAK13006 WisBlock CAN Module pinout diagram

#### Electrical Characteristics

##### Operating Conditions

**MCP2518FD**

| Symbol | Description                    | Min. | Nom. | Max. | Unit |
| ------ | ------------------------------ | ---- | ---- | ---- | ---- |
| VDD    | Supply voltage range           | 2.7  | -    | 5.5  | V    |
| Idd    | Active Current                 | -    | 15   | 20   | mA   |
| Idds   | Sleep Current                  | -    | 15   | 60   | uA   |

**ATA6563**

| Symbol    | Description                     | Min. | Nom. | Max. | Unit |
| --------- | ------------------------------- | ---- | ---- | ---- | ---- |
| VCC       | Supply voltage range            | 4.5  | -    | 5.5  | V    |
| Ivcc_stby | Standby Mode Current            | -    | 7    | 12   | uA   |
| Ivcc_sil  | Silent Mode Current             | 1.9  | 2.5  | 3.2  | mA   |
| Ivcc_rec  | Normal Mode Current (recessive) | 2.0  |  -   | 5.0  | mA   |
| Ivcc_dom  | Normal Mode Current (dominant)  | 30   | 50   | 70   | mA   |

#### Mechanical Characteristic

##### Board Dimensions

Figure 4 shows the dimensions and the mechanic drawing of the RAK13006 module.

> **Image:** RAK13006 WisBlock CAN Module mechanic drawing

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

#### Schematic Diagram

- CAN Controller and CAN PHY Transceiver:

> **Image:** RAK13006 CAN controller and transceiver

- 5-V Boost converter for CAN PHY transceiver voltage supply:

> **Image:** 5V Boost

