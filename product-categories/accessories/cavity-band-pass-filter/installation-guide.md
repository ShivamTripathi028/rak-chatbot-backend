---
slug: /product-categories/accessories/cavity-band-pass-filter/installation-guide/
title: "Step-by-Step Installation Guide: RAK Outdoor Band-Pass Filter"
description: Learn how to install the RAK Outdoor Cavity Band-Pass Filter. Includes cable connection, mounting, sealing, and grounding steps for outdoor reliability.
image: https://images.docs.rakwireless.com/accessories/cavity-band-pass-filter/cavity-band-pass-filter.png
keywords:
  - RAK Band-Pass Filter installation
  - LoRaWAN outdoor filter setup
  - LoRa gateway interference protection
  - Outdoor RF filter installation
  - Cavity band-pass filter mounting
  - Sealing and grounding LoRa filter
  - Protect LoRaWAN gateway from interference
sidebar_label: Installation Guide
date: 2025-10-09
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK Outdoor Cavity Band-Pass Filter Installation Guide

This section provides step-by-step instructions for installing the Cavity Band-Pass Filter.

## Package Inclusions

The package contains the following items:

<RkImage
  src="https://images.docs.rakwireless.com/accessories/cavity-band-pass-filter/packagelist.png"
  width="80%"
  caption="Package Inclusions"
/>

+ 1 x [RAK Outdoor Cavity Band-Pass Filter](https://store.rakwireless.com/products/outdoor-cavity-band-pass-filter-lorawan?utm_source=docs_center&utm_medium=organic&utm_campaign=rak_outdoor_cavity_band-pass_filter_documentation_installation_guide_page&utm_term=cavity_band-pass_filter&utm_content=store_link) (selected frequency variant)
+ 1 x RF coaxial cables
+ 2 x Mounting clamps
+ 1 x Waterproof tape
+ 1 x PVC insulating tape

:::tip NOTE
 The frequency range is specified on the **product label**. Please check the sticker on the device to confirm your model.
 :::

## Installation Guide

### 1. Connect the Coaxial RF Cable

Connect one of the included coaxial RF cables to **Port 1** on the filter. Tighten the connector securely.

   <RkImage
     src="https://images.docs.rakwireless.com/accessories/cavity-band-pass-filter/conect-to-coaxial-rf-cable.png"
     width="35%"
     caption="Connect the Coaxial RF Cable to Port 1"
   />

### 2. Attach the Antenna

1. Connect your LoRa antenna to **Port 2** of the filter:

   <RkImage
     src="https://images.docs.rakwireless.com/accessories/cavity-band-pass-filter/conect-to-antenna.png"
     width="20%"
     caption="Attach the LoRa antenna to Port 2"
   />

2. After attaching cables and antenna, apply **weatherproof sealing** to every exposed RF connection. Follow the procedures described in the [Weather Protection](https://docs.rakwireless.com/product-categories/accessories/cavity-band-pass-filter/installation-guide/#weather-protection?intsource=docs_center&intmedium=organic&intcampaign=rak_outdoor_cavity_band-pass_filter_documentation_installation_guide_page&intterm=weather_protection&intcontent=documentation_link) section.

### 3. Mount the Filter

We recommend mounting the filter slightly higher than the gateway to simplify cable routing.

**Mounting Tips:**
- Ensure clamps are tight and stable to prevent movement from wind or vibration.
- Mount the filter **vertically upright** to maintain waterproof integrity.
- For outdoor installation, use anti-slip rubber pads or rust-proof washers between the clamp and mounting bracket.

**Mounting Steps:**
1. Use a screwdriver to loosen the clamp by rotating the screw counterclockwise.

2. Insert the clamp through the holes on the filter’s mounting bracket.

   <RkImage
     src="https://images.docs.rakwireless.com/accessories/cavity-band-pass-filter/step2.png"
     width="30%"
     caption="Insert clamp through the mounting bracket"
   />

3. Wrap the clamp around the mounting pole.

4. Adjust the filter's height and position, then tighten the screw clockwise.

   <RkImage
     src="https://images.docs.rakwireless.com/accessories/cavity-band-pass-filter/step4.png"
     width="30%"
     caption="Secure the filter onto the mounting pole"
   />

5. Connect the free end of the coaxial cable from **Port 1** to the LoRa antenna port on the gateway.

6. Apply **weatherproof sealing** to the **Port 1** connection.

## Weather Protection

To ensure long-term outdoor reliability, all exposed RF connectors must be sealed using PVC insulating tape and waterproof self-amalgamating tape.

1. Clean the connector surface to remove dust, oil, or moisture.

2. Wrap a layer of PVC insulating tape with 50% overlap, extending about 10&nbsp;mm beyond the connector end.

   <RkImage
     src="https://images.docs.rakwireless.com/accessories/cavity-band-pass-filter/wrap-pvc.png"
     width="30%"
     caption="Wrap the first layer of PVC tape"
   />

3. Stretch waterproof self-amalgamating tape to double its length, then wrap three layers with 50% overlap. Hold firmly for a few seconds.

   <RkImage
     src="https://images.docs.rakwireless.com/accessories/cavity-band-pass-filter/stretch-waterproof.png"
     width="30%"
     caption="Apply waterproof self-amalgamating tape"
   />

4. Apply three final layers of PVC tape with 50% overlap, covering both ends of the connector.

   <RkImage
     src="https://images.docs.rakwireless.com/accessories/cavity-band-pass-filter/wrap-pvc-agian.png"
     width="30%"
     caption="Apply the final PVC tape layers"
   />

## Lightning Protection (Recommended)

For outdoor installations, proper grounding is strongly recommended.

- Connect a **10 AWG or thicker grounding wire** from the **Ground Pad** on the filter to a verified earth ground point.
- This helps prevent damage from lightning-induced surges and improves ESD safety.

:::warning
 Lightning strikes can generate powerful electrical surges that may harm sensitive electronic devices. The warranty **does not** cover damages caused by lightning strikes or other natural events.
 :::


<RkBottomNav/>