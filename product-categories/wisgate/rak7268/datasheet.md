---
title: RAK7268 WisGate Edge Lite 2 Datasheet | LoRaWAN Gateway Specs
description: Explore the RAK7268 LoRaWAN gateway’s specs, including PoE, LTE, and MQTT support. Designed for IoT projects needing a reliable and scalable network solution.
keywords:
  - rak7268
  - rak7268 lorawan gateway
  - rak7268 datasheet
  - rak7268 specifications
  - rak7268 features
  - wisgate edge lite 2 specs
  - rak gateway specs
  - rak7268 ethernet connectivity
  - wisgate edge lite 2 interfaces
  - lorawan gateway specifications
  - 8 channel lorawan gateway
  - ethernet-enabled lorawan gateway
  - lorawan gateway for chirpstack and ttn
  - lorawan gateway with poe
  - lorawan mqtt and tls support
  - poe-powered lorawan gateway
  - indoor lorawan gateway
  - iot gateway with wi-fi setup
  - lorawan gateway lte
tags:
  - rak7268
  - wisgate
  - datasheet
image: https://images.docs.rakwireless.com/wisgate/rak7268/datasheet/RAK7268.png
sidebar_label: Datasheet
date: 2021-04-11
---

# RAK7268 WisGate Edge Lite 2 Datasheet

## Overview

### Description

The RAK7268 WisGate Edge Lite 2 is a full 8-channel indoor gateway, based on the LoRaWAN protocol, with built-in Ethernet connectivity for a straightforward setup. There is an onboard Wi-Fi setup (supporting 2.4 GHz Wi-Fi) that allows it to be easily configured via the default Wi-Fi AP mode. Additionally, the gateway supports LTE uplink communication connections (optional).

As with the other RAKwireless Industrial Gateways, it also supports MQTT Bridge mode, with the option for TLS authentication.

Power-over-Ethernet (PoE) is supported to serve cases where wall or ceiling mounting is required without the need to install additional power lines.

The open-source software for the management and configuration of this gateway device is based on OpenWRT. It has a built-in LoRa packet forwarder and a graphical user interface, allowing for a quick setup without giving up the freedom of a fully customized solution.

RAK7268 also supports the MQTT Bridge function, can use the MQTT integrated to third-party platforms.

RAK7268 is especially suitable for small and medium-sized deployment scenarios in industry applications, saving the additional cost for server and R&D investment, and has the advantages of high execution efficiency.

### Features

- Full LoRaWAN Stack support (V 1.0.3) with Semtech SX1302
- Supports 2.4 GHz Wi-Fi AP for configuration
- 100M Base-T Ethernet with PoE
- Multi back-haul with Ethernet, Wi-Fi, Cellular
- OpenWRT software supports  Web UI for easy configuration and monitoring
- Can integrate with both private (ChirpStack) and public (TTN) network servers
- TF card for log backup and LoRa frame buffering (in case of backhaul failover)
- Built-in Network Server for easy deployment of applications and integration of gateways
- LTE Cat 4 network (optional)

## Specifications

### Overview

The overview presents the block diagram for the RAK7268 that shows the internal architecture of the board.

#### Block Diagram

> **Image:** WisGate Edge Lite 2 Block Diagram

### Hardware

The hardware specification covers only the interfacing of the RAK7268 and its corresponding functionalities. It also presents the parameters and the standard values of the board.

#### Interfaces

The hardware interfaces of RAK7268 gateway include DC 12 V, ETH interface, Console interface, Reset key, TF Card slot, Status indicator LEDs, LoRa Antenna connector, etc.

> **Image:** WisGate Edge Lite 2 Interfaces

##### Reset Key Functions

The function of the Reset key is as follows:
  - **Short press**: Restart the gateway.
  - **Long press** (5 sec and above): Restore factory settings.

##### LED Indicators

