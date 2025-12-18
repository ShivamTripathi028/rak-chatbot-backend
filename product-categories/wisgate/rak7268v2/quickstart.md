---
slug: /product-categories/wisgate/rak7268v2/quickstart/
title: RAK7268V2/RAK7268CV2 WisGate Edge Lite 2 Guide
description: Step-by-step instructions for installing and deploying the RAK7268V2/RAK7268CV2 WisGate Edge Lite 2 gateway, including setup, configuration, and mounting options.
image: "https://images.docs.rakwireless.com/wisgate/rak7268-v2/rak7268v2.png"
keywords:
  - Indoor gateway
  - 8 Channel gateway
  - RAK7268V2 manual
  - WisGate Edge Lite 2 guides
  - LoRaWAN gateway setup
  - build IoT gateway
sidebar_label: Quick Start Guide
tags:
 - rak7268v2
 - rak7268cv2
 - wisgate
 - quickstart
date: 2022-09-26
---

# RAK7268V2/RAK7268CV2 WisGate Edge Lite 2 Quick Start Guide

This manual provides brief instructions for installing and deploying the gateway.

## Prerequisites

+ <a href="https://store.rakwireless.com/products/wisgate-edge-lite-2-rak7268v2-rak7268cv2?utm_source=WisGateRAK7268V2&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAK7268V2/RAK7268CV2 WisGate Edge Lite 2</a>
+ <a href="https://store.rakwireless.com/products/ethernet-cable-gland?utm_source=EthernetCableGland&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">Ethernet Cable</a> (RJ-45 Port) for Ethernet connection
+ A Windows/MacOS/Linux Computer
+ Installation Accessories (e.g., mounting kit, power supply, screws, etc.)
+ **NanoSIM Card** (for LTE version) – If you're using the cellular version of the gateway, ensure you have a SIM card ready for installation. **Size:** 12 mm x 9 mm x 0.67 mm.

### Package Inclusion

> **Image:** RAK7268V2/RAK7268CV2 package contents

+ 1pc Gateway
+ 1pc LoRa antenna
+ 1pc Power supply
+ 1pc mounting bracket

## Product Configuration

### Gateway Installation Guide

:::warning
***Do not*** eject the SD card located in the SD card slot during installation, as it stores logs and data essential for the device's performance.
:::

#### Insert SIM Card

If you are using the cellular variant of the gateway, refer to this section. Otherwise, skip it.

:::warning
The SIM card slot of the cellular versions is not hot-swappable. Make sure the gateway is switched off before inserting or ejecting the SIM card.
:::

1. On the **back** of the gateway, locate the **NanoSIM card slot**.

> **Image:** NanoSIM card slot

2. Insert the **NanoSIM card** into the slot, ensuring it is securely seated.

#### Mount the Bracket

The gateway supports wall-mounting, ceiling-mounting, and rail-mounting. You can choose one according to your needs.

##### Wall Mounting

1. Use a **5-millimeter drill bit** to drill three (3) holes on a wall. It is recommended to mark the location of the holes on the wall before drilling.
2. Insert the expansion tubes into the drilled holes.
3. Secure the bracket to the wall using screws through the holes in the bracket.

> **Image:** Wall-mounted bracket installation

##### Ceiling Mounting

:::tip NOTE
For ceiling mounting, you need to choose a ceiling that is strong enough to support the gateway. It is recommended to mark the hole locations on the ceiling before installing the bracket.
:::

1. Choose self-tapping screws or expansion tubes and self-tapping screws to install the bracket according to the actual material of the ceiling.
2. (Optional) Refer to this step when installing the bracket using expansion tubes and self-tapping screws. Otherwise, skip it.
  -  Use a 5-millimeter drill bit to drill three holes in the ceiling.
  - Insert the expansion tubes into the holes drilled in the ceiling.
3. Secure the bracket to the ceiling using self-tapping screws through the holes in the bracket.

> **Image:** Ceiling-mounted bracket installation

##### T-Shaped Keel Mounting

In this section, a T-shaped keel is used as an example. You can choose other types of rails for installation.

:::tip NOTE
The bracket supports rail widths of 14 mm, 16 mm and 24 mm.
:::

1. Remove the mounting clip from the bracket.
2. Insert one side of the T-shaped keel into the two clips of the bracket.
3. Insert the two T-shaped hooks on the mounting clip into the T-shaped rails of the bracket, slide the mounting clip to the other side of the T-shaped keel, and make sure the clip is in place.

> **Image:** Bracket mounted on T-shaped keel structure

#### Install the Gateway

1. Align the lower edge of the gateway's hanging hole with the bracket's locking plate.
2. Move the gateway closer to the bracket so that the bracket's locking plate enters the gateway's hanging hole.
3. Pull the gateway to ensure that the gateway is in place.

> **Image:** Fixed gateway

### Attach the Antenna

1. **LoRa Antenna**

    Attach the **LoRa antenna** by screwing it onto the connector labeled **LoRa** on the gateway.
2. **LTE Antennas** *(if applicable)*

    For gateway models with **external LTE antenna support**, screw the **LTE antennas** onto the **RP-SMA connectors** labeled **MAIN** and **AUX**.

