---
slug: /product-categories/wisblock/rak12013/overview/
title: RAK12013 WisBlock Radar Sensor Module
description: RAK12013 is a WisBlock sensor that applies the Doppler radar effect to detect moving objects/motion using microwaves at a 360 degrees angle within 7 meters radius.
image: "https://images.docs.rakwireless.com/wisblock/rak12013/rak12013.png"
keywords:
  - wisblock
  - RAK12013
  - RCWL
  - RCWL-9196
sidebar_label: Product Overview
---

# RAK12013 WisBlock Radar Sensor Module

Thank you for choosing **RAK12013 WisBlock Radar Sensor Module** in your awesome IoT Project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

* [RAK12013 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak12013/quickstart/)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak12013/datasheet/)
* [WisBlock Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/quickstart/)
* [WisBlock Source Code Repository](https://github.com/RAKWireless/WisBlock/)
* [RAK12013 3D Model](https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK12013.step)
* [40-Pin Male Connector 3D file](https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/M40S1003K6M.stp)
* [WisBlock IO Tutorial](https://learn.rakwireless.com/hc/en-us/articles/26743881131927-How-To-Make-Your-Own-WisBlock-IO-Board)

**Example**

[Sample Code: RAK12013_Radar_3GHZ](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/IO/RAK12013_Radar_3GHZ)

## Product Description

RAK12013 is a 3.2 GHz microwave radar module based on RCWL-9196. It uses the Doppler radar effect to detect moving objects/motion using microwaves. The RCWL-9196 will transmit and receive a 3.2 GHz radar signal and compare the difference between the two signals to determine whether the object is moving or not.

:::tip NOTE
1. Radar signals don't interfere with other signals such as LoRa, WiFi, and Bluetooth; but multiple radar signals interfere with each other between single individuals over a distance greater than 1 meter.
2. The component side of the PCB module is the positive sensing face, while the opposite side is the negative sensing face. The negative sensing face is less effective in terms of sensing.
:::

## Product Features

* **Module specifications**
    * 3.3 V Power Supply
    * Current Consumption: < 3 uA
    * Chipset: RCWL RCWL-9196
    * Motion Detection Module
    * Detection Distance: 5 - 7 meters
    * Detection Area: 360 degrees angle with no blind spot
    * Frequency: 3.2 GHz
    * Trigger Way: repeat trigger

* **Size**
    * 25 x 35 mm

## Prerequisites

To use a **RAK12013**, you need at least a **WisBlock Base** to plug the module in. **WisBlock Base** provides power supply to the **RAK12013** module. Furthermore, you need a **WisBlock Core** module to use the sensor.

:::warning
Make sure to fix the module with the screws to ensure a proper function.
:::

