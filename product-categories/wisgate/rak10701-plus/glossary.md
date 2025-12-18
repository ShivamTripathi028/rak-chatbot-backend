---
slug: /product-categories/wisgate/rak10701-plus/glossary/
title: RAK10701-Plus Field Tester for LoRaWAN
description: RAK10701-Plus Field Tester for LoRaWAN is a ready-to-use WisNode for evaluating deployed LoRaWAN network. It has a GNSS, a touchscreen LCD for the user interface, and is powered by a rechargeable battery.
image: https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/physical-interface.png
keywords:
    - lorawan
    - field tester plus
    - rak10701-plus
sidebar_label: Glossary 
date: 2025-05-23
tags:
  - glossary
  - field tester plus
---

# Field Tester Plus Glossary of Key Terms

Quickly look up important terms and definitions used throughout this guide for easier understanding and navigation.

## Work Modes

| Term | Definition |
| --- | --- |
| Field Tester Mode | Full-featured mode after joining an LNS and integrating the Field Test Data Processor Extension. Displays both uplink and downlink metrics, including RSSI, SNR, packet loss, distance, and supports CSV export. |
| LinkCheck Mode | Basic mode when joined to an LNS but Field Test Extension is not installed or not properly configured. Only downlink RSSI, SNR, and gateway count are displayed. |

## LoRa Metrics

| Term | Definition |
| --- | --- |
| Uplink RSSI | Signal strength measured at the gateway from the Field Tester Plus's uplink. |
| Uplink SNR | Signal-to-noise ratio of the uplink, measured at the gateway. |
| Downlink RSSI | Signal strength received by the device from the gateway (based on LinkCheck response). |
| Downlink SNR | Signal-to-noise ratio of the downlink, measured by the Field Tester Plus. |
| Packet Loss Rate (Uplink) | Percentage of lost uplink packets, calculated from frame counter gaps. |
| Packet Loss Rate (Downlink) | Loss percentage based on missing LinkCheck responses. |
| Number of Gateways | Number of gateways that received the last uplink. |
| Gateway EUI | Shortened EUI (unique ID) of the nearest receiving gateway. |

## Location and Distance

| Term | Definition | Dependencies |
| --- | --- | --- |
| Max Distance / Min Distance | Estimated distance to the farthest/nearest gateway, based on GPS. | Requires GPS and gateway location data. |
| Latitude / Longitude | Real-time geographic coordinates obtained by the device. | Requires outdoor environment and GPS fix. |
| Location Label | Manual tag entered to label test points (alternative to GPS indoors). | User-defined input. |

## Device Status

| Term | Definition |
| --- | --- |
| Last Refresh | Time since the last successfully processed uplink. |
| Battery Level | Displays the device's current battery percentage. Recommended to recharge when low. |

## User Actions

| Term | Definition |
| --- | --- |
| Stop/Start Sending | Pause or resume automatic uplinks via the pause icon. |
| Location Tagging (Label) | Manually set a label for the test point to enable CSV recording. |
| Force Uplink | Double-press the side button to send an immediate uplink outside the scheduled interval. |

