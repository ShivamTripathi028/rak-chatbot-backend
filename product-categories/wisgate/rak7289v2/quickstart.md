---
title: RAK7289V2/RAK7289CV2 WisGate Edge Pro V2 Guide
description: Step-by-step installation guide for RAK7289V2 and RAK7289CV2 WisGate Edge Pro gateways. Learn SIM setup, PoE, Wi-Fi, and lightning protection options.
image: "https://images.docs.rakwireless.com/wisgate/rak7289v2-rak7289cv2/rak7289v2.png"
keywords:
    - RAK7289V2
    - WisGate Edge Pro V2 Guide
    - LoRaWAN gateway setup
sidebar_label: Quick Start Guide
---

# RAK7289V2/RAK7289CV2 WisGate Edge Pro V2 Quick Start Guide

This manual provides brief instructions for installing and deploying the gateway.

## Prerequisites

### Hardware

+ <a href="https://store.rakwireless.com/products/wisgate-edge-pro-rak7289v2-rak7289cv2?utm_source=WisGateRAK7289V2&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">**RAK7289V2/RAK7289CV2 WisGate Edge Pro**</a>
+ <a href="https://store.rakwireless.com/products/ethernet-cable-gland?utm_source=EthernetCableGland&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">Ethernet Cable</a> (RJ-45 Port) for Ethernet connection
+ A Windows/Mac OS/Linux Computer
+ Installation Accessories (e.g., mounting kit, power supply, screws, etc.)
+ **NanoSIM Card** (for LTE version) – If you're using the cellular version of the gateway, ensure you have a SIM card ready for installation. **Size:** 12 x 9 x 0.67 mm.

### Package Inclusion

> **Image:** RAK7289V2/RAK7289CV2 package list

:::tip NOTE
The LoRa antennas are not included. They need to be bought separately one for the 8-channel gateway and two for the 16-channel one.
:::

## Product Configuration

### Gateway Installation Guide

This section provides the instructions on mounting and securing the mounting kit to the enclosure and the mounting pole.

#### Insert SIM Card

If you will use the cellular variant of the gateway, you can refer to this section. Otherwise, skip it.

:::warning

The SIM card slot of the cellular versions is not hot-swappable. Make sure the gateway is switched off before inserting or ejecting the SIM card.
:::

1.  Start by unscrewing the cap of the NanoSIM interface on the gateway enclosure to expose the SIM card slot.

> **Image:** Unscrewing the cap of the NanoSIM interface

2. Push the SIM card into the card slot according to the placement method marked on the interface.

> **Image:** Inserting the SIM card

3. Once completed, screw back the metal cap. Make sure it is tightly screwed.

#### Mounting

1. Fix the bracket included in the mounting kit on the bottom of the enclosure with four M6*12 screws.

> **Image:** Mounting the bracket to the enclosure

2. Position the pole clamps together around the pole, then tighten them with bolts, washers, and nuts.

> **Image:** Mounting the clamps to a pole

:::tip NOTE

The diameter of the pole that is supported by the brackets is 50-100 mm. If the pole diameter is more than this value, hose clamps can be used. The standard mounting kit does not include hose clamps. If needed, they should be purchased separately.

The clamp's back also has openings for hose clamps that are not included in the mounting kit.

:::

> **Image:** Mounting using hose clamps

3. Mount the enclosure and secure it to the bracket.

   
> **Image:** Fastening the enclosure to the bracket

  - **Hang** the enclosure on the pre-installed mounting hook (①).
  - Use the **adjustment screw** (②) to fine-tune the vertical angle of the gateway. This allows you to correct any tilt caused by the enclosure‘s draft angle or pole misalignment, ensuring that the antenna is perfectly vertical.
  - Once the alignment is complete, **secure the enclosure** by tightening the two M6×12 screws (③).

#### Attach the Antennas

Attach the LoRa antenna(s). You need to attach one LoRa antenna for the 8-channel gateway, or two LoRa antennas for the 16-channel gateway.

> **Image:** RAK7289V2/RAK7289CV2 with attached antennas

#### Connect the PoE Adapter

If you choose to power the gateway via PoE or access the gateway and internet via the ETH port, you need to refer to this section. Otherwise, skip it.

Connect one end of the Ethernet cable (Cat5e or better) to the **ETH(PoE)** port on the gateway and the other end to the **PoE** port of the PoE injector.

### Weather Protection

To better protect the Ethernet cable gland and the antenna connector from the weather, you need to cover them with PVC tape.

1. Clean the surface area of the connector that will be wrapped. Wrap a layer of PVC tape with a 50% overlap according to the rotation direction of the connector. Continue wrapping the PVC tape to about 10 mm below the end of the connector.

> **Image:** Wrapping with PVC tape

2. Cut off about 50 cm waterproof tape. Stretch it to double the length. Wrap three layers around the connector with a 50% overlap. Hold the tape in place with your hand for a few seconds.

> **Image:** Wrapping with waterproof tape

