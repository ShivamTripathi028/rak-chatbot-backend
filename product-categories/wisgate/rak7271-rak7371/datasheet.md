---
slug: /product-categories/wisgate/rak7271-rak7371/datasheet/
title: RAK7271/RAK7371 WisGate Developer Base Datasheet
description: Comprehensive datasheet for RAK7271/RAK7371 WisGate Developer Base, a device designed to convert mPCIe LoRa concentrator modules into USB Type-C pluggable LoRaWAN gateways for seamless integration.
image: "https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/rak7271-rak7371.png"
keywords:
    - RAK7271
    - RAK7371
    - WisGate Developer Base
    - mPCIe LoRa concentrator
    - LPWAN integration
    - LoRaWAN Gateway
    -  Outdoor Gateway
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK7271/RAK7371 WisGate Developer Base Datasheet

## Overview

### Description

The RAK Developer Base is a device designed for integration with desktop, mobile, or embedded systems. It enables the RAK2287 or RAK5146 mPCIe LoRa concentrator modules to function as USB Type-C pluggable devices, utilizing the included Type-C to Type-A cable.

This new approach enables easy integration into existing hardware, such as routers and industrial PCs, adding LoRaWAN gateway capabilities. For example, it can transform a laptop into a testbed LoRaWAN gateway by simply plugging it in and running the appropriate software stack.

Equipped with fully functional concentrator modules, it supports 8 uplink channels and 1 downlink channel at SF7–12 (RAK2287) or SF5–12 (RAK5146).

The RAK Developer Base is an ideal solution for LPWAN deployments where integration with existing hardware is crucial, or scenarios when on the go deployment is required, for drive testing or coverage evaluation in mobile scenarios.

This device provides a complete and cost-efficient LoRa gateway solution, offering up to 10 programmable parallel demodulation paths.

### Features

- Compatible with RAK2287(SX1302) / RAK5146(SX1303) concentrator modules with 8 uplink channels and 1 downlink channel.
- 2 x SX125x Tx/Rx front-ends.
- Tx power up to 27&nbsp;dBm, Rx sensitivity down to -139&nbsp;dBm @ SF12, BW 125&nbsp;kHz.
- Supports global license-free frequency band (EU433, CN470, IN865, EU868, US915, AU915, KR920, AS923)
- USB Type C interface port (USB 2.0)


### Package Contents

- 1pc RAK Developer Base
- 1pc USB Type C to A Cable
- 1pc LoRa Antenna (2.3 dBi)

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/datasheet/1.package-contents.png"
  width="70%"
  caption="Package Contents"
/>

## Specifications

### Overview

The RAK7271/RAK7371 WisGate Developer Base consists of four components:

1. RAK2005
2. RAK2287/RAK5146
3. iPEX to RP-SMA female cable
4. Casing

#### Block Diagram

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/datasheet/2.block-diagram.png"
  width="80%"
  caption="WisGate Developer Base Block Diagram"
/>

### Hardware

The hardware specification covers the interfacing of WisGate Developer Base and its corresponding functionalities. It also presents the parameters and the standard values of the board.

#### Interfaces

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/datasheet/3.interfaces.png"
  width="70%"
  caption="WisGate Developer Base Interfaces"
/>

- **Power supply**: There is a 5&nbsp;V to 3.3&nbsp;V DC-DC converter integrated on RAK2005, so the 5&nbsp;V DC that comes from the USB interface is enough for this device.
- **USB Interface**: This device can connect to any USB 2.0 host equipped with compatible drivers. The RAK2287/RAK5146 module inside supports high-speed USB-to-SPI conversion via the STM32L412KBU6. It features a USB 2.0 compliant interface with a maximum data rate of 480&nbsp;Mb/s, serving as the communication interface with an external host application processor.
- **RP-SMA antenna interface**: The modules feature a single RF interface via a standard RPSMA connector with a characteristic impedance of 50&nbsp;Ω. This RF port supports both transmission (Tx) and reception (Rx), serving as the antenna interface.


#### RF Characteristics

##### Operating Frequencies

The WisGate Developer Base supports the LoRaWAN bands in the table below.

| **Region**    | **Frequency (MHz)** |
| ------------- | ------------------- |
| China         | CN470               |
| Russia        | RU864               |
| India         | IN865               |
| Europe        | EU433, EU868        |
| North America | US915               |
| Australia     | AU915               |
| Korea         | KR920               |
| Asia          | AS923               |

##### LoRa RF Characteristics

It is highly recommended to use optimized RSSI calibration values, which is part of the HAL v3.1. For both, Radio 1 and 2, the RSSI-Offset should be set -169.0. The following table gives the typical sensitivity level of the RAK2287 and RAK5146.

| Signal Bandwidth (kHz) | Spreading Factor | Sensitivity (dBm) |
| :--------------------: | :--------------: | :---------------: |
|          125           |        12        |       -139        |
|          125           |        7         |       -125        |
|          250           |        12        |       -136        |
|          250           |        7         |       -123        |
|          500           |        12        |       -134        |
|          500           |        7         |       -120        |


#### Antenna Specifications

##### LoRa Antenna

WisGate Developer Base comes with LoRa Antenna with RP-SMA Male connector, shown in Figure 4.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/datasheet/4.lora-antenna.png"
  width="60%"
  caption="LoRa Antenna"
/>

##### Antenna Dimension

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/datasheet/5.antenna-dimension.png"
  width="70%"
  caption="Antenna Dimension in mm"
/>

##### Antenna Parameters

