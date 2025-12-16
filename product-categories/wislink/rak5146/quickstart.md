---
slug: /product-categories/wislink/rak5146/quickstart/
title: RAK5146 LoRaWAN Gateway Quick Start Guide | Setup & Configuration
description: Get started with the RAK5146 LoRaWAN Concentrator. Setup firmware, configure gateway channels, mount hardware, and connect to TTN or ChirpStack network.
image: "https://images.docs.rakwireless.com/wislink/rak5146/rak5146.png"
keywords:
  - rak5146
  - rak5146 lorawan concentrator
  - rak lorawan gateway module
  - rak5146 setup
  - setup rak6156 on raspberry pi
  - rak5146 firmware setup
  - configure rak5146 with spi usb
  - mni-pcie lorawan concentrator guide
  - connect rak5146 to ttn
  - mount rak5146 to the mpcie slot
  - listen before talk feature for iot devices
  - fine timestamp for lorawan networks
  - lorawan gateway concentrator guide
  - lora concentrator gps module
  - sx126x lora transceiver
  - sx1303 baseband processor
  - zoe-m8q gps module
  - configure multichannel lorawan concentrator
tags:
  - rak5146
  - wislink
  - quickstart
sidebar_label: Quick Start Guide
date: 2021-04-11
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK5146 WisLink LoRaWAN Concentrator Quick Start Guide

## Prerequisites

The following sections list the components and tools required to get started with the development board. Some of these items are included in the package, while others must be provided separately.

### Hardware Tools

- <a href="https://store.rakwireless.com/products/wislink-concentrator-module-sx1303-rak5146-lorawan?utm_campaign=BuyFromStore&utm_medium=Document&utm_source=WisBlockRAK5146&variant=39677269409990" target="_blank">RAK5146 WisLink LPWAN Concentrator</a>
- **Raspberry Pi 3/4** (RAK5146 bundle includes a Raspberry Pi 3 or 4)
- <a href="https://store.rakwireless.com/products/rak2287-pi-hat?utm_source=RAK5146PiHAT&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAK5146 Pi HAT</a> (RAK5146 bundle includes a RAK5146 Pi HAT)
- LoRa and GPS antennas
- A 16&nbsp;GB SD card (included in the RAK5146 bundle only), a card reader, and a PC

### Software Tools

- <a href="https://www.balena.io/etcher/" target="_blank">Balena Etcher</a>: a tool for burning the firmware on the SD card
- <a href="https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html" target="_blank">PuTTY</a>: a Windows tool for SSH, required to connect to the gateway
- Latest <a href="https://downloads.rakwireless.com/LoRa/RAK5146/Firmware/RAK5146_USB_Latest_Firmware.zip" target="_blank">RAK5146 Firmware</a>

## Device Firmware Setup

For an easy and quick way of having a fully functional gateway, a Precompiled Firmware Image is provided. This section gives you step-by-step instructions on how to install the Image into your SD Card used for the gateway.

### Burn the Latest Firmware

1. Download the latest firmware of **<a href="https://downloads.rakwireless.com/LoRa/RAK5146/Firmware/RAK5146_USB_Latest_Firmware.zip" target="_blank">RAK5146</a>**, which is based on the Raspbian OS.
2. Use an image writing tool to install the firmware on the SD card. For this tutorial, **<a href="https://www.balena.io/etcher/" target="_blank">Etcher</a>**, an open-source utility for burning image files, will be used.
3. Insert your SD Card into the SD Card reader and plug it into your computer.
4. Open the balenaEtcher Software, and select the downloaded image file in the first section of the balenaEtcher.

:::tip NOTE
The SD card should be automatically detected by the Etcher software. If not, secure a proper connection.
:::

Click **Flash** and wait for a couple of minutes until it displays **Flash Complete**.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/1.png"
  width="80%"
  caption="Balena Etcher Software"
/>

## Assembly Guide

To create a functioning RAK5146 WisLink LPWAN Concentrator, put these several components together.

### Mount the Concentrator

1. Insert your **RAK5146 mPCIe card** into the mPCIe slot on the **RAK2287/RAK5146 Pi HAT**. Make sure the card fits securely into the connector and sticks out at a **45-degree angle**.
2. Gently press it down and fasten it with 2 screws. Use **Figure 2** as a reference.

If you have positioned the card correctly, the screw holes on the RAK2287 will match the ones on the RAK2287/RAK5146 Pi HAT.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/2.png"
  width="50%"
  caption="Assembly of the Concentrator and the HAT"
/>

### Antennas

