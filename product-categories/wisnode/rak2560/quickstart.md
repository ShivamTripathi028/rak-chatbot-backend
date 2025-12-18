---
slug: /product-categories/wisnode/rak2560/quickstart/
title: RAK2560 WisNode Sensor Hub Quickstart
description: Contains instructions and tutorials for installing and deploying your RAK2560. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: "https://images.docs.rakwireless.com/wisnode/rak2560/rak2560.jpg"
keywords:
    - RAK2560
    - quickstart
    - wisnode
    - sensor hub
sidebar_label: Quick Start Guide
---

# RAK2560 WisNode Sensor Hub Quick Start Guide

## Prerequisites

Before going through each and every step of using the RAK2560 WisNode Sensor Hub module, make sure to prepare the necessary items listed below:

### Hardware Tools

- [RAK2560 WisNode Sensor Hub](https://store.rakwireless.com/products/sensor-hub?utm_source=RAK2560WisNodeSense&utm_medium=Document&utm_campaign=BuyFromStore)
- Accessories - Sensor Probe, Probe IO, or a combination (numbers and variations depending on the use case)
- Additional accessories - Probe Cable, Probe Splitter, power supply, and others (numbers and variations depending on the use case)
- An Android or iOS mobile device with Bluetooth and NFC

### Software

- [WisToolBox](https://docs.rakwireless.com/product-categories/software-tools/wistoolbox/wistoolbox-mobile/)

> **Image:** Sensor Hub ecosystem

:::tip NOTE

WisNode Sensor Hub can be powered with batteries or a dedicated power adapter. It supports 2 to 4 battery types: ER18505 3.6 V 4000 mAh Li-SOCl2 NON-rechargeable lithium batteries which are NOT included upon purchase.

You can source the batteries locally or from one of the global electronics distributors:
1. [Amazon](https://www.amazon.com/EEMB-Capacity-Batteries-Rechargeable-Certified/dp/B07TTGW7XQ/ref=sr_1_1_sspa?crid=3Q1EZ9Y11KCKN&keywords=ER18505&qid=1676374193&sprefix=er18505%2Caps%2C201&sr=8-1-spons&psc=1&smid=A3JZ0E8P9D7DI&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExWFpINDM3V1VLVkdWJmVuY3J5cHRlZElkPUExMDE2MzEzMkRZWDVTQ1VaQURPRyZlbmNyeXB0ZWRBZElkPUEwOTc1NjU3QTFDVFBINFIwUjEyJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)
2. [Mouser](https://www.mouser.bg/ProductDetail/Ultralife/ER18505?qs=zfu6fx%252B1HVV05VN8zSGKvA%3D%3D)
3. [AliExpress](https://www.aliexpress.com/item/1005004658194639.html?spm=a2g0o.productlist.main.1.7a477185fc5rOu&algo_pvid=8404268f-c97a-4f0e-b093-fea934f49acb&algo_exp_id=8404268f-c97a-4f0e-b093-fea934f49acb-0&pdp_ext_f=%7B%22sku_id%22%3A%2212000030006218882%22%7D&pdp_npi=3%40dis%21BGN%217.95%217.15%21%21%21%21%21%402102110316763743466464381d06f9%2112000030006218882%21sea%21BG%21827888164&curPageLogUid=P9xZl9592JjT)

:::

## Product Configuration

### Power On the Sensor Hub

1. Connect the Sensor Probe/Probe IO to the port of the RAK2560-Hub.

:::warning
Do not power the Sensor Hub before connecting the sensors to avoid damage to the device.
:::

:::tip NOTE
If the Sensor Probe with Temperature, Humidity, and Pressure is used (RAK1901+RAK1902), there will be two temperature values in the WisToolBox. Due to the different accuracy of the temperature sensors, the values might be different.
:::

2. Use the power supply of your choice that is compatible with the device.

:::tip NOTE
Using the 12 V<sub>DC</sub> adapter provided with the Sensor Hub is recommended. You can also use 4 x EVE ER18505 3.6 V Lithium 4000 mAh battery and the voltage must be stable.
:::

### Device Configuration via WisToolBox

#### Accessing the Sensor Hub

1. Download and install the WisToolBox App on your smartphone.

> **Image:** WisToolBox App

2. Launch the app and make sure that the NFC is enabled on your mobile device and the Bluetooth is on. Press **SELECT DEVICE**.

> **Image:** App home screen

3. Select the connection mode to pair the device.

> **Image:** Connection mode

4. Select the Sensor Hub from the list of devices.

> **Image:** In-app list of devices

5. Pair your smartphone and the Sensor Hub by touching your phone to the **N** symbol on the front of the Hub and pressing **CONNECT** in the app. Retain the position of the smartphone touching the **N** symbol on the Hub and wait until the scan is done.

> **Image:** Pairing the Hub to your smartphone

6. Once the scan is done, a **Scan successful** message will appear.

> **Image:** Scan successful

7. Automatic synchronization will start, wait until the process is complete.

> **Image:** Device syncing

:::tip 
By default, the BLE advertising of the Sensor Hub is turned off automatically if no connection is established within 30 seconds of availability. Connect to the RAK device immediately after powering it on again.
<!-- or power it on again. -->

Some Android smartphones require GPS enabled to permit connection to BLE. When GPS is enabled, no sensitive information is used or shared with the application.
:::

#### Sensor Hub Info

When the data synchronization process is completed, you will see the **SENSOR HUB INFO** screen.

- **HARDWARE** - Product hardware version information
- **FIRMWARE** - Product software version information
- **DEVEUI** - EUI number of the device
- **HARDWARE MODEL** - Product model
- **HUB SERIAL** - The serial number of the device
- **№ SENSOR PROBES** - Number of Sensors Probes currently connected to the device
- **Documentation** - A link to the RAK Documentation center
- **Disconnect device** - Break the connection between your smartphone and the Hub

> **Image:** Sensor Hub Info

#### LoRa and LoRaWAN Parameters

In the **LORA & LORAWAN PARAMETERS** tab, you can set and see all the information needed so the device can join a network server of your choice.

1. Configure the **Join mode** and **Active region** in **Global settings**.

> **Image:** LoRa and LoRaWAN parameters screen

2. In the **Active region** menu, select the LoRaWAN band to be used.

> **Image:** Active region list

3. You can see the Sensor Hub **Application EUI**, **Application Key**, and **Device EUI** that are needed to register the device in the network.
4. You can turn on/off the **Enable auto-join** and **ADR** buttons according to your preferences.
5. Press the **Join network** button, and the device will be able to access the network, assuming you registered it properly.

#### Sensor Probe

1. In the **SENSOR PROBE** screen, you can get all the information about the connected sensors.

- **Probe ID** - The ID that the Sensor Hub uses to identify the probe (until a reset is made). Value: 1~250
- **Hardware** - Probe's type version information
- **Firmware** - Probe's software version information
- **Hardware model** - Product model
- **Probe type** - RAK2560-Probe has two WisBlock slots that allow the mount of one or two WisBlock sensor modules in the mass production phase.
- **Sensor count** - The number of sensors in the probe.

The table shows the probe, module combination, and functionalities.

| Probe | Module Combination |             |          | Function            |                     |          |
| :---: | :----------------: | :---------: | :------: | :-----------------: | :-----------------: | :------: |
|       |                    | Temperature | Humidity | Barometric Pressure | 3-Axis Acceleration | Gas      |
| A     | RAK1901            | ✔    | ✔ |                     |                     |          |
| B     | RAK1902            | ✔    | ✔ | ✔            |                     |          |
| C     | RAK1904            |             |          |                     | ✔            |          |
| D     | RAK1906            | ✔    | ✔ | ✔            |                     | ✔ |
| AB    | RAK1901+RAK1902    | ✔    | ✔ | ✔            |                     |          |
| AC    | RAK1901+RAK1904    | ✔    | ✔ |                     | ✔            |          |
| BC    | RAK1902+RAK1904    | ✔    | ✔ | ✔            | ✔            |          |
| CD    | RAK1904+RAK1906    | ✔    | ✔ | ✔            | ✔            | ✔ |

> **Image:** Synchronization in progress

> **Image:** Sensor Probe screen

2. Each sensor has a dropdown menu with the option to set some parameters as well.

> **Image:** Sensor parameters

- **Detailed sensor settings** - Configure the parameter for sending the data.

> **Image:** Detailed sensor settings

- **Sensor data** - The currently fetched data value
- **Toogle button sensor data changes** - Send data if there is any change in the sensor value
- **Sensor interval(s)** - Payload sending interval in seconds (when periodic sensor rule is used). Limit: 60~86400 seconds
- **Toogle button for periodic uplink** - Sends data in the time interval configured
- **Lower Threshold** - Set up the lower value for the sending rules
- **Upper Threshold** - Set up the upper value for the sending rules

3. The Sensor Probe sends data to the Sensor Hub according to established rules. Those rules are as follows:

| Name      | Bit | Description                                                                                                        |
| --------- | --- | ------------------------------------------------------------------------------------------------------------------ |
| Alert     | 0   | If below/above/between is triggered, the probe's sending interval will temporarily be changed to the min interval. |
| Below     | 1   | If the below threshold is triggered, data will be sent.                                                            |
| Above     | 2   | If the above threshold is triggered, data will be sent.                                                            |
| Periodic  | 3   | Data follows the sensor's send interval.                                                                           |
| Between   | 4   | Data is between the below and above the threshold values.                                                          |
| Different | 5   | Data is different than the last data.                                                                              |

** Example 1:**

```
Key = 0x03(Hex) = 0b00000011(Bin)
```

**0x03** will enable the **alert** and the **below** rules. If **below** is triggered, data will be sent to the Sensor Hub.

- 0b00000001 = Alert Enable
- 0b00000010 = Below Enable

**Example 2:**

```
Key = 0x08(Oct) = 0b00001000(Bin)
```

**0x08** will enable the **periodic** rule. The probe will send data according to the sensor's interval set.

- 0b00001000 = Periodic Enable

## Configuring Sensor Hub for LoRaWAN Usage

In this video, you can learn how to visualize your Sensor Hub data in Datacake using a WisGate Edge Gateway and TTN.

<div style={{ position: 'relative', paddingBottom: '56.25%', height: '50%', overflow: 'hidden' }}>

  <iframe
    src="https://www.youtube.com/embed/9vMRT_G1tFI?si=VmDyj5fbJEPDyX6r"
    title="Send your Sensor Hub data to Datacake using TTN and WisGate Edge"
    frameBorder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowFullScreen
    style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%' }}
  />
  
</div>

:::tip NOTE
This YouTube tutorial covers the Weather Station, but the basics apply to all solutions.
:::

