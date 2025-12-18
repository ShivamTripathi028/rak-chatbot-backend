---
slug: /product-categories/software-apis-and-libraries/wisgateos2/fleet-management/
title: WisGateOS 2 User Manual | Complete Guide for LoRaWAN Gateway Software
description: Configure WisGateOS 2 for LoRaWAN gateways with Basics Station, MultiWAN, MQTT, and HTTP integrations. Secure connections with OpenVPN & WireGuard.
image: "https://images.docs.rakwireless.com/product-logos/wisgateos2.png"
keywords:
  - gateway fleet management
  - wisdm remote management
  - remote monitoring for gateways
tags:
  - wisdm
  - fleet management
sidebar_label: Fleet Management with WisDM
date: 2022-08-01
---



import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'



# Fleet Management with WisDM

## What is WisDM?

[WisDM](https://wisdm.rakwireless.com/login?from=::organizations) is a cloud-based **gateway management platform** designed to simplify the **deployment, configuration, and monitoring** of RAK gateways. It provides a centralized and efficient solution for managing IoT gateway fleets, offering the following key features:

+ **Remote Configuration** - Secure cloud-based configuration and management of gateways.
+ **Mass Deployment** - Group-based provisioning and batch configuration for multiple devices.
+ **Live Monitoring** - Real-time performance metrics, system logs, and device health monitoring.
+ **Automated Alerts** - Email notifications for abnormal gateway behavior or status changes.
+ **Over-the-Air (OTA) Updates** - Remote firmware upgrades without manual intervention.
+ **Secure Remote Access** - Web-based SSH terminal for full gateway control.

## Why Use WisDM for Fleet Management?

Managing a large number of gateways manually can be inefficient and costly. WisDM offers a **scalable, cost-effective, and VPN-free** approach to remote gateway management, designed to simplify large-scale deployments and reduce operational overhead.

Key advantages include:

- **Zero-Touch Remote Management (No VPN Required)**<br/>
  Traditionally, configuring and managing gateways remotely required a VPN connection to each device's local UI. With WisDM, users can **remotely configure and monitor thousands of gateways** seamlessly without the need for a VPN.
- **Reduced Operational Costs & Increased Stability**<br/>
  By eliminating the need for on-site visits, WisDM **reduces installation and maintenance costs** while ensuring a more **stable and secure** remote management experience.
- **Multi-Tiered Access Control**<br/>
  Unlike traditional VPN-based solutions, WisDM allows businesses to **assign different user roles with varying levels of access permissions**. This is particularly beneficial for **system integrators, network operators, and enterprises** managing large-scale deployments.

## Integrate your Gateway with WisDM

### Enable WisDM Integration on the Gateway

1. Navigate to **Settings > WisDM**.
2. Enable the **Allow WisDM integration** option to connect the gateway to the **WisDM Platform** for remote management.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/settings/settings-wisdm.png"
  width="100%"
  caption="WisDM tab"
/>

### Register the Gateway in WisDM

Enabling **Allow WisDM integration** option does not automatically register your gateway in WisDM. ***Registration must be completed separately on the WisDM platform*** to enable full remote monitoring and management capabilities. For detailed registration steps, refer to the [WisDM Documentation](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisdm/getting-started/#add-a-gateway-to-a-location).



## Check WisDM Integration Status

Navigate to **Settings > WisDM** to view the **Registered in WisDM** indicator. This shows whether the gateway is successfully registered with the platform.

The indicator can display one of the following statuses:

- <img src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/settings/wisdm-registered-gateway.png" width="16px"/>: The gateway is successfully registered in WisDM and can be monitored, configured, and managed remotely.<br/>
- <img src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/settings/wisdm-unregistered-gateway.png" width="16px"/>: The gateway has not been registered in WisDM yet. Remote management and FOTA are not available until registration is completed.

## Enable FOTA (Firmware Over-The-Air)

Once your gateway is integrated with WisDM, **FOTA** provides an easy way to perform firmware updates remotely. To enable this feature:

1. Navigate to **Settings > WisDM** 
2. Enable **FOTA**.

:::tip NOTE
If you prefer to manually update the firmware via the WisGateOS 2 Web UI, you must disable **FOTA**.
:::

<RkBottomNav/>