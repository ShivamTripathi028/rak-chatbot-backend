---
title: RAK7248 Quick Start | LoRaWAN & LTE Gateway Setup & Configuration
description: Get started with the RAK7248 WisGate Developer D4H! This guide walks you through setup, LoRaWAN configuration, and network integration.
image: https://images.docs.rakwireless.com/wisgate/rak7248/rak7248.png
keywords: 
  - raspberry pi 4 lora gateway
  - lorawan gateway raspberry pi
  - rak7248 setup
  - lte cellular gateway
  - open-source lorawan gateway
  - semtech sx1302 lora concentrator
  - secure lorawan gateway access point
  - lorawan gateway internet access points setup
  - connect rak7248 to ttn
  - configure gateway in ethernet port
date: 2020-09-25
sidebar_label: Quick Start Guide
---

    

# RAK7248 Quick Start Guide

## Prerequisites

### What Do You Need?

1. [RAK7248/RAK7248C/RAK7248P WisGate Developer D4H Gateway](https://store.rakwireless.com/products/rak7248?utm_source=RAK7248WisGateDeveloperD4H&utm_medium=Document&utm_campaign=BuyFromStore)
2. 16 GB SD Card + Card Reader
3. 5 V at least 2.5 A Micro USB Power Supply
4. A Windows/Mac OS/Linux Computer
5. Latest [RAK7248 Firmware](https://docs.rakwireless.com/product-categories/wisgate/rak7248/datasheet/#software)

### What's Included in the Package?

> **Image:** RAK7248/P WisGate Developer D4H Gateway package contents

> **Image:** RAK7248C WisGate Developer D4H Gateway package contents

## Product Configuration

After burning the firmware image onto the SD Card, make sure you have inserted the SD Card into the **RAK7248 WisGate Developer D4H Gateway** and have the LoRa, and GPS Antenna connected. Refer to the guide on [how to burn the image](https://learn.rakwireless.com/hc/en-us/articles/26744073850775-How-To-Set-Up-WisGate-Developer-Gateway-Firmware).

:::warning
Before powering the Raspberry Pi 4, you should connect the LoRa, LTE (only in the Cellular variant), and the GPS antennas. Not doing so might damage the boards.

After the antennas are attached and the SD card is inserted into the Raspberry Pi, you can safely power on the gateway.
:::

### Wi-Fi AP Mode

By default, the gateway will work in Wi-Fi AP Mode, which means you can find an SSID named **Rakwireless_XXXX** on your PC Wi-Fi Network List.

> **Image:** RAKwireless access point

:::tip NOTE

**XXXX** is the last 2 bytes of your RAK7248’s WiFi MAC address. Connect to this Wi-Fi SSID using the password provided below. Take note of the default IP address of the gateway provided below as this will be needed in connecting via SSH. By default, the gateway will work in Wi-Fi AP Mode, which means you can find an SSID named **Rakwireless_XXXX** on your PC Wi-Fi Network List.

- **Wi-Fi Password**: rakwireless
- **Default IP Address**: 192.168.230.1
:::

### Raspberry Pi 4 Ethernet Port

You can also connect your PC with the gateway through an Ethernet cable. By default, the IP address of the gateway’s Ethernet interface is `192.168.10.10`, so you need to set the IP address of your PC’s Ethernet to the same network segment, for example, `192.168.10.20`.

1. To do this on a Windows PC, go to **Control Panel -> Network and Internet -> Network and Sharing Center** and click **Ethernet**.

> **Image:** Network and sharing center

2. Click **Properties**, then slect **Internet Protocol Version 4 (TCP/IPv4)**.

> **Image:** Ethernet properties

3. By default, the PC will obtain an IP Address automatically. Click **Option Use the following IP Address** and enter the IP address `192.168.10.20` then press **OK**.

> **Image:** TCP/IPv4 Properties

Now, you should be able to access your gateway from your PC successfully using the IP Address `192.168.10.10` through SSH.

### Log into the Gateway

#### Windows OS

SSH (Secure Shell) is typically used to log in to a remote machine and execute commands. There are a lot of free and good SSH Clients out there, namely [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), [BitVise SSH Client](https://www.bitvise.com/ssh-client-download), [MobaXterm](https://mobaxterm.mobatek.net/) and many more. Feel free to choose one that fits your needs, but for this guide, you will be using Putty

> **Image:** Putty Software for SSH in Windows

- If you have connected to the gateway through Wi-Fi AP Mode, the IP Address is `192.168.230.1`
- If you have connected to the gateway through Ethernet, the IP Address is `192.168.10.10`
- It will then prompt you to enter the username and password. The default username and password are:

  - **Username**: pi
  - **Password**: raspberry

> **Image:** Command line after log in

#### Mac OS

Open the Terminal of Mac OS. Launch the **Terminal** application found in "the /Applications/Utilities/" directory. You can also launch it from Spotlight by hitting **Command + Spacebar** and typing **Terminal**, and then return:

> **Image:** Opening terminal in Mac OS

Open the terminal of Mac OS. Enter root mode by typing the following command:

```
sudo -i
```

#### Linux OS

If the OS of your PC is Linux, you should do the same as the Mac OS, except the root mode.

### Accessing the Internet

Assuming you have successfully logged into your gateway using SSH. Enter the following command in the command line:

```
sudo gateway-config
```

You will then see a page like the following picture:

> **Image:** Configuration options for the gateway

1. **Set pi password**- used to set/change the password of the gateway.
2. **Set RAK Gateway Channel Plan** - used to configure the frequency, which the gateway will operate on, and the LoRaWAN Server which the gateway will work with.
3. **Restart packet-forwarder** - used to restart the LoRa packet forwarder.
4. **Edit packet-forwarder config** - used to open the global_conf.json file, to edit LoRaWAN parameters manually.
5. **Configure WIFI** - used to configure the Wi-Fi settings in order to connect to a network.
6. **Configure LAN** - used to configure the Ethernet adapter settings.****

#### Connect through Wi-Fi

If you want to connect through Wi-Fi, it can easily be done with the Wireless capabilities of the Raspberry Pi 4 by choosing **5 Configure WIFI**. By default, the RAK7248 WisGate Developer D4H Gateway works in Wi-Fi AP Mode.

For the gateway to connect to the router, it must work in Wi-Fi Client Mode.

> **Image:** Configuration options for Wi-Fi

There are 5 options to choose from in the Wi-Fi configuration menu:

1. **Enable AP Mode/Disable Client Mode** - the gateway will work in Wi-Fi Access Point Mode after rebooting while the Wi-Fi Client Mode will be disabled (this is the default mode).
2. **Enable Client Mode/Disable AP Mode** - the gateway will work in Wi-Fi Client mode after rebooting, while Wi-Fi AP Mode will be disabled.
3. **Modify SSID and pwd for AP Mode** - used to modify the SSID and password of the Wi-Fi AP. Only works if the Wi-Fi AP Mode is enabled.
4. **Add New SSID for Client** - this is used if you want to connect to a new Wi-Fi Network. Only works in Wi-Fi Client mode.
5. **Change Wi-Fi Country** - this is used to modify the Resident Country to match Wi-Fi standards.

:::warning

To enable Wi-Fi Client Mode, you have to disable AP Mode first.
:::

Once Wi-Fi AP Mode has been disabled by choosing **2 Enable Client Mode/Disable AP Mode**, you can now then connect to a new Wi-Fi Network by choosing **4 Add New SSID for Client**.

> **Image:** Add a new SSID

- Start by selecting your country of residence:

> **Image:** Selecting country of residence

- Enter the SSID of the network you want to connect:

:::warning
Make sure to input the correct Wi-Fi SSID and Password, or you will not be able to connect to the RAK7248 again via SSH in Wi-Fi AP Mode. If stuck in this situation, follow the procedure listed in the [Reverting to Wi-Fi AP Mode](https://docs.rakwireless.com/product-categories/wisgate/rak7248/lorawan-network-server-guide/#connecting-with-chirpstack) section, which is applicable for all Raspberry Pi-based gateways to work again in Wi-Fi AP mode.
:::

> **Image:** SSID of the Network you want to connect to

- Type the password. If there is none, leave the field empty.

> **Image:** Wi-Fi password

#### Connect through Ethernet

- In the main configuration menu, choose **6 Configure LAN**. This will let you set up a static IP address for the gateway’s Ethernet adapter.

- Type a static IP Address according to the IP address of the router you want to connect to. Note that the gateway and the router must be in the same network segment. Otherwise, the connection will fail.

- By default, the IP Address of the gateway's Ethernet is `192.168.10.10`.

> **Image:** Default gateway Ethernet IP Address

- Then configure the IP address of the router. This is the LAN interface IP address of the router.

> **Image:** Router LAN IP

- Press **OK** and the success message will appear.
- After reboot, the gateway will connect to the router successfully through Ethernet.

#### Reboot

Lastly, reboot the gateway using the command shown below and put it in the command line.

```
sudo reboot
```

## Optional Configuration

The configurations in this section are only optional and situational.

### Reverting to Wi-Fi AP Mode

If you have entered either or both incorrect Wi-Fi SSID and Password in the Wi-Fi Client Mode setup for the RAK7248 WisGate Developer D4H Gateway to connect to the router, follow this set of steps to work again in Wi-Fi AP Mode and redo the setup.

- Remove the SD Card from your RAK7248 WisGate Developer D4H Gateway and insert it into your PC. Your PC should be able to detect it the same way as on the image below:\

> **Image:** Creating rak_ap file to your SD Card

- Using your **Command Prompt** or **Terminal**, navigate to your SD Card and type the following command to generate the **rak_ap** file.

```
cd > rak_ap
```

- Check if the rak_ap file is created successfully. If so, re-insert the SD Card into your RAK7248 WisGate Developer D4H Gateway, and it should work again in Wi-Fi AP Mode.

### Configuring the Gateway

If you have successfully logged into your gateway using SSH, enter the following command in the command line:

```
sudo gateway-config
```

You will see the following page:

> **Image:** Configuration options for the gateway

1. **Set pi password** - used to set/ change the password of the gateway.
2. **Set up RAK Gateway Channel Plan** - used to configure the frequency, which the gateway will operate on, and the LoRaWAN Server which the gateway will work with.
3. **Restart packet-forwarder**- used to restart the LoRa packet forwarder.
4. **Edit packet-forwarder config** - used to open the global_conf.json file, to edit LoRaWAN parameters manually.
5. **Configure WIFI** - used to configure Wi-Fi settings in order to connect to a network.
6. **Configure LAN** - used to configure the Ethernet adapter settings.

:::tip NOTE

A unique ID will be generated for the gateway. This is also called gateway EUI in the figure above, and it is essential for registering the gateway with any LoRa Network Server (TTN, ChirpStack).
:::

There is yet another way to get your Gateway ID, by just entering the following command in the command line.

```
sudo gateway-version
```

When generating the ID by using the command, you will see the following:

> **Image:** Gateway ID using the command line

#### Setting a New Password for the Gateway

It is a good security practice to change the default password Raspberry Pi which is the same for all Raspberry Pi devices.

1. First, choose **1 Set pi password** option referred to on the image below.

> **Image:** Set Pi password

2. Next, press **Yes**, and you will be asked to enter your new password twice then click **Enter**.

> **Image:** Confirm password change

3. The success message for changing the password will then pop up.

> **Image:** Successful password change

#### Setup RAK Gateway Channel Plan

This menu allows you to select your LoRa frequency band and one of the two available Networks Server options by choosing **2 Setup RAK Gateway Channel Plan**.

> **Image:** Choosing Setup RAK Gateway Channel Plan

You can choose one of two supported LoRa Servers: **TTN** or **ChirpStack**.

##### Server is TTN

:::tip NOTE
If you want to use the ChirpStack for your Network server, head to the next section: [**Server is ChirpStack**](#server-is-chirpstack).
:::

> **Image:** Server is TTN

If you choose TTN as the LoRa Server, you will see the same page, as shown in **Figure 27**. Visit the [LoRa Alliance Regional Parameter](https://lora-alliance.org/wp-content/uploads/2021/05/RP002-1.0.3-FINAL-1.pdf) for more information on your local frequency plan. This will allow you to choose the correct plan.

> **Image:** Selecting the TTN channel plan

After choosing the correct frequency, the success message will appear, as shown in **Figure 28**.

> **Image:** Selecting the TTN channel plan

:::tip NOTE
- When a Channel plan is selected, the gateway is configured to connect to the nearest cluster to the region. If new clusters are presented, the channel plans will be updated. For now, the only available clusters are:
   - eu1.cloud.thethings.network (European)
   - au1.cloud.thethings.network (Australian)
   - nam1.cloud.thethings.network (North American)
:::

- If you want to use another cluster, you can change the server address by selecting **4 Edit packet-forwarder config**.
- If you want to use TTN for the LoRa Network server, you can skip the **If the Server is ChirpStack** section and head to [registering the gateway in TTN](https://docs.rakwireless.com/product-categories/wisgate/rak7248/lorawan-network-server-guide/#connecting-with-chirpstack).

##### Server is ChirpStack

> **Image:** Server is ChirpStack

If you choose ChirpStack as your LoRa Server, you will see the following page with two options available:

1. **ChirpStack Channel Plan Configuration** - used to configure your Regional Frequency Band.
2. **ChirpStack ADR Configure** - used to enable/disable the Adaptive Data Rate (ADR) functionality.

> **Image:** Configure ChirpStack channel plan

First, select **1 ChirpStack Channel-plan configuration** for configuring your frequency channel. Then, set the IP address of the ChirpStack.

> **Image:**  Regional Frequency Band Option

> **Image:** Default ChirpStack IP Address

:::tip NOTE

- The default IP Address is `127.0.0.1`. The latest firmware/GitHub repository installs ChirpStack on the Raspberry Pi.
:::

- If you want to use an external ChirpStack, you need to set it to its IP Address.
- If you have selected **ChirpStack ADR Configure** instead, you can enable/disable the **Adaptive Data Rate (ADR)** functionality:

  
> **Image:** ChirpStack ADR Enable/Disable

- If you want to use ChirpStack for the LoRa Network server, you can head to [registering the gateway in ChirpStack](https://docs.rakwireless.com/product-categories/wisgate/rak7248/lorawan-network-server-guide/#connecting-with-chirpstack).