The module includes with two antennas: GPS, and LoRa. Both are equipped with pigtail cables that have uFL connectors, which fit onto the corresponding ports on the RAK5146. These ports are clearly labeled. Match each antenna to its appropriate port and gently press until the connectors securely fit together.

:::warning
It is not recommended to power the device with the antennas detached, as this might damage the circuitry.
:::

### Mount the HAT

Take the RAK2287/RAK5146 Pi HAT, which now has the RAK5146 securely mounted on top, and place it over the Raspberry Pi. Both the Pi and the HAT have a **40-pin connector** that should align and fit together when pressed on top of each other.

### SD Card

Insert the SD card with the Firmware you flashed in the previous step into the SD card slot on the bottom of the Raspberry Pi.

### Boot

Power the Raspberry Pi using the Micro USB port (Pi3) or the USB Type-C port (Pi4). As this is the first time booting the OS, it may take a few minutes for everything to set up.

:::tip NOTE
It is recommended to use at least a 2.5&nbsp;A (for Raspberry Pi 3B+) or a 3&nbsp;A (for Raspberry Pi 4) power supply.
:::

### Burn the Latest Firmware

Refer to the Raspberry Pi Setup guide to check how to flash the latest Raspberry Pi OS. Set it up to work with the RAK5146 LPWAN concentrator.

## Access the Gateway

There are two ways to connect to your RAK5146 WisLink LPWAN Concentrator setup.

:::warning
Before powering the Raspberry Pi 3B+ or 4, install the LoRa and GPS antennas. Not doing so might damage the boards.
:::

### 1. Wi-Fi AP Mode

By default, the Gateway will work in Wi-Fi AP mode, which means that you should be able to find an SSID named **RAKwireless_XXXX** on the Wi-Fi network list, for example:

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/3.png"
  width="80%"
  caption="RAKWireless Access Point"
/>

:::tip NOTE
Connect to this Wi-Fi SSID using "**rakwireless**" as the default password. The default IP address of the gateway's Wi-Fi is `192.168.230.1`. Make note of this IP address, as it will be needed to connect via SSH.
:::

There is no need to configure the IP address of your PC, as it will be automatically assigned by the DHCP server.

### 2. Via the Ethernet Port on the Raspberry Pi

You can also connect your PC to the gateway using an Ethernet cable. By default, the IP address of the gateway’s Ethernet interface is `192.168.10.10`, so you need to set the IP address of your PC’s Ethernet to the same network segment, for example, `192.168.10.20`.

- To do this, in Windows, go to **Control Panel** > **Network and Internet** > **Network and Sharing Center** and click **Ethernet**.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/4.png"
  width="100%"
  caption="Network and Sharing Center"
/>

- Click **Properties**, then choose **Internet Protocol Version 4 (TCP/IPv4)**.


<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/5.png"
  width="75%"
  caption="Ethernet Properties"
/>

- By default, the PC will obtain an IP address automatically. Click the option **Use the following IP Address** and enter the IP address: `192.168.10.20` and press **OK**.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/6.png"
  width="75%"
  caption="TCP/IPv4 Properties"
/>

Now, you should be able to access your gateway from your PC successfully using the IP address `192.168.10.10`through SSH.

## Log Into the Gateway

### 1. Windows OS

Secure Shell (SSH) is typically used to log in to a remote machine and execute commands. There are a lot of free and good SSH Clients out there namely <a href="https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html" target="_blank">**Putty**</a>, <a href="https://www.bitvise.com/ssh-client-download" target="_blank">**BitVise SSH Client**</a>, <a href="https://mobaxterm.mobatek.net/" target="_blank">**MobaXterm**</a> and many more. Feel free to choose one that fits your needs, but this guide will use Putty.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/7.png"
  width="40%"
  caption="Putty Software for SSH in Windows"
/>

- If you have connected to the gateway through **Wi-Fi AP Mode**, the IP address is `192.168.230.1`.
- If you have connected to the gateway through **Ethernet**, the IP address is `192.168.10.10`.
- You will be prompted to enter the username and password. The default username and password are provided below:
  - **Username**: `pi`
  - **Password**: `raspberry`

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/8.png"
  width="60%"
  caption="Command line after login"
/>

### 2. macOS

Open the macOS Terminal. Launch the **Terminal** application, which is found in the `/Applications/Utilities/` directory. You can also launch it from Spotlight, press **Command + Spacebar**, type **Terminal**, and then return.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/9.png"
  width="80%"
  caption="Open the Terminal in macOS"
/>

Open the macOS terminal. Enter **root mode** by typing the following command: `sudo -i`.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/10.png"
  width="50%"
  caption="SSH in macOS"
/>

