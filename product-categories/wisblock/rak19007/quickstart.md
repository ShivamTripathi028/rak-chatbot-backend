---
slug: /product-categories/wisblock/rak19007/quickstart/
title: RAK19007 WisBlock Base Board Quick Start Guide | Setup & Configuration
description: Set up your RAK19007 Base Board! Learn to integrate LoRaWAN, BLE, and sensors, and power it via battery or solar for modular IoT projects.
image: https://images.docs.rakwireless.com/wisblock/rak19007/rak19007.png
keywords:
  - iot board with expansion slots
  - wisblock base board
  - lorawan base board
  - modular iot base board
  - low power iot development board
  - rak19007
  - low power mcu
  - lorawan development board
  - lorawan board setup guide
  - battery powered iot devices
date: 2022-07-04
sidebar_label: Quick Start Guide
---

# RAK19007 WisBlock Base Board 2nd Gen Quick Start Guide

This guide introduces the RAK19007 WisBlock Base Board 2nd Gen and how to use it.

## Prerequisite

### What Do You Need?

Before going through each and every step on using the WisBlock Base Board 2nd Gen, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK19007 WisBlock Base Board 2nd Gen](https://store.rakwireless.com/products/rak19007-wisblock-base-board-2nd-gen?utm_source=RAK19007&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- Your choice of [WisBlock Modules](https://store.rakwireless.com/pages/wisblock).
It is highly recommended to also check the dedicated Quick Start Guide that you can follow on various WisBlock Modules. Each Quick Start Guide of these modules contains the detailed steps on how to open the example codes and upload them to the WisBlock Core.
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- Type-C USB cable for programming and debugging

#### Software

Based on the choice of the WisBlock Core, select a Development Environment:

**Programming via Arduino IDE**
- [RAKwireless BSP support for Arduino](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index)
In Arduino IDE, once you installed the BSP, the examples for WisBlock Core will be automatically included on the list of examples.

**Programming via PlatformIO IDE:**
- [RAKwireless WisBlock modules in PlatformIO](https://github.com/RAKWireless/WisBlock/blob/master/PlatformIO/README.md)

## Product Configuration

### Overview

To give you a better understanding of how the WisBlock Base works, the block diagram and power supply diagram of RAK19007 are provided in this section.

#### Block Diagram

The block diagram shown in **Figure 1** shows the internal architecture and external interfaces of the RAK19007 WisBlock Base Board 2nd Gen.

> **Image:** RAK19007 WisBlock Base Board 2nd Gen block diagram

The MCU in the WisBlock Core module offers the I2C, UART, and SPI data buses to the sensor modules. Through these buses, the MCU can control and retrieve data from the sensors.

Some types of MCU have fewer IO pins. In such cases, not all the pins of the data bus are connected. For example, only I2C and UART are connected.

Some MCU IO pins have an alternate function. In this case, you have the option to modify the IO via software or rework the hardware to redefine the function of IO. Refer to the datasheet of WisBlock Core to get all the details.

#### Power Supply Diagram of RAK19007

> **Image:** Power supply block diagram

The RAK19007 is designed to be powered by a battery and provides the charger circuitry for **lithium batteries**. The charger circuitry can be connected to a wall outlet charger through the Type-C USB connector, or the specific connector for a solar panel. The voltage coming from the Type-C USB port or solar panel connector goes only to a charger chip. The charger chip detects if the battery needs to be recharged. When the battery is fully charged, the charger chip will stop charging. The output of the charger chip is used to supply the WisBlock modules via a step-down converter.

A high-efficiency step-down converter with a low quiescent current is used for generating 3.3 V. This 3.3 V power supply drives the consumption of the WisBlock Core module and the sensor modules. The max current supported by the 3.3 V LDO is 750 mA.

3V3_S is another 3.3 V power supply, it can be controlled by the MCU to disconnect the power sensors during idle periods to save power. 3V3_S is controlled by the IO2 pin on the WisBlock Core board.

- Set **IO2=1**, 3V3_S is on.
- Set **IO2=0**, 3V3_S is off.

### Hardware Setup

#### RAK19007 WisBlock Base Board 2nd Gen Installation Guide

RAK19007 WisBlock Base Board 2nd Gen is the main board that allows you to attach a WisBlock Core, sensors, and IO modules through the standardized expansion connectors. These connectors provide a data bus interconnection between the modules attached to the RAK19007 Base Board.

This guide shows the details related to the installation of modules into the RAK19007 board. The following section discusses the general concepts to manipulate the WisBlock Connector in any WisBlock Module. The installation and removal details of each type of WisBlock module: Core and Sensor are explained.

##### Attaching a WisBlock Connector

The WisBlock Connector is the interface between the RAK19007 board and the WisBlock Core, Sensor, and IO modules. Before connecting these modules, read the following instructions:

:::tip NOTE

This guide uses two arrows. Refer to **Figure 3** for its representation.

:::

> **Image:** Notation within the guide

1. Align the connectors. Keep the header parallel and place it lightly in the corresponding lap joint of the socket.

> **Image:** Alignment of WisBlock Connector

2. Fit the connector. Tilt one end of the connector (header) less than 20 degrees, while do not apply force during this process, gently place the other end in parallel.

> **Image:** Fit the WisBlock Connector’s header inside of the socket

3. After the above alignment steps, the header and socket are matched but still not buckled.

> **Image:** WisBlock Connector’s header matched inside of the socket

4. Apply forces evenly by pressing in parallel, then there will be a sound confirming the completion of the buckling.

> **Image:** Apply forces to buckle the heard to the socket

5. In the process of buckling and applying force, avoid the application of uneven force on both sides.

> **Image:** Avoid applying uneven forces

6. When the buckling process is completed, check that the header and socket are kept in parallel.

> **Image:** Correct way to buckle the WisBlock Connector’s header to the socket

7. If after buckling, the header and socket are not in a parallel state (not fully assembled in one place), then press the even force on both sides of the long side to complete the correct buckling.

> **Image:** WisBlock Connector’s header is not parallel to the socket

8. When the aforementioned steps are not completed yet, do not apply force to buckle. Otherwise, there will be a risk to damage the connector. When the connector cannot be smoothly buckled down, repeat the alignment step.

##### Detaching a WisBlock Connector

1. To disconnect the header from the socket, pull out in parallel with even forces.

> **Image:** Correct way: Applying even forces to detach the header from the socket

2. Avoid pulling out the header asymmetrically in the long-side direction.

> **Image:** Wrong way: Applying uneven forces to detach the header from the socket

3. The short-side of the connector can be pulled out asymmetrically, but apply the force vertically and avoid rotating the header.

> **Image:** Wrong way: Do not rotate the header

4. Avoid applying forces in a single corner.

> **Image:** Wrong way: Do not apply force in a single corner of the header

#####  Assembling a WisBlock Module

###### WisBlock Core

A WisBlock Core module is designed to be installed on the CPU slot of the RAK19007 Base Board. As shown in **Figure 15**, the location is properly marked by silkscreen. Follow carefully the procedure defined in [attaching a WisBlock Connector](https://docs.rakwireless.com/product-categories/wisblock/rak19007/quickstart/#attaching-a-wisconnector) section in order to attach a Core module.

Once attached, fix the module  with one or more pieces of M1.2 x 3 mm screws depending on the WisBlock Core.

> **Image:** WisBlock Core silkscreen on the RAK19007 Base Board

###### WisBlock IO

A WisBlock IO module is designed to be installed on the IO slot of the RAK19007 Base Board. As shown in **Figure 16**, the location is properly marked by silkscreen. Follow carefully the procedure defined in [attaching a WisBlock Connector](https://docs.rakwireless.com/product-categories/wisblock/rak19007/quickstart/#attaching-a-wisconnector) section in order to attach an IO module.

Once attached, fix the module with one or more pieces of M1.2 x 3 mm screws depending on the WisBlock IO.

> **Image:** WisBlock IO silkscreen on the RAK19007 Base Board

###### WisBlock Sensor

A WisBlock Sensor module is designed to be installed on the Sensor slots of the RAK19007 Base Board. As shown in **Figure 17**, the location of the slots is properly marked by silkscreen. Follow carefully the procedure of the section, [attaching a WisBlock Connector](https://docs.rakwireless.com/product-categories/wisblock/rak19007/quickstart/#attaching-a-wisconnector), to attach a WisBlock Sensor module. Once attached, fix the module with an M1.2 x 3 mm screw.

> **Image:** WisBlock Sensor silkscreen on the top of RAK19007 Base Board

##### Disassembling a WisBlock Module

1. The procedure to disassemble any type of WisBlock modules is the same. As shown in **Figure 18**, first, remove the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed, on the PCB of a WisBlock module, there is a silkscreen that shows the correct location where force can be applied. By applying even force under the marked area, the module can be detached from the Base Board. See **Figure 19** and **Figure 20**.

> **Image:** Detaching silkscreen on the WisBlock module

> **Image:** Applying even forces on the proper location of a WisBlock module to detach the module from the Base Board

#### Battery Connection

RAK19007 can be powered via the USB cable or Li-Ion/LiPo battery via the dedicated connectors, as shown in **Figure 21**. The matching connector for the battery wires is a [JST PHR-2 2 mm pitch female](https://www.jst-mfg.com/product/detail_e.php?series=199).

> **Image:** Battery connector pin order

The battery can be recharged as well via a small solar panel, as shown in **Figure 22**. The GND pin of [Battery Connector](https://docs.rakwireless.com/product-categories/wisblock/rak19007/datasheet/#battery-connector) is located on edge of the board.

:::warning

- Battery can cause harm if not handled properly.
- Only 3.7-4.2 V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Make sure the battery wires match the polarity on the RAK19007 board. Not all batteries have the same wiring.

:::

#### Solar Panel Connection

> **Image:** Solar panel connector VIN and GND

:::warning

- Only 5 V solar panels are supported. Do not use 12 V solar panels. It will destroy the charging unit and eventually other electronic parts.
- The GND pin of the Solar Panel Connector is located on edge of the board. Make sure the Solar Panel wires are matching the polarity on the RAK19007 board.

:::

The full specification of the [Solar Panel Connection](https://docs.rakwireless.com/product-categories/wisblock/rak19007/datasheet/#solar-panel-connector-2) can be found on the datasheet of the RAK19007 WisBlock Base Board 2nd Gen.

### LEDs

Three LEDs are used to indicate the operating status. Below are the functions of the LEDs:

🔴 Red LED - Connected to the charger chip to indicate the charger status. When the battery is charging, this red LED is on. When the battery is full, this LED is weak light or off.

🟢 Green LED - Connected to the MCU module, controlled by MCU defined by the user.

🔵 Blue LED - Connected to the MCU module, controlled by MCU defined by the user.

### Software Setup

The WisBlock Core is designed to be interfaced with other WisBlock Modules like sensors, displays, and other interfaces. To make useful devices, you need to upload a source code to the WisBlock Core.
Before you continue, you should have already set up either an [Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index) or [PlatformIO](https://github.com/RAKWireless/WisBlock/blob/master/PlatformIO/README.md).

#### WisBlock Examples Repository

To quickly build your IoT device with less hassle, example codes for WisBlock Core are provided. You can access the codes on the [WisBlock Example code repository](https://github.com/RAKWireless/WisBlock/tree/master/examples). The example codes on folder `common` are compatible with RAK4631, RAK11200, and RAK11310 WisBlock cores.

