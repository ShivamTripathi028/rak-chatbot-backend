---
slug: /product-categories/wisblock/rak19003/quickstart/
title: RAK19003 WisBlock Mini Base Board Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK19003. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: https://images.docs.rakwireless.com/wisblock/rak19003/rak19003-n.png').default
keywords:
    - RAK19003
    - wisblock
    - quickstart
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK19003 WisBlock Mini Base Board Quick Start Guide

This guide introduces the RAK19003 WisBlock Base Board and how to use it.

## Prerequisite

### What Do You Need?

Before going through each and every step on using the RAK19003 WisBlock Mini Base Board, make sure to prepare the necessary items listed below:

#### Hardware

- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- Your choice of [WisBlock Modules](https://store.rakwireless.com/pages/wisblock).
It is highly recommended to also check the dedicated Quick Start Guide that you can follow on various WisBlock Modules. Each Quick Start Guide of these modules contains the detailed steps on how to open the example codes and upload them to the WisBlock Core.
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- Type-C USB cable for programming and debugging

#### Software

Based on the choice of the WisBlock Core, select a Development Environment:

<b>Programming via Arduino IDE</b>
- [RAKwireless BSP support for Arduino](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index)
In Arduino IDE, once you installed the BSP, the examples for WisBlock Core will be automatically included on the list of examples.

<b>Programming via PlatformIO IDE:</b>
- [RAKwireless WisBlock modules in PlatformIO](https://github.com/RAKWireless/WisBlock/blob/master/PlatformIO/README)


## Product Configuration

### Overview

To give you a better understanding of how the WisBlock Base works, the block diagram and power supply diagram of RAK19003 are provided in this section.

#### Block Diagram

The block diagram is shown in **Figure 1** that shows the internal architecture and external interfaces of the RAK19003 board.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/datasheet/block-diagram.svg"
  figureCount="1"
  caption="RAK19003 WisBlock Base block diagram" 
   width="90%"
/>

The MCU in the WisBlock Core module offers the I2C, UART, and SPI data buses to the sensor modules. Through these buses, the MCU can control and retrieve data from the sensors.

Some types of MCU have fewer IO pins. In such cases, not all the pins of the data bus are connected. For example, only I2C and UART are connected.

Some MCU IO pins have an alternate function. In this case, you have the option to modify the IO via software or rework the hardware to redefine the function of IO. Refer to the datasheet of WisBlock Core to get all the details.

#### Power Supply Diagram of RAK19003

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/quickstart/rak19003-ps.png"
  figureCount="2"
  caption="Power Supply Block Diagram" 
   width="90%"
/>

The RAK19003 is designed to be powered by a battery and provides the charger circuitry for **lithium batteries**. The charger circuitry can be connected to a wall outlet charger through the Type-C USB connector, or the specific connector for a solar panel.

A high-efficiency step-down converter with a low quiescent current is used for generating 3.3&nbsp;V. This 3.3&nbsp;V power supply drives the consumption of the WisBlock Core module and the sensor modules. The max current supported by the 3.3&nbsp;V LDO is 750&nbsp;mA.

3V3_S is another 3.3&nbsp;V power supply, it can be controlled by the MCU in order to disconnect the power sensors during idle periods to save power. 3V3_S is controlled by an IO2 pin on the WisBlock Core board.

- Set **IO2=1**, 3V3_S is on.
- Set **IO2=0**, 3V3_S is off.


### Hardware Setup

#### RAK19003 WisBlock Base Board Installation Guide

RAK19003 WisBlock Base Board is the main board that allows you to attach MCU, sensors, and IO modules through the standardized expansion connectors. These connectors provide a data bus interconnection between the modules attached to the RAK19003 Base Board.

This guide shows the details related to the installation of modules into the RAK19003 board. The following section discusses the general concepts to manipulate the WisConnector in any WisBlock Module. The installation and removal details of each type of WisBlock module: Core and Sensor are explained.

##### Attaching a WisConnector

The WisConnector is the interface between the RAK19003 module and the WisBlock Core, Sensor, and IO modules. Before connecting these modules, read the following instructions:

:::tip NOTE

This guide uses two arrows. Refer to **Figure 3** for its representation.

:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/quickstart/1.arrows.png"
  figureCount="3"
  caption="Notation within the guide" 
   width="50%"
/>

1. Align the connectors. Keep the header parallel and place it lightly in the corresponding lap joint of the socket.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/quickstart/2.alignment.png"
  figureCount="4"
  caption="Alignment of WisConnector" 
   width="75%"
/>

2. Fit the connector. Tilt one end of the connector (header) less than 20 degrees, while do not apply force during this process, gently place the other end in parallel.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/quickstart/3.header-to-socket.png"
  figureCount="5"
  caption="Fit the WisConnector’s header inside of the socket" 
   width="75%"
/>

3. After the above alignment steps, the header and socket are matched but still not buckled.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/quickstart/4.header-matched.png"
  figureCount="6"
  caption="WisConnector’s header matched inside of the socket" 
   width="75%"
/>

4. Apply forces evenly by pressing in parallel, then there will be a sound confirming the completion of the buckling.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/quickstart/5.buckle-the-head.png"
  figureCount="7"
  caption="Apply forces to buckle the heard to the socket" 
   width="75%"
/>

5. In the process of buckling and applying force, avoid the application of uneven force on both sides.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/quickstart/6.uneven-forces.png"
  figureCount="8"
  caption="Avoid applying uneven forces" 
   width="75%"
/>

6. When the buckling process is completed, check that the header and socket are kept in parallel.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/quickstart/7.buckle-header-to-socket.png"
  figureCount="9"
  caption="Correct way to buckle the WisConnector’s header to the socket" 
   width="75%"
/>

7. If after buckling, the header and socket are not in a parallel state (not fully assembled in one place), then press the even force on both sides of the long side to complete the correct buckling.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/quickstart/8.not-parallel.png"
  figureCount="10"
  caption="WisConnector’s header is not parallel to the socket" 
   width="75%"
/>

8. When the aforementioned steps are not completed yet, do not apply force to buckle. Otherwise, there will be a risk to damage the connector. When the connector cannot be smoothly buckled down, repeat the alignment step.

##### Detaching a WisConnector

1. To disconnect the header from the socket, pull out in parallel with even forces.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/quickstart/9.detach-header.png"
  figureCount="11"
  caption="Correct way: Applying even forces to detach the header from the socket" 
   width="75%"
/>

2. Avoid pulling out the header asymmetrically in the long-side direction.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/quickstart/10.wrong-way-of-detaching.png"
  figureCount="12"
  caption="Wrong way: Applying uneven forces to detach the header from the socket" 
   width="60%"
/>

3. The short-side of the connector can be pulled out asymmetrically, but apply the force vertically and avoid rotating the header.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/quickstart/11.dont-rotate.png"
  figureCount="13"
  caption="Wrong way: Do not rotate the header" 
   width="60%"
/>

4. Avoid applying forces in a single corner.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/quickstart/12.dont-apply-force.png"
  figureCount="14"
  caption="Wrong way: Do not apply force in a single corner of the header" 
   width="55%"
/>

#####  Assembling a WisBlock Module

###### WisBlock Core

A WisBlock Core module is designed to be installed on the CPU slot of the RAK19003 Base Board. As shown in **Figure 15**, the location is properly marked by silkscreen. Follow carefully the procedure defined in [attaching a WisConnector](https://docs.rakwireless.com/product-categories/wisblock/rak19003/quickstart/#attaching-a-wisconnector) section in order to attach a Core module.

Once attached, fix the module  with one or more pieces of M1.2 x 3&nbsp;mm screws depending on the WisBlock Core.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/quickstart/rak19003-top-assembly.png"
  figureCount="15"
  caption="WisBlock Core silkscreen on the RAK19003 Base Board" 
   width="40%"
/>

###### WisBlock Sensor

A WisBlock Sensor module is designed to be installed on the Sensor slot of the RAK19003 Base Board. There are two (2) available sensor slots in the RAK19003 Base Board. As shown in **Figure 16**, the location of the slots is properly marked by silkscreen. Follow carefully the procedure of the section, [attaching a WisConnector](https://docs.rakwireless.com/product-categories/wisblock/rak19003/quickstart/#attaching-a-wisconnector), to attach a WisBlock Sensor module. Once attached, fix the module with an M1.2 x 3&nbsp;mm screw.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/quickstart/rak19003-bottom-assembly.png"
  figureCount="16"
  caption="WisBlock Sensor silkscreen on the RAK19003 Base Board" 
   width="40%"
/>


##### Disassembling a WisBlock Module

1. The procedure to disassemble any type of WisBlock modules is the same. As shown in **Figure 17**, first, remove the screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/quickstart/rak19003-top-remove.png"
  figureCount="17"
  caption="Removing screws from the WisBlock module" 
   width="40%"
/>

2. Once the screws are removed, on the PCB of a WisBlock module, there is a silkscreen that shows the correct location where force can be applied. By applying even force under the marked area, the module can be detached from the Base Board. See **Figure 18** and **Figure 19**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/quickstart/17.detaching-silkscreen.png"
  figureCount="18"
  caption="Detaching silkscreen on the WisBlock module" 
   width="75%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/quickstart/18.detaching-module.png"
  figureCount="19"
  caption="Applying even forces on the proper location of a WisBlock module to detach the module from the Base Board" 
   width="65%"
/>


#### Battery Connection

RAK19003 can be powered via the USB cable or Li-Ion/LiPo battery via the dedicated connectors, as shown in **Figure 20**. The matching connector for the battery wires is a [JST PHR-2 2&nbsp;mm pitch female](https://www.jst-mfg.com/product/detail_e.php?series=199).

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/datasheet/battery-connector.svg"
  figureCount="20"
  caption="Battery Connector Pin Order" 
   width="50%"
/>

The battery can be recharged as well via a small Solar Panel, as shown in **Figure 21**. The matching connector for the solar panel wires is an [JST ZHR-2 1.5&nbsp;mm pitch female](https://www.jst-mfg.com/product/detail_e.php?series=287). The GND pin of [Battery Connector](https://docs.rakwireless.com/product-categories/wisblock/rak19003/datasheet/#battery-connector) is located on edge of the board.

:::warning

- Battery can cause harm if not handled properly.
- Only 3.7-4.2&nbsp;V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause fire.
- Make sure the battery wires match the polarity on the RAK19003 board. Not all batteries have the same wiring.

:::

#### Solar Panel Connection

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19003/datasheet/solar-panel.svg"
  figureCount="21"
  caption="Solar Panel Connector VIN and GND" 
   width="45%"
/>



:::warning 

- Only 5&nbsp;V solar panels are supported. Do not use 12&nbsp;V solar panels. It will destroy the charging unit and eventually other electronic parts.
- The GND pin of the Solar Panel Connector is located on edge of the board. Make sure the Solar Panel wires are matching the polarity on the RAK19003 board.

:::

The full specification of [Solar Panel Connection](https://docs.rakwireless.com/product-categories/wisblock/rak19003/datasheet/#solar-panel-connector) can be found on the datasheet of the WisBlock Base.

### Software Setup

The WisBlock Core is designed to be interfaced with other WisBlock Modules like sensors, displays, and other interfaces. To make useful devices, you need to upload a source code to the WisBlock Core.
Before you continue, you should have either an [Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index) or [PlatformIO](https://github.com/RAKWireless/WisBlock/blob/master/PlatformIO/README) already setup.

#### WisBlock Examples Repository

To quickly build your IoT device with less hassle, example codes for WisBlock Core are provided.

You can access the codes on the [WisBlock Example code repository](https://github.com/RAKWireless/WisBlock/tree/master/examples). The example codes on folder `common` are compatible with RAK4631, RAK11200, and RAK11310 WisBlock cores.

<RkBottomNav/>


