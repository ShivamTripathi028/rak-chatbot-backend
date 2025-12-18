---
slug: /product-categories/software-apis-and-libraries/wisgateos2/network/
title: WisGateOS 2 User Manual | Complete Guide for LoRaWAN Gateway Software
description: Configure WisGateOS 2 for LoRaWAN gateways with Basics Station, MultiWAN, MQTT, and HTTP integrations. Secure connections with OpenVPN & WireGuard.
image: "https://images.docs.rakwireless.com/product-logos/wisgateos2.png"
keywords:
  - ethernet connection setup
  - wifi setup for gateway
  - 4g lte internet configuration
  - lte sim card setup
  - wan failover setup
  - auto failover
  - multi-network backup
  - lan ip configuration
  - icmp tracking
  - http tracking
tags:
  - network management
  - ethernet
  - wi-fi
  - lte
  - wan failover
  - wan priority
  - lan ip setup
  - multi-network backup
sidebar_label: Network
date: 2022-08-01
---

# Network

In the **Network** menu, you can configure both **WAN** (Wide Area Network) and **LAN** (Local Area Network) interfaces. The **WAN** section handles the settings for connecting to external networks (e.g., the internet), while the **LAN** section manages local network connections within your environment.

## WAN

In the **WAN** menu, you can manage the priority of the WAN interfaces. If the highest-priority interface goes down, the gateway will automatically switch to the next available interface for Internet access. The status of each interface is indicated by a red/green light next to the interface name, showing whether the interface is available or not.

> **Image:** WAN tab

