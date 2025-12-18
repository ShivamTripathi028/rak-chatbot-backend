---
slug: /product-categories/wisnode/solar-radiation-monitoring/datasheet/
title: Solar Radiation Monitoring Solution Datasheet
description: Provides comprehensive information about your Sensor Hub Solar Radiation solution to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
keywords:
  - datasheet
  - wisnode
  - sensor hub
image: https://images.docs.rakwireless.com/wisnode/solar-radiation-monitoring/solarsolution.png
sidebar_label: Datasheet
---

# Solar Radiation Monitoring Solution Datasheet

## Solution Overview

### Description

The Solar Radiation Sensor Solution combines the RAK Sensor Hub with the RK200-03 Solar Pyranometer Radiation Sensor, making it well-suited for monitoring solar activity in weather stations, solar installations, and agriculture. Equipped with a temperature compensation circuit, the sensor ensures accurate data by minimizing ambient temperature effects.

With the plug-and-play feature of the Sensor Hub, the Solar Radiation Sensor Solution comes with pre-installed components ready for easy installation and connection. The sensor provides highly accurate solar radiation readings, with the Sensor Hub collecting and transmitting the data via LoRaWAN or NB-IoT/CAT M1.

The Sensor Hub’s connectivity function allows for versatile data transmission to the cloud using the two most commonly used communication protocols in IoT. This versatility ensures that data is readily available for storage, visualization, and in-depth analysis, enabling informed decision-making based on comprehensive knowledge of solar radiation levels.

### Features

- Supports LoRa® and NB -IoT/LTE CAT-M wireless communication modes
- Support LoRa frequency band: CN470, EU868, IN865, RU864, US915, AU915,  KR920, and AS923-1/2/3/4
- Easy to configure, and the network access configuration can be completed through the WisToolBox app on mobile devices.
- Comply with WMO standards
- Suitable for harsh environments
- Low power consumption
- External DC power supply (optional)
- Solar panel power supply (optional)
- Long transmission distance
- High sensitivity
- Easy to install

## Hardware Specifications

### Sensor Hub Specifications

