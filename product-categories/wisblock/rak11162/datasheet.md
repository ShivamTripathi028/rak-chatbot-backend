---
slug: /product-categories/wisblock/rak11162/datasheet/
title: RAK11162 WisBlock LoRaWAN Module Datasheet | Specs & Features
description: Explore the WisBlock RAK11162 LoRaWAN & WiFi/BLE module datasheet. Get detailed specs on STM32WLE5 LoRa transceiver, ESP8684 Wi-Fi/BLE, power consumption, and RF performance.
image: https://images.docs.rakwireless.com/wisblock/rak11162/rak11162.png
keywords:
  - rak11162 module
  - rak11162 datasheet
  - lorawan module datasheet
  - lorawan ble wifi module specs
  - ble 5 module specs
  - ble 5 module specs
  - wifi transceiver
  - stm32wle5 mcu
  - esp32-c2 mcu
  - lorawan module for iot
  - stm32wle5 lorawan development board
  - esp32-c2 lorawan development board
  - lora wireless module
  - low power mcu
  - lora p2p communiation
  - low power consumption modules
  - triple rf iot lorawan module
tags:
  - rak11162
  - datasheet
  - wisblock
sidebar_label: Datasheet
date: 2025-05-23
---

# RAK11162 WisBlock LoRaWAN Module Datasheet

## Overview

### Description

The **RAK11162** is a WisBlock Core module for RAK **WisBlock**. It extends the **WisBlock** series with a low power STM32WLE MCU that supports LoRa and a ESP8684 co-processor for Bluetooth 5.0 (Bluetooth Low Energy) and Wi-Fi. Compliant with LoRaWAN 1.0.4 specifications (Classes A, B, and C), the module also supports LoRa point-to-point (P2P) communication, facilitating the quick implementation of customized LoRa networks.

With its three RF communication capabilities, LoRa, BLE, and Wi-Fi, this module is well-suited for various IoT applications, including home automation, sensor networks, building automation, and other IoT network applications.

By default, RAK11162 runs on RUI3 (RAKwireless Unified Interface) firmware, allowing standalone operation with custom firmware development via Arduino-compatible RUI3 APIs. Sensors and other external peripherals can be interfaced directly, eliminating the need for an additional MCU.

### Features

- Based on **STM32WLE5**
	- ARM 32-bit Cortex – M4
	- 256 kB Flash and 64 kB SRAM
	- **LoRaWAN 1.0.4** specification compliant
	- **Supported bands**: EU433, CN470, IN865, EU868, AU915, US915, KR920, RU864, and AS923-1/2/3/4
	- LoRaWAN Activation by OTAA/ABP
	- LoRa Point-to-Point (P2P) communication
	- Transmitter output power, programmable up to +22 dBm
	– 137 dBm for LoRa (BW = 125 kHz, SF = 12)
	- TCXO crystal
- Wi-Fi modem processor based on **Espressif ESP8684**
	- 32-bit RISC-V single-core processor, up to 120 MHz
	- 576 KB ROM
	- 2 MB Flash
	- 272 kB SRAM
	- BLE 5.0 support
		- Bluetooth LE: Bluetooth 5.3 certified
		- High power mode (20 dBm)
		- Speed: 125 Kbps, 500 Kbps, 1 Mbps, 2 Mbps
	- Wi-Fi support
		- Complies with IEEE 802.11b/g/n
		- Supports 20 MHz bandwidth in 2.4 GHz band
		- 1T1R mode with data rate up to 72.2 Mbps
- Custom firmware using Arduino via RUI3 API
- Easy-to-use AT Command set STM32WLE5 and LoRa settings via UART interface
- Espressif AT command to set ESP8684 Wi-Fi and BLE settings via UART interface (same as for STM32WLE5)
- I/O ports: UART/I2C/SPI/ADC/GPIO
- Long-range: greater than 10 km with optimized antenna
- Ultra-low-power consumption of ~2.8 μA in sleep mode (ESP8684 powered down)
- **Supply Voltage**: 1.8 V ~ 3.6 V
- **Temperature range**: -40° C ~ 85° C

## Specifications

### Overview

The overview covers the RAK11162 board overview and the mounting mechanics of the board into the base board.

#### Board Overview

> **Image:** RAK11162 internal system block diagram

#### Mounting Sketch

The RAK11162 module is designed to work with the RAK19007 base board. **Figure 2** shows how a RAK11162 module should be mounted on top of the RAK19007.

> **Image:** RAK11162 mounting sketch

### Hardware

The hardware specification is categorized into three parts: RF, electrical, and mechanical parameters. These include tabular data of the functionalities and standard values for the RAK11162 WisBlock LPWAN Module.

