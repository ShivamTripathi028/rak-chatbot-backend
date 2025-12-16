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

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK9105U Downlink Commands and Uplink Data Format

## Downlink Command Reference

The **RAK9105U PowerLink - Remote Reboot Switch for LoRaWAN** supports remote control through standard **LoRaWAN Class C downlink commands**. These commands allow you to control power outputs and configure key parameters such as uplink intervals.

### Output Control Commands

<table>
  <thead>
    <tr>
      <th>Hex Command</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>00 00</td>
      <td>Turn **OFF** 5&nbsp;V Output (Output 3, USB-C)</td>
    </tr>
    <tr>
      <td>00 01</td>
      <td>Turn **ON** 5&nbsp;V Output (Output 3, USB-C)</td>
    </tr>
    <tr>
      <td>01 00</td>
      <td>Turn **OFF** 12&nbsp;V Output (Output 2, Barrel Jack)</td>
    </tr>
    <tr>
      <td>01 01</td>
      <td>Turn **ON** 12&nbsp;V Output (Output 2, Barrel Jack)</td>
    </tr>
    <tr>
      <td>02 01</td>
      <td>Set uplink interval to 1&nbsp;minute</td>
    </tr>
    <tr>
      <td>02 1E</td>
      <td>Set uplink interval to 30&nbsp;minutes</td>
    </tr>
  </tbody>
</table>


:::tip NOTE
If the connected device (e.g., gateway or router) has internal capacitors, the power-off action may take a few seconds to complete.
:::

### Uplink Interval Configuration Commands

Use these downlinks to adjust how frequently the RAK9105U sends uplink data:

<table>
  <thead>
    <tr>
      <th>Hex Command</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>02 01</td>
      <td>Set uplink interval to **1&nbsp;minute**</td>
    </tr>
    <tr>
      <td>02 1E</td>
      <td>Set uplink interval to **30&nbsp;minutes**</td>
    </tr>
  </tbody>
</table>

If you need to set a specific uplink transmission period, you can execute the **ATC+SENDFREQ** command in the WisToolBox under ADVANCE > OPEN CONSOLE to set the uplink **ATC+SENDFREQ** transmission period in minutes (1-1440&nbsp;minutes).

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/downlink-uplink/atc-send-frequency.png"
  caption="ATC send frequency"
  width="100%"
/>

## Uplink Data Description

The **RAK9105U PowerLink - Remote Reboot Switch for LoRaWAN** periodically sends uplink data to the LoRaWAN network server after a successful OTAA join. In this DC-powered configuration, the uplink payload structure is simple and consistent.

### Uplink Structure

When powered by a standard **9–24&nbsp;V<sub>DC</sub> input**, the device reports basic operational status via **Port 1**:
- **Output status**: Indicates whether **Output 2** (12&nbsp;V) and **Output 3** (5&nbsp;V) are ON or OFF
- **SW version** of the RAK9105U MCU

This data allows you to verify the current power output state and track firmware updates remotely.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak9105u/downlink-uplink/rak9105u-end-device-packet-capture.png"
  caption="End Device Packet Capture"
  width="100%"
/>

### Payload Structure

The following is an example of how to interpret the payload sent via Port 1 in DC power mode.

<table>
  <thead>
    <tr>
      <th colSpan="3">Port: 1</th>
      <th colSpan="2">Payload: 0369</th>
    </tr>
    <tr>
      <th>Data Type</th>
      <th>Byte</th>
      <th>Parameter</th>
      <th>Raw Data</th>
      <th>Parsed Data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>U8</td>
      <td>1&nbsp;Byte</td>
      <td>Output status</td>
      <td>3</td>
      <td>5&nbsp;V Output ON <br/> 12&nbsp;V Output ON <br/> Data description can be found in the [Output status](#output-status) section.</td>
    </tr>
    <tr>
      <td>U8</td>
      <td>1&nbsp;Byte</td>
      <td>9105U SW version</td>
      <td>69</td>
      <td>1.0.5</td>
    </tr>
  </tbody>
</table>

### Output Status

<table>
  <thead>
    <tr>
      <th>Status Code</th>
      <th>Output 3 (5&nbsp;V, USB-C)</th>
      <th>Output 2 (12&nbsp;V, Barrel Jack)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>OFF</td>
      <td>OFF</td>
    </tr>
    <tr>
      <td>1</td>
      <td>ON</td>
      <td>OFF</td>
    </tr>
    <tr>
      <td>2</td>
      <td>OFF</td>
      <td>ON</td>
    </tr>
    <tr>
      <td>3</td>
      <td>ON</td>
      <td>ON</td>
    </tr>
  </tbody>
</table>

<RkBottomNav/>