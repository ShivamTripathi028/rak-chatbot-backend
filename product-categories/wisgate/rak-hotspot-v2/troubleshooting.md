---
title: Troubleshooting
description: Walks through different connection scenarios with your RAK Hotspot v2. This includes both the outdoor and indoor enclosure and antennas of RAKwireless suitable for your LoRaWAN Gateway.
keywords:
- RAK Hotspot v2
- Troubleshooting
- wisgate
image: https://images.docs.rakwireless.com/wisgate/rak-hotspot-v2/rak-hotspot-v2.png
sidebar_label: Troubleshooting
---

# Troubleshooting

## Status LEDs

The RAK Hotspot V2 includes two (2) small LEDs for status:

> **Image:** Status LED location

🔴 **Red LED**: A solid red light indicates that the Pi is receiving power and is functioning normally. If the red LED flashes, it signifies a power supply issue. To resolve this, reconnect the power and check again.

🟢 **Green LED**: When powered on, the green LED will blink randomly for approximately 5 seconds before stopping. If the green LED continues blinking repeatedly for an extended period, it typically indicates an issue, often with the SD card or potentially with the power supply.

In case the green LED continues blinking persistently, consider the following recommendations:

1. Unplug the USB-C power cable.
2. Remove the microSD card, verify its position, and reinsert it securely, ensuring it is properly seated. The card may have shifted during shipping or been inserted incorrectly, possibly upside down.
3. Reconnect the USB-C power cable, ensuring it is securely plugged in all the way.

## Proper Connection Scenarios with the RAK Outdoor Enclosure/Antennas

### Scenario 1 (Indoor, Optimal)

Products Used:

