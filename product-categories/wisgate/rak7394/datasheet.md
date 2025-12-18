---
title: RAK7394 WisGate Developer CM4 Datasheet
description: Provides comprehensive information about your RAK7394 WisGate Developer CM4 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisgate/rak7394/rak7394.png
keywords:
    - datasheet
    - wisgate
    - RAK7394
    - RAK7394P
    - RAK7394C
sidebar_label: Datasheet
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK7394 WisGate Developer CM4 Datasheet

## Overview

### Description

The **RAK7394 WisGate Developer CM4** is a LoRaWAN Gateway that has a cellular and a PoE variant. This gateway consists of a RAKR314 CM4 Carrier Board + Raspberry Pi Compute Module 4 (CM4), RAK2287 Concentrator, and RAK2287 Pi HAT.

- **Cellular Variant**: The RAK7394C includes the RAKR314 CM4 Carrier Board with a Raspberry Pi CM4, a RAK2287 Concentrator, a RAK2013 Cellular Pi HAT for cellular connectivity, and a RAK2287 Pi HAT.

- **PoE Variant**: The RAK7394P includes the RAKR314 CM4 Carrier Board with a Raspberry Pi CM4, a RAK2287 Concentrator, a RAK9003 for PoE support, and a RAK2287 Pi HAT.

The **RAK2287 Concentrator** includes a GPS module and a heat sink for better performance and thermal heat dissipation management, and its housing is built with an aluminum casing. It also uses the **SX1302** chip from Semtech® whose built-in LoRa concentrator IP core is a powerful digital signal processing engine. 

This concentrator can receive up to **8 LoRa packets** with different spreading factors on different channels and is available in multiple variants so it can be used for international standard bands. This unique capability allows the implementation of innovative network architectures advantageous over other short-range systems.

The **RAK2287 Pi HAT** is a converter board with a Raspberry Pi form factor that enables the RAK2287 module to be mounted on top of the RAKR314 CM4 Carrier Board. It integrates one (1) 40-pin female Pi HAT connector and one mPCIe connector to connect RAK2287 (RAK9003 in PoE variant/RAK2013 in Cellular variant) to the CM4 Carrier Board.

The **RAKR314 Carrier Board** is designed specifically for the Raspberry Compute Module CM4 following the Raspberry Pi4 form factor. This feature-packed board includes a standard 40 PIN GPIO and supports the RAK PoE HAT, making it an excellent choice for power-over-ethernet applications.

With two USB 2.0 ports, two USB 3.0 ports, two USB-type C ports (one for power and one for programming), and an Ethernet port, this board has all the connectivity options you need. The SD card slot also provides extra storage for the eMMC CM4 modules or serves as a main (boot) for non-eMMC modules. One of the best things about the RAKR314 is that it allows you to utilize the power of the CM4 module in the familiar Raspberry Pi form factor, so you can take advantage of all your existing HATs.

The **RAK7389** is designed for prototyping, proof-of-concept demonstrations, and evaluation. It features a ready-to-use LoRaWAN Gateway OS that connects seamlessly to a LoRaWAN server. With its developer-friendly design, it is easy to set up, even for users with limited technical expertise, making it an excellent choice for building LoRaWAN systems. Offering exceptional value and functionality, it supports a wide range of applications, including Smart Grid, Intelligent Farming, and other IoT enterprise solutions.

:::tip NOTE
By default, the CM4 comes with еMMC and the SD card can be used for additional storage. The SD card can be used for Boot only with CM4 Lite models.
:::

### Features

