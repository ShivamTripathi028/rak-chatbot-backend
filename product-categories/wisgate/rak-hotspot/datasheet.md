---
title: RAK Hotspot Datasheet
description: Provides comprehensive information about your RAK Hotspot to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
keywords:
- datasheet
- wisgate
- RAK Hotspot
image: https://images.docs.rakwireless.com/wisgate/rak-hotspot/rak-hotspot.png
sidebar_label: Datasheet
---

# RAK Hotspot Datasheet

## Overview

### Description

**Hotspot Details**

- Efficient for mining Helium (HNT) cryptocurrency
- Complete set-up in minutes using a smartphone
- LongFi technology maximizes range and battery life without Wi-Fi, cellular or Bluetooth
- Low Power – only uses about the same amount as an LED light bulb (5 W)
- Easily manage Hotspots and tokens from the mobile app
- LongFi™ Technology

![longfi](https://images.docs.rakwireless.com/wisgate/rak-hotspot/icons/longfi.png)

Helium LongFi is a technology architecture that combines a leading wireless technology, LoRaWAN, and the Helium Blockchain. LongFi is optimized for miles of range, and long battery life for IoT devices.

![proof-of-coverage](https://images.docs.rakwireless.com/wisgate/rak-hotspot/icons/proof-of-coverage.png)

RAK Hotspot earns Helium when devices connect, and for validating wireless coverage delivered by peers. Using a system called Proof-of-Coverage, RAK Hotspot earns more Helium when they are in the range of other RAK Hotspot, but need to be at least 300 meters apart.

Range depends on the environment: for rural areas, **up to 10 miles or more**, but for more dense areas, **up to a mile**. Single RAK Hotspot earns less as they can only issue Challenges over the internet and cannot participate in Proof-of-Coverage.

![wireless-coverage](https://images.docs.rakwireless.com/wisgate/rak-hotspot/icons/wireless-coverage.png)

- Provide coverage across many square miles with a single RAK Hotspot.
- Based on initial testing, only about 50 to 100 RAK Hotspots are needed to provide complete
coverage for an entire city.

![connect-anything](https://images.docs.rakwireless.com/wisgate/rak-hotspot/icons/connect-anything.png)

- Create a new global network for billions of devices
- Any IoT device can become Helium-enabled using readily available off-the-shelf hardware components, software, and a reference design that is open source for anyone to improve upon.

### Features

- Computing with Raspberry Pi4 (Linux)
- 2 GB on-board RAM
- 32 GB SD card
- Based on the LoRa Concentrator Engine: Semtech® SX1302
- Built-in Heat Sink for thermal heat dissipation management
- Supports 5 V/ 3 A power supply
- IP30 housing
- TX power up to 27 dBm, RX sensitivity down to -139 dBm @SF12, BW 125 kHz
- LoRa Frequency band support: RU864, IN865, EU868, US915, AU915, KR920, AS923.
- Includes Pi ready 'ID EE PROM', GPIO setup, and device tree can be automatically configured
from vendor information
- Supports a fully open source LoRaWAN server

## Specifications

### Overview

The overview covers the RAK Hotspot details and block diagram.

#### Board Overview

The outer dimensions of the RAK Hotspot are **92 mm x 68.3 mm x 57.2 mm**.

> **Image:** Device Dimensions

#### Hotspot Details

**Figure 2** illustrates the basic building blocks of the RAK Hotspot. The RAK2287 is a vital component, providing all LoRaWAN connectivity. It manages the reception and transmission of LoRa frames and handles signal modulation and demodulation, among other tasks.

Higher-level protocol functions and LoRa frame processing are carried out by the embedded host system (Raspberry Pi). Processed LoRa frames are then forwarded to a LoRaWAN server. The detailed segmentation of protocol-related tasks is beyond the scope of this document.

> **Image:** RAK Hotspot System Structure

#### Block Diagram

The RAK Hotspot receives and transmits radio messages. The embedded host system (Raspberry Pi 4) handles the processing of these messages and the associated protocol tasks. Processed radio messages are then sent to a Helium LoRaWAN server. The block diagram of the RAK Hotspot is shown in **Figure 3**.

> **Image:** RAK Hotspot Block Diagram

:::tip NOTE
The specific segmentation of protocol-related tasks is beyond the scope of this document.
:::

### Hardware

#### Interfaces

The interface of RAK Hotspot is shown in **Figure 4**.

> **Image:** RAK Hotspot Interfaces

#### RF Characteristics

##### Operating Frequencies

The RAK Hotspot supports all LoRaWAN frequency.

| **Region**    | **Frequency (MHz)** |
| ------------- | ------------------- |
| Europe        | EU868               |
| North America | US915               |
| Asia          | AS923               |
| Australia     | AU915               |
| Korea         | KR920               |
| India         | IN865               |
| Russia        | RU864               |

##### LoRa RF Characteristics

###### Transmitter RF Characteristics

The RAK Hotspot has an excellent transmitter performance. It is highly recommended to use an optimized configuration for the power level configuration, which is part of the HAL. This results in a mean RF output power level and current consumption.

| **PA Control** | **PWID Control** | **Power**   |
| -------------- | ---------------- | ----------- |
| **0**          | 10               | -6 dBm |
| **0**          | 13               | -3 dBm |
| **0**          | 17               | 0 dBm  |
| **0**          | 20               | 4 dBm  |
| **1**          | 0                | 8 dBm  |
| **1**          | 2                | 10 dBm |
| **1**          | 4                | 12 dBm |
| **1**          | 7                | 14 dBm |
| **1**          | 9                | 16 dBm |
| **1**          | 10               | 17 dBm |
| **1**          | 12               | 19 dBm |
| **1**          | 13               | 20 dBm |
| **1**          | 16               | 23 dBm |
| **1**          | 18               | 25 dBm |
| **1**          | 20               | 26 dBm |
| **1**          | 22               | 27 dBm |

:::tip NOTE
Typically, there is a ±1.5 dB difference between the actual test value and the table data.
:::

:::tip NOTE
Unless otherwise specified, T = 25 ℃ and VDD = 5 V (Typ.).
:::

| **Parameter**                              | **Condition**            | **Min**       | **Typ.** | **Max**       |
| ------------------------------------------ | ------------------------ | ------------- | -------- | ------------- |
| **Frequency Range**                        |                          | 863 MHz  |          | 870 MHz  |
| **Modulation Techniques**                  | FSK/LoRa                 |               |          |               |
| **TX Frequency Variation vs. Temperature** | Power Level Setting : 20 | -3 kHz   |          | +3 kHz   |
| **TX Power Variation vs. Temperature**     | Power Level Setting : 20 | -5 dBm   |          | +5 dBm   |
| **TX Power Variation**                     |                          | -1.5 dBm |          | +1.5 dBm |

| **Parameter**             | **Condition** | **Min**      | **Typ.** | **Max**      |
| ------------------------- | ------------- | ------------ | -------- | ------------ |
| **Frequency Range**       |               | 902 MHz |          | 928 MHz |
| **Modulation Techniques** | FSK/LoRa      |              |          |              |

###### Receiver RF Characteristics

It is highly recommended, to use optimized RSSI calibration values, which is part of the HAL v3.For both, Radio 1 and 2, the RSSI-Offset should be set at -169.0. The following table gives the typical sensitivity level of the RAK Hotspot.

| **Signal Bandwidth (Khz)** | **Spreading Factor** | **Sensitivity (dBm)** |
| :------------------------: | :------------------: | :-------------------: |
|            125             |          12          |         -139          |
|            125             |          7           |         -125          |
|            250             |          12          |         -136          |
|            250             |          7           |         -123          |
|            500             |          12          |         -134          |
|            500             |          7           |         -120          |

#### Antenna Specifications

##### LoRa Antenna

###### Overview

The LoRa Antenna with RP-SMA Male connector is shown in the figure below:

> **Image:** LoRa® Antenna

###### Antenna Dimension

The antenna's mechanical dimension is shown below:

> **Image:** LoRa® Antenna Dimension (mm)

###### Antenna Parameters

| Items                              | Specifications                       | Specifications                       |
| ---------------------------------- | ------------------------------------ | ------------------------------------ |
| Frequency Range                    | 863~870 MHz                     | 902~928 MHz                     |
| Peak Gain                          | 2.8 dBi                         | 2.3 dBi                         |
| Voltage Standard Wave Ratio (VSWR) | ≤1.5                                 | ≤1.5                                 |
| Efficiency                         | >80 %                           | >80 %                           |
| Feed Impedance                     | 50 Ohms                         | 50 Ohms                         |
| Working Temperature & Humidity     | T: -35~+75° C, H: 5~95 %RH | T: -35~+75° C, H: 5~95 %RH |

#### Electrical Requirements

The RAK Hotspot operates at 5 V / 3 A

| **Parameter**      | **Min.** | **Typical** | **Max**     |
| ------------------ | -------- | ----------- | ----------- |
| **LoRa Tx mode**   | -        | -           | 950 mA |
| **Standby power**  | -        | 550 mA | -           |
| **Burn test mode** | -        | -           | 940 mA |

:::tip NOTE
* LoRa Tx mode: The LoRa module works at the maximum transmit power state.
* Burn test mode: Raspberry Pi CPU and memory are running at full capacity.
:::

#### Environmental Requirements

The table below lists the operation and storage temperature requirements:

| **Parameter**                   | **Min.**    | **Typical** | **Max**     |
| ------------------------------- | ----------- | ----------- | ----------- |
| **Operation Temperature Range** | -10 ºC | +25 ºC | +55 ºC |
| **Storage Temperature Range**   | -40 ºC |             | +85 ºC |

### Firmware

| **Model**   | **Raspberry Pi Board** | **Firmware Version** | **Source** |
| ----------- | ---------------------- | -------------------- | ---------- |
| RAK Hotspot | Raspberry Pi 4         |                      |            |

### Software

#### LoRaWAN

* Supports class A, C
* Supports connect to TTN server Supports LoRa package forward
* Supports build-in ChirpStack® LoRaWAN Server

#### Network Protocol Stack

* Supports 802.11ac
* Supports Wi-Fi AP mode and Client mode
* Supports DHCP

## Certification

### Certifications
- **KC:** https://downloads.rakwireless.com/LoRa/RAK_Hotspot/Certification/RAK7248_HotspotV2.0_KC_Certification.pdf
- **RCM:** https://downloads.rakwireless.com/LoRa/RAK_Hotspot/Certification/RAK7248_HotspotV2.0_RCM_Certification.pdf

### FCC Caution

Any changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate the equipment.

This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

:::tip IMPORTANT NOTE
This equipment has been tested and found to comply with the limits for a Class B digital device, according to part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation. This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used following the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:

* Reorient or relocate the receiving antenna.
* Increase the separation between the equipment and receiver.
* Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
* Consult the dealer or an experienced radio/TV technician for help.
:::

### FCC Radiation Exposure Statement

This equipment complies with FCC radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 20 cm between the radiator & your body.

:::warning ISEDC Warning
This device complies with Innovation, Science, and Economic Development Canada licence-exempt RSS standard(s). Operation is subject to the following two conditions:

1. this device may not cause interference, and
2. this device must accept any interference, including interference that may cause undesired operation of the device.

The device complies with RF exposure guidelines, users can obtain Canadian information on RF exposure and compliance. The minimum distance from the body to use the device is 20 cm.
:::

