---
slug: /product-categories/wislink/rak8213/datasheet/
title: RAK8213 WisLink Cellular mPCIe Datasheet
description: Provides comprehensive information about your RAK8213 WisLink Cellular BG96 Arduino Shield to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wislink-lte/rak8213/rak8213.png"
keywords:
  - datasheet
  - wislink
  - RAK8213
sidebar_label: Datasheet
---

# RAK8213 WisLink Cellular mPCIe Datasheet

## Overview

### Description

The **RAK8213 WisLink Cellular mPCIe** is a multi-band LTE Cat M1/Cat NB1/EGPRS module based on the **Quectel BG96** with a standard PCI Express® form factor (**Mini PCIe**). It offers a maximum data rate of 375 Kbps downlink and 375 Kbps uplink.

RAK8213’s built-in GNSS module can support **GPS, GLONASS, BeiDou/Compass, Galileo, QZSS, integrated GNSS** greatly simplifies product design and provides faster, more accurate and more reliable positioning.

Rich Internet protocol, industry-standard interfaces (USB/UART/I2C/Status indicators) and rich features (applicable to Windows XP, Windows Vista, Windows 7/8/8.1/10, Linux drivers for Linux and Android) Modules that extend applicability are suitable for a wide range of M2M applications such as wireless POS, smart metering, and tracking.

### Features

- **LTE Cat. M1/Cat.NB1/EGPRS module** with Mini PCIe form factor, optimized for M2M and IoT applications
- USB Drivers and support 2.0 high speed interface
- Quectel Enhanced AT commands
- Feature refinements: supports **DFOTA, VoLTE**
- Easy migration from **Quectel GSM/GPRS, UMTS/HSPA and LTE modules**
- Robust mounting and interfaces
- PCM interface available for VOLTE

## Specifications

### Overview

The overview shows the top and back view of the RAK8213 board. It also presents the block diagram that discusses how the board works.

#### Module Overview

The board is of standard mPCIe size. The top of the board is populated by the **Cellular and GNSS antenna connectors** (both **IPEX**) and the keys (Power and Reset), together with the **BG96 module** itself. The bottom contains the **Micro Sim Slot** and the **ESIM** pad (optional, not provided).

> **Image:** RAK8213 Board Overview

#### Block Diagram

The RAK8213 card integrates **one BG96 module** which represents the core of the device. This provides the related NB-IoT modem and processing functionalities. Additional signal conditioning circuitry is implemented for PCI Express Mini Card compliance, and two UFL connectors are available for external antennas integration.

> **Image:** RAK8213 Block Diagram

### Hardware

The hardware is categorized into seven (7) parts. It discusses the pinouts and their corresponding functions and diagrams. It also covers the parameters and standard values of the board.

#### Pin Definition

> **Image:** RAK8213 Pin Definition

| **Type** | **Description** |
| -------- | --------------- |
| **IO**   | Bidirectional   |
| **DI**   | Digital input   |
| **DO**   | Digital output  |
| **PI**   | Power input     |
| **PO**   | Power output    |
| **AI**   | Analog input    |
| **AO**   | Analog output   |
| **OC**   | Open collector  |
| **OD**   | Open drain      |
| **NC**   | No Connection   |

| **Pin Number** | **Mini PCIe Pin Rev. 2.0** | **RAK8213 Pin**   | **Type** | **Description**                                                 | **Remarks**                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------- | -------------------------- | ----------------- | -------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1              | WAKE#                      | PI_PWRKEY         | DI       | Turn the module on/off                                          | - 3.3 V power domain.
- When RAK8213 is in power off mode, it can be turned on to normal mode by driving the PI_PWRKEY pin to a high level for at least 500 ms.
- When RAK821 is in normal mode, driving the PI_PWRKEY pin to a high level voltage for at least 650 ms, the module will execute power-down procedure after the PI_PWRKEY is released. 
 - This pin defaults to NC, and the module will be turned on automatically after powered on. |
|                |                            | J6                |          | Turn on/off the Module Manual Key                               | - When RAK8213 is in power off mode, it can be turned on to normal mode by pushing J6 for at least 500 ms.
- When RAK8213 is in normal mode, it can be turned to power off mode by pushing J6 for at least 650 ms, the module will execute power-down procedure after the J6 is released. If unused, just ignore it. 
 - Not used in default.                                                                                                               |
| 2              | 3.3Vaux                    | 3V3               | PI       | 3.3 V<sub>DC</sub> supply                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 3              | COEX1                      | VBUS_CTRL         | DO       | USB detection control                                           | - 3.3 V power domain.
- High level: Enable USB detection
- Low level: Disable USB detection   
 - This pin defaults to NC.                                                                                                                                                                                                                                                                                                                                    |
