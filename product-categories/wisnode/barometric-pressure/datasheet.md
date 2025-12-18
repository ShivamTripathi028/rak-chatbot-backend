---
slug: /product-categories/wisnode/barometric-pressure/datasheet/
title: Barometric Pressure Monitoring Solution Datasheet
description: Provides comprehensive information about your Sensor Hub Barometric Pressure solution to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/barometric-pressure-sensor.png"
keywords:
  - datasheet
  - wisnode
  - sensor hub
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# Barometric Pressure Monitoring Solution - Datasheet

## Solution Overview

### Description

The Sensor Hub Barometric Pressure Monitoring solution is a version of the Sensor Hub that includes the popular RAK1902 barometric pressure sensor in the [Sensor Probe.](https://store.rakwireless.com/products/atmosphere-monitoring?m=3&h=sensorhub-solution&variant=42510932508870) This solution can be used in scenarios with critical requirements for barometric pressure, such as meteorology, aviation, marine navigation, engineering, and construction, among others.

With the plug-and-play feature of the Sensor Hub, the Barometric Pressure Solution comes with pre-installed components ready for easy installation and connection. The sensor provides highly accurate barometric pressure readings, with the Sensor Hub collecting and transmitting the data via LoRaWAN or NB-IoT/CAT M1.

The Sensor Hub’s connectivity function allows for versatile data transmission to the cloud using the two most commonly used communication protocols in IoT. This versatility ensures that data is readily available for storage, visualization, and in-depth analysis, enabling informed decision-making based on comprehensive knowledge of barometric pressure levels.

### Features

- Supports LoRa® and NB -IoT/LTE CAT-M wireless communication modes
- Support LoRa frequency band: CN470, EU868, IN865, RU864, US915, AU915,  KR920, and AS923-1/2/3/4
- Easy to configure, and the network access configuration can be completed through the WisToolBox app on mobile devices.
- Single wire protocol
- Automatic recognition of the sensor type
- Low power consumption
  - External DC power supply (optional)
  - Solar panel power supply (optional)
- Long transmission distance
- Waterproof (probe body protection level: IP67)
- Easy to install

###  Device List

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/datasheet/f1barpressolution_accesories.png"
  width="100%"
  caption="Device List"
/>

| Device List                              | Description                             |
|------------------------------------------|-----------------------------------------|
| 1 x Sensor Hub<br/>1 x Mounting Kit      | Sensor Hub + SensorHub Installation Kit |
| 1 x Micro Sensor Probe                   | RAK1902 Barometric Pressure Sensor      |
| 1 x Power Adapter <br /> 1 x Power Cable | Sensor Hub Power Adapter + Power Cable  |
| 1 x Cable Tie                            | For wiring or fixing                    |

## Hardware Specifications

### Sensor Hub Datasheet

For more detailed information about the Sensor Hub, refer to the [Sensor Hub Datasheet.](https://docs.rakwireless.com/product-categories/wisnode/rak2560/hub-datasheet#overview)

### RAK1902 Barometric Pressure Sensor Datasheet

| Parameter                    | Value                    |
|------------------------------|--------------------------|
| Pressure Range               | 260 ~ 1260&nbsp;hPa      |
| Pressure Precision           | ± 0.1&nbsp;hPa           |
| Pressure Sensitivity         | 4096&nbsp;LSB/hPa        |
| RMS Pressure Sensing Noise   | 0.0075&nbsp;hPa&nbsp;RMS |
| Pressure Output Data Rate    | 1/10/25/50/75 Hz         |
| Temperature Range            | -40°&nbsp;C ~ 85°&nbsp;C |
| Temperature Precision        | ±1.5°&nbsp;C             |
| Temperature Output Data Rate | 1/10/25/50/75&nbsp;Hz    |
| Interface                    | I2C                      |
| Module Size                  | 10&nbsp;mm x 10&nbsp;mm  |
| VDD (module power supply)    | 1.7&nbsp;V ~ 3.6&nbsp;V  |
| Shutdown Current             | 1&nbsp;uA                |

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
| Battery Cell    | Commonly known as a battery is the fundamental unit of energy storage, which converts chemical energy to electrical energy.                                                                                                                                                                                           |
| Battery Module  | Intermediate energy storage unit, comprising several individual cells and circuitry components, along with electrical and communication interfaces.                                                                                                                                                                   |
| Battery Pack    | A comprehensive power system consisting of multiple battery modules and circuits working together to supply power to electrical devices.                                                                                                                                                                              |
| Rated Voltage   | Refers to the approximate voltage value that a battery is designed to operate at or provide.                                                                                                                                                                                                                          |
| Capacity        | The amount of electrical charge that a fully charged battery can store and subsequently provide to a device or system. It is typically measured in ampere-hours (Ah).                                                                                                                                                 |
| Energy Capacity | The total amount of energy that a fully charged battery can deliver under specific conditions.<br/>Unit: Watt-hours (Wh) or kilowatt-hours (kWh)                                                                                                                                                                      |
| Rated Capacity  | At the beginning of life (BOL), the minimum capacity that a fully charged battery can provide at a discharge rate of 1 C (discharge C-rate).                                                                                                                                                                          |
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

As shown in **Figure 2**, the RAK9154 battery system comprises two sets of three 2600 mAh battery units connected in series. The system also incorporates one (1) BMS board integrated with an 18 V input solar charger.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/datasheet/f2barpressolution_dimensions.png"
  width="80%"
  caption="RAK9154 battery system"
/>

- **Electrical Characteristics**

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/datasheet/f3barpressolution_bdiagram1.png"
  width="80%"
  caption="RAK9154 electrical schematic diagram"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/barometric-pressure-sensor/datasheet/f4barpressolution_bdiagram2.png"
  width="80%"
  caption="System circuit schematic diagram"
/>



##### Battery System Panel Connector

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
      <td rowSpan = "5">SP11  <br/> IP67 <br/> Rated current 2&nbsp;A  <br/> Contact diameter 0.75&nbsp;mm * 5</td>
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
      <td rowSpan = "2">SP11  <br/> IP67 <br/> Rated current 1&nbsp;A  <br/> Contact diameter 1.0&nbsp;mm * 2</td>
    </tr>
    <tr>
      <td>Pin1: PV-</td>
    </tr>
  </tbody>
</table>


#### Sensor Characteristics

The following tables show the sensor data definition and the data format of the Barometric Pressure Monitoring Solution. 

- <b>Register Summary</b>
  
| Sensor Name | Sensor Type | Data Length | Ratio |   Range    |   Unit   |
|:-----------:|:-----------:|:-----------:|:-----:|:----------:|:--------:|
| Temperature |    0x67     |      2      |  0.1  |  -40 ~ 85  | °&nbsp;C |
|  Barometer  |    0x73     |      2      |  0.1  | 260 ~ 1260 |   hPa    |

- <b>Data Interpretation</b>

| ID (Channel) |  Type  |  Data   |
|:------------:|:------:|:-------:|
|    1 byte    | 1 byte | 2 bytes |

With the defined data, here's how to interpret the payload received data:

<b> Data Example: </b> 

Payload (hex) received data: `0367 00CA 0473 24F5`

- **Temperature Sensor Data Unit**

| ID (Channel) | Type | Data |
|:------------:|:----:|:----:|
|      03      |  67  | 00CA |

Convert the value to decimal:

Temperature: `0367`, 
Data: `000CA`

```
00CA (hex) = 202 (dec)
202 × 0.1 (conversion factor) = 20.2°&nbsp;C
```

- **Barometric Pressure Sensor Data Unit**

| ID (Channel) | Type | Data |
|:------------:|:----:|:----:|
|      04      |  73  | 24F5 |

Convert the value to decimal:

Temperature: `0473`, 
Data: `24F5`

```
24F5 (hex) = 9461 (dec)
9461 × 0.1 (conversion factor) = 946.1 hPa
```

#### Environmental Requirements

##### Transportation Requirements

:::warning
- When transporting the battery, avoid severe vibrations, shaking, and exposure to sunlight or rain. 
- Do not invert the battery to prevent potential short circuits. 
- During loading and unloading, exercise caution to prevent the battery from falling, rolling, enduring heavy pressure, or being inverted. 
:::

##### Storage Requirements

Store the module in a partially charged state, typically around 40&nbsp;% state of charge (SOC). Ensure the storage environment meets the following requirements:

<b>Temperature and Humidity</b>

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Value</th>
      <th>Remark</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowSpan = "2">Temperature</td>
      <td>-30°&nbsp;C to 50°&nbsp;C, 40% SOC</td>
      <td>Storage time < 3&nbsp;months</td>
    </tr>
    <tr>
      <td>0°&nbsp;C to 25°&nbsp;C, 40% SOC</td>
      <td>Storage time > 3&nbsp;months</td>
    </tr>
    <tr>
      <td>Humidity</td>
      <td>2%RH to 90%RH</td>
      <td> < 85% Recommended </td>
    </tr>
  </tbody>
</table>

- **Storage Environment**: 
    - Store the product in a clean, ventilated, and cool environment.
    - Avoid direct sunlight, high temperatures, corrosive gases, severe vibration, mechanical shaking, and heavy pressure.
    - Keep the product away from heat sources and store it at an altitude below 1500&nbsp;meters, maintaining atmospheric pressure between 86&nbsp;kPa and 106&nbsp;kPa.

- **Maintenance**: 
    - Charge and discharge the device once a month while storing it at room temperature or in a dry and ventilated environment. 
    - If storing the device takes more than 30 days, adjust the SOC to 40&nbsp;% after charging. 
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

<RkBottomNav/>