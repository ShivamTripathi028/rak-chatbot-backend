---
slug: /product-categories/wislink/rak5146/datasheet/
title: RAK5146 LoRaWAN Gateway Module Datasheet | Specs & Features 
description: View the datasheet for RAK5146, a high-performance LoRaWAN gateway module with SX1303, SX126X transceiver, GPS module, and Listen Before Talk (LBT) feature.
image: "https://images.docs.rakwireless.com/wislink/rak5146/rak5146.png"
keywords:
  - rak5146
  - rak5146 lorawan concentrator
  - rak5146 datasheet
  - rak5146 specifications
  - rak lorawan gateway module datasheet
  - rak5146 hardware specifications
  - integrating rak5146 with embedded systems
  - rak5146 power consumption
  - mni-pcie lorawan concentrator
  - listen before talk feature for lorawan networks
  - sx126x lora transceiver
  - sx1303 baseband processor
  - zoe-m8q gps module
  - lorawan gateway concentrator specs
  - lora concentrator gps module datasheet
  - multichannel lorawan concentrator specifications
  - fine timestamp for lorawan networks
  - lorawan concentrator with sx1303
  - iot gps module for lorawan
tags:
  - rak5146
  - wislink
  - datasheet
sidebar_label: Datasheet
date: 2021-04-11
---

# RAK5146 WisLink LoRaWAN Concentrator Datasheet

## Overview

### Product Description

The **RAK5146** is an LPWAN Concentrator Module in a mini-PCIe form factor, featuring the Semtech SX1303 and SX126X for the Listen Before Talk (LBT) feature, enabling seamless integration into existing routers or other network equipment with LPWAN Gateway capabilities.

This concentrator can be used with any embedded platform that has an available mini-PCIe slot with SPI/USB connectivity. Additionally, it includes an onboard **ZOE-M8Q GPS** chip.

This module offers an exceptional, comprehensive, and cost-efficient gateway solution. It provides up to 10 programmable parallel demodulation paths, an 8 x 8 channel LoRa packet detector, 8 x SF5-SF12 LoRa demodulators, and 8 x SF5-SF10 LoRa demodulators.

Additionally, RAK5146 can detect an uninterrupted combination of packets at 8 different spreading factors and 10 channels. It can continuously demodulate up to 16 packets, making it suitable for smart metering fixed networks and Internet-of-Things (IoT) applications.

### Product Features

- Designed based on **Mini PCI-e form factor**
- **SX1303 baseband processor** emulates 8 x 8 channels LoRa packet detectors, 8x SF5-SF12 LoRa demodulators, 8x SF5-SF10 LoRa demodulators, one 125/250/500 kHz high-speed LoRa demodulator, and one (G)FSK demodulator
- 3.3 V **Mini PCI-e**, compatible with **3G/LTE card** of Mini PCI-e type
- Tx power up to 27 dBm, Rx sensitivity down to -139 dBm @ SF12, BW 125 kHz
- Supports **global license-free frequency band**: EU868, EU433, RU864, CN470, US915, AS923, AU915, KR920, and IN865
- Supports optional **SPI/USB** interfaces.
- Listen Before Talk
- Fine Timestamp
- Built-in **ZOE-M8Q** GPS module

## Specifications

### Overview

The overview shows the top and back views of the RAK5146 board. It also presents the block diagram that discusses how the board works.

#### Board Overview

The RAK5146 is a compact LPWAN Gateway Module, making it suitable for integration in systems where mass and size constraints are essential. It has been designed with the PCI Express Mini Card form factor in mind, so it can easily become a part of products that comply with the standard, where they allow cards with a thickness of at least 5.5 mm.

The board has two UFL interfaces for the LoRa and GNSS antennas and a standard 52-pin connector (mPCIe).

> **Image:** Board Overview

#### Block Diagram

The RAK5146 concentrator is equipped with one SX1303 chip and two SX1250 chips. One SX1303 chip is used for RF signal processing and serves as the core of the device, while the other SX1250 chip handles the related LoRa modem and processing functionalities.

Additional signal conditioning circuitry is implemented to comply with the PCI Express Mini Card standard, and one UFL connector is provided for the integration of external antennas.

> **Image:** Block Diagram

### Hardware

The hardware is categorized into seven (7) parts. It discusses the interfacing, pinouts, and its corresponding functions and diagrams. It also covers the parameters and standard values of the board.

#### Interfaces

##### Power Supply

