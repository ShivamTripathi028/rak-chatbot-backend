---
title: RAK3172 Low-Level Development | STM32WL LoRaWAN SoC Firmware Guide
description: Create custom firmware for the RAK3172 LoRaWAN Module using STM32WL SDK. Learn STM32CubeIDE setup, LoRaWAN development, and RF SOC integration.
image: https://images.docs.rakwireless.com/wisduo/rak3172-module/rak3172-module.png
keywords:
  - stm32wl based module
  - system on chip in iot
  - custom firmware for lorawan soc
  - stm32wle5ccu6 lora
  - rak3172 custom firmware
  - stm32cubeide tutorial
  - stm32wl sdk firmware development
  - lorawan firmware development guide
  - stm32wl cubeide integration
  - rf system on chip
date: 2021-04-12
sidebar_label: Low Level Development
slug: /product-categories/wisduo/rak3172-module/low-level-development/
download: true
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK3172 WisDuo LoRaWAN Module Low Level Development Reference

## Overview

The RAK3172 module utilizes an RF System-on-Chip IC from STMicroelectronics, specifically the STM32WL series, which finds application in various LPWAN IoT devices.

STM32WL microcontrollers incorporate a sub-GHz radio based on Semtech SX126x, catering to the demands of a diverse range of Low-Power Wide Area Network (LPWAN) wireless applications in industrial and consumer Internet-of-Things (IoT) domains. The specific STM32WL microcontroller employed in the RAK3172 is the STM32WLE5CCU6.

While the RAK3172 has a built-in default firmware with a set of AT commands that can be interfaced with an external host like other microcontrollers, it can also be used by developing custom firmware directly on its chip using the STM32WL SDK from STMicroelectronics. Taking this approach will reduce the overall cost of the device because there will be no need for an external microcontroller, but it will require extra software development effort.

This guide will illustrate how to generate custom firmware for the STM32WLE5CCU6, which is inside the RAK3172 module. It supports three STM32WL SDK versions: v1.0.0, v1.2.0, and v1.3.0.

