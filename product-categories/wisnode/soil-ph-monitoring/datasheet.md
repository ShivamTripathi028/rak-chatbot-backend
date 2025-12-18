---
slug: /product-categories/wisnode/soil-ph-monitoring/datasheet/
title: Soil pH Monitoring Solution Datasheet
description: Contains the key features of the Soil pH Monitoring Solution, detailing its main technical specifications, physical attributes, and data configuration.
keywords:
- Sensor Hub
- Soil pH
- Sensor Hub Solutions
- datasheet
image: https://images.docs.rakwireless.com/wisnode/soil-ph-monitoring/soil-ph.png
sidebar_label: Datasheet
---

# Soil pH Monitoring Solution Datasheet

## Solution Overview

### Description

The Soil pH Solution offers an effective tool for monitoring soil pH levels, comprising the RAK Sensor Hub and Soil pH sensor JXBS-3001-PF 485. This comprehensive monitoring system is well-suited for various applications, including agricultural greenhouses, flower cultivation, and pasture grasslands.

With the plug-and-play feature of the Sensor Hub, the Soil pH Solution comes with pre-installed components ready for easy installation and connection. The sensor provides highly accurate soil pH readings, with the Sensor Hub collecting and transmitting the data via LoRaWAN or NB-IoT/CAT M1.

The Sensor Hub’s connectivity function allows for versatile data transmission to the cloud using the two most commonly used communication protocols in IoT. This versatility ensures that data is readily available for storage, visualization, and in-depth analysis, enabling informed decision-making based on comprehensive knowledge of soil pH levels.

### Features

- Support LoRa and NB-IoT/LTE CAT-M wireless communication modes
- Support LoRaWAN frequency bands: CN470, EU868, IN865, RU864, US915, AU915, KR920, and AS923-1/2/3/4
- Wide measurement range: 0 ~ 1999 mg/kg
- Resolution: 1 mg/kg (mg/l)
- Easy to install and configure
- Configurable network access with the WisToolBox mobile app 
- pH electrode in the probe 
- Stable signal
- Good linearity

## Specifications

### Sensor Hub Specifications

