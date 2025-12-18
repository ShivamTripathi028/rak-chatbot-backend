---
title: RAK7244 WisGate Developer D4 Gateway Datasheet
description: Provides comprehensive information about your RAK7244 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
keywords:
- datasheet
- wisgate
- RAK7244
image: https://images.docs.rakwireless.com/wisgate/rak7244/quickstart/1.main/RAK7244.png
sidebar_label: Datasheet
---

    

# RAK7244 WisGate Developer D4 Gateway Datasheet

## Overview

### Description

The RAK7244 WisGate Developer D4 Gateway is a device that consists of a Raspberry Pi 4, a RAK2245 Pi HAT, which includes a GPS module and a Heat Sink for better performance and thermal heat dissipation management.

There is a total of 3 configuration options:

1. **RAK7244** - this is the base model with the Raspberry Pi 4 and RAK2245.
2. **RAK7244C** - this is the Cellular Version that includes the Raspberry Pi 4, RAK2245, and the RAK2013 Cellular Pi Hat
3. **RAK7244P** - · this version allows for powering the gateway via PoE by adding the RAK9003 Pi HAT to the base configuration (RPi 4 + RAK2245 + RAK9003)

The built-in RAK2245 Pi HAT uses the SX1301 RF front-end chip from Semtech®, which is a powerful LoRa digital processing engine. It is able to receive up to 8 LoRa packets simultaneously sent with different spreading factors on different channels and is available in multiple variants so it can be used for all LoRa Alliance® frequency bands. This unique capability allows for innovative network architectures to be implemented, that are advantageous over other short-range systems. The built-in RAK2013 Cellular Pi HAT in the RAK7244C is based on the EG95 from Quectel, which is an LTE CAT4 module optimized specifically for M2M and IoT Applications. The RAK7244P is particularly suitable for deployment in cases where there is existing networking infrastructure and PoE is provisioned.

The RAK7244 WisGate Developer D4 Gateway is ideal for prototyping, proof-of-concept demonstrations or evaluation of future deployment scenarios. It includes a ready to use Firmware based on Raspbian OS, that makes it possible to connect the Gateway to any standard LoRaWAN Server. It is developer friendly as the large Raspbian OS community is a well-established one. It is especially suited to addressing a variety of applications like Smart Grids, Intelligent Farms and other IoT Enterprise applications.

### Features

- Refreshed Case design with a new MCU (**Raspberry Pi4**)
- Preassembled, fully functioning **LoRaWAN Gateway**
- Full LoRaWAN Stack support (**version 1.0.2**)
- Supports for **8 channels** and spreading factors (SF7-SF12)
- Frequency band support: EU433, CN470, RU864, IN865, EU868, US915, AU915, KR920, AS923
- Tx Power: **27 dBm Max**
- RX Sensitivity: **-139dBm**
- Integrates **Ublox MAX-7Q GPS** module
- **Quectel EG95** LTE module (Optional with the RAK7244C model)
- **PoE 802.3 af** support (Optional with the RAK7244P model)

### Package Contents

> **Image:** RAK7244/RAK7244P Package Contents

> **Image:** RAK7244C Package Contents

## Specifications

### Overview

The overview covers the RAK7244 board overview and block diagram of the three configuration options:RAK7244, RAK7244C and RAK7244P.

#### Board Overview

The outer dimensions of Casing are 92mm x 68.3mm x 57.2mm (LxWxH) as shown below. They are the same for all 3 models: RAK7244/7244C/7244P. The example in Figure 3 is RAK7244C

> **Image:**  RAK7244C Casing Outer Dimensions

#### Block Diagram

##### RAK7244

The figure below summarizes the basic building blocks of RAK7244. The RAK2245 is an essential part of any of the RAK7244 models as it provides all LoRaWAN connectivity. It receives and transmits LoRa Frames and takes care of modulating/demodulating the signals among others. The processing of the LoRa Frames as well as higher level protocol related tasks is done by the embedded host system (Raspberry Pi). Received and processed LoRa Frames are being sent to a LoRaWAN Server. The segmentation of protocol related tasks is outside the scope of this document.

> **Image:** RAK7244 System Structure

##### RAK7244P

The figure below summarizes the basic building blocks of RAK7244P. It has the same functionality as far as LoRaWAN goes as RAK7244. In addition, there is the possibility to power the Gateway using a PoE 802.3 af compatible source (42-57VDC). This is made possible by the RAK9003 PoE HAT.

