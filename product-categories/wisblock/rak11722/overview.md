---
slug: /product-categories/wisblock/rak11722/overview/
title: RAK11722 WisBlock LPWAN Module
description: The RAK11722 is a WisBlock Core module within the RAK WisBlock ecosystem, featuring firmware based on RUI3. It enhances the series with an Ambiq Apollo3 SoC MCU that supports Bluetooth 5.0 (BLE) and integrates the latest LoRa transceiver from Semtech, the SX1262.
image: "https://images.docs.rakwireless.com/wisblock/rak11722/rak11722.png"
keywords:
    - RAK11722
    - wisblock
    - Ambiq
    - Apollo3 Blue
    - AMA3B1KK-KBR-B0
    - Semtech
    - SX1262
sidebar_label: Product Overview    
---

# RAK11722 WisBlock LPWAN Module

Thank you for choosing **RAK11722 WisBlock LPWAN Module** in your awesome IoT Project! To help you get started, we have provided you with all the necessary documentation for your product.

- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak11722/at-command-manual/" target="_blank">AT Command Manual</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak11722/datasheet/" target="_blank">Datasheet</a>
- <a href="https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK11722.stp" target="_blank">RAK11722 3D Model</a>
- <a href="https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/M40S1003K6M.stp" target="_blank">40-Pin Male Connector 3D File</a>

## Product Description

The RAK11722 WisBlock Core module is a RAK11720 stamp module with an expansion PCB and connectors compatible with the WisBlock Base Boards. It allows an easy way to access the pins of the RAK11720 module to simplify development and testing processes.

The module itself comprises a RAK11720 as its main component. The RAK11720 is a combination of an Ambiq Apollo3 Blue AMA3B1KK-KBR-B0 SoC MCU and an SX1262 LoRa chip. It features ultra-low power consumption of 2.37 uA during sleep mode and high LoRa output power up to 22 dBm during a transmission mode.

Additionally, RAK11722 complies with LoRaWAN 1.0.3 protocols and supports LoRa point-to-point communication. The RF communication characteristic of the module (LoRa + BLE) makes it suitable for a variety of applications. These include home automation, sensor networks, building automation, and personal area network applications. Examples are health/fitness sensors, monitors, and more.

## Product Features

- Based on **AMA3B1KK-KBR-B0** and **SX1262**
- ARM Cortex-M4F
- 1 MB Flash and 348 KB SRAM
- **LoRaWAN 1.0.3** specification compliant
- **Supported bands**: EU433, CN470, IN865, EU868, AU915, US915, KR920, RU864, and AS923-1/2/3/4
- LoRaWAN Activation by OTAA/ABP
- LoRa Point-to-Point (P2P) communication
- Custom firmware using Arduino via RUI3 API
- Easy-to-use AT Command set via UART interface
- **I/O ports**: UART/I2C/SPI/ADC/GPIO
- Long-range - greater than 10 km with optimized antenna
- Ultra-low-power consumption of 2.37 μA in sleep mode
- **Supply Voltage**: 1.8 V ~ 3.6 V
- **Temperature range**: -40° C ~ 85° C

## Prerequisites

To use a **RAK11722**, you need at least a **WisBlock Base** to plug the module in. **WisBlock Base** is the power supply for the **RAK11722** module and has the programming/debug interface.

:::warning
- Make sure to fix the module with the screws to ensure proper function.
- When using the LoRa or Bluetooth Low Energy transceivers, ensure that an antenna is always connected. Using these transceivers without an antenna can damage the system.
:::

:::tip Note
For CE and FCC certifications we provide an AT command guide.    
You can find it in our <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/certification-guide" target="_blank">RUI3 documentation</a> or get it from our <a href="https://downloads.rakwireless.com/#RUI/RUI3/Certification%20Guide/" target="_blank">Download Center</a>.    
::: 

