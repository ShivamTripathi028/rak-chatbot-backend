---
slug: /product-categories/wisgate/rak10701-plus/faqs-troubleshooting/
title: RAK10701-Plus Field Tester for LoRaWAN
description: Learn how to troubleshoot your Field Tester Plus for LoRaWAN and find solutions to common issues.  
image: https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/physical-interface.png
keywords:
    - lorawan
    - field tester plus
    - rak10701-plus
    - field tester plus issues
    - troubleshoot field tester plus
sidebar_label: FAQs & Troubleshooting
tags:
  - rak10701-plus
  - field tester plus
  - network coverage solution
  - faqs
  - troubleshooting
date: 2025-05-23
---

# Field Tester Plus for LoRaWAN FAQs & Troubleshooting

Find quick solutions to common problems, detailed explanations of testing concepts, and tips for optimizing your LoRaWAN field testing results.

## Troubleshooting Guide

| Issue | Possible Cause | Suggested Solution |
| --- | --- | --- |
| No network connection | - Incorrect OTAA parameters (DevEUI, AppEUI, AppKey) - Device not within range of a gateway - LNS not configured to accept device | - Verify that OTAA parameters match on both device and LNS - Ensure gateway is powered and within range - Check LNS logs for join requests |
| Device stuck at "Joining" or "Failed" status | - OTAA failed due to wrong credentials or no downlink - Gateway cannot reach device (downlink path issue) | - Check Field Tester status display and LNS console - Move closer to the gateway - Confirm the gateway can send downlinks (LinkCheck test) |
| Only downlink data is shown (no uplink or packet loss) | - Field Test Extension is not installed or not integrated - LNS is not supported | - Confirm that Field Test Extension is installed on the gateway - If not supported, the device is in LinkCheck Mode |
| High packet loss | - Intermittent gateway reception - Physical obstructions - Too far from gateway - Interference from other RF sources | - Try testing in open areas or reposition the gateway - Reduce Data Rate (DR) for longer range - Switch to a higher TX power setting |
| Low SNR or RSSI | - RF interference - Testing location is poorly covered | - Identify and avoid areas near large metal structures or high interference sources - Move closer to gateway or use a lower DR |
| GPS not updating | - Indoor environment - Weak satellite signal | - Move the device outdoors with a clear view of the sky - Wait a few minutes for satellite lock |
| Label is missing in CSV report | - Location label not set before testing | - Go to Settings > Label and set a custom label before starting test (see Section 5) - If GPS is unavailable, labeling is essential for report clarity |
| Button press not detected | - Device is busy (sending packets) - Button press too quick | - Wait until the current transmission is complete - Press and hold longer until blue indicator appears |

## Frequently Asked Questions

### 1. Why Do We Need the Field Test Extension?

The **Field Test Extension** enables local signal processing on **WisGateOS 2-based gateways**, allowing the Field Tester Plus to perform full-featured testing, even in offline or indoor environments. It allows the system to:
- Process **uplink and downlink signal metrics** in real time
- **Calculate packet loss** and **distance to gateways** (when GPS is available)
- **Export structured CSV reports** for coverage analysis

### 2. Why Do I Need Downlink Data?

Downlink data helps you understand how well the device hears the gateway — not just how well the gateway hears the device. **This is important for**:
- Validating bi-directional communication (e.g., OTAA joins, confirmed messages)
- Ensuring control or command messages from the network can reach the device
- Diagnosing coverage issues in indoor or edge environments

### 3. Why Does the Field Tester Plus Come With Multiple Antennas?

LoRaWAN end devices in real-world deployments use **different types of antennas** — some with better range and gain, others with compact but lower performance.
By testing with **multiple antenna** types, you can:
- **Simulate different end device conditions** (e.g., long-range sensor vs. compact tracker)
- **Reflect the diversity of antenna performance** across real deployments
- **Collect more objective and realistic signal data** by accounting for antenna gain differences
- Identify **coverage weak spots** that might be hidden when only using a high-gain antenna.

Using a **lower-gain antenna** during testing can help you detect **borderline coverage areas**, ensuring the network supports even the weaker RF devices.

### 4. Why Am I Only Seeing Downlink Metrics?

