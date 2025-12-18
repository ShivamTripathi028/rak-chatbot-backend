---
slug: /product-categories/wisnode/co2-concentration/datasheet/
title: CO2 Concentration Solution Datasheet
description: Provides comprehensive information about your Sensor Hub CO2 Concentration solution to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisnode/co2-concentration-monitoring/co2-sensor.png
keywords:
  - datasheet
  - wisnode
  - sensor hub
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# CO<sub>2</sub> Concentration Solution Datasheet

## Solution Overview

### Description

The Sensor Hub CO<sub>2</sub> Concentration Monitoring solution comprises the RK300-03, and the Sensor Hub. This solution incorporates advanced infrared absorption gas detection technology and it is widely used in various fields and locations requiring CO<sub>2</sub> concentration detection, such as air quality monitoring, greenhouses, smart homes, schools, and industrial production.

With the plug-and-play feature of the Sensor Hub, the CO<sub>2</sub> Concentration Monitoring solution comes with pre-installed components ready for easy installation and connection. The sensor provides highly accurate CO<sub>2</sub> Concentration readings, with the Sensor Hub collecting and transmitting the data via LoRaWAN or NB-IoT/CAT M1.

The Sensor Hub’s connectivity function allows for versatile data transmission to the cloud using the two most commonly used communication protocols in IoT. This versatility ensures that data is readily available for storage, visualization, and in-depth analysis, enabling informed decision-making based on comprehensive knowledge of CO<sub>2</sub> levels.

### Features

- Supports LoRa® and NB -IoT/LTE CAT-M wireless communication modes
- Support LoRa frequency band: CN470, EU868, IN865, RU864, US915, AU915,  KR920, and AS923-1/2/3/4
- Easy to configure, and the network access configuration can be completed through the WisToolBox app on mobile devices.
- Effectively blocks water vapor
- Good stability
- Low power consumption
  - External DC power supply (optional)
  - Solar panel power supply (optional)
- Long service life
- High sensitivity
- Fast response
- Easy to install


## Hardware Specifications

### Sensor Hub Specifications

