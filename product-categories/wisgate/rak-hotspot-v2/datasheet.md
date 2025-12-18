---
title: RAK Hotspot V2 Datasheet
description: Provides comprehensive information about your RAK Hotspot V2 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
keywords:
- datasheet
- wisgate
- RAK Hotspot V2
image: https://images.docs.rakwireless.com/wisgate/rak-hotspot-v2/rak-hotspot-v2.png
sidebar_label: Datasheet
---

# RAK Hotspot V2 Datasheet

## Overview

### Description

**Hotspot Details**

- Efficient for mining the **Helium (HNT)** cryptocurrency
- Complete setup in minutes using a smartphone
- **LongFi technology** maximizes range and battery life without Wi-Fi, cellular, or Bluetooth
- Low Power: Only consumes about the same amount of energy as an LED light bulb (5 W)
- Easily manage hotspots and tokens from the mobile app

![longfi](https://images.docs.rakwireless.com/wisgate/rak-hotspot/icons/longfi.png)

**Helium LongFi** is a technology architecture that combines leading wireless technology, LoRaWAN, and the Helium Blockchain. LongFi is optimized for miles of range and long battery life for IoT devices.

![proof-of-coverage](https://images.docs.rakwireless.com/wisgate/rak-hotspot/icons/proof-of-coverage.png)

RAK Hotspots earn Helium when devices connect and for validating wireless coverage provided by peers. Through a system called Proof-of-Coverage, RAK Hotspots earn more Helium when they are within range of other RAK Hotspots, provided they are at least 300 meters apart.

The range depends on the environment: in rural areas, it can reach **up to 10 miles or more**, while in dense urban areas, it is typically **up to a mile**. A single RAK Hotspot earns less because it can only issue Challenges over the internet and cannot participate in Proof-of-Coverage.

![wireless-coverage](https://images.docs.rakwireless.com/wisgate/rak-hotspot/icons/wireless-coverage.png)

- A single RAK Hotspot can deliver coverage over many square miles
- Initial testing suggests that complete city coverage can be achieved with only 50 to 100 RAK Hotspots.

![connect-anything](https://images.docs.rakwireless.com/wisgate/rak-hotspot/icons/connect-anything.png)

- Establish a global network capable of connecting billions of devices
- Any IoT device can be Helium-enabled using easily accessible off-the-shelf hardware components, software, and an open-source reference design that is available for anyone to enhance.

## Product Features

- Utilizes the Raspberry Pi 4 computer board
- Onboard RAM: 2 GB, 4 GB, or 8 GB
- 32 GB SD card
- Based on the LoRa Concentrator Engine: Semtech® SX1302
- Built-in heat sink for efficient thermal heat dissipation management
- Supports 5 V / 2.4 A power supply
- IP30 housing
- TX power up to 27 dBm, RX sensitivity down to -139 dBm @SF12, BW 125 kHz
- LoRa frequency band support includes RU864, IN865, EU868, US915, AU915, KR920, and AS923
- 2.4 GHz and 5.0 GHz IEEE 802.11b/g/n/ac wireless LAN, Bluetooth 5.0, BLE

## Specifications

### Overview

The overview provides the details and block diagram of the RAK Hotspot.

#### Device Overview

The outer dimensions of the RAK Hotspot are **92 mm x 68.3 mm x 57.2 mm**.

> **Image:** Device Dimensions

#### Hotspot Details

**Figure 2** summarizes the basic building blocks of the RAK Hotspot. The RAK2287 is essential to the device's functionality, providing all LoRaWAN connectivity. In addition, it sends and receives LoRa frames and handles signal modulation and demodulation.

The embedded host system, Raspberry Pi, is responsible for processing the LoRa frames and other high-level protocol-related tasks. After receiving and processing the LoRa frames, they are then sent to a LoRaWAN server.

> **Image:** RAK Hotspot System Structure

#### Block Diagram

The RAK Hotspot serves as the central hardware solution for all LoRa-based radio communication that receives and transmits radio messages. The embedded host system, Raspberry Pi, handles the processing of the LoRa frames and other high-level protocol-related tasks. Once the radio messages are received and processed, they are sent to a LoRaWAN server.

> **Image:** RAK Hotspot Block Diagram

:::tip NOTE
The detailed segmentation of protocol-related tasks is beyond the scope of this document.
:::

### Hardware

#### Interfaces

> **Image:** RAK Hotspot Interfaces

#### RF Characteristics

##### Operating Frequencies

The RAK Hotspot supports all LoRaWAN frequency channels, including RU864, IN865, EU868, US915, AU915, KR920, and AS923. Configuring these channels is straightforward when building the firmware from the source code.

##### LoRa RF Characteristics

###### Transmitter RF Characteristics

The RAK Hotspot boasts excellent transmitter performance. It is highly recommended to utilize an optimized configuration for the power level configuration, which is part of the Hardware Abstraction Layer (HAL). HAL ensures a consistent RF output power level and current consumption.

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
- Usually, there's a ±1.5 dB variance between the actual test value and the data in the table.
- If nothing else is stated, T=25 ℃, VDD=5 V (Typ.).
:::

| **Parameter**                              | **Condition**           | **Min**       | **Max**       |
| ------------------------------------------ | ----------------------- | ------------- | ------------- |
| **Frequency Range**                        | -                       | 863 MHz  | 870 MHz  |
| **Modulation Techniques**                  | FSK/LoRa                | -             | -             |
| **TX Frequency Variation vs. Temperature** | Power Level Setting: 20 | -3 kHz   | +3 kHz   |
| **TX Power Variation vs. Temperature**     | Power Level Setting: 20 | -5 dBm   | +5 dBm   |
| **TX Power Variation**                     | -                       | -1.5 dBm | +1.5 dBm |

| **Parameter**             | **Condition** | **Min**      | **Max**      |
| ------------------------- | ------------- | ------------ | ------------ |
| **Frequency Range**       | -             | 902 MHz | 928 MHz |
| **Modulation Techniques** | FSK/LoRa      | -            | -            |

###### Receiver RF Characteristics

It is highly recommended to use optimized RSSI calibration values, which are part of HAL v3.1. For both Radio 1 and 2, the RSSI-Offset should be set to -169.0. The following table provides the typical sensitivity level of the RAK Hotspot.

| **Signal Bandwidth (kHz)** | **Spreading Factor** | **Sensitivity (dBm)** |
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

The LoRa antenna with RP-SMA Male connector is shown in Figure 5.

> **Image:** LoRa Antenna

###### Antenna Dimension

> **Image:** LoRa Antenna Dimension (mm)

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

The RAK Hotspot operates at a voltage of 5 V and a current of 2.4 A.

| **Parameter**      | **Min.** | **Typical** | **Max**     |
| ------------------ | -------- | ----------- | ----------- |
| **LoRa Tx Mode**   | -        | -           | 950 mA |
| **Standby Power**  | -        | 550 mA | -           |
| **Burn Test Mode** | -        | -           | 940 mA |

:::tip NOTE
* **LoRa Tx Mode**: The LoRa module operates at the maximum transmit power state.
* **Burn Test Mode**: Raspberry Pi CPU and memory are running at full capacity.
:::

#### Environmental Requirements

The table below lists the operation and storage temperature requirements:

| **Parameter**                   | **Min.**    | **Typical** | **Max**     |
| ------------------------------- | ----------- | ----------- | ----------- |
| **Operation Temperature Range** | -10 ºC | +25 ºC | +55 ºC |
| **Storage Temperature Range**   | -40 ºC | -           | +85 ºC |

<!-- ### Firmware

| **Model**   | **Raspberry Pi Board** | **Firmware Version** | **Source** |
| ----------- | ---------------------- | -------------------- | ---------- |
| RAK Hotspot | Raspberry Pi 4         |                      |            | --> |

### Software

#### LoRaWAN

* Supports Class A & C
* Supports connection to the Helium Network

#### Network Protocol Stack

* Supports 802.11ac
* Supports Wi-Fi AP mode and Client mode
* Supports DHCP

## Certification

### Certifications
- **BSMI:** https://downloads.rakwireless.com/LoRa/RAK_Hotspot/Certification/RAK7248_HotspotV2.0_BSMI_Certification.pdf
- **CE:** https://downloads.rakwireless.com/LoRa/RAK_Hotspot/Certification/RAK7248_HotspotV2.0_CE_Certification.pdf
- **ERP:** https://downloads.rakwireless.com/LoRa/RAK_Hotspot/Certification/RAK7248_HotspotV2.0_ERP_Certification.pdf
- **FCC:** https://downloads.rakwireless.com/LoRa/RAK_Hotspot/Certification/RAK7248_HotspotV2.0_FCC_Certification.pdf
- **IMDA:** https://downloads.rakwireless.com/LoRa/RAK_Hotspot/Certification/RAK7248_HotspotV2.0_IMDA_Certification.zip
- **KC:** https://downloads.rakwireless.com/LoRa/RAK_Hotspot/Certification/RAK7248_HotspotV2.0_KC_Certification.pdf
- **NBTC:** https://downloads.rakwireless.com/LoRa/RAK_Hotspot/Certification/RAK7248_HotspotV2.0_NBTC_Certification.zip
- **NCC:** https://downloads.rakwireless.com/LoRa/RAK_Hotspot/Certification/RAK7248_HotspotV2.0_NCC_Certification.pdf
- **NTC:** https://downloads.rakwireless.com/LoRa/RAK_Hotspot/Certification/RAK7248_HotspotV2.0_NTC_Certification.jpg
- **RCM:** https://downloads.rakwireless.com/LoRa/RAK_Hotspot/Certification/RAK7248_HotspotV2.0_RCM_Certification.pdf
- **REACH:** https://downloads.rakwireless.com/LoRa/RAK_Hotspot/Certification/RAK7248_HotspotV2.0_REACH_Report.pdf
- **ROHS:** https://downloads.rakwireless.com/LoRa/RAK_Hotspot/Certification/RAK7248_HotspotV2.0_ROHS_Report.pdf
- **SUTEL:** https://downloads.rakwireless.com/LoRa/RAK_Hotspot/Certification/RAK7248_HotspotV2.0_SUTEL_Certification.pdf
- **UKCA:** https://downloads.rakwireless.com/LoRa/RAK_Hotspot/Certification/RAK7248_HotspotV2.0_UKCA_Certification.pdf
- **VIETNAM:** https://downloads.rakwireless.com/LoRa/RAK_Hotspot/Certification/RAK7248_HotspotV2.0_Vietnam_Certification.pdf

### FCC Caution

Any changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate the equipment.

This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

:::tip IMPORTANT NOTE
This equipment has been tested and found to comply with the limits for a Class B digital device, according to part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation. This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used following the instructions, may cause harmful interference to radio communications.

However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:

* Reorient or relocate the receiving antenna.
* Increase the separation between the equipment and receiver.
* Connect the equipment to an outlet on a circuit different from that to which the receiver is connected.
* Consult the dealer or an experienced radio/TV technician for help.
:::

### FCC Radiation Exposure Statement

This equipment complies with FCC radiation exposure limits set forth for an uncontrolled environment. It should be installed and operated with a minimum distance of 20 cm between the radiator and your body.

:::warning ISEDC Warning
This device complies with Innovation, Science, and Economic Development Canada's licence-exempt RSS standard(s). Operation is subject to the following two conditions:

1. this device may not cause interference, and
2. this device must accept any interference, including interference that may cause undesired operation of the device.

The device complies with RF exposure guidelines, users can obtain Canadian information on RF exposure and compliance. The minimum distance from the body to use the device is 20 cm.
:::