- Computing with Raspberry Pi Compute Module 4.
- Based on the LoRa Concentrator Engine: Semtech SX1302.
- Supports Cellular module (Quectel BG96 or EG95) for NB-IoT / LTE CAT-M1 / LTE CAT1 / LTE CAT4 (only in Cellular variant).
- Built-in Ublox ZOE-M8Q GPS Module.
- Built-in Heat Sink for thermal heat dissipation management.
- Supports 5&nbsp;V / 3&nbsp;A and Power-Over-Ethernet (only in PoE variant) power supply.
- IP30 housing.
- TX power up to 27&nbsp;dBm, RX sensitivity down to -139&nbsp;dBm @SF12, BW 125&nbsp;kHz.
- LoRa Frequency band support: RU864, IN865, EU868, US915, AU915, KR920, AS923.
- Includes Pi-ready 'ID EEPROM', GPIO setup, and device tree can be automatically configured from vendor information.
- Supports a fully open-source LoRaWAN server.

## Specifications

### Overview

The overview covers the RAK7394 board and block diagram.

#### Circuit Board Modules Stack

The basic building blocks of the RAK7394 are summarized in **Figures 1-3**. A key component is the RAK2287, which provides LoRaWAN connectivity. It handles the transmission and reception of LoRa Frames, as well as signal modulation and demodulation. 

Higher-level protocol tasks and the processing of LoRa Frames are managed by the embedded host system (Raspberry Pi). Processed LoRa Frames are then forwarded to a LoRaWAN Server. The segmentation of protocol-related tasks is beyond the scope of this document.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/datasheet/2.rak7394-structure.png"
  width="70%"
  caption="RAK7394 System Structure"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/datasheet/3.rak7394c-structure.png"
  width="70%"
  caption="RAK7394C System Structure"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/datasheet/4.rak7394p-structure.png"
  width="70%"
  caption="RAK7394P System Structure"
/>

#### Block Diagram

The RAK7394 serves as the central hardware solution for all LoRa-based radio communication. It handles the transmission and reception of radio messages, while the processing of these messages and protocol-related tasks is performed by the embedded host system (Raspberry Pi 4). Processed radio messages are forwarded to a LoRaWAN server. The block diagram of the RAK7394 is illustrated in **Figure 4**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/datasheet/7.block-diagram.png"
  width="80%"
  caption="RAK7394C Block Diagram"
/>

##### RAK9003 Pi HAT

:::tip NOTE
The specific segmentation of protocol-related tasks is beyond the scope of this document.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/datasheet/8.rak9003.png"
  width="60%"
  caption="RPi to RAK9003"
/>

##### RAK2013 Cellular Pi HAT

The **RAK2013 Cellular Pi HAT** is an add-on board designed according to the Raspberry Pi HAT standard. It enables the transmission of UART data from the Raspberry Pi through a Cellular network and operates in LTE CAT4 mode.

An additional feature of the board is the integrated audio codec and audio amplifier, which allow for VoLTE support. Thus, there is an earphone connector, MIC connector, and speaker connector with an audio amplifier.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/datasheet/9.rak2013.png"
  width="70%"
  caption="RAKR314 to RAK2013"
/>

### Hardware

#### Interfaces

The interfaces of RAK7394 are shown in **Figures 7 and 8**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/datasheet/5.rak7394-rak7394p-interfaces.png"
  width="90%"
  caption="RAK7394/RAK7394P Interfaces"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/datasheet/6.rak7394c-interfaces.png"
  width="70%"
  caption="RAK7394C Interfaces"
/>

#### RF Characteristics

##### Operating Frequencies

The RAK7394 models support all LoRaWAN bands.

<table>
    <thead>
        <tr>
            <th>Region</th>
            <th>Frequency (MHz)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Europe</td>
            <td>EU433</td>
        </tr>
        <tr>
            <td>China</td>
            <td>CN470</td>
        </tr>
        <tr>
            <td>Russia</td>
            <td>RU864</td>
        </tr>
        <tr>
            <td>India</td>
            <td>IN865</td>
        </tr>
        <tr>
            <td>Europe</td>
            <td>EU868</td>
        </tr>
        <tr>
            <td>North America</td>
            <td>US915</td>
        </tr>
        <tr>
            <td>Australia</td>
            <td>AU915</td>
        </tr>
        <tr>
            <td>Korea</td>
            <td>KR920</td>
        </tr>
        <tr>
            <td>Asia</td>
            <td>AS923</td>
        </tr>
    </tbody>