If you need detailed information about the Sensor Hub, including technical specifications and features, refer to the [Sensor Hub Datasheet](https://docs.rakwireless.com/product-categories/wisnode/rak2560/hub-datasheet#overview) page.

### Sensor Probe IO + CO<sub>2</sub> Concentration  Sensor Specifications

**Sensor Probe IO Datasheet** 

- For details, refer to the [Probe IO Datasheet](https://docs.rakwireless.com/product-categories/wisnode/rak2560/probe-io-datasheet#overview).

**RK-300-03 CO2 Concentration Sensor Datasheet**

| Parameter             | Value                                              |
|-----------------------|----------------------------------------------------|
| Range (concentration) | 0 - 5000&nbsp;ppm                                  |
| Precision             | ± 3&nbsp;%FS @ 25°&nbsp;C                          |
| Preheat Time          | 3 minutes                                          |
| Response Time         | 20&nbsp;s                                          |
| Temperature Drift     | ≤ 0.2&nbsp;%FS/°&nbsp;C                                   |
| Stability             | < ± 40&nbsp;ppm/year                               |
| Repeatability         | < ± 1&nbsp;%FS                                     |
| Temperature Effect    | ± 2&nbsp;% (- 10°&nbsp;C ~  40°&nbsp;C)            |
| Power Supply          | 5&nbsp;V, 12 ~ 24&nbsp;V<sub>DC</sub>              |
| Output                | 0 ~ 5&nbsp;V, 4 ~ 20&nbsp;mA, RS485                |
| Power Consumption     | < 0.25&nbsp;W                                      |
| Operating Temperature | -20°&nbsp;C ~ 60°&nbsp;C @ 15&nbsp;% - 80&nbsp;%RH |
| Storage Conditions    | 40°&nbsp;C ~ 70°&nbsp;C @ 20&nbsp;% - 90&nbsp;%RH  |
| IP Rating             | IP65                                               |

**RK-300-03 CO2 Concentration Sensor Dimensions**

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/co2-concentration-monitoring/datasheet/f1co2sensor_dimensions.png"
  width="60%"
  caption="Sensor Dimensions"
/>

### Solar Cell System Specifications

#### Definition of Terms

<b>List of Abbreviations</b>

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


<b>Terminologies</b>

| Terminology     | Definition                                                                                                                                                                                                                                                                                                            |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Battery Cell    | Commonly known as a battery. It is the fundamental unit of energy storage, which converts chemical energy to electrical energy.                                                                                                                                                                                       |
| Battery Module  | The intermediate energy storage unit, comprising several individual cells and circuitry components, along with electrical and communication interfaces.                                                                                                                                                               |
| Battery Pack    | A comprehensive power system consisting of multiple battery modules and circuits working together to supply power to electrical devices.                                                                                                                                                                              |
| Rated Voltage   | Refers to the approximate voltage value that a battery is designed to operate at or provide.                                                                                                                                                                                                                          |
| Capacity        | The amount of electrical charge that a fully charged battery can store and subsequently provide to a device or system. It is typically measured in ampere-hours (Ah).                                                                                                                                                 |
| Energy Capacity | The total amount of energy that a fully charged battery can deliver under specific conditions. It is typically measured in watt-hours (Wh) or kilowatt-hours (kWh).                                                                                                                                                   |
| Rated Capacity  | The minimum capacity that a fully charged battery can deliver at the beginning of its life (BOL), typically measured under specific conditions such as a discharge rate of 1C (discharge C-rate).                                                                                                                     |
| Units           | **V**: Volt, voltage<br/>**A**: Ampere, current<br/>**Ah**: Ampere-hour, charge<br/>**Wh**: Watt-hour, electrical energy<br/>**Ω**: Ohm, resistance<br/>**°&nbsp;C**: degrees Celsius, temperature<br/>**mm**: millimeter, length<br/>**s**: seconds, time <br/>**kg**: kilogram, weight<br/>**Hz**: Hertz, frequency |


#### Main Specifications 

| Parameter                              | Specifications                                                                                  | Remark                                                                           |
|----------------------------------------|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Battery Model                          | RAK9154                                                                                         |                                                                                  |
| Battery Cell Model                     | Rechargeable cylindrical lithium-ion battery H18650CH                                           | H18650CH or equivalent product.                                                  |
| Rated Capacity                         | 5200&nbsp;mAh                                                                                   |                                                                                  |
| Rated Voltage                          | 10.8&nbsp;V                                                                                     | Single battery voltage 3.6&nbsp;V                                                |
| Operating Voltage Range                | 9&nbsp;V~12.6&nbsp;V                                                                            |                                                                                  |
| Rated Power                            | 56.16&nbsp;Wh                                                                                   |                                                                                  |
| SOC Transportation Range               | 50&nbsp;%                                                                                       |                                                                                  |
| Operating Temperature                  | Charging temperature: 0°&nbsp;C~45°&nbsp;C<br/>Discharge temperature: -20°&nbsp;C~60°&nbsp;C    |                                                                                  |
| Storage Temperature                    | -20°&nbsp;C~60°&nbsp;C                                                                          | More than three months @25°&nbsp;C                                               |
| Operating Humidity                     | 20~80°&nbsp;%RH                                                                                 |                                                                                  |
| PV Input                               | 18°&nbsp;V/1.0°&nbsp;A                                                                          | Typical                                                                          |
| Maximum PV Input Voltage               | 30&nbsp;V                                                                                       | Open circuit voltage                                                             |
| Maximum Continuous Charging Current    | 0.2&nbsp;C (1.0&nbsp;A)                                                                         | Limited by solar charger                                                         |
| Maximum Continuous Discharging current | 0.4&nbsp;C (2.0&nbsp;A)                                                                         |                                                                                  |
| ∆ Voltage                              | ≤20&nbsp;mV                                                                                     | SOC 30&nbsp;%~60&nbsp;%; rest for at least 2 hours after charging or discharging |
| Weight                                 | 0.85&nbsp;Kg                                                                                    |                                                                                  |
| Size                                   | Length: 180&nbsp;(±3)&nbsp;mm<br/>Width: 130&nbsp;(±3)&nbsp;mm<br/>Height: 60&nbsp;(±3)&nbsp;mm |                                                                                  |

#### Interfaces

##### Battery System Structure

As illustrated in **Figure 2**, the RAK9154 battery system comprises two sets of three 2600&nbsp;mAh battery units connected in series. The system also incorporates one (1) BMS board integrated with an 18 V input solar charger.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/co2-concentration-monitoring/datasheet/f2co2solution_dimensions.png"
  width="60%"
  caption="RAK9154 battery system"
/>

#### Electrical Characteristics

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/co2-concentration-monitoring/datasheet/f3co2solution_bdiagram1.png"
  width="60%"
  caption="RAK9154 electrical schematic diagram"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/co2-concentration-monitoring/datasheet/f4co2solution_bdiagram2.png"
  width="60%"
  caption="System circuit schematic diagram"
/>

<table>
  <thead>
    <tr>
      <th>Connector</th>
      <th>Connector Socket Model</th>
      <th>Connector Plug Model</th>
      <th>Definition</th>
      <th>Remark</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowSpan = "4">**Gateway Load**</td>
      <td rowSpan = "4">SP1110/P4</td>
      <td rowSpan = "4">SP1110/P4-N</td>
      <td>Pin1: P+</td>
      <td rowSpan = "4">SP11  <br/> IP67 <br/> Rated current 2&nbsp;A  <br/> Contact diameter 0.75&nbsp;mm * 4</td>
    </tr>
    <tr>
      <td>Pin2: P-</td>
    </tr>
    <tr>
      <td>Pin3: R485A</td>
    </tr>
    <tr>
      <td>Pin4: RS485B</td>
    </tr>
    <tr>
      <td rowSpan = "5">**Sensor Hub Load**</td>
      <td rowSpan = "5">SP1110/P5</td>
      <td rowSpan = "5">SP1110/P5-N</td>
      <td>Pin1: P+</td>
      <td rowSpan = "5">SP11  <br/> IP67 <br/> Rated current 2&nbsp;A  <br/> Contact diameter 0.75&nbsp;mm * 4</td>
    </tr>
    <tr>
      <td>Pin2: P-</td>
    </tr>
    <tr>
      <td>Pin3: TXD</td>
    </tr>
    <tr>
      <td>Pin4: 3V3_In</td>
    </tr>
    <tr>
      <td>Pin5: RXD</td>
    </tr>
    <tr>
      <td rowSpan = "2">**PV Input**</td>
      <td rowSpan = "2">SP1110/P2</td>
      <td rowSpan = "2">SP1110/P2-N</td>
      <td>Pin1: PV+</td>
      <td rowSpan = "2">SP11  <br/> IP67 <br/> Rated current 1&nbsp;A  <br/> Contact diameter 0.75&nbsp;mm * 4</td>
    </tr>
    <tr>
      <td>Pin1: PV-</td>
    </tr>
  </tbody>
</table>


#### Sensor Characteristics

The following table shows the sensor data definition and the data format of the CO<sub>2</sub> Concentration Solutions.

- **Sensor Data Definitions**

| Sensor Name                  | Sensor Type | Data Length | Range  | Unit |
|------------------------------|-------------|-------------|--------|------|
| CO<sub>2</sub> Concentration | 0x7D        | 2           | 0~5000 | ppm  |

- **Data Format**

| ID (Channel) | Type   | Data    |
|--------------|--------|---------|
| 1 Byte       | 1 Byte | 2 Bytes |

With the defined data, here's how to interpret the payload received data:

- **Data Example**

Payload (hexadecimal) received data is: `15 7d 02 AA`

| ID (Channel) | Type | Data |
|--------------|------|------|
| 15           | 7D   | 02AA |

`157D` (CO<sub>2</sub> concentration) - `02AA` (Data)

Convert the value to decimal:

````
02 AA (hex) = 682 (10 dec)
682 × 1 (conversion coefficient) = 682 ppm
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
| Temperature | -30°&nbsp;C to 50°&nbsp;C  <br/> 0°&nbsp;C to 25°&nbsp;C | Time period < 3 months <br/> Time period > 3 months |
| Humidity    | 2&nbsp;%RH to 90&nbsp;%RH                                | < 85&nbsp;% Recommended                             |

- **Storage Environment**: Store the product in a clean, ventilated, and cool environment, avoiding direct sunlight, high temperatures, corrosive gases, severe vibration, mechanical shaking, and heavy pressure. Keep the product away from heat sources and store it at an altitude below 1500&nbsp;meters, maintaining atmospheric pressure between 86&nbsp;kPa and 106&nbsp;kPa.

- **Maintenance**: Charge and discharge the device once a month while storing it at room temperature or in a dry and ventilated environment. If storing the device takes more than 30 days, adjust the SOC to 40&nbsp;% after charging. If the module is expected to be stored for more than 30 days, adjust the State of Charge (SOC) to 40&nbsp;% after charging is completed.

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

<RkBottomNav/>