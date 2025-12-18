---
slug: /product-categories/wisblock/rak12027/overview/
title: RAK12027 WisBlock Earthquake Sensor Module
description: RAK12027 is a WisBlock Earthquake Sensor Module based on D7S, the world’s smallest high-precision seismic sensor from Omron. It detects earthquake seismic intensity.
image: https://images.docs.rakwireless.com/wisblock/rak12027/rak12027.jpg
keywords:
    - wisblock
    - RAK12027
    - D75
    - Omron
sidebar_label: Product Overview
---

# RAK12027 WisBlock Earthquake Sensor Module

Thank you for choosing **RAK12027 WisBlock Earthquake Sensor Module** in your next IoT Project! 🎉 To help you get started, we have provided you with all the necessary documentation for your product.

* [RAK12027 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak12027/quickstart/)
* [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak12027/datasheet/)
* <a href="https://docs.rakwireless.com/product-categories/wisblock/quickstart/" target="_blank">WisBlock Quick Start Guide</a>
* [WisBlock Source Code Repository](https://github.com/RAKWireless/WisBlock/)
* [RAK12027 3D Model](https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK12027.stp)
* [24-Pin Male Connector 3D File](https://downloads.rakwireless.com/3D_File/Accessory/WisConnector/M24S1003K6M.stp)
* [WisBlock Sensor Tutorial](https://learn.rakwireless.com/hc/en-us/articles/26687819464343-How-To-Make-Your-Own-WisBlock-Sensor-Board)

## Product Description

The RAK12027 is an Earthquake Sensor Module, a part of the RAKWireless WisBlock sensor Series. It carries D7S, the world’s smallest high-precision seismic sensor from Omron. It communicates with the target MCU over I2C interface, and it communicates with the target MCU over I2C interface and interrupts pins.

When an earthquake occurs with a seismic intensity equivalent to five (5) upper or higher on the JMA (Japan Meteorological Agency) Seismic Intensity Scale, the D7S will activate the shut-off output to notify the user that an earthquake has occurred. Also, the D7S has a **collapse alert system** that notifies if the device changes its horizontal position by more that 20-degree, which assumed that the structure mounted has already collapsed.

:::warning
Do not use the sensor in safety devices or for applications in which the sensor operation would directly affect human life.
:::

## Product Features

* **Sensor specifications**
    * Chipset: **Omron D7S**
    * Voltage supply: **3.3 V**
    * Using the SI value, which has a high correlation with the seismic intensity scale that indicates the magnitude of an earthquake, provides higher-precision judgment of seismic intensity scales
    * A higher degree of freedom for incorporation into devices and prolonged operation on battery power
    * The shutoff output terminal (INT1) operates equivalent to a conventional mechanical vibration sensor and ensures compatibility with mechanical vibration sensors
    * Collapse alarm integrated
    * I2C digital output interface
    * Operating temperature: **-30° C ~ 70° C**

* **Module size**
    * 10 x 23 mm

## Prerequisites

To use a **RAK12027**, you need at least a **WisBlock Base board** to plug the module in. **WisBlock Base board** provides power supply to the **RAK12027** module. Furthermore, you need a **WisBlock Core** module to use the sensor.

:::warning
Make sure to fix the module with the screws to ensure a proper function.
:::

