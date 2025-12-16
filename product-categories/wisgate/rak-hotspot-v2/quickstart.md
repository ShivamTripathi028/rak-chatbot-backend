---
title: RAK Hotspot V2 Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK Hotspot v2. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Gateway/Module.
keywords:
- RAK Hotspot V2
- wisgate
- quickstart
image: https://images.docs.rakwireless.com/wisgate/rak-hotspot-v2/rak-hotspot-v2.png
sidebar_label: Quick Start Guide
---


import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK Hotspot V2 Quick Start Guide

## Prerequisites

### Hardware

1. [**RAK Hotspot V2**](https://store.rakwireless.com/products/rak-hotspot-miner?utm_source=RAKHotspotMiner&utm_medium=Document&utm_campaign=BuyFromStore)
2. 32&nbsp;GB microSD Card (included)
3. USB Type-C Power Adapter (included)

:::warning
The SIM card slot of the cellular versions is not hot-swappable. Ensure that the gateway is switched off before inserting or ejecting the SIM card.
:::

### Package Inclusion

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak-hotspot-v2/quickstart/package-contents.png"
  width="75%"
  caption="RAK Hotspot V2 Package Inclusion"
/>

## Product Configuration

For antenna mounting scenarios and ensuring a proper connectivity chain, refer to the <a href="/product-categories/wisgate/rak-hotspot-v2/troubleshooting/#proper-miner-connection-scenarios-with-the-rak-outdoor-enclosure-antennas" target="_blank">Troubleshooting guide.</a>
### Download the Helium App

The application is available for both Android and iOS. You can manually search for it or simply scan the QR code provided in **Figure 2**.

* [**Android**](https://play.google.com/store/apps/details?id=com.helium.wallet)
* [**iOS**](https://apps.apple.com/ph/app/helium-hotspot/id1450463605)

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak-hotspot/quickstart/qr.png"
  width="50%"
  caption="QR Codes"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak-hotspot/quickstart/app.png"
  width="50%"
  caption="iOS and Android App"
/>


### Power On the RAK Hotspot V2

1. Connect the LoRa antenna before powering on the device.

:::warning
When powering on the Hotspot, **DO NOT** leave the port antenna open to avoid potential damage to the device.
:::

2. Plug in and connect the included power supply to the USB-C port on the RAK Hotspot V2.
3. After approximately one minute, you can add the RAK Hotspot V2 to the Helium app. Press the pairing button on the side to enable the **Hotspot Pairing** mode.
4. Select **Set up Hotspot** in the app and follow the instructions. Press the **Pairing** button when requested.

:::tip NOTE
To reconnect to the app in the future, simply press the button.
:::

#### Account Security

When setting up your account, you will be prompted to enter a 12-word seed phrase. This phrase is essential for recovering or transferring your account to a new phone if needed.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak-hotspot/quickstart/fill-up.png"
  width="50%"
  caption="Account recovery or transfer keywords"
/>

