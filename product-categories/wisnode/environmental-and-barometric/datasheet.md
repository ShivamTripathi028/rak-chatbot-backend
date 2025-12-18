---
slug: /product-categories/wisnode/environmental-and-barometric/datasheet/
title: Datasheet
description: Provides comprehensive information of your Environmental and Barometric Monitoring Solution to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisnode/environmental-and-barometric-solution/environmental-and-barometric-solution.png"
keywords:
  - datasheet
  - Sensor Hub Solutions
  - Environmental and Barometric
sidebar_label: Datasheet
---

# Environmental and Barometric Monitoring Solution Datasheet

## Solution Overview

### Description

The Environmental and Barometric Monitoring Solution integrates the RAK1901 temperature and humidity sensor and RAK1902 barometric pressure sensor. This solution features low power consumption and accurate data acquisition capabilities. It has critical requirements for temperature, humidity, and barometric pressure, ideal for the food industry, agricultural, and industrial applications.

With the plug-and-play feature of the Sensor Hub, the Environmental and Barometric Monitoring Solution comes with pre-installed components ready for easy installation and connection. The sensor provides highly accurate soil pH readings, with the Sensor Hub collecting and transmitting the data via LoRaWAN or NB-IoT/CAT M1.

The Sensor Hub’s connectivity function allows for versatile data transmission to the cloud using the two most commonly used communication protocols in IoT. This versatility ensures that data is readily available for storage, visualization, and in-depth analysis, enabling informed decision-making based on comprehensive knowledge of temperature, humidity and barometric pressure levels.

### Features

- Supports LoRa® and NB -IoT/LTE CAT-M wireless communication modes
- Support LoRa frequency band: CN470, EU868, IN865, RU864, US915, AU915, KR920, AS923-1/2/3/4
- Easy to install
- Configurable network access with the WisToolBox mobile app
- Automatic recognition of sensor type
- Low power consumption
- Long transmission distance
- Single wire protocol
- IP rating: IP67
- Support solar panel and 12 V<sub>DC</sub> power adapter for power supply

## Specifications

### Sensor Hub Specifications

