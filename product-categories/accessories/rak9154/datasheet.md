---
slug: /product-categories/accessories/rak9154/datasheet/
title: RAK9154 Solar Battery Datasheet
description: Provides comprehensive information about your RAK9154 Solar Battery to help you in using it. This information includes technical specifications, characteristics, and requirements.
image: "https://images.docs.rakwireless.com/accessories/rak9154/rak9154.png"
keywords:
 - RAK9154
 - Solar Battery
 - Datasheet
 - Accessories
 - Power Supply
sidebar_label: Datasheet
---

# RAK9154 Solar Battery Datasheet

## Overview

### Description

The RAK9154 Solar Battery is created especially to power RAK Sensor Hub or provide backup power for the WisGate Edge Pro V2 and Prime V2. Designed to provide an eco-friendly and sustainable power solution, this innovative device utilizes a small but powerful solar panel and integrates a 5.2 Ah battery, and a solar charge controller in one compact unit.

### Features

- Battery capacity: 5200 mAh
- Operating temperature: -20～60° C
- Dimensions: 180 x 130 x 60 mm
- Outputs: one 12 V<sub>DC</sub> output for Sensor Hub; one 9-12 V<sub>DC</sub> output for WisGate Edge Pro/Prime
- Integrated BMS and heater
- Supported mounting pole diameter: 55～80 mm

## Specifications

### Overview

> **Image:** RAK9154 Solar Battery Overview

| Parameter                        | Value                                                                         | Notes                                  |
| -------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------- |
| Cell type                        | Rechargeable Lithium-Ion                                                      |                                        |
| Nominal capacity                 | 5200 mAh                                                                 | 5.2 Ah                            |
| Rated voltage                    | 10.8 V                                                                   | Single cell voltage 3.6 V         |
| Operating voltage range          | 9～13.2 V                                                                |Output 1 – if SensorHub is connected – 12V DC 
Output 1 and 2 – if used with other devices, the connected device should withstand a voltage of up to 16 V DC. |
| Rated energy                     | 56.16 Wh                                                                 |                                        |
| SOC transportation range         | 50%                                                                           |                                        |
| Operating temperature            | Charging temperature: 0～45° C
Discharge temperature: -20～60° C |                                        |
| Storage temperature              | -20～55° C                                                               | Longer than three months at 25° C |
| Working humidity                 | 20～80% RH                                                               |                                        |
| PV input                         | 18 V / 1.0 A                                                        | Typical                                |
| Max PV input voltage             | 30 V                                                                     | Open-circuit voltage max               |
| Max charging  continuous current | 0.25 C (1.3 A)                                                      | Limited by the solar charger           |
| Max discharge continuous current | 0.6 C (3.12 A)                                                      |                                        |
| Dimensions (L, W, H)             | 180 x 130 x 60 mm (±3 mm)                                           |                                        |

### Hardware

#### Dimensions and External Surface Requirements

The appearance of the RAK9154 battery system is shown in **Figure 2**. The battery system consists of two groups of 2600 mAh cells connected in serial and one BMS board which integrated 18 V input solar charger.

The appearance of the assembly has no obvious processing flaws or bumps, no cracks on the surface, and no burrs on the weld.

> **Image:** RAK9154 Dimensions and interfaces

#### Electrical Characteristics

> **Image:** RAK9154 Electrical diagram

:::tip NOTE
For reference only, this module does not contain a sampling wiring harness.
:::

> **Image:** RAK9154 Wiring diagram

#### Panel Connector Definition

| Connector       | Connector Socket Model | Connector Plug Type | Definition                                             | Note                                                                |
| --------------- | ---------------------- | ------------------- | ------------------------------------------------------ | ------------------------------------------------------------------- |
| Gateway Load    | SP1110/P4              | SP1110/P4-N         | Pin1: P+; Pin2: P-; Pin3: RS485A; Pin4: RS485B         | SP11; IP67; Rate current 2 A; Contact diameter 0.75 mm*4  |
| Sensor Hub Load | SP1110/P5              | SP1110/P5-N         | Pin1: P+; Pin2: P-; Pin3: TXD; Pin4: 3V3_In; Pin5: RXD | SP11;  IP67; Rate current 2 A; Contact diameter 0.75 mm*5 |
| PV INPUT        | SP1110/P2              | SP1110/P2-N         | Pin1: PV+; Pin2: PV-                                   | SP11; IP67; Rate current 1 A; Contact diameter 1.0 mm*2   |

