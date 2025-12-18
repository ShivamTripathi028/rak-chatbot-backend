---
slug: /product-categories/wisnode/weather-station/datasheet/
title: Weather Station Monitoring Solution Datasheet
description: Provides comprehensive information of your Weather Station Solution to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
keywords:
  - datasheet
  - Sensor Hub Solutions
  - Weather Station
image: https://images.docs.rakwireless.com/wisnode/weather-station/weather-station-solution.png
sidebar_label: Datasheet
---

# Weather Station Monitoring Solution Datasheet

## Solution Overview

### Description

The Weather Station Solution is built with RAK Sensor Hub and RK900-09 Miniature Ultrasonic Weather Station Sensor. This solution features a high-strength structural design, ensuring reliable operation even in the harshest of climates and environments. Equipped with high-precision sensors, the Weather Station Solution is ideal for environmental monitoring, industry, agriculture, and transportation.

With the plug-and-play feature of the Sensor Hub, the Weather Station Solution comes with pre-installed components ready for easy installation and connection. The sensor provides highly accurate wind speed and direction, temperature, humidity, and pressure readings, with the Sensor Hub collecting and transmitting the data via LoRaWAN or NB-IoT/CAT M1.

The Sensor Hub’s connectivity function allows for versatile data transmission to the cloud using the two most commonly used communication protocols in IoT. This versatility ensures that data is readily available for storage, visualization, and in-depth analysis, enabling informed decision-making based on comprehensive knowledge of the weather.

### Features

- Support LoRa and NB-IoT/LTE CAT-M wireless communication modes
- Support LoRaWAN frequency bands: CN470, EU868, IN865, RU864, US915, AU915, KR920, and AS923-1/2/3/4
- Easy to install and configure
- Configurable network access with the WisToolBox mobile app
- RS485 output
- High precision
- Versatile climate assessment
- High-strength structural design
- IP rating: IP65
- Support solar panel and 12 V<sub>DC</sub> power adapter for power supply

## Specifications

### Sensor Hub Specifications

For details, refer to the <a href="https://docs.rakwireless.com/product-categories/wisnode/rak2560/hub-datasheet/#description" target="_blank">RAK2560 WisNode Sensor Hub Datasheet</a>.

### Sensor Probe IO + Weather Station Sensor Specifications

**Sensor Probe IO Datasheet**

- For details, refer to the <a href="https://docs.rakwireless.com/product-categories/wisnode/rak2560/probe-io-datasheet/#overview" target="_blank">Probe IO Datasheet</a>.

**Micro Weather Sensor Datasheet**

| Monitoring Item | Parameter Content | Range | Resolution | Precision |
| --- | --- | --- | --- | --- |
| Wind Speed | Ultrasonic Wave | 0 ~ 40 m/s | 0.01 m/s | ±0.5+2%FS |
| Wind Direction |  | 0 ~ 359° | 1° | ±3° |
| Atmospheric Temperature | MEMS | -40 ~ +100° C | 0.1° C | ±0.5° C |
| Atmospheric Humidity |  | 0 ~ 100%RH | 0.1%RH | ±3% |
| Atmospheric Pressure |  | 10 ~ 1100 hPa | 0.1 hPa | ±1.5 hPa |
| Power Supply | 12 VDC |  |  |  |
| Output | RS485 |  |  |  |
| Communication Protocol | Modbus-RTU |  |  |  |
| Power Consumption | 0.6 W |  |  |  |
| Operating Temperature |  | -40 ~ +80° C |  |  |
| IP Rating | IP65 |  |  |  |
| Main Materials | ABS + Aluminum alloy |  |  |  |

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
| Capacity | The amount of electrical charge that a fully charged battery can store and subsequently provide to a device or system.Unit: Ampere-hours (Ah) |
| Energy Capacity | The total amount of energy that a fully charged battery can deliver under specific conditions.Unit: Watt-hours (Wh) or kilowatt-hours (kWh) |
| Rated Capacity | At the beginning of life (BOL), the minimum capacity that a fully charged battery can provide at a discharge rate of 1 C (discharge C-rate). |
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
| Battery Cell Model | Rechargeable cylindrical lithium-ion battery H18650CH | H18650CH or products of the same level |
| Rated Capacity | 5200 mAh | 5.2 Ah |
| Rated Voltage | 10.8 V | Single cell voltage 3.6 V |
| Operating Voltage Range | 9 V～12.6 V |  |
| Rated Power | 56.16 Wh |  |
| SOC Transportation Range | 0.5 |  |
| Operating Temperature | Charging temperature:0° C ~ 45° C |  |
|  | Discharging temperature:-20° C ~ 60° C |  |
| Storage Temperature | -20° C ~ 60° C | Over 3 months @ 25° C |
| Operating Humidity | 20 ~ 80%RH |  |
| PV input | 18 V/1.0 A | Typical |
| Maximum PV Input Voltage | 30 V | Open circuit voltage |
| Maximum Charging Continuous Current | 0.2 C (1.0 A) | Limited by solar chargers |
| Maximum Discharge Continuous Current | 0.4 C (2.0 A) |  |
| ∆ Voltage | ≤20 mV | Rest for at least 2 hours after charging or discharging |
| Weight | 0.85 Kg |  |
| Size | Length: 180 (±3) mmWidth: 130 (±3) mmHeight: 60 (±3) mm |  |

