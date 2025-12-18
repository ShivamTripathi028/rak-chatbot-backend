---
slug: /product-categories/wisgate/rak7266/quickstart/
title: RAK7266 WisGate Soho Lite Guide
description: Step-by-step instructions for installing and deploying the RAK7266 WisGate Soho Lite gateway, including setup, configuration, and mounting options.
image: "https://images.docs.rakwireless.com/wisgate/rak7266/rak7266.png"
keywords:
  - Indoor gateway
  - 8 Channel gateway
  - RAK7266 manual
  - WisGate Soho Lite guides
  - LoRaWAN gateway setup
  - build IoT gateway
sidebar_label: Quick Start Guide
tags:
  - rak7266
  - wisgate
  - quickstart
date: 2026-06-26
---

# RAK7266 WisGate Soho Lite Quick Start Guide

This manual provides brief instructions for installing and deploying the gateway.

## Prerequisites

+ <a href="https://store.rakwireless.com/products/wisgate-soho-lite-lorawan-gateway-rak7266?utm_source=docs_center&utm_medium=organic&utm_campaign=rak7266-documentation-quickstart-page&utm_term=rak7266_wisgate_soho_lite&utm_content=store_link" target="_blank">RAK7266 WisGate Soho Lite</a>
+ [Ethernet Cable](https://store.rakwireless.com/products/ethernet-cable-gland?utm_source=docs_center&utm_medium=organic&utm_campaign=rak7266-documentation-quickstart-page&utm_term=ethernet-cable&utm_content_store-link) (RJ-45 Port): Required if you plan to use Ethernet as a wired backhaul or for initial configuration.
+ A Windows/MacOS/Linux Computer
+ Installation Accessories (e.g., mounting kit, power supply, screws, etc.)
+ **NanoSIM Card** – **Size:** 12 mm x 9 mm x 0.67 mm.

### Package Inclusion

+ 1 × Gateway
+ 1 × LoRa Antenna
+ 1 × LTE Antenna *(only for external LTE antenna models)*
+ 1 × Power Supply
+ 1 × Mounting Bracket

> **Image:** RAK7266 package contents

:::tip NOTE

+ The power adapter shown in the **Figure 1** is for reference only. The actual adapter included in the package may vary depending on the selected bundle.
+ **Figure 1** shows the **external LTE antenna version** of RAK7266.
  For models with **built-in LTE antenna**, the LTE antenna is integrated into the enclosure, and no separate LTE antenna is included in the box.

:::

## Gateway Installation Guide

:::warning
- **DO NOT** eject the SD card located in the SD card slot during installation, as it stores logs and data essential for the device's performance.
- The SIM card slot of the cellular versions is not hot-swappable. Make sure the gateway is switched off before inserting or ejecting the SIM card.
:::

### Insert SIM Card

1. On the **back** of the gateway, locate the **NanoSIM card slot**.

> **Image:**  Inserting SIM card

2. Insert the **NanoSIM card** into the slot, ensuring it is properly inserted.

### Mount the Bracket

The gateway can be mounted in multiple ways: wall-mounting, ceiling-mounting, or using a rail. Choose the appropriate mounting style based on your environment and needs.

#### Wall Mounting

1. Use a **5-mm drill bit** to drill three holes on the wall where you want to mount the gateway. It’s recommended to mark the hole positions before drilling to ensure accurate placement.
2. Insert the expansion plugs into the drilled holes.
3. Secure the mounting bracket to the wall using screws through the bracket holes.

> **Image:**  Mounting bracket

#### Ceiling Mounting

:::tip NOTE
For ceiling mounting, ensure the ceiling is strong enough to support the gateway. Mark the hole positions before drilling.
:::

1. Choose either self-tapping screws or expansion tubes with self-tapping screws to install the bracket, depending on the material of the ceiling.
2. (Optional) Refer to this step when installing the bracket using expansion tubes and self-tapping screws. Otherwise, skip it.
  - Use a 5 mm drill bit to drill 3 holes in the ceiling.
  - Insert the expansion tubes into the holes drilled in the ceiling.
3. Secure the bracket to the ceiling using self-tapping screws through the holes in the bracket.

> **Image:**  Mounting bracket

#### T-Shaped Keel Mounting

You can use a T-shaped keel for mounting the bracket on a rail system. The following instructions apply to a T-shaped keel, but other types of rails can also be used.

:::tip NOTE
The bracket supports rail widths of 14 mm, 16 mm, and 24 mm.
:::

1. Remove the mounting clip from the bracket.
2. Insert one side of the T-shaped keel into the two clips of the bracket.
3. Insert the two T-shaped hooks on the mounting clip into the T-shaped rails of the bracket, slide the mounting clip to the other side of the T-shaped keel, and make sure the clip is in place.

> **Image:**  Mounting bracket

### Install the Gateway

1. Align the lower edge of the gateway's hanging hole with the bracket's locking plate.
2. Move the gateway closer to the bracket until the bracket's locking plate engages with the gateway's hanging hole.
3. Pull the gateway to ensure that the gateway is in place.

> **Image:** Fixed gateway

### Attach the Antenna

1. **LoRa Antenna**

    Attach the **LoRa antenna** by screwing it onto the connector labeled **LoRa** on the gateway.
2. **LTE Antenna**

    Screw the **LTE antenna** onto the connector labeled **MAIN** to ensure optimal cellular performance.

### Power On and Status Verification

#### Power the Gateway

:::warning
**DO NOT** power the device if any antenna port (LoRa or LTE) has been left open to avoid potential damage to the RAK7266 WisGate Soho Lite.
:::

The **RAK7266 WisGate Soho Lite** can be powered via a **12 V<sub>DC</sub> power adapter** (included in the product package).

1. Connect the power adapter to the **12 V<sub>DC</sub>** jack on the gateway.
2. Plug the other end of the adapter into a power outlet.

#### Startup Status Checklist

To verify if the gateway is operating normally after powering on, check the following:

| **LED**                                  | **Expected Status After Power-On**            | **Description**                                                                                                                                                                                                                                                                                   |
| ---------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PWR LED**                              | **ON (solid)**                                | Power is connected; the gateway is powered on.                                                                                                                                                                                                                                                    |
| **Breathing LED**                        | **Red (fast blinking)**                       | When the gateway is first powered on and not yet connected to the internet, the LED will show **red with a fast blink** to indicate a network issue.
 Once the gateway successfully connects to the internet, the LED will switch to **blue with a slow blink**, indicating normal operation. |
| **ETH LED** *(if Ethernet is connected)* | **ON / Flickering**                           | Ethernet port is active; data transmission may be occurring.                                                                                                                                                                                                                                      |
| **WLAN LED**                             | **ON / Flickering**                           | WiFi AP mode is active and functional.                                                                                                                                                                                                                                                           |
| **LoRa LED**                             | **ON / Flickering**                           | Indicates the LoRa transceiver is operational and handling packets.                                                                                                                                                                                                                               |
| **LTE LED**                              | **Fast flickering or slow idle blinking**     | LTE module is either transmitting data or searching for a network.                                                                                                                                                                                                                                |

:::tip NOTE
For more detailed LED behavior and additional indicators, refer to the [RAK7266 Datasheet LED Indicators](https://docs.rakwireless.com/product-categories/wisgate/rak7266/datasheet/#led-indicators-details).
:::

## Access the Gateway

In this section, two methods of accessing the gateway are provided to offer different alternatives based on the availability of the required resources.

#### WiFi AP Mode

By default, the gateway will work in WiFi AP Mode which means that you can find an SSID named like **RAK7266_XXXX** on your PC's WiFi network list. **XXXX** is the last two bytes of the gateway's MAC address.

> **Image:** Accessing the gateway via WiFi AP Mode

1. Connect to the gateway’s WiFi.
   :::tip NOTE
    No password is required to connect via WiFi.
   :::
2. Open a web browser and enter the IP address: `192.168.230.1`
3. On the first login, you must set a login password. The password must meet the following requirements:
    - At least 12 characters long
    - Has at least one special character (`!“#$%&\‘()*+,-./:;<=>?@[]^_{|}~`)
    - Has at least one number
    - Has at least one standard Latin letter (used in the English alphabet)

> **Image:** Web UI login page

4. Click **Set password** to continue. You will be redirected to the **LoRaWAN Statistics** page.

> **Image:** LoRaWAN statistics page

5. On the next login, use the password you set. The default login username is **root**.

> **Image:** Login page with set password

#### WAN Port (Ethernet)

> **Image:** Accessing the gateway via WAN Port (Ethernet)

1. Connect the Ethernet cable from the gateway’s **ETH** port to your PC’s Ethernet port.
2. Set a static IP address on your PC in the same subnet as the gateway:
   :::tip NOTE
   The default IP of the gateway is `169.254.X.X`, derived from the last 4 bits of the MAC address. For example, if the last 4 bits are `0F:01`, the gateway IP is `169.254.15.1`.
   Set your PC's IP address accordingly, e.g., `169.254.15.100`.
   :::
3. Open the **Internet Properties** of your PC, and select **Internet Protocol Version 4 (TCP/IPv4)**.

> **Image:** Internet properties

4. Select **Use the following IP address**, and set the PC’s IP address (e.g., `169.254.15.100`). Ensure the PC’s IP address is in the same subnet as the gateway (e.g., if the gateway IP is `169.254.15.1`, set the PC to `169.254.15.100`).

> **Image:** Setting IP address of the PC

In this example, you can access the gateway on the `169.254.15.1` address.

5. In a web browser, enter the gateway's IP (e.g., `169.254.15.1`) to access the Web UI.
6. Set the login password following the same rules as in [WiFi mode](#wifi-ap-mode).
7. After setting the password, the LoRaWAN Statistics page will load.
8. Use the username `root` and your password for future logins.

## Access the Internet

The RAK7266 WisGate Soho Lite supports LTE, WiFi, and Ethernet backhaul. With the Multi-WAN failover feature, all can be configured simultaneously, allowing the gateway to switch automatically to a backup when the primary connection fails.

- The gateway will automatically use the **highest-priority available connection**, and fall back to others as needed.
- The **default priority** is typically: **Ethernet** > **WiFi** > **LTE**, but this can be customized.
- To configure Multi-WAN behavior, refer to the [WisGateOS 2 User Manual > Network > WAN](hhttps://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/?intsource=docs_center&intmedium=organic&intcampaign=rak7266_documentation_quickstart_page&intterm=wisgateos2_user_manual_network_wan&intcontent=documentation_link#change-priority).

#### Connect Through WiFi

> **Image:** Connect the internet via WiFi

1. Log in to the Web UI, go to **Network** > **WAN** > **WiFi**.
2. Expand the WiFi section and click on **Settings**. Ensure the **Interface** is enabled.
3. Click the **Scan** button to select your **ESSID**, or manually enter the ESSID of the network by clicking **Enter network (E)SSID manually**.
4. Choose the correct **Encryption** method and enter the appropriate **Key**.

   :::tip NOTE
   Assuming you have entered the correct parameter values, you should receive an IP address assigned by your WiFi router's (AP) built-in DHCP server. You can use this new IP address to log in via a web browser.
   :::

> **Image:** WiFi settings

For details, refer to the <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/?intsource=docs_center&intmedium=organic&intcampaign=rak7266_documentation_quickstart_page&intterm=wisgateos2_user_manual_wan_wifi&intcontent=documentation_link#wi-fi" target="_blank">WisGateOS 2 User Manual > WAN > Wi-Fi</a>.

#### Connect Through Ethernet

> **Image:** Accessing the Internet through Ethernet

1. Connect one end of an Ethernet cable to the gateway’s **ETH** port, and the other end to your router.

:::tip NOTE
The router's DHCP server will automatically assign an IP address to the gateway. You can use this IP to access the gateway via a web browser.
:::

> **Image:** Connect through Ethernet settings

If additional configuration is required, refer to the [WisGateOS 2 User Manual > WAN > Ethernet](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/?intsource=docs_center&intmedium=organic&intcampaign=rak7266_documentation_quickstart_page&intterm=wisgateos2_user_manual_complete_guide_for_lorawan_gateway_software&intcontent=documentation_link#ethernet).

#### Connect Through LTE

The RAK7266 WisGate Soho Lite includes built-in LTE support and will typically connect to the cellular network automatically once a valid SIM card is inserted.
However, in some regions, **manual APN configuration** may be required depending on your mobile operator.
To manually configure APN and other LTE settings:

1. Log in to the Web UI and navigate to **Network > WAN > Cellular**.
2. Expand the Cellular section and click on **Settings**.
3. Enter the required **APN**, **username**, **password**, and **PIN code** if provided by your mobile operator.

> **Image:** Connect through cellular settings

For details on each parameter, refer to the [WisGateOS 2 User Manual > WAN > Cellular](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/?intsource=docs_center&intmedium=organic&intcampaign=rak7266_documentation_quickstart_page&intterm=wisgateos2_user_manual_wan_cellular&intcontent=documentation_link#cellular).

:::tip NOTE

Make sure that your SIM card is activated and supports data services.

:::