- If you are not in root mode, enter `ssh pi@192.168.230.1` in the terminal to log in to the gateway, the default password is "**raspberry**".
- If you connect your PC with the gateway through Ethernet Cable, enter `ssh pi@192.168.10.10`, the default password is "**raspberry**".

Now, you have successfully logged into the gateway via SSH, as shown in **Figure 11**.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/11.png"
  width="50%"
  caption="Log-in Successful Notification"
/>

### 3. Linux OS

If the OS of your PC is Linux, you should do the same as the macOS, except for the root mode.


## Product Configuration

### Configure the Gateway

1. Assuming you have successfully logged into your gateway using SSH. Enter the following command in the command line:

```sh
sudo gateway-config
```

2. Then, you will see a page similar to the one shown in **Figure 12**.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/12-new.png"
  width="50%"
  caption="Configuration options for the gateway"
/>

- **Set pi password**: Used to set or change the password of the gateway.
- **Set up RAK Gateway Channel Plan**: Used to configure the operating frequency of the gateway and the LoRaWAN Server it will connect with.
- **Restart packet-forwarder**: Used to restart the LoRa packet forwarding process.
- **Edit packet-forwarder Config**: Used to open and manually edit LoRaWAN parameters in the `global_conf.json` file.
- **Configure WIFI**: Used to configure the Wi-Fi settings for network connections.
- **Configure LAN**: Used to configure the Ethernet adapter settings.

:::tip NOTE
A unique ID, also known as the Gateway EUI, will be generated for the gateway. This ID is highlighted in red in **Figure 12** and is essential for registering the gateway with any LoRa Network Server (e.g., TTN, ChirpStack).
:::

There is also another way to get your **Gateway ID**, just enter the command below in the command line:

```sh
sudo gateway-version
```

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/13.png"
  width="50%"
  caption="Gateway ID using the command line"
/>

#### Set a New Password for the Gateway

It is a good security practice to change the default password "**raspberry**" which is the same on all Raspberry Pi devices.

1. Choose the **1 Set pi password** option referred on **Figure 14**.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/14.png"
  width="50%"
  caption="Set Pi Password"
/>

2. Press **Yes** and you will be asked to enter your new password twice then press **Enter**.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/15.png"
  width="50%"
  caption="Confirm Password Change"
/>

Once the password is successfully changed, a success message will appear.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/16.png"
  width="50%"
  caption="Successful Password Change"
/>


#### Set Up RAK Gateway Channel Plan

This menu allows you to select your LoRa frequency band and one of the two available Networks Server options.

1. Choose option **2 Setup RAK Gateway LoRa concentrator**.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/17.png"
  width="50%"
  caption="Choose Setup RAK Gateway LoRa concentrator"
/>

2. Select one of two supported LoRa servers: **TTN** or **ChirpStack**.

##### Server is TTN

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/18.png"
  width="50%"
  caption="Server Is TTN"
/>

- **The Things Network (TTN)**: If you choose TTN as the LoRa Server, you will see the following page. Visit the <a href="https://lora-alliance.org/wp-content/uploads/2021/05/RP002-1.0.3-FINAL-1.pdf" target="_blank">LoRa Alliance Regional Parameters</a> for more information on your local TTN frequency plan. This will allow you to choose the correct plan.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/19.png"
  width="50%"
  caption="Select the TTN Channel Plan"
/>

After choosing the correct frequency, the success message will appear as shown in **Figure 20**.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/20.png"
  width="50%"
  caption="Successfully Changed the Frequency"
/>

##### Server is Chirpstack


<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/21.png"
  width="50%"
  caption="Server Is Chirpstack"
/>

If you choose Chirpstack as your LoRa Server, you will see the following page with two options available:

- **ChirpStack Channel Plan Configuration**: Used to configure your Regional Frequency Band
- **ChirpStack ADR Configure**:  Used to enable/disable the Adaptive Data Rate (ADR)
functionality.

1. Select option **1** for configuring your Regional Frequency Band.


<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/23.png"
  width="50%"
  caption="Regional Frequency Band Option"
/>

2. Set the IP address of the ChirpStack that you want your gateway to connect with.


<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/24.png"
  width="35%"
  caption="Default LoRaServer IP address"
/>

:::tip NOTE
The default IP address is `127.0.0.1`. If you want to use an independent LoRa Server running on another device or a cloud-based LoRa Server, set it to the corresponding IP address.
:::

### Connect to a Network

If you want to use TTN or an independent ChirpStack network server, which may be deployed in a local area network or remotely, connect your gateway to a networking device that provides internet connectivity, such as a router. There are two options available for this purpose.

