---
slug: /product-categories/wisblock/rak3372/quickstart/
title: RAK3372 WisBlock LPWAN Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK3372. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: https://images.docs.rakwireless.com/wisblock/rak3372/rak3372.png
keywords:
  - RAK3372
  - quickstart
  - wisblock
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK3372 WisBlock LPWAN Module Quick Start Guide

This guide explains how to use the RAK3372 as a WisBlock Core module, including steps for preparing the hardware and setting up the necessary software.

Although the RAK3372 WisBlock Core offers many more features and applications, this guide focuses only on demonstrating the <a href="https://docs.rakwireless.com/product-categories/wisblock/rak3372/quickstart/#compile-an-example-with-arduino-led-breathing" target="_blank">LED Breathing</a> and the <a href="https://docs.rakwireless.com/product-categories/wisblock/rak3372/quickstart/#lorawan-example" target="_blank">LoRaWAN OTAA</a> example.

By following this guide, you will successfully set up a working RAK3372 WisBlock Core.

This guide also includes instructions on how to perform <a href="https://docs.rakwireless.com/product-categories/wisblock/rak3372/quickstart/#upgrading-the-firmware" target="_blank">firmware update</a>.

## Prerequisite

### Package Inclusions

Before going through each and every step on using RAK3372 WisBlock Core, make sure to prepare the necessary items listed below:

#### Hardware

- <a href="https://store.rakwireless.com/products/wisblock-core-module-rak3372?utm_source=RAK3372&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAK3372 WisBlock Core</a>
- Your choice of <a href="https://store.rakwireless.com/collections/wisblock-base" target="_blank">WisBlock Base</a>
- USB Cable
- <a href="https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">Li-Ion/LiPo battery</a> (optional)
- <a href="https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">Solar charger</a> (optional)

#### Software

##### Arduino IDE

- Download and install the <a href="https://www.arduino.cc/en/Main/Software" target="_blank">Arduino IDE</a>.

:::warning
_**If you are using Windows 10**_: <br/>
Do _**NOT**_ install the Arduino IDE from the Microsoft App Store. Instead, install the original Arduino IDE from the <a href="https://www.arduino.cc/en/software" target="_blank">Arduino official website</a>. The Arduino app from the Microsoft App Store has problems using third-party Board Support Packages.
:::

- Add <a href="#rak3172-rui3-board-support-package-in-arduino-ide" target="_blank">RAK3172 as a supported board in Arduino IDE</a> by updating Board Manager URLs in **Preferences** settings of Arduino IDE with the JSON URL below.


```json
https://raw.githubusercontent.com/RAKWireless/RAKwireless-Arduino-BSP-Index/main/package_rakwireless_com_rui_index.json
```
After that, add **RAKwireless RUI STM32 Boards** via Arduino board manager.


## Product Configuration

### Hardware Setup

The RAK3372 must be connected to a WisBlock Base along with an antenna. Various WisBlock Modules can be interfaced using the available slots on the WisBlock Base. Additionally, a battery can be added as a power source, with optional solar charging. All hardware-related configurations for the RAK3372 are covered in this guide.

This section covers:

- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak3372/quickstart/#rak3372-to-wisblock-base" target="_blank">RAK3372 Connection to Base Board</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak3372/quickstart/#assembling-and-disassembling-of-wisblock-modules" target="_blank">Assembling and Disassembling of WisBlock Modules</a>
- <a href="https://docs.rakwireless.com/product-categories/wisblock/rak3372/quickstart/#battery-and-solar-connection" target="_blank">Antenna and Battery/Solar Connection</a>

#### RAK3372 to WisBlock Base

The RAK3372 will not work without a WisBlock Base board. The WisBlock Base provides a USB connection for programming the RAK3372. It also provides a power source and various interfaces to RAK3372 so that it can be connected to other <a href="https://store.rakwireless.com/pages/wisblock" target="_blank">WisBlock Modules</a> via different module slots.

RAKwireless offers many <a href="https://store.rakwireless.com/collections/wisblock-base" target="_blank">WisBlock Base Boards</a> compatible with WisBlock Core. It is highly recommended to look at these WisBlock Base boards to see what matches your requirements in terms of available module slots, power supply options, and overall size.

