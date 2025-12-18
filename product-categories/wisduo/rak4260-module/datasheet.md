---
title: RAK4260 WisDuo LPWAN Module Datasheet
description: Provides comprehensive information about your RAK4260 Module to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
keywords:
- datasheet
- wisduo
- RAK4260
image: https://images.docs.rakwireless.com/wisduo/rak4260-module/RAK4260-Module.png
sidebar_label: Datasheet
---

    

# RAK4260 WisDuo LPWAN Module Datasheet

## Overview

### Description

The **RAK4260 WisDuo LPWAN Module** is based on **Microchip’s ATSAMR34J18B**. It is a SiP device integrating a 32-bit ARM Cortex M0+ MCU with a LoRa Transceiver in a 15 mm x 15 mm compact package.

The SAM R34 chip provides a number of highly configurable peripherals (configurable as I2C/SPI/UART interfaces). There are 12-bit ADC in addition to the aforementioned.

It is a perfect solution for any LoRaWAN end node developer. The integration of the MCU and LoRa Transceiver reduces size and minimizes costs. Having such a compact solution within a single package reduces time to market and allows for rapid development and deployment for a number of scenarios.

RAK4260 is a solution that is cost-efficient and flexible that can be deployed in a wide variety of IoT scenarios that require the long-range connectivity and great battery life that LoRaWAN provides.

### Features

- Industry's lowest power LoRa SiP device
- 32-bit ARM Cortex M0+ MCU and LoRa Transceiver
- Small form factor: 15 mm x 15 mm  compact package
- 256 KB Flash and 40 KB RAM accommodates application code and stack
- Most cost and size effective solution, eliminating the need for external MCU
- Fully supported 862 to 1020 MHz frequency coverage
- Receive Sensitivity down to -148 dBm
- Maximum Transmit Power up to 20 dBm
- Low RX current of 17 mA (typical)
- LoRa Technology, (G)FSK, (G)MSK

## Specifications

### Overview

The overview section covers the RAK4260 WisDuo LPWAN Module board overview where both top and bottom views are presented. It also includes the functional block diagram showing the interfaces of the board.

#### Board Overview

**Figure 1** and **Figure 2** present the different views of the RAK4260 chip labeled for the proper reference.

> **Image:** RAK4260 WisDuo LPWAN Module Top View

> **Image:** RAK4260 Bottom View

#### Block Diagram

The block diagram of the RAK4260 shows the various interfaces for the specific functionalities set in the product overview.

> **Image:** RAK4260 Interfaces

### Hardware

The hardware specifications are categorized into five parts. It presents the schematic diagram and pinouts of the module. This section covers also the electrical, mechanical, and frequency parameters including tabular data and diagrams of the RAK4260 WisDuo LPWAN Module board.

#### Pin Definition

Provided in this section is the pinout of the RAK4260 WisDuo LPWAN Module.

> **Image:** RAK4260 Board Pinout

:::warning
When using `RFC` pin for antenna and not the IPEX connector variant, there are design considerations to make sure optimum RF performance.

- RF trace must be away from interference (switching node of DC-DC supply, high current/voltage pulses from controllers of inductive load like motor, signal generators, etc.)
- RF trace must have 50 Ohms impedance. It is advisable to use an impedance simulation software tool to achieve this requirement.
- If using an external antenna connector, make it close to the `RFC` pin.
- Ground plane optimization is critical on certain antenna types like monopole.
- GND trace used for RF path return must be directly connected to the GND plane and not be treated as thermal relief.
- It is recommended for the RF trace to be routed in a curve and not in a sharp 90 degrees.

