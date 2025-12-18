---
slug: /product-categories/wisblock/rak5811/overview/
title: RAK5811 WisBlock 0-5V Interface Module
description: RAK5811 is a WisBlock Interface module which extends the WisBlock system with 2 analog input ports. The analog ports have a 0-5V input range and are connected to the WisBlock Core MCU’s analog inputs.
image: "https://images.docs.rakwireless.com/wisblock/rak5811/RAK5811.png"
keywords:
    - RAK5811
    - wisblock
    - STMicroelectronics
    - LM2902
sidebar_label: Product Overview
---

# RAK5811 WisBlock 0-5V Interface Module

Thank you for choosing **RAK5811 WisBlock 0-5V Interface Module** in your awesome IoT Project! To help you get started, we have provided you with all the necessary documentation for your product.

* [RAK5811 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak5811/quickstart/)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak5811/datasheet/)
* <a href="https://docs.rakwireless.com/product-categories/wisblock/quickstart/" target="_blank">WisBlock Quick Start Guide</a>
* [WisBlock Source Code Repository](https://github.com/RAKWireless/WisBlock/)
* [RAK5811 3D Model](https://downloads.rakwireless.com/LoRa/WisBlock/WisBlock-3D/pwb-rak5811.stp)
* [40-Pin Male Connector 3D File](https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/M40S1003K6M.stp)
* [WisBlock Interface Tutorial](https://learn.rakwireless.com/hc/en-us/articles/26743881131927-How-To-Make-Your-Own-WisBlock-IO-Board)

**Examples**

* For WisBlock Core **RAK4630:** [Sample Code: RAK5811 0-5V](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK4630/IO/RAK5811_0-5V)
* For WisBlock Core **RAK11200:** [Sample Code: RAK5811 0-5V](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK11200/IO/RAK5811_0-5V)
* For WisBlock Core **RAK11310:** [Sample Code: RAK5811 0-5V](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK11300/IO/RAK5811_0-5V)

**Complete solution for Water Level Monitoring**

* For WisBlock Core RAK4630: [Sample Code: Water Level Monitoring](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK4630/solutions/Water_Level_Monitoring)
* For WisBlock Core RAK11310: [Sample Code: Water Level Monitoring](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK11300/solutions/Weather_Monitoring)

## Product Description

The RAK5811 WisBlock Interface module is designed to be part of a production-ready IoT solution in a modular way and must be combined with a WisBlock Core and a Base module. RAKWireless has standardized the way modules are interconnected to the baseboards with the WisBlock Interface Connectors. This standard connector is a small high-density connector that not only saves spaces on the circuit boards but also allows to implement high-speed communication bus.

The RAK5811 is a 0-5 V analog input interface module. The signal is routed through the IO bus to the WisBlock Core module. Inside of the WisBlock Core module, the MCU digitizes the signal and the sampled data is transmitted, for example, via a LoRa transceiver.

The RAK5811 module features two input channels capable of transmitting analog signals ranging from 0-5 V. Signal amplification and conversion for the two 0-5 V channels are achieved by an embedded high-precision operational amplifier that can operate across a wide range of temperatures.

In addition, this module integrates a 12 V power supply. Connected to the 12 V power supply is an embedded operational amplifier for powering external sensors with voltages up to 12 V.

The connection of the 0-5 V sensors is done through the fast crimping terminal without the need for special tools, this simplifies the installation process on the field.

## Product Features

*	Two 0-5 V analog input channels
*	Compatible with multiple WisBlock Core modules, such as the RAK4631
*	10 mV conversion accuracy
*	Supports low power consumption mode, the module can be powered off by WisBlock Core module for saving energy during idle periods
*	12 V output to power external sensors
*	Reserved I2C expansion interface
*	Fast crimping terminal to easily connect external components on the field
*	Designed with a 2 kV ESD protection level
*   Chipset: STMicroelectronics LM2902
*	Small dimensions of 35 mm x 25 mm

## Prerequisites

To use a **RAK5811**, you need at least a **WisBlock Base** to plug the module in. Furthermore, you need a **WisBlock Core** module to control the module.

:::warning
Make sure to fix the module with the screws to ensure a proper function.
:::