This usually means the **Field Test data processor Extension** is not installed or not integrated with your network server.
In this case, the device operates in **LinkCheck Mode**, which allows:
- Basic downlink evaluation via LinkCheck responses
- No uplink RSSI, packet loss, or distance calculations

### 5. Can I Use the Field Tester Plus Indoors?

Yes — the Field Tester Plus works indoors, but with some limitations:
- **GPS location and distance to gateway** will not be available
- You must use **manual location labels** to identify test points in reports
- Signal conditions may vary due to obstructions like walls or metal structures

### 6. What Happens If I Forget to Label a Test Point?

If the location label remains NULL:
- That test point **will not be saved in the CSV report**
- Your data will be **missing or unlabeled**, which makes post-analysis difficult

### 7. What’s the Difference Between Field Tester Plus and Old Field Tester Pro?

| Issue | Possible Cause | Suggested Solution |
| --- | --- | --- |
| Uplink RSSI/SNR | YES |  |
| Uplink Packet Loss Rate | YES |  |
| Downlink RSSI/SNR | YES | YES |
| Downlink Packet Loss Rate | YES |  |
| Lat/Long GPS Info | YES | YES |
| Max Distance | YES | YES |
| Min Distance | YES | YES |
| Label Display | YES |  |
| Label Setting | YES |  |
| Stop or Start Sending Button | YES |  |
| Last Refresh | YES |  |
| Gateway EUI | YES |  |
| No. of Gateway | YES |  |
| Historical Data | YES | YES |
| Touchscreen Setting | YES | YES |
| Device Status | YES | YES |
| CSV Data Export | YES |  |
| Offline Local Server | YES |  |
| LinkCheck Mode | YES |  |

### 8. What Do the Fault Codes Mean?

| Fault Code | Description |
| --- | --- |
| GPS INIT FAILED | GPS module initialization error. Check module connection; replace GPS if issue persists. |
| TP INIT FAILED | Touch panel initialization error. Check screen connection; replace screen module if issue persists. |
| FLASH INIT FAILED | Internal flash error. May indicate RAK4631 failure; replace RAK4631 module. |
| LORA INIT FAILED | LoRa chip error. May indicate RAK4631 failure; replace RAK4631 module. |
| LOW VOLTAGE | Battery is critically low; recharge immediately. |

> **Image:** RAK10701-Plus GPS Failure

### 9. How Is the Distance to Gateways Calculated?

RAK10701-Plus calculates the estimated distance to gateways using GPS. Here’s how it works:

- The device obtains its GPS location (outdoor only).
- The gateway must have a known location (latitude/longitude set in the system).
- The distance between the device and the gateway is then calculated and displayed as:
    - Nearest Gateway Distance
    - Farthest Gateway Distance
- The unit of distance is meters, with a minimum unit of 250 meters.

:::tip NOTE
Note: This feature only works in outdoor environments with active GPS.
:::

### 10. How Is Packet Loss Calculated?

Packet loss is calculated based on the frame sequence number. Each uplink or downlink message carries a frame sequence number in the application layer data. The sequence number increments by 1 for each packet sent. Here’s the calculation method:

**Frame Sequence Number**:

Uplink messages use 2 bytes for the frame sequence number, with a range of 1-65535.
Downlink messages use 1.5 bytes (12 bits) for the frame sequence number, with a range of 1-4095.

When the frame sequence number exceeds the maximum value, it will restart from 1.

**Packet Loss Rate Calculation**:

Both uplink and downlink packet loss rates use a sliding window method with a window size of 50.
Each time a message is received, the frame number is added to the sliding window. If the window contains fewer than 50 packets, the actual number of received packets is counted.
When the sliding window is full (50 messages), the oldest frame number is removed from the window, and the latest frame number is added.

**Example**:

If the received frame numbers are 2, 4, and 5, the theoretical number of received packets is `5 - 2 + 1 = 4`, and the actual number of received packets is 3, so the packet loss rate is `(4 - 3) / 4 = 25%`.
After the window is full with 50 messages, the packet loss rate is calculated based on the most recent data in the window.

:::tip NOTE
The sliding window will be cleared, and the frame number reset each time a label is updated.
:::

