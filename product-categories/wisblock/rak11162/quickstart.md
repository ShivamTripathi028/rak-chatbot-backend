---
slug: /product-categories/wisblock/rak11162/quickstart/
title: RAK11162 LoRaWAN BLE Wi-Fi Quick Start Guide | Setup & Configuration
description: Quickly set up your RAK11162 WisBlock Core module for LoRaWAN, Wi-Fi, P2P mode, and firmware updates using WisToolBox. Includes TTN and ChirpStack configuration steps.
image: https://images.docs.rakwireless.com/wisblock/rak11160/rak11160.png
keywords:
  - rak11162 module
  - rak11162 datasheet
  - lorawan module datasheet
  - lorawan ble wifi module specs
  - ble 5 module specs
  - ble 5 module specs
  - wifi transceiver
  - stm32wle5 mcu
  - esp32-c2 mcu
  - lorawan module for iot
  - stm32wle5 lorawan development board
  - esp32-c2 lorawan development board
  - lora wireless module
  - low power mcu
  - lora p2p communication
  - low power consumption modules
  - triple rf iot lorawan module
tags:
  - rak11162
  - quickstart
  - wisblock
date: 2025-05-23
sidebar_label: Quick Start Guide
---

# RAK11162 WisDuo LoRaWAN + BLE + Wi-Fi Module Quick Start Guide

This guide covers the setup of the RAK11162 as a Stand-Alone Device Using RUI3.

:::warning
Due to the STM32WLE5's limitation of only two UART interfaces, no UART is available for the WisBlock Sensor and IO slots. As a result, WisBlock modules that rely on UART communication are not compatible with the RAK11162 Core module. Additionally, because of limited available GPIOs, the second I2C interface used by some WisBlock modules is not accessible through the IO slot.
:::

## Prerequisites

Before going through each and every step on using RAK11162 WisBlock Core, make sure to prepare the necessary items listed below:

#### Hardware