| 4              | GND                        | GND               | -        | Ground                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 5              | COEX2                      | GNSS_PWR_CTRL     | DO       | Active GNSS antenna power supply control                        | - 3.3 V power domain.
- High level: Enable power supply (3.3 V)
- Low level: Disable power supply 
 - This pin defaults to NC.                                                                                                                                                                                                                                                                                                                           |
| 6              | 1.5V                       | NC                |          | No Connection                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 7              | CLKREQ#                    | PI_AP_READY       | DI       | Application processor sleep state detection                     | - 3.3 V power domain. If unused, keep this pin open.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 8              | UIM_PWR                    | SIM_VDD_PCIE      | PO       | Power supply for (U) SIM card                                   | - Either 1.8 V or 3.0 V is supported by the module automatically.
- No Connection by default. Using (U) SIM card connector on board.                                                                                                                                                                                                                                                                                                                           |
| 9              | GND                        | GND               |          | Ground                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 10             | UIM_DATA                   | SIM_DATA_PCIE     | IO       | Data signal of (U) SIM card                                     | - No Connection by default. Using (U) SIM card connector on board.                                                                                                                                                                                                                                                                                                                                                                                                          |
| 11             | REFCLK-                    | PI_UART_TX        | DI       | UART receive data of RAK8213                                    | - 3.3 V power domain. Connect to BG96’s UART_RX internally.                                                                                                                                                                                                                                                                                                                                                                                                            |
| 12             | UIM_CLK                    | SIM_CLK_PCIE      | DO       | Clock signal of (U) SIM card                                    | - No Connection by default. Using (U) SIM card connector on board.                                                                                                                                                                                                                                                                                                                                                                                                          |
| 13             | REFCLK+                    | PI_UART_RX        | DO       | UART transmit data of RAK8213                                   | - 3.3 V power domain. Connect to BG96’s UART_TX internally.                                                                                                                                                                                                                                                                                                                                                                                                            |
| 14             | UIM_RESET                  | SIM_RST_PCIE      | DO       | Reset signal of (U) SIM card                                    | - No Connection by default. Using (U) SIM card connector on board.                                                                                                                                                                                                                                                                                                                                                                                                          |
| 15             | GND                        | GND               |          | Ground                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 16             | UIM_VPP                    | SIM_PRESENCE_PCIE | DI       | (U) SIM card insertion detection                                | - No Connection by default. Using (U) SIM card connector on board.                                                                                                                                                                                                                                                                                                                                                                                                          |
| 17             | RESERVED                   | PI_RI             | DO       | DO                                                              | - 3.3 V power domain. If unused, keep this pin open.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 18             | GND                        | GND               |          | Ground                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 19             | RESERVED                   | NC                |          | No Connection                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 20             | W_DISABLE#                 | PI_W_DISABLE      | DI       | Airplane mode control                                           | - 3.3 V power domain.
- Pull-up by default.
- In low voltage level, the module can enter into airplane mode.
- If unused, keep this pin open.                                                                                                                                                                                                                                                                                                                 |
| 21             | GND                        | GND               |          | Ground                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 22             | PERST#                     | PI_RESET          | DI       | Reset the module                                                | - 3.3 V power domain. If unused, keep this pin open.                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                |                            | J5                |          | Reset the module Manual Key                                     | - Reset the module manually by pushing down J5. If unused, just ignore it.                                                                                                                                                                                                                                                                                                                                                                                                  |
| 23             | PERn0                      | PI_CTS            | DO       | Clear to send                                                   | - 3.3 V power domain. If unused, keep this pin open.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 24             | 3.3Vaux                    | 3V3               | PI       | 3.3 V<sub>DC</sub> supply                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 25             | PERp0                      | PI_RTS            | DI       | Request to send                                                 | - 3.3 V power domain. If unused, keep this pin open.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 26             | GND                        | GND               |          | Ground                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 27             | GND                        | GND               |          | Ground                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 28             | 1.5V                       | PI_PSM            | DO       | Power saving mode indicator                                     | - 3.3 V power domain. If unused, keep this pin open.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 29             | GND                        | GND               |          | Ground                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 30             | SMB_CLK                    | BG96_I2C_SCL      | OD       | I2C serial clock. Used for external codec.                      | - 1.8 V power domain.
- Pull-up resistor has been set internally.
- No Connection by default.                                                                                                                                                                                                                                                                                                                                                                    |
| 31             | PETn0                      | PI_DTR            | DI       | Data terminal ready (sleep mode control)                        | - 3.3 V power domain. If unused, keep this pin open.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 32             | SMB_DATA                   | BG96_I2C_SDA      | OD       | I2C serial data. Used for external codec.                       | - 1.8 V power domain.
- Pull-up resistor has been set internally.
- No Connection by default.                                                                                                                                                                                                                                                                                                                                                                    |
| 33             | PETp0                      | PI_DCD            | DO       | Data carrier detection                                          | - 3.3 V power domain. If unused, keep this pin open.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 34             | GND                        | GND               |          | Ground                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 35             | GND                        | GND               |          | Ground                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 36             | USB_D-                     | USB-              | IO       | USB differential data (-)                                       | - Require differential impedance of 90 Ω.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 37             | GND                        | GND               |          | Ground                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 38             | USB_D+                     | USB+              | IO       | USB differential data (+)                                       | - USB differential data (+)                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 39             | 3.3Vaux                    | 3V3               | PI       | 3.3 V<sub>DC</sub> supply                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 40             | GND                        | GND               |          | Ground                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 41             | 3.3Vaux                    | 3V3               | PI       | 3.3 V<sub>DC</sub> supply                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 42             | LED_WWAN#                  | NETLIGHT_LED      | DO       | Indicate the module’s network activity status                   | **Logic Level Changes / _Network Status_**