### Power On the Gateway

:::warning
Do not power the device if the LoRa antenna port has been left open to avoid potential damage to the RAK7268V2/RAK7268CV2 WisGate Edge Lite 2.
:::

The RAK7268V2/RAK7268CV2 can be powered using one of the following options:

+ **Power Adapter (12 V<sub>DC</sub> or 9~24 V<sub>DC</sub>, depending on your device)**

1. Connect the power adapter to the device.
2. Plug the other end of the adapter into a power outlet.

+ **Power over Ethernet (PoE)** *(Optional, PoE injector not included in the shipment)*

1. Connect an Ethernet cable to the device's **ETH(PoE)** port.
2. Ensure the PoE injector is properly connected and powered.

The **PWR LED** will turn on when the device is powered correctly.

### Key LED Indicators After Power On

| **LED**                                  | **Expected Status After Power-On**        | **Description**                                                                                                                                                                                                                                                                                   |
|------------------------------------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **PWR LED**                              | **ON (solid)**                            | Power is connected; the gateway is powered on.                                                                                                                                                                                                                                                    |
| **Breathing LED**                        | **Red (fast blinking)**                   | When the gateway is first powered on and not yet connected to the internet, the LED will show **red with a fast blink** to indicate a network issue.
 Once the gateway successfully connects to the internet, the LED will switch to **blue with a slow blink**, indicating normal operation. |
| **ETH LED** *(if Ethernet is connected)* | **ON / Flickering**                       | Ethernet port is active; data transmission may be occurring.                                                                                                                                                                                                                                      |
| **WLAN LED**                             | **ON / Flickering**                       | WiFi AP mode is active and functional.                                                                                                                                                                                                                                                           |
| **LoRa LED**                             | **ON / Flickering**                       | Indicates the LoRa transceiver is operational and handling packets.                                                                                                                                                                                                                               |
| **LTE LED** *(RAK7268CV2 only)*          | **Fast flickering or slow idle blinking** | LTE module is either transmitting data or searching for a network.                                                                                                                                                                                                                                |

