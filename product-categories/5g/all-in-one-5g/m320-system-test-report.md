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

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# All-in-One 5G. M320 System Test Report

## Overview

This test report applies to the All-in-One 5G and is mainly a test for NR-related functions. The test items covered in this report mainly include basic function tests, performance tests, coverage tests, and stability tests.

- With a **5&nbsp;ms** cycle and a **6:4:5** slot ratio, 5G NR achieves a maximum downlink throughput of up to **270&nbsp;Mbps** and uplink throughput of up to **40&nbsp;Mbps**.
- With a **TDD config2** configuration, 4G LTE achieves a maximum downlink throughput of up to **106&nbsp;Mbps** and uplink throughput of up to **13&nbsp;Mbps**.
- Both gNodeB and eNodeB successfully passed the FTP download stability test over 7 days
- At **45&nbsp;m** away and invisible test point, 5G achieved **150&nbsp;Mbps** downlink and **19&nbsp;Mbps** uplink
- At **50&nbsp;m** away and invisible test point, LTE achieved **19&nbsp;Mbps** downlink and **200&nbsp;Kbps** uplink

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

<RkImage
img src="https://images.docs.rakwireless.com/5g/all-in-one-5g/test-report/image-20240426151713590.png" 
width="60%" 
/>

## Test Result

### Performance Test

#### 5G NR Performance Test

| Cycle/Slot Ratio | Test Point                            | Downlink Average Throughput | Uplink Average Throughput |
|------------------|---------------------------------------|-----------------------------|---------------------------|
| 5&nbsp;ms, 6:4:4 | Excellent - very good signal strength | 270&nbsp;Mbps               | 40&nbsp;Mbps              |

<RkImage
img src="https://images.docs.rakwireless.com/5g/all-in-one-5g/test-report/image-20240426152147481.png" 
width="60%" 
/>

<RkImage
img src="https://images.docs.rakwireless.com/5g/all-in-one-5g/test-report/image-20240426152305933.png" 
width="60%" 
/>

#### 4G LTE Performance Test

| Cycle/Slot Ratio | Test Point                            | Downlink Average Throughput | Uplink Average Throughput |
|------------------|---------------------------------------|-----------------------------|---------------------------|
| TDD config2      | Excellent - very good signal strength | 106&nbsp;Mbps               | 13&nbsp;Mbps              |


<RkImage
img src="https://images.docs.rakwireless.com/5g/all-in-one-5g/test-report/image-20240426152546550.png" 
width="100%" 
/>


<RkImage
img src="https://images.docs.rakwireless.com/5g/all-in-one-5g/test-report/image-20240426152615335.png" 
width="100%" 
/>

## Stability Test



| Test Case                     | Duration of Operation | Test Result |
|-------------------------------|-----------------------|-------------|
| 5G NR 32 UE FTP Download Test | 7                     | Pass        |
| LTE 32 UE FTP Download Test   | 7                     | Pass        |


<RkImage
img src="https://images.docs.rakwireless.com/5g/all-in-one-5g/test-report/image-20240426153313647.png" 
width="100%" 
/>

<RkImage
img src="https://images.docs.rakwireless.com/5g/all-in-one-5g/test-report/image-20240426153346729.png" 
width="70%" 
/>

#### Test Captures

<RkImage
img src="https://images.docs.rakwireless.com/5g/all-in-one-5g/test-report/image-20240426153415756.png" 
width="100%" 
/>

<RkImage
img src="https://images.docs.rakwireless.com/5g/all-in-one-5g/test-report/image-20240426153440701.png" 
width="50%" 
/>

### Coverage Test

<RkImage
img src="https://images.docs.rakwireless.com/5g/all-in-one-5g/test-report/image-20240426160948756.png" 
width="100%" 
/>

#### Test Result

<b>5G NR Coverage Test Result</b>

| 5G Test Point | RSRP0 | RSRP1 | SINR | DL&nbsp;Mbps  | UL              | Visibility          | Distance  |
|---------------|-------|-------|------|---------------|-----------------|---------------------|-----------|
| Point B       | -96   | -96   | 24   | 212&nbsp;Mbps | 20-24&nbsp;Mbps | Invisible           | 9&nbsp;m  |
| Point C       | -100  | -100  | 20   | 200&nbsp;Mbps | 21-22&nbsp;Mbps | Invisible           | 20&nbsp;m |
| Point D       | -96   | -96   | 26   | 234&nbsp;Mbps | 25-26&nbsp;Mbps | Basically Visible   | 23&nbsp;m |
| Point E       | -90   | -90   | 28   | 255&nbsp;Mbps | 30&nbsp;Mbps    | Invisible           | 34&nbsp;m |
| Point F       | -109  | -109  | 14   | 150&nbsp;Mbps | 19-20&nbsp;Mbps | Invisible           | 45&nbsp;m |
| Point G       | -121  | -121  | NA   | NA            | NA              | Invisible & Dropped | 50&nbsp;m |

<b>4G LTE Coverage Test Result</b>

| 4G Test Point | RSRP0 | RSRP1 | SINR | DL&nbsp;Mbps | UL                | Visibility          | Distance  |
|---------------|-------|-------|------|--------------|-------------------|---------------------|-----------|
| Point B       | -89   | -83   | 28   | 76&nbsp;Mbps | 6.3&nbsp;Mbps     | Invisible           | 9&nbsp;m  |
| Point C       | -83   | -90   | 28   | 24&nbsp;Mbps | 8&nbsp;Mbps       | Invisible           | 20&nbsp;m |
| Point D       | -91   | -85   | 28   | 85&nbsp;Mbps | 2.1&nbsp;Mbps     | Basically Visible   | 23&nbsp;m |
| Point E       | -88   | -90   | 27   | 92&nbsp;Mbps | 3&nbsp;Mbps       | Invisible           | 34&nbsp;m |
| Point F       | -97   | -97   | 27   | 98&nbsp;Mbps | 2.2&nbsp;Mbps     | Invisible           | 45&nbsp;m |
| Point G       | -115  | -118  | 10   | 19&nbsp;Mbps | 0.2-0.3&nbsp;Mbps | Invisible & Dropped | 50&nbsp;m |
| Point H       | -127  | -117  | 5    | NA           | NA                | Invisible & Dropped | 60&nbsp;m |


<RkBottomNav/>