---
slug: /product-categories/wistrio/rak8212/at-command-manual/
title: RAK8212 WisTrio iTracker Pro AT Command Manual
description: For an easier experience with your RAK8212 WisTrio iTracker Pro, a comprehensive list of commands in configuring your device is provided.
image: "https://images.docs.rakwireless.com/wistrio/rak7205-5205/rak5205.png"
keywords:
  - wistrio
  - at command manual
  - rak7205
  - rak5205
  - wistrio
  - tracker
  - lpwan
  - lorawan
sidebar_label: AT Command Manual
---

# RAK8212 WisTrio iTracker Pro AT Command Manual

The purpose of this section is to demonstrate how to configure the RAK8212 WisTrio iTracker Pro thru the use of AT Commands via Bluetooth. The list below shows the AT Commands available for use:

| **AT Command**                                                      | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `at+version`                                                          | Get the current firmware version number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `at+set_config=device:restart`                                        | After set, the device will restart.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `at+get_config=device:status`                                         | Get all information about the device’s hardware components and their current status                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `at+set_config=device:sleep:X`                                   | After set, the device will go to sleep or wake up immediately. 
• **0** - sleep 
• **1** - wake up                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `at+set_config=device:sleep_interval:X:Y`                    | Set the sleep interval. 
• **X** - **0**: off, **1**: on. 
• **Y** - the interval time. (ms) If the **X** is set to 1, it means that the device will sleep for **Y** ms after sending a message automatically in a loop, until you set **X** to 0.                                                                                                                                                                                                                                                                                                                     |
| `at+set_config=device:gps:X`                                    | • **X** - **0**: close, **1**: open, **2**: sleep, **3**: standby                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `at+scan=cellular`                                                    | Scan the Cellular networks available in your place                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `at+set_config=cellular:XXX:Y:ZZZ: AAA:BBB:C` | Sets the IP address and port on which you want to send data to through Cellular. 
• **XXX** - the IP address you want to send data to. 
• **Y** - the port you want to send data to. 
• **ZZZ** -The cellular operator’s long name you want to connect, for example:CHINA MOBILE. 
• **AAA** - The short name of the Cellular operator, for example: CMCC. 
• **BBB** - The operator’s APN name, for example CMNET. 
• **C** - The number of the Cellular network type. For example, 0 indicates GSM, 8 indicates LTE cat.M1, and 9 indicates LTE cat.NB1. |
| `at+set_config=cellular:XXX`                                     | Set the Cellular module using the Cellular module’s common AT commands which come from its manufacturer. 
• **XXX -** The Cellular module’s common AT commands. For the full list of supported Quectel BG96 AT Commands, go [here](https://www.quectel.com/product/bg96.htm).                                                                                                                                                                                                                                                                                           |
| `at+send=cellular:XXX`                                           | Send data through cellular. 
• **XXX -** The data you want to send.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

