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

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK7394 WisGate Developer CM4 Quick Start Guide

## Prerequisites

### Hardware

- RAK7394/RAK7394C/RAK7394P WisGate Developer CM4 Gateway
- 5&nbsp;V at least 2.5&nbsp;A Micro USB power supply
- A Windows/Mac OS/Linux Computer

### Software

- Latest Firmware

### Package Inclusion

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/1.rak7394p.png"
  width="90%"
  caption="RAK7394P package inclusion"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/2.rak7394c.png"
  width="90%"
  caption="RAK7394C package inclusion"
/>

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

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/3.access-point.png"
  width="70%"
  caption="RAKwireless access point"
/>

:::tip NOTE
**XXXX** is the last 2 bytes of your RAK7394’s Wi-Fi MAC address. Connect to this Wi-Fi SSID using the password provided below. Take note of the default IP address of the gateway provided below as this will be needed in connecting via SSH.

- **Wi-Fi Password**: rakwireless
- **Default IP Address**: 192.168.230.1
:::

#### Ethernet Port

Power up the RAK7394 and connect it to your router via an Ethernet cable. By default, the OS operates in DHCP client mode. Then, look up the IP address your gateway gets assigned from the router. It will be listed as **rakpios**. Use your favorite SSH tool to log in and get started.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/4.network.png"
  width="100%"
  caption="Gateway-assigned IP address"
/>

### Log into the Gateway

#### Windows OS

SSH (Secure Shell) is commonly used to log in to a remote machine and execute commands. Many free and reliable SSH clients are available, such as [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), [BitVise SSH Client](https://www.bitvise.com/ssh-client-download), [MobaXterm](https://mobaxterm.mobatek.net/), and others. 

1. Choose the client that best suits your needs. For this guide, however, Putty will be used.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/7.putty.png"
  width="45%"
  caption="Putty Software for SSH in Windows"
/>


2. Log in via SSH, enter the default password, and then set a new password when prompted.

The default RAKPiOS username is **rak**, and the password is **changeme**. During your first login, you will be required to change the default password for security purposes.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/8.command_win.png"
  width="100%"
  caption="First login password change"
/>

3. After changing the default password (as required), the terminal and SSH session will close automatically. Reopen the session and log in using the new password.

#### macOS

1. Open the Terminal on macOS by launching the Terminal application located in the `/Applications/Utilities/` directory. Alternatively, you can open it using Spotlight by pressing **Command + Spacebar** and typing **Terminal**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/9.mac.png"
  width="60%"
  caption="macOS terminal search"
/>

2. After opening the terminal of macOS, enter **root mode** by typing the following command:

```
sudo -i
```
3. Then, you need to run the following command:
```
ssh user@IP-Address
```
4. You will be asked to provide a password for login.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/8.command_mac.png"
  width="100%"
  caption="Login prompt"
/>

#### Linux OS

If your PC runs Linux, follow the same steps as for macOS, except for enabling root mode (step 2).

### Access to Internet
#### Connect Through Wi-Fi

1. To connect the RAK7394 to a Wi-Fi network, execute the following command:
```
sudo raspi-config
```
<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/10_config.png"
  width="100%"
  caption="Enter config mode"
/>

2. When you execute the command, you will be prompted to enter the **sudo** password. Enter the password to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/11_password.png"
  width="100%"
  caption="Enter the password"
/>

3. The Raspberry Pi configuration tool will open. Navigate to and select **System Options**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/12_config_tool.png"
  width="100%"
  caption="Raspberry Pi configuration Tool"
/>

4. Select **Wireless LAN**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/13_wireless.png"
  width="100%"
  caption="Wireless LAN"
/>

5. You will be asked to select the country in which the Pi is to be used. Select the corresponding country.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/14_wireless_country.png"
  width="100%"
  caption="Select country of operation"
/>

6. Confirm the selection.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/15_wireless_confirmation.png"
  width="100%"
  caption="Selection confirmation"
/>

7. You will be prompted to enter the SSID of the wireless network you wish to connect to. After entering the SSID, click **OK**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/16_wireless_ssid.png"
  width="100%"
  caption="Enter the SSID"
/>

8. Next, you will be prompted to enter the passphrase for your Wi-Fi. If your network does not require a passphrase, leave this box empty. Once all the settings are configured, the tool will return to the main menu. Select **Finish** to close the window.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/17_wireless_finish.png"
  width="100%"
  caption="Raspberry Pi configuration tool"
/>

9. The RAK7394 should now be connected to Wi-Fi. To verify the connection, use the **ifconfig** command. The console should display information indicating that the connection is established.

```
ifconfig
```

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/18_wireless_connected.png"
  width="100%"
  caption="RAK7394 connected to Wi-Fi"
/>

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

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/19.config_tool_pwd.png"
  width="100%"
  caption="Open the configuration tool"
/>

2. From the menu, select **System Options**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/20.config_tool.png"
  width="100%"
  caption="Configuration tool"
/>

3. Select **Password**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/21.system_options.png"
  width="100%"
  caption="System options"
/>

4. A message will appear informing you that you need to enter a new password.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/22.password.png"
  width="100%"
  caption="Password"
/>

5. After clicking **OK**, you will be prompted to enter a new password and then confirm it by entering it again.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/23.password_confirm.png"
  width="100%"
  caption="Enter and confirm the new password"
/>


6. After confirming the password, the configuration tool will display a message indicating that the password has been changed successfully.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/24.password_changed.png"
  width="100%"
  caption="Password changed"
/>

### Switch Network Interfaces

1. To manage your network interfaces, execute the following command:

```
rakpios-cli
```
<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/25.network_switch.png"
  width="100%"
  caption="Execute the command"
/>

2. You will see a menu with the available configuration options, select **Manage networks**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/26.network_configuration.png"
  width="100%"
  caption="Configuration options"
/>

3. This will display a list of available interfaces. Select the desired interface and configure it as preferred by making the necessary changes.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7394/quickstart/27.interfaces.png"
  width="100%"
  caption="Available network interfaces"
/>



<RkBottomNav/>