| LEDs | Status Indication Description |
| --- | --- |
| PWR LED | Power indicator - The LED is on when device power is on |
| Breathing LED | Breathing after system up |
| ETH LED | ON - Linkup |
| ETH LED | OFF - Linkdown |
| ETH LED | Flicker - Data transmitting and receiving |
| LoRa LED | ON - LoRa is working |
| LoRa LED | OFF - LoRa is not working |
| LoRa LED | Flicker - Indicate LoRa Packet receiving and sending |
| WLAN LED | AP Mode: |
| WLAN LED | -ON - The AP is up |
| WLAN LED | -OFF - The AP is down |
| WLAN LED | -Flicker - Data receiving and sending |
| WLAN LED | STA Mode: |
| WLAN LED | -Slow flicker (1 Hz) - Disconnected |
| WLAN LED | -ON - Connected |
| WLAN LED | -Flicker - Data receiving and sending |
| LTE LED | Slow Flicker (1800 ms High / 200 ms Low) - Network searching |
| LTE LED | Slow flicker (200 ms High / 1800 ms Low) - Idle |
| LTE LED | Fast flicker (125 ms High / 125 ms Low) - Ongoing data transfer |

#### Main Specifications

| Feature | Specifications |
| --- | --- |
| Computing | MT7628, DDR2 RAM 128 MB |
| Wi-Fi feature | Frequency: 2.4 GHz (802.11b/g/n) |
| Wi-Fi feature | RX Sensitivity: -95 dBm (Min) |
| Wi-Fi feature | TX Power: 20 dBm (Max) |
| Wi-Fi feature | Operation channels: 2.4 GHz: 1-13 |
| LoRa feature | SX1302 Mini PCIe card |
| LoRa feature | 8 Channels |
| LoRa feature | RX Sensitivity: -139 dBm (Min) |
| LoRa feature | TX Power: 27 dBm (Max) |
| LoRa feature | Frequency: EU433/CN470/EU868/US915/AS923/AU915/IN865/KR920 |
| Cellular | Supports Quectel EG95-E/EG95-NA (IoT/M2M -optimized LTE Cat 4 Module) |
| Cellular | EG95-E for EMEA Region |
| Cellular | - LTE FDD: B1/B3/B7/B8/B20/B28A |
| Cellular | - WCDMA: B1/B8 |
| Cellular | - GSM/EDGE: B3/B8 |
| Cellular | EG95-NA for North America Region |
| Cellular | - LTE FDD: B2/B4/B5/B12/B13 |
| Cellular | - WCDMA: B2/B4/B5 |
| Cellular | Optional supports other PCIe LTE module for Global Region |
| Power supply | DC 12 V - 1 A |
| Power supply | PoE (IEEE 802.3 af), 36~57 VDC |
| Power consumption | 12 W (typical) |
| ETH | RJ45 (10/100 M) |
| Console | Type-C USB |
| Antenna | LoRa: RP-SMA female connector |
| Antenna | LTE: Internal antenna |
| Antenna | Wi-Fi: Internal antenna |
| LEDs | POWER LED |
| LEDs | Breathing LED (Top side) |
| LEDs | ETH LED (On ETH connector) |
| LEDs | LoRa LED |
| LEDs | WLAN LED |
| LEDs | LTE LED |
| Ingress protection | IP30 |
| Enclosure material | Plastic |
| Weight | 0.3 kg |
| Dimension | 166x127x36 mm |
| Operating temperature | -10 to 55 ˚C |
| Installation method | Wall mounting |

#### RF Specifications

##### Wi-Fi Radio Specifications