:::warning
- RAK3372 WB_IO3 (WisBlock IO Pin 3) is connected to PB12 of the RAK3172 module. This pin is internally connected to a 10&nbsp;kΩ resistor as mentioned on the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/datasheet/#pin-definition" target="_blank">pin definition table of the RAK3172 datasheet</a>. Other WisBlock modules that use this pin will have possible conflict.
:::

To illustrate, RAK3372 can be connected to <a href="https://store.rakwireless.com/products/rak19007-wisblock-base-board-2nd-gen?utm_source=RAK19007&utm_medium=Document&utm_campaign=BuyFromStore" target="_blank">RAK19007 WisBlock Base</a>, as shown in **Figure 1**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/rak19007-connect.png"
  width="60%"
  caption="RAK3372 connection to WisBlock Base RAK19007"
/>

Some pins are exposed on <a href="https://docs.rakwireless.com/product-categories/wisblock/rak19007/datasheet/#interfaces" target="_blank">RAK19007</a>, and you can easily use them via header pins. The labels are at the back, as shown in **Figure 2**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/io-pins.png"
  width="35%"
  caption="WisBlock Base exposed pins"
/>

Each WisBlock Base board provides a unique set of header pins for use. However, these header pins may vary between different WisBlock Base boards. Commonly, you will find IO pins and communication protocol pins such as I2C and UART. For more details, refer to the <a href="https://docs.rakwireless.com/product-categories/wisblock#wisblock-base" target="_blank">official documentation for the specific WisBlock Base</a> used in your project.

You can access the AT commands via UART2 by default, and possibly via UART1. Firmware update is only possible via UART2. A built-in USB-Serial converter is on the board to easily connect the RAK3372 to the USB port of the PC.

There are useable LEDs as well in the WisBlock Base. You can control them in your code via the `GREEN_LED` and `BLUE_RED` macro.

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

**Figure 3** shows how to mount the RAK3372 module on top of a WisBlock Base board (RAK19007). Follow carefully the procedure defined in <a href="https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard" target="_blank">WisBlock module assembly/disassembly instructions</a> to secure the connection safely. Once attached, carefully fix the module with one or more pieces of M1.2 x 3&nbsp;mm screws depending on the module.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19007/quickstart/13.wisblock-core-silkscreen.png"
  width="50%"
  caption="RAK3372 mounting sketch"
/>

##### Disassembling

The procedure in disassembling any type of WisBlock modules is the same.

1. First, remove the screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak19007/quickstart/16.removing-screws.png"
  width="70%"
  caption="Remove the screws from the WisBlock module"
/>

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1910/quickstart/17.detaching-silkscreen.png"
  width="70%"
  caption="Detach the silkscreen on the WisBlock module"
/>

3. Apply force to the module at the position of the connector, as shown in **Figure 6**, to detach the module from the baseboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak1910/quickstart/18.detaching-module.png"
  width="70%"
  caption="Apply even forces on the proper location of a WisBlock module"
/>

#### LoRa Antenna

Another important component of RAK3372 is the antenna.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/wisblock_antenna.png"
  width="30%"
  caption="LoRa Antenna"
/>

You need to ensure that it is properly connected to have a good LoRa signal. Also, note that you can damage the RF section of the chip if you power the module without an antenna connected to the IPEX connector.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/rak3372-antenna-label.png"
  width="30%"
  caption="RAK3372 IPEX antenna connector"
/>

:::tip NOTE
Detailed information about the RAK3372 LoRa PCB antenna can be found on the <a href="https://downloads.rakwireless.com/#LoRa/WisBlock/Accessories/" target="_blank">antenna datasheet</a>. Keep in mind that the PCB antenna is intended ideally only for prototyping and device evaluation. For enterprise deployments, it is advisable to consider a better antenna for reliable performance.
:::

:::warning
- When using the LoRa transceiver, make sure that it is connected to an antenna. Using the transceiver chip without an antenna can damage the system.
- Make sure to fix the module with screws to ensure proper function.
:::

#### Battery and Solar Connection

RAK3372 can be powered via the USB cable or Li-Ion/LiPo battery via the dedicated connectors, as shown in **Figure 9**. The matching connector for the battery wires is a <a href="https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable" target="_blank">JST PHR-2 2&nbsp;mm pitch female</a>.

