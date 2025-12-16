---
slug: /product-categories/wisblock/rak13300/datasheet/
title: RAK13300 WisBlock LPWAN Wireless Module Datasheet
description: Provides comprehensive information about your RAK13300 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak13300/rak13300.png"
keywords:
    - RAK13300
    - wisblock
    - datasheet
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK13300 WisBlock LPWAN Wireless Module Datasheet

## Overview

### Description

The RAK13300 is a LoRa module based on the SX1262 LoRa chip. It provides an easy-to-use, small-size, and low-power solution for long-range wireless data applications.

The module complies with LoRaWAN standards and supports LoRa point-to-point communication. It can easily connect to different LoRaWAN server platforms like TheThingsNetwork (TTN), Chirpstack, Actility, etc.


### Features

- Based on Semtech SX1262 LoRa chip
- LoRaWAN Specification compatible
- Supports the following bands: EU433, CN470, IN865, EU868, AU915, US915, KR920, RU864, and AS923
- LoRaWAN Activation by OTAA/ABP
- LoRa Point-to-Point (P2P) communication
- Ultra-Low Power Consumption
- Supply Voltage: 2.0&nbsp;V ~ 3.6&nbsp;V
- Temperature Range: -40°&nbsp;C ~ 85°&nbsp;C
- Module Size: 25&nbsp;mm x 35&nbsp;mm

## Specifications

### Overview

#### Mounting

The RAK13300 WisBlock LPWAN can be mounted to the IO slot of the WisBlock Base board. **Figure 1** shows the mounting mechanism of the RAK13300 on a WisBlock Base board, such as the [RAK5005-O](https://store.rakwireless.com/products/rak5005-o-base-board).

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13300/datasheet/mounting.png" 
  figureCount="1"
  caption="RAK13300 WisBlock LPWAN Mounting" 
   width="60%"
/>

### Hardware

The hardware specification is categorized into five parts. It shows the pinouts and their corresponding functions and diagrams. It also covers the rf, electrical, and mechanical parameters, which include the tabular data of the functionalities and standard ratings of the RAK13300 WisBlock LPWAN Wireless Module.

#### Chipset
| Vendor   | Part number |
| -------- | ----------- |
| Semtech  | SX1262      |

#### Pin Definition

The RAK13300 WisBlock LPWAN comprises a standard WisIO connector. The WisIO connector allows the RAK13300 module to be mounted to a WisBlock baseboard, such as RAK5005-O. The pin order of the connector and the pinout definition is shown in **Figure 2**.

:::tip NOTE

**SPI** related pin, **NRESET**, **ANT_SW**，**DIO1**，**3V3** and **GND** are connected to WisIO connector.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13300/datasheet/rak13300_pinouts.svg" 
  figureCount="2"
  caption="RAK13300 WisBlock LPWAN Pinout" 
   width="80%"
/>


#### RF Characteristics
##### Operating Frequencies

The table below shows the supported LoRaWAN Bands of the RAK13300 module:

| Module      | Region    | Frequency (MHz) |
| ----------- | --------- | --------------- |
| RAK13300(L) | Europe    | EU433           |
|             | China     | CN470           |
| RAK13300    | Europe    | EU868           |
|             | America   | US915           |
|             | Australia | AU915           |
|             | Korea     | KR920           |
|             | Asia      | AS923           |
|             | India     | IN865           |
|             | Russia    | RU864           |

#### Electrical Characteristics

##### Absolute Maximum Ratings

| **Symbol** | **Description**                      | **Min.** | **Nom.** | **Max.** | **Unit** | **Note** |
| ---------- | ------------------------------------ | -------- | -------- | -------- | -------- | -------- |
| 3V3_S      | LoRa chip and IO pins supply voltage | -0.5     | 3.3      | 3.9      | V        | Connected internally to VBAT_SX and VBAT_SX_IO |
| ESD HBM    | Human body model                     | -        | -        | 2000     | V        |          |
| ESD  CDM   | Charged device model                 | -        | -        | 500      | V        |          |

##### Recommended Operating Conditions

| **Symbol** | **Description**                       | **Min.** | **Nom.** | **Max.** | **Unit** | **Note** |
| ---------- | ------------------------------------- | -------- | -------- | -------- | -------- | -------- |
| 3V3_S      | LoRa chip and IO pins supply voltage  | 2.0      | 3.3      | 3.7      | V        |Connected internally to VBAT_SX and VBAT_SX_IO |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 3** shows the dimensions and the mechanical drawing of the RAK13300 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13300/datasheet/mechanical-drawing.png" 
  figureCount="3"
  caption="RAK13300 WisBlock LPWAN Dimensions" 
   width="70%"
/>

##### WisConnector PCB Layout

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13300/datasheet/pcb-layout.png" 
  figureCount="4"
  caption="WisConnector PCB Footprint and Recommendations" 
   width="100%"
/>


#### Schematic Diagram

##### Connector

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13300/datasheet/pinout.png" 
  figureCount="5"
  caption="RAK13300 Module WisConnector" 
   width="60%"
/>

##### Oscillator

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13300/datasheet/oscillator.png" 
  figureCount="6"
  caption="RAK13300 Oscillator" 
   width="60%"
/>

##### SX1262

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13300/datasheet/sx162.png" 
  figureCount="7"
  caption="RAK13300 Module WisConnector" 
   width="100%"
/>

:::tip NOTE
- Uses DC-DC Converter as default.
- **J1** is an IPEX Connector for LoRa antenna.
:::

## Certification

<RkCertificationIcons certifications={[

{'ce': 'https://downloads.rakwireless.com/LoRa/WisBlock/RAK13300/Certification/RAK13300_CE_Certification.pdf',

},

{'fcc': 'https://downloads.rakwireless.com/LoRa/WisBlock/RAK13300/Certification/RAK13300_FCC_Certification.zip',

},

{'ised': 'https://downloads.rakwireless.com/LoRa/WisBlock/RAK13300/Certification/RAK13300_ISED_Certification.pdf',

},

{'ukca': 'https://downloads.rakwireless.com/LoRa/WisBlock/RAK13300/Certification/RAK13300_UKCA_Certification.pdf',

},

]}/>

<RkBottomNav/>