---
title: RAK3172-SiP WisDuo LPWAN SiP Datasheet
description: Provides comprehensive information about the RAK3172-SiP to help you use it. This information includes technical specifications, characteristics, and requirements, and also discusses the device components.
image: https://images.docs.rakwireless.com/wisduo/rak3172-sip/rak3172-sip.png
keywords:
  - datasheet
  - wisduo
  - RAK3172-SiP
sidebar_label: Datasheet
slug: /product-categories/wisduo/rak3172-sip/datasheet/
download: true
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK3172-SiP WisDuo LPWAN SiP Datasheet

## Overview

### Description

RAK3172-SiP (and the RAK3172LP-SiP variant) are low-power, long-range transceivers based on the STM32WLE5JC SoC in a system-in-package form factor.  These two modules use different RF output paths to optimize current consumption depending on the application.  RAK3172-SiP uses RFO_HP, while RAK3172LP-SiP uses the RFO_LP of the STM32WL SoC transceiver.

WisDuo SiP LoRa modules provide a small, easy-to-use, low-power solution for long-range wireless data applications. These modules comply with Classes A, B, and C of the LoRaWAN 1.0.3 specifications. They can easily connect to different LoRaWAN server platforms such as TheThingsNetwork (TTN), Helium, ChirpStack, and Actility. They also support LoRa point-to-point (P2P) communication mode, which facilitates the quick implementation of customized long-range LoRa networks.

You can configure the mode and operation of the RAK3172-SiP/RAK3172LP-SiP using AT commands via a UART interface or create custom firmware using the RUI3 API.  The RAK3172-SiP/RAK3172LP-SiP are very small and offer low-power features suitable for battery-powered applications.


:::warning
The RAK3172-SiP does not have pre-flashed LoRaWAN credentials and you have to define and setup your own unique credentials for the SiP's.
:::

### Features

- Based on **STM32WLE5JC**
- Two variants available
    - RAK3172-SiP (uses RFO_HP)
    - RAK3172LP-SiP (uses RFO_LP)
- System-in-Package form factor
- RUI3 API compatible
- **LoRaWAN 1.0.3** specification compliant
- **Supported bands**: IN865, EU868, AU915, US915, KR920, RU864, and AS923
- LoRaWAN Activation by OTAA/ABP
- LoRa Point-to-Point (P2P) communication
- Custom firmware using Arduino via RUI3 API
- Easy-to-use AT Command set via UART interface
- Long-range - up to 15&nbsp;km with optimized antenna
- ARM Cortex-M4 32-bit
- 256&nbsp;kbytes flash memory with ECC
- 64&nbsp;kbytes RAM
- Ultra-low power consumption of 1.69&nbsp;μA in sleep mode
- **Supply voltage**: 2.0&nbsp;V ~ 3.6&nbsp;V
- **Temperature range**: -40°&nbsp;C ~ 85°&nbsp;C
- **Size**: 12&nbsp;mm x 12&nbsp;mm x 1.22&nbsp;mm
- **Package**: LGA73 type

## Specifications

This section covers the hardware and software specifications for the RAK3172-SiP.  It also includes a block diagram and an updated firmware link for the RAK3172-SiP WisDuo Module.

### Overview

#### Block Diagram

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-sip/datasheet/rak3172-block-diagram.svg"
  width="70%"
  caption="RAK3172-SiP system block diagram"
  zoomMode={true}
/>

### Hardware

The hardware specification is categorized into six parts.  It discusses the interfacing, pinouts, and their corresponding functions and diagrams. It also covers the RF, electrical, mechanical, and environmental parameters, including tabular data of the functionalities and standard values of the RAK3172-SiP WisDuo LPWAN SiP module.

:::tip NOTE

For the reference application schematic of RAK3172-SiP with minimum components requirements, refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3272-sip-breakout-board/datasheet/#hardware" target="_blank">RAK3272-SiP Breakout Board Datasheet.</a>

:::

#### Interfaces

| Module        | Interfaces                            |
| :-----------: | :-----------------------------------: |
| RAK3172-SiP   | UART2 (Default for AT Command), UART1 |
| RAK3172LP-SiP | UART2 (Default for AT Command), UART1 |

#### Pin Definition

You can check the pin definitions on the table and illustration, as shown in **Figure 2**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-sip/datasheet/rak3172-sip-pins.png"
  width="40%"
  caption="RAK3172-SiP top view pin diagram"
  zoomMode={true}
/>

:::warning
When using the `RF_OUT` pin for an antenna and not the IPEX connector variant, design considerations are necessary to ensure optimum RF performance.

