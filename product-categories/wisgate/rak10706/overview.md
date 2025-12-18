---
slug: /product-categories/wisgate/rak10706/overview/
title: RAK10706 Signal Meter for LoRa
description: The RAK10706 is a basic signal meter. It works in both LoRa P2P and LoRaWAN mode.
image: https://images.docs.rakwireless.com/wisnode/rak10706/rak10706.png
keywords:
    - lorawan
    - lora p2p
    - signal meter
    - rak10706
    - wisnode
    - coverage tester
sidebar_label: Product Overview
download: true
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK10706 Signal Meter for LoRa

Thank you for choosing **RAK10706 Signal Meter for LoRa** in your awesome IoT project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

* [Quick Start Guide](https://docs.rakwireless.com/product-categories/wisgate/rak10706/quickstart/)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisgate/rak10706/datasheet/)

:::tip NOTE
- The [source code of RAK10706](https://github.com/RAKWireless/RAK10706-Signal-Meter) is open-sourced.
- The device may need to be charged first if it’s new out of the box, as the battery could have been drained during shipping.
:::

## Product Description

The **RAK10706 Signal Meter for LoRa** operates in LoRa P2P and LoRaWAN modes, with an OLED display and single-button interface. It’s a ready-to-use WisNode for evaluating LoRaWAN networks, featuring a GNSS, antenna, and display showing gateway count, distance, RSSI, and SNR. It logs test results in CSV format on an SD card and is powered by a rechargeable battery. The device charges via USB Type-C and has a user button and On/Off switch.

## Product Features

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

## Difference Between the RAK10706 Signal Meter and the RAK10701 Field Tester

One of the advantages of the RAK10706 Signal Meter is that there is no backend installations required on LoRaWAN servers (e.g., Helium, TTN, Chirpstack) in LinkCheck Packet mode. It works with any LoRaWAN server, such as AWS IoT Core or Actility.

The RAK10706 uses LinkCheckReq to gather information about the connection to the gateway(s). This helps monitor connectivity. With LinkCheck, the LoRaWAN server reports the number of gateways and the demodulation margin. The demodulation margin is calculated by the LoRaWAN server. It provides insights into the received signal quality. A higher margin indicates better signal quality.<br/>
Extract from the LoRaWAN 1.0.3 Specification:

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10706/lorawan-linkcheck.png"
  width="70%"
  caption="LinkCheck explanation"
/>

## Prerequisites

To use the **RAK10706**, you need the following:
- LoRaWAN LinkCheck test mode
   - To be in a coverage of a LoRaWAN gateway registered to a supported LoRaWAN Network Server. 
   - RAK10706 must registered as a device on the LoRaWAN Network Server.
   - RAK10706 must be sufficiently charged.
- LoRa P2P test mode
   - RAK10706 must be setup for same P2P frequency, SF, CR, BW, Preamble Length as other P2P nodes in the network.

<RkBottomNav/>