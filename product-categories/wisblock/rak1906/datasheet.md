---
slug: /product-categories/wisblock/rak1906/datasheet/
title: RAK1906 WisBlock Environmental Sensor Module Datasheet
description: Provides comprehensive information about your RAK1906 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak1906/rak1906.png"
keywords:
  - datasheet
  - wisblock
  - RAK1906
sidebar_label: Datasheet
date: 2020-08-22
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'


# RAK1906 WisBlock Environmental Sensor Module Datasheet

## Overview

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1906/datasheet/rak1906.png"
  figureCount="1"
  caption="RAK1906 WisBlock Environmental Sensor"
   width="50%"
/>

### Description

The RAK1906 WisBlock Environmental Sensor Module, part of the RAK WisBlock Sensor series, is a 4-in-1 digital sensor board that comprises gas, humidity pressure, and temperature sensor, based on the Bosch® BME680 module. The RAK1906 is ideal for applications such as indoor air quality, home automation, and building IoT solutions.

### Features

* **Sensor specifications**
    * Voltage supply: 3.3&nbsp;V
    * Current consumption: 0.15&nbsp;uA to 350&nbsp;uA
    * Chipset: BOSCH BME680
    * Temperature range: -40&nbsp;°C to 85&nbsp;°C
    * Humidity range: 0 to 100%
    * Pressure range: 300&nbsp;hPa to 1100&nbsp;hPa
    * Gas sensor response time < 1&nbsp;sec
    * Sensor outputs can be used with the [Bosch BSEC library](https://github.com/BoschSensortec/BSEC-Arduino-library) algorithm to calculate the IAQ (Indoor Air Quality) index

* **Size**
    * 10 x 10&nbsp;mm

## Specifications
### Overview

#### Mounting

**Figure 2** shows the mounting mechanism of the RAK12001 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) board. The RAK12001 module can be mounted on the slots: **A, B, C, D, E, & F**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1906/datasheet/rak19xx_mounting.png"
  figureCount="2"
  caption="RAK1906 WisBlock Environmental Sensor Mounting"
   width="50%"
/>

### Hardware

The hardware specification is categorized into six parts. It shows the chipset of the module and discusses the pinouts, sensors, and the corresponding functions and diagrams. It also covers the electrical and mechanical parameters that include the tabular data of the functionalities and standard values of the RAK1906 WisBlock Environmental Sensor Module.


####  Chipset

| Vendor | Part Number |
| ------ | ----------- |
| BOSCH  | BME680      |

#### Pin Definition

The RAK1906 WisBlock Environmental Sensor Module comprises a standard WisBlock connector. The WisBlock connector allows the RAK1906 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 3**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1906/datasheet/rak1906_pinout.svg"
  figureCount="3"
  caption="RAK1906 WisBlock Environmental Sensor Pinout"
   width="60%"
/>

:::tip NOTE
Only the **I2C** related pin, **VDD**, and **GND** are connected to this module.
:::

If a 24-pin WisBlock Sensor connector is used, the IO used for the output pulse depends on what slot the module is plugged in. The following table shows the default IO used for different slots:

| SLOT A | SLOT B | SLOT C | SLOT D | SLOT E | SLOT F |
| ------ | ------ | ------ | ------ | ------ | ------ |
| WB_IO1 | WB_IO2 | WB_IO3 | WB_IO5 | WB_IO4 | WB_IO6 |


