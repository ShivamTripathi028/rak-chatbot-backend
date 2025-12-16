---
title: RAK7268 WisGate Edge Lite 2 Quick Start | LoRaWAN Gateway Setup & Configuration
description: Set up your RAK7268 WisGate Edge Lite 2 with this guide. Configure the 8-channel indoor LoRaWAN gateway, access the Web UI, & optimize OpenWRT settings easily.
image: https://images.docs.rakwireless.com/wisgate/rak7268/datasheet/rak7268.png
keywords:
  - wisgate edge lite 2
  - semtech sx1302 lora chip
  - rak7268
  - rak gateway
  - rak7268 setup
  - 8 channel indoor lorawan gateway
  - lorawan indoor gateway
  - openwrt lorawan gateway
  - lorawan gateway
  - configure rak7268 lorawan gateway
date: 2021-04-11
sidebar_label: Quick Start Guide
---


import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK7268 Quick Start Guide

## Prerequisites

### What Do You Need?

1. [**RAK7268/RAK7268C WisGate Edge Lite 2**](https://store.rakwireless.com/products/wisgate-edge-lite-2-rak7268-rak7268c?utm_source=WisGateRAK7268&utm_medium=Document&utm_campaign=BuyFromStore)
2. [Ethernet Cable](https://store.rakwireless.com/products/ethernet-cable-gland?utm_source=EthernetCableGland&utm_medium=Document&utm_campaign=BuyFromStore) (RJ-45 Port) – for Ethernet connection
3. A Windows/MacOS/Linux computer

:::warning
The SIM card slot of the cellular versions is not hot-swappable. Make sure the gateway is switched off before inserting or ejecting the SIM card.
:::

## Product Configuration

### Power on the Gateway

1. Attach the LoRa Antenna.

First and foremost, screw on the antenna to the RP-SMA connector on the back panel of the RAK7268/C WisGate Edge Lite 2.

:::warning
Do not power the device if the LoRa Antenna port has been left open to avoid potential damage to the RAK7268/RAK7268C WisGate Edge Lite 2.
:::

2. Power the gateway **ON**.

It is recommended to use the **12&nbsp;V DC adapter** that comes with the RAK7268/RAK7268C WisGate Edge Lite 2. Optionally, you can use your own **PoE cable** and **injector** since the device supports PoE.

#### Casing and Ports

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7268/quickstart/1.top-view.png"
  width="40%"
  caption="RAK7268/C WisGte Edge Lite 2 Top View"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7268/quickstart/2.back-view.png"
  width="70%"
  caption="RAK7268/C WisGate Edge Lite 2 Back Panel"
/>

#### Status LED Indicators

<table>
    <tr><td><b>LEDs</b></td><td><b>Status Indication Description</b></td></tr>
    <tr><td>PWR LED</td><td>Power indicator - The LED is on when the device powered.</td></tr>
    <tr><td>Breathing LED</td><td>Breathing after system is up</td></tr>
    <tr><td rowSpan="4">ETH LED</td></tr>
    	<tr><td>ON - Link is up</td></tr>
    	<tr><td>OFF - Link is down</td></tr>
    	<tr><td>Flicker - Ongoing data transfer</td></tr>
    <tr><td rowSpan="4">LoRa LED</td></tr>
    	<tr><td>ON - LoRa is up</td></tr>
    	<tr><td>OFF - LoRa is down</td></tr>
    	<tr><td>Flicker - Ongoing data transfer</td></tr>
    <tr><td rowSpan="9">WLAN LED</td></tr>
    	<tr><td>AP Mode:</td></tr>
    		<tr><td>     - ON - The AP is up</td></tr>
    		<tr><td>     - OFF - The AP is down</td></tr>
    		<tr><td>     - Flicker - Ongoing data transfer</td></tr>
    	<tr><td>STA Mode:</td></tr>
    		<tr><td>     - Slow flicker (1&nbsp;Hz) - Disconnected</td></tr>
    		<tr><td>     - ON - Connected</td></tr>
    		<tr><td>     - Flicker - Ongoing data transfer</td></tr>
    <tr><td rowSpan="4">LTE LED (will light up only on RAK7268C)</td></tr>
    	<tr><td>Slow flicker (1800&nbsp;ms High / 200&nbsp;ms Low) - Network searching</td></tr>
    	<tr><td>Slow flicker (200&nbsp;ms High / 1800&nbsp;ms Low) - Idle</td></tr>
    	<tr><td>Fast flicker (125&nbsp;ms High / 125&nbsp;ms Low) - Ongoing data transfer</td></tr>
</table>

#### Reset Key Functions

The functions of the **Reset** key are as follows:

1. **Short press** - Restarts the gateway.
2. **Long press (5 seconds and above)** - Restores factory settings.


### Access the Gateway

In this section, several ways of accessing the gateway are provided to have different alternatives for you to choose from depending on the availability of the requirements needed.

:::warning
Do not power the device if the LoRa Antenna port has been left open to avoid potential damage to the RAK7268/RAK7268C WisGate Edge Lite 2.
:::

#### Wi-Fi AP Mode

By default, the gateway will work in Wi-Fi AP Mode which means that you can find an SSID named **RAK7268_XXXX** on your PC's Wi-Fi Network List. **XXXX** is the last two bytes of the gateway's MAC address.

:::tip NOTE
 No password is required to connect via Wi-Fi
:::

Using your preferred Web browser, log in with the credentials provided below:

- **Browser Address**: 192.168.230.1
- **Username**: root
- **Password**: root

#### WAN Port (Ethernet)

Connect the Ethernet cable to the port marked ETH on the gateway and the other end to the PoE port of the PoE injector. Connect the LAN port of the PoE injector to your PC.

The default IP is **169.254.X.X.** The last two segments (X.X) are mapped from the last four bits of the MAC address of your gateway.

For example, the last four bits of the MAC address are 0F:01, and the IP address is 169.254.15.1. Make sure to manually set the address of your PC to one in the same network (for example 169.254.15.100). Use the same credentials for the Web UI as for AP mode.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7268/quickstart/3.login-page.png"
  width="100%"
  caption="Web UI Login Page"
/>


### Access the Internet

#### Connect through Wi-Fi

Go into the **Network>Wi-Fi** menu and make sure to select **Client** in the **Mode** field. Enter or click "**Scan**" to choose your **ESSID**, select the right **Encryption** method and enter the correct **Key**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7268/quickstart/4.connect-through-wi-fi.png"
  width="100%"
  caption="Connect through Wi-Fi Credentials"
/>

:::tip NOTE
Assuming you have entered the correct parameter values you should get an IP address assigned by your Wi-Fi router's (AP) built-in DHCP server. You can use this new IP address to log in via a web browser (same way as in AP mode).
:::

#### Connect through Ethernet

Connect the one end of the Ethernet cable to the Ethernet on the Gateway and the other end to your router. The router’s DHCP server should assign an IP Address to the Gateway. You can change the default settings below if you wish (Full details in the [WisGateOS User Manual](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos/overview/#overview)).

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7268/quickstart/5.connect-through-ethernet.png"
  width="100%"
  caption="Connect through Ethernet Settings"
/>

