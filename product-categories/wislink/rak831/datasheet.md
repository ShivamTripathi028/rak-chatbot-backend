---
slug: /product-categories/wislink/rak831/datasheet/
title: RAK831 WisLink LPWAN Concentrator Datasheet
description: Provides technical information about the RAK831 WisLink LPWAN Concentrator for its usage. This information includes specifications, characteristics, requirements and the device components.
image: "https://images.docs.rakwireless.com/wislink-lora/rak831/rak831.png"
keywords:
  - datasheet
  - wislink
  - RAK831
sidebar_label: Datasheet
---

# RAK831 WisLink LPWAN Concentrator Datasheet

## Overview

### Description

The **RAK831 WisLink LPWAN Concentrator** is designed for a wide variety of applications like **Smart Metering**, **IoT** (Internet of Things) and **M2M** (Machine-to-machine) applications. It is a multi-channel high performance Transceiver module designed to receive several LoRa packets simultaneously using different spreading factors on multiple channels. The concentrator module RAK831 can be integrated into a gateway as a complete RF front-end of this gateway. It provides the possibility to enable robust communication between a gateway and a huge amount of LoRa end-nodes spread over a wide range of distance. The RAK831 needs a host system for proper operation.

This is an ideal modular product to help you realize the whole LoRa system development. With the USB-SPI converter module FT2232, you can quickly make the software development in your PC. Also, you can integrate the concentrator module to your production product to realize the gateway function. This is a very economic way to address a huge variety of applications like Smart Grid, Intelligent Farm, intelligent Farm and Other IoT applications.

The RAK831 needs a host system like Raspberry Pi or WisAP (OpenWRT based) or WisCam for proper operation. The host processor can be a PC or MCU that will be connected to RAK831 via USB or SPI.

RAK831 is able to receive up to 8 LoRa packets simultaneously sent with different spreading factors on different channels. This unique capability allows the implementation of innovative network architectures advantageous over other short range systems:

End-point nodes (e.g. sensor nodes) can change the frequency with each transmission in a random pattern. This provides a vast improvement of the system robustness in terms of interference immunity and radio channel diversity.

Applications possible with the RAK831 include Smart Metering, Wireless Star Networks, Home, Building, Industrial automation, Remote Control, Wireless Sensors Network, M2M, IoT and Wireless Alarm and Security Systems.

### Features

- **Compact size** 80 mm x 50 mm x 5 mm
- LoRaWAN modulation technology
- **Frequency bands**: 433 MHz, 470 MHz, 868 MHz, 915 MHz
- Orthogonal spreading factors
- **Minimum Sensitivity**: -142.5 dBm
- **Maximum Link Allotment**: 162 dB
- SPI interface
- SX1301 base band processor
- Emulates up to forty-nine (49) LoRa demodulators
- Twelve (12) parallel demodulation paths
- One (1) (G) FSK demodulator
- Two (2) SX1257 Tx/Rx front-ends High frequency
- Two (2) x SX1255 Tx/Rx front-ends low frequency
- **Supply voltage**: 5 V<sub>DC</sub>
- Optimized RF Interface 50
- Up to 23 dBm output power
- Optional GPS receiver
- **Line of Sight Range**: up to 15 kilometers

## Specifications

### Overview

The overview shows the top view of the RAK831 board and its outer dimension. It also presents the block diagram that discusses how the board works.

#### Board Overview

##### Module Overview

The Concentrator Module currently available is in SPI version with its board shown in **Figure 1**.

> **Image:** RAK831 WisLink LPWAN Concentrator Board Overview

##### Module Dimensions

The outer dimensions of the RAK831 are given by **80 mm x 50 mm** with ± 0.2 mm tolerance. The RAK831 provides four drills for screwing the PCB to another unit each with a drill diameter of 3 mm.

> **Image:** RAK831 WisLink LPWAN Concentrator Board Dimension

#### Block Diagram

##### SX1301

The RAK831 includes Semtech’s SX1301 which is a digital baseband chip that includes a massive digital signal processing engine specifically designed to offer breakthrough gateway capabilities in the ISM bands worldwide. SX1301 integrates the LoRa concentrator IP.

> **Image:** SX1301 Chip Block Diagram

