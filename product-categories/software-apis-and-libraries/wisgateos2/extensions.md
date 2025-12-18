---
slug: /product-categories/software-apis-and-libraries/wisgateos2/extensions/
title: WisGateOS 2 User Manual | Complete Guide for LoRaWAN Gateway Software
description: Configure WisGateOS 2 for LoRaWAN gateways with Basics Station, MultiWAN, MQTT, and HTTP integrations. Secure connections with OpenVPN & WireGuard.
image: "https://images.docs.rakwireless.com/product-logos/wisgateos2.png"
keywords:
  - wisgateos2 software extensions
  - install gateway extensions
  - customizable gateway features
  - feature expansion rak gateway
tags:
  - software extensions
sidebar_label: Extensions
date: 2022-08-01
---

# Extensions

WisGateOS 2 supports extensions, which provides additional features and functions that can be added, removed, or updated based on your needs.

> **Image:** Extensions

## Supported Extensions

<details>
  <summary>**Breathing Light** – Customize gateway LED behavior</summary>
  
| Description | By using the breathing light extension, you can personalize the LED light's working modes, frequency, and color. |
| --- | --- |
| Usage | Change LED behavior to meet site requirements, such as disabling blinking, adjusting colors for specific alerts, or matching internal maintenance standards. |
| Support | HW: WisGate Edge Lite 2 and WisGate Soho LiteSW: WisGateOS 2 |

</details>

<details>
  <summary>**Custom Logo** – Brand the Web UI with your logo</summary>
  
| Description | The Custom Logo extension allows you to upload your logo in the Web UI. |
| --- | --- |
| Usage | Quickly brand the gateway UI for customer deliveries, demos, or white-label projects. |
| Support | HW: All WisGateOS 2 gatewaysSW: WisGateOS 2 |

</details>

<details>
  <summary>**Country Settings (LBT)** – Set country code and enable Listen-Before-Talk</summary>
  
| Description | Set your country to automatically apply the correct LoRaWAN frequency plan, maximum transmit power, and channel list. Enable Listen-Before-Talk (LBT) for regions where it is mandatory to check channel availability before transmission. |
| --- | --- |
| Usage | Ensure regulatory compliance in regions such as AS923-JP and KR920, and reduce interference in dense deployments. |
| Support | HW: Only gateways with LBT-capable hardwareSW: WisGateOS 2 |

</details>

<details>
  <summary>**Open/Close Port** – Control port access and allowlist IPs</summary>
  
| Description | Manage which network ports are open on the gateway and restrict access to trusted IP addresses or subnets, reducing the risk of unauthorized connections. |
| --- | --- |
| Usage | Limit SSH/HTTP access to admin networks, allow MQTT/HTTPS only for internal systems, comply with enterprise security policies. |
| Support | HW: All WisGateOS 2 gatewaysSW: WisGateOS 2 |

</details>

<details>
  <summary>**Solar Battery** – Monitor solar power system status</summary>
  
| Description | Display real-time operational data of the gateway's solar battery, including performance, health, cycle count, capacity, and charging/discharging modes, helping to assess system reliability. |
| --- | --- |
| Usage | Monitor off-grid or solar-powered sites, schedule preventive maintenance, and verify performance during prolonged low-sunlight conditions. |
| Support | HW: RAK Battery Plus-compatible gateways (RAK7240V2, RAK7267, RAK7289V2, RAK7285)SW: WisGateOS 2 |

</details>

<details>
  <summary>**WireGuard VPN** – Lightweight, high-speed encrypted tunnel</summary>
  
| Description | Creates a secure WireGuard VPN tunnel between the gateway and a remote VPN server, enabling encrypted, low-latency communication over the internet. |
| --- | --- |
| Usage | Protect remote operations, enable cross-region private networking, and maintain high-speed secure connectivity. |
| Support | HW: All WisGateOS 2 gatewaysSW: WisGateOS 2 |

</details>

<details>
  <summary>**OpenVPN Client** – Connect gateway to an OpenVPN server</summary>
  
