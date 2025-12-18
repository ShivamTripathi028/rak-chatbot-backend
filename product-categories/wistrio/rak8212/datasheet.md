---
slug: /product-categories/wistrio/rak8212/datasheet/
title: RAK8212 WisTrio iTracker Pro Datasheet
description: Provides comprehensive information about your RAK8212 WisTrio iTracker Pro to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wistrio/rak8212/rak8212.png"
keywords:
  - wistrio
  - rak8212
  - tracker
  - datasheet
  - nb-iot
  - bluetooth
sidebar_label: Datasheet
---

# RAK8212 WisTrio iTracker Pro Datasheet

## Overview

### Description

The **iTracker Pro RAK8212** is versatile developer board aimed at aiding in quick prototypes using NB-IOT. The board includes a vast array of connectivity options like **NB-IoT**, **Bluetooth 5.0** and **GPS** and sensors like an **accelerometer**, **light sensor** and **barometric sensor**. At the heart of the module is the venerable **Nordic NRF52832 BLE** processor. The NB-IoT connectivity is provided by the **Quectel BG96 module**. The RAK8212 module is **Arduino friendly** and can be programmed using the IDE. The board also provides **SWD interface** for programming the **NRF52832** core. The combination of BLE and NB-IoT provides flexible low power consumption development along with myriad of application option ranging from telemetry to live tracking and environment sensing.

Applications can be made with the RAK8212 like Vehicle location/fleet transportation management, Safety monitoring of old/young children, Animal protection and animal husbandry management, Loss of assets / personnel positioning and Other remote, battery powered applications.

### Features

- **Arduino Compatible** – Host controller NRF52832 has been widely used in Arduino environment
- Integrated **Quectel BG96 NB-IoT wireless communication Module**, with GPS built-in
- Integrated **LIS3DH** ultra low-power, high performance 3-axes *nano* accelerometer
- Integrated **LIS2MDL** ultra-low-power, high-performance 3-axis digital magnetic sensor
- Integrated **BME280** ultra low-power, high linearity, high accuracy sensors for pressure, humidity, and temperature
- Integrated **OPT3001** that measures the intensity of visible light
- Size: **43 mm x 38 mm x 18 mm**
- **Operation temperature** -40° C to +85° C
- Power supply 3.3 V to 5 V (power at solar panel connector P2)

### Bluetooth

- **Bluetooth 5.0**
- Single chip,highly flexible, 2.4 GHz multi-protocol
- **32-bit ARM Cortex-M4F Processor**
- **512 kB flash + 64 kB RAM**
- Supports concurrent Bluetooth low energy/ANT protocol operation
- Up to +4 dBm output power
- -96 dBm sensitivity, Bluetooth low energy
- 2 data rates (2 Mbps/1 Mbps)
- PPI-maximum flexibility for power-efficient applications and code simplification
- Automated power management system with automatic power management of each peripheral
- Configurable I/O mapping for analog and digital I/O  3 x Master/Slave SPI
- 2 x Two-wire interface (I²C)
- UART (RTS/CTS)
- 3 x PWM
- AES HW encryption
- 12-bit ADC
- Real Time Counter (RTC)
- Digital microphone interface (PDM)
- On-chip balun
- (OTA) Over-the-Air firmware update

### Applications

- Vehicle location / fleet transportation management
- Safety monitoring of old / young children
- Animal protection and animal husbandry management
- Loss of assets / personnel positioning
- Other remote, battery powered applications

## Specifications

### Overview

The overview covers the RAK8212 board overview where the front and back views are presented. It also includes the block diagram that shows the core of the module.

#### Module Overview

> **Image:** RAK8212 WisTrio iTracker Pro Top View

> **Image:** RAK8212 WisTrio iTracker Pro Bottom View

#### Block Diagram

> **Image:** System Block Diagram

### Hardware

The hardware specification is categorized into six parts. It discusses the pinout and its corresponding functions and diagrams. It also covers the parameters and standard values of the board in terms of electrical and environmental

#### Pin Definition

> **Image:** RAK8212 Pin Definition

| NO  | Name         | Type     | Description                               |
| --- | ------------ | -------- | ----------------------------------------- |
| P1  | VDD_nRF      | P        | VCC33                                     |
| P1  | SWDIO        | DI/DO    | Debug                                     |
| P1  | SWDCLK       | DI       | Debug                                     |
| P1  | GND          |          | Ground                                    |
| P2  | VBUS         | P        | Charging interface/Connect to Solar panel |
| P2  | GND          |          | Ground                                    |
| P3  | BAT          | P        | Power Supply                              |
| P3  | TEMP         | O        | Charge indicator                          |
| P3  | GND          |          | Ground                                    |
| P4  | RESET        | Reset    | Reset                                     |
| P4  | VCC33        | P        | VCC33                                     |
| P4  | GND          |          | Ground                                    |
| P4  | TILT_DOUT    | DI/DO,AI | Extended interface                        |
| P5  | SENSOR_DOUT1 | DI/DO,AI | Extended interface                        |
| P5  | SENSOR_DOUT2 | DI/DO,AI | Extended interface                        |
| P5  | VCC33        | P        | VCC33                                     |
| P5  | GND          |          | Ground                                    |

#### General Specifications

##### Overall Specification