</table>


##### Cellular Frequency Bands (Only for RAK7394C)

The Quectel EG95 is a series of LTE CAT4 modules specifically optimized for M2M and IoT applications. Utilizing 3GPP Rel. 11 LTE technology, it offers data rates of 150&nbsp;Mbps for downlink and 50&nbsp;Mbps for uplink.

<table>
    <thead>
        <tr>
            <th>Frequency</th>
            <th>EG95-E</th>
            <th>EG95-NA</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>LTE FDD</td>
            <td>B1 / B3 / B7 / B8 / B20 / B28A</td>
            <td>B2 / B4 / B5 / B12 / B13</td>
        </tr>
        <tr>
            <td>WCDMA</td>
            <td>B1 / B8</td>
            <td>B2 / B4 / B5</td>
        </tr>
        <tr>
            <td>GSM / EDGE</td>
            <td>900 / 1800&nbsp;MHz</td>
            <td>-</td>
        </tr>
        <tr>
            <td>Region</td>
            <td>Europe</td>
            <td>North America</td>
        </tr>
    </tbody>
</table>

##### LoRa RF Characteristics

###### Transmitter RF Characteristics

The RAK7394 features excellent transmitter performance. It is highly recommended to use an optimized power level configuration, included as part of the HAL, to achieve balanced RF output power and current consumption.

<table>
    <thead>
        <tr>
            <th>PA Control</th>
            <th>PWID Control</th>
            <th>Power</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0</td>
            <td>10</td>
            <td>-6&nbsp;dBm</td>
        </tr>
        <tr>
            <td>0</td>
            <td>13</td>
            <td>-3&nbsp;dBm</td>
        </tr>
        <tr>
            <td>0</td>
            <td>17</td>
            <td>0&nbsp;dBm</td>
        </tr>
        <tr>
            <td>0</td>
            <td>20</td>
            <td>4&nbsp;dBm</td>
        </tr>
        <tr>
            <td>1</td>
            <td>0</td>
            <td>8&nbsp;dBm</td>
        </tr>
        <tr>
            <td>1</td>
            <td>2</td>
            <td>10&nbsp;dBm</td>
        </tr>
        <tr>
            <td>1</td>
            <td>4</td>
            <td>12&nbsp;dBm</td>
        </tr>
        <tr>
            <td>1</td>
            <td>7</td>
            <td>14&nbsp;dBm</td>
        </tr>
        <tr>
            <td>1</td>
            <td>9</td>
            <td>16&nbsp;dBm</td>
        </tr>
        <tr>
            <td>1</td>
            <td>10</td>
            <td>17&nbsp;dBm</td>
        </tr>
        <tr>
            <td>1</td>
            <td>12</td>
            <td>19&nbsp;dBm</td>
        </tr>
        <tr>
            <td>1</td>
            <td>13</td>
            <td>20&nbsp;dBm</td>
        </tr>
        <tr>
            <td>1</td>
            <td>16</td>
            <td>23&nbsp;dBm</td>
        </tr>
        <tr>
            <td>1</td>
            <td>18</td>
            <td>25&nbsp;dBm</td>
        </tr>
        <tr>
            <td>1</td>
            <td>20</td>
            <td>26&nbsp;dBm</td>
        </tr>
        <tr>
            <td>1</td>
            <td>22</td>
            <td>27&nbsp;dBm</td>
        </tr>
    </tbody>
</table>

:::tip NOTE
- Typically, there is a ±1.5&nbsp;dBi variance between the actual test values and the table data.  
- Unless otherwise specified, measurements are taken at T = 25°&nbsp;C and VDD = 5&nbsp;V (typical).
:::

