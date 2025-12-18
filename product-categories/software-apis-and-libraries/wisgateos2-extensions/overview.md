---
title: WisGateOS 2 Manual | Customizable LoRaWAN Gateway Software
description: Explore WisGateOS 2 extensions, customize your LoRaWAN gateway, and enable secure connections with OpenVPN & WireGuard. Tailor your gateway to your needs!
image: "https://images.docs.rakwireless.com/product-logos/wisgateos2-extensions.png"
keywords:
  - wisgateos 2
  - wisgateos 2 extensions
  - wisgateos 2 user manual
  - rak lora gateway software
  - lorawan gateway software manual
  - lora settings configuration
  - country settings for lorawan
  - lorawan gateway extensions guide
  - wisgateos 2 packet forwarding
  - custom logo extension wisgateos 2
  - failover reboot lorawan
  - openvpn wireguard for gateways
  - wifi ethernet integration wisgateos 2
sidebar_label: Overview
date: 2022-04-07
tags:
  - wisgateos 2 extensions
  - wisgateos 2
  - user manual
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# WisGateOS 2 Extensions User Manual

## Overview

WisGateOS 2 introduces an extension framework that enables gateways to install additional software modules. Extensions can be added, removed, or updated as needed, making deployments more flexible and adaptable.

Starting from WisGateOS 2 2.2.x, the extension installation process is further improved for better security and user experience:
- All extensions are verified with a digital signature to ensure authenticity and compatibility.
- The Extension Gallery enables direct access to verified extensions, simplifying installation and management workflows.
- An Internet connection is required during installation to complete the signature verification.

To check your gateway firmware version, navigate to **Dashboard** > **Overview** in the Web UI.
- For gateways running **WisGateOS 2 2.2.x or later**, proceed to the updated steps in the [WisGateOS 2 2.2.x or Later](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later) section.
- For gateways running **WisGateOS 2 2.0.x or 2.1.x**, follow the installation procedure outlined in the [WisGateOS 2 2.0.x/2.1.x](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x) section.

## Supported Extensions

<details>
  <summary><strong>Breathing Light</strong> – Customize gateway LED behavior</summary>
  <table>
    <tr><td><strong>Description</strong></td><td>By using the breathing light extension, you can personalize the LED light's working modes, frequency, and color.</td></tr>
    <tr><td><strong>Usage</strong></td><td>Change LED behavior to meet site requirements, such as disabling blinking, adjusting colors for specific alerts, or matching internal maintenance standards.</td></tr>
    <tr><td><strong>Support</strong></td><td>HW: WisGate Edge Lite 2 and WisGate Soho Lite<br/> SW: WisGateOS 2</td></tr>
  </table>
</details>

<details>
  <summary><strong>Custom Logo</strong> – Brand the Web UI with your logo</summary>
  <table>
    <tr><td><strong>Description</strong></td><td>The Custom Logo extension allows you to upload your logo in the Web UI.</td></tr>
    <tr><td><strong>Usage</strong></td><td>Quickly brand the gateway UI for customer deliveries, demos, or white-label projects.</td></tr>
    <tr><td><strong>Support</strong></td><td>HW: All WisGateOS 2 gateways<br/>SW: WisGateOS 2</td></tr>
  </table>
</details>

<details>
  <summary><strong>Country Settings (LBT)</strong> – Set country code and enable Listen-Before-Talk</summary>
  <table>
    <tr><td><strong>Description</strong></td><td>Set your country to automatically apply the correct LoRaWAN® frequency plan, maximum transmit power, and channel list. Enable Listen-Before-Talk (LBT) for regions where it is mandatory to check channel availability before transmission.</td></tr>
    <tr><td><strong>Usage</strong></td><td>Ensure regulatory compliance in regions such as AS923-JP and KR920, and reduce interference in dense deployments.</td></tr>
    <tr><td><strong>Support</strong></td><td>HW: Only gateways with LBT-capable hardware<br/>SW: WisGateOS 2</td></tr>
  </table>
</details>

<details>
  <summary><strong>Open/Close Port</strong> – Control port access and allowlist IPs</summary>
  <table>
    <tr><td><strong>Description</strong></td><td>Manage which network ports are open on the gateway and restrict access to trusted IP addresses or subnets, reducing the risk of unauthorized connections.</td></tr>
    <tr><td><strong>Usage</strong></td><td>Limit SSH/HTTP access to admin networks, allow MQTT/HTTPS only for internal systems, comply with enterprise security policies.</td></tr>
    <tr><td><strong>Support</strong></td><td>HW: All WisGateOS 2 gateways<br/>SW: WisGateOS 2</td></tr>
  </table>
</details>

<details>
  <summary><strong>Solar Battery</strong> – Monitor solar power system status</summary>
  <table>
    <tr><td><strong>Description</strong></td><td>Display real-time operational data of the gateway’s solar battery, including performance, health, cycle count, capacity, and charging/discharging modes, helping to assess system reliability.</td></tr>
    <tr><td><strong>Usage</strong></td><td>Monitor off-grid or solar-powered sites, schedule preventive maintenance, and verify performance during prolonged low-sunlight conditions.</td></tr>
    <tr><td><strong>Support</strong></td><td>HW: RAK Battery Plus-compatible gateways (RAK7240V2, RAK7267, RAK7289V2, RAK7285)<br/>SW: WisGateOS 2</td></tr>
  </table>
</details>

