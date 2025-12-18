---
title: RAK7285/RAK7285C WisGate Edge Ultra Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK7285. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device.
image: "https://images.docs.rakwireless.com/wisgate/rak7285/rak7285.png"
keywords:
  - quickstart
  - RAK7285
  - RAK7285C
  - wisgate
sidebar_label: Quick Start Guide
---

# RAK7285/RAK7285C WisGate Edge Ultra Quick Start Guide

## Prerequisites

1. <a href="https://store.rakwireless.com/products/wisgate-edge-ultra-full-duplex-the-ultimate-lora-gateway-for-iot-solutions-rak7285-rak7285c?utm_source=RAK7285&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAK7285/RAK7285C WisGate Edge Ultra</a>
2. [Ethernet Cable](https://store.rakwireless.com/products/ethernet-cable-gland?utm_source=EthernetCableGland&utm_medium=Document&utm_campaign=BuyFromStore) (RJ-45 Port) for Ethernet connection
3. A Windows / Mac OS / Linux Computer

:::warning

The SD card in the SD card slot must not be ejected. Doing so may affect the performance of the device, as various logs and data are stored on it.

:::

### Package Inclusion

> **Image:** RAK7285/RAK7285C packing list

:::tip NOTE
+ This product does not include the LoRa antenna/s. The antennas are sold separately.
+ The antennas listed in the packing list include LTE antennas. If you purchased the gateway without cellular connectivity, the LTE antennas are not included in the bundle.
  :::

## Product Configuration

### Gateway Installation Guide

#### Insert SIM Card

If you will use the cellular variant of the gateway, you can refer to this section. Otherwise, skip it.

:::warning
The SIM card slot of the cellular versions is not hot-swappable. Make sure the gateway is switched off before inserting or ejecting the SIM card.
:::

1. Start by unscrewing the cap of the NanoSIM interface on the gateway enclosure to expose the SIM card slot.

> **Image:** Unscrewing the cap of the NanoSIM interface

2. Push the SIM card into the card slot according to the placement method marked on the interface.

> **Image:** Inserting the NanoSIM card

3. Once completed, screw back the metal cap. Make sure it is tightly screwed.

#### Installation

This section provides instructions on how to mount and secure the mounting kit to the enclosure and the mounting pole.

1. Attach the mount adapter included in the mounting kit on the bottom of the enclosure using four M6 x 12 mm screws.

> **Image:** Attaching the mount adapter to the enclosure

2. After attaching the mount adapter, fix the device bracket on it with four M6*12 screws.

> **Image:** Mounting the device bracket to the enclosure

3. Position and fasten the pole clamps together around the pole with bolts, washers, and nuts.

> **Image:** Mounting the clamps to a pole

:::tip NOTE

The pole supported by the brackets has a diameter ranging from 50~100 mm. If the pole diameter exceeds 100 mm, you can use steel strips instead. The standard mounting kit does not include steel strips, they are sold separately.

:::

> **Image:** Mounting using steel strips

4. Hang up the enclosure and affix it with two M6*12 screws.

> **Image:** Fastening the enclosure to the bracket

#### Attach the Antennas

Attach the LoRa, Wi-Fi, and GPS antennas. If you choose the LTE variant, you also need to attach the LTE antennas.

> **Image:** RAK7285/RAK7285C with attached antennas

#### Connect the PoE Adapter

If you choose to power the gateway via PoE or access the gateway and internet via the ETH port, you need to refer to this section. Otherwise, skip it.

Connect one end of the Ethernet cable (Cat5e or better) to the **ETH(PoE)** port on the gateway and the other end to the **PoE** port of the PoE injector.

### Weather Protection

To better protect the Ethernet cable gland and the antenna connector from the weather, you need to cover them with PVC tape.

1. Clean the surface area of the connector that will be wrapped. Wrap a layer of PVC tape with a 50% overlap according to the rotation direction of the connector. Continue wrapping the PVC tape to about 10 mm below the end of the connector.

> **Image:** Wrapping with PVC tape

2. Cut off about 50 cm waterproof tape. Stretch it to double its length and wrap three layers around the connector with a 50% overlap. Hold the tape in place with your hand for a few seconds.

> **Image:** Wrapping with waterproof tape

3. Wrap three additional layers with PVC tape with natural uncoiling force and a 50% overlap. Ensure to cover the head and the tail of the connector.

> **Image:** Final PVC wrapping

### Lightning Protection

This section covers the installation of the lightning surge protection system when deploying the RAK7285/RAK7285C  gateway, both outdoors and indoors. Such a protection system must be taken into consideration to ensure a fully functional gateway without interruptions or damage from lightning.

> **Image:** Full lightning protection set-up

#### Outdoor Surge Protection System

- **Antenna Grounding**: RAKwireless recommends installing a lightning arrestor on all the antenna N-type terminals. The arrestors must be N-type Female to Male to fit the antenna and enclosure connectors. Ensure you use a 10 AWG or better wire to connect the screw terminals of the arrestors to the grounding rail mounted on the building wall (grounding bar in the case of field deployment).
- **Gateway Grounding**: Additionally, it is recommended to use another 10 AWG or better grounding wire to connect the screw terminal on the right side of the gateway casing to the grounding rail (bar).

:::tip NOTE

+ No additional protection for the Ethernet cabling is required on the gateway side. It already has a built-in surge protection system (GDT + Anti-surge resistor).

+ No additional protection is required for the LoRa antennas. The cavity diplexer integrated into the LoRa antenna ports provides surge protection for the LoRa antennas.

:::

#### Indoor Surge Protection

For protecting the indoor equipment and circuitry connected to the gateway, it is recommended to install an Ethernet port SPD lightning arrestor. This device should be positioned along the cabling that connects the gateway to the PoE injector. Make sure you connect its grounding wire terminal to an appropriate building grounding point.

:::warning
Should you fail to adhere to the recommendations in this document, RAKwireless carries no responsibility for any damage your equipment incurs due to a lightning strike.
:::

#### Recommended Equipment

- <a href="https://store.rakwireless.com/products/lightning-arrestor-for-gps-antenna" target="_blank">Lightning Arrestor for GPS Antenna</a>: This lightning arrestor connects the antenna to the GPS receiver. It is a surge protection device that secures the transceiver against transients, over-voltage, and surge currents induced by lightning bolts. By employing a high-pass filter, this product can effectively suppress low-frequency interference caused by lightning while allowing the GPS signal to pass through with low insertion loss. A transient suppression device (TVS) and a gas discharge tube (GDT) are used to protect the DC feed circuit.
- <a href="https://store.rakwireless.com/products/lightning-arrestor" target="_blank">Lightning arrestor for the LTE and Wi-Fi antennas</a>: This is a surge protection device for securing transceivers against over-voltage and surge current induced by lightning bolts. RAKwireless recommends installing lightning arrestors on all N-type antenna terminals, including LTE and 2.4G Wi-Fi antennas.
- <a href="https://store.rakwireless.com/products/pulsar-cable-rak9731-rak9733?utm_source=RAK9731&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">Pulsar Cable RAK9731</a>: RAK9731 Pulsar cable is used for RAK7285 Lightning Protection. This cable is an N-Type Male to N-Type Female cable with 1.5 m, 3 m, 5 m, 10 m, or longer custom lengths. It is an LMR-400 coaxial cable with N-type connectors.
- <a href="https://store.rakwireless.com/products/signal-surge-protective?variant=29842390122541?utm_source=signalsurgeprotectivedevice&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">Signal Surge Protective Device</a>: This surge protective device is suitable for CAT6 or Class E cables, providing protection for equipment from surges and over-voltages induced by lightning or produced in internal systems. It is widely used in comprehensive network wiring projects in offices, industries, or similar telecommunication applications, such as Gigabit Ethernet, ATM, ISDN, and VoIP systems.
- <a href="(https://store.rakwireless.com/products/cat5-ethernet-cable?utm_source=ethernetcable&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">Ethernet Cabling</a>: A CAT5 Ethernet cable is recommended for an outdoor surge protection system. It is used for connections between the PoE injector, Ethernet SPD, router/switch, and the Ethernet/PoE port on RAK7285/RAK7285C.

### Power On the Gateway

:::warning
Do not power the device if any antenna port has been left open.
:::

The gateway supports multiple power supply options. Connect the gateway to the appropriate power source based on your requirements.

**Power Cord + PoE Adapter**: The gateway is powered via PoE. Make sure you have completed the steps defined in [Connect the PoE Adapter](#connect-the-poe-adapter) section.

1. Connect one end of the power cord to the PoE adapter.
2. Connect the other end of power cord to a power outlet, your gateway can be powered on.

> **Image:** Powering the gateway using PoE

**DC Cable**: The gateway is powered by an external DC power supply. You need to use the DC cable to connect an external power supply. The external power supply voltage range: 9~36 V<sub>DC</sub>.

> **Image:** Powering the gateway using external DC power supply

The gateway also supports **RAK9155 Battery Plus** as its power supply. <a href="https://store.rakwireless.com/products/rak-battery-plus-rak9155?variant=42309251563718" target="_blank">RAK9155 Battery Plus</a> is not included in the bundle, it needs to be purchased separately.

### Access the Gateway

In this section, two methods of accessing the gateway are provided to offer different alternatives based on the availability of the required resources.

#### Wi-Fi AP Mode

By default, the gateway will work in Wi-Fi AP Mode which means that you can find an SSID named like "**RAK7285_XXXX or RAK7285C_XXXX**" on your PC's Wi-Fi Network List. "XXXX" is the last two bytes of the Gateway MAC address.

1. To access the Web Management Platform, input the following IP Address in your Web browser: `192.168.230.1`

:::tip NOTE
No password is required to connect via Wi-Fi.
:::

> **Image:** Accessing the gateway via Wi-Fi AP Mode

2. For security reasons, upon the first login, you must set a login password. To do this, enter the desired password and confirm it in the provided fields. The password must meet the following requirements:

- At least 12 characters long
- Has at least one special character (`!“#$%&\‘()*+,-./:;<=>?@[]^_{|}~`)
- Has at least one number
- Has at least one standard Latin letter (used in the English alphabet)

> **Image:** Web UI login page

3. When the fields are filled in, click the **Set password** button to apply it. The web UI is now accessible and it will load the **LoRaWAN Statistics page**.

> **Image:** LoRaWAN statistics page

4. On the next log in, you need to use the set password for access. The default login username is **root**.

> **Image:** Login page with set password

#### WAN Port (Ethernet)

To access the gateway through the ETH (PoE) port, make sure you have completed the steps defined in the [Connect the PoE Adapter](#connect-the-poe-adapter) section.

1. Connect one end of another Ethernet cable to the LAN port on the PoE adapter, and the other end to your PC.

> **Image:** Accessing the gateway via WAN Port (Ethernet)

:::tip NOTE
The default IP is **169.254.X.X**. The last two segments(X.X) are mapped from the last four bits of the MAC address of your gateway. For example, the last four bits of the MAC address are `0F:01`, and the IP address is `169.254.15.1`. Make sure to manually set the address of your PC to one in the same network (for example, `169.254.15.100`).
:::

2. Open the head to the **Ethernet Properties** and click the **Internet Protocol Version 4 (TCP/IPv4)**.

> **Image:** Internet properties

3. Select **Use the following IP address** and set the IP address (for example, `169.254.15.100`).

> **Image:** Setting IP address of the PC

In this example, you can access the gateway on the `169.254.15.1` address.

4. For security reasons, upon the first login, you must set a login password. To do this, enter the desired password and confirm it in the provided fields. The password must meet the following requirements:

- At least 12 characters long
- Has at least one special character (`!“#$%&\‘()*+,-./:;<=>?@[]^_{|}~`)
- Has at least one number
- Has at least one standard Latin letter (used in the English alphabet)

> **Image:** Web UI login page

5. When the fields are filled in, click the **Set password** button to apply it. The Web UI is now accessible, and it will load the LoRaWAN Statistics page.

> **Image:** LoRaWAN statistics page

6. On the next log in, you need to use the set password for access. The default login username is **root**.

> **Image:** Login Page with set password

### Access the Internet

In this section, two methods of accessing the internet are provided to give you different alternatives to choose from, depending on the availability of the necessary requirements.

#### Connect Through Wi-Fi

1. Access the gateway's Web UI, and navigate to **Network** > **WAN** > **Wi-Fi**.
2. Expand the Wi-Fi block and click on **Settings**. Make sure the **Interface** is enabled.

> **Image:** Accessing the Internet using Wi-Fi

- For additional information, check the <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview" target="_blank">WisGateOS 2 User Manual</a>.

> **Image:** Wi-Fi settings

3. You can either click the **Scan** button to choose your **ESSID** or manually type the ESSID of the network by clicking **enter network (E)SSID manually**.
4. Select the right **Encryption** method and enter the correct **Key**.

:::tip NOTE
Assuming you have entered the correct parameter values, you should receive an IP address assigned by your Wi-Fi router's (AP) built-in DHCP server. You can use this new IP address to log in via a web browser (the same way as in AP mode).
:::

#### Connect Through Ethernet/PoE

To access the Internet through the ETH (PoE) port, make sure you have completed the steps defined in the [Connect the PoE Adapter](#connect-the-poe-adapter) section.

1. Connect one end of an Ethernet cable to the port labeled **ETH** on the gateway, and the other end to the PoE port of the PoE injector.

> **Image:** Accessing the Internet through Ethernet

2. Connect the LAN port of the PoE injector to your router. The router's DHCP server should assign an IP address to the gateway.

3. Now, you can access the assigned IP to access the gateway. You can change the default settings below if you wish (details in the <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview" target="_blank">WisGateOS 2 User Manual</a>).

> **Image:** Connect through Ethernet settings

## Tutorials

In this section, you can browse tutorials about the RAK7285/RAK7285CV2 gateway to help you better understand and use the product.

| Tutorials                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <a href="https://www.youtube.com/watch?v=G2AxL5r9w_U" target="_blank">Fiberglass Antenna Mounting Solution for Outdoor Setup - Outdoor LoRaWAN Gateway, RAK9731</a>                                                                       |
| <a href="https://learn.rakwireless.com/hc/en-us/articles/26688300221079-How-To-Use-the-MQTT-Broker-Like-a-Pro-Examples" target="_blank">Use the MQTT Broker Like a Pro + Examples</a>                                                     |
| <a href="https://learn.rakwireless.com/hc/en-us/articles/26527371792535-How-To-Configure-WisGate-Edge-V2-Gateways-Remote-Management-OpenVPN" target="_blank">WisGate Edge V2 Gateways Remote Management - OpenVPN</a>                     |
| <a href="https://learn.rakwireless.com/hc/en-us/articles/26526970499735-How-To-Configure-ThingsBoard-with-MQTT-HTTP-Integrations-via-WisGateOS2" target="_blank">ThingsBoard Configuration with MQTT/HTTP Integrations via WisGateOS 2</a> |
| <a href="https://learn.rakwireless.com/hc/en-us/articles/26688144537623-How-To-Install-OpenVPN-for-Ubuntu-Systems" target="_blank">OpenVPN Server Installation Guide (For Ubuntu sys)</a>                                                 |

