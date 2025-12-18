

# BLE Scanner

## Prerequisite

Before compiling the **RUI3 BLE Examples**, you must check the procedures described in the Prerequisite section of [RAK4631-R QuickStart Guide](https://docs.rakwireless.com/product-categories/wisblock/rak4631-r/quickstart/#prerequisite).
You will also need to install and configure the Arduino IDE, as described in the RAK4631-R [Software](https://docs.rakwireless.com/product-categories/wisblock/rak4631-r/quickstart/#software) section.

## Loading the Example

The project is available on Arduino IDE **RAK WisBlock RUI Examples**.

1. Launch Arduino IDE then go to: **File** -> **Examples** -> **RAK WisBlock RUI examples** -> **Example** -> **BLE_Scanner**. 

> **Image:** RAK WisBlock RUI BLE configuration example

2. Once the example code is open, you can now select the correct serial port, as shown in **Figure 2**.

> **Image:** Selecting the correct serial port

3. The last step is to upload the code by clicking the highlighted **Upload** icon.

> **Image:** Uploading the BLE scanner example code

4. You should now be able to see the project logs on the serial monitor of Arduino IDE.

The log shows details of nearby BLE Devices: **MAC Address**, **RSSI**, and **raw BLE data**.

> **Image:** Serial monitor BLE scan log

## Example Details

This sketch shows how to scan BLE devices using [RUI3 BLE API](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/ble/).

