---
slug: /product-categories/wisgate/rak7240v2/quickstart/
title: RAK7240V2/RAK7240CV2 WisGate Edge Prime Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK7240V2. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Gateway.
image: "https://images.docs.rakwireless.com/wisgate/rak7240-v2/rak7240v2.png"
keywords:
  - RAK7240v2
  - RAK7240CV2
  - wisgate
  - quickstart
sidebar_label: Quick Start Guide
---

# RAK7240V2/RAK7240CV2 WisGate Edge Prime Quick Start Guide

This manual provides brief instructions for installing and deploying the gateway.

## Prerequisites

### Hardware

1. <a href="https://store.rakwireless.com/products/wisgate-edge-prime-rak7240v2-rak7240cv2?utm_source=WisGateRAK7240CV2&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">**RAK7240V2/RAK7240CV2 WisGate Edge Prime**</a>
2. <a href="https://store.rakwireless.com/products/ethernet-cable-gland?utm_source=EthernetCableGland&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">**Ethernet Cable**</a> (RJ-45 Port) for Ethernet connection
3. A Windows/MacOS/Linux Computer
4. Installation Accessories (e.g., mounting kit, power supply, screws, etc.)
5. **NanoSIM Card** (for LTE version): If you're using the cellular version of the gateway, ensure you have a SIM card ready for installation. **Size:** 12 mm x 9 mm x 0.67 mm.

### Package Inclusion

**Variant with DC Input Interface**

> **Image:** RAK7240V2/RAK7240CV2 package list 1

**Variant without DC Input Interface**

> **Image:** RAK7240V2/RAK7240CV2 package list 2

:::tip NOTE
+ LoRa® antenna is **not included** and must be purchased separately.
+ LTE antennas are included **only** with **8-channel cellular models (RAK7240CV2)**.
:::

## Installation

### Insert SIM Card *(For cellular models only: RAK7240CV2)*

:::warning
The SIM card slot of the cellular versions is not hot-swappable. Make sure the gateway is switched off before inserting or ejecting the SIM card.
:::

1. Start by unscrewing the cap of the NanoSIM interface on the gateway enclosure to expose the SIM card slot.

> **Image:** Unscrewing the cap of the NanoSIM interface

2. Push the SIM card into the card slot according to the placement method marked on the interface.

> **Image:** Inserting the SIM card

3. Once completed, screw back the metal cap. Make sure it is tightly screwed.

> **Image:** Screwing back the metal cap

### Mount the Gateway

1. Fix the installation kit at the bottom of the device with four M5 x 8 mm screws.

> **Image:** Fixing the installation kit to the RAK7240V2/RAK7240CV2

2. Slide the steel band clamps through the rectangular hole of the installation kit. Wrap the band clamps around the pole, lock them, and then tighten the clamps using a screwdriver.

> **Image:** Fixing the RAK7240V2/RAK7240CV2 to a Pole

### Install Antennas and Cables

1. Attach the LoRa®, Wi-Fi, and GPS antennas. If you're using a cellular model, connect the LTE antennas as well.
2. **(Optional)** If you plan to use PoE for power or Ethernet for network connectivity, you may now connect an Ethernet cable to the gateway's ETH (PoE) port.

#### Lightning Protection (Recommended)

:::warning
Lightning strikes can generate powerful electrical surges that may harm sensitive electronic devices. It is essential to take appropriate precautions to minimize the risk of damage. The warranty provided does not cover damages resulting from lightning strikes or other acts of nature.
:::

To ensure optimal performance and protect your equipment from potential damage, it is strongly recommended to install proper **grounding** and **lightning protection** for:
+ All **antenna connectors** (LoRa®, GPS, Wi-Fi, LTE)
+ The **ETH(PoE)** port
+ The gateway enclosure

> **Image:** Full lightning protection set-up

##### Outdoor Surge Protection System

- **Antenna Grounding**

  Install a lightning arrestor on each antenna's N-type terminal (LoRa®, LTE, Wi-Fi, GPS). The arrestors must be N-type Female to Male to match the antenna and enclosure connectors.
  Use **10 AWG or thicker** grounding wire to connect the arrestor's screw terminal to the **grounding rail mounted on the building wall** or a **grounding bar** in field deployments.
- **Gateway Grounding**

  Connect the grounding screw located on the bottom side of the gateway to the same grounding rail or bar using a **10 AWG or thicker** wire. This ensures proper discharge path for any electrical surges through the gateway chassis.

##### Indoor Surge Protection

To protect **indoor devices** connected to the gateway (e.g., PoE injectors, switches, routers), install an **Ethernet SPD (Surge Protection Device)** along the cable between the gateway and the PoE injector.

