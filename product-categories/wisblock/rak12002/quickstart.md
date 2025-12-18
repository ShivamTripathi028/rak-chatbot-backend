---
slug: /product-categories/wisblock/rak12002/quickstart/
description: Contains instructions and tutorials for installing and deploying your RAK12002. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak12002/rak12002.png"
keywords:
  - quickstart
  - RAK12002
  - wisblock
sidebar_label: Quick Start Guide
---

# RAK12002 WisBlock RTC Module Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step on using RAK12002 WisBlock module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK12002 WisBlock RTC Module](https://store.rakwireless.com/collections/wisblock-extra/products/rtc-module-rak12002?variant=40102983598278?utm_source=RAK12002&utm_medium=Document&utm_campaign=BuyFromStore)
- Your choice of [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base/)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

##### Arduino

- Download and install [Arduino IDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino Boards Manager, install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

## Product Configuration

### Hardware Setup

The RAK12002 is a Real-Time Clock module, part of the RAKwireless WisBlock Series, which was designed to provide real-time clock capabilities on your WisBlock projects. The RTC chip is based on RV-3028-C7 from Micro Crystal which can be interfaced via I2C.

For more information about RAK12002, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak12002/datasheet/).

> **Image:** RAK12002 connection to WisBlock Base

:::tip NOTE
- You can connect the RAK12002 to any of the WisBlock Base Board Slot A to D.
- RAK12002 has a built-in supercapacitor that can provide up to 7 days of extra timing capability in case the Li-Ion Battery is drained or disconnected.
:::

> **Image:** RAK12002 connection to WisBlock Base Slots A to D

#### Assembling and Disassembling of WisBlock Modules

##### Assembling Procedure

The RAK12002 module can be mounted on the IO slot of the WisBlock Base board, as shown in **Figure 3**. Also, always secure the connection of the WisBlock module by using the compatible screws.

> **Image:** RAK12002 mounting connection to WisBlock Base module

##### Disassembling Procedure

The procedure in disassembling any type of WisBlock modules is the same.

1. First, remove the screws.

> **Image:** Removing screws from the WisBlock module

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

> **Image:** Detaching silkscreen on the WisBlock module

3. Apply force to the module at the position of the connector, as shown in **Figure 6**, to detach the module from the baseboard.

> **Image:** Applying even forces on the proper location of a WisBlock module

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts.
:::

### Software Configuration and Example

