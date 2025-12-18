---
slug: /product-categories/wisnode/water-level-monitoring/datasheet/
title: Water Level Monitoring Solution Datasheet
description: Provides comprehensive information of your Water Level Monitoring Solution to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisnode/water-level-monitoring/water-level-monitoring.png"
keywords:
  - datasheet
  - WisNode
sidebar_label: Datasheet
---

 

# Water Level Monitoring Solution Datasheet

## Solution Overview

### Description

The Water Level Monitor Sensor Solution is an ideal tool for monitoring water levels. It comprises the RAK Sensor Hub and ULB16 sensor, which is suitable for use in various settings, such as hydrology exploration, water tank level measurements, and sewage. 

With the plug-and-play feature of the Sensor Hub, the Water Level Solution comes with pre-installed components ready for easy installation and connection. The sensor provides highly accurate water level readings, with the Sensor Hub collecting and transmitting the data via LoRaWAN or NB-IoT/CAT M1.

The Sensor Hub’s connectivity function allows for versatile data transmission to the cloud using the two most commonly used communication protocols in IoT. This versatility ensures that data is readily available for storage, visualization, and in-depth analysis, enabling informed decision-making based on comprehensive knowledge of water levels.

### Features

- Support LoRaWAN and NB-IoT/LTE CAT-M wireless communication modes
- Support LoRa frequency band: CN470, EU868, IN865, RU864, US915, AU915, KR920, AS923-1/2/3/4
- Wide measurement range: 0~200 mH2O
- Resolution: 0.25% FS
- Easy to install and configure
- Configurable network access with the WisToolBox mobile app
- Pressure diaphragm in the probe
- Reverse polarity and current limiting protections
- Sturdy and durable structure with IP68 protection rating

## Specifications

### Sensor Hub Specifications

For details, refer to the <a href="https://docs.rakwireless.com/product-categories/wisnode/rak2560/hub-datasheet#overview" target="_blank">Sensor Hub Datasheet</a>.

### Sensor Probe IO + Water Level Monitoring Sensor Specifications

**Sensor Probe IO Datasheet**

- For details, refer to the <a href="https://docs.rakwireless.com/product-categories/wisnode/rak2560/probe-io-datasheet" target="_blank">Probe IO Datasheet</a>.

**ULB16 Water Level Sensor Datasheet**

| Parameter | Technical Specifications |
| --- | --- |
| DC Power Supply (default) | 12~36 VDC |
| Electrical Connection | Φ7.6 mm shielded cable with vent hose |
| Measurement Precision | 0.25~0.5% FS |
| Measurement Range | 0~1 mH2O - 200 mH2O |
| Long-Term Stability | < 0.1% FS/year |
| Output Signal | 4-20 mA |
| Operating Temperature | 0~70° C |
| Material of Housing | 304 Stainless Steel |

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
| SOC | Stage of Charge |

**Terminologies**

| Terminology | Definition |
| --- | --- |
| Battery Cell | Commonly known as a battery. It is the fundamental unit of energy storage, which converts chemical energy to electrical energy. |
| Battery Module | Intermediate energy storage unit, comprising several individual cells and circuitry components, along with electrical and communication interfaces. |
| Battery Pack | A comprehensive power system consisting of multiple battery modules and circuits working together to supply power to electrical devices. |
| Rated Voltage | Refers to the approximate voltage value that a battery is designed to operate at or provide. |
| Capacity | The amount of electrical charge that a fully charged battery can store and subsequently provide to a device or system. It is typically measured in ampere-hours (Ah) |
| Energy Capacity | The total amount of energy that a fully charged battery can deliver under specific conditions. It is typically measured in watt-hours (Wh) or kilowatt-hours (kWh). |
| Rated Capacity | The minimum capacity that a fully charged battery can deliver at the beginning of its life (BOL), typically measured under specific conditions such as a discharge rate of 1C (discharge C-rate). |
| Unit | V: Volt, voltage |
| Unit | A: Ampere, current |
| Unit | Ah: Ampere-hour, electric charge |
| Unit | Wh: Watt-hour, electrical energy |
| Unit | Ω: Ohm, resistance |
| Unit | ° C: Celsius, temperature |
| Unit | mm: millimeter, length |
| Unit | s: second, time |
| Unit | kg: kilogram, weight |
| Unit | Hz: Hertz, frequency |

#### Main Specifications

| Parameter | Technical Specifications | Remark |
| --- | --- | --- |
| Battery Model | RAK9154 |  |
| Battery Cell Model | Rechargeable cylindrical lithium-ion battery H18650CH | H18650CH or equivalent product |
| Rated Capacity | 5200 mAh |  |
| Rated Voltage | 10.8 V | Single cell voltage 3.6 V |
| Operating Voltage Range | 9 V ~ 12.6 V |  |
| Rated Power | 56.16 Wh |  |
| SOC Transportation Range | 50% |  |
| Operating Temperature | Charging temperature:0° C ~ 45° CDischarge temperature:- 20° C ~ 60° C |  |
| Storage Temperature | - 20° C ~ 60° C | More than three months @ 25° C |
| Working Humidity | 20 ~ 80%RH |  |
| PV Input | 18 V / 1.0 A | Typical |
| Maximum PV Input Voltage | 30 V | Open circuit voltage |
| Maximum Continuous Charging Current | 0.2 C (1.0 A) | Limited by solar charger |
| Maximum Continuous Discharge Current | 0.4 C (2.0 A) |  |
| ΔVoltage | ≤ 20 mV | SOC 30% ~ 60%; rest for at least 2 hours after charging or discharging |
| Weight | 0.85 kg |  |
| Dimensions | Length: 180 (± 3) mmWidth: 130 (± 3) mmHeight: 60 (± 3) mm |  |