<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Condition</th>
            <th>Min.</th>
            <th>Typical</th>
            <th>Max.</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Frequency Range</td>
            <td>-</td>
            <td>863&nbsp;MHz</td>
            <td>-</td>
            <td>870&nbsp;MHz</td>
        </tr>
        <tr>
            <td>Modulation Techniques</td>
            <td>FSK/LoRa</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td>TX Frequency Variation vs. Temperature</td>
            <td>Power Level Setting: 20</td>
            <td>-3&nbsp;kHz</td>
            <td>-</td>
            <td>+3&nbsp;kHz</td>
        </tr>
        <tr>
            <td>TX Power Variation vs. Temperature</td>
            <td>Power Level Setting: 20</td>
            <td>-5&nbsp;dBm</td>
            <td>-</td>
            <td>+5&nbsp;dBm</td>
        </tr>
        <tr>
            <td>TX Power Variation</td>
            <td>-</td>
            <td>-1.5&nbsp;dBm</td>
            <td>-</td>
            <td>+1.5&nbsp;dBm</td>
        </tr>
    </tbody>
</table>

###### Receiver RF Characteristics

It is highly recommended, to use optimized RSSI calibration values, which is part of the HAL v3.1. For both, Radio 1 and 2, the RSSI-Offset should be set at -169.0. The following table gives the typical sensitivity level of the RAK2287.

<table>
    <thead>
        <tr>
            <th>Signal Bandwidth (kHz)</th>
            <th>Spreading Factor</th>
            <th>Sensitivity (DBM)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>125</td>
            <td>12</td>
            <td>-139</td>
        </tr>
        <tr>
            <td>125</td>
            <td>7</td>
            <td>-125</td>
        </tr>
        <tr>
            <td>250</td>
            <td>12</td>
            <td>-136</td>
        </tr>
        <tr>
            <td>250</td>
            <td>7</td>
            <td>-123</td>
        </tr>
        <tr>
            <td>500</td>
            <td>12</td>
            <td>-134</td>
        </tr>
        <tr>
            <td>500</td>
            <td>7</td>
            <td>-120</td>
        </tr>
    </tbody>
</table>


#### Antenna Specifications

##### LoRa Antenna

The LoRa Antenna with RP-SMA male connector is shown in **Figure 9**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/datasheet/10.antenna.png"
  width="50%"
  caption="LoRa Antenna"
/>

###### LoRa Antenna Dimensions

The antenna's mechanical dimensions are shown in **Figure 10**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/datasheet/11.antenna-dimensions.png"
  width="40%"
  caption="LoRa Antenna Dimensions"
/>

###### LoRa Antenna Parameters

<table>
    <thead>
        <tr>
            <th>Item</th>
            <th>Specification</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Voltage Standard Wave Ratio (VSWR)</td>
            <td>1.5:1</td>
        </tr>
        <tr>
            <td>Gain</td>
            <td>-2.0&nbsp;dBi</td>
        </tr>
        <tr>
            <td>Working Temperature & Humidity</td>
            <td>T:-35°&nbsp;C ~ +80°&nbsp;C, H: 0%&nbsp;RH ~ 95%&nbsp;RH</td>
        </tr>
        <tr>
            <td>Storage Temperature & Humidity</td>
            <td>T:-40°&nbsp;C ~ +85°&nbsp;C, H: 0%&nbsp;RH ~ 95%&nbsp;RH</td>
        </tr>
    </tbody>
</table>


##### LTE Antenna

For a built-in BG96, there is one LTE antenna and one GPS antenna. For module built-in EG91/EG95, there are two LTE antennas and no GPS antenna.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/datasheet/12.lte-antenna.png"
  width="45%"
  caption="LTE Antenna"
/>

###### LTE Antenna Dimensions

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/datasheet/13.lte-antenna-dimensions.png"
  width="45%"
  caption="LTE Antenna Dimensions"
/>

###### LTE Antenna Parameters