- Flicker slowly (200 ms Low /1800 ms High) / _Network searching_
- Flicker slowly (1800 ms Low /200 ms High) /_Idle_
- Flicker quickly (125 ms Low /125 ms High) / _Data transfer is ongoing_
- Always low / _Voice Calling_
- 3.3 V power domain. If unused, keep this pin open.                                                                                         |
| 43             | GND                        | GND               |          | Ground                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 44             | LED_WLAN#                  | NC                |          | No Connection                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 45             | RESERVED                   | BG96_PCM_CLK      | DO       | PCM clock output                                                | - 1.8 V power domain. No Connection by default.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 46             | LED_WPAN#                  | STATUS_LED        | DO       | Indicate the module’s operation status.                         | - 3.3 V power domain. 
- It will output low level when the module is powered on. 
- If unused, keep this pin open.                                                                                                                                                                                                                                                                                                                                               |
| 47             | RESERVED                   | BG96_PCM_OUT      | DO       | PCM frame synchronization output                                | - 1.8 V power domain. No Connection by default.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 48             | 1.5V                       | VDD_EXT_1V8       | PO       | Provide 1.8 V for external circuit

IOmax=10 mA | - Power supply for external GPIO’s pull-up circuits. No Connection by default.                                                                                                                                                                                                                                                                                                                                                                                              |
| 49             | RESERVED                   | BG96_PCM_IN       | DI       | PCM data input                                                  | - 1.8 V power domain. No Connection by default.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 50             | GND                        | GND               |          | Ground                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 51             | RESERVED                   | BG96_PCM_SYNC     | DO       | PCM data output                                                 | - 1.8 V power domain. No Connection by default.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 52             | 3.3Vaux                    | 3V3               | PI       | 3.3 V<sub>DC</sub> supply                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

#### General Specifications

The following table describes the detailed features of RAK8213 module:

| **Features**               | **Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mini PCIe Interface        | Using the PCI Express Mini Card 1.2 standard interface                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Power Supply               | - **Supply voltage**: 3.3~3.6 V
- **Typical supply voltage**: 3.3 V                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Transmitting Power         | - Class 3 (23 dBm ± 2 dB) for LTE-FDD bands
- Class 3 (23 dBm ± 2 dB) for LTE-TDD bands
- Class 4 (33 dBm ± 2 dB) for GSM850
- Class 4 (33 dBm ± 2 dB) for EGSM900
- Class 1 (30 dBm ± 2 dB) for DCS1800
- Class 1 (30 dBm ± 2 dB) for PCS1900
- Class E2 (27 dBm ± 3 dB) for GSM850 8-PSK
- Class E2 (27 dBm ± 3 dB) for EGSM900 8-PSK
- Class E2 (26 dBm ± 3 dB) for DCS1800 8-PSK
- Class E2 (26 dBm ± 3 dB) for PCS1900 8-PSK |
| LTE Features               | - Support LTE Cat M1 and LTE Cat NB1
- Support 1.4 MHz RF bandwidth for LTE Cat M1
- Support 200 KHz RF bandwidth for LTE Cat NB1
- Support SISO in DL direction
- Cat M1: Max. 375 Kbps (DL)/375 Kbps (UL)
- Cat NB1: Max. 32 Kbps (DL)/70 Kbps (UL)                                                                                                                                                                                                                                                               |
| GSM Features               | **GPRS:**

