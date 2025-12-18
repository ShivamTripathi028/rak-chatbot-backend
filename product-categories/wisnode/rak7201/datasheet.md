---
slug: /product-categories/wisnode/rak7201/datasheet/
title: RAK7201 WisNode Button 4K Datasheet
description: Provides comprehensive information about your RAK7201 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisnode/rak7201/datasheet/rak7201.png"
keywords:
  - datasheet
  - RAK7201
  - wisnode
sidebar_label: Datasheet
---

# RAK7201 WisNode Button 4K Datasheet

## Overview

### Description

The **RAK7201 WisNode Button 4K** is a remote wireless trigger device. It supports user-defined functions for each key and is based on the LoRaWAN 1.0.2 protocol. Supported LoRaWAN bands are IN865, EU868, AU915, US915, KR920, and AS923.

This WisNode Button is suitable for a variety of Smart Home applications. Including, but not limited to, entertainment system control, control of lights, a snooze button for the alarms, or a remote trigger. A device with long-range wireless connectivity, amazing battery life, and four programmable buttons. There are tons of applications this device can fit into.

> **Image:** RAK7201

### Features

- 4 Buttons with LED indicator
- **Product Size:** 43 x 57 x 15 mm
- **LoRaWAN** 1.0.2 compatible
- **Battery:** 350 mAh
- **Battery working time:** 1 year (Rechargeable)
- **Power Consumption:** Transmit: 77.4-153* mA, Standby: 4.8 uA
- **Operating Temperature:** -20° C to 60° C
- **Working Environment:** Indoor

*transmit current depends on factors such as transmit power, SF, and Payload Length

## Specifications

### Overview

| Parameter             | Value                     |
| --------------------- | ------------------------- |
| LoRa protocol         | LoRaWAN 1.0.2 Class A     |
| LoRa TX power         | 20 dBm max           |
| LoRa RX sensitivity   | -136 dBm             |
| LoRa antenna          | Spring antenna            |
| Battery capacity      | 350 mAh              |
| Charge current        | 500 mA/ 5 V     |
| Battery lifetime      | 1 year                    |
| Sleep current         | 4.8 uA               |
| Operating temperature | -20° C to 60° C |
| Dimensions            | 43 x 57 x 15 mm      |
| Mounting              | Sticker                   |

> **Image:** Deployment Scenario

### Hardware

The hardware specification covers the parameters of the RAK7201 in terms of electrical and supported LoRaWAN frequency parameters.

#### RF Characteristics

| Parameter           | Value                 |
| ------------------- | --------------------- |
| LoRa protocol       | LoRaWAN 1.0.2 Class A |
| LoRa TX power       | 20 dBm max       |
| LoRa RX sensitivity | -136 dBm         |
| LoRa Antenna        | Spring antenna        |

The RAK7201 supports different LoRaWAN frequency bands for different country regions.

| Region        | Frequency Band Common Name (MHz) |
| ------------- | -------------------------------- |
| Europe        | EU868                            |
| India         | IN865                            |
| North America | US915                            |
| Australia     | AU915                            |
| Asia          | AS923                            |
| Korea         | KR920                            |

#### Actuators

> **Image:** RAK7201 buttons and LED

- **Buttons**

RAK7201 has 4 buttons, which all can be configured to execute defined functionality. The stock firmware is configured to send the buttons ID number via a LoRa frame, whenever one is pressed.

- **LEDs**
1. Blue LEDs

There are four blue LEDs, one per button, which light when a press occurs.

| Status                    | Function                                          |
| ------------------------- | ------------------------------------------------- |
| Flash once                | The button is pressed.                            |
| Flash twice               | The server received button information correctly. |
| Four LEDs flash clockwise | Joining the network.                              |
| Four LEDs flash for 1s    | Joining to the network is successful.             |
| Four LEDs are lit up      | RAK7201 is in configuration mode.                 |

2. Red LED on button 2

The red LED on Button 2 indicates the charging status of the RAK7201.

| Status | Function                     |
| ------ | ---------------------------- |
| on     | The battery is charging.     |
| off    | The battery is not charging. |

3. Red LED on button 4

The red LED on button 4 indicates the network related information.

| Status                                 | Function                       |
| -------------------------------------- | ------------------------------ |
| Flash for 1s                           | Joining to the network failed. |
| Flash for 1s after a button is pressed | Not connected to the network.  |
| Flash twice                            | Transmission failed.           |

#### Interfaces

RAK7201 has a standard Micro USB port on the side, that adheres to the USB 2.0 specification. This port is used as both configuration interface and for charging the battery.

#### Electrical Characteristics

The following are the electrical characteristics of RAK7201 WisNode Button 4K. For specific details regarding a project, [contact us](mailto:support@rakwireless.com).

Power consumption:

| Parameter            | Value      | Unit |
| -------------------- | ---------- | ---- |
| Transmitting current | 77.4-153\* | mA   |
| Standby current      | 4.8        | uA   |

\*transmit current depends on factors as transmit power, SF and payload length.

#### Battery Specification

The RAK7201 comes with a 350 mAh rechargeable LiPo battery inside. In need of replacement, adhere to the specification.

| Parameter               | Value                                    | Unit |
| ----------------------- | ---------------------------------------- | ---- |
| Nominal Battery Voltage | 3.7                                      | V    |
| Nominal capacity        | 350                                      | mAh  |
| Temperature range       | -20º~60º (discharge), 15º-45º (charging) | C    |
| Battery dimensions      | 5.7 x 21 x 37.5                          | mm   |

### Firmware

| Model   | Version | Source                                                                                          |
| ------- | ------- | ----------------------------------------------------------------------------------------------- |
| RAK7201 | V1.0.2  | [Download](https://downloads.rakwireless.com/LoRa/RAK7201/Firmware/RAK7201_Latest_Firmware.zip) |

#### Working Modes

The WisNode Button 4K supports LoRaWAN. LoRaWAN supported modes are OTAA and ABP network mode. Class A communication.

### Models/Bundles

| Model   | Description                                                 |
| ------- | ----------------------------------------------------------- |
| RAK7201 | 4 keys LoRaWAN button (EU868/IN865/AU915/US915/KR920/AS923) |

## Certification

