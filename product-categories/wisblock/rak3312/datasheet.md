---
slug: /product-categories/wisblock/rak3312/datasheet/
title: RAK3312 WisBlock LoRaWAN Module Datasheet | Specs & Features
description: Explore the WisBlock RAK3312 LoRaWAN and WiFi/BLE module datasheet for detailed specifications on the Semtech SX1262 LoRa transceiver, ESP32-S3, power consumption, and RF performance.
image: https://images.docs.rakwireless.com/wisblock/rak3312/rak3312.png
keywords:
  - rak3312 module
  - sx1262 lora transceiver
  - esp32-s3 wifi ble
  - lorawan module for iot
  - esp32-s3 wifi ble development board
  - lorawan ble wifi module
  - low power mcu
  - lora p2p communication
  - lora wireless module
  - low power consumption modules
  - long range communication
  - triple rf iot lorawan module
tags:
  - rak3312
  - datasheet
  - wisblock
sidebar_label: Datasheet
date: 2025-05-23
---

# RAK3312 WisBlock LoRaWAN Module Datasheet

## Overview

### Description

The **RAK3312** is a low-power, long-range LoRaWAN module based on the Espressif ESP32-S3 MCU with an integrated Semtech SX1262 LoRa transceiver. It supports triple wireless connectivity with LoRa, BLE, and WiFi, making it highly versatile for a wide range of IoT applications including home automation, sensor networks, and building automation.

The module supports custom firmware development using the Arduino framework and provides multiple I/O interfaces such as UART, I2C, SPI, ADC, and GPIO. It also features an MHF4 IPEX connector for seamless integration with external antennas.

### Features

- Based on **Espressif ESP32-S3**
	- Xtensa® 32-bit LX7 dual-core microprocessor
	- 16 MB Flash
	- 512 kB SRAM
	- 512 kB RAM
	- 8 MB PSRAM
	- 16 kB RTC SRAM
- LoRa transceiver **Semtech SX1262**
	- LoRa and LoRaWAN support
	- Frequency support from 863 MHz to 928 MHz
- Compliant with the **LoRaWAN 1.0.2** (LoRaWAN **BasicModem** support in preparation)
- **Supported bands**: IN865, EU868, AU915, US915, KR920, RU864, and AS923-1/2/3/4
- LoRaWAN Activation by OTAA/ABP
- LoRa Point-to-Point (P2P) communication
- BLE 5.0 support
- WiFi support
- Custom firmware using Arduino
- I/O ports: UART/I2C/SPI/ADC/GPIO
- Long-range: greater than 10 km with optimized antenna
- **Supply Voltage**: 3.0 V\~3.6 V
- **Temperature range**: -40° C\~65° C

## Specifications

### Overview

The overview covers the RAK3312 board overview and the mounting mechanics of the board into the base board.

> **Image:** RAK3312 internal system block diagram

#### Mounting Sketch

The RAK3312 module is designed to work with the RAK19007 base board. **Figure 2** shows how a RAK3312 module should be mounted on top of the RAK19007.

> **Image:** RAK3312 mounting sketch

### Hardware

The hardware specifications are categorized into three parts: RF, electrical, and mechanical parameters. These include tables detailing functionalities and standard values for the RAK3312 WisBlock LPWAN Module.

#### Internal Connections Between ESP32-S3 MCU and SX1262 LoRa transceiver

| SX1262   | ESP32-S3 | Function               |
| -------- | -------- | ---------------------- |
| SPI_NSS  | GPIO7    | SPI select             |
| SPI_SCK  | GPIO5    | SPI clock              |
| SPI_MISO | GPIO3    | SPI Master in          |
| SPI_MOSI | GPIO6    | SPI Master out         |
| NRESET   | GPIO8    | SX1262 reset           |
| ANT_SW   | GPIO4    | SX1262 RF switch power | 
| DIO1     | GPIO47   | SX1262 DIO1            |
| BUSY     | GPIO48   | SX1262 BUSY            |

#### Interfaces

| Interfaces                                 |
| ------------------------------------------ |
| USB (Default for Serial log and FW update) |
| 2 x I2C                                    |
| 1 x UART                                   |
| 1 x SPI                                    |

#### WisBlock Pin Assignments