- Support GPRS multi-slot class 33 (33 by default)
- Coding scheme: CS-1, CS-2, CS-3 and CS-4
- Max. 107 Kbps (DL)/85.6 Kbps (UL)

**EDGE:**

- Support EDGE multi-slot class 33 (33 by default)
- Support GMSK and 8-PSK for different MCS (Modulation and Coding Scheme)
- Downlink coding schemes: CS 1-4 and MCS 1-9
- Uplink coding schemes: CS 1-4 and MCS 1-9
- Max. 296 Kbps (DL)/236.8 Kbps (UL)                                                                                     |
| Internet Protocol Features | - Support **PPP/TCP/UDP/SSL/TLS/FTP(S)/HTTP(S)/NITZ/PING/MQTT** protocols
- Support **Password Authentication Protocol** (PAP) and **Challenge Handshake Authentication Protocol** (CHAP) protocols which are usually used for PPP connections                                                                                                                                                                                                                                                                                                                |
| SMS                        | - Text and PDU mode
- Point to point MO and MT
- SMS cell broadcast
- SMS storage: ME by default                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| (U) SIM Card Interface     | - Support USIM/SIM card: 1.8 V, 3.0 V                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Audio Feature \*\*         | - Support one digital audio interface: PCM interface                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| USB Interface              | - Compliant with USB 2.0 specification (slave only) and the data transfer rate can reach up to 480 Mbps
- Used for AT command communication, data transmission, GNSS NMEA output, software debugging and firmware upgrade
- Support USB serial drivers for **Windows** 7/8/8.1/10, **Linux** 3.x(3.4 or later)/4.1~4.15, **Android** 4.x/5.x/6.x/7.x/8.x/9.x                                                                                                                                                                                          |
| UART Interfaces            | **UART1:**

- Used for data transmission and AT command communication;
- 115200 bps by default;
- The default frame format is 8N1 (8 data bits, no parity, 1 stop bit) ;
- Support RTS and CTS hardware flow control;

**UART2:**

- Used for module debugging and log output;
- 115200 bps baud rate;

**UART3:**

- Used for outputting GNSS data or NMEA sentences;                                                                                                                                      |
| AT Commands                | - 3GPP TS 27.007 and 3GPP TS 27.005 AT commands, as well as Quectel enhanced AT commands                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Network Indication         | - One NETLIGHT pin for network connectivity status indication                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Antenna Interfaces         | - Main antenna (ANT_MAIN) and GNSS antenna (ANT_GNSS) interfaces                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Physical Characteristics   | - **Size**: (51.0±0.15) mm × (30.0±0.15) mm × (4.9±0.2) mm
- **Weight**: approx. 128.6 g                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Temperature Range          | - **Operation temperature range**: -35° C ~ +75° C _(1)_
- **Extended temperature range**: -40° C ~ +85° C _(2)_
- **Storage temperature range**: -40° C ~ +90° C                                                                                                                                                                                                                                                                                                                                                            |
| Firmware Upgrade           | - USB interface, DFOTA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| RoHS                       | - All hardware components are fully compliant with EU RoHS directive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

:::tip NOTE
\*\* means under development.

_(1)_ Within the operation temperature range, the module is 3GPP compliant.

_(2)_ Within an extended temperature range, the module remains the ability to establish and maintain a voice, SMS, data transmission, emergency call, etc. There is no unrecoverable malfunction. There are also no effects on radio spectrum and no harm to the radio network. Only one or more parameters like Pout might reduce in their value and exceed the specified tolerances. When the temperature returns to the normal operating temperature levels, the module will meet 3GPP specifications again.
:::

#### GNSS Receiver

RAK8213 includes a fully integrated **Global Navigation Satellite System (GNSS)** solution that supports Gen8C-Lite of Qualcomm (GPS, GLONASS, BeiDou/Compass, Galileo andQZSS).

The module supports standard NMEA-0183 protocol, and outputs NMEA sentences at 1 Hz data update rate via USB interface by default. By default, RAK8213 GNSS engine is switched off. It has to be switched on via AT command.

##### GNSS Performance

The following table shows the GNSS performance of RAK8213:

| **Parameter**             | **Description**       | **Conditions**                  | **Typical**     | **Unit**   |
| ------------------------- | --------------------- | ------------------------------- | --------------- | ---------- |
| Sensitivity