3. Wrap three additional layers with PVC tape with natural uncoiling force and a 50% overlap. Ensure to cover the head and the tail of the connector.

> **Image:** Final PVC wrapping

### Lightning Protection

This section covers the installation of the lightning surge protection system when deploying the RAK7289V2/RAK2789CV2 gateway, both outdoors and indoors. Such a protection system must be taken into consideration to ensure a fully functional gateway without interruptions or damage from lightning..

> **Image:** Full lightning protection set-up

#### Outdoor Surge Protection System

- **Antenna Grounding**: RAKwireless recommends installing a lightning arrestor on all the antenna N-type terminals. The arrestors must be N-type Female to Male to fit the antenna and enclosure connectors. Ensure you use a 10 AWG or better wire to connect the screw terminals of the arrestors to the grounding rail mounted on the building wall (grounding bar in the case of field deployment).
- **Gateway Grounding**: Additionally, it is recommended to use another 10 AWG or better grounding wire to connect the screw terminal on the bottom-left side of the gateway casing to the grounding rail (bar).

:::tip NOTE
No additional protection for the Ethernet cabling is required on the gateway side. It already has a built-in surge protection system (GDT + Anti-surge resistor).
:::

#### Indoor Surge Protection

For protecting the indoor equipment and circuitry connected to the gateway, it is recommended to install an Ethernet port SPD lightning arrestor. This device should be positioned along the cabling that connects the gateway to the PoE injector. Make sure you connect its grounding wire terminal to an appropriate building grounding point.

:::warning

Should you fail to adhere to the recommendations in this document, RAKwireless carries no responsibility for any damage your equipment incurs due to a lightning strike.

:::

#### Recommended Equipment

- <a href="https://store.rakwireless.com/products/lightning-arrestor" target="_blank">Lightning Arrestor for the LoRa Antennas</a>: This surge protective device safeguards transceivers against over-voltage and surge current induced by lightning strikes. RAKwireless recommends installing a lightning arrestor on all LoRa N-type antenna terminals.

- <a href="https://store.rakwireless.com/products/pulsar-cable-rak9731-rak9733?variant=39677580968134" target="_blank">Pulsar cable RAK9731</a>: The RAK9731 Pulsar cable is utilized for lightning protection with the RAK7289V2/RAK7289CV2. This cable features an N-Type Male to N-Type Female configuration and is available in custom lengths of 1.5 m, 3 m, 5 m, 10 m, or longer. It is constructed with LMR-400 coaxial cable and N-type connectors.