:::warning
Due to the STM32WLE5's limitation of only two UART interfaces, no UART is available for the WisBlock Sensor and IO slots. As a result, WisBlock modules that rely on UART communication are not compatible with the RAK11162 Core module. Additionally, because of limited available GPIOs, the second I2C interface used by some WisBlock modules is not accessible through the IO slot.
:::

#### Chipset
| Vendor    | Part Number |
|-----------|-------------|
| STM       | STM32WLE5   |
| Espressif | ESP8684     |

#### Internal Connections Between STM32WLE5 MCU and ESP32-C2 MCU

| STM32WLE5 Name | STM32WLE5 Pin | ESP32-C2 Name | ESP32-C2 Pin | Function               |
| -------------- | ------------- | ------------- | ------------ | ---------------------- |
| UART TX        | PA2           | UART RX       | MTCK/GPIO6   | UART                   |
| UART RX        | PA3           | UART TX       | MTDO/GPIO7   | UART                   |
| Enable         | PA0           | CHIP_EN       | CHIP_EN      | ESP32-C2 enable        |

#### RF Characteristics

##### LoRa Transceiver

The RAK11162 WisBlock Core module supports the LoRaWAN bands, as shown in the table below. When buying an RAK11162 module, pay attention to specifying the correct core module, RAK11162 H/L, for your region. **H** denotes high-frequency regions and **L** for low-frequency regions.

| Module | Region | Frequency |
| --- | --- | --- |
| RAK11162 (L) | Europe | EU433 |
| RAK11162 (L) | China | CN470 |
| RAK11162 (H) | Europe | EU868 |
| RAK11162 (H) | North America | US915 |
| RAK11162 (H) | Australia | AU915 |
| RAK11162 (H) | Korea | KR920 |
| RAK11162 (H) | Asia | AS923-1/2/3/4 |
| RAK11162 (H) | India | IN865 |
| RAK11162 (H) | Russia | RU864 |

###### TX Power

Transmitter output power, programmable up to +22 dBm.

###### RX Sensitivity

- -124 dBm for LoRa（BW = 125 kHz, SF = 7 ）
- -121 dBm for LoRa (BW = 250 kHz, SF = 7)
- –137 dBm for LoRa (BW = 125 kHz, SF = 12)
- –134 dBm for LoRa（BW = 250 kHz, SF = 12）

##### Wi-Fi

###### Operating Frequencies

2412 ~ 2484 MHz

###### TX Power

| Rate                  | Type (dBm) |
|-----------------------|-----------------|
| 802.11b, 1 Mbps  | 21.5            |
| 802.11b, 11 Mbps | 21.5            |
| 802.11g, 6 Mbps  | 21.5            |
| 802.11g, 54 Mbps | 19.5            |
| 802.11n, HT20, MCS0   | 21.0            |
| 802.11n, HT20, MCS7   | 19.0            |

###### RX Sensitivity

| Rate                  | Type (dBm) |
|-----------------------|-----------------|
| 802.11b, 1 Mbps  | -99.0           |
| 802.11b, 11 Mbps | -90.0           |
| 802.11g, 6 Mbps  | -94.0           |
| 802.11g, 54 Mbps | -77.0           |
| 802.11n, HT20, MCS0   | -92.5           |
| 802.11n, HT20, MCS7   | -74.0           |

##### Bluetooth

###### Operating Frequencies

2402 ~ 2480 MHz

###### TX Power

| Rate                  | Type (dBm) |
|-----------------------|-----------------|
| 802.11b, 1 Mbps  | 21.5            |
| 802.11b, 11 Mbps | 21.5            |
| 802.11g, 6 Mbps  | 21.5            |
| 802.11g, 54 Mbps | 19.5            |
| 802.11n, HT20, MCS0   | 21.0            |
| 802.11n, HT20, MCS7   | 19.0            |

###### RX Sensitivity

| Rate                  | Type (dBm) |
|-----------------------|-----------------|
| 802.11b, 1 Mbps  | -99.0           |
| 802.11b, 11 Mbps | -90.0           |
| 802.11g, 6 Mbps  | -94.0           |
| 802.11g, 54 Mbps | -77.0           |
| 802.11n, HT20, MCS0   | -92.5           |
| 802.11n, HT20, MCS7   | -74.0           |

#### Electrical Characteristics

##### Operating Voltage

| Feature | Minimum | Typical | Maximum |   Unit    |
|:-------:|:-------:|:-------:|:-------:|:---------:|
|   VDD   |   3.0   |   3.3   |   3.6   | Volts (V) |

##### Operating Current

The current consumption measurements are taken with a 3.3 V supply at 25° C of ambient temperature.

