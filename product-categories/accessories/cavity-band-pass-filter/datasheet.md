---
slug: /product-categories/accessories/cavity-band-pass-filter/datasheet/
title: "High-Rejection LoRaWAN Filter Datasheet: RAK Outdoor Band-Pass"
description: View the RAK Band-Pass Filter Datasheet for LoRaWAN gateways. Includes electrical, mechanical, and RF specs with high-rejection, low-loss, IP67-rated performance.
image: "https://images.docs.rakwireless.com/accessories/cavity-band-pass-filter/cavity-band-pass-filter.png"
keywords:
  - LoRaWAN band-pass filter datasheet
  - High-rejection LoRa filter
  - Outdoor RF cavity filter
  - LoRa gateway interference filter
  - Industrial LoRaWAN filter
  - IP67 LoRa filter
  - N-Female band-pass filter
  - Low insertion loss LoRa filter
sidebar_label: Datasheet
date: 2025-10-09
---

# RAK Outdoor Cavity Band-Pass Filter Datasheet

## Overview

### Description

The **RAK Outdoor Cavity Band-Pass Filter** is an RF accessory designed to enhance LoRaWAN gateway performance in environments with high interference. It allows only the target LoRa frequency band to pass while attenuating out-of-band signals such as LTE, 5G, radar, and industrial noise.

The filter is based on a high-Q resonant cavity design, isolating the target frequency band and reducing the impact of external interference. This ensures stable and reliable gateway performance in urban and industrial deployments where RF noise is significant.

### Features

- **High out-of-band rejection**: >75 dB attenuation to suppress LTE, 5G, radar, and other signals.
- **Low insertion loss**: 2.0–3.2 dB (model dependent), preserving LoRa signal strength.
- **Easy integration**: Standard N-Female connectors, no adapters required.
- **Available frequency variants**: EU868, US915, IN865, RU864, AU915, KR920, AS923-1/2/3/4, CN470.

## Specifications

### Interfaces

The band-pass filter provides the following interfaces:

| Name                        | Description                                                                             |
|-----------------------------|-----------------------------------------------------------------------------------------|
| N-Female Connector (Port 1) | Connects the filter to the LoRa gateway via RF coaxial cable.                           |
| N-Female Connector (Port 2) | Connects the filter to the external LoRa antenna.                                       |
| Ground Pad                  | Provides connection to earth ground for ESD and surge protection. Strongly recommended. |

> **Image:** Band-pass filter interfaces

### Filter Variants and Specifications

