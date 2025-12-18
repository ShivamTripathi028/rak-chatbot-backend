---
slug: /product-categories/wistrio/rak10715/quickstart/
title: RAK10715 WisTrio LTE-M NB-IoT LoRaWAN Development Board Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK10715 WisTrio LTE-M NB-IoT LoRaWAN Development Board. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device.
image: "https://images.docs.rakwireless.com/wistrio/rak10715/rak10715.png"
keywords:
    - RAK10715
    - wistrio
    - nb-iot
    - lte
    - lorawan
    - quick start guide
sidebar_label: Quick Start Guide
download: true
---

# RAK10715 WisTrio LTE-M NB-IoT LoRaWAN Development Board Quick Start Guide

## Prerequisites

Before going through each step in the installation guide of the RAK10715 WisTrio LTE-M NB-IoT LoRaWAN Development Board, make sure to prepare the necessary items listed below:

### Hardware

- [RAK10715 WisBlock Solution LTE-M NB-IoT LoRaWAN Development Board](https://store.rakwireless.com/products/link-one-lte-m-nb-iot-lorawan-device-based-on-nrf52840-sx1262-and-bg77-arduino-ide-compatible?variant=42659406512326?utm_source=LinkOne&utm_medium=Document&utm_campaign=BuyFromStore)
- USB-C Cable
- Li-Ion 3.7 V rechargeable battery
- 5 V Solar Panel (optional)

### Software

- Download and install the [ArduinoIDE.](https://www.arduino.cc/en/Main/Software)
- To add the RAKwireless Core boards on your Arduino Boards Manager, install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

### Package Inclusion

When you buy RAK10715, you can choose between two variants: one with bare modules and antennas and one with an enclosure and more optimized antennas.

> **Image:** RAK10715 modules without Enclosure

> **Image:** RAK10715 with Enclosure

## Product Configuration

### Hardware Setup

#### RAK10715 Without Enclosure

1. Assemble each module, including the respective antenna. Refer to **Figure 3** for the connections.

> **Image:** RAK10715 Modules and Antenna Connection

2. When the modules are plugged in together, they should look the same as in **Figures 4** and **Figure 5**:

> **Image:** RAK10715 Modules top view

> **Image:** RAK10715 Modules bottom view

#### RAK10715 With Enclosure

1. If you got the RAK10715 with enclosure, you have to prepare the WisBlock Modules together with the WisBlock Baseplate with antenna, circular connector, IPEX-SMA cellular antenna connector, and GPS antenna.

> **Image:** RAK10715 with Enclosure

2. On the WisBlock Baseplate, you have to remove the cutout that is designed to be used for the mini-base board. This cutout part must be removed for RAK10715.

> **Image:** Removing the cutout section of the WisBlock Baseplate

3. After removing the cutout, you can now attach the WisBlock Base Board to the WisBlock baseplate using screws.

> **Image:** Attaching the WisBlock Base board to WisBlock Baseplate with PCB Antenna

4. The next step is to connect the IPEX-IPEX from the WisBlock Core to the WisBlock Baseplate with an antenna.

> **Image:** IPEX-to-IPEX connector

5. Then, you can attach it to the enclosure and complete it with the rest of the parts.

> **Image:** Mounting the modules to RAK10715 enclosure

> **Image:** Assembled RAK10715 with all the parts

:::tip NOTE
After assembling all the parts, connect the battery to the WisBlock Base. Without the battery connected, the BG77 Cellular Module will not be able to function correctly due to a lack of power source. The USB connection will not be able to provide enough power to achieve enough performance stability.
:::

### Software Setup

1. Install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index) for WisBlock by using the ```https://raw.githubusercontent.com/RAKwireless/RAKwireless-Arduino-BSP-Index/main/package_rakwireless_index.json``` board installation package, the WisBlock Core RAK4631 should now be available on the Arduino IDE.
2. RAK10715 uses the RAK4631 WisBlock Core as the main processor.

> **Image:** Selecting RAK4631 WisBlock Core of RAK10715

3. Once you are ready with the Arduino IDE software and the RAK4631 board has already been added, you can now check the cellular examples available for the RAK5860 Cellular Wireless module. You can look at examples for TCP, MQTT, HTTP, and GPS on the [RAK5860 Examples Repository](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/communications/Cellular/RAK5860_BG77_Module).

:::tip NOTE
RAK10715 software guide is focused on cellular applications. If you are looking for its LoRa and LoRaWAN functionality,
you can check the the [RAK4631 LoRa/LoRaWAN examples repository](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK4630/communications/LoRa).

For low-power examples, you can check:
- [LoRA P2P Deep Sleep example](https://github.com/RAKWireless/WisBlock/tree/master/tutorials/RAK4631-Deep-Sleep-P2P)
- [LoRaWAN Deep Sleep example](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK4630/communications/LoRa/LoRaWAN/RAK4631-DeepSleep-LoRaWan)
:::

4. The basic software example you can run is the [BG77_Unvarnished_Transmission](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/communications/Cellular/RAK5860_BG77_Module/BG77_Unvarnished_Transmission). This is a UART passthrough to the BG77 from RAK4631. This code will power up the module correctly, and after initialization, AT commands are passed and received to the BG77 module. In the example below, the module responded to `AT` and `ATI` commands.

> **Image:** UART Passthrough to BG77 Module

#### Software Examples

This section provides different example codes that can be used with RAK10715.

- [GNSS Satellite](quickstart.md#gnss-satellite-example)
- [HTTP Access](quickstart.md#http-access-example)
- [TCP Client](quickstart.md#tcp-client-example)
- [MQTT](quickstart.md#mqtt-example)

The following examples show different protocols that RAK10715 can use it to access and send data to the cloud. This can be done easily with the included Monogoto SIM card on RAK10715.

:::warning
All the examples that use cellular connectivity should update the APN sections of the code for the cellular SIM card used. To illustrate, the code below configures the PDP context to `1` and APN to `data.mono` for a Monogoto SIM.

```c
  command = "AT+QICSGP=1,1,\"data.mono\",\"\",\"\",1";
  BG77_write(command.c_str());
  BG77_read(2000);
```
:::

##### GNSS Satellite Example

1. Go to the [GNSS satellite example code from the RAK5860 repository](https://github.com/RAKWireless/WisBlock/blob/master/examples/common/communications/Cellular/RAK5860_BG77_Module/RAK5860_GNSS_Satellite/RAK5860_GNSS_Satellite.ino).
2. Copy and paste the code into the Arduino IDE and click upload.

> **Image:** GNSS Example Code

:::warning
BG77 is based on a cost-optimized architecture in which WWAN (LTE Cat-M1, LTE Cat-NB2, and GSM) and GNSS Rx chains share certain hardware blocks. As a result, the modules do not support the concurrent operation of WWAN and GNSS.
:::

3. The process will turn on the GNSS and the Acquire Positioning Information and Query Satellite System, as shown in the example. It should be able to obtain the latitude and longitude within 30 s ~ 2 mins of power-up. Open `Serial Terminal` in Arduino from the Tools tab to see the output data/coordinates.

:::tip NOTE
If there are no coordinates shown, make sure that you are exposed to a clear sky. You can also double-check that the antenna connector is properly attached to the module.
:::

> **Image:** Serial Terminal output waiting for coordinates

##### HTTP Access Example

1. Go to the [HTTP Access example code from the RAK5860 repository](https://github.com/RAKWireless/WisBlock/blob/master/examples/common/communications/Cellular/RAK5860_BG77_Module/RAK5860_Access_HTTP_Server/RAK5860_Access_HTTP_Server.ino).
2. Copy and paste the code into the Arduino IDE and click upload.

> **Image:** HTTP Example Code

3. The process will first configure the APN of the cellular network, then set up the URL of the HTTP server to be accessed, send an HTTP GET/Read request, and enable the output of the HTTP response header to display on the Serial Terminal of the Arduino IDE.

:::tip NOTE

The APN must be configured to the correct setting based on the SIM card used on RAK10715.

The server to be accessed in the example is `sina.com`, but this can be changed to a different website.

:::

> **Image:** Successful HTTP Get with reply

##### TCP Client Example

1. Go to the [TCP Client example code from the RAK5860 repository](https://github.com/RAKWireless/WisBlock/blob/master/examples/common/communications/Cellular/RAK5860_BG77_Module/RAK5860_TCP_Client/RAK5860_TCP_Client.ino).
2. Copy and paste the code into the Arduino IDE and click upload.

> **Image:** TCP Example Code

3. The process will first configure the APN of the cellular network, then create a TCP socket connection and send data to the TCP server. You can see the status if the device has already sent the payload via the serial terminal of the Arduino IDE.

:::tip NOTE
You need to configure your own TCP server that will receive the transferred data. You have to edit the `AT+QIOPEN` and put the address of your server.
:::

> **Image:** TCP Client connection

> **Image:** Data transmitted from TCP Client

##### MQTT Example

1. Go to the [MQTT Client example code from the RAK5860 repository](https://github.com/RAKWireless/WisBlock/blob/master/examples/common/communications/Cellular/RAK5860_BG77_Module/RAK5860_MQTT/RAK5860_MQTT.ino).
2. Copy and paste the code into the Arduino IDE and click upload.

> **Image:** MQTT Example

3. The process will first configure the APN of the cellular network, then configure the MQTT Broker (in this example, pointing to a specific address). It will then subscribe to an MQTT topic in the setup section and continuously publish **Hello RAKwireless** at fixed intervals. You can see the status if the device has already sent the payload via the serial terminal of the Arduino IDE.

> **Image:** MQTT Subscription to Topic

> **Image:** MQTT Publishing in a fixed interval