- The RF trace must be away from sources of interference (switching nodes of DC-DC supplies, high-current/high-voltage pulses from controllers of inductive loads like motors, signal generators, etc.).
- The RF trace must have 50-ohm impedance.  Using impedance simulation software is advisable to achieve this.
- If using an external antenna connector, position it close to the `RF_OUT` pin.
- Ground plane optimization is critical for certain antenna types, such as monopoles.
- The GND trace used for the RF return path must be directly connected to the GND plane and not treated as a thermal relief.
- It is recommended to route the RF trace in a curve, rather than with sharp 90-degree angles.

In addition, with a commitment to making IoT easy, RAK offers a dedicated service for <a href="https://store.rakwireless.com/products/antenna-rf-design-service-including-pcb-design-tuning-matching-and-rf-test" target="_blank">Antenna RF Design</a> which includes PCB design, tuning, matching, and RF testing.
:::


| **Pin No.** | **Name**     | **Type** | **Description**                                                    |
| :---------: | :----------: | :------: | ------------------------------------------------------------------ |
| 1           | PA13         | I        | Reserved - SWD debug pin (SWDIO)                                   |
| 2           | PA14         | O        | Reserved - SWD debug pin (SWCLK)                                   |
| 3           | VDD          |          | VDD                                                                |
| 4           | VBAT         |          | VDD (For RTC)                                                      |
| 5           | PC13         | I/O      | GPIO                                                               |
| 6           | VREF+        |          | Input reference voltage for ADC                                    |
| 7           | VDDA         |          | External power supply for the analog sections (ADC Converter)      |
| 8           | PA15         | I/O      | GPIO or PIN_A4                                                     |
| 9           | PB15         | I/O      | GPIO                                                               |
| 10          | VFBSMPS      |          | DC-DC switching power feedback                                     |
| 11          | VDDMPS       |          | DC-DC switching power input                                        |
| 12          | GND          |          | Ground                                                             |
| 13          | VLXSMPS      |          | DC-DC switching output                                             |
| 14          | PB3          | I/O      | GPIO or PIN_A0                                                     |
| 15          | PB4          | I/O      | GPIO or PIN_A1                                                     |
| 16          | PB5          | I/O      | GPIO                                                               |
| 17          | PB6/UART1_TX | I/O      | GPIO or UART1_TX                                                   |
| 18          | PB7/UART1_RX | I/O      | GPIO or UART1_RX                                                   |
| 19          | PB8          | I/O      | GPIO                                                               |
| 20          | PB9          | I/O      | GPIO                                                               |
| 21          | PC0          | I/O      | GPIO                                                               |
| 22          | PC1          | I/O      | GPIO                                                               |
| 23          | PC2          | I/O      | GPIO                                                               |
| 24          | PC3          | I/O      | GPIO                                                               |
| 25          | PC4          | I/O      | GPIO                                                               |
| 26          | PC5          | I/O      | GPIO                                                               |
| 27          | PC6          | I/O      | GPIO                                                               |
| 28          | GND          |          | Ground                                                             |
| 29          | PA2/UART2_TX | O        | Reserved - UART2/LPUART1 Interface (AT Commands and FW Update)     |
| 30          | PA3/UART2_RX | I        | Reserved - UART2/LPUART1 Interface (AT Commands and FW Update)     |
| 31          | PA4          | I/O      | GPIO or SPI1 (SPI1_CS)                                             |
| 32          | PA5          | I/O      | GPIO or SPI1 (SPI1_CLK)                                            |
| 33          | PA6          | I/O      | GPIO or SPI1 (SPI1_MISO)                                           |
| 34          | PA7          | I/O      | GPIO or SPI1 (SPI1_MOSI)                                           |
| 35          | GND          |          | Ground                                                             |
| 36          | GND          |          | Ground                                                             |
| 37          | RF_OUT       | O        | RF Output                                                          |
| 38          | GND          |          | Ground                                                             |
| 39          | GND          |          | Ground                                                             |
| 40          | NC           |          | Not connected                                                      |
| 41          | NC           |          | Not connected                                                      |
| 42          | NC           |          | Not connected                                                      |
| 43          | BOOT 0       | I        | Boot Mode Select pin (Activates STM32WL UART Bootloader when HIGH) |
| 44          | NRST         | I        | MCU Reset (NRST)                                                   |
| 45          | NC           |          | Not connected                                                      |
| 46          | GND          |          | Ground                                                             |
| 47          | GND          |          | Ground                                                             |
| 48          | PB11         | I/O      | GPIO                                                               |
| 49          | PB10         | I/O      | GPIO                                                               |
| 50          | PA9          | I/O      | GPIO or I2C_SCL                                                    |
| 51          | PA8          | I/O      | GPIO                                                               |
| 52          | GND          |          | Ground                                                             |
| 53          | VDDPA        |          | RF PA power input                                                  |
| 54          | VDDRF        |          | RF Segment power input                                             |
| 55          | VDD          |          | VDD                                                                |
| 56          | GND          |          | Ground                                                             |
| 57          | PB1          | I/O      | GPIO                                                               |
| 58          | PB2          | I/O      | GPIO or PIN_A2                                                     |
| 59          | PB12         | I/O      | GPIO                                                               |
| 60          | PB13         | I/O      | GPIO                                                               |
| 61          | PB14         | I/O      | GPIO                                                               |
| 62          | PA10         | I/O      | GPIO or PIN_A3 or I2C_SDA                                          |
| 63          | PA11         | I/O      | GPIO                                                               |
| 64          | PA12         | I/O      | GPIO                                                               |
| 65-73       | GND          |          | Ground                                                             |


