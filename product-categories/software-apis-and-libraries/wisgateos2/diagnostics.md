---
slug: /product-categories/software-apis-and-libraries/wisgateos2/diagnostics/
title: WisGateOS 2 User Manual | Complete Guide for LoRaWAN Gateway Software
description: Configure WisGateOS 2 for LoRaWAN gateways with Basics Station, MultiWAN, MQTT, and HTTP integrations. Secure connections with OpenVPN & WireGuard.
image: "https://images.docs.rakwireless.com/product-logos/wisgateos2.png"
keywords:
  - gateway diagnostics
  - system log monitoring
  - view system logs
  - network utilities tools
  - ping test
  - traceroute tool
  - nslookup test
  - download logs
tags:
  - diagnostics
  - system log
  - ping test
  - traceroute
  - nslookup
sidebar_label: Diagnostics
date: 2022-08-01
---

# Diagnostics

In the **Diagnostics** menu, review the system logs on the gateway and perform checks.

## System Log

The **System log** tab displays complete system-level logs, primarily used for debugging and troubleshooting. 

The **Auto refresh** switch in the top right corner turns automatic log updates on or off.

> **Image:** System log tab

### Download System Log

To download system logs, follow these steps:

1. Navigate to **Settings** > **File browser**.

> **Image:** File browser

2. Go to **mmcblk0p1** > **syslog**.

> **Image:** syslog

3. Select the log file based on the timestamp and click to download.

### Configure System Log

If you need to configure log storage settings or forward logs to an external server, refer to the **[Configuring System Log](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/settings/#configure-the-system-log)** section.

## Network Utilities

The **Network utilities** page provides built-in diagnostic tools for network troubleshooting. These tools allow you to check connectivity, trace network routes, and perform DNS lookups directly from the gateway.

> **Image:** Network utilities tab

### Available Tools

- **Ping**: Tests the reachability of a host by sending ICMP echo request packets and measuring response times. This helps determine if a device or server is online.
- **Trace**: Displays the route packets take to reach a destination, showing the intermediate hops. Useful for identifying network latency or connection issues.
- **Nslookup**: Queries the Domain Name System (DNS) to obtain the IP address corresponding to a domain name or vice versa.

### How to Use

1. Enter an **IPv4 Address** or **Hostname** in the input field.

   :::tip NOTE
   For **Nslookup**, only a domain name is allowed.
   :::

2. Pick your desired tool:

   - **Ping** to check connectivity.
   - **Trace** to view the routing path.
   - **Nslookup** to resolve domain names.

3. The results will be displayed in the console output area below.