#### Sensors
##### Temperature Sensor
<table  align="center">
<thead>
  <tr>
    <th>Parameter</th>
    <th>Symbol</th>
    <th>Condition</th>
    <th>Min</th>
    <th>Typ</th>
    <th>Max</th>
    <th>Unit</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Operating Temperature Range</td>
    <td>T<sub>A</sub></td>
    <td>Operational</td>
    <td>-40</td>
    <td>25</td>
    <td>85</td>
    <td>°C</td>
  </tr>
  <tr>
    <td>Supply Current</td>
    <td>I<sub>DD,T</sub></td>
    <td>1&nbsp;Hz Forced Mode, Temperature Measurement Only</td>
    <td></td>
    <td>1.0</td>
    <td></td>
    <td>µA</td>
  </tr>
  <tr>
    <td rowspan="2">Absolute Accuracy Temperature</td>
    <td>A<sub>T,25</sub></td>
    <td>25&nbsp;°C</td>
    <td></td>
    <td>±0.5</td>
    <td></td>
    <td>°C</td>
  </tr>
  <tr>
    <td>A<sub>T,full</sub></td>
    <td>0-65&nbsp;°C</td>
    <td></td>
    <td>±1.0</td>
    <td></td>
    <td>°C</td>
  </tr>
  <tr>
    <td>Output Resolution</td>
    <td>R<sub>T</sub></td>
    <td>API Output Resolution </td>
    <td></td>
    <td>0.01</td>
    <td></td>
    <td>°C</td>
  </tr>
</tbody>
</table>

##### Humidity Sensor
<table align="center">
<thead>
  <tr>
    <th>Parameter</th>
    <th>Symbol</th>
    <th>Condition</th>
    <th>Min</th>
    <th>Typ</th>
    <th>Max</th>
    <th>Unit</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">Operating Range</td>
    <td></td>
    <td></td>
    <td>-40</td>
    <td>25</td>
    <td>85</td>
    <td>°C</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>0</td>
    <td></td>
    <td>100</td>
    <td>% r.H.</td>
  </tr>
  <tr>
    <td rowspan="2">Full Accuracy Range</td>
    <td></td>
    <td></td>
    <td>0</td>
    <td></td>
    <td>65</td>
    <td>°C</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>10</td>
    <td></td>
    <td>90</td>
    <td>% r.H.</td>
  </tr>
  <tr>
    <td>Supply Current </td>
    <td>I<sub>DD,H</sub></td>
    <td>1&nbsp;Hz Forced Mode, <p>Temperature and Humidity Measurement</p></td>
    <td></td>
    <td>2.1</td>
    <td>2.8</td>
    <td>µA</td>
  </tr>
  <tr>
    <td>Absolute Accuracy</td>
    <td>A<sub>h</sub></td>
    <td>20-80% r.H., 25&nbsp;°C, including hysteresis</td>
    <td></td>
    <td>±3</td>
    <td></td>
    <td>% r.H.</td>
  </tr>
</tbody>
</table>

##### Pressure Sensor
<table align="center">
<thead>
  <tr>
    <th>Parameter</th>
    <th>Symbol</th>
    <th>Condition</th>
    <th>Min</th>
    <th>Typ</th>
    <th>Max </th>
    <th>Unit</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">Operating Temperature Range</td>
    <td rowspan="2">T<sub>A</sub></td>
    <td>Operational</td>
    <td>-40</td>
    <td>25</td>
    <td>85</td>
    <td rowspan="2">°C</td>
  </tr>
  <tr>
    <td>Full Accuracy</td>
    <td>0</td>
    <td></td>
    <td>65</td>
  </tr>
  <tr>
    <td>Operating Pressure range</td>
    <td>P</td>
    <td>Full Accuracy</td>
    <td>300</td>
    <td></td>
    <td>1100</td>
    <td>hPa</td>
  </tr>
  <tr>
    <td>Supply Current</td>
    <td>I<sub>DD,LP</sub></td>
    <td>1&nbsp;Hz Forced Mode, Pressure, and Temperature, Lowest Power</td>
    <td></td>
    <td>3.1</td>
    <td>4.2</td>
    <td>µA</td>
  </tr>
  <tr>
    <td rowspan="2">Temperature Coefficient Of Offset</td>
    <td rowspan="2">TCO<sub>P</sub></td>
    <td rowspan="2">25-40&nbsp;°C, 900&nbsp;hPa</td>
    <td></td>
    <td>±1.3</td>
    <td></td>
    <td>Pa,K</td>
  </tr>
  <tr>
    <td></td>
    <td>±10.9</td>
    <td></td>
    <td>cm/K</td>
  </tr>
  <tr>
    <td>Absolute Accuracy Pressure</td>
    <td>A<sub>p,full</sub></td>
    <td>300-1100&nbsp;hPa <p>0-65&nbsp;°C</p></td>
    <td></td>
    <td>±0.6</td>
    <td></td>
    <td>hPa</td>
  </tr>