#### Environmental Requirements

##### Standard Experiment Condition

Unless otherwise stated, all specifications are performed under the following environmental conditions:

- Temperature: 25±3° C
- Humidity: 65±20% RH

:::note
This guide covers winter operation for RAK solar and battery systems. For deployment-specific instructions, refer to [Winter Deployment Guide](https://downloads.rakwireless.com/Accessories/RAK9155/RAK%20Winter%20Operational%20Guidance%20for%20Battery%20and%20Solar%20Systems.pdf).
:::

#### Transportation and Storage

##### Transportation Requirements

During transportation, the battery should be protected from severe vibration, shock, sun, and rain. It should not be inverted to avoid short circuits from happening. During the loading and the unloading process, it should be handled gently to prevent falling, rolling, heavy pressure, and inversion.

##### Storage Requirements

The module is stored in an incompletely charged state, typically around 40% SOC. Product storage environment requirements are as follows:

- **Storage temperature:** Storage time < 3 months, then stored at -20 ~ 55° C, 40% SOC; Storage time > 3 months, then 0 ~ 25° C, 40% SOC.
- **Storage humidity:** Humidity is 2 ~ 90% RH, it is recommended to store in the range of no more than 85% RH.
- **Storage environment:** The product should be stored in a clean, ventilated, and cool environment, avoiding direct sunlight, high temperature, corrosive gas, severe vibration, mechanical shock, and heavy pressure; away from heat source; altitude is less than 1500 meters, atmospheric pressure is 86~106 kPa.
- **Maintenance:** In a dry and ventilated environment, recharging is required once a month during storage. The maintenance test method during product storage is as follows: Under normal temperature conditions, the product should be charged and discharged once a month with standard charging. If the module is expected to be stored for more than 30 days, the SOC will be adjusted to 40% after the charging is completed.

:::warning
This product must comply with the operating instructions. Any installation, maintenance, and use of this product must strictly comply with the relevant safety regulations.

- Do not store or use at high temperatures, and must be kept away from heat. These environments above the safe temperature range can cause significant degradation in the performance and life of the product, and even cause serious consequences such as burning and explosion.
- Storage and use in environments with high static or high electromagnetic radiation are prohibited. Otherwise, the electronic components in this product may be damaged, which may cause safety hazards.
- Do not get it wet or even soak it in water. Otherwise, it may cause internal short circuits, loss of function, or abnormal chemical reactions of the product, and cause fire, smoke, explosion, and other accidents.
- If you find any abnormalities such as smoke, high heat, discoloration or deformation, while in use, storage, transportation, and service, you should contact the professional department immediately to further observe and control the risks.
- Do not dispose discarded products in fire or hot furnaces. Waste batteries should be recycled and recycling should be done by professional agencies or organizations.
- Do not let the product carry heavy load or pressure. It should not be stacked on top of each other.
- Although this battery is not a high-pressure energy storage device, non-professionals, and improper operation and use may still cause serious consequences such as burning and explosion. The installation and maintenance of the battery system must be operated by professional technicians. Its usage must strictly abide by the relevant safety regulations; non-professionals are strictly prohibited to install, repairing battery systems and abuse.
:::

## Certification

### Certifications
- **CE:** https://downloads.rakwireless.com/Accessories/RAK9154/Certification/RAK9154_CE_Certification.pdf
- **FCC:** https://downloads.rakwireless.com/Accessories/RAK9154/Certification/RAK9154_FCC_Certification.pdf
- **ROHS:** https://downloads.rakwireless.com/Accessories/RAK9154/Certification/RAK9154_RoHS_Report.pdf