| Feature | Specifications |
| --- | --- |
| Wireless Standard | IEEE 802.11b/g/n |
| Operating Frequency | ISM band: 2.412~2.472 GHz |
| Operation Channels | 2.4 GHz: 1-13 |
| Transmit Power(The max power maybe differentdepending on local regulations) - per chain | 802.11b |
| Transmit Power(The max power maybe differentdepending on local regulations) - per chain | 19 dBm @1 Mbps |
| Transmit Power(The max power maybe differentdepending on local regulations) - per chain | 19 dBm @11 Mbps |
| Transmit Power(The max power maybe differentdepending on local regulations) - per chain | 802.11g |
| Transmit Power(The max power maybe differentdepending on local regulations) - per chain | 18 dBm @6 Mbps |
| Transmit Power(The max power maybe differentdepending on local regulations) - per chain | 16 dBm @54 Mbps |
| Transmit Power(The max power maybe differentdepending on local regulations) - per chain | 802.11n (2.4G) |
| Transmit Power(The max power maybe differentdepending on local regulations) - per chain | 18 dBm @MCS0 (HT20) |
| Transmit Power(The max power maybe differentdepending on local regulations) - per chain | 16 dBm @MCS7 (HT20) |
| Transmit Power(The max power maybe differentdepending on local regulations) - per chain | 17 dBm @MCS0 (HT40) |
| Transmit Power(The max power maybe differentdepending on local regulations) - per chain | 15 dBm @MCS7 (HT40) |
| Receiver Sensitivity(Typical) | 802.11b |
| Receiver Sensitivity(Typical) | -95 dBm @1 Mbps |
| Receiver Sensitivity(Typical) | -88 dBm @11 Mbps |
| Receiver Sensitivity(Typical) | 802.11g |
| Receiver Sensitivity(Typical) | -90 dBm @6 Mbps |
| Receiver Sensitivity(Typical) | -75 dBm @54 Mbps |
| Receiver Sensitivity(Typical) | 802.11n (2.4G) |
| Receiver Sensitivity(Typical) | -89 dBm @MCS0 (HT20) |
| Receiver Sensitivity(Typical) | -72 dBm @MCS7 (HT20) |
| Receiver Sensitivity(Typical) | -86 dBm @MCS0 (HT40) |
| Receiver Sensitivity(Typical) | -68 dBm @MCS7 (HT40) |

##### LoRa Radio Specifications

| Feature              | Specifications                                  |
| -------------------- | ----------------------------------------------- |
| Operating Frequency  | EU433/CN470/EU868/US915/AS923/AU915/IN865/KR920 |
| Transmit Power       | 27 dBm (Max)                               |
| Receiver Sensitivity | -139 dBm (Min)                             |

##### LTE Radio Specifications

| Feature                          | Specification                                                                                                   |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| EG95-E for EMEA Region           | LTE FDD:  B1/B3/B7/B8/B20/B28A
WCDMA:  B1/B8
GSM/EDGE:  B3/B8                                         |
| EG95-NA for North America Region | LTE FDD:  B2/B4/B5/B12/B13
WCDMA:  B2/B4/B5
Optional supports other PCIE LTE module for Global Region |

#### Electrical Requirements

The Gateway comes with a 12 V-1 A power adaptor. It is also fully compatible with PoE (IEEE  802.3af), 36~57 V<sub>DC</sub>.

The typical power consumption is 12 W.

#### Environmental Requirements

The casing is IP30 rated and is made of plastic. There are holes for a mounting bracket on the back, in order to simplify wall mounting. The enclosure, while robust, is not meant for outdoor deployment and should be kept away from moisture.

| Parameter             | Value             |
| --------------------- | ----------------- |
| Dimensions            | 66x127x36 mm |
| Weight                | 0.3 kg       |
| Operating temperature | -10 to 55 °C |

### Firmware

The firmware sits on OpenWRT, which makes it possible to customize it. There is a Web UI for easy configuration and management of the device, as well as the possibility for SSH2 management.