<details>
  <summary><strong>WireGuard VPN</strong> – Lightweight, high-speed encrypted tunnel</summary>
  <table>
    <tr><td><strong>Description</strong></td><td>Creates a secure WireGuard VPN tunnel between the gateway and a remote VPN server, enabling encrypted, low-latency communication over the internet.</td></tr>
    <tr><td><strong>Usage</strong></td><td>Protect remote operations, enable cross-region private networking, and maintain high-speed secure connectivity.</td></tr>
    <tr><td><strong>Support</strong></td><td>HW: All WisGateOS 2 gateways<br/>SW: WisGateOS 2</td></tr>
  </table>
</details>

<details>
  <summary><strong>OpenVPN Client</strong> – Connect gateway to an OpenVPN server</summary>
  <table>
    <tr><td><strong>Description</strong></td><td>Establishes an encrypted VPN tunnel between the gateway and a remote OpenVPN server, enabling secure communication and remote management over public or private networks.</td></tr>
    <tr><td><strong>Usage</strong></td><td>Secure access over Ethernet/Wi‑Fi/LTE; HQ private network integration.</td></tr>
    <tr><td><strong>Support</strong></td><td>HW: All WisGateOS 2 gateways<br/>SW: WisGateOS 2</td></tr>
  </table>
</details>

<details>
  <summary><strong>Operation & Maintenance</strong> – Scheduled reboot & LTE auto-recovery</summary>
  <table>
    <tr><td><strong>Description</strong></td><td>Provides scheduled gateway reboots and automatic LTE module restart when connectivity loss is detected, ensuring stable operation in remote or critical deployments.</td></tr>
    <tr><td><strong>Usage</strong></td><td>Maintain uptime in unstable cellular networks, reduce manual intervention at unmanned sites, and simplify post-deployment maintenance.</td></tr>
    <tr><td><strong>Support</strong></td><td>HW: LTE-compatible gateways RAK7268CV2, RAK7240CV2, RAK7289CV2, RAK7285C, RAK7266, RAK7267<br/>SW: WisGateOS 2 v2.2.x or later</td></tr>
  </table>
</details>

<details>
  <summary><strong>Field Test Data Processor</strong> – Local signal analysis & coverage visualization</summary>
  <table>
    <tr><td><strong>Description</strong></td><td>Processes uplink data from RAK10701-Plus Field Tester via MQTT, computing RSSI, SNR, and packet loss locally. Supports CSV export, heatmap coverage visualization, and offline testing with manual location tags, with no cloud dependency.</td></tr>
    <tr><td><strong>Usage</strong></td><td>Pre-deployment surveys; indoor/outdoor optimization; GPS-denied testing; periodic coverage audits.</td></tr>
    <tr><td><strong>Support</strong></td><td>HW: WisGateOS 2 gateway + RAK10701-Plus Field Tester<br/>SW: WisGateOS 2 v2.2.x or later</td></tr>
  </table>
</details>

<details>
  <summary><strong>Failover Reboot</strong> – Auto-recover by rebooting LTE/gateway when all links fail</summary>
  <table>
    <tr><td><strong>Description</strong></td><td>Monitors LTE, Ethernet, and Wi-Fi links. If all enabled connections are offline, it first attempts recovery by rebooting the LTE module. If unsuccessful, the system reboots the gateway to restore connectivity.</td></tr>
    <tr><td><strong>Usage</strong></td><td>Multi-link networks requiring autonomous recovery; high-availability edge nodes; rooftop/remote sites where LTE reboot is the primary failover method.</td></tr>
    <tr><td><strong>Support</strong></td><td>HW: WisGateOS 2 gateways with multiple network interfaces (Ethernet/LTE/Wi-Fi)<br/>SW: WisGateOS 2 v2.2.x or later</td></tr>
  </table>
</details>

<details>
  <summary><strong>Wi‑Fi Reboot</strong> – Auto‑recover Wi‑Fi via ping/httping checks</summary>
  <table>
    <tr><td><strong>Description</strong></td><td>Periodically checks Wi-Fi connectivity and, if all tests fail, reboots the Wi-Fi module or the entire gateway to restore connection.</td></tr>
    <tr><td><strong>Usage</strong></td><td>Factories or campuses with AP roaming; indoor weak-signal floors; temporary hotspots or unstable Wi-Fi environments.</td></tr>
    <tr><td><strong>Support</strong></td><td>HW: All WisGateOS 2 gateways<br/>SW: WisGateOS 2 v2.2.x or later</td></tr>
  </table>
</details>

<details>
  <summary><strong>RF Spectrum Scanner</strong> – Real-time spectrum scan & channel analysis</summary>
  <table>
    <tr><td><strong>Description</strong></td><td>Scan defined bands and generate color-coded heatmaps of RSSI over time/frequency to detect interference, noisy channels, and spectrum patterns.</td></tr>
    <tr><td><strong>Usage</strong></td><td>Pre-deployment site surveys; urban interference diagnosis; optimize LoRa® channel plans; periodic RF audits.</td></tr>
    <tr><td><strong>Support</strong></td><td>HW: RAK7289V2 / RAK7289CV2<br/>SW: WisGateOS 2 v2.2.x or later</td></tr>
  </table>
</details>

<details>
  <summary><strong>LoRa Packet Local Storage</strong> – Store & retain LoRa® packets as CSV</summary>
  <table>
    <tr><td><strong>Description</strong></td><td>Record and manage all uplink and downlink LoRa® packets with configurable retention periods. It provides a reliable local data source for network analysis, performance monitoring, and troubleshooting.</td></tr>
    <tr><td><strong>Usage</strong></td><td>Network analysis; performance monitoring; troubleshooting; compliance-ready audits.</td></tr>
    <tr><td><strong>Support</strong></td><td>HW: All WisGateOS 2 gateways<br/>SW: WisGateOS 2 v2.2.15 or later</td></tr>
  </table>
</details>



<RkBottomNav/>