(GNSS) | Cold start            | - Autonomous                    | -146            | dBm        |
|                           | Reacquisition         | - Autonomous                    | -157            | dBm        |
|                           | Tracking              | - Autonomous                    | -157            | dBm        |
| TTFF

(GNSS)        | Cold start @ open sky | - Autonomous 
- XTRA enabled | 31

11.54 | s

s |
|                           | Warm start @ open sky | - Autonomous 
- XTRA enabled | 21

2.52  | s

s |
|                           | Hot start @ open sky  | - Autonomous
- XTRA enabled  | 27

1.82  | s

s |
| Accuracy 

(GNSS)   | CEP-50                | - Autonomous @ open sky         | < 2.5            | m          |

:::tip NOTE
1. **Tracking sensitivity**: the lowest GNSS signal value at the antenna port on which the module can keep on positioning for 3 minutes.

2. **Reacquisition sensitivity**: the lowest GNSS signal value at the antenna port on which the module can fix position again within 3 minutes after loss of lock.

3. **Cold start sensitivity**: the lowest GNSS signal value at the antenna port on which the module fixes position within 3 minutes after executing cold start command.
:::

#### RF Characteristics

##### Operating Frequencies

The RAK8213 is an **LTE Cat M1/Cat NB1/EGPRS** module offering maximum data rates of 375 kbps downlink and uplink. It features global frequency bands, ultra-low power consumption.

| **3GPP Band**       | **Transmit** | **Receive** | **Unit** |
| ------------------- | ------------ | ----------- | -------- |
| LTE-FDD B1          | 1920~1980    | 2110~2170   | MHz      |
| LTE-FDD B2, PCS1900 | 1850~1910    | 1930~1990   | MHz      |
| LTE-FDD B3, DCS1800 | 1710~1785    | 1805~1880   | MHz      |
| LTE-FDD B4          | 1710~1755    | 2110~2155   | MHz      |
| LTE-FDD B5, GSM850  | 824~849      | 869~894     | MHz      |
| LTE-FDD B8, EGSM900 | 880~915      | 925~960     | MHz      |
| LTE-FDD B12         | 699~716      | 729~746     | MHz      |
| LTE-FDD B13         | 777~787      | 746~756     | MHz      |
| LTE-FDD B18         | 815~830      | 860~875     | MHz      |
| LTE-FDD B19         | 830~845      | 875~890     | MHz      |
| LTE-FDD B20         | 832~862      | 791~821     | MHz      |
| LTE-FDD B25 _(1)_   | 1850~1915    | 1930~1995   | MHz      |
| LTE-FDD B26 _(2)_   | 814~849      | 859~894     | MHz      |
| LTE-FDD B28         | 703~748      | 758~803     | MHz      |
| LTE-FDD B39         | 1880~1920    | 1880~1920   | MHz      |

:::tip NOTE
_(1)_ LTE-FDD B25 is supported on BG96 of R1.2 hardware version.

_(2)_ means under development.
:::

#### Electrical Characteristics

##### Operation and Storage Temperatures

The operation and storage temperatures of the module are listed in the following table:

| **Parameter**                     | **Minimum** | **Typical** | **Maximum** | **Unit** |
| --------------------------------- | ----------- | ----------- | ----------- | -------- |
| Operation Temperature Range _(1)_ | -35         | +25         | +75         | ºC       |
| Extended Temperature Range _(2)_  | -40         |             | +85         | ºC       |
| Storage Temperature Range         | 40          |             | +90         | ºC       |

:::tip NOTE
\_(1)\_Within operation temperature range, the module is 3GPP compliant.

_(2)_ Within extended temperature range, the module remains the ability to establish and maintain a voice, SMS, data transmission, emergency call, etc. There is no unrecoverable malfunction. There are also no effects on radio spectrum and no harm to radio network. Only one or more parameters like Pout might reduce in their value and exceed the specified tolerances. When the temperature returns to the normal operating temperature levels, the module will meet 3GPP specifications again.
:::

##### Current Consumption

The following table shows current consumption of RAK8213:

:::tip NOTE
**LTE-FDD B25** is supported on BG96 of R1.2 hardware version.
:::

