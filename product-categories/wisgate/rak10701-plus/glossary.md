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

import RkBottomNav from '@site/src/components/Document/BottomNav'

# Field Tester Plus Glossary of Key Terms

Quickly look up important terms and definitions used throughout this guide for easier understanding and navigation.

## Work Modes

<table>
  <thead>
    <tr>
      <th>Term</th>
      <th>Definition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Field Tester Mode</b></td>
      <td>Full-featured mode after joining an LNS and integrating the Field Test Data Processor Extension. Displays both uplink and downlink metrics, including RSSI, SNR, packet loss, distance, and supports CSV export.</td>
    </tr>
    <tr>
      <td><b>LinkCheck Mode</b></td>
      <td>Basic mode when joined to an LNS but Field Test Extension is not installed or not properly configured. Only downlink RSSI, SNR, and gateway count are displayed.</td>
    </tr>
  </tbody>
</table>

## LoRa Metrics

<table>
  <thead>
    <tr>
      <th>Term</th>
      <th>Definition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Uplink RSSI</b></td>
      <td>Signal strength measured at the gateway from the Field Tester Plus's uplink.</td>
    </tr>
    <tr>
      <td><b>Uplink SNR</b></td>
      <td>Signal-to-noise ratio of the uplink, measured at the gateway.</td>
    </tr>
    <tr>
      <td><b>Downlink RSSI</b></td>
      <td>Signal strength received by the device from the gateway (based on LinkCheck response).</td>
    </tr>
    <tr>
      <td><b>Downlink SNR</b></td>
      <td>Signal-to-noise ratio of the downlink, measured by the Field Tester Plus.</td>
    </tr>
    <tr>
      <td><b>Packet Loss Rate (Uplink)</b></td>
      <td>Percentage of lost uplink packets, calculated from frame counter gaps.</td>
    </tr>
    <tr>
      <td><b>Packet Loss Rate (Downlink)</b></td>
      <td>Loss percentage based on missing LinkCheck responses.</td>
    </tr>
    <tr>
      <td><b>Number of Gateways</b></td>
      <td>Number of gateways that received the last uplink.</td>
    </tr>
    <tr>
      <td><b>Gateway EUI</b></td>
      <td>Shortened EUI (unique ID) of the nearest receiving gateway.</td>
    </tr>
  </tbody>
</table>

## Location and Distance


<table>
  <thead>
    <tr>
      <th>Term</th>
      <th>Definition</th>
      <th>Dependencies</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Max Distance / Min Distance</b></td>
      <td>Estimated distance to the farthest/nearest gateway, based on GPS.</td>
      <td>Requires GPS and gateway location data.</td>
    </tr>
    <tr>
      <td><b>Latitude / Longitude</b></td>
      <td>Real-time geographic coordinates obtained by the device.</td>
      <td>Requires outdoor environment and GPS fix.</td>
    </tr>
    <tr>
      <td><b>Location Label</b></td>
      <td>Manual tag entered to label test points (alternative to GPS indoors).</td>
      <td>User-defined input.</td>
    </tr>
  </tbody>
</table>

## Device Status

<table>
  <thead>
    <tr>
      <th>Term</th>
      <th>Definition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Last Refresh</b></td>
      <td>Time since the last successfully processed uplink.</td>
    </tr>
    <tr>
      <td><b>Battery Level</b></td>
      <td>Displays the device's current battery percentage. Recommended to recharge when low.</td>
    </tr>
  </tbody>
</table>

## User Actions

<table>
  <thead>
    <tr>
      <th>Term</th>
      <th>Definition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Stop/Start Sending</b></td>
      <td>Pause or resume automatic uplinks via the pause icon.</td>
    </tr>
    <tr>
      <td><b>Location Tagging (Label)</b></td>
      <td>Manually set a label for the test point to enable CSV recording.</td>
    </tr>
    <tr>
      <td><b>Force Uplink</b></td>
      <td>Double-press the side button to send an immediate uplink outside the scheduled interval.</td>
    </tr>
  </tbody>
</table>

<RkBottomNav/>