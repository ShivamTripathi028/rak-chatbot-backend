---
slug: /product-categories/accessories/rakdap1/quickstart/
title: RAKDAP1 Quick Start | Flash & Debug LoRaWAN Modules via DAPLink
description: Learn how to set up and use RAKDAP1 for SWD flashing and debugging. Follow this quick start guide to program LoRaWAN modules using DAPLink on Windows, macOS, and Linux.
image: https://images.docs.rakwireless.com/accessories/rakdap1-flash-and-debug-tool/rakdap1.png
keywords: 
  - rakdap1
  - rakdap1 debug tool
  - rakdap1 flash programmer
  - rakdap1 installation guide
  - install rakdap1 on windows
  - rakdap1 setup guide
  - rakdap1 pyocd installation
  - rakdap1 firmware update
  - daplink flash tool
  - debug arm cortex based mcu
  - flash firmware in lorawan modules
  - configure arm cortex mcu for flashing
  - programming tool for embedded systems
  - software for flashing embedded mcus
  - debug and program iot devices
  - debugging tools in embedded system
  - daplink firmware upgrade
  - mcu bootloader flashing
date: 2020-09-22
sidebar_label: Quick Start Guide
---

# RAKDAP1 Flash and Debug Tool Quick Start Guide

## Installation

As mentioned, RAKDAP1 is an SWD flash and debug tool that runs [**DAPLink**](https://os.mbed.com/docs/mbed-os/v5.15/tools/daplink.html#daplink-features) to connect your RAKwireless product to your computer. It has an easy to use command line interface and supports the leading industry standard tool chains to program and debug the target system.

The following are the supported tools:

1. **pyOCD**
2. **IAR Workbench**
3. **Keil MDK**

To use it, the open-source pyOCD Python SW is required. If you have already installed Python 3 on your computer, you can proceed to [Installation of pyOCD](#pyocd-installation).

### Python 3 Installation

Before anything else, it requires you to install Python 3 on your computer. Download the latest Python 3 from the official Python website. Go to their [Python Downloads](https://www.python.org/downloads/) and choose an installer depending on your system.

#### Windows

1. Choose the python installer for Windows.
2. Once downloaded, start the installation process.
3. Make sure to check the **`Add python.exe to PATH`**. Otherwise, you will have to add it manually later.

> **Image:** Installing Python for Windows

4. Wait until the installation is finished.

> **Image:** Disable the Path Limit

5. After the installation has finished, open a command prompt window and check the versions of **Python** and **pip3** using the following command listed below.

```
python --version
```

```
pip --version
```

> **Image:** Checking the Python and pip3 versions

:::tip NOTE
pip3 is required to install additional Python packages.
:::

#### MacOS

Open the terminal on your Mac machine and type the following commands:

```
ruby -e $(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)
```

```
export PATH="/usr/local/opt/python/libexec/bin:$PATH"
```

:::tip NOTE
If your macOS is based on Apple M chips, you might need to use this path:

`export PATH="/opt/homebrew/opt/python/libexec/bin:$PATH"` or `export PATH="/opt/homebrew/opt/python@3/libexec/bin:$PATH"`
:::

```
brew install python
```

```
python --version
```

```
brew install libusb
```

#### Linux

Open the terminal on your Linux machine and type the following command:

```
sudo apt-get install python3
```

### pyOCD Installation

Next step is to install pyOCD which is the SW tool required to flash bootloaders and application SW.

1. To start the installation, open the command prompt and use the following command:

```
pip3 install pyocd
```

> **Image:** Installing pyOCD

2. After the installation is finished, check the version.

```
pyocd --version
```

> **Image:** pyOCD version

### Support Packages Installation

To flash and debug MCU, DAPLink needs support packages. These support packages are MDK files. For more details, you can refer to the supporting list of [MDK](https://www.keil.com/dd2/Pack/).

But before installing, check the list first to know the required package for your RAKwireless product.

| MODEL | SUPPORTED PACKAGE |
| --- | --- |
| RAK3172 Module | stm32wle5 |
| RAK811 Module | stm32l151cb |
| RAK8710 | stm32l151cb |
| RAK4200 Module | stm32l071kb |
| Products using RAK4200 | stm32l071kb |
| RAK4270 Module | stm32l071kb |
| Products using RAK4270 | stm32l071kb |
| RAK7201/7202/7203 | stm32l071kb |
| RAK4600 Module | nrf52 |
| RAK4600 Evaluation Board | nrf52 |
| RAK8212 Board | nrf52 |
| RAK813 Module | nrf52 |
| RAK5010 | nrf52840 |
| RAK4630 | nrf52840 |
| RAK4631 | nrf52840 |
| RAK3401 | nrf52840 |
| RAK4260 Evaluation Board | atsaml21j18a |
| Products using RAK4260 | atsaml21j18a |
| RAK11720 and its variants | AMA3B1KK-KBR |

To install the support package, use the following command:

```
pyocd pack --i \<PACKAGE\>
```
For example, if you have RAK4630 module, enter the following command:

```
pyocd pack --i nrf52840
```

> **Image:** Installing NRF52840 into the RAK4630 module

To check installed packages, you can use the command:

```
pyocd pack -s
```

Before flashing a new firmware, you can also perform the erase command.

:::warning

Erasing the flash memory will remove all configured parameters in the modules like factory settings and LoRaWAN parameters (EUIs and keys).

:::

```
pyocd erase -t \<PACKAGE\> --chip
```

For example, if you use RAK4630 module, you can use this command:

```
pyocd erase -t nrf52840 --chip
```

## How to Flash an MCU

Before flashing a firmware or a bootloader for your product, connect it first to the RAKDAP1 SWD interface.

Here is an overview on how to connect the SWD interface. If you cannot find your product in the list, check the product documentation in the [RAK Documentation Center](https://docs.rakwireless.com).

### RAK3172 Module

> **Image:** RAK3172 Module Pinout

### RAK811 Module

> **Image:** RAK811 Module Pinout

### RAK4200 Module

> **Image:** RAK4200 Module Pinout

### RAK4600 Module

> **Image:** RAK4600 Module Pinout

### RAK4270 Module

> **Image:** RAK4270 Module Pinout

### RAK4260 Module

> **Image:** RAK4260 Module Pinout

### RAK4260 Evaluation Board

> **Image:** RAK4260 Evaluation Board Pinout

### RAK4600 Evaluation Board

> **Image:** RAK4600 Evaluation Board Pinout

### RAK4630 Module
- For RAK4630 module, it is recommended to include an external DC supply or battery to prevent errors during bootloader flashing.

> **Image:** RAK4630 in WisBlock Base

Open the command prompt or terminal, then go to the directory where you saved the firmware file you want to flash using the `cd <path>` command.

The pyocd command syntax to flash the file is the following:

```
pyocd flash -t \<PACKAGE\> \<FILENAME\>
```

- Change **\<PACKAGE\>** to the support package from above list.
- Change **\<FILENAME\>** to the filename you want to flash. The file should be in __.hex__ format.

Here is an example to flash the bootloader to a RAK4631 WisBlock Core module:

```
pyocd flash -t nrf52840 RAK4631_latest_final.hex
```

> **Image:** Flashing the bootloader into the RAK4630 module

> **Image:** Flashing bootloader completed

