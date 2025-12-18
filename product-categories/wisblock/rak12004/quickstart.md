---
slug: /product-categories/wisblock/rak12004/quickstart/
title: RAK12004 WisBlock MQ2 Gas Sensor Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK12004. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak12004/rak12004.png"
keywords:
  - quickstart
  - RAK12004
  - wisblock
sidebar_label: Quick Start Guide
---

# RAK12004 WisBlock MQ2 Gas Sensor Module Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step on using RAK12004 WisBlock MQ2 module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK12004 WisBlock MQ2 Gas Sensor Module](https://store.rakwireless.com/products/mq2-gas-sensor-module-rak12004?utm_source=RAK12004&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base) with IO slot
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

- Download and install [Arduino IDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino project, install the RAKwireless Arduino BSP. Follow the steps in the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

RAK12004 module is part of the WisBlock Sensor category and extends the WisBlock system with a gas sensor alert system. The RAK12004 connects to the WisBlock Base Board through the IO slot. The **Figure 1** shows the assembly of a [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core) highlighted in green and the module RAK12004 highlighted in red. Also, always secure the connection of the WisBlock module by using the compatible screws. For more information about RAK12004, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak12004/datasheet/).

> **Image:** RAK12004 connection to WisBlock Base Board

#### Assembling and Disassembling of WisBlock Modules

##### Assembling

As shown in **Figure 2**, the location for the IO slot is properly marked by silkscreen. Follow carefully the procedure defined in [WisBlock Base board assembly/disassembly instructions](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard) to attach a WisBlock module. Once attached, carefully fix the module with one or more pieces of M1.2 x 3 mm screws depending on the module.

> **Image:** RAK12004 connection to WisBlock Base Board

##### Disassembling

The procedure in disassembling any type of WisBlock modules is the same.

1. First, remove the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

> **Image:** Detaching silkscreen on the WisBlock module

3. Apply force to the module at the position of the connector, as shown in **Figure 5**, to detach the module from the baseboard.

> **Image:** Applying even forces on the proper location of a WisBlock module

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts. RAK12004 uses I2C and IO pins it can cause possible conflict especially on some IO modules.
:::

After all this setup, you can now connect the battery and USB cable to start programming your WisBlock Core.

:::warning
- Batteries can cause harm if not handled properly.
- Only 3.7-4.2 V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause a fire.
- Only 5 V solar panels are supported. Do not use 12 V solar panels. It will destroy the charging unit and eventually other electronic parts.
- Make sure the battery wires match the polarity on the WisBlock Base board. Not all batteries have the same wiring.
:::

### Software Configuration and Example

The RAK12004 has an electronic sensor used for sensing the concentration of gases in the air. It contains a sensing material whose resistance changes when it comes in contact with the gas. Concentrations of gas is measured using a voltage divider network present in the sensor. The output of the sensing element is connected to a 12-bit ADC (ADC121C021) which communicates through I2C to the application.

#### Initial Test of the RAK12004 WisBlock Module

1. Install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index) for WisBlock by using the `package_rakwireless_index.json` board installation package. The WisBlock Core should now be available on the Arduino IDE.

2. You need to select first the WisBlock Core you have.

**RAK4631 Board**

> **Image:** Selecting RAK4631 as WisBlock Core

**RAK11200 Board**

> **Image:** Selecting RAK11200 as WisBlock Core

**RAK11310 Board**

> **Image:** Selecting RAK11310 as WisBlock Core