For details, refer to the [RAK2560 WisNode Sensor Hub Datasheet](https://docs.rakwireless.com/product-categories/wisnode/rak2560/hub-datasheet#description).

### Environmental and Barometric Sensor Datasheet

**RAK1901 Temperature and Humidity Sensor Datasheet**

| Monitoring Item | Principle |
| --- | --- |
| Temperature Sensor Precision | ±2.0° C |
| Temperature Range | -40° C ～+125° C |
| Temperature Resolution | 0.01° C |
| Humidity Sensor Precision | ±2.0 %RH |
| Humidity Range | 0~100 %RH |
| Humidity Resolution | 0.01 %RH |
| Module Size | 10 x 10 mm |
| Interface | I2C |
| VDD (module power supply) | 3.3 V |
| Sleep current | 0.3 uA |
| Measuring Current (normal mode) | 430 uA |
| Measuring Current (low power mode) | 270 uA |

**RAK1902 Barometric Pressure Sensor Datasheet**

| Monitoring Item | Principle |
| --- | --- |
| Pressure Range | 260 hPa ～1260 hPa |
| Pressure Precision | ± 0.1 hPa |
| Temperature range | -40° C ～+85° C |
| Temperature Precision | ±1.5° C |
| Pressure Sensitivity | 4096 LSB/hPa |
| RMS Pressure Sensing Noise | 0.0075 hPa RMS |
| Pressure Output Data Rate | 1/10/25/50/75 Hz |
| Temperature Output Data Rate | 1/10/25/50/75 Hz |
| Module Size | 10 x 10 mm |
| Interface | I2C |
| VDD (module power supply) | 1.7 V ～3.6 V |
| Shutdown Current | 1 uA |

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
| Battery Cell Model | Rechargeable cylindrical lithium-ion battery H18650CH | H18650CH or similar products |
| Rated Capacity | 5200 mAh | 5.2 Ah |
| Rated Voltage | 10.8 V | Single cell voltage 3.6 V |
| Operating Voltage Range | 9 V ～12.6 V |  |
| Rated Power | 56.16 Wh |  |
| SOC Transportation Range | 0.5 |  |
| Operating Temperature | Charging temperature: 0° C ～45° C Discharge temperature: -20° C ～60° C |  |
| Storage Temperature | -20° C ～60° C | More than three months at 25° C |
| Operating Humidity | 20 %RH ～80 %RH |  |
| PV input | 18 V/1.0 A | Typical |
| Maximum PV Input Voltage | 30 V | Open circuit voltage |
| Maximum Charging Continuous Current | 0.2 C (1.0 A) | Limited by solar charger |
| Maximum Discharge Continuous Current | 0.4 C (2.0 A) |  |
| ∆ Voltage | ≤20 mV | SOC 30%~60%; rest for at least 2 hours after charging or discharging |
| Weight | 0.85 kg |  |
| Size | Length: 180 (±3) mm Width: 130 (±3) mm Height: 60 (±3) mm |  |

#### Interfaces

##### Battery System Structure

As shown in **Figure 1**, the RAK9154 battery system comprises two sets of three 2600 mAh battery units connected in series. The system also incorporates one (1) BMS board integrated with an 18 V input solar charger.

> **Image:** RAK9154 battery system

#### Electrical Characteristics

> **Image:** RAK9154 electrical schematic diagram

> **Image:** System circuit schematic diagram

| Connector | Connector Socket Model | Connector Plug Model | Definition | Remark |
| --- | --- | --- | --- | --- |
| **Gateway Load** | SP1110/P4 | SP1110/P4-N | Pin1: P+ | SP11 IP67 Rated current 2 A Contact diameter 0.75 mm * 4 |
| **Gateway Load** | SP1110/P4 | SP1110/P4-N | Pin2: P- | SP11 IP67 Rated current 2 A Contact diameter 0.75 mm * 4 |
| **Gateway Load** | SP1110/P4 | SP1110/P4-N | Pin3: R485A | SP11 IP67 Rated current 2 A Contact diameter 0.75 mm * 4 |
| **Gateway Load** | SP1110/P4 | SP1110/P4-N | Pin4: RS485B | SP11 IP67 Rated current 2 A Contact diameter 0.75 mm * 4 |
| **Sensor Hub Load** | SP1110/P5 | SP1110/P5-N | Pin1: P+ | SP11 IP67 Rated current 2 A Contact diameter 0.75 mm * 5 |
| **Sensor Hub Load** | SP1110/P5 | SP1110/P5-N | Pin2: P- | SP11 IP67 Rated current 2 A Contact diameter 0.75 mm * 5 |
| **Sensor Hub Load** | SP1110/P5 | SP1110/P5-N | Pin3: TXD | SP11 IP67 Rated current 2 A Contact diameter 0.75 mm * 5 |
| **Sensor Hub Load** | SP1110/P5 | SP1110/P5-N | Pin4: 3V3_In | SP11 IP67 Rated current 2 A Contact diameter 0.75 mm * 5 |
| **Sensor Hub Load** | SP1110/P5 | SP1110/P5-N | Pin5: RXD | SP11 IP67 Rated current 2 A Contact diameter 0.75 mm * 5 |
| **PV Input** | SP1110/P2 | SP1110/P2-N | Pin1: PV+ | SP11 IP67 Rated current 1 A Contact diameter 0.75 mm * 2 |
| **PV Input** | SP1110/P2 | SP1110/P2-N | Pin1: PV- | SP11 IP67 Rated current 1 A Contact diameter 0.75 mm * 2 |

#### Sensor Characteristics

The following table shows the sensor data definition and the data format of the Environmental and Barometric Solution.

- **Sensor Data Definitions**

| Sensor Name | Sensor Type | Data Length | Ratio | Scope | Unit |
| --- | --- | --- | --- | --- | --- |
| Temperature_RAK1901 | 0x67 | 2 | 0.1 | -40 ~ +125 | ° C |
| Humidity | 0x68 | 1 | 1 | 0 ~ 100 | %RH |
| Temperature_RAK1902 | 0x67 | 2 | 0.1 | -40 ~ +85 | ° C |
| Barometer | 0x73 | 2 | 0.1 | 260 ~ 1260 | hPa |

- **Data Format**

|  | ID (channel) | Type | Data |
| --- | --- | --- | --- |
| RAK1901 Temperature Sensor Data Unit | 1 Byte | 1 Byte | 2 Bytes |
| RAK1901 Humidity Sensor Data Unit | 1 Byte | 1 Byte | 1 Byte |
| RAK1902 Temperature Sensor Data Unit | 1 Byte | 1 Byte | 2 Bytes |
| RAK1902 Pressure Sensor Data Unit | 1 Byte | 1 Byte | 2 Bytes |

With the defined data, here's how to interpret the payload received data:

**Data Example:**

Payload (hex) received data: `016700c8026819036700ca047324f5`

|  | ID (channel) | Type | Data |
| --- | --- | --- | --- |
| RAK1901 Temperature Sensor Data Unit | 01 | 67 | 00c8 |
| RAK1901 Humidity Sensor Data Unit | 02 | 68 | 19 |
| RAK1902 Temperature Sensor Data Unit | 03 | 67 | 00ca |
| RAK1902 Pressure Sensor Data Unit | 04 | 73 | 24f5 |

Convert the sensor data from hexadecimal to decimal:

- **Temperature_RAK1901**: `0167`
- **Data**: `00c8`

```
00c8 (hex) = 200 (dec)
200 × 0.1 (conversion coefficient) = 20° C
```

- **Humidity**: `0268`
- **Data**: `19`

```
19 (hex) = 25 (dec)
25 × 1 (conversion coefficient) = 25 %RH
```

- **Temperature_RAK1902**: `0367`
- **Data**: `00ca`

```
00ca (hex) = 202 (dec)
202 × 0.1 (transformation coefficient) = 20.2° C
```

- **Barometer**: `0473`
- **Data**: `24f5`

```
24f5 (hex) = 9461 (dec)
9461 × 0.1 (transformation coefficient) = 946.1 hPa
```

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

| Parameter | Value | Remark |
| --- | --- | --- |
| Temperature | -30° C to 50° C, 40% SOC | Storage time < 3 months |
| Temperature | 0° C to 25° C, 40% SOC | Storage time > 3 months |
| Humidity | 2 %RH to 90 %RH | < 85% Recommended |

- **Storage Environment**: 
    - Store the product in a clean, ventilated, and cool environment.
    - Avoid direct sunlight, high temperatures, corrosive gases, severe vibration, mechanical shaking, and heavy pressure.
    - Keep the product away from heat sources and store it at an altitude below 1500 meters, maintaining atmospheric pressure between 86 kPa and 106 kPa.

- **Maintenance**: 
    - Charge and discharge the device once a month while storing it at room temperature or in a dry and ventilated environment. 
    - If storing the device takes more than 30 days, adjust the SOC to 40% after charging. 
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

