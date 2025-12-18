---
slug: /product-categories/wisgate/rak10701-h/datasheet/
title: RAK10701-H Field Mapper for LoRaWAN Datasheet
description: Provides comprehensive information of your RAK10701-H Field Mapper for Helium Network to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisnode/rak10701/rak10701-h.png
keywords:
    - lorawan
    - field tester
    - rak10701-h
    - datasheet
sidebar_label: Datasheet
download: true
---

# RAK10701-H Field Mapper for Helium Datasheet

## Overview

### Description

The **RAK10701-H Field Mapper for Helium Network** is a ready-to-use device for evaluating the coverage of the Helium Network. It is a plug-and-play device with its included DC (data credits), which allows you to use it immediately without needing extra configurations. It has a GNSS receiver for checking its current location and a touchscreen LCD for the user interface. It shows the number of hotspots the device can reach and other parameters like approximate distance, RSSI, and SNR.

:::warning
The latest RAK10701 Field Mapper firmware (custom mode) only works on the following LoRaWAN Network Servers: **Helium**, **The Things Network**, and **Chirpstack**.  
:::

:::tip NOTE
The [source code of RAK10701](https://github.com/RAKWireless/RAK10701-Field-Tester) is open-sourced (except the RUI3 APIs).

The device has to be charged first if it comes fresh from shipping. There is a possibility that the battery was drained during its transport.
:::

### Features

- Supports LoRaWAN regions: RU864, IN865, EU868, US915, AU915, KR920, AS923-1/2/3/4
- Compatible with LoRaWAN 1.0.3
- Already registered on the Helium console
- Free DC (data credits) to use the Field Mapper for Helium
- Shows the number of hotspots in the range
- Shows min and max RSSI levels
- Shows min and max distance to hotspots in range
- Discovery mode to create a map showing the Field Mapper location and the location of the detected Helium hotspots
- Compatible with WisToolBox and allows wireless configuration via BLE
- Powered by 3200 mAh battery
- Rechargeable over a USB Type-C connector
- 320x240 TFT touchscreen
- 2.0 dBi external antenna via RP-SMA connector
- Operating Temperature: -10° C ~ 60° C
- Storage Temperature: -40° C ~ 80° C

## Specifications

### Overview

RAK10701-H Field Mapper for Helium Network with the external antenna.

> **Image:** RAK10701-H Field Mapper for Helium Network

### Hardware

The hardware specification is categorized into five (5) parts. It shows the interfacing of the tracker. It also covers the rf, antennas, electrical, environmental, and mechanical parameters that include the tabular data of the functionalities and standard values of the RAK10701-H Field Mapper for Helium Network.

#### Interfaces

The RAK10701-H Field Mapper for Helium Network has four interfaces which are the touch screen LCD, external button, antenna port, and USB connector.

##### Touchscreen TFT LCD

The touchscreen LCD is the main interface of the device. Most of the user interaction is done via the touchscreen LCD.

> **Image:** RAK10701-H front view with an LCD screen

You can interact with the device and check the data needed on your LoRaWAN network field testing. The icons highlighted in the red box are the areas responsive to touch. Other parts of the screen will not be responsive to any touch input.

> **Image:** RAK10701-H home display

:::tip NOTE
The complete details on different pages of the screens are discussed in the [RAK10701-H Quick Start Guide](https://docs.rakwireless.com/product-categories/wisgate/rak10701-h/quickstart/).
:::

##### External Button

There is one external button on RAK10701, which can be used in various scenarios.

1. Turning on and off (holding for five seconds)
2. Forced uplink (double-click)
3. Sleep and wake-up (single click)

> **Image:** RAK10701-H useable button

##### Antenna RP-SMA Connector

On top of the RAK10701-H Field Mapper for Helium Network is an RP-SMA port for the external antenna.

> **Image:** RAK10701-H RP-SMA antenna port

The antenna included in the RAK10701-h has a 2.0 dBi gain. You can put a different antenna as long as it can fit on the RP-SMA connector.

> **Image:** 2.0 dBi antenna

:::tip NOTE
Detailed information about the LoRa antenna can be found on the datasheet:

- [9xx MHz Antenna](https://downloads.rakwireless.com/Accessories/Antenna/SMA-Antenna/RPSMA-J-915MHz_LoRa_Antenna_Specifications.pdf)
- [8xx MHz Antenna](https://downloads.rakwireless.com/Accessories/Antenna/SMA-Antenna/RPSMA-J-868MHz_LoRa_Antenna_Specifications.pdf)
:::

##### USB Type-C for Charging and WisToolBox Configuration

There is also a USB interface on the RAK10701. You can use [WisToolBox](https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/overview/) software to configure the devices via USB connection. You also have the option to configure the device wirelessly via BLE connection using the [WisToolBox Mobile App](https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/wistoolbox-mobile/) compatible with iOS and Android.

> **Image:** USB Type-C connector access

#### RF Characteristics

##### LoRaWAN Operating Frequencies

The RAK10701-H Field Tester for LoRaWAN supports the regional bands shown in the table below. When purchasing a RAK10701, pay attention to specifying the correct variant for your region.

| Region        | Frequency (MHz) | RAK10701-H Field Mapper for Helium Network |
| ------------- | --------------- | ------------------------------------------ |
| Russia        | RU864           | 8xx MHz version                            |
| India         | IN865           | 8xx MHz version                            |
| Europe        | EU868           | 8xx MHz version                            |
| North America | US915           | 9xx MHz version                            |
| Canada        | US915           | 9xx MHz version                            |
| Australia     | AU915           | 9xx MHz version                            |
| Korea         | KR920           | 9xx MHz version                            |
| Asia          | AS923-1/2/3/4   | 9xx MHz version                            |

##### GPS Antenna

| Items     | Parameter        |
| --------- | ---------------- |
| Frequency | 1575.42 MHz |

#### Electrical Characteristics

##### Working Mode

| Mode      | Condition | Power Consumption |
| --------- | --------- | ----------------- |
| Idle Mode | LCD on    | 120 mA       |
|           | LCD off   | 60 mA        |

##### Battery Supply

The RAK10701-H Field Mapper for Helium Network is equipped with a built-in rechargeable 3.7 V Li-ion battery with 3200 mAh capacity. This can be charged via a USB Type-C connector interface.

#### Environmental Characteristics

The table below lists the operation and storage temperature requirements.

| Parameter             | Min.        | Typical     | Max.        |
| --------------------- | ----------- | ----------- | ----------- |
| Storage Temp. Range   | -40° C | +25° C | +80° C |
| Operation Temp. Range | -10° C | +25° C | +60° C |

#### Mechanical Characteristics

- Dimensions: 100 mm x 75 mm x 38 mm
- Weight: approximately 8.6 oz (243.8 g) without battery

### Firmware

Download the latest firmware version of RAK10701-H via the <a href="https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/overview"> WisToolBox</a>.