This illustration uses RAK19007 as WisBlock Base. There are other <a href="https://store.rakwireless.com/collections/wisblock-base" target="_blank">WisBlock Base</a> boards available, and you need to check the datasheet of the specific WisBlock Base board for the right polarity and other parameters.

:::warning

- Batteries can cause harm if not handled properly.
- Only 3.7-4.2&nbsp;V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5&nbsp;V solar panels are supported. Do not use 12&nbsp;V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires match the polarity on the WisBlock Base Board. Not all batteries have the same wiring.

:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/rak3372-battery.png"
  width="50%"
  caption="WisBlock Base Battery Connection"
/>

The battery can also be recharged via a small solar panel, as shown in **Figure 10**. The matching connector for the solar panel wires is a <a href="https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable" target="_blank">JST ZHR-2 1.5&nbsp;mm pitch female</a>.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/rak3372-solar.png"
  width="50%"
  caption="Solar panel connection"
/>

Specifications of the battery and solar panel can be found on the datasheet of the <a href="https://docs.rakwireless.com/product-categories/wisblock#wisblock-base" target="_blank">WisBlock Base</a>.

### Software Initial Guide

#### Software Setup

The default firmware of RAK3372 is based on RUI3, which allows you to develop your custom firmware to connect sensors and other peripherals to it. To develop your custom firmware using Arduino IDE, you need first to add **RAKwireless RUI STM32 Boards** in the Arduino board manager, which will be discussed in this guide. You can then use <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/arduino-api/" target="_blank">RUI3 APIs</a> for your intended application. 

You can upload the custom firmware via UART. The AT commands of RAK3372 is still available even if you compile custom firmware via RUI3. You can send AT commands via UART2 connection.

##### RAK3372 RUI3 Board Support Package in Arduino IDE

If you don't have an Arduino IDE yet, download it from the <a href="https://www.arduino.cc/en/Main/Software" target="_blank">Arduino official website</a> and follow the installation procedure depending on your machine.

:::tip NOTE
**For Windows 10 and up users**:
If you installed the Arduino IDE from the Microsoft App Store, uninstall it and download the version from the <a href="https://www.arduino.cc/en/Main/Software" target="_blank">Arduino official website</a>. The Microsoft App Store version has compatibility issues with third-party Board Support Packages.
:::

Once the Arduino IDE has been installed successfully, configure the IDE to add the RAK3372 to its board selection by following these steps.

1. Open Arduino IDE and go to **File** > **Preferences**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/preferences.png"
  width="100%"
  caption="Arduino preferences"
/>

2. To add the RAK3372 to your Arduino Boards list, edit the **Additional Board Manager URLs**. Click the icon, as shown in **Figure 12**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/additional-boards.png"
  width="80%"
  caption="Modify Additional Board Manager URLs"
/>

3. Copy the URL below and paste it on the field, as shown in **Figure 13**. If there are other URLs already listed, add them on the next line. Then, click **OK**.

```json
https://raw.githubusercontent.com/RAKWireless/RAKwireless-Arduino-BSP-Index/main/package_rakwireless_com_rui_index.json
```

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/preferences-url.png"
  width="100%"
  caption="Add additional board manager URLs"
/>

4. Restart the Arduino IDE.

5. Open the **Boards Manager** from Tools Menu.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/boards-manager.png"
  width="100%"
  caption="Open Arduino boards manager"
/>

6. Write **RAK** in the search bar, as shown in **Figure 15**. This will show the available RAKwireless module boards that you can add to your Arduino Board list.

7. Select **RAKwireless RUI STM32 Boards**, and click on **Install** to install the latest version of the **RAKwireless RUI STM32 Boards**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/rui3-stm32.png"
  width="80%"
  caption="Install RAKwireless RUI STM32 Boards"
/>

##### Configure RAK3372 on Boards Manager

8. Once the BSP is installed, select  **Tools** > **Boards Manager** > **RAKWireless RUI STM32 Modules** > **WisDuo RAK3172 Evaluation Board**. The RAK3372 WisBlock Core uses the RAK3172 WisDuo module, so you must select that board, as shown in **Figure 16**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/rui-stm32.png"
  width="100%"
  caption="Select RAK3172 Module"
/>

##### RAK3372 COM Port on Device Manager