The RAK5146 concentrator module must be powered through the 3.3 Vaux pins by a DC power supply. It is crucial that the voltage remains stable, as the current drawn can vary significantly during operation, depending on the power consumption profile of the SX1303 chip. For more detailed information, refer to the [SX1303 Datasheet](https://www.mouser.com/pdfDocs/Semtech_DS_SX1303_W_APP_V12.pdf?srsltid=AfmBOorRE9ZyQGK-xv0f898zlxmmsGZkUw15zWufE9kwhomDklU-DTuu).

##### SPI Interface

SPI interface mainly provides for the Host_SCK, Host_MISO, Host_MOSI, Host_CSN pins of the system connector. The SPI interface gives access to the configuration register of SX1303 via a synchronous full-duplex protocol. Only the slave side is implemented.

##### USB Interface

The USB interface mainly provides for the USB_D+, USB_D- pins of the system connector. The USB interface gives access to the configuration register of SX1303 via an MCU STM32L412KBU6. Only the slave side is implemented.

##### UART and I2C Interface

The RAK5146 integrates a ZOE-M8Q GPS module, which supports both UART and I2C interfaces. The PINs on the golden finger provide a UART connection and an I2C connection, which allows direct access to the GPS module. The PPS (Pulse Per Second) signal is connected internally to the SX1303, as well as to the golden finger, making it available for use by the host board.

##### GPS_PPS

The RAK5146 includes the GPS_PPS input for received packets time-stamped and Fine timestamp.

##### RESET

The RAK5146 SPI card includes the RESET active-high input signal to reset the radio operations as specified by the SX1303 Specification. RAK5146 USB card’s RESET is controlled by the MCU.

##### Antenna RF Interface

The module has one RF interface over a standard UFL connector (Hirose U. FL-R-SMT) with a characteristic impedance of 50 Ω. The RF port (J1) supports both Tx and Rx, providing the antenna interface.

#### Pin Definition

> **Image:** Pinout Diagram

| Type | Description    |
| ---- | -------------- |
| IO   | Bidirectional  |
| DI   | Digital input  |
| DO   | Digital output |
| OC   | Open collector |
| OD   | Open drain     |
| PI   | Power input    |
| PO   | Power output   |
| NC   | No connection  |

| Pin No. | mPCIe Pin Rev. 2.0 | RAK5146 Pin   | Type | Description                                 | Remarks                                                                        |
| ------- | ------------------ | ------------- | ---- | ------------------------------------------- | ------------------------------------------------------------------------------ |
| 1       | WAKE#              | SX1261_BUSY   | DO   | No connection by default                    | Reserved for future applications                                               |
| 2       | 3.3 Vaux      | 3V3           | PI   | 3.3 V<sub>DC</sub> supply              |                                                                                |
| 3       | COEX1              | SX1261_DIO1   | IO   | No connection by default                    | Reserved for future applications                                               |
| 4       | GND                | GND           |      | Ground                                      |                                                                                |
| 5       | COEX2              | SX1261_DIO2   | IO   | No connection by default                    | Reserved for future applications                                               |
| 6       | 1.5 V         | GPIO(6)       | IO   | No connection by default                    | Connect to the SX1303's GPIO (6)                                               |
| 7       | CLKREQ#            | SX1261_NSS    | DI   | No connection by default                    | Reserved for future applications                                               |
| 8       | UIM_PWR            | NC            |      | No connection                               |                                                                                |
| 9       | GND                | GND           |      | Ground                                      |                                                                                |
| 10      | UIM_DATA           | NC            |      | No connection                               |                                                                                |
| 11      | REFCLK-            | SX1261_NRESET | DI   | No connection by default                    | Reserved for future application                                                |
| 12      | UIM_CLK            | NC            |      | No connection                               |                                                                                |
| 13      | REFCLK+            | MCU_NRESET    | DI   | RESET signal for MCU of RAK5146-USB         | Active low                                                                     |
| 14      | UIM_RESET          | NC            |      | No connection                               |                                                                                |
| 15      | GND                | GND           |      | Ground                                      |                                                                                |
| 16      | UIM_VPP            | NC            |      | No connection                               |                                                                                |
| 17      | RESERVED           | NC            |      | No connection                               |                                                                                |
| 18      | GND                | GND           |      | Ground                                      |                                                                                |
| 19      | RESERVED           | PPS           | DO   | Time pulse output                           | Leave open if not in use                                                       |
| 20      | W_DISABLE#         | NC            |      | No connection                               |                                                                                |
| 21      | GND                | GND           |      | Ground                                      |                                                                                |
| 22      | PERST#             | SX1303_RESET  | DI   | RAK5146-SPI reset input                     | Active high, ≥100 ns for SX1303 reset                                     |
| 23      | PERn0              | RESET_GPS     | DI   | GSP module ZOE-M8Q reset input              | Active low, leave open if not in use                                           |
| 24      | 3.3Vaux            | 3v3           | PI   | 3.3 V<sub>DC</sub> supply              |                                                                                |
| 25      | PERp0              | STANDBY_GPS   | DI   | GPS module ZOE-M8Q external interrupt input | Active low, leave open if not in use                                           |
| 26      | GND                | GND           |      | Ground                                      |                                                                                |
| 27      | GND                | GND           |      | Ground                                      |                                                                                |
| 28      | 1.5 V         | GPIO(8)       |      | Connect to the SX1303's GPIO (8)            |                                                                                |
| 29      | GND                | GND           |      | Ground                                      |                                                                                |
| 30      | SMB_CLK            | I2C_SCL       | IO   | HOST SCL                                    | Connect to GPS module ZOE-M8Q's SCL internally, leave open if not in use       |
| 31      | PETn0              | PI_UART_TX    | DI   | HOST UART_TX                                | Connect to GPS module ZOE-M8Q's UART_RT internally, leave open if not in use   |
| 32      | SMB_DATA           | I2C_SDA       | IO   | HOST SDA                                    | Connect to GPS module ZOE-M8Q's SDA internally, leave open if not in use       |
| 33      | PETp0              | PI_UART_RX    | DO   | HOST UART_RX                                | ` Connect to GPS module ZOE-M8Q's UART_TX internally, leave open if not in use |
| 34      | GND                | GND           |      | Ground                                      |                                                                                |
| 35      | GND                | GND           |      | Ground                                      |                                                                                |
| 36      | USB_D-             | USB_DM        | IO   | USB differential data (-)                   | Require differential impedance of 90 Ω                                    |
| 37      | GND                | GND           |      | Ground                                      |                                                                                |
| 38      | USB_D+             | USB_DP        | IO   | USB differential data (+)                   | Require differential impedance of 90 Ω                                    |
| 39      | 3.3 Vaux      | 3V3           | PI   | 3.3 V<sub>DC</sub> supply              |                                                                                |
| 40      | GND                | GND           |      | Ground                                      |                                                                                |
| 41      | 3.3Vaux            | 3V3           | Pi   | 3.3 V<sub>DC</sub> supply              |                                                                                |
| 42      | LED_WWAN#          | NC            |      | No connection                               |                                                                                |
| 43      | GND                | GND           |      | Ground                                      |                                                                                |
| 44      | LED_WLAN#          | NC            |      | No connection                               |                                                                                |
| 45      | RESERVED           | HOST_SCK      | IO   | Host SPI SCK                                |                                                                                |
| 46      | LED_WPAN#          | NC            |      | No connection                               |                                                                                |
| 47      | RESERVED           | HOST_MISO     | IO   | Host SPI MISO                               |                                                                                |
| 48      | 1.5 V         | NC            |      | No connection                               |                                                                                |
| 49      | RESERVED           | HOST_MOSI     | IO   | Host SPI MOSI                               |                                                                                |
| 50      | GND                | GND           |      | Ground                                      |                                                                                |
| 51      | RESERVED           | HOST_CSN      | IO   | Host SPI CSN                                |                                                                                |
| 52      | 3.3 Vaux      | 3V3           | PI   | 3.3 V<sub>DC</sub> supply              |                                                                                |

#### LED Definition

> **Image:** RAK5146 LED Definition

#### RF Characteristics

##### Operating Frequencies

The board supports the following LoRaWAN frequency channels, allowing easy configuration while building the firmware from the source code.

| Region        | Frequency (MHz)   |
| ------------- | ----------------- |
| Europe        | EU868 
 EU433 |
| North America | US915             |
| Russia        | RU864             |
| Asia          | AS923             |
| Australia     | AU915             |
| Korea         | KR920             |
| India         | IN865             |
| China         | CN470             |

##### RF Characteristics

The following table gives typically sensitivity level of the RAK5146 concentrator module.

| Signal Bandwidth (kHz) | Spreading Factor | Sensitivity (dBm) |
| ---------------------- | ---------------- | ----------------- |
| 125                    | 12               | -139              |
| 125                    | 7                | -125              |
| 250                    | 7                | -123              |
| 500                    | 12               | -134              |
| 500                    | 7                | -120              |

#### Electrical Requirements

Exceeding any limits specified in the Absolute Maximum Ratings section can result in permanent damage to the device. These ratings are intended for stress testing only. Operating the module under these conditions, or outside the parameters defined in the Operating Conditions section, should be avoided. Extended exposure to Absolute Maximum Rating conditions may compromise the device's reliability.

The operating condition range defines the limits within which the functionality of the device is guaranteed. While application information is provided, it is advisory only and does not form part of the specification.

##### Absolute Maximum Rating

The limiting values given below are following the Absolute Maximum Rating System (IEC 134).

| Symbol  | Description           | Condition                                  | Min         | Max        |
| ------- | --------------------- | ------------------------------------------ | ----------- | ---------- |
| 3.3Vaux | Module supply voltage | Input DC voltage at 3.3Vaux pins           | -0.3 V | 3.6 V |
| USB     | USB D+/D- pins        | Input DC voltage at USB interface pins     | -           | 3.6 V |
| RESET   | RAK5146 reset input   | Input DC voltage at RESET input pin        | -0.3 V | 3.6 V |
| SPI     | SPI interface         | Input DC voltage at SPI interface pin      | -0.3 V | 3.6 V |
| GPS_PPS | GPS 1 PPS input       | Input DC voltage at GPS_PPS input pin      | -0.3 V | 3.6 V |
| Rho_ANT | Antenna ruggedness    | Output RF load mismatch ruggedness at ANT1 | -           | 10:1 VSWR  |
| Tstg    | Storage temperature   |                                            | -40° C | 85° C |

:::warning
The product is not protected against overvoltage or reversed voltages. If necessary, voltage spikes exceeding the power supply voltage specification, as outlined in the table above, must be limited to values within the specified boundaries by using appropriate protection devices.
:::

##### Maximum ESD

The table below lists the maximum ESD.

| Parameter | Min | Typical | Max         | Remarks                                    |
| --------- | --- | ------- | ----------- | ------------------------------------------ |
| ESD_HBM   |     |         | 1000 V | Charged Device Model JESD22-C101 CLASS III |
| ESD_CDM   |     |         | 1000 V | Charged Device Model JESD22-C101 CLASS III |

:::tip NOTE
While this module is designed for robustness, it remains susceptible to damage from electrostatic discharge (ESD). Proper ESD protection must be maintained during handling or transportation. Static charges on the human body or equipment can easily reach several kilovolts and discharge undetectably. To prevent damage, always follow industry-standard ESD handling precautions.
:::

##### Power Consumption

| Mode             | Condition                                                         | Min         | Typical      | Max         |
| ---------------- | ----------------------------------------------------------------- | ----------- | ------------ | ----------- |
| Active Mode (TX) | The power of the TX channel is 27 dBm and 3.3 V supply. | 511 mA | 512 mA  | 513 mA |
| Active Mode (RX) | TX disabled and RX enabled.                                       | 70 mA  | 81.6 mA | 101 mA |

##### Power Supply Range

Input voltage at **3.3 Vaux** must be above the normal operating range minimum limit to switch-on the module.

| Symbol        | Parameter                             | Min      | Typical    | Max        |
| ------------- | ------------------------------------- | -------- | ---------- | ---------- |
| 3.3 Vaux | Module supply operating input voltage | 3 V | 3.3 V | 3.6 V |

#### Mechanical Characteristics

The board weighs 16.3 grams, is 30 mm wide, and 50.96 mm tall. The dimensions of the module fall completely within the **PCI Express Mini Card Electromechanical Specification**, except for the card's thickness (5.5 mm at its thickest).

> **Image:** Dimensions

#### Environmental Requirements

##### Operating Conditions

| Parameter                    | Min         | Typical     | Max         | Remarks                                                                            |
| ---------------------------- | ----------- | ----------- | ----------- | ---------------------------------------------------------------------------------- |
| Normal operating temperature | -40° C | +25° C | +85° C | Normal operating temperature range (fully functional and meet 3GPP specifications) |

:::tip NOTE
Unless specified otherwise, all operating condition specifications are based on an ambient temperature of 25° C. Operation outside the specified conditions is not recommended, as extended exposure beyond these limits may impact the device's reliability.
:::

#### Schematic Diagram

The RAK5146 concentrator module is based on Semtech's reference design for the SX1303. The SPI interface is available on the PCIe connector. **Figure 5** illustrates the minimum application schematic for the RAK5146 card. It should be powered with at least 3.3 V / 1 A DC power and have the SPI interface connected to the main processor.

> **Image:** Schematic Diagram

## Models / Bundles

In general, the RAK5146's variation is defined as **RAK5146 - XYZ**, where **X, Y, Z is the model variant**. Refer to the tables below to understand the different variants and their specifications.

| Symbol                  | Description                                                                                                                   |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| X - Supported region    | <ul><li>1 - US915 = 9XX MHz for US915/AU915/KR920/AS923</li><li>2 - EU868 = 8XX MHz for EU868/RU864/IN865</li></ul> |
| Y - Interface type      | <ul><li>1 - SPI</li><li>2 - USB</li></ul>                                                                                     |
| Z - Additional features | <ul><li>0 - No additional features</li><li>2 - LBT</li><li>5 - GPS</li><li>6 - LBT+GPS</li></ul>                              |

| Model       | Frequency                           |  USB  |  SPI  |  LBT  |  GPS  |  PID   |
| ----------- | ----------------------------------- | :---: | :---: | :---: | :---: | :----: |
| RAK5146-126 | 9XX MHz for US915/AU915/KR920/AS923 |   √   |       |   √   |   √   | 516013 |
| RAK5146-122 | 9XX MHz for US915/AU915/KR920/AS923 |   √   |       |   √   |       | 516018 |
| RAK5146-125 | 9XX MHz for US915/AU915/KR920/AS923 |   √   |       |       |   √   | 516011 |
| RAK5146-120 | 9XX MHz for US915/AU915/KR920/AS923 |   √   |       |       |       | 516012 |
| RAK5146-115 | 9XX MHz for US915/AU915/KR920/AS923 |       |   √   |       |   √   | 516010 |
| RAK5146-110 | 9XX MHz for US915/AU915/KR920/AS923 |       |   √   |       |       | 516023 |
| RAK5146-226 | 8XX MHz for EU868/RU864/IN865       |   √   |       |   √   |   √   | 515014 |
| RAK5146-222 | 8XX MHz for EU868/RU864/IN865       |   √   |       |   √   |       | 515018 |
| RAK5146-225 | 8XX MHz for EU868/RU864/IN865       |   √   |       |       |   √   | 515012 |
| RAK5146-220 | 8XX MHz for EU868/RU864/IN865       |   √   |       |       |       | 515013 |
| RAK5146-215 | 8XX MHz for EU868/RU864/IN865       |       |   √   |       |   √   | 515011 |
| RAK5146-210 | 8XX MHz for EU868/RU864/IN865       |       |   √   |       |       | 515022 |

## Certification

### Certifications
- **ANATEL:** https://downloads.rakwireless.com/LoRa/RAK5146/Certification/RAK5146_ANATEL_Certification.pdf
- **CE:** https://downloads.rakwireless.com/LoRa/RAK5146/Certification/RAK5146_CE_Certification.zip
- **FCC:** https://downloads.rakwireless.com/LoRa/RAK5146/Certification/RAK5146_FCC_Certification.zip
- **IMDA:** https://downloads.rakwireless.com/LoRa/RAK5146/Certification/RAK5146_IMDA_Certification.pdf
- **ISED:** https://downloads.rakwireless.com/LoRa/RAK5146/Certification/RAK5146_ISED_Certification.pdf
- **JRL:** https://downloads.rakwireless.com/LoRa/RAK5146/Certification/RAK5146_JRL_Certification.pdf
- **KC:** https://downloads.rakwireless.com/LoRa/RAK5146/Certification/RAK5146_KC_Certification.pdf
- **MIC:** https://downloads.rakwireless.com/LoRa/RAK5146/Certification/RAK5146_MIC_Certification.pdf
- **MOC:** https://downloads.rakwireless.com/LoRa/RAK5146/Certification/RAK5146_MOC_Certification.pdf
- **NCC:** https://downloads.rakwireless.com/LoRa/RAK5146/Certification/RAK5146_NCC_Certification.pdf
- **RCM:** https://downloads.rakwireless.com/LoRa/RAK5146/Certification/RAK5146_RCM_Certification.pdf
- **REACH:** https://downloads.rakwireless.com/LoRa/RAK5146/Certification/RAK5146_REACH_Report.pdf
- **ROHS:** https://downloads.rakwireless.com/LoRa/RAK5146/Certification/RAK5146_RoHS_Report.pdf
- **SIRIM:** https://downloads.rakwireless.com/LoRa/RAK5146/Certification/RAK5146_SIRIM_QAS_Certification.pdf
- **SUTEL:** https://downloads.rakwireless.com/LoRa/RAK5146/Certification/RAK5146_SUTEL_Certification.pdf
- **UKCA:** https://downloads.rakwireless.com/LoRa/RAK5146/Certification/RAK5146_UKCA_Certification.zip
- **WPC:** https://downloads.rakwireless.com/LoRa/RAK5146/Certification/RAK5146_WPC_Certification.pdf

