---
title: RAK7267 WisGate Soho Pro Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK7267. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device.
image: "https://images.docs.rakwireless.com/wisgate/rak7201/rak7267.png"
keywords:
  - quickstart
  - RAK7267
  - wisgate
sidebar_label: Quick Start Guide
---

# RAK7267 WisGate Soho Pro Quick Start Guide

## Prerequisites

### Hardware

1. [RAK7267 WisGate Soho Pro](https://store.rakwireless.com/products/wisgate-soho-pro-gateway-rak7267?variant=43997899751622)
2. A Windows/Mac OS/Linux Computer
3. Installation Accessories (e.g., mounting kit, power supply, screws, etc.)
4. **NanoSIM Card** – Prepare a NanoSIM card (12 mm x 9 mm x 0.67 mm) before installation to enable cellular connectivity.

### Package Inclusion

> **Image:** RAK7267 package list

:::tip NOTE
The packing list shows cables for all power options supported by the gateway. This may not exactly match the cable options out of the box, depending on the bundle you purchased.
:::

## Product Configuration

### Installation

:::warning
- **DO NOT** eject the SD card located in the SD card slot during installation, as it stores logs and data essential for the device's performance.
- The SIM card slot of the cellular versions is not hot-swappable. Make sure the gateway is switched off before inserting or ejecting the SIM card.
:::

#### Insert SIM Card

1. Start by unscrewing the cap of the NanoSIM interface on the gateway Unify enclosure to expose the SIM card slot.

> **Image:** SIM card slot

2. Push the SIM card into the card slot according to the placement method marked on the interface.

> **Image:** Inserting the SIM card

3. Once completed, screw back the metal cap. Make sure it is tightly screwed.

#### Mounting

This section provides the instructions on mounting and securing the mounting kit to the enclosure and the mounting pole.

1. Fix the pole mounts marked with the letter A on the gateway Unify enclosure using four (4) pieces of M3 x 8 mm head screw with a washer. The fixed positions are shown in **Figure 5**.

> **Image:** Pole mounts marked with the letter A

> **Image:** Fixing the pole mounts on the enclosure

2. After fixing the mounts on the enclosure, place the Unify Enclosure onto the pole by using two (2) steel strips (65\~89 mm).

:::tip NOTE

The steel strips **ONLY** support 65\~89 mm diameter pole.

:::

> **Image:** Fixing the enclosure on the pole

### Lightning Protection

This section covers the installation of the lightning surge protection system when deploying the RAK7267 gateway outdoors. Such a protection system must be taken into consideration to ensure a fully functional gateway without interruptions or damage from lightning..

**Gateway Grounding**: It is recommended to use another 10 AWG or better grounding wire to connect the screw terminal on the bottom side of the gateway casing to the grounding rail (bar).

### Power On the Gateway

In this section, it is assumed that you have read and performed the procedures listed in the **Installation** part of this document.

The gateway supports multiple power supply options. Connect the gateway to the appropriate power source based on the power cables included in the bundle you purchased.

**Cable and Power Adapter:** When the gateway is deployed indoors, it is recommended to use the cable and power adapter to power the gateway.

> **Image:** Powering the gateway through a DC adapter

**DC Cable:** If you use a customized external DC power supply to power the gateway, you need to use the DC cable to connect the external power supply. The external power supply voltage range:  9~36 V<sub>DC</sub>.

> **Image:** Powering the gateway through an external DC power source

**Cable for RAK9155 Battery Plus**: For outdoor deployment scenarios, it is recommended to use RAK9155 Battery Plus as its power supply. This cable is dedicated to the RAK9155 Battery Plus.

> **Image:** Powering the gateway through RAK Battery Plus

:::tip NOTE
[RAK9155 Battery Plus](https://store.rakwireless.com/products/rak-battery-plus-rak9155?variant=42309251563718) is not included in the bundle, it needs to be purchased separately.
:::

### Access the Gateway

For RAK7267, you need to access the gateway through Wi-Fi AP Mode. You can find an SSID, named **RAK7267_XXXX** on your PC's Wi-Fi network list. **XXXX** is the last two bytes of the gateway's MAC address.

1. To access the Web Management Platform, input the following IP Address in your Web browser: `192.168.230.1`.

   :::tip NOTE

   No password is required to connect via Wi-Fi.

   :::

> **Image:** Accessing the gateway via Wi-Fi AP mode

2. For security reasons, upon the first login, you must set a login password. To do this, enter the desired password and confirm it in the provided fields. The password must meet the following requirements:

- At least 12 characters long
- Has at least one special character (`!“#$%&\‘()*+,-./:;<=>?@[]^_{|}~`)
- Has at least one number
- Has at least one standard Latin letter (used in the English alphabet)

> **Image:** Web UI login page

3. When the fields are filled in, click the **Set password** button to apply it. The web UI is now accessible and it will load the **LoRaWAN Statistics page**.

> **Image:** LoRaWAN statistics page

4. On the next log in, you need to use the set password for access. The default login username is **root**.

> **Image:** Login Page with set password

### Access the Internet

In this section, two methods of accessing the internet are provided to give you different alternatives to choose from, depending on the availability of the necessary requirements.

#### Connect Through Wi-Fi

> **Image:** Accessing the Internet using Wi-Fi

1. Access the gateway's Web UI, and navigate to **Network** > **WAN** > **Wi-Fi**.

2. Expand the Wi-Fi block and click on **Settings**. Make sure the **Interface** is enabled.

3. Click the **Scan** button to select your **ESSID**, or manually enter the ESSID of the network by clicking **Enter network (E)SSID manually**.

4. Choose the correct **Encryption** method and enter the appropriate **Key**.

   :::tip NOTE
   Assuming you have entered the correct parameter values, you should receive an IP address assigned by your Wi-Fi router's (AP) built-in DHCP server. You can use this new IP address to log in via a web browser (the same way as in AP mode).
   :::

   
> **Image:** Wi-Fi settings

For additional information, check the [WisGateOS 2 User Manual > WAN > Wi-Fi](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#wi-fi).

#### Connect Through Cellular

After inserting the SIM card, the gateway will automatically attempt to connect to the cellular network.

1. If manual APN configuration is needed, go to **Network** > **WAN** > **Cellular** in the Web UI.

2. Expand the **Cellular** section and click on **Settings**.

   
> **Image:** Cellular Interface Page

3. For parameter configuration, refer to the [WisGateOS 2 User Manual > WAN > Cellular ](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#cellular).

   
> **Image:** Cellular settings

:::tip NOTE
Make sure that your SIM card is activated and supports data services.
:::

## Tutorials

In this section, you can browse tutorials about the RAK7267 gateway to help you better understand and use the product.

| Tutorials                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Use the MQTT Broker Like a Pro + Examples](https://learn.rakwireless.com/hc/en-us/articles/26688300221079-How-To-Use-the-MQTT-Broker-Like-a-Pro-Examples)                                                      |
| [WisGate Edge V2 Gateways Remote Management - OpenVPN](https://learn.rakwireless.com/hc/en-us/articles/26527371792535-How-To-Configure-WisGate-Edge-V2-Gateways-Remote-Management-OpenVPN)                      |
| [ThingsBoard Configuration with MQTT/HTTP Integrations via WisGateOS 2](https://learn.rakwireless.com/hc/en-us/articles/26526970499735-How-To-Configure-ThingsBoard-with-MQTT-HTTP-Integrations-via-WisGateOS2) |
| [OpenVPN Server Installation Guide (For Ubuntu sys)](https://learn.rakwireless.com/hc/en-us/articles/26688144537623-How-To-Install-OpenVPN-for-Ubuntu-Systems)                                                  |

