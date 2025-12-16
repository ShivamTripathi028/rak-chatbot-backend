---
slug: /product-categories/wisgate/rak10701-plus/firmware-update/
title: RAK10701-Plus Field Tester for LoRaWAN Firmware Update
description: Keep your Field Tester Plus firmware updated for an optimal performance! Use USB or Bluetooth to access new features and performance improvements.
image: https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/physical-interface.png
keywords:
    - lorawan
    - field tester plus
    - rak10701-plus
    - update field tester plus firmware
    - network coverage solution device
sidebar_label: Firmware Update
tags:
  - rak10701-plus
  - field tester plus
  - network coverage solution
  - firmware update
date: 2025-05-23
---

import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkImage from '@site/src/components/Image'

# RAK10701-Plus Field Tester for LoRaWAN Firmware Update

This guide explains how to upgrade the firmware of the Field Tester Plus using either a USB connection or Bluetooth. Keeping the firmware up to date ensures stable performance, compatibility with tools, and access to the latest features.

## Upgrade the Firmware of the Field Tester Plus

There are two available methods to upgrade the firmware of the Field Tester Plus:
- **USB Upgrade via PC**:
Use a USB Type-C cable to connect the Field Tester Plus to a computer and perform the firmware upgrade through the WisToolBox Desktop App.
- **BLE Upgrade via Smartphone:**
Use Bluetooth Low Energy (BLE) to wirelessly upgrade the device via the **WisToolBox Mobile App** on Android or iOS.
Both methods produce the same result. Choose the one that best suits your available tools and environment.

### Prerequisites

**Hardware Requirements:**
- **RAK10701-Plus device**
- **USB Type-C connection cable** (for serial upgrade via PC)
- **PC (Windows/macOS)** for USB upgrade
- **Smartphone (Android/iOS)** for BLE (Bluetooth) upgrade
**Software Requirements:**
- <a href="https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/wistoolbox-desktop/" target="_blank">WisToolBox Desktop App</a> (for PC, via USB connection)
- <a href="https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/wistoolbox-mobile/" target="_blank">WisToolBox Mobile App</a> (for smartphone, via BLE connection)

### USB (Serial) Upgrade via PC

1. Connect the **RAK10701-Plus** to the PC using a **USB Type-C cable**.
2. Open the **WisToolBox Desktop App**.
3. Click **START** to begin scanning.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/wistoolbox-connection-rak10701.png"
  width="100%"
  caption="WisToolBox USB Connection To RAK10701"
/>

4. Once the device is detected as **RAK10701-Plus**, click **CONNECT**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/wistoolbox-connection-settings.png"
  width="100%"
  caption="WisToolBox Connection Settings"
/>

5. In the connected device list, select **Field Tester Plus** to view device details.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/field-tester-device-details.png"
  width="100%"
  caption="Field Tester Device Details"
/>

6. Go to the **FIRMWARE** tab.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/wistoolbox-device-firmware-tab.png"
  width="100%"
  caption="WisToolBox Device Firmware Tab"
/>

7. Select the firmware version you want to upgrade to, then click **UPGRADE DEVICE**.
8. Confirm the correct COM port is selected, and click **UPGRADE** to start.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/update-firmware-rak10701-plus.png"
  width="100%"
  caption="Update Firmware RAK10701-Plus"
/>

9. Wait until the process shows **Successfully Updated**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/update-firmware-process.png"
  width="100%"
  caption="Update Fimware Loading Screen"
/>
<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/firmware-update-succesfull.png"
  width="100%"
  caption="Firmware Update Successfull"
/>

10. After upgrade, the device will reboot automatically. Verify the new firmware version under **Settings**.

### BLE (Bluetooth) Upgrade via Smartphone

1. Open the **WisToolBox Mobile App** on your Android/iOS device.
2. Tap **START** on the home screen.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/mobile-wistoolbox-device-tab.png"
  width="40%"
  caption="Mobile WisToolBox Device Tab"
/>

3. Select **BLE Pairing**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/mobile-wistoolbox-connection-mode.png"
  width="40%"
  caption="Mobile WisToolBox Connection Mode"
/>

4. Follow the pairing instructions and then click **CONNECT**.
    - Keep Bluetooth enabled on your phone.
    - Keep the Field Tester Plus powered on.
    - Keep the phone and device close together.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/mobile-wistoolbox-ble-pairing.png"
  width="40%"
  caption="Mobile WisToolBox BLE Pairing"
/>

5. Once you have located your `RAK10701.######`, tap the green link button.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/mobile-wistoolbox-searching-devices.png"
  width="40%"
  caption="Mobile WisToolBox Searching Devices"
