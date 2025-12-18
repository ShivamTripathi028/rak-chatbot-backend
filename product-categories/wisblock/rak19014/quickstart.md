---
slug: /product-categories/wisblock/rak19014/quickstart/
title: RAK19014 WisBlock Battery USB Power Slot Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK19014. Instructions are written in a detailed, step-by-step manner for easier setup. Aside from hardware configuration, it also includes software setup with detailed example codes to help you get started.
image: https://images.docs.rakwireless.com/wisblock/rak19014/rak19014.png
keywords:
  - quickstart
  - wisblock
  - RAK19014
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK19014 WisBlock Battery USB Power Slot Module Quick Start Guide

## Prerequisite


Before going through each step of using the RAK19014 WisBlock Battery USB Power Slot Module, make sure you have prepared the necessary items listed below:

- <a href="https://store.rakwireless.com/products/usb-battery-power-slot-module-rak19014?utm_source=RAK19014&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAK19014 WisBlock Battery USB Power Slot Module</a>
- Your choice of <a href="https://store.rakwireless.com/collections/wisblock-base/" target="_blank">WisBlock Base</a>
- Your choice of <a href="https://store.rakwireless.com/collections/wisblock-core" target="_blank">WisBlock Core</a>
- <a href="https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">External battery</a>

### Hardware Configuration

### Installation Guide

The RAK19014 WisBlock Battery USB Power Slot Module is a power board comprising a battery connector, a reset push button, and a power connector that connects to the WisBlock Base board.

For more information about the RAK19014, refer to the <a href="https://docs.rakwireless.com/product-categories/wisblock/rak19014/datasheet/" target="_blank">Datasheet</a>.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19014/quickstart/rak19014-setup.png"
  width="70%"
  caption="RAK19014 hardware setup"
  zoomMode={true}
/>

:::tip NOTE
The voltage of the battery must not exceed 4.3&nbsp;V.
:::

##### Attach a WisConnector

The RAK19014 WisBlock Battery USB Power Slot Module can be mounted on the power slot of the WisBlock Base board, as shown in **Figure 2**. Also, always secure the connection of the WisBlock module using compatible screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19014/quickstart/mounting-mechanism.png"
  width="60%"
  caption="RAK19014 mounting connection to WisBlock Base module"
  zoomMode={true}
/>


##### Detach a WisConnector

The procedure for disassembling any type of WisBlock module is the same.

1. First, remove the screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19014/quickstart/removing_screws.png"
  width="60%"
  caption="Removing screws from the WisBlock module"
  zoomMode={true}
/>

2. Once the screws are removed, check the module's silkscreen to find the correct location for applying force.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19014/quickstart/detach_silkscreen.png"
  width="70%"
  caption="Detach silkscreen on the WisBlock module"
  zoomMode={true}
/>

3. Apply force to the module at the connector's position, as shown in **Figure 5**, to detach it from the baseboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19014/quickstart/detach_module.png"
  width="70%"
  caption="Applying even forces on the proper location of a WisBlock module"
  zoomMode={true}
/>

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the <a href="https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool" target="_blank">WisBlock Pin Mapper</a> tool for possible conflicts.
:::

### Battery Selector

RAK19014 WisBlock Battery USB Power Slot Module can be powered by an external battery via the dedicated connectors, as shown in **Figure 6**. The matching connector for the battery cable is a <a href="https://www.jst-mfg.com/product/detail_e.php?series=199" target="_blank">JST PHR-2 2&nbsp;mm pitch female</a>. A cable assembly for the battery connector is also available for purchase in <a href="https://store.rakwireless.com/products/battery-connector-cable" target="_blank">RAK store</a>.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19014/quickstart/battery.png"
  width="60%"
  caption="External battery connector pin"
  zoomMode={true}
/>

:::warning

- Batteries can cause harm if not handled properly.
- Ensure the battery wires match the polarity on the RAK19014 board. Not all batteries have the same wiring.

:::

## Product Configuration

### Software Setup

The WisBlock Core is designed to interface with other WisBlock modules, such as sensors, displays, and other interfaces. To make useful devices, you need to upload source code to the WisBlock Core.
Based on your choice of WisBlock Core, select a development environment:

#### Arduino IDE BSP Installation

<b>Programming via Arduino IDE</b>
- <a href="https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index" target="_blank">RAKwireless BSP support for Arduino</a>
<br/>In the Arduino IDE, once you install the BSP, examples for the WisBlock Core will be automatically included in the list of examples.

#### PlatformIO BSP Installation

<b>Programming via PlatformIO IDE:</b>
- <a href="https://github.com/RAKWireless/WisBlock/blob/master/PlatformIO/README" target="_blank">RAKwireless WisBlock modules in PlatformIO</a>

## Examples 

To quickly build your IoT device with less hassle, example codes for the WisBlock Core are provided. You can access the codes on the <a href="https://github.com/RAKWireless/WisBlock/tree/master/examples" target="_blank">WisBlock Example code repository</a>. The example codes on folder `common` are compatible with RAK4631, RAK11200, and RAK11310 WisBlock cores.
The two user LEDs of RAK19014 can be accessed using macro definitions `LED_GREEN` / `PIN_LED1` for the green LED and `LED_BLUE` / `PIN_LED2` for the blue LED.

## Tutorials and Resources

<a href="https://www.youtube.com/watch?v=fv0y22VDVB0" target="_blank">Create Modular Power Supply with WisBlock Power Boards</a>

<RkBottomNav/>