> **Image:** RAK7244P System Structure

##### RAK7244C

The figure below summarizes the basic building blocks of RAK7244C. It has the same functionality as far as LoRaWAN goes as RAK7244. Its backhaul capabilities, however, are enhanced, with the additional of the RAK2013 Cellular HAT. This allows the Gateway to use its LTE modem to forward data to the Cloud.

> **Image:** RAK7244C Gateway System Structure

### Hardware

The hardware specification is categorized into six parts. It discusses the interfacing, pinouts, and their corresponding functions and diagrams. It also covers the parameters of operating frequencies, antenna, electrical, and environmental.

#### Interfaces

##### RAK7244 / RAK7244P

> **Image:** RAK7244/RAK7244P Interfaces

##### RAK7244C

> **Image:** RAK7244C Interfaces

#### Pin Definition

There are 3 available configuration options for the RAK7244x:

1. RAK7244 - Raspberry Pi 4 + RAK2245 Pi hat
2. RAK7244C - Raspberry Pi 4 + RAK2245 Pi Hat + RAK2013 Cellular Pi Hat
3. RAK7244P - Raspberry Pi 4 + RAK2245 Pi Hat + RAK9003 PoE Hat.

##### RAK9003 Pi Hat

The RAK9003 Pi HAT is a PoE (802.3 af) board, that is designed to be mounted on top of the 40-pin connector on a Raspberry Pi 3/4.

> **Image:** RAK7244P Hardware Structure

