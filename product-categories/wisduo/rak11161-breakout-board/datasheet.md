---
title: RAK11161 WisDuo LoRaWAN BLE WiFi Breakout Board Specs & Datasheet
description: Access the RAK11161 datasheet for comprehensive specs, featuring STM32WLE5 LoRa transceiver, ESP8684 WiFi/BLE, ultra-low power, and long-range connectivity.
image: https://images.docs.rakwireless.com/wisduo/rak11160-module/rak11160-module.png
keywords:
  - rak11161
  - wisduo
  - lorawan module
  - lorawan ble wifi module specs
  - espressif esp8684
  - stm32wle5 lora module with ble and wifi
  - ble 5 lora module
  - long range low power mcu
  - rak11161 datasheet
  - rak11161 specs
  - wisduo rak11161 specs
  - esp8684 lora module specs
tags:
  - rak11161
  - datasheet
  - wisduo
sidebar_label: Datasheet
slug: /product-categories/wisduo/rak11161-breakout-board/datasheet/
date: 2025-08-14
---

# RAK11161 WisDuo LoRaWAN + BLE + WiFi Breakout Board Datasheet

## Overview

### Description

The **RAK11161** is a breakout board for the low-power, long-range LoRaWAN module RAK11160 based on the STM32WLE5 MCU with integrated LoRa transceiver. It uses an Espressif ESP8684 co-processor to support Bluetooth 5.0 (with Bluetooth Low Energy support) and WiFi connectivity.

Compliant with LoRaWAN 1.0.4 specifications (Classes A, B, and C), the module also supports LoRa point-to-point (P2P) communication, facilitating quick implementation of customized LoRa networks. Additionally, RAK11161 offers three RF communication capabilities (LoRa, BLE, and WiFi), making it well-suited for various IoT applications, such as home automation, sensor networks, building automation, and other IoT network applications.

By default, RAK11161 runs on the RUI3 (RAKwireless Unified Interface) firmware, allowing standalone operation with custom firmware development via Arduino-compatible RUI3 APIs. Sensors and other external peripherals can connect directly, eliminating the need for an additional MCU. Alternatively, the RAK11161 can be interfaced with an external host MCU using AT commands via UART.

### Features

- Based on RAK11160
- Provides all RAK11160 pins via a pin header
- Includes Serial Wire Debug (SWD) interface for the STM32WLE5CC
- UART interface for ESP8684 debug
- UART interface for AT command interface
- Based on **STM32WLE5**
	- Arm 32-bit Cortex-M4
	- 256 kB Flash and 64 kB SRAM
	- **LoRaWAN 1.0.4** specification compliant
	- **Supported bands**: IN865, EU868, AU915, US915, KR920, RU864, and AS923-1/2/3/4
	- LoRaWAN Activation by OTAA/ABP
	- LoRa Point-to-Point (P2P) communication
	- Transmitter output power, programmable up to +22 dBm
	– 137 dBm for LoRa (BW = 125 kHz, SF = 12)
	- TCXO crystal
- WiFi modem processor based on **Espressif ESP8684**
	- 32-bit RISC-V single-core processor, up to 120 MHz
	- 576 KB ROM
	- 2 MB Flash
	- 272 kB SRAM
	- BLE 5.0 support
		- Bluetooth LE: Bluetooth 5.3 certified
		- High power mode (20 dBm)
		- Speed: 125 Kbps, 500 Kbps, 1 Mbps, 2 Mbps
	- WiFi support
		- Complies with IEEE 802.11b/g/n
		- Supports 20 MHz bandwidth in 2.4 GHz band
		- 1T1R mode with data rate up to 72.2 Mbps
- Custom firmware using Arduino via RUI3 API
- Easy-to-use AT command set for STM32WLE5 and LoRa settings via the UART interface
- Espressif AT commands for configuring ESP8684 WiFi and BLE settings via the UART interface (similar to STM32WLE5 commands)
- I/O ports: UART/I2C/SPI/ADC/GPIO
- Long-range: greater than 10 km with optimized antenna
- Consumes ~6 μA with ESP8684 powered down and STM32WLE5 in deep sleep
- **Supply Voltage**: 3.0 V\~3.6 V
- **Temperature range**: -40° C\~85° C
- Dimensions: 29 mm x 40 mm