| WisBlock Pin | ESP32 GPIO   |
| ------------ | ------------ |
| WB_IO1       | GPIO21       |
| WB_IO2       | GPIO14       |
| WB_IO3       | GPIO41       |
| WB_IO4       | GPIO42       |
| WB_IO5       | GPIO38       |
| WB_IO6       | GPIO39       |
| WB_IO7       | _NA_         |
| LED_GREEN    | GPIO46       |
| LED_BLUE     | GPIO45       |
| TXD0         | _NA_         |
| RXD0         | _NA_         |
| TXD1         | U0TXD/GPIO43 |
| RXD1         | U0RXD/GPIO44 |
| I2C1_SDA     | GPIO9        |
| I2C1_SCL     | GPIO40       |
| I2C2_SDA     | GPIO17       |
| I2C2_SCL     | GPIO18       |
| SPI_CS       | GPIO12       |
| SPI_CLK      | GPIO13       |
| SPI_MOSI     | GPIO11       |
| SPI_MISO     | GPIO10       |

#### ESP32-S3 SX1262 connections

| ESP32-S3 | SX1262          |
| -------- | --------------- |
| GPIO7    | SX1262_SPI_NSS  |
| GPIO5    | SX1262_SPI_SCK  |
| GPIO6    | SX1262_SPI_MOSI |
| GPIO3    | SX1262_SPI_MISO |
| GPIO8    | SX1262_NRESET   |
| GPIO48   | SX1262_BUSY     |
| GPIO47   | SX1262_DIO1     |
| GPIO4    | SX1262_ANT_SW   |

#### RF Characteristics

##### LoRa Transceiver

The RAK3312 WisBlock Core module supports various LoRaWAN bands, as listed in the table below. When purchasing a RAK3312 module, make sure to choose the correct variant for your region:
- **RAK3312 (L)** for low-frequency regions
- **RAK3312 (H)** for high-frequency regions

| Module | Region | Frequency |
| --- | --- | --- |
| RAK3312 (L) | Europe | EU433 |
| RAK3312 (L) | China | CN470 |
| RAK3312 (H) | Europe | EU868 |
| RAK3312 (H) | North America | US915 |
| RAK3312 (H) | Australia | AU915 |
| RAK3312 (H) | Korea | KR920 |
| RAK3312 (H) | Asia | AS923-1/2/3/4 |
| RAK3312 (H) | India | IN865 |
| RAK3312 (H) | Russia | RU864 |

- **TX Power**: Transmitter output power is programmable up to +22 dBm.

- **RX Sensitivity**
  - -124 dBm for LoRa（BW = 125 kHz, SF = 7 ）
  - -121 dBm for LoRa (BW = 250 kHz, SF = 7)
  - –137 dBm for LoRa (BW = 125 kHz, SF = 12)
  - –134 dBm for LoRa（BW = 250 kHz, SF = 12）

##### WiFi

- **Operating Frequencies**: 2412\~2484 MHz

- **TX Power**

| Rate                  | Value         |
| --------------------- | ------------- |
| 802.11b, 1 Mbps  | 21.0 dBm |
| 802.11b, 11 Mbps | 21.0 dBm |
| 802.11g, 6 Mbps  | 20.5 dBm |
| 802.11g, 54 Mbps | 19.0 dBm |
| 802.11n, HT20, MCS0   | 19.5 dBm |
| 802.11n, HT20, MCS7   | 18.5 dBm |
| 802.11n, HT40, MCS0   | 19.5 dBm |
| 802.11n, HT40, MCS7   | 18.0 dBm |

- **RX Sensitivity**

| Rate                  | Value          |
| --------------------- | -------------- |
| 802.11b, 1 Mbps  | –98.4 dBm |
| 802.11b, 11 Mbps | -88.6 dBm |
| 802.11g, 6 Mbps  | –93.2 dBm |
| 802.11g, 54 Mbps | –76.5 dBm |
| 802.11n, HT20, MCS0   | –92.6 dBm |
| 802.11n, HT20, MCS7   | –74.2 dBm |
| 802.11n, HT40, MCS0   | –90.0 dBm |
| 802.11n, HT40, MCS7   | –71.4 dBm |

##### Bluetooth

- **Operating Frequencies**: 2402\~2480 MHz

- **TX Power**