3. Install the [RAKwireless MQx Library](https://github.com/RAKWireless/RAK-MQx-Library) using Arduino Library Manager.

4. On the Arduino IDE, select **Sketch** -> **Include Library** -> **Manage Libraries**, as shown in **Figure 9**.

5. On the **Library Manager** text area, type **RAKwireless MQx**.

> **Image:** Arduino Library Manager

6. To finish the installation, click on the **Install** button, as shown in **Figure 10**.

> **Image:** Finish RAK-MQx library Installation

7. Once the library is installed, open the **RAK12004_MQ2_Sampling** example.

8. On the Arduino IDE, select **File** -> **Examples** -> **RAKWireless MQx Libraries** -> **RAK12004_MQ2_Sampling**, as shown in **Figure 11**.

> **Image:** Open RAK12004 MQ2 Sampling Sketch

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated code for the RAK12004 WisBlock MQ2 Gas Sensor Module that can be found on the [RAK12004 WisBlock Example Code Repository](https://github.com/RAKWireless/RAK-MQx-Library/tree/main/examples).
:::

9. You can now select the right serial port and upload the code, as shown in **Figure 12** and  **Figure 13**.

> **Image:** Selecting the correct Serial Port

> **Image:** Uploading the RAK12004 example code on RAK4631

To extend the use of the RAK-MQx library, check the link [RAK-MQx Library methods](https://github.com/RAKWireless/RAK-MQx-Library#usage)

#### Build RAK12004 Example on PlatformIO IDE (optional)

:::tip NOTE
This procedure was tested only on Windows 10 and Ubuntu.
:::

1. Install the original PlatformIO platform, as shown in [PlatformIO First Install](https://github.com/RAKWireless/WisBlock/blob/master/PlatformIO/README.md#first-install) section.

- For WisBlock Core RAK4631, install **Nordic nRF52** platform.
- For WisBlock Core RAK11200, install **Espressif 32** platform.
- For WisBlock Core RAK11310, install **Raspberry Pi RP2040** platform.

2. Open a project example that uses the new installed platform.

3. Launch **Visual Studio Code** and select **PlatformIO PIO Home**.

4. On **PIO Home**, click on **Project Examples**.

5. Choose **arduino-blink** project, then click on **Import** button.

> **Image:** Import arduino-blink project

6. Click the **Yes** button on the trust window.

> **Image:** PlatformIO trust authors

7. Build the project and ignore warnings and errors.

8. Download and install the [RAK Patch script](https://raw.githubusercontent.com/RAKWireless/WisBlock/master/PlatformIO/RAK_PATCH.zip).

9. Unzip the contents of RAK_PATCH.zip into the folder RAK_PATCH in your PlatformIO installation folder.

The table below shows the PlatformIO installation directory for each operating system:

| PlatformIO path on different OS |                                      |
| :------------------------------ | :----------------------------------- |
| Windows 10                      | `%UserProfile%\.platformio\`         |
| Linux                           | `~/.platformio/`                     |
| MacOS                           | `/Users/{Your_User_id}/.platformio/` |

**Figure 16** shows the PlatformIO installation directory on Windows 10.

> **Image:** RAK patch folder on Windows

10.  Open a command prompt in **`%UserProfile%.platformio\RAK_PATCH`** folder and execute python **`./rak_patch.py`**.

> **Image:** RAK patch installed on Windows

:::warning
In case of any platform update on PlatformIO, the **RAK_PATH** script must be executed again after the platform update.
:::

11. Import the RAK12004 Arduino Project to PlatformIO.

12. Open **PlatformIO PIO Home** and select **Import Arduino Project**, as shown in **Figure 18**.

> **Image:** Import RAK12004 Arduino Project

13. Select your preferred **WisBlock Core** and check "**Use Libraries installed by the Arduino IDE**" option, as shown in **Figure 19**.

14. Then choose the directory of the original RAK12004 Arduino Project.

> **Image:** Select Board and check Import Libraries

15. To finish the import, click on the **Import** button, as shown in **Figure 20**.

> **Image:** Select Board and check Import libraries

16. Build the imported project on the PlatformIO.

Now, you can build the project by clicking on the highlighted icon, as shown in **Figure 21**.

> **Image:** Build Arduino imported project

17. Upload the imported project on the PlatformIO.

18. To upload the project on the target board, click on the highlighted icon, as shown in **Figure 22**.

> **Image:** Upload Arduino imported project