## Specifications

### Overview

#### Block Diagram

> **Image:** RAK11161 system block diagram

### Hardware

The hardware specification is categorized into three parts: RF, electrical, and mechanical parameters. These include tabular data of the functionalities and standard values for the RAK11161 WisDuo LPWAN Module.

#### Internal Connections Between STM32WLE5 MCU and ESP32-C2 MCU

| STM32WLE5 Name | STM32WLE5 Pin | ESP32-C2 Name | ESP32-C2 Pin | Function               |
| -------------- | ------------- | ------------- | ------------ | ---------------------- |
| UART TX        | PA2           | UART RX       | MTCK/GPIO6   | UART                   |
| UART RX        | PA3           | UART TX       | MTDO/GPIO7   | UART                   |
| Enable         | PA0           | CHIP_EN       | CHIP_EN      | ESP32-C2 enable        |

#### Interfaces

|  Module  |                        Interfaces                        |
| :------: | :------------------------------------------------------: |
| RAK11161 | UART2 (Default for AT command and FW update for STM32WL) |

#### Pin Definition

> **Image:** RAK11161 module pinout diagram GPIO headers

> **Image:** RAK11161 module pinout diagram flashing and debug headers

##### STM32WLE5 pin headers

- **ST_GPIO Column 1 (at PCB edge)**

| **Pin No.** | **Name** | **Type** | **Description**    |
| ----------- | -------- | -------- | ------------------ |
| 1           | NSS      | SPI      | PA4 SPI select     |
| 2           | SCK      | SPI      | PA5 SPI Clock      |
| 3           | MISO     | SPI      | PA6 SPI MISO       |
| 4           | MOSI     | SPI      | PA7 SPI MOSI       |
| 5           | PA8      | I/O      | STM32 GPIO         |
| 6           | PA10     | I/O      | STM32 GPIO         |
| 7           | SDA      | I2C      | PA11 I2C Data      |
| 8           | SCL      | I2C      | PA12 I2C Clock     |
| 9           | GND      | POWER    | Ground connections |

- **ST_GPIO Column 2**

| **Pin No.** | **Name** | **Type** | **Description**      |
| ----------- | -------- | -------- | -------------------- |
| 1           | PB5      | I/O      | STM32 GPIO           |
| 2           | PA15     | I/O      | STM32 GPIO           |
| 3           | PA1      | I/O      | STM32 GPIO           |
| 4           | PB4      | I/O      | STM32 GPIO           |
| 5           | PB3      | I/O      | STM32 GPIO           |
| 6           | PA9      | I/O      | STM32 GPIO           |
| 7           | PB2      | I/O      | STM32 GPIO           |
| 8           | PB12     | I/O      | STM32 GPIO           |
| 9           | VCC      | POWER    | VDD - Voltage Supply |

##### ESP8684 pin headers

| **Pin No.** | **Name** | **Type** | **Description** |
| ----------- | -------- | -------- | --------------- |
| 1           | IO0      | I/O      | ESP8684 GPIO    |
| 2           | IO1      | I/O      | ESP8684 GPIO    |
| 3           | IO2      | I/O      | ESP8684 GPIO    |
| 4           | IO3      | I/O      | ESP8684 GPIO    |
| 5           | IO4      | I/O      | ESP8684 GPIO    |
| 6           | IO5      | I/O      | ESP8684 GPIO    |
| 7           | IO8      | I/O      | ESP8684 GPIO    |
| 8           | IO10     | I/O      | ESP8684 GPIO    |
| 9           | IO18     | I/O      | ESP8684 GPIO    |

:::info
The GPIO pins of the ESP8684 ***cannot*** be controlled by the STM32WLE5 directly.
:::

##### STM32WLE5 debug pin headers ST_DEBUG