| **Parameter** | **Description**                          | **Condition**                     | **Typical**_(1)_ | **Unit** |
| ------------- | ---------------------------------------- | --------------------------------- | ---------------- | -------- |
| **IVBAT**     | **Leakage Current**                      | Power off mode                    | 8                | uA       |
|               | **PSM**                                  | Power Saving Mode @ Real Network  | 10               | uA       |
|               | **Rock Bottom Sleep** _(2)_              | AT+CFUN=0 @ Sleep State           | 0.8              | mA       |
|               | **Sleep State** _(3)_                    | DRX=1.28 s @ Instrument      | 1.5              | mA       |
|               |                                          | DRX=1.28 s @ Instrument      | 1.96             | mA       |
|               |                                          | e-I-DRX=20.48 s @ Instrument | 1.2              | mA       |
|               |                                          | e-I-DRX=20.48 s @ Instrument | 1.1              | mA       |
|               |                                          | @ Real 2G Network                 | 2.0              | mA       |
|               | **Idle State**                           | DRX=1.28 s @ Instrument      | 15               | mA       |
|               |                                          | DRX=1.28 s @ Instrument      | 15               | mA       |
|               |                                          | e-I-DRX=20.48 s @ Instrument | 15               | mA       |
|               |                                          | e-I-DRX=20.48 s @ Instrument | 15               | mA       |
|               |                                          | @ Real 2G Network                 | 15               | mA       |
|               | **LTE Cat M1 Data Transfer (GNSS OFF)**  | LTE-FDD B1 @ 23.31 dBm       | 220              | mA       |
|               |                                          | LTE-FDD B2 @ 23.05 dBm       | 208              | mA       |
|               |                                          | LTE-FDD B3 @ 23.09 dBm       | 214              | mA       |
|               |                                          | LTE-FDD B4 @ 23.19 dBm       | 214              | mA       |
|               |                                          | LTE-FDD B5 @ 23.22 dBm       | 210              | mA       |
|               |                                          | LTE-FDD B8 @ 21.83 dBm       | 203              | mA       |
|               |                                          | LTE-FDD B12 @ 21.88 dBm      | 215              | mA       |
|               |                                          | LTE-FDD B13 @ 21.96 dBm      | 197              | mA       |
|               |                                          | LTE-FDD B18 @ 23.04 dBm      | 212              | mA       |
|               |                                          | LTE-FDD B19 @ 23.13 dBm      | 211              | mA       |
|               |                                          | LTE-FDD B20 @ 23.07 dBm      | 209              | mA       |
|               |                                          | LTE-FDD B25 @ 23.01 dBm      | 211              | mA       |
|               |                                          | LTE-FDD B26 @ TBD                 | TBD              | mA       |
|               |                                          | LTE-FDD B28 @ 22.52 dBm      | 215              | mA       |
|               |                                          | LTE-TDD B39 @ TBD                 | TBD              | mA       |
|               | **LTE Cat NB1 Data Transfer (GNSS OFF)** | LTE-FDD B1 @ 22.8 dBm        | 170              | mA       |
|               |                                          | LTE-FDD B2 @ 22.6 dBm        | 171              | mA       |
|               |                                          | LTE-FDD B3 @ 22.6 dBm        | 161              | mA       |
|               |                                          | LTE-FDD B4 @ 22.6 dBm        | 161              | mA       |
|               |                                          | LTE-FDD B5 @ 22.9 dBm        | 156              | mA       |
|               |                                          | LTE-FDD B8 @ 22.7 dBm        | 170              | mA       |
|               |                                          | LTE-FDD B12 @ 23 dBm         | 170              | mA       |
|               |                                          | LTE-FDD B13 @ 22.9 dBm       | 167              | mA       |
|               |                                          | LTE-FDD B18 @ 23.1 dBm       | 159              | mA       |
|               |                                          | LTE-FDD B19 @ 22.9 dBm       | 155              | mA       |
|               |                                          | LTE-FDD B20 @ 22.7 dBm       | 157              | mA       |
|               |                                          | LTE-FDD B25 @ 23 dBm         | 165              | mA       |
|               |                                          | LTE-FDD B26 @ TBD                 | TBD              | mA       |
|               |                                          | LTE-FDD B28 @ 22.5 dBm       | 163              | mA       |
|               | **GPRS Data Transfer (GNSS OFF)**        | GSM850 4UL 1DL @ 30.17 dBm   | 575              | mA       |
|               |                                          | GSM850 3UL 2DL @ 32 dBm      | 533              | mA       |
|               |                                          | GSM850 2UL 3DL @ 32.74 dBm   | 402              | mA       |
|               |                                          | GSM850 1UL 4DL @ 32.52 dBm   | 220              | mA       |
|               |                                          | EGSM900 4UL 1DL @ 30.54 dBm  | 586              | mA       |
|               |                                          | EGSM900 3UL2DL @ 31.36 dBm   | 556              | mA       |
|               |                                          | EGSM900 2UL 3DL @ 32.62 dBm  | 399              | mA       |
|               |                                          | EGSM900 1UL 4DL @ 32.75 dBm  | 228              | mA       |
|               |                                          | DCS1800 4UL 1DL @ 29.81 dBm  | 543              | mA       |
|               |                                          | DCS1800 3UL 2DL @ 30.09 dBm  | 426              | mA       |
|               |                                          | DCS1800 2UL 3DL @ 30.1 dBm   | 301              | mA       |
|               |                                          | DCS1800 1UL4DL @ 30.34 dBm   | 182              | mA       |
|               |                                          | PCS1900 4UL 1DL @ 29.64 dBm  | 516              | mA       |
|               |                                          | PCS1900 3UL 2DL @ 29.86 dBm  | 404              | mA       |
|               |                                          | PCS1900 2UL 3DL @ 29.7 dBm   | 281              | mA       |
|               |                                          | PCS1900 1UL 4DL @ 29.94 dBm  | 171              | mA       |
|               | **EDGE Data Transfer (GNSS OFF)**        | GSM850 4UL1DL @ 26.02 dBm    | 403              | mA       |
|               |                                          | GSM850 3UL 2DL @ 26.11 dBm   | 312              | mA       |
|               |                                          | GSM850 2UL 3DL @ 26.57 dBm   | 224              | mA       |
|               |                                          | GSM850 1UL 4DL @ 26.92 dBm   | 224              | mA       |
|               |                                          | EGSM900 4UL 1DL @ 25.92 dBm  | 136              | mA       |
|               |                                          | EGSM900 3UL 2DL @ 26.11 dBm  | 391              | mA       |
|               |                                          | EGSM900 2UL 3DL @ 26.16 dBm  | 301              | mA       |
|               |                                          | EGSM900 1UL 4DL @ 26.88 dBm  | 217              | mA       |
|               |                                          | DCS1800 4UL 1DL @ 24.7 dBm   | 133              | mA       |
|               |                                          | DCS1800 3UL 2DL @ 25.97 dBm  | 373              | mA       |
|               |                                          | DCS1800 2UL 3DL @ 25.03 dBm  | 286              | mA       |
|               |                                          | DCS1800 1UL 4DL @ 25.03 dBm  | 208              | mA       |
|               |                                          | PCS1900 4UL1DL @ 24.92 dBm   | 127              | mA       |
|               |                                          | PCS1900 3UL 2DL @ 24.86 dBm  | 375              | mA       |
|               |                                          | PCS1900 2UL 3DL @ 25.17 dBm  | 288              | mA       |
|               |                                          | PCS1900 1UL 4DL @ 25.31 dBm  | 207              | mA       |
|               | _\_LTE Voice (GNSS OFF) _\_              | Voice @ LTE Cat M1 network        | 108              | mA       |

