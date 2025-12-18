

# BLE Configuration

## Prerequisite

Before compiling the **RUI3 BLE Examples**, you must check the procedures described in the Prerequisite section of [RAK4631-R QuickStart Guide](https://docs.rakwireless.com/product-categories/wisblock/rak4631-r/quickstart/#prerequisite).
You will also need to install and configure the Arduino IDE, as described in the RAK4631-R [Software](https://docs.rakwireless.com/product-categories/wisblock/rak4631-r/quickstart/#software) section.

## Loading the Example

The project is available on Arduino IDE **RAK WisBlock RUI Examples**.

1. Launch Arduino IDE then go to: **File** -> **Examples** -> **RAK WisBlock RUI examples** -> **Example** -> **BLE_Configuration**.
 

> **Image:** RAK WisBlock RUI BLE configuration example

2. Once the example code is open, you can now select the correct serial port, as shown in **Figure 2**.

> **Image:** Selecting the correct serial port

3. The last step is to upload the code by clicking the highlighted **Upload** icon.

> **Image:** Uploading the BLE_Configuration example code

4. You should now be able to see the project logs on the serial monitor of Arduino IDE.

> **Image:** Serial monitor BLE_Configuration log

## Example details

This sketch shows [RUI3 BLE API](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/ble/) configuration parameters that can be used in your RUI3 project.

## Configurable Parameters

## Start BLE UART Service

Start the [BLE UART Service](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/#start) using BLE API.

```c
api.ble.uart.start();
```
### Advertise Status

Get the current [Advertise Status](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/#status) using BLE API.

```c
get_dav_status = api.ble.advertise.status();
```

### Set Tx Power Level

Set the [Tx Power Level](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/#set). The code below sets the Tx Power to 8 dBm.

```c
get_dav_status = api.ble.settings.txPower.set(8);
```

### Set BLE Broadcast Name

Set the [Broadcast Name](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/#set-3). The code below sets the Broadcast Name to **RAKBLE-4631**.

```c
char dev_name[12] = { 'R', 'A', 'K', 'B', 'L', 'E', '-', '4', '6', '3', '1', '\0' };

  if (!(ret = api.ble.settings.broadcastName.set(dev_name, 12))) {
      Serial.printf("BLE Configuration - set broadcast name is incorrect! \r\n");
      return;
  }
```
### Start the BLE Advertising

Configure the [BLE Advertising](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/#start-2) timeout.

```c
if (!(ret = api.ble.advertise.start(60))) {
      Serial.printf("BLE Configuration - set start advertise parameter is incorrect! \r\n");
    return;
}
```
### Get the BLE Advertising Interval

Get the current [advertising interval](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/ble/#get-3) in milliseconds.

```c
int32_t get_adv_interval = api.ble.settings.advertiseInterval.get();
```

### Get Device MAC Address

Get the current [MAC Address](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/ble/#get) position 2.
```c
char *get_position_2_mac_addr = api.ble.mac.get(2);
```

## Scanning BLE Advertising Packets

You can check the BLE packets sent by the `BLE_Configuration` project using the [nRF Connect for Mobile](https://www.nordicsemi.com/Products/Development-tools/nrf-connect-for-mobile) tool.

> **Image:** nRF Connect for Mobile tool scan