:::tip NOTE
For more detailed LED behavior and additional indicators, refer to the [RAK7268V2/RAK7268CV2 Datasheet – LED Indicators.](https://docs.rakwireless.com/product-categories/wisgate/rak7268v2/datasheet/#led-indicators-details)
:::

### Access the Gateway

In this section, two methods of accessing the gateway are provided to offer different alternatives based on the availability of the required resources.

#### WiFi AP Mode

By default, the gateway will work in WiFi AP Mode which means that you can find an SSID named like **RAK7268V2_XXXX or RAK7268CV2_XXXX** on your PC's WiFi Network List. **XXXX** is the last two bytes of the Gateway MAC address.

> **Image:** Accessing the gateway via WiFi AP Mode

1. Connect to the gateway’s WiFi.

   :::tip NOTE
    No password is required to connect via WiFi.
   :::

2. Open a web browser and enter the IP address: `192.168.230.1`
3. On the first login, you must set a login password. The password must:
    - At least 12 characters long
    - Has at least one special character (`!“#$%&\‘()*+,-./:;<=>?@[]^_{|}~`)
    - Has at least one number
    - Has at least one standard Latin letter (used in the English alphabet)

> **Image:** Web UI login page

4. Click **Set password** to continue. You will be redirected to the **LoRaWAN Statistics** page.

> **Image:** LoRaWAN statistics page

5. For future logins, use the password you set. The default login username is **root**.

> **Image:** Login page with set password

#### WAN Port (Ethernet)

> **Image:** Access the gateway via WAN Port (Ethernet)

1. Connect the Ethernet cable from the gateway’s **ETH(PoE)** port to your PC’s Ethernet port.
2. Set a static IP address on your PC in the same subnet as the gateway:
   :::tip NOTE
   The default IP of the gateway is `169.254.X.X`, derived from the last 4 bits of the MAC address. For example, if the last 4 bits are `0F:01`, the gateway IP is `169.254.15.1`.
   Set your PC's IP address accordingly, e.g., `169.254.15.100`.
   :::
3. Open the **Internet Properties** of your PC, and select **Internet Protocol Version 4 (TCP/IPv4)**.

> **Image:** Internet properties

4. Select **Use the following IP address**, and set the PC’s IP address (e.g., `169.254.15.100`). Ensure the PC’s IP address is in the same subnet as the gateway (e.g., if the gateway IP is `169.254.15.1`, set the PC to `169.254.15.100`).

> **Image:** Set IP address of the PC

In this example, you can access the gateway on the `169.254.15.1` address.

5. In a web browser, enter the gateway's IP (e.g., `169.254.15.1`) to access the Web UI.
6. Set the login password following the same rules as in [WiFi mode](#wifi-ap-mode).
7. After setting the password, the LoRaWAN Statistics page will load.
8. Use the username `root` and your password for future logins.

### Access the Internet

The RAK7268V2/RAK7268CV2 WisGate Edge Lite 2 supports Ethernet and WiFi backhaul by default, while the RAK7268CV2 model additionally supports LTE. With the Multi-WAN failover feature, all available interfaces can be configured simultaneously, allowing the gateway to switch automatically to a backup when the primary connection fails.

- The gateway will automatically use the **highest-priority available connection**, and fall back to others as needed.
- The **default priority** is typically: **Ethernet > Wi-Fi > LTE** (if available), but this can be customized.
- To configure Multi-WAN behavior, refer to the [WisGateOS 2 User Manual > Network > WAN](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#change-priority).

:::tip NOTE
The examples in this section use the **DC 12V version** of the gateway as the reference model.
:::

#### Connect Through WiFi

> **Image:** Connect the internet via WiFi

1. Log in to the Web UI, go to **Network** > **WAN** > **Wi-Fi**.
2. Expand the WiFi section and click on **Settings**. Ensure the **Interface** is enabled.
3. Click the **Scan** button to select your **ESSID**, or manually enter the ESSID of the network by clicking **Enter network (E)SSID manually**.
4. Choose the correct **Encryption** method and enter the appropriate **Key**.
   :::tip NOTE
   Assuming you have entered the correct parameter values, you should receive an IP address assigned by your WiFi router's (AP) built-in DHCP server. You can use this new IP address to log in via a web browser.
   :::
   
> **Image:** WiFi settings

For details, refer to the <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#wi-fi" target="_blank">WisGateOS 2 User Manual > WAN > WiFi</a>.

#### Connect Through Ethernet

> **Image:** Access the Internet through Ethernet

1. Connect one end of an Ethernet cable to the gateway’s **ETH(PoE)** port, and the other end to your router.

:::tip NOTE
The router's DHCP server will automatically assign an IP address to the gateway. You can use this assigned IP to access the gateway via a web browser.
:::

> **Image:** Connect through Ethernet settings

If additional configuration is required, refer to the [WisGateOS 2 User Manual > WAN > Ethernet](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#ethernet).

:::tip NOTE
The gateway does not come with a PoE adapter by default. You can use one to power the gateway through Ethernet if needed, but it's optional.
:::

#### **Connect Through LTE (For LTE Version)**

If your gateway supports LTE and you have inserted the SIM card, the gateway will automatically connect to the cellular network once the SIM card is inserted.

1. If manual APN configuration is needed, go to **Network** > **WAN** > **Cellular** in the Web UI.
2. Expand the Cellular section and click on **Settings**.

> **Image:** Connect through cellular settings

3. For parameter configuration, refer to the [WisGateOS 2 User Manual > WAN > Cellular](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#cellular).

:::tip NOTE

Make sure that your SIM card is activated and supports data services.

:::

## Tutorials

In this section, you can browse tutorials about the RAK7268V2/RAK7268CV2 gateway to help you better understand and use the product.

| Tutorials                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <a href="https://www.youtube.com/watch?v=nt4duMB3qDo" target="_blank">Let’s go! Unboxing and placing your WisGate Edge Lite 2</a>                                                                                                                        |
| <a href="https://www.youtube.com/watch?v=yzgv2VCLb-8" target="_blank">It’s alive! Powering and accessing your WisGate Edge Lite 2</a>                                                                                                                    |
| <a href="https://learn.rakwireless.com/hc/en-us/articles/26688300221079-How-To-Use-the-MQTT-Broker-Like-a-Pro-Examples" target="_blank">Use the MQTT Broker Like a Pro + Examples</a>                                                                    |
| <a href="https://learn.rakwireless.com/hc/en-us/articles/26527371792535-How-To-Configure-WisGate-Edge-V2-Gateways-Remote-Management-OpenVPN">WisGate Edge V2 Gateways Remote Management - OpenVPN</a>                                                    |
| <a href="https://learn.rakwireless.com/hc/en-us/articles/26526970499735-How-To-Configure-ThingsBoard-with-MQTT-HTTP-Integrations-via-WisGateOS2" target="_blank">ThingsBoard Configuration with MQTT/HTTP Integrations via WisGateOS 2</a>               |
| <a href="https://learn.rakwireless.com/hc/en-us/articles/26688144537623-How-To-Install-OpenVPN-for-Ubuntu-Systems" target="_blank">OpenVPN Server Installation Guide (For Ubuntu sys)</a>                                                                |
| **IoT Solutions**                                                                                                                                                                                                                                        |
| <a href ="https://www.rakwireless.com/en-us/company/about/rakstar-success-story/metropolitan-wireless-international" target="_blank">LoRaWAN Based Temperature Monitoring System Provided by Metropolitan Wireless International (MWI) Using RAK7268</a> |
| <a href="https://www.rakwireless.com/en-us/company/about/rakstar-success-story/innovkez" target="_blank">Boosting Facility Management Efficiency with IoT Technology, a Solution by Innovkez</a>                                                         |
| <a href="https://www.rakwireless.com/en-us/company/about/rakstar-success-story/innovative-water-quality-monitoring-systems" target="_blank"> Water Quality Monitoring Systems for Fish Farming Businesses</a>                                            |