If you need detailed information about the Sensor Hub, including technical specifications and features, refer to the [Sensor Hub Datasheet](https://docs.rakwireless.com/product-categories/wisnode/rak2560/hub-datasheet#overview) page.

### Sensor Probe IO + Solar Radiation Sensor Specifications

**Sensor Probe IO Datasheet** 

- For details, refer to the [Probe IO Datasheet](https://docs.rakwireless.com/product-categories/wisnode/rak2560/probe-io-datasheet#overview).

**Model 485 Solar Radiation Sensor Datasheet**

| Parameter                            | Value                                                       |
|--------------------------------------|-------------------------------------------------------------|
| Spectral Range                       | 300 - 3200 nm                                          |
| Measuring Range                      | 0 - 2000 W/m2                                          |
| Measuring angle                      | 2π solid angle                                              |
| Nonlinearity (precision)             | < ± 2 %                                                |
| Response Time                        | ≤ 20 seconds (99 %)                               |
| Zero Drift (temperature drift: 5k/h) | ± 5 W/m2                                               |
| Cosine Correction                    | ≤ ± 7 % (solar altitude angle = 10 °)             |
| Temperature Effect                   | ± 2 % (- 10° C ~ 40° C)                          |
| Power Supply                         | 5 V, 12 ~ 24 V<sub>DC</sub>                       |
| Output                               | 0 ~ 20 mV, 0 ~ 5 V, 4 ~ 20 mA, RS485, SDI-12 |
| Sensitivity                          | 7 - 14 μV * W - 1 * m2                                 |
| Internal Resistance                  | 350 Ω                                                  |
| Stability                            | ± 2 %/year                                             |
| Operating Temperature                | - 40° C ~ 80° C                                   |
| Storage Conditions                   | 10° C ~ 60° C @ 20 % - 90 %RH           |
| Recalibration Interval               | 2 years                                                |
| Desiccant                            | Silica gel desiccant                                        |
| Shell                                | Aluminum alloy instrument box                               |
| Dimensions                           | ø 185 * 120 mm                                         |
| Weight (excluding packaging)         | 2.5 kg                                                 |
| Mounting bracket (optional)          | Horizontal bracket or adjustable angle bracket              |
| IP Rating                            | IP65                                                        |

### Solar Cell System Specifications

#### Definition of Terms

**List of Abbreviations**

| Abbreviation | Definition                  |
|--------------|-----------------------------|
| BMS          | Battery Management System   |
| BMU          | Battery Management Unit     |
| BOL          | Begin of Life               |
| Bus-bar      | Battery Pole Connecting Rod |
| CMC          | Cell Manager Circuit        |
| EOL          | End of Life                 |
| HV           | High Voltage                |
| LV           | Low Voltage                 |
| OCV          | Open Circuit Voltage        |
| SOC          | Stage of charge             |

**Terminologies**

| Terminology     | Definition                                                                                                                                                                                                                                                                                                            |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Battery Cell    | Commonly known as a battery. It is the fundamental unit of energy storage, which converts chemical energy to electrical energy.                                                                                                                                                                                       |
| Battery Module  | Intermediate energy storage unit, comprising several individual cells and circuitry components, along with electrical and communication interfaces.                                                                                                                                                                   |
| Battery Pack    | A comprehensive power system consisting of multiple battery modules and circuits working together to supply power to electrical devices.                                                                                                                                                                              |
| Rated Voltage   | Refers to the approximate voltage value that a battery is designed to operate at or provide.                                                                                                                                                                                                                          |
| Capacity        | The amount of electrical charge that a fully charged battery can store and subsequently provide to a device or system. It is typically measured in ampere-hours (Ah).                                                                                                                                                 |
| Energy Capacity | The total amount of energy that a fully charged battery can deliver under specific conditions. It is typically measured in watt-hours (Wh) or kilowatt-hours (kWh).                                                                                                                                                   |
| Rated Capacity  | The minimum capacity that a fully charged battery can deliver at the beginning of its life (BOL), typically measured under specific conditions such as a discharge rate of 1C (discharge C-rate).                                                                                                                     |
| Units           | **V**: Volt, voltage
**A**: Ampere, current
**Ah**: Ampere-hour, charge
**Wh**: Watt-hour, electrical energy
**Ω**: Ohm, resistance
**° C**: degrees Celsius, temperature
**mm**: millimeter, length
**s**: seconds, time 
**kg**: kilogram, weight
**Hz**: Hertz, frequency |

#### Main Specifications 

| Parameter                              | Specifications                                                                                  | Remark                                                                           |
|----------------------------------------|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Battery Model                          | RAK9154                                                                                         |                                                                                  |
| Battery Cell Model                     | Rechargeable cylindrical lithium-ion battery H18650CH                                           | H18650CH or equivalent product.                                                  |
| Rated Capacity                         | 5200 mAh                                                                                   |                                                                                  |
| Rated Voltage                          | 10.8 V                                                                                     | Single battery voltage 3.6 V                                                |
| Operating Voltage Range                | 9 V ~ 12.6 V                                                                            |                                                                                  |
| Rated Power                            | 56.16 Wh                                                                                   |                                                                                  |
| SOC Transportation Range               | 50 %                                                                                       |                                                                                  |
| Operating Temperature                  | Charging temperature: 0° C ~ 45° C
Discharge temperature: -20° C ~ 60° C    |                                                                                  |
| Storage Temperature                    | -20° C ~ 60° C                                                                          | More than three months @25° C                                               |
| Operating Humidity                     | 20~80° %RH                                                                                 |                                                                                  |
| PV Input                               | 18° V/1.0° A                                                                          | Typical                                                                          |
| Maximum PV Input Voltage               | 30 V                                                                                       | Open circuit voltage                                                             |
| Maximum Continuous Charging Current    | 0.2 C (1.0 A)                                                                         | Limited by solar charger                                                         |
| Maximum Continuous Discharging current | 0.4 C (2.0 A)                                                                         |                                                                                  |
| ∆ Voltage                              | ≤20 mV                                                                                     | SOC 30 % ~ 60 %; rest for at least 2 hours after charging or discharging |
| Weight                                 | 0.85 Kg                                                                                    |                                                                                  |
| Size                                   | Length: 180 (±3) mm
Width: 130 (±3) mm
Height: 60 (±3) mm |                                                                                  |

#### Interfaces

##### Battery System Structure

The RAK9154 battery system is depicted in Figure 1. This battery system comprises two sets of three 2600mAh battery cells connected in series, accompanied by a BMS board that integrates an 18 V input solar charger.

> **Image:** RAK9154 battery system

#### Electrical Characteristics

> **Image:** RAK9154 electrical schematic diagram

> **Image:** System circuit schematic diagram

| Connector | Connector Socket Model | Connector Plug Model | Definition | Remark |
| --- | --- | --- | --- | --- |
| Gateway Load | SP1110/P4 | SP1110/P4-N | Pin1: P+ | SP11IP67Rated current 2 AContact diameter 0.75 mm * 4 |
| Gateway Load | SP1110/P4 | SP1110/P4-N | Pin2: P- | SP11IP67Rated current 2 AContact diameter 0.75 mm * 4 |
| Gateway Load | SP1110/P4 | SP1110/P4-N | Pin3: R485A | SP11IP67Rated current 2 AContact diameter 0.75 mm * 4 |
| Gateway Load | SP1110/P4 | SP1110/P4-N | Pin4: RS485B | SP11IP67Rated current 2 AContact diameter 0.75 mm * 4 |
| Sensor Hub Load | SP1110/P5 | SP1110/P5-N | Pin1: P+ | SP11IP67Rated current 2 AContact diameter 0.75 mm * 4 |
| Sensor Hub Load | SP1110/P5 | SP1110/P5-N | Pin2: P- | SP11IP67Rated current 2 AContact diameter 0.75 mm * 4 |
| Sensor Hub Load | SP1110/P5 | SP1110/P5-N | Pin3: TXD | SP11IP67Rated current 2 AContact diameter 0.75 mm * 4 |
| Sensor Hub Load | SP1110/P5 | SP1110/P5-N | Pin4: 3V3_In | SP11IP67Rated current 2 AContact diameter 0.75 mm * 4 |
| Sensor Hub Load | SP1110/P5 | SP1110/P5-N | Pin5: RXD | SP11IP67Rated current 2 AContact diameter 0.75 mm * 4 |
| PV Input | SP1110/P2 | SP1110/P2-N | Pin1: PV+ | SP11IP67Rated current 1 AContact diameter 0.75 mm * 4 |
| PV Input | SP1110/P2 | SP1110/P2-N | Pin1: PV- | SP11IP67Rated current 1 AContact diameter 0.75 mm * 4 |

#### Sensor Characteristics

The following table shows the sensor data definition and the data format of the Solar Radiation Solutions.

- **Sensor Dara Definitions**

| Sensor Name | Sensor Type | Data Length | Ratio | Range | Unit            |
|-------------|-------------|-------------|-------|-------|-----------------|
| Pyranometer | 0xC3        | 2           | 1     | 0-200 | W/m<sup>2</sup> |

- **Data Format**

| ID (Channel) | Type   | Data    |
|--------------|--------|---------|
| 1 Byte       | 1 Byte | 2 Bytes |

With the defined data, here's how to interpret the payload received data:

- **Data Example**

Payload (hexadecimal) received data is: `01 C3 00 12`

| ID (Channel) | Type | Data |
|--------------|------|------|
| 01           | C3   | 0012 |

`01C3` (Pyranometer) - `0012` (Data)

Convert the value to decimal:

````
00 12 (hex) = 18 (10 dec)
18 × 1 (conversion coefficient) = 18 W/m2
````

#### Environmental Requirements

##### Transportation Requirements

:::warning
- When transporting the battery, avoid severe vibrations, shaking, and exposure to sunlight or rain. 
- Do not invert the battery to prevent potential short circuits. 
- During loading and unloading, exercise caution to prevent the battery from falling, rolling, enduring heavy pressure, or being inverted. 
:::

##### Storage Requirements

Store the module in a partially charged state, typically around 40% state of charge (SOC). Ensure the storage environment meets the following requirements:

**Temperature and Humidity**

| Parameter   | Description                                              | Remark                                              |
|-------------|----------------------------------------------------------|-----------------------------------------------------|
| Temperature | -30° C to 50° C  
 0° C to 25° C | Time period < 3 months 
 Time period > 3 months |
| Humidity    | 2 %RH to 90 %RH                                | < 85 % Recommended                             |

- **Storage Environment**: Store the product in a clean, ventilated, and cool environment, avoiding direct sunlight, high temperatures, corrosive gases, severe vibration, mechanical shaking, and heavy pressure. Keep the product away from heat sources and store it at an altitude below 1500 meters, maintaining atmospheric pressure between 86 kPa and 106 kPa.

- **Maintenance**: Charge and discharge the device once a month while storing it at room temperature or in a dry and ventilated environment. If storing the device takes more than 30 days, adjust the SOC to 40 % after charging. If the module is expected to be stored for more than 30 days, adjust the State of Charge (SOC) to 40 % after charging is completed.

The operation of the product must adhere to the provided operating instructions. Installation, maintenance, and usage of this product must strictly comply with relevant safety regulations.

:::warning
-	Avoid storing or using the product in high-temperature environments, and keep it away from heat sources. Temperatures outside the safe range can significantly reduce the performance and lifespan of the product, and may even cause serious consequences such as combustion and explosion.
-	Do not store or use the product in environments with high static electricity or high electromagnetic radiation. Doing so may damage the electronic components of the battery, leading to safety hazards.
-	Avoid exposing the battery to water or immersing it in water. Otherwise, it may result in internal short circuits, loss of function, or abnormal chemical reactions, leading to fire, smoke explosion, and other incidents.
-	If you notice any smoking, heating, discoloration, deformation, or any other abnormalities during the use, storage, transportation, and service of the product, contact a professional immediately for assistance.
-	Do not discard waste batteries in fires or incinerators. Waste batteries should be recycled by professional institutions or organizations.
-	It is strictly prohibited to place heavy objects on the product or stack them on top of each other.
-	Although this module is not a high-voltage energy storage device, improper operation and use of the device may lead to serious consequences such as combustion and explosion. 
-	Only professional technicians must handle the installation and maintenance of the battery system. All operations must strictly adhere to relevant safety regulations. Non-professionals are strictly prohibited from installing, maintaining, and misusing the battery system.
:::

