---
slug: /product-categories/wisblock/rak5811/quickstart/
title: RAK5811 WisBlock 0-5V Interface Module Quick Start Guide
description: Contains instructions and tutorials for installing and deploying your RAK5811. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your device. Aside from the hardware configuration, it also contains a software setup that includes detailed example codes that will help you get started.
image: "https://images.docs.rakwireless.com/wisblock/rak5811/RAK5811.png"
keywords:
  - quickstart
  - wisblock
  - RAK5811
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK5811 WisBlock 0-5V Interface Module Quick Start Guide

## Prerequisite

### What Do You Need?

Before going through each and every step on using the RAK5811 WisBlock module, make sure to prepare the necessary items listed below:

#### Hardware

- [RAK5811 WisBlock 0-5V Interface Module](https://store.rakwireless.com/collections/wisblock-interface/products/rak5811-0-5v-analog-interface/)
- [WisBlock Base](https://store.rakwireless.com/collections/wisblock-base/)
- Your choice of [WisBlock Core](https://store.rakwireless.com/collections/wisblock-core)
- USB Cable
- [Li-Ion/LiPo battery (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/battery-connector-cable?utm_source=BatteryConnector&utm_medium=Document&utm_campaign=BuyFromStore)
- [Solar charger (optional)](https://store.rakwireless.com/collections/wisblock-accessory/products/solar-panel-connector-cable?utm_source=SolarPanelConnector&utm_medium=Document&utm_campaign=BuyFromStore)

#### Software

##### Arduino
- Download and install [Arduino IDE](https://www.arduino.cc/en/Main/Software).
- To add the RAKwireless Core boards on your Arduino Boards Manager, install the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index).

##### PlatformIO

To use the WisBlock Core modules with PlatformIO, you need to install a small script named RAK_PATCH. The script can be installed on WisBlock Core RAK4631, RAK11200, and RAK11310. Install [RAK_PATCH on PlatformIO](https://github.com/RAKWireless/WisBlock/blob/master/PlatformIO/README).

:::warning
RAK_PATCH script was tested only on Windows 10 and Ubuntu.
In the case of the Raspberry PI 2040 platform update on PlatformIO, the RAK_PATH script must be executed again after the platform update.
:::

## Product Configuration

### Overview

To give you a better understanding of how the RAK5811 Module works, the block diagram is provided in this section.

#### Block Diagram

In the RAK5811 module, as shown in **Figure 1**, the 0-5&nbsp;V input signal is connected to the operational amplifier by the R1/R2 voltage divider. The operational amplifier output is routed to an analog input of the MCU to be digitalized by an internal ADC.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/rak5811-block-diagram.png"
  figureCount="1"
  width="60%"
  caption="RAK5811 Block Diagram"
/>

Once the signal is digitalized, you can recover the original voltage value by applying the following relation:

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/voltage-divider.png"
  figureCount="2"
  width="25%"
  caption="RAK5811 Voltage divider relation"
/>

Where Vout is the WisBlock Core read voltage, Vin is the analog input voltage (0-5&nbsp;V). From the voltage divider R1 is 1&nbsp;MΩ and R2 is 1.5&nbsp;MΩ, so the final relationship is: **Vin = Vout / 0.6**.

As shown in **Figure 1**, the module provides an output of 12&nbsp;V to power industrial sensors. This 12&nbsp;V output is controlled by a TPS60146 DC-DC booster. The **Enable** pin allows to control the output voltage of the booster module and sets the RAK5811 module into a low power consumption mode.

### Hardware Setup

#### Installation

##### Mounting Mechanism

The RAK5811 module is part of the WisBlock Interface category, which connects to the baseboard through the IO slot. Execute the following instructions carefully to install your WisConnector into the Baseboard:

1. Keep the RAK5811 module parallel to the baseboard, and gently place and plug WisConnector into the IO slot receptacle of the baseboard. The IO slot has an outer silkscreen on it to assist with the alignment. At this point, apply force evenly along with the module and press again. There will be a sound to confirm the successful completion of the attachment process.

:::tip NOTE
For detailed instructions, refer to the [WisBlock Installation Guide](https://learn.rakwireless.com/hc/en-us/articles/26743966497431-How-To-Install-RAK5005-O-Baseboard/).
:::

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/wisconnector.png"
  figureCount="3"
  width="60%"
  caption="WisConnector and IO slot"
/>

2. Always secure the RAK5811 module with **3 x M1.2 x3 pan head screws**, as shown in **Figure 4** below.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/rak5811_mounting.png"
  figureCount="4"
  width="60%"
  caption="RAK5811 mounting mechanism on a WisBlock Base module"
/>

##### RAK5811 Fast Crimping Terminal Mechanism

The RAK5811 features a fast-crimping terminal connector to simplify and ensure the wiring process on the fields. The fast-crimping terminal can support cable with a width between 20 AWG to 24 AWG. The usual stripping length is around 6 to 7&nbsp;mm.

As shown in **Figure 5**, during the crimping process, you should first press down and maintain the spring head of the crimping terminal firmly, then insert the stripped cable head into the corresponding connector’s hole. Once inserted correctly, release the spring head, and the crimping process is completed.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/crimping_process.png"
  figureCount="5"
  width="40%"
  caption="RAK5811 Crimping"
/>

:::tip NOTE
To learn more about the Pinout Diagram of the RAK5811 Module, refer to the [Datasheet](https://docs.rakwireless.com/product-categories/wisblock/rak5811/datasheet/#pin-definition).
:::

##### Disassembling Procedure

The procedure in disassembling any type of WisBlock module is the same.

1. Remove the screws.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/removing_screw.png"
  figureCount="6"
  width="70%"
  caption="Removing screws from the WisBlock module"
/>

2. Once the screws are removed, check the silkscreen of the module to find the correct location where force can be applied.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/detach_silkscreen.png"
  figureCount="7"
  width="70%"
  caption="Detaching silkscreen on the WisBlock module"
/>

3. Apply force to the module at the position of the connector, as shown in **Figure 8**, to detach the module from the baseboard.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/detach_module.png"
  figureCount="8"
  width="70%"
  caption="Applying even forces on the proper location of a WisBlock module"
/>

:::tip NOTE
If you will connect other modules to the remaining WisBlock Base slots, check on the [WisBlock Pin Mapper](https://learn.rakwireless.com/hc/en-us/articles/26743306645143-How-To-Use-the-WisBlock-IO-Pin-Mapping-Tool) tool for possible conflicts.
:::

:::warning

- Battery can cause harm if not handled properly.
- Only 3.7-4.2&nbsp;V Rechargeable LiPo batteries are supported. It is highly recommended not to use other types of batteries with the system unless you know what you are doing.
- If a non-rechargeable battery is used, it has to be unplugged first before connecting the USB cable to the USB port of the board to configure the device. Not doing so might damage the battery or cause fire.
- Make sure the battery wires match the polarity on the RAK WisBlock Base Board. Not all batteries have the same wiring.
- Only 5&nbsp;V solar panels are supported. Do not use 12&nbsp;V solar panels. It will destroy the charging unit and eventually other electronic parts.
:::

### Software Configuration and Example

#### Arduino Setup

The RAK5811 module includes a 12&nbsp;V voltage source which is controlled by the WisBlock Core module via the **Enable** pin of the WisBlock Base. This GPIO must be set to **HIGH** before sampling. The 12&nbsp;V voltage source is also designed to provide the power supply to the operational amplifier of the module. Before connecting a sensor to the RAK5811 module, you must be sure that the sensor can safely operate at 5&nbsp;V.

If you already installed the [RAKwireless Arduino BSP](https://github.com/RAKWireless/RAKwireless-Arduino-BSP-Index), the WisBlock Core and example code should now be available on the Arduino IDE.

1. Select the WisBlock Core you have, as shown in **Figure 9** to **Figure 11**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/rak4631_board.png"
  figureCount="9"
  width="100%"
  caption="Selecting RAK4631 as WisBlock Core"
/>


<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/rak11200_board.png"
  figureCount="10"
  width="100%"
  caption="Selecting RAK11200 as WisBlock Core"
/>


<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/rak11310_board.png"
  figureCount="11"
  width="100%"
  caption="Selecting RAK11310 as WisBlock Core"
/>

2. You can access the programming guide for the RAK5811 module by opening the example codes depending on your WisBlock Core, as shown in **Figure 12** to **Figure 14**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/example_rak4631_rak5811.png"
  figureCount="12"
  width="100%"
  caption="Opening RAK5811 example for RAK4631 WisBlock Core"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/example_rak11200_rak5811.png"
  figureCount="13"
  width="100%"
  caption="Opening RAK5811 example for RAK11200 WisBlock Core"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/example_rak11310_rak5811.png"
  figureCount="14"
  width="100%"
  caption="Opening RAK5811 example for RAK11310 WisBlock Core"
/>

3. After opening the example code, you can now select the right port and upload the code, as shown in **Figure 15** and **Figure 16**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/rak4631_select_port.png"
  figureCount="15"
  width="100%"
  caption="Selecting the correct Serial Port"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/rak4631_upload.png"
  figureCount="16"
  width="100%"
  caption="Uploading the RAK5811 example code"
/>

4. When you successfully uploaded the example sketch, open the Serial Monitor of the Arduino IDE to see the ADC reading logs, as shown in **Figure 17** and **Figure 18**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/rak4631_logs.png"
  figureCount="17"
  width="90%"
  caption="RAK4631 and RAK5811 example log"
/>

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/rak11200_logs.png"
  figureCount="18"
  width="90%"
  caption="RAK11200 and RAK5811 example log"
/>


#### PlatformIO Setup (Optional)

To develop using PlatformIO, you need to install the RAK_PATCH script as described in the section [PlatformIO](https://docs.rakwireless.com/product-categories/wisblock/rak5811/quickstart/#platformio).

1. Open the [RAK5811 Arduino example](https://docs.rakwireless.com/product-categories/wisblock/rak5811/quickstart/#software-configuration-and-example). Then install the libraries, build the project, and save the sketch.

2. Now launch open **Platformio** &gt; **PIO Home** and click on **import Arduino project** button, as shown in **Figure 19**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/pio-import.png"
  figureCount="19"
  width="100%"
  caption="Import Arduino project"
/>

3. Configure **Import Arduino Project** parameters:

  - On the boards list, select your favorite WisCore. For example: **WisCore RAK11310 Board (RAKwireless)** (Label 1).
  - Check **Use libraries installed by Arduino IDE** (Label 2).
  - Choose the directory of your Arduino project to be imported (Label 3).
  - To finish import, click on the **Import** button (Label 4).

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/pio-import-config.png"
  figureCount="20"
  width="60%"
  caption="Configure Import parameters"
/>

4. On the Trust author window, click **Yes**.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/pio-trust.png"
  figureCount="21"
  width="50%"
  caption="Trust author window"
/>

Now, your project is imported successfully.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/imported_rak5811.png"
  figureCount="22"
  width="100%"
  caption="Imported Arduino project"
/>

On the imported project, check the **platformio.ini** file:

The parameter **libs_extra_dirs** is your Arduino library directory.
In case of upload error, add the parameter **upload_port**.

```c
[env:rak11300]
platform = raspberrypi
board = rak11300
framework = arduino
lib_extra_dirs = ~/Documents/Arduino/libraries
upload_port = COM8
```

If your project is running on Windows, use the Device Manager program to find correct the COM port allocated.

<RkImage
  src="https://images.docs.rakwireless.com/wisblock/rak5811/quickstart/dev_manager_rak11300.png"
  figureCount="23"
  width="70%"
  caption="Windows Device Manager Ports (COM & LPT)"
/>

#### Code Explanation RAK4631 Example

##### 1.1 Initializes WisBlock RAK5811 Module
- Enable booster

```c
/* WisBLOCK 5811 Power On*/
pinMode(WB_IO1, OUTPUT | PULLUP);
digitalWrite(WB_IO1, HIGH);
```
##### 1.2 Initializes Analog Input Pin and Configure ADC

- The **`analogReference`** function configure the reference voltage used for analog input. The reference voltage is the value used as the top of the input range.
- The **`analogOversampling`** is a method to achieve a higher resolution without using an external ADC.

```c{2,3}
pinMode(WB_A1, INPUT_PULLDOWN);
analogReference(AR_INTERNAL_3_0);
analogOversampling(128);
```
##### 1.3 Get ADC Samples
- At the end of sampling, the sketch calculates the average ADC.
```c
for (i = 0; i < NO_OF_SAMPLES; i++)
{
    mcu_ain_raw += analogRead(WB_A1);
}
average_raw = mcu_ain_raw / i;
```
##### 1.4 Process ADC Samples

- Calculate raw voltage based on ADC reference and resolution
- Reduce input signal to 6/10

```c
mcu_ain_voltage = average_raw * 3.0 / 1024;   // ref 3.0V / 10bit ADC

voltage_sensor = mcu_ain_voltage / 0.6;     // WisBlock RAK5811 (0 ~ 5V).   Input signal reduced to 6/10 a

depths = (voltage_sensor * 1000 - 574) * 2.5;   //Convert to millivolt. 574mv is the default output from sensor

Serial.printf("-------average_value------ = %d\n", average_raw);
Serial.printf("-------voltage_sensor------ = %f\n", voltage_sensor);
Serial.printf("-------depths------ = %d mm\n", depths);
```

#### Code Explanation RAK11200 Example

##### 1.1 Initializes WisBlock RAK5811 Module

- Enable booster

```c
  /* WisBLOCK 5811 Power On*/
pinMode(WB_IO1, OUTPUT | PULLUP);
digitalWrite(WB_IO1, HIGH);
```
##### 1.2 Initializes Analog Input and Configure ADC

- The function **`adcAttachPin`** attach a GPIO pin to ADC.
- The function **`analogSetAttenuation`** sets the input attenuation for all ADC pins. The default value is ADC_11db.
- The function **`analogReadResolution`** set the size (bits) of the ADC. The default value is 12-bit resolution.

```c{1,2,3}
adcAttachPin(WB_A1);
analogSetAttenuation(ADC_11db);
analogReadResolution(12);
```
##### 1.3 Get ADC Samples
- At the end of sampling, the sketch calculates the average ADC.
```c
for (i = 0; i < NO_OF_SAMPLES; i++)
{
    adc_raw += analogRead(sensor_pin);
}
average_adc_raw = adc_raw / NO_OF_SAMPLES;
```


##### 1.4 Process ADC Samples

- The function **`esp_adc_cal_raw_to_voltage(average_adc_raw)`** convert adc_raw value to voltage in mV.

```c{1}
voltage_mcu_ain = esp_adc_cal_raw_to_voltage(average_adc_raw);
voltage_sensor = voltage_mcu_ain / 0.6;   //WisBlock RAK5811 (0 ~ 5V). Input signal reduced to 6/10 and output
depths = (voltage_sensor * 1000 - 574) * 2.5; //Convert to millivolt. 574mv is the default V output from sensor
```

:::warning
ADC measurements will be noisier while WiFi is on, often due to poor power and/or signal filtering.
:::

##### 1.5 ADC Calibration API
Espressif provides a library (API) for ADC calibration that uses tables for comparison. You can find more details about ESP32 [ADC calibration](https://docs.espressif.com/projects/esp-idf/en/v5.1/esp32/api-reference/peripherals/adc_calibration.html) on Espressif ADC API.


<RkBottomNav/>