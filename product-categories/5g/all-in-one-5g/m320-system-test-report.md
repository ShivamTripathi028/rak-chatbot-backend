---
title: All-in-One 5G. M312 System Test Report
description: Displays the All-in-One 5G test requirements and results in different areas and work scenarios. This ensures that your All-in-One 5G device can operate and perform efficiently in various conditions.
image: "https://images.docs.rakwireless.com/5g/all-in-one-5g/all-in-one-5g.png"
keywords:
  - All-in-One 5G
  - 5G
  - Test Report
sidebar_label: M320 System Test Report
slug: /product-categories/5g/all-in-one-5g/m320-system-test-report/
---

# All-in-One 5G. M320 System Test Report

## Overview

This test report applies to the All-in-One 5G and is mainly a test for NR-related functions. The test items covered in this report mainly include basic function tests, performance tests, coverage tests, and stability tests.

- With a **5 ms** cycle and a **6:4:5** slot ratio, 5G NR achieves a maximum downlink throughput of up to **270 Mbps** and uplink throughput of up to **40 Mbps**.
- With a **TDD config2** configuration, 4G LTE achieves a maximum downlink throughput of up to **106 Mbps** and uplink throughput of up to **13 Mbps**.
- Both gNodeB and eNodeB successfully passed the FTP download stability test over 7 days
- At **45 m** away and invisible test point, 5G achieved **150 Mbps** downlink and **19 Mbps** uplink
- At **50 m** away and invisible test point, LTE achieved **19 Mbps** downlink and **200 Kbps** uplink

#### Test Equipments

| Name         | Count   | Description                          |
|--------------|---------|--------------------------------------|
| M320         | Several | Runs eNodeB & gNodeB together        |
| External 5GC | 1       | External 5GC serve gNodeB and 5G UEs |
| External EPC | 1       | External EPC serve eNodeB and 4G UEs |
| OMC          | 1       | radio configuration                  |
| FTP server   | Several | FTP download and upload test server  |
| UE           | 32      | Multi UEs simulator                  |
| CPE          | 32      | Real physical 4G & 5G UEs            |

#### Network Topology

## Test Result

### Performance Test

#### 5G NR Performance Test

| Cycle/Slot Ratio | Test Point                            | Downlink Average Throughput | Uplink Average Throughput |
|------------------|---------------------------------------|-----------------------------|---------------------------|
| 5 ms, 6:4:4 | Excellent - very good signal strength | 270 Mbps               | 40 Mbps              |

#### 4G LTE Performance Test

| Cycle/Slot Ratio | Test Point                            | Downlink Average Throughput | Uplink Average Throughput |
|------------------|---------------------------------------|-----------------------------|---------------------------|
| TDD config2      | Excellent - very good signal strength | 106 Mbps               | 13 Mbps              |

## Stability Test

| Test Case                     | Duration of Operation | Test Result |
|-------------------------------|-----------------------|-------------|
| 5G NR 32 UE FTP Download Test | 7                     | Pass        |
| LTE 32 UE FTP Download Test   | 7                     | Pass        |

#### Test Captures

### Coverage Test

#### Test Result

**5G NR Coverage Test Result**

| 5G Test Point | RSRP0 | RSRP1 | SINR | DL Mbps  | UL              | Visibility          | Distance  |
|---------------|-------|-------|------|---------------|-----------------|---------------------|-----------|
| Point B       | -96   | -96   | 24   | 212 Mbps | 20-24 Mbps | Invisible           | 9 m  |
| Point C       | -100  | -100  | 20   | 200 Mbps | 21-22 Mbps | Invisible           | 20 m |
| Point D       | -96   | -96   | 26   | 234 Mbps | 25-26 Mbps | Basically Visible   | 23 m |
| Point E       | -90   | -90   | 28   | 255 Mbps | 30 Mbps    | Invisible           | 34 m |
| Point F       | -109  | -109  | 14   | 150 Mbps | 19-20 Mbps | Invisible           | 45 m |
| Point G       | -121  | -121  | NA   | NA            | NA              | Invisible & Dropped | 50 m |

**4G LTE Coverage Test Result**

| 4G Test Point | RSRP0 | RSRP1 | SINR | DL Mbps | UL                | Visibility          | Distance  |
|---------------|-------|-------|------|--------------|-------------------|---------------------|-----------|
| Point B       | -89   | -83   | 28   | 76 Mbps | 6.3 Mbps     | Invisible           | 9 m  |
| Point C       | -83   | -90   | 28   | 24 Mbps | 8 Mbps       | Invisible           | 20 m |
| Point D       | -91   | -85   | 28   | 85 Mbps | 2.1 Mbps     | Basically Visible   | 23 m |
| Point E       | -88   | -90   | 27   | 92 Mbps | 3 Mbps       | Invisible           | 34 m |
| Point F       | -97   | -97   | 27   | 98 Mbps | 2.2 Mbps     | Invisible           | 45 m |
| Point G       | -115  | -118  | 10   | 19 Mbps | 0.2-0.3 Mbps | Invisible & Dropped | 50 m |
| Point H       | -127  | -117  | 5    | NA           | NA                | Invisible & Dropped | 60 m |