In the following example, you will be using the [RAK12002 WisBlock RTC Module](https://store.rakwireless.com/collections/wisblock-extra/products/rtc-module-rak12002?variant=40102983598278) to setup the time and date.

#### RAK12002 in RAK4631 WisBlock Core Guide

##### Arduino Setup

1. First, you need to select the RAK4631 WisBlock Core.

> **Image:** Selecting RAK4631 as WisBlock Core

2. Next, copy the following sample code into your Arduino IDE.

<details>
<summary> Click to view the code </summary>

```c
/**
   @file RAK12002_RTC_DateTime_RV-3028-C7.ino
   @author rakwireless.com
   @brief Set and read RTC time.
   @version 0.1
   @date 2021-04-30
   @copyright Copyright (c) 2021
**/

#include "Melopero_RV3028.h" //Click here to get the library: http://librarymanager/All#Melopero_RV3028

Melopero_RV3028 rtc;

/**
 * @brief Arduino setup function
 * @note Called once after power on or reset
 *
 */
void setup()
{
  // Initialize Serial for debug output
  time_t timeout = millis();
  Serial.begin(115200);
  while (!Serial)
  {
    if ((millis() - timeout) < 5000)
    {
      delay(100);
    }
    else
    {
      break;
    }
  }
  rtc.initDevice(); // First initialize and create the rtc device

  rtc.writeToRegister(0x35,0x00);
  rtc.writeToRegister(0x37,0xB4); //Direct Switching Mode (DSM): when VDD < VBACKUP, switchover occurs from VDD to VBACKUP

  rtc.set24HourMode();  // Set the device to use the 24hour format (default) instead of the 12 hour format

  // Set the date and time
  // year, month, weekday, date, hour, minute, second
  // Note: time is always set in 24h format
  // Note: month value ranges from 1 (Jan) to 12 (Dec)
  // Note: date value ranges from 1 to 31
  rtc.setTime(2021, 4, 6, 30, 0, 0, 0);
}

/**
 * @brief Arduino loop function
 * @note Output date and time every second
 *
 */
void loop()
{
  Serial.printf("%d:%d:%d %d/%d/%d \n",rtc.getHour(),rtc.getMinute(),rtc.getSecond(),rtc.getYear(),rtc.getMonth(),rtc.getDate());
  delay(1000);
}

```
</details>

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated code for the RAK4631 WisBlock Core Module that can be found on the [RAK12002 WisBlock Example Code Repository](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK12002_RTC_DateTime_RV-3028-C7)
:::

3. Click the link to locate the library.

> **Image:** Locating the required library in the Library Manager

4. Install the required library, as shown in **Figure 9**.

> **Image:** Installing the Library

5. Select the correct port and upload your code, as shown in **Figure 10** and **Figure 11**.

> **Image:** Selecting the correct Serial Port

> **Image:** Uploading code

6. When you successfully uploaded the example sketch, open the Serial Monitor of the Arduino IDE to see the RAK12002 date/time logs, as shown in **Figure 12**. You will be able to see the Time and Date in the Serial Monitor.

> **Image:** RAK12002 date/time logs

7. You can set the time and date in the code, as shown in **Figure 13** and **Figure 14**.

> **Image:** Code for setting the time and date in RAK12002

> **Image:** Time and Date format

#### RAK12002 in RAK11200 WisBlock Core Guide

##### Arduino Setup

1. Select the RAK11200 WisBlock Core.

> **Image:** Selecting RAK11200 as WisBlock Core

2. Next, copy the following sample code into your Arduino IDE.

<details>
<summary> Click to view the code </summary>

```c
/**
   @file RAK12002_RTC_DateTime_RV-3028-C7.ino
   @author rakwireless.com
   @brief Set and read RTC time.
   @version 0.1
   @date 2021-04-30
   @copyright Copyright (c) 2021
**/

#include "Melopero_RV3028.h" //Click here to get the library: http://librarymanager/All#Melopero_RV3028

Melopero_RV3028 rtc;

/**
 * @brief Arduino setup function
 * @note Called once after power on or reset
 *
 */
void setup()
{
  // Initialize Serial for debug output
  time_t timeout = millis();
  Serial.begin(115200);
  while (!Serial)
  {
    if ((millis() - timeout) < 5000)
    {
      delay(100);
    }
    else
    {
      break;
    }
  }
  rtc.initDevice(); // First initialize and create the rtc device

  rtc.writeToRegister(0x35,0x00);
  rtc.writeToRegister(0x37,0xB4); //Direct Switching Mode (DSM): when VDD < VBACKUP, switchover occurs from VDD to VBACKUP

  rtc.set24HourMode();  // Set the device to use the 24hour format (default) instead of the 12 hour format

  // Set the date and time
  // year, month, weekday, date, hour, minute, second
  // Note: time is always set in 24h format
  // Note: month value ranges from 1 (Jan) to 12 (Dec)
  // Note: date value ranges from 1 to 31
  rtc.setTime(2021, 4, 6, 30, 0, 0, 0);
}

/**
 * @brief Arduino loop function
 * @note Output date and time every second
 *
 */
void loop()
{
  Serial.printf("%d:%d:%d %d/%d/%d \n",rtc.getHour(),rtc.getMinute(),rtc.getSecond(),rtc.getYear(),rtc.getMonth(),rtc.getDate());
  delay(1000);
}

```
</details>

:::tip NOTE
If you experience any error in compiling the example sketch, check the updated code for the RAK11200 WisBlock Core Module that can be found on the [RAK12002 WisBlock Example Code Repository](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK12002_RTC_DateTime_RV-3028-C7)
:::

3. Click the link to locate the library.

> **Image:** Locating the required library in the Library Manager

4. Install the required library, as shown in **Figure 17**.

> **Image:** Installing the Library

5. Select the correct port and upload your code, as shown in **Figure 18** and **Figure 19**.

> **Image:** Selecting the correct Serial Port

> **Image:** Uploading code

:::tip NOTE
RAK11200 requires the BOOT0 pin to be configured properly before uploading. If not done properly, uploading the source code to RAK11200 will fail. Check the full details on the [RAK11200 Quick Start Guide](https://docs.rakwireless.com/product-categories/wisblock/rak11200/quickstart/#uploading-to-wisblock).
:::

6. When you successfully uploaded the example sketch, open the Serial Monitor of the Arduino IDE to see the RAK12002 date/time logs, as shown in **Figure 20**. You will be able to see the Time and Date in the Serial Monitor.

> **Image:** RAK12002 date/time logs

7. You can set the time and date in the code, as shown in **Figure 21** and **Figure 22**.

> **Image:** Code for setting the time and date in RAK12002

> **Image:** Time and Date format

#### RAK12002 in RAK11300 WisBlock Core Guide

##### Arduino Setup

1. Select the RAK11300 WisBlock Core, as shown in **Figure 23**.

> **Image:** Selecting RAK11300 as WisBlock Core

2. Next, copy the following sample code into your Arduino IDE:

```c
/**
   @file RAK12002_RTC_DateTime_RV-3028-C7.ino
   @author rakwireless.com
   @brief Set and read RTC time.
   @version 0.1
   @date 2021-04-30
   @copyright Copyright (c) 2021
**/

#include "Melopero_RV3028.h" //Click here to get the library: http://librarymanager/All#Melopero_RV3028

Melopero_RV3028 rtc;

/**
 * @brief Arduino setup function
 * @note Called once after power on or reset
 *
 */
void setup()
{
  // Initialize Serial for debug output
  time_t timeout = millis();
  Serial.begin(115200);
  while (!Serial)
  {
    if ((millis() - timeout) < 5000)
    {
      delay(100);
    }
    else
    {
      break;
    }
  }
  rtc.initDevice(); // First initialize and create the rtc device

  rtc.writeToRegister(0x35,0x00);
  rtc.writeToRegister(0x37,0xB4); //Direct Switching Mode (DSM): when VDD < VBACKUP, switchover occurs from VDD to VBACKUP

  rtc.set24HourMode();  // Set the device to use the 24hour format (default) instead of the 12 hour format

  // Set the date and time
  // year, month, weekday, date, hour, minute, second
  // Note: time is always set in 24h format
  // Note: month value ranges from 1 (Jan) to 12 (Dec)
  // Note: date value ranges from 1 to 31
  rtc.setTime(2021, 4, 6, 30, 0, 0, 0);
}

/**
 * @brief Arduino loop function
 * @note Output date and time every second
 *
 */
void loop()
{
  Serial.printf("%d:%d:%d %d/%d/%d \n",rtc.getHour(),rtc.getMinute(),rtc.getSecond(),rtc.getYear(),rtc.getMonth(),rtc.getDate());
  delay(1000);
}

```
:::tip NOTE
If you experience any error in compiling the example sketch, check the updated code for the RAK11300 WisBlock Core Module that can be found on the [RAK12002 WisBlock Example Code Repository](https://github.com/RAKWireless/WisBlock/tree/master/examples/common/sensors/RAK12002_RTC_DateTime_RV-3028-C7).

:::

3. Click the link to locate the library, as shown in **Figure 24**.

> **Image:** Locating the required library in the Library Manager

4. Install the required library, as shown in **Figure 25**.

> **Image:** Installing the Library

5. Select the correct port and upload your code, as shown in **Figure 26** and **Figure 27**.

> **Image:** Selecting the correct Serial Port

> **Image:** Uploading code

6. When you successfully uploaded the example sketch, open the Serial Monitor of the Arduino IDE to see the RAK12002 date/time logs, as shown in **Figure 28**. You will be able to see the Time and Date in the Serial Monitor.

> **Image:** RAK12002 date/time logs

7. You can set the time and date in the code, as shown in **Figure 29** and **Figure 30**.

> **Image:** Code for setting the time and date in RAK12002

> **Image:** Time and Date format

