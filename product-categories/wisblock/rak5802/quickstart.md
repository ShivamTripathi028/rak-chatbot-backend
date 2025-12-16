---
slug: /product-categories/wisblock/rak5802/quickstart/
title: RAK5802 WisBlock RS485 Interface Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK5802. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: https://images.docs.rakwireless.com/wisblock/rak5802/rak5802.png
keywords:
  - quickstart
  - wisblock
  - RAK5802
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK5802 WisBlock RS485 Interface Module Quick Start Guide



## Prerequisite

### What Do You Need?

Before going through each and every step on using the RAK5802 WisBlock module, make sure to prepare the necessary items listed below:

#### Hardware

- 2 x [RAK5802](https://store.rakwireless.com/products/rak5802-rs485-interface?utm_source=RAK5802&utm_medium=Document&utm_campaign=BuyFromStore)
- 2 x Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base)
- 2 x Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- 2 x USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install [Arduino IDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino board, install the RAKwireless Arduino BSP. Follow the steps in the [GitHub repo](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

WisBlock can integrate this module, which extends the WisBlock system with an industrial RS485 data transmission interface.

RAK5802 supports one RS485 interface. There are also two voltage sources available on the connectors, which you can use on your external device or circuit. One is the battery voltage via PWR pin, which is directly coming from the battery connected to the WisBlock Base. The other one is the 3.3&nbsp;V regulated output, which comes from the WisBlock Base, as well, and powers the entire WisBlock board, including the WisBlock Core and other connected modules. In addition, an Analog A1 input (via WB_A1 in code) and I2C interface connection are available on the crimping terminal.


<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/rak5802_pinout.png" 
  figureCount="1"
  caption="RAK5802 sensor connector" 
   width="70%"
/>


For more information about the RAK5802, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak5802/datasheet/).

The RAK5802 module is part of the WisBlock Interface category, which connects to the base board through the IO slot. Also, always secure the connection of the WisBlock module by using compatible screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/rak5802_assembly.png" 
  figureCount="2"
  caption="RAK5802 connection to WisBlock Base" 
   width="80%"
/>


#### Installation

##### Mounting Mechanism

The RAK5802 module is part of the WisBlock Interface category, which connects to the baseboard through the IO slot. The installation method is shown in **Figure 3** and **Figure 4**.

1. Keep the RAK5802 module parallel to the baseboard, and gently place and plug WisConnector into the IO slot receptacle of the baseboard. The IO slot has an outer silkscreen on it to assist with the alignment. At this point, apply force evenly along with the module and press again. There will be a sound to confirm the successful completion of the attachment process.

:::tip NOTE
For detailed instructions, refer to the [WisBlock Installation Guide](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/).
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/wisconnector.png" 
  figureCount="3"
  caption="WisConnector" 
   width="50%"
/>


2. Always secure the RAK5802 module with **3 x M1.2 x3 pan head screws**, as shown in **Figure 4**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/rak5802_mounting.png" 
  figureCount="4"
  caption="RAK5802 connection to WisBlock Base" 
   width="70%"
/>


##### RAK5802 Sensor Connector Crimping Mechanism

The RAK5802 features a fast-crimping terminal connector to simplify and ensure the wiring process on the fields. The fast-crimping terminal can support cable with a width between 20 AWG to 24 AWG. The usual stripping length is around 6 to 7&nbsp;mm.

As shown in **Figure 5**, during the crimping process, you should first press down and maintain the spring head of the crimping terminal firmly, then insert the stripped cable head into the corresponding connector’s hole. Once inserted correctly, then release the spring head, and the crimping process is completed.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/crimping_process.png" 
  figureCount="5"
  caption="RAK5802 Sensor Connector" 
   width="40%"
/>


##### Disassembling Procedure

The procedure in disassembling any type of WisBlock module is the same.

1. Remove the screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/16.removing-screws.png" 
  figureCount="6"
  caption="Removing screws from the WisBlock module" 
   width="70%"
/>


2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/17.detaching-silkscreen.png" 
  figureCount="7"
  caption="Detaching silkscreen on the WisBlock module" 
   width="70%"
/>


3. Apply force to the module at the position of the connector, as shown in **Figure 8**, to detach the module from the baseboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/18.detaching-module.png" 
  figureCount="8"
  caption="Applying even forces on the proper location of a WisBlock module" 
   width="70%"
/>


:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts. RAK5802 uses UART and I2C communication lines, and it can cause possible conflict especially on other WisBlock Modules connected to Slot A to D of the WisBlock Base.
:::

After all this setup, you can now connect the battery (optional) and USB cable to start programming your WisBlock Core.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/battery-connection.gif" 
  figureCount="9"
  caption="Battery connection to WisBlock Base Board" 
   width="50%"
/>


:::warning

- Batteries can cause harm if not handled properly.
- Only 3.7-4.2&nbsp;V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5&nbsp;V solar panels are supported. Do not use 12&nbsp;V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires are matching the polarity on the WisBlock Base board. Not all batteries have the same wiring.

:::

### Software Configuration and Example

A ready-to-use SW library and tutorial make it easy to connect any sensor that is using the RS485 interface.

The sample code will require two sets of WisBlock Base (RAK5005-O), WisBlock Core (RAK4631/RAK11200) and WisBlock RS485 Interface Module. You only need to connect the two wires of the RS485 bus, as shown in **Figure 10**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/rak5802_test_connection.png" 
  figureCount="10"
  caption="Connection Diagram" 
   width="60%"
/>


#### Initial Test of the RAK5802 WisBlock Module

If you already installed the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index), the WisBlock Core and example code should now be available on the Arduino IDE.

