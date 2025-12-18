---
slug: /product-categories/wisnode/rak2560/probe-io-datasheet/
title: RAK2560 WisNode Sensor Hub Probe IO Datasheet
description: Provides comprehensive information about your RAK2560 WisNode Probe IO to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisnode/rak2560/rak2560.jpg"
keywords:
    - datasheet
    - wisnode
    - rak2560
    - sensor probe io
    - sensor hub
sidebar_label: Probe IO Datasheet
---

# RAK2560 WisNode Sensor Probe IO Datasheet

## Overview

### Description

The **Probe IO** is an accessory for the Sensor Hub solution platform. It supports modules with various communication protocols like RS-485, SDI-12, 4-20 mA signal, and DI/DO. This accessory can work with RAKwireless modules to ensure the best solution for your project.

:::tip NOTE
- The Probe IO could not be used as a standalone product. You need the <a href="https://store.rakwireless.com/products/sensor-hub?utm_source=RAK2560WisNodeSense&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAK2560 WisNode Sensor Hub</a> in order to use this probe.
:::

### Product Features

- Support one RS-485 device<sup>[1]</sup>
- Support one SDI-12 device<sup>[1]</sup>
- Support one 4-20 mA device<sup>[1]</sup>
- Support two DO (dry contact)<sup>[1]</sup>
- Support one DI<sup>[1]</sup>
- Supply 5 V / VIN / 24 V (0.5 A) power
- One-wire protocol<sup>[1]</sup>
- Waterproof (IP67-rated for the probe body)

:::tip NOTE
<sup>[1]</sup> - Custom or 3rd party sensors cannot be connected to the Probe IO Sensor Hub. If the desired sensor is not available in the <a href="https://store.rakwireless.com/collections/sensorhub-solution?utm_source=RAK2560WisNodeSense&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">SensorHub Solutions</a>, reach us at <a href="mailto:support@rakwireless.com" target="_blank">support@rakwireless.com</a> and we will check the compatibility of your desired sensor. 
:::

## Specifications

### Overview

#### Dimensions

The **Probe IO** dimensions are 74 x 33 x 26 mm. There is one physical port for connection to the Sensor Hub with a 50 cm cable length. The **Probe IO** is IP67-rated and suitable for outdoor use. The device is designed to meet the UL/EN60950-22 standard.

> **Image:** RAK2560 WisNode Probe IO dimensions

#### Block Diagram

RAK2560's **Probe IO** uses MCU STM32L051C8 for a control center. The **Probe IO** supports four (4) types of device interfaces and DI/DO to control or monitor the working environment directly.

> **Image:** RAK2560 WisNode Probe IO block diagram

### Hardware

The hardware specification is categorized into four (4) parts. It shows the pinouts of the Probe IO and their corresponding functions and diagrams. It also covers the power supply and environmental characteristics that include the tabular data of the functionalities and standard values of the RAK2560 WisNode Probe IO.

#### Pin Definition

##### Connector (Sensor Hub Side)

> **Image:** RAK2560 WisNode Probe IO connector

| Pin No. | Name          | Type | Description                   | Remarks                                                       |
|---------|---------------|------|-------------------------------|---------------------------------------------------------------|
| 1       | Vin           | PI   | 12 V<sub>DC</sub> supply | Input 5~16 V                                             |
| 2       | GND           | -    | Ground                        | -                                                             |
| 3       | Reserved      | IO   | Not defined                   | Reserved for future use                                       |
| 4       | Vcc_Probe     | PI   | Power supply for the probe    | 3.3 V<sub>DC</sub> support mode; 3.4 V battery mode |
| 5       | One-wire UART | IO   | Communication with probe      |                                                               |

##### Probe IO PCBA

> **Image:** RAK2560 WisNode Probe IO PCBA pin definition