:::tip NOTE
_(1)_**Typical value** means the average current consumption value.

_(2)_**Rock Bottom Sleep** means the operation is performed with **AT+CFUN=0** and **AT+QSLCK=1** (DTR pin at high level).

_(3)_**Sleep state** with UART connected and USB disconnected. The module can enter sleep mode through executing **AT+QSCLK=1** command via UART interface and then controlling the module’s DTR pin.
:::

The following table shows GNSS Current Consumption:

| **Description**       | **Conditions**               | **Typical** | **Unit** |
| --------------------- | ---------------------------- | ----------- | -------- |
| Searching (AT+CFUN=0) | Cold Start @ Passive Antenna | 41.7        | mA       |
|                       | Lost State @ Passive Antenna | 42          | mA       |
| Tracking (AT+CFUN=0)  | Instrument Environment       | 21.7        | mA       |
|                       | Open Sky @ Passive Antenna   | 36          | mA       |
|                       | Open Sky @ Active Antenna    | 35          | mA       |

##### RF Output Power

The following table shows the RF output power of RAK8213:

| **Frequency**                                              | **Max**                 | **Min**          |
| ---------------------------------------------------------- | ----------------------- | ---------------- |
| LTE-FDD B1/B2/B3/B4/B5/B8/B12/B13/B18/B19/B20/B25/ B26/B28 | 23 dBm ± 2 dB | -                |
| LTE-TDD B39                                                | 23 dBm ± 2 dB | -                |
| GSM850/EGSM900                                             | 33 dBm ± 2 dB | 5 dBm ± 5dB |
| DCS1800/PCS1900                                            | 30 dBm ± 2 dB | 0 dBm ± 5dB |
| GSM850/EGSM900 (8-PSK)                                     | 27 dBm ± 3 dB | 5 dBm ± 5dB |
| DCS1800/PCS1900 (8-PSK)                                    | 26 dBm ± 3 dB | 0 dBm ± 5dB |

