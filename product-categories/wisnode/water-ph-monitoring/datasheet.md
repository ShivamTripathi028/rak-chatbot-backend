---
slug: /product-categories/wisnode/water-ph-monitoring/datasheet/
title: Water pH Monitoring Solution Datasheet
description: Provides comprehensive information about your Sensor Hub Water pH solution to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
keywords:
  - datasheet
  - wisnode
  - sensor hub
image: https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/waterphsolution.png
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# Water pH Monitoring Solution Datasheet

## Solution Overview

### Description

The Water pH Sensor Solution integrates the RAK Sensor Hub with the JXBS-4001-pH Water pH Sensor. The probe features a pH glass electrode and an Ag/AgCl reference electrode, ensuring stable signals and high precision. This sensor offers a wide measuring range, good linearity, excellent waterproof performance, and is both easy to use and install.

With the plug-and-play feature of the Sensor Hub, the Water pH Sensor Solution comes with pre-installed components ready for easy installation and connection. The sensor provides highly accurate water pH readings, with the Sensor Hub collecting and transmitting the data via LoRaWAN or NB-IoT/CAT M1.

The Sensor Hub’s connectivity function allows for versatile data transmission to the cloud using the two most commonly used communication protocols in IoT. This versatility ensures that data is readily available for storage, visualization, and in-depth analysis, enabling informed decision-making based on comprehensive knowledge of water pH levels.


### Features

- Support LoRa and NB -IoT/LTE CAT-M wireless communication modes
- Support LoRa frequency band: CN470, EU868, IN865, RU864, US915, AU915, KR920, and AS923-1/2/3/4
- Easy to install and configure
- Configurable network access with the WisToolBox mobile app
- Configurable manual and automatic water temperature compensation function
- Stable signal
- Wide measuring range
- Low power consumption
    - External DC power supply (optional)
    - Solar panel power supply (optional)
- Long transmission distance
- High Precision
- Good waterproof performances


## Hardware Specifications

### Sensor Hub Specifications