#### RF Characteristics

The RAK3172-SiP supports the frequency of operation from 863 to 930&nbsp;Mhz.

##### Operating Frequencies

| Region        | Frequency     |
| :-----------: | :-----------: |
| Europe        | EU868         |
| North America | US915         |
| Australia     | AU915         |
| Korea         | KR920         |
| Asia          | AS923-1/2/3/4 |
| India         | IN865         |
| Russia        | RU864         |

#### Electrical Characteristics

##### Absolute Maximum Ratings

| Parameter    | Minimum     | Typical | Maximum | Unit      |
| :----------: | :---------: | :-----: | :-----: | :-------: |
| VDD and GPIO | -0.3&nbsp;V | -       | 3.9     | Volts (V) |


##### Operating Voltage

| Parameter                             | Minimum | Typical | Maximum | Unit      |
| :-----------------------------------: | :-----: | :-----: | :-----: | :-------: |
| VCC                                   | 1.8     | -       | 3.6     | Volts (V) |
| VDDA (ADC or COMP used)               | 1.71    | -       | 3.6     | Volts (V) |
| VDDA (VREFBUF used)                   | 2.4     | -       | 3.6     | Volts (V) |
| VDDA (ADC, COMP, or VREFBUF not used) | 0       | -       | 3.6     | Volts (V) |
| VBAT                                  | 1.55    | -       | 3.6     | Volts (V) |
| VDDSMPS                               | 1.8     | -       | 3.6     | Volts (V) |
| VDDRF                                 | 1.8     | -       | 3.6     | Volts (V) |
| VDDPA                                 | 1.8     | -       | 3.6     | Volts (V) |
| VREF+                                 | 2.0     | -       | VDDA    | Volts (V) |
| VREF+ (VDDA < 2&nbsp;V)               | VDDA    | -       | VDDA    | Volts (V) |


##### Operating Current

###### RAK3172-SiP (uses RFO_HP RF output)

| Parameter  | Condition   | Current Consumption (Typical) |
| :--------: | :---------: | :---------------------------: |
| TX mode    | 20&nbsp;dBm | 87&nbsp;mA                    |
| RX mode    | -           | 6.14&nbsp;mA                  |
| Sleep mode | -           | 1.69&nbsp;uA                  |

###### RAK3172LP-SiP (uses RFO_LP RF output)

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Condition</th>
      <th>Current Consumption (Typical)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan = "4" >TX mode</td>
      <td>14&nbsp;dBm</td>
      <td>39.1&nbsp;mA</td>
    </tr>
    <tr>
      <td>12&nbsp;dBm</td>
      <td>33&nbsp;mA</td>
    </tr>
    <tr>
      <td>10&nbsp;dBm</td>
      <td>28&nbsp;mA</td>
    </tr>
    <tr>
      <td>8&nbsp;dBm</td>
      <td>25&nbsp;mA</td>
    </tr>
    <tr>
      <td>RX mode</td>
      <td>-</td>
      <td>9.69&nbsp;mA</td>
    </tr>
    <tr>
      <td>Sleep mode</td>
      <td>-</td>
      <td>2.1&nbsp;uA</td>
    </tr>
  </tbody>
</table>

#### Mechanical Characteristics

##### Module Dimensions

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-sip/datasheet/rak3172-sip-mechanical.png"
  width="80%"
  caption="RAK3172-SiP mechanical dimension"
  zoomMode={true}
/>

##### Layout Recommendation

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-sip/datasheet/rak3172-sip-pad.png"
  width="40%"
  caption="RAK3172-SiP layout"
  zoomMode={true}
/>

#### Environmental Characteristics

##### Operating Temperature

| Feature               | Minimum | Typical | Maximum | Unit |
| :-------------------: | :-----: | :-----: | :-----: | :--: |
| Operating Temperature | -40     | 25      | 85      | °C   |

##### Storage Temperature

| Feature             | Minimum | Typical | Maximum | Unit |
| :-----------------: | :-----: | :-----: | :-----: | :--: |
| Storage Temperature | -40     | -       | 85      | °C   |

