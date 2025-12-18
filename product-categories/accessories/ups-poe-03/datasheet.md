---
slug: /product-categories/accessories/ups-poe-03/datasheet/
title: UPS PoE-03 Datasheet
description: Provides comprehensive information about your UPS PoE-03 to help you use it. This information includes technical specifications, characteristics, and battery information.
image: "https://images.docs.rakwireless.com/accessories/ups-poe-03/1.ups-poe-03.png"
keywords:  
 - UPS-PoE-03
 - datasheet
sidebar_label: Datasheet
---

# UPS PoE-03 Datasheet

## Overview

### Description

The UPS PoE-03 is a specialized Uninterruptible Power Supply (UPS) device designed specifically for Power over Ethernet (PoE) applications, providing backup power and protection to PoE-powered devices. It has useful features such as surge protection, voltage regulation, and intelligent battery management. It also has intelligent adapter power capability detection and overcurrent buck control.

When the output current exceeds the rated current, the output voltage drops and the output power is adjusted; when the output current exceeds 5% of the rated current, the overcurrent protection is triggered.

This product provides power to the RAK7268 Indoor Gateway and the RAK7289 Outdoor Gateway without requiring a main power supply.

### Features

- Input：100-240 V<sub>AC</sub> (50~60 Hz)
- Output:
  - 48 V<sub>DC</sub> 0.23 A
  - 9~12 V<sub>DC</sub> 3 A
  - 5 V<sub>DC</sub> 1.5 A
- Offers intelligent recognition of adapter power capability
- Supports overcurrent buck regulation
- Supports adjustment of small current charging based on voltage drop switching, with small switching changes and short switching time
- Supports low battery warning signal for lithium batteries, external power supply, or lithium battery power supply warning signal
- The internal lithium battery pack has comprehensive protection against overcharging, discharging, overcurrent, short circuit
- Support hardware, MCU control, and other multiple protection
- Net Weight：265 g
- Dimension: 105 x 105 x 27.5 mm

## Specifications

### Overview

> **Image:** UPS PoE-03 function diagram

### Hardware

#### Interfaces

> **Image:** UPS PoE-03 parts

| Number | Label                                                      |
| ------ | ---------------------------------------------------------- |
| 1      | Working Indicator                                          |
| 2      | Power On/Off Switch                                        |
| 3      | Charging Indicator                                         |
| 4      | 110-240 V<sub>AC</sub> Power Input port               |
| 5      | 5 V<sub>DC</sub> 1.5 A Output port               |
| 6      | 9~12 V<sub>DC</sub> 3 A Output port              |
| 7      | LAN IN                                                     |
| 8      | 48.0 V<sub>DC</sub> 0.23 A Output port (LAN OUT) |

| Port                                  | Specification                            |
| ------------------------------------- | ---------------------------------------- |
| Input Port AC 110 V ~ 240 V | US/EU/UK 8 digit-character AC power port |
| Output no-load voltage                | 5.5 x 2.5 mm DC Female connector    |
| Average output conversion efficiency  | 5.5 x 2.5 mm DC Female connector    |
| Output current                        | RJ45 (LAN OUT)                           |

##### LED Indicator Status

| LED | Status              |
| --- | ------------------- |
| 🟢   | Device is ON.       |
| 🔴   | Device is charging. |

- Short press the switch button turns on/off the device.
- No input: Shuts down when the battery voltage falls 9 V
- No external input: Battery voltage below 9 V shuts down output. Green light turns off.
- Charging the device turns on the red LED and automatically turns off when it's full charged.

#### Electrical Characteristics

| Item                                 | Min.       | Typical                                                                                                         | Max.       | Unit |
| ------------------------------------ | ---------- | --------------------------------------------------------------------------------------------------------------- | ---------- | ---- |
| Power input port voltage             | 110 V | 220 V                                                                                                      | 240 V | V    |
| Output no-load voltage               | 5 V   | 5 V + 9 V + 12 V + 48 V                                                                     | 48 V  | V    |
| Average output conversion efficiency | -          | ≥85%                                                                                                            | -          | -    |
| Output current                       | -          | 48 V<sub>DC</sub> 0.23 A 
 9~12 V<sub>DC</sub> 3 A 
 5 V<sub>DC</sub> 1.5 A | -          | -    |

#### Battery Information

##### Li-Ion Battery Protection Characteristics

| Item | Symbol | Description | Standard |
| --- | --- | --- | --- |
| Overcharge protection | V DET1 | Overcharge monitoring voltage | 4.25±0.05 V |
| Overcharge protection | tV DET1 | Overcharge detection delay time | 700～1300 ms |
| Overcharge protection | V REL1 | Overcharge release voltage | 4.15±0.08 V |
| Over-discharge protection | V DET2 | Over-discharge detection voltage | 2.40±0.2 V |
| Over-discharge protection | tV DET2 | Over-discharge detection delay time | 80～170 ms |
| Overcurrent protection | V DET3 | Overcurrent detection voltage | 0.20±0.025V |
| Overcurrent protection | I DP | Overcurrent protection current | 3~6 A |
| Overcurrent protection | tV DET3 | Detection delay time | 8~12 ms |
| Overcurrent protection | - | Protection release condition | Disconnect the load |
| Short-circuit protection | - | Protection condition | External circuit short circuit |
| Short-circuit protection | T SHORT | Detection delay time | ≤12 us |
| Short-circuit protection | - | Protection release condition | Disconnect the short circuit |
| Lithium battery Internal resistance | R DS | Main circuit on-state resistance | VC = 4.2 V；RDS≤60 mΩ |
| Current consumption | I DD | Internal circuit consumption during operation | IDD≤30.0 μA |

#### Battery Working & Storage Conditions

| Description                                       | Temperature               |
| ------------------------------------------------- | ------------------------- |
| Lithium battery charging working environment      | 0° C ~ +45° C   |
| Lithium battery discharging working environment   | 0° C ~ +45° C   |
| Battery capacity in 40% ~ 60% storage for 30 days | -20° C ~ +45° C |
| Battery capacity in 40% ~ 60% storage for 90 days | -20° C ~ +35° C |

:::tip NOTE
- Low-temperature environments reduce discharge capacity.
- If the UPS POE-03 is not used for an extended period of time, it should be fully charged and stored in a cool, dry place, and it should be charged once every 3~5 months.
:::