| **Pin No.** | **Name** | **Type** | **Description**       |
| ----------- | -------- | -------- | --------------------- |
| 1           | VCC      | POWER    | VDD - Voltage Supply  |
| 2           | DIO      | SWD IO   | SWD/JLIN/STLink data  |
| 3           | DCK      | SWD CLK  | SWD/JLIN/STLink clock |
| 4           | GND      | POWER    | Ground connections    |
| 5           | RESET    |          | STM32WLE5 reset       |

##### STM32WLE5 debug/programming pin headers ST_UART2

| **Pin No.** | **Name** | **Type** | **Description**      |
| ----------- | -------- | -------- | -------------------- |
| 1           | ST_BOOT  |          | STM32 BOOT0 pin      |
| 2           | VCC      | POWER    | VDD - Voltage Supply |
| 3           | RX2      | UART     | STM32 UART RX        |
| 4           | TX2      | UART     | STM32 UART TX        |
| 5           | GND      | POWER    | Ground connections   |

##### ESP8684 debug/programming pin headers ESP_DEBUG

| **Pin No.** | **Name** | **Type** | **Description**      |
| ----------- | -------- | -------- | -------------------- |
| 1           | VCC      | POWER    | VDD - Voltage Supply |
| 2           | TX       | UART     | ESP8684 UART TX      |
| 3           | RX       | UART     | ESP8684 UART RX      |
| 4           | GND      | POWER    | Ground connections   |
| 5           | ESP_BOOT |          | ESP8684 Boot pin     |

#### Schematics

> **Image:** RAK11161 schematics

#### RF Characteristics

##### LoRa Transceiver

The RAK11161 module supports many LoRaWAN bands as shown in the table below.

| Module | Region | Frequency |
| --- | --- | --- |
| RAK11161 (H) | Europe | EU868 |
| RAK11161 (H) | North America | US915 |
| RAK11161 (H) | Australia | AU915 |
| RAK11161 (H) | Korea | KR920 |
| RAK11161 (H) | Asia | AS923-1/2/3/4 |
| RAK11161 (H) | India | IN865 |
| RAK11161 (H) | Russia | RU864 |

###### TX Power

Transmitter output power, programmable up to +22 dBm.

###### RX Sensitivity

- -124 dBm for LoRa（BW = 125 kHz, SF = 7 ）
- -121 dBm for LoRa (BW = 250 kHz, SF = 7)
- –137 dBm for LoRa (BW = 125 kHz, SF = 12)
- –134 dBm for LoRa（BW = 250 kHz, SF = 12）

##### WiFi

###### Operating Frequencies

2412\~2484 MHz

###### TX Power

| Rate                  | Type (dBm) |
| --------------------- | --------------- |
| 802.11b, 1 Mbps  | 21.5            |
| 802.11b, 11 Mbps | 21.5            |
| 802.11g, 6 Mbps  | 21.5            |
| 802.11g, 54 Mbps | 19.5            |
| 802.11n, HT20, MCS0   | 21.0            |
| 802.11n, HT20, MCS7   | 19.0            |

###### RX Sensitivity

| Rate                  | Type (dBm) |
| --------------------- | --------------- |
| 802.11b, 1 Mbps  | -99.0           |
| 802.11b, 11 Mbps | -90.0           |
| 802.11g, 6 Mbps  | -94.0           |
| 802.11g, 54 Mbps | -77.0           |
| 802.11n, HT20, MCS0   | -92.5           |
| 802.11n, HT20, MCS7   | -74.0           |

##### Bluetooth

###### Operating Frequencies

2402\~2480 MHz

###### TX Power

| Rate                  | Type (dBm) |
| --------------------- | --------------- |
| 802.11b, 1 Mbps  | 21.5            |
| 802.11b, 11 Mbps | 21.5            |
| 802.11g, 6 Mbps  | 21.5            |
| 802.11g, 54 Mbps | 19.5            |
| 802.11n, HT20, MCS0   | 21.0            |
| 802.11n, HT20, MCS7   | 19.0            |

###### RX Sensitivity