- [Signal Surge Protective Device:](https://store.rakwireless.com/products/signal-surge-protective?variant=29842390122541) This device is designed to protect Category 6 or Class E cables, safeguarding equipment from surge and over-voltage events caused by lightning or internal system factors. It finds extensive application in office and industrial network wiring projects, as well as telecommunications setups including Gigabit Ethernet, ATM, ISDN, and VoIP systems.

- [Ethernet Cabling:](https://store.rakwireless.com/products/cat5-ethernet-cable) For outdoor surge protection systems, a CAT5 Ethernet Cable is recommended. It serves to establish connections between the PoE injector, Ethernet SPD, router/switch, and the Ethernet/PoE port on RAK7289.

### Power On the Gateway

:::warning

Do not power the device if any antenna port has been left open.

:::

The gateway supports multiple power supply options. Connect the gateway to the appropriate power source based on your needs.

**Power Cord + PoE Adapter**: The gateway is powered via PoE, make sure you have completed the steps defined in [Connect the PoE Adapter](#connect-the-poe-adapter) section.

1. Connect one end of the power cord to the PoE adapter.
2. Connect the other end of power cord to a power outlet, your gateway can be powered on.

> **Image:** Powering the gateway using PoE

**DC Cable**: The gateway is powered by an external DC power supply. You need to use the DC cable to connect an external power supply. The external power supply voltage range:  12 V<sub>DC</sub>.

> **Image:** Powering the gateway using external DC power supply

The gateway also supports **RAK9155 Battery Plus** as its power supply. <a href="https://store.rakwireless.com/products/rak-battery-plus-rak9155?variant=42309251563718" target="_blank">RAK9155 Battery Plus</a> need to be purchased separately.

### Access the Gateway

In this section, two methods of accessing the gateway are provided to offer different alternatives based on the availability of the required resources.

#### Wi-Fi AP Mode

By default, the gateway will operate in Wi-Fi AP Mode. This means that you can find an SSID named **"RAK7289V2_XXXX or RAK7289CV2_XXXX"** on your PC's Wi-Fi Network List, where **"XXXX"** represents the last two bytes of the Gateway MAC address.

> **Image:** Accessing the gateway via Wi-Fi AP Mode

1. Connect to the gateway’s Wi-Fi.

   :::tip NOTE
    No password is required to connect via Wi-Fi.
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

> **Image:** Login Page with set password

#### WAN Port (Ethernet)

To access the gateway through the ETH (PoE) port, make sure you have completed the steps defined in the [Connect the PoE Adapter](#connect-the-poe-adapter) section.

> **Image:** Accessing the gateway via WAN Port (Ethernet)

1. Connect one end of another Ethernet cable to the LAN port on the PoE adapter, and the other end to your PC.
2. Set a static IP address on your PC in the same subnet as the gateway:

:::tip NOTE
The default IP of the gateway is `169.254.X.X`, derived from the last 4 bits of the MAC address. For example, if the last 4 bits are `0F:01`, the gateway IP is `169.254.15.1`.
Set your PC's IP address accordingly, e.g., `169.254.15.100`.

:::

3. Open the **Internet Properties** of your PC, and select **Internet Protocol Version 4 (TCP/IPv4)**.

> **Image:** Internet properties

4. Select **Use the following IP address**, and set the PC’s IP address (e.g., `169.254.15.100`). Ensure the PC’s IP address is in the same subnet as the gateway (e.g., if the gateway IP is `169.254.15.1`, set the PC to `169.254.15.100`).

> **Image:** Setting IP address of the PC

5. In a web browser, enter the gateway's IP (e.g., `169.254.15.1`) to access the Web UI.

6. Set the login password following the same rules as in [Wi-Fi mode](#wi-fi-ap-mode).

7. After setting the password, the LoRaWAN Statistics page will load.

8. Use the username `root` and your password for future logins.

### Access the Internet

You can connect the gateway to the internet through Wi-Fi, Ethernet, or LTE (for LTE models).

#### Connect Through Wi-Fi

> **Image:** Accessing the Internet via Wi-Fi

1. Log in to the Web UI, go to **Network** > **WAN** > **Wi-Fi**.

2. Expand the Wi-Fi section and click on **Settings**. Ensure the **Interface** is enabled.

3. Click the **Scan** button to select your **ESSID**, or manually enter the ESSID of the network by clicking **Enter network (E)SSID manually**.

4. Choose the correct **Encryption** method and enter the appropriate **Key**.

   :::tip NOTE
   Assuming you have entered the correct parameter values, you should receive an IP address assigned by your Wi-Fi router's (AP) built-in DHCP server. You can use this new IP address to log in via a web browser.
   :::

   For details, refer to the <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#wi-fi" target="_blank">WisGateOS 2 User Manual>WAN>Wi-Fi</a>.

> **Image:** Wi-Fi settings

#### Connect Through Ethernet

To access the Internet through the ETH (PoE) port, make sure you have completed the steps defined in the [Connect the PoE Adapter](#connect-the-poe-adapter) section.

> **Image:** Accessing the Internet through Ethernet

1. Connect the Ethernet cable to the **ETH(PoE)** port, and the other end to the PoE port of the PoE injector.

2. Connect the LAN port of the PoE injector to your router. The router's DHCP server should assign an IP Address to the gateway.

3. Now, you can access the assigned IP address to access the gateway. If you wish, you can change the default settings below (details in the [WisGateOS 2 User Manual > WAN > Ethernet](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#ethernet)).

> **Image:** Connect through Ethernet settings

#### Connect Through Cellular

If your gateway supports LTE and you have inserted the SIM card, the gateway will automatically connect to the cellular network once the SIM card is inserted.

1. If manual APN configuration is needed, go to **Network** > **WAN** > **Cellular** in the Web UI.

> **Image:** Cellular Interface Page

2. Expand the Cellular section and click on **Settings**.

- For additional information, check the [WisGateOS 2 User Manual > WAN > Cellular](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#cellular).

> **Image:** Cellular settings

## Tutorials

In this section, you can browse tutorials about the RAK7289V2/RAK7289CV2 gateway to help you better understand and use the product.

| Tutorials                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <a href="https://learn.rakwireless.com/hc/en-us/articles/26688300221079-How-To-Use-the-MQTT-Broker-Like-a-Pro-Examples" target="_blank">Use the MQTT Broker Like a Pro + Examples</a>                                                     |
| <a href="https://learn.rakwireless.com/hc/en-us/articles/26527371792535-How-To-Configure-WisGate-Edge-V2-Gateways-Remote-Management-OpenVPN" target="_blank">WisGate Edge V2 Gateways Remote Management - OpenVPN</a>                     |
| <a href="https://learn.rakwireless.com/hc/en-us/articles/26526970499735-How-To-Configure-ThingsBoard-with-MQTT-HTTP-Integrations-via-WisGateOS2" target="_blank">ThingsBoard Configuration with MQTT/HTTP Integrations via WisGateOS 2</a> |
| <a href="https://learn.rakwireless.com/hc/en-us/articles/26688144537623-How-To-Install-OpenVPN-for-Ubuntu-Systems" target="_blank">OpenVPN Server Installation Guide (For Ubuntu sys)</a>                                                 |
| **IoT Solutions**                                                                                                                                                                                                                         |
| <a href="https://www.rakwireless.com/en-us/company/about/rakstar-success-story/pilot-things" target="_blank">Transforming Agriculture with LoRaWAN®: How AgriSens is Powering Productivity for Farmers</a>                                |

