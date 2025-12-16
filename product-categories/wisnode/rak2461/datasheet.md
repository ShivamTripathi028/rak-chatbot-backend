---
slug: /product-categories/wisnode/rak2461/datasheet/
title: RAK2461 WisNode Bridge IO Lite Datasheet
description: Provides comprehensive information about your RAK2461 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisnode/rak2461/datasheet/rak2461.png"
keywords:
  - datasheet
  - RAK2461
  - wisnode
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK2461 WisNode Bridge IO Lite Datasheet

## Overview

### Description

The **RAK2461 WisNode Bridge IO Lite** bridges different Digital Inputs, Outputs (Relay), and RS-485 communication to LoRaWAN® for industrial applications. The device relays data using the LoRaWAN network as a means of wirelessly transmitting to and from the end devices.

It is an ideal solution for seamless LoRaWAN communication within industrial environments. Engineered with industrial-grade reliability and based on the RAK3172-T LoRaWAN module, the RAK2461 ensures long-range connectivity, even in extreme temperatures from -20°&nbsp;C to +70°&nbsp;C.

This device can operate on all LoRaWAN bands within the standard parameters set by the LoRa Alliance. It offers versatile mounting options for easy installation in any environment, whether for industrial automation or smart city infrastructure. Together with a <a href="https://docs.rakwireless.com/product-categories/wisgate/" target="_blank"> RAK Gateway </a>, building a wireless industrial system or extending an existing one can be easy and quick. Moreover, the RAK2461 offers unparalleled performance and durability.

The device comes in two variants:

| Model   | Variants        | Description                                                          |
|---------|-----------------|----------------------------------------------------------------------|
| RAK2461 | RS485-DIx4-DOx1 | One RS485 interface, four digital inputs(DI), one digital output(DO) |
| RAK2461 | RS485-DOx4      | One RS485 interface, four digital outputs(DO)                        |


### Features

- **Regional Parameters Version:** RP001-1.0.3
- **LoRaWAN 1.0.3** protocol stack
- **Class support:** Class C
- One (1) **RS-485 host port**
- Four (4) **Relay NC/NO port** (optional)
- Four (4) **Photocoupler DI ports** and one (1) **Relay NC/NO port** (optional)
- **Power input:** 9&nbsp;V ~ 24&nbsp;V
- **Power output:** 9&nbsp;V ~ 24&nbsp;V (depending on the input)
- Based on the RAK3172-T module
- Wall and DIN rail mounting

## Specifications

### Main Specifications

| Parameter               | Specifications                                                                                                                                                                                                       |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LoRa Feature            | Regional Parameters Version: RP001-1.0.3 <br/> Protocol stack: LoRaWAN 1.0.3 <br/> Frequency: EU868 / IN865 / RU864 / US915 / AU915 / KR920 / AS923 / CN470 <br/> LoRaWAN mode: Class C <br/> Tx power: 22&nbsp;dBm |
| RS485 Feature           | Data rate: 9600 <br/> Carrying capacity: Up to 32 devices <br/> Protection:  <br/> 18&nbsp;kV HBM protection <br/> 13&nbsp;kV IEC61000-4-2 contact discharge <br/> 4&nbsp;kV IEC61000-4-4 fast transient burst       |
| Power Supply            | 9-24 VDC input <br/> 5&nbsp;V for USB Type-C                                                                                                                                                                         |
| Input Voltage           | 9&nbsp;V ~ 24&nbsp;V                                                                                                                                                                                                 |
| Output Voltage          | 9&nbsp;V ~ 24&nbsp;V (depending on the input)                                                                                                                                                                        |
| Rated Power             | DI type: 1&nbsp;W <br/> DO type (Relay): 2&nbsp;W                                                                                                                                                                    |
| Configuration Interface | USB Type-C                                                                                                                                                                                                           |
| LED Indicator           | Power LED <br/> Data LED                                                                                                                                                                                             |
| Antenna                 | RP-SMA external omnidirectional LoRa antenna                                                                                                                                                                         |
| Ingress Protection      | IP31                                                                                                                                                                                                                 |
| Enclosure Material      | Metal                                                                                                                                                                                                                |
| Dimensions              | 93.6&nbsp;mm × 100.3&nbsp;mm × 24&nbsp;mm                                                                                                                                                                            |
| Operating Conditions    | Operating Temperature: -20°&nbsp;C to +70°&nbsp;C <br/>Storage temperature: -20°&nbsp;C to +70°&nbsp;C <br/>Operating humidity: 0 - 90%&nbsp;RH <br/>Storage humidity: 0 - 90%&nbsp;RH                               |
| Installation method     | Wall or DIN rail                                                                                                                                                                                                     |



### Hardware

