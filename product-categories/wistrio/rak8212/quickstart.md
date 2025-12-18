---
slug: /product-categories/wistrio/rak8212/quickstart/
title: RAK8212 WisTrio iTracker Pro Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK8212 WisTrio iTracker Pro. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device.
image: "https://images.docs.rakwireless.com/wistrio/rak8212/rak8212.png"
keywords:
  - wistrio
  - rak8212
  - tracker
  - quick start guide
  - nb-iot
  - bluetooth
sidebar_label: Quick Start Guide
---

# RAK8212 WisTrio iTracker Pro Quick Start Guide

## Prerequisite

Before going through each and every step in the installation guide of the RAK8212 WisTrio iTracker Pro Module, make sure to prepare the necessary items listed below:

1. [RAK8212 WisTrio iTracker Pro](https://store.rakwireless.com/products/rak8212-itracker-pro?utm_source=RAK8212iTrackerPro&utm_medium=Document&utm_campaign=BuyFromStore)
2. Emulator Kit
3. Connector Wires
4. 3.3 V Battery Power Supply
5. Windows PC
6. Android/IOS Mobile Device

:::tip NOTE
This device released by RAKwireless is already pre-loaded with its latest firmware upon manufacturing. If you want to have your device's firmware burned or upgraded, refer to the sections below:

- <a href="quickstart#device-firmware-setup" className='no-icon' style={{ color: '#006ac6' }}>Device Firmware Setup</a>

:::

### Package Inclusions

- 1 pc - RAK8212 Developer Board
- 1 pc - GPS Antenna
- 1 pc - PCB Antenna
- 1 pc - Battery Line
- 5 pcs - Dupont Line

## Product Configuration

### Checking Device Logs

You can check the logs for debugging purposes on your RAK8212 WisTrio iTracker Pro through **J-link RTT Viewer**

#### Through J-link RTT Viewer

1. If you want to check the logs of RAK8212 WisTrio iTracker Pro using this method, make sure you have connected the RAK8212 with your PC through JTAG like the following diagram below:

:::warning
You still have to connect the battery to the RAK8212 to power the board.
:::

2. Go to the Official Website of **Segger** where you can Download the [J-Flash software](https://www.segger.com/products/debug-probes/j-link/tools/j-flash/about-j-flash/). Open the program **J-Link RTT Viewer V6.60f** and choose "**USB**" for the type of connection to J-Link. After which, press **OK**.

> **Image:** J-Link RTT Viewer

3. Choose the device parameters as the following picture shows and press **OK**.

> **Image:** J-Link RTT Viewer Connection Parameters

4. **Connect** to your RAK8212 WisTrio iTracker Pro by navigating through **File** > **Connect** in the Main Menu. Alternatively, you could just press **F2** to do the same process.

> **Image:** Connecting to J-Link

5. Once connection is obtained, you should see the same log as shown in the image below:

> **Image:** Log Checking through J-Link RTT Viewer

### Configuring RAK8212 WisTrio iTracker Pro

You can configure your RAK8212 WisTrio iTracker Pro by sending AT Commands through Bluetooth.

:::tip NOTE
For the complete list of AT Commands available for configuring your RAK8212 WisTrio iTracker Pro, kindly check the <a href="https://docs.rakwireless.com/product-categories/wistrio/rak8212/at-command-manual/" target="_blank">AT Commands for iTracker Pro</a> section.
:::

#### Through BLE

1. In order to configure the RAK8212 WisTrio iTracker Pro through BLE, download and install **nRF Connect** which is developed by Nordic Semiconductor and is also available in both App Store and Google Play Store.

> **Image:** nRF Connect App in Android and IOS

2. Make sure the Bluetooth on your mobile is turned on. Open the application and you will see all BLE devices in range in the scan list:

> **Image:** nRF Master Control Panel (BLE) device connecting

3. Upon connecting, a pop-up window displays and in the third item "**Nordic UART Service**", click the arrow marked in the red box which enables you to write commands through **BLE**.

> **Image:** AT+command sending through BLE

4. Click the arrow which is marked by the red box in the picture below, you will see the following page:

> **Image:** Nordic UART Service RX Characteristics

5. You can now then send AT commands to the RAK8212 WisTrio iTracker Pro. Meanwhile, you can also see log information in RTT Viewer as discussed in [Checking Device Logs](quickstart.md#checking-device-logs) section.

- For example, if you want to check the current firmware’s version send the following command:

> **Image:** AT+command for RAK8212 Firmware Version

6. Then, you can see the version number in RTT Viewer tool:

> **Image:** RAK8212 Firmware Version in RTT Viewer Tool

### Connecting to Cellular Network

This section is a sample guide on how to connect you RAK8212 WisTrio iTracker Pro to a Cellular Network.

1. Insert a SIM Card into your RAK8212 WisTrio iTracker Pro .

2. Make sure that your RAK8212 WisTrio iTracker Pro is connected to your mobile device over BLE according to the [Configuring your RAK8212 WisTrio iTracker Pro](quickstart.md#configuring-rak8212-wistrio-itracker-pro) section.

3. Now, send `at+scan=cellular` from mobile device over BLE to RAK8212 WisTrio iTracker Pro as shown in the image below:

> **Image:** AT+command for scanning Cellular Network

4. Wait for about 20 seconds, and you should see some information similar to the image shown below in the RTT Viewer:

> **Image:** Cellular Network Scan in RTT Viewer

:::tip NOTE
There may be several Cellular operator’s network signal detected upon scanning. In this section, the cellular networks available are CHINA MOBILE and CHN-UNICOM Cellular network.
:::

## Miscellaneous

### Device Firmware Setup

An easy and quick way to have a fully functional **RAK8212 WisTrio iTracker Pro** is by using a Pre-compiled Firmware Image provided. In this section are the step by step instructions on how to install the Image into your device.

#### Burn the latest Firmware

1. If you want to get a pre-compiled firmware instead of compiling the source code by
yourself, download the [latest firmware](https://downloads.rakwireless.com/#Cellular/RAK8212/Firmware/).
2. Download and install **[J-Link tool](https://downloads.rakwireless.com/#Cellular/RAK8212/Tool/)** on your Windows PC.
3. Connect the RAK8212 WisTrio iTracker Pro with your PC through through your JTAG Emulator Kit as follows:

> **Image:** RAK8212 to Windows PC connection thru JTag Emulator Kit

4. Now, **Open** the program **J-Flash V6.41a** which you just installed and click **Start J-Flash**

> **Image:** J-Flash Start Connection

5. Click the **button** marked with the **red box** in the image below labeled **Figure 15**, then you can see the following page as shown in **Figure 16** and in the table provided.

> **Image:** J-Flash Target Device Choosing

> **Image:** J-Flash Target Device Parameter

| **Parameter** | **Value**               |
|---------------|-------------------------|
| Manufacturer  | Nordic Semiconductor    |
| Device        | nRF52832_xxAA           |
| Core          | Cortex-M4               |
| Flash Size    | 512 KB + 4 KB |
| RAM Size      | 64 KB              |

6. Click **OK** and a window pops-up, as shown in **Figure 17**.

> **Image:** J-Flash Target Device Parameter Selection Window

7. Now, connect to the RAK8212 WisTrio iTracker Pro by navigating through **Target** > **Connect** in the **Main Menu.**

> **Image:** Connecting to the RAK8212 WisTrio iTracker Pro

:::tip NOTE
If the connection is unsuccessful, please recheck the connections between the RAK8212 WisTrio iTracker Pro, JTAG, and the connecting wires.
:::

8. Open the download firmware of the RAK8212 WisTrio iTracker Pro by dragging it into the window as shown in the image below:

> **Image:** RAK8212 Firmware Opening

9. Before going into the firmware process, make sure to have the old firmware erased in the chip by navigating through **Target** > **Manual Programming** > **Erase Chip** in the **Main Menu** or by doing the process shown in **Figure 20**.

> **Image:** RAK8212 Old Firmware Data Erasing

10. After the successful erasing of the old Firmware, you can start to burn the new firmware into RAK8212 WisTrio iTracker Pro by navigating through **Target** > **Production Programming** in the **Main Menu** or by Pressing "**F7**".

11. Wait for a couple of seconds and a notification pop-ups showing a successful burning of the updated firmware as shown in the image below:

> **Image:** RAK8212 Firmware Burning Successful

#### Firmware Logs Checking

1. **Open** the program **J-Link RTT Viewer V6.41a** which you just installed and click **OK**.

2. Choose the parameters as shown in the image and in the table provided below and click **OK**.

> **Image:** Firmware Log Checking Parameters

| **Parameter** | **Value**            |
|---------------|----------------------|
| Manufacturer  | Nordic Semiconductor |
| Device        | nRF52832_xxAA        |
| Core          | Cortex-M4            |
| Flash Size    | 516 KB          |
| RAM Size      | 64 KB           |

3. Connect by navigating through **File** > **Connect** in the **Main Menu** or by pressing **F2**.

> **Image:** Firmware Log Sample

:::tip NOTE
If no logs are shown upon connecting, try resetting the RAK8212 WisTrio iTracker Pro and redo the [Firmware Logs Checking](quickstart.md#firmware-logs-checking) section.
:::

