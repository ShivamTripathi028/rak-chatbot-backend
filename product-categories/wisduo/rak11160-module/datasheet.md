---
title: RAK11160 WisDuo LoRaWAN BLE WiFi Module Specs & Datasheet
description: Access the RAK11160 datasheet for comprehensive specs, featuring STM32WLE5 LoRa transceiver, ESP8684 WiFi/BLE, ultra-low power, and long-range connectivity.
image: https://images.docs.rakwireless.com/wisduo/rak11160-module/rak11160-module.png
keywords:
  - rak11160
  - wisduo
  - lorawan module
  - lorawan ble wifi module specs
  - espressif esp8684
  - stm32wle5 lora module with ble and wifi
  - ble 5 lora module
  - long range low power mcu
  - rak11160 datasheet
  - rak1110 specs
  - rak11160 specs
  - wisduo rak11160 specs
  - esp8684 lora module specs
tags:
  - rak11160
  - datasheet
  - wisduo
sidebar_label: Datasheet
slug: /product-categories/wisduo/rak11160-module/datasheet/
date: 2025-04-24
---

# RAK11160 WisDuo LoRaWAN + BLE + WiFi Module Datasheet

## Overview

### Description

The RAK11160 is a low-power, long-range LoRaWAN module based on the STM32WLE5 MCU with integrated LoRa transceiver. It uses an Espressif ESP8684 co-processor to support Bluetooth 5.0 (Bluetooth Low Energy) and WiFi connectivity. Compliant with LoRaWAN 1.0.4 specifications (Classes A, B, and C), the module also supports LoRa point-to-point (P2P) communication, facilitating the quick implementation of customized LoRa networks. With its three RF communication capabilities—LoRa, BLE, and WiFi—this module is well-suited for various IoT applications, including home automation, sensor networks, building automation, and other IoT network applications.

By default, RAK11160 runs on RUI3 (RAKwireless Unified Interface) firmware, allowing standalone operation with custom firmware development via Arduino-compatible RUI3 APIs. Sensors and other external peripherals can be interfaced directly, eliminating the need for an additional MCU. Alternatively, the RAK11160 can be interfaced with an external host MCU using AT commands via UART.

:::tip NOTE
There are two variants available for the RAK11160 Module:

(1) With MHF4 IPEX connector to connect external antennas

(2) No IPEX connector but with RF pinout to connect custom antenna
:::

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
- Easy-to-use AT Command set STM32WLE5 and LoRa settings via UART interface
- Espressif AT command to set ESP8684 WiFi and BLE settings via UART interface (same as for STM32WLE5)
- I/O ports: UART/I2C/SPI/ADC/GPIO
- Long-range: greater than 10 km with optimized antenna
- Ultra-low-power consumption of ~2.8 μA in sleep mode (ESP8684 powered down)
- **Supply Voltage**: 1.8 V ~ 3.6 V
- **Temperature range**: -40° C ~ 85° C

## Specifications

### Overview

#### Block Diagram

> **Image:** RAK11160 system block diagram

### Hardware

The hardware specification is categorized into three parts: RF, electrical, and mechanical parameters. These include tabular data of the functionalities and standard values for the RAK11160 WisDuo LPWAN Module.

#### Internal Connections Between STM32WLE5 MCU and ESP32-C2 MCU

| STM32WLE5 Name | STM32WLE5 Pin | ESP32-C2 Name | ESP32-C2 Pin | Function               |
| -------------- | ------------- | ------------- | ------------ | ---------------------- |
| UART TX        | PA2           | UART RX       | MTCK/GPIO6   | UART                   |
| UART RX        | PA3           | UART TX       | MTDO/GPIO7   | UART                   |
| Enable         | PA0           | CHIP_EN       | CHIP_EN      | ESP32-C2 enable        |

#### Interfaces

|  Module  |                  Interfaces                  |
| :------: | :------------------------------------------: |
| RAK11160 | UART2 (Default for AT command and FW update) |

#### Pin Definition

> **Image:** RAK11160 module pinout diagram

:::warning
When using `RF_LoRa`, `RF_WIFI` pins for antenna and not the IPEX connector variant, there are design considerations to make sure optimum RF performance.

- RF traces must be away from interference (switching nodes of DC-DC supplies, high-current/voltage pulses from controllers of inductive loads like motors, signal generators, etc.).
- RF traces must have 50 ohm impedance. It is advisable to use an impedance simulation software tool to achieve this requirement.
- If using an external antenna connector, place it close to the LoRa RF and BLE RF pins.
- Ground plane optimization is critical for certain antenna types like monopoles.
- The GND trace used for the RF return path must be directly connected to the GND plane and not treated as a thermal relief.
- It is recommended that RF traces be routed in curves, not sharp 90 degree angles.

