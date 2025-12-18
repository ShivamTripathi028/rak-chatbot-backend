---
title: RAK3212 LoRaWAN Breakout Board with BLE & WiFi Datasheet | Specs & Features
description: Access the RAK3212 datasheet for comprehensive specs, a low-power, long-range LoRaWAN module with Espressif ESP32-S3 MCU, Semtech SX1262 LoRa Transceiver.
image: https://images.docs.rakwireless.com/wisduo/rak3212-breakout-board/rak3212.png
keywords:
  - rak3212
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
slug: /product-categories/wisduo/rak3212-breakout-board/datasheet/
date: 2025-08-22
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK3212 WisDuo LoRaWAN + BLE + WiFi Breakout Board Datasheet

## Overview

### Description

The **RAK3212** is a breakout board featuring the RAK3112 module, which combines the Espressif ESP32-S3 MCU with a Semtech SX1262 LoRa transceiver. This low-power, long-range module supports LoRaWAN, BLE, and WiFi, making it ideal for a wide range of IoT applications such as home automation, sensor networks, building automation.


### Features

- Based on [RAK3112 (ESP32-S3 MCU + SX1262 LoRa transceiver)](https://docs.rakwireless.com/product-categories/wisduo/rak3112-module/datasheet/)
- Provides all RAK3112 pins via header
- **MCU**: **Espressif ESP32-S3**
	- Xtensa® 32-bit LX7 dual-core microprocessor
	- 16&nbsp;MB Flash
	- 512&nbsp;kB SRAM
	- 512&nbsp;kB RAM
	- 8&nbsp;MB PSRAM
	- 16&nbsp;kB RTC SRAM
- LoRa transceiver: **Semtech SX1262**
	- 863-928&nbsp;MHz, LoRa/LoRaWAN support
- **LoRaWAN 1.0.2** compliant (**BasicModem** support in preparation)
- **Supported bands**: IN865, EU868, AU915, US915, KR920, RU864, and AS923-1/2/3/4
- LoRaWAN Activation: OTAA/ABP
- LoRa Point-to-Point (P2P) communication
- BLE 5.0 support
- WiFi support
- Custom firmware using Arduino
- I/O ports: UART/I2C/SPI/ADC/GPIO
- Long-range: greater than 10&nbsp;km with optimized antenna
- **Supply Voltage**: 3.0&nbsp;V\~3.6&nbsp;V
- **Temperature range**: -40°&nbsp;C\~65°&nbsp;C
- **Dimensions**: 29&nbsp;mm x 40&nbsp;mm x 4.28&nbsp;mm

## Specifications

### Overview

#### Block Diagram

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3112-module/datasheet/rak3112-block-diagram.png"
  width="100%"
  caption="RAK3112 system block diagram"
/>

### Hardware

The hardware specification is categorized into three parts: RF, electrical, and mechanical parameters. These include tables of functionalities and standard values for the RAK3112 WisDuo LPWAN Module.

#### Internal Connections Between ESP32-S3 MCU and SX1262 LoRa transceiver

| SX1262   | ESP32-S3 | Function               |
|----------|----------|------------------------|
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
- GPIO33 to GPIO37 are on the stamp module’s pins, but with the 16&nbsp;MB Flash chip, these GPIOs are not available.
- GPIO4 is used internally and not available.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3212-breakout-board/rak3212-headers.png"
  width="30%"
  caption="RAK3212 Pin Headers"
/>

###### RAK3212 Pins

Pin Header J3

| **Pin No.** | **Name**     | **Type** | **Description**       |
|-------------|--------------|----------|-----------------------|
| 1           | 5V           | Power    | 5&nbsp;V USB          |
| 2           | 5V           | Power    | 5&nbsp;V USB          |
| 3           | GND          | Power    | GND                   |
| 4           | GND          | Power    | GND                   |
| 5           | GND          | Power    | GND                   |
| 6           | GPIO0 / Boot | I/O Boot | GPIO Bootloader force |
| 7           | GND          | Power    | GND                   |
| 8           | VCC          | Power    | 3.3&nbsp;V Supply     |
| 9           | VCC          | Power    | 3.3&nbsp;V Supply     |

Pin Header J4

| **Pin No.** | **Name**       | **Type**       | **Description** |
|-------------|----------------|----------------|-----------------|
| 1           | GPIO18/I2C SCL | I2C Clock      | I2C 2 SCL       |
| 2           | GPIO21/AIN0    | GPIO/Analog In | GPIO            |
| 3           | GPIO38         | GPIO           | GPIO            |
| 4           | GPIO39         | GPIO           | GPIO            |
| 5           | GPIO40/I2C SCL | GPIO/I2C Clock | I2C 1 SCL       |
| 6           | GPIO41         | GPIO           | GPIO            |
| 7           | GPIO42         | GPIO           | GPIO            |
| 8           | GPIO45         | GPIO           | GPIO            |
| 9           | GPIO46         | GPIO           | GPIO            |

Pin Header J5

| **Pin No.** | **Name**        | **Type**       | **Description** |
|-------------|-----------------|----------------|-----------------|
| 1           | GPIO1           | GPIO           | GPIO            |
| 2           | GPIO2           | GPIO           | GPIO            |
| 3           | GPIO9/I2C SDA   | GPIO/I2C Data  | I2C 1 SDA       |
| 4           | GPIO10/SPI MISO | GPIO/SPI MISO  | SPI MISO        |
| 5           | GPIO11/SPI MOSI | GPIO/SPI MOSI  | SPI MOSI        |
| 6           | GPIO12/SPI CS   | GPIO/SPI CS    | SPI CS          |
| 7           | GPIO13/SPI SCK  | GPIO/SPI SCK   | SPI SCK         |
| 8           | GPIO14/AIN1     | GPIO/Analog In | GPIO            |
| 9           | GPIO17/I2C SDA  | GPIO/I2C Data  | I2C 2 SDA       |

Pin Header J6

| **Pin No.** | **Name** | **Type**      | **Description**           |
|-------------|----------|---------------|---------------------------|
| 1           | GPIO33   | GPIO          | N/A with 16&nbsp;MB PSRAM |
| 2           | GPIO34   | GPIO          | N/A with 16&nbsp;MB PSRAM |
| 3           | GPIO35   | GPIO/I2C Data | N/A with 16&nbsp;MB PSRAM |
| 4           | GPIO36   | GPIO/SPI MISO | N/A with 16&nbsp;MB PSRAM |
| 5           | GPIO37   | GPIO/SPI MOSI | N/A with 16&nbsp;MB PSRAM |
| 6           | GPIO4    | NC            | N/A                       |
| 7           | UART0_RX | GPIO/UART     | UART 0 RX                 |
| 8           | UART0_TX | GPIO/UART     | UART 0 TX                 |
| 9           | GND      | Power         | GND                       |

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

##### WiFi

###### Operating Frequencies

2412\~2484&nbsp;MHz

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
| 802.11b, 1&nbsp;Mbps  | -98.4           |
| 802.11b, 11&nbsp;Mbps | -88.6           |
| 802.11g, 6&nbsp;Mbps  | -93.2           |
| 802.11g, 54&nbsp;Mbps | -76.5           |
| 802.11n, HT20, MCS0   | -92.6           |
| 802.11n, HT20, MCS7   | -74.2           |
| 802.11n, HT40, MCS0   | -90.0           |
| 802.11n, HT40, MCS7   | -71.4           |

##### Bluetooth

###### Operating Frequencies

2402\~2480&nbsp;MHz

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
| BLE @1&nbsp;Mbps   | -97.5           |
| BLE @2&nbsp;Mbps   | -93.5           |
| BLE @125&nbsp;Kbps | -104.5          |
| BLE @500&nbsp;Kbps | -101            |


#### Electrical Characteristics

##### Operating Voltage

| Feature | Minimum | Typical | Maximum |   Unit    |
|:-------:|:-------:|:-------:|:-------:|:---------:|
|   VDD   |   3.0   |   3.3   |   3.6   | Volts (V) |

##### Operating Current

The current consumption measurements are taken with a 3.3&nbsp;V supply at an ambient temperature of 25°&nbsp;C.

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
      <td rowSpan="4">WiFi TX</td>
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
      <td rowSpan="2">WiFi RX</td>
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
      <td rowSpan="4">LoRa TX</td>
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
      <td>LoRa RX</td>
      <td>LoRa 125&nbsp;kHz</td>
      <td>25.46</td>
      <td>mA</td>
    </tr>
  </tbody>
</table>

##### Sleep Current

The current consumption measurements are taken with a 3.3&nbsp;V supply at 25°&nbsp;C of ambient
temperature.

| Feature      | Condition                                                            | Maximum | Unit |
|--------------|----------------------------------------------------------------------|---------|------|
| Light-sleep  | VDD_SPI and WiFi are powered down, and all GPIOs are high-impedance. | 241     | uA   |
| Deep-sleep 1 | RTC memory and RTC peripherals are powered up.                       | 9       | uA   |
| Deep-sleep 2 | RTC memory is powered up. RTC peripherals are powered down.          | 8       | uA   |
| Power off    | CHIP_PU is set to low level. The chip is shut down.                  | 2       | uA   |


#### Mechanical Characteristics

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3212-breakout-board/rak3212-dimensions.svg"
  width="70%"
  caption="RAK3212 board dimension"
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

#### Schematic Diagram

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3212-breakout-board/rak3212-bb-schematic.svg"
  width="100%"
  caption="RAK3212 schematic diagram"
/>

### Firmware

The RAK3212 does not include pre-installed firmware. To use the module, you must develop your own application with the Arduino IDE and the Espressif BSP.

Example projects for LoRa, LoRaWAN, BLE, and WiFi are available in our <a href='https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK3112' target='_blank'>GitHub repository.</a> Additionally, a guide for firmware development can be found in the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3112-module/quickstart/#software-setup" target="_blank">RAK3112 Quick Start Guide.</a>



<!--
### Certification

Work in progress -->

<RkBottomNav/>