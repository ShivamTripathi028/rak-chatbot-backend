---
slug: /product-categories/wisblock/rak19012/quickstart/
title: RAK19012 WisBlock USB LiPo Solar Power Slot Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK19012. Instructions are written in a detailed, step-by-step manner for easier setup. Aside from hardware configuration, it also includes software setup with detailed example codes to help you get started.
image: https://images.docs.rakwireless.com/wisblock/rak19012/rak19012.png
keywords:
    - RAK19012
    - wisblock
    - quickstart
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK19012 WisBlock USB LiPo Solar Power Slot Module Quick Start Guide

## Prerequisites

Before going through each step of using the RAK19012 WisBlock USB LiPo Solar Power Slot Module, make sure you have prepared the necessary items listed below:

- <a href="https://store.rakwireless.com/products/rak19012-usb-lipo-solar-power-slot-module?utm_source=RAK19012&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAK19012 WisBlock USB LiPo Solar Power Slot Module</a>
- Your choice of <a href="https://store.rakwireless.com/collections/wisblock-base/" target="_blank">WisBlock Base board with Power Slot</a>
- Your choice of <a href="https://store.rakwireless.com/collections/wisblock-core" target="_blank">WisBlock Core</a>
- <a href="https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">Li-Ion/LiPo battery (optional)</a>
- <a href="https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">Solar charger (optional)</a>


## Hardware Configuration

### Installation Guide

The RAK19012 should be attached to the power slot connector of a WisBlock Base board with a power slot. It is a power board providing the same features and interfaces as standard WisBlock Base boards: a USB-C connector, battery and solar panel connectors, LED indicators, and a reset button.

:::warning 

RAK19012 **only** supports WisBlock Base boards with Power Slot. It is not compatible with all WisBlock Base boards.

:::

For more information about RAK19012, refer to the <a href="https://docs.rakwireless.com/product-categories/wisblock/rak19012/datasheet/" target="_blank">Datasheet</a>.

#### Attach a WisConnector


The RAK19012 module can be mounted on the power slot of the WisBlock Base board, as shown in **Figure 1**. Also, always secure the connection of the WisBlock module by using compatible screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19012/quickstart/mounting-mechanism.png"
  figureCount="2"
  caption="RAK19012 mounting connection to WisBlock Base module" 
   width="60%"
  zoomMode={true}
/>

#### Detach a WisConnector

The procedure for disassembling any type of WisBlock module is the same.

1. First, remove the screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19012/quickstart/removing_screw.png"
  figureCount="3"
  caption="Removing screws from the WisBlock module" 
   width="70%"
  zoomMode={true}
/>

2. Once the screws are removed, check the module's silkscreen to find the correct location for applying force.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19012/quickstart/detach_silkscreen.png"
  figureCount="4"
  caption="Detach silkscreen on the WisBlock module" 
   width="70%"
  zoomMode={true}
/>

3. Apply force to the module at the connector's position, as shown in **Figure 5**, to detach it from the baseboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19012/quickstart/detach_module.png"
  figureCount="5"
  caption="Applying even forces on the proper location of a WisBlock module" 
   width="70%"
  zoomMode={true}
/>

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the <a href="https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool" target="_blank">WisBlock Pin Mapper</a> tool for possible conflicts.
:::

### Battery Selector

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19012/quickstart/rak19012-battery-solar.svg"
  figureCount="6"
  caption="Battery and solar panel connectors polarity" 
   width="50%"
  zoomMode={true}
/>

#### Rechargeable Battery

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19012/quickstart/rak19012-rak19010.svg"
  figureCount="1"
  caption="RAK19012 pinout and connector assignments" 
   width="70%"
  zoomMode={true}
/>

:::tip NOTE
The voltage of the battery must not exceed 4.3&nbsp;V.
:::

RAK19012 can be powered by a rechargeable Li-ion/LiPo battery via the dedicated connectors, as shown in **Figure 6**. The matching connector for the rechargeable battery wires is a <a href="https://www.jst-mfg.com/product/detail_e.php?series=199" target="_blank">JST PHR-2 2 mm pitch female</a>. A cable assembly for the rechargeable battery connector is also available for purchase in <a href="https://store.rakwireless.com/products/battery-connector-cable" target="_blank">RAK store</a>.

:::warning 

- Batteries can cause harm if not handled properly.
- Only 3.7&nbsp;V-4.2&nbsp;V rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you are familiar with the risks.
- Ensure the battery wires, both rechargeable and non-rechargeable, match the polarity on the RAK19012 board. Not all batteries have the same wiring.

:::

#### Solar Panel Connection

The battery can be recharged, as well, via a small Solar Panel, as shown in **Figure 6**. The matching connector for the solar panel wires is an <a href="https://www.jst-mfg.com/product/detail_e.php?series=287" target="_blank">JST ZHR-2 1.5&nbsp;mm pitch female</a>. A cable assembly for the solar panel connector is also available for purchase in <a href="https://store.rakwireless.com/products/solar-panel-connector-cable" target="_blank">RAK store</a>.


:::warning 

- Only 5&nbsp;V solar panels are supported. Do not use 12&nbsp;V solar panels. It will destroy the charging unit and eventually other electronic parts.
- The GND pin of the solar panel connector is located on edge of the board. Ensure the solar panel wires match the polarity on the RAK19012 board.

:::

## Product Configuration

### Software Setup

No software is required to use the RAK19012. However, to control the two user LEDs and monitor the battery voltage, it must be attached to a WisBlock Base and WisBlock Core.

### Examples

To quickly build your IoT device with less hassle, example codes for WisBlock Core are provided. You can access the codes in the <a href="https://github.com/RAKWireless/WisBlock/tree/master/examples" target="_blank">WisBlock example code repository</a>. The example codes in the `common` folder are compatible with RAK4631, RAK11200, and RAK11310 WisBlock Cores.
The two user LEDs of the RAK19012 can be accessed using macrodefinitions `LED_GREEN`/`PIN_LED1` for the green LED and `LED_BLUE`/`PIN_LED2` for the blue LED. For battery voltage reading, `WB_A0` is used.

## Tutorials and Resources

<a href="https://www.youtube.com/watch?v=fv0y22VDVB0" target="_blank">Create Modular Power Supply with WisBlock Power Boards</a>

<RkBottomNav/>