In addition, with our commitment to making IoT easy, we offer dedicated service for <a href="https://store.rakwireless.com/products/antenna-rf-design-service-including-pcb-design-tuning-matching-and-rf-test" target="_blank">Antenna RF Design which includes PCB design, tuning, matching and RF testing</a>.
:::

| **Pin No.** | **Name**               | **Type** | **Description**                                                             |
| ----------- | ---------------------- | -------- | --------------------------------------------------------------------------- |
| 1           | VDD_ST                 | POWER    | VDD - Voltage Supply STM32                                                  |
| 2           | GND                    | POWER    | Ground connections                                                          |
| 3           | ST_PA8                 | I/O      | STM32 GPIO                                                                  |
| 4           | ST_PA9                 | I/O      | STM32 GPIO                                                                  |
| 5           | ST_RST                 |          | STM32 MCU Reset (nRST)                                                      |
| 6           | ST_BOOT0               |          | STM32 BOOT0 pin                                                             |
| 7           | ST_PB2                 | I/O      | STM32 GPIO                                                                  |
| 8           | ST_PB12                | I/O      | STM32 GPIO                                                                  |
| 9           | ST_PA10                | I/O      | STM32 GPIO                                                                  |
| 10          | ST_PA11/IST_I2C2_SDA   | I/O      | GPIO and I2C2 (SDA)                                                         |
| 11          | ST_PA11/IST_I2C2_SDL   | I/O      | GPIO and I2C2 (SDL)                                                         |
| 12          | ST_PA13/ST_SWDIO       | I/O      | Jlink/SW DIO                                                                |
| 13          | ST_PA14/ST_SWCLK       | I/O      | Jlink/SW CLK                                                                |
| 14          | ST_PA15                | I/O      | STM32 GPIO                                                                  |
| 15          | GND                    | POWER    | Ground connections                                                          |
| 16          | WIFI_Extern_Ant        | RF       | WiFI/BLE RF Port (only available on **RAK11160 NO-IPEX connector variant**) |
| 17          | GND                    | POWER    | Ground connections                                                          |
| 18          | VDD_ESP                | POWER    | VDD - Voltage Supply ESP8684                                                |
| 19          | ESP_GPIO0              | I/O      | ESP8684 GPIO                                                                |
| 20          | ESP_GPIO1              | I/O      | ESP8684 GPIO                                                                |
| 21          | ESP_GPIO2              | I/O      | ESP8684 GPIO                                                                |
| 22          | ESP_GPIO3              | I/O      | ESP8684 GPIO                                                                |
| 23          | GND                    | POWER    | Ground connections                                                          |
| 24          | ESP_GPIO5              | I/O      | ESP8684 GPIO                                                                |
| 25          | ESP_GPIO4              | I/O      | ESP8684 GPIO                                                                |
| 26          | ESP_GPIO8              | I/O      | ESP8684 GPIO                                                                |
| 27          | ESP_GPIO9              | I/O      | ESP8684 GPIO                                                                |
| 28          | ESP_GPIO10             | I/O      | ESP8684 GPIO                                                                |
| 29          | ESP_GPIO18             | I/O      | ESP8684 GPIO                                                                |
| 30          | ESP_GPIO19/ESP_UART_RX | I/O      | ESP8684 Debug UART RX                                                       |
| 31          | ESP_GPIO20/ESP_UART_TX | I/O      | ESP8684 Debug UART TX                                                       |
| 32          | ST_PB3                 | I/O      | STM32 GPIO                                                                  |
| 33          | ST_PB4                 | I/O      | STM32 GPIO                                                                  |
| 34          | ST_PB5                 | I/O      | STM32 GPIO                                                                  |
| 35          | ST_PA1                 | I/O      | STM32 GPIO                                                                  |
| 36          | GND                    | POWER    | Ground connections                                                          |
| 37          | GND                    | POWER    | Ground connections                                                          |
| 38          | LoRa_Extern_Ant        | RF       | LORa RF Port (only available on **RAK11160 NO-IPEX connector variant**)     |
| 39          | GND                    | POWER    | Ground connections                                                          |
| 40          | ST_PA2/ST_UART2_TX     | I/O      | STM32 UART TX                                                               |
| 41          | ST_PA3/ST_UART2_RX     | I/O      | STM32 UART RX                                                               |
| 42          | ST_PA4/ST_NSS          | I/O      | STM32 SPI NSS                                                               |
| 43          | ST_PA5/ST_SCK          | I/O      | STM32 SPI CLK                                                               |
| 44          | ST_PA6/ST_MISO         | I/O      | STM32 SPI MISO                                                              |
| 45          | ST_PA7/ST_MOSI         | I/O      | STM32 SPI MOSI                                                              |

#### RF Characteristics

##### LoRa Transceiver

The RAK11160 module supports the LoRaWAN bands, as shown in the table below. When buying an RAK11160 module, pay attention to specifying the correct core module, RAK11160 H/L, for your region. **H** denotes high-frequency regions and **L** denotes low-frequency regions.

