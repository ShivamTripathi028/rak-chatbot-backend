---
title: RAK3112 LoRaWAN Module with BLE & Wi-Fi Datasheet | Specs & Features
description: Access the RAK3112 datasheet for comprehensive specs, a low-power, long-range LoRaWAN module with Espressif ESP32-S3 MCU, Semtech SX1262 LoRa Transceiver.
image: https://images.docs.rakwireless.com/wisduo/rak3112-module/rak3112-module.png
keywords:
  - rak3112
  - wisduo
  - lorawan module
  - lorawan ble wifi module
  - espressif esp32-s3
  - semtech sx1262 
  - ble 5 lora module
  - long range low power mcu
tags:
  - rak3112
  - datasheet
  - wisduo
sidebar_label: Datasheet
slug: /product-categories/wisduo/rak3112-module/datasheet/
date: 2025-06-06
---

# RAK3112 WisDuo LPWAN+BLE+Wi-Fi Module Datasheet

## Overview

### Description

The RAK3112 is a low-power, long-range LoRaWAN module based on the Espressif ESP32-S3 MCU with an integrated Semtech SX1262 LoRa transceiver. Supporting LoRa, BLE, and Wi-Fi, this module is ideal for various IoT applications such as home automation, sensor networks, building automation, and other IoT network applications.

:::tip NOTE
There are two variants available for the RAK3112 Module:
1. With MHF4 IPEX connector to connect external antennas.
2. No IPEX connector but with RF pinout to connect custom antenna.
:::

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
- **LoRaWAN 1.0.2** specification compliant (LoRaWAN **BasicModem** support in preparation)
- **Supported bands**: IN865, EU868, AU915, US915, KR920, RU864, and AS923-1/2/3/4
- LoRaWAN Activation by OTAA/ABP
- LoRa Point-to-Point (P2P) communication
- BLE 5.0 support
- Wi-Fi support
- Custom firmware using Arduino
- I/O ports: UART/I2C/SPI/ADC/GPIO
- Long-range: greater than 10 km with optimized antenna
- **Supply Voltage**: 3.0 V ~ 3.6 V
- **Temperature range**: -40° C ~ 65° C

## Specifications

### Overview

#### Block Diagram

> **Image:** RAK3112 system block diagram

### Hardware

The hardware specification is categorized into three parts: RF, electrical, and mechanical parameters. These include tabular data of the functionalities and standard values for the RAK3112 WisDuo LPWAN Module.

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
|--------------------------------------------|
| USB (Default for AT command and FW update) |
| 2 x I2C                                    |
| 1 x UART                                   |
| 1 x SPI                                    |

#### Pin Definition

:::info
- GPIO33 to GPIO37 are on the stamp modules pins, but with the 16 MB Flash chip, these GPIO's are not available.
- GPIO4 is used internally and not available.
:::

> **Image:** RAK3112 module pinout diagram

| **Pin No.** | **Name**          | **Type**      | **Description**                                                         |
|-------------|-------------------|---------------|-------------------------------------------------------------------------|
| 1           | NC                | --            | Not connected                                                           |
| 2           | USB_D-            | USB           | USB -                                                                   |
| 3           | USB_D+            | USB           | USB +                                                                   |
| 4           | GPIO33 / NC*      | --            | GPIO (not available with 16MB Flash)                                    |
| 5           | GPIO34 / NC*      | --            | GPIO (not available with 16MB Flash)                                    |
| 6           | GPIO44 / UART0_RX | I/O UART      | GPIO / UART RX                                                          |
| 7           | GPIO43 / UART1_TX | I/O UART      | GPIO / UART TX                                                          |
| 8           | GPIO35 / NC*      | --            | GPIO (not available with 16MB Flash)                                    |
| 9           | GPIO36 / NC*      | --            | GPIO (not available with 16MB Flash)                                    |
| 10          | GPIO37 / NC*      | --            | GPIO (not available with 16MB Flash)                                    |
| 11          | GPIO38            | I/O           | GPIO                                                                    |
| 12          | GPIO39            | I/O           | GPIO                                                                    |
| 13          | GPIO40 / I2C1_SCL | I/O I2C       | GPIO / I2C SCL                                                          |
| 14          | GND               | POWER         | Ground connections                                                      |
| 15          | RF_WiFi           | RF            | Wi-Fi RF Port (only available on **RAK3112 NO-IPEX connector variant**) |
| 16          | GND               | POWER         | Ground connections                                                      |
| 17          | RESET             | Reset         | ESP32S3 Reset                                                           |
| 18          | GPIO41            | I/O           | GPIO                                                                    |
| 19          | GPIO42            | I/O           | GPIO                                                                    |
| 20          | VDD               | POWER         | VDD - Voltage Supply                                                    |
| 21          | VDD               | POWER         | VDD - Voltage Supply                                                    |
| 22          | GND               | POWER         | Ground connections                                                      |
| 23          | GPIO45            | I/O           | GPIO                                                                    |
| 24          | GPIO0 / Boot      | I/O Boot      | GPIO Bootloader force                                                   |
| 25          | GPIO46            | I/O           | GPIO                                                                    |
| 26          | GPIO1             | I/O           | GPIO                                                                    |
| 27          | GPIO2             | I/O           | GPIO                                                                    |
| 28          | GPIO9 / I2C1_SDA  | I/O I2C       | GPIO / I2C SDA                                                          |
| 29          | GPIO4 / NC        | I/O           | GPIO (not available)                                                    |
| 30          | GPIO10 / SPI_MISO | I/O SPI       | GPIO / SPI MISO                                                         |
| 31          | GPIO11 / SPI_MOSI | I/O SPI       | GPIO / SPI MOSI                                                         |
| 32          | GPIO12 / SPI_CS   | I/O SPI       | GPIO / SPI CS                                                           |
| 33          | GPIO13 / SPI_SCK  | I/O SPI       | GPIO / SPI SCK                                                          |
| 34          | GPIO14 / AIN1     | I/O Analog In | GPIO / Analog In                                                        |
| 35          | GND               | POWER         | Ground connections                                                      |
| 36          | GND               | POWER         | Ground connections                                                      |
| 37          | RF_LoRa           | RF            | LoRa RF Port (only available on **RAK3112 NO-IPEX connector variant**)  |
| 38          | GND               | POWER         | Ground connections                                                      |
| 39          | GPIO18 / I2C2_SCL | I/O I2C       | GPIO / I2C SCL                                                          |
| 40          | GPIO17 / I2C2_SDA | I/O I2C       | GPIO / I2C SDA                                                          |
| 41          | GPIO21 / AIN0     | I/O Analog In | GPIO / Analog In                                                        |
| 42          | GND               | I/O           | Ground connections                                                      |
| 43          | NC                | --            | Not connected                                                           |
| 44          | NC                | --            | Not connected                                                           |