If you need detailed information about the Sensor Hub, including technical specifications and features, refer to the [Sensor Hub Datasheet](https://docs.rakwireless.com/product-categories/wisnode/rak2560/hub-datasheet/) page.

### Sensor Probe IO + Water pH Sensor Datasheet

**Sensor Probe IO Datasheet** 

- For details, refer to the [Probe IO Datasheet](https://docs.rakwireless.com/product-categories/wisnode/rak2560/probe-io-datasheet/).

**Water pH sensor (JXBS-4001- pH) datasheet**

<table>
  <tr>
    <th colSpan="3">PARAMETER</th>
    <th>CONTENT</th>
  </tr>
  <tr>
    <td rowSpan="4">Transmitter</td>
    <td colSpan="2">DC Power Supply</td>
    <td>12&nbsp;V - 24&nbsp;V<sub>DC</sub></td>
  </tr>
  <tr>
    <td colSpan="2">Power Consumption</td>
    <td>≤ 0.15&nbsp;W (@12&nbsp;V<sub>DC</sub>, 25°&nbsp;C)</td>
  </tr>
  <tr>
    <td colSpan="2">Output signal</td>
    <td>485 / 4 - 20&nbsp;mA / 0 - 10&nbsp;V</td>
  </tr>
  <tr>
    <td colSpan="2">Size</td>
    <td>105&nbsp;mm × 86&nbsp;mm × 45.5&nbsp;mm</td>
  </tr>
  <tr>
    <td rowSpan="9">Probe</td>
    <td colSpan="2">Cable Length</td>
    <td>5 meters (default)</td>
  </tr>
  <tr>
    <td colSpan="2">Response Time</td>
    <td>≤ 15&nbsp;s</td>
  </tr>
  <tr>
    <td rowSpan="3">pH</td>
    <td>Measuring Range</td>
    <td>0 - 14&nbsp;pH</td>
  </tr>
  <tr>
    <td>Measurement Precision</td>
    <td>0.01&nbsp;pH</td>
  </tr>
  <tr>
    <td>Resolution</td>
    <td>± 0.5&nbsp;pH (default)</td>
  </tr>
  <tr>
    <td rowSpan="3">Temperature</td>
    <td>Measuring Range</td>
    <td>-10°&nbsp;C - 80°&nbsp;C</td>
  </tr>
  <tr>
    <td>Measurement Precision</td>
    <td>0.1°&nbsp;C</td>
  </tr>
  <tr>
    <td>Resolution</td>
    <td>0.1°&nbsp;C</td>
  </tr>
</table>


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
| Battery Module  | Intermediate energy storage unit, comprising several individual cells and circuitry components, along with electrical and communication interfaces.                                                                                                                                                                   |
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
| Operating Voltage Range                | 9&nbsp;V ~ 12.6&nbsp;V                                                                            |                                                                                  |
| Rated Power                            | 56.16&nbsp;Wh                                                                                   |                                                                                  |
| SOC Transportation Range               | 50&nbsp;%                                                                                       |                                                                                  |
| Operating Temperature                  | Charging temperature: 0°&nbsp;C ~ 45°&nbsp;C<br/>Discharge temperature: -20°&nbsp;C ~ 60°&nbsp;C    |                                                                                  |
| Storage Temperature                    | -20°&nbsp;C ~ 60°&nbsp;C                                                                          | More than three months @25°&nbsp;C                                               |
| Operating Humidity                     | 20~80°&nbsp;%RH                                                                                 |                                                                                  |
| PV Input                               | 18°&nbsp;V/1.0°&nbsp;A                                                                          | Typical                                                                          |
| Maximum PV Input Voltage               | 30&nbsp;V                                                                                       | Open circuit voltage                                                             |
| Maximum Continuous Charging Current    | 0.2&nbsp;C (1.0&nbsp;A)                                                                         | Limited by solar charger                                                         |
| Maximum Continuous Discharging current | 0.4&nbsp;C (2.0&nbsp;A)                                                                         |                                                                                  |
| ∆ Voltage                              | ≤20&nbsp;mV                                                                                     | SOC 30&nbsp;% ~ 60&nbsp;%; rest for at least 2 hours after charging or discharging |
| Weight                                 | 0.85&nbsp;Kg                                                                                    |                                                                                  |
| Size                                   | Length: 180&nbsp;(±3)&nbsp;mm<br/>Width: 130&nbsp;(±3)&nbsp;mm<br/>Height: 60&nbsp;(±3)&nbsp;mm |                                                                                  |

#### Interfaces

##### Battery System Structure

As illustrated in **Figure 2**, the RAK9154 battery system comprises two sets of three 2600&nbsp;mAh battery units connected in series. The system also incorporates one (1) BMS board integrated with an 18 V input solar charger.The RAK9154 battery system is depicted in **Figure 2**. This battery system comprises two sets of three 2600&nbsp;mAh battery cells connected in series, accompanied by a BMS board that integrates an 18&nbsp;V input solar charger.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/datasheet/f2waterphsolution_dimensions.png"
  width="60%"
  caption="RAK9154 battery system"
/>

#### Electrical Characteristics

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/datasheet/f3waterphsolution_bdiagram1.png"
  width="60%"
  caption="RAK9154 electrical schematic diagram"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/water-ph-monitoring/datasheet/f4waterphsolution_bdiagram2.png"
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
      <td rowSpan = "4">Gateway Load</td>
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
      <td rowSpan = "5">Sensor Hub Load</td>
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
      <td rowSpan = "2">PV Input</td>
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

The following table shows the sensor data definition and the data format of the water pH solution.

- **Sensor Data Definitions**

| Sensor Name | Sensor Type | Data Length | Range | Unit            |
|-------------|-------------|-------------|-------|-----------------|
| Water pH    | 0x15        | 2           | 0-14  | pH              |

- **Data Format**

| ID (Channel) | Type   | Data    |
|--------------|--------|---------|
| 1 Byte       | 1 Byte | 2 Bytes |

With the defined data, here's how to interpret the payload received data:

- **Data Example**

Payload (hexadecimal) received data is: `15 C1 04 3E`

| ID (Channel) | Type | Data |
|--------------|------|------|
| 15           | C1   | 043E |

`15C1` (Water pH) - `043E` (Data)

Convert the value to decimal:

````
04 3E (hex) = 1086 (dec)
1086 × 0.01 (conversion coefficient) = 10.86 pH
````

#### Environmental Requirements

##### Transportation Requirements

:::warning WARNING
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

- **Maintenance**: Charge and discharge the device once a month while storing it at room temperature or in a dry and ventilated environment. If storing the device takes more than 30 days, adjust the SOC to 40&nbsp;% after charging. 

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