| Module | Region | Frequency |
| --- | --- | --- |
| RAK11160 (L) | Europe | EU433 |
| RAK11160 (L) | China | CN470 |
| RAK11160 (H) | Europe | EU868 |
| RAK11160 (H) | North America | US915 |
| RAK11160 (H) | Australia | AU915 |
| RAK11160 (H) | Korea | KR920 |
| RAK11160 (H) | Asia | AS923-1/2/3/4 |
| RAK11160 (H) | India | IN865 |
| RAK11160 (H) | Russia | RU864 |

###### TX Power

Transmitter output power, programmable up to +22 dBm.

###### RX Sensitivity

- -124 dBm for LoRa（BW = 125 kHz, SF = 7 ）
- -121 dBm for LoRa (BW = 250 kHz, SF = 7)
- –137 dBm for LoRa (BW = 125 kHz, SF = 12)
- –134 dBm for LoRa（BW = 250 kHz, SF = 12）

##### WiFi

###### Operating Frequencies

2412 ~ 2484 MHz

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

2402 ~ 2480 MHz

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
|   Lora TX    |  +22 dBm @ 868 ~ 915 Mhz   |     120      |  mA   |
|              |  +20 dBm @ 868 ~ 915 Mhz   |    107.5     |  mA   |
|              |  +17 dBm @ 868 ~ 915 Mhz   |      98      |  mA   |
|              |  +14 dBm @ 868 ~ 915 Mhz   |      92      |  mA   |
|   Lora RX    |          LoRa 125 kHz           |     5.46     |  mA   |

##### Sleep Current

The current consumption measurements are taken with a 3.3 V supply at 25° C of ambient
temperature. ESP8684 disabled.

|       Feature       |                 Condition                  | Maximum | Unit  |
| :-----------------: | :----------------------------------------: | :-----: | :---: |
| Current Consumption | Supply current in Stop 1 mode RTC disabled |   2.8   |  μA   |

#### Mechanical Characteristics

##### Module Dimensions

> **Image:** RAK11160 board dimension

##### Layout Recommendation

> **Image:** RAK11160 PCB footprint and recommendations

#### Environmental Characteristics

##### Operating Temperature

|        Feature        | Minimum | Typical | Maximum |   Unit   |
| :-------------------: | :-----: | :-----: | :-----: | :------: |
| Operating Temperature |   -40   |   25    |   85    | ° C |

##### Storage Temperature

|       Feature       | Minimum | Typical | Maximum |   Unit   |
| :-----------------: | :-----: | :-----: | :-----: | :------: |
| Storage Temperature |   -40   |    -    |   85    | ° C |

##### Recommended Reflow Profile

> **Image:** Reflow Profile for RAK11160

Standard conditions for reflow soldering:

- Pre-heating Ramp (A) (Initial temperature: 150° C): **1 ~ 2.5° C/sec**
- Soaking Time (T2) (150 ~ 180° C): **60 ~ 100 sec**
- Peak Temperature (G): **230 ~ 250° C**
- Reflow Time (T3) (> 220° C): **30 ~ 60 sec**
- Ramp-up Rate (B): **0 ~ 2.5° C/sec**
- Ramp-down Rate (C): **1 ~ 3° C/sec**

### Firmware

Download the latest RAK11160 WisDuo LPWAN Module firmware provided below. RAK11160 (L) and RAK11160 (H) use the same firmware and it will automatically detect the variant of the module being used.

| Model           | Version                                                         | Source                                                                                                            |
| --------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| RAK11160 (.bin) | RUI3 Application Code only (default baudrate = 115200)          | <a href="https://downloads.rakwireless.com/RUI/RUI3/Image/RAK11160_latest.bin" target="_blank">Download</a>       |
| RAK11160 (.hex) | RUI3 Bootloader and Application Code(default baudrate = 115200) | <a href="https://downloads.rakwireless.com/RUI/RUI3/Image/RAK11160_latest_final.hex" target="_blank">Download</a> |

### Certification

### Certifications
- **CE:** https://downloads.rakwireless.com/LoRa/RAK11160/Certification/RAK11160_CE_Certification.pdf
- **FCC:** https://downloads.rakwireless.com/LoRa/RAK11160/Certification/RAK11160_FCC_Certification.pdf
- **ISED:** https://downloads.rakwireless.com/LoRa/RAK11160/Certification/RAK11160_ISED_Certification.pdf

:::tip Note
For CE and FCC certifications we provide an AT command guide.    
You can find it in our <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/certification-guide" target="_blank">RUI3 documentation</a> or get it from our <a href="https://downloads.rakwireless.com/#RUI/RUI3/Certification%20Guide/" target="_blank">Download Center</a>.    
::: 

### Certifications
- **CE:** https://downloads.rakwireless.com/LoRa/RAK11160/Certification/RAK11160_CE_Certification.pdf