The hardware specification describes the device's interfaces and parameters.

#### Interfaces

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2461/datasheet/rak2461_top.png"
  caption="RAK2461 WisNode Bridge IO Lite interfaces top (DO and DI)"
  width="70%"
/>

##### Power Interfaces

RAK2461 WisNode Bridge IO can be powered by a DC power supply (9&nbsp;V ~ 24&nbsp;V) through the Vin, the voltage must be stable. This power supply also used to power sensors or devices connected to the Vout.

| Interfaces | Description                                                                                          |
|------------|------------------------------------------------------------------------------------------------------|
| Vin        | Stable voltage input: 9&nbsp;V ~ 24&nbsp;V                                                           |
| GND        | Ground, Vin and GND form a voltage input loop                                                        |
| Vout       | Voltage output: 9&nbsp;V ~ 24&nbsp;V (depending on the input) <br/> Vout output is controlled by MCU |
| GND        | Ground, Vout and GND form a voltage output loop                                                      |

##### Console

The USB type-C port of the device is used for configuration. For configuration purposes, the device can also be powered by the Console port. But type-C port will not provide power to sensors or devices connected to the Vout (J4/pin3).

##### Reset

 Press Reset button to restart the device. 

##### LED Indicators

| LEDs | Status Indication Description                                        |
|------|----------------------------------------------------------------------|
| PWR  | Static on - System works. PWR is controlled by MCU.                  |
| Data | Flicker - Data is being transferred <br/> Off - No data transmission |

##### LoRa

LoRa antenna interface. RP-SMA external omnidirectional antenna.

#### Data Interfaces

- **RS-485 interface**: RS-485 master baud rate is 9600. Multiple devices can be connected, but for more than 5 devices the recommended length is 30 m.
- **Relay (DO)**: The maximum voltage is 240 V. You can choose between NC and NO based on the use case. (DC - 30&nbsp;V / 3&nbsp;A, AC - 250&nbsp;V / 3&nbsp;A).
- **Photocoupler (DI)**: By default, DI supports Dry Contact. If Wet Contact is required, you can contact RAK technical support. The maximum input voltage should be 5&nbsp;V and the DI COM should be connected to the negative pole. 

##### RAK2461-RS485-DOx4

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2461/datasheet/rak2461_bottom_1.png"
  caption="RAK2461 WisNode Bridge IO Lite interfaces bottom (RS485-DOx4)"
  width="70%"
/>

| Interfaces            | Description                                                   |
|-----------------------|---------------------------------------------------------------|
| RS485_A               | RS485 Data +                                                  |
| RS485_B               | RS485 Data -                                                  |
| DO1 / DO2 / DO3 / DO4 | NO: Normally Open <br/> COM: Common <br/> NC: Normally Closed |
| GND                   | Ground                                                        |
| 12&nbsp;V_Out         | Voltage output: 12&nbsp;V / 500&nbsp;mA                       |

##### RAK2461-RS485-DIx4-DOx1

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak2461/datasheet/rak2461_bottom_2.png"
  caption="RAK2461 WisNode Bridge IO Lite interfaces bottom (RS485-DIx4-DOx1)"
  width="70%"
/>

| Interfaces            | Description                                                   |
|-----------------------|---------------------------------------------------------------|
| RS485_A               | RS485 Data +                                                  |
| RS485_B               | RS485 Data -                                                  |
| DI1 / DI2 / DI3 / DI4 | IN: Signal input <br/> COM: Common                            |
| DO                    | NO: Normally Open <br/> COM: Common <br/> NC: Normally Closed |
| 5&nbsp;V_Out          | Voltage output: 5&nbsp;V / 500&nbsp;mA                        |
| GND                   | Ground                                                        |
| 12&nbsp;V_Out         | Voltage output: 12&nbsp;V / 500&nbsp;mA                       |



## Models/Bundles

| Model       | RS-485 | Relay (DO) | Photocoupler (DI) |
|-------------|:------:|:----------:|:-----------------:|
| RAK2461-X01 |   ✓    |   ✓ (4x)   |                   |
| RAK2461-X11 |   ✓    |     ✓      |      ✓ (4x)       |

## Certification

<RkCertificationIcons certifications={[
    {
        'ce': 'https://downloads.rakwireless.com/LoRa/RAK2461/Certification/RAK2461_CE_Certification.pdf',
    },
    {
        'fcc': 'https://downloads.rakwireless.com/LoRa/RAK2461/Certification/RAK2461_FCC_Certification.pdf',
    },
    {
        'ised': 'https://downloads.rakwireless.com/LoRa/RAK2461/Certification/RAK2461_ISED_Certification.pdf',
    }
]} />

<RkBottomNav/>