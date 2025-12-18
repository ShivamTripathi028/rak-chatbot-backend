---
slug: /product-categories/meshtastic/wismesh-b1/datasheet/
title: Meshtastic WisMesh Board ONE Datasheet
description: Provides comprehensive information about your WisMesh Board ONE to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/meshtastic/wismesh-board-one.png"
keywords:
  - datasheet
  - meshtastic
sidebar_label: Datasheet
---

# Meshtastic WisMesh Board ONE Datasheet

## Overview

**WisMesh Board ONE** is a breakout board for the RAK4630, specifically designed for Meshtastic. Unlike other baseboards such as RAK19007, WisMesh Board ONE reduces the number of connectors to compact the board size while retaining connectors for a solar panel, battery, OLED display, USB, and a sensor slot. The sensor slot was initially intended for a GPS module (RAK12500) but is compatible with other WisBlock sensor modules. WisMesh Board ONE features a built-in PCB Bluetooth antenna and two surface-mount nuts for securing the OLED display. All GPIOs and power connections are accessible via pin headers.

For more information about the RAK4630, please refer to the RAK Document Center: [RAK4630 Documentation](https://docs.rakwireless.com/product-categories/wisduo/rak4630-module/overview).

For additional details about Meshtastic, please visit the official website: [Meshtastic](https://meshtastic.org/).

### Applications

- Meshtastic device

### Main Features

- Based on the RAK4630
- Supports LoRa and Bluetooth
- Compatible with Meshtastic firmware
- Compatible with 5 V solar panels
- Supports 3.7 V rechargeable lithium batteries
- Standard Type-C connector for debugging and charging
- 1.3-inch OLED display
- Battery charging indicator light (red), two general indicator lights (green and red)
- One reset button, one general-purpose button
- Integrated PCB Bluetooth antenna
- MHF1 IPEX connector for LoRa antenna
- Sensor slot for GPS module (RAK12500)
- Compact size: 34.4 mm x 60.8 mm

## Specifications

### Overview

> **Image:** WisMesh Board ONE top view

> **Image:** WisMesh Board ONE bottom view

#### Block Diagram

> **Image:** WisMesh Board ONE powertree

> **Image:** WisMesh Board ONE signal block diagram

### Electrical Characteristics

#### Absolute Maximum Ratings

The Absolute Maximum Ratings of the device are shown in the table below. The stress ratings are the functional operation of the device.

:::warning
1. If the stress rating goes above what is listed, it may cause permanent damage to the device.
2. Under the listed conditions is not advised.
3. Exposure to maximum rating conditions may affect the device reliability.
:::

| **Ratings**                             | Maximum Value   | Unit |
|-----------------------------------------|-----------------|------|
| Power supply on the USB port (**VBUS**) | –0.3 to 5.5     | V    |
| Battery voltage (**VBAT**)              | –0.3 to 4.3     | V    |
| Solar panel voltage (**CONN_S**)        | –0.3 to 5.5     | V    |
| IOs of WisBlock connector               | –0.3 to VDD+0.3 | V    |
| ESD                                     | 2000            | V    |

:::warning
The WisMesh Board ONE, as any electronic equipment, is sensitive to **electrostatic discharge (ESD)**. Improper handling can cause permanent damage to the module.
:::

#### Recommended Operating Conditions

| **Symbol** | **Description**                     | **Min.** | **Nom.** | **Max.** | **Unit** |
| ---------- | ----------------------------------- | -------- | -------- | -------- | -------- |
| CONN_S     | power from solar panel or DC Supply | -        | 5        | 5.5      | V        |
| VBAT       | Battery voltage                     | 3.3      | -        | 4.20    | V        |
| 3V3        | DC-DC output                        | -        | 3.3      | -        | V        |
| I<sub>OCP</sub>          | Over current protection on the external input | -        | 490      | -    | mA      |
| I<sub>CHG</sub>         | Constant charging current on battery | -        | 440   | -        | mA       |

#### Battery Connector

The WisMesh Board ONE can be powered by a rechargeable battery, connected to the **P2 connector**. The nominal operating voltage of the battery should be within the range shown in the following table. The matching connector for the battery wires is an [JST PHR-2 2 mm pitch female](https://www.jst-mfg.com/product/detail_e.php?series=199).

:::tip NOTE
Depending on the regional requirements, the WisMesh Board ONE can have a two pin (US) or a three pin (EU) battery connector. In case the three pin connector is on the board, only batteries with an integratec NTC temperature sensor and a three wire cable can be connected and charged.
:::

| **Minimum** | **Typical** | **Maximum** | **Unit** |
|-------------|-------------|-------------|----------|
| 3.3         | 3.7         | 4.3         | V        |

The Type-C USB connector is used as a charging port. The voltage and current fed to the battery through the port should not exceed its charging limits, as shown in the table below.

| **Parameter**    | **Value**        |
|------------------|------------------|
| Charging voltage | 4.5 – 5.5 V |
| Charging current | 440 mA      |

A suitable Li-ion battery should have the following parameters as shown in the table below:

| **Parameter**     | **Value**            |
|-------------------|----------------------|
| Standard voltage  | 3.7 V           |
| Charging voltage  | 4.2 V           |
| Capacity          | As required          |
| Discharge current | At least 500 mA |

:::tip NOTE
Do not use a non-rechargeable battery.
:::

#### Solar Panel Connector

A 5 V solar panel can be connected to the board via the **P1 connector**. The solar panel can also be used to charge the Li-ion battery. The matching connector for the solar panel wires is an [JST ZHR-2 1.5 mm pitch female](https://www.jst-mfg.com/product/detail_e.php?series=287).

### Hardware

The hardware specification presents the electrical, environmental, and mechanical parameters that include the tabular data of the functionalities and standard values of the WisMesh Board ONE.

#### Interfaces

WisMesh Board ONE provides the following interfaces, headers, two buttons, and WisBlock Connectors.

- One Type-C USB connector
- One connector for the Sensor slot
- Two pin headers 2.54 mm hole pads
- 2-pin battery interface
- 2-pin solar panel interface

Additionally, the WisMesh Board ONE has two user-definable LEDs, one power supply/charging indicator LED, a reset button, a user-definable button and a reset button.

##### Type-C USB port

The Type-C USB connector is compliant with the USB 2.0 specification. This USB interface directly communicates with the connected **WisBlock Core** module. It is also used as a charging input port for the battery. Here are some of the advantages of the Type-C USB connector:

* Smaller and reversible connector shape
* Port can be input or output
* Fast battery charging

> **Image:** USB Type-C receptacle pinout

##### J4 and J9 Headers

On the WisMesh Board ONE, there are two 2.54 mm pitch headers for IO extension. GPIOs, SPI, I2C, SWD pins from the WisDuo module are exposed on these headers.

###### J4 Header Pinout

| **Pin** | **Pin Name** | **Description**           | **nRF52840 GPIO** |
|---------|--------------|---------------------------|-------------------|
| 1       | BAT_NTC      | NTC sensor of the battery | ---               |
| 2       | VBAT         | Battery supply            | ---               |
| 3       | VBUS_D       | USB supply                | ---               |
| 4       | GND          | Ground pin                | ---               |
| 5       | 3V3          | 3.3 V                | ---               |
| 6       | GND          | Ground pin                | ---               |
| 7       | I2C1_SDA     | I2C 1 data                | GPIO P0.13        |
| 8       | I2C1_SCL     | I2C 1 clock               | GPIO P0.14        |
| 9       | RXD0         | Serial 2 RX               | GPIO P0.19        |
| 10      | TXD0         | Serial 2 TX               | GPIO P0.20        |
| 11      | SWDIO        | SWD interface             | ---               |
| 12      | SWDCLK       | SWD interface             | ---               |
| 13      | RESET        | Reset pin                 | ---               |
| 14      | AIN0         | Analog input 0            | GPIO P0.05        |
| 15      | AIN1         | Analog input 1            | GPIO P0.31        |

###### J9 Header Pinout

| **Pin** | **Pin Name** | **Description**               | **nRF52840 GPIO** |
|---------|--------------|-------------------------------|-------------------|
| 1       | 3V3_S        | 3.3 V, controlled by IO2 | ---               |
| 2       | GND          | Ground pin                    | ---               |
| 3       | IO2          | GPIO 2                        | GPIO P1.02        |
| 4       | SPI_MOSI     | SPI MOSI pin                  | GPIO P0.30        |
| 5       | SPI_CLK      | SPI Clock pin                 | GPIO P0.03        |
| 6       | IO1          | GPIO 1                        | GPIO P0.17        |
| 7       | SPI_CS       | SPI CS pin                    | GPIO P0.26        |
| 8       | SPI_MISO     | SPI MISO pin                  | GPIO P0.29        |
| 9       | IO8          | GPIO 8                        | GPIO P0.02        |
| 10      | SW1          | Switch pin                    | GPIO P1.01        |
| 11      | IO5          | GPIO 5                        | GPIO P0.09        |
| 12      | IO6          | GPIO 6                        | GPIO P0.10        |
| 13      | IO7          | GPIO 7                        | GPIO P0.28        |

#### Battery and Solar Panel / 5V Connection

WisMesh Board ONE can be powered via the USB cable or Li-ion/LiPo battery via the dedicated connectors, as shown below. The matching connector for the battery wires is a [JST PHR-2 2 mm pitch female](https://www.jst-mfg.com/product/detail_e.php?series=199).

The battery can be recharged as well via a small solar panel or a regulated 5V supply, as shown below. The matching connector for the battery wires is a [JST ZHR-2 1.5 mm pitch female](https://www.jst-mfg.com/product/detail_e.php?series=287).

:::warning
- Batteries can cause harm if not handled properly.
- Only 3.7-4.2 V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system.
- If a non-rechargeable battery is used, it must be unplugged before connecting the USB cable to the board's USB port to configure the device. Failing to do so could damage the battery or cause a fire.
- Make sure the battery wires match the polarity on the board. Not all batteries have the same wiring.
:::

:::warning
- Only 5 V solar panels are supported. Do not use 12 V solar panels. It will destroy the charging unit and eventually other electronic parts.
- The GND pin of the Solar Panel Connector is located on edge of the board. Make sure the Solar Panel wires are matching the polarity on the WisMesh Board ONE.
:::

#### LEDs

Three LEDs are used to indicate the operating status. Below are the functions of the LEDs:

- 🔴 **Red LED** - Connected to the charger chip to indicate the charger status. When the battery is charging, this red LED is on. When the battery is full, this LED is weak light or off.
- 🟢 **Green LED** - Connected to the WisBlock Core module, controlled by MCU defined by the user.
- 🔵 **Blue LED** - Connected to the Wisblock Core module, controlled by MCU defined by the user.

#### RESET Push Button

The Reset Push Button is connected to the WisBlock Core module. When pushed, it resets the MCU.

#### User Push Button

The User Push Button is connected to the WisBlock Core modules IO5. It requires firmware support to use this button.

#### Connector for WisBlock Sensor

The WisBlock sensor module connector is a **24-pin board-to-board connector**.

> **Image:** WisBlock Sensor module connector

| **Sensor Slot** | **Pin Number** | **Pin Number** | **Sensor Slot** |
|-----------------|----------------|----------------|-----------------|
| TXD1            | 1              | 2              | GND             |
| SPI_CS          | 3              | 4              | SPI_CLK         |
| SPI_MISO        | 5              | 6              | SPI_MOSI        |
| I2C1_SCL        | 7              | 8              | I2C1_SDA        |
| VDD             | 9              | 10             | IO4             |
| 3V3_S           | 11             | 12             | IO3             |
| NC              | 13             | 14             | 3V3_S           |
| NC              | 15             | 16             | VDD             |
| NC              | 17             | 18             | NC              |
| NC              | 19             | 20             | NC              |
| NC              | 21             | 22             | NC              |
| GND             | 23             | 24             | RXD1            |

As for the following table, it shows the pin name and description of each pin in the WisBlock Sensor module connector.

| **Pin Number** | **Connector D** | **Type** | **Description**                                                                                                                                 |
|----------------|-----------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| 1              | TXD1            | I/O      | UART TX signal                                                                                                                                  |
| 2              | GND             | S        | Ground                                                                                                                                          |
| 3              | SPI_CS          | I/O      | SPI chip select signal                                                                                                                          |
| 4              | SPI_CLK         | I/O      | SPI clock                                                                                                                                       |
| 5              | SPI_MISO        | I/O      | SPI MISO signal                                                                                                                                 |
| 6              | SPI_MOSI        | I/O      | SPI MOSI signal                                                                                                                                 |
| 7              | I2C1_SCL        | I/O      | I2C clock signal                                                                                                                                |
| 8              | I2C1_SDA        | I/O      | I2C data signal                                                                                                                                 |
| 9              | VDD             | S        | Generated by CPU module. Used to power sensor board if MCU IO level is not 3.3 V                                                           |
| 10             | IO4             | I/O      | General purpose IO. IO2 controls the power switch of 3V3_S. When the 3V3_S function is used, IO2 can not be used as an interrupt of the sensor. |
| 11             | 3V3_S           | S        | 3.3 V power supply. Can be shut down by the CPU module.                                                                                    |
| 12             | IO3             | I/O      | General purpose IO - IO controls the power switch of 3V3_S. When the 3V3_S function is used, IO2 cannot be used as an interrupt of the sensor.  |
| 13             | NC              | NC       | Not connected                                                                                                                                   |
| 14             | 3V3_S           | S        | 3.3 V power supply. Can be shut down by the CPU module.                                                                                    |
| 15             | NC              | NC       | Not connected                                                                                                                                   |
| 16             | VDD             | S        | Generated by CPU module. Used to power sensor board if the MCU IO level is not 3.3 V.                                                      |
| 17             | NC              | NC       | Not connected                                                                                                                                   |
| 18             | NC              | NC       | Not connected                                                                                                                                   |
| 19             | NC              | NC       | Not connected                                                                                                                                   |
| 20             | NC              | NC       | Not connected                                                                                                                                   |
| 21             | NC              | NC       | Not connected                                                                                                                                   |
| 22             | NC              | NC       | Not connected                                                                                                                                   |
| 23             | GND             | S        | Ground                                                                                                                                          |
| 24             | RXD1            | I/O      | UART RX signal                                                                                                                                  |

### Mechanical Characteristics

#### Board Dimensions

Dimensions and the mechanic drawing of WisMesh Board ONE.

> **Image:** WisMesh Board ONE mechanic drawing

#### Environmental Characteristics

The table below lists the operation and storage temperature requirements of WisMesh Board ONE:

| **Parameter**                 | **Minimum** | **Typical** | **Maximum** |
|-------------------------------|:-----------:|:-----------:|:-----------:|
| Operational Temperature Range | –35° C | +25° C | +75° C |
| Extended Temperature Range    | –40° C | +25° C | +80° C |
| Storage Temperature Range     | –40° C | +25° C | +80° C |

### Schematic Diagram

#### Overcurrent Protection

Overcurrent protection is designed to safeguard electrical circuits and components from excessive current levels that could potentially cause damage or hazards. The protection current is determined by the combined resistance of resistors R59 and R25.

> **Image:** OCP

#### Charge Management

The SGM4152 is used as the charge management chip. D2 is the charging indicator (red LED). During the charging process, the indicator will be on. When charging is not occurring or when charging is complete, the indicator will turn off.

The chip includes battery temperature-related charging control. Charging will stop if the battery temperature exceeds 55° C or falls below 0° C. This feature enhances device safety and is also a requirement for CE certification (IEC 62368‑1). Battery temperature sensing is typically achieved using a Negative Temperature Coefficient (NTC) thermistor, which can be integrated inside the battery or soldered onto the board (R62).

> **Image:** Charge management

> **Image:** Battery connector

#### Power Path

When an external power source is available, priority is given to using the external power supply.

> **Image:** Power Path

#### DC-DC

The buck converter generates 3.3 V.

> **Image:** DC-DC

#### Load Switch

The load switch status can be controlled through IO2.

> **Image:** Load Switch

#### OLED Display Interface

> **Image:** OLED display interface

#### Sensor Slot

This slot is specifically for the GPS module (RAK12500), but it can also be used for other WisBlock Sensor modules.

> **Image:** Sensor Slot

#### Pin Header

The pin headers on WisMesh Board ONE extend the power and signals of the RAK4630, allowing users to customize their own designs through the pin headers.

> **Image:** Pin Headers

