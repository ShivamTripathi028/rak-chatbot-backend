---
title: RAK7240 Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK7240. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Gateway.
keywords:
- RAK7240
- wisgate
- quickstart
image: https://images.docs.rakwireless.com/wisgate/rak7240/quickstart/rak7240.png
sidebar_label: Quick Start Guide
---
    

# RAK7240 Quick Start Guide

## Prerequisites

### What Do You Need?

1. [**RAK7240 WisGate Edge Prime**](https://store.rakwireless.com/products/rak7240-outdoor-lpwan-gateway?utm_source=RAK7240WisGateEdgePrime&utm_medium=Document&utm_campaign=BuyFromStore)
2. A Windows/Mac OS/Linux Computer

:::warning
The SIM card slot of the cellular versions is not hot-swappable. Make sure the gateway is switched off before inserting or ejecting the SIM card.
:::

### What's Included in the Package?

> **Image:** RAK7240 WisGate Edge Prime

:::tip NOTE
The number of antennas depends on what you order. Refer to the store for more information.
:::

## Product Configuration

### Gateway Installation Guide

For details about the interfaces and connectors of RAK7240 WisGate Edge Prime Gateway enclosure, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisgate/rak7240/datasheet/#interfaces-hardware-interfaces).

#### Installation

There are two options for installing the RAK7240 WisGate Edge Prime Gateway:

##### Pole Mounting

1. Fix the installation kit at the bottom of the device with four M5*8 screws.

> **Image:** Fixing the Installation Kit to the RAK7240

2. Slide the steel band clamps through the rectangular hole of the installation kit. Wrap the band clamps around the pole, lock them, and then tighten the clamps using a screwdriver.

> **Image:** Fixing the RAK7240 to a Pole

##### Wall Mounting

1. Use Ø5 mm drill head and drill four (4) holes on the wall according to the dimension displayed in Figure 4. Plug the screw anchors in the wall.

> **Image:** RAK7240 wall mounting dimensions

2. Using the tapping screws, attach the device to the wall.

> **Image:** Fixing RAK7240 to a wall

#### Weather Protection

To better protect the Ethernet cable gland and the antenna connector from the weather, you need to cover them with PVC tape.

1. Clean the surface area of the connector that will be wrapped. Wrap a layer of PVC tape with a 50% overlap according to the rotation direction of the connector. Continue wrapping the PVC tape to about 10 mm below the end of the connector.

> **Image:** Wrapping with PVC tape

2. Cut off about 50 cm waterproof tape. Stretch it to double the length, and wrap three layers around the connector with a 50% overlap. Hold the tape in place with your hand for a few seconds.

> **Image:** Wrapping with waterproof tape

3. Wrap three additional layers with PVC tape with natural uncoiling force and a 50% overlap. Make sure to cover the head and the tail of the connector.

> **Image:** Final PVC wrapping

### Power on the Gateway

1. Attach the antennas

First and foremost, screw on the antennas. All 5 of them should be installed, two (2) antennas on the **bottom** (**Wi-Fi**, **GPS**) and three (3) on the **top** (**LoRa**, **LTE**)

:::warning
Do not power the device if any antenna port has been left open. In case you do not desire to use one or more antenna features, make sure to terminate the port with a **50 Ohm load**.
:::

2. Power on the Gateway

It is recommended to use a **CAT5 Cable** to provide power to the Gateway. Attach one end to the provided **PoE injector** and the other to the **Ethernet Port** (ETH) on the bottom of the casing.

> **Image:** Powering the Gateway using PoE

### Access the Gateway

#### Wi-Fi AP Mode

By default, the Gateway will work in Wi-Fi AP Mode which means that you can find an SSID named like "**RAK7240_XXXX**" on your PC's Wi-Fi Network List. "XXXX" is the last two bytes of the Gateway MAC address. To access the Web Management Platform, input the IP Address: **192.168.230.1** in your Web browser.

:::tip NOTE
No password is required to connect via Wi-Fi.
:::

Using your preferred Web browser, input the aforementioned IP Address and you should see the same Log-in Page shown in the following image. Login the credentials provided below:

- **Username**: root
- **Password**: root

> **Image:** Accessing the Gateway via Wi-Fi AP Mode

#### WAN Port (Ethernet)

Connect the Ethernet cable to the port marked “ETH” on the Gateway and the other end to the PoE port of the PoE injector. Connect the LAN port of the PoE injector to your PC.

The default IP is **169.254.X.X**. The last two segments(X.X) are mapped from the last four bits of the MAC address of your gateway. For example, the last four bits of the MAC address are 0F:01, and the IP address is 169.254.15.1. Make sure to manually set the address of your PC to one in the same network (for example 169.254.15.100). Use the same credentials for the Web UI as for AP mode.

> **Image:** Accessing the Gateway via WAN Port (Ethernet)

### Access the Internet

#### Connect through Wi-Fi

> **Image:** Accessing the Internet using Wi-Fi

Go into the **Network>Wi-Fi Menu** and make sure to enable the **Wireless Client** as it is disabled initially. Enter or click "**Scan**" to choose your **ESSID**, select the right **Encryption** method and enter the correct **Key**.

> **Image:** Connect through Wi-Fi Credentials

:::tip NOTE
Assuming you have entered the correct parameter values you should get an IP address assigned by your Wi-Fi router's (AP) built-in DHCP server. You can use this new IP address to log in via a web browser (same way as in AP mode).
:::

#### Connect through Ethernet/PoE

> **Image:** Accessing the Internet through Ethernet

Connect the Ethernet cable to the port marked “ETH” on the Gateway and the other end to the PoE port of the PoE injector. Connect the LAN port of the PoE injector to your router. The router’s DHCP server should assign an IP Address to the Gateway. You can change the default settings below if you wish (details in the User Manual).

> **Image:** Connect through Ethernet Settings