- [RAK Hotspot V2](https://store.rakwireless.com/products/rak-hotspot-miner?utm_source=RAKHotspotMiner&utm_medium=Document&utm_campaign=BuyFromStore)
- [Magnetic Antenna Base](https://store.rakwireless.com/products/antenna-magnetic-base?utm_source=MagneticAntennaBase&utm_medium=Document&utm_campaign=BuyFromStore)
- [Fiberglass Antenna](https://store.rakwireless.com/products/fiber-glass-antenna-1?m=2&h=helium-antenna&variant=43034794721478?utm_source=868-930MHz8dBiFiberGlassAntenna&utm_medium=Document&utm_campaign=BuyFromStore)

> **Image:** RAK Hotspot V2 + Magnetic Antenna Base + Fiberglass Antenna

### Scenario 2 (Indoor, Suboptimal)

Products Used:

- [RAK Hotspot V2](https://store.rakwireless.com/products/rak-hotspot-miner?utm_source=RAKHotspotMiner&utm_medium=Document&utm_campaign=BuyFromStore)
- Converter Cable (included with any of the Fiberglass Antennas)
- [Fiberglass Antenna](https://store.rakwireless.com/products/fiber-glass-antenna-1?m=2&h=helium-antenna&variant=43034794721478?utm_source=868-930MHz8dBiFiberGlassAntenna&utm_medium=Document&utm_campaign=BuyFromStore)

> **Image:** RAK Hotspot V2 + Converter Cable + Fiberglass Antenna

### Scenario 3 (Outdoor, Optimal)

Products Used:

- [RAK Hotspot V2](https://store.rakwireless.com/products/rak-hotspot-miner?utm_source=RAKHotspotMiner&utm_medium=Document&utm_campaign=BuyFromStore)
- [Outdoor Enclosure Kit RAKBox-GW-3](https://store.rakwireless.com/products/Outdoor-Enclosure-Kit-H?utm_source=OutdoorEnclosureKitH&utm_medium=Document&utm_campaign=BuyFromStore)
- [Lightning Arrestor](https://store.rakwireless.com/products/lightning-arrestor?utm_source=GPS-SPD&utm_source=docs_center&utm_medium=organic&utm_campaign=rak_hotspot_v2_documentation_troubleshooting_page&utm_term=lightning_arrestor&utm_content=store_link)
- [Fiberglass Antenna](https://store.rakwireless.com/products/fiber-glass-antenna-1?m=2&h=helium-antenna&variant=43034794721478?utm_source=868-930MHz8dBiFiberGlassAntenna&utm_medium=Document&utm_campaign=BuyFromStore)

> **Image:** RAK Hotspot V2 + Outdoor Enclosure Kit RAKBox-GW-3 + Lightning Arrestor + Fiberglass Antenna

### Scenario 4 (Outdoor, Suboptimal)

Products Used:

- [RAK Hotspot V2](https://store.rakwireless.com/products/rak-hotspot-miner?utm_source=RAKHotspotMiner&utm_medium=Document&utm_campaign=BuyFromStore)
- Converter Cable (included with any of the Fiberglass Antennas)
- [Lightning Arrestor](https://store.rakwireless.com/products/lightning-arrestor?utm_source=GPS-SPD&utm_source=docs_center&utm_medium=organic&utm_campaign=rak_hotspot_v2_documentation_troubleshooting_page&utm_term=lightning_arrestor&utm_content=store_link)
- [Fiberglass Antenna](https://store.rakwireless.com/products/fiber-glass-antenna-1?m=2&h=helium-antenna&variant=43034794721478)

> **Image:** RAK Hotspot V2 + Converter Cable + Lightning Arrestor + Fiberglass Antenna

### Scenario 5 (Outdoor, Suboptimal)

Products Used:

- [RAK Hotspot V2](https://store.rakwireless.com/products/rak-hotspot-miner?utm_source=RAKHotspotMiner&utm_medium=Document&utm_campaign=BuyFromStore)
- [Pulsar Cable LMR400 RAK9733](https://store.rakwireless.com/products/pulsar-cable-rak9731-rak9733?utm_source=RAK9733&utm_medium=Document&utm_campaign=BuyFromStore)
- [Fiberglass Antenna](https://store.rakwireless.com/products/fiber-glass-antenna-1?m=2&h=helium-antenna&variant=43034794721478?utm_source=868-930MHz8dBiFiberGlassAntenna&utm_medium=Document&utm_campaign=BuyFromStore)

> **Image:** RAK Hotspot V2 + Pulsar Cable LMR400 RAK9733 + Fiberglass Antenna

### Scenario 6 (Outdoor, Suboptimal)

Products Used:

- [RAK Hotspot V2](https://store.rakwireless.com/products/rak-hotspot-miner?utm_source=RAKHotspotMiner&utm_medium=Document&utm_campaign=BuyFromStore)
- [Pulsar Cable LMR400 RAK9733](https://store.rakwireless.com/products/pulsar-cable-rak9731-rak9733?utm_source=RAK9733&utm_medium=Document&utm_campaign=BuyFromStore)
- [Lightning Arrestor](https://store.rakwireless.com/products/lightning-arrestor?utm_source=GPS-SPD&utm_source=docs_center&utm_medium=organic&utm_campaign=rak_hotspot_v2_documentation_troubleshooting_page&utm_term=lightning_arrestor&utm_content=store_link)
- [Fiberglass Antenna](https://store.rakwireless.com/products/fiber-glass-antenna-1?m=2&h=helium-antenna&variant=43034794721478?utm_source=868-930MHz8dBiFiberGlassAntenna&utm_medium=Document&utm_campaign=BuyFromStore)

> **Image:** RAK Hotspot V2 + Pulsar Cable LMR400 RAK9733 + Lightning Arrestor + Fiberglass Antenna

### Scenario 7 (Outdoor, Suboptimal)

Products Used:

- [RAK Hotspot V2](https://store.rakwireless.com/products/rak-hotspot-miner?utm_source=RAKHotspotMiner&utm_medium=Document&utm_campaign=BuyFromStore)
- [Outdoor Enclosure Kit RAKBox-GW-3](https://store.rakwireless.com/products/Outdoor-Enclosure-Kit-H?utm_source=OutdoorEnclosureKitH&utm_medium=Document&utm_campaign=BuyFromStore)
- [Fiberglass Antenna](https://store.rakwireless.com/products/fiber-glass-antenna-1?m=2&h=helium-antenna&variant=43034794721478?utm_source=868-930MHz8dBiFiberGlassAntenna&utm_medium=Document&utm_campaign=BuyFromStore)

> **Image:** RAK Hotspot V2 + Outdoor Enclosure Kit RAKBox-GW-3 + Fiberglass Antenna

### Scenario 8 (Outdoor, Suboptimal)

Products Used:

- [RAK Hotspot V2](https://store.rakwireless.com/products/rak-hotspot-miner?utm_source=RAKHotspotMiner&utm_medium=Document&utm_campaign=BuyFromStore)
- [Outdoor Enclosure Kit RAKBox-GW-3](https://store.rakwireless.com/products/Outdoor-Enclosure-Kit-H?utm_source=OutdoorEnclosureKitH&utm_medium=Document&utm_campaign=BuyFromStore)
- [Pulsar Cable LMR400 RAK9731](https://store.rakwireless.com/products/pulsar-cable-rak9731-rak9733?utm_source=RAK9731&utm_medium=Document&utm_campaign=BuyFromStore)
- [Fiberglass Antenna](https://store.rakwireless.com/products/fiber-glass-antenna-1?m=2&h=helium-antenna&variant=43034794721478)

> **Image:** RAK Hotspot V2 + Outdoor Enclosure Kit RAKBox-GW-3 + Pulsar Cable LMR400 RAK9731 + Fiberglass Antenna

### Scenario 9 (Outdoor, Suboptimal)

Products Used:

- [RAK Hotspot V2](https://store.rakwireless.com/products/rak-hotspot-miner?utm_source=RAKHotspotMiner&utm_medium=Document&utm_campaign=BuyFromStore)
- [Outdoor Enclosure Kit RAKBox-GW-3](https://store.rakwireless.com/products/Outdoor-Enclosure-Kit-H?utm_source=OutdoorEnclosureKitH&utm_medium=Document&utm_campaign=BuyFromStore)
- [Pulsar Cable LMR400 RAK9731](https://store.rakwireless.com/products/pulsar-cable-rak9731-rak9733?utm_source=RAK9731&utm_medium=Document&utm_campaign=BuyFromStore)
- [Lightning Arrestor](https://store.rakwireless.com/products/lightning-arrestor?utm_source=GPS-SPD&utm_source=docs_center&utm_medium=organic&utm_campaign=rak_hotspot_v2_documentation_troubleshooting_page&utm_term=lightning_arrestor&utm_content=store_link)
- [Fiberglass Antenna](https://store.rakwireless.com/products/fiber-glass-antenna-1?m=2&h=helium-antenna&variant=43034794721478?utm_source=868-930MHz8dBiFiberGlassAntenna&utm_medium=Document&utm_campaign=BuyFromStore)

> **Image:** RAK Hotspot V2 + Outdoor Enclosure Kit RAKBox-GW-3 + Pulsar Cable LMR400 RAK9731 + Lightning Arrestor + Fiberglass Antenna