Connect the RAK3372 via UART and check RAK3372 COM Port using Windows **Device Manager**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/rui-port.png"
  width="70%"
  caption="Device manager ports (COM & LPT)"
/>

##### Compile an Example with Arduino LED Breathing

1. Once your RAK3372 WisBlock Core is added to the Arduino IDE, try to run a simple program to test your setup. There is a built-in LED in the WisBlock Base board that you can control via RUI3 custom firmware.

2. Launch Arduino IDE and configure WisDuo RAK3172 Evaluation Board on board selection. See [**Figure 16**](#configure-rak3372-on-boards-manager).

3. Connect the RAK3372 via UART and check RAK3372 COM Port. See [**Figure 17**](#rak3372-com-port-on-device-manager).

4. Open the **Tools** Menu and select a COM port. **COM28** is currently used. COM port number varies depending on the PC.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/select-port.png"
  width="100%"
  caption="Select COM port"
/>

5. You can now see the serial monitor icon and click it to connect the COM port.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/serial-mon.png"
  width="100%"
  caption="Open Arduino serial monitor"
/>

6. If the connection is successful, you can send AT Commands to RAK3372. For example, to check the RUI version, type `AT+VER=?` on the text area and click on the **Send** button, as shown in **Figure 20**.

:::tip NOTE
If there is no reply, make sure you have selected the right COM port or double-check the USB connection.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/arduino-console.png"
  width="100%"
  caption="Send AT commands and Arduino serial monitor COM28"
/>

7. Open **Arduino_Led_Breathing** example code.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/led-example.png"
  width="100%"
  caption="Arduino Led Breathing example"
/>

8. Click on the **Verify** icon to check if you have successfully compiled the example code.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/verify-code.png"
  width="100%"
  caption="Verify the example code"
/>

9. Click the **Upload** icon to send the compiled firmware to your RAK3372 WisBlock Core module.

:::tip NOTE
RAK3172 module in the WisBlock Core should automatically go to BOOT mode when the firmware is uploaded via Arduino IDE.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/upload-code.png"
  width="100%"
  caption="Upload the example code"
/>

10. If the upload is successful, you will see an **Upgrade Complete** message.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/dev-prog.png"
  width="100%"
  caption="Device programmed successfully"
/>

11. After the Device Programmed is completed, you will see that LEDs are blinking.

##### LoRaWAN Example

This example illustrates how to program RAK3372 WisBlock Core as a stand-alone LoRaWAN end-device via <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/arduino-api/" target="_blank">RUI3 Arduino APIs</a>. To use the RAK3372 WisBlock Core module as a LoRaWAN end-device, it must be within range of a functioning **LoRaWAN gateway** that is registered to a **LoRaWAN network server (LNS)** or has a built-in network server.

:::tip NOTE
If you are new to LoRaWAN, here are a few good references about LoRaWAN and gateways:

- <a href="https://news.rakwireless.com/lorawan-r-101-all-you-need-to-know/" target="_blank">LoRaWAN 101</a>
- <a href="https://news.rakwireless.com/what-is-a-lorawan-gateway/" target="_blank">What is a LoRaWAN Gateway</a>
- <a href="https://news.rakwireless.com/how-do-lorawan-gateways-work/" target="_blank">How do LoRaWAN Gateways work?</a>
- <a href="https://news.rakwireless.com/things-to-consider-when-picking-a-lorawan-gateway/" target="_blank">Things to Consider When Picking A LoRaWAN Gateway</a>

RAKwireless LoRaWAN gateway models like <a href="https://store.rakwireless.com/collections/wisgate-edge" target="_blank">WisGate Edge</a> have built-in network servers. It is also common that the LoRaWAN network server is external or in the cloud. The popular LoRaWAN network server in the cloud that you can use for free (but offers enterprise service, too) is <a href="https://www.thethingsnetwork.org/" target="_blank">TTN</a>.

To correctly run this example, it is necessary to configure the LoRaWAN parameters and create an OTAA application on your LoRaWAN gateway.

:::

###### Register the LoRaWAN Gateway on TTNv3 Community Edition

After configuring your gateway, you need to register it in TTNv3:

1. Log in to the TTNv3 Network Server with a web browser.

- <a href="https://eu1.cloud.thethings.network/" target="_blank">Europe</a>
- <a href="https://nam1.cloud.thethings.network/" target="_blank">North America</a>
- <a href="https://au1.cloud.thethings.network/" target="_blank">Australia</a>

2. Navigate to the **Console** page and click on **gateway** icon, as shown in **Figure 25**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/ttnv3-initial-a.png"
  width="100%"
  caption="TTNv3 gateway registration and configuration"
/>

3. On **General Settings**, enter the **Gateway ID**, **Gateway EUI**, and **Gateway Name**. This information is available in your LoRaWAN gateway configuration. Select the **Gateway Server address** according to the region where the LoRaWAN gateway will be installed.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/ttnv3-gwconfig-a.png"
  width="100%"
  caption="TTNv3 gateway registration and configuration"
/>

4. Select the **Frequency plan** for your region (used by TTN), then click on the **Create gateway** button. This will add a new gateway to TTNv3.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/ttnv3-add-a.png"
  width="100%"
  caption="TTNv3 add new Gateway"
/>

###### Create a LoRaWAN Applications in TTN

1. Go to <a href="https://console.cloud.thethings.network/" target="_blank">The Things Network platform</a> and select a cluster, as shown in **Figure 28**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/image_1-a.png"
  width="100%"
  caption="Select a Cluster in TTN V3"
/>

You can use the same login credentials on the TTN V2 if you have one. If you have no account yet, create one.

2. To register as a new user to TTN, click on **Login with The Things ID** then select **register** on the next page, as shown in **Figure 29** and **Figure 30**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/image_2.png"
  width="100%"
  caption="Login using TTN account"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/image_3.png"
  width="100%"
  caption="Registration of new account"
/>

3. You should now be on the step of creating your TTN account. Fill in all the necessary details and activate your account.

4. Log in on the platform using your username/email and password then click **Submit**, as shown in **Figure 31**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/image_4.png"
  width="100%"
  caption="Log in to TTN platform"
/>

5. Click **Authorize** to proceed.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/image_5.png"
  width="100%"
  caption="Authorization to TTN"
/>

6. Now that you are logged in to the platform, the next step is to create an application. Click **Create an application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/image_6.png"
  width="100%"
  caption="Create TTN application for your LoRaWAN devices"
/>

7. To have an application registered, input first the specific details and necessary information about your application then click **Create application**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/image_7.png"
  width="100%"
  caption="Details of the TTN application"
/>

If you had no error during the previous step, you should now be on the application console page. The next step is to add end-devices to your TTN application. LoRaWAN specification enforces that each end-device has to be personalized and activated. There are two options for registering devices depending on the activation mode you select. Activation can be done either via Over-The-Air-Activation (OTAA) or Activation-By-Personalization (ABP). This guide will show OTAA.

###### TTN OTAA Device Registration

1. Go to your application console to be able to register a device. To start adding an OTAA end-device, click **+ Add end device**, as shown in **Figure 35**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/image_8.png"
  width="100%"
  caption="Add end device"
/>

2. To register the module, first click **Manually**, then configure the activation method by selecting **Over the air activation (OTAA)** and a compatible **LoRaWAN version**, and finally click the **Start** button, as shown in **Figure 36** and **Figure 37**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/image_9.png"
  width="100%"
  caption="Manually register the device to TTN"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/image_10.png"
  width="100%"
  caption="Device activation configuration"
/>

3. Put a unique **End device ID** and EUIs (**DevEUI** and **AppEUI**), as shown in **Figure 38**. Check if your module has a DevEUI on the sticker or QR that you can scan then use this as the device unique DevEUI.

Optionally, you can add a more descriptive **End device name** and **End device description** about your device.

4. After filling in all the details, click **Network layer settings** to proceed to the next step.

:::tip NOTE
It is advisable to use a meaningful end-device ID, end-device name, and end-device description that will match your device's purpose. The end-device ID `rak-device` is for illustration purposes only.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/image_11.png"
  width="100%"
  caption="OTAA Device Information"
/>

5. The next step is to set up the **Frequency plan**, a compatible **Regional Parameter version**, and the **LoRaWAN class** supported. Then, click **Join settings**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/image_12.png"
  width="100%"
  caption="OTAA Configuration"
/>

6. The last step in the registration of a new OTAA end-device is the configuration of the **AppKey**. To get the AppKey, click the **generate button**. Then, click **Add end device** to finish your new device registration.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/image_13.png"
  width="100%"
  caption="OTAA AppKey generation and device registration"
/>

You should now be able to see the device on the TTN console after you fully register your device, as shown in **Figure 41**.

:::tip NOTE

- The **AppEUI**, **DevEUI**, and **AppKey** are essential parameters for activating your LoRaWAN end-device using OTAA. For security purposes, the **AppKey** is hidden by default but can be revealed by clicking the "Show" button. You can also use the "Copy" button to quickly copy these parameters.
- The three OTAA parameters on the TTN device console are MSB by default.
- These parameters are always accessible on the device console page, as shown in [**Figure 50**](#firmware-upgrade-procedure).
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/image_14.png"
  width="100%"
  caption="OTAA device successfully registered to TTN"
/>


###### Upload LoRaWAN Example to RAK3372

After a successful registration of the RAK3372 device on the LNS, you can now proceed with running the LoRaWAN OTAA demo application example.

1. Launch the Arduino IDE and configure WisDuo RAK3172 Evaluation Board on board selection. See [**Figure 16**](#configure-rak3372-on-boards-manager).
2. Connect the RAK3372 via UART and check RAK3372 COM Port. See [**Figure 17**](#rak3372-com-port-on-device-manager).
3. Open the example code under **RAK WisBlock RUI examples**: **File** > **Examples** > **RAK WisBlock RUI examples** > **Example** > **LoRaWan_OTAA**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/otaa-rak3172.png"
  width="100%"
  caption="OTAA LoRaWAN application example"
/>

4. In the example code, modify the device EUI **OTAA_DEVEUI**, the application EUI **OTAA_APPEUI**, and the application key **OTAA_APPKEY**.

- The **OTAA_DEVEUI** parameter should match the device EUI registered in your network server. Note that your RAK3372 module has a sticker with a QR code printed on it. You can use the QR code information to configure the **OTAA_DEVEUI** parameter. The **OTAA_DEVEUI** format is MSB first.

```c
  // OTAA Device EUI MSB
#define OTAA_DEVEUI   {0x11, 0x33, 0x55, 0x77, 0x99, 0x22, 0x44, 0x66}
```
- The **OTAA_APPEUI** parameter. This parameter should also be the same as the **APPEUI** in the network server you configured.

```c
  // OTAA Application EUI MSB
#define OTAA_APPEUI   {0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x09}
```

- Another important parameter to change is the application key **OTAA_APPKEY**. This parameter should also be the same as the **APPKEY** in the network server you configured. The **OTAA_APPKEY** format is MSB first.

```c
// OTAA Application Key MSB
#define OTAA_APPKEY   {0x04, 0xFA, 0x4E, 0x62, 0x6E, 0xF5, 0xCF, 0x22, 0x7C, 0x96, 0x96, 0x01, 0x17, 0x62, 0x75, 0xC2}
```

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/lorawan_otaa_parameter.png"
  width="190%"
  caption="Configure DEVEUI, APPEUI and APPKEY"
/>

3. Depending on the Regional Band you selected, you might need to configure the sub-band of your RAK module to match the gateway and LoRaWAN network server. This is especially important for Regional Bands like US915, AU915, and CN470.

This guide uses EU868. However, if you are using other regional bands, update it and possibly the channels. For example, if you are using US915 and AU915, set up the channel mask using the `mask.set` API. Channels 8 to 15 are the most commonly used channels in the US915 and AU915 bands, corresponding to a mask value of two.

*Here's example on using US915 with OTAA_BAND equal to 5:*

```c
  if (!api.lorawan.band.set(OTAA_BAND)) {
    Serial.printf("LoRaWan OTAA - set band is incorrect! \r\n");
    return;
  }
  uint16_t maskBuff = 0x0002;
  if (!api.lorawan.mask.set(&maskBuff)) {
    Serial.printf("LoRaWan OTAA - set mask is incorrect! \r\n");
    return;
  }

```

:::tip NOTE
RAK3372 supports the following regions:

* RAK_REGION_EU433 = 0
* RAK_REGION_CN470 = 1
* RAK_REGION_RU864 = 2
* RAK_REGION_IN865 = 3
* RAK_REGION_EU868 = 4
* RAK_REGION_US915 = 5
* RAK_REGION_AU915 = 6
* RAK_REGION_KR920 = 7
* RAK_REGION_AS923 = 8
* RAK_REGION_AS923-2 = 9
* RAK_REGION_AS923-3 = 10
* RAK_REGION_AS923-4 = 11
:::

:::tip NOTE
- Make sure you have configured the correct RAK board before uploading the code. See <a href="#configure-rak3372-on-boards-manager" target="_blank">Configure RAK3372 on Boards Manager</a> section.
- Also, check <a href="#rak3372-com-port-on-device-manager" target="_blank">RAK3372 COM Port on Device Manager</a> section.
:::

4. Open the **Tools** Menu and select a COM port. **COM28** is currently used.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/select-port.png"
  width="100%"
  caption="Select COM port"
/>

5. The last step is to upload the code by clicking the **Upload** icon on Arduino IDE. Take note that you should select the right board and COM port.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/otaa-upload.png"
  width="100%"
  caption="Upload the code"
/>

6. You should now be able to view the console logs through the serial monitor in the Arduino IDE. If the COM port disconnects, the terminal output may not appear immediately. To resolve this, reconnect the module or press the reset button to restore the terminal output.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/serial-console.png"
  width="90%"
  caption="Arduino serial monitor logs"
/>

7. Check on the LoRaWAN network TTN console logs if your device has been successfully joined with the `join-request` and `join-accept` messages.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/ttn-log.png"
  width="90%"
  caption="TTN console log"
/>

## Miscellaneous

### Upgrading the Firmware

If you want to upgrade to the latest version of the firmware of the module, follow this section. The latest firmware can be found in the software section of <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/datasheet/#firmware" target="_blank">RAK3172 Datasheet</a>.

:::tip NOTE

**What if the RAK3372 WisBlock Core module stops responding to AT commands and/or firmware updates?**

You can recover your device by using the `.hex` file in the datasheet and uploading it using STM32CubeProgrammer. The guide on updating STM32 firmware using STM32CubeProgrammer can be found in the <a href="https://learn.rakwireless.com/hc/en-us/articles/26687606549911-How-To-Guide-STM32CubeProgrammer-for-RAK-modules" target="_blank">Learn section</a>.

:::

:::warning

Uploading the `.hex` file via STM32CubeProgrammer will erase all configured data on the device.

:::

#### Firmware Upgrade Through UART2

##### Minimum Hardware and Software Requirements

Refer to the table for the minimum hardware and software requirements to perform the firmware upgrade via UART2:

| Hardware/Software | Requirement                                   |
| ----------------- | --------------------------------------------- |
| Computer          | A Windows/Ubuntu/Mac computer                 |
| Firmware File     | Bin firmware file downloaded from the website |
| Others            | A USB to TTL module                           |

##### Firmware Upgrade Procedure

Execute the following procedure to upgrade the firmware in the **Device Firmware Upgrade** (DFU) mode through the UART2 interface.

:::tip NOTE
RAK3172 should automatically go to BOOT mode when the firmware is uploaded via RAK DFU Tool or WisToolBox.
:::

1. Download the latest <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/datasheet/#firmware" target="_blank">RAK3172 Firmware</a>.

2. Download the <a href="https://downloads.rakwireless.com/#LoRa/Tools/RAK_Device_Firmware_Upgrade_tool/)" target="_blank">RAK Device Firmware Upgrade (DFU) Tool</a>.

3. Connect the RAK3372 module to the computer using a USB-to-TTL cable.

4. Open the Device Firmware Upgrade tool. Select the serial port and baud rate (115200) of the module and click the **Select Port** button.

:::tip NOTE

If your firmware upload always fails, check your current baud rate setting using the `AT+BAUD=?` command and use that baud rate value in the RAK DFU Tool. Check if you selected the right COM port.

:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/1.png"
  width="80%"
  caption="Device Firmware Upgrade Tool"
/>

5. Select the application firmware file of the module with the suffix `.bin`.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/2.png"
  width="80%"
  caption="Select firmware"
/>

6. Click the **Upgrade** button to upgrade the device. After the upgrade is complete, the RAK3372 will be ready to work with the new firmware.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/3.png"
  width="80%"
  caption="Firmware upgrading"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak3372/quickstart/4.png"
  width="80%"
  caption="Upgrade successful"
/>


<RkBottomNav/>