##### Recommended Equipment

- <a href="https://store.rakwireless.com/products/lightning-arrestor-for-gps-antenna" target="_blank">Lightning Arrestor for GPS Antenna</a>: A surge protection device designed specifically for GPS antennas. It uses a high-pass filter to block low-frequency lightning-induced interference while maintaining minimal insertion loss for GPS signals. The device integrates a **TVS diode** and **gas discharge tube (GDT)** to protect the DC feed circuit from transients and over-voltage events.
- <a href="https://store.rakwireless.com/products/lightning-arrestor" target="_blank">Lightning arrestor for the LoRa, LTE and Wi-Fi antennas</a>: This is a surge protection device for securing transceivers against over-voltage and surge current induced by lightning bolts. RAKwireless recommends installing lightning arrestors on all N-type antenna terminals, including LTE and 2.4G Wi-Fi antennas.
- <a href="https://store.rakwireless.com/products/signal-surge-protective?variant=29842390122541?utm_source=signalsurgeprotectivedevice&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">Signal Surge Protective Device</a>: Designed for **CAT6 or Class E network cables**, this SPD protects Ethernet-connected equipment from voltage surges induced by lightning or internal switching transients. It is widely used in industrial and office communication systems, including **Gigabit Ethernet**, **ATM**, **ISDN**, and **VoIP**.

#### Weather Protection

To better protect the Ethernet cable gland and the antenna connector from the weather, cover them with PVC tape.
1. Clean the surface area of the connector that will be wrapped. Wrap a layer of PVC tape with a 50% overlap according to the rotation direction of the connector. Continue wrapping the PVC tape to about 10 mm below the end of the connector.

> **Image:** Wrapping with PVC tape

2. Cut off about 50 cm waterproof tape. Stretch it to double its length and wrap three layers around the connector with a 50% overlap. Hold the tape in place with your hand for a few seconds.

> **Image:** Wrapping with waterproof tape

3. Wrap three additional layers with PVC tape with natural uncoiling force and a 50% overlap. Ensure to cover the head and the tail of the connector.

> **Image:** Final PVC wrapping

## Power On the Gateway

:::warning
Do not power the device if any antenna port has been left open. In case you do not desire to use one or more antenna features, make sure to terminate the port with a **50 Ω load**.
:::

Your gateway supports multiple power input options depending on the model variant:

### PoE (Power over Ethernet)

1. Connect the Ethernet cable from the gateway's **ETH (PoE)** port into the PoE output port of the injector.
2. Plug the injector into a power outlet to power up the gateway.
   
> **Image:** Powering the gateway using PoE

### DC Power Input (9\~24 V<sub>DC</sub>)

The gateway includes a pre-terminated DC power cable, designed for direct connection with RAK Battery Plus.

To use RAK Battery Plus, simply connect the included DC power cable between the battery and the gateway's DC input port.

> **Image:** Powering the gateway using RAK Battery Plus

:::tip NOTE
<a href="https://store.rakwireless.com/products/rak-battery-plus-rak9155?variant=42309251563718" target="_blank">RAK9155 Battery Plus</a> is not included in the bundle, it needs to be purchased separately.
:::

If you're using your own 9\~24 V<sub>DC</sub> power supply, you may trim the open end of the cable and connect the wires to your power source.

Polarity:
  - Red wire = Positive (+)
  - Black wire = Negative (–)

:::warning
Use caution when trimming and wiring. Incorrect polarity may damage the gateway and void the warranty.
:::

## Access the Gateway

In this section, two methods of accessing the gateway are provided to offer different alternatives based on the availability of the required resources.

### Wi-Fi AP Mode

By default, the gateway will work in Wi-Fi AP Mode which means that you can find an SSID named like **RAK7240V2_XXXX** or **RAK7240CV2_XXXX** on your PC's Wi-Fi Network List. **XXXX** is the last two bytes of the Gateway MAC address.

> **Image:** Accessing the gateway via Wi-Fi AP Mode

1. Connect to the gateway's Wi-Fi.
   :::tip NOTE
   No password is required to connect via Wi-Fi.
   :::
2. Open a web browser and enter the IP address: `192.168.230.1`.
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

### WAN Port (Ethernet)