/>

6. After pairing, wait for **Data Synchronization** to complete.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/mobile-wistoolbox-data-synchronization.png"
  width="40%"
  caption="Mobile WisToolBox Data Synchronization"
/>

7. Enter the **DEVICE INFO** page and scroll down to **Device firmware**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/mobile-wistoolbox-device-information.png"
  width="40%"
  caption="Mobile WisToolBox Device Information"
/>

8. Review the available firmware versions and corresponding release notes.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/mobile-wistoolbox-firmware-updates-available.png"
  width="40%"
  caption="Mobile WisToolBox Firmware Updates Available"
/>

9. Tap **UPGRADE DEVICE** to begin the firmware update.
10. Confirm all upgrade settings are correct, then click **Upgrade Firmware** to start the upgrade process.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/mobile-wistoolbox-update-firmware-device.png"
  width="40%"
  caption="Mobile WisToolBox Update Firmware Device"
/>

11. Wait until the process shows **Successfully Updated**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/mobile-wistoolbox-updating-loading-screen.png"
  width="40%"
  caption="Mobile WisToolBox Updating Loading Screen"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/mobile-wistoolbox-updating-successfull.png"
  width="40%"
  caption="Mobile WisToolBox Updating Successfull"
/>

12. After the upgrade, the device will reboot automatically. Verify the new firmware version under **DEVICE INFO**.

## Upgrade RAK10701-L/P to RAK10701-Plus

The RAK10701-L, RAK10701-P, and RAK10701-Plus share identical hardware. You can upgrade a RAK10701-L or RAK10701-P to the Field Tester Plus version by uploading the corresponding firmware via the custom firmware upgrade process.

:::tip Compatibility Reminder
After upgrading, you cannot downgrade the device back to the RAK10701-L or RAK10701-P firmware.
:::

### Prerequisites
**Hardware Requirements**:
- **RAK10701-L/RAK10701-P device**
- **USB Type-C connection cable**
- **PC (Windows/macOS)/Laptop**
**Software Requirements**:
- <a href="https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/wistoolbox-desktop/" target="_blank">WisToolBox Desktop App</a>
- <a href="https://downloads.rakwireless.com/#LoRa/RAK10701-Plus/Firmware/" target="_blank">RAK10701-Plus firmware</a>

### Upgrade Procedure
1. Connect your RAK10701-L or RAK10701-P to your PC/Laptop via a USB Type-C cable.
2. Open the **WisToolBox Desktop App**.
3. Click **START** to begin scanning.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/wistoolbox-dashboard.png"
  width="100%"
  caption="WisToolBox DashBoard "
/>

4. WisToolBox will search for connected devices.
If it shows **No device detected**, reconnect the RAK10701 and click **TRY AGAIN**.

:::tip NOTE
Ensure the device is recognized as a COM port.
If detection fails, use a different USB cable, another USB port, or a different PC.
If the device has been stored for a long time, charge it before attempting the upgrade.
:::

5. Once detected, the **Connection settings** page will appear, showing the correct device name (RAK10701-L or RAK10701-P). Click **CONNECT** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/wistoolbox-connection-settings-tab.png"
  width="100%"
  caption="WisToolBox Connection Settings Tab"
/>

6. Once connected, the device will be shown as **WisNode Field Tester**. Click on **FIRMWARE** to open the firmware update section.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/wistoolbox-field-test-device-info.png"
  width="100%"
  caption="WisToolBox Field Test Device Information"
/>

7. On the firmware settings, click **Custom**. You can drag-and-drop the RAK10701-Plus firmware in this section.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/wistoolbox-field-test-upgrade-device.png"
  width="100%"
  caption="WisToolBox Field Test Upgrade Device"
/>

8. After selecting the downloaded firmware, click **UPGRADE DEVICE**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/wistoolbox-select-firmware-to-upgrade.png"
  width="100%"
  caption="WisToolBox Select Firmware to Upgrade"
/>

9. Confirm the correct COM port is selected, and click **UPGRADE** to start.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/wistoolbox-upgrade-firmware.png"
  width="100%"
  caption="WisToolBox Upgrade Firmware"
/>

10. Wait until the process shows **Successfully Updated**.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/firmware-update/wistoolbox-upgrade-firmware-successfull.png"
  width="100%"
  caption="WisToolBox Upgrade Firmware Successfull"
/>

11. Once the firmware is uploaded, the device will be recognized as RAK10701-Plus. You can then use WisToolBox to send AT commands via the console.

:::tip NOTE
WisToolBox v1.4.5 provides limited support for RAK10701-Plus.
:::

<RkBottomNav/>