---
slug: /product-categories/wisblock/rak19011/quickstart/
title: RAK19011 WisBlock Dual IO Base Board with Power Slot Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK19011. Instructions are written in a detailed, step-by-step manner for easier setup. Aside from hardware configuration, it also includes software setup with detailed example codes to help you get started.
image: https://images.docs.rakwireless.com/wisblock/rak19011/rak19011.png
keywords:
  - RAK19011
  - quickstart
  - wisblock
sidebar_label: Quick Start Guide
---

# RAK19011 WisBlock Dual IO Base Board with Power Slot Quick Start Guide

This guide introduces the RAK19011 WisBlock Dual IO Base Board with Power Slot and how to use it.

## Prerequisites

Before going through each and every step on using the RAK19011 WisBlock Dual IO Base Board with Power Slot, make sure to prepare the necessary items listed below:

## Hardware

- Your choice of <a href="https://store.rakwireless.com/collections/wisblock-power-management" target="_blank">WisBlock Base Power Module</a>.
- <a href="https://store.rakwireless.com/products/rak19011-max-base-board-third-generation?utm_source=RAK19011&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAK19011 WisBlock Dual IO Base Board with Power Slot</a>.
- Your choice of <a href="https://store.rakwireless.com/collections/wisblock-core" target="_blank">WisBlock Core</a>.
- Your choice of <a href="https://store.rakwireless.com/pages/wisblock" target="_blank">WisBlock Modules</a>.

It is also highly recommended to check the dedicated quick start guide that you can follow on various WisBlock Modules. Each quick start guide of these modules contains detailed steps to open the example codes and upload them to the WisBlock Core.

### Safety Information

:::warning

- RAK19011 requires a WisBlock power module for power and connector interfaces. It lacks USB and battery/power connectors; these functionalities must be added using an appropriate WisBlock power module.
- Securely fasten the modules with screws to ensure proper function.

:::

### Installation Guide

The RAK19011 WisBlock Dual IO Base Board with Power Slot is the main board for attaching MCUs, power modules, sensors, and IO modules via standardized expansion connectors. These connectors provide data bus interconnection between the attached modules.

This guide details module installation on the RAK19011 WisBlock Dual IO Base Board with Power Slot.

##### Attach a WisConnector

The WisConnector is the interface between the RAK19011 module and the WisBlock Core, WisBlock Power, sensor, and I/O modules. Before connecting these modules, read the following instructions:

:::tip NOTE

This guide uses two arrows. Refer to **Figure 1** for its representation.

:::

> **Image:** Notation within the guide

1. Align the connectors. Keep the header parallel and place it lightly in the corresponding lap joint of the socket.

> **Image:** Alignment of WisConnector

2. Fit the connector. Tilt one end of the connector (header) less than 20 degrees; do not apply force during this process. Gently place the other end in parallel.

> **Image:** Fit the WisConnector’s header inside of the socket

3. After the above alignment steps, the header and socket are matched but still not buckled.

> **Image:** WisConnector’s header matched inside of the socket

4. Apply forces evenly by pressing in parallel; then, a sound will confirm the completion of the buckling.

> **Image:** Apply forces to buckle the heard to the socket 

5. When buckling and applying force, avoid uneven force application on both sides.

> **Image:** Avoid applying uneven forces

6. When the buckling process is complete, check that the header and socket remain parallel.

> **Image:** Correct way to buckle the WisConnector’s header to the socket

7. After buckling, if the header and socket are not parallel (not fully assembled), press evenly on both long sides to complete the buckling.

> **Image:** WisConnector’s header is not parallel to the socket

8. If the aforementioned steps are not yet complete, do not force the buckle. Otherwise, the connector may be damaged. If the connector cannot be smoothly buckled, repeat the alignment step.

##### Detach a WisConnector

1. To disconnect the header from the socket, pull it out parallel, using even force.

> **Image:** Correct way: Applying even forces to detach the header from the socket

2. Avoid pulling out the header asymmetrically in the lengthwise direction.

> **Image:** Wrong way: Applying uneven forces to detach the header from the socket

3. The short-side of the connector can be pulled out asymmetrically, but apply the force vertically and avoid rotating the header.

> **Image:** Wrong way: Do not rotate the header

4. Avoid applying forces in a single corner.

> **Image:** Wrong way: Do not apply force in a single corner of the header

##### Assemble a WisBlock Module

 **WisBlock Core**