|  Work Mode   |              Condition               | Peak Current | Unit |
|:------------:|:------------------------------------:|:------------:|:----:|
|   Wi-Fi TX   | 802.11b, 1 Mbps, @ 22 dBm  |     370      |  mA  |
|              | 802.11g, 54 Mbps, @ 20 dBm |     320      |  mA  |
|              |  802.11n, HT20, MCS7, @ 19 dBm  |     300      |  mA  |
|   Wi-Fi RX   |          802.11b/g/n, HT20           |      65      |  mA  |
| Bluetooth TX |     Bluetooth LE @ 20.0 dBm     |     320      |  mA  |
|              |     Bluetooth LE @ 9.0 dBm      |     190      |  mA  |
|              |    Bluetooth LE @ –15.0 dBm     |     150      |  mA  |
| Bluetooth RX |             Bluetooth LE             |      62      |  mA  |
|   Lora TX    |  +22 dBm @ 868 ~ 915 Mhz   |     120      |  mA  |
|              |  +20 dBm @ 868 ~ 915 Mhz   |    107.5     |  mA  |
|              |  +17 dBm @ 868 ~ 915 Mhz   |      98      |  mA  |
|              |  +14 dBm @ 868 ~ 915 Mhz   |      92      |  mA  |
|   Lora RX    |          LoRa 125 kHz           |     5.46     |  mA  |

##### Sleep Current

The current consumption measurements are taken with a 3.3 V supply at 25° C of ambient temperature. ESP8684 disabled.

|       Feature       |                 Condition                  | Maximum | Unit |
|:-------------------:|:------------------------------------------:|:-------:|:----:|
| Current Consumption | Supply current in stop 1 mode RTC disabled |   2.8   |  μA  |

##### Schematic Diagram

:::warning
Due to the STM32WLE5's limitation of only two UART interfaces, no UART is available for the WisBlock Sensor and IO slots. As a result, WisBlock modules that rely on UART communication are not compatible with the RAK11162 Core module. Additionally, because of limited available GPIOs, the second I2C interface used by some WisBlock modules is not accessible through the IO slot.
:::

> **Image:** RAK11162 WisDuo Module

**Core Module**: The breakout module itself has a RAK11160 at its core, and it shows the core module pin and connection information.

> **Image:** RAK11162 WisBlock Core connector

**WisConnector**: The breakout module allows the RAK4630 stamp module pinout to be transferred by the board-to-board WisConnector.

**WisConnector Pin Order**: The pin order of the WisConnector is located in the bottom layer of the module.

> **Image:** RAK11162 programming connectors

**SWD Interface and UART Interface**: The breakout module exposes two programming interfaces.
- SWD debug and flash interface for the STM32WLE5.
- UART debug and flash interface for the ESP8684.

> **Image:** RAK11162 USB

**USB**: The breakout module has a USB interface that is connected to the STM32WLE5 UART2 for AT commands and flashing of STM32WLE5 firmware over USB.

#### Environmental Characteristics

##### Operating Temperature

|        Feature        | Minimum | Typical | Maximum |   Unit   |
|:---------------------:|:-------:|:-------:|:-------:|:--------:|
| Operating Temperature |   -40   |   25    |   85    | ° C |

##### Storage Temperature

|       Feature       | Minimum | Typical | Maximum |   Unit   |
|:-------------------:|:-------:|:-------:|:-------:|:--------:|
| Storage Temperature |   -40   |    -    |   85    | ° C |

#### Mechanical Characteristics

##### Board Dimensions

> **Image:** Mechanical Dimensions

##### WisConnector PCB Layout

> **Image:** WisConnector PCB footprint and recommendations

### Firmware

Download the latest RAK11162 WisBlock LPWAN Module firmware provided below. RAK11162 (L) and RAK11162 (H) use the same firmware and it will automatically detect the variant of the module being used.

:::info
The RAK11162 WisBlock Core module is based on the RAK11160 WisDuo LPWAN+BLE+Wi-Fi module. Therefore, the default firmware for the RAK11162 is the same with RAK11160.
:::

| Model           | Version                                                         | Source                                                                                                            |
|-----------------|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| RAK11160 (.bin) | RUI3 Application Code only (default baudrate = 115200)          | <a href="https://downloads.rakwireless.com/RUI/RUI3/Image/RAK11160_latest.bin" target="_blank">Download</a>       |
| RAK11160 (.hex) | RUI3 Bootloader and Application Code(default baudrate = 115200) | <a href="https://downloads.rakwireless.com/RUI/RUI3/Image/RAK11160_latest_final.hex" target="_blank">Download</a> |

### Certification

:::tip Note
For CE and FCC certifications we provide an AT command guide.    
You can find it in our <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/certification-guide" target="_blank">RUI3 documentation</a> or get it from our <a href="https://downloads.rakwireless.com/#RUI/RUI3/Certification%20Guide/" target="_blank">Download Center</a>.    
::: 

