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

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

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
	- 16&nbsp;MB Flash
	- 512&nbsp;kB SRAM
	- 512&nbsp;kB RAM
	- 8&nbsp;MB PSRAM
	- 16&nbsp;kB RTC SRAM
- LoRa transceiver **Semtech SX1262**
	- LoRa and LoRaWAN support
	- Frequency support from 863&nbsp;MHz to 928&nbsp;MHz
- **LoRaWAN 1.0.2** specification compliant (LoRaWAN **BasicModem** support in preparation)
- **Supported bands**: IN865, EU868, AU915, US915, KR920, RU864, and AS923-1/2/3/4
- LoRaWAN Activation by OTAA/ABP
- LoRa Point-to-Point (P2P) communication
- BLE 5.0 support
- Wi-Fi support
- Custom firmware using Arduino
- I/O ports: UART/I2C/SPI/ADC/GPIO
- Long-range: greater than 10&nbsp;km with optimized antenna
- **Supply Voltage**: 3.0&nbsp;V ~ 3.6&nbsp;V
- **Temperature range**: -40°&nbsp;C ~ 65°&nbsp;C

## Specifications

### Overview

#### Block Diagram

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3112-module/datasheet/rak3112-block-diagram.png"
  width="100%"
  caption="RAK3112 system block diagram"
/>

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
- GPIO33 to GPIO37 are on the stamp modules pins, but with the 16&nbsp;MB Flash chip, these GPIO's are not available.
- GPIO4 is used internally and not available.
:::



<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3112-module/datasheet/rak3112-pinout.png"
  width="100%"
  caption="RAK3112 module pinout diagram"
/>

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
- RF traces must have 50&nbsp;Ω impedance. It is advisable to use an impedance simulation software tool to achieve this requirement.
- If using an external antenna connector, place it close to the LoRa RF and BLE RF pins.
- Ground plane optimization is critical for certain antenna types like monopoles.
- The GND trace used for the RF return path must be directly connected to the GND plane and not treated as a thermal relief.
- It is recommended that RF traces be routed in curves, not sharp 90&nbsp;degree angles.

In addition, with our commitment to making IoT easy, we offer dedicated service for <a href="https://store.rakwireless.com/products/antenna-rf-design-service-including-pcb-design-tuning-matching-and-rf-test" target="_blank">Antenna RF Design which includes PCB design, tuning, matching and RF testing.</a>
:::

#### RF Characteristics

##### LoRa Transceiver

The RAK3112 module supports many LoRaWAN bands as shown in the table below.

<table>
  <thead>
    <tr>
      <th>Module</th>
      <th>Region</th>
      <th>Frequency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowSpan = "7">RAK3112 (H)</td>
      <td>Europe</td>
      <td>EU868</td>
    </tr>
    <tr>
      <td>North America</td>
      <td>US915</td>
    </tr>
    <tr>
      <td>Australia</td>
      <td>AU915</td>
    </tr>
    <tr>
      <td>Korea</td>
      <td>KR920</td>
    </tr>
    <tr>
      <td>Asia</td>
      <td>AS923-1/2/3/4</td>
    </tr>
    <tr>
      <td>India</td>
      <td>IN865</td>
    </tr>
    <tr>
      <td>Russia</td>
      <td>RU864</td>
    </tr>
  </tbody>
</table>

###### TX Power

Transmitter output power, programmable up to +22&nbsp;dBm.

###### RX Sensitivity

- -124&nbsp;dBm for LoRa（BW = 125&nbsp;kHz, SF = 7）
- -121&nbsp;dBm for LoRa (BW = 250&nbsp;kHz, SF = 7)
- -137&nbsp;dBm for LoRa (BW = 125&nbsp;kHz, SF = 12)
- -134&nbsp;dBm for LoRa（BW = 250&nbsp;kHz, SF = 12）

##### Wi-Fi

###### Operating Frequencies

2412 ~ 2484&nbsp;MHz

###### TX Power