| Variant | Band (MHz) | Insertion Loss (dB) | Rejection (dB) | Dimensions (mm) | Weight (kg) | LoRaWAN Region |
| --- | --- | --- | --- | --- | --- | --- |
| [BPF01](#bpf01-470510mhz) | 470–510 | < 2.5 | > 75 | 280 × 170 × 75 | 3.6 | CN470 |
| [BPF03](#bpf03-863870mhz) | 863–870 | < 2.5 | > 75 | 228 × 164.6 × 51.5 | 1.5 | EU868, RU864 |
| [BPF04](#bpf04-865867mhz) | 865–867 | < 3.2 | > 80 | 250 × 170 × 55 | 3 | IN865 |
| [BPF05](#bpf05-902928mhz) | 902–928 | < 2.0 | > 75 | 270 × 170 × 55 | 3 | US915 |
| [BPF06](#bpf06-915921mhz) | 915–921 | < 2.5 | > 75 | 250 × 170 × 55 | 3 | AS923-3, AS923-4 |
| [BPF07](#bpf07-915928mhz) | 915–928 | < 2.6 | > 75 | 250 × 170 × 55 | 3 | AU915, AS923-1 |
| [BPF08](#bpf08-920925mhz) | 920–925 | < 2.85 | > 80 | 228 × 164.6 × 51.5 | 1.5 | AS923-2, KR920 (Hong Kong, Macao, Taiwan, Singapore, Thailand, etc.) |

Detailed specifications for each filter variant are provided in the following sections, including its **LoRaWAN region**, **electrical** and **mechanical** parameters, and a **typical frequency response curve**.

#### BPF01 (470–510 MHz)

- **LoRaWAN Region:** CN470

##### Electrical Specifications

| Parameter                        | Specification                                        |
|----------------------------------|------------------------------------------------------|
| Pass Band (MHz)                  | 470\~510                                             |
| Insertion Loss (dB)              | < 2.5 (470\~510 MHz)                            |
| Stop Band Attenuation (dB)       | > 75 (0\~465 MHz) 
 75 (515\~2000 MHz) |
| VSWR                             | < 1.25                                               |
| Input Power (W)                  | < 100                                                |
| Intermodulation Products (dBm)   | < -150 (3rd order, with 2 x 37 dBm)             |
| Operating Temperature (° C) | -40 to +65                                           |
| IP Rating                        | IP67                                                 |
| Deployment Environment           | Outdoor                                              |
| Connector                        | N-Female                                             |

##### Mechanical Specifications

| Parameter                          | Specification                                                 |
|------------------------------------|---------------------------------------------------------------|
| Filter Dimensions (H x W x D) (mm) | 280 x 170 x 75 (without connector, without mounting brackets) |
| Packing Dimensions (mm)            | 450 x 325 x 190 (double unit)                                 |
| Filter Weight (kg)                 | 3.6                                                           |

##### Typical Frequency Response

**Figure 2** shows a typical 470-510 MHz frequency response curve. Actual results may vary with component and environmental factors.

> **Image:** 470-510 MHz Frequency Response

#### BPF03 (863–870 MHz)

- **LoRaWAN Region:** EU868, RU864

##### Electrical Specifications

| Parameter                        | Specification                                        |
|----------------------------------|------------------------------------------------------|
| Pass Band (MHz)                  | 863\~870                                             |
| Insertion Loss (dB)              | < 2.5 (863\~870 MHz)                            |
| Stop Band Attenuation (dB)       | > 70 (0\~860 MHz) 
 70 (873\~4000 MHz) |
| VSWR                             | < 1.25                                               |
| Input Power (W)                  | < 100                                                |
| Intermodulation Products (dBm)   | < -150 (3rd order, with 2 x 37 dBm)             |
| Operating Temperature (° C) | -40 to +65                                           |
| IP Rating                        | IP67                                                 |
| Deployment Environment           | Outdoor                                              |
| Connector                        | N-Female                                             |

##### Mechanical Specifications

| Parameter                          | Specification                                                     |
|------------------------------------|-------------------------------------------------------------------|
| Filter Dimensions (H x W x D) (mm) | 228 x 164.6 x 51.5 (without connector, without mounting brackets) |
| Packing Dimensions (mm)            | 450 x 325 x 190 (double unit)                                     |
| Filter Weight (kg)                 | 1.5                                                               |

##### Typical Frequency Response

**Figure 3** shows a typical 863-870 MHz frequency response curve. Actual results may vary with component and environmental factors.

> **Image:** 863-870 MHz Frequency Response

#### BPF04 (865–867 MHz)

- **LoRaWAN Region:** IN865

##### Electrical Specifications

| Parameter                        | Specification                                        |
|----------------------------------|------------------------------------------------------|
| Pass Band (MHz)                  | 865\~867                                             |
| Insertion Loss (dB)              | < 3.2 (865\~867 MHz)                            |
| Stop Band Attenuation (dB)       | > 80 (0\~863 MHz) 
 80 (870\~4000 MHz) |
| VSWR                             | < 1.25                                               |
| Input Power (W)                  | < 100                                                |
| Intermodulation Products (dBm)   | < -150 (3rd order, with 2 x 37 dBm)             |
| Operating Temperature (° C) | -40 to +65                                           |
| IP Rating                        | IP67                                                 |
| Deployment Environment           | Outdoor                                              |
| Connector                        | N-Female                                             |

##### Mechanical Specifications

| Parameter                          | Specification                                                 |
|------------------------------------|---------------------------------------------------------------|
| Filter Dimensions (H x W x D) (mm) | 250 x 170 x 55 (without connector, without mounting brackets) |
| Packing Dimensions (mm)            | 450 x 325 x 190 (double unit)                                 |
| Filter Weight (kg)                 | 3                                                             |

##### Typical Frequency Response

**Figure 4** shows a typical 865-867 MHz frequency response curve. Actual results may vary with component and environmental factors.

> **Image:** 865-867 MHz Frequency Response

#### BPF05 (902–928 MHz)

- **LoRaWAN Region:** US915

##### Electrical Specifications

| Parameter                        | Specification                                        |
|----------------------------------|------------------------------------------------------|
| Pass Band (MHz)                  | 902\~928                                             |
| Insertion Loss (dB)              | < 2.0 (902\~928 MHz)                            |
| Stop Band Attenuation (dB)       | > 75 (0\~889 MHz) 
 75 (931\~4000 MHz) |
| VSWR                             | < 1.25                                               |
| Input Power (W)                  | < 100                                                |
| Intermodulation Products (dBm)   | < -150 (3rd order, with 2 x 37 dBm)             |
| Operating Temperature (° C) | -40 to +65                                           |
| IP Rating                        | IP67                                                 |
| Deployment Environment           | Outdoor                                              |
| Connector                        | N-Female                                             |

##### Mechanical Specifications

| Parameter                          | Specification                                                 |
|------------------------------------|---------------------------------------------------------------|
| Filter Dimensions (H x W x D) (mm) | 270 x 170 x 55 (without connector, without mounting brackets) |
| Packing Dimensions (mm)            | 450 x 325 x 190 (double unit)                                 |
| Filter Weight (kg)                 | 3                                                             |

##### Typical Frequency Response

**Figure 5** shows a typical 902-928 MHz frequency response curve. Actual results may vary with component and environmental factors.

> **Image:** 902-928 MHz Frequency Response

#### BPF06 (915–921 MHz)

- **LoRaWAN Region:** AS923-3, AS923-4

##### Electrical Specifications

| Parameter                        | Specification                                        |
|----------------------------------|------------------------------------------------------|
| Pass Band (MHz)                  | 915\~921                                             |
| Insertion Loss (dB)              | < 2.5 (915\~921 MHz)                            |
| Stop Band Attenuation (dB)       | > 75 (0\~912 MHz) 
 75 (924\~4000 MHz) |
| VSWR                             | < 1.25                                               |
| Input Power (W)                  | < 100                                                |
| Intermodulation Products (dBm)   | < -150 (3rd order, with 2 x 37 dBm)             |
| Operating Temperature (° C) | -40 to +65                                           |
| IP Rating                        | IP67                                                 |
| Deployment Environment           | Outdoor                                              |
| Connector                        | N-Female                                             |

##### Mechanical Specifications

| Parameter                          | Specification                                                 |
|------------------------------------|---------------------------------------------------------------|
| Filter Dimensions (H x W x D) (mm) | 250 x 170 x 55 (without connector, without mounting brackets) |
| Packing Dimensions (mm)            | 450 x 325 x 190 (double unit)                                 |
| Filter Weight (kg)                 | 3                                                             |

##### Typical Frequency Response

**Figure 6** shows a typical 915-921 MHz frequency response curve. Actual results may vary with component and environmental factors.

> **Image:** 915-921 MHz Frequency Response

#### BPF07 (915–928 MHz)

- **LoRaWAN Region:** AU915, AS923-1

##### Electrical Specifications

| Parameter                        | Specification                                        |
|----------------------------------|------------------------------------------------------|
| Pass Band (MHz)                  | 915\~928                                             |
| Insertion Loss (dB)              | < 2.6 (915\~928 MHz)                            |
| Stop Band Attenuation (dB)       | > 75 (0\~912 MHz) 
 75 (931\~4000 MHz) |
| VSWR                             | < 1.25                                               |
| Input Power (W)                  | < 100                                                |
| Intermodulation Products (dBm)   | < -150 (3rd order, with 2 x 37 dBm)             |
| Operating Temperature (° C) | -40 to +65                                           |
| IP Rating                        | IP67                                                 |
| Deployment Environment           | Outdoor                                              |
| Connector                        | N-Female                                             |

##### Mechanical Specifications

| Parameter                          | Specification                                                 |
|------------------------------------|---------------------------------------------------------------|
| Filter Dimensions (H x W x D) (mm) | 250 x 170 x 55 (without connector, without mounting brackets) |
| Packing Dimensions (mm)            | 450 x 325 x 190 (double unit)                                 |
| Filter Weight (kg)                 | 3                                                             |

##### Typical Frequency Response

**Figure 7** shows a typical 915-928 MHz frequency response curve. Actual results may vary with component and environmental factors.

> **Image:** 915-928 MHz Frequency Response

#### BPF08 (920–925 MHz)

- **LoRaWAN Region:** AS923-2, KR920 (Hong Kong, Macao, Taiwan, Singapore, Thailand, etc.)

##### Electrical Specifications

| Parameter                        | Specification                                        |
|----------------------------------|------------------------------------------------------|
| Pass Band (MHz)                  | 920\~925                                             |
| Insertion Loss (dB)              | < 2.85 (920\~925 MHz)                           |
| Stop Band Attenuation (dB)       | > 80 (0\~917 MHz) 
 80 (928\~4000 MHz) |
| VSWR                             | < 1.25                                               |
| Input Power (W)                  | < 100                                                |
| Intermodulation Products (dBm)   | < -150 (3rd order, with 2 x 37 dBm)             |
| Operating Temperature (° C) | -40 to +65                                           |
| IP Rating                        | IP67                                                 |
| Deployment Environment           | Outdoor                                              |
| Connector                        | N-Female                                             |

##### Mechanical Specifications

| Parameter                          | Specification                                                     |
|------------------------------------|-------------------------------------------------------------------|
| Filter Dimensions (H x W x D) (mm) | 228 x 164.6 x 51.5 (without connector, without mounting brackets) |
| Packing Dimensions (mm)            | 450 x 325 x 190 (double unit)                                     |
| Filter Weight (kg)                 | 1.5                                                               |

##### Typical Frequency Response

**Figure 8** shows a typical 920-925 MHz frequency response curve. Actual results may vary with component and environmental factors.

> **Image:** 920-925 MHz Frequency Response