In addition, with a commitment to making IoT easy, RAK offers a dedicated service for [Antenna RF Design](https://store.rakwireless.com/products/antenna-rf-design-service-including-pcb-design-tuning-matching-and-rf-test) which includes PCB design, tuning, matching, and RF testing.
:::

|  PIN  |     NAME      |  I/O  |                Description                 |
| ----- | ------------- | ----- | ------------------------------------------ |
|   1   |      GND      |   -   |                   Ground                   |
|   2   |      RFC      |   -   |                  RF Port                   |
|   3   |      GND      |   -   |                   Ground                   |
|   4   |     PA27      |  I/O  |                  EIC/GCLK                  |
|   5   |     PA06      |  I/O  |   EIC/RSTC/ADC/PTC/OPAMP/TC/CCL/SERCOM0    |
|   6   |     PA07      |  I/O  |     EIC/RSTC/ADC/OPAMP/TC/CCL/SERCOM0      |
|   7   |     PA08      |  I/O  |       DC/PTC/TC/CCL/SERCOM0/SERCOM2        |
|   8   |     PA09      |  I/O  |     EIC/ADC/PTC/TC/CCL/SERCOM0/SERCOM2     |
|   9   |     PB22      |  I/O  |            SERCOM5/TC/GCLK/CCL             |
|  10   |      GND      |   -   |                   Ground                   |
|  11   |    VCC3V3     |   -   |                3V3 power in                |
|  12   |    VCC3V3     |   -   |                3V3 power in                |
|  13   |   PA17_SCL    |  I/O  |    EIC/PTC/TC/GCLK/CCL/SERCOM1/SERCOM3     |
|  14   |   PA16_SDA    |  I/O  |    EIC/PTC/TC/GCLK/CCL/SERCOM1/SERCOM3     |
|  15   |     PA15      |  I/O  |        EIC/TC/GCLK/SERCOM2/SERCOM4         |
|  16   |     PA14      |  I/O  |        EIC/TC/GCLK/SERCOM2/SERCOM4         |
|  17   |      GND      |   -   |                   Ground                   |
|  18   |      GND      |   -   |                   Ground                   |
|  19   | PA18 UART3 RX |  I/O  |     EIC/PTC/TC/AC/CCL/SERCOM1/SERCOM3      |
|  20   | PA19 UART3 TX |  I/O  |     EIC/PTC/TC/AC/CCL/SERCOM1/SERCOM3      |
|  21   |      NC       |   -   |               No Connection                |
|  22   |   PA23_MOSI   |  I/O  |   EIC/PTC/TC/AC/CCL/GCLK/SERCOM3/SERCOM5   |
|  23   |    PA22_SS    |  I/O  |     EIC/PTC/TC/AC/CCL/SERCOM3/SERCOM5      |
|  24   |   PB23_SCK    |  I/O  |          EIC/SERCOM5/TC/GCLK/CCL           |
|  25   |   PB02_MISO   |  I/O  |        EIC/ADC/SERCOM5/TC/SUPC/CCL         |
|  26   |  PA25 USB P   |  I/O  |     EIC/SERCOM3/SERCOM5/TC/USB_DM/CCL      |
|  27   |  PA24 USB N   |  I/O  |     EIC/SERCOM3/SERCOM5/TC/USB_DM/CCL      |
|  28   |      GND      |   -   |                   Ground                   |
|  29   |      RST      |   -   |                 MCU Reset                  |
|  30   |  PA30_SWDCLK  |  I/O  |                   SWDCLK                   |
|  31   |  PA31_SWDIO   |  I/O  |                   SWDIO                    |
|  32   | PA04 UART1 TX |  I/O  | EIC/RSTC/VREFB/ADC/AC/OPAMP/TC/CCL/SERCOM0 |
|  33   | PA05 UART1 RX |  I/O  |    EIC/RSTC/ADC/AC/OPAMP/TC/CCL/SERCOM0    |
|  34   |      NC       |   -   |               No Connection                |
|  35   |      GND      |   -   |                   Ground                   |
|  36   |      GND      |   -   |                   Ground                   |
|  37   |      GND      |   -   |                   Ground                   |
|  38   |      GND      |   -   |                   Ground                   |
|  39   |      GND      |   -   |                   Ground                   |
|  40   |      GND      |   -   |                   Ground                   |

##### RF Switch Pin Definition

| **BAND_SEL** | **TX/RX** |
| :----------: | :-------: |
|     PA13     |    D2     |

##### RF Switch control logic table

| **LoRa Mode** | **BAND_SEL** | **TX/RX** | **PA28** |
| :-----------: | :----------: | :-------: | :------: |
| Shutdown      |      L       |     L     |    L     |
| PA_BOOST      |      L       |     H     |    H     |
| RFI_HF (RX)   |      H       |     L     |    H     |
| RFO_HF        |      H       |     H     |    H     |

:::tip NOTE
PA28 is RF Switch VDD pin

H  = High level

L  = Low level 

:::

#### RF Requirements

##### Operating Frequencies

The RAK4260 supports LoRaWAN frequency included in the table provided below:

|    Region     | Frequency (MHz) |
| :-----------: | :-------------: |
|    Europe     |      EU868      |
| North America |      US915      |
|   Australia   |      AU915      |
|     Asia      |      AS923      |
|     India     |      IN865      |
|     Korea     |      KR920      |

#### Electrical Characteristics

##### Power Consumption

Shown in the table provided below is the power consumption of the RAK4260 WisDuo LPWAN Module.

|             Item              |   Power Consumption   |         Condition          |
| :---------------------------: | :-------------------: | :------------------------: |
| OUTPUT POWER 20 dB (MAX) |     126.3 mA     |   PA_BOOST V=3.3 V    |
|    OUTPUT POWER 17 dB    | 95.6 mA(typical) |   PA_BOOST V=3.3 V    |
|    OUTPUT POWER 14 dB    |     33.1 mA      |    RFO_HF V=3.3 V     |
|         Receive mode          |     13.6 mA      |             -              |
|          Sleep mode           |      860 nA      | V=3.3 V Backup Mode |

##### OUTPUT POWER 20 dB(MAX)PA_BOOST mode

> **Image:** OUTPUT POWER 20 dB(MAX)

##### OUTPUT POWER 17 dB(PA_BOOST mode)

> **Image:** OUTPUT POWER 17 dB

##### OUTPUT POWER 14 dB(RFO_HF mode)

> **Image:** OUTPUT POWER 14 dB

##### Receive Mode

> **Image:** Receive Mode

##### Sleep Mode

> **Image:** Sleep Mode

##### Sensitivity Level

The following chart shows the receiving sensitivity of RAK4260 at 868 Mhz.

| Receive Power @iPEX | PER (%) @SF7 |
| :-----------------: | :----------: |
|     -40 to -124     |      0       |
|        -125         |      3       |
|        -126         |      20      |
|        -127         |      78      |
|        -128         |     100      |
|        -129         |     100      |
|        -130         |     100      |

> **Image:** Sensitivity Level (SF7)

| Receive Power @iPEX | PER (%) @SF7 |
| :-----------------: | :----------: |
|     -50 to -134     |      0       |
|        -135         |      0       |
|        -136         |      0       |
|        -137         |      0       |
|        -138         |      7       |
|        -139         |      80      |
|        -140         |     100      |

> **Image:** Sensitivity Level (SF12)

#### Schematic Diagram

> **Image:** RAK4260 WisDuo LPWAN Module Schematic Diagram

#### Mechanical Characteristics

> **Image:** RAK4260 Top View Dimensions

> **Image:** RAK4260 Side View Dimensions

### Software

The latest firmware for the RAK4260 WisDuo LPWAN Module is provided in the given table.

#### Firmware

| Model   | Source                                                                                          |
| ------- | ----------------------------------------------------------------------------------------------- |
| RAK4260 | [Download](https://downloads.rakwireless.com/LoRa/RAK4260/Firmware/RAK4260_Latest_Firmware.rar) |

<!-- ## Certification -->
