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
import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK Outdoor Cavity Band-Pass Filter Datasheet

## Overview

### Description

The **RAK Outdoor Cavity Band-Pass Filter** is an RF accessory designed to enhance LoRaWAN gateway performance in environments with high interference. It allows only the target LoRa frequency band to pass while attenuating out-of-band signals such as LTE, 5G, radar, and industrial noise.

The filter is based on a high-Q resonant cavity design, isolating the target frequency band and reducing the impact of external interference. This ensures stable and reliable gateway performance in urban and industrial deployments where RF noise is significant.

### Features

- **High out-of-band rejection**: >75&nbsp;dB attenuation to suppress LTE, 5G, radar, and other signals.
- **Low insertion loss**: 2.0–3.2&nbsp;dB (model dependent), preserving LoRa signal strength.
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

<RkImage
  src="https://images.docs.rakwireless.com/accessories/cavity-band-pass-filter/band-pass-filter-interfaces.png"
  width="100%"
  caption="Band-pass filter interfaces"
/>

### Filter Variants and Specifications

<table>
  <thead>
    <tr>
      <th>Variant</th>
      <th>Band (MHz)</th>
      <th>Insertion Loss (dB)</th>
      <th>Rejection (dB)</th>
      <th>Dimensions (mm)</th>
      <th>Weight (kg)</th>
      <th>LoRaWAN Region</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>[BPF01](#bpf01-470510mhz)</td>
      <td>470–510</td>
      <td>< 2.5</td>
      <td>> 75</td>
      <td>280 × 170 × 75</td>
      <td>3.6</td>
      <td>CN470</td>
    </tr>
    <tr>
      <td>[BPF03](#bpf03-863870mhz)</td>
      <td>863–870</td>
      <td>< 2.5</td>
      <td>> 75</td>
      <td>228 × 164.6 × 51.5</td>
      <td>1.5</td>
      <td>EU868, RU864</td>
    </tr>
    <tr>
      <td>[BPF04](#bpf04-865867mhz)</td>
      <td>865–867</td>
      <td>< 3.2</td>
      <td>> 80</td>
      <td>250 × 170 × 55</td>
      <td>3</td>
      <td>IN865</td>
    </tr>
    <tr>
      <td>[BPF05](#bpf05-902928mhz)</td>
      <td>902–928</td>
      <td>< 2.0</td>
      <td>> 75</td>
      <td>270 × 170 × 55</td>
      <td>3</td>
      <td>US915</td>
    </tr>
    <tr>
      <td>[BPF06](#bpf06-915921mhz)</td>
      <td>915–921</td>
      <td>< 2.5</td>
      <td>> 75</td>
      <td>250 × 170 × 55</td>
      <td>3</td>
      <td>AS923-3, AS923-4</td>
    </tr>
    <tr>
      <td>[BPF07](#bpf07-915928mhz)</td>
      <td>915–928</td>
      <td>< 2.6</td>
      <td>> 75</td>
      <td>250 × 170 × 55</td>
      <td>3</td>
      <td>AU915, AS923-1</td>
    </tr>
    <tr>
      <td>[BPF08](#bpf08-920925mhz)</td>
      <td>920–925</td>
      <td>< 2.85</td>
      <td>> 80</td>
      <td>228 × 164.6 × 51.5</td>
      <td>1.5</td>
      <td>AS923-2, KR920 (Hong Kong, Macao, Taiwan, Singapore, Thailand, etc.)</td>
    </tr>
  </tbody>
</table>

Detailed specifications for each filter variant are provided in the following sections, including its **LoRaWAN region**, **electrical** and **mechanical** parameters, and a **typical frequency response curve**.

#### BPF01 (470–510&nbsp;MHz)

- **LoRaWAN Region:** CN470

##### Electrical Specifications

| Parameter                        | Specification                                        |
|----------------------------------|------------------------------------------------------|
| Pass Band (MHz)                  | 470\~510                                             |
| Insertion Loss (dB)              | < 2.5 (470\~510&nbsp;MHz)                            |
| Stop Band Attenuation (dB)       | > 75 (0\~465&nbsp;MHz) <br/> 75 (515\~2000&nbsp;MHz) |
| VSWR                             | < 1.25                                               |
| Input Power (W)                  | < 100                                                |
| Intermodulation Products (dBm)   | < -150 (3rd order, with 2 x 37&nbsp;dBm)             |
| Operating Temperature (°&nbsp;C) | -40 to +65                                           |
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

**Figure 2** shows a typical 470-510&nbsp;MHz frequency response curve. Actual results may vary with component and environmental factors.

<RkImage
  src="https://images.docs.rakwireless.com/accessories/cavity-band-pass-filter/470-510-frequency-reponse.png"
  width="100%"
  caption="470-510 MHz Frequency Response"
/>

#### BPF03 (863–870&nbsp;MHz)

- **LoRaWAN Region:** EU868, RU864

##### Electrical Specifications

| Parameter                        | Specification                                        |
|----------------------------------|------------------------------------------------------|
| Pass Band (MHz)                  | 863\~870                                             |
| Insertion Loss (dB)              | < 2.5 (863\~870&nbsp;MHz)                            |
| Stop Band Attenuation (dB)       | > 70 (0\~860&nbsp;MHz) <br/> 70 (873\~4000&nbsp;MHz) |
| VSWR                             | < 1.25                                               |
| Input Power (W)                  | < 100                                                |
| Intermodulation Products (dBm)   | < -150 (3rd order, with 2 x 37&nbsp;dBm)             |
| Operating Temperature (°&nbsp;C) | -40 to +65                                           |
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

**Figure 3** shows a typical 863-870&nbsp;MHz frequency response curve. Actual results may vary with component and environmental factors.

<RkImage
  src="https://images.docs.rakwireless.com/accessories/cavity-band-pass-filter/863-870-frequency-response.png"
  width="100%"
  caption="863-870 MHz Frequency Response"
/>

#### BPF04 (865–867&nbsp;MHz)

- **LoRaWAN Region:** IN865

##### Electrical Specifications

| Parameter                        | Specification                                        |
|----------------------------------|------------------------------------------------------|
| Pass Band (MHz)                  | 865\~867                                             |
| Insertion Loss (dB)              | < 3.2 (865\~867&nbsp;MHz)                            |
| Stop Band Attenuation (dB)       | > 80 (0\~863&nbsp;MHz) <br/> 80 (870\~4000&nbsp;MHz) |
| VSWR                             | < 1.25                                               |
| Input Power (W)                  | < 100                                                |
| Intermodulation Products (dBm)   | < -150 (3rd order, with 2 x 37&nbsp;dBm)             |
| Operating Temperature (°&nbsp;C) | -40 to +65                                           |
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

**Figure 4** shows a typical 865-867&nbsp;MHz frequency response curve. Actual results may vary with component and environmental factors.

<RkImage
  src="https://images.docs.rakwireless.com/accessories/cavity-band-pass-filter/865-867-frequency-response.png"
  width="100%"
  caption="865-867 MHz Frequency Response"
/>

#### BPF05 (902–928&nbsp;MHz)

- **LoRaWAN Region:** US915

##### Electrical Specifications

| Parameter                        | Specification                                        |
|----------------------------------|------------------------------------------------------|
| Pass Band (MHz)                  | 902\~928                                             |
| Insertion Loss (dB)              | < 2.0 (902\~928&nbsp;MHz)                            |
| Stop Band Attenuation (dB)       | > 75 (0\~889&nbsp;MHz) <br/> 75 (931\~4000&nbsp;MHz) |
| VSWR                             | < 1.25                                               |
| Input Power (W)                  | < 100                                                |
| Intermodulation Products (dBm)   | < -150 (3rd order, with 2 x 37&nbsp;dBm)             |
| Operating Temperature (°&nbsp;C) | -40 to +65                                           |
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

**Figure 5** shows a typical 902-928&nbsp;MHz frequency response curve. Actual results may vary with component and environmental factors.

<RkImage
  src="https://images.docs.rakwireless.com/accessories/cavity-band-pass-filter/902-928-frequency-response.png"
  width="100%"
  caption="902-928 MHz Frequency Response"
/>

#### BPF06 (915–921&nbsp;MHz)

- **LoRaWAN Region:** AS923-3, AS923-4

##### Electrical Specifications

| Parameter                        | Specification                                        |
|----------------------------------|------------------------------------------------------|
| Pass Band (MHz)                  | 915\~921                                             |
| Insertion Loss (dB)              | < 2.5 (915\~921&nbsp;MHz)                            |
| Stop Band Attenuation (dB)       | > 75 (0\~912&nbsp;MHz) <br/> 75 (924\~4000&nbsp;MHz) |
| VSWR                             | < 1.25                                               |
| Input Power (W)                  | < 100                                                |
| Intermodulation Products (dBm)   | < -150 (3rd order, with 2 x 37&nbsp;dBm)             |
| Operating Temperature (°&nbsp;C) | -40 to +65                                           |
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

**Figure 6** shows a typical 915-921&nbsp;MHz frequency response curve. Actual results may vary with component and environmental factors.

<RkImage
  src="https://images.docs.rakwireless.com/accessories/cavity-band-pass-filter/915-921-frequency-response.png"
  width="100%"
  caption="915-921 MHz Frequency Response"
/>

#### BPF07 (915–928&nbsp;MHz)

- **LoRaWAN Region:** AU915, AS923-1

##### Electrical Specifications

| Parameter                        | Specification                                        |
|----------------------------------|------------------------------------------------------|
| Pass Band (MHz)                  | 915\~928                                             |
| Insertion Loss (dB)              | < 2.6 (915\~928&nbsp;MHz)                            |
| Stop Band Attenuation (dB)       | > 75 (0\~912&nbsp;MHz) <br/> 75 (931\~4000&nbsp;MHz) |
| VSWR                             | < 1.25                                               |
| Input Power (W)                  | < 100                                                |
| Intermodulation Products (dBm)   | < -150 (3rd order, with 2 x 37&nbsp;dBm)             |
| Operating Temperature (°&nbsp;C) | -40 to +65                                           |
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

**Figure 7** shows a typical 915-928&nbsp;MHz frequency response curve. Actual results may vary with component and environmental factors.

<RkImage
  src="https://images.docs.rakwireless.com/accessories/cavity-band-pass-filter/915-928-frequency-response.png"
  width="100%"
  caption="915-928 MHz Frequency Response"
/>

#### BPF08 (920–925&nbsp;MHz)

- **LoRaWAN Region:** AS923-2, KR920 (Hong Kong, Macao, Taiwan, Singapore, Thailand, etc.)

##### Electrical Specifications

| Parameter                        | Specification                                        |
|----------------------------------|------------------------------------------------------|
| Pass Band (MHz)                  | 920\~925                                             |
| Insertion Loss (dB)              | < 2.85 (920\~925&nbsp;MHz)                           |
| Stop Band Attenuation (dB)       | > 80 (0\~917&nbsp;MHz) <br/> 80 (928\~4000&nbsp;MHz) |
| VSWR                             | < 1.25                                               |
| Input Power (W)                  | < 100                                                |
| Intermodulation Products (dBm)   | < -150 (3rd order, with 2 x 37&nbsp;dBm)             |
| Operating Temperature (°&nbsp;C) | -40 to +65                                           |
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

**Figure 8** shows a typical 920-925&nbsp;MHz frequency response curve. Actual results may vary with component and environmental factors.

<RkImage
  src="https://images.docs.rakwireless.com/accessories/cavity-band-pass-filter/920-925-frequency-response.png"
  width="100%"
  caption="920-925 MHz Frequency Response"
/>



<RkBottomNav/>