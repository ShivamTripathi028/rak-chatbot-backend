---
slug: /product-categories/wisgate/rak10701-plus/field-test/
title: Conduct Field Tests With RAK10701-Plus Field Tester for LoRaWAN
description: Get the detailed workflow on how to conduct field tests with the Field Tester Plus, analyze real-time metrics, and export structured reports. 
image: https://images.docs.rakwireless.com/wisnode/rak10701/quickstart/physical-interface.png
keywords:
    - lorawan
    - field tester plus
    - conduct a field test with field tester plus
    - rak10701-plus
    - network coverage solution device
sidebar_label: Field Test With Field Tester Plus
tags:
  - rak10701-plus
  - field tester plus
  - network coverage solution
  - field test
date: 2025-05-23
---

import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkImage from '@site/src/components/Image'


# Conduct Field Tests With RAK10701-Plus Field Tester for LoRaWAN

This document outlines standard and scenario-based field testing workflows designed to accurately validate LoRaWAN coverage and network quality in real-world conditions.

## How Field Tester Plus Works?

Before performing field testing, it’s important to understand how the Field Tester Plus operates under different conditions.
After powering on and connecting to a LoRaWAN Network Server (LNS), the Field Tester Plus operates in one of two modes depending on your gateway setup:

<table>
  <thead>
    <tr>
      <th>Mode</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Field Tester Mode (Extension Installed)</b></td>
      <td>Full metric reporting, including uplink and downlink RSSI/SNR, packet loss, and CSV report generation.</td>
    </tr>
    <tr>
      <td><b>LinkCheck Mode (No Extension Installed)</b></td>
      <td>Limited to Downlink RSSI/SNR and gateway count only. No uplink analysis or CSV export available.</td>
    </tr>
    </tbody>
</table>

The following workflow summarizes the field testing preparation and execution:


<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/field-test/field-tester-workflow.png"
  width="45%"
  caption="Field Tester Workflow"
/>

## Standard Testing Procedure

### Pre-Test Checklist

Before beginning field tests, confirm the following:

- **Environmental Setup**: Confirm gateway installation and area accessibility.
- **Device Setup**:
    - Set the LoRaWAN Frequency Band.
    - Configure OTAA parameters via **WisToolBox** (if required).
    - Ensure the antenna is connected securely.
- **Network Setup:**
    - Register the Field Tester Plus and gateway to the same LNS.
- Install Field Test Data Processor Extension to enable full metric reporting.

### Test Execution

1. Power on the Field Tester Plus (press and hold the side button for 5 seconds).
2. Wait for LoRaWAN join confirmation (Joined status will appear).
3. Adjust device settings if needed:
    - TX Interval
    - Data Rate (DR)
    - ADR ON/OFF
4. Relocate the device to the physical test point you want to evaluate.
5. Trigger uplinks manually (double-press the button) or wait for auto-sending.

**Real-time displayed metrics** (in Field Tester Mode):

- **Uplink Metrics**: RSSI, SNR, Packet Loss, Data Rate.
- **Downlink Metrics**: RSSI, SNR, Packet Loss, Data Rate.
- **MAX Distance**: Estimated distance to the farthest gateway (requires GPS; minimum resolution is 250&nbsp;meters).
- **MIN Distance**: Estimated distance to the nearest gateway (requires GPS; minimum resolution is 250&nbsp;meters).
- **Gateway Count**: Number of gateways that successfully received the last uplink.
- **Location**: GPS coordinates (if GPS available) or manually entered Location Label for indoor or GPS-denied environments.

:::tip NOTE
You can also monitor real-time test data through the **Field Test Data Processor Extension** on your WisGateOS 2 gateway, which provides a broader view including all recent packets, signal quality, and heatmap visualization.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/field-test/field-tester-data-overview.png"
  width="100%"
  caption="Field Tester Data Overview"
/>

### Manual Labeling (Optional)

You can assign a Location Label to mark specific test points for easier data organization and analysis.

By default, the label is set to **NULL**. If it is not updated, the test data will be excluded from the CSV file.

**To set a label:**

