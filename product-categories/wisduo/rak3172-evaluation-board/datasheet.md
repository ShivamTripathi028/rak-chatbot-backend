---
title: RAK3172 STM32 LoRaWAN Evaluation Board Datasheet | Specs & Features
description: Explore the RAK3172 Evaluation Board with STM32WLE5CCU6. Get pinout details, specs, and LoRaWAN features for IoT development. Ideal for low-power RF projects!
image: https://images.docs.rakwireless.com/wisduo/rak3172-evaluation-board/rak3172-evaluation.png
keywords: 
  - stm32wle5ccu6
  - rak3172 
  - rak3172 pinout
  - lora transceiver
  - lora evaluation board
  - rak3172 evaluation board
  - stm32 lorawan
  - lora development board
  - lora wireless module
  - low power lorawan module
date: 2021-07-23
sidebar_label: Datasheet
slug: /product-categories/wisduo/rak3172-evaluation-board/datasheet/
download: true
---

# RAK3172 Evaluation Board Datasheet

## Overview

### Description

The RAK3172-E is a WisDuo evaluation board for the RAK3172 module, using an STM32WLE5CCU6 SoC chip.  It is based on the RAK3372 WisBlock Core, compatible with the RAK5005-O base board. It provides easy access to the important pins of the RAK3172 module, simplifying development and testing. It also allows connection of other modules to the base board slots, enabling the building of complete IoT projects with integrated connectors for battery and solar panel, plus an onboard charging circuit.

This module complies with LoRaWAN 1.0.3 specifications (Classes A, B, and C). It also supports LoRa point-to-point (P2P) communication, facilitating the quick implementation of customized long-range LoRa networks.

### Features

- Based on **STM32WLE5CCU6**
- **LoRaWAN 1.0.3** specification compliant
- **Supported bands**: EU433, CN470, IN865, EU868, AU915, US915, KR920, RU864, and AS923-1/2/3/4
- LoRaWAN Activation by OTAA/ABP
- LoRa Point-to-Point (P2P) communication
- Custom firmware using Arduino via RUI3 API
- Easy to use AT command set via UART interface
- Long-range - greater than 15 km with optimized antenna
- ARM Cortex-M4 32-bit
- 256 kbytes flash memory with ECC
- 64 kbytes RAM
- **Supply Voltage**: 5 V via USB or 3.7-4.2 V using Li-Ion Battery
- **Temperature Range**: -20° C ~ 70° C

## Specifications

This section covers the hardware and software specifications for the RAK3172 Evaluation Board.  It includes the interfaces, operating parameters, and a link to the board's latest firmware.

### Overview

> **Image:** RAK3172 Evaluation Board Overview

### Hardware

The hardware specification is categorized into six parts.  It discusses the interfacing, pinouts, and their corresponding functions and diagrams. It also covers the electrical, mechanical, and environmental parameters, including tabular data of the functionalities and standard values of the RAK3172 Evaluation Board.

#### Interfaces

> **Image:** RAK3172 Evaluation Board Interfaces

> **Image:** Parts RAK3372 Module

##### RF Interface

The RF Antenna of the RAK3172 Evaluation Board is connected to a standard iPEX antenna connector.

> **Image:** RAK3172 LoRa antenna

:::warning
Make sure to install the LoRa antenna first before powering the RAK3172 Evaluation Board. Failure to do so can damage the board.
:::

##### USB Interface

The Micro-B USB connector is compliant with the USB 2.0 specification. The pin definition of the USB interface is shown below:

| **Pin Number** | **Pin Name** | **Description**             |
| -------------- | ------------ | --------------------------- |
| 1              | USB_VBUS     | (+5 V) USB Bus Voltage |
| 2              | USB_DM       | USB Bus D+ positive pin     |
| 3              | USB_DP       | USB Bus D- negative pin     |
| 4              | NC           | Not connected               |
| 5              | GND          | Ground                      |

> **Image:** RAK3172 Micro-B USB connector

The USB data bus is connected to a **USB-SERIAL CH340** chip. The **CH340** is a series of USB bus adapters that provide a virtual serial interface over the USB bus.

##### Battery Connector

The RAK3172 Evaluation Board can be powered by a battery via the P1 connector. The battery is not included in the packaging.

Use **Figure 6** as a guide to connect the battery. The pin highlighted in the yellow box with the triangle silkscreen mark indicates pin 1 (GND).

> **Image:** RAK3172 EVB battery connector

