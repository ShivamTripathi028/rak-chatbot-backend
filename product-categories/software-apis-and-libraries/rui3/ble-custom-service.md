

# BLE Custom Service

## Prerequisite

Before compiling the **RUI3 BLE Examples**, you must check the procedures described in the Prerequisite section of [RAK4631-R QuickStart Guide](https://docs.rakwireless.com/product-categories/wisblock/rak4631-r/quickstart/#prerequisite).
You will also need to install and configure the Arduino IDE, as described in the RAK4631-R [Software](https://docs.rakwireless.com/product-categories/wisblock/rak4631-r/quickstart/#software) section.

## Loading the Example

The project is available on Arduino IDE **RAK WisBlock RUI examples**.

1. Launch Arduino IDE then go to: **File** -> **Examples** -> **RAK WisBlock RUI examples** -> **Example** -> **BLE_BLE_Custom_Service**.

> **Image:** RAK WisBlock RUI BLE Custom Service example

2. Once the example code is open, you can now select the correct serial port, as shown in **Figure 2**.

> **Image:** Selecting the correct serial port

3. The last step is to upload the code by clicking the highlighted **Upload** icon.

> **Image:** Uploading the BLE Custom Service example code

## Example Details

This sketch creates a custom BLE service with two Characteristics:

- Notify Characteristic. The notification can be enabled or disabled.
- Read Characteristic.

### Initializes BLE Custom Services

RUI3 API to initialize [custom](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/#init) BLE Services:

```c
api.ble.custom.init();
```
### Create BLE Service

[BLE Service](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/#rakbleservice-2) API.

```c
RAKBleService hrms = RAKBleService(base_uuid);
```
### Create BLE Characteristic

[BLE Characteristic](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/#rakblecharacteristic-2) API.

```c
RAKBleCharacteristic hrmc = RAKBleCharacteristic(UUID16_CHR_HEART_RATE_MEASUREMENT);
RAKBleCharacteristic bslc = RAKBleCharacteristic(UUID16_CHR_BODY_SENSOR_LOCATION);
```

Methods for Characteristic:

```c
  hrmc.setProperties(RAK_CHR_PROPS_NOTIFY);
  hrmc.setPermission(RAK_SET_OPEN);
  hrmc.setFixedLen(2);  
```
### Register Callback

Register a [callback](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/#setcccdwritecallback) API.

```c
hrmc.setCccdWriteCallback(cccd_callback);  
```
On function `cccd_callback` you need to check the `chars_uuid`parameter and use the pointer `*cccd_value` to read the values.

```c
// You should create your own RAKBleCharacteristic instance to use this API.
RAKBleCharacteristic hrmc = RAKBleCharacteristic(YOUR_UUID);

void cccd_callback(uint16_t chars_uuid, uint8_t * cccd_value)
{
  // process YOUR_UUID 
  if (chars_uuid ==  YOUR_UUID) {
 
      // get cccd_value
      String cccd_value1 = String(cccd_value[0], HEX);
  }

}
```

### Arduino Serial Monitor Log

> **Image:** BLE Custom Service log

