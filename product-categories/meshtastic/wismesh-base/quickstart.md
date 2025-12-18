---
title: RAK19026 WisMesh Base Board Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your Meshtastic WisMesh Base. For a full documentation check the documentation of Meshtastic.org
image: "https://images.docs.rakwireless.com/meshtastic/wismesh-base-board.png"
keywords:
  - RAK4631
  - wisblock
  - Meshtastic
  - Nordic
  - nRF52840
  - Semtech
  - SX1262
sidebar_label: Quick Start Guide
---

# RAK19026 WisMesh Base Board Quick Start Guide

WisMesh Base is a base board, ideal for creating your own Meshtastic node, simplifying assembly without requiring extra cables.

This guide covers the basics for the RAKwireless Meshtastic devices that are not covered by the [Meshtastic documentation](https://meshtastic.org/docs/introduction).

For detailed instructions how to configure the devices for the Meshtastic network, follow the [Meshtastic Getting Started](https://meshtastic.org/docs/getting-started) guide.

You can also check the Meshtastic Basic Device Setup Guide:.

<div class="flex items-center flex-col align-center gap-2">
  [ Meshtastic Basic Device Setup ](https://docs.rakwireless.com/product-categories/meshtastic/meshtastic-basic-device-setup/)
</div>

----

The Meshtastic Base is different from our other WisBlock Base Boards, as it has the RAK4630 module directly mounted on the Base Board.

:::warning Important
This documentation is for board version VC. There are some differences to the older board versions.
For information on older board versions, check the referring datasheet:
- [Latest board version VC](https://docs.rakwireless.com/product-categories/meshtastic/wismesh-base/datasheet-vc/)
- [Board version VA](https://docs.rakwireless.com/product-categories/meshtastic/wismesh-base/datasheet-va/)
:::

## Prerequisite

Before going through each and every step on using WisMesh Pocket, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK19026 WisMesh Base](https://store.rakwireless.com/products/rak19007-wisblock-base-board-2nd-gen?utm_source=RAK19026)
- Your choice of [WisBlock Modules](https://store.rakwireless.com/pages/wisblock).

It is highly recommended to also check the dedicated Quick Start Guide that you can follow on various WisBlock Modules. Each Quick Start Guide of these modules contains the detailed steps on how to open the example codes and upload them to the WisBlock Core.
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- Type-C USB cable for programming and debugging

#### Software

The RAK4630 on the WisMesh Base Board comes already pre-flashed with the Meshtastic firmware.

:::tip NOTE
To be sure to run the latest version of the Meshtastic firmware, we advice you to download the latest [Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is autodetected. This device works with the stock firmware.

- For the WisMesh Base RAK19026: use **`firmware-rak4631-w.x.yy.zzzzzzz.uf2`**
- For the WisMesh Base RAK19026:  _**DO NOT USE**_ **`firmware-rak4631_eink-w.x.yy.zzzzzzz.uf2`**
:::

## Product Configuration

### Overview

To give you a better understanding of how the WisMesh Base works, the block diagram of the RAK19026 is provided in this section.

#### Block Diagram

The block diagram in **Figure 1** shows the internal architecture and external interfaces of the RAK19026 WisMesh Base Board.

> **Image:** RAK19026 WisMesh Base Board block diagram

The RAK4630 module on the WisMesh Base Boards is based on the Nordic nRF52840 MCU and the Semtech SX1262 LoRa transceiver. It offers the I2C, UART, and SPI data buses and GPIO's to the sensor modules. Through these buses, the MCU can control and retrieve data from the sensors.

Some MCU IO pins have an alternate function. In this case, you have the option to modify the IO via software or rework the hardware to redefine the function of IO. Refer to the [WisDuo RAK4630 datasheet](https://docs.rakwireless.com/product-categories/wisduo/rak4630-module/datasheet/) to get all the details.

The RAK19026 is designed to be powered by a battery and has a charger circuitry for **lithium batteries**. The charger circuitry can be connected to a wall outlet charger through a Type-C USB connector, or the specific connector for a solar panel. The voltage coming from the Type-C USB port or solar panel connector goes only to a charger chip. The charger chip detects when to recharge the battery and stops charging when it is fully charged.  The output of the charger chip is used to supply the WisBlock modules via a step-down converter.

:::tip NOTE
To comply with CE regulations, the board versions for Europe are equipped with a 3 pin battery connector and can be only used with Li-Ion batteries with an integrated NTC temperature sensor and a 3 wire connector.
Other board versions are equipped with a 2 pin battery connector. An NTC temperature sensor is integrated on the main board.
:::

A switch between the battery output and the on-board DC-DC converter can power down the MCU and all sensor and IO modules. The charger chip remains active in the OFF position, allowing the battery to recharge through the USB port or solar connector.

A high-efficiency step-down converter with a low quiescent current is used to generate 3.3 V. This 3.3 V power supply drives the consumption of the WisBlock Core module and the sensor modules. The max current supported by the 3.3 V LDO is 750 mA.

3V3_S is another 3.3 V power supply, it can be controlled by the MCU to disconnect the power sensors during idle periods to save power. 3V3_S is controlled by the IO2 pin on the WisBlock Core board.

- Set **IO2=1**, 3V3_S is on.
- Set **IO2=0**, 3V3_S is off.

### Hardware Setup

#### RAK19026 WisMesh Base Board Installation Guide

RAK19026 WisBlock Base Board is the main board with an onboard RAK4630 WisDuo module. It allows you to attach WisBlock sensors and IO modules through the standardized expansion connectors. These connectors provide a data bus interconnection between the modules attached to the RAK19026 Base Board.

This guide shows the details related to the installation of modules into the RAK19026 board. The following section discusses the general concepts to manipulate the WisBlock Connector in any WisBlock Module. The installation and removal details of each type of WisBlock module: Core and Sensor are explained.

##### Attaching a WisBlock Connector

The WisBlock Connector is the interface between the RAK19026 board and the WisBlock Core, Sensor, and IO modules. Before connecting these modules, read the following instructions:

:::tip NOTE
This guide uses two arrows. Refer to **Figure 2** for its representation.
:::

> **Image:** Notation within the guide

1. Align the connectors. Keep the header parallel and place it lightly in the corresponding lap joint of the socket.

> **Image:** Alignment of WisBlock Connector

2. Fit the connector. Tilt one end of the connector (header) less than 20 degrees, gently place the other end parallel without applying force.

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

###### WisBlock IO

A WisBlock IO module is designed to be installed on the IO slot of the RAK19026 Base Board. The location is properly marked by silkscreen. Follow carefully the procedure defined in [attaching a WisBlock Connector](https://docs.rakwireless.com/product-categories/wisblock/rak19007/quickstart/#attaching-a-wisblock-connector) section in order to attach an IO module.
 Once attached, fix the module with one or more pieces of M1.2 x 3 mm screws depending on the WisBlock IO.

> **Image:** WisBlock IO silkscreen on the RAK19026 Base Board

###### WisBlock Sensor

A WisBlock Sensor module is designed to be installed on the Sensor slots of the RAK19026 Base Board. The location of the slots is properly marked by silkscreen. Follow carefully the procedure of the section, [attaching a WisBlock Connector](https://docs.rakwireless.com/product-categories/wisblock/rak19007/quickstart/#attaching-a-wisblock-connector), to attach a WisBlock Sensor module. Once attached, fix the module with an M1.2 x 3 mm screw.

> **Image:** WisBlock Sensor silkscreen on the top of RAK19026 Base Board

##### Disassembling a WisBlock Module

1. The procedure to disassemble any type of WisBlock modules is the same. As shown below, first, remove the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed, on the PCB of a WisBlock module, there is a silkscreen that shows the correct location where force can be applied. By applying even force under the marked area, the module can be detached from the Base Board.

> **Image:** Detaching silkscreen on the WisBlock module

> **Image:** Applying even forces on the proper location of a WisBlock module to detach the module from the Base Board

#### Battery and Solar Panel / 5V Connection

RAK19026 can be powered via the USB cable or Li-Ion/LiPo battery via the dedicated connectors, as shown in **Figure 19**. The matching connector for the battery wires is a depending on the board variant
- For EU/UK (CE & UKCA certification) [JST PHR-3 2 mm pitch female](https://www.jst-mfg.com/product/detail_e.php?series=199).
- For other markets  [JST PHR-2 2 mm pitch female](https://www.jst-mfg.com/product/detail_e.php?series=199).

The battery can be recharged as well via a small solar panel or a regulated 5 V supply, as shown in **Figure 19**. The matching connector for the battery wires is a [JST ZHR-2 1.5 mm pitch female](https://www.jst-mfg.com/product/detail_e.php?series=287).

> **Image:** Battery connector pin order

:::warning IMPORTANT
The version of the RAK19026 with a 3-pin battery connector requires a matching battery with NTC temperature sensor and a 3-wire cable. If a different battery is used, the battery will not be charged.
:::

:::warning
- Battery can cause harm if not handled properly.
- Only 3.7-4.2 V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Make sure the battery wires match the polarity on the RAK19026 board. Not all batteries have the same wiring.
:::

:::warning
- Only 5 V solar panels are supported. Do not use 12 V solar panels. It will destroy the charging unit and eventually other electronic parts.
- The GND pin of the Solar Panel Connector is located on edge of the board. Make sure the Solar Panel wires are matching the polarity on the RAK19007 board.
:::

The full specification of the [Solar Panel Connection](https://docs.rakwireless.com/product-categories/meshtastic/wismesh-base/datasheet-vc/) can be found on the datasheet of the RAK19026 WisMesh Base Board 2nd Gen.

### LEDs

Three LEDs are used to indicate the operating status. Below are the functions of the LEDs:

🔴 Red LED - Connected to the charger chip to indicate the charger status. When the battery is charging, this red LED is on. When the battery is full, this LED is weak light or off.

🟢 Green LED - Connected to the MCU module, controlled by MCU defined by the user.

🔵 Blue LED - Connected to the MCU module, controlled by MCU defined by the user.

### Software Setup

To be sure to run the latest version of the Meshtastic firmware, we advice you to download the latest [Meshtastic firmware](https://meshtastic.org/downloads) and upload it to your RAKwireless device to make it compatible with the Meshtastic network.

For Firmware 1.3 and 2.0 (from November 1, 2022), the WisBlock Base board is autodetected. This device works with the stock firmware.

- All the base boards with RAK4631/RAK4630: - **`firmware-rak4631-w.x.yy.zzzzzzz.uf2`**
- For RAK19026:  _**DO NOT USE**_ - **`firmware-rak4631_eink-w.x.yy.zzzzzzz.uf2`**

**Flashing the WisMesh Base firmware:**

The RAK4630 on the WisMesh Base Board come pre-flashed with the Meshtastic firmware. If you encounter problems, update the Meshtastic firmware to the latest version.

- [**Meshtastic.org** guide to flash nRF52 devices](https://meshtastic.org/docs/getting-started/flashing-firmware/nrf52)

For the setup of the WisMesh Base Board for the Meshtastic network, follow the [configuration guide](https://meshtastic.org/docs/configuration) in the Meshtastic documentation.