The SX1301 is a smart baseband processor for long range ISM communication. In the receiver part, it receives I and Q digitized bit stream for one or two receivers (SX1257), demodulates these signals using several demodulators, adapting the demodulators settings to the received signal and stores the received demodulated packets in a FIFO to be retrieved from a host system (PC, MCU). In the transmitter part, the packets are modulated using a programmable (G)FSK/LoRa modulator and sent to one transmitter (SX1257). Received packets can be time-stamped using a GPS PPS input.

The SX1301 has an internal control block that receives microcode from the host system (e.g. PC, MCU). The microcode is provided by Semtech as a binary file to load into the SX1301 at power-on (see Semtech application support for more information).

The control of the SX1301 by the host system (PC, MCU) is made using a Hardware Abstraction Layer (HAL). The Hardware Abstraction Layer source code is provided by Semtech and can be adapted by the host system developers.

It is highly recommended to fully re-use the latest HAL as provided by Semtech on [https://github.com/Lora-net](https://github.com/Lora-net).

###### Block Diagram

> **Image:** RAK831 WisLink LPWAN Concentrator Block Diagram

The SX1301 digital baseband chip contains ten (10) programmable reception paths. These paths have differentiated levels of programmability and allow different use cases. It is important to understand the differences between these demodulation paths to make the best possible use of the system.

###### IF8 LoRa channel

This channel is connected to one SX1257 using any arbitrary intermediate frequency within the allowed range. This channel is LoRa only. The demodulation bandwidth can be configured to be 125, 250 or 500 kHz. The data rate can be configured to any of the LoRa available data rates (SF7 to SF12) but, as opposed to IF0 to IF7, only the configured data rate will be demodulated. This channel is intended to serve as a high speed backhaul link to other gateways or infrastructure equipment. This demodulation path is compatible with the signal transmitted by the SX1272 and SX1276 chip families.

###### IF9 (G) FSK channel

The IF9 channel is connected to a GFSK demodulator. The channel bandwidth and bit rate can be adjusted. This demodulator offers a very high level of configurability, going well beyond the scope of this document. The demodulator characteristics are essentially the same as the GFSK demodulator implemented on the SX1232 and SX1272 Semtech chips. This demodulation path can demodulate any legacy FSK or GFSK formatted signal.

###### IF0 to IF7 LoRa channels

Those channels are connected to one SX1257. The channel bandwidth is 125 kHz and cannot be modified or configured. Each channel IF frequency can be individually configured. On each of those channels, any data rate can be received without prior configuration.

Several packets using different data rates (different spreading factors) may be demodulated simultaneously even on the same channel. Those channels are intended to be used for a massive asynchronous star network of 10000’s of sensor nodes. Each sensor may use a random channel (amongst IF0 to IF7) and a different data rate for any transmission.

Sensors located near the gateway will typically use the highest possible data rate in the fixed 125 kHz channel bandwidth (e.g. 6 kbit/s) while sensors located far away will use a lower data rate down to 300 bit/s (minimum LoRa data rate in a 125 kHz channel).

The SX1301 digital baseband chip scans the 8 channels (IF0 to IF7) for preambles of all data rates at all times.

The chip is able to demodulate simultaneously up to 8 packets. Any combination of spreading factor and intermediate frequency for up to 8 packets is possible (e.g. one SF7 packet on IF0, one SF12 packet on IF7 and one SF9 packet on IF1 simultaneously).

The SX1301 can detect simultaneously preambles corresponding to all data rates on all IF0 to IF7 channels. However, it cannot demodulate more than 8 packets simultaneously. This is because the SX1301 architecture separates the preamble detection and signal acquisition task from the demodulation process. The number of simultaneously demodulated packets (in this case 8) is an arbitrary system parameter and may be set to other values for a customer specific circuit.

The unique multi data-rate multi-channel demodulation capacity SF7 to SF12 and of channels IF0 to IF7 allows innovative network architectures to be implemented.

> **Image:** IF0 to IF7 LoRa Channels

### Hardware

The hardware is categorized into five (5) parts. It discusses the interfacing, pinouts and its corresponding functions and diagrams. It also covers the parameters and standard values of the board.

#### Interfaces

##### External Module Connector

###### SPI

The connector on the bottom side provides an SPI connection, which allows direct access to the SX1301 SPI interface. This gives the target system the possibility to use existing SPI interfaces to communicate.

After powering up RAK831, it is required to **reset** SX1301 via **Pin 19**. If the HAL driver from Github is used this functionality is already implemented.

###### GPS PPS

In case of available PPS signals in the target system, it is possible to connect this available signal to the appropriate pin at the connector.

###### Digital IOs

There are five GPIOs of the SX1301 available, which gives the user some possibilities to get information about the system status. These pins are the same, as they are used for the LEDs on the RAK831.

As default setting the LEDs

1. Backhaul packet
2. TX packet
3. RX Sensor packet
4. RX FSK packet
5. RX buffer not empty
6. Power

#### Pin Definition

The RAK831 provides headers at the bottom side, which have a pitch of **2.54 mm**. The description of the pins is given in the table below.

> **Image:** RAK831 WisLink LPWAN Concentrator Module Pinout Diagram

| Pin |    Name    | Type  |         Description         |
|:---:|:----------:|:-----:|:---------------------------:|
|  1  |    +5V     | POWER |  +5 V Supply Voltage   |
|  2  |    +5V     | POWER |  +5 V Supply Voltage   |
|  3  |    GND     |  GND  |           Ground            |
|  4  |  LNA_EN_A  | Input | SX1301 Radio C Sample Valid |
|  5  |    GND     |  GND  | GPS Module LDO: Enable Pin  |
|  6  |    GND     |  GND  |           Ground            |
|  7  | RADIO_EN_A | Input |         SX1257_A_EN         |
|  8  |   PA_G8    | Input |          PA GAIN 0          |
|  9  | RADIO_EN_B | Input |         SX1257_B_EN         |
| 10  |   PA_G16   | Input |          PA GAIN 1          |
| 11  |  PA_EN_A   | Input |            PA EN            |
| 12  |    GND     |  GND  |           Ground            |
| 13  | RADIO_RST  |  RST  |      SX1257_A_B RESET       |
| 14  |    GND     |  GND  |           Ground            |
| 15  |    CSN     |  SPI  |       SX1301 SPI_NSS        |
| 16  |    MOSI    |  SPI  |       SX1301 SPI_MOSI       |
| 17  |    MISO    |  SPI  |       SX1301 SPI_MISO       |
| 18  |    SCK     |  SPI  |       SX1301 SPI_CLK        |
| 19  |   RESET    |  RST  |        SX1301 RESET         |
| 20  |   GPIO0    | GPIO  |         SX1301 GPIO         |
| 21  |   GPIO1    | GPIO  |         SX1301 GPIO         |
| 22  |   GPIO2    | GPIO  |         SX1301 GPIO         |
| 23  |   GPIO3    | GPIO  |         SX1301 GPIO         |
| 24  |   GPIO4    | GPIO  |         SX1301 GPIO         |

#### RF Characteristics

##### Transmitter RF Characteristics

The RAK831 has excellent transmitter performance. It is highly recommended to use the optimized configuration for the power level configuration, which is part of the HAL. This results in a mean RF output power level and current consumption.

| PA Control | DAC Control | MIX Control | DIG Gain | Nominal RF Power Level \[dBm\] |
|:----------:|:-----------:|:-----------:|:--------:|:------------------------------:|
|     0      |      3      |      8      |    0     |               -5               |
|     0      |      3      |      9      |    0     |               -3               |
|     0      |      3      |     11      |    0     |               0                |
|     0      |      3      |     15      |    0     |               3                |
|     1      |      3      |      9      |    0     |               6                |
|     1      |      3      |     11      |    0     |               10               |
|     1      |      3      |     12      |    0     |               11               |
|     2      |      3      |      8      |    0     |               12               |
|     2      |      3      |      9      |    0     |               13               |
|     1      |      3      |     15      |    0     |               14               |
|     2      |      3      |     10      |    0     |               15               |
|     2      |      3      |     11      |    0     |               16               |
|     2      |      3      |     11      |    0     |               17               |
|     2      |      3      |     12      |    0     |               18               |
|     2      |      3      |     13      |    0     |               19               |
|     2      |      3      |     14      |    0     |               20               |

At **T=25° C, VDD=5 V (Typ.)** if nothing else is stated:

:::tip NOTE
The table below is for 868 MHz RAK831 WisLink LPWAN Concentrator. Other frequencies are also supported such as 433 MHz, 470 MHz, and 915 MHz Frequency Range.
:::

| Parameter                              | Condition              | Min  | Typ. | Max  | Unit |
|----------------------------------------|------------------------|------|------|------|------|
| Frequency Range                        | -                      | 863  | -    | 870  | MHz  |
| Modulation Techniques                  | FSK/LoRaWAN            | -    | -    | -    | -    |
| TX Frequency Variation vs. Temperature | Power Level Setting:20 | -3   | -    | +3   | kHz  |
| TX Power Variation vs. Temperature     | Power Level Setting:20 | -5   | -    | +5   | dB   |
| TX Power Variation                     | -                      | -1.5 | -    | +1.5 | dB   |

##### Receiver RF Characteristics

It is highly recommended to use optimized RSSI calibration values, which is part of the HALv3.1. For both, Radio 1 and 2, **the RSSI-Offset should be set -169.0**.

The following table gives typically sensitivity level of the RAK831 :

| Signal Bandwidth [KHz] | Spreading Factor | Sensitivity [dBm] |
|:----------------------:|:----------------:|:-----------------:|
|          125           |        12        |       -137        |
|          125           |        7         |       -126        |
|          250           |        12        |       -136        |
|          250           |        7         |       -123        |
|          500           |        12        |       -134        |
|          500           |        7         |       -120        |

##### RF Key Components

This section introduces the key components in RAK831 and helps the developer to utilize the system to realize a system level design.

**1. LDO**

The system power supply is provided by the external 5 V<sub>DC</sub> power supply. SX1301 and related clock crystal is powered by Dual output LDO transformer outputs 1.8 V and 3.3 V in order to meet the normal working condition of SX1301. Other key components are powered by LDO transformer output 3.3 V. To be aware of the system design of LDO's power supply enable is provided by the output GPIO of SX1301 as default. The connection method of pin enable should be kept the same as Semtech official code. At the same time, system design also needs to keep flexibility and all LDO enable should be connected to pin DB24. For this case, the user can run the official reference code in this board, and also can change all external enable clock as they need to achieve the flexibility debugging.

**2. Power amplifier**

The Power amplifier chooses RFMD LF Power Amplifier and built in two steps gain. It realize the Max. 0.5 W output power. The frequency range can cover from 380~960 MHz. The two steps gain control table as:

| Parameter | Specification | Unit | Condition |  |  |
| --- | --- | --- | --- | --- | --- |
| Overall |  |  |  |  | T=25° C, V CC =3.6 V, V PD =V BAS =3.0 V, P IN =0 dBm, Freq=9125 MHz |
| CW Output Power |  | 27.5 |  | dBm | VCC=3.6 V |
| CW Output Power |  | 30 |  | dBm | VCC=5 V |
| Small Signal Gain |  | 32 |  | dB | PIN=-10 dBm |
| Second Harmonic |  | 23 |  | dBc | Without external second harmonic trap |
| Third Harmonic |  | 45 |  | dBc | - |
| CW Efficiency | 55 | 63 |  | % | G16="high", G8="high", PIN=0 dBm |
| Power Down "ON" |  | 3.0 |  | V | Voltage supplied to the input |
| Power Down "OFF" | 0 | 0.5 | 0.8 | V | Voltage supplied to the input |
| VPD Input Current |  | 6 |  | mA | Only in "ON" state |
| G16, G8 "ON" | 1.7 |  | 3.0 | V | Voltage supplied to the input |
| G16, G8 "OFF" | 0 |  | 0.7 | V | Voltage supplied to the input |
| G16, G8 Input Current |  | 1.0 |  | mA | Only in "ON" state |
| Output Power | 26.5 | 27.5 | 29 | dBm | G16="high", G8="high", PIN=0 dBm |
| Output Power | 21 | 23 | 25 | dBm | G16="high", G8="low", PIN=0 dBm |
| Output Power | 14 | 16 | 18 | dBm | G16="low", G8="high", PIN=0 dBm |
| Output Power | 3 | 5 | 8 | dBm | G16="low", G8="low", PIN=0 dBm |
| Turn On/Off Time |  | 200 |  | ns | - |

**3. RF switch**

The RF switch chooses RFSW1 01 2 which has advantage of high Isolation and low insertion loss. This chip handles the switch between Tx and Rx. The control logic is shown in **Figure 7**. Especially need highlight that the pin of CTRL was controlled by SX1301 ’s GPIO through the output signal of LNA_EN_A, the Pin of EN was controlled by SX1301’s GPIO through the output signal of RADIO_EN_A. Simultaneously, it also can be controlled by an external input signal through DB24.

| State    | VDD                      | CTRL       | EN    | RF Path  |
|----------|--------------------------|------------|-------|----------|
| 1        | 2.7 V to 4.6 V | VHIGH      | VHIGH | ANT-RF2  |
| 2        | 2.7 V to 4.6 V | VLOW       | VHIGH | ANT-RF1  |
| Shutdown | 2.7 V to 4.6 V | Don't Care | VLOW  | Shutdown |

> **Image:** RF Switch Schematic Diagram

#### Electrical Characteristics

Listed in this document are the different electrical characteristics of RAK831 WisLink LPWAN Concentrator.

:::warning
Stress greater than one or more of the limiting values listed under **Absolute Maximum Ratings** may cause permanent damage to the radio module.
:::

##### Absolute Maximum Ratings

| Parameter             | Condition | Min  | Typ. | Max | Unit     |
|-----------------------|-----------|------|------|-----|----------|
| Supply Voltage(VDD)   | -         | -0.3 | 5.0  | 5.5 | V        |
| Operating Temperature | -         | -40  |      | +85 | ° C |
| RF Input Power        | -         |      |      | -15 | dBm      |

:::warning
With RF output power level above +15 dBm, a minimum distance to a transmitter should be 1 meter to avoid a too large input level.
:::

##### Global Electrical Characteristics

| Parameter            | Condition  | Min | Typ. | Max | Unit |
|----------------------|------------|-----|------|-----|------|
| Supply Voltage (VDD) |            | 4.8 | 5.0  | 5.2 | V    |
| Current Consumption  | RX Current |     | 100  |     | mA   |
|                      | TX Current |     | 80   |     | mA   |

At **T=25° C, VDD=5 V (Typ.)** if nothing else stated

| Parameter                        | Condition                          | Min | Typ. | Max | Unit |
|----------------------------------|------------------------------------|-----|------|-----|------|
| Logic low input threshold (VIL)  | “0” logic input                    | -   |      | 0.4 | V    |
| Logic high input threshold (VIH) | “1” logic input                    | 2.9 |      | 3.3 | V    |
| Logic low output level (VOL)     | “0” logic output, 2 mA sink   | -   |      | 0.4 | V    |
| Logic high output level (VOH)    | “1” logic output, 2 mA source | 2.9 |      | 3.3 | V    |

#### Schematic Diagram

The following images are the schematic diagram of the RAK831 WisLink LPWAN Concentrator:

> **Image:** RAK831 Schematic Diagram

> **Image:** RAK831 Schematic Diagram

### Firmware

Download the latest firmware of the RAK831 in the table provided below.

| Model  | Raspberry Pi Board | Firmware Version | Source                                                                                                 |
|--------|--------------------|------------------|--------------------------------------------------------------------------------------------------------|
| RAK831 | Raspberry Pi 3B+   | V4.2.5R          | [Download](https://downloads.rakwireless.com/LoRa/RAK2245-Pi-HAT/Firmware/RAK2245_Latest_Firmware.zip) |
| RAK831 | Raspberry Pi 4     | V4.2.5R          | [Download](https://downloads.rakwireless.com/LoRa/RAK2245-Pi-HAT/Firmware/RAK2245_Latest_Firmware.zip) |

## Models / Bundles

Order Information

| Part Number | Band Frequency |
|-------------|----------------|
| RAK831_433  | 433 MHz   |
| RAK831_470  | 470 MHz   |
| RAK831_868  | 868 MHz   |
| RAK831_915  | 915 MHz   |