1. Tap the gear icon to open **SETTINGS**.
2. The **Label (NULL)** field will blink by default.
3. Tap ![up arrow icon](https://images.docs.rakwireless.com/wisnode/rak10701-plus/network-setup/up-arrow.png) to open the on-screen keyboard.
4. Enter a label (up to 6 characters) and press **enter**.
5. The labeled test cycle (usually 50 packets) will begin.

### Post-Test Data Analysis (Data Export and Interpretation)

After completing field testing, you can export the structured test data for further analysis.

#### Export the Test Data

1. Open the **Field Test Data Processor Extension** UI on your WisGateOS 2 gateway.
2. Go to **Device Overview** page and click the **Export** button located in the top-right corner.
3. Download the generated CSV report.

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/field-test/field-tester-csv-file.png"
  width="100%"
  caption="Field Tester CSV File"
/>

**Contents of the CSV Report**

Each row in the CSV file corresponds to a **labeled test point.**

<table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>label</b></td>
      <td>Location label manually entered.</td>
    </tr>
    <tr>
      <td><b>time</b></td>
      <td>UTC timestamp when the data was recorded.</td>
    </tr>
    <tr>
      <td><b>rssi</b></td>
      <td>Uplink signal strength (Received Signal Strength Indicator).</td>
    </tr>
    <tr>
      <td><b>snr</b></td>
      <td>Uplink signal-to-noise ratio.</td>
    </tr>
    <tr>
      <td><b>signal_quality</b></td>
      <td>Qualitative signal evaluation (e.g., Excellent, Good, Poor).</td>
    </tr>
    <tr>
      <td><b>dr</b></td>
      <td>LoRaWAN data rate used during transmission.</td>
    </tr>
    <tr>
      <td><b>region</b></td>
      <td>LoRaWAN frequency band (e.g., EU868, US915).</td>
    </tr>
    <tr>
      <td><b>total receive</b></td>
      <td>Number of uplink packets received.</td>
    </tr>
    <tr>
      <td><b>total send</b></td>
      <td>Number of uplink packets sent.</td>
    </tr>
    <tr>
      <td><b>packet loss rate</b></td>
      <td>Percentage of lost packets.</td>
    </tr>
    <tr>
      <td><b>latitude</b></td>
      <td>GPS latitude (if available).</td>
    </tr>
    <tr>
      <td><b>longitude</b></td>
      <td>GPS longitude (if available).</td>
    </tr>
    <tr>
      <td><b>gwCount</b></td>
      <td>Number of gateways that successfully received the uplink.</td>
    </tr>
    <tr>
      <td><b>num_1_gateway_eui</b></td>
      <td>EUI of the nearest receiving gateway.</td>
    </tr>
    <tr>
      <td><b>num_1_gateway_distance</b></td>
      <td>Estimated distance to the nearest gateway (requires GPS, minimum resolution: 250&nbsp;meters).</td>
    </tr>
    <tr>
      <td><b>Label Final PLR</b></td>
      <td>Final packet loss rate calculated after completing the label cycle.</td>
    </tr>
    </tbody>
</table>

#### Signal Quality Reference

<RkImage
  src="https://images.docs.rakwireless.com/wisnode/rak10701-plus/field-test/signal-quality-reference.png"
  width="100%"
  caption="Signal Quality Reference"
/>

<table>
  <thead>
    <tr>
      <th>Metric</th>
      <th>Ideal Range</th>
      <th>When to Take Action</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>RSSI (Received Signal Strength Indicator)</b></td>
      <td>-30&nbsp;dBm to -90&nbsp;dBm</td>
      <td>If below -120&nbsp;dBm, signal is very weak and likely unusable → Consider adding a gateway or adjusting placement</td>
    </tr>
    <tr>
      <td><b>SNR (Signal-to-Noise Ratio)</b></td>
      <td>Greater than 0&nbsp;dB</td>
      <td>If below 0&nbsp;dB, especially -10&nbsp;dB or worse, interference is likely → Check for RF noise or obstructions.</td>
    </tr>
    <tr>
      <td><b>Packet Loss Rate</b></td>
      <td>≤ 5&nbsp;%</td>
      <td>If above 20%, this indicates unstable connectivity → Improve antenna setup or enhance coverage area.</td>
    </tr>
    </tbody>
</table>

## Scenario-Based Field Testing

This section explains how to apply the Field Tester Plus in different real-world situations to optimize LoRaWAN network deployment, coverage validation, and performance evaluation.

### Pre-Deployment Gateway Planning

Identify the optimal locations for new gateways to maximize coverage and network performance.

**Testing Steps**

At each candidate site:
1. Place the Field Tester Plus stationary position.
2. Transmit at least 50 uplinks (automatic or manual).
3. Record the following key metrics:
    - **RSSI** (Target: > -90&nbsp;dBm)
    - **SNR** (Target: > 0&nbsp;dB)
    - **Packet Loss** (Threshold: < 5%)

**Data Analysis**

1. Export the CSV report from the Field Test Data Processor Extension.
2. Analyze average RSSI, SNR, and packet loss at each site.

**Recommendations Based on Results**

<table>
  <thead>
    <tr>
      <th>Issue</th>
      <th>Possible Cause</th>
      <th>Recommended Action</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Weak signal (RSSI < -120&nbsp;dBm)</b></td>
      <td>Excessive distance from the gateway</td>
      <td>Install a new gateway closer to the affected coverage area</td>
    </tr>
    <tr>
      <td><b>High interference (SNR < -10&nbsp;dB)</b></td>
      <td>Environmental RF noise or obstacles</td>
      <td>Change frequency or relocate the gateway</td>
    </tr>
    <tr>
      <td><b>High packet loss (>20&nbsp;%)</b></td>
      <td>Obstructed signal path or poor backhaul connectivity</td>
      <td>Deploy additional gateways or optimize the placement of the existing gateway</td>
    </tr>
    </tbody>
</table>

### Post-Deployment Coverage Validation

Verify that installed gateways provide reliable coverage across the operational area.

**Testing Steps**

1. **Prioritize critical test points**:
    - **Access Points** (Entries/Exits): Validate seamless device onboarding.
    - **Structural Challenges** (Basements/Elevators): Assess signal penetration in difficult environments.
    - **High-Traffic Areas** (Retail Spaces): Check network resilience under load.
2. **At each test location**:
    - Assign descriptive labels to test points (e.g., B1-Parking-A12).
    - Complete at least **50 uplinks** to ensure statistical reliability.
3. **For critical zones** (Optional Best Practice):
    - Conduct measurements at different times of the day—morning, afternoon, and peak hours—to capture signal variations.
4. **Record the following key metrics**:
    - **RSSI** (Target: > -90&nbsp;dBm)
    - **SNR** (Target: > 0&nbsp;dB)
    - **Packet Loss Rate** (Threshold: < 5%)

**Data Analysis**
- Correlate packet loss with physical obstructions (via labeled test points)
- Observe whether **RSSI, SNR, or packet loss** fluctuates throughout the day.

**Recommendations Based on Results**


<table>
  <thead>
    <tr>
      <th>Finding</th>
      <th>Interpretation</th>
      <th>Recommended Action</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Low RSSI (Weak Signal)</b></td>
      <td>Gateway coverage is insufficient</td>
      <td>Reposition the gateway or deploy a repeater</td>
    </tr>
    <tr>
      <td><b>Poor SNR (High Interference)</b></td>
      <td>Signal is blocked or distorted by obstacles</td>
      <td>Investigate the surroundings, adjust the frequency, or reposition the gateway</td>
    </tr>
    <tr>
      <td><b>High Packet Loss</b></td>
      <td>Fluctuating or unstable connections</td>
      <td>Enable ADR or lower the data rate (e.g., DR3 → DR2)</td>
    </tr>
    </tbody>
</table>


:::tip NOTE
After adjusting the network (moving gateway, adjusting power, etc.), repeat the testing cycle to validate performance improvements.
:::

### Maximum Coverage Distance Testing

Determine the maximum effective communication distance from a gateway under real deployment conditions.

**Radial Testing Pattern**
1. Start at the gateway's location (0 meters).
2. Walk outward along different radial paths from the gateway.
3. Maintain a consistent walking speed (~1&nbsp;m/s) and antenna orientation.

**Real-Time Monitoring:**
- **Distance**: Measures via GPS (if available) or through manual tracking.
- **RSSI**: Triggers an alert if it drops below –120&nbsp;dBm.
- **Packet Loss Rate**: Triggers an alert if it exceeds 20%.

**Recommendations Based on Results**


<table>
  <thead>
    <tr>
      <th>Problem</th>
      <th>Cause</th>
      <th>Solution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>RSSI < -120&nbsp;dBm</b></td>
      <td>Signal strength is too weak</td>
      <td>Increase transmission power or antenna gain</td>
    </tr>
    <tr>
      <td><b>Packet Loss Rate > 20&nbsp;%</b></td>
      <td>Instability in the communication link</td>
      <td>Reduce the data rate (e.g., DR1 to DR0)</td>
    </tr>
    <tr>
      <td><b>Join Failures</b></td>
      <td>Gateway is too far from the device</td>
      <td>Deploy more gateways to improve coverage density</td>
    </tr>
    </tbody>
</table>

<RkBottomNav/>