1. You need to select first the WisBlock Core you have, as shown in **Figure 11** to **Figure 13**.

**Using RAK4631 WisBlock Core**

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/rak4631_board.png" 
  figureCount="11"
  caption="Selecting RAK4631 as WisBlock Core" 
   width="100%"
/>


**Using RAK11200 WisBlock Core**

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/rak11200_board.png" 
  figureCount="12"
  caption="Selecting RAK11200 as WisBlock Core" 
   width="100%"
/>


**Using RAK11300 WisBlock Core**

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/rak11300_board.png" 
  figureCount="13"
  caption="Selecting RAK11300 as WisBlock Core" 
   width="100%"
/>


2. The Basic Sample Code for RAK5802 in GitHub will work on all WisBlock Core. You can open the example codes depending on your WisBlock Core, as shown in **Figure 14** to **Figure 16**.

- Sample code for [RAK4631](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK4630/IO/RAK5802_RS485)


<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/rak4631_example.png" 
  figureCount="14"
  caption="Opening RAK5802 example code for RAK4631 WisBlock Core" 
   width="100%"
/>


- Sample code for [RAK11200](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK11200/IO/RAK5802_RS485)

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/rak11200_example.png" 
  figureCount="15"
  caption="Opening RAK5802 example code for RAK11200 WisBlock Core" 
   width="100%"
/>


- Sample code for [RAK11300](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK11300/IO/RAK5802_RS485)

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/rak11300_example.png" 
  figureCount="16"
  caption="Opening RAK5802 example code for RAK11300 WisBlock Core" 
   width="100%"
/>


3. Once the example code is open, install the [Arduino RS485](https://www.arduino.cc/en/Reference/ArduinoRS485) library by clicking the yellow-highlighted link, as shown in **Figure 17** and **Figure 18**. Or, if you are using Modbus protocol, install the [Arduino Modbus](https://www.arduino.cc/en/ArduinoModbus/ArduinoModbus).

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/rak5802_code.png" 
  figureCount="17"
  caption="Installing the compatible library for RAK5802 Module" 
   width="100%"
/>


<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/rak5802_search.png" 
  figureCount="18"
  caption="Accessing the library used for RAK5802 Module" 
   width="100%"
/>


4. After successful installation of the library, you can now select the right serial port and upload the 'Receiver' code to the first board and 'Sender' code to the second board, as shown in **Figure 19** and **Figure 20**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/rak5802_select_port.png" 
  figureCount="19"
  caption="Selecting the correct Serial Port" 
   width="100%"
/>


<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/rak5802_upload.png" 
  figureCount="20"
  caption="Uploading the RAK5802 example code" 
   width="100%"
/>


5. When you successfully uploaded the example sketch, connect the board with the 'Receiver' code, open the Serial Monitor of the Arduino IDE, and power the 'Sender' board via USB or Battery to see the reading logs. If you see the logs, as shown in **Figure 21**, then your RAK5802 is properly communicating to the WisBlock core.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5802/quickstart/rak5802_logs.png" 
  figureCount="21"
  caption="RAK5802 data logs from 'Sender' board" 
   width="100%"
/>



<RkBottomNav/>



