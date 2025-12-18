---
title: RUI3 | Unified IoT Development API for LoRaWAN
description: RUI3 is a unified IoT development API for LoRaWAN, LoRa P2P, and LPWAN, simplifying firmware customization and AT command control for seamless integration. 
image: "https://images.docs.rakwireless.com/software-apis-and-library/software-apis-and-library/rui3/rui3.png"
keywords:
  - at commands list
  - lora at commands
  - rui3 firmware
  - rui3 at commands
  - api for iot devices
  - iot development framework
  - lorawan firmware customization
  - lorawan at commands
  - lora p2p command
  - at command examples
sidebar_label: Product Overview
date: 2022-04-07
download: true
---

# RAKwireless Unified Interface V3 (RUI3)

## Overview

The RAKwireless Unified Interface V3 (RUI3) is designed to help IoT developers make their IoT products faster. It is compatible to RAK LPWAN modules. It supports the standard AT Commands which is known to many people<!---, as well as the Binary Mode-->.<!---The Binary mode is an improved version of the AT command with its efficient byte-array based protocol and implementation of checksum.--> RUI3 also allows you to create your own custom firmware using RUI3 APIs that are compatible to popular IDEs like Arduino and Visual Studio. With custom firmware, you will not need any external host microcontroller or microprocessor which can save you cost, circuit board space and current consumption.

### Hardware Compatibility

To start creating your custom RUI3 firmware, check the links of the individual RUI3 modules Quick Start Guides. There is a detailed documentation of RUI3 Arduino API as well.

RUI3 is compatible to the following RAK LPWAN modules:

| RAK Devices                                                                                                                     | Quick Start Guides                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [RAK4630](https://docs.rakwireless.com/product-categories/wisduo/rak4630-module/overview/)                                      | [RAK4630 RUI3 Guide](https://docs.rakwireless.com/product-categories/wisduo/rak4630-module/quickstart/#rak4630-as-a-stand-alone-device-using-rui3)                                    |
| [RAK4631-R](https://docs.rakwireless.com/product-categories/wisblock/rak4631-r/overview/)                                       | [RAK4631-R RUI3 Guide](https://docs.rakwireless.com/product-categories/wisblock/rak4631-r/quickstart/)                                                                                |
| [RAK3172](https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/overview/)                                      | [RAK3172 RUI3 Guide](https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/quickstart/#rak3172-as-a-stand-alone-device-using-rui3)                                    |
| [RAK3272S](https://docs.rakwireless.com/product-categories/wisduo/rak3272s-breakout-board/overview/)                            | [RAK3272S RUI3 Guide](https://docs.rakwireless.com/product-categories/wisduo/rak3272s-breakout-board/quickstart/#rak3272s-breakout-board-as-a-stand-alone-device-using-rui3)          |
| [RAK3372 / RAK3172 Evaluation Board](https://docs.rakwireless.com/product-categories/wisduo/rak3172-evaluation-board/overview/) | [RAK3172 Evaluation Board RUI3 Guide](https://docs.rakwireless.com/product-categories/wisduo/rak3172-evaluation-board/quickstart/#rak3172-e-as-a-stand-alone-device-using-rui3)       |
| [RAK3172-SiP](https://docs.rakwireless.com/product-categories/wisduo/rak3172-sip/overview/)                                     | [RAK3172-SiP RUI3 Guide](https://docs.rakwireless.com/product-categories/wisduo/rak3172-sip/quickstart/#rak3172-sip-as-a-stand-alone-device-using-rui3)                               |
| [RAK3272-SiP](https://docs.rakwireless.com/product-categories/wisduo/rak3272-sip-breakout-board/overview/)                      | [RAK3272-SiP RUI3 Guide](https://docs.rakwireless.com/product-categories/wisduo/rak3272-sip-breakout-board/quickstart/#rak3272-sip-breakout-board-as-a-stand-alone-device-using-rui3) |
| [RAK11720](https://docs.rakwireless.com/product-categories/wisduo/rak11720-module/overview/)                                    | [RAK11720 RUI3 Guide](https://docs.rakwireless.com/product-categories/wisduo/rak11720-module/quickstart/#rak11720-as-a-stand-alone-device-using-rui3)                                 |
| [RAK11721](https://docs.rakwireless.com/product-categories/wisduo/rak11721-breakout-board/overview/)                            | -                                                                                                                                                                                     |
| [RAK11722](https://docs.rakwireless.com/product-categories/wisblock/rak11722/overview/)                                         | -                                                                                                                                                                                     |
| [RAK11160](https://docs.rakwireless.com/product-categories/wisduo/rak11160-module/overview/)                                    | [RAK11160 RUI3 Guide](https://docs.rakwireless.com/product-categories/wisduo/rak11160-module/quickstart/#rak11160-as-a-stand-alone-device-using-rui3)                                 |

### RUI3 Software Guide

#### Writing RUI3 Custom Firmware

RAKwireless Unified Interface V3 (RUI3) features are utilized by using its RUI3 API.

:::tip NOTE
**RUI3 Board Support Package JSON URL**

 `https://raw.githubusercontent.com/RAKWireless/RAKwireless-Arduino-BSP-Index/main/package_rakwireless_com_rui_index.json`.
:::

The RUI3 API is well explained with examples codes in this documentation.

- [Arduino API](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/arduino-api/)
- [System](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/system/)
- [LoRaWAN](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/lorawan/)
- [BLE](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/ble/)
<!--- [Binary Mode](/RUI3/Binary-Mode/)-->

For you to compile and upload to the RAK module the RUI3 codes, you need to have an Arduino IDE, Visual Studio Code or Visual Studio IDE in your PC or laptop. The guide on doing this is on the quick start guide of the specific module you are using which is mentioned in the [Hardware Compatibility](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/#hardware-compatibility) section of this document.

#### Use of RUI3 Serial Commands (AT<!--- and Binary-->)

The RAK LPWAN modules with RUI3 can also be interfaced with an external host via [AT command mode (default)](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/at-command-manual/)<!--- and [Binary command mode](/RUI3/Serial-Operating-Modes/binary-command-manual/)-->. A custom serial interface can be created by the user using [Custom Mode](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/custom-mode/). When the serial interface is configured for Custom mode, the standard AT commands are disabled and will not be accepted anymore by the module unless switched again to AT mode.

The interfaces of RUI3 are via UART, USB, BLE, and NFC. The physical and wireless RUI3 interfaces are abstracted to behave as Serial Port, where the three [RUI3 Serial Operating Modes](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/serial-operating-modes/) can be configured by the user.

:::tip NOTE
RUI3 Serial Mode default configuration is `AT Command` and still available even with RUI3 Custom Firmware.
:::

[WisToolBox](https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/overview/) is also a compatible software tool with RUI3-powered devices. It can set up the LoRa/LoRaWAN parameters and configurations of the device and can also manage firmware updates.

#### RUI3 Supported IDE

- [Arduino IDE](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/supported-ide/#arduino-ide)
- [Visual Studio Code](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/supported-ide/#visual-studio-code-arduino-extension)
- [Visual Studio IDE](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/supported-ide/#visual-studio-ide)

