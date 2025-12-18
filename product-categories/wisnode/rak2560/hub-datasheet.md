---
slug: /product-categories/wisnode/rak2560/hub-datasheet/
title: RAK2560 WisNode Sensor Hub Datasheet
description: Provides comprehensive information about your RAK2560 WisNode Sensor Hub to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisnode/rak2560/rak2560.jpg"
keywords:
    - datasheet
    - wisnode
    - rak2560
    - sensor hub
sidebar_label: Hub Datasheet
---

# RAK2560 WisNode Sensor Hub Datasheet

## Overview

### Description

The RAK2560 WisNode Sensor Hub is a modular sensor ecosystem consisting of the main body and multiple pre-configured sensor probes. It has pluggable and interchangeable probes and supports the integration of third-party sensors. These characteristics make the Sensor Hub an ideal and adaptable solution platform for a wide range of IoT applications requiring environmental monitoring.

The Sensor Hub is housed in a robust, waterproof enclosure with two (2) sensor probe ports for connecting sensors or an external power source, such as a solar panel. It can operate with an external power supply or in full battery mode, depending on the deployment location.

With the use of the WisToolBox app, the Sensor Hub and its sensor probes can be easily configured. The application is available on mobile and desktop.

### Product Features

- LoRa 868-930 MHz support
- Based on [RAK4630](https://docs.rakwireless.com/product-categories/wisduo/rak4630-module/overview/#product-description) (MCU: nRF52840, Radio Chip: SX1262)
- [RUI3](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/#overview) - based code
- Auto-detection of the power source
- Auto-detection of the Sensor Probes
- 2~4 pcs 3.6 V ER18505 4000 mAh Li-SOCl2 primary lithium batteries
- 12 V<sub>DC</sub> over power supply or solar panel
- NB-IoT interface module ([RAK5860](https://docs.rakwireless.com/product-categories/wisblock/rak5860/overview/)) support (optional)
- Embedded antenna
  - High efficiency (over 75%) LoRa Band 860~930 MHz
  - Support 700 ~ 960 MHz and 1700 ~ 2170 MHz.
- NFC tag for power on and smart connect over BLE
- Prevent theft via the hall effect sensor on the exclusive mounting bracket
- IP66-rated waterproof enclosure
- Sensor ports can host multiple Sensor Probes via Probe Splitters

## Specifications

### Overview

#### Main Specifications

| Feature              | Specification                                                                                                                                                                                                                 |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Wireless technology  | Support LoRa end node (915 MHz / 868 MHz)
Support Bluetooth for easy setup
Support NFC for easy setup                                                                                           |
| Antenna              | 1 x internal: high-gain and high-efficiency LoRa antenna (also support NB-IoT)
1 x internal: NFC antenna
1 x internal: Bluetooth antenna                                                                            |
| External interfaces  | 2 x SP11 connector (IP67) for multiple-purpose sensors
The SP11 supports a 12 V power adapter and a solar panel kit for external power                                                                              |
| Weatherproof design  | IP66 rated
SP11 connector for professional installation and fast deployment
Plastic top (UL-746C), UV-resistant
Metal body, die-casted, with solid and good thermal dissipation
Internal gasket (UL-94V0) |
| Power source         | Supports the following power source:<ul><li>+12 V<sub>DC</sub> at 1 A (12 W) power adapter</li><li>12 V<sub>DC</sub> solar panel
</li><li>4 x ER18505 Li-SOCl2 batteries (4000 mAh) </li></ul>  |
| Mounting options     | Solid mounting kit for wind speed load of 215 km/h
Pole-mount (vertical or horizontal)
Wall-mount                                                                                                              |
| Enclosure dimensions | 120 x 80 x 39 mm                                                                                                                                                                                     |
| Surge and ESD        | 6 kV surge and 8 kV ESD protection                                                                                                                                                                                  |
| Working environment  | -30° C to +60° C
Suitable for outdoor and indoor use                                                                                                                                                           |
| Storage temperature  | -40° C to +80° C                                                                                                                                                                                                    |

#### Dimensions

The dimensions for the body of the Sensor Hub are 120 x 80 x 39 mm. There are two equal physical ports for Sensor Probe—the DC supply and the Probe IO at the bottom of the enclosure.

> **Image:** RAK2560 WisNode Sensor Hub dimensions

#### Block Diagram

The **RAK2560 Sensor Hub** uses RAK4630 as a core. The One-wire protocol provides easy connection and easy assembly. The device supports two kinds of wireless communication, LoRa, and NB-IoT that are switchable. A hybrid power system provides more possibilities to customize the Hub to correspond to the customer/market demands.

> **Image:** RAK2560 WisNode Sensor Hub block diagram

### Hardware

The hardware specification is categorized into five (5) parts. It shows the pinouts of the sensor hub and their corresponding functions and diagrams. It also covers the RF, power supply, and environmental characteristics that include the tabular data of the functionalities and standard values of the RAK2560 WisNode Sensor Hub.

#### Pin Definition

Each of the two ports has five (5) pins and they are the same for both ports.

> **Image:** RAK2560 WisNode Sensor Hub pin definition

| Pin No. | Name          | Type | Description                   | Remarks                                                       |
| ------- | ------------- | ---- | ----------------------------- | ------------------------------------------------------------- |
| 1       | Vin           | PI   | 12 V<sub>DC</sub> supply | Input 5~16 V                                             |
| 2       | GND           | -    | Ground                        | -                                                             |
| 3       | Reserved      | IO   | Not defined                   | Reserved for future use                                       |
| 4       | Vcc_Probe     | PO   | Power supply for the probe    | 3.3 V<sub>DC</sub> support mode; 3.4 V battery mode |
| 5       | One-wire UART | IO   | Communication with probe      | Applications                                                  |

#### RF Characteristics
##### Operating Frequencies

The board supports the following LoRa frequency channels, allowing easy configuration while building the firmware from the source code.

| Region        | Frequency    |
| ------------- | ------------ |
| Europe        | EU868        |
| North America | US915        |
| Asia          | AS923, AS920 |
| Australia     | AU915        |
| Korea         | KR920        |
| India         | IN865        |

:::tip NOTE
The frequency band parameters vary by region and comply with local regulations. Keep your location in mind when placing an order.
:::

#### Power Supply

The **RAK2560 Sensor Hub** must be supplied through the 12 V SP11 pins by a DC power supply or 4 x EVE ER18505 3.6 V Lithium 4000 mAh battery and the voltage must be stable.

##### Power Consumption

| Mode               | Condition                                                    | Min         | Typical      | Max         |
| ------------------ | ------------------------------------------------------------ | ----------- | ------------ | ----------- |
| Active mode (TX)   | The power of TX channel is 20 dBm and 3.6 V supply | 110 mA | 120 mA  | 130 mA |
| Active mode (RX)   | TX disabled and RX enabled                                   | 7.5 mA | 8.55 mA | 15 mA  |
| Active mode (idle) | TX disabled and RX disabled. MCU wake up                     | 3.0 mA | 3.3 mA  | 3.6 mA |
| Sleep mode         | Sleep mode                                                   | 13 uA  | 15 uA   | 20 uA  |

#### Environmental Requirements

##### Operating Conditions

| Parameter                    | Min         | Typical     | Max         |
| ---------------------------- | ----------- | ----------- | ----------- |
| Normal operating temperature | –30° C | +25° C | +80° C |

#### Sensor Connection Diagram

The **RAK2560** can support both Sensor Probes and Probe IO in all possible combinations.

:::tip NOTE
If you want to add a Probe IO to your setup, the Sensor Hub must be supplied by an external 12 V<sub>DC</sub> power source.
:::

> **Image:** RAK2560 WisNode Sensor Hub connection schematics

### Software

| Supported Protocol | Description                                                                            |
| ------------------ | -------------------------------------------------------------------------------------- |
| NFC                | For waking up the Sensor Hub via the WisToolBox App                                    |
| BLE                | For pairing the Sensor Hub to a mobile device for configuration via the WisToolBox App |
| LoRaWAN            | For data transfer, provided by the RAK4630 WisBlock LPWAN module                       |
| NB-IoT             | For data transfer, optional, provided by the RAK5860 WisBlock NB-IoT interface module  |
| One-wire UART      | For communication between the Sensor Probe/Probe IO and the Hub                        |

### Firmware

Download the latest firmware version of RAK2560 Sensor Hub in the table provided below.

|       Model        |    Version     |                                             Firmware                                              |
| :----------------: | :------------: | :-----------------------------------------------------------------------------------------------: |
| RAK2560 Sensor Hub | Release 1.2.27 | [Download](https://downloads.rakwireless.com/LoRa/SensorHub/Firmware/RAK2560_Latest_Firmware.zip) |

### Certification

### Certifications
- **CE:** https://downloads.rakwireless.com/LoRa/SensorHub/Certification/SensorHub_RAK2560_RAK2560C_CE_Certification.pdf
- **FCC:** https://downloads.rakwireless.com/LoRa/SensorHub/Certification/SensorHub_RAK2560_RAK2560C_FCC_Certification.pdf
- **ISED:** https://downloads.rakwireless.com/LoRa/SensorHub/Certification/SensorHub_RAK2560_RAK2560C_ISED_Report.pdf

