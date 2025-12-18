---
title: RAK3112 LoRaWAN BLE Wi-Fi Quick Start Guide | Setup & Configuration
description: Quickly set up your RAK3112 module for LoRaWAN, Wi-Fi, P2P mode. Includes TTN and ChirpStack configuration steps.
image: https://images.docs.rakwireless.com/wisduo/RAK3112-module/rak3112-module.png
keywords:
  - wisduo
  - lorawan module
  - lorawan ble wifi module setup
  - espressif esp32-s3 with ble and wifi
  - semtech sx1262 lora module
  - rak3112 quick start
  - rak3112 setup
  - rak3112 device configuration
  - long range low power mcu
tags:
  - rak3112  
  - quickstart
  - wisduo
sidebar_label: Quick Start Guide
slug: /product-categories/wisduo/rak3112-module/quickstart/
date: 2025-04-24
---

# RAK3112 WisDuo LPWAN + BLE + Wi-Fi Module Quick Start Guide

## Prerequisites

Before going through the steps of installing the RAK3112 WisDuo LPWAN Module, make sure to prepare the necessary items listed below.

### Hardware

- [RAK3112 WisDuo LPWAN+BLE+Wi-Fi Module](https://store.rakwireless.com/products/wisduo-lora-wifi-module-rak3112)
- Computer
- USB adapter

### Software

- Download and install the [Arduino IDE](https://www.arduino.cc/en/Main/Software).

:::warning
***For Windows 10 users***: **DO NOT** install the Arduino IDE from the Microsoft App Store. Instead, install the original Arduino IDE from the [Arduino official website](https://support.arduino.cc/hc/en-us/articles/360019833020-Download-and-install-Arduino-IDE). The Arduino app from the Microsoft App Store has problems using third-party Board Support Packages.
:::

## Product Configuration

This section of the guide covers the following:

1. [Hardware Setup and Access to IO pins of RAK3112](https://docs.rakwireless.com/product-categories/wisduo/rak3112-module/quickstart/#hardware-setup)
2. [LoRaWAN OTAA and ABP Example with Arduino IDE](https://docs.rakwireless.com/product-categories/wisduo/rak3112-module/quickstart/#lorawan-example)
3. [Wi-Fi Example](https://docs.rakwireless.com/product-categories/wisduo/rak3112-module/quickstart/#wifi-example)

#### Hardware Setup

The RAK3112 requires a few hardware connections to function properly. The bare minimum requirement is to have the power section properly configured, along with the reset pull-up resistor, antennas, USB connection for firmware updates.

> **Image:** RAK3112 schematic

Ensure the antennas are properly connected for a strong LoRa and BLE signal. Note that powering the module without an antenna connected to the IPEX MHF4 connectors can damage the RF section of the chip.

> **Image:** LoRa antenna

> **Image:** Wi-Fi/BLE antenna

RAK3112 has a label on its sticker indicating where to connect the antennas, as illustrated in **Figure 4**.

> **Image:** RAK3112 antenna label

:::tip NOTE
- Detailed information about the RAK3112 LoRa IPEX MHF4 antenna can be found on the [863-870 MHz antenna datasheet](https://downloads.rakwireless.com/LoRa/WisBlock/Accessories/RAK_PCB_Antenna_for_LoRa_863-870_MHz_(RAKARB04)_Datasheet.pdf) or the [902-928 MHz antenna datasheet](https://downloads.rakwireless.com/LoRa/WisBlock/Accessories/RAK_PCB_Antenna_for_LoRa_902-928_MHz_(RAKARB03)_Datasheet.pdf).
- If the RAK3112 is not an IPEX MHF4 variant, the connection to the antennas are done via the RF pins. RAKwireless offers [RF Antenna Design Service](https://store.rakwireless.com/products/antenna-rf-design-service-including-pcb-design-tuning-matching-and-rf-test) for custom PCB designs.
:::

:::warning
- **Standard IPEX connector will not work on RAK3112.** The IPEX antenna connectors of RAK3112 are a different variant called [IPEX MHF-4](https://www.i-pex.com/product/mhf-4). This is specially designed for low-profile circuit boards with limited spaces.
- When using the LoRa, Wi-Fi or Bluetooth Low Energy transceivers, make sure that the antennas are connected. Using these transceivers without an antenna can damage the module.
:::

#### Software Setup

The RAK3112 does not come with default firmware. You have to develop your application based on the Arduino IDE, using the Espressif BSP.
Examples of how to use LoRa, LoRaWAN, BLE, and WiFi are provided in our [Github repo](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK3112)

##### RAK3112 RUI3 Board Support Package in Arduino IDE

If you don't have an Arduino IDE yet, download it on the [Arduino official website](https://www.arduino.cc/en/Main/Software).

:::tip NOTE
**For Windows 10 and up users**:
If you installed the Arduino IDE from the Microsoft App Store, uninstall it and reinstall the IDE from the [Arduino official website](https://support.arduino.cc/hc/en-us/articles/360019833020-Download-and-install-Arduino-IDE). The version from the Microsoft App Store has issues with third-party Board Support Packages.
:::

After successfully installing the Arduino IDE, configure it to add the RAK3112 to its board selection by following these steps:

Install the Espressif ESP32 BSP in Arduino following the guide [Installing Arduino-ESP32 support](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html).

The RAK3312 is supported by the official Espressif BSP as _**RAKwireless RAK3112**_ board.

##### Using the RAK3112 with PlatformIO

**Solution to use the RAK3112 with the ESP32 platform in PlatformIO (temporary)**

To use the RAK3112 with PlatformIO and the ESP32 platform, a custom project structure is required. This includes an additional folder in the project folder and some extra entries in the platformio.ini file of the project.

- Download the folder _**rakwireless**_ from our [Github repo](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK3112/IDE-Patches/PlatformIO)

- Copy this folder into your project folder.

Your project folder should look like this:

> **Image:** RAK3112 Board definition in PlatformIO project folder

- Add the following entries to the platformio.ini file of your project:

```ini
[platformio]
default_envs = rak3112
description = RAK3112
boards_dir = rakwireless/boards

[env:rak3112]
framework = arduino
platform = platformio/espressif32
board = rak3112

build_flags = -I rakwireless/variants/rak3112

```

_**boards_dir = rakwireless/boards**_ tells PlatformIO where to find additional boards for the ESP32 platform.

_**board = rak3112**_ tells PlatformIO to use the custom board rak3112 from the additional boards folder.

_**build_flags = -I rakwireless/variants/rak3112**_ tells PlatformIO where to find _**pins_arduino.h**_ and _**variant.h**_ files for the board RAK3112.

Keep these entries in the platformio.ini file and add your other definitions, e.g. lib_deps or additional build_flags.

##### Compile an Example with Arduino

After adding the RAK3112 to the Arduino IDE, test your setup by running a simple program.

1. Copy the example code below and paste it into the Arduino IDE.

<details>
<summary> Click to view the example code. </summary>

```c
void setup() {
  Serial.begin(115200);
}

void loop() {
  Serial.println("Hello");
  delay(5000);
}
```
</details>

> **Image:** Example code

8. Click the **Verify** button to compile and check for errors.

> **Image:** Verify the example code

9. When the compilation is complete, click the **Upload** button to flash the firmware to the RAK3112.

> **Image:** Upload the example code

10. Upon successful upload, the **Device programmed** message will appear.

> **Image:** Device Programmed

11. After the **Device Programmed** is completed, you will see the "Hello" message every 5 seconds in the console.

> **Image:** Application log output

##### RAK3112 IO Pins and Peripherals

This section discusses how to use and access the pinouts of the RAK3112 using Arduino APIs. It shows basic code for using digital IO, analog input, UART, and I2C.

###### RAK3112 Digital IO Pins

Available Digital IO Pins in RAK3112

| **Pin No.** | **Name**          | **Type**      | **Description**                                                         |
|-------------|-------------------|---------------|-------------------------------------------------------------------------|
| 11          | GPIO38            | I/O           | GPIO                                                                    |
| 12          | GPIO39            | I/O           | GPIO                                                                    |
| 18          | GPIO41            | I/O           | GPIO                                                                    |
| 19          | GPIO42            | I/O           | GPIO                                                                    |
| 23          | GPIO45            | I/O           | GPIO                                                                    |
| 24          | GPIO0 / Boot      | I/O Boot      | GPIO Bootloader force                                                   |
| 25          | GPIO46            | I/O           | GPIO                                                                    |
| 26          | GPIO1             | I/O           | GPIO                                                                    |
| 27          | GPIO2             | I/O           | GPIO                                                                    |

Any of the pins listed in the table above can be used. Pins with specific functions, such as UART and I2C, are also usable but with limitations. Those dedicated pins have been excluded from this illustration of digital IO pins.

<details>

<summary> Click to view the example code. </summary>

```c
/*
 RAK3112 Digital I/O Example
*/

void setup()
{
  pinMode(WB_IO1, OUTPUT); // Change the WB_IO1 (GPIO21) to any digital pin you want. Also, you can set this to INPUT or OUTPUT
}

void loop()
{
  digitalWrite(WB_IO1,HIGH); //Change the PA8 to any digital pin you want. Also, you can set this to HIGH or LOW state.
  delay(1000); // delay for 1 second
  digitalWrite(WB_IO1,LOW); //Change the PA8 to any digital pin you want. Also, you can set this to HIGH or LOW state.
  delay(1000); // delay for 1 second
}
```
</details>

###### RAK3112 Analog Input Pins

Available Analog input Pins in RAK3112

| **Pin No.** | **Name**          | **Type**      | **Description**                                                         |
|-------------|-------------------|---------------|-------------------------------------------------------------------------|
| 34          | GPIO14 / AIN1     | I/O Analog In | GPIO / Analog In                                                        |
| 41          | GPIO21 / AIN0     | I/O Analog In | GPIO / Analog In                                                        |

Any of the pins shown in the table above can be used as an Analog Input Pin. See the example code below.

<details>
<summary> Click to view the example code. </summary>

```c
/*
RAK3112 Analog Input Pins

*/

#define analogPin 21  // Use GPIO21

int val = 0;  // variable to store the value read

void setup()
{
  Serial.begin(115200);
}

void loop()
{
  val = analogRead(analogPin);  // read the input pin
  Serial.println(val);          // debug value
}
```
</details>

###### RAK3112 Serial Interface Peripherals

- ** UART **

There is one UART peripheral and one USB peripheral available on the RAK3112.

| **Pin No.** | **Name**          | **Type**      | **Description**                                                         |
|-------------|-------------------|---------------|-------------------------------------------------------------------------|
| 2           | USB_D-            | USB           | USB -                                                                   |
| 3           | USB_D+            | USB           | USB +                                                                   |
| 6           | GPIO44 / UART0_RX | I/O UART      | GPIO / UART RX                                                          |
| 7           | GPIO43 / UART1_TX | I/O UART      | GPIO / UART TX                                                          |

<details>
<summary> Click to view the example code. </summary>

```c
void setup()
{
  Serial.begin(115200);                   // By default Serial is using the USB port.
  Serial0.begin(115200);                  // Serial0 is assigned to the UART0 RX/TX pins
}

void loop()
{
  Serial.println("RAK3112 USB TEST!");
  Serial0.println("RAK3112 UART TEST!");
  delay(1000); // delay for 1 second
}
```
</details>

- ** I2C **

The RAK3112 has two I2C ports

| **Pin No.** | **Name**          | **Type**      | **Description**                                                         |
|-------------|-------------------|---------------|-------------------------------------------------------------------------|
| 13          | GPIO40 / I2C1_SCL | I/O I2C       | GPIO / I2C SCL                                                          |
| 28          | GPIO9 / I2C1_SDA  | I/O I2C       | GPIO / I2C SDA                                                          |
| 39          | GPIO18 / I2C2_SCL | I/O I2C       | GPIO / I2C SCL                                                          |
| 40          | GPIO17 / I2C2_SDA | I/O I2C       | GPIO / I2C SDA                                                          |

Make sure you have an I2C device connected to the specified I2C pins to run the example code below.

<details>
<summary> Click to view the example code. </summary>

```c
#include <Wire.h>

void setup()
{
  Wire.begin();             // Wire is using the I2C2 port on GPIO18 and GPIO17

  Serial.begin(115200);
  while (!Serial);
  Serial.println("\nI2C Scanner");
}

void loop()
{
  byte error, address;
  int nDevices;

  Serial.println("Scanning...");

  nDevices = 0;
  for(address = 1; address < 127; address++ )
  {
    // The i2c_scanner uses the return value of
    // the Write.endTransmisstion to see if
    // a device did acknowledge to the address.
    Wire.beginTransmission(address);
    error = Wire.endTransmission();

    if (error == 0)
    {
      Serial.print("I2C device found at address 0x");
      if (address<16)
        Serial.print("0");
      Serial.print(address,HEX);
      Serial.println("  !");

      nDevices++;
    }
    else if (error==4)
    {
      Serial.print("Unknown error at address 0x");
      if (address<16)
        Serial.print("0");
      Serial.println(address,HEX);
    }
  }
  if (nDevices == 0)
    Serial.println("No I2C devices found\n");
  else
    Serial.println("done\n");

  delay(5000);           // wait 5 seconds for next scan
}
```
</details>

- ** SPI **

The RAK3112 has two SPI ports. But only one SPI port is available for peripherals and exposed. The second SPI port is used internally for the connection to the LoRa transceiver.

| **Pin No.** | **Name**          | **Type**      | **Description**                                                         |
|-------------|-------------------|---------------|-------------------------------------------------------------------------|
| 30          | GPIO10 / SPI_MISO | I/O SPI       | GPIO / SPI MISO                                                         |
| 31          | GPIO11 / SPI_MOSI | I/O SPI       | GPIO / SPI MOSI                                                         |
| 32          | GPIO12 / SPI_CS   | I/O SPI       | GPIO / SPI CS                                                           |
| 33          | GPIO13 / SPI_SCK  | I/O SPI       | GPIO / SPI SCK                                                          |

#### LoRaWAN Example

This example illustrates how to program the RAK3112 as a stand-alone LoRaWAN end device via Arduino APIs and the SX126x-Arduino library. To use the RAK3112 as a LoRaWAN end device, it must be within reach of a working **LoRaWAN gateway** registered to a **LoRaWAN network server (LNS)** or with a built-in network server.

:::tip NOTE
If you are new to LoRaWAN, here are a few good references about LoRaWAN and gateways:
- [LoRaWAN® 101: All You Need To Know](https://news.rakwireless.com/lorawan-r-101-all-you-need-to-know/)
- [What is a LoRaWAN Gateway?](https://news.rakwireless.com/what-is-a-lorawan-gateway/)
- [How Do Gateways for LoRaWAN® Work?](https://news.rakwireless.com/how-do-lorawan-gateways-work/)
- [Things to Consider When Picking a LoRaWAN® Gateway](https://news.rakwireless.com/things-to-consider-when-picking-a-lorawan-gateway/)

:::

To enable the RAK3112 module as a LoRaWAN end-device, a device must first be registered with the LoRaWAN network server. This guide covers both TTN and ChirpStack LoRaWAN network servers and the associated Arduino codes and AT commands for the RAK3112.

- [TheThingsNetwork Guide](https://docs.rakwireless.com/product-categories/wisduo/rak3112-module/quickstart/#connecting-to-the-things-network-ttn): How to login, register new accounts, and create new applications on TTN.
- [RAK3112 TTN OTAA Guide](https://docs.rakwireless.com/product-categories/wisduo/rak3112-module/quickstart/#ttn-otaa-device-registration): How to add OTAA device on TTN and what AT commands to use on RAK3112 OTAA activation.

#### Connect with The Things Network (TTN)

This section shows how to connect the RAK3112 module to the TTN platform.

:::tip NOTE
A working gateway connected to TTN is required, or the device must be within the coverage of a TTN community network.
:::

> **Image:** The Things Stack

As shown in **Figure 22**, The Things Stack (TTN V3) is an open-source LoRaWAN network server suitable for global, geo-distributed public and private deployments as well as for small local networks. The architecture follows the LoRaWAN Network Reference Model for standards compliance and interoperability. This project is actively maintained by [The Things Industries](https://www.thethingsindustries.com/).

LoRaWAN is a protocol for low-power wide-area networks. It allows large-scale Internet of Things deployments where low-powered devices efficiently communicate with internet-connected applications over long-range wireless connections.

The RAK3112 WisDuo module can be part of this ecosystem as a device, and the objective of this section is to demonstrate how simple it is to send data to The Things Stack using the LoRaWAN protocol. To achieve this, the RAK3112 WisDuo module must be located within the coverage of a LoRaWAN gateway connected to The Things Stack server.

1. Sign up for a TTN account.

a. Go to [The Things Network](https://www.thethingsnetwork.org/) and click on **Sign up**.

> **Image:** Sign up an account in TTN

b. Select a community type by clicking **Get started**.

> **Image:** TTN community type

c. Sign up through The Things ID by clicking **Sign up for free**.

> **Image:** Sign up through The Things ID

d. Enter your details, agree to the Terms and Conditions, and click **Sign up to The Things ID**.

> **Image:** Enter account details

e. Then, select a cluster as shown in **Figure 27**.

> **Image:** Select a cluster in TTN

Use the same login credentials on the TTN V2 if you have one. If you have no account yet, create one.

2. Once logged in to the platform, create an application by clicking **Create an application**.

> **Image:** Create a TTN application for your LoRaWAN devices

3. Navigate to the **Applications** tab.

> **Image:** Details of the TTN application

4. Fill in the necessary information about your application, then click **Create application**.

> **Image:** TTN application

If you had no errors in the previous step, the application console page should now be visible. The next step is to add end-devices to your TTN application.

LoRaWAN specifications enforce that each end-device has to be personalized and activated. There are two options for registering devices, depending on the activation mode selected. Activation can be done either via Over-The-Air-Activation (OTAA) or Activation-By-Personalization (ABP).

##### TTN OTAA Device Registration

1. Go to your application console to register a device. To start adding an OTAA end-device, click **+Register end device**, as shown in **Figure 31**.

> **Image:** Register OTAA end-device

2. Register the board by selecting **Enter end device specifics manually**.

> **Image:** Enter OTAA end-device specifics manually

3. Configure the **Frequency plan**, compatible **LoRaWAN version**, and supported **Regional Parameters version**.

> **Image:** OTAA Frequency plan setup

> **Image:** OTAA LoRaWAN version setup

> **Image:** OTAA LoRaWAN Regional Parameters version setup

4. Set the **JoinEUI**.

> **Image:** OTAA JoinEUI setup

5. Click **Show advanced activation, LoRaWAN class and cluster settings**.

> **Image:** OTAA Show advanced activation

6. Configure the following, then click **Confirm**.
  - Activation mode: **Over the air activation (OTAA)**
  - Additional LoRaWAN class capabilities: **None (class A only)**

> **Image:** OTAA LoRaWAN class and cluster settings

7. Once completed, push the _**Confirm**_ button, then enter the device's JoinEUI credential in the **JoinEUI** field.

:::tip NOTE
- The **AppEUI** (**Join EUI**), **DevEUI**, and **AppKey** are hidden in this section as these are unique to a specific device. The **DevEUI** is specific to every RAK3112 device, while the **AppEUI** and **AppKey** should be generated individually for each device and application.
- The **AppEUI** is the same as **JoinEUI**.
:::

> **Image:** OTAA DevEUI credential

8. Click **Generate** under **AppKey**, as shown in **Figure 39**.

> **Image:** OTAA AppKey credential

9. Once done, click **Register end device** to complete the process.

> **Image:** Click Register end device

After completing the device registration, the device should appear on the TTN console, as shown in **Figure 41**.

:::tip NOTE
- The **AppEUI** (**Join EUI**), **DevEUI**, and **AppKey** are the parameters required to activate your LoRaWAN end-device via OTAA.
- The three OTAA parameters on the TTN device console are MSB by default.
- These parameters are always accessible on the device console page, as shown in **Figure 41**.
:::

> **Image:** OTAA end-device successfully registered to TTN

##### Upload OTAA LoRaWAN Example to RAK3112

After successfully registering the RAK3112 device to the LoRaWAN Network Server, proceed with running the RAK3112_OTAA demo application example.

1. Get the example code from [RAK3112_OTAA](https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK3112/communications/LoRa/RAK3112_OTAA).
Copy the code into the Arduino IDE sketch.

> **Image:** OTAA LoRaWAN application example

2. In the example code, modify the device EUI (**DevEUI**) and application key (**AppKey**).

- The DevEUI must match the one registered on your network server. This is the same DevEUI in the RAK3112 sticker if this is the one you used in **Step 7** of the [TTN OTAA Device Registration](https://docs.rakwireless.com/product-categories/wisduo/rak3112-module/quickstart/#ttn-otaa-device-registration) section. DevEUI is **MSB**.

```c
// OTAA Device EUI MSB
uint8_t nodeDeviceEUI[8] = {0xac,0x1f,0x09,0xff,0xfe,0x00,0x00,0x00};
```

- The AppEUI (Join EUI) must match the one registered on your network server as well.

```c
// OTAA Application Key MSB
uint8_t nodeAppEUI[8] = {0x70,0xB3,0xD5,0x7E,0xD0,0x02,0x01,0xE1};
```

- Another important parameter to update is the AppKey, which must match the one configured on your network server in **Step 8** of the [TTN OTAA Device Registration](https://docs.rakwireless.com/product-categories/wisduo/rak3112-module/quickstart/#ttn-otaa-device-registration). AppKey is an **MSB**.

```c
// OTAA Application Key MSB
uint8_t nodeAppKey[16] = {0x2b,0x84,0xe0,0xb0,0x9b,0x68,0xe5,0xcb,0x42,0x17,0x6f,0xe7,0x53,0xdc,0xee,0x79};
```

> **Image:** Update the OTAA, DevEUI, and AppKey

3. This guide uses the AS923-3 regional band, so no changes are needed in the example code. For a different region, update the band in the code accordingly.

:::tip NOTE
RAK3112 supports the following regions (based on definition in SX126x-Arduino library):
* LORAMAC_REGION_EU433 = 4
* LORAMAC_REGION_CN470 = 2
* LORAMAC_REGION_RU864 = 12
* LORAMAC_REGION_IN865 = 7
* LORAMAC_REGION_EU868 = 5
* LORAMAC_REGION_US915 = 8
* LORAMAC_REGION_AU915 = 1
* LORAMAC_REGION_KR920 = 6
* LORAMAC_REGION_AS923 = 0
* LORAMAC_REGION_AS923_2 = 9
* LORAMAC_REGION_AS923_3 = 10
* LORAMAC_REGION_AS923_4 = 11

Additionally, for US915, configuring the channel mask is necessary, with channels 8 to 15 being the most commonly used in this band.

The LoRaWAN region is set in the `lmh_init()` call:

```c
lmh_init(&lora_callbacks, lora_param_init, true, CLASS_A, LORAMAC_REGION_AS923_3);
```

:::

4. The last step is to upload the code by clicking the **Upload** icon. Take note that you should select the right board and port.

> **Image:** Upload the OTAA example code

The terminal logs should now be visible in the Serial Monitor of the Arduino IDE. If the COM port disconnects, the terminal output may not appear immediately. Reconnecting the module or pressing the reset button can help restore the output.

> **Image:** Terminal logs

5. Check the ***Live data*** section on the LoRaWAN network server to see if the device has successfully joined with the `join request` and `join accept` logs.

> **Image:** OTAA live data on TTN

### Arduino Installation

Refer to [Software section](#software).