:::warning
When using `RF_LoRa`, `RF_WIFI` pins for antenna and not the IPEX connector variant, there are design considerations to make sure optimum RF performance.

- RF traces must be away from interference (switching nodes of DC-DC supplies, high-current/voltage pulses from controllers of inductive loads like motors, signal generators, etc.).
- RF traces must have 50 Ω impedance. It is advisable to use an impedance simulation software tool to achieve this requirement.
- If using an external antenna connector, place it close to the LoRa RF and BLE RF pins.
- Ground plane optimization is critical for certain antenna types like monopoles.
- The GND trace used for the RF return path must be directly connected to the GND plane and not treated as a thermal relief.
- It is recommended that RF traces be routed in curves, not sharp 90 degree angles.

In addition, with our commitment to making IoT easy, we offer dedicated service for [Antenna RF Design which includes PCB design, tuning, matching and RF testing.](https://store.rakwireless.com/products/antenna-rf-design-service-including-pcb-design-tuning-matching-and-rf-test)
:::

#### RF Characteristics

##### LoRa Transceiver

The RAK3112 module supports many LoRaWAN bands as shown in the table below.

| Module | Region | Frequency |
| --- | --- | --- |
| RAK3112 (H) | Europe | EU868 |
| RAK3112 (H) | North America | US915 |
| RAK3112 (H) | Australia | AU915 |
| RAK3112 (H) | Korea | KR920 |
| RAK3112 (H) | Asia | AS923-1/2/3/4 |
| RAK3112 (H) | India | IN865 |
| RAK3112 (H) | Russia | RU864 |

###### TX Power

Transmitter output power, programmable up to +22 dBm.

###### RX Sensitivity

- -124 dBm for LoRa（BW = 125 kHz, SF = 7）
- -121 dBm for LoRa (BW = 250 kHz, SF = 7)
- -137 dBm for LoRa (BW = 125 kHz, SF = 12)
- -134 dBm for LoRa（BW = 250 kHz, SF = 12）

##### Wi-Fi

###### Operating Frequencies

2412 ~ 2484 MHz

###### TX Power

| Rate                  | Type (dBm) |
|-----------------------|-----------------|
| 802.11b, 1 Mbps  | 21.0            |
| 802.11b, 11 Mbps | 21.0            |
| 802.11g, 6 Mbps  | 20.5            |
| 802.11g, 54 Mbps | 19.0            |
| 802.11n, HT20, MCS0   | 19.5            |
| 802.11n, HT20, MCS7   | 19.0            |
| 802.11n, HT40, MCS0   | 19.5            |
| 802.11n, HT40, MCS7   | 18.0            |

###### RX Sensitivity

| Rate                  | Type (dBm) |
|-----------------------|-----------------|
| 802.11b, 1 Mbps  | –98.4           |
| 802.11b, 11 Mbps | -88.6           |
| 802.11g, 6 Mbps  | –93.2           |
| 802.11g, 54 Mbps | –76.5           |
| 802.11n, HT20, MCS0   | –92.6           |
| 802.11n, HT20, MCS7   | –74.2           |
| 802.11n, HT40, MCS0   | –90.0           |
| 802.11n, HT40, MCS7   | –71.4           |

##### Bluetooth

###### Operating Frequencies

2402 ~ 2480 MHz

###### TX Power

| Rate               | Type (dBm)                               |
|--------------------|-----------------------------------------------|
| BLE @1 Mbps   | Programmable from -24 dBm to 20 dBm |
| BLE @2 Mbps   | Programmable from -24 dBm to 20 dBm |
| BLE @125 Kbps | Programmable from -24 dBm to 20 dBm |
| BLE @500 Kbps | Programmable from -24 dBm to 20 dBm |

###### RX Sensitivity

| Rate               | Type (dBm) |
|--------------------|-----------------|
| BLE @1 Mbps   | –97.5           |
| BLE @2 Mbps   | –93.5           |
| BLE @125 Kbps | –104.5          |
| BLE @500 Kbps | –101            |

#### Electrical Characteristics

##### Operating Voltage

| Feature | Minimum | Typical | Maximum |   Unit    |
|:-------:|:-------:|:-------:|:-------:|:---------:|
|   VDD   |   3.0   |   3.3   |   3.6   | Volts (V) |

##### Operating Current

The current consumption measurements are taken with a 3.3 V supply at 25° C of ambient temperature.

| Work Mode | Condition | Peak current | Unit |
| --- | --- | --- | --- |
| Wi-Fi TX | 802.11b, 1 Mbps, @21 dBm | 340 | mA |
| Wi-Fi TX | 802.11g, 54 Mbps, @19 dBm | 291 | mA |
| Wi-Fi TX | 802.11n, HT20, MCS7, @18.5 dBm | 283 | mA |
| Wi-Fi TX | 802.11n, HT40, MCS7, @18 dBm | 286 | mA |
| Wi-Fi RX | 802.11b/g/n, HT20 | 88 | mA |
| Wi-Fi RX | 802.11n, HT40 | 91 | mA |
| Lora TX | +22 dBm@ 868 to 915Mhz | 140 | mA |
| Lora TX | +20 dBm@ 868 to 915 Mhz | 127.5 | mA |
| Lora TX | +17 dBm@ 868 to 915 Mhz | 118 | mA |
| Lora TX | +14 dBm@ 868 to 915 Mhz | 112 | mA |
| Lora RX | LoRa 125 kHz | 25.46 | mA |

##### Sleep Current

The current consumption measurements are taken with a 3.3 V supply at 25° C of ambient
temperature.

| Feature      | Condition                                                             | Maximum | Unit |
|--------------|-----------------------------------------------------------------------|---------|------|
| Light-sleep  | VDD_SPI and Wi-Fi are powered down, and all GPIOs are high-impedance. | 241     | uA   |
| Deep-sleep 1 | RTC memory and RTC peripherals are powered up.                        | 9       | uA   |
| Deep-sleep 2 | RTC memory is powered up. RTC peripherals are powered down.           | 8       | uA   |
| Power off    | CHIP_PU is set to low level. The chip is shut down.                   | 2       | uA   |

#### Mechanical Characteristics

##### Module Dimensions

> **Image:** RAK3112 board dimension

##### Layout Recommendation

> **Image:** RAK3112 PCB footprint and recommendations

#### Environmental Characteristics

##### Operating Temperature

|        Feature        | Minimum | Typical | Maximum |   Unit   |
|:---------------------:|:-------:|:-------:|:-------:|:--------:|
| Operating Temperature |   -40   |   25    |   65    | ° C |

##### Storage Temperature

|       Feature       | Minimum | Typical | Maximum |   Unit   |
|:-------------------:|:-------:|:-------:|:-------:|:--------:|
| Storage Temperature |   -40   |    -    |   85    | ° C |

##### Recommended Reflow Profile

> **Image:** Reflow Profile for RAK3112

Standard conditions for reflow soldering:

- Pre-heating Ramp (A) (Initial temperature: 150° C): **1 ~ 2.5° C/sec**
- Soaking Time (T2) (150 ~ 180° C): **60 ~ 100 sec**
- Peak Temperature (G): **230 ~ 250° C**
- Reflow Time (T3) (> 220° C): **30 ~ 60 sec**
- Ramp-up Rate (B): **0 ~ 2.5° C/sec**
- Ramp-down Rate (C): **1 ~ 3° C/sec**

#### Schematic Diagram (Minimal)

> **Image:** RAK3112 minimal schematic

### Firmware

The RAK3112 does not come with default firmware. You have to develop your application based on the Arduino IDE, using the Espressif BSP.
Examples of how to use LoRa, LoRaWAN, BLE, and WiFi are available in the [GitHub repo](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK3112)
A guide for firmware development can be found in the [RAK3112 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisduo/rak3112-module/quickstart/#software-setup)

<!--
### Certification

Work in progress -->