#### Interfaces

##### Battery System Structure

As shown in **Figure 1**, the RAK9154 battery system comprises two sets of three 2600 mAh battery units connected in series. The system also incorporates one (1) BMS board integrated with an 18 V input solar charger.

> **Image:** RAK9154 battery system

#### Electrical Characteristics

> **Image:** RAK9154 electrical diagram

> **Image:** System circuit diagram

**Battery System Panel Connector**

| Connector | Connector Socket Model | Connector Plug Model | Definition | Remark |
| --- | --- | --- | --- | --- |
| Gateway Load | SP1110/P4 | SP1110/P4-N | Pin1: P+ | SP11IP67Rated current 2 AContact diameter 0.75 mm * 4 |
| Gateway Load | SP1110/P4 | SP1110/P4-N | Pin2: P- | SP11IP67Rated current 2 AContact diameter 0.75 mm * 4 |
| Gateway Load | SP1110/P4 | SP1110/P4-N | Pin3: RS485A | SP11IP67Rated current 2 AContact diameter 0.75 mm * 4 |
| Gateway Load | SP1110/P4 | SP1110/P4-N | Pin4: RS485B | SP11IP67Rated current 2 AContact diameter 0.75 mm * 4 |
| Sensor Hub Load | SP1110/P5 | SP1110/P5-N | Pin1: P+ | SP11IP67Rated current 2 AContact diameter 0.75 mm * 5 |
| Sensor Hub Load | SP1110/P5 | SP1110/P5-N | Pin2: P- | SP11IP67Rated current 2 AContact diameter 0.75 mm * 5 |
| Sensor Hub Load | SP1110/P5 | SP1110/P5-N | Pin3: TXD | SP11IP67Rated current 2 AContact diameter 0.75 mm * 5 |
| Sensor Hub Load | SP1110/P5 | SP1110/P5-N | Pin4: 3V3_In | SP11IP67Rated current 2 AContact diameter 0.75 mm * 5 |
| Sensor Hub Load | SP1110/P5 | SP1110/P5-N | Pin5: RXD | SP11IP67Rated current 2 AContact diameter 0.75 mm * 5 |
| PV Input | SP1110/P2 | SP1110/P2-N | Pin1: PV+ | SP11IP67Rated current 1 AContact diameter 1.0 mm * 2 |
| PV Input | SP1110/P2 | SP1110/P2-N | Pin2: PV- | SP11IP67Rated current 1 AContact diameter 1.0 mm * 2 |

#### Sensor Characteristics

**Sensor Data Definition**

| Sensor Name        | Sensor Type | Data Length | Scope | Unit |
|--------------------|-------------|-------------|-------|------|
| Water Level Sensor | 0x01        | 2           | 0 ~ 5 | m    |

**Data Format**

| Water Level Sensor _ Data Unit |  |  |
| --- | --- | --- |
| ID (Channel) | Type | Data |
| 1 byte | 1 byte | 2 bytes |

**Data Sample 1:**

Payload (hex) received data: ***01 02 01 e0***

**Water Level Sensor Data Sample 1**

| Water Level Sensor _ Data Unit |  |  |
| --- | --- | --- |
| ID (Channel) | Type | Data |
| 01 | 02 | 01e0 |

Convert the sensor data from hexadecimal to decimal:

```
0102 (Water Level) - data 01e0
01e0 (hex) = 480 (dec)
0 x 0.01 (conversion coefficient) = 4.8 m/s
```

**Data Conversion** 

**Sample:** 

A current range of 4~20 mA corresponds to a measurement depth range of 0~5 m. The water level is converted using a proportional factor of 3.2 mA ((20-4) mA / (5-0) m) increasing of the current for every 1 meter increase in depth. The monitored current value is 4.8 mA, and the current increases by 4.8-4=0.8 mA. Thus, the calculation method is as follows: 

**Water Level depth** = 0.8 mA/3.2 mA x m = 0.25 m

#### Environmental Requirements

##### Transportation Requirements

:::warning
- When transporting the battery, avoid severe vibrations, shaking, and exposure to sunlight or rain. 
- Do not invert the battery to prevent potential short circuits. 
- During loading and unloading, exercise caution to prevent the battery from falling, rolling, enduring heavy pressure, or being inverted.
:::

##### Storage Requirements

Store the module in a partially charged state, typically around 40% state of charge (SOC). Ensure the storage environment meets the following requirements:

**Storage Temperature and Humidity Requirements**

| Parameter | Description | Remark |
| --- | --- | --- |
| Temperature | -30° C to 50° C | Time period < 3 months |
| Temperature | 0° C to 25° C | Time period > 3 months |
| Humidity | 2%RH to 90%RH | < 85% Recommended |

- **Storage Environment**: Store the product in a clean, ventilated, and cool environment, avoiding direct sunlight, high temperatures, corrosive gases, severe vibration, mechanical shaking, and heavy pressure. Keep the product away from heat sources and store it at an altitude below 1500 meters, maintaining atmospheric pressure between 86 kPa and 106 kPa.
  
- **Maintenance**: Charge and discharge the device once a month while storing it at room temperature or in a dry and ventilated environment. 
    - If storing the device takes more than 30 days, adjust the SOC to 40% after charging. 
    - If the module is expected to be stored for more than 30 days, adjust the State of Charge (SOC) to 40 % after charging is completed.

The operation of the product must adhere to the operating instructions. Installation, maintenance, and usage of the product must strictly comply with relevant safety regulations.

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