:::tip NOTE
For gateways that do not support the **Ethernet** port (such as the **[RAK7267](https://docs.rakwireless.com/product-categories/wisgate/rak7267/datasheet)**), the **Ethernet** option will not be available in the interface list.
:::

### Change Priority

In a **Multi-Network** setup, managing WAN interface priorities ensures that the gateway seamlessly switches between available networks based on their priority, enabling continuous connectivity even in the event of network failures. This is particularly useful for providing **backup** connectivity when the primary network is unavailable.

You can adjust the priority of each WAN interface to control the preferred network connection. Follow the steps below to modify the interface priority:

1. Click the **Change Priority** button.
2. Use the arrows (<img src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/main/c.png" width="6%"/>) next to each interface name to change its priority.

> **Image:** Editing WAN interface priority

- The **upward arrow** increases the priority, making that network the preferred one.
- The **downward arrow** decreases the priority, making it a secondary or backup network.

3. Click **Save**.

### Ethernet

Displays information for the selected Ethernet interface. Expand the interface details by clicking on the interface name or the arrow to the left of it (<img src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/main/d.png"/>).

> **Image:** Ethernet

  - **Protocol type**: Specifies the protocol type.
  - **IP Address**: The IP address assigned to the gateway.
  - **Netmask**: The gateway's network mask.
  - **Connection time**: The duration the gateway has been connected to the interface.
  - **RX**: Received packets.
  - **TX**: Sent packets.
  - **DNS**: DNS server addresses.
  - **Settings**: Network interface and tracking preferences for ethernet mode.
    + **General**: Ensure that the Ethernet interface is configured correctly with static IP, DHCP, or PPPoE settings, giving the gateway a stable and predictable network connection.

      
> **Image:** Ethernet settings General tab

      + **Enable WAN and disable LAN**: Enabling this option activates the WAN interface and disables LAN.
      + **Static address**: Configure a static address for the gateway.
        - **IPv4 Address**: The static IPv4 address for the gateway.
        - **IPv4 Netmask**: The netmask for the gateway.
        - **IPv4 Router**: The IPv4 router address.
        - **DNS Server**: Custom DNS server address.
      + **DHCP client**: Use the router's DHCP server to assign an IP address.
        - **Use DNS servers advertised by router**: Enable this to assign DNS from the router.
        - **DNS Server**: Add custom DNS addresses.
      + **PPPoE**: Set Point-to-Point Protocol over Ethernet (PPPoE), with **PAP/CHAP Username** and **Password** provided by the internet provider. The **DNS server advertised by router** allows the gateway to obtain a DNS address from the router. If you want to use a custom DNS server, you need to disable this option.

    + **Tracking**: Provide the mechanism for the gateway to continuously monitor the network interface's stability and automatically failover to another available interface when necessary, ensuring continuous connectivity even in case of network issues.

      
> **Image:** Ethernet settings Tracking tab

      - **Type**: Select the method for link tracking.
        - **ICMP**: Sends ping packets to test connectivity at the IP level.
        - **HTTP**: Sends HTTP GET requests to confirm service availability at the application level.
      - **Target address**
        + For **ICMP**: Supports IP addresses and domain names.
        + For **HTTP**: Supports domain names, full URLs, or IP addresses.
        + The Target address supports a single input of up to 100 characters.
      - **Reliability**: Define the minimum number of IP addresses that need to respond to confirm a successful ping.
      - **Ping count**: The number of pings to send.
      - **Ping timeout (s)**: The time allowed for each ping.
      - **Ping interval**: The interval between pings.
      - **Down**: The number of consecutive ping failures required to confirm that the interface is down.
      - **Up**: The number of consecutive ping successes required to confirm that the interface is up.

### Wi-Fi

Displays information about the selected Wi-Fi interface. Expand the interface details by clicking on the interface name or the arrow to the left of it (<img src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/main/d.png"/>).

> **Image:** Wi-Fi

  - **Protocol Type**: Specifies the protocol type.
  - **IP Address**: The IP address assigned to the gateway.
  - **Netmask**: The netmask assigned to the gateway.
  - **Connection time**: The duration the gateway has been connected to the Wi-Fi interface.
  - **Channel**: The operating frequency used by the Wi-Fi network.
  - **(E)SSID**: The SSID of the Wi-Fi network.
  - **BSSID**: The MAC address of the Wi-Fi access point or router.
  - **Bitrate**: The bitrate of the Wi-Fi network.
  - **DNS**: DNS server addresses.
  - **Settings**: Set the network interface and tracking preferences for Wi-Fi mode.
    + **General**: Ensure the Wi-Fi interface is set up properly with either static or dynamic (DHCP) addressing, SSID, encryption, and network settings. It helps the gateway connect securely and consistently to the Wi-Fi network.

      
> **Image:** Wi-Fi settings General tab

      - **Enabled/Disabled**: Enable or disable the Wi-Fi interface.
      - **Available (E)SSID networks**: Scan for available Wi-Fi networks and select one, or manually enter the details.
      - **(E)SSID**: Extended Service Set Identifier.
      - **Encryption**: Select the type of encryption used by the network and enter the password. Options include **No Encryption**, **WPA-PSK**, **WPA2-PSK**, and **WPA-PSK/WPA2-PSK Mixed Mode** (recommended).
      - **Static address**: Configure a static address for the gateway.
        - **IPv4 Address**: The desired static IPv4 address.
        - **IPv4 Netmask**: The netmask.
        - **IPv4 Router**: The IPv4 router address.
        - **DNS Server**: Custom DNS address.
      - **DHCP client**: Use the router's DHCP server to assign an IP.
        - **Use DNS servers advertised by router**: Enable to assign DNS from the router or specify a custom DNS.
        - **DNS Server**: Add custom DNS addresses.

    + **Tracking**: Monitor the health of the Wi-Fi interface by performing periodic ping tests. If the interface becomes unstable (fails too many pings), it will failover to another interface. Once it becomes stable again, the gateway can switch back to the Wi-Fi network.

      
> **Image:** Wi-Fi settings Tracking tab

      - **Type**: Select the method for link tracking.
        - **ICMP**: Sends ping packets to test connectivity at the IP level.
        - **HTTP**: Sends HTTP GET requests to confirm service availability at the application level.
      - **Target address**
        + For **ICMP**: Supports IP addresses and domain names.
        + For **HTTP**: Supports domain names, full URLs, or IP addresses.
        + The Target address supports a single input of up to 100 characters.
      - **Reliability**: Define the minimum number of IP addresses that need to respond to confirm a successful ping.
      - **Ping count**: The number of pings to send.
      - **Ping timeout (s)**: The time allowed for each ping.
      - **Ping interval**: The interval between pings.
      - **Down**: The number of consecutive ping failures required to confirm that the interface is down.
      - **Up**: The number of consecutive ping successes required to confirm that the interface is up.

### Cellular

Displays information for the selected cellular interface. Expand the interface details by clicking on the interface name or the arrow to the left of it (<img src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/main/d.png"/>).

> **Image:** Cellular

  - **RSRP**: Reference Signal Received Power. Indicates the strength of the received LTE reference signal.
  - **RSRQ**: Reference Signal Received Quality. Reflects signal quality by considering interference and signal strength.
  - **SINR**: Signal-to-Interference-and-Noise Ratio. Measures signal quality relative to background noise.
  - **RSSI**: Received Signal Strength Indicator. Represents the total received signal power, including interference and noise.
  - **IP Address**: The IP assigned to the gateway.
  - **Netmask**: The netmask assigned to the gateway.
  - **IMSI**: International Mobile Subscriber Identity.
  - **ICCID**: Integrated Circuit Card Identifier.
  - **IMEI**: International Mobile Equipment Identity.
  - **Connection time**: The duration the gateway has been connected to the interface.
  - **Network**: The cellular network standard.
  - **RAT**: Radio Access Technology. Indicates the wireless technology in use.
  - **SIM Card Status**: The status of the SIM card.
  - **Settings**: Set the network interface and tracking preferences for cellular mode.
    - **General**: The purpose of the **General** settings is to configure the cellular connection (APN, username, password, PIN) to ensure the gateway can properly connect to the cellular network.

      
> **Image:** Cellular settings General tab

        - **Enabled/Disabled**: Enable or disable the cellular interface.
        - **APN (optional)**: The Access Point Name for the connection.
        - **User (optional)**: Username for authentication (leave empty if not required).
        - **Password (optional)**: Password for authentication (leave empty if not required).
        - **PIN code (optional)**: The SIM card's PIN code (leave empty if not required).

    - **Tracking**: The **Tracking** settings ensure the gateway maintains stable connectivity by regularly testing the cellular network. If the network becomes unreliable (fails pings consecutively), the gateway will automatically switch to another available interface, ensuring continuous service.

      
> **Image:** Cellular settings Tracking tab

      - **Type**: Select the method for link tracking.
        - **ICMP**: Sends ping packets to test connectivity at the IP level.
        - **HTTP**: Sends HTTP GET requests to confirm service availability at the application level.
      - **Target address**
        + For **ICMP**: Supports IP addresses and domain names.
        + For **HTTP**: Supports domain names, full URLs, or IP addresses.
        + The Target address supports a single input of up to 100 characters.
      - **Reliability**: Define the minimum number of IP addresses that need to respond to confirm a successful ping.
      - **Ping count**: The number of pings to send.
      - **Ping timeout (s)**: The time allowed for each ping.
      - **Ping interval**: The interval between pings.
      - **Down**: The number of consecutive ping failures required to confirm that the interface is down.
      - **Up**: The number of consecutive ping successes required to confirm that the interface is up.

## LAN

In the **LAN** tab, you can view and configure the settings for your Local Area Network (LAN) interfaces. The status of each interface is indicated by a red/green light, showing whether the interface is enabled or disabled.

> **Image:** LAN tab

### DHCP Server

The **DHCP Server** section allows you to configure the gateway's LAN IP settings. By default, the gateway has a preconfigured DHCP server that assigns IP addresses to connected devices. You can modify these settings as needed. Expand the interface details by clicking on the interface name or the arrow to the left of it (<img src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/main/d.png"/>).

> **Image:** DHCP Server

- **IP Address**: The default IP address of the gateway's DHCP server.
- **Netmask**: The subnet mask for the DHCP server.
- **Settings**: Set the network interface preferences for DHCP server.

  
> **Image:**  DHCP Settings

  + **Address**: The IPv4 address of the LAN DHCP server.
  + **Netmask**: The subnet mask for the DHCP server.

### Ethernet

The field only shows if the interface is active. Expand the interface details by clicking on the interface name or the arrow to the left of it (<img src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/main/d.png"/>).

> **Image:** Ethernet

- **Enable LAN and disable WAN**: Toggle this option to enable the LAN Ethernet interface and disable the WAN Ethernet interface.

    
> **Image:** Ethernet settings

### Wi-Fi

Manage the settings for the Wi-Fi LAN interface in this section. The Wi-Fi interface allows the gateway to create a wireless access point (AP) for local devices to connect. Expand the interface details by clicking on the interface name or the arrow to the left of it (<img src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/main/d.png"/>).

> **Image:** Wi-Fi

- **(E)SSID**: The name of the Access Point (AP) provided by the gateway.
- **Encryption**: The encryption method used to secure the Wi-Fi connection.
- **Settings**: Set the network interface and tracking preferences for Wi-Fi mode.

  
> **Image:** Wi-Fi settings

  - **Enabled/Disabled**: Enable or disable the Wi-Fi LAN interface.
  - **Channel**: Set the Wi-Fi channel. The default is **Auto**, which allows the gateway to automatically choose the optimal channel.
  - **(E)SSID**: The SSID for the wireless AP.
  - **Encryption**:  Select the encryption type for the Wi-Fi AP. Available options include:
    - **No Encryption**
    - **WPA-PSK**
    - **WPA2-PSK**
    - **WPA-PSK/WPA2-PSK Mixed Mode**
  - **Hidden**: Option to hide the SSID, making the AP invisible to devices scanning for networks.