To access the gateway through the ETH (PoE) port, make sure you have completed the steps defined in the [Install Antennas and Cables](#install-antennas-and-cables) section.

> **Image:** Accessing the gateway via WAN Port (Ethernet)

1. Connect one end of another Ethernet cable to the LAN port on the PoE adapter, and the other end to your PC.
2. Set a static IP address on your PC in the same subnet as the gateway:
   :::tip NOTE
   The default IP is **169.254.X.X**. The last two segments(X.X) are mapped from the last four bits of the MAC address of your gateway. For example, the last four bits of the MAC address are `0F:01`, and the IP address is `169.254.15.1`. Make sure to manually set the address of your PC to one in the same network (for example, `169.254.15.100`).
   :::
3. Open the **Internet Properties** of your PC, and select **Internet Protocol Version 4 (TCP/IPv4)**.

> **Image:** Internet properties

4. Select **Use the following IP address**, and set the PC's IP address (e.g., `169.254.15.100`). Ensure the PC's IP address is in the same subnet as the gateway (e.g., if the gateway IP is `169.254.15.1`, set the PC to `169.254.15.100`).

> **Image:** Setting IP address of the PC

In this example, you can access the gateway on the `169.254.15.1` address.

5. In a web browser, enter the gateway's IP (e.g., `169.254.15.1`) to access the Web UI.
6. Set the login password following the same rules as in [Wi-Fi mode](#wi-fi-ap-mode).
7. After setting the password, the LoRaWAN Statistics page will load.
8. Use the username `root` and your password for future logins.

## Access the Internet

You can connect the gateway to the internet through Wi-Fi, Ethernet, or LTE (for LTE models).

### Connect Through Wi-Fi

> **Image:** Accessing the Internet via Wi-Fi

1. Log in to the Web UI, go to **Network** > **WAN** > **Wi-Fi**.
2. Expand the Wi-Fi section and click on **Settings**. Ensure the **Interface** is enabled.
3. Click the **Scan** button to select your **ESSID**, or manually enter the ESSID of the network by clicking **Enter network (E)SSID manually**.
4. Choose the correct **Encryption** method and enter the appropriate **Key**.
   :::tip NOTE
   Assuming you have entered the correct parameter values, you should receive an IP address assigned by your Wi-Fi router's (AP) built-in DHCP server. You can use this new IP address to log in via a web browser (the same way as in AP mode).
   :::
   For details, refer to the [**WisGateOS 2 User Manual** > **WAN** > **Wi-Fi**](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#wi-fi).

> **Image:** Wi-Fi settings

### Connect Through Ethernet/PoE

To access the Internet through the ETH (PoE) port, make sure you have completed the steps defined in the [Install Antennas and Cables](#install-antennas-and-cables) section.

> **Image:** Accessing the Internet through Ethernet

1. Connect the LAN port of the PoE injector to your route. The router's DHCP server should assign an IP address to the gateway.

:::tip
The router's DHCP server will automatically assign an IP address to the gateway. You can use this assigned IP to access the gateway via a web browser.
:::

> **Image:** Default settings

If additional configuration is required, refer to the [**WisGateOS 2 User Manual** > **WAN** > **Ethernet**](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#ethernet).

### Connect Through Cellular

If your gateway supports LTE and you have inserted the SIM card, the gateway will automatically connect to the cellular network once the SIM card is inserted.

1. If manual APN configuration is needed, go to **Network** > **WAN** > **Cellular** in the Web UI.
2. Expand the Cellular section and click on **Settings**.
   
> **Image:** Cellular Interface Page

For parameter configuration, refer to the [**WisGateOS 2 User Manual** > **WAN** > **Cellular**](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#cellular).

## Tutorials

In this section, you can browse tutorials about the RAK7240V2/RAK7240CV2 gateway to help you better understand and use the product.

| Tutorials                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <a href="https://www.youtube.com/watch?v=G2AxL5r9w_U" target="_blank">Fiberglass Antenna Mounting Solution for Outdoor Setup - Outdoor LoRaWAN Gateway, RAK9731</a>                                                                        |
| <a href="https://learn.rakwireless.com/hc/en-us/articles/26688300221079-How-To-Use-the-MQTT-Broker-Like-a-Pro-Examples" target="_blank">Use the MQTT Broker Like a Pro + Examples</a>                                                      |
| <a href="https://learn.rakwireless.com/hc/en-us/articles/26527371792535-How-To-Configure-WisGate-Edge-V2-Gateways-Remote-Management-OpenVPN" target="_blank">WisGate Edge V2 Gateways Remote Management - OpenVPN</a>                      |
| <a href="https://learn.rakwireless.com/hc/en-us/articles/26526970499735-How-To-Configure-ThingsBoard-with-MQTT-HTTP-Integrations-via-WisGateOS2" target="_blank">ThingsBoard Configuration with MQTT/HTTP Integrations via WisGateOS 2</a> |
| <a href="https://learn.rakwireless.com/hc/en-us/articles/26688144537623-How-To-Install-OpenVPN-for-Ubuntu-Systems" target="_blank">OpenVPN Server Installation Guide (For Ubuntu sys)</a>                                                  |