##### Recommended Reflow Profile

:::warning
- On SMT reflow process, follow MSL3 (Moisture Sensitivity Level 3) guidance for PCBA assembly.
- Before SMT reflow, it is recommended to bake at 125°&nbsp;C for 12&nbsp;hours first to reduce the risk of soldering issues and abnormalities.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-sip/datasheet/reflow.jpg"
  width="50%"
  caption="Reflow profile for RAK3172-SiP"
  zoomMode={true}
/>

Standard conditions for reflow soldering:

- Pre-heating Ramp (A) (Initial temperature: 150°&nbsp;C): **1~2.5°&nbsp;C/sec**
- Soaking Time (T2) (110~190°&nbsp;C): **90~120&nbsp;sec**
- Peak Temperature (G): **240~245°&nbsp;C**
- Reflow Time (T3) (240-245°&nbsp;C): **50~70&nbsp;sec**
- Ramp-up Rate (B): **1-3°&nbsp;C/sec**
- Ramp-down Rate (C): **1~5°&nbsp;C/sec**

### Software

Download the latest RAK3172-SiP WisDuo LPWAN SiP firmware provided below.

- The **bin file** contains the application code only and you need the RAK DFU Tool to upload this file to RAK3172-SiP via UART.
- The **hex file** contains both the bootloader and the application code. You need to <a href="https://learn.rakwireless.com/hc/en-us/articles/26687606549911-How-To-Guide-STM32CubeProgrammer-for-RAK-Modules" target="_blank">use STM32CubeProgrammer to upload</a> this.

RAK3172-SiP uses UART2 serial pins to upload the latest firmware.

#### Firmware/OS

Download the latest RAK3172-SiP and RAK3172LP-SiP firmware provided below.

| Model                | Version                   | Source                                                                                                                 |
| :------------------: | :-----------------------: | :--------------------------------------------------------------------------------------------------------------------: |
| RAK3172-SiP (.bin)   | RUI3 (App only)           | <a href="https://downloads.rakwireless.com/RUI/RUI3/Image/RAK3272-SiP_latest.bin" target="_blank">Download</a>         |
| RAK3172-SiP (.hex)   | RUI3 (Bootloader and App) | <a href="https://downloads.rakwireless.com/RUI/RUI3/Image/RAK3272-SiP_latest_final.hex" target="_blank">Download</a>   |
| RAK3172LP-SiP (.bin) | RUI3 (App only)           | <a href="https://downloads.rakwireless.com/RUI/RUI3/Image/RAK3272LP-SiP_latest.bin" target="_blank">Download</a>       |
| RAK3172LP-SiP (.hex) | RUI3 (Bootloader and App) | <a href="https://downloads.rakwireless.com/RUI/RUI3/Image/RAK3272LP-SiP_latest_final.hex" target="_blank">Download</a> |


## Models and Bundles

### Ordering Information

| P/N                 | Model       | Frequency                           | SKU    |
| :-----------------: | :---------: | :---------------------------------: | :----: |
| RAK3172-SIP-8-SM-NI | RAK3172-SiP | 8XX MHz for RU864/IN865/EU868       | 305041 |
| RAK3172-SIP-9-SM-NI | RAK3172-SiP | 9XX MHz for US915/AU915/KR920/AS923 | 306039 |

## Certification

<RkCertificationIcons certifications={[
    {
        'anatel': 'https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_ANATEL_Certification.pdf',
    },
    {
        'ce': 'https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_CE_Certification.pdf',
    },
    {
        'fcc': 'https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_FCC_Certification.zip',
    },
    {
        'ised': 'https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_ISED_Certification.pdf',
    },
    {
        'jrl': 'https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_JRL_Certfication.pdf',
    },
    {
        'kc': 'https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_KC_Certification.pdf',
    },
    {
        'lorawan': 'https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_Lora_Alliance_Certification.pdf',
    },
    {
        'rcm': 'https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_RCM_Certification.pdf',
    },
    {
        'reach': 'https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_REACH_Report.pdf',
    },
    {
        'rohs': 'https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_RoHS_Report.pdf',
    },
    {
        'rsm': 'https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_RSM_Certification.pdf',
    },
    {
        'ukca': 'https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_UKCA_Certification.pdf',
    },
    {
        'wpc': 'https://downloads.rakwireless.com/LoRa/RAK3172/Certification/RAK3172_WPC_Certification.pdf',
    },
]} />

:::tip Note
For CE and FCC certifications we provide an AT command guide.    
You can find it in our <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/certification-guide" target="_blank">RUI3 documentation</a> or get it from our <a href="https://downloads.rakwireless.com/#RUI/RUI3/Certification%20Guide/" target="_blank">Download Center</a>.    
::: 

  <RkBottomNav/>
