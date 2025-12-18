---
slug: /product-categories/wisnode/water-temperature/datasheet/
title: Water Temperature Monitoring Solution Datasheet
description: Water Temperature Monitoring Solution offers an effective tool for monitoring Water Temperature values, comprising the RAK Sensor Hub and Water Temperature sensor JXBS-3001-SW-RS.
keywords:
  - datasheet
  - Sensor Hub Solutions
  - Water Temperature
image: https://images.docs.rakwireless.com/wisnode/water-temperature/water-temperature.png
sidebar_label: Datasheet
---

# Water Temperature Monitoring Solution Datasheet

## Solution Overview

### Description

The Water Temperature Monitoring Solution is built with RAK Sensor Hub and JXBS-3001-SW-RS Water Temperature Sensor. This comprehensive monitoring system is well-suited for various applications, including cold storage, pharmaceutical factory GMP monitoring, and HVAC systems.

With the plug-and-play feature of the Sensor Hub, the Water Temperature Monitoring Solution comes with pre-installed components ready for easy installation and connection. The sensor provides highly accurate water temperature readings with the Sensor Hub collecting and transmitting the data via LoRaWAN or NB-IoT/CAT M1.

The Sensor Hub’s connectivity function allows for versatile data transmission to the cloud using the two most commonly used communication protocols in IoT. This versatility ensures that data is readily available for storage, visualization, and in-depth analysis, enabling informed decision-making based on comprehensive knowledge of water temperature levels.

### Features

- Support LoRa® and NB-IoT/ LTE CAT-M wireless communication modes
- Support LoRa frequency bands: CN470, EU868, IN865, RU864, US915, AU915, KR920, and AS923-1/2/3/4
- Easy to install and configure
- Configurable network access with the WisToolBox mobile app
- Long Service Life
- High precision
- Exd IICT6 explosion-proof rating
- High-strength structural design
- Support solar panel and 12 V<sub>DC</sub> power adapter for power supply

## Specifications

### Sensor Hub Specifications

