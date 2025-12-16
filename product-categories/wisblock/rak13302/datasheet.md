---
slug: /product-categories/wisblock/rak13302/datasheet/
title: RAK13302 WisBlock LPWAN Wireless Module Datasheet
description: Provides comprehensive information about your RAK13302 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak13302/rak13302.png"
keywords:
    - rak13302
    - wisblock
    - datasheet
sidebar_label: Datasheet
tags:
    - rak13302
    - wisblock
    - datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK13302 WisBlock LPWAN Wireless Module Datasheet

## Overview

### Description

The RAK13302 is a LoRa module built around the Semtech SX1262 LoRa transceiver and the SKY66122 signal booster. It offers an easy-to-use, compact, and low-power solution for long-range wireless data applications.

Fully compliant with LoRaWAN standards, the RAK13302 also supports LoRa Point-to-Point (P2P) communication. It seamlessly integrates with LoRaWAN network servers, including The Things Network (TTN), ChirpStack, Actility, and more.

With its 1-watt signal booster, the RAK13302 is well-suited for applications that demand extended communication range.

The module is compatible with the RAK6421 RPi WisBlock HAT and WisBlock Base Boards, when used in conjunction with the RAK3401 or RAK11200 WisBlock Core module.

### Features

- Based on Semtech SX1262 LoRa chip and SKY66122 booster chip
- LoRaWAN Specification compatible
- Supports 902-928&nbsp;MHz
- LoRaWAN Activation by OTAA/ABP
- LoRa Point-to-Point (P2P) communication
- Ultra-Low Power Consumption
- Supply Voltage: 5&nbsp;V
- Temperature Range: -40°&nbsp;C ~ 85°&nbsp;C
- Module Size: 25&nbsp;mm x 35&nbsp;mm

## Specifications

### Overview

#### Mounting

The RAK13302 WisBlock LPWAN can be mounted to the IO slot of the WisBlock Base board. **Figure 1** shows the mounting mechanism of the RAK13302 on a WisBlock Base board, such as the [RAK19007](https://docs.rakwireless.com/product-categories/wisblock/rak19007/overview/).

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13302/datasheet/mount-rak13302.png"
  caption="RAK13302 Wireless Module mounting mechanism"
  width="60%"
/>

### Hardware

The hardware specification is categorized into five parts. It shows the pinouts and their corresponding functions and diagrams. It also covers the rf, electrical, and mechanical parameters, which include the tabular data of the functionalities and standard ratings of the RAK13302 WisBlock LPWAN Wireless Module.

#### Chipset

| Vendor  | Part Number |
| ------- | ----------- |
| Semtech | SX1262      |
| Sky     | SKY66122    |

:::warning
Due to the high power RF signal output, the module requires as supply through USB on the WisBlock Base Board or an external 5&nbsp;V supply voltage.
:::

#### Pin Definition

The RAK13302 WisBlock LPWAN comprises a standard WisIO connector. The WisIO connector allows the RAK13302 module to be mounted to a WisBlock baseboard, such as RAK19007. The pin order of the connector and the pinout definition is shown in **Figure 2**.

:::tip NOTE

**SPI** related pin, **NRESET**, **ANT_SW**，**DIO1**，**BUSY**, **EX_5V**, **VBAT**, **3V3**, and **GND** are connected to WisIO connector.
EX_5V is for an external 5&nbsp;V power supply for the booster.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13302/datasheet/rak13302-pinout.png"
  caption="RAK13302 Wireless Module pinouts"
  width="80%"
/>

#### Power Selector Jumper

The 3-pin jumper header is to select the supply source for the booster chip.

| Jumprer Position  | Supply Source                           |
| :---------------: | --------------------------------------- |
| IN_5V to 5&nbsp;V | Supply from WisBlock Base Board Battery |
| EX_5V to 5&nbsp;V | Supply from Jx connector                |

:::tip NOTE
If the supply is through EX_5V, the whole WisBlock Base Board can be supplied through this source.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13302/datasheet/rak13302-supply.png"
  caption="RAK13302 5&nbsp;V supply selection"
  width="80%"
/>

**External power supply cable connections:**

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13302/datasheet/rak13302-power-cable.png"
  caption="RAK13302 5&nbsp;V supply selection"
  width="80%"
/>


#### RF Characteristics

##### Operating Frequencies

The RAK13302 supports LoRa 902-928&nbsp;MHz frequencies.

#### Electrical Characteristics

| **Symbol** | **Description**                | **Min.** | **Nom.** | **Max.** | **Unit** |
| :--------: | ------------------------------ | :------: | :------: | :------: | :------: |
|    VBAT    | Power supply from battery      |   3.0    |    -     |   4.2    |    V     |
|    3V3     | 3.3&nbsp;V from base board     |    -     |   3.3    |    -     |    V     |
|   EX_5V    | External 5&nbsp;V power supply |    -     |    5     |    -     |    V     |

### Transmit Power VS Peak Current

| SX1262 Config (dBm) | Peak Current @5&nbsp;V (mA) | Output Power (dBm) |
| :-----------------: | :-------------------------: | :----------------: |
|         22          |            1000             |        30.0        |
|         19          |             740             |        27.0        |
|         16          |             560             |        24.0        |
|         13          |             410             |        21.0        |
|         10          |             300             |        18.0        |
|          7          |             230             |        15.0        |
|          4          |             170             |        12.0        |
|          1          |             110             |        9.0         |

###  RX sensitivity VS Average Current

| SX1262 Config @125&nbsp;kHz | Average Current @5&nbsp;V (mA) | RX Sensitivity (dBm) |
| :-------------------------: | :----------------------------: | :------------------: |
|             SF7             |               12               |         -125         |
|             SF8             |               12               |         -128         |
|             SF9             |              12-               |         -133         |
|            SF10             |               12               |         -134         |
|            SF11             |               12               |         -137         |
|            SF12             |               12               |         -140         |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 3** shows the dimensions and the mechanical drawing of the RAK13302 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13302/datasheet/rak13302-dimensions.png"
  caption="RAK13302 Wireless Module dimensions"
  width="70%"
/>

##### WisConnector PCB Layout

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13302/datasheet/wisconnector-pcb-footprint.png"
  caption="WisConnector PCB Footprint and Recommendations"
  width="100%"
/>


#### Schematic Diagram

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13302/datasheet/rak13302-schematic.svg"
  figureCount="5"
  caption="RAK13302 Schematic"
   width="100%"
/>

##### Connector

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13302/datasheet/rak13302-module-pinout.png"
  caption="RAK13302 Module WisConnector"
  width="60%"
/>

##### SX1262

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13302/datasheet/sx162.png"
  caption="RAK13302 Module SX1262"
  width="100%"
/>

#### PA

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13302/datasheet/rak13302-amplifier.png"
  caption="RAK13302 Amplifier"
  width="80%"
/>

#### Boost

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13302/datasheet/rak13302-5v-booster.png"
  caption="RAK13302 5&nbsp;V booster"
  width="60%"
/>

#### Connector for External 5V

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13302/datasheet/rak13302-5v-connector.png"
  caption="RAK13302 5&nbsp;V external connector"
  width="60%"
/>

#### Pin Header for Power Selection

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak13302/datasheet/rak13302-5v-selector.png"
  caption="RAK13302 5&nbsp;V selector"
  width="60%"
/>

:::tip NOTE
If the supply is through EX_5V, the whole WisBlock Base Board can be supplied through this source.
:::

<RkBottomNav/>