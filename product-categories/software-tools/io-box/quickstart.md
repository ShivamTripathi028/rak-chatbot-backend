---
title: IO.Box Quick Start Guide
description: Learn how to use IO.Box for easy WisNode Bridge Lite management, including LoRaWAN setup, AI/AO, DI/DO, Modbus configuration, device info, and firmware upgrades. Streamline your IoT device effortlessly with IO.Box.
image: https://images.docs.rakwireless.com/software-tools/io-box.png
keywords:
  - wistoolbox
sidebar_label: Quick Start Guide
---

# IO.Box Quick Start Guide

IO.Box is a software application designed for the easy configuration of WisNode Bridge devices, specifically the [RAK2470](https://store.rakwireless.com/products/wisnode-bridge-serial-prime-rak2470?utm_source=rak2470&utm_medium=Document&utm_campaign=BuyFromStore) and the RAK246X series devices. This application is available for:

- [Windows](https://apps.microsoft.com/detail/9nbxvlt622bs?hl=en-US&gl=US)
- [Linux](https://downloads.rakwireless.com/#IO.Box/) (coming soon)
- [Mac](https://downloads.rakwireless.com/#IO.Box/) (coming soon)

## Connect a Device

1. To configure the application, connect the device to the computer using the provided USB cable.
2. Start the IO.Box and click **Connect Device**.

> **Image:** Start the IO.Box

3. After clicking **Connect Device**, the device will be automatically detected, and the **LoRaWAN Configuration** tab will appear.

:::tip NOTE
- If the device is not automatically detected, click **Connect Manually** and follow the instructions to add it.
- The main menu on the left will differ depending on the device you are configuring.
:::

## Interface

#### LoRaWAN Tab

In this tab, you can see and change the LoRaWAN configuration and information. After the configuration, click **Save** to register the changes.

> **Image:** LoRaWAN tab

- **Device EUI** - The unique identifier of the device.
- **Region** - LoRaWAN region/band.
- **Join Mode** - Configure the Join mode based on the device's network access mode.
    - **Over-The-Air Activation (OTAA)**
    - **Activation By Personalization (ABP)**.
- **Class** - The LoRaWAN Class (C).
- **Application EUI** - Confirm that it matches the device's Application EUI as registered in the network server.
- **Application Key** - Verify its alignment with the device's Application key registered in the network server.
- **Confirm Mode** - Activate to receive confirmation messages from the network server for each uplink.
- **ADR** - Allows the network server to control the data rate for your device.
- **Data Collection Interval** - Set up the data collection period (polling period) of the device.
  - Range: 60~86400 seconds
- **LoRaWAN Status** - Indicates if the device is joined in the LoRaWAN network or not.

#### RS485 Tab

In this tab, you can configure the device to match the RS485 settings of the connected sensor.

> **Image:** RS485 tab

- **RS485 Interface Configuration** - The parameters between the sensor that is going to be connected and the bridge device need to match.
  - **Baudrate** - Select the communication speed for the RS485 interface, measured in bits per second. Choose a rate that matches your sensor's requirements.
  - **Databits** - Select the number of data bits for each character in the RS485 communication. Typically, options include 7 or 8 bits, depending on your sensor's protocol requirements.
  - **Stopbits** - Select the number of stop bits used in the RS485 communication. Common options are 1 or 2, depending on your sensor's data transmission protocol.
  - **Parity** - Select the parity setting for the RS485 interface. Options typically include **None** for no parity, **Even** for even parity, or **Odd** for odd parity. Choose based on your sensor's communication requirements.
-  **Modbus Poll Task** - Here, you can see/create/delete/edit the Modbus poll that will be issued to the sensor connected to the bridge. Also, you can enable or disable the given Modbus poll.

#### DI/DO Tab

In this tab, you can set up the Digital Output. This tab appears only if your device supports DI/DO (like RAK2461). You can enable or disable, and change the state of the digital output ports. Then click **Save** to send the configuration to the device.

> **Image:** DI/DO tab

- **Port ID** - The digital input port ID, found on the device's enclosure label.
- **Channel ID** - The polling task ID, included in the uplink data to indicate the data source.
- **Output State** - Toggle to change the state of this digital output port (active or inactive).
- **Enable** - Toggle to activate the polling task, enabling it to report the port's state.

#### System Tab

This tab shows the general information about your device, you can choose the power output and you can perform system resets and updates.

> **Image:** System tab 1

> **Image:** System tab 2

- ** Device Version Information **
  - **Hardware Version** - Displays the specific version of the device's hardware.
  - **Firmware Version** - Displays the device's firmware version.
  - **Device EUI** - Displays the unique identifier assigned by the manufacturer.
  - **Device Model** - Displays the specific model name or number of the device.
  - **Serial Number** - Displays the device's serial number of the device.
  - **Device Type** - Indicates the device's category, defining its interface types and functionalities. For detailed specifications, refer to the model information.
  - **Frequency Band** - The device's frequency band.

- ** Power Output **
  - **DC Vout Output** - Toggle to enable or disable the Vout power output. When enabled, Vout passes through the same voltage as the Vin input.
  - **DC 12V Output** - Toggle to enable or disable the 12V_Out power output, which provides a 12 V/0.5 A power output when enabled.

:::tip NOTE
The **Power Output** option is not available in **RAK2470**.
:::

- ** System Reset & Firmware Update ** - Buttons for performing the desired task.

#### Console Tab

This tab shows a log of the AT commands sent by the IO.Box and the device's responses.

> **Image:** Console tab