<table>
    <thead>
        <tr>
            <th>Item</th>
            <th>Specification</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Frequency (MHz)</td>
            <td>700 / 800 / 880 / 960 / 1710 / 1880 / 2170</td>
        </tr>
        <tr>
            <td>Voltage Standard Wave Ratio (VSWR)</td>
            <td>9.3 / 4.6 / 3.6 / 4.9 / 9.3 / 4.4 / 15</td>
        </tr>
        <tr>
            <td>Gain</td>
            <td>1.63 / 1.84 / 1.96 / 2.23 / 0.03 / 0.01 / 1.97</td>
        </tr>
        <tr>
            <td>Working Temperature & Humidity</td>
            <td>T:-35°&nbsp;C ~ +80°&nbsp;C, H: 0%&nbsp;RH ~ 95%&nbsp;RH</td>
        </tr>
        <tr>
            <td>Storage Temperature & Humidity</td>
            <td>T:-40°&nbsp;C ~ +85°&nbsp;C, H: 0%&nbsp;RH ~ 95%&nbsp;RH</td>
        </tr>
    </tbody>
</table>


##### GPS Antenna

The GPS antenna with SMA Male Connector for Developer Gateway is shown in **Figure 13**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/datasheet/14.gps-antenna.png"
  width="40%"
  caption="GPS Antenna"
/>

###### GPS Antenna Dimensions

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/datasheet/15.gps-antenna-dimensions.png"
  width="50%"
  caption="GPS Antenna Dimensions"
/>

###### GPS Antenna Environmental Requirements

<table>
    <thead>
        <tr>
            <th>Conditions</th>
            <th>Temperature</th>
            <th>Humidity</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Working</td>
            <td>-35°&nbsp;C to +80°&nbsp;C</td>
            <td>0%&nbsp;RH ~ 95%&nbsp;RH</td>
        </tr>
        <tr>
            <td>Storage</td>
            <td>-40°&nbsp;C to +85°&nbsp;C</td>
            <td>0%&nbsp;RH ~ 95%&nbsp;RH</td>
        </tr>
    </tbody>
</table>

###### GPS Antenna Parameters

<table>
    <thead>
        <tr>
            <th>Items</th>
            <th>Specifications</th>
            <th>PET</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Range of Receiving Frequency</td>
            <td>1575.42±1.1</td>
            <td>±2.5</td>
        </tr>
        <tr>
            <td>Center Frequency (MHz) w/ 30&nbsp;mm2 GND plane</td>
            <td>1575.42</td>
            <td>±3.0</td>
        </tr>
        <tr>
            <td>Bandwidth (MHz) (Return Loss ≤ -10&nbsp;dB)</td>
            <td>≥10</td>
            <td>±0.5</td>
        </tr>
        <tr>
            <td>VSWR (in Center Frequency)</td>
            <td>≤2.0</td>
            <td>±0.5</td>
        </tr>
        <tr>
            <td>Gain (Zenith) (dBi Typ.) w/ 70&nbsp;mm2 GND Plane</td>
            <td>4.5</td>
            <td>±0.5</td>
        </tr>
        <tr>
            <td>Axial Ratio (dB) w/ 70&nbsp;mm2 GND Plane</td>
            <td>3.0</td>
            <td>±0.2</td>
        </tr>
        <tr>
            <td>Polarization</td>
            <td>Right-Handed Circular</td>
            <td>-</td>
        </tr>
        <tr>
            <td>Impedance (Ω)</td>
            <td>50</td>
            <td>-</td>
        </tr>
        <tr>
            <td>Frequency Temperature Coefficient (ppm/ºC)</td>
            <td>0±10</td>
            <td>-</td>
        </tr>
    </tbody>
</table>

##### Amplifier Specifications