</tbody>
</table>

##### IAQ algorithm

:::tip NOTE
The IAQ is not calculated by the Bosch BME680 directly. The measured sensor values need to be send to the [Bosch BSEC library](https://github.com/BoschSensortec/BSEC-Arduino-library) algorithm to calculate the IAQ (Indoor Air Quality) index.
:::

<table align="center">
<thead>
  <tr>
    <th>Parameter</th>
    <th>Symbol</th>
    <th>Condition</th>
    <th>Min</th>
    <th>Typ</th>
    <th>Max </th>
    <th>Unit</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Accuracy Status</td>
    <td>AX<sub>IAQ</sub></td>
    <td>Android Compatible</td>
    <td>0</td>
    <td></td>
    <td>3</td>
    <td></td>
  </tr>
  <tr>
    <td>IAQ Resolution</td>
    <td>IAQ<sub>rs</sub></td>
    <td></td>
    <td></td>
    <td>1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>IAQ Range</td>
    <td>IAQ<sub>rg</sub></td>
    <td></td>
    <td>0</td>
    <td></td>
    <td>500</td>
    <td></td>
  </tr>
  <tr>
    <td>Sensor-to-sensor Deviation</td>
    <td>IAQ<sub>S2S</sub></td>
    <td>All Operation Modes</td>
    <td></td>
    <td>±15%<p>±15</p></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td rowspan="2">Durability To Siloxanes </td>
    <td>IAQ<sub>S2S</sub></td>
    <td>Sensor-to-sensor Deviation</td>
    <td></td>
    <td>±15%<p>±15</p></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>IAQ<sub>drift</sub></td>
    <td>Drift at Low &amp; High Concentrations</td>
    <td></td>
    <td>±1%<p>±4</p></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

#### Electrical Characteristics
##### Recommended Operating Conditions
| Symbol            | Description                 | Min.  | Nom.  | Max.  | Unit  |
| ----------------- | --------------------------- | :---: | :---: | :---: | :---: |
| V<sub>DD</sub>    | Power supply for the module | 1.71  |  3.3  |  3.6  |   V   |
| I<sub>sleep</sub> | Sleep current               |   -   | 0.15  |   -   |  uA   |
| I<sub>DD</sub>    | Humidity Measure current    |   -   |  340  |   -   |  uA   |
| I<sub>DD</sub>    | Pressure Measure current    |   -   |  714  |   -   |  uA   |
| I<sub>DD</sub>    | Temperature Measure current |   -   |  350  |   -   |  uA   |



#### Mechanical Characteristics

##### Board Dimensions

**Figure 4** shows the dimensions and the mechanic drawing of the RAK1906 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1906/datasheet/rak19xx_mechanic_drawing.png"
  figureCount="4"
  caption="RAK1906 WisBlock Environmental Sensor mechanic dimensions"
   width="60%"
/>

##### WisConnector PCB Layout

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1906/datasheet/mxxs1003k6m.png"
  figureCount="5"
  caption="WisConnector PCB footprint and recommendations"
   width="100%"
/>

#### Schematic Diagram

**Figure 6** shows the schematic of the RAK1906 module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1906/datasheet/rak1906-schematic.png"
  figureCount="6"
  caption="RAK1906 WisBlock Environmental Sensor schematics"
   width="100%"
/>

<RkBottomNav/>