---
slug: /product-categories/software-apis-and-libraries/wisgateos2/security/
title: WisGateOS 2 User Manual | Complete Guide for LoRaWAN Gateway Software
description: Configure WisGateOS 2 for LoRaWAN gateways with Basics Station, MultiWAN, MQTT, and HTTP integrations. Secure connections with OpenVPN & WireGuard.
image: "https://images.docs.rakwireless.com/product-logos/wisgateos2.png"
keywords:
  - ssh access
  - dhcp client port
  - http port 80
  - https port 443
  - mqtt port 1883
  - http port 8080
  - firewall configuration
tags:
  - security
  - open ports
sidebar_label: Security
date: 2022-08-01
---

# Security

## Default Open Ports

This section provides an overview of the default open ports in **WisGateOS 2**, along with their protocols and services.

| Port | Protocol | Service     | Description                                                                                                                                                  |
|------|----------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 22   | TCP      | SSH         | Remote command-line management, typically used by administrators to securely log into the gateway.                                                           |
| 68   | UDP      | DHCP Client | Used by the gateway as a DHCP client to receive IP lease and renewal responses from DHCP servers. Required for automatic IP address assignment and renewals. |
| 80   | TCP      | HTTP        | Standard WebUI access to the gateway (unencrypted).                                                                                                          |
| 443  | TCP      | HTTPS       | Secure WebUI access to the gateway (encrypted).                                                                                                              |
| 1883 | TCP      | MQTT        | MQTT transport, used for data exchange between the gateway and the LNS or external application platforms.                                                    |
| 8080 | TCP      | HTTP        | ChirpStack or internal service API/management interface, commonly used for backend integration or testing purposes.                                          |

:::tip NOTE
- By default, **port `8080`** is not enabled on all gateways. Currently, it is only available on **RAK7437**.
- If you need to **manage gateway ports**, you can use the **RAK Open/Close Port Extension**.

  For details, refer to the Open/Close Port documentation:  
  - [WisGateOS 2 v2.2.x or later](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-22x-or-later#rak-openclose-port)  
  - [WisGateOS 2 v2.0.x / v2.1.x](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x#openclose-port)
:::