- [STM32CubeIDE guide with STM32WL SDK v1.0.0](#rak3172-on-stm32cubeide-with-stm32wl-sdk-v100)
- [STM32CubeIDE guide with STM32WL SDK v1.2.0](#rak3172-on-stm32cubeide-with-stm32wl-sdk-v120)
- [STM32CubeIDE guide with STM32WL SDK v1.3.0](#rak3172-on-stm32cubeide-with-stm32wl-sdk-v130)


:::tip NOTE
- **STM32WL SDK v1.0.0** was tested on **STM32CubeIDE v1.7.0**.
- **STM32WL SDK v1.2.0** was tested on **STM32CubeIDE v1.10.0**.
- **STM32WL SDK v1.3.0** was tested on **STM32CubeIDE v1.10.0 and v1.14.0**.
:::


## Guide on Using STM32WL SDK Using STM32CubeIDE

### Installation of STM32Cube IDE

1. Download the <a href="https://www.st.com/en/development-tools/stm32cubeide.html#overview&secondary=st-get-software" target="_blank">STM32Cube IDE</a> from the STMicroelectronics website. Then select the latest version compatible with your computer.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-getsw.png"
  width="80%"
  caption="STM32CubeIDE Software Download"
  zoomMode={true}
/>

2. A license agreement from STMicroelectronics will be displayed, and you must agree to log in using your STMicroelectronics account. Create an account if you do not already have one.

3. After downloading, unzip the installer file and begin the installation process. Simply click **Next** on the initial installation window and accept the license agreement.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-install.png"
  width="50%"
  caption="STM32CubeIDE Installation"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-license-agreement.png"
  width="50%"
  caption="STM32CubeIDE License Agreement"
  zoomMode={true}
/>

3. The next step is to determine the directory where you want the STM32CubeIDE software to be installed. Simply click **Next** to use the default folder, or you can select a different location.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-directory.png"
  width="50%"
  caption="STM32CubeIDE Directory Location"
  zoomMode={true}
/>

4. Select optional components for installation, such as J-Link and ST-Link drivers. It is highly recommended to include these drivers, as they will be useful for debugging and uploading binary firmware files to the STM32WL chip.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-drivers.png"
  width="50%"
  caption="STM32CubeIDE Drivers"
  zoomMode={true}
/>

5. The progress bar will be displayed as the installation begins.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-install-going.png"
  width="50%"
  caption="STM32CubeIDE On-going Installation"
  zoomMode={true}
/>

6. During installation, STMicroelectronics device drivers may appear. These are not required for STM32WL, so you can leave them uninstalled.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-device-driver.png"
  width="50%"
  caption="STM32CubeIDE Optional Device Drivers"
  zoomMode={true}
/>

7. If there are no issues during the installation process, you should be finished and can now create a desktop shortcut for the STM32CubeIDE application.


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-complete.png"
  width="50%"
  caption="STM32CubeIDE Installation Successful"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-shortcut.png"
  width="50%"
  caption="STM32CubeIDE Installation Finished"
  zoomMode={true}
/>

8. Check if the installation of STM32CubeIDE was successful by trying to run the application. It should be free of errors. The application will prompt you for the workspace, and you can accept the default location if you do not want to specify a different one. You also have the option to create multiple workspaces, but only one can be active at a time.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-workspace.png"
  width="50%"
  caption="STM32CubeIDE Workspace Selection"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-running-app.png"
  width="90%"
  caption="STM32CubeIDE Application Running"
  zoomMode={true}
/>

### RAK3172 on STM32CubeIDE with STM32WL SDK v1.0.0

STMicroelectronics provides a free IDE called STM32CubeIDE, which you can use to develop firmware for various STM32 microcontrollers, including the STM32WL series. Based on Eclipse, it is a complete software IDE where you can easily debug your code with built-in integration to tools like ST-Link and other features like STM32CubeMX. It is multiplatform software that can run on Windows, Linux, and macOS.

You cannot directly select RAK3172 on the STM32CubeIDE, but you can use the STM32WLE5CCU6 inside it with the STM32WL SDK from STMicroelectronics to start your own custom firmware. This guide is only applicable to STM32WL SDK v1.0.0.

#### Getting STM32WL SDK v1.0.0

This guide only works on v1.0.0 of the SDK.

1. If you already have the STM32CubeIDE running on your machine, the next step is to download the <a href="https://www.st.com/en/embedded-software/stm32cubewl.html#get-software" target="_blank">STM32WL SDK v1.0.0</a> from the STMicroelectronics website.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32wl-sdk-download-page.png"
  width="70%"
  caption="STM32WL SDK Download Page"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32wl-v1-0-0-download.png"
  width="85%"
  caption="STM32WL V1.0.0 Download"
  zoomMode={true}
/>

2. The downloaded files usually go to the downloads folder. You need to extract it, and then you will see the STM32WL SDK firmware folder.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32wl-v1-0-0.png"
  width="60%"
  caption="STM32WL V1.0.0"
  zoomMode={true}
/>

3. The structure of the extracted files should be the same as shown in **Figure 15**. Do not change this folder structure. It contains many examples related to the STM32WL chip.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32wl-v1-0-0-folder-structure.png"
  width="70%"
  caption="STM32WL V1.0.0 Folder Structure"
  zoomMode={true}
/>


#### Modifications for the RAK3172

##### Files Modification Needed to Run STM32WL SDK LoRaWAN Examples to RAK3172

If you already have the STM32WL V1.0.0 SDK folder, there are only a few files that you need to update to be able to create firmware that will run on the RAK3172.

:::tip NOTE

STM32 microcontroller firmware created using STM32CubeIDE (with the help of STM32CubeMX) has a **.ioc** file. This is a configuration file created by the STM32CubeMX tool. This is a useful tool in setting up peripherals and drivers quickly in the STM32 development ecosystem. However, once you make the file modifications mentioned in this guide, you cannot create a new **.ioc** file or modify it via STM32CubeMX. Otherwise, the modified files needed by the RAK3172 will be overwritten and will revert to their original state in the **.ioc** file.

In cases where you need to use STM32CubeMX to set up peripherals or drivers, you just need to repeat the same modifications mentioned in this section.
:::

1. Download the <a href="https://downloads.rakwireless.com/LoRa/RAK3172/Firmware/RAK3172_Low_Level_Development.zip" target="_blank">Low Level Development zip file</a> from the RAK downloads site. Extract the zip file and inside the folder are four files that need to be copy-pasted on specific locations of the STM32WL V1.0.0 folder to make it compatible with RAK3172.

The majority of these files are for setting up the RF channel front end of the radio section on the STM32WL chip. Also, the startup file must be changed because the default startup on STM32WL SDK V1.0.0 is for the STM32WL55 series and not for STM32WLE5. The RAK3172 is based on STM32WLE5CCU6.

:::tip NOTE
This guide will demonstrate how to run the **LoRaWAN_End_Node** example of the STM32WL SDK to RAK3172. If you need to run other LoRaWAN-related examples like **LoRaWAN_AT_Slave**, you need to update the files on that folder.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/rak3172-low-level-development-files.png"
  width="60%"
  caption="RAK3172 Low Level Development Files"
  zoomMode={true}
/>

2. The radio related files `radio_board_if.c`, `radio_board_if.h`, and `radio_conf` must be placed in this location of the STM32WL SDK folder `\STM32Cube_FW_WL_V1.0.0\Projects\NUCLEO-WL55JC\Applications\LoRaWAN\LoRaWAN_End_Node\LoRaWAN\Target`. You have to overwrite or replace the old files.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/rak3172-radio-files.png"
  width="60%"
  caption="RAK3172 Radio Related Files for Modification"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/rak3172-radio-replace.png"
  width="40%"
  caption="RAK3172 Radio Related Files Replaced"
  zoomMode={true}
/>

3. You also need to update the startup file. Place the `startup_stm32wle5ccux.s` file in this location: `\STM32Cube_FW_WL_V1.0.0\Projects\NUCLEO-WL55JC\Applications\LoRaWAN\LoRaWAN_End_Node\STM32CubeIDE\Application\Startup`. There is a default startup file in that directory named `startup_stm32wl55jcix.s`. Delete that file.

The updated startup folder should be the same, as shown in **Figure 19**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/rak3172-radio-related-files-replaced.png"
  width="60%"
  caption="RAK3172 Radio Related Files Replaced"
  zoomMode={true}
/>

##### Initial Build Test for the RAK3172 Custom Firmware

1. After making the file modifications, the next step is to test if the **LoRaWAN_End_Node** example can be built without errors.

:::tip NOTE
If this is your first time using STM32CubeIDE, it shows the **Information Center** by default. Just close it and access the project in the left panel.
:::

2. Open the STM32CubeIDE and click on `File` then `Open Projects from File System`.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-openproject.png"
  width="90%"
  caption="Open the Project in STM32CubeIDE"
  zoomMode={true}
/>

3. You then need to browse to the project folder location by clicking the **Directory** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide_open_dir.png"
  width="90%"
  caption="Locate the Project Directory in STM32CubeIDE"
  zoomMode={true}
/>

4. You should locate this directory `\STM32Cube_FW_WL_V1.0.0\Projects\NUCLEO-WL55JC\Applications\LoRaWAN\LoRaWAN_End_Node`. Click on **STM32CubeIDE** folder once, then click the **Select Folder**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-project-stm32cube.png"
  width="70%"
  caption="Select the STM32CubeIDE Project Folder"
  zoomMode={true}
/>

5. You should now see **STM32CubeIDE** checked and ready to be imported as an **Eclipse project**. If not checked, click the checkbox and then the **Finish** button. It will take some time to fully import the entire project.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-finalopen-project.png"
  width="70%"
  caption="Open the LoRaWAN_End_Node Project"
  zoomMode={true}
/>

6. After the successful import, you should now see the **LoRaWAN_End_Node** project structure on the left side of the STM32CubeIDE.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-rak3172-initproject.png"
  width="90%"
  caption="Open the STM32CubeIDE Project"
  zoomMode={true}
/>

7. With the modified files already implemented, you can check if the files are updated by checking the startup file `startup_stm32wle5ccux.s` and the `radio_board_if.c`. The startup file must be updated to show `startup_stm32wle5ccux.s`. You should see `#if defined(RAK3172_RF_CHANNEL_SWITCH)` on line 72 of the `radio_board_if.c` file, as shown in **Figure 25**. If not, then you were not successful in changing these files with the [Low Level Development required modification](#files-modification-needed-to-run-stm32wl-sdk-lorawan-examples-to-rak3172).

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-rak3172-modfile.png"
  width="90%"
  caption="Open the STM32CubeIDE Project"
  zoomMode={true}
/>

8. You can now attempt to build the project by setting the build configuration to release, which will generate a `.bin` file.

:::tip NOTE
If you have an ST-LINK debugging tool, you can also choose **Debug** instead of **Release**.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-buildconfig.png"
  width="90%"
  caption="Configure Build to Release"
  zoomMode={true}
/>

9. After setting the build configuration, you are now ready to build the project. You should see a successful compilation and generation of a `.bin` file.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-rak3172-build.png"
  width="90%"
  caption="Build the Project"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/successful-project-build.png"
  width="90%"
  caption="Successful Project Build"
  zoomMode={true}
/>


### RAK3172 on STM32CubeIDE with STM32WL SDK v1.2.0

The previous guide is for STM32WL SDK version 1.0.0. This guide is compatible with STM32WL SDK v1.2.0 and v1.3.0.

#### Getting STM32WL SDK v1.2.0

1. If you already have the STM32CubeIDE running on your machine, the next step is to download the <a href="https://www.st.com/en/embedded-software/stm32cubewl.html#get-software" target="_blank">STM32WL SDK v1.2.0</a> from the STMicroelectronics website.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32wl-sdk-download-page.png"
  width="70%"
  caption="STM32WL SDK Download Page"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32wl-v1-2-0-download.png"
  width="85%"
  caption="STM32WL V1.2.0 Download"
  zoomMode={true}
/>

2. The downloaded files usually go to the downloads folder. You need to extract it, and then you will see the STM32WL SDK firmware folder.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32wl-v1-2-0.png"
  width="60%"
  caption="STM32WL V1.2.0"
  zoomMode={true}
/>

3. The structure of the extracted files should be the same as shown in **Figure 32**. Do not change this folder structure. It contains many examples related to the STM32WL chip.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32wl-v1-2-0-folder-structure.png"
  width="70%"
  caption="STM32WL V1.2.0 Folder Structure"
  zoomMode={true}
/>


#### Modifications for the RAK3172

##### Files Modification Needed to Run STM32WL SDK LoRaWAN Examples to RAK3172

If you already have the STM32WL V1.2.0 SDK folder, there are only a few files that you need to update to create firmware that will run on the RAK3172.

:::tip NOTE

STM32 microcontroller firmware created using STM32CubeIDE (with the help of STM32CubeMX) has a **.ioc** file. This is a configuration file created by the STM32CubeMX tool. This is a useful tool in setting up peripherals and drivers quickly in the STM32 development ecosystem. However, once you make the file modifications mentioned in this guide, you cannot create a new **.ioc** file or modify it via STM32CubeMX. Otherwise, the modified files needed by the RAK3172 will be overwritten and will revert to their original state in the **.ioc** file.

In cases where you need to use STM32CubeMX to set up peripherals or drivers, you just need to repeat the same modifications mentioned in this section.
:::

1. Download the <a href="https://downloads.rakwireless.com/LoRa/RAK3172/Firmware/RAK3172_Low_Level_Development_v1_2_0.zip" target="_blank">Low-Level Development zip file for v1.2.0</a> from the RAK downloads site. Extract the zip file, and inside the folder are four files that need to be copied and pasted to specific locations in the STM32WL V1.2.0 folder to make it compatible with RAK3172.

The majority of these files are for setting up the RF channel front end of the radio section on the STM32WL chip. Also, the startup file must be changed because the default startup on STM32WL SDK V1.2.0 is for the STM32WL55 series and not for STM32WLE5. The RAK3172 is based on STM32WLE5CCU6.

:::tip NOTE
This guide will demonstrate how to run the **LoRaWAN_End_Node** example of the STM32WL SDK to RAK3172. If you need to run other LoRaWAN-related examples like **LoRaWAN_AT_Slave**, you need to update the files on that folder.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/rak3172-low-level-development-files.png"
  width="60%"
  caption="RAK3172 Low Level Development Files"
  zoomMode={true}
/>

2. The radio related files `radio_board_if.c`, `radio_board_if.h`, and `radio_conf` must be placed in this location of the STM32WL SDK folder `\STM32Cube_FW_WL_V1.2.0\Projects\NUCLEO-WL55JC\Applications\LoRaWAN\LoRaWAN_End_Node\LoRaWAN\Target`. You have to overwrite or replace the old files.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/rak3172-radio-files.png"
  width="60%"
  caption="RAK3172 Radio Related Files for Modification"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/rak3172-radio-replace.png"
  width="40%"
  caption="RAK3172 Radio Related Files Replaced"
  zoomMode={true}
/>

3. You also need to update the startup file. Move the `startup_stm32wle5ccux.s` file to this location: `\STM32Cube_FW_WL_V1.2.0\Projects\NUCLEO-WL55JC\Applications\LoRaWAN\LoRaWAN_End_Node\STM32CubeIDE\Application\User\Startup`. Delete the default startup file in that directory, named `startup_stm32wl55jcix.s`.

The updated startup folder should look like the one shown in **Figure 36**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/rak3172-radio-related-files-replaced.png"
  width="60%"
  caption="RAK3172 Radio Related Files Replaced"
  zoomMode={true}
/>

4. After the modifications above, there are minor changes needed to be adjusted on other source files.

- On *\STM32Cube_FW_WL_V1.2.0\Projects\NUCLEO-WL55JC\Applications\LoRaWAN\LoRaWAN_End_Node\Core\Inc\platform.h*, you need to comment out `#define USE_BSP_DRIVER`. It should be `//#define USE_BSP_DRIVER`.
- On *\STM32Cube_FW_WL_V1.2.0\Projects\NUCLEO-WL55JC\Applications\LoRaWAN\LoRaWAN_End_Node\LoRaWAN\Target\lorawan_conf.h*, you need to change the version of LoRaWAN to 1.0.3 which is the commonly used LNS version at the moment of this writing. To do this, you have to change LORAMAC_SPECIFICATION_VERSION to 0x01000300. It should look like this `#define LORAMAC_SPECIFICATION_VERSION 0x01000300`. However, if you are using LoRaWAN version 1.0.4 on your LNS, you do not need to perform this step since the DevNonce will be handled correctly.


##### Initial Build Test for the RAK3172 Custom Firmware

1. After making the file modifications, the next step is to test if the **LoRaWAN_End_Node** example can be built without errors.

:::tip NOTE
If this is your first time using STM32CubeIDE, it shows the **Information Center** by default. Just close it and access the project in the left panel.
:::

2. Open the STM32CubeIDE and click on `File` then `Open Projects from File System`.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-openproject.png"
  width="90%"
  caption="Open the Project in STM32CubeIDE"
  zoomMode={true}
/>

3. You then need to browse to the project folder location by clicking the **Directory** button.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide_open_dir.png"
  width="90%"
  caption="Locate the Project Directory in STM32CubeIDE"
  zoomMode={true}
/>

4. You should locate this directory `\STM32Cube_FW_WL_V1.2.0\Projects\NUCLEO-WL55JC\Applications\LoRaWAN\LoRaWAN_End_Node`. Click on **STM32CubeIDE** folder once, then click the **Select Folder**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-project-stm32cube.png"
  width="70%"
  caption="Select the STM32CubeIDE Project Folder"
  zoomMode={true}
/>

5. You should now see the **STM32CubeIDE** checked and ready to be imported as an **Eclipse project**. If not checked, select the checkbox and then click the **Finish** button. It will take some time to fully import the entire project.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-finalopen-project.png"
  width="70%"
  caption="Open the LoRaWAN_End_Node Project"
  zoomMode={true}
/>

6. After the successful import, you should now see the **LoRaWAN_End_Node** project structure on the left side of the STM32CubeIDE.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-rak3172-initproject.png"
  width="90%"
  caption="Open the STM32CubeIDE Project"
  zoomMode={true}
/>

7. With the modified files already implemented, you can check if the files are updated by checking the startup file `startup_stm32wle5ccux.s` and the `radio_board_if.c`. The startup file must be updated to show `startup_stm32wle5ccux.s`. You should see `#if defined(RAK3172_RF_CHANNEL_SWITCH)` on line 72 of the `radio_board_if.c` file, as shown in **Figure 42**. If not, then you were not successful in changing these files with the [Low Level Development required modification](#files-modification-needed-to-run-stm32wl-sdk-lorawan-examples-to-rak3172).

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-rak3172-modfile.png"
  width="90%"
  caption="Open the STM32CubeIDE Project"
  zoomMode={true}
/>

8. The next step is to ensure that a bin file will be generated for your release build. Go to the properties and ensure that *Convert to binary file (-O binary)* is checked.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-bin-settings.png"
  width="90%"
  caption="Bin generation settings"
  zoomMode={true}
/>

9. You can now attempt to build the project by setting the build configuration to release, which will generate a `.bin` file.

:::tip NOTE
If you have an ST-LINK debugging tool, you can also choose **Debug** instead of **Release**.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-buildconfig.png"
  width="90%"
  caption="Configure Build to Release"
  zoomMode={true}
/>

10. After setting the build configuration, you are now ready to build the project. You should see a successful compilation and generation of a `.bin` file.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-rak3172-build.png"
  width="90%"
  caption="Build the Project"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/successful-project-build.png"
  width="90%"
  caption="Successful Project Build"
  zoomMode={true}
/>

### RAK3172 on STM32CubeIDE with STM32WL SDK v1.3.0

The STM32WL SDK v1.3.0 guide is nearly identical to the [guide for v1.2.0](#rak3172-on-stm32cubeide-with-stm32wl-sdk-v120).

Follow the same procedure for changing the radio-related source files and startup file. You can also use the same RF source files used in v1.2.0 for v1.3.0. However, you must work with v1.3.0 of the STM32WL SDK package instead of the older version (v1.2.0).

## Running the LoRaWAN_End_Node Example of STM32WL SDK on RAK3172

### Configuration to Connect the LoRaWAN Network Server

Once you have a working project and have been able to build with no errors in the STM32CubeIDE, the next step is to configure the LoRaWAN parameters to be able to run the **LoRaWAN_End_Node** example code with the RAK3172.

1. First, you need to register the device to the network server. You can follow the guide on how to register a device in TTN V3 or Chirpstack using the procedure discussed in the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/quickstart/#ttn-otaa-device-registration" target="_blank">RAK3172 TTN V3 OTAA Quick Start Guide</a> or in the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/quickstart/#chirpstack-otaa-device-registration" target="_blank">RAK3172 Chirpstack OTAA Quick Start Guide</a> respectively.

:::tip NOTE
By default, the **LoRaWAN_End_Node** example will work on the EU868 region. This is set in the `lora_app.h` that can be found in this location `/STM32Cube_FW_WL_V1.0.0/Projects/NUCLEO-WL55JC/Applications/LoRaWAN/LoRaWAN_End_Node/LoRaWAN/App/`(for v1.0.0), `/STM32Cube_FW_WL_V1.2.0/Projects/NUCLEO-WL55JC/Applications/LoRaWAN/LoRaWAN_End_Node/LoRaWAN/App/`(for v1.2.0) and `/STM32Cube_FW_WL_V1.3.0/Projects/NUCLEO-WL55JC/Applications/LoRaWAN/LoRaWAN_End_Node/LoRaWAN/App/`(for v1.3.0).
:::

2. To activate and connect your device via OTAA, you need to obtain the following parameters: **DEVEUI**, **APPEUI**, and **APPKEY**.

Once you successfully register your device with TTN V3, you should see these parameters, as shown in **Figure 47**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/ttn-v3-registration.png"
  width="60%"
  caption="OTAA device registration in TTN V3"
  zoomMode={true}
/>

3. With the device registered to TTN V3, you should edit the `se-identity.h` file to update the required OTAA parameters. On the STM32CubeIDE, click **File** and select **Open File...**. You should navigate to this directory `\STM32Cube_FW_WL_Vx.y.z\Projects\NUCLEO-WL55JC\Applications\LoRaWAN\LoRaWAN_End_Node\LoRaWAN\App` (where Vx.y.z represents the version number of the SDK, such as v1.0.0, v1.2.0, or v1.3.0) to find the `se-identity.h` file, then click **Open**.


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-select-se-file.png"
  width="90%"
  caption="Open the File Needed to Modify with OTAA Parameters"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-open-se-file.png"
  width="60%"
  caption="Open the se-identity.h File"
  zoomMode={true}
/>

4. The `se-identity.h` header file must be updated with the common DEVEUI, APPEUI, and APPKEY parameters in the device registration on the network server. In this example, you can see that the `LORAWAN_DEVEUI_EUI`, `LORAWAN_JOIN_EUI`, and `LORAWAN_APP_KEY` are updated, as shown in **Figure 50**. These values are based on the TTN V3 registration in **Figure 47**.

The `LORAWAN_JOIN_EUI` is the same as the `App_EUI` in this guide which is the term that adheres to the **LoRaWAN Specification V1.1**.

:::tip NOTE
To ensure that your device works on both LoRaWAN versions (**LoRaWAN Specifications V1.0.x and V1.1**), make sure that the application root key `LORAWAN_APP_KEY` and the network root key `LORAWAN_NWK_KEY` of the `se-identity.h` file are exactly the same. Otherwise, you might encounter MIC-related errors while joining the network.

```c
/*!
 * Application root key
 */
#define LORAWAN_APP_KEY                                    2B,7E,15,16,28,AE,D2,A6,AB,F7,15,88,09,CF,4F,3C

/*!
 * Network root key
 */
#define LORAWAN_NWK_KEY                                    2B,7E,15,16,28,AE,D2,A6,AB,F7,15,88,09,CF,4F,3C
```
:::

The macro `STATIC_DEVICE_EUI` is also updated to `1` instead of `0` because a generated DEVEUI in TTN V3 is used in this guide instead of the embedded DEVEUI of the device.

:::tip NOTE
STM32WL SDK v1.3.0 has different structure of `se-identity.h` file. It does not have `STATIC_DEVICE_EUI` and is available only on lower versions of the SDK.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-modified-se-file.png"
  width="90%"
  caption="Modified se-identity.h File"
  zoomMode={true}
/>

:::tip NOTE
These parameters are usually set and code generated in the **.ioc** file via STM32CubeMX. However, that method is not possible since a direct modification of the radio-related source files is done in this guide. Any further code generation via STM32CubeMX after the modifications in the previous steps in this guide will override all the changes that are required to run the LoRaWAN_End_Node project example for the RAK3172 module.
:::

### Generation of BIN file

With all the necessary files modified and edited, you can now generate your `.bin` FW file and upload it to your RAK3172 module.

1. The first step is to first clean the project to remove any outdated binary files in the project folder, followed by building it. Sometimes, **Build Project** is not clickable, so you can use **Build All** as an alternative. You only have one project as of now, so that should work fine as well.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-cleanbuild-project.png"
  width="90%"
  caption="Clean and Build the STM32CubeIDE Project"
  zoomMode={true}
/>

2. After a successful build, you should see in console **Finished building: LoRaWAN_End_Node.bin**. Also, check if there's a generated `LoRaWAN_End_Node.bin` firmware file in the following folder location: `\STM32Cube_FW_WL_Vx.y.z\Projects\NUCLEO-WL55JC\Applications\LoRaWAN\LoRaWAN_End_Node\STM32CubeIDE\Release` (Vx.y.z means the version number of the SDK - v1.0.0, v1.2.0 or v1.3.0). The bin file is the firmware binary that you need to upload to your RAK3172 module.

:::tip NOTE
For the generated compiled files, `hex` format is also acceptable.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeide-buildok-project.png"
  width="90%"
  caption="Successful Build with BIN File for RAK3172"
  zoomMode={true}
/>

## Uploading the FW Generated Using STM32CubeProgrammer

The generated binary (.bin) firmware file is ready to be uploaded to the RAK3172.

To upload this binary file, you will need to use STM32CubeProgrammer, created by STMicroelectronics.

<a href="https://www.st.com/en/development-tools/stm32cubeprog.html" target="_blank">Download the latest version STM32CubeProgrammer</a> and the one compatible with your computer.

In this guide, you will use the internal UART bootloader of the STM32WL and connect the RAK3172 to a USB to Serial converter tool. You need to connect five pins: power supply pins (3.3&nbsp;V and GND), UART2 pins (TX and RX), and the Boot0 pin (connected to 3.3&nbsp;V), as shown in **Figure 53**.

:::warning
RAKDAP1 hardware debugger **DOES NOT** work with STM32CubeProgrammer. It is advisable to use an alternative USB-UART converter when using the UART bootloader of STM32WL to upload a .bin nor .hex file.
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/rak3172-boot0.png"
  width="55%"
  caption="RAK3172 Connection to USB-UART Converter with Boot0 Pin at 3.3V Level"
  zoomMode={true}
/>

:::tip NOTE
You can also use an ST-LINK to upload the `.bin` file to RAK3172.
:::

1. Once the hardware is now ready, you can open the STM32CubeProgrammer. Then you need to open the `LoRaWAN_End_Node.bin` FW file from this folder location `\STM32Cube_FW_WL_V1.0.0\Projects\NUCLEO-WL55JC\Applications\LoRaWAN\LoRaWAN_End_Node\STM32CubeIDE\Release`(for v1.0.0) or `\STM32Cube_FW_WL_V1.2.0\Projects\NUCLEO-WL55JC\Applications\LoRaWAN\LoRaWAN_End_Node\STM32CubeIDE\Release`(for v1.2.0).

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeprog-open.png"
  width="80%"
  caption="STM32CubeProgrammer Application"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeprog-browse-bin.png"
  width="80%"
  caption="Locating the .bin Firmware File"
  zoomMode={true}
/>

2. If everything is successful, you should now see the `LoRaWAN_End_Node.bin` FW file in the STM32CubeProgrammer.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeprog-loaded-bin.png"
  width="80%"
  caption="Loaded .bin Firmware File to the STM32CubeProgrammer"
  zoomMode={true}
/>

3. By default, the STM32CubeProgrammer selects ST-LINK as the upload interface. Therefore, you need to change it to UART and select the correct COM port. After setting up the UART connection, you can now connect and see that the device has been detected.


<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeprog-uart.png"
  width="80%"
  caption="Selecting UART as Programming Interface"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeprog-poart.png"
  width="80%"
  caption="Selecting the Right COM Port"
  zoomMode={true}
/>

4. You need to ensure that the `Boot0` is connected to VDD (3.3&nbsp;V) when the device is powered up, else, the STM32CubeProgrammer might not detect the device. The logs of a detected device are shown in **Figure 59**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeprog-connected.png"
  width="80%"
  caption="RAK3172 Detected by STM32CubeProgrammer"
  zoomMode={true}
/>

5. If the device is detected by the STM32CubeProgrammer, you can now upload the firmware by clicking **Download**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeprog-uploading.png"
  width="80%"
  caption="Firmware Uploading in Progress"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/stm32cubeprog-uploaded.png"
  width="80%"
  caption="Firmware Successfully Uploaded"
  zoomMode={true}
/>

6. After the successful download, restart the device and remove the connection of the Boot0 pin to VDD (3.3&nbsp;V), leaving you only with four-pin connections (power supply lines and UART2) as shown in **Figure 62**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/rak3172-connection-to-uart.png"
  width="50%"
  caption="RAK3172 Connection to UART"
  zoomMode={true}
/>

7. By using serial terminal software, check the serial output logs of the RAK3172 with the newly uploaded firmware with the baud rate set to 115200. You should be able to see the serial logs, as shown in **Figure 63**.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/rak3172-uart2-logs.png"
  width="40%"
  caption="RAK3172 UART2 Logs"
  zoomMode={true}
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/rak3172-uart2-logs-for-sdk-v1-3-0.png"
  width="55%"
  caption="RAK3172 UART2 Logs for SDK version 1.3.0"
  zoomMode={true}
/>

8. With the device registered with TTN, you should now see a successful join and LoRaWAN device uplink.

<RkImage
  src="https://images.docs.rakwireless.com/wisduo/rak3172-module/low-level-development/ttn-join-success.png"
  width="90%"
  caption="RAK3172 in TTN V3 Join and Uplink"
  zoomMode={true}
/>

<RkBottomNav/>