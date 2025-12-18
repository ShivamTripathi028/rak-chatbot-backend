---
slug: /product-categories/wisnode/rak9105u/downlink-uplink/
title: RAK9105U Downlink & Uplink Command Guide
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
    - command guide
sidebar_label: Downlink and Uplink
date: 2025-07-10
---

# RAK9105U Downlink Commands and Uplink Data Format

## Downlink Command Reference

The **RAK9105U PowerLink - Remote Reboot Switch for LoRaWAN** supports remote control through standard **LoRaWAN Class C downlink commands**. These commands allow you to control power outputs and configure key parameters such as uplink intervals.

### Output Control Commands

| Hex Command | Description |
| --- | --- |
| 00 00 | Turn **OFF** 5 V Output (Output 3, USB-C) |
| 00 01 | Turn **ON** 5 V Output (Output 3, USB-C) |
| 01 00 | Turn **OFF** 12 V Output (Output 2, Barrel Jack) |
| 01 01 | Turn **ON** 12 V Output (Output 2, Barrel Jack) |
| 02 01 | Set uplink interval to 1 minute |
| 02 1E | Set uplink interval to 30 minutes |

:::tip NOTE
If the connected device (e.g., gateway or router) has internal capacitors, the power-off action may take a few seconds to complete.
:::

### Uplink Interval Configuration Commands

Use these downlinks to adjust how frequently the RAK9105U sends uplink data:

| Hex Command | Description |
| --- | --- |
| 02 01 | Set uplink interval to **1 minute** |
| 02 1E | Set uplink interval to **30 minutes** |

If you need to set a specific uplink transmission period, you can execute the **ATC+SENDFREQ** command in the WisToolBox under ADVANCE > OPEN CONSOLE to set the uplink **ATC+SENDFREQ** transmission period in minutes (1-1440 minutes).

> **Image:** ATC send frequency

## Uplink Data Description

The **RAK9105U PowerLink - Remote Reboot Switch for LoRaWAN** periodically sends uplink data to the LoRaWAN network server after a successful OTAA join. In this DC-powered configuration, the uplink payload structure is simple and consistent.

### Uplink Structure

When powered by a standard **9–24 V<sub>DC</sub> input**, the device reports basic operational status via **Port 1**:
- **Output status**: Indicates whether **Output 2** (12 V) and **Output 3** (5 V) are ON or OFF
- **SW version** of the RAK9105U MCU

This data allows you to verify the current power output state and track firmware updates remotely.

> **Image:** End Device Packet Capture

### Payload Structure

The following is an example of how to interpret the payload sent via Port 1 in DC power mode.

| Port: 1 | Payload: 0369 |  |  |  |
| --- | --- | --- | --- | --- |
| U8 | 1 Byte | Output status | 3 | 5 V Output ON 12 V Output ON Data description can be found in the [Output status](#output-status) section. |
| U8 | 1 Byte | 9105U SW version | 69 | 1.0.5 |

### Output Status

| Status Code | Output 3 (5 V, USB-C) | Output 2 (12 V, Barrel Jack) |
| --- | --- | --- |
| 0 | OFF | OFF |
| 1 | ON | OFF |
| 2 | OFF | ON |
| 3 | ON | ON |