A WisBlock Core module is designed to be installed on the CPU slot of the RAK19011 WisBlock Dual IO Base Board with Power Slot. As shown in **Figure 14**, the location is properly marked by the silkscreen. Follow carefully the procedure defined in [attaching a WisConnector](#attaching-a-wisconnector) section to attach a Core module. Once attached, fix the module with one or more pieces of M1.2 x 3 mm screws depending on the WisBlock Core.

> **Image:** WisBlock Core silkscreen on the RAK19011 Base Board

 **WisBlock Power**

A WisBlock Power module is designed to be installed on the Power slot of the RAK19011 WisBlock Dual IO Base Board with a Power Slot. As shown in **Figure 15**, the location is properly marked by the silkscreen. Follow carefully the procedure defined in [attaching a WisConnector](#attaching-a-wisconnector) section to attach a Core module. Once attached, fix the module with one or more pieces of M1.2 x 3 mm screws depending on the WisBlock Core.

> **Image:** WisBlock Power silkscreen on the RAK19011 Base Board

**WisBlock Sensor**

A WisBlock Sensor module is designed to be installed on the sensor slot of the RAK19011 WisBlock Dual IO Base Board with Power Slot. There are six (6) available sensor slots in the RAK19011 WisBlock Dual IO Base Board with Power Slot. As shown in **Figure 16**, the location of the slots is properly marked by the silkscreen. Follow carefully the procedure of the section, [attaching a WisConnector](#attaching-a-wisconnector), to attach a WisBlock Sensor module. Once attached, fix the module with an M1.2 x 3 mm screw.

> **Image:** WisBlock Sensor silkscreen on the RAK19011 Base Board

 **WisBlock IO**

A WisBlock IO module is designed to be installed on the IO slot of the RAK19011 WisBlock Dual IO Base Board with Power Slot. There are two (2) IO slots in the RAK19011 WisBlock Dual IO Base Board with Power Slot. As shown in **Figure 17**, the location is properly marked by the silkscreen. Follow carefully the procedure of the section, [attaching a WisConnector](#attaching-a-wisconnector), to attach a WisBlock IO module. Once attached, fix the module with three pieces of M1.2 x 3 mm screws.

> **Image:** WisBlock IO silkscreen on the RAK19011 Base Board

##### Disassemble a WisBlock Module

1. The procedure to disassemble any type of WisBlock module is the same. As shown in **Figure 18**, first, remove the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed from a WisBlock module's PCB, a silkscreen indicates the correct location to apply force. Applying even force under the marked area detaches the module from the base board. See Figures **19** and **20**.

> **Image:** Detach silkscreen on the WisBlock module

> **Image:** Applying even forces on the proper location of a WisBlock module to detach the module from the Base Board

## Product Configuration

### Software Setup

The WisBlock Core is designed to interface with other WisBlock modules, such as sensors, displays, and other interfaces. To make useful devices, you need to upload source code to the WisBlock Core.
Based on your choice of WisBlock Core, select a development environment:

#### Arduino IDE BSP Installation

**Programming via Arduino IDE**
- <a href="https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index" target="_blank">RAKwireless BSP support for Arduino</a>

In the Arduino IDE, once you install the BSP, examples for the WisBlock Core will be automatically included in the list of examples.

#### PlatformIO BSP Installation

**Programming via PlatformIO IDE**
- <a href="https://github.com/RAKWireless/WisBlock/blob/master/PlatformIO/README" target="_blank">RAKwireless WisBlock modules in PlatformIO</a>

To better understand the WisBlock Base, the RAK19011 block diagram is provided in this section.

 **Block Diagram**

The block diagram shown in **Figure 20** shows the internal architecture and external interfaces of the RAK19011 board.

> **Image:** RAK19011 WisBlock Dual IO Base Board with Power Slot block diagram

The MCU in the WisBlock Core module offers I2C, UART, and SPI data buses to the sensor and I/O modules. Through these buses, the MCU can control and retrieve data from the sensors. The RAK19011 WisBlock Dual I/O Base Board with Power Slot board connects all these modules.

### Examples

To quickly build your IoT device with less hassle, example codes for WisBlock Core are provided. You can access the codes on the <a href="https://github.com/RAKWireless/WisBlock/tree/master/examples" target="_blank">WisBlock Example code repository</a>. The example codes on folder `common` are compatible with RAK4631, RAK11200, and RAK11310 WisBlock cores.

#### Tutorials and Resources

<a href="https://www.youtube.com/watch?v=lElJb0KDK7U" target="_blank">Create Modular Power Supply with WisBlock Power Boards</a>