#### Interfaces

##### Battery System Structure

As shown in **Figure 1**, the RAK9154 battery system comprises two sets of three 2600 mAh battery units connected in series. The system also incorporates one (1) BMS board integrated with an 18 V input solar charger.

> **Image:** RAK9154 battery system

#### Electrical Characteristics

> **Image:** RAK9154 electrical diagram

> **Image:** System circuit schematic

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
| PV Input | SP1110/P2 | SP1110/P2-N | Pin1: PV+ | SP11IP67Rated current 2 AContact diameter 0.75 mm * 4 |
| PV Input | SP1110/P2 | SP1110/P2-N | Pin1: PV- | SP11IP67Rated current 2 AContact diameter 0.75 mm * 4 |

#### Sensor Characteristics

The following table shows the sensor data definition and the data format of the Weather Station Solution.

- **Register Summary**

| Register Name  | Function Code | Register Address | Data Length | Sensor Code | Ratio    | Unit          | Resolution         | Range | Precision |
| -------------- | ------------- | ---------------- | ----------- | ----------- | -------- | ------------- | ------------------ | ----- | --------- |
| Wind Speed     | 0x03          | 0x0000           | 2           | 0xBE        | m/s      | 0.01 m/s | 0 ~ 40 m/s    | 0.01  |
| Wind Direction | 0x03          | 0x0001           | 2           | 0xBF        | °        | 1°            | 0 ~ 359°           | 1     |
| Temperature    | 0x03          | 0x0002           | 2           | 0x67        | ° C | 0.1° C   | -40 ~ 100° C  | 0.1   |
| High Humidity  | 0x03          | 0x0003           | 2           | 0x70        | %        | 0.1%RH        | 0 ~ 100%RH         | 0.1   |
| Pressure       | 0x03          | 0x0004           | 2           | 0x73        | mbar     | 0.1 hPa  | 10 ~ 1100 hPa | 0.1   |

- **Data Interpretation**

| Sensor Data Unit | ID (Channel) | Type   | Data    |
| ---------------- | ------------ | ------ | ------- |
| Wind Speed       | 1 Byte       | 1 Byte | 2 Bytes |
| Wind Direction   | 1 Byte       | 1 Byte | 2 Bytes |
| Temperature      | 1 Byte       | 1 Byte | 2 Bytes |
| Humidity         | 1 Byte       | 1 Byte | 2 Bytes |
| Air Pressure     | 1 Byte       | 1 Byte | 2 Bytes |

With the defined data, here's how to interpret the payload received data:

**Data Sample 1:**

Payload (hex) received data: `1be000002bf000003670122047001ac057324fe`

| Sensor Data Unit | ID (Channel) | Type | Data |
| ---------------- | ------------ | ---- | ---- |
| Wind Speed       | 01           | be   | 0000 |
| Wind Direction   | 02           | bf   | 0000 |
| Temperature      | 03           | 67   | 0122 |
| Humidity         | 04           | 70   | 01ac |
| Air Pressure     | 05           | 73   | 24fe |

Convert the sensor data from hexadecimal to decimal:

- **Wind Speed**: `01be`
- **Data**: `0000`

```
0000 (hex) = 0 (dec)
0 x 0.01 (conversion factor) = 0 m/s
```

- **Wind Direction**: `02bf`
- **Data**: `0000`

```
0000 (hex) = 0 (dec)
0 x 1 (conversion factor) = 0°
```

- **Temperature**: `0367`
- **Data**: `0122`

```
0122 (hex) = 290 (dec)
290 x 0.1 (conversion factor) = 29° C
```

- **Humidity**: `0470`
- **Data**: `01ac`

```
01ac (hex) = 428 (dec)
428 x 0.1 (conversion factor) = 42.8%RH
```

- **Air Pressure**: `0573`
- **Data**: `24fe`  

```
24fe (hex) = 9470 (dec)
9470 x 0.1 (conversion factor) = 947 hPa
```

** Data Sample 2: **

Payload (hex) received data: `01be00c002bf000403670122047001ac057324ff`

| Sensor Data Unit | ID (Channel) | Type | Data |
| ---------------- | ------------ | ---- | ---- |
| Wind Speed       | 01           | be   | 00c0 |
| Wind Direction   | 02           | bf   | 0004 |
| Temperature      | 03           | 67   | 0122 |
| Humidity         | 04           | 70   | 01ac |
| Air Pressure     | 05           | 73   | 24ff |

Convert the sensor data from hexadecimal to decimal:

- **Wind Speed**: `01be`
- **Data**: `00c0`

```
00c0 (hex) = 192 (dec)
192 x 0.01 (conversion factor) = 1.92 m/s
```

- **Wind Direction**: `02bf`
- **Data**: `0004`

```
0004 (hex) = 4(dec)
4 x 1 (conversion factor) = 4°
```

- **Temperature**: `0367`
- **Data**: `0122`

```
0122 (hex) = 290 (dec)
290 x 0.1 (conversion factor) = 29° C
```

- **Humidity**: `0470`
- **Data**: `01ac`

```
01ac (hex) = 428 (dec)
428 x 0.1 (conversion factor) = 42.8%RH
```

- **Air Pressure**: `0573`
- **Data**: `24ff`  

```
24ff (hex) = 9471 (dec)
9471 x 0.1 (conversion factor) = 947.1 hPa
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