| Rate                  | Type&nbsp;(dBm) |
|-----------------------|-----------------|
| 802.11b, 1&nbsp;Mbps  | 21.0            |
| 802.11b, 11&nbsp;Mbps | 21.0            |
| 802.11g, 6&nbsp;Mbps  | 20.5            |
| 802.11g, 54&nbsp;Mbps | 19.0            |
| 802.11n, HT20, MCS0   | 19.5            |
| 802.11n, HT20, MCS7   | 19.0            |
| 802.11n, HT40, MCS0   | 19.5            |
| 802.11n, HT40, MCS7   | 18.0            |

###### RX Sensitivity

| Rate                  | Type&nbsp;(dBm) |
|-----------------------|-----------------|
| 802.11b, 1&nbsp;Mbps  | –98.4           |
| 802.11b, 11&nbsp;Mbps | -88.6           |
| 802.11g, 6&nbsp;Mbps  | –93.2           |
| 802.11g, 54&nbsp;Mbps | –76.5           |
| 802.11n, HT20, MCS0   | –92.6           |
| 802.11n, HT20, MCS7   | –74.2           |
| 802.11n, HT40, MCS0   | –90.0           |
| 802.11n, HT40, MCS7   | –71.4           |

##### Bluetooth

###### Operating Frequencies

2402 ~ 2480&nbsp;MHz

###### TX Power

| Rate               | Type&nbsp;(dBm)                               |
|--------------------|-----------------------------------------------|
| BLE @1&nbsp;Mbps   | Programmable from -24&nbsp;dBm to 20&nbsp;dBm |
| BLE @2&nbsp;Mbps   | Programmable from -24&nbsp;dBm to 20&nbsp;dBm |
| BLE @125&nbsp;Kbps | Programmable from -24&nbsp;dBm to 20&nbsp;dBm |
| BLE @500&nbsp;Kbps | Programmable from -24&nbsp;dBm to 20&nbsp;dBm |

###### RX Sensitivity

| Rate               | Type&nbsp;(dBm) |
|--------------------|-----------------|
| BLE @1&nbsp;Mbps   | –97.5           |
| BLE @2&nbsp;Mbps   | –93.5           |
| BLE @125&nbsp;Kbps | –104.5          |
| BLE @500&nbsp;Kbps | –101            |


#### Electrical Characteristics

##### Operating Voltage

| Feature | Minimum | Typical | Maximum |   Unit    |
|:-------:|:-------:|:-------:|:-------:|:---------:|
|   VDD   |   3.0   |   3.3   |   3.6   | Volts (V) |

##### Operating Current

The current consumption measurements are taken with a 3.3&nbsp;V supply at 25°&nbsp;C of ambient temperature.

<table>
  <thead>
    <tr>
      <th>Work Mode</th>
      <th>Condition</th>
      <th>Peak current</th>
      <th>Unit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowSpan="4">Wi-Fi TX</td>
      <td>802.11b, 1&nbsp;Mbps, @21&nbsp;dBm</td>
      <td>340</td>
      <td>mA</td>
    </tr>
    <tr>
      <td>802.11g, 54&nbsp;Mbps, @19&nbsp;dBm</td>
      <td>291</td>
      <td>mA</td>
    </tr>
    <tr>
      <td>802.11n, HT20, MCS7, @18.5&nbsp;dBm</td>
      <td>283</td>
      <td>mA</td>
    </tr>
    <tr>
      <td>802.11n, HT40, MCS7, @18&nbsp;dBm</td>
      <td>286</td>
      <td>mA</td>
    </tr>
    <tr>
      <td rowSpan="2">Wi-Fi RX</td>
      <td>802.11b/g/n, HT20</td>
      <td>88</td>
      <td>mA</td>
    </tr>
    <tr>
      <td>802.11n, HT40</td>
      <td>91</td>
      <td>mA</td>
    </tr>
    <tr>
      <td rowSpan="4">Lora TX</td>
      <td>+22&nbsp;dBm@ 868&nbsp;to&nbsp;915Mhz</td>
      <td>140</td>
      <td>mA</td>
    </tr>
    <tr>
      <td>+20&nbsp;dBm@ 868 to 915&nbsp;Mhz</td>
      <td>127.5</td>
      <td>mA</td>
    </tr>
    <tr>
      <td>+17&nbsp;dBm@ 868 to 915&nbsp;Mhz</td>
      <td>118</td>
      <td>mA</td>
    </tr>
    <tr>
      <td>+14&nbsp;dBm@ 868 to 915&nbsp;Mhz</td>
      <td>112</td>
      <td>mA</td>
    </tr>
    <tr>
      <td>Lora RX</td>
      <td>LoRa 125&nbsp;kHz</td>
      <td>25.46</td>
      <td>mA</td>
    </tr>
  </tbody>