#### Connect Through Wi-Fi

If you want to connect through Wi-Fi, you can easily do so using the wireless capabilities of the Raspberry Pi 3B+ or Raspberry Pi 4 by selecting **5 Configure WIFI**. By default, the RAK5146 WisLink LPWAN Concentrator operates in Wi-Fi AP Mode.

1. To connect the gateway to a router, it must be set to Wi-Fi Client Mode.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/25.png"
  width="50%"
  caption="Configuration options for WIFI"
/>

There are 5 options to choose from in the Wi-Fi configuration menu:

- **Enable AP Mode/Disable Client Mode**: After rebooting, the gateway will operate in Wi-Fi Access Point Mode while the Wi-Fi Client Mode will be disabled (this is the default mode).
- **Enable Client Mode/Disable AP Mode**: After rebooting, the gateway will operate in Wi-Fi Client Mode, and Wi-Fi AP Mode will be disabled.
- **Modify SSID and pwd for AP Mode**: This option is used to modify the SSID and password of the Wi-Fi AP. It only works if the Wi-Fi AP Mode is enabled.
- **Add New SSID for Client**: This is used if you want to connect to a new Wi-Fi network. It only works in Wi-Fi Client Mode.
- **Change Wi-Fi Country**: This is used to modify the resident country to match the Wi-Fi standards.

:::warning
To enable Wi-Fi Client Mode, you must first disable the AP Mode.
:::

2. Once Wi-Fi AP Mode has been disabled by choosing "**2 Enable Client Mode/Disable AP Mode**", connect to a new Wi-Fi Network by choosing "**4 Add New SSID for Client**".

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/26.png"
  width="50%"
  caption="Add a new SSID"
/>

3. Select your country of residence:

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/27.png"
  width="50%"
  caption="Select a Country of Residence"
/>

4. Enter the SSID of the network you want to connect to.

:::warning
Make sure to input the correct Wi-Fi SSID and password. Otherwise, you will not be able to reconnect to the RAK5146 WisLink LPWAN Concentrator via SSH when it is in Wi-Fi AP Mode. If you find yourself in this situation, follow the procedure outlined in the <a href="https://docs.rakwireless.com/product-categories/wislink/rak5146/quickstart/#revert-to-wi-fi-ap-mode/">Connecting to a Network</a> document, which is applicable for all Raspberry Pi-based gateways to restore Wi-Fi AP mode functionality.
:::

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/28.png"
  width="50%"
  caption="SSID of the Network you want to connect to."
/>


5. Enter the password as well. Leave it empty if there is none.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/29.png"
  width="50%"
  caption="Password of the Wi-Fi"
/>

#### Connect Through Ethernet

To connect to the router using an Ethernet cable, follow these steps:

1. In the main configuration menu, choose **6 Configure LAN**. This allows you to set up a static IP address for the Gateway’s Ethernet adapter.
2. Enter a static IP address that corresponds to your router's IP address range. Make sure that the LoRaWAN gateway and the router are in the same network segment. Otherwise, the connection will fail.
3. By default, the IP address of the gateway's Ethernet is `192.168.10.10`.


<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/30.png"
  width="35%"
  caption="Default gateway Ethernet IP address"
/>

4. Configure the IP address of the router. This will be the LAN interface IP address of the router.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/31.png"
  width="35%"
  caption="LAN Interface IP address of the Router"
/>

5. Press **OK** and a success message will appear.
6. Finally, reboot the gateway using the command `sudo reboot` in the command line and it will connect to the router successfully through Ethernet.

#### Optional Configurations

The configurations in this section are optional and situational.

##### Revert to Wi-Fi AP Mode

If you have entered incorrect Wi-Fi SSID and/or password during the Wi-Fi Client Mode setup for the RAK5146 WisLink LPWAN Concentrator, follow these steps to revert to Wi-Fi AP Mode and redo the setup:

1. Remove the SD Card from your RAK5146 WisLink LPWAN Concentrator and insert it into your PC. Your PC should be able to detect as shown in **Figure 32**.

<RkImage
  zoomMode={true}
  src="https://images.docs.rakwireless.com/wislink/rak5146/quickstart/32.png"
  width="30%"
  caption="Create rak_ap file to your SD Card"
/>

2. Using your **Command Prompt** or **Terminal**, navigate to your SD Card and type the command `rak_ap` to generate a file.

```
cd > rak_ap
```

3. Check if the `rak_ap` file is created successfully. If so, re-insert the SD Card into your RAK5146 WisLink LPWAN Concentrator and it should work again in Wi-Fi AP Mode.

<RkBottomNav/>