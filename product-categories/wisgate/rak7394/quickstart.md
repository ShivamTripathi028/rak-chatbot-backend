---
title: RAK7394 WisGate Developer CM4 Quickstart
description: Contains instructions and tutorials for installing and deploying your RAK7394. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device.
image: https://images.docs.rakwireless.com/wisgate/rak7394/rak7394.png
keywords:
    - RAK7394
    - RAK7394P
    - RAK7394C
    - wisgate
    - quickstart
sidebar_label: Quick Start Guide 
---

# RAK7394 WisGate Developer CM4 Quick Start Guide

## Prerequisites

### Hardware

- RAK7394/RAK7394C/RAK7394P WisGate Developer CM4 Gateway
- 5 V at least 2.5 A Micro USB power supply
- A Windows/Mac OS/Linux Computer

### Software

- Latest Firmware

### Package Inclusion

> **Image:** RAK7394P package inclusion

> **Image:** RAK7394C package inclusion

## Product Configuration

### Power the Gateway

:::warning
Before powering the device, ensure that the LoRa, LTE (for the Cellular variant only), and GPS antennas are connected. Failing to attach the antennas may damage the boards. Once the antennas are securely connected, the gateway can be powered on safely.
:::

Power the gateway using the provided power adapter by inserting it into the USB-C Power Supply slot. If you are unsure which one of the two USB-C slots is for powering the gateway and which one is for booting, consult the [Interfaces](https://docs.rakwireless.com/product-categories/wisgate/rak7394/datasheet/#hardware) section of the gateway's datasheet

:::tip NOTE
The RAK7394P WisGate Developer CM4 Gateway supports Power-over-Ethernet (PoE). You can use a PoE injector to power the gateway via an Ethernet cable.
:::

### Access the Gateway

This section outlines several methods for accessing the gateway, offering different alternatives based on the availability of the required resources.

#### Wi-Fi AP Mode

By default, when you power on RAK7394 and no other connection is established with the device (eg. Ethernet connection) the gateway will work in Wi-Fi AP mode, which means you can find an SSID named RAK_XXXX on your PC Wi-Fi Network List.

> **Image:** RAKwireless access point

:::tip NOTE
**XXXX** is the last 2 bytes of your RAK7394’s Wi-Fi MAC address. Connect to this Wi-Fi SSID using the password provided below. Take note of the default IP address of the gateway provided below as this will be needed in connecting via SSH.

- **Wi-Fi Password**: rakwireless
- **Default IP Address**: 192.168.230.1
:::

#### Ethernet Port

Power up the RAK7394 and connect it to your router via an Ethernet cable. By default, the OS operates in DHCP client mode. Then, look up the IP address your gateway gets assigned from the router. It will be listed as **rakpios**. Use your favorite SSH tool to log in and get started.

> **Image:** Gateway-assigned IP address

### Log into the Gateway

#### Windows OS

SSH (Secure Shell) is commonly used to log in to a remote machine and execute commands. Many free and reliable SSH clients are available, such as [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), [BitVise SSH Client](https://www.bitvise.com/ssh-client-download), [MobaXterm](https://mobaxterm.mobatek.net/), and others. 

1. Choose the client that best suits your needs. For this guide, however, Putty will be used.

> **Image:** Putty Software for SSH in Windows

2. Log in via SSH, enter the default password, and then set a new password when prompted.

The default RAKPiOS username is **rak**, and the password is **changeme**. During your first login, you will be required to change the default password for security purposes.

> **Image:** First login password change

3. After changing the default password (as required), the terminal and SSH session will close automatically. Reopen the session and log in using the new password.

#### macOS

1. Open the Terminal on macOS by launching the Terminal application located in the `/Applications/Utilities/` directory. Alternatively, you can open it using Spotlight by pressing **Command + Spacebar** and typing **Terminal**.

> **Image:** macOS terminal search

2. After opening the terminal of macOS, enter **root mode** by typing the following command:

```
sudo -i
```
3. Then, you need to run the following command:
```
ssh user@IP-Address
```
4. You will be asked to provide a password for login.

> **Image:** Login prompt

#### Linux OS

If your PC runs Linux, follow the same steps as for macOS, except for enabling root mode (step 2).

### Access to Internet
#### Connect Through Wi-Fi

1. To connect the RAK7394 to a Wi-Fi network, execute the following command:
```
sudo raspi-config
```

> **Image:** Enter config mode

2. When you execute the command, you will be prompted to enter the **sudo** password. Enter the password to proceed.

> **Image:** Enter the password

3. The Raspberry Pi configuration tool will open. Navigate to and select **System Options**.

> **Image:** Raspberry Pi configuration Tool

4. Select **Wireless LAN**.

> **Image:** Wireless LAN

5. You will be asked to select the country in which the Pi is to be used. Select the corresponding country.

> **Image:** Select country of operation

6. Confirm the selection.

> **Image:** Selection confirmation

7. You will be prompted to enter the SSID of the wireless network you wish to connect to. After entering the SSID, click **OK**.

> **Image:** Enter the SSID

8. Next, you will be prompted to enter the passphrase for your Wi-Fi. If your network does not require a passphrase, leave this box empty. Once all the settings are configured, the tool will return to the main menu. Select **Finish** to close the window.

> **Image:** Raspberry Pi configuration tool

9. The RAK7394 should now be connected to Wi-Fi. To verify the connection, use the **ifconfig** command. The console should display information indicating that the connection is established.

```
ifconfig
```

> **Image:** RAK7394 connected to Wi-Fi

#### Connect Through Ethernet

If you are accessing the gateway through the RAKR314 Carrier Board Ethernet Port, you are automatically connected to the internet via the Ethernet connection.

### Reboot

Lastly, reboot the gateway using the command shown below and put it in the command line.
```
sudo reboot
```
## Optional Configuration
### Reflashing Procedure

To reflash the RAK7394, you need to disassemble the enclosure to access the RAK314 inside.

When you have access to the RAK314, you need to follow this [guide.](https://docs.rakwireless.com/product-categories/wisgate/rakr314/flashing-the-os/)

### Change the Password

1. To change the password, use the following command to open the configuration tool:
```
sudo raspi-config
```

> **Image:** Open the configuration tool

2. From the menu, select **System Options**.

> **Image:** Configuration tool

3. Select **Password**.

> **Image:** System options

4. A message will appear informing you that you need to enter a new password.

> **Image:** Password

5. After clicking **OK**, you will be prompted to enter a new password and then confirm it by entering it again.

> **Image:** Enter and confirm the new password

6. After confirming the password, the configuration tool will display a message indicating that the password has been changed successfully.

> **Image:** Password changed

### Switch Network Interfaces

1. To manage your network interfaces, execute the following command:

```
rakpios-cli
```

> **Image:** Execute the command

2. You will see a menu with the available configuration options, select **Manage networks**.

> **Image:** Configuration options

3. This will display a list of available interfaces. Select the desired interface and configure it as preferred by making the necessary changes.

> **Image:** Available network interfaces

