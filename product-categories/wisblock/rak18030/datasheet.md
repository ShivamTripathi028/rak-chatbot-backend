---
slug: /product-categories/wisblock/rak18030/datasheet/
title: RAK18030 WisBlock Audio PDM Microphone Module Datasheet
description: Provides comprehensive information about your RAK18030 to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisblock/rak18030/rak18030.png"
keywords:
  - datasheet
  - wisblock audio
  - RAK18030
  - SPK0641HT4H-1
  - Knowles
sidebar_label: Datasheet
---

# RAK18030 WisBlock Audio PDM Microphone Module Datasheet

## Overview

### Description

RAK18030 is a WisBlock Audio that extends the WisBlock system based on the SPK0641HT4H-1 module from Knowles. This module is a mono PDM microphone module, where the analog audio is converted to a Pulse Density Modulation (PDM) output. When used with other WisBlock modules, you can achieve rich applications such as audio monitoring, recording, and even voice control functions.

### Features

* **Sensor Specifications**
    * Voltage supply: **3.3 V ~ 3.6 V**
    * Current consumption: **26 uA ~ 800 uA**
    * Chipset: **SPK0641HT4H-1**
    * PDM Microphone
    * Left or Right Channel Selection
    * Flat frequency response: 20 Hz - 20,000 Hz
    * Low distortion of 2.2% at 115 dB SPL
    * 64.5 dB(A) Signal-to-Noise Ratio
    * Omnidirectional sensitivity

* **Module Size**
    * 15x25 mm

## Specifications

### Overview

> **Image:** RAK18030 WisBlock Audio PDM Microphone Module top and bottom view

#### Mounting

##### Mount to WisBlock Base

**Figure 2** shows the mounting mechanism of the RAK18030 module on a [WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock/quickstart/#wisblock-base) board. The RAK18030 module can be mounted on the IO slots.

> **Image:** RAK18030 mount to WisBlock Base

##### Mount to Enclosure

If you want to use the RAK18030 with an enclosure, there are two (2) mounting screw holes that are provided to mount the microphone module up against a hole in the enclosure. In this case, an FPC or a [WisBlock IO Extension Cable](https://docs.rakwireless.com/product-categories/wisblock/rak19008/overview/) is required to connect the RAK18030 to the WisBlock system.

:::tip NOTE
- The FPC with the Audio Interposer board is recommended as it provides a better mechanical mounting than the IO extension cable.
:::

> **Image:** RAK18030 mount to the enclosure

##### Mount to WisBlock Audio Stack

With the use of WisBlock Audio Spacer, the RAK18030 can be mounted to any other WisBlock Audio module. **Figure 4** shows the mounting mechanism of the RAK18030 on a WisBlock Audio Stack.

> **Image:** RAK18030 mount to WisBlock Audio Stack

### Hardware

The hardware specification is categorized into five (5) parts. It shows the chipset of the module and discusses the pinouts and their corresponding functions and diagrams. It also covers the electrical and mechanical parameters that include the tabular data of the functionalities and standard values of the RAK18030 WisBlock Audio PDM Microphone Module.

#### Chipset

| Vendor        | Part Number |
| ------------- | ----------- |
| SPK0641HT4H-1 | Knowles     |

#### Pin Definition

##### WisBlock IO Connector

The RAK18030 WisBlock Audio PDM Microphone comprises a standard WisBlock connector. The WisBlock connector allows the RAK18030 module to be mounted to a WisBlock Base board. The pin order of the connector and the pinout definition is shown in **Figure 5**.

> **Image:** RAK18030 WisBlock Module pinout diagram

:::tip NOTE
- **3V3** and **GND** are power supply from the WisBlock Base.
- **MIC_CTR_IO1** is the GPIO from WisBlock Core. The MIC can be controlled as a left or right channel.
- **MIC_PDM1_Data** and **MIC_PDM1_CLK** are PDM signals.
:::

##### WisBlock FPC Connector

The RAK18030 WisBlock Audio PDM Microphone comprises a standard FPC connector. The FPC connector allows the RAK18030 module to be connected to a WisBlock Audio Interposer board, such as RAK18003. The pin order of the connector and the pinout definition is shown in **Figure 6**.

> **Image:** RAK18030 FPC connector pinout diagram

:::tip NOTE
- **3V3** and **GND** are power supply from the WisBlock Audio Interposer board.
- **MIC_CTR_IO1** is the GPIO from the Interposer board. The MIC can be controlled as a left or right channel.
- **MIC_PDM1_Data** and **MIC_PDM1_CLK** are PDM signals.
- **MIC_Check** is a signal to let the Interposer board know if the RAK18030 exists or is connected.
:::

#### Electrical Characteristics

##### Acoustic and Electrical Specifications

| Symbol            | Description                                                                       | Min. | Nom. | Max. | Unit  |
| ----------------- | --------------------------------------------------------------------------------- | ---- | ---- | ---- | ----- |
| V<sub>DD</sub>    | Supply voltage                                                                    | 1.6  | 3.3  | 3.6  | V     |
| I<sub>dd1</sub>   | Current consumption in performacnce mode (@3.6 V)                            | -    | 700  | 800  | uA    |
| I<sub>dd2</sub>   | Current consumption in Low-Power mode (@3.6 V)                               | -    | 270  | 330  | uA    |
| I<sub>sleep</sub> | Current consumption in Sleep Mode mode (@3.6 V)                              | -    | 26   | -    | uA    |
| Sensitivity       | 94 dB SPL @ 1 kHz                                                       | -27  | -26  | -25  | dBFS  |
| SNR               | Signal-to-noise ratio (94 dB SPL @ 1 kHz, A-weighted, Performance Mode) | -    | 64.5 | -    | dB(A) |
| Clock             | Input clock frequency                                                             | 0.35 | -    | 4.8  | MHz   |
| T<sub>op</sub>    | Operating temperature range                                                       | -40  | -    | +85  | °C    |

#### Mechanical Characteristics

##### Board Dimensions

**Figure 7** shows the dimensions and the mechanical drawing of the RAK18030 module.

> **Image:** RAK18030 WisBlock Sensor mechanical drawing

##### WisBlock Connector PCB Layout

> **Image:** WisBlock Connector PCB footprint and recommendations

#### Schematic Diagram

##### Digital Microphone

The **Pin 3** of the SPK0641HT4H-1 is used to control the MIC as a left or right channel.

- The MIC is the left channel when **Pin 3** is `HIGH`.
- The MIC is the right channel when **Pin 3** is `LOW`.

By default, the RAK18030 is the right channel. But, you can remove the 10 kΩ resistor on **R9** and connect it to **R8** to change the MIC to the left channel as its default. You may also use **MIC_CTR_IO1** to select the MIC as the right or left channel.

> **Image:** RAK18030 WisBlock Digital Microphone schematic diagram

**Figure 10** shows the full schematic diagram of the RAK18030 Audio PDM Microphone module.

> **Image:** RAK18030 schematic diagram