| Items                              | Specifications                       | Specifications                       |
| ---------------------------------- | :----------------------------------- | ------------------------------------ |
| Frequency Range                    | 863~870&nbsp;MHz                     | 902~928&nbsp;MHz                     |
| Peak Gain                          | 2.8&nbsp;dBi                         | 2.3&nbsp;dBi                         |
| Voltage Standard Wave Ratio (VSWR) | ≤ 1.5                                | ≤ 1.5                                |
| Efficiency                         | > 80%                                | > 80%                                |
| Feed Impedance                     | 50&nbsp;Ω                            | 50&nbsp;Ω                            |
| Working Temperature & Humidity     | T: -30~+75°&nbsp;C, H: 5~95&nbsp;%RH | T: -30~+75°&nbsp;C, H: 5~95&nbsp;%RH |

#### Electrical Requirements

:::warning

- Exceeding one or more of the ratings listed in the Absolute Maximum Rating section may result in permanent damage to the device. These ratings are intended only as stress limits. The device should not be operated at these ratings or under any conditions outside the specified operating conditions.
- Prolonged exposure to Absolute Maximum Rating conditions may impact the device's reliability. The Operating Conditions section defines the range within which the device's functionality is guaranteed. Any application information provided is advisory and does not constitute part of the specification.

:::

##### Absolute Maximum Rating

The limiting values given below are in accordance with the Absolute Maximum Rating System (IEC 134).

| Symbol | Description            | Condition                                   | Min         | Max            |
| ------ | ---------------------- | ------------------------------------------- | ----------- | -------------- |
| 5V     | Device  supply voltage | Input  DC voltage                           | –0.3&nbsp;V | 5.25&nbsp;V    |
| USB    | USB  D+/D- pins        | Input  DC voltage at USB interface pins     | -           | 3.6&nbsp;V     |
| ANT    | Antenna  ruggedness    | Output  RF load mismatch ruggedness at ANT1 | -           | 10:1&nbsp;VSWR |
| Tstg   | Storage  Temperature   | -                                           | –40&nbsp;°C | 85&nbsp;°C     |


:::tip NOTE

The product is not protected against overvoltage or reversed voltages. Voltage spikes exceeding the power supply voltage specification, given in the table above, must be limited to values within the specified boundaries by using appropriate protection devices.

:::

##### Maximum ESD

| Parameter | Typical    | Remarks                                            |
| --------- | ---------- | -------------------------------------------------- |
| ESD       | ±4&nbsp;KV | Indirect Discharge VCP according to IEC 61000-4-2  |
| ESD       | ±4&nbsp;KV | Indirect Discharge HCP according Fto IEC 61000-4-2 |

##### Operating Conditions

| Parameter             | Min         | Typical     | Max         |
| --------------------- | ----------- | ----------- | ----------- |
| Operating temperature | –40&nbsp;°C | +25&nbsp;°C | +85&nbsp;°C |


:::warning

Unless otherwise specified, all operating condition specifications assume an ambient temperature of 25°&nbsp;C. Operation outside the specified conditions is not recommended, and extended exposure to such conditions may impact the device's reliability.

:::

##### Power Supply Range

| Symbol   | Parameter                             | Min         | Typical  | Max         |
| -------- | ------------------------------------- | ----------- | -------- | ----------- |
| 5&nbsp;V | Device supply operating input voltage | 4.75&nbsp;V | 5&nbsp;V | 5.25&nbsp;V |

##### Power Consumption

| Mode             | Condition                                                   | Typical     |
| ---------------- | ----------------------------------------------------------- | ----------- |
| Active Mode (TX) | The power of TX channel is 27&nbsp;dBm and 5&nbsp;V supply. | 365&nbsp;mA |
| Active Mode (RX) | TX disabled and RX enabled.                                 | 66&nbsp;mA  |

#### Environmental Characteristics

| Parameter                   | Min         | Typical     | Max         |
| --------------------------- | ----------- | ----------- | ----------- |
| Operation Temperature Range | -40&nbsp;°C | +25&nbsp;°C | +85&nbsp;°C |

#### Mechanical Characteristics

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/datasheet/6.mechanical-dimension.png"
  width="50%"
  caption="WisGate Developer Base Dimension"
/>
## Models / Bundles

| Product   | Concentrator | GPS | LBT | USB |
| --------- | ------------ | --- | --- | --- |
| RAK7271-Y | RAK2287      |     |     | √   |
| RAK7371-Y | RAK5146      |     |     | √   |


| Parameter            | Variations                                                                             |
| -------------------- | -------------------------------------------------------------------------------------- |
| Y - Supported Region | 1 - EU433; 2 - CN470; 3 - EU868; 4 - US915; 5 - KR920; 6 - AS923; 7 - IN865; 8 - AU915 |

## Certification

<RkCertificationIcons certifications={[
    {
        'ce': 'https://downloads.rakwireless.com/LoRa/RAK7371/Certification/RAK7371_CE_Certification.pdf',
    },
    {
        'fcc': 'https://downloads.rakwireless.com/LoRa/RAK7371/Certification/RAK7371_FCC_and_ISED_Report.pdf',
    },
    {
        'reach': 'https://downloads.rakwireless.com/LoRa/RAK7371/Certification/RAK7371_RAK7271_REACH_Report.pdf',
    },
    {
        'rohs': 'https://downloads.rakwireless.com/LoRa/RAK7371/Certification/RAK7371_RAK7271_RoHS_Report.pdf',
    },


]} />


<RkBottomNav/>