| **Model Name**            | RAK8212                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Dimension**             | **L x W x H**: 43 mm x 38 mm x 18 mm                                                                 |
| **Interface**             | Digital I/O, Analog input                                                                                           |
| **Frequency Band**        | **Cat.M1/Cat.NB1:**
LTE FDD: B1/B2/B3/B4/B5/B8/B12/B13/B18/B19/B20/B26/B28
LTE TDD: B39 (for Cat.M1 only) |
|                           | **EGPRS:** 850/900/1800/1900 MHz                                                                               |
| **Antenna Type**          | External antenna                                                                                                    |
| **Operating Temperature** | -40° C to +85° C                                                                                          |
| **Storage Temperature**   | -40° C to +85° C                                                                                          |
| **Power Supply**          | 3.5 V~18 V                                                                                                |

##### GPS Specification

| **Feature**          | **Description**                                |
| -------------------- | ---------------------------------------------- |
| Navigation Satellite | GPS, GLONASS, BeiDou/Compass, Galileo and QZSS |
| Protocols            | NMEA 0183                                      |

##### GPRS Specification

| **Feature**        | **Description**                                                                                                     |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Frequency Band     | **Cat.M1/Cat.NB1**:
LTE FDD: B1/B2/B3/B4/B5/B8/B12/B13/B18/B19/B20/B26/B28
LTE TDD: B39 (for Cat.M1 only) |
|                    | **EGPRS**:
850/900/1800/1900 MHz                                                                          |
| Data rate          | **Cat.M1**:
Max. 375 Kbps (DL), Max. 375 Kbps (UL)                                                   |
|                    | **Cat.NB1**:
Max. 32 Kbps (DL), Max. 70 Kbps (UL)                                                    |
|                    | **GPRS**:
Max. 85.6 Kbps (DL), Max. 85.6 Kbps (UL)                                                   |
|                    | **EDGE**:
Max. 236.8 Kbps (DL), Max. 236.8 Kbps (UL)                                                 |
| Message            | Send and receive point to point SMS                                                                                 |
|                    | Text and PDU mode                                                                                                   |
| Transmitting Power | Class 3 (23 dBm±2.7 dB) for LTE-FDD bands                                                                 |
|                    | Class 3 (23 dBm±2.7 dB) for LTE-TDD bands                                                                 |
|                    | Class 4 (33 dBm±2 dB) for GSM850                                                                          |
|                    | Class 4 (33 dBm±2 dB) for GSM900                                                                          |
|                    | Class 1 (30 dBm±2 dB) for DCS1800                                                                         |
|                    | Class 1 (30 dBm±2 dB) for PCS1900                                                                         |
|                    | Class E2 (27 dBm±3 dB) for GSM850 8-PSK                                                                   |
|                    | Class E2 (27 dBm±3 dB) for GSM900 8-PSK                                                                   |
|                    | Class E2 (26 dBm±3 dB) for DCS1800 8-PSK                                                                  |
|                    | Class E2 (26 dBm±3 dB) for PCS1900 8-PSK                                                                  |
| Sensitivity        | -103 dBm @ LTE-TDD B39 3GPP                                                                                    |
| Power              | Power Consumption under LTE Cat.M1 Network:                                                                         |
|                    | **OFF State**                                                                                                       |
|                    | Power down Leakage Current 8 µA                                                                                |
|                    | **Power Saving Mode**                                                                                               |
|                    | PSM @Real Network 10.4 µA                                                                                      |
|                    | **Standby State**                                                                                                   |
|                    | DRX=1.28 s @Real Network 1.99 mA                                                                          |
|                    | **Active State**                                                                                                    |
|                    | 23 dBm @Instrument 190 mA                                                                                 |
|                    | 18 dBm @Instrument 155 mA                                                                                 |
|                    | 12 dBm @Instrument 136 mA                                                                                 |
|                    | 0 dBm @Instrument 124 mA                                                                                  |
|                    | Data Transfer @Real Network 99 mA                                                                              |
|                    | Voice @Real Network 108 mA                                                                                     |
| Protocol           | TCP/UDP/PPP                                                                                                         |

#### RF Characteristics

| Item           | Specification                                                                                                                                 |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Frequency Band | Cat.M1/Cat.NB1: LTE FDD: B1/B2/B3/B4/B5/B8/B12/B13/B18/B19/B20/B26/B28 LTE TDD: B39 (for Cat.M1 only) 
EGPRS: 850/900/1800/1900 MHz |

#### Electrical Characteristics

##### Power Requirements

| Item         | Specification        |
| ------------ | -------------------- |
| Power Supply | 3.5 V~18 V |

#### Environmental Characteristics

| Item                  | Specification              |
| --------------------- | -------------------------- |
| Operating Temperature | -40° C to +85° C |
| Storage Temperature   | -40° C to +85° C |

#### Schematic Diagram

> **Image:** Schematic Diagram #1

> **Image:** Schematic Diagram #2

> **Image:** Schematic Diagram #3

> **Image:** Schematic Diagram #4

> **Image:** Schematic Diagram #5

### Firmware

Download the latest firmware of RAK8212 in the table provided below.

| Model     | Version  | Source                                                                                                |
| --------- | -------- | ----------------------------------------------------------------------------------------------------- |
| RAK8212   | V3.0.0.8 | [Download](https://downloads.rakwireless.com/Cellular/RAK8212/Firmware/RAK8212_Latest_Firmware.rar)   |
| RAK8212-M | V3.0.0.8 | [Download](https://downloads.rakwireless.com/Cellular/RAK8212/Firmware/RAK8212-M_Latest_Firmware.rar) |

