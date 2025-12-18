---
slug: /product-categories/software-apis-and-libraries/wisgateos2/settings/
title: WisGateOS 2 User Manual | Complete Guide for LoRaWAN Gateway Software
description: Configure WisGateOS 2 for LoRaWAN gateways with Basics Station, MultiWAN, MQTT, and HTTP integrations. Secure connections with OpenVPN & WireGuard.
image: "https://images.docs.rakwireless.com/product-logos/wisgateos2.png"
keywords:
  - system settings configuration
  - encrypted backup setup
  - remote log server setup
  - log rotation settings
  - gateway reset to defaults
  - time settings 
  - change gateway password
  - language settings gateway
  - user preferences
tags:
  - system settings
  - backup & restore
  - remote log server
  - log rotation
  - time settings
  - change password
  - language settings
sidebar_label: System Settings
date: 2022-08-01
---



import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# System Settings

In the **Settings** section, you can manage and configure various settings of the gateway, including changing its name, setting up system logs, synchronizing time, managing backups and restores, accessing files, and customizing user preferences.

## General Settings

The **General Settings** tab provides options to modify the gateway's name, configure system logs, synchronize time via an NTP server, and reboot the device.

### Change the Gateway Name

The default gateway name can be updated to improve identification within a network.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/settings/change-name.png"
  width="80%"
  caption="Changing the gateway name"
/>

1. Navigate to **Settings** > **General settings**.
2. Enter the desired name in the **Name** field.
3. Click **Save** to apply the change.

### Configure the System Log

The **System Log** settings allow management of log storage and forwarding logs to an external server for **monitoring, troubleshooting, and long-term analysis**.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/settings/setup-syslog.png"
  width="80%"
  caption="Configure the System Log"
/>

1. Navigate to **Settings** > **General settings**.
2. **Set Log Buffer Size:** Enter the maximum log buffer size (

  in KiB) in the **Buffer size (KiB)** field (e.g., 64 KiB).
3. **Choose Log Retention Period:** Select a duration from the **Log expiration** dropdown:
   - 14 days
   - 1 month
   - 3 months
   - 6 months
   - 12 months
4. **Configure External Log Storage (Optional):**
   + Enter the **External system log server IP address** if remote log storage is required.
   + Specify the **Port number** used by the external log server.
5. Click **Save** to apply changes.

### Time Synchronization

The gateway supports **Network Time Protocol (NTP)** to maintain accurate system time.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/settings/time-sync.png"
  width="80%"
  caption="Time synchronization"
/>

1. Navigate to **Settings** > **General settings**.
2. Toggle **Enable NTP client** to activate time synchronization.
3. Configure NTP servers in the **NTP server candidates** list:
   - Click **Add new server candidate** to add an NTP server (e.g., `pool.ntp.org`).
   - To remove an NTP server, click the **×** button next to it.
4. Click **Save** to apply the settings.

### Reboot the Gateway

This option restarts the gateway. **All unsaved changes will be lost** during the reboot.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/settings/reboot-gateway.png"
  width="80%"
  caption="Reboot the Gateway"
/>

1. Navigate to **Settings** > **General settings**.
2. Click the **Reboot** button.
3. In the confirmation dialog, click **Confirm** to restart the gateway.

## Backup and Restore

This tab enables **backup**, **restore**, or **reset** of the gateway settings to ensure configuration management and recovery.

### Backup Configuration

Creating a **backup of the current gateway configuration** allows restoration when necessary. For added security, the backup file can be **encrypted with a password**.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/settings/backup.png"
  width="100%"
  caption="Backup configuration"
/>

1. Navigate to **Settings** > **Backup and Restore**.
2. (Optional) **Enable Backup Encryption:**
   + Check the **Set password to protect the backup archive** box.
   + Enter a secure password to encrypt the backup file.
3. Click **Generate and download backup** to create and download the backup archive.
4. Store the backup file in a secure location for future use.

### Restore Configuration

Restoring a backup reverts the gateway settings to the state saved in the selected archive.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/settings/restore.png"
  width="100%"
  caption="Restore configuration"
/>

:::warning IMPORTANT
Restoring a backup will overwrite the current settings. Make sure the correct file is used.
:::

1. Navigate to **Settings** > **Backup and Restore**.
2. Click **choose file** or drag and drop the backup archive into the designated upload area.
3. After the file is loaded, click the **Restore** button.
4. When prompted for a password:
   - **Encrypted backup**: Enter the correct password, then click **Restore** again.
   - **Plain backup**: A password dialog still appears, but no password is required. Simply click **Restore** again.
5. Wait for the process to complete. The gateway will automatically reboot.
    :::warning
    Do not power off the device during this time.
    :::

### Reset to Factory Defaults

Resets the gateway to its original factory settings, permanently erasing all configurations.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/settings/reset.png"
  width="100%"
  caption="Reset to factory defaults"
/>

:::warning IMPORTANT
This action is **irreversible**. Ensure you have a backup before proceeding.
:::

1. Navigate to **Settings** > **Backup and Restore**.
2. Click the **Reset** button.
3. In the confirmation dialog, click **Reset** to reset the gateway.
4. Wait for the gateway to reboot with factory default settings.

## File Browser

The **File Browser** allows you to access the gateway’s file system directly through the Web UI, making it easy to view or download files. It provides access to system log files, firmware images, configuration data, and other stored resources.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/settings/settings-file-browser.png"
  width="100%"
  caption="File browser tab"
/>

1. Navigate to **Settings** > **File Browser** > **mnt** > **mmcblk0p1**.
2. Select the target folder, enter it, then click and download the file.

## User Preferences

The **User Preferences** section allows customization of personal settings, including **password management, timezone, and language selection**.

### Access User Preferences

To modify your preferences, navigate to the **User Preferences** option in the bottom-left corner of the interface.

1. In the bottom-left corner, choose **User preferences** to set your personal preferences for the gateway.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/user-preferences/user-button.png"
  width="40%"
  caption="User button"
/>

2. Selecting this option will redirect you to the **User Preferences** page.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/user-preferences/user-preferences.png"
  width="80%"
  caption="User preferences"
/>

### Available Settings

- **Change Password**: Update your Web UI access password to meet the security requirements.
- **Time Settings**: Configure the gateway's local time and synchronize it with your browser if needed.
- **Language**: Select the system language for the Web UI.

### Log Out

To log out of the Web UI, click **Logout** in the bottom-left corner.

<RkBottomNav/>