The pin definition of the RAK3172 Evaluation Board Li-Ion battery connector is shown in the table below. The matching connector for the battery wires is a [JST PHR-2 2 mm pitch female](https://www.jst-mfg.com/product/detail_e.php?series=199).

** P1 Battery Connector **

| **Pin** | **Pin Name** | **Description**               |
| ------- | ------------ | ----------------------------- |
| 1       | GND          | Ground                        |
| 2       | VBAT         | Positive + pin of the battery |

The full specification of RAK3172 Evaluation Board battery is shown in the table below.

| **No.** | **Item**                  | **Specification**                    |
| ------- | ------------------------- | ------------------------------------ |
| 1       | Charge Cut-off Voltage    | 4.2 V                           |
| 2       | Nominal Voltage           | 3.7 V                           |
| 3       | Discharge Cut-off Voltage | 2.75 V                          |
| 4       | Typical Capacity          | 2650 mAh                        |
| 5       | Max Discharge Current     | 0.5 C at 25 ℃ to 45 ℃ |
| 6       | PH Connector              | 2.0 mm pitch                    |
| 7       | Cable Length              | 110.0±3.0 mm                    |
| 8       | Cable Color               | Red: VBAT, Black: GND                |

:::tip NOTE
The voltage of the Li-Ion battery **must not exceed 4.3 V**. When connecting the battery make sure the polarity is correct. Not all connectors are wired the same.
:::

##### Solar Panel Connector

A 5 V solar panel can be connected to the board via the P2 connector to charge the battery. The solar panel is not included in the RAK3172 Evaluation Board packaging. Use **Figure 7** as a guide to connect the solar panel. The pin highlighted in the yellow box with triangle silkscreen marking indicates pin 1 (5 V solar panel positive).

> **Image:** RAK3172 EVB solar connector

The pin definition of the RAK3172 Evaluation Board solar panel connector is shown in the table below. The matching connector for the solar panel wires is an [JST ZHR-2 1.5 mm pitch female](https://www.jst-mfg.com/product/detail_e.php?series=287).

** P2 Solar Panel connector **

| **Pin** | **Pin Name** | **Description**               |
| ------- | ------------ | ----------------------------- |
| 1       | C0NN_5V      | Positive + pin of solar panel |
| 2       | GND          | GND                           |

The full specification of the Solar Panel for the RAK3172 Evaluation Board is shown in the table below.

| **No.** | **Item**        | **Specification**                                        |
| ------- | --------------- | -------------------------------------------------------- |
| 1       | Nominal Voltage | 5 V                                                 |
| 2       | Typical Current | 80 mA                                               |
| 3       | Size            | Length: 60 mm, Width: 60 mm, Height: 2 mm |
| 4       | Connector       | 1.5 mm pitch                                        |
| 5       | Cable Color     | Red: C0NN_5V, Black: GND                                 |

:::tip NOTE
The output of the solar panel **must not exceed 5.5 V**. Otherwise, it may cause permanent damage to the board.
:::

##### LEDs

- 🔴 **Red LED** - connected to the charger chip to indicate the charger status. When the battery is charging, the red LED is on. When the battery is full, this LED is dimmed or off.
- 🟢 **Green LED** - connected to the MCU module, can be controlled in code by the user.
- 🔵 **Blue LED** - connected to the MCU module, can be controlled in code by the user.

##### RESET Button

The reset push button is connected to the NRST pin of the RAK3172. When pushed, it resets the MCU.

#### Pin Definition

The following tables below show the pin definitions of the RAK3172 Evaluation Board:

##### J10, J11, J12 2.54 mm header

###### J10

| **Pin Number** | **Pin Name**  | **Description**                      | **Microcontroller Pin** |
| -------------- | ------------- | ------------------------------------ | ----------------------- |
| 1              | BOOT0         | Boot for ST MCU                      | BOOT0                   |
| 2              | VDD           | Power supply generated by CPU module |                         |
| 3              | TX1/USART1_TX | USART1 TX pin                        | PB6                     |
| 4              | RX1/USART1_RX | USART1 RX pin                        | PB7                     |

###### J11

| **Pin Number** | **Pin Name** | **Description**               | **Microcontroller Pin** |
| -------------- | ------------ | ----------------------------- | ----------------------- |
| 1              | AIN1         | ADC input signal              | PB3                     |
| 2              | IO1          | General purpose IO            | PB5                     |
| 3              | IO2          | Power switch control of 3V3_S | PA8                     |
| 4              | GND          | Ground                        |                         |

:::tip NOTE
3V3_S is another 3.3 V power supply that can be turned on and off by the MCU. Set pin IO2 to `LOW`/`0` when the sensor is not in use to save power.
:::

###### J12

| **Pin Number** | **Pin Name** | **Description**                      | **Microcontroller Pin** |
| -------------- | ------------ | ------------------------------------ | :---------------------: |
| 1              | GND          | Ground                               |                         |
| 2              | I2C1_SCL     | I2C clock pin                        |          PA12           |
| 3              | I2C1_SDA     | I2C data pin                         |          PA11           |
| 4              | VDD          | Power supply generated by CPU module |                         |

#### RF Characteristics

The RAK3172 supports two frequency variations: RAK3172(L) for low radio frequencies and RAK3172(H) for high radio frequencies.

##### Operating Frequencies

| Module     | Region        | Frequency     |
| ---------- | ------------- | ------------- |
| RAK3172(L) | Europe        | EU433         |
|            | China         | CN470         |
| RAK3172(H) | Europe        | EU868         |
|            | North America | US915         |
|            | Australia     | AU915         |
|            | Korea         | KR920         |
|            | Asia          | AS923-1/2/3/4 |
|            | India         | IN865         |
|            | Russia        | RU864         |

#### Electrical Characteristics

##### Operating Voltage

Power is supplied to the RAK3172 Evaluation Board via USB (5 V) or a Li-Ion battery.

The LDO regulator can operate on the following voltage range:

| Feature | Minimum | Maximum | Unit      |
| ------- | ------- | ------- | --------- |
| Vin     | 1.8     | 6.5     | Volts (V) |

##### Schematic Diagram

> **Image:** RAK3172 Evaluation Board Schematic Diagram

#### Mechanical Characteristics

##### Module Dimensions

> **Image:** RAK3172 Physical Dimension

#### Environmental Characteristics

##### Operating Temperature

| Feature               | Minimum | Typical | Maximum | Unit |
| --------------------- | ------- | ------- | ------- | ---- |
| Operating Temperature | -35     | 25      | 70      | °C   |

### Software

Download the latest firmware for the RAK3172 WisDuo evaluation board provided below.  The RAK3172(L) and RAK3172(H) use the same firmware; it will automatically detect the module variant.

The **bin file** contains the application code only and you need the RAK DFU Tool to upload this file to the module.

The **hex file** contains both the bootloader and the application code. You need to use STM32CubeProgrammer to upload this.

:::warning
Uploading the `**.hex**` file via STM32CubeProgrammer will erase all configured data on the device.
:::

RAK3172 uses UART2's serial pins to upload the latest firmware.

:::tip NOTE
RAK3172 should automatically go to BOOT mode when the firmware is being uploaded via RAK DFU Tool or WisToolBox.

If BOOT mode is not initiated, you can manually send `AT+BOOT` command to start bootloader mode.
:::

#### Firmware/OS

| Model   | Version                                         | Source                                                                                          |
| ------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| RAK3172 | RUI3 (default baudrate = 115200)                |   [Download](https://downloads.rakwireless.com/RUI/RUI3/Image/RAK3172-E_latest.bin)             |
| RAK3172 | RUI3 (default baudrate = 115200)                |   [Download](https://downloads.rakwireless.com/RUI/RUI3/Image/RAK3172-E_latest_final.hex)       |
| RAK3172 | **DEPRECATED** V1.0.4 (default baudrate = 9600) | [Download](https://downloads.rakwireless.com/LoRa/RAK3172/Firmware/RAK3172_Latest_Firmware.zip) |

:::warning
There are RAK3172 devices loaded with old firmware versions which are not based on RUI3 (RAKwireless Unified Interface V3). These devices have v1.0.4 and below.

If the host microcontroller code is based on this old firmware, we have a [RAK3172 AT Command migration guide](https://learn.rakwireless.com/hc/en-us/articles/26687498449559-AT-Command-Migration-Guide-of-RAK3172-to-RUI3-RAKwireless-Unified-Interface-V3/) that explain in detail the few differences between the two AT commands set.
:::

### Certification

:::tip Note
For CE and FCC certifications we provide an AT command guide.    
You can find it in our [RUI3 documentation](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/certification-guide) or get it from our [Download Center](https://downloads.rakwireless.com/#RUI/RUI3/Certification%20Guide/).    
::: 

