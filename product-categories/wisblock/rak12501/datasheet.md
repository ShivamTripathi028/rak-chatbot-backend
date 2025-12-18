---
slug: /product-categories/wisblock/rak12501/datasheet/
title: RAK12501 WisBlock GNSS Location Module Datasheet
description: Provides comprehensive information about your RAK12501 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak12501/rak12501.png"
keywords:
    - rak12501 gnss module
    - wisblock
    - datasheet
    - quecter l76k
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK12501 WisBlock GNSS Location Module Datasheet

## Overview
<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12501/datasheet/rak12501-location-module.png"
  caption="RAK12501 WisBlock GNSS Location Module"
  width="40%"
/>

### Description

The RAK12501 WisBlock GNSS Location Module is designed to be part of a production-ready IoT solution in a modular way and must be combined with a WisBlock Core and a Base module.

Equipped with the Quectel L76K, the RAK12501 supports a wide variety of satellite data protocols such as GPS, GLONASS, QZSS, and BeiDou. This ensures the retrieval of precise location data. The module features exceptional performance, high sensitivity, and minimal acquisition time. A very suitable module for your low-power IoT solution needs.

### Features

* **Module Specification**
    * Uses the very accurate GNSS Module: **Quectel L76K**
    * Location Accuracy of ±2.5&nbsp;meter
    * Velocity Accuracy of ±0.1&nbsp;m/s
    * GPS, GLONASS, QZSS, and BeiDou Satellite support
    * Serial communication to WisBlock Core support
    * 1&nbsp;Hz Update Rate
    * Location Fix:
      * Cold Start: 35&nbsp;seconds
      * Hot Start: 1&nbsp;second
    * Operating Voltage: 3.3&nbsp;V
    * Operating Current: < 25&nbsp;mA

* **Size**
    * Module Size: 10&nbsp;mm x 23&nbsp;mm

## Specifications

### Overview

#### Mounting

**Figure 2** shows the mounting mechanism of the RAK12501 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. The RAK12501 module can be mounted on the slots: **SLOT A  or SLOT D**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12500/datasheet/rak12500-mounting.png"
  caption="RAK12501 Module mounting mechanism"
  width="60%"
/>

### Hardware

The hardware specification is categorized into five parts that cover the chipset and pinouts and the corresponding functions and diagrams of the board. It also presents the parameters and their standard values in terms of electrical and mechanical.

#### Chipset

The RAK12501 utilizes a very accurate Quectel L76K chip. See the manufacturer's [Quectel L76K Page](https://www.quectel.com/product/gnss-l76/) for more details.

| Vendor  | Part Number |
| :-----: | :---------: |
| Quectel |    L76K     |


#### Pin Definition

The RAK12501 WisBlock GNSS Location Module comprises a standard WisBlock connector. The WisBlock connector allows the RAK12501 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 3**.
<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12501/datasheet/rak12501-pin.png"
  caption="RAK12501 GNSS Module pinout"
  width="60%"
/>

:::tip NOTE
Only the UART related pins, VDD, and GND are connected to this module. WB_IO2 is used to control the power supply of the module.
:::

#### Electrical Characteristics

##### Recommended Operating Conditions

The table below shows the recommended operating conditions for the RAK12501 WisBlock GNSS Location Module:

| **Symbol**              | **Description**             | **Min.** | **Nom.** | **Max.** | **Unit** |
| ----------------------- | --------------------------- | -------- | -------- | -------- | -------- |
| V<sub>DD</sub>          | Power supply for the module | 2.8      | 3.3      | 4.3      | V        |
| I<sub>Acquisition</sub> | Power Acquisition           | -        | 25       | -        | mA       |
| I<sub>Tracking:</sub>   | Power Tracking              | -        | 18       | -        | mA       |
| I<sub>Saving:</sub>     | Power Saving                | -        | 7        | -        | uA       |


#### Mechanical Characteristics

##### Board Dimensions

**Figure 4** shows the dimensions and mechanical drawing of the RAK12501 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12501/datasheet/rak12501-board-dimensions.png"
  caption="RAK12501 board dimensions"
  width="60%"
/>

##### WisConnector PCB Layout

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12500/datasheet/mxxs1003k6m.png"
  caption="WisConnector PCB footprint and recommendations"
  width="100%"
/>

#### Schematic Diagram

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak12501/datasheet/rak12501-schematic.png"
  caption="RAK12501 schematic diagram"
  width="100%"
/>

<RkBottomNav/>