For details, refer to the [RAK2560 WisNode Sensor Hub Datasheet](https://docs.rakwireless.com/product-categories/wisnode/rak2560/hub-datasheet/#description).

### Sensor Probe IO + Water Temperature Datasheet

**Sensor Probe IO Datasheet**

- Refer to the [Probe IO Datasheet](https://docs.rakwireless.com/product-categories/wisnode/rak2560/io-datasheet/#overview) for more details.

**Water Temperature Sensor Datasheet**

| PART/PARAMETER NAME | PARAMETER CONTENT |  |
| --- | --- | --- |
| Transmitter | DC Power Supply | 12 V DC - 24 V DC |
| Transmitter | Power Consumption | ≤ 0.15 W(12 V DC 25° C) |
| Transmitter | Output Signal | RS485 |
| Transmitter | Response Time | ≤ 10 s |
| Transmitter | Working Temperature | - 20 ~ 50° C |
| Transmitter | Working Humidity | 0 ~ 95 % RH |
| Transmitter | Working Pressure | 0.9 - 1.1 atm |
| Transmitter | Dimensions | 110 mm × 85 mm × 44 mm |
| Probe | Measurement Range | - 55 ~ 125° C |
| Probe | Temperature Resolution | 0.1° C |
| Probe | Precision | ± 0.5° C |
| Probe | Response Time | ≤ 15 s |
| Probe | Cable Length | 5 m |

### Solar Cell System Datasheet

#### Definition of Terms

**List of Abbreviations**

| Abbreviation | Definition |
| --- | --- |
| BMS | Battery Management System |
| BMU | Battery Management Unit |
| BOL | Begin of Life |
| Bus-bar | Battery Pole Connecting Rod |
| CMC | Cell Manager Circuit |
| EOL | End of Life |
| HV | High Voltage |
| LV | Low Voltage |
| OCV | Open Circuit Voltage |
| SOC | State of charge |

**Terminologies**

| Terminology | Definition |
| --- | --- |
| Battery Cell | Commonly known as a battery. It is the fundamental unit of energy storage, which converts chemical energy to electrical energy. |
| Battery Module | The intermediate energy storage unit comprises several individual cells, circuitry components, and electrical and communication interfaces. |
| Battery Pack | A comprehensive power system consisting of multiple battery modules and circuits working together to supply power to electrical devices. |
| Rated Voltage | Refers to the approximate voltage value that a battery is designed to operate at or provide. |
| Capacity | The amount of electrical charge that a fully charged battery can store and subsequently provide to a device or system. Unit: Ampere-hours (Ah) |
| Energy Capacity | The total amount of energy that a fully charged battery can deliver under specific conditions. Unit: Watt-hours (Wh) or kilowatt-hours (kWh) |
| Rated Capacity | At the beginning of life (BOL), the minimum capacity that a fully charged battery can provide at a discharge rate of 1 C (discharge C-rate). |
| Unit | V : Volt, voltage |
| Unit | A : Ampere, current |
| Unit | Ah : Ampere-hour, electric charge |
| Unit | Wh : Watt-hour, electrical energy |
| Unit | Ω : Ohm, resistance |
| Unit | ° C : Celsius, temperature |
| Unit | mm : millimeter, length |
| Unit | s : second, time |
| Unit | kg : kilogram, weight |
| Unit | Hz : Hertz, frequency |

#### Main Specifications

| Parameter | Technical Specifications | Remark |
| --- | --- | --- |
| Battery Model | RAK9154 |  |
| Battery Cell Model | Rechargeable cylindrical lithium-ion battery H18650CH | H18650CH or products of the same level |
| Rated Capacity | 5200 mAh | 5.2 Ah |
| Rated Voltage | 10.8 V | Single cell voltage 3.6 V |
| Operating Voltage Range | 9 V～12.6 V |  |
| Rated Power | 56.16 Wh |  |
| SOC Transportation Range | 50% |  |
| Operating Temperature | Charging temperature: 0° C ~ 45° C |  |
| Operating Temperature | Discharging temperature: -20° C ~ 60° C |  |
| Storage Temperature | -20° C ~ 60° C | Over 3 months @ 25° C |
| Operating Humidity | 20 ~ 80%RH |  |
| PV input | 18 V/1.0 A | Typical |
| Maximum PV Input Voltage | 30 V | Open circuit voltage |
| Maximum Charging Continuous Current | 0.2 C (1.0 A) | Limited by solar chargers |
| Maximum Discharge Continuous Current | 0.4 C (2.0 A) |  |
| ∆ Voltage | ≤20 mV | Rest for at least 2 hours after charging or discharging |
| Weight | 0.85 Kg |  |
| Size | Length: 180 (±3) mm Width: 130 (±3) mm Height: 60 (±3) mm |  |

#### Interfaces

##### Battery System Structure

As shown in **Figure 1**, the RAK9154 battery system comprises two sets of three 2600 mAh battery units connected in series. The system also incorporates one (1) BMS board integrated with an 18 V input solar charger.

> **Image:** RAK9154 battery system

#### Electrical Characteristics

> **Image:** RAK9154 electrical diagram

> **Image:** System circuit schematic

| Connector | Connector Socket Model | Connector Plug Model | Definition | Remark |
| --- | --- | --- | --- | --- |
| Gateway Load | SP1110/P4 | SP1110/P4-N | Pin1: P+ | SP11 IP67 Rated current 2 A Contact diameter 0.75 mm * 4 |
| Gateway Load | SP1110/P4 | SP1110/P4-N | Pin2: P- | SP11 IP67 Rated current 2 A Contact diameter 0.75 mm * 4 |
| Gateway Load | SP1110/P4 | SP1110/P4-N | Pin3: R485A | SP11 IP67 Rated current 2 A Contact diameter 0.75 mm * 4 |
| Gateway Load | SP1110/P4 | SP1110/P4-N | Pin4: RS485B | SP11 IP67 Rated current 2 A Contact diameter 0.75 mm * 4 |
| Sensor Hub Load | SP1110/P5 | SP1110/P5-N | Pin1: P+ | SP11 IP67 Rated current 2 A Contact diameter 0.75 mm * 4 |
| Sensor Hub Load | SP1110/P5 | SP1110/P5-N | Pin2: P- | SP11 IP67 Rated current 2 A Contact diameter 0.75 mm * 4 |
| Sensor Hub Load | SP1110/P5 | SP1110/P5-N | Pin3: TXD | SP11 IP67 Rated current 2 A Contact diameter 0.75 mm * 4 |
| Sensor Hub Load | SP1110/P5 | SP1110/P5-N | Pin4: 3V3_In | SP11 IP67 Rated current 2 A Contact diameter 0.75 mm * 4 |
| Sensor Hub Load | SP1110/P5 | SP1110/P5-N | Pin5: RXD | SP11 IP67 Rated current 2 A Contact diameter 0.75 mm * 4 |
| PV Input | SP1110/P2 | SP1110/P2-N | Pin1: PV+ | SP11 IP67 Rated current 1 A Contact diameter 0.75 mm * 4 |
| PV Input | SP1110/P2 | SP1110/P2-N | Pin1: PV- | SP11 IP67 Rated current 1 A Contact diameter 0.75 mm * 4 |

#### Sensor Characteristics

The following table shows the sensor data definition and the data format of the Water Temperature Monitoring Solution.

- **Sensor Data Definitions**

| Register Name     | Function Code | Register Address | Data Length | Sensor Code | Unit     | Resolution   | Range             | Precision |
|-------------------|---------------|------------------|-------------|-------------|----------|--------------|-------------------|-----------|
| Water Temperature | 0x03          | 0x0000           | 2           | 0x67        | ° C | 0.01° C | -55 ~ 125° C | 0.1       |

- **Data Format**

| Sensor Data Unit  | ID (Channel) | Type   | Data    |
|-------------------|--------------|--------|---------|
| Water Temperature | 1 Byte       | 1 Byte | 2 Bytes |

With the defined data, here's how to interpret the payload received data:

**Data Sample 1:**

Payload (hex) received data: `156700fc`

| Sensor Data Unit  | ID (Channel) | Type | Data |
|-------------------|--------------|------|------|
| Water Temperature | 15           | 67   | 00fc |

Convert the sensor data from hexadecimal to decimal:

- **Wind Speed**: `1567`
- **Data**: `00fc`

```
00fc (hex) = (0 × 16³) + (0 × 16²) + (15 × 16¹) + (12 × 16⁰) = 252₁₀
252 x 0.01 (conversion factor) = 25.2° C
```

#### Environmental Requirements

##### Transportation Requirements

:::warning
- When transporting the battery, avoid severe vibrations, shaking, and exposure to sunlight or rain. 
- Do not invert the battery to prevent potential short circuits. 
- During loading and unloading, exercise caution to prevent the battery from falling, rolling, enduring heavy pressure, or being inverted.
:::

##### Storage Requirements

Store the module in a partially charged state, typically around 40 % state of charge (SOC). Ensure the storage environment meets the following requirements:

**Temperature and Humidity**

| Parameter | Value | Remark |
| --- | --- | --- |
| Temperature | -30° C to 50° C, 40% SOC | Storage time < 3 months |
| Temperature | 0° C to 25° C, 40% SOC | Storage time > 3 months |
| Humidity | 2%RH to 90%RH | < 85% Recommended |

- **Storage Environment**: Store the product in a clean, ventilated, and cool environment. Avoid direct sunlight, high temperatures, corrosive gasses, severe vibration, mechanical shock, and heavy pressure. Keep it away from heat sources and store below 1,500 meters altitude, with the atmospheric pressure between 86 kPa and 106 kPa.

- **Maintenance**: Charge and discharge the device once a month while storing it at room temperature or in a dry and ventilated environment. If storing the device takes more than 30 days, adjust the SOC to 40 % after charging.

The operation of the product must adhere to the operating instructions. Installation, maintenance, and use of the product must strictly comply with relevant safety regulations.

:::warning
- Avoid storing or using the product in high-temperature environments and keep it away from heat sources. Temperatures outside the safe range can significantly reduce the performance and lifespan of the product and may even cause serious consequences such as combustion and explosion. 
- Do not store or use the product in environments with high static electricity or high electromagnetic radiation. Doing so may damage the electronic components of the battery, leading to safety hazards.
- Avoid exposing the battery to water or immersing it in water. Otherwise, it may result in internal short circuits, loss of function, or abnormal chemical reactions, leading to fire, smoke explosion, and other incidents.
- If you notice any smoking, heating, discoloration, deformation, or any other abnormalities during the use, storage, transportation, and service of the product, contact a professional immediately for assistance.
- Do not discard waste batteries in fires or incinerators. Waste batteries should be recycled by professional institutions or organizations.
- It is strictly prohibited to place heavy objects on top of the product or stack them on top of each other. 
- Although this module is not a high-voltage energy storage device, improper operation and use of the device may lead to serious consequences such as combustion and explosion. 
- Only professional technicians must handle the installation and maintenance of the battery system. All operations must strictly adhere to relevant safety regulations. Non-professionals are strictly prohibited from installing, maintaining, and misusing the battery system.
:::

