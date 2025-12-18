---
title: RAK4630 LoRaWAN BLE Module Firmware Update | USB & BLE OTA DFU Guide
description: Update RAK4630 firmware via USB or BLE OTA DFU. Follow this guide for step-by-step instructions on secure and seamless firmware upgrades.
image: https://images.docs.rakwireless.com/wisduo/rak4630-module/rak4630-module.png
keywords: 
  - low power lora module
  - rak4630 firmware update
  - nrf52840 low power mode
  - rak4630 bootloader update
  - iot module firmware upgrade
  - bootloader update
  - nordic nrf52840 dfu
  - stm32 firmware flashing
  - secure bootloader for rak4630
  - rak4630 firmware recovery
date: 2022-07-04
sidebar_label: Device Firmware Update
slug: /product-categories/wisduo/rak4630-module/dfu/
download: true
---

# RAK4630 WisBlock LoRaWAN+BLE Module Firmware Update

There will be situations where you need to update the firmware of your RAK4630.  Additionally, there are times when you may want to reload the firmware to ensure everything is properly configured. Updating the firmware of the RAK4630 WisDuo can be done via USB connection or wirelessly using BLE via OTA DFU (Over-the-Air Device Firmware Update). These methods are discussed in this guide.

- [Firmware Update via USB](#firmware-update-via-usb)
- [Firmware Update via BLE Using OTA DFU](#firmware-update-using-ble-via-ota-dfu)

## Prerequisites

### What Do You Need?

-  [nRFutil utility program](https://github.com/NordicSemiconductor/pc-nrfutil/releases)
- nRF Connect Mobile application
   -  [iOS App Store](https://apps.apple.com/us/app/nrf-connect-for-mobile/id1054362403)
   -  [Android Play Store](https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp&hl=en&gl=US)
-  [DFU Distribution Package](https://downloads.rakwireless.com/RUI/RUI3/Image/RAK4631_latest_dfu_package.zip)
-  [Latest RAK4630 FW DFU Distribution Package](https://downloads.rakwireless.com/RUI/RUI3/Image/RAK4631_latest_dfu_package.zip)

## Firmware Update via USB

You need a direct connection to the RAK4630's USB bus before proceeding with the update. Check the minimum schematic in the [quick start guide's hardware setup section](https://docs.rakwireless.com/product-categories/wisduo/rak4630-module/quickstart/#hardware-setup). This guide covers the three most popular operating systems.

- [Windows](#windows)
- [Linux](#linux)
- [MacOS](#macos)

### Windows

1. Create a new folder in your `C:\` drive named `RAK4631-R Update`.
2. Download the  [nRFutil.exe](https://github.com/NordicSemiconductor/pc-nrfutil/releases) and the  [latest DFU Package](https://downloads.rakwireless.com/RUI/RUI3/Image/RAK4631_latest_dfu_package.zip). Once you downloaded both files, put them in the `RAK4631-R Update` folder you created as shown in Figure 1.

> **Image:** nRFutil.exe and RAK4630 Latest Firmware

3. Connect the RAK4630 via USB and check if the port is detected in Device Manager.  In this guide, it is detected as COM32. The COM port number may vary depending on the PC. If no port appears in Device Manager, try double-clicking the reset button and checking again.

> **Image:** Checking COM Port via Device Manager

4. After that, send the `AT+BOOT` command to the device via serial terminal software. Follow the [guide on using Tera Term from the RAK4631-R documentation](#how-to-check-firmware-version-using-tera-term), but instead of checking the firmware version, input `AT+BOOT`. You will see no reply as the module will restart; it will then be momentarily disconnected before re-establishing the connection to Tera Term.

:::tip NOTE
Disconnect teh device from TeraTerm/Serial Terminal software or close it to free the COM port before the firmware update.  Otherwise, errors may occur during the update.
:::

:::warning
**Recovery Mode**

If `AT+BOOT` cannot be sent to the device, you can enable DFU mode via the UART2_TX pin. Connect the UART2_TX pin to GND, then reset the device to enter DFU mode.  Proceed to the next step and upload the firmware without the `AT+BOOT` command.
:::

> **Image:** AT+BOOT to Initialize Boot Mode

5. After initiating Boot mode, execute the firmware update. Open the command prompt and navigate to the `RAK4631-R Update` folder. This folder contains the nRFutil and the latest firmware.  Input `cd C:/RAK4631-R Update/` followed by `nrfutil.exe dfu serial -pkg RAK4631_latest_dfu_package.zip -p COM32`. Ensure you have the correct `.zip` file name and `COM port number` to avoid errors.

:::tip NOTE
Change the COM port number in the command to match your PC.  In this example, it is COM32, but it may differ on your PC.
:::

> **Image:** FW Update Using nRFutil

6. Check if the firmware successfully updated using the `AT+VER=?` command. Follow the [guide on using Tera Term from the RAK4631-R documentation](#how-to-check-firmware-version-using-tera-term) to check the firmware version and confirm the device update.

> **Image:** RAK4631-R Latest Firmware Version Check

### Linux

#### Setup the Linux Environment

1. First, open a new terminal and install all necessary dependencies.

```
sudo apt-get update
sudo apt-get install net-tools git curl python xclip python3-pip
```

2. Verify that you have installed `Python 3.7` or later. Check your Python version, as shown in **Figure 6**.

> **Image:** Check Python version

3. Add `.local` folder to Linux `$PATH` variable.

```
export PATH="$HOME/.local:$PATH"
```

4. Install `nrfutil`. It is available as a package in the Python Package Index (PyPI). Execute the following command:

```
sudo apt-get update
pip3 install nrfutil --user
```

#### Setup the Device Console Port in Linux

1. Install the minicom using the following commands:

```
sudo apt-get update
sudo apt-get install minicom
```

2. To open the minicom terminal utility with the ttyACM0 interface. The correct port name can be determined using `dmesg`, as shown in the [next steps](#execute-the-firmware-update-via-usb).

Enter the following code: `minicom -D /dev/ttyACM0`

#### Execute the Firmware Update via USB

1. Download the zip file  [DFU Distribution Package](https://downloads.rakwireless.com/#RUI/V3/Image/).

When you plug the RAK4630 into a Linux computer via USB, the `dmesg` command will show the information **cdc_acm 1-1:1.0: ttyACM0: USB ACM device**

> **Image:** Checking USB CDC device using dmesg command

In this case, the RAK4630 **USB CDC** device name is `/dev/ttyACM0`.

2. Perform the steps described in the section [Setup the Device Console Port in Linux](#setup-the-device-console-port-in-linux).

3. On minicom, enter the following AT command:

```
AT+BOOT
```

4. Open the terminal and navigate to the directory containing the DFU distribution package. Then, execute the following command:

`nrfutil dfu usb-serial -pkg RAK4631_latest_dfu_package.zip -p /dev/ttyACM0`

5. To check the device's firmware version in the minicom console, enter the following AT command:

```
AT+VER=?
```

You should see then the current FW version of the module.

### MacOS

1. Download  [nrfutil](https://github.com/NordicSemiconductor/pc-nrfutil/releases/download/v6.1.3/nrfutil-mac.1). Usually, the `nrfutil-mac.1` file will go to the downloads folder. This section assumes any downloaded file goes to the downloads folder.

2. Open the terminal and navigate to the downloads directory or the location where you saved the downloaded file.  Replace `username` with your actual username;  `apple` is used as an example in this guide.

```
cd /Users/username/Downloads
```

3. Make the `nrfutil-mac.1` executable.

```
chmod +x nrfutil-mac.1
```

> **Image:** Download nrfutil for macOS

4. You also need to determine the RAK4630's port name using the command:

```
ls /dev/cu.*
```

> **Image:** Check the port

5. Download the  [RAK4630 Firmware](https://downloads.rakwireless.com/RUI/RUI3/Image/RAK4631_latest_dfu_package.zip). Usually, the `RAK4631_latest_dfu_package.zip` file will go to the downloads folder.

6. Open serial terminal software and run the command `AT+BOOT` to enable the RAK4630's bootloader mode.

```
AT+BOOT
```

7. Finally, execute the firmware update.

:::tip NOTE
- The `nrfutil-mac.1` must be in the same folder as `RAK4631_latest_dfu_package.zip`.  In this guide, this is the **Downloads** folder.
- Ensure you are connected to the correct port. The port name on your computer may differ from the one in this guide.
- The update may take some time. Do not remove the USB or close the terminal application during the upload process.
:::

```
./nrfutil-mac.1 dfu usb-serial -pkg RAK4631_latest_dfu_package.zip -p /dev/cu.usbmodemC0D048F6604F1
```

## Firmware Update Using BLE via OTA DFU

This section covers how to update your RAK4630 firmware wirelessly via BLE. First, you need to download and install the nRF Connect developed by Nordic Semiconductor. The App is available both in  [Play Store](https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp&hl=en&gl=US) and  [App Store](https://apps.apple.com/us/app/nrf-connect-for-mobile/id1054362403).

- [DFU OTA Using iOS](#dfu-ota-using-ios)
- [DFU OTA Using Android](#dfu-ota-using-android)

> **Image:** nRF Connect App available in Play Store and App Store

### DFU OTA Using iOS

#### OTA DFU Over BLE

1. Download the  [DFU package](https://downloads.rakwireless.com/RUI/RUI3/Image/RAK4631_latest_dfu_package.zip) of the RAK4630 and save it on your mobile phone.

:::tip NOTE
You can upload the Distribution packet (ZIP) file to  [iCloud Services](https://www.icloud.com/) and then download it to your smartphone.
:::

Make sure Bluetooth on your mobile device is turned on.

2. Press the reset button and wait a couple of seconds.

3. Open the nRF Connect mobile application.  You will see all BLE devices in range in the scanner list.

> **Image:** Available Bluetooth Devices

4. Look for a BLE Device named **RAK.XXXXXX** in the scanner list of the app. Connect to this device and then click on the **Client** tab. Then, choose "**Secure DFU Service**".

:::tip NOTE
By default, the BLE signal of the RAK4630 turns off automatically if no connection is established after 60 seconds. Connect to **RAK.XXXXXX** immediately after pressing the reset button.
:::

> **Image:** Secure DFU service

5.  Click the button highlighted in red, as shown in **Figure 13**.

> **Image:** Buttonless DFU

7. A **Write Value** window will pop up. Select **Bool** tab, move the switch from `False` to `True` then press the **Write** button.

> **Image:** Resetting the bootloader via Bluetooth

8. Now, the RAK4630 is in DFU mode. In the application, you will see the default status overview of the RAK4630.

> **Image:** RAK4630 default status overview after resetting

9. In the Scanner list, find a BLE device named **DfuTarg** and then click the **Connect** button.

> **Image:** RAK4630 Default Bluetooth ID after Resetting

10. After connecting, select the **DFU** tab, then click **Open Document Picker**. This will prompt you to select the distribution packet zip file of the firmware you have downloaded. Press **OK**, and it will automatically start to upgrade the firmware of your RAK4630 through DFU over BLE.

> **Image:** Distribution Packet File Type under DFU

:::tip NOTE
You can upload the distribution packet (ZIP) file to  [iCloud Services](https://www.icloud.com/) and download it to your smartphone.
:::

11. After upgrading, the module restarts, and the DFU connection disconnects. Now you can use your RAK4630 with the latest firmware.

> **Image:** DFU upgrading of RAK4630 firmware via BLE

### DFU OTA Using Android

#### OTA DFU Over BLE

1. Download the  [DFU package of the RAK4630](https://downloads.rakwireless.com/RUI/RUI3/Image/RAK4631_latest_dfu_package.zip) and save it on your mobile phone.

:::tip NOTE
You can upload the Distribution packet (ZIP) file to Google Drive and download it to your smartphone.
:::

Make sure Bluetooth on your mobile device is turned on.

2. Press the reset button and wait a couple of seconds.

3. Open the nRF Connect mobile application.  The scanner list will show all BLE devices in range.

> **Image:** Available Bluetooth Devices in the Nordic App

4. Look for a BLE Device named **RAK.XXXXXX** in the scanner list of the app. Connect to this device and then click the **Client** tab. Then, choose **Secure DFU Services**.

:::tip NOTE
By default, the BLE signal of the RAK4630 turns off automatically if no connection is established after 60 seconds. Connect to **RAK.XXXXXX** immediately after pressing the reset button.
:::

> **Image:** Secure DFU service in the Nordic App

5. Click the button highlighted in red, as shown in **Figure 21**.

> **Image:** Buttonless DFU

6. Click the arrow-up button highlighted in a red box.

7. A **Write value** window will pop up. Press the **SEND** button.

> **Image:** Resetting the Bootloader via Bluetooth

8. Now, the RAK4630 is in DFU mode.  The application will show the default status overview of the RAK4630.

> **Image:** RAK4630 default status overview after resetting

9. In the Devices list, find a BLE device named **DfuTarg** and click on the **Connect** button.

> **Image:** RAK4630 default Bluetooth ID after resetting

After connecting, click the **DFU** icon (highlighted in red in **Figure 25**).

10. Select the **distribution packet (.ZIP)** and press **OK**. This will prompt you to select the downloaded firmware's ZIP file.  The RAK4630's firmware will then automatically upgrade via DFU over BLE.

> **Image:** Distribution packet file type under DFU

:::tip NOTE
You can upload the distribution packet (ZIP) file to Google Drive and download it to your smartphone.
:::

11. After upgrading, the module restarts, and the DFU connection will be disconnected.  You can now use your RAK4630 with the latest firmware.

> **Image:** DFU upgrading of RAK4630 firmware via BLE