For details, refer to the [RAK2560 WisNode Sensor Hub Datasheet](https://docs.rakwireless.com/product-categories/wisnode/rak2560/hub-datasheet#description).

### Sensor Probe IO + Soil pH Sensor Specifications

**Sensor Probe IO Datasheet** 

- For details, refer to the [Probe IO Datasheet](https://docs.rakwireless.com/product-categories/wisnode/rak2560/probe-io-datasheet#overview).

**Model 485 Soil pH Sensor Datasheet**

| Parameter                 | Technical Specifications                         |
| ------------------------- | ------------------------------------------------ |
| DC Power Supply (default) | 12 V<sub>DC</sub> to 24 V<sub>DC</sub> |
| Power Consumption         | ≤0.15 W                                     |
| pH Test Range             | 3 ~ 9 pH                                      |
| Long-Term Stability       | ≤5 %/year                                   |
| Output Signal             | RS485 output (Modbus protocol)                   |
| Operating Temperature     | 0° C to -55° C                         |
| Responding Speed          | ≤1 5 s                                      |

### Solar Cell System Datasheet

#### Definition of Terms

**List of Abbreviations**

| Abbreviation | Definition                  |
| ------------ | --------------------------- |
| BMS          | Battery Management System   |
| BMU          | Battery Management Unit     |
| BOL          | Begin of Life               |
| Bus-bar      | Battery Pole Connecting Rod |
| CMC          | Cell Manager Circuit        |
| EOL          | End of Life                 |
| HV           | High Voltage                |
| LV           | Low Voltage                 |
| OCV          | Open Circuit Voltage        |
| SOC          | Stage of Charge             |

**Terminologies**

| Terminology     | Definition                                                                                                                                                                                                                                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Battery Cell    | Commonly known as a battery. It is the fundamental unit of energy storage, which converts chemical energy to electrical energy.                                                                                                                                                                              |
| Battery Module  | The intermediate energy storage unit comprises several individual cells, circuitry components, and electrical and communication interfaces.                                                                                                                                                                  |
| Battery Pack    | A comprehensive power system consisting of multiple battery modules and circuits working together to supply power to electrical devices.                                                                                                                                                                     |
| Rated Voltage   | Refers to the approximate voltage value that a battery is designed to operate at or provide.                                                                                                                                                                                                                 |
| Capacity        | The amount of electrical charge that a fully charged battery can store and subsequently provide to a device or system. Unit: Ampere-hours (**Ah**)                                                                                                                                                           |
| Energy Capacity | The total amount of energy that a fully charged battery can deliver under specific conditions. Unit: Watt-hours (**Wh**) or kilowatt-hours (**kWh**)                                                                                                                                                         |
| Rated Capacity  | The minimum capacity that a fully charged battery can deliver at the beginning of its life (BOL), typically measured under specific conditions such as a discharge rate of 1 C (discharge C-rate).                                                                                                      |
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

| Parameter                              | Specifications                                                                                | Remark                                                                           |
| -------------------------------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Battery Model                          | RAK9154                                                                                       |                                                                                  |
| Battery Cell Model                     | Rechargeable cylindrical lithium-ion battery H18650CH                                         | H18650CH or equivalent product                                                   |
| Rated Capacity                         | 5200 mAh                                                                                 |                                                                                  |
| Rated Voltage                          | 10.8 V                                                                                   | Single battery voltage 3.6 V                                                |
| Operating Voltage Range                | 9 V ~ 12.6 V                                                                          |                                                                                  |
| Rated Power                            | 56.16 Wh                                                                                 |                                                                                  |
| SOC Transportation Range               | 50%                                                                                           |                                                                                  |
| Operating Temperature                  | Charging temperature: 0° C ~ 45° C
Discharge temperature: -20° C ~ 60° C   |                                                                                  |
| Storage Temperature                    | -20° C ~ 60° C                                                                        | More than three months @ 25° C                                              |
| Operating Humidity                     | 20 ~ 80° %RH                                                                               |                                                                                  |
| PV Input                               | 18° V/1.0° A                                                                        | Typical                                                                          |
| Maximum PV Input Voltage               | 30 V                                                                                     | Open circuit voltage                                                             |
| Maximum Continuous Charging Current    | 0.2 C (1.0 A)                                                                       | Limited by solar charger                                                         |
| Maximum Continuous Discharging current | 0.4 C (2.0 A)                                                                       |                                                                                  |
| ∆ Voltage                              | ≤20 mV                                                                                   | SOC 30 % ~ 60 %; rest for at least 2 hours after charging or discharging |
| Weight                                 | 0.85 Kg                                                                                  |                                                                                  |
| Dimension                              | Length: 180 (±3) mm
Width: 130 (±3) mm
Height: 60 (±3) mm |                                                                                  |

#### Interfaces

##### Battery System Structure

As shown in **Figure 1**, the RAK9154 battery system comprises two sets of three 2600 mAh battery units connected in series. The system also incorporates one (1) BMS board integrated with an 18 V input solar charger.

> **Image:** RAK9154 battery system

#### Electrical Characteristics

> **Image:** RAK9154 electrical diagram

> **Image:** System circuit diagram

| Connector           | Connector Socket Model | Connector Plug Model | Definition                                                     | Remark                                                                        |
| ------------------- | ---------------------- | -------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Gateway Load**    | SP1110/P4              | SP1110/P4-N          | Pin1: P+
Pin2: P-
Pin3: R485A
Pin4: RS485B            | SP11
IP67
Rated current 2 A
Contact diameter
0.75 mm *4 |
| **Sensor Hub Load** | SP1110/P5              | SP1110/P5-N          | Pin1: P+
Pin2: P-
Pin3: TXD
Pin4: 3V3_In
Pin5: RXD | SP11
IP67
Rated current 2 A
Contact diameter 0.75 mm *5    |
| **PV Input**        | SP1110/P2              | SP1110/P2-N          | Pin1: PV+
Pin2: PV-                                         | SP11
IP67
Rated current 1 A
Contact diameter 1.0 mm *2     |

#### Sensor Characteristics

The following tables show the sensor data definition and the data format of the Soil pH Monitoring Solution. 

- **Register Summary**
  
|      Register Name      | Function Code | Register Address | Data Length | Sensor Code | Ratio | Unit  | Resolution | Range | Precision |
| :---------------------: | :-----------: | :--------------: | :---------: | :---------: | :---: | :---: | :--------: | :---: | :-------: |
| High Precision pH Value |     0x03      |      0x0006      |      2      |    0xC1     | 0.01  |  pH   |  ± 0.3pH   | 3 ~ 9pH |  ± 0.3pH  |
| Low Precision pH Value  |     0x03      |      0x000d      |      2      |    0xC2     |  0.1  |  pH   |  ± 0.3pH   | 3 ~ 9pH |  ± 0.3pH  |

- **Data Interpretation**

| ID (Channel) |  Type  |  Data   |
| :----------: | :----: | :-----: |
|    1 byte    | 1 byte | 2 bytes |

With the defined data, here's how to interpret the payload received data:

** Data Sample 1: ** 

Payload (hex) received data: `01C1 0320`

| ID (Channel) | Type  | Data  |
| :----------: | :---: | :---: |
|      01      |  C1   | 0320  |

Convert the value to decimal:

- **pH**: `01C1`
- **Data**: `0320`

```
0320 (hex) = 800 (dec)
800 × 0.01 (conversion factor) = 8 pH
```

** Data Sample 2: ** 

Payload (hex) received data: `01C2 002d`

| ID (Channel) | Type  | Data  |
| :----------: | :---: | :---: |
|      01      |  C2   | 002d  |

Convert the value to decimal:

- **pH**: `01C2`
- **Data**: `002d`

```
002d (hex) = 45 (dec)
45 × 0.1 (conversion factor) = 4.5 pH
```

#### Environmental Requirements

##### Transportation Requirements

:::warning
- When transporting the battery, avoid severe vibrations, shaking, and exposure to sunlight or rain. 
- Do not invert the battery to prevent potential short circuits. 
- During loading and unloading, exercise caution to prevent the battery from falling, rolling, enduring heavy pressure, or being inverted. 
:::

##### Storage Requirements

Store the module in a partially charged state, typically around 40 % state of charge (SOC). Ensure the storage environment meets the following requirements:

**Temperature and Humidity**

| Parameter | Value | Remark |
| --- | --- | --- |
| Temperature | -30° C to 50° C, 40% SOC | Storage time < 3 months |
| Temperature | 0° C to 25° C, 40% SOC | Storage time > 3 months |
| Humidity | 2%RH to 90%RH | < 85% Recommended |

- **Storage Environment**: 
    - Store the product in a clean, ventilated, and cool environment.
    - Avoid direct sunlight, high temperatures, corrosive gases, severe vibration, mechanical shaking, and heavy pressure.
    - Keep the product away from heat sources and store it at an altitude below 1500 meters, maintaining atmospheric pressure between 86 kPa and 106 kPa.

- **Maintenance**: 
    - Charge and discharge the device once a month while storing it at room temperature or in a dry and ventilated environment. 
    - If storing the device takes more than 30 days, adjust the SOC to 40 % after charging. 
    - If the module is expected to be stored for more than 30 days, adjust the State of Charge (SOC) to 40% after charging is completed.

The operation of the product must adhere to the provided operating instructions. Installation, maintenance, and usage of this product must strictly comply with relevant safety regulations.

:::warning
- Avoid storing or using the product in high-temperature environments, and keep it away from heat sources. Temperatures outside the safe range can significantly reduce the performance and lifespan of the product, and may even cause serious consequences such as combustion and explosion.
- Do not store or use the product in environments with high static electricity or high electromagnetic radiation. Doing so may damage the electronic components of the battery, leading to safety hazards.
- Avoid exposing the battery to water or immersing it in water. Otherwise, it may result in internal short circuits, loss of function, or abnormal chemical reactions, leading to fire, smoke explosion, and other incidents.
- If you notice any smoking, heating, discoloration, deformation, or any other abnormalities during the use, storage, transportation, and service of the product, contact a professional immediately for assistance.
- Do not discard waste batteries in fires or incinerators. Waste batteries should be recycled by professional institutions or organizations.
- It is strictly prohibited to place heavy objects on the product or stack them on top of each other.
- Although this module is not a high-voltage energy storage device, improper operation and use of the device may lead to serious consequences, such as combustion and explosion.
- Only professional technicians must handle the installation and maintenance of the battery system. All operations must strictly adhere to relevant safety regulations. Non-professionals are strictly prohibited from installing, maintaining, and misusing the battery system.
:::