- <a href="https://store.rakwireless.com/products/RAK11162?utm_source=RAK11162WisBlockLPWANModule&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAK11162 WisBlock Core LPWAN+BLE+Wi-Fi Module</a>
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base)
- Your choice of [WisBlock Modules](https://store.rakwireless.com/pages/wisblock)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install the <a href="https://www.arduino.cc/en/Main/Software" target="_blank">Arduino IDE</a>.

:::warning
_**If you are using Windows 10**_.
Do _**NOT**_ install the Arduino IDE from the Microsoft App Store. Instead, install the original Arduino IDE from the <a href="https://support.arduino.cc/hc/en-us/articles/360019833020-Download-and-install-Arduino-IDE" target="_blank">Arduino official website</a>. The Arduino app from the Microsoft App Store has problems using third-party Board Support Packages.
:::

- Add RAK11162 as a supported board in Arduino IDE by updating Board Manager URLs in **Preferences** settings of Arduino IDE with this JSON URL `https://raw.githubusercontent.com/RAKWireless/RAKwireless-Arduino-BSP-Index/main/package_rakwireless_com_rui_index.json`. After that, add **RAKwireless RUI SMT32 Boards** via Arduino board manager.
- <a href="https://downloads.rakwireless.com/LoRa/Tools/RAK_SERIAL_PORT_TOOL_V1.2.1.zip" target="_blank">RAK Serial Port Tool</a>

## Product Configuration

### Hardware Setup

#### RAK11162 to WisBlock Base

The RAK11162 will not work without a WisBlock Base board. The WisBlock Base provides a USB connection for programming the RAK11162. It also provides a power source and various interfaces to RAK11162 so that it can be connected to other [WisBlock Modules](https://store.rakwireless.com/pages/wisblock) via different module slots.

RAKwireless offers many [WisBlock Base Boards](https://store.rakwireless.com/collections/wisblock-base) compatible with WisBlock Core. It is highly recommended for you to look on these WisBlock Base boards to see what matches your requirements in terms of available module slots, power supply options, and overall size.

To illustrate, RAK11162 can be connected to RAK19007 WisBlock Base, as shown in **Figure 1**.

> **Image:** RAK11162 Connection to WisBlock Base RAK19007

Few pins are exposed on RAK19007, and you can easily use them via header pins. The labels are at the back, as shown in **Figure 2**.

> **Image:** WisBlock Base exposed pins

More information can be found on the [official documentation of the specific WisBlock Base](https://docs.rakwireless.com/product-categories/wisblock#wisblock-base) you used in your project.

For RAK19007 WisBlock Base with RAK11162 WisBlock Core, the accessible GPIO pins are defined as follows in the Arduino IDE and Platform IO:

- `WB_IO1` for IO1 pin
- `WB_IO2` for IO2 pin (Also used to control the 3.3 V supply of some WisBlock Modules to achieve low-power IoT devices.)
- `WB_A0` for AIN

There are usable LEDs as well that can be controlled by the RAK11162 on the WisBlock Base board:

- `LED_GREEN`
- `LED_BLUE`

I2C_1 is also exposed on the header of the WisBlock Base board.

- RAK11162 has its I2C interface exposed on the **I2C_1** header pins. These pins are as well shared to the WisBlock Base Slots A-D.

:::warning
Due to the STM32WLE5's limitation of only two UART interfaces, no UART is available for the WisBlock Sensor and IO slots. As a result, WisBlock modules that rely on UART communication are not compatible with the RAK11162 Core module.

Additionally, because of limited available GPIOs, the second I2C interface used by some WisBlock modules is not accessible through the IO slot.
:::

#### RAK11162 to WisBlock Modules

RAK11162 WisBlock Core is designed to be interfaced with other [WisBlock Modules](https://store.rakwireless.com/pages/wisblock) like sensors, displays, and other interfaces. You need to connect these modules to the compatible slots on the WisBlock Base.

Each WisBlock Modules that will be used with RAK11162 WisBlock Core have a dedicated quick start guide you can follow on how to connect to the WisBlock Base.

Listed are the quick start guide of some [WisBlock modules you can buy from our store](https://store.rakwireless.com/pages/wisblock):

:::tip NOTE
The listed links are just examples. **All WisBlock Modules** have their own quick start guide that you can use as a reference to get started on specific modules.
:::

- [RAK1901 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak1901/quickstart/)
- [RAK1902 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak1902/quickstart/)
- [RAK1903 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak1903/quickstart/)

**Figure 3** shows an illustration on how you can combine various WisBlock Modules with the RAK11162 WisBlock Core via the WisBlock Base board.

> **Image:** RAK11162 Connection to WisBlock Base and other WisBlock Modules

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

**Figure 4** shows how to mount the RAK11162 module on top of a WisBlock Base board (RAK19007). Follow carefully the procedure defined in [WisBlock module assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard) in order to secure the connection safely. Once attached, carefully fix the module with one or more pieces of M1.2 x 3 mm screws depending on the module.

> **Image:** RAK11162 Mounting Sketch

##### Disassembling

The procedure in disassembling any type of WisBlock module is the same.

1. First, remove the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

> **Image:** Detaching silkscreen on the WisBlock module

3. Apply force to the module at the position of the connector, as shown in **Figure 7**, to detach the module from the baseboard.

> **Image:** Applying even forces on the proper location of a WisBlock module

#### LoRa and Wi-Fi/BLE Antenna

Another important part component of RAK11162 is the antennas.

> **Image:** LoRa Antenna

> **Image:** BLE/Wi-Fi Antenna

You need to ensure that these antennas are properly connected to have a good LoRa and BLE signal. Also, note that you can damage the RF section of the chip if you power the module without an antenna connected to the IPEX connector.

RAK11162 has a label on its sticker where to connect the antennas, as shown in **Figure 10**.

> **Image:** RAK11162 antenna label

:::tip NOTE
- Detailed information about the RAK11162 LoRa IPEX MHF4 antenna can be found on the <a href="https://downloads.rakwireless.com/LoRa/WisBlock/Accessories/RAK_PCB_Antenna_for_LoRa_863-870_MHz_(RAKARB04)_Datasheet.pdf" target="_blank">863-870 MHz antenna datasheet</a> or the <a href="https://downloads.rakwireless.com/LoRa/WisBlock/Accessories/RAK_PCB_Antenna_for_LoRa_902-928_MHz_(RAKARB03)_Datasheet.pdf" target="_blank">902-928 MHz antenna datasheet</a>.
- If the RAK11162 is not an IPEX MHF4 variant, the connection to the antennas are done via the RF pins. RAKwireless offers <a href="https://store.rakwireless.com/products/antenna-rf-design-service-including-pcb-design-tuning-matching-and-rf-test" target="_blank">RF Antenna Design Service</a> for custom PCB designs.
:::

:::warning
- **Standard IPEX connector will not work on RAK11162.** The IPEX antenna connectors of RAK11162 are a different variant called <a href="https://www.i-pex.com/product/mhf-4" target="_blank">IPEX MHF-4</a>. This is specially designed for low-profile circuit boards with limited spaces.
- When using the LoRa, Wi-Fi or Bluetooth Low Energy transceivers, make sure that the antennas are connected. Using these transceivers without an antenna can damage the module.
:::

#### Battery and Solar Connection

RAK11162 can be powered via the USB cable or Li-Ion/LiPo battery via the dedicated connectors, as shown in **Figure 11**. The matching connector for the battery wires is a [JST PHR-2 2 mm pitch female](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable).

This illustration uses RAK19007 as WisBlock Base. There are other [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base) boards available, and you need to check the datasheet of the specific WisBlock Base board for the right polarity and other parameters.

:::warning

- Batteries can cause harm if not handled properly.
- Only 3.7-4.2 V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5 V solar panels are supported. Do not use 12 V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires match the polarity on the WisBlock Base board. Not all batteries have the same wiring.

:::

> **Image:** WisBlock Base connection

> **Image:** Battery connection

The battery can be recharged as well via small solar panel, as shown in **Figure 13**. The matching connector for the solar panel wires is an [JST ZHR-2 1.5 mm pitch female](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable).

> **Image:** Solar panel connection

Specification of the battery and solar panel can be found on the datasheet of the WisBlock Base.

### Software Setup

The default firmware of the RAK11162 is based on RUI3, which allows you to develop your own custom firmware to connect sensors and other peripherals to it. To develop your custom firmware using the Arduino IDE:

- Add **RAKwireless RUI STM32 Boards** to the Arduino board manager, which will be discussed in this guide.
- Use [RUI3 APIs](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/overview/#writing-rui3-custom-firmware) for your intended application.
- Send AT commands and upload custom firmware via UART or wirelessly via BLE.

:::tip NOTE
The AT commands in RAK11162 are still available even if you compile custom firmware via RUI3, and there is an option to disable them.
:::

#### RAK11162 RUI3 Board Support Package in Arduino IDE

If you don't have an Arduino IDE yet, download it on the <a href="https://www.arduino.cc/en/Main/Software" target="_blank">Arduino official website</a>.

:::tip NOTE
**For Windows 10 and up users**:
If your Arduino IDE was installed from the Microsoft App Store, you need to reinstall your Arduino IDE by downloading it from the <a href="https://support.arduino.cc/hc/en-us/articles/360019833020-Download-and-install-Arduino-IDE" target="_blank">Arduino official website</a>. The Arduino app from the Microsoft App Store has problems using third-party Board Support Packages.
:::

After successfully installing the Arduino IDE, configure it to add the RAK11162 to its board selection by following these steps:

1. Open Arduino IDE and go to **File** > **Preferences**.

> **Image:** Arduino preferences

2. To add the RAK11162 to your Arduino Boards list, edit the **Additional Board Manager URLs**. Click the icon, as shown in **Figure 15**.

> **Image:** Modify additional Board Manager URLs

3. Copy the URL `https://raw.githubusercontent.com/RAKWireless/RAKwireless-Arduino-BSP-Index/main/package_rakwireless_com_rui_index.json` and paste it on the field. If other URLs are already there, just add them on the next line. After adding the URL, click **OK**.

> **Image:** Add additional Board Manager URLs

4. Restart the Arduino IDE.
5. Open the **Boards Manager** from the **Tools** menu.

> **Image:** Open the Arduino Boards Manager

6. Write `RAK` in the search bar, as shown in **Figure 18**. This will display the available **RAKwireless module boards** that can be added to your Arduino board list. Select and install the latest version of the **RAKwireless RUI STM32 Boards**.

> **Image:** Install RAKwireless RUI STM32 boards

7. Once the BSP is installed, select **Tools** > **Boards Manager** > **RAKwireless RUI STM32 Modules** > **WisDuo RAK11160 Board**.

> **Image:** Select the RAK11162 Module

#### Compile an Example With Arduino

1. After adding the RAK11162 to the Arduino IDE, test your setup by running a simple program.

> **Image:** RAK11162 Test

2. Connect the RAK11162 via USB and check the RAK11162 COM port using Windows **Device Manager**. Double-check the USB cable and USB port if the module is not detected.

> **Image:** Device Manager Ports (COM & LPT)

3. Choose RAK11162 in the board selection by navigating to **Tools** > **Boards Manager** and choosing **RAKwireless RUI STM32 Modules** > **WisDuo RAK11160 Board**.

> **Image:** Select RAK11162 module

4. Open the **Tools** menu and select a COM port. **COM27** is currently used.

> **Image:** Select COM port

5. Click on the **Serial Monitor** icon to connect to the COM port.

> **Image:** Open Arduino serial monitor

6. Once connected to the COM port, send AT commands to the RAK11162. For example, to check the RUI version, type `AT+VER=?` in the text field and press **Send**, as shown in **Figure 25**.

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

9. When the compilation is complete, click the **Upload** button to flash the firmware to the RAK11162.

> **Image:** Upload the example code

10. Upon successful upload, the **Device programmed** message will appear.

> **Image:** Device Programmed

:::tip NOTE
- The RAK11162 should automatically enter BOOT mode when firmware is uploaded via the Arduino IDE.
- If it does not, BOOT mode can be manually activated by sending the `AT+BOOT` command. In BOOT mode, standard AT commands will no longer work unless `AT+RUN` is sent to exit BOOT mode.
:::

11. After the **Device Programmed** is completed, you will see the "Hello" message every 5 seconds in the console.

> **Image:** Application log output

#### LoRaWAN Example

This example illustrates how to program the RAK11162 as a stand-alone LoRaWAN end-device via RUI3 Arduino APIs. To use RAK11162 as a LoRaWAN end-device, it must be within reach of a working **LoRaWAN gateway** registered to a **LoRaWAN network server (LNS)** or with a built-in network server.

:::tip NOTE
If you are new to LoRaWAN, here are a few good references about LoRaWAN and gateways:
- <a href="https://news.rakwireless.com/lorawan-r-101-all-you-need-to-know/" target="_blank">LoRaWAN® 101: All You Need To Know</a>
- <a href="https://news.rakwireless.com/what-is-a-lorawan-gateway/" target="_blank">What is a LoRaWAN Gateway?</a>
- <a href="https://news.rakwireless.com/how-do-lorawan-gateways-work/" target="_blank">How Do Gateways for LoRaWAN® Work?</a>
- <a href="https://news.rakwireless.com/things-to-consider-when-picking-a-lorawan-gateway/" target="_blank">Things to Consider When Picking a LoRaWAN® Gateway</a>

:::

To enable the RAK11162 module as a LoRaWAN end-device, a device must first be registered with the LoRaWAN network server. This guide covers both TTN and ChirpStack LoRaWAN network servers and the associated Arduino codes and AT commands for the RAK11162.

- [TheThingsNetwork Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11162/quickstart/#connecting-to-the-things-network-ttn): How to login, register new accounts, and create new applications on TTN.
- [RAK11162 TTN OTAA Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11162/quickstart/#ttn-otaa-device-registration): How to add OTAA device on TTN and what AT commands to use on RAK11162 OTAA activation.
- [RAK11162 TTN ABP Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11162/quickstart/#ttn-abp-device-registration): How to add ABP device on TTN and what AT commands to use on RAK11162 ABP activation.
- [ChirpStack Guide](https://docs.rakwireless.com/product-categories/wisduo/rak11160-module/quickstart/#connecting-with-chirpstack): How to create new applications on ChirpStack.
- [RAK11162 ChirpStack OTAA Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11162/quickstart/#chirpstack-otaa-device-registration): How to add OTAA device to ChirpStack and what AT commands to use on RAK11162 OTAA activation.
- [RAK11162 ChirpStack ABP Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11162/quickstart/#chirpstack-abp-device-registration): How to add ABP device on ChirpStack and what AT commands to use on RAK11162 ABP activation.

#### Connect With The Things Network (TTN)

This section shows how to connect the RAK11162 module to the TTN platform.

:::tip NOTE
A working gateway connected to TTN is required, or the device must be within the coverage of a TTN community network.
:::

> **Image:** The Things Stack

As shown in **Figure 32**, The Things Stack (TTN V3) is an open-source LoRaWAN network server suitable for global, geo-distributed public and private deployments as well as for small local networks. The architecture follows the LoRaWAN Network Reference Model for standards compliance and interoperability. This project is actively maintained by <a href="https://www.thethingsindustries.com/" target="_blank">The Things Industries</a>.

LoRaWAN is a protocol for low-power wide-area networks. It allows large-scale Internet of Things deployments where low-powered devices efficiently communicate with internet-connected applications over long-range wireless connections.

The RAK11162 WisDuo module can be part of this ecosystem as a device, and the objective of this section is to demonstrate how simple it is to send data to The Things Stack using the LoRaWAN protocol. To achieve this, the RAK11162 WisDuo module must be located within the coverage of a LoRaWAN gateway connected to The Things Stack server.

1. Sign up for a TTN account.

a. Go to <a href="https://www.thethingsnetwork.org/" target="_blank">The Things Network</a> and click on **Sign up**.

> **Image:** Sign up an account in TTN

b. Select a community type by clicking **Get started**.

> **Image:** TTN community type

c. Sign up through The Things ID by clicking **Sign up for free**.

> **Image:** Sign up through The Things ID

d. Enter your details, agree to the Terms and Conditions, and click **Sign up to The Things ID**.

> **Image:** Enter account details

e. Then, select a cluster as shown in **Figure 36**.

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

1. Go to your application console to register a device. To start adding an OTAA end-device, click **+Register end device**, as shown in **Figure 40**.

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
- The **AppEUI**, **DevEUI**, and **AppKey** are hidden in this section as these are unique to a specific device. The **DevEUI** is specific to every RAK11162 device, while the **AppEUI** and **AppKey** should be generated individually for each device and application.
- The **AppEUI** is the same as **JoinEUI**.
:::

> **Image:** OTAA DevEUI credential

8. Click **Generate** under **AppKey**, as shown in **Figure 39**.

> **Image:** OTAA AppKey credential

9. Once done, click **Register end device** to complete the process.

> **Image:** Click Register end device

After completing the device registration, the device should appear on the TTN console, as shown in **Figure 50**.

:::tip NOTE
- The **AppEUI**, **DevEUI**, and **AppKey** are the parameters required to activate your LoRaWAN end-device via OTAA. For security reasons, the **AppKey** is hidden by default but can be revealed by clicking the **Show** button. The parameters can also be quickly copied using the **Copy** button.
- The three OTAA parameters on the TTN device console are MSB by default.
- These parameters are always accessible on the device console page, as shown in **Figure 50**.
:::

> **Image:** OTAA end-device successfully registered to TTN

##### Upload OTAA LoRaWAN Example to RAK11162

After successfully registering the RAK11162 device to the LoRaWAN Network Server, proceed with running the LoRaWAN OTAA demo application example.

1. Open the example code under **RAK WisBlock RUI examples**.

> **Image:** OTAA LoRaWAN application example

2. In the example code, modify the device EUI (**DevEUI**) and application key (**AppKey**).

- The DevEUI must match the one registered on your network server. This is the same DevEUI in the RAK11162 sticker if this is the one you used in **Step 7** of the [TTN OTAA Device Registration](https://docs.rakwireless.com/product-categories/wisduo/rak11160-module/quickstart/#ttn-otaa-device-registration) section. DevEUI is **MSB**.

```c
  // OTAA Device EUI MSB
  uint8_t node_device_eui[8] = {0xAC, 0x1F, 0x09, 0xFF, 0xFE, 0x03, 0xEF, 0xAB};
```

- Another important parameter to update is the AppKey, which must match the one configured on your network server in **Step 8** of the [TTN OTAA Device Registration](https://docs.rakwireless.com/product-categories/wisduo/rak11160-module/quickstart/#ttn-otaa-device-registration). AppKey is an **MSB**.

```c
// OTAA Application Key MSB
  uint8_t node_app_key[16] = {0xD9, 0xB8, 0x70, 0x18, 0x3E, 0xF1, 0x00, 0x1D, 0x1B, 0x4F, 0x2B, 0x4C, 0xBF, 0x60, 0xCA, 0x83};
```

> **Image:** Update the OTAA, DevEUI, and AppKey

3. This guide uses the EU868 regional band, so no changes are needed in the example code. For a different region, update the band in the code accordingly.

:::tip NOTE
RAK11162 supports the following regions:
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
- The RAK11162 should automatically enter BOOT mode when firmware is uploaded via Arduino IDE.
- If BOOT mode is not initiated, send `AT+BOOT` manually to force BOOT mode.
:::

> **Image:** Upload the OTAA example code

The terminal logs should now be visible in the Serial Monitor of the Arduino IDE. If the COM port disconnects, the terminal output may not appear immediately. Reconnecting the module or pressing the reset button can help restore the output.

> **Image:** Terminal logs

5. Check the ***Live data*** section on the LoRaWAN network server to see if the device has successfully joined with the `join request` and `join accept` logs.

> **Image:** OTAA live data on TTN

##### TTN ABP Device Registration

1. To register an ABP device, go to your application console and select the application to which you want your device to be added. Then click **+Register end device**, as shown in **Figure 56**.

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

6. Once completed, enter the device's DevEUI credentials in the **DevEUI** field. Alternatively, use the **Generate** button to create create a DevEUI automatically.

:::tip NOTE
- The **DevEUI**, **Device address**, **AppKey**, and **NwkSKey** are hidden in this section as they are unique to each device. The **DevEUI** is specific to every RAK11162 device, while the **Device address**, **AppKey**, and **NwkSKey** should be generated individually for each device and application.
:::

> **Image:** ABP DevEUI credential

7. Click **Generate** under **Device address**, **AppSKey**, and **NwkSKey**, as shown in **Figure 63** to **Figure 65** respectively.

> **Image:** ABP Device address

> **Image:** ABP AppSKey credential

> **Image:** ABP NwkSKey credential

8. Once done, click **Register end device** to complete the process.

> **Image:** Click Register end device

After completing the device registration, the device should appear on the TTN console, as shown in **Figure 67**.

> **Image:** ABP end-device successfully registered to TTN

##### Upload ABP LoRaWAN Example to RAK11162

After successfully registering the RAK11162 module to the LoRaWAN Network Server as an ABP device, proceed with running the LoRaWAN ABP demo application example.

1. Open the example code under **RAK WisBlock RUI examples**.

> **Image:** ABP LoRaWAN application example

2. In the example code, modify the device address (**DEVADDR**), application session key (**APPSKEY**), and network session key (**NWKSKEY**). All these parameters should match the ones generated on the LoRaWAN network server.

> **Image:** Update the DEVADDR, APPSKEY, and NWKSKEY

3. This guide uses the EU868 regional band, so no changes are needed in the example code. For a different region, update the band in the code accordingly.

:::tip NOTE
RAK11162 supports the following regions:
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

4. The last step is to upload the code by clicking the **Upload** icon. Note that you should select the right board and port, as shown in the previous example [LED Blinking](https://docs.rakwireless.com/product-categories/wisduo/rak11160-module/quickstart/#compile-an-example-with-arduino-led-breathing).

:::tip NOTE
- The RAK11162 should automatically enter BOOT mode when firmware is uploaded via Arduino IDE.
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

> **Image:** Advance MAC settings

d. Check `Resets frame counters`. With this enabled, all uplinks and downlinks will be successful even if the device resets/restarts.

> **Image:** Resets Frame Counters

#### Connect With ChirpStack

This section shows how to connect the RAK11162 module to the ChirpStack platform.

> **Image:** Connect RAK11162 to the ChirpStack platform

The ChirpStack, previously known as the LoRaServer project, provides open-source components for building LoRaWAN networks. In the case of TTN, the RAK11162 module is located in the periphery and will transmit the data to the backend servers through a LoRaWAN gateway. Learn more about <a href="https://www.ChirpStack.io/" target="_blank">ChirpStack</a>.

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

Fill in the required parameters, as shown **Figure 79**.

> **Image:** Create a new application

* For this setup, create an Application named **rak_node_test**.

ChirpStack LoraServer supports multiple system configurations, with only one by default.

* **Service profile**: Field is to select the system profile.
* **Payload codec**: It is the parsing method for selecting load data, such as parsing LPP format data.

> **Image:** Fill in the parameters of an application

**Register a New Device**

1. Choose the application created in the previous step, then select the **DEVICES** tab, as shown in **Figure 81** and **Figure 82**.

> **Image:** List of applications created

> **Image:** Application Device tab

2. Once inside the **DEVICE** tab, create a new device (LoRaWAN node) by clicking the **+CREATE** button.

> **Image:** Add a new device

3. Once the node is created, fill in the necessary data. Click the icon to automatically generate a **Device EUI**, or manually enter the correct Device EUI in the edit box.

> **Image:** Add a node into the RAK11162 module

Fill in the parameters requested:
* **Device name and Device description**: These are descriptive texts about your device.
* **Device EUI**: This interface allows you to generate a Device EUI automatically by clicking the generate icon. A specific Device EUI can also be entered directly into the form.
* **Device Profile**:
  * If you want to join in OTAA mode, select **DeviceProfile_OTAA**.
  * If you want to join in ABP mode, select **DeviceProfile_ABP**.

:::tip NOTE
- Device profiles **DeviceProfile_OTAA** and **DeviceProfile_ABP** are only available if you are using the built-in ChirpStack LoRaWAN Server of RAK Gateways.

- If you have your own ChirpStack installation, set up the device profile with `LoRaWAN MAC version 1.0.4` and `LoRaWAN Regional Parameters revision B` to make it compatible with RAK11162.
:::

> **Image:** Generate a new device EUI 

##### ChirpStack OTAA Device Registration

1. If you have selected **DeviceProfile_OTAA**, as shown in **Figure 86**, after the device is created, an Application Key must be created for this device.

> **Image:** ChirpStack OTAA activation

2. A previously created **Application Key** can be entered here, or a new one can be generated automatically by clicking the icon highlighted in red in **Figure 87**.

> **Image:** ChirpStack OTAA set application keys

3. Once the **Application Key** is added to the form, the process can be finalized by clicking the **SET DEVICE-KEYS** button.

* As shown in **Figure 88**, a new device should be listed in the **DEVICES** tab. The most important parameters, such as the **Device EUI**, are shown in the summary.

> **Image:** ChirpStack OTAA list of the device in the device tab

4. To end the process, it is a good practice to review that the **Application Key** is properly associated with this device. The **Application Key** can be verified in the **KEYS (OTAA)** tab, as shown in **Figure 89**.

> **Image:** Application key associated with the new device

5. After registering the RAK11162 in ChirpStack as an OTAA device, create a [custom firmware using the Arduino IDE for the RAK11162](https://docs.rakwireless.com/product-categories/wisduo/rak11160-module/quickstart/#uploading-otaa-lorawan-example-to-rak11160) or use [OTAA AT Commands](https://docs.rakwireless.com/product-categories/wisduo/rak11160-module/quickstart/#otaa-configuration-for-ttn-via-wistoolbox-console) with an external MCU host.

:::tip NOTE
Standard OTAA mode requires the **Device EUI**, **Application Key**, and **Application EUI**, but in ChirpStack’s implementation, only the Device EUI and the Application Key are mandatory. The Application EUI is not required and is not recorded in the Application tab. However, the Device EUI can be reused as the Application EUI when configuring the node.
:::

##### ChirpStack ABP Device Registration

1. When registering a new device, selecting **DeviceProfile_ABP**, as shown in **Figure 90**, signals to the ChirpStack platform that the device will join the LoRaWAN network using ABP mode.

:::tip NOTE
Tick **Disable counting frame verification** to prevent synchronization issues during testing. When the module restarts, the frame counter resets to zero, which ChirpStack may interpret as a replay attack. While disabling this feature is safe for testing, ensure it is enabled in production. Note that in RAK11162, the frame counter resets upon reboot.
:::

> **Image:** Configure a device in the ChirpStack console

2. After selecting the ABP mode, the following parameters will appear under the **ACTIVATION** tab:
  - **Device Address**
  - **Network Session Key**
  - **Application Session Key**

> **Image:** ChirpStack ABP activation parameters

3. The parameters can be generated as random numbers by the platform or can be set with user values. Once these parameters are filled in properly, the process is completed by clicking on the **ACTIVATE DEVICE** button.
4. After registering the RAK11162 in ChirpStack as an ABP device, create a [custom firmware using Arduino IDE for RAK11162](https://docs.rakwireless.com/product-categories/wisduo/rak11160-module/quickstart/#uploading-abp-lorawan-example-to-rak11160) or use [ABP AT Commands](https://docs.rakwireless.com/product-categories/wisduo/rak11160-module/quickstart/#abp-configuration-for-ttn-via-wistoolbox-console) with external MCU host.

#### Wi-Fi Example With RUI3 API

The RUI3 BSP does not include an example for the usage of Wi-Fi on the RAK11162.
This simple example code shows how to connect to an Wi-Fi AP in station mode.

For easier understanding, the code is split here into several parts.

1. Testing the connection to ESP8684 by powering up the ESP8684 and check the response received.
The ESP8684 can be forced into low power mode by controlling the PA0 GPIO of the STM32WLE5. If set to low, the ESP8684 is shut down, if set to high, the ESP8684 is powering up.
Connection to the ESP8684 is done by sending an ***`AT`*** to it through Serial1 of the STM32WLE5 and wait for the response, which should include ***`OK`***.

:::info Expected response
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

2. Set the ESP8684 into Wi-Fi station mode to be able to connect to a Wi-Fi AP.

:::info Expected response

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

3. Request connection to the selected Wi-Fi AP

:::info Expected response
```
AT+cwjap="<MQTT_WIFI_APN>","<MQTT_WIFI_PW>"
WIFI DISCONNECT
WIFI CONNECTED
WIFI GOT IP

OK
```
:::

<details>
<summary> Click to view the example code. </summary>
```c
	// Connect ESP8684 to Wi-Fi AP
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

/** Wi-Fi TX buffer */
char wtx_buf[512];
/** Wi-Fi RX buffer */
char wrx_buf[512];

/** Wi-Fi AP name */
char MQTT_WIFI_APN[32] = "RAKwireless";
/** Wi-Fi AP password */
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

	api.system.firmwareVersion.set("RAK11160-WIFI");

	Serial.println("RAK11160 Wi-Fi");
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

	// Connect ESP8684 to Wi-Fi AP
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
There are many options to setup the ESP8684, only the basic commands are shown here. For a full description how to control the ESP8684, check the <a href="https://docs.espressif.com/projects/esp-at/en/latest/esp32/AT_Command_Set/index.html" target="_blank">Espressif AT command manual</a>.
:::

:::tip NOTE
More examples for the RAK11162 can be found in the <a href="https://github.com/RAKWireless/RUI3-Best-Practice" target="_blank">RUI3-Best-Practices</a> on GitHub.
A more functional example that uses the RAK11162 as a gateway between LoRa P2P devices and an MQTT server can be found in the <a href="https://github.com/RAKWireless/RUI3-Best-Practice" target="_blank">RUI3-Best-Practices</a>
:::

## Miscellaneous

### Upgrade the Firmware

To upgrade the module to the latest firmware version, follow the steps in this section. The latest firmware can be found in the software section of <a href="https://docs.rakwireless.com/product-categories/wisblock/rak11162/datasheet/#firmware" target="_blank">RAK11162 Datasheet</a>.

:::tip NOTE
**What if the RAK11160 module stops responding to AT commands and firmware updates?** 

To recover your device, use the `.hex` file found in the datasheet and upload it using STM32CubeProgrammer. The guide on updating STM32 firmware using STM32CubeProgrammer can be found on RAK Learn site:

- <a href="https://learn.rakwireless.com/hc/en-us/articles/26687606549911-How-To-Guide-STM32CubeProgrammer-for-RAK-Modules" target="_blank">How To Guide: STM32CubeProgrammer for RAK Modules</a>
:::

:::warning
Uploading the **.hex** file via STM32CubeProgrammer will erase all configured data on the device.
:::

#### Firmware Upgrade Through UART2

##### Minimum Hardware and Software Requirements

Refer to the table for the minimum hardware and software required to perform the firmware upgrade via UART2:

| Hardware/Software | Requirement                                   |
| :---------------: | :-------------------------------------------: |
| Computer          | A Windows/Ubuntu/Mac computer                 |
| Firmware File     | Bin firmware file downloaded from the website |
| Others            | A USB to TTL module                           |

##### Firmware Upgrade Procedure

Execute the following procedure to upgrade the firmware in Device Firmware Upgrade (DFU) mode through the UART2 interface.

:::tip NOTE
- The RAK11162 should automatically enter BOOT mode when firmware is uploaded via RAK DFU Tool or WisToolBox.
- If BOOT mode is not initiated, manually send `AT+BOOT` command to start bootloader mode.
:::

1. Download the latest application firmware of the RAK11160.

	- <a href="https://downloads.rakwireless.com/#RUI/RUI3/Image/" target="_blank">RAK11162 Firmware</a>

Refer to the table below:

|      Model       |                             Version                              |                                             Source                                                                 |
| :--------------: | :--------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------: |
|  RAK11160 (.bin) |      RUI3 Application Code only (default baudrate = 115200)      |  <a href="https://downloads.rakwireless.com/RUI/RUI3/Image/RAK11160_latest.bin" target="_blank">Download</a>       |
|  RAK11160 (.hex) | RUI3 Bootloader and Application Code (default baudrate = 115200) |  <a href="https://downloads.rakwireless.com/RUI/RUI3/Image/RAK11160_latest_final.hex" target="_blank">Download</a> |

2. Download the RAK Device Firmware Upgrade (DFU) tool.
	- <a href="https://downloads.rakwireless.com/#LoRa/Tools/RAK_Device_Firmware_Upgrade_tool/" target="_blank">RAK Device Firmware Upgrade (DFU) Tool</a>

3. Connect the RAK11162 module with a computer through a USB to TTL.
4. Open the **RAK Device Firmware Upgrade Tool**. Select the serial port and baud rate (115200) of the module and click the **Select Port** button.

:::tip NOTE
- If the firmware upload repeatedly fails, check your current baud rate setting using the `AT+BAUD=?` command and use that baud rate value in the RAK DFU Tool.
- Another option is to check if you selected the right COM port.
:::

> **Image:** RAK Device Firmware Upgrade Tool

5. Select the application firmware file of the module with the suffix **.bin**.

> **Image:** Select firmware

6. Click the **Upgrade** button to upgrade the device. After the upgrade is complete, the RAK11162 will be ready to work with the new firmware.

> **Image:** Upgrade firmware

> **Image:** Upgrade successful

### Arduino Installation

Refer to [Software section](#software).