For detailed information about the RAK9003 Pi Hat, go to the [RAK9003 PoE Hat Datasheet](https://docs.rakwireless.com/product-categories/wishat/rak9003-poe-pi-hat/datasheet/).

##### RAK2245 Pi Hat

The **RAK2245 Pi HAT** is an LPWAN Gateway Concentrator Module based on the Pi HAT standard, and can be mounted to Pi board with 40-pin connector. The image below shows the hardware structure of the LoRa portion which describes the integration between RAK2245 and Raspberry Pi 4.

> **Image:** RAK7244C LPWAN Developer Gateway Hardware Structure

For detailed information about the RAK2245 Pi Hat, Go to the [RAK2245 Pi Hat Datasheet](https://docs.rakwireless.com/product-categories/wislink/rak2245-pi-hat/datasheet/).

##### RAK2013 Pi HAT

The RAK2013 is an add-on board based on the Raspberry Pi HAT standard that can transmit UART data from Raspberry Pi to the Cellular network. It supports several cellular protocols, such as NB-IoT, CAT-M, CAT1 or CAT 4, by choosing different modular on the board. The device is capable of integrating audio codec and audio amplifier along with the carrier operator's network, plus it supports Voice Over LTE (VoLTE) function. It is easy to use with the earphone connector, MIC connector and speaker connector having an audio amplifier.

> **Image:** Cellular Hardware Structure

For detailed information about the RAK2013 Pi HAT, Go to the [RAK2013 Pi HAT Datasheet](https://docs.rakwireless.com/product-categories/wislink/rak2013/datasheet/).

#### RF Characteristics

##### Operating Frequencies

All models of the Developer Gateway support all LoRaWAN bands.

| **Region**    | **Frequency (Mhz)** |
| ------------- | ------------------- |
| Europe        | EU433, EU868        |
| China         | CN470               |
| Russia        | RU864               |
| India         | IN865               |
| North America | US915               |
| Australia     | AU915               |
| Korea         | KR920               |
| Asia          | AS923               |

##### LoRa

###### Transmitter RF

The RAK2245 has an excellent transmitter performance. It is highly recommended to use an optimized configuration for the power level configuration, which is part of the HAL. These results are in a mean RF output power level and current consumption.

| **PA Control** | **DAC Control** | **MIX Control** | **DIG Gain** | **Nominal RF Power Level (dBm)** |
| -------------- | --------------- | --------------- | ------------ | -------------------------------- |
| 0              | 3               | 8               | 0            | -6                               |
| 0              | 3               | 10              | 0            | -3                               |
| 0              | 3               | 14              | 0            | 0                                |
| 1              | 3               | 9               | 3            | 4                                |
| 1              | 3               | 8               | 0            | 8                                |
| 1              | 3               | 9               | 0            | 10                               |
| 1              | 3               | 11              | 0            | 12                               |
| 1              | 3               | 12              | 0            | 14                               |
| 1              | 3               | 13              | 0            | 16                               |
| 2              | 3               | 12              | 0            | 17                               |
| 2              | 3               | 13              | 0            | 19                               |
| 2              | 3               | 14              | 0            | 20                               |
| 3              | 3               | 10              | 0            | 0                                |
| 3              | 3               | 11              | 0            | 0                                |
| 3              | 3               | 12              | 0            | 25                               |
| 3              | 3               | 13              | 0            | 26                               |
| 3              | 3               | 14              | 0            | 27                               |

T = 25℃ at VDD = 5V (Typ.) as default if nothing else stated.

| **Parameter**                              | **Condition**            | **Min**  | **Typ.** | **Max**  |
| ------------------------------------------ | ------------------------ | -------- | -------- | -------- |
| **Frequency Range**                        |                          | 863 Mhz  |          | 870 Mhz  |
| **Modulation Techniques**                  | FSK/LoRaTM               |          |          |          |
| **TX Frequency Variation vs. Temperature** | Power Level Setting : 20 | -3 Khz   |          | +3 Khz   |
| **TX Power Variation vs. Temperature**     | Power Level Setting : 20 | -5 dBm   |          | +5 dBm   |
| **TX Power Variation**                     |                          | -1.5 dBm |          | +1.5 dBm |

###### Receiver RF

It is highly recommended, to use optimized RSSI calibration values, which is part of the HAL v3.1. For both, Radio 1 and 2, the RSSI-Offset should be set to -169.0. The following table gives typical sensitivity level of the RAK2245.

| **Signal Bandwidth (Khz)** | **Spreading Factor** | **Sensitivity (dBm)** |
| -------------------------- | -------------------- | --------------------- |
| 125                        | 12                   | -139                  |
| 125                        | 7                    | -126                  |
| 250                        | 12                   | -136                  |
| 250                        | 7                    | -123                  |
| 500                        | 12                   | -134                  |
| 500                        | 7                    | -120                  |

##### Cellular

The Quectel EG95 is part of the LTE CAT4 module series that are specially optimized for Machine to Machine (M2M) and Internet of Things (IoT) applications. Adopted from 3GPP Rel. 11 LTE technology, which delivers data rates of 150Mbps downlink and 50Mbps uplink.

| **Frequency**  | **EG95-E**                     | **EG95-NA**              |
| -------------- | ------------------------------ | ------------------------ |
| **LTE FDD**    | B1 / B3 / B7 / B8 / B20 / B28A | B2 / B4 / B5 / B12 / B13 |
| **WCDMA**      | B1 / B8                        | B2 / B4 / B5             |
| **GSM / EDGE** | 900 / 1800 MHz                 |                          |
| **Region**     | Europe                         | North America            |

#### Antenna Specifications

##### LoRa

The LoRa Antenna with RP-SMA male connector is shown in the image below:

> **Image:** LoRa Antenna Overview

###### Antenna Dimension

The figure below shows the antenna's mechanical dimension.

> **Image:** LoRa Antenna Dimension

###### Antenna Parameters

| Items                              | Specifications                 |
| ---------------------------------- | ------------------------------ |
| Voltage Standard Wave Radio (VSWR) | 1:1.5                          |
| Gain                               | -2.0 dBi                       |
| Working Temperature & Humidity | T:-35 ºC ~ +80 ºC, H: 0% ~ 95% |
| Storage Temperature & Humidity | T:-40 ºC ~ +85 ºC, H: 0% ~ 95% |

##### LTE

The LTE antenna for the Developer Gateway with RP-SMA male connector the covers working frequency band from 824MHz to 2690MHz. The antenna is shown in Figure 14.

> **Image:** LTE Antenna

###### Antenna Dimension

> **Image:** LTE Antenna Dimension

###### Antenna Parameters

| Items                              | Specifications                                 |
| ---------------------------------- | ---------------------------------------------- |
| Frequency (MHz)                    | 700 / 800 / 880 / 960 / 1710 / 1880 / 2170     |
| Voltage Standard Wave Radio (VSWR) | 9.3 / 4.6 / 3.6 / 4.9 / 9.3 / 4.4 / 15         |
| Gain (dBi)                         | 1.63 / 1.84 / 1.96 / 2.23 / 0.03 / 0.01 / 1.97 |
| Working Temperature & Humidity | T:-35 ºC ~ +80 ºC, H: 0% ~ 95%                 |
| Storage Temperature & Humidity | T:-40 ºC ~ +85 ºC, H: 0% ~ 95%                 |

##### GPS

The GPS antenna with SMA male connector for Pilot Gateway is shown below

> **Image:** GPS Antenna

###### GPS Antenna Dimension

> **Image:** GPS Antenna Dimensions

###### GPS Environmental Requirements

The antenna environmental requirements are listed in the table below:

| Conditions | Temperature     | Humidity |
| ---------- | --------------- | -------- |
| Working    | -35 ºC ~ +80 ºC | 0% ~ 95% |
| Storage    | -40 ºC ~ +85 ºC | 0% ~ 95% |

###### GPS Antenna Parameters

The GPS Antenna specifications are listed in the table below:

| Item                                        | Specifications        | PET  |
| ------------------------------------------- | --------------------- | ---- |
| Range of Receiving Frequency                | 1575.42±1.1           | ±2.5 |
| Center Frequency (MHz) w/ 30mm2 GND plane   | 1575.42               | ±3.0 |
| Bandwidth (MHz) (Return Loss ≤ -10dB)       | ≥10                   | ±0.5 |
| VSWR (in Center Frequency)                  | ≤2.0                  | ±0.5 |
| Gain (Zenith) (dBi Typ.) w/ 70mm2 GND Plane | 4.5                   | ±0.5 |
| Axial Ratio (dB) w/ 70mm2 GND Plane         | 3.0                   | ±0.2 |
| Polarization                                | Right-Handed Circular |      |
| Impedance (Ω)                               | 50                    |      |
| Frequency Temperature Coefficient (ppm/ºC)  | 0±10                  |      |

Amplifier Specifications are listed below:

| Item              | Specifications |
| ----------------- | -------------- |
| Frequency Range   | 1575.42 MHz    |
| Gain              | 27 dB          |
| VSWR              | ≤ 2.0 V        |
| Noise Coefficient | ≤ 2.0 dBm      |
| DC Voltage        | 3 ~ 5 V        |
| DC Current        | 5 ± 2 mA       |

Environmental test performance specifications are listed below:

| Item              | Normal Temp. | High Temp [1] | Low Temp [2] |
| ----------------- | ------------ | ------------- | ------------ |
| Amplifier Gain    | 27dB ± 2.0   | 27dB ± 2.0    | 27dB ± 2.0   |
| VSWR              | ≤ 2.0        | ≤ 2.0         | ≤ 2.0        |
| Noise Coefficient | ≤ 2.0        | ≤ 2.0         | ≤ 2.0        |

:::tip NOTE
**1** - High temperature test: soap in temperature (85º C) and humidity (95%) chamber for 24- hour and return to normal temperature (at least for 1-hour) without visual shape change.

**2** - Low temperature test: soap in temperature (-40º C) chamber for 24-hour and return to normal temperature (at least for 1-hour) without visual shape change
:::

#### Electrical Characteristics

The Pilot Gateway Pro operates at 5V/2.5A, that are provisioned through an USB Type C port.

| **Parameter**                   | **Min.** | **Typical** | **Max** |
| ------------------------------- | -------- | ----------- | ------- |
| **Current in CAT M mode**       |          | 300mA       |         |
| **Current in GSM mode (peak）** |          |             | 3500mA  |
| **Cellular power off mode**     |          | 10mA        |         |

#### Environmental Requirements

The table below lists the operation and storage temperature requirements for RAK7244:

| **Parameter**                   | **Min.** | **Typical** | **Max** |
| ------------------------------- | -------- | ----------- | ------- |
| **Operation Temperature Range** | -35 ˚C   | +25 ˚C      | +70 ˚C  |
| **Extended Temperature Range**  | -40 ˚C   |             | +75 ˚C  |
| **Storage Temperature Range**   | -40 ˚C   |             | +80 ˚C  |

### Firmware

Download the latest firmware of the RAK7244X series in the table provided below.

| Model                | Raspberry Pi Board | Firmware Version | Source                                                                                                                               |
| -------------------- | ------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| RAK7244 and RAK7244P | Raspberry Pi 4     | 4.2.6R           | [Download](https://downloads.rakwireless.com/LoRa/Developer-LoRaWAN-Gateway-RAK7244%26RAK7244P/Firmware/RAK7244_Latest_Firmware.zip) |
| RAK7244C             | Raspberry Pi 4     | 4.2.6R           | [Download](https://downloads.rakwireless.com/LoRa/Developer-LoRaWAN-Gateway-RAK7244C/Firmware/RAK7244C_Latest_Firmware.zip)          |

<!-- ## Certification -->