| J1     | Name      | Description            |
|--------|-----------|------------------------|
| Pin 14 | 485_A+    | RS-485 port            |
| Pin 15 | 485_B-    | RS-485 port            |
| Pin 16 | UART1_TX  | MCU UART-TX            |
| Pin 17 | UART1_RX  | MCU UART-RX            |
| Pin 18 | GND       | -                      |
| Pin 19 | GND       | -                      |
| Pin 20 | 4-20mA_IN | 4-20 mA analog in |
| Pin 21 | GND       | -                      |
| Pin 22 | GPIO1     | MCU GPIO               |
| Pin 23 | GPIO2     | MCU GPIO               |
| Pin 24 | GPIO3     | MCU GPIO               |
| Pin 25 | GND       | -                      |
| Pin 26 | SDI-12_IN | -                      |

| J6     | Name      | Description             |
|--------|-----------|-------------------------|
| Pin 1  | DO0_OUT   | Dry contact out         |
| Pin 2  | DO0_COM   | Dry contact common      |
| Pin 3  | DO1_OUT   | Dry contact out         |
| Pin 4  | DO1_COM   | Dry contact common      |
| Pin 5  | DI        | Dry contact in          |
| Pin 6  | DI_COM    | Dry contact common      |
| Pin 7  | DC3v3_OUT | Supply 150 mA      |
| Pin 8  | GND       | -                       |
| Pin 9  | GND       | -                       |
| Pin 10 | VIN       | Adapter power           |
| Pin 11 | GND       | -                       |
| Pin 12 | DC24V     | Supply current 1 A |
| Pin 13 | 5V0       | Supply current 1 A |

##### Standard Type for Probe IO

> **Image:** RAK2560 WisNode Probe IO SP11 device side

| Type   | Pin 1         | Pin 2 | Pin 3 | Pin 4   | Pin 5     |
|--------|---------------|-------|-------|---------|-----------|
| RS-485 | VIN/24 V | GND   | NC    | B-      | A+        |
| SDI-12 | VIN/24 V | GND   | NC    | NC      | Data      |
| 4-20   | VIN/24 V | GND   | NC    | NC      | Signal-in |
| DO     | VIN/24 V | GND   | NC    | DO0_COM | DO0_OUT   |
| DI     | VIN/24 V | GND   | NC    | DI_COM  | DI        |

#### Power Supply

The **Probe IO** must be supplied through the 3.4 ~ 3.6 V SP11 Pin 4 from the main body of the Sensor Hub. The module's power is only supplied through the VIN / 24 V of SP11 Pin 1.

##### Power Consumption

| Mode        | Condition        | Min         | Typical     | Max         |
|-------------|------------------|-------------|-------------|-------------|
| Active mode | Read sensor data | 3.2 mA | 3.5 mA | 3.6 mA |
| Sleep mode  | Sleep mode       | 40 uA  | 60 uA  | 90 uA  |

#### Environmental Requirements
##### Operating Conditions

| Parameter                    | Min         | Typical     | Max         |
|------------------------------|-------------|-------------|-------------|
| Normal operating temperature | –30° C | +25° C | +80° C |

#### Sensor Connection Diagram

The **RAK2560** can support both Sensor Probes and Probe IO in all possible combinations.

:::tip NOTE
If you buy a Probe IO sensor solution like the soil moisture sensor, you will need a Probe IO to connect it with the Sensor Hub. To integrate an additional Probe IO into your configuration, the Sensor Hub requires an external 12 V<sub>DC</sub> power supply. It cannot operate on batteries.
:::

> **Image:** RAK2560 WisNode Probe IO connection schematics

### Certification

### Certifications
- **CE:** https://downloads.rakwireless.com/LoRa/SensorHub/Certification/SensorHub_RAK2560_RAK2560C_CE_Certification.pdf
- **FCC:** https://downloads.rakwireless.com/LoRa/SensorHub/Certification/SensorHub_RAK2560_RAK2560C_FCC_Certification.pdf
- **ISED:** https://downloads.rakwireless.com/LoRa/SensorHub/Certification/SensorHub_RAK2560_RAK2560C_ISED_Report.pdf

