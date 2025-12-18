---
title: RAK11161 Quick Start | WisDuo LoRaWAN BLE WiFi Breakout Board Setup
description: Quickly set up your RAK11161 Breakout Board for LoRaWAN, WiFi, P2P mode, and firmware updates using WisToolBox. Includes TTN and ChirpStack configuration steps.
image: https://images.docs.rakwireless.com/wisduo/rak11161-breakout-board/rak11161.png
keywords:
  - wisduo
  - lorawan module
  - lorawan ble wifi module setup
  - espressif esp8684
  - stm32wle5 lora module with ble and wifi
  - rak11161 quick start
  - rak11161 setup
  - rak11161 device configuration
  - long range low power mcu
  - rak11161 device setup guide
  - rak11161 configuration
tags:
  - rak11161  
  - quickstart
  - wisduo
sidebar_label: Quick Start Guide
slug: /product-categories/wisduo/rak11161-breakout-board/quickstart/
date: 2025-08-05
---

# RAK11161 WisDuo LoRaWAN + BLE + WiFi Breakout Board Quick Start Guide

This guide covers the following topics:

- [RAK11161 as a Stand-Alone Device Using RUI3](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#rak11161-as-a-stand-alone-device-using-rui3)
- [RAK11161 as a LoRa/LoRaWAN Modem via AT Command](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#rak11161-as-a-lora-lorawan-modem-via-at-command)

## Prerequisites

Before going through the steps of installing the RAK11161 WisDuo LPWAN Breakout Board, make sure you have the necessary items listed below.

### Hardware

- [RAK11161 WisDuo LPWAN+BLE+WiFi Breakout Board](https://store.rakwireless.com/products/RAK11161?utm_source=RAK11161&utm_medium=Document&utm_campaign=BuyFromStore)
- Computer
- USB to UART TTL adapter

### Software

- Download and install the [Arduino IDE](https://www.arduino.cc/en/Main/Software).

:::warning
***For Windows 10 users***: **DO NOT** install the Arduino IDE from the Microsoft App Store. Instead, install the original Arduino IDE from the [Arduino official website](https://support.arduino.cc/hc/en-us/articles/360019833020-Download-and-install-Arduino-IDE). The Arduino app from the Microsoft App Store has problems using third-party Board Support Packages.
:::

- Add [RAK11161 as a supported board in Arduino IDE](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#-board-support-package-in-arduino-ide) by updating Board Manager URLs in **Preferences** settings of Arduino IDE with this JSON URL `https://raw.githubusercontent.com/RAKWireless/RAKwireless-Arduino-BSP-Index/main/package_rakwireless_com_rui_index.json`. After that, add **RAKwireless RUI SMT32 Boards** via Arduino board manager.
- [RAK Serial Port Tool](https://downloads.rakwireless.com/LoRa/Tools/RAK_SERIAL_PORT_TOOL_V1.2.1.zip)

## Product Configuration

### RAK11161 as a Stand-Alone Device Using RUI3

This section of the guide covers the following:

1. [Hardware Setup and Access to IO pins of RAK11161](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#hardware-setup)
2. [LoRaWAN OTAA and ABP Example with Arduino IDE](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#lorawan-example)
3. [WiFi Example with RUI3 API](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#wifi-example-with-rui3-api)

#### Hardware Setup

The RAK11161 requires a few hardware connections to function properly. The bare minimum requirement is to have the power section properly configured, along with antennas and a UART connection for AT commands and firmware updates.

> **Image:** RAK11161 schematic

Ensure the antennas are properly connected for a strong LoRa and BLE signal. Powering the module without an antenna connected to the IPEX MHF4 connectors can damage the RF section of the chip.

> **Image:** LoRa antenna

> **Image:** WiFi/BLE antenna

RAK11161 has a label on its sticker indicating where to connect the antennas, as illustrated in **Figure 4**.

> **Image:** RAK11161 antenna label

:::tip NOTE
- Detailed information about the RAK11161 LoRa IPEX MHF4 antenna can be found on the [863-870 MHz antenna datasheet](https://downloads.rakwireless.com/LoRa/WisBlock/Accessories/RAK_PCB_Antenna_for_LoRa_863-870_MHz_(RAKARB04)_Datasheet.pdf) or the [902-928 MHz antenna datasheet](https://downloads.rakwireless.com/LoRa/WisBlock/Accessories/RAK_PCB_Antenna_for_LoRa_902-928_MHz_(RAKARB03)_Datasheet.pdf).
:::

:::warning
- **Standard IPEX connectors will not work on the RAK11161.** The IPEX antenna connectors of RAK11161 are a different variant called [IPEX MHF-4](https://www.i-pex.com/product/mhf-4). This is specially designed for low-profile circuit boards with limited spaces.
- When using the LoRa, WiFi or Bluetooth Low Energy transceivers, make sure that the antennas are connected. Using these transceivers without an antenna can damage the module.
:::

#### Software Setup

The default firmware of the RAK11161 is based on RUI3, which allows you to develop your own custom firmware to connect sensors and other peripherals. To develop your custom firmware using the Arduino IDE, follow these steps:

- Add **RAKwireless RUI STM32 Boards** to the Arduino board manager, which will be discussed in this guide.
- Use [RUI3 APIs](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/overview/#writing-rui3-custom-firmware) for your intended application.
- Send AT commands and upload custom firmware via UART or wirelessly via BLE.

:::tip NOTE
The AT commands in RAK11161 are still available even if you compile custom firmware via RUI3, and there is an option to disable them.
:::

##### RAK11161 RUI3 Board Support Package in Arduino IDE

If you don't have an Arduino IDE yet, download it on the [Arduino official website](https://www.arduino.cc/en/Main/Software).

:::tip NOTE
**For Windows 10 and up users**:
If you installed the Arduino IDE from the Microsoft App Store, uninstall it and reinstall the IDE from the [Arduino official website](https://support.arduino.cc/hc/en-us/articles/360019833020-Download-and-install-Arduino-IDE). The version from the Microsoft App Store has issues with third-party Board Support Packages.
:::

After successfully installing the Arduino IDE, configure it to add the RAK11161 to its board selection by following these steps:

1. Open Arduino IDE and go to **File** > **Preferences**.

> **Image:** Arduino Preferences

2. To add the RAK11161 to your Arduino Boards list, edit the **Additional Board Manager URLs** and click the icon, as shown in **Figure 6**.

> **Image:** Modify Additional Board Manager URLs

3. Copy the URL `https://raw.githubusercontent.com/RAKWireless/RAKwireless-Arduino-BSP-Index/main/package_rakwireless_com_rui_index.json` and paste it on the field. If other URLs are already there, add this new URL on the next line. After adding the URL, click **OK**.

> **Image:** Add Additional Board Manager URLs

4. Restart the Arduino IDE.
5. Open the **Boards Manager** from the **Tools** menu.

> **Image:** Open the Arduino Boards Manager

6. Type `RAK` in the search bar, as shown in **Figure 9**. This will display the available **RAKwireless module boards** that can be added to your Arduino board list. Select and install the latest version of the **RAKwireless RUI STM32 Boards**.

> **Image:** Install RAKwireless RUI STM32 boards

7. Once the BSP is installed, select **Tools** > **Boards Manager** > **RAKwireless RUI STM32 Modules** > **WisDuo RAK11161 Board**.

> **Image:** Select RAK11161 Module

##### Compile an Example with Arduino

1. After adding the RAK11161 to the Arduino IDE, test your setup by running a simple program.

> **Image:** RAK11161 Test

2. Connect the RAK11161 via USB and check the RAK11161 COM port using Windows **Device Manager**. Double-check the USB cable and USB port if the module is not detected.

> **Image:** Device Manager Ports (COM & LPT)

3. Choose RAK11161 in the board selection by navigating to **Tools** > **Boards Manager** and choosing **RAKwireless RUI STM32 Modules** > **WisDuo RAK11160 Board**.

> **Image:** Select RAK11161 breakout board

4. Open the **Tools** menu and select a COM port. **COM27** is currently used.

> **Image:** Select COM port

5. Click on the **Serial Monitor** icon to connect to the COM port.

> **Image:** Open Arduino serial monitor

6. Once connected to the COM port, send AT commands to the RAK11161. For example, to check the RUI version, type `AT+VER=?` in the text field and press **Send**, as shown in **Figure 16**.

> **Image:** Arduino serial monitor COMx

7. Copy the example code below and paste it into Arduino IDE.

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

9. When the compilation is complete, click the **Upload** button to flash the firmware to the RAK11161.

> **Image:** Upload the example code

10. Upon successful upload, the **Device programmed** message will appear.

> **Image:** Device Programmed

:::tip NOTE
- The RAK11161 should automatically enter BOOT mode when firmware is uploaded via the Arduino IDE.
- If it does not, BOOT mode can be manually activated by sending the `AT+BOOT` command. In BOOT mode, standard AT commands will no longer work unless `AT+RUN` is sent to exit BOOT mode.
:::

11. After the **Device Programmed** is completed, you will see the "Hello" message every 5 seconds in the console.

> **Image:** Application log output

##### RAK11161 IO Pins and Peripherals

This section discusses how to use and access the pinouts of the RAK11161 Breakout Board using RUI3 APIs. It shows basic code for using digital IO, analog input, UART, and I2C.

###### RAK11161 Digital IO Pins

Available Digital IO Pins in RAK11161 (with notes on pins with Analog capability)

| ST_GPIO Header # - Pin # | GPIO                 |
|--------------------------|----------------------|
| 1-5                      | ST_PA8               |
| 2-6                      | ST_PA9               |
| 2-7                      | ST_PB2  / Analog(A2) |
| 2-8                      | ST_PB12              |
| 1-6                      | ST_PA10 / Analog(A3) |
| 2-2                      | ST_PA15 / Analog(A4) |
| 2-5                      | ST_PB3  / Analog(A0) |
| 2-4                      | ST_PB4  / Analog(A1) |
| 2-1                      | ST_PB5               |

:::info
The GPIO pins of the ESP8684 ***cannot*** be controlled by the STM32WLE5 directly.
:::

Any of the pins listed in the table above can be used. Pins with specific functions, such as UART and I2C, are also usable but with limitations. Those dedicated pins have been excluded from this illustration of digital IO pins.

<details>

<summary> Click to view the example code. </summary>

```c
/*
 RAK11161 Digital I/O Example

 You can use any of the following as Digital I/O:

ST_PA8    PA8
ST_PA9    PA9
ST_PB2    PB2
ST_PA10   PA10
ST_PB12   PB12
ST_PB3    PB3
ST_PB4    PB4
ST_PB5    PB5
ST_PA1    PA1
ST_PA15   PA15
*/

void setup()
{
  pinMode(PA8, OUTPUT); //Change the PA8 to any digital pin you want. Also, you can set this to INPUT or OUTPUT
}

void loop()
{
  digitalWrite(PA8,HIGH); //Change the PA8 to any digital pin you want. Also, you can set this to HIGH or LOW state.
  delay(1000); // delay for 1 second
  digitalWrite(PA8,LOW); //Change the PA8 to any digital pin you want. Also, you can set this to HIGH or LOW state.
  delay(1000); // delay for 1 second
}
```
</details>

###### RAK11161 Analog Input Pins

Available Analog input Pins in RAK11161

| ST_GPIO Header # - Pin # | Analog in |
|--------------------------|-----------|
| 2-5                      | PB3       |
| 2-4                      | PB4       |
| 2-7                      | PB2       |
| 1-6                      | PA10      |
| 2-2                      | PA15      |

Any of the pins shown in the table above can be used as an Analog Input Pin. See the example code below.

<details>
<summary> Click to view the example code. </summary>

```c
/*
RAK11161 Analog Input Pins

ST_PB5    PB5
ST_PA10   PA10
ST_PB3    PA3
ST_PB4    PB4

*/

#define analogPin PB5  // or you can use PB5

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

###### RAK11161 Serial Interface Peripherals

- ** UART **

There is one UART peripheral available on the RAK11161. There are also different [Serial Operating Modes](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/serial-operating-modes/) possible in RUI3, namely AT Mode, and Custom Mode.

|  **Serial Port**  | **Serial Instance Assignment** | **Default Mode** |
|:-----------------:|:------------------------------:|:----------------:|
| UART2 (PA3)/(PA2) |             Serial             |    AT Command    |

<details>
<summary> Click to view the example code. </summary>

```c
void setup()
{
  Serial.begin(115200);                   // By default Serial is used for FW update and AT command.
}

void loop()
{
  Serial1.println("RAK11161 TEST!");
  delay(1000); // delay for 1 second
}
```
</details>

- ** I2C **

| **I2C** | **ST_GPIO Header # - Pin #** | **GPIO** |
|:--------|:-----------------------------|:--------:|
| SDA     | 1-7                          |   PA11   |
| SCL     | 1-8                          |   PA12   |

Make sure you have an I2C device connected to the specified I2C pins to run the example code below.

<details>
<summary> Click to view the example code. </summary>

```c
#include <Wire.h>

void setup()
{
  Wire.begin();

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

| **SPI** | **ST_GPIO Header # - Pin #** | **GPIO** |
|:--------|:-----------------------------|:--------:|
| NSS     | 1-1                          |   PA4    |
| SCK     | 1-2                          |   PA5    |
| MISO    | 1-3                          |   PA6    |
| MOSI    | 1-4                          |   PA7    |

#### LoRaWAN Example

This example illustrates how to program the RAK11161 as a stand-alone LoRaWAN end-device via RUI3 Arduino APIs. To use RAK11161 as a LoRaWAN end-device, it must be within reach of a working **LoRaWAN gateway** registered to a **LoRaWAN network server (LNS)** or with a built-in network server.

:::tip NOTE
If you are new to LoRaWAN, here are a few good references about LoRaWAN and gateways:
- [LoRaWAN® 101: All You Need To Know](https://news.rakwireless.com/lorawan-r-101-all-you-need-to-know/)
- [What is a LoRaWAN Gateway?](https://news.rakwireless.com/what-is-a-lorawan-gateway/)
- [How Do Gateways for LoRaWAN® Work?](https://news.rakwireless.com/how-do-lorawan-gateways-work/)
- [Things to Consider When Picking a LoRaWAN® Gateway](https://news.rakwireless.com/things-to-consider-when-picking-a-lorawan-gateway/)

:::

To enable the RAK11161 Breakout Board as a LoRaWAN end-device, a device must first be registered with the LoRaWAN network server. This guide covers both TTN and ChirpStack LoRaWAN network servers and the associated Arduino codes and AT commands for the RAK11161.

- [The Things Network Guide](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#connecting-to-the-things-network-ttn): How to login, register new accounts, and create new applications on TTN.
- [RAK11161 TTN OTAA Guide](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#ttn-otaa-device-registration): How to add OTAA device on TTN and what AT commands to use on RAK11161 OTAA activation.
- [RAK11161 TTN ABP Guide](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#ttn-abp-device-registration): How to add ABP device on TTN and what AT commands to use on RAK11161 ABP activation.
- [ChirpStack Guide](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#connecting-with-chirpstack): How to create new applications on ChirpStack.
- [RAK11161 ChirpStack OTAA Guide](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#chirpstack-otaa-device-registration): How to add OTAA device to ChirpStack and what AT commands to use on RAK11161 OTAA activation.
- [RAK11161 ChirpStack ABP Guide](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#chirpstack-abp-device-registration): How to add ABP device on ChirpStack and what AT commands to use on RAK11161 ABP activation.

#### Connect with The Things Network (TTN)

This section shows how to connect the RAK11161 Breakout Board to the TTN platform.

:::tip NOTE
A working gateway connected to TTN is required, or the device must be within the coverage of a TTN community network.
:::

> **Image:** The Things Stack

As shown in **Figure 22**, The Things Stack (TTN V3) is an open-source LoRaWAN network server suitable for global, geo-distributed public and private deployments as well as for small local networks. The architecture follows the LoRaWAN Network Reference Model for standards compliance and interoperability. This project is actively maintained by [The Things Industries](https://www.thethingsindustries.com/).

LoRaWAN is a protocol for low-power wide-area networks. It allows large-scale Internet of Things deployments where low-powered devices efficiently communicate with internet-connected applications over long-range wireless connections.

The RAK11161 WisDuo Breakoout Board can be part of this ecosystem as a device, and the objective of this section is to demonstrate how simple it is to send data to The Things Stack using the LoRaWAN protocol. To achieve this, the RAK11161 WisDuo Breakout Board must be located within the coverage of a LoRaWAN gateway connected to The Things Stack server.

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

4. Set the **JoinEUI** by entering zeros into the field.

> **Image:** OTAA JoinEUI setup

5. Click **Show advanced activation, LoRaWAN class and cluster settings**.

> **Image:** OTAA Show advanced activation

6. Configure the following, then click **Confirm**.
  - Activation mode: **Over the air activation (OTAA)**
  - Additional LoRaWAN class capabilities: **None (class A only)**

> **Image:** OTAA LoRaWAN class and cluster settings

7. Once completed, enter the device's DevEUI credential in the **DevEUI** field. This will automatically generate the specific end-device ID of your board.

:::tip NOTE
- The **AppEUI**, **DevEUI**, and **AppKey** are hidden in this section as these are unique to a specific device. The **DevEUI** is specific to every RAK11161 device, while the **AppEUI** and **AppKey** should be generated individually for each device and application.
- The **AppEUI** is the same as **JoinEUI**.
:::

> **Image:** OTAA DevEUI credential

8. Click **Generate** under **AppKey**, as shown in **Figure 39**.

> **Image:** OTAA AppKey credential

9. Once done, click **Register end device** to complete the process.

> **Image:** Click Register end device

After completing the device registration, the device should appear on the TTN console, as shown in **Figure 41**.

:::tip NOTE
- The **AppEUI**, **DevEUI**, and **AppKey** are the parameters required to activate your LoRaWAN end-device via OTAA. For security reasons, the **AppKey** is hidden by default but can be revealed by clicking the **Show** button. The parameters can also be quickly copied using the **Copy** button.
- The three OTAA parameters on the TTN device console are MSB by default.
- These parameters are always accessible on the device console page, as shown in **Figure 41**.
:::

> **Image:** OTAA end-device successfully registered to TTN

##### Upload OTAA LoRaWAN Example to RAK11161

After successfully registering the RAK11161 device to the LoRaWAN Network Server, proceed with running the LoRaWAN OTAA demo application example.

:::tip NOTE
If you use RAK11161 as a LoRaWAN modem with AT commands instead of a stand-alone device, there is a dedicated section for the [OTAA AT Commands guide](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#otaa-configuration-for-ttn-via-wistoolbox-console) in the later portion of this document.
:::

1. Open the example code under **RAK WisBlock RUI examples**.

> **Image:** OTAA LoRaWAN application example

2. In the example code, modify the device EUI (**DevEUI**) and application key (**AppKey**).

- The DevEUI must match the one registered on your network server. This is the same DevEUI in the RAK11161 sticker if this is the one you used in **Step 7** of the [TTN OTAA Device Registration](https://docs.rakwireless.com/product-categories/wisduo/rak11160-module/quickstart/#ttn-otaa-device-registration) section. DevEUI is **MSB**.

```c
  // OTAA Device EUI MSB
  uint8_t node_device_eui[8] = {0xAC, 0x1F, 0x09, 0xFF, 0xFE, 0x03, 0xEF, 0xAB};
```

- Another important parameter to update is the AppKey, which must match the one configured on your network server in **Step 8** of the [TTN OTAA Device Registration.](https://docs.rakwireless.com/product-categories/wisduo/rak11160-module/quickstart/#ttn-otaa-device-registration) AppKey is an **MSB**.

```c
// OTAA Application Key MSB
  uint8_t node_app_key[16] = {0xD9, 0xB8, 0x70, 0x18, 0x3E, 0xF1, 0x00, 0x1D, 0x1B, 0x4F, 0x2B, 0x4C, 0xBF, 0x60, 0xCA, 0x83};
```

> **Image:** Update the OTAA, DevEUI, and AppKey

3. This guide uses the EU868 regional band, so no changes are needed in the example code. For a different region, update the band in the code accordingly.

:::tip NOTE
RAK11161 supports the following regions:
* RAK_REGION_EU433 = 0
* RAK_REGION_CN470 = 1
* RAK_REGION_RU864 = 2
* RAK_REGION_IN865 = 3
* RAK_REGION_EU868 = 4
* RAK_REGION_US915 = 5
* RAK_REGION_AU915 = 6
* RAK_REGION_KR920 = 7
* RAK_REGION_AS923-1 = 8
* RAK_REGION_AS923-2 = 9
* RAK_REGION_AS923-3 = 10

Additionally, for US915, configuring the channel mask is necessary, with channels 8 to 15 being the most commonly used in this band.

This is the additional code on how to do it:

```c
  if(!(ret = api.lorawan.band.set(5)))      // configure to US915
  {
       Serial.printf("LoRaWan OTAA - set band is incorrect! \r\n");
       return;
  }

  uint16_t maskBuff = 0x0002;               // configure the mask for channels 8-15
  api.lorawan.mask.set(&maskBuff);
```

:::

4. The last step is to upload the code by clicking the **Upload** icon. Take note that you should select the right board and port.

:::tip NOTE
- The RAK11161 should automatically enter BOOT mode when firmware is uploaded via Arduino IDE.
- If BOOT mode is not initiated, send `AT+BOOT` manually to force BOOT mode.
:::

> **Image:** Upload the OTAA example code

The terminal logs should now be visible in the Serial Monitor of the Arduino IDE. If the COM port disconnects, the terminal output may not appear immediately. Reconnecting the module or pressing the reset button can help restore the output.

> **Image:** Terminal logs

5. Check the ***Live data*** section on the LoRaWAN network server to see if the device has successfully joined with the `join request` and `join accept` logs.

> **Image:** OTAA live data on TTN

##### TTN ABP Device Registration

1. To register an ABP device, go to your application console and select the application to which you want your device to be added. Then click **+Register end device**, as shown in **Figure 47**.

> **Image:** Register ABP end-device

2. Register the board by selecting **Enter end device specifics manually**.

> **Image:** Enter ABP end-device specifics manually

3. Configure the **Frequency plan**, compatible **LoRaWAN version**, and supported **Regional Parameters version**.

> **Image:** ABP Frequency plan setup

> **Image:** ABP LoRaWAN version setup

4. Click **Show advanced activation, LoRaWAN class and cluster settings**.

> **Image:** ABP Show advanced activation

5. Configure the following, then click **Confirm**.
  - Activation mode: **Activation by personalization (ABP)**
  - Additional LoRaWAN class capabilities: **None (class A only)**
  - Network defaults (tick off the box): Use network's default MAC settings

> **Image:** ABP LoRaWAN class and cluster settings

6. Once completed, enter the device's DevEUI credentials in the **DevEUI** field. Alternatively, use the **Generate** button to create a DevEUI automatically.

:::tip NOTE
- The **DevEUI**, **Device address**, **AppKey**, and **NwkSKey** are hidden in this section as they are unique to each device. The **DevEUI** is specific to every RAK11161 device, while the **Device address**, **AppKey**, and **NwkSKey** should be generated individually for each device and application.
:::

> **Image:** ABP DevEUI credential

7. Click **Generate** under **Device address**, **AppSKey**, and **NwkSKey**, as shown in **Figure 54** to **Figure 56** respectively.

> **Image:** ABP Device address

> **Image:** ABP AppSKey credential

> **Image:** ABP NwkSKey credential

8. Once done, click **Register end device** to complete the process.

> **Image:** Click Register end device

After completing the device registration, the device should appear on the TTN console, as shown in **Figure 58**.

> **Image:** ABP end-device successfully registered to TTN

##### Upload ABP LoRaWAN Example to RAK11161

After successfully registering the RAK11161 Breakout Board to the LoRaWAN Network Server as an ABP device, proceed with running the LoRaWAN ABP demo application example.

:::tip NOTE

If you use RAK11161 as a LoRaWAN modem using AT commands instead of a stand-alone device, there is a dedicated section for [ABP AT Commands guide](https://docs.rakwireless.com/product-categories/wisduo/rak11160-module/quickstart/#abp-configuration-for-ttn-via-wistoolbox-console) in the later portion of this document.

:::

1. Open the example code under **RAK WisBlock RUI examples**.

> **Image:** ABP LoRaWAN application example

2. In the example code, modify the device address (**DEVADDR**), application session key (**APPSKEY**), and network session key (**NWKSKEY**). All these parameters should match the ones generated on the LoRaWAN network server.

> **Image:** Update the DEVADDR, APPSKEY, and NWKSKEY

3. This guide uses the EU868 regional band, so no changes are needed in the example code. For a different region, update the band in the code accordingly.

:::tip NOTE
RAK11161 supports the following regions:
* RAK_REGION_EU433 = 0
* RAK_REGION_CN470 = 1
* RAK_REGION_RU864 = 2
* RAK_REGION_IN865 = 3
* RAK_REGION_EU868 = 4
* RAK_REGION_US915 = 5
* RAK_REGION_AU915 = 6
* RAK_REGION_KR920 = 7
* RAK_REGION_AS923-1 = 8
* RAK_REGION_AS923-2 = 9
* RAK_REGION_AS923-3 = 10

Additionally, for US915, configuring the channel mask is necessary, with channels 8 to 15 being the most commonly used in this band.

This is the additional code on how to do it.

```c
  if(!(ret = api.lorawan.band.set(5)))      // configure to US915
  {
       Serial.printf("LoRaWan OTAA - set band is incorrect! \r\n");
       return;
  }

  uint16_t maskBuff = 0x0002;               // configure the mask for channels 8-15
  api.lorawan.mask.set(&maskBuff);
```

:::

4. The last step is to upload the code by clicking the **Upload** icon. Note that you should select the right board and port, as shown in the previous example [LED Blinking.](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#compile-an-example-with-arduino-led-breathing)

:::tip NOTE
- The RAK11161 should automatically enter BOOT mode when firmware is uploaded via Arduino IDE.
- If BOOT mode is not initiated, send `AT+BOOT` manually to force BOOT mode.
:::

> **Image:** Upload the ABP example code

The terminal logs should now be visible in the Serial Monitor of the Arduino IDE. If the COM port disconnects, the terminal output may not appear immediately. Reconnecting the module or pressing the reset button can help restore the output.

> **Image:** Terminal logs

5. Check the ***Live data*** section on the LoRaWAN network server if your device is able to send uplink packets.

> **Image:** ABP live data on TTN

6. On ABP, frame counters for both uplink and downlink need to be tracked by the device firmware. However, on RUI3 ABP, there is no tracking, and frame counts will go back to zero when the device resets. This will result in failures on uplinks and downlinks. To prevent this issue, enable the **Resets frame counters** option by following these steps:

a. On The Things Network (TTN) Console and go to **General settings**.

> **Image:** ABP General settings

b. Expand the **Network Layer** by clicking the **Expand** button.

> **Image:** ABP network layer expansion

c. Click on the **Advanced MAC settings** dropdown.

> **Image:** Advanced MAC settings

d. Check `Resets frame counters`. With this enabled, all uplinks and downlinks will be successful even if the device resets/restarts.

> **Image:** Resets Frame Counters

#### Connect with ChirpStack

This section shows how to connect the RAK11161 Breakout Board to the ChirpStack platform.

> **Image:** Connect RAK11161 to the ChirpStack platform

The ChirpStack, previously known as the LoRaServer project, provides open-source components for building LoRaWAN networks. In the case of Chirpstack, the RAK11161 Breakout Board is located in the periphery and will transmit the data to the backend servers through a LoRaWAN gateway. Learn more about [ChirpStack](https://www.ChirpStack.io/).

:::tip NOTE
In this guide, it is assumed that you are using a RAK Gateway and its built-in ChirpStack. Also, the gateway with the ChirpStack must be configured successfully. The frequency band of the nodes should be consistent with the frequency band of the gateway and ChirpStack installation.
:::

##### Create a New Application on ChirpStack

1. Log in to the ChirpStack server using your ChirpStack credentials.
2. Navigate to the **Applications** section and click **+CREATE** to create a new application.

:::tip NOTE
By default, creating a new application is recommended, but existing ones can also be reused.
:::

> **Image:** Applications section

Fill in the required parameters, as shown **Figure 70**.

> **Image:** Create a new application

* For this setup, create an Application named **rak_node_test**.

ChirpStack LoraServer supports multiple system configurations, with only one by default.

* **Service profile**: Field is to select the system profile.
* **Payload codec**: The parsing method for processing payload data, such as parsing LPP format data.

> **Image:** Fill in the parameters of an application

**Register a New Device**

1. Choose the application created in the previous step, then select the **DEVICES** tab, as shown in **Figure 72** and **Figure 73**.

> **Image:** List of applications created

> **Image:** Application Device tab

2. Once inside the **DEVICE** tab, create a new device (LoRaWAN node) by clicking the **+CREATE** button.

> **Image:** Add a new device

3. Once the node is created, fill in the necessary data. Click the icon to automatically generate a **Device EUI**, or manually enter the correct Device EUI in the edit box.

> **Image:** Add a node into the RAK11161 Breakout Board

Fill in the parameters requested:
* **Device name and Device description**: These are descriptive texts about your device.
* **Device EUI**: This interface allows you to generate a Device EUI automatically by clicking the generate icon. A specific Device EUI can also be entered directly into the form.
* **Device Profile**:
  * If you want to join in OTAA mode, select **DeviceProfile_OTAA**.
  * If you want to join in ABP mode, select **DeviceProfile_ABP**.

:::tip NOTE
- Device profiles **DeviceProfile_OTAA** and **DeviceProfile_ABP** are only available if you are using the built-in ChirpStack LoRaWAN Server of RAK Gateways.

- If you have your own ChirpStack installation, set up the device profile with `LoRaWAN MAC version 1.0.4` and `LoRaWAN Regional Parameters revision B` to make it compatible with RAK11161.
:::

> **Image:** Generate a new device EUI 

##### ChirpStack OTAA Device Registration

1. If you have selected **DeviceProfile_OTAA**, as shown in **Figure 77**, after the device is created, an Application Key must be created for this device.

> **Image:** ChirpStack OTAA activation

2. A previously created **Application Key** can be entered here, or a new one can be generated automatically by clicking the icon highlighted in red in **Figure 78**.

> **Image:** ChirpStack OTAA set application keys

3. Once the **Application Key** is added to the form, the process can be finalized by clicking the **SET DEVICE-KEYS** button.

* As shown in **Figure 79**, a new device should be listed in the **DEVICES** tab. The most important parameters, such as the **Device EUI**, are shown in the summary.

> **Image:** ChirpStack OTAA list of the device in the device tab

4. To end the process, it is a good practice to review that the **Application Key** is properly associated with this device. The **Application Key** can be verified in the **KEYS (OTAA)** tab, as shown in **Figure 80**.

> **Image:** Application key associated with the new device

5. After registering the RAK11161 in ChirpStack as an OTAA device, create a [custom firmware using the Arduino IDE for the RAK11161](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#uploading-otaa-lorawan-example-to-rak11160) or use [OTAA AT Commands](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#otaa-configuration-for-ttn-via-wistoolbox-console) with an external MCU host.

:::tip NOTE
Standard OTAA mode requires the **Device EUI**, **Application Key**, and **Application EUI**, but in ChirpStack's implementation, only the Device EUI and the Application Key are mandatory. The Application EUI is not required and is not recorded in the Application tab. However, the Device EUI can be reused as the Application EUI when configuring the node.
:::

##### ChirpStack ABP Device Registration

1. When registering a new device, selecting **DeviceProfile_ABP**, as shown in **Figure 81**, signals to the ChirpStack platform that the device will join the LoRaWAN network using ABP mode.

:::tip NOTE
Tick **Disable counting frame verification** to prevent synchronization issues during testing. When the module restarts, the frame counter resets to zero, which ChirpStack may interpret as a replay attack. While disabling this feature is safe for testing, ensure it is enabled in production. Note that in RAK11161, the frame counter resets upon reboot.
:::

> **Image:** Configure a device in the ChirpStack console

2. After selecting the ABP mode, the following parameters will appear under the **ACTIVATION** tab:
  - **Device Address**
  - **Network Session Key**
  - **Application Session Key**

> **Image:** ChirpStack ABP activation parameters

3. The parameters can be generated as random numbers by the platform or can be set with user values. Once these parameters are filled in properly, the process is completed by clicking on the **ACTIVATE DEVICE** button.
4. After registering the RAK11161 in ChirpStack as an ABP device, create a [custom firmware using Arduino IDE for RAK11161](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#uploading-abp-lorawan-example-to-rak11160) or use [ABP AT Commands](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#abp-configuration-for-ttn-via-wistoolbox-console) with external MCU host.

#### WiFi Example with RUI3 API

The RUI3 BSP does not include an example for the usage of WiFi on the RAK11161.
This simple example code shows how to connect to a WiFi AP in station mode.

For easier understanding, the code is split here into several parts.

1. Test the connection to the ESP8684 by powering it on and checking the response. The ESP8684 can be forced into low-power mode by controlling the PA0 GPIO pin of the STM32WLE5. Setting it low shuts down the ESP8684, while setting it high powers it up. To communicate with the ESP8684, send the ***`AT`*** command through Serial1 of the STM32WLE5 and wait for the response, which should include ***`OK`***.

:::info
Expected response is
```
AT

OK
```
:::

<details>
<summary> Click to view the example code. </summary>
```c
	// Initialize interface to ESP8684
	Serial1.begin(115200);
	// Enable ESP8684
	pinMode(WB_ESP8684, OUTPUT);
	digitalWrite(WB_ESP8684, HIGH);
	// Wait for ESP8684 bootup
	bool found_esp8684 = false;
	time_t start = millis();
	while ((millis() - start) < 30000)
	{
		Serial1.println("AT");
		Serial1.flush();
		if (wait_ok_response(10000))
		{
			Serial.println("ESP8684 found");
			found_esp8684 = true;
			break;
		}
		delay(500);
	}
```
</details>

2. Set the ESP8684 into WiFi station mode to be able to connect to a WiFi AP.

:::info
Expected response is
```
AT+CWMODE=1,1

OK
```
:::

<details>
<summary> Click to view the example code. </summary>
```c
	// Set ESP8684 into station mode and enable auto connect AT+CWMODE=1,1
	// Clear send buffer
	memset(wrx_buf, 0, 512);
	snprintf(wrx_buf, 511, "AT+CWMODE=1,1\r\n");
	Serial1.printf("%s", wrx_buf);
	Serial1.flush();
	if (wait_ok_response(10000))
	{
		Serial.printf("\r\nESP8684 mode set: ==>%s<==\r\n", wtx_buf);
	}
	else
	{
		Serial.printf("\r\nESP8684 mode failed: ==>%s<==\r\n", wtx_buf);
	}
```
</details>

3. Request connection to the selected WiFi AP

:::info
Expected response is
```
AT+CWJAP="<MQTT_WIFI_APN>","<MQTT_WIFI_PW>"
WIFI DISCONNECT
WIFI CONNECTED
WIFI GOT IP

OK
```
:::

<details>
<summary> Click to view the example code. </summary>
```c
	// Connect ESP8684 to WiFi AP
	// Clear send buffer
	memset(wrx_buf, 0, 512);
	snprintf(wrx_buf, 511, "AT+CWJAP=\"%s\",\"%s\"\r\n", MQTT_WIFI_APN, MQTT_WIFI_PW);
	Serial1.printf("%s", wrx_buf);
	Serial1.flush();
	/** Expected response ********************
	AT+cwjap="<MQTT_WIFI_APN>","<MQTT_WIFI_PW>"
	WIFI DISCONNECT
	WIFI CONNECTED
	WIFI GOT IP

	OK
	*****************************************/
	if (wait_ok_response(10000))
	{
		Serial.printf("\r\nESP8684 connected: ==>%s<==\r\n", wtx_buf);
	}
	else
	{
		Serial.printf("\r\nESP8684 not connected: ==>%s<==\r\n", wtx_buf);
	}
```
</details>

Here is the complete example code:

<details>
<summary> Click to view the example code. </summary>
```c
#include <Arduino.h>

// Define enable pin for ESP8684
#define WB_ESP8684 PA0

/** WiFi TX buffer */
char wtx_buf[512];
/** WiFi RX buffer */
char wrx_buf[512];

/** WiFi AP name */
char MQTT_WIFI_APN[32] = "RAKwireless";
/** WiFi AP password */
char MQTT_WIFI_PW[32] = "RAKwireless";

/**
 * @brief Wait for response from ESP8684
 *
 * @param timeout time to wait in milliseconds
 * @param wait_for character array to wait for
 * @return true "OK" string received
 * @return false "OK" string not received, timeout
 */
bool wait_ok_response(time_t timeout)
{
	time_t start = millis();
	int buff_idx = 0;
	bool got_ok = false;

	// Clear TX buffer
	memset(wtx_buf, 0, 512);

	while ((millis() - start) < timeout)
	{
		if (Serial1.available() != 0)
		{
			char rcvd = Serial1.read();
			wtx_buf[buff_idx] = rcvd;
			buff_idx++;
			if (buff_idx == 512)
			{
				// Buffer overflow, return false
				return false;
			}

			if (strstr(wtx_buf, "OK") != NULL)
			{
				return true;
			}
		}
		delay(5);
	}
	return false;
}

/**
 * @brief Arduino setup function, called once
 *
 */
void setup(void)
{
	// Start Serial
	Serial.begin(115200);

	// Delay for 5 seconds to give the chance for AT+BOOT
	delay(5000);

	api.system.firmwareVersion.set("RAK11161-WIFI");

	Serial.println("RAK11161 WiFi");
	Serial.println("---------------------------------------------------------------");
	Serial.println("Setup the device with WisToolBox or AT commands before using it");
	Serial.println("---------------------------------------------------------------");

	// Initialize interface to ESP8684
	Serial1.begin(115200);
	// Enable ESP8684
	pinMode(WB_ESP8684, OUTPUT);
	digitalWrite(WB_ESP8684, HIGH);
	// Wait for ESP8684 bootup
	bool found_esp8684 = false;
	time_t start = millis();
	while ((millis() - start) < 30000)
	{
		Serial1.println("AT");
		Serial1.flush();
		/** Expected response ********************
		AT

		OK
		*****************************************/
		if (wait_ok_response(10000))
		{
			Serial.println("ESP8684 found");
			found_esp8684 = true;
			break;
		}
		delay(500);
	}

	// Set ESP8684 into station mode and enable auto connect AT+CWMODE=1,1
	// Clear send buffer
	memset(wrx_buf, 0, 512);
	snprintf(wrx_buf, 511, "AT+CWMODE=1,1\r\n");
	Serial1.printf("%s", wrx_buf);
	Serial1.flush();
	/** Expected response ********************
	AT+CWMODE=1,1

	OK
	*****************************************/
	if (wait_ok_response(10000))
	{
		Serial.printf("\r\nESP8684 mode set: ==>%s<==\r\n", wtx_buf);
	}
	else
	{
		Serial.printf("\r\nESP8684 mode failed: ==>%s<==\r\n", wtx_buf);
	}

	// Connect ESP8684 to WiFi AP
	// Clear send buffer
	memset(wrx_buf, 0, 512);
	snprintf(wrx_buf, 511, "AT+CWJAP=\"%s\",\"%s\"\r\n", MQTT_WIFI_APN, MQTT_WIFI_PW);
	Serial1.printf("%s", wrx_buf);
	Serial1.flush();
	/** Expected response ********************
	AT+cwjap="<MQTT_WIFI_APN>","<MQTT_WIFI_PW>"
	WIFI DISCONNECT
	WIFI CONNECTED
	WIFI GOT IP

	OK
	*****************************************/
	if (wait_ok_response(10000))
	{
		Serial.printf("\r\nESP8684 connected: ==>%s<==\r\n", wtx_buf);
	}
	else
	{
		Serial.printf("\r\nESP8684 not connected: ==>%s<==\r\n", wtx_buf);
	}
}

/**
 * @brief Arduino loop. Not used
 *
 */
void loop(void)
{
	api.system.sleep.all();
}
```
</details>

:::info
There are many options to setup the ESP8684, only the basic commands are shown here. For a full description how to control the ESP8684, check the [Espressif AT command manual](https://docs.espressif.com/projects/esp-at/en/latest/esp32/AT_Command_Set/index.html).
:::

:::tip NOTE
More examples for the RAK11161 can be found in the [RUI3-Best-Practices on GitHub](https://github.com/RAKWireless/RUI3-Best-Practice), including the functional example that uses the RAK11161 as a gateway between LoRa P2P devices and an MQTT server.
:::

### RAK11161 as a LoRa/LoRaWAN Modem via AT Command

The RAK11161 module can be configured using AT commands via the UART2 interface by default. A USB-to-UART TTL adapter and a serial terminal tool are required to connect the RAK11161 to a computer's USB port. Using the [WisToolBox](https://docs.rakwireless.com/product-categories/software-tools/wistoolbox) is highly recommended for convenient AT command execution and real-time console output. The RAK11161 can be configured in two ways:
- LoRaWAN End-Device
- [LoRa P2P](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/quickstart/#lora-p2p-mode): Point-to-point communication between two RAK11161 Breakout Boards.

UART Parameters for AT Commands:

* Baud Rate: **115200 baud** (Default but configurable)
* Data Bits: **8 bits**
* Stop Bits: **1 stop bit**
* Parity: **NONE**

#### OTAA Configuration for TTN via WisToolBox Console

The RAK11161 Breakout Board can be configured for OTAA using **WisToolBox**, which automatically detects the board when connected to a PC. The following steps outline the setup process in the **WisToolBox Console**.

1. To begin the configuration, type `ATE` to enable command echoing, then press **Enter**.

It is recommended to start by testing the console and verifying that the current configuration is working by sending these two AT commands:

```
AT
```

```
ATE
```

`ATE` is useful for tracking the commands and troubleshooting.

You will receive `OK` when you input the two commands. After setting `ATE`, see all the commands you input together with the replies.

:::tip NOTE

If there is no `OK` or any reply, check if the device is powered correctly. If you are getting power from a USB port, ensure that you have a good USB cable.

:::

> **Image:** Type a command to send

> **Image:** Enable local echoing

> **Image:** Local echoing enabled

2. Set the LoRaWAN join mode to **OTAA**. To determine the required parameter, type `AT+NJM?` in the console terminal and press **Enter**.

> **Image:** Join mode query

> **Image:** Join mode options

- For **OTAA**, input `AT+NJM=1` and then press **Enter** as shown in **Figure 88**.

> **Image:** OTAA join mode

3. Once done, set the LoRaWAN region to EU868. To verify the required parameter, type `AT+BAND?` in the console terminal and press **Enter**. For **EU868**, enter `AT+BAND=4` and press **Enter**. For other regional bands, refer to the **List of band parameter options** table below.

Set the frequency/region to EU868.

```
AT+BAND=4
```

:::tip NOTE
- Based on the selected Regional Band, configuring the sub-band on the RAK11161 may be necessary to ensure compatibility with the gateway and LoRaWAN network server. This is particularly important for bands such as US915, AU915, and CN470.
- To [configure the masking of channels for the sub-bands](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/at-command-manual/#at-mask), use the `AT+MASK` command that can be found on the AT Command Manual.
- To illustrate, use sub-band 2 by sending the command `AT+MASK=0002`.
:::

**List of band parameter options**

| Code | Regional Band |
|:----:|:-------------:|
|  0   |     EU433     |
|  1   |     CN470     |
|  2   |     RU864     |
|  3   |     IN865     |
|  4   |     EU868     |
|  5   |     US915     |
|  6   |     AU915     |
|  7   |     KR920     |
|  8   |    AS923-1    |
|  9   |    AS923-2    |
|  10  |    AS923-3    |
|  11  |    AS923-4    |

> **Image:** Frequency band query

> **Image:** Frequency band options

- For **EU868**, enter `AT+BAND=4` and press **Enter**. For other regional bands, refer to the **List of band parameter options** table below.

> **Image:** EU868 frequency band

4. Update the OTAA credentials of the device. Open the console where the RAK11161 end device was created, copy the specific **Activation information** needed.

> **Image:** Your created OTAA device overview in the TTN Console

**For the Application EUI (**AppEUI**)**

a. Copy the AppEUI credential, as shown in **Figure 93**.

> **Image:** Copy the AppEUI credential from TTN

b. Go to the WisToolBox console and write the appropriate AT command.
- For the **AppEUI**, write the `AT+APPEUI` command, as shown in **Figure 94** to **Figure 96**.

> **Image:** Search for the AppSKey command

> **Image:** Insert AT+APPEUI command in the console

> **Image:** AT+APPEUI in the console

c. Paste the copied credential after the AT command into the WisToolBox console, and press **Enter**.

> **Image:** Paste AppEUI credential from TTN to the console

5. After adding the AppEUI credential, do the same procedure for the **Application key (AppKey)** and the **Device EUI (DevEUI)**.

**For the Application key (**AppKey**)**

a. Copy the AppKey credential, as shown in **Figure 98**.

> **Image:** Copy the AppKey credential from TTN

b. Go to the WisToolBox console and write the `AT+APPKEY` command, as shown in **Figure 99** to **Figure 101**.

> **Image:** Search for the AppKey command

> **Image:** Insert AT+APPKEY command in the console

> **Image:** AT+APPKEY in the console

c. Paste the copied credential after the AT command, as shown in **Figure 102**, and press **Enter**.

> **Image:** Paste AppKey credential from TTN to the console

**For the Device EUI (**DevEUI**)**

a. Copy the DevEUI credential, as shown in **Figure 103**.

> **Image:** Copy the DevEUI credential from TTN

b. Go to the WisToolBox console and write the `AT+DEVEUI` command, as shown in **Figure 104** to **Figure 105**.

> **Image:** Search for the AT+DEVEUI command

> **Image:** AT+DEVEUI in the console

c. Paste the copied credential after the AT command, as shown in **Figure 106**, and press **Enter**.

> **Image:** Paste DevEUI credential from TTN to the console

6. With the OTAA device set up using the WisToolBox console, it is ready to join the network. Open the WisToolBox console, enter `AT+JOIN`, change it to `AT+JOIN=1`, and press **Enter** to initiate the connection.

:::tip NOTE
- `AT+JOIN` command parameters are optional. Configure the settings for auto-join, reattempt interval, and the number of join attempts if your application needs them. If not configured, it will use the default parameter values.
- `AT+JOIN` and `AT+JOIN=1` also share the common functionality of trying to join the network.
:::

Join command format: **`AT+JOIN=w:x:y:z`**

| Parameter |                         Description                          |
|:---------:|:------------------------------------------------------------:|
|     w     |         Join command - 1: joining, 0: stop joining.          |
|     x     | Auto-join config - 1: auto-join on power-up, 0: no auto-join |
|     y     |  Reattempt interval in seconds (7-255) - 8 is the default.   |
|     z     |     Number of join attempts (0-255) - 0 is the default.      |

After 5-6 seconds, if the request is successfully received by a LoRa gateway, a `+EVT:JOINED` status reply will appear.

:::tip NOTE
- If the OTAA device failed to join, check if your device is within reach of a working LoRaWAN gateway that is configured to connect to TTN. It is also important to check that all your OTAA parameters (DevEUI, APPEUI, and AppKey) are correct using the `AT+DevEUI=?`, `AT+APPEUI=?`, and `AT+AppKey=?` commands. Lastly, ensure that the antenna of your device is properly connected.
- After checking all the things above, try to join again.
:::

> **Image:** Search for the AT+JOIN command

> **Image:** Insert AT+JOIN command in the console

> **Image:** AT+JOIN in the console

> **Image:** Join blocking mode

> **Image:** OTAA device successfully joined the network

> **Image:** OTAA device join process displayed in TTN Live data

7. With the end-device properly joined to the TTN, try to send some payload after a successful join.

> **Image:** Search for the AT+SEND command

> **Image:** Insert AT+SEND command in the console

Send command format: **`AT+SEND=<port>:<payload>`**
```
AT+SEND=2:12345678
```

> **Image:** Add the port and payload

> **Image:** Transmission log confirmation

The data sent by the RAK11161 module appears in the ***Live data*** section of the TTN device console. Additionally, the ***Last seen*** timestamp should reflect activity from a few seconds or minutes ago.

> **Image:** OTAA test data sent and displayed in TTN Live data

#### ABP Configuration for TTN via WisToolBox Console

This section shows the ABP configuration guide using **WisToolBox console**. Below are the steps for setting up your **RAK11161** using **WisToolBox Console**.

1. To begin the configuration, type `ATE` to enable command echoing. Then, press **Enter**.

It is recommended to start by testing the console and verifying that the current configuration is working by sending these two AT commands:

```
AT
```

```
ATE
```

`ATE` is useful for tracking the commands and troubleshooting.

You will receive `OK` when you input the two commands. After setting `ATE`, see all the commands you input together with the replies.

:::tip NOTE

If there is no `OK` or any reply, check if the device is powered correctly. If you are getting power from a USB port, ensure that you have a good USB cable.

:::

> **Image:** Type a command to send

> **Image:** Enable local echoing

> **Image:** Local echoing enabled

2. Set the LoRaWAN join mode to **ABP**. To determine the required parameter, type `AT+NJM?` in the console terminal and press **Enter**.

> **Image:** Join mode query

> **Image:** Join mode options

- For **ABP**, input `AT+NJM=0` and then press **Enter**, as shown in **Figure 123**.

> **Image:** ABP join mode

3. Once done, set the LoRaWAN region to EU868. To verify the required parameter, type `AT+BAND?` in the console terminal and press **Enter**.

```
AT+BAND=4
```

:::tip NOTE
- Based on the selected Regional Band, configuring the sub-band on the RAK11161 may be necessary to ensure compatibility with the gateway and LoRaWAN network server. This is particularly important for bands such as US915, AU915, and CN470.
- To [configure the masking of channels for the sub-bands](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/at-command-manual/#at-mask), use the `AT+MASK` command that can be found on the AT Command Manual.
- To illustrate, use sub-band 2 by sending the command `AT+MASK=0002`.
:::

**List of band parameter options**

| Code | Regional Band |
|:----:|:-------------:|
|  0   |     EU433     |
|  1   |     CN470     |
|  2   |     RU864     |
|  3   |     IN865     |
|  4   |     EU868     |
|  5   |     US915     |
|  6   |     AU915     |
|  7   |     KR920     |
|  8   |    AS923-1    |
|  9   |    AS923-2    |
|  10  |    AS923-3    |
|  11  |    AS923-4    |

> **Image:** Frequency band query

> **Image:** Frequency band options

- For **EU868**, enter `AT+BAND=4` and press **Enter**. For other regional bands, refer to the **List of band parameter options** table below.

> **Image:** EU868 frequency band

4. Update the ABP credentials of the device. Open the console where the RAK11161 end device was created, copy the specific **Activation information** needed.

> **Image:** Your created ABP device overview in the TTN Console

**For the Application session key (**AppSKey**)**

a. Copy the AppSKey credential, as shown in **Figure 128**.

> **Image:** Copy the AppSKey credential from TTN

b. Go to the WisToolBox console and write the appropriate AT command.
- For the **AppSKey**, write the `AT+APPSKEY` command, as shown in **Figure 129** to **Figure 131**.

> **Image:** Search for the AppSKey command

> **Image:** Insert AT+APPSKEY command in the console

> **Image:** AT+APPSKEY in the console

c. Paste the copied credential after the AT command into the WisToolBox console, and press **Enter**.

> **Image:** Paste AppKey credential from TTN to the console

5. After adding the **AppSKey** credential, do the same procedure for the **Device address** and the Network session key (**NwkSKey**).

**For **Device address****

a. Copy the Device address, as shown in **Figure 133**.

> **Image:** Copy the Device Address credential from TTN

b. Go to the WisToolBox console and write the `AT+DEVADDR` command, as shown in **Figure 134** to **Figure 136**.

> **Image:** Search for the Device Address command

> **Image:** Insert AT+DEVADDR command in the console

> **Image:** AT+DEVADDR in the console

c. Paste the copied credential after the AT command, as shown in **Figure 137**, and press **Enter**.

> **Image:** Paste Device address from TTN to the console

**For Network session key (**NwkSKey**)**

a. Copy the NwkSKey credential, as shown in **Figure 138**.

> **Image:** Copy the NwkSKey credential from TTN

b. Go to the WisToolBox console and write the `AT+NWKSKEY` command, as shown in **Figure 139** to **Figure 141**.

> **Image:** Search for the AT+NWKSKEY command

> **Image:** Insert AT+NWKSKEY command in the console

> **Image:** AT+NWKSKEY in the console

c. Paste the copied credential after the AT command, as shown in **Figure 142**, and press **Enter**.

> **Image:** Paste NwkSKey credential from TTN to the console

6. With the ABP device configured using the WisToolBox console, it is now directly connected to the network, eliminating the need for a joining procedure. To test data transmission, reopen the WisToolBox terminal console and send a payload to TTN.

> **Image:** Search for the AT+SEND command

> **Image:** Insert AT+SEND command in the console

Send command format: **`AT+SEND=<port>:<payload>`**
```
AT+SEND=2:12345678
```

> **Image:** Add the port and payload

> **Image:** Transmission log confirmation

The data sent by the RAK11161 Breakout Board appears in the ***Live data*** section of the TTN device console. Additionally, the ***Last seen*** timestamp should reflect activity from a few seconds or minutes ago.

> **Image:** ABP test data sent and displayed in TTN Live data

##### LoRa P2P Mode

This section shows how to set up and connect two RAK11161 units to work in the LoRa P2P mode. The configuration of the RAK11161 units is done by connecting the two modules to a general-purpose computer using a USB-UART converter.

The setup of each RAK11161 can be done separately, but testing the LoRa P2P mode will require having both units connected simultaneously. This could be done by having one computer with two USB ports or two computers with one USB port each.

It is recommended to start by testing the serial communication and verifying the current configuration is working by sending these two AT commands:

```
AT
```

```
ATE
```

`ATE` will echo the commands you input to the module, which is useful for tracking the commands and troubleshooting.

You will receive `OK` when you input the two commands. After setting `ATE`, see all the commands you input together with the replies.

Try again `AT` and you should see it on the terminal followed by `OK`.

> **Image:** AT command response

1. To set up the RAK11161 to work in LoRa P2P mode, input the work mode command on both RAK11161 Breakout Boards. If sending commands via USB, disconnecting and reconnecting the module may be necessary as it switches modes of operation.

```
AT+NWM=0
```

2. For this P2P setup, the LoRa parameters are the following:

- Link frequency: **868000000 Hz**
- Spreading factor: **7**
- Bandwidth: **125 kHz**
- Coding Rate: 0 = **4/5**
- Preamble Length: **10**
- Power: **14 dBm**

```
AT+P2P=868000000:7:125:0:10:14
```

> **Image:** P2P setup

<!-- There seems to be no P2P mode section in the AT command manual page of RAK11161 yet. This comment and the comment tag on the NOTE will be removed once the P2P mode section will be added. -->

<!-- :::tip NOTE
Refer to the [P2P Mode](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/at-command-manual/) section of the AT command documentation to learn more about the definition of the parameters used.
::: -->

3. To set one module as a receiver (RX), set the value of the P2P to receive a command to 65535.

```
AT+PRECV=65535
```

With one module configured as RX, the other device will be the TX. Try to sending a P2P payload.

```
AT+PSEND=11223344
```

:::tip NOTE

- If the `AT+PRECV` value is set to 65534, the device will continuously listen to P2P LoRa TX packets without any timeout. This is the same as setting the device in RX mode.
- If the `AT+PRECV` value is set to 65535, the device will listen to P2P TX without a timeout. But it will stop listening once a P2P LoRa packet is received to save power.
- If the `AT+PRECV` value is 0, the device will stop listening to P2P TX data. The device is in TX mode.

:::

> **Image:** Sent and received P2P LoRa Packets

### WiFi Example with AT Commands

The ESP8684 co-processor is handling the WiFi and BLE communication. The STM32WLE5 can communicate with the ESP8684 with AT commands through its internal UART.

The Espressif AT command manual can be found on Espressif's website in [ESP-AT User Guide](https://docs.espressif.com/projects/esp-at/en/latest/esp32/AT_Command_Set/index.html).

:::info
There are many options to setup the ESP8684, only the basic commands are shown here. For a full description how to control the ESP8684, please check the Espressif AT command manual.
:::

To send AT commands from the console or an external host MCU, you have to change the UART mode of the STM32WLE5 to loop-through mode. This is done with the AT command AT+ESP=x

To enable loop-through mode:
```AT
AT+ESP=1
```

To disable loop-through mode:
```AT
AT+ESP=0
```

#### Connect to a WiFi AP

To connect to a WiFi AP, the ESP8684 must be set to station mode. Then the AP name and AP access password must be provided.
The AP name and AP access password are stored in the ESP8684 and will be reused on the next reboot/power up to automatically connect WiFi.

Connect to a WiFi AP and enable auto-connect:
```AT
AT+ESP=1

AT+CWMODE=1,1
AT+CWJAP="<MQTT_WIFI_APN>","<MQTT_WIFI_PW>"
```
Replace `<MQTT_WIFI_APN>` and `<MQTT_WIFI_PW>` with the AP name and access credential of the WiFi access point.

If the ESP8684 can successfully connect to the WiFi AP, it will response with
```AT
WIFI DISCONNECT
WIFI CONNECTED
WIFI GOT IP

OK
```

#### Connect to a MQTT Broker Through WiFi

To connect to the MQTT broker two AT commands are required to setup the connection.

Define user:
```AT
AT+MQTTUSERCFG=0,1,"<MQTT_USER>","<MQTT_USERNAME>","<MQTT_PASSWORD>",0,0,""
```
Replace `<MQTT_USER>`, `<MQTT_USERNAME>` and `<MQTT_PASSWORD>` with the user ID, username and password required to connect.

Define connection and start connection:
```AT
AT+MQTTCONN=0,"<MQTT_URL>",<MQTT_PORT>,0
```
Replace `<MQTT_URL>` and `<MQTT_PORT>` with the URL or IP address of the MQTT broker and the used port.

If the setup and connection is successful, the ESP8684 will response with `OK` and `+MQTTCONNECTED`:
```AT
AT+MQTTUSERCFG=0,1,"<MQTT_USER>","<MQTT_USERNAME>","<MQTT_PASSWORD>",0,0,""

OK

AT+MQTTCONN=0,"<MQTT_URL>",<MQTT_PORT>,0
+MQTTCONNECTED:0,1,"<MQTT_URL>","<MQTT_PORT>","",0

OK
```

Then it is possible to publish data with:
```AT
AT+MQTTPUB=0,"<MQTT_PUB>","<data>",0,0
```
Replace `<MQTT_PUB>`with the topic to which the data should be published, and replace `<data>` with the string containing the data to publish.

It is as well possible to subscribe to a topic on the MQTT broker with:
```AT
AT+MQTTSUB=0,"<MQTT_TOPIC>",1
```
Replace `<MQTT_TOPIC>`with the topic to subscribe to.

:::info
The received data of the subscription will be reported by the ESP8684 with an asynchronous event. To receive this event, the loop-through of the ESP8684 to the host MCU must stay enabled.
:::

## Miscellaneous

### Upgrade the Firmware

To upgrade the module to the latest firmware version, follow the steps in this section. [RAK11161 latest firmware](https://docs.rakwireless.com/product-categories/wisduo/rak11161-breakout-board/datasheet/#firmware) can be found in the software section of the datasheet.

:::tip NOTE
**What if the RAK11161 Breakout Board stops responding to AT commands and firmware updates?**
To recover your device, use the `.hex` file found in the datasheet and upload it using STM32CubeProgrammer. The guide on updating STM32 firmware using STM32CubeProgrammer can be found in the [How To Guide: STM32CubeProgrammer for RAK Modules](https://learn.rakwireless.com/hc/en-us/articles/26687606549911-How-To-Guide-STM32CubeProgrammer-for-RAK-Modules).
:::

:::warning
Uploading the **.hex** file via STM32CubeProgrammer will erase all configured data on the device.
:::

#### Firmware Upgrade Through UART2

##### Minimum Hardware and Software Requirements

Refer to the table for the minimum hardware and software required to perform the firmware upgrade via UART2:

| Hardware/Software |                  Requirement                  |
|:-----------------:|:---------------------------------------------:|
|     Computer      |         A Windows/Ubuntu/Mac computer         |
|   Firmware File   | Bin firmware file downloaded from the website |
|      Others       |              A USB to TTL module              |

##### Firmware Upgrade Procedure

Execute the following procedure to upgrade the firmware in Device Firmware Upgrade (DFU) mode through the UART2 interface.

:::tip NOTE
- The RAK11161 should automatically enter BOOT mode when firmware is uploaded via RAK DFU Tool or WisToolBox.
- If BOOT mode is not initiated, manually send `AT+BOOT` command to start bootloader mode.
:::

1. Download the latest application firmware of the RAK11161.

	- [RAK11161 Firmware](https://downloads.rakwireless.com/#RUI/RUI3/Image/)

Refer to the table below:

|      Model      |                             Version                              |                                                      Source                                                       |
|:---------------:|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| RAK11161 (.bin) |      RUI3 Application Code only (default baudrate = 115200)      |    [Download](https://downloads.rakwireless.com/RUI/RUI3/Image/RAK11160_latest.bin)    |
| RAK11161 (.hex) | RUI3 Bootloader and Application Code (default baudrate = 115200) | [Download](https://downloads.rakwireless.com/RUI/RUI3/Image/RAK11160_latest_final.hex) |

2. Download the RAK Device Firmware Upgrade (DFU) tool.
	- [RAK Device Firmware Upgrade (DFU) Tool](https://downloads.rakwireless.com/#LoRa/Tools/RAK_Device_Firmware_Upgrade_tool/)

3. Connect the RAK11161 Breakout Board with a computer through a USB to TTL.
4. Open the **RAK Device Firmware Upgrade Tool**. Select the serial port and baud rate (115200) of the module and click the **Select Port** button.

:::tip NOTE
- If the firmware upload repeatedly fails, check your current baud rate setting using the `AT+BAUD=?` command and use that baud rate value in the RAK DFU Tool.
- Another option is to check if you selected the right COM port.
:::

> **Image:** RAK Device Firmware Upgrade Tool

5. Select the application firmware file of the module with the suffix **.bin**.

> **Image:** Select firmware

6. Click the **Upgrade** button to upgrade the device. After the upgrade is complete, the RAK11161 will be ready to work with the new firmware.

> **Image:** Upgrade firmware

> **Image:** Upgrade successful

### Arduino Installation

Refer to [Software section](#software).