| Description | Establishes an encrypted VPN tunnel between the gateway and a remote OpenVPN server, enabling secure communication and remote management over public or private networks. |
| --- | --- |
| Usage | Secure access over Ethernet/Wi‑Fi/LTE; HQ private network integration. |
| Support | HW: All WisGateOS 2 gatewaysSW: WisGateOS 2 |

</details>

<details>
  <summary>**Operation & Maintenance** – Scheduled reboot & LTE auto-recovery</summary>
  
| Description | Provides scheduled gateway reboots and automatic LTE module restart when connectivity loss is detected, ensuring stable operation in remote or critical deployments. |
| --- | --- |
| Usage | Maintain uptime in unstable cellular networks, reduce manual intervention at unmanned sites, and simplify post-deployment maintenance. |
| Support | HW: LTE-compatible gateways RAK7268CV2, RAK7240CV2, RAK7289CV2, RAK7285C, RAK7266, RAK7267SW: WisGateOS 2 v2.2.x or later |

</details>

<details>
  <summary>**Field Test Data Processor** – Local signal analysis & coverage visualization</summary>
  
| Description | Processes uplink data from RAK10701-Plus Field Tester via MQTT, computing RSSI, SNR, and packet loss locally. Supports CSV export, heatmap coverage visualization, and offline testing with manual location tags—no cloud dependency. |
| --- | --- |
| Usage | Pre-deployment surveys; indoor/outdoor optimization; GPS-denied testing; periodic coverage audits. |
| Support | HW: WisGateOS 2 gateway + RAK10701-Plus Field TesterSW: WisGateOS 2 v2.2.x or later |

</details>

<details>
  <summary>**Failover Reboot** – Auto-recover by rebooting LTE/gateway when all links fail</summary>
  
| Description | Monitors LTE, Ethernet, and Wi-Fi links. If all enabled connections are offline, it first attempts recovery by rebooting the LTE module. If unsuccessful, the system reboots the gateway to restore connectivity. |
| --- | --- |
| Usage | Multi-link networks requiring autonomous recovery; high-availability edge nodes; rooftop/remote sites where LTE reboot is the primary failover method. |
| Support | HW: WisGateOS 2 gateways with multiple network interfaces (Ethernet/LTE/Wi-Fi)SW: WisGateOS 2 v2.2.x or later |

</details>

<details>
  <summary>**Wi‑Fi Reboot** – Auto‑recover Wi‑Fi via ping/httping checks</summary>
  
| Description | Periodically checks Wi-Fi connectivity and, if all tests fail, reboots the Wi-Fi module or the entire gateway to restore connection. |
| --- | --- |
| Usage | Factories or campuses with AP roaming; indoor weak-signal floors; temporary hotspots or unstable Wi-Fi environments. |
| Support | HW: All WisGateOS 2 gatewaysSW: WisGateOS 2 v2.2.x or later |

</details>

<details>
  <summary>**RF Spectrum Scanner** – Real-time spectrum scan & channel analysis</summary>
  
| Description | Scan defined bands and generate color-coded heatmaps of RSSI over time/frequency to detect interference, noisy channels, and spectrum patterns. |
| --- | --- |
| Usage | Pre-deployment site surveys; urban interference diagnosis; optimize LoRa channel plans; periodic RF audits. |
| Support | HW: RAK7289V2 / RAK7289CV2SW: WisGateOS 2 v2.2.x or later |

</details>

<details>
  <summary>**LoRa Packet Local Storage** – Store & retain LoRa packets as CSV</summary>
  
| Description | Record and manage all uplink and downlink LoRa packets with configurable retention periods. It provides a reliable local data source for network analysis, performance monitoring, and troubleshooting. |
| --- | --- |
| Usage | Network analysis; performance monitoring; troubleshooting; compliance-ready audits. |
| Support | HW: All WisGateOS 2 gatewaysSW: WisGateOS 2 v2.2.15 or later |

</details>

## Install and Use

To install and use extensions, follow the installation guide that matches your WisGateOS 2 version:
  - <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later/" target="_blank">For WisGateOS 2 version 2.2.x or later</a>
  - <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/" target="_blank">For WisGateOS 2 versions 2.0.x and 2.1.x</a>