| Rate                   | Value                                         |
| ---------------------- | --------------------------------------------- |
| 802.11b, 1 Mbps   | Programmable from -24 dBm to 20 dBm |
| 802.11b, 2 Mbps   | Programmable from -24 dBm to 20 dBm |
| 802.11g, 125 kbps | Programmable from -24 dBm to 20 dBm |
| 802.11g, 500 Kbps | Programmable from -24 dBm to 20 dBm |

- **RX Sensitivity**

| Rate                   | Value          |
| ---------------------- | -------------- |
| 802.11b, 1 Mbps   | –97.5 dBm |
| 802.11b, 2 Mbps   | –93.5 dBm |
| 802.11g, 125 Kbps | -94.0 dBm |
| 802.11g, 250 Kbps | -77.0 dBm |

#### Electrical Characteristics

##### Operating Voltage

| Feature | Minimum | Typical | Maximum |   Unit    |
| :-----: | :-----: | :-----: | :-----: | :-------: |
|   VDD   |   3.0   |   3.3   |   3.6   | Volts (V) |

##### Operating Current

The current consumption measurements are taken with a 3.3 V supply at an ambient temperature of 25° C.

| Work Mode |              Condition               | Peak Current | Unit  |
| :-------: | :----------------------------------: | :----------: | :---: |
|  WiFi TX  | 802.11b, 1 Mbps, @ 21 dBm  |     340      |  mA   |
|           | 802.11g, 54 Mbps, @ 19 dBm |     291      |  mA   |
|           | 802.11n, HT20, MCS7, @ 18.5 dBm |     283      |  mA   |
|           |  802.11n, HT40, MCS7, @ 18 dBm  |     286      |  mA   |
|  WiFi RX  |          802.11b/g/n, HT20           |      88      |  mA   |
|           |            802.11n, HT40             |      91      |  mA   |
|  Lora TX  |   +22 dBm @ 868\~915 Mhz   |     140      |  mA   |
|           |   +20 dBm @ 868\~915 Mhz   |    127.5     |  mA   |
|           |   +17 dBm @ 868\~915 Mhz   |     118      |  mA   |
|           |   +14 dBm @ 868\~915 Mhz   |     112      |  mA   |
|  Lora RX  |          LoRa 125 kHz           |    25.46     |  mA   |

##### Sleep Current

The current consumption measurements are taken with a 3.3 V supply at 25° C of ambient temperature.

|   Feature   |                              Condition                              | Maximum | Unit  |
| :---------: | :-----------------------------------------------------------------: | :-----: | :---: |
| Lightsleep  | VDD_SPI and WiFi are powered down, and all GPIOs are high-impedance |   241   |  μA   |
| Deepsleep 1 |            RTC memory and RTC peripherals are powered up            |    9    |  μA   |
| Deepsleep 2 |     RTC memory is powered up. RTC peripherals are powered down      |    8    |  μA   |
|  Power off  |         CHIP_PU is set to low level. The chip is shut down          |    2    |  μA   |

##### Schematic Diagram

> **Image:** RAK3312 Schematic

**WisConnector**: The breakout module enables the RAK3312 stamp module's pinout to be accessed through the board-to-board WisConnector

**WisConnector Pin Order**: The WisConnector pin order is located in the bottom layer of the module.

#### Environmental Characteristics

##### Operating Temperature

|        Feature        | Minimum | Typical | Maximum |   Unit   |
| :-------------------: | :-----: | :-----: | :-----: | :------: |
| Operating Temperature |   -40   |   25    |   85    | ° C |

##### Storage Temperature

|       Feature       | Minimum | Typical | Maximum |   Unit   |
| :-----------------: | :-----: | :-----: | :-----: | :------: |
| Storage Temperature |   -40   |    -    |   85    | ° C |

#### Mechanical Characteristics

##### Board Dimensions

> **Image:** Mechanical Dimensions

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

### Firmware

The RAK3312 does not come with default firmware. You have to develop your application based on the Arduino IDE, using the Espressif BSP. Examples of how to use LoRa, LoRaWAN, BLE, and WiFi are available in the <a href="https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK3112" target="_blank">GitHub repo.</a>

For firmware development guide, refer to <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3312/quickstart/#software-setup" target="_blank">RAK3312 Quick Start Guide</a>