<table>
    <thead>
        <tr>
            <th>Item</th>
            <th>Specification</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Frequency Range</td>
            <td>1575.42&nbsp;MHz</td>
        </tr>
        <tr>
            <td>Gain</td>
            <td>27&nbsp;dB</td>
        </tr>
        <tr>
            <td>VSWR</td>
            <td>≤ 2.0&nbsp;V</td>
        </tr>
        <tr>
            <td>Noise Coefficient</td>
            <td>≤ 2.0&nbsp;dBm</td>
        </tr>
        <tr>
            <td>DC Voltage</td>
            <td>3 ~ 5&nbsp;V</td>
        </tr>
        <tr>
            <td>DC Current</td>
            <td>5 ± 2&nbsp;mA</td>
        </tr>
    </tbody>
</table>

##### Environmental Test Performance Specifications

<table>
    <thead>
        <tr>
            <th>Item</th>
            <th>Normal Temp.</th>
            <th>High Temp.</th>
            <th>Low Temp.</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amplifier Gain</td>
            <td>27&nbsp;dB ± 2.0</td>
            <td>27&nbsp;dB ± 2.0</td>
            <td>27&nbsp;dB ± 2.0</td>
        </tr>
        <tr>
            <td>VSWR</td>
            <td>≤ 2.0</td>
            <td>≤ 2.0</td>
            <td>≤ 2.0</td>
        </tr>
        <tr>
            <td>Noise Coefficient</td>
            <td>≤ 2.0</td>
            <td>≤ 2.0</td>
            <td>≤ 2.0</td>
        </tr>
    </tbody>
</table>

:::tip NOTE
- **High-Temperature Test**: The device was placed in a chamber for 24 hours with the temperature set to 85°&nbsp;C and humidity at 95%&nbsp;RH. Afterward, the temperature was returned to normal for at least an hour. **The device showed no physical deformation.**
- **Low-Temperature Test**: The device was placed in a chamber for 24 hours with the temperature set to -40°&nbsp;C. Afterward, the temperature was returned to normal for at least an hour. **The device showed no physical deformation.**
:::

#### Electrical Requirements

The RAK7394/RAK7394C/RAK7394P operates at 5&nbsp;V / 3&nbsp;A, which is provisioned through a USB Type-C port.

<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Min.</th>
            <th>Typical</th>
            <th>Max.</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>LoRa Tx mode</td>
            <td>-</td>
            <td>-</td>
            <td>950&nbsp;mA</td>
        </tr>
        <tr>
            <td>Standby power</td>
            <td>-</td>
            <td>550&nbsp;mA</td>
            <td>-</td>
        </tr>
        <tr>
            <td>Burn test mode</td>
            <td>-</td>
            <td>-</td>
            <td>940&nbsp;mA</td>
        </tr>
    </tbody>
</table>

#### Mechanical Dimension

The outer dimension of RAK7394 is **92 x 68.3 x 57.2&nbsp;mm**.

:::tip NOTE
The dimensions are identical for both the RAK7394C and RAK7394P variants.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/datasheet/1.dimensions.png"
  width="40%"
  caption="RAK7394/RAK7394C/RAK7394P Dimensions"
/>

#### Environmental Requirements

<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Min.</th>
            <th>Typical</th>
            <th>Max.</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Operation Temperature Range</td>
            <td>-10°&nbsp;C</td>
            <td>+25°&nbsp;C</td>
            <td>+55°&nbsp;C</td>
        </tr>
        <tr>
            <td>Storage Temperature Range</td>
            <td>-40°&nbsp;C</td>
            <td>-</td>
            <td>+85°&nbsp;C</td>
        </tr>
    </tbody>
</table>

#### Firmware/OS

| Version |                                                                       Source                                                                       |
| :-----: | :------------------------------------------------------------------------------------------------------------------------------------------------: |
| v0.7.1  | [Download](https://downloads.rakwireless.com/LoRa/Software_Firmware/RAKPiOS/History-Version-Release/20230815-rakpios-0.7.1-RAK7394-arm64-lite.zip) |

<RkBottomNav/>