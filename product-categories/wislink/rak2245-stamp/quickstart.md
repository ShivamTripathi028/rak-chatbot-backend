---
slug: /product-categories/wislink/rak2245-stamp/quickstart/
title: RAK2245 Stamp WisLink LPWAN Concentrator Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK2245 Stamp WisLink LPWAN Concentrator. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: "https://images.docs.rakwireless.com/wislink/rak2245-stamp/rak2245-stamp.png"
keywords:
    - wislink
    - lpwan
    - rak2245 stamp
    - concentrator
    - lpwan
    - quickstart
sidebar_label: Quick Start Guide
---

# RAK2245 Stamp WisLink LPWAN Concentrator Quick Start Guide

## Prerequisites

1. [RAK2245 Stamp WisLink LPWAN Concentrator](https://store.rakwireless.com/products/rak2245-stamp-edition?utm_source=RAK2245WisLink-LoRaStampEdition&utm_medium=Document&utm_campaign=BuyFromStore)
2. Raspberry Pi 3B+
3. 16 GB SD card + card reader
4. 5 V at least 2 A Micro USB Power Supply
5. A Windows/Mac OS/Linux Computer
6. Latest [RAK2245 Stamp Firmware](datasheet.md#firmware)

## Package Inclusions

- 1pc - RAK2245 Stamp WisLink LPWAN Concentrator
- 1pc - iPEX LoRa Antenna
- 1pc - Passive GPS Antenna

## Product Configuration

### Accessing your Gateway

After burning the firmware image onto the SD card, make sure you have inserted the SD card into the **Raspberry Pi with the RAK2245 Stamp WisLink LPWAN Concentrator Module** and have the LoRa and GPS Antenna connected. After which, you can now safely power on the gateway. In this document, several ways in accessing the gateway are provided to have different alternatives for you to choose depending on the availability of the requirements needed.

:::warning
Before powering the Raspberry Pi, you should connect the LoRa and GPS antennas. Not doing so might damage the boards.
:::

#### 1. Wi-Fi AP Mode

By default, the gateway will work in Wi-Fi AP Mode which means that you can find a SSID named like "**Rakwireless_XXXX**" on your PC Wi-Fi Network List.

> **Image:** RAKWireless Access Point

:::tip NOTE
Connect to this Wi-Fi SSID by using \"**rakwireless**\" as the default password. The default IP address of the Gateway's Wi-Fi is **`192.168.230.1`**. Take note of this IP address as this will be needed in connecting via SSH.
:::

#### 2. Via the Ethernet port on the Raspberry Pi 3B+

You can also connect your PC with the gateway through an Ethernet cable. By default, the IP address of the Gateway’s Ethernet interface is `192.168.10.10`, so you need to set the IP address of your PC’s Ethernet to the same network segment, for example, `192.168.10.20`_._

- To do this in Windows, go to Control Panel -> Network and Internet -> Network and Sharing Center and Click **Ethernet**

> **Image:** Network and Sharing Center

- Click **Properties** then Choose **Internet Protocol Version 4 (TCP/IPv4).**

> **Image:** Ethernet Properties

- By default, it will obtain an IP Address automatically. Click the Option "Use the following IP Address" and enter the IP Address: `192.168.10.20` and press **OK**.

> **Image:** TCP/IPv4 Properties

Now, you should be able to access your gateway from your PC successfully using the IP Address `192.168.10.10`through SSH.

#### Log into the Gateway via SSH

##### 1. Windows OS

SSH (Secure Shell) is typically used to log in to a remote machine and execute commands. There are a lot of free and good SSH Clients out there namely [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), [BitVise SSH Client](https://www.bitvise.com/ssh-client-download), [MobaXterm ](https://mobaxterm.mobatek.net/)and many more. Feel free to choose one that fits your needs, you will be using Putty for this guide.

> **Image:** Putty Software for SSH in Windows

- If you have connected to the gateway through **Wi-Fi AP Mode**, the IP Address is `192.168.230.1`
- If you have connected to the gateway through **Ethernet**, the IP Address is `192.168.1.10`
- It will then prompt you to enter the username and password. The default username is "**pi**" and the default password is "**raspberry**"

> **Image:** Command Line after Log-in

##### 2. Mac OS

Open the Terminal of Mac OS. Launch the **Terminal** application, which is found in "/Applications/Utilities/" directory but you can also launch it from Spotlight by hitting **Command + Spacebar** and typing “Terminal” and then return:

> **Image:** Opening Terminal in Mac OS

Open the terminal of Mac OS. Enter **root mode** by typing the following command: "`sudo -i`"

> **Image:** SSH in Mac OS

- If you are not in root mode, enter "`ssh pi@192.168.230.1`" in the terminal to login to your Gateway, the default password is "**raspberry**".
- If you connect your PC with the gateway through Ethernet Cable, you should enter "`ssh pi@192.168.10.10`", the default password is "**raspberry**".

Now, you have logged into the gateway through SSH successfully the same with **Figure 9**.

> **Image:** Log-in Successful Notification

##### 3. Linux OS

If the OS of your PC is Linux, you should do the same as the Mac OS, except for the root mode.

### Accessing the Internet

Assuming you have successfully logged into your gateway using SSH, enter the following command in the command line:

```sh
sudo gateway-config
```

You will now then see a page like the following picture below

> **Image:** Configuration Options for the Gateway

1. **Set pi password** - used to set/change the password of the Gateway.
2. **Set up RAK Gateway LoRa Concentrator** - used to configure the frequency, which the gateway will operate on, and the LoRa Server which the gateway will work with.
3. **Edit packet-forwarder config-** used to open the global_conf.json file, in order to edit LoRaWAN parameters manually.
4. **Restart packet -forwarder** - used to restart the LoRa packet forwarded process.
5. **Configure Wifi** - used to configure the Wi-Fo settings in order to connect to a network.
6. **Configure LAN** - used to configure the Ethernet adapter settings.

#### Connect through Wi-Fi

If you want to connect through Wi-Fi, it can easily be done with the Wireless capabilities of the Raspberry Pi by choosing "**5 Configure WIFI**". By default, the RAK2245 Stamp WisLink LPWAN Concentrator works in Wi-Fi AP Mode. In order for the gateway to connect to the router, it must work in Wi-Fi Client Mode.

> **Image:** Configuration options for Wi-Fi

There are 5 options to choose from in the Wi-Fi configuration menu:

1. **Enable AP Mode/Disable Client Mode** - the gateway will work in Wi-Fi Access Point Mode after rebooting while the Wi-Fi Client Mode will be disabled (this is the default mode).
2. **Enable Client Mode/Disable AP Mode** - the gateway will work in Wi-Fi Client mode after rebooting, while Wi-FI AP Mode will be disabled.
3. **Modify SSID and pwd for AP Mode** - used to modify the SSID and password of the Wi-Fi AP. Only works if the Wi-Fi AP Mode is enabled.
4. **Add New SSID for Client** - is used if you want to connect to a new Wi-Fi Network. Only works in Wi-Fi Client mode.
5. **Change Wi-Fi Country** - is used to modify the Resident Country to match with Wi-Fi standards.

:::warning
In order to enable Wi-Fi Client Mode, you have to disable AP Mode.
:::

Once Wi-Fi AP Mode has been disabled by choosing "**2 Enable Client Mode/Disable AP Mode**", you can now then connect to a new Wi-Fi Network by choosing "**4 Add New SSID for Client**"

> **Image:** Add a new SSID

- Start by selecting your country of residence:

> **Image:** Selecting Country of Residence

- Enter the SSID of the network you want to connect:

:::warning
Ensure to input the correct Wi-Fi SSID and Password or you will not be able to connect to the RAK2245 Stamp Edition again via SSH in Wi-Fi AP Mode. If stuck in this situation, follow the procedure listed in the [Accessing the Internet](#reverting-to-wi-fi-ap-mode) document which is applicable for all Raspberry Pi based gateways to work again in Wi-Fi AP mode.
:::

> **Image:** SSID of the Network you want to connect to

- Enter also the password. Just leave it empty if None.

> **Image:** Password of the Wi-Fi

#### Connect through Ethernet

If you want to connect to the router through Ethernet Cable, do the following steps:

- In the main configuration menu, choose **“6 Configure LAN”**. This will let you set up a static IP address for the Gateway’s Ethernet adapter.
- Just fill a static IP Address according to the IP address of the router you want to connect. The gateway and the router must be in the same network segment, otherwise the connection will fail.
- By default, the IP Address of the Gateway's Ethernet is `192.168.10.10`

> **Image:** Default gateway Ethernet IP address

- Then configure the router's IP Address. It must be the true IP address of the router:

> **Image:** LAN Interface IP Address of the Router

- Press OK then the success message will appear.
- Lastly, reboot the gateway using the command "`sudo reboot`" in the command line and it will connect to the router successfully through Ethernet.

#### Optional Configurations

These configurations under this section are only optional and situational.

##### Reverting to Wi-Fi AP Mode

In the event that you have entered either or both incorrect Wi-Fi SSID and Password in the Wi-Fi Client Mode setup for the RAK2245 Stamp WisLink LPWAN Concentrator to connect to the router, follow these set of steps for you to work again in Wi-Fi AP Mode and redo the setup.

- Remove the SD card from your RAK2245 Stamp WisLink LPWAN Concentrator and insert it into your PC. Your PC should be able to detect it the same with **Figure 18**.

> **Image:** Creating rak_ap file to your SD card

- Using your **Command Prompt** or **Terminal**, navigate to your SD Card and type this command to generate the **rak_ap** file.

```sh
cd > rak_ap
```

- Check if the rak_ap file is created successfully. If so, re-insert the SD card into your RAK2245 Stamp WisLink LPWAN Concentrator and it should work again in Wi-Fi AP Mode.

### Configuring the Gateway

Assuming you have successfully logged into your gateway using SSH, enter the following command in the command line:

```sh
sudo gateway-config
```

You will now then see a page like **Figure 19**.

> **Image:** Configuration Options for the Gateway

1. **Set pi password** - used to set/change the password of the Gateway.
2. **Set up RAK Gateway LoRa Concentrator** - used to configure the frequency, which the gateway will operate on, and the LoRa Server which the gateway will work with.
3. **Edit packet-forwarder config-** used to open the global_conf.json file, in order to edit LoRaWAN parameters manually.
4. **Restart packet -forwarder** - used to restart the LoRa packet forwarded process.
5. **Configure Wifi** - used to configure the Wi-Fo settings in order to connect to a network.
6. **Configure LAN** - used to configure the Ethernet adapter settings.

:::tip NOTE
A unique ID will be generated for Gateway. This is also called Gateway EUI and is essential for registering the gateway with any LoRa Network Server (TTN, Chirpstack).
:::

There is also another way to get your **Gateway ID**, just enter the command below in the command line:

> **Image:** Gateway ID using the command line

#### Set a new password for the Gateway

It is a good security practice to change the default password "**raspberry**" which is the same on all Raspberry Pi devices.

1. First, choose "**1 Set pi password**" option referred on the image below.

> **Image:** Set Pi Password

2. Next, press "**Yes**" and you will be asked to enter your new password twice then press "**Enter**".

> **Image:** Confirm Password Change

3. Alright, the success message for changing password will then pop up.

> **Image:** Successful Password Change

#### Set up RAK Gateway LoRa Concentrator

This menu allows you to select your LoRa frequency band and one of the two available Networks Server options by choosing "**2 Setup RAK Gateway LoRa concentrator**".

> **Image:** Choosing Setup RAK Gateway LoRa concentrator

You can choose one of two supported LoRa Servers: **TTN** or **ChirpStack**.

##### Server is TTN

> **Image:** Server Is TTN

- **TTN (The Things Network)** - If you choose TTN as the LoRa Server, you will see the following page. Visit this [article](https://www.thethingsnetwork.org/docs/lorawan/frequencies-by-country.html) for more information on your local TTN frequency plan. This will allow you to choose the correct plan

> **Image:** Selecting the TTN Channel Plan

After choosing the correct frequency, the success message will appear as shown below.

> **Image:** Successfully Changed the Frequency

##### Server is Chirpstack

> **Image:** Server Is Chirpstack

**ChirpStack** - If you choose Chirpstack as your LoRa Server, you will see the following page with two options available:

- **ChirpStack Channel Plan Configuration** - used to configure your Regional Frequency Band.
- **ChirpStack ADR Configure** - used to enable/disable the Adaptive Data Rate (ADR) functionality.

First, select option 1 for configuring your Regional Frequency Band

> **Image:** Regional Frequency Band Option

Then, set the IP address of the ChirpStack which you want your gateway to work with:

> **Image:** Default ChirpStack IP Address

:::tip NOTE
The default IP Address is **`127.0.0.1`** which means you will be using the Built-in LoRa Server. If you want to use an independent LoRa Server running on another device or a cloud based LoRa Server, you need to set it to the corresponding IP address
:::

- If you have instead selected "**Chirpstack ADR Configure**" you can enable/disable the Adaptive Data Rate (ADR) functionality:

> **Image:** Chirpstack ADR Enable/Disable

### Connecting to The Things Network (TTN)

The Things Network is about enabling low power devices to use long range [gateways](https://www.thethingsnetwork.org/docs/gateways/) to connect to an open-source, decentralized network to exchange data with Application. Learn more about the [Things Network](https://www.thethingsnetwork.org/docs/) on their website.

- First, you should have connected your gateway to the router in order to access the internet according to the method which has been introduced in the [Accessing the Internet](#accessing-the-internet) section of this document.
- Second, configure your gateway and choose TTN as the LoRa Server and choose a correct frequency according to the method which has been introduced in the [Configuring the Gateway](#configuring-the-gateway) section.
- Now go to the TTN Website: [https://www.thethingsnetwork.org/](https://www.thethingsnetwork.org/) and Login. You will then see the following page:

> **Image:** The Things Network Home Page

- Choose Console then Click Gateways.

> **Image:** The Things Network Console Page

- All of your registered gateways will be displayed on a page. Click "**register gateway**"

> **Image:** Adding a gateway to TTN

> **Image:** Registering your gateway

- **Gateway EUI** - refers to the Gateway ID you obtained from the previous steps. In case you forgot, just type "**gateway-version**" in the command line. This must be the same with the Gateway's True Gateway ID otherwise you will fail to register your gateway on TTN.

> **Image:** RAK2245 Stamp WisLink LPWAN Concentrator ID in SSH

:::tip NOTE
Make sure to select the \"**I'm using the legacy packet forwarder**\" check box.
:::

- **Description** - A human readable description of your Gateway.
- **Frequency Plan** - This is the frequency you want to use and it must be the same with gateway and the Node.
- **Router** - The router this gateway will connect to. To reduce latency, pick a router that is in a region which is close to the location of the gateway.
- **Location** - Choose the location of the gateway by entering its coordinates. This is reflected on the Gateway World Map.
- **Antenna Placement** - Where is your antenna placed? Is it placed indoors or outdoors?

Click **Register Gateway** and wait for a couple of minutes. If the status of your gateway is **Connected**.

> **Image:** RAK2245 Stamp WisLink LPWAN Concentrator TTN Connection Success

### Connect the Gateway with ChirpStack

The ChirpStack or previously known as LoRa Server project provides open-source components for building LoRaWAN networks. You can learn more about ChirpStack [**here**](https://www.chirpstack.io/)

For the RAK2245 Stamp WisLink LPWAN Concentrator Concentrator Module, there are two (2) ways to use the ChirpStack:

#### 1. Using the built-in ChirpStack

There is a built-in ChirpStack in every RAK Developer gateway if you use the latest firmware.

- When you use it for the first time after burning the latest firmware, the gateway will work in the EU868 Band and use the built-in ChirpStack as its default LoRa Server. If you don't want to change the frequency or LoRa Server, you don't have to do anything as this will be configured automatically when the gateway boots.
- However if it is not the first time and you want to use the built-in ChirpStack as the LoRa Server, follow the steps discussed in [Configuring the Gateway](#configuring-the-gateway) section.
- **Optional:** If ever you disabled the AP Mode and you have connected it to your own Wifi network (Client Mode). You can search for your gateway’s IP Address via [**Advanced IP Scanner**](https://www.advanced-ip-scanner.com/). Copy the IP Address of your Gateway, it should have a Manufacturer name of **Raspberry Pi Foundation**:

> **Image:** IP address of your RAK2245 Stamp WisLink LPWAN Concentrator using IP Scanner

There is a Web-based UI that comes with the ChirpStack instance. Simply open a browser and enter the following credentials:

- **Browser Address**: "Gateway IP Address:8080" (**Example**: http://192.168.254.176:8080)
- **Username**: admin
- **Password**: admin

:::warning
It is advisable to change your password to tighten the security of your account. You can change this by clicking the \"change password\" button at the user icon.
:::

> **Image:** ChirpStack Web-based UI

- Everything should be pre-configured: Device profiles have been created, the gateway has been registered with the server, etc. If you go to the Gateways tab and click on rak_gateway, you should see the gateway details page.

> **Image:** Available Gateways in Chirpstack

- Go to the rak_gateway and see the "Last seen" status. It must be a few seconds ago which signifies that the gateway is visible in the ChirpStack server.

> **Image:** Last Seen Status

#### 2. Using an Independent ChirpStack

You can setup an Independent ChirpStack by yourself. This is a lot more complicated having to deploy a remote ChirpStack by yourself but [Chirpstack](https://www.chirpstack.io/guides/debian-ubuntu/) provided a detailed guide on how to do it.

> **Image:** Chirpstack Getting Started Guide on Ubuntu

:::warning
Remember to run the \"`sudo gateway-config`\" command in the CLI and point the gateway to the IP address of the machine you just installed Chirpstack on. This can be done in item 2 in the menu \"**Setup RAK Gateway LoRa**® **concentrator**\"!
:::

- Assuming you have set it up correctly, Login to your ChirpStack to register your gateway by opening the ChirpStack's web page in a browser by entering "IP Address of ChirpStack:8080".

> **Image:** ChirpStack Login Page

- The default username is "**admin**" and the password is also "**admin**".

> **Image:** ChirpStack Home Page

- Click "Gateways" and Press "**+ CREATE**" to register your Gateway.

> **Image:** ChirpStack Registered Gateways

- Click "**Create**" to register your gateway and fill up the necessary information.

> **Image:** Registering your own Gateway

- Fill in the Gateway ID that you got from the last section ([Configuring the Gateway](#configuring-the-gateway)), also called Gateway EUI.
- If you have properly configured your gateway and there is a network connection between the external ChirpStack and your gateway, you should see the following page and status:

> **Image:** Successfully Registered the gateway

