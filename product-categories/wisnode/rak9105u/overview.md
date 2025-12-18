---
slug: /product-categories/wisnode/rak9105u/overview/
title: RAK9105U Remote Reboot Switch for LoRaWAN
description: The PowerLink RAK9105U is a remote power management device designed for LoRaWAN-enabled networks, allowing users to remotely reboot and control power for gateways, routers, CPEs, and cameras.
image: "https://images.docs.rakwireless.com/accessories/rak9105u/1.rak9105u.png"
keywords:
    - RAK9105U
    - wisnode
    - smart power control
    - remote management
tags:
    - rak9105u
    - wisnode
    - overview
sidebar_label: Product Overview
date: 2025-07-10
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK9105U PowerLink - Remote Reboot Switch for LoRaWAN

Thank you for choosing **RAK9105U PowerLink - Remote Reboot Switch for LoRaWAN** in your awesome IoT project! 🎉 To help you get started, we have provided you all the necessary documentation for your product.

- <a href="https://docs.rakwireless.com/product-categories/wisnode/rak9105u/quickstart/" target="_blank">Quick Start Guide</a>
- <a href="https://docs.rakwireless.com/product-categories/wisnode/rak9105u/downlink-uplink/" target="_blank">Downlink Commands and Uplink Data Format</a>
- <a href="https://docs.rakwireless.com/product-categories/wisnode/rak9105u/datasheet/" target="_blank">Datasheet</a>


## Product Description

The **RAK9105U PowerLink** is a LoRaWAN-based remote power controller designed for managing power supply to devices such as gateways, LTE CPEs, WiFi routers, and IP cameras, especially in remote or hard-to-reach deployment environments.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/overview/rak9105u-outdoor-deployment.png"
  caption="RAK9105U Outdoor Deployment"
  width="60%"
/>

- <b>Remote Power Switching</b><br/>
By placing the RAK9105U between the power source and the target device, users can send **LoRaWAN downlink commands** to remotely toggle the power on or off.
- <b>Remote Device Reboot</b><br/>
Ideal for scenarios where devices freeze or require periodic reboots, such as LoRaWAN gateways or LTE CPEs in field installations.

## Product Features

- Integrated RAK3172 LoRa module for long-range, low-power wireless control
- Supports LoRaWAN 1.0.3 Class C protocol
- Multi-band compatibility for global deployment
- Onboard LoRa antenna (Optional external antenna via IPEX connector)
- Remote power switching and rebooting via LoRaWAN® downlink commands
- Plug-and-play integration available with Datacake platform
- Wide-range DC power input: 9–24&nbsp;V via terminal block or DC jack (Compatible with RAK Battery Plus system for solar-powered deployments)
- Triple output design:
    - 1 always-on 12&nbsp;V<sub>DC</sub> output
    - 2 controllable outputs (12&nbsp;V + 5&nbsp;V USB-C)

## Usage Scenarios

- <b>Plug-and-Play Solution Kit</b><br/>
Pre-configured with a LoRaWAN gateway and fully integrated into the Datacake platform, enabling immediate remote power control via mobile app—ideal for rapid deployment and PoC testing.
- <b>Custom Integration</b><br/>
Connect the RAK9105U to your own LoRaWAN network server and application platform for full control, automation, and cloud integration. Suitable for scalable and production-grade environments.

## How It Works

The **RAK9105U PowerLink** enables reliable **remote power control** by functioning as an intelligent switch between a DC power source and a connected device (e.g., gateway, LTE router, camera).

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/overview/rak9105u-connectivity-overview.png"
  caption="RAK9105U Connectivity Overview"
  width="80%"
/>

<b>Power Input Options</b><br/>
The RAK9105U is powered by a 9–24&nbsp;V<sub>DC</sub> source, such as a power adapter or a solar battery system.

<b>Connection to Target Device</b><br/>
It is placed between the power source and your end device (e.g., gateway), supplying power via its output ports.

<b>LoRaWAN Connectivity</b><br/>
The built-in RAK3172 module connects to a LoRaWAN network, allowing the device to receive downlink commands from the cloud.

<b>Remote Reboot Function</b><br/>
When a user sends a command (e.g., via Datacake), the RAK9105U toggles one of its output channels—effectively rebooting the connected device.

<b>Always-On Listening</b><br/>
Thanks to Class C operation, the RAK9105U constantly listens for commands, ensuring fast response time without delay.

<RkBottomNav/>