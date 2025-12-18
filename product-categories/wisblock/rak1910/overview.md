---
slug: /product-categories/wisblock/rak1910/overview/
title: RAK1910 WisBlock GNSS Location Module Datasheet
description: RAK1910 is a WisBlock Sensor that extends the WisBlock system with a u-Blox MAX-7Q GPS module. A ready-to-use SW library and tutorial make it easy to build up a GPS-based location tracker.
image: "https://images.docs.rakwireless.com/wisblock/rak1910/rak1910.png"
keywords:
  - wisblock
  - RAK1910
  - u-blox
  - MAX-7Q
sidebar_label: Product Overview
---

# RAK1910 WisBlock GNSS Location Module

Thank you for choosing **RAK1910 WisBlock GNSS Location Module** in your awesome IoT Project! 🎉 To help you get started, we have provided you all the necessary documentation for your product.

* [RAK1910 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak1910/quickstart/)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak1910/datasheet/)
* <a href="https://docs.rakwireless.com/product-categories/wisblock/quickstart/" target="_blank">WisBlock Quick Start Guide</a>
* [WisBlock Source Code Repository](https://github.com/RAKWireless/WisBlock/)
* [RAK1910 3D Model](https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK1910.stp)
* [24-Pin Male Connector 3D File](https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/M24S1003K6M.stp)
* [WisBlock Sensor Tutorial](https://learn.rakwireless.com/hc/en-us/articles/26687819464343-How-To-Make-Your-Own-WisBlock-Sensor-Board)

**Examples**

- For All WisBlock Core Modules:
    * [Sample Code: RAK1910](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK1910_GPS_UBLOX7)
- For WisBlock Core RAK4630:
    * [Sample Code: GPS Tracker](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK4630/solutions/GPS_Tracker)

- **LoRaWAN GPS Tracker Kits Based on WisBlock RAK1910**
    * [LoRaWAN Tracker Kit](https://store.rakwireless.com/collections/kits-bundles/products/wisblock-kit-3-gps-tracker?utm_source=WisBlockKit3&utm_medium=Document&utm_campaign=BuyFromStore)
    * [LoRaWAN Tracker Kit with Solar Panel](https://store.rakwireless.com/collections/kits-bundles/products/wisblock-kit-2-lora-based-gps-tracker-with-solar-panel?utm_source=WisBlockKit2&utm_medium=Document&utm_campaign=BuyFromStore)

## Product Description

The RAK1910 WisBlock GNSS Location Module module, part of the RAK Wireless Wisblock series, is a u-blox MAX-7Q GNSS (GPS, GLONASS, QZSS, and SBAS) module. This module features exceptional performance, high sensitivity, and minimal acquisition time, which makes it suitable for low-power IoT solutions. The RAK1910 positioning module is a GNSS receiver. It receives and tracks the GPS (including SBAS and QZSS) and the GLONASS signals. QZSS and SBAS signals (by default) can be received concurrently with GPS signals.

## Product Features

* **Sensor specifications**
    * Voltage Supply: 3.3 V
    * Current Consumption: 15 uA to 22 mA
    * Chipset: u-Blox MAX-7Q
    * High accuracy of 2.5 m
    * 10 Hz update rate
    * 0.1 m/s velocity accuracy
    * 0.5 degrees heading accuracy
    * Fast location fix. 29 sec from cold start to first fix. 1 sec from hot start
    * GPS and GLONASS satellite support

* **Size**
    * 10 x 23 mm

## Prerequisites

To use a **RAK1910**, you need at least a **WisBlock Base** and a **GPS Antenna** to plug the module in. **WisBlock Base** provides power supply to the **RAK1910** module. Furthermore, you need a **WisBlock Core** module to use the sensor.

:::warning
* The included active GPS antenna must be connected to the iPEX antenna connector on the board. Otherwise, the module will not work.
* Make sure to fix the module with the screws to ensure a proper function.
:::

