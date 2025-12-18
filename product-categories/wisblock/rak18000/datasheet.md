---
slug: /product-categories/wisblock/rak18000/datasheet/
title: RAK18000 WisBlock PDM Stereo Microphone Module Datasheet
description: Provides comprehensive information about your RAK18000 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak18000/rak18000.png"
keywords:
  - datasheet
  - wisblock
  - RAK18000
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK18000 WisBlock PDM Stereo Microphone Module Datasheet

## Overview
<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18000/datasheet/rak18000_back_front.png" 
  caption="RAK18000 PDM Stereo Microphone Module" 
  width="40%"
/>

### Description

**RAK18000** is a **WisBlock Sensor** module that extends the **WisBlock** system with sound sensing capability. It is based on two MP34DT06J microphone modules.

The RAK18000 is a digital microphone module that is designed to detect sounds and to support left and right channels. It is also capable of changing microphone orientation on the left or right channel through the switch resistor.

### Features

* **Module Specifications**

    - Voltage Supply: 3.3&nbsp;V
    - Current Consumption: 5&nbsp;µA to 650&nbsp;µA
    - Chipset: ST MP34DT06J
    - 64&nbsp;dB signal-to-noise ratio
    - –26&nbsp;dBFS ± 1&nbsp;dB sensitivity
    - Stereo microphone 2 x MP34DT06J
    - Low power consumption

* **Size**
    * 25 x 15&nbsp;mm

## Specifications

### Overview

#### Mounting

The RAK18000 WisBlock PDM Stereo Microphone Module can be mounted to the IO slot of the [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. **Figure 2** shows the mounting mechanism of the RAK18000 on a WisBlock Base module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18000/datasheet/rak18000_mounting.png" 
  caption="RAK18000 PDM Stereo Microphone Module Mounting" 
  width="50%"
/>

### Hardware

The hardware specification is categorized into five parts that cover the chipset and pinouts and the corresponding functions and diagrams of the board. It also presents the parameters and their standard values in terms of acoustic, electrical, and mechanical.

#### Chipset
| Vendor | Part number |
| ------ | ----------- |
| ST     | MP34DT06J   |

#### Pin Definition

The RAK18000 WisBlock PDM Stereo Microphone Module comprises a standard WisBlock connector. The WisBlock connector allows the RAK18000 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 3**.

:::tip NOTE
**DMIC1**, **DMCLK**, **3V3**, and **GND** are connected to WisConnector.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18000/datasheet/rak18000_pinout.svg" 
  caption="RAK18000 PDM Stereo Microphone Module Pinout Diagram" 
  width="60%"
/>

#### Acoustic and Electrical Characteristics

The table below shows RAK18000 digital microphone module acoustic and electrical characteristics:

| Symbol            | Description                            | Min. | Nom.  | Max. | Unit  |
| ----------------- | -------------------------------------- | ---- | ----- | ---- | ----- |
| V<sub>DD</sub>    | Supply Voltage                         | 1.6  | 3.3   | 3.6  | V     |
| I<sub>DD</sub>    | Current consumption in normal mode     | -    | 650   | -    | µA    |
| I<sub>ddPdn</sub> | Current consumption in power-down mode | -    | -     | 5    | µA    |
| AOP               | Acoustic Overload Point                | -    | 122.5 |      | dBSPL |
| SNR               | Signal-to-Noise Ratio                  | -    | 64    | -    | dB    |
| Clock             | Input clock frequency                  | 1.2  | 2.4   | 3.25 | MHz   |
| T<sub>op</sub>    | Operating temperature range            | -40  | -     | +85  | °C    |

#### Mechanical Characteristic

##### Board Dimensions

Figure 4 shows the dimensions and the mechanical drawing of the RAK18000 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18000/datasheet/rak18000_mechanic_drawing.png" 
  caption="RAK18000 PDM Stereo Microphone Module Mechanical Drawing" 
  width="60%"
/>

##### WisConnector PCB Layout

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18000/datasheet/mxxs1003k6m.png" 
  caption="WisConnector PCB footprint and recommendations" 
  width="100%"
/>

#### Schematic Diagram

##### WisConnector Connection

Figure 6 shows the WisConnector connection and the digital microphone data line connected to **IO3** and the clock line connected to **IO4**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18000/datasheet/wisio-connection.png" 
  figureCount="6"
  caption="RAK18000 PDM Stereo Microphone Module Connection" 
   width="80%"
/>

##### Digital Microphone

Figure 7 shows the schematic of RAK18000. The two digital microphones, left or right channel, can be switch through R6, R7, R8, and R9.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak18000/datasheet/digital-microphone.png" 
  caption="RAK18000 PDM Stereo Microphone Module Schematic" 
  width="100%"
/>

<RkBottomNav/>