| Model                       | Firmware Version | Source                                                                                     |
| --------------------------- | ---------------- | ------------------------------------------------------------------------------------------ |
| RAK7268 WisGate Edge Lite 2 | WisGateOS V1.3.9 | [Download](https://downloads.rakwireless.com/LoRa/WisGateOS/WisGateOS_Latest_Firmware.zip) |

### Software

#### Software Features

| LoRaWAN                       | Network            | Management                            |
| ----------------------------- | ------------------ | ------------------------------------- |
| Supports class A, C           | Wi-Fi AP mode      | WEB management                        |
| LoRa package forward          | Uplink backup      | SSH2                                  |
| Country code setup            | 802.1q             | Firmware update                       |
| TX Power setup                | DHCP Server/Client | NTP                                   |
| Data logger                   | Router module NAT  | Configuring the LoRa Packet Forwarder |
| Statistics                    | Firewall           | Build-in Server                       |
| Location setup                | LTE APN setup      | OpenVPN, Ping Watch Dog               |
| Server address and Port setup |                    | MQTT Bridge                           |

## Certification

### Certifications
- **ANATEL:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_ANATEL_Certification.zip
- **CE:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_RAK7268V2_RAK7268C_RAK7268CV2_CE_Certification.pdf
- **CE:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268C_CE_Certification.pdf
- **FCC:** https://downloads.rakwireless.com/LoRa/RAK7268V2/Certification/RAK7268_RAK7268V2_FCC_Certification.pdf
- **FCC:** https://downloads.rakwireless.com/LoRa/RAK7268V2/Certification/RAK7268C_RAK7268CV2_FCC_Certification.pdf
- **ISED:** https://downloads.rakwireless.com/LoRa/RAK7268V2/Certification/RAK7268_RAK7268V2_IC_Certification.pdf
- **ISED:** https://downloads.rakwireless.com/LoRa/RAK7268V2/Certification/RAK7268C_RAK7268CV2_IC_Certification.pdf
- **JRL:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_RAK7268V2_RAK7268C_RAK7268CV2_JRL_Certification.pdf
- **JTBL:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_RAK7268V2_JTBL_Certification.pdf
- **KC:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_KC_Certification.pdf
- **KC:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268C_KC_Certification.pdf
- **RCM:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_RAK7268C_RCM_Certification.pdf
- **REACH:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268C_RAK7268CV2_RAK7268_RAK7268V2_REACH_Report.pdf
- **ROHS:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268C_RAK7268CV2_RAK7268_RAK7268V2_RoHS_Report.pdf
- **RSM:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_RAK7268V2_RAK7268C_RAK7268CV2_RSM_Certification.pdf
- **SRRC:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_SRRC_Certification.pdf
- **SUBTEL:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_SUBTEL_Certification.pdf
- **UKCA:** https://downloads.rakwireless.com/LoRa/RAK7268/Certification/RAK7268_RAK7268V2_RAK7268C_RAK7268CV2_UKCA_Certification.pdf

### FCC Caution

Any changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate the equipment.

This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

:::tip NOTE

This equipment has been tested and found to comply with the limits for a Class B digital device, according to part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation. This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used following the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:

1. Reorient or relocate the receiving antenna.
2. Increase the separation between the equipment and receiver.
3. Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
4. Consult the dealer or an experienced radio/TV technician for help.

:::

### FCC Radiation Exposure Statement

This equipment complies with FCC radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 20 cm between the radiator and your body.

### ISEDC Warning

This device complies with Innovation, Science, and Economic Development Canada licence-exempt RSS standard(s). Operation is subject to the following two conditions:

1. This device may not cause interference;

2. This device must accept any interference, including interference that may cause undesired operation of the device.

Le présent appareil est conforme aux CNR d' Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes :

1. l'appareil nedoit pas produire de brouillage, et

2. l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

The device complies with RF exposure guidelines, users can obtain Canadian information on RF exposure and compliance. The minimum distance from the body to use the device is 20 cm.

Le présent appareil est conforme Après examen de ce matériel aux conformité ou aux limites d’intensité de champ RF, les utilisateurs peuvent sur l’exposition aux radiofréquences et la conformité and compliance d’acquérir les informations correspondantes. La distance minimale du corps à utiliser le dispositif est de 20 cm.