</table>

##### Sleep Current

The current consumption measurements are taken with a 3.3&nbsp;V supply at 25°&nbsp;C of ambient
temperature.

| Feature      | Condition                                                             | Maximum | Unit |
|--------------|-----------------------------------------------------------------------|---------|------|
| Light-sleep  | VDD_SPI and Wi-Fi are powered down, and all GPIOs are high-impedance. | 241     | uA   |
| Deep-sleep 1 | RTC memory and RTC peripherals are powered up.                        | 9       | uA   |
| Deep-sleep 2 | RTC memory is powered up. RTC peripherals are powered down.           | 8       | uA   |
| Power off    | CHIP_PU is set to low level. The chip is shut down.                   | 2       | uA   |


#### Mechanical Characteristics

##### Module Dimensions

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4630-module/datasheet/mechanical_drawing.png"
  width="70%"
  caption="RAK3112 board dimension"
/>

##### Layout Recommendation

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak4630-module/datasheet/pcb_footprint.png"
  width="70%"
  caption="RAK3112 PCB footprint and recommendations"
/>

#### Environmental Characteristics

##### Operating Temperature

|        Feature        | Minimum | Typical | Maximum |   Unit   |
|:---------------------:|:-------:|:-------:|:-------:|:--------:|
| Operating Temperature |   -40   |   25    |   65    | °&nbsp;C |

##### Storage Temperature

|       Feature       | Minimum | Typical | Maximum |   Unit   |
|:-------------------:|:-------:|:-------:|:-------:|:--------:|
| Storage Temperature |   -40   |    -    |   85    | °&nbsp;C |

##### Recommended Reflow Profile

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak11720-module/datasheet/reflow.png"
  width="70%"
  caption="Reflow Profile for RAK3112"
/>

Standard conditions for reflow soldering:

- Pre-heating Ramp (A) (Initial temperature: 150°&nbsp;C): **1 ~ 2.5°&nbsp;C/sec**
- Soaking Time (T2) (150 ~ 180°&nbsp;C): **60 ~ 100&nbsp;sec**
- Peak Temperature (G): **230 ~ 250°&nbsp;C**
- Reflow Time (T3) (> 220°&nbsp;C): **30 ~ 60&nbsp;sec**
- Ramp-up Rate (B): **0 ~ 2.5°&nbsp;C/sec**
- Ramp-down Rate (C): **1 ~ 3°&nbsp;C/sec**

#### Schematic Diagram (Minimal)

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3112-module/datasheet/rak3112-minimal-schematic.png"
  width="100%"
  caption="RAK3112 minimal schematic"
/>

### Firmware

The RAK3112 does not come with default firmware. You have to develop your application based on the Arduino IDE, using the Espressif BSP.
Examples of how to use LoRa, LoRaWAN, BLE, and WiFi are available in the <a href="https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK3112" target="_blank">GitHub repo</a>
A guide for firmware development can be found in the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3112-module/quickstart/#software-setup" target="_blank">RAK3112 Quick Start Guide</a>

<!--
### Certification

Work in progress -->

<RkBottomNav/>