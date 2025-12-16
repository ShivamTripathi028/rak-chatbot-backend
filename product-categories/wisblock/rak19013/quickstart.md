---
slug: /product-categories/wisblock/rak19013/quickstart/
title: RAK19013 WisBlock LiPo Solar Power Slot Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK19013. Instructions are written in a detailed, step-by-step manner for easier setup. Aside from hardware configuration, it also includes software setup with detailed example codes to help you get started.
image: https://images.docs.rakwireless.com/wisblock/rak19013/rak19013.png
keywords:
  - quickstart
  - wisblock
  - RAK19013
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK19013 WisBlock LiPo Solar Power Slot Module Quick Start Guide

## Prerequisite

Before going through each step of using the RAK19013 WisBlock LiPo Solar Power Slot module, make sure you have prepared the necessary items listed below:

- <a href="https://store.rakwireless.com/products/rak19013-lipo-solar-power-slot-module?utm_source=RAK19013&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAK19013 WisBlock LiPo Solar Power Slot Module</a>
- Your choice of <a href="https://store.rakwireless.com/collections/wisblock-base/" target="_blank">WisBlock Base</a>
- Your choice of <a href="https://store.rakwireless.com/collections/wisblock-core" target="_blank">WisBlock Core</a>
- <a href="https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">Li-Ion/LiPo battery (optional)</a>
- <a href="https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">Solar charger (optional)</a>
- <a href="https://store.rakwireless.com/products/rak5804-io-extension-board?utm_source=RAK5804&utm_medium=Document&utm_campaign=BuyFromStore)(Reprogramming of the WisBlock Core via USB" target="_blank">RAK5804 WisBlock Interface Module</a>

## Hardware Configuration

### Installation Guide

The RAK19013 WisBlock LiPo Solar Power Slot Module is a power board comprising a battery connector, a solar panel connector, a reset push button, and a power connector that connects to the WisBlock Base board.

For more information about RAK19013, refer to the <a href="https://docs.rakwireless.com/product-categories/wisblock/rak19013/datasheet/" target="_blank">Datasheet</a>.



#### Attach a WisConnector

The RAK19013 module can be mounted on the I/O slot of the WisBlock Base board, as shown in **Figure 1**. Also, always secure the connection of the WisBlock module by using compatible screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19013/quickstart/mounting-mechanism.png"
  width="60%"
  caption="RAK19013 mounting connection to WisBlock Base module"
  zoomMode={true}
/>


#### Detach a WisConnector

The procedure for disassembling any type of WisBlock module is the same.

1. First, remove the screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19013/quickstart/removing_screw.png"
  width="60%"
  caption="Removing screws from the WisBlock module"
  zoomMode={true}
/>

2. Once the screws are removed, check the module's silkscreen to find the correct location for applying force.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19013/quickstart/detach_silkscreen.png"
  width="70%"
  caption="Detach silkscreen on the WisBlock module"
  zoomMode={true}
/>

3. Apply force to the module at the connector's position, as shown in **Figure 6**, to detach it from the baseboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19013/quickstart/detach_module.png"
  width="70%"
  caption="Applying even forces on the proper location of a WisBlock module"
  zoomMode={true}
/>

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the <a href="https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool" target="_blank">WisBlock Pin Mapper</a> tool for possible conflicts.
:::

### Battery Selector

#### Rechargeable Battery

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19013/quickstart/rak19013-rechargeable.svg"
  width="80%"
  caption="RAK19013 pinout and connector assignments"
  zoomMode={true}
/>

:::tip NOTE
The voltage of the battery must not exceed 4.3&nbsp;V.
:::


RAK19013 can be powered by a rechargeable Li-Ion/LiPo battery via the dedicated connectors, as shown in **Figure 7**. The matching connector for the rechargeable battery wires is a <a href="https://www.jst-mfg.com/product/detail_e.php?series=199" target="_blank">JST PHR-2 2 mm pitch female</a>. A cable assembly for the rechargeable battery connector is also available for purchase in <a href="https://store.rakwireless.com/products/battery-connector-cable" target="_blank">RAK store</a>.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19013/quickstart/rak19013-battery-connection.svg"
  width="40%"
  caption="Rechargeable battery connector pin"
  zoomMode={true}
/>

:::warning

- Batteries can cause harm if not handled properly.
- Only 3.7&nbsp;V-4.2&nbsp;V rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- Make sure the battery wires, both rechargeable and non-rechargeable, match the polarity on the RAK19013 board. Not all batteries have the same wiring.

:::

### Solar Panel Connection

The battery can be recharged, as well, via a small Solar Panel, as shown in **Figure 8**. The matching connector for the solar panel wires is an <a href="https://www.jst-mfg.com/product/detail_e.php?series=287" target="_blank">JST ZHR-2 1.5 mm pitch female</a>. A cable assembly for the solar panel connector is also available for purchase in <a href="https://store.rakwireless.com/products/solar-panel-connector-cable" target="_blank">RAK store</a>.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19013/quickstart/rak19013-solar-connection.svg"
  width="40%"
  caption="Solar panel connector VIN and GND"
  zoomMode={true}
/>


:::warning

- Only 5&nbsp;V solar panels are supported. Do not use 12&nbsp;V solar panels; this will destroy the charging unit and eventually other electronic parts.
- The GND pin of the solar panel connector is located on the edge of the board. Ensure the solar panel wires match the polarity on the RAK19013 board.

:::

## Product Configuration

### Software Setup

Since there is no USB port on the RAK19013, the only way to upload code is by using a RAK5804.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19013/quickstart/rak19013-rechargeable-rak5804.svg"
  width="80%"
  caption="RAK19013 and RAK5804 Connector assignments"
  zoomMode={true}
/>

Based on your choice of WisBlock Core, select a development environment:

#### Arduino IDE BSP Installation

<b>Programming via Arduino IDE</b>
- <a href="https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index" target="_blank">RAKwireless BSP support for Arduino</a>
<br/>In the Arduino IDE, once you install the BSP, examples for the WisBlock Core will be automatically included in the list of examples.

#### PlatformIO BSP Installation

<b>Programming via PlatformIO IDE:</b>
- <a href="https://github.com/RAKWireless/WisBlock/blob/master/PlatformIO/README" target="_blank">RAKwireless WisBlock modules in PlatformIO</a>

### Examples 

To quickly build your IoT device with less hassle, example codes for WisBlock Core are provided. You can access the codes on the <a href="https://github.com/RAKWireless/WisBlock/tree/master/examples" target="_blank">WisBlock Example code repository</a>. The example codes on folder `common` are compatible with RAK4631, RAK11200, and RAK11310 WisBlock Cores.
The two user LEDs of RAK19013 can be accessed using macrodefinitions `LED_GREEN` / `PIN_LED1` for the green LED and `LED_BLUE` / `PIN_LED2` for the blue LED. For the battery voltage reading, `WB_A0` is used.

## Tutorials and Resources

<a href="https://www.youtube.com/watch?v=fv0y22VDVB0" target="_blank">Create Modular Power Supply with WisBlock Power Boards</a>

<RkBottomNav/>