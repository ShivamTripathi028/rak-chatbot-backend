---
title: RAK9003 PoE Pi HAT Datasheet
description: Provides comprehensive information about your RAK9003 PoE Pi HAT to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wishat/rak9003/rak9003.png"
keywords:
    - datasheet
    - wishat
    - RAK9003 PoE Pi HAT
sidebar_label: Datasheet
---

# RAK9003 PoE Pi HAT Datasheet

## Overview

### Description

The **RAK9003 PoE Pi HAT** is an add-on board with a Raspberry PI form factor, compatible with RPi 3B+ and RPi4 which can be plugged into a Raspberry Pi directly. The RAK9003 PoE Pi HAT makes it possible to power the Raspberry Pi via a standard CAT 5 Ethernet cable.

The RAK9003 PoE Pi HAT is designed to be compatible with the IEEE 802.3af/at Power-over-Ethernet (PoE). It is compatible with both PoE Mode A and Mode B. The RAK9003 PoE Pi HAT signature and control circuit provides the PoE AT compatibility signature and power classification required by the Power Sourcing Equipment (PSE) before applying up to 30 W power to the port. The RAK9003 PoE Pi HAT is compatible with Class 0 to Class 4 equipment. The high efficiency DC/DC converter operates over a wide input voltage range and provides a regulated low ripple and low noise output. The DC/DC converter also has built-in overload and short-circuit output protection.

### Key Features

- Raspberry Pi form factor with a 40-pin compatible header (**Pi3 B+, Pi4** compatible)
- Conforming to the IEEE 802.3af/at (mode A & mode B), **25W max load**
- Contains physical layer power negotiation circuitry, compatible with **Class 0 to Class 4 equipment**
- Wide operating voltage: **42 V ~ 57 V**
- Output Current: **5 V @ 5 A**
- Output voltage ripple: **200 mVPP**
- High Efficiency: **83% (input 48 V, 5 V @ 5 A)**
- High isolation: **1.5 kV isolation** input to output
- **Overcurrent / short-circuit** protection
- **RoHS Compliant**
- Operating Temperature: **-40° C ～+85° C**

## Specifications

### Overview

The overview covers only the block diagram of the RAK9003 PoE Pi HAT.

#### Block Diagram

> **Image:** RAK9003 PoE Pi HAT Block Diagram

### Hardware

The hardware specification shows the pinouts of the RAK9003 and its corresponding functions. It also presents the parameters and the standard values of the board.

#### Pin Definition

> **Image:** RAK9003 PoE HAT Pinout Diagram

| **Pin No.** | **Name**  | **Description**  |
| ----------- | --------- | ---------------- |
| 1           | NC        | No Connection    |
| 2           | +5 V | +5 V Output |
| 3           | NC        | No Connection    |
| 4           | +5 V | +5 V Output |
| 5           | NC        | No Connection    |
| 6           | GND       | GND              |
| 7           | NC        | No Connection    |
| 8           | NC        | No Connection    |
| 9           | GND       | GND              |
| 10          | NC        | No Connection    |
| 11          | NC        | No Connection    |
| 12          | NC        | No Connection    |
| 13          | NC        | No Connection    |
| 14          | GND       | GND              |
| 15          | NC        | No Connection    |
| 16          | NC        | No Connection    |
| 17          | NC        | No Connection    |
| 18          | NC        | No Connection    |
| 19          | NC        | No Connection    |
| 20          | GND       | GND              |
| 21          | NC        | No Connection    |
| 22          | NC        | No Connection    |
| 23          | NC        | No Connection    |
| 24          | NC        | No Connection    |
| 25          | GND       | GND              |
| 26          | NC        | No Connection    |
| 27          | NC        | No Connection    |
| 28          | NC        | No Connection    |
| 29          | NC        | No Connection    |
| 30          | GND       | GND              |
| 31          | NC        | No Connection    |
| 32          | NC        | No Connection    |
| 33          | NC        | No Connection    |
| 34          | GND       | GND              |
| 35          | NC        | No Connection    |
| 36          | NC        | No Connection    |
| 37          | NC        | No Connection    |
| 38          | NC        | No Connection    |
| 39          | GND       | GND              |
| 40          | NC        | No Connection    |

#### Electrical Characteristics

##### Typical Characteristics

> **Image:** Noise VIN = 42 V, IO = 5 A, 5~20 MHz Bandwidth

> **Image:** Transient Response, VIN = 42 V IO = 50% ~ 100% ~ 50%

> **Image:** Noise VIN = 48 V, IO = 5 A, 5~20 MHz Bandwidth

> **Image:** Transient Response, VIN = 48 V, IO = 50% ~ 100% ~ 50%

> **Image:** Noise VIN = 57 V, IO = 5 A, 5~20 MHz Bandwidth

> **Image:** Transient Response VIN = 57 V, IO = 50% ~ 100% ~ 50%

> **Image:** Power Down VIN = 42 V, C1: Output Voltage, C2: PSE Out, C3: Input Current, ILoad = 100% IO max

> **Image:** Short-Circuit Output, VIN = 42 V

> **Image:** Power Down VIN = 48 V, C1: Output Voltage, C2: PSE Out, C3: Input Current, ILoad = 100% IO max

> **Image:** Short-Circuit Output, VIN = 48 V

> **Image:** Power Down, VIN = 57 V, C1: Output Voltage, C2: PSE Out, C3: Input Current, ILoad = 100% IO max

> **Image:** Short-Circuit Output VIN = 57 V

> **Image:** Efficiency

> **Image:** Power Dissipation

> **Image:** Startup form 56 V 802.3at PSE, C1: Output Voltage, C2: PSE Out, C3: Input Current, ILoad = 100% IO max

> **Image:** Derating Curve

##### Operating Conditions

The table below lists the operation voltage and temperature ranges:

| Parameter             | Description       | Min.        | Typical     | Max.        |
| --------------------- | ----------------- | ----------- | ----------- | ----------- |
| Input Voltage         | Input DC Voltage  | 42 V   | 48 V   | 57 V   |
| Output Voltage        | Output DC voltage | 4.9 V  | 5.0 V  | 5.1 V  |
| Operating Temperature | Temperature Range | -40° C | +25° C | +85° C |

##### Maximum ESD

The table below lists the maximum ESD:

| Parameter                    | Min | Typical | Max       | Remarks                                      |
| ---------------------------- | --- | ------- | --------- | -------------------------------------------- |
| ESD sensitivity for all pins | -   | -       | 1 kV | Human Body Model according to JESD22-A114    |
| ESD immunity for ANT1        | -   | -       | 4 kV | Contact Discharge according to IEC 61000-4-2 |
| -                            | -   | -       | 8 kV | Air Discharge according to IEC 61000-4-2     |

:::tip NOTE
The module is an Electrostatic Sensitive Device and requires special precautions when handling.
:::

