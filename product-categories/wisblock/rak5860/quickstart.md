---
slug: /product-categories/wisblock/rak5860/quickstart/
title: RAK5860 WisBlock NB-IoT Interface Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK5860. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak5860/rak5860.png"
keywords:
    - RAK5860
    - wisblock
    - quickstart
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK5860 WisBlock NB-IoT Interface Module Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each step of using the RAK5860 WisBlock NB-IoT Interface Module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK5860](https://store.rakwireless.com/products/rak5860-lte-nb-iot-extension-board?utm_source=RAK5860&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- GNSS and GSM Antennas
- [Li-Ion/LiPo battery](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install the [Arduino IDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino board, install the RAKwireless Arduino BSP. Follow the steps in the [GitHub repo](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

You can integrate the RAK5860 module on your WisBlock project to extend its functionality and have Cellular, LPWAN, LTE-M, and NB-IoT capability with GPS. This is ideal for IoT and tracking applications where there is a cellular LPWAN network in the area. For more information about RAK5860, refer to its [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak5860/datasheet/).

RAK5860 module can be mounted to the IO slot of the WisBlock Base and communicates with the WisBlock Core via UART. The module is activated via `WB_IO1` pin of the WisBlock Core. Two antennas must also be connected to the module, one for the GNSS antenna port and one for the Cellular antenna port. An external battery (Li-Ion/LiPo 3.7-4.2&nbsp;V) is also required to power up the module properly.

:::warning 
- Batteries can cause harm if not handled properly.
- Only 3.7-4.2&nbsp;V rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board, to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5&nbsp;V solar panels are supported. Do not use 12&nbsp;V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires match the polarity on the WisBlock Base board. Not all batteries have the same wiring.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/rak5860_assembly.png" 
  caption="RAK5860 connection to WisBlock Base" 
   width="60%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/battery-connection.gif" 
  caption="WisBlock Base battery polarity and connection" 
   width="30%"
/>


#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 3**, the location for the module slots is properly marked by silkscreen. Follow the procedure defined in the [WisBlock Base assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3&nbsp;mm screws, depending on the module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/rak5860_mounting.png" 
  caption="RAK5860 connection to WisBlock Base" 
   width="70%"
/>

##### Disassembling

The procedure for disassembling any type of WisBlock module is the same.

1. First, remove the screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/16.removing-screws.png" 
  caption="Removing screws from the WisBlock module" 
   width="70%"
/>

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/17.detaching-silkscreen.png" 
  caption="Detaching silkscreen on the WisBlock module" 
   width="70%"
/>

3. Apply force to the module at the position of the connector, as shown in **Figure 6**, to detach the module from the baseboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/18.detaching-module.png" 
  caption="Applying even forces on the proper location of a WisBlock module" 
   width="70%"
/>

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock IO Pin Mapping Tool](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) for possible conflicts. RAK5860 uses UART communication lines, and it can cause possible conflict, especially on some modules that also use UART.
:::

### Software Configuration and Example

The RAK5860 WisBlock GSM/GPRS Module uses UART serial communication lines. In this example code, you will be able to send AT commands to the RAK5860 module. This will ensure that your RAK5860 is functional and ready for your IoT project.

#### Initial Test of the RAK5860 WisBlock Module

If you have already installed the [RAKWireless Arduino BSP](https://github.com/RAKWireless/RAKWireless-Arduino-BSP-Index), the WisBlock Core and example code should be available in the Arduino IDE.

1. First, you need to select the WisBlock Core you have, as shown in **Figure 7** to **Figure 9**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/rak4631_board.png" 
  caption="Selecting RAK4631 as WisBlock Core" 
   width="100%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/rak11200_board.png" 
  caption="Selecting RAK11200 as WisBlock Core" 
   width="100%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/rak11300_board.png" 
  caption="Selecting RAK11300 as WisBlock Core" 
   width="100%"
/>

2. You also need to select the right serial port to upload the code, as shown in **Figure 10**.

:::tip NOTE
If you are using RAK11200 as WisBlock Core, you need to configure the BOOT0 pin before uploading. You need to short it to the ground then press the reset button of the WisBlock Base before releasing the BOOT0 pin. If not done properly, uploading the source code to RAK11200 will fail. Check the full details on the [RAK11200 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/).
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/select_port.png" 
  caption="Selecting the correct Serial Port" 
   width="100%"
/>

3. Once you are ready with the Arduino IDE software and the WisBlock Core modules are already added, you can now check the Cellular examples available for the RAK5860 Cellular Wireless module. You can look at examples for TCP, MQTT, HTTP, and GPS on the [RAK5860 Examples Repository](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/communications/Cellular/RAK5860_BG77_Module).
4. The basic software example you can run is the [BG77_Unvarnished_Transmission](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/communications/Cellular/RAK5860_BG77_Module/BG77_Unvarnished_Transmission). This is a UART passthrough to the BG77 from RAK4631. This code will power up the module correctly and after initialization, AT commands is passed and received to the BG77 module. In the example below, the module responded to `AT` and `ATI` commands.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/sw_uart_passthru.png" 
  caption="UART Passthrough to BG77 Module" 
   width="85%"
/>

##### Software Examples

The following examples will illustrate the different protocols where RAK5860 can be used to access and send data to cloud.

:::warning 
All the examples that use cellular connectivity should update the APN sections of the code. To illustrate, the code below configures the PDP context to `1` and APN to `data.mono` for Monogoto SIM.

You can purchase [Monogoto SIM in the RAKwireless store](https://store.rakwireless.com/products/iot-sim-card-for-wisnode-modules?_pos=2&_sid=0f017e546&_ss=r&variant=42658018787526).

```c
  command = "AT+QICSGP=1,1,\"data.mono\",\"\",\"\",1";
  BG77_write(command.c_str());
  BG77_read(2000);
```
:::

###### GNSS Satellite Example

1. Go to the [GNSS satellite example code from the RAK5860 repository](https://github.com/RAKWireless/WisBlock/blob/master/examples/common/communications/Cellular/RAK5860_BG77_Module/RAK5860_GNSS_Satellite/RAK5860_GNSS_Satellite.ino).
2. Copy and paste the code to Arduino IDE, and click upload.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/sw_gnss_1.png" 
  caption="GNSS Example Code" 
   width="70%"
/>

:::warning 
BG77 is based on a cost-optimized architecture in which WWAN (LTE Cat-M1, LTE Cat-NB2, and GSM) and GNSS Rx chains share certain hardware blocks. As a result, the modules do not support the concurrent operation of WWAN and GNSS.
:::

3. The process will turn on the GNSS and Acquire Positioning Information and Query Satellite System as shown in the example. It should be able to obtain the latitude and longitude during the 30&nbsp;s ~ 2&nbsp;mins on power up. Open the `Serial Terminal` of Arduino from the Tools tab to see the output data/coordinates.

:::tip NOTE
If there are no coordinates data shown, make sure that you are exposed to a clear sky. You can also double-check that the antenna connector is properly attached to the module.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/sw_gnss_2.png" 
  caption="Serial Terminal output waiting for coordinates" 
   width="70%"
/>

###### HTTP Access Example

1. Go to the [HTTP Access example code from the RAK5860 repository](https://github.com/RAKWireless/WisBlock/blob/master/examples/common/communications/Cellular/RAK5860_BG77_Module/RAK5860_Access_HTTP_Server/RAK5860_Access_HTTP_Server.ino).
2. Copy and paste the code to Arduino IDE, and click upload.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/sw_http_1.png" 
  caption="HTTP Example Code" 
   width="65%"
/>

3. The process will first configure the APN of the cellular network, then set up the URL of the HTTP server to be accessed, send an HTTP GET/Read request, and enable the output of the HTTP response header to display on the Serial Terminal of the Arduino IDE.

:::tip NOTE
The server to be accessed in the example is `sina.com` but this can be changed to a different website.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/sw_http_2.png" 
  caption="Successful HTTP Get with reply" 
   width="65%"
/>

###### TCP Client Example

1. Go to the [TCP Client example code from the RAK5860 repository](https://github.com/RAKWireless/WisBlock/blob/master/examples/common/communications/Cellular/RAK5860_BG77_Module/RAK5860_TCP_Client/RAK5860_TCP_Client.ino).
2. Copy and paste the code to Arduino IDE and click upload.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/sw_tcp_1.png" 
  caption="TCP Example Code" 
   width="65%"
/>

3. The process will first configure the APN of the cellular network, then create a TCP socket connection and send data to the TCP server. You can see the status if the device has already sent the payload via the Serial Terminal of the Arduino IDE.

:::tip NOTE
You need to configure your own TCP server that will receive the transferred data. You have to edit the `AT+QIOPEN` and put the address of your server.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/sw_tcp_2.png" 
  caption="TCP Client connection" 
   width="80%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/sw_tcp_3.png" 
  caption="Data transmitted from TCP Client" 
   width="80%"
/>

###### MQTT Example

1. Go to the [MQTT Client example code from the RAK5860 repository](https://github.com/RAKWireless/WisBlock/blob/master/examples/common/communications/Cellular/RAK5860_BG77_Module/RAK5860_MQTT/RAK5860_MQTT.ino).
2. Copy and paste the code to Arduino IDE, and click upload.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/sw_mqtt_1.png" 
  caption="MQTT Example" 
   width="65%"
/>

3. The process will first configure the APN of the cellular network, then configure the MQTT Broker (in this example, pointing to a specific address). It will then subscribe to an MQTT topic in the setup section and continuously publish **Hello RAKwireless** at fixed intervals. You can see the status if the device has already sent the payload via the Serial Terminal of the Arduino IDE.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/sw_mqtt_2.png" 
  caption="MQTT Subscription to Topic" 
   width="65%"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5860/quickstart/sw_mqtt_3.png" 
  caption="MQTT Publishing in fix intervals" 
   width="65%"
/>

<RkBottomNav/>