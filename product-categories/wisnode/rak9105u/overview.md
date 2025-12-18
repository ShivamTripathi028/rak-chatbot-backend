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

# RAK9105U PowerLink - Remote Reboot Switch for LoRaWAN

Thank you for choosing **RAK9105U PowerLink - Remote Reboot Switch for LoRaWAN** in your awesome IoT project! 🎉 To help you get started, we have provided you all the necessary documentation for your product.

- [Quick Start Guide](https://docs.rakwireless.com/product-categories/wisnode/rak9105u/quickstart/)
- [Downlink Commands and Uplink Data Format](https://docs.rakwireless.com/product-categories/wisnode/rak9105u/downlink-uplink/)
- [Datasheet](https://docs.rakwireless.com/product-categories/wisnode/rak9105u/datasheet/)

## Product Description

The **RAK9105U PowerLink** is a LoRaWAN-based remote power controller designed for managing power supply to devices such as gateways, LTE CPEs, WiFi routers, and IP cameras, especially in remote or hard-to-reach deployment environments.

> **Image:** RAK9105U Outdoor Deployment

- **Remote Power Switching**

By placing the RAK9105U between the power source and the target device, users can send **LoRaWAN downlink commands** to remotely toggle the power on or off.
- **Remote Device Reboot**

Ideal for scenarios where devices freeze or require periodic reboots, such as LoRaWAN gateways or LTE CPEs in field installations.

## Product Features

- Integrated RAK3172 LoRa module for long-range, low-power wireless control
- Supports LoRaWAN 1.0.3 Class C protocol
- Multi-band compatibility for global deployment
- Onboard LoRa antenna (Optional external antenna via IPEX connector)
- Remote power switching and rebooting via LoRaWAN® downlink commands
- Plug-and-play integration available with Datacake platform
- Wide-range DC power input: 9–24 V via terminal block or DC jack (Compatible with RAK Battery Plus system for solar-powered deployments)
- Triple output design:
    - 1 always-on 12 V<sub>DC</sub> output
    - 2 controllable outputs (12 V + 5 V USB-C)

## Usage Scenarios

- **Plug-and-Play Solution Kit**

Pre-configured with a LoRaWAN gateway and fully integrated into the Datacake platform, enabling immediate remote power control via mobile app—ideal for rapid deployment and PoC testing.
- **Custom Integration**

Connect the RAK9105U to your own LoRaWAN network server and application platform for full control, automation, and cloud integration. Suitable for scalable and production-grade environments.

## How It Works

The **RAK9105U PowerLink** enables reliable **remote power control** by functioning as an intelligent switch between a DC power source and a connected device (e.g., gateway, LTE router, camera).

> **Image:** RAK9105U Connectivity Overview

**Power Input Options**

The RAK9105U is powered by a 9–24 V<sub>DC</sub> source, such as a power adapter or a solar battery system.

**Connection to Target Device**

It is placed between the power source and your end device (e.g., gateway), supplying power via its output ports.

**LoRaWAN Connectivity**

The built-in RAK3172 module connects to a LoRaWAN network, allowing the device to receive downlink commands from the cloud.

**Remote Reboot Function**

When a user sends a command (e.g., via Datacake), the RAK9105U toggles one of its output channels—effectively rebooting the connected device.

**Always-On Listening**

Thanks to Class C operation, the RAK9105U constantly listens for commands, ensuring fast response time without delay.