| Rate                  | Type (dBm) |
| --------------------- | --------------- |
| 802.11b, 1 Mbps  | -99.0           |
| 802.11b, 11 Mbps | -90.0           |
| 802.11g, 6 Mbps  | -94.0           |
| 802.11g, 54 Mbps | -77.0           |
| 802.11n, HT20, MCS0   | -92.5           |
| 802.11n, HT20, MCS7   | -74.0           |

#### Electrical Characteristics

##### Operating Voltage

| Feature | Minimum | Typical | Maximum |   Unit    |
| :-----: | :-----: | :-----: | :-----: | :-------: |
|   VDD   |   3.0   |   3.3   |   3.6   | Volts (V) |

##### Operating Current

The current consumption measurements are taken with a 3.3 V supply at 25° C of ambient
temperature .

|  Work Mode   |              Condition               | Peak Current | Unit  |
| :----------: | :----------------------------------: | :----------: | :---: |
|   WiFi TX    | 802.11b, 1 Mbps, @ 22 dBm  |     370      |  mA   |
|              | 802.11g, 54 Mbps, @ 20 dBm |     320      |  mA   |
|              |  802.11n, HT20, MCS7, @ 19 dBm  |     300      |  mA   |
|   WiFi RX    |          802.11b/g/n, HT20           |      65      |  mA   |
| Bluetooth TX |     Bluetooth LE @ 20.0 dBm     |     320      |  mA   |
|              |     Bluetooth LE @ 9.0 dBm      |     190      |  mA   |
|              |    Bluetooth LE @ –15.0 dBm     |     150      |  mA   |
| Bluetooth RX |             Bluetooth LE             |      62      |  mA   |
|   Lora TX    |   +22 dBm @ 868\~915 MHz   |     120      |  mA   |
|              |   +20 dBm @ 868\~915 MHz   |    107.5     |  mA   |
|              |   +17 dBm @ 868\~915 MHz   |      98      |  mA   |
|              |   +14 dBm @ 868\~915 MHz   |      92      |  mA   |
|   Lora RX    |          LoRa 125 kHz           |     5.46     |  mA   |

##### Sleep Current

The current consumption measurements are taken with a 3.3 V supply at 25° C of ambient
temperature. ESP8684 disabled.

|       Feature       |              Condition               | Maximum | Unit  |
| :-----------------: | :----------------------------------: | :-----: | :---: |
| Current Consumption | Supply current with ESP8684 disabled |   ~6    |  μA   |

#### Mechanical Characteristics

##### Module Dimensions

> **Image:** RAK11161 board dimension

> **Image:** RAK11161 pinheaders

#### Environmental Characteristics

##### Operating Temperature

|        Feature        | Minimum | Typical | Maximum |   Unit   |
| :-------------------: | :-----: | :-----: | :-----: | :------: |
| Operating Temperature |   -40   |   25    |   85    | ° C |

##### Storage Temperature

|       Feature       | Minimum | Typical | Maximum |   Unit   |
| :-----------------: | :-----: | :-----: | :-----: | :------: |
| Storage Temperature |   -40   |    -    |   85    | ° C |

### Firmware

Download the latest RAK11161 WisDuo LPWAN Module firmware provided below. RAK11161 (L) and RAK11161 (H) use the same firmware and it will automatically detect the variant of the module being used.

| Model           | Version                                                         | Source                                                                                                            |
| --------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| RAK11161 (.bin) | RUI3 Application Code only (default baudrate = 115200)          | <a href="https://downloads.rakwireless.com/RUI/RUI3/Image/RAK11160_latest.bin" target="_blank">Download</a>       |
| RAK11161 (.hex) | RUI3 Bootloader and Application Code(default baudrate = 115200) | <a href="https://downloads.rakwireless.com/RUI/RUI3/Image/RAK11160_latest_final.hex" target="_blank">Download</a> |

### Certification

:::tip Note
For CE and FCC certifications we provide an AT command guide.    
You can find it in our <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/certification-guide" target="_blank">RUI3 documentation</a> or get it from our <a href="https://downloads.rakwireless.com/#RUI/RUI3/Certification%20Guide/" target="_blank">Download Center</a>.    
::: 