##### RF Receiving Sensitivity

:::tip NOTE
**Cat M1/ 3GPP, Cat NB1 /3GPP** and **GSM/3GPP** are the RF Receiving Sensitivity of RAK8213 in dBm.
:::

| **Network** | **Band**          | **Primary** | **Diversity**        | **Cat M1/ 3GPP** | **Cat NB1**_(1)_**/3GPP** | **GSM/3GPP** |
| ----------- | ----------------- | ----------- | -------------------- | ---------------- | ------------------------- | ------------ |
| **LTE**     | LTE-FDD B1        | Supported   | Not Supported        | -107.0/-102.7    | -112.5/-107.5             |              |
|             | LTE-FDD B2        |             |                      | -106.7/-100.3    | -112.5/-107.5             |              |
|             | LTE-FDD B3        |             |                      | -106.8/-99.3     | -113/-107.5               |              |
|             | LTE-FDD B4        |             |                      | -106.9/-102.3    | -112.5/-107.5             |              |
|             | LTE-FDD B5        |             |                      | -107.0/-100.8    | -114/-107.5               |              |
|             | LTE-FDD B8        |             |                      | -107.3/-99.8     | -113/-107.5               |              |
|             | LTE-FDD B12       |             |                      | -107.7/-99.3     | -113.5/-107.5             |              |
|             | LTE-FDD B13       |             |                      | -106.5/-99.3     | -112/-107.5               |              |
|             | LTE-FDD B18       |             |                      | -107.5/-102.3    | -113.5/-107.5             |              |
|             | LTE-FDD B19       |             |                      | -107.1/-102.3    | -114/-107.5               |              |
|             | LTE-FDD B20       |             |                      | -107.2/-99.8     | -114/-107.5               |              |
|             | LTE-FDD B25 _(2)_ |             |                      | -106/-100.3      | -112/-107.5               |              |
|             | LTE-FDD B26       |             |                      | TBD/-100.3       | TBD/-107.5                |              |
|             | LTE-FDD B28       |             |                      | -107.2/-100.8    | -113/-107.5               |              |
|             | LTE-FDD B39       |             |                      | TBD /-103        | Not Supported             |              |
| **GSM**     | GSM850/EGSM900    | Supported   | Not

Supported |                  |                           | -109/-102    |
|             | DCS1800/PCS1900   |             |                      |                  |                           | -108.5/-102  |

:::tip NOTE
\_(1)\_LTE Cat NB1 receiving sensitivity without repetitions.

\_(2)\_LTE-FDD B25 is supported on BG96 of R1.2 hardware version.
:::

##### Electrostatic Discharge

The module is not protected against **electrostatics discharge (ESD)** in general. Consequently, it is subject to ESD handling precautions that typically apply to ESD sensitive components. Proper ESD handling and packaging procedures must be applied throughout the processing, handling and operation of any application that incorporates the module.

The following table shows the electrostatic discharge characteristics of RAK8213:

| **Tested Interfaces**                | **Contact Discharge** | **Air Discharge** | **Unit** |
| ------------------------------------ | --------------------- | ----------------- | -------- |
| 3.3Vaux, GND                         | ±10                   | ±15               | kV       |
| Main/GNSS Antenna 

Interfaces | ±10                   | ±15               | kV       |

#### Mechanical Characteristics

The board only weighs 128.6 grams, its length is 51 mm while its width is 30 mm. The dimensions of the module fall completely within the **PCI Express Mini Card Electromechanical Specification**, except for the card's thickness (nominal value of 4.9 mm).

> **Image:** RAK8213 Board Overview

#### Schematic Diagram

**Figure 5** shows RAK8213’s PCIe interface schematic.

> **Image:** RAK8213 Schematic Diagram

### Firmware

Download the latest firmware version of RAK8212 in the table provided below.

| Model   | Version | Source                                                                                              |
| ------- | ------- | --------------------------------------------------------------------------------------------------- |
| RAK8213 | V1.0.1  | [Download](https://downloads.rakwireless.com/Cellular/RAK8213/Firmware/RAK8213_Latest_Firmware.zip) |

## Models / Bundles

### Ordering Information

| **Model** | **Description**                                                 | **Supported Regions** |
| --------- | --------------------------------------------------------------- | --------------------- |
| RAK8213   | Multi-band LTE Cat M1/Cat NB1/EGPRS module of Mini-PCIe edition | Global                |

