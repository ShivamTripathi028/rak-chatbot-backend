---
slug: /product-categories/wisgate/rak10706/datasheet/
title: RAK10706 Signal Meter for LoRa Datasheet
description: Provides comprehensive information of your RAK10706 Signal Meter for LoRa to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: https://images.docs.rakwireless.com/wisnode/rak10706/rak10706.png
keywords:
    - datasheet
    - lorawan
    - lora p2p
    - signal meter
    - rak10706
    - wisnode
    - coverage tester
sidebar_label: Datasheet
download: true
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK10706 Signal Meter for LoRa Pro Datasheet

## Overview

### Description

The **RAK10706 Signal Meter for LoRa** operates in LoRa P2P and LoRaWAN modes, with an OLED display and single-button interface. It’s a ready-to-use WisNode for evaluating LoRaWAN networks, featuring a GNSS, antenna, and display showing gateway count, distance, RSSI, and SNR. It logs test results in CSV format on an SD card and is powered by a rechargeable battery. The device charges via USB Type-C and has a user button and On/Off switch.

:::tip NOTE
- The RAK10706 Signal Meter firmware works with any LoRaWAN Network Servers that supports LinkCheckReq.  
- The [source code of RAK10706](https://github.com/RAKWireless/RAK10706-Signal-Meter) is open-sourced.
- The device has to be charged first if it comes fresh from shipping. There is a possibility that the battery was drained during its transport.
:::

### Features

- Supports LoRaWAN regions: RU864, IN865, EU868, US915, AU915, KR920, & AS923-1/2/3/4
- Supports LoRa P2P from 830 to 960&nbsp;MHz frequencies
- Compatible with LoRaWAN 1.0.3
- Offers different test modes
   - LoRaWAN LinkCheck
      - Works with any LoRaWAN server supporting LinkCheckRequest
      - Does not require any backend installation
      - Shows Number of gateways in range
      - Shows signal quality at gateways as Demodulation Margin
      - Shows RX SNR and RSSI of downlink from LNS
      - Shows sent and lost packet count
   - LoRa P2P
      - Works in any LoRa P2P setup
      - Shows received packet count
      - Can send out test packets to other LoRa P2P nodes
- WisToolBox compatible
   - Allows wireless configuration via BLE
- Powered by 3,200&nbsp;mAh battery
- Rechargeable over a USB Type-C connector
- 1.3" OLED display
- Single button UI and device control
- 2.3&nbsp;dBi external antenna via RP-SMA connector
- Operating Temperature: -10°&nbsp;C ~ 60°&nbsp;C
- Storage Temperature: -40°&nbsp;C ~ 80°&nbsp;C


## Specifications

### Overview

RAK10706 Signal Meter for LoRa with an external antenna.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/rak10706-view-1.png"
  width="40%"
  caption="RAK10706 Signal Meter for LoRa"
/>

### Hardware

The hardware specification is categorized into five (5) parts. It shows the interfacing of the tracker. It also covers the rf, antennas, electrical, environmental, and mechanical parameters that include the tabular data of the functionalities, and standard values of the RAK10706 Signal Meter for LoRa.

#### Interfaces

The RAK10706 Signal Meter for LoRa has multiple interfaces, which are:
- OLED display
- external button
- antenna port
- SD card slot
- USB connector
- RESET button
- Device and charging status indicators

##### OLED display

The OLED display is the visual interface of the device. Most of the test results are displayed on the OLED display.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/rak10706-oled.png"
  width="75%"
  caption="RAK10706 front view with the OLED screen"
/>

:::tip NOTE
The complete details on different pages of the screen are discussed in the [RAK10706 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisgate/rak10706/quickstart/).
:::

##### External Button

There is one external button on RAK10706 which can be used in various scenarios.

1. Turn display on and off (holding for five seconds)
2. Forced uplink (double-click)
3. Forced uplink with DR sweep
4. Open the device settings UI

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/rak10706-button.png"
  width="50%"
  caption="RAK10706 button"
/>

##### Antenna RP-SMA Connector

On top of the RAK10706 Signal Meter for LoRa is an RP-SMA port for the external antenna.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/rak10706-antenna.png"
  width="40%"
  caption="RAK10706 RP-SMA antenna port"
/>

The RAK10706 package includes one antenna with a 2.3&nbsp;dBi gain.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701/datasheet/interface-blade-antenna.png"
  width="30%"
  caption="2.3 dBi antenna"
/>

:::tip NOTE
Detailed information about the LoRa antenna can be found on the datasheet:

- [9xx MHz Antenna](https://docs.rakwireless.com/product-categories/accessories/rakarj16/overview/)
- [8xx MHz Antenna](https://docs.rakwireless.com/product-categories/accessories/rakarj17/overview/)
:::

##### SD card slot

On top of the RAK10706 Signal Meter for LoRa is an SD card slot.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/rak10706-sd-card.png"
  width="40%"
  caption="RAK10706 SD card port"
/>

:::warning IMPORTANT
The SD card slot is covered with a flexible rubber lid to protect the device from the environment. The rubber lid does not protect against water intrusion.
:::

##### USB Type-C for Charging, WisToolBox Configuration, Status Indicators and Reset Button

There is also a USB interface on RAK10706. You can use [WisToolBox](https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/overview/) software to configure the devices via USB connection. You also have the option to configure the device wirelessly via BLE connection using the [WisToolBox Mobile App](https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/wistoolbox-mobile/). The WisToolBox Mobile App compatible with iOS and Android. 

Next to the USB connector is a RESET button (requires a pin to use), and status indicators for charging and activities.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/rak10706-usb-open.png"
  width="40%"
  caption="RAK10706 USB-C port"
/>

:::warning IMPORTANT
The USB connector slot is closed with a flexible rubber lid to protect the device from the environment. The rubber lid does not protect against water intrusion.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/rak10706-usb-closed.png"
  width="40%"
  caption="RAK10706 USB-C port closed"
/>

#### WisBlock Modules

The RAK10706 is built with WisBlock BaseBoard and WisBlock modules.    
The main part is the [RAK19026 Base Board](https://docs.rakwireless.com/product-categories/meshtastic/wismesh-base/overview/) which includes
- [RAK4630 LoRa module](https://docs.rakwireless.com/product-categories/wisduo/rak4630-module/overview/)
- u-blox ZOE-M8Q GNSS module (as used in the [RAK12500 WisBlock Sensor module](https://docs.rakwireless.com/product-categories/wisblock/rak12500/overview/))
- Voltage regulator and battery charger
- 1.3" OLED display
- Battery connector 
- 5&nbsp;V supply connector for solar panel or external power supply
- ON/OFF switch
- User button

On the Base Board a [RAK15002 SD-Card](https://store.rakwireless.com/products/sd-card-module-rak15002?utm_source=RAK15002&utm_medium=Document&utm_campaign=BuyFromStore) module is plugged into the IO slot. The SD card is used for data logging.    

An optional [RAK12002 RTC module](https://store.rakwireless.com/products/rtc-module-rak12002?utm_source=RAK12002&utm_medium=Document&utm_campaign=BuyFromStore) is available to provide precise time stamps to the logs.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/rak19026-top.png"
  width="40%"
  caption="RAK19026 top view"
/>
<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/rak19026-bottom.png"
  width="40%"
  caption="RAK19026 bottom view"
/>

#### RF Characteristics

##### LoRaWAN Operating Frequencies

The RAK10706 Signal Meter for LoRa supports the regional bands shown in the table below. When purchasing a RAK10706, pay attention to specifying the correct variant for your region.

| Region        | Frequency (MHz) | RAK10706 Signal Meter for LoRa |
|---------------|-----------------|--------------------------------|
| Russia        | RU864           | 8xx&nbsp;MHz version           |
| India         | IN865           | 8xx&nbsp;MHz version           |
| Europe        | EU868           | 8xx&nbsp;MHz version           |
| North America | US915           | 9xx&nbsp;MHz version           |
| Canada        | US915           | 9xx&nbsp;MHz version           |
| Australia     | AU915           | 9xx&nbsp;MHz version           |
| Korea         | KR920           | 9xx&nbsp;MHz version           |
| Asia          | AS923-1/2/3/4   | 9xx&nbsp;MHz version           |

##### GPS Antenna

| Items     | Parameter        |
|-----------|------------------|
| Frequency | 1575.42&nbsp;MHz |

#### Electrical Characteristics

<!-- Needs to be confirmed
##### Working Mode

| Mode                 | Condition        | Power Consumption            |
|----------------------|------------------|------------------------------|
| Idle Mode (LoRaWAN)  | OLED On          | ~&nbsp;8&nbsp;mA             |
|                      | OLED Off         | 60&nbsp;mA                   |
| Packet TX (LoRaWAN)  | OLED On          | depends on selected TX power |
|                      | OLED Off         | depends on selected TX power |
| Idle Mode (LoRa P2P) | OLED On          | 120&nbsp;mA                  |
|                      | OLED Off         | 60&nbsp;mA                   |
| Packet TX (LoRa P2P) | OLED On          | depends on selected TX power |
|                      | OLED Off         | depends on selected TX power |
| Location tracking    | GNSS searching   | 120&nbsp;mA                  |
|                      | GNSS maintaining | 60&nbsp;mA                   |
-->

##### Battery Supply

The RAK10706 Signal Meter for LoRa is equipped with a built-in rechargeable 3.7&nbsp;V Li-ion battery with 3200&nbsp;mAh capacity. This can be charged via a USB Type-C connector interface.

#### Environmental Characteristics

The table below lists the operation and storage temperature requirements.

| Parameter             | Min.        | Typical     | Max.        |
|-----------------------|-------------|-------------|-------------|
| Storage Temp. Range   | -40°&nbsp;C | +25°&nbsp;C | +80°&nbsp;C |
| Operation Temp. Range | -10°&nbsp;C | +25°&nbsp;C | +60°&nbsp;C |

:::warning IMPORTANT
The enclosure is made of ABS material. It should be protected from direct sun light and extreme temperatures to avoid damage to the enclosure.
:::

#### Mechanical Characteristics

- Dimensions (without antenna): 102.5&nbsp;mm x 60&nbsp;mm x 28.5&nbsp;mm
<!-- - Weight: approximately ???&nbsp;oz (???&nbsp;g) without battery -->

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/rak10706-dimensions.png"
  width="40%"
  caption="RAK10706 Dimensions"
/>

### Firmware


Download the latest firmware version of RAK10706 from our [Download Center](https://downloads.rakwireless.com/#LoRa/RAK10706/Firmware/) and flash it to the <a href="https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/overview"> WisToolBox</a>.


<RkBottomNav/>