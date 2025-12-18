---
title: RAK811 WisDuo Breakout Board AT Command Manual
description: For an easier experience with your LoRaWAN Module, a comprehensive list of commands for the LoRa P2P and LoRaWAN communication is provided. A serial communication interface is also presented for the two-way communication of the RAK811 Breakout Board.
image: "https://images.docs.rakwireless.com/wisduo/rak811-breakout-board/rak811-breakout.png"
keywords:
    - RAK811 Breakout Board
    - wisduo
    - At Command Manual
sidebar_label: AT Command Manual
slug: /product-categories/wisduo/rak811-breakout-board/at-command-manual/
download: true
---

# RAK811 Breakout Board AT Command Manual

## Introduction

The RAK811 Breakout Board is designed to simplify LoRaWAN and LoRa Point-to-Point (P2P) communication. It provides easy integration of LoRa technology into your projects using AT commands via a UART communication interface.

These AT commands allow you to configure parameters for LoRa P2P and LoRaWAN communication, control the available GPIO pins, and manage the analog input of the RAK811. Additionally, any microcontroller with a UART interface can be used to control the RAK811 Breakout Board.

The UART serial communication is available on the **UART1 port** via **Pin 6 (TX1)** and **Pin 7 (RX1)**. The default UART1 communication settings are **115200 / 8-N-1**, and firmware upgrades can also be performed through this port. For details about the pin distribution and a schematic of a reference application, refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak811-breakout-board/datasheet/" target="_blank">RAK811 Breakout Board Datasheet</a>. A complete description of the RAK811 Breakout Board's pins can be found in <a href="https://docs.rakwireless.com/product-categories/wisduo/rak811-breakout-board/at-command-manual/#appendix-iv-pin-description-of-rak811-breakout-board" target="_blank">Appendix IV</a>.

The RAK811 Breakout Board also supports a secondary serial port, **UART3**, accessible through **Pin 25 (TX3)** and **Pin 26 (RX3)**. Like UART1, UART3 operates with default parameters of **115200 / 8-N-1** and can serve as an alternative for sending AT commands. Additionally, UART3 can be utilized for developing custom firmware using <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui/" target="_blank">RUI</a>.

Note that **UART3 pins are not exposed on the RAK811 Breakout Module**. To access these pins, you will need to use the RAK811 Breakout Board or the RAK811 Evaluation Board.

For AT commands example usage, refer to these sections of the Quick Start Guide:

- <a href="https://docs.rakwireless.com/product-categories/wisduo/rak811-breakout-board/quickstart/#connecting-to-the-things-stack-ttn-v3" target="_blank">TTN OTAA/ABP</a>
- <a href="https://docs.rakwireless.com/product-categories/wisduo/rak811-breakout-board/quickstart/#connecting-to-chirpstack" target="_blank">ChirpStack OTAA/ABP</a>
- <a href="https://docs.rakwireless.com/product-categories/wisduo/rak811-breakout-board/quickstart/#lora-p2p-mode" target="_blank">LoRa P2P</a>

## AT Command Syntax

AT commands are based on ASCII characters. Each command begins with the prefix `AT` or `at` and ends with `<CR><LF>` (i.e., `\r\n`). The maximum length of an AT command is **255 characters**, including the `<CR><LF>` at the end. For clarity, the `\r\n` suffix is omitted throughout the rest of the document.

The AT commands can be classified into the following groups:

- **Read Command**: Used to retrieve the current configuration or status of the module. The command name and parameter list are separated by the `=` character, while the `<m>` parameter and its associated value `<n>` are separated by the `:` character.

```
at+get_config=<m>:<n>
```

- **Write Command**: Used to write or modify the module's current configuration. The command name and parameter list are separated by the `=` character, while the `<m>` parameter and its associated value `<n>` are separated by the `:` character.

```
at+set_config=<m>:<n>
```

- **Operational Command**: Commands used to execute specific actions rather than reading or writing configurations.

```
at+send=lora:<m>:<n> // Sends data through the LoRa transceiver.
```

- **Special Command**: The RAK811 UART port operates in two modes: **Configuration Mode** (default) and **Data Transmission Mode**. In Data Transmission Mode, ASCII payloads can be sent directly to the network server via UART without using the AT Command interface, such as `at+send=lora:X:YYY`. For more details, refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak811-breakout-board/at-command-manual/#interface-type-at-command" target="_blank">Interface Type AT Command</a> section of this document.

:::tip NOTE
To enable Data Transmission Mode, use the command: `at+set_config=device:uart_mode:<index>:<mode>`. To switch back to Configuration Mode (default AT Command mode), input `+++`. Note that the `+++` command does not include terminators such as `\r` or `\n`.
:::

After the command is executed by the module, a reply is sent back to the external MCU. If the command is successful, the usual reply has the following format:

```
OK [information]\r\n
```

:::tip NOTE

Only Read Commands provide information in the reply message, whereas Write Commands do not include an informative description in their responses.

:::

The firmware developed running in the external MCU will expect at a minimum string of `Ok\r\n` after sending a successful command to the board. On the other hand, when the command is not successfully executed by the board, you will receive a response in the following format:

```
ERROR: [ErrCode]\r\n
```

## Error Code Table

| Error Code | Description                                                                                                                                                                 |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1          | The last command received is an unsupported AT command.                                                                                                                     |
| 2          | Invalid parameter in the AT command.                                                                                                                                        |
| 3          | There is an error when reading or writing the flash memory.                                                                                                                 |
| 4          | There is an error when reading or writing through the IIC bus.                                                                                                                  |
| 5          | There is an error when sending data through the UART port. Check if you exceed 256 bytes UART buffer.                                                                                                                  |
| 80         | The LoRa transceiver is busy, could not process a new command.                                                                                                              |
| 81         | LoRa service is unknown. Unknown MAC command received by the node. Execute commands that are not supported in the current state, such as sending the `at+join` command in P2P mode. |
| 82         | The LoRa parameters are invalid.                                                                                                                                            |
| 83         | The LoRa parameters are invalid.                                                                                                                                            |
| 84         | The LoRa data rate (DR) is invalid.                                                                                                                                         |
| 85         | The LoRa frequency and data rate are invalid.                                                                                                                               |
| 86         | The device has not joined into a LoRa network.                                                                                                                              |
| 87         | The length of the packet exceeded the maximum allowed by the LoRa protocol.                                                                                                 |
| 88         | Service is closed by the server. Due to the limitation of duty cycle, the server will send the "SRV_MAC_DUTY_CYCLE_REQ" MAC command to close the service.                      |
| 89         | This is an unsupported region code.                                                                                                                                         |
| 90         | The duty cycle is restricted, preventing data transmission at this time. Data can only be sent once the time limit is lifted.                                                              |
| 91         | No valid LoRa channel could be found.                                                                                                                                       |
| 92         | No available LoRa channel could be found.                                                                                                                                   |
| 93         | The status indicates an error, which typically signifies that the internal state of the protocol stack is incorrect.                                                                                              |
| 94         | Time out reached while sending the packet through the LoRa transceiver.                                                                                                     |
| 95         | Time out reached while waiting for a packet in the LoRa RX1 window.                                                                                                         |
| 96         | Time out reached while waiting for a packet in the LoRa RX2 window.                                                                                                         |
| 97         | There is an error while receiving a packet during the LoRa RX1 window.                                                                                                      |
| 98         | There is an error while receiving a packet during the LoRa RX2 window.                                                                                                      |
| 99         | Failed to join into a LoRa network.                                                                                                                                         |
| 100        | A duplicate downlink message has been detected, indicating that a message with an invalid downlink count was received.                                                                              |
| 101        | Payload size is not valid for the current data rate (DR).                                                                                                                   |
| 102        | Many downlink packets are lost.                                                                                                                                             |
| 103        | Address fail. The address of the received packet does not match the address of the current node.                                                                            |
| 104        | Invalid MIC is detected in the LoRa message.                                                                                                                                |

## General AT Command

1. ** at+version **

This command is used to get the current firmware version number.

| Operation | Command      | Response              |
| --------- | ------------ | --------------------- |
| Read      | `at+version` | `OK <version number>` |

**Parameter**: NONE

**Example**:

```
at+version\r\n
OK V3.0.0.14.H
```

2. ** at+help **

This command is used to obtain all the AT commands supported by the current firmware.

| Operation | Command   | Response               |
| --------- | --------- | ---------------------- |
| Read      | `at+help` | `OK <all AT commands>` |

**Parameter**: NONE

**Example**:

```
at+help\r\n

OK Device AT commands:

  at+version
  at+help
  at+set_config=device:restart
  at+set_config=device:sleep:X
  at+get_config=device:status
  at+set_config=device:uart:X:Y
  at+set_config=device:uart_mode:X:Y
  at+send=uart:X:YYY
  at+set_config=device:gpio:X:Y
  at+get_config=device:gpio:X
  at+get_config=device:adc:X

LoRaWAN AT commands:

  at+set_config=lora:default_parameters
  at+join
  at+send=lora:X:YYY
  at+set_config=lora:region:XXX
  at+get_config=lora:channel
  at+set_config=lora:dev_eui:XXXX
  at+set_config=lora:app_eui:XXXX
  at+set_config=lora:app_key:XXXX
  at+set_config=lora:dev_addr:XXXX
  at+set_config=lora:apps_key:XXXX
  at+set_config=lora:nwks_key:XXXX
  at+set_config=lora:multicastenable:X
  at+set_config=lora:multicast_dev_addr:XXXX
  at+set_config=lora:multicast_apps_key:XXXX
  at+set_config=lora:multicast_nwks_key:XXXX
  at+set_config=lora:join_mode:X
  at+set_config=lora:work_mode:X
  at+set_config=lora:ch_mask:X:Y
  at+set_config=lora:class:X
  at+set_config=lora:confirm:X
  at+set_config=lora:dr:X
  at+set_config=lora:tx_power:X
  at+set_config=lora:adr:X
  at+get_config=lora:status
  at+set_config=lora:dutycycle_enable:X
  at+set_config=lora:send_repeat_cnt:X

LoRaP2P AT commands:

  at+set_config=lorap2p:XXX:Y:Z:A:B:C
  at+set_config=lorap2p:transfer_mode:X
  at+send=lorap2p:XXX
```

3. **at+set_config=device:restart**

This command is used to restart the device.

| Operation | Command                        | Response |
| --------- | ------------------------------ | -------- |
| Read      | `at+set_config=device:restart` |          |

**Parameter**: NONE

**Example**:

```
at+set_config=device:restart

LoRa (R) is a registered trademark or service mark of Semtech Corporation or its affiliates. LoRaWAN (R) is a licensed mark.

RAK811 Version:3.0.0.14.H
UART1 work mode: RUI_UART_NORMAL, 9600, N81
UART3 work mode: RUI_UART_NORMAL, 115200, N81
LoRa work mode: P2P
LoRa P2P Transfer_mode: Sender
Initialization OK
```

4. **at+set_config=device:sleep:`<status>`**

This command is used to change the current state of the device between the sleep and the wake-up mode.

| Operation | Command                               | Response     |
| --------- | ------------------------------------- | ------------ |
| Write     | `at+set_config=device:sleep:<status>` | `OK<STATUS>` |

**Parameter**:

| Status | 0: wake up1: sleep |
| --- | --- |

**Example**:

```
at+set_config=device:sleep:1\r\n
OK Sleep

at+set_config=device:sleep:0\r\n
OK Wake Up
```

:::tip NOTE

During sleep mode, **Pin 7 (RX1)** and **Pin 26 (RX3)** are automatically configured as wake-up pins in external interrupt mode with an internal pull-down resistor. Wake-up is triggered by a rising edge on these RX pins.

:::

5. **at+get_config=device:status**

This command is used to obtain the current status of the device.

| Operation | Command                       | Response          |
| --------- | ----------------------------- | ----------------- |
| Read      | `at+get_config=device:status` | `OK<information>` |

**Parameter**: None

**Example**:

```
at+get_config=device:status\r\n
OK Board Core:RAK811
MCU:STM32L151CBU6A
LoRa chip:SX1276
```

## Interface Type AT Command

1. **at+set_config=device:uart:`<index>:<baud_rate>`**

This command is used to configure the baud rate for a UART port.

:::tip NOTE
No reply will be received after executing this configuration if a different baud rate is set. To restore UART serial communication, adjust the UART baud rate setting in the Serial Port Tool to match the newly configured baud rate.
:::

| Operation | Command                                         | Response |
| --------- | ----------------------------------------------- | -------- |
| Write     | `at+set_config=device:uart:<index>:<baud_rate>` | `OK`     |

**Parameter**:

| index | UART Number: 1 or 3. Two UART ports are currently supported starting FW V3.0.0.14.H - UART1 and UART3 |
| --- | --- |
| baud_rate | UART Baud rate：1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200 |

**Example**:

```
at+set_config=device:uart:1:115200\r\n
```

2. **at+set_config=device:uart_mode:`<index>:<mode>`**

This command is used to set the UART operation from AT **configuration mode** to **data transmission mode**.

In **Data Transmission Mode**, standard AT Commands are disabled, and any data sent to UART is transmitted directly to the network server as an ASCII payload with `\r\n`. For example, if you input `AZ`, the network server will receive an uplink hex value of `415A0D0A`, where **A**=`0x41`, **Z**=`0x5A`, **\r**=`0x0D`, and **\n**=`0x0A`.

:::tip NOTE

To switch back from data transmission mode to configuration mode, use `+++` (`+++` without `\ r\ n`).

:::

| Operation | Command                                         | Response |
| --------- | ----------------------------------------------- | -------- |
| Write     | `at+set_config=device:uart_mode:<index>:<mode>` | `OK`     |

**Parameter**:

| index | UART Number: 1 or 3. Two UART ports are currently supported starting FW V3.0.0.14.H - UART1 and UART3 |
|-------|-------------------------------------------------------------------------------------------------------|
| mode  | UART Mode： Only 1 can be selected, which means the UART is set to data transmission mode             |

**Example**:

```
at+set_config=device:uart_mode:1:1\r\n
OK

+++
OK
```

3. **at+send=uart:`<index>:<data>`**

This command is used for sending data over a UART port.

| Operation | Command                       | Response |
| --------- | ----------------------------- | -------- |
| Write     | `at+send=uart:<index>:<data>` | `OK`     |

**Parameter**:

| index | UART Number: 1 or 3. Two UART ports are currently supported starting FW V3.0.0.14.H - UART1 and UART3 |
| --- | --- |
| mode | The data to be sent can have a maximum length of **250 characters**, which is equivalent to 255 minus the length of the `at+...` command and the `\r\n` terminators. |

**Example**:

```
at+send=uart:1:12345\r\n
OK
```

4. **at+get_config=device:gpio:`<pin_num>`**

This command is used to obtain the voltage level status of a pin on a module.
| Operation | Command                               | Response     |
| --------- | ------------------------------------- | ------------ |
| Read      | `at+get_config=device:gpio:<pin_num>` | `OK<status>` |

**Parameter**:

| pin_num | Pin index of the module(GPIO pins available on this Breakout board are Pin 2, Pin 3, Pin 4, Pin 5, Pin 8, Pin 9, Pin 14, Pin 15, Pin 16, Pin 20, Pin 22, and Pin 23 of the RAK811 module) |
| --- | --- |
| status（Return Value） | 0: Low Voltage Level1: High Voltage Level |

> **Image:** GPIO Pinout Mapping for RAK811 Breakout Board

**Example**:

```
at+get_config=device:gpio:2\r\n
OK 1
```

5. **at+set_config=device:gpio:`<pin_num>:<status>`**

This command is used to set the voltage level state (high or low) of a pin on a board.

| Operation | Command                                        | Response |
| --------- | ---------------------------------------------- | -------- |
| Write     | `at+set_config=device:gpio:<pin_num>:<status>` | `OK`     |

**Parameter**:

|  pin_num  |  Pin index of the module  (GPIO pins available on this Breakout board are Pin 2, Pin 3, Pin 4, Pin 5, Pin 8, Pin 9, Pin 14, Pin 15, Pin 16, Pin 20, Pin 22, and Pin 23 of the RAK811 module)  |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  status   |  0: Low Voltage Level 
 1: High Voltage Level                                                                                                                                                                               |

**Example**:

```
at+set_config=device:gpio:2:0\r\n
OK
```

6. **at+get_config=device:adc:```<pin_num>```**

This command is used to obtain the voltage level of an ADC pin of the board.

| Operation | Command                              | Response      |
| --------- | ------------------------------------ | ------------- |
| Read      | `at+get_config=device:adc:<pin_num>` | `OK<voltage>` |

**Parameter**:

| pin_num | ADC pin index of the module(ADC pins available on this Breakout board are different between high and low-frequency modules.- For low-frequency modules, the ADC pins are Pin 2, Pin 3, Pin 4, Pin 5, Pin 15, Pin 20, Pin 22, and Pin 23- For high-frequency modules, the ADC pins are in 2, Pin 3, Pin 4, Pin 20, Pin 22, and Pin 23) |
| --- | --- |
| Voltage（Return Value） | Voltage，Unit:mV |

> **Image:** ADC Pinout of the RAK811 Breakout board on Low-frequency modules

> **Image:** ADC Pinout of the RAK811 Breakout board on High-frequency modules

**Example**:

```
at+get_config=device:adc:2\r\n
OK 1663mV
```

## LoRaWAN Type AT Command

1. **at+join**

This command is used to join a LoRaWAN network.

| Operation | Command   | Response          |
| --------- | --------- | ----------------- |
|           | `at+join` | `OK Join Success` |

**Parameter**: NONE

**Example**:

```
at+join\r\n
OK Join Success
```

2. **at+send=lora:`<port>:<data>`**

This command is used to send data via LoRaWAN.

| Operation | Command                      | Response |
| --------- | ---------------------------- | -------- |
|           | `at+send=lora:<port>:<data>` | `OK `    |

**Parameter**:

| port | The sending port for LoRa ranges from **1 to 223**. |
| --- | --- |
| data | The sending data format is in hexadecimal format. The possible values are between00-FF. The module will internally cast every two characters into a byte before sending it to the LoRa transceiver. The maximum length varies depending on the band frequency and DR (LoRaWAN standard). Refer toAppendix III. |

**Example**:

When sending data as unconfirmed uplink:

```
at+send=lora:1:5A00\r\n
OK
```

When sending data as confirmed uplink:

```
at+send=lora:1:5A00\r\n
OK
at+recv=0,-105,-12,0
```

:::tip NOTE

When sending a confirmed message, you will receive an ACK response, i.e. `at+recv=...`.
The `0, -105, -12,0` stands for:
  * `0`: For the LoRa port;
  * `-105`: For the RSSI;
  * `-12`: For the SNR;
  * `0`: For the length of the data (no valid data in ACK).
:::

3. **at+set_config=lora:region:`<region>`**

This command is used for setting the appropriate working frequency band.

| Operation | Command                              | Response |
| --------- | ------------------------------------ | -------- |
| Write     | `at+set_config=lora:region:<region>` | `OK `    |

**Parameter**:

| region | EU433, CN470, IN865, EU868, US915, AU915, KR920, AS923. The default is EU868. |
| --- | --- |

**Example**:

```
at+set_config=lora:region:EU868\r\n
OK
```

:::tip NOTE
In the AS923 frequency band, the supported frequency plan is "as2" and dwell is set to 1.
:::

4. **at+get_config=lora:channel**

This command is used to read all the LoRa channel information given the current region configured on the board.

| Operation | Command                      | Response                   |
| --------- | ---------------------------- | -------------------------- |
| Read      | `at+get_config=lora:channel` | `OK <channel information>` |

**Parameter**: NONE

**Example**: EU868 region

```
at+get_config=lora:channel\r\n
OK *0,on,868100000,0,5; *1,on,868300000,0,5; *2,on,868500000,0,5; 3,off,0,0,0; 4,off,0,0,0; 5,off,0,0,0; 6,off,0,0,0; 7,off,0,0,0; *8,on,867100000,0,5; *9,on,867300000,0,5; *10,on,867500000,0,5; *11,on,867700000,0,5; *12,on,867900000,0,5; 13,off,0,0,0; 14,off,0,0,0; 15,off,0,0,0
```

:::tip NOTE

With "***0,on,868100000,0,5**" as an example，the following is the channel parameter analysis:

- `*` at the beginning, if the channel is open;
- `0` is the channel ID;
- `on` indicates the current status of the channel;
- `868100000` is the actual frequency of the channel，unit is Hz;
- `0,5` indicates the DR of the channel, DR0~DR5.

:::

5. **at+set_config=lora:ch_mask:`<channel_number>:<status>`**

This command is used for switching a channel (turn on or off) in the current region.

| Operation | Command                                                | Response |
| --------- | ------------------------------------------------------ | -------- |
| Write     | `at+set_config=lora:ch_mask:<channel_number>:<status>` | `OK `    |

**Parameter**:

| channel_number | Channel number |
| --- | --- |
| status | 0: off1: on |

**Example**:

```
at+set_config=lora:ch_mask:0:0\r\n
OK
```

6. **at+set_config=lora:dev_eui:`<dev_eui>`**

This command is used to set the Device EUI parameter for the LoRaWAN OTAA mode.

| Operation | Command                                | Response |
| --------- | -------------------------------------- | -------- |
| Write     | `at+set_config=lora:dev_eui:<dev_eui>` | `OK `    |

**Parameter**:

| dev_eui | Device EUI |
| --- | --- |

**Example**:

```
at+set_config=lora:dev_eui:3530353064377716\r\n
OK
```

7. **at+set_config=lora:app_eui:`<app_eui>`**

This command is used to set the Application EUI parameter for the LoRaWAN OTAA mode.

| Operation | Command                                | Response |
| --------- | -------------------------------------- | -------- |
| Write     | `at+set_config=lora:app_eui:<app_eui>` | `OK `    |

**Parameter**:

| app_eui | Application EUI |
| --- | --- |

:::tip NOTE
All zero value Application EUI `at+set_config=lora:app_eui:0000000000000000` is **not supported** and will return error.
:::

**Example**:

```
at+set_config=lora:app_eui:0000000000000001\r\n
OK
```

8. **at+set_config=lora:app_key:`<app_key>`**

This command is used to set the Application Key parameter for the LoRaWAN OTAA mode.

| Operation | Command                                | Response |
| --------- | -------------------------------------- | -------- |
| Write     | `at+set_config=lora:app_key:<app_key>` | `OK `    |

**Parameter**:

| app_key | Application Key |
| --- | --- |

**Example**:

```
at+set_config=lora:app_key:841986913ACD00BBC2BE2479D70F3228\r\n
OK
```

9. **at+set_config=lora:dev_addr:`<dev_addr>`**

This command is used to set the Device Address parameter for the LoRaWAN ABP mode.

| Operation | Command                                  | Response |
| --------- | ---------------------------------------- | -------- |
| Write     | `at+set_config=lora:dev_addr:<dev_addr>` | `OK `    |

**Parameter**:

| dev_addr | Device Address |
| --- | --- |

**Example**:

```
at+set_config=lora:dev_addr:260125D7\r\n
OK
```

10. **at+set_config=lora:apps_key:`<apps_key>`**

This command is used to set the Application Session Key parameter for the LoRaWAN ABP mode.

| Operation | Command                                  | Response |
| --------- | ---------------------------------------- | -------- |
| Write     | `at+set_config=lora:apps_key:<apps_key>` | `OK `    |

**Parameter**:

| apps_key | Application Session Key |
| --- | --- |

**Example**:

```
at+set_config=lora:apps_key:841986913ACD00BBC2BE2479D70F3228\r\n
OK
```

11. **at+set_config=lora:nwks_key:`<nwks_key>`**

This command is used to set the Network Session Key parameter for the LoRaWAN ABP mode.

| Operation | Command                                  | Response |
| --------- | ---------------------------------------- | -------- |
| Read      | `at+set_config=lora:nwks_key:<nwks_key>` | `OK `    |

**Parameter**:

| nwks_key | Network Session Key |
| --- | --- |

**Example**:

```
at+set_config=lora:nwks_key:69AF20AEA26C01B243945A28C9172B42\r\n
OK
```

12. **at+set_config=lora:multicastenable:`<IsEnable>`**

| Operation | Command                                         | Response |
| --------- | ----------------------------------------------- | -------- |
| Write     | `at+set_config=lora:multicastenable:<IsEnable>` | `OK `    |

**Parameter**:

| IsEnable | 0: disable1: enableThe default is disable. |
| --- | --- |

**Example**:

```
at+set_config=lora:multicastenable:1\r\n
OK
```

13. **at+set_config=lora:multicast_dev_addr:`<multicast_dev_addr>`**

This command is used for setting the Device Address for the multicast feature.

| Operation | Command                                                      | Response |
| --------- | ------------------------------------------------------------ | -------- |
| Write     | `at+set_config=lora:multicast_dev_addr:<multicast_dev_addr>` | `OK `    |

**Parameter**:

| multicast_dev_addr | Multicast Device Address |
| --- | --- |

**Example**:

```
at+set_config=lora:multicast_dev_addr:260111fd\r\n
OK
```

14. **at+set_config=lora:multicast_apps_key:`<multicast_apps_key>`**

This command is used to set the Application Session Key for the multicast feature.

| Operation | Command                                                      | Response |
| --------- | ------------------------------------------------------------ | -------- |
| Write     | `at+set_config=lora:multicast_apps_key:<multicast_apps_key>` | `OK `    |

**Parameter**:

| multicast_app_addr | Multicast Application Session Key |
| --- | --- |

**Example**:

```
at+set_config=lora:multicast_apps_key:F13DDFA2619B10411F02F042E1C0F356\r\n
OK
```

15. ** `at+set_config=lora:multicast_nwks_key:<multicast_nwks_key>` **

This command is used to set the Network Session Key for the multicast feature.

| Operation | Command                                                      | Response |
| --------- | ------------------------------------------------------------ | -------- |
| Write     | `at+set_config=lora:multicast_nwks_key:<multicast_nwks_key>` | `OK `    |

**Parameter**:

| multicast_nwks_key | Multicast Network Session Key |
| --- | --- |

**Example**:

```
at+set_config=lora:multicast_nwks_key:1D1991F5377C675879C39B6908D437A6\r\n
OK
```

16. **at+set_config=lora:join_mode:`<mode>`**

This command is used to switch the LoRaWAN access mode between the OTAA and the ABP mode.

| Operation | Command                               | Response |
| --------- | ------------------------------------- | -------- |
| Write     | `at+set_config=lora:join_mode:<mode>` | `OK `    |

**Parameter**:

| mode | Activation mode0: OTAA1: ABPThe default is OTAA. |
| --- | --- |

**Example**:

```
at+set_config=lora:join_mode:1\r\n
OK
```

17. **at+set_config=lora:class:`<class>`**

This command is used to set LoRaWAN class to Class A, Class B, or Class C.

| Operation | Command                            | Response |
| --------- | ---------------------------------- | -------- |
| Write     | `at+set_config=lora:class:<class>` | `OK `    |

**Parameter**:

| class | 0: Class A1: Class B （Not supported at this time）2: Class CThe default is Class A. |
| --- | --- |

**Example**:

```
at+set_config=lora:class:0\r\n
OK
```

18. **at+set_config=lora:confirm:`<type>`**

This command is used for setting the type of messages to be sent: Confirmed/Unconfirmed.

| Operation | Command                             | Response |
| --------- | ----------------------------------- | -------- |
| Write     | `at+set_config=lora:confirm:<type>` | `OK `    |

**Parameter**:

| type | 0: unconfirm type1: confirm typeThe default is unconfirm type. |
| --- | --- |

**Example**:

```
at+set_config=lora:confirm:0\r\n
OK
```

19. **at+set_config=lora:dr:`<dr>`**

This command is used to set the data rate (DR) of LoRa.

| Operation | Command                      | Response |
| --------- | ---------------------------- | -------- |
| Write     | `at+set_config=lora:dr:<dr>` | `OK `    |

**Parameter**:

| dr | The LoRa data rate is region-specific. In most LoRa regions, data rates typically range from **0 to 5**. For detailed information, refer to the LoRaWAN 1.0.2 specification. |
| --- | --- |

20. **at+set_config=lora:tx_power:`<tx_power>`**

This command is used to set the RF transmission power level of the LoRa transceiver.

| Operation | Command                                  | Response |
| --------- | ---------------------------------------- | -------- |
| Write     | `at+set_config=lora:tx_power:<tx_power>` | `OK `    |

**Parameter**:

| tx_power | Refer toAppendix IIfor possible values of tx_power. The table of Appendix II is based on LoRaWAN 1.0.2 specification. LoRa transmit power level varies depending on frequency band.If the resulting TX power is higher than the capability of LoRa Radio, the output power will be based on the max TX power of the LoRa Radio in the module. For RAK811 module, the max TX power is 20dBm. Take note of this when using regional bands with MaxEIRP higher than 20dBm like US915, AU915 and IN865 whose MaxEIRP is 30dBm.The default setting is 0. |
| --- | --- |

**Example**:

```
at+set_config=lora:tx_power:0\r\n
OK
```

21. **at+set_config=lora:adr:`<status>`**

This command is used to turn on/off the ADR feature of the LoRa communication.

| Operation | Command                           | Response |
| --------- | --------------------------------- | -------- |
| Write     | `at+set_config=lora:adr:<status>` | `OK `    |

**Parameter**:

| status | 0: Turn off1: Turn onThe default is on. |
| --- | --- |

**Example**:

```
at+set_config=lora:adr:0\r\n
OK
```

22. **at+get_config=lora:status**

This command is used to get all the information related to the current LoRa status, except the channel information.

| Operation | Command                     | Response                  |
| --------- | --------------------------- | ------------------------- |
| Read      | `at+get_config=lora:status` | `OK <lora status detail>` |

**Parameter**: NONE

**Example**:

```
at+get_config=lora:status\r\n
OK Work Mode: LoRaWAN
Region: EU868
Send_interval: 600s
Auto send status: false.
MulticastEnable: true.
Multi_Dev_Addr: 260111FD
Multi_Apps_Key: F13DDFA2619B10411F02F042E1C0F356
Multi_Nwks_Key: 1D1991F5377C675879C39B6908D437A6
Join_mode: OTAA
DevEui: 0000000000000888
AppEui: 0000000000000888
AppKey: 00000000000008880000000000000888
Class: C
Joined Network:false
IsConfirm: unconfirm
AdrEnable: true
EnableRepeaterSupport: false
RX2_CHANNEL_FREQUENCY: 869525000, RX2_CHANNEL_DR:0
RX_WINDOW_DURATION: 3000ms
RECEIVE_DELAY_1: 1000ms
RECEIVE_DELAY_2: 2000ms
JOIN_ACCEPT_DELAY_1: 5000ms
JOIN_ACCEPT_DELAY_2: 6000ms
Current Datarate: 4
Primeval Datarate: 4
ChannelsTxPower: 0
UpLinkCounter: 0
DownLinkCounter: 0
```

23. **at+set_config=lora:dutycycle_enable:`<status>`**

This command is used to enable or disable the Duty Cycle feature.

| Operation | Command                                        | Response |
| --------- | ---------------------------------------------- | -------- |
| Write     | `at+set_config=lora:dutycycle_enable:<status>` | `OK `    |

**Parameter**:

| status | 0: disable1: enableThe default is disable. |
| --- | --- |

**Example**:

```
at+set_config=lora:dutycycle_enable:1\r\n
OK
```

24. **at+set_config=lora: send_repeat_cnt:`<num>`**

This command sets the number of retransmission attempts for an uplink message. When enabled, the board will resend a message if the corresponding ACK (downlink) is not received after sending a confirmed uplink message. The default value is **0**, meaning the board will not resend any messages by default.

| Operation | Command                                     | Response |
| --------- | ------------------------------------------- | -------- |
| Write     | `at+set_config=lora: send_repeat_cnt:<num>` | `OK `    |

**Parameter**:

| num | Number of retries, up to 8.The default is 0. |
| --- | --- |

**Example**:

```
at+set_config=lora:send_repeat_cnt:1\r\n
OK
```

25. **at+set_config=lora:default_parameters**

This command is used to restore OTAA, ABP, multicast related network access parameters set at the factory, including dev_eui，app_eui, etc.

| Operation | Command                                 | Response |
| --------- | --------------------------------------- | -------- |
| Write     | `at+set_config=lora:default_parameters` | `OK `    |

**Parameter**: NONE

**Example**:

```
at+set_config=lora:default_parameters\r\n
OK
```

## LoRa P2P Type AT Command

1. **at+set_config=lora:work_mode:`<mode>`**

This command is used to switch the LoRa operating mode between **LoRaWAN** and **LoRa P2P** modes. Executing this command will cause the module to restart.

| Operation | Command                               | Response |
| --------- | ------------------------------------- | -------- |
| Write     | `at+set_config=lora:work_mode:<mode>` |          |

**Parameter**:

| mode | Work mode of LoRa0: LoRaWAN1: LoRa P2PThe default is LoRaWAN mode. |
| --- | --- |

**Example**：

```
at+set_config=lora:work_mode:1\r\n
UART1 work mode: RUI_UART_NORMAL
Current work_mode:P2P
Initialization OK
```

2. **at+set_config=lorap2p:`<frequency>:<spreadfact>:<bandwidth>:<codingrate>:<preamlen>:<power>`**

This command is used to set the relevant parameters of LoRa P2P mode and is only valid when the LoRa mode is switched to LoRa P2P before.

| Operation | Command                                                                                      | Response |
| --------- | -------------------------------------------------------------------------------------------- | -------- |
| Write     | `at+set_config=lorap2p:<frequency>:<spreadfact>:<bandwidth>:<codingrate>:<preamlen>:<power>` | OK       |

**Parameter**:

| frequency | Frequency, the unit is HzThe default is 869525000 Hz. |
| --- | --- |
| spreadfact | Spreading factorThe default is 12. |
| bandwidth | 0: 125 kHz1: 250 kHz2: 500 kHzThe default is 0. |
| codingrate | 1: 4/52: 4/63: 4/74: 4/8The default is 1. |
| preamble | Preamble Length. 5~65535The default is 8. |
| power | TX power. The unit is in dBm. 5~20The default is 20. |

**Example**：

```
at+set_config=lorap2p:869525000:12:0:1:8:20\r\n
OK
```

3. **at+set_config=lorap2p:transfer_mode:`<mode>`**

This command is used to switch the state of the LoRa transceiver between sending and receiving state, and it is only valid when the LoRa mode is set to LoRa P2P before.

| Operation | Command                                       | Response |
| --------- | --------------------------------------------- | -------- |
| Write     | `at+set_config=lorap2p: transfer_mode:<mode>` | OK       |

**Parameter**：

| mode | 1: receiver mode2: sender modeThe default is sender mode. |
| --- | --- |

**Example**：
```
at+set_config=lorap2p:transfer_mode:1\r\n
OK
```

4. **at+send=lorap2p:`<data>`**

This command is used to send data through LoRa P2P and is only valid when the LoRa work mode is set to LoRa P2P before.

| Operation | Command                  | Response |
| --------- | ------------------------ | -------- |
| Send      | `at+send=lorap2p:<data>` | OK       |

**Parameter**：

| data | The data to be sent, and the format is hexadecimal. |
| --- | --- |

**Example**：
```
at+send=lorap2p:1234\r\n
OK
```

In LoRa P2P mode, the receiving node receives the data and outputs the data in the following format:

```
at+recv=<RSSI>,<SNR>,<Data Length>:<Data>
```

## Appendix

### Appendix I: Data Rate by Region

** EU433/EU868/AS923 **

| Data Rate | Configuration             | Indicative Physical Bit Rate [bit/s] |
| --------- | ------------------------- | ------------------------------------ |
| 0         | LoRa: SF12 / 125 kHz | 250                                  |
| 1         | LoRa: SF11 / 125 kHz | 440                                  |
| 2         | LoRa: SF10 / 125 kHz | 980                                  |
| 3         | LoRa: SF9 / 125 kHz  | 1760                                 |
| 4         | LoRa: SF8 / 125 kHz  | 3125                                 |
| 5         | LoRa: SF7 / 125 kHz  | 5470                                 |
| 6         | LoRa: SF7 / 250 kHz  | 11000                                |
| 7         | FSK: 50 kbps         | 50000                                |
| 8 ~ 15    | RFU                       |                                      |

** CN470/KR920 **

| Data Rate | Configuration             | Indicative Physical Bit Rate [bit/s] |
| --------- | ------------------------- | ------------------------------------ |
| 0         | LoRa: SF12 / 125 kHz | 250                                  |
| 1         | LoRa: SF11 / 125 kHz | 440                                  |
| 2         | LoRa: SF10 / 125 kHz | 980                                  |
| 3         | LoRa: SF9 / 125 kHz  | 1760                                 |
| 4         | LoRa: SF8 / 125 kHz  | 3125                                 |
| 5         | LoRa: SF7 / 125 kHz  | 5470                                 |
| 6 ~ 15    | RFU                       |                                      |

** US915 **

| Data Rate | Configuration             | Indicative Physical Bit Rate [bit/s] |
| --------- | ------------------------- | ------------------------------------ |
| 0         | LoRa: SF10 / 125 kHz | 980                                  |
| 1         | LoRa: SF9 / 125 kHz  | 1760                                 |
| 2         | LoRa: SF8 / 125 kHz  | 3125                                 |
| 3         | LoRa: SF7 / 125 kHz  | 5470                                 |
| 4         | LoRa: SF8 / 500 kHz  | 12500                                |
| 5 ~ 7     | RFU                       |                                      |
| 8         | LoRa: SF12 / 500 kHz | 980                                  |
| 9         | LoRa: SF11 / 500 kHz | 1760                                 |
| 10        | LoRa: SF10 / 500 kHz | 3900                                 |
| 11        | LoRa: SF9 / 500 kHz  | 7000                                 |
| 12        | LoRa: SF8 / 500 kHz  | 12500                                |
| 13        | LoRa: SF7 / 500 kHz  | 21900                                |
| 14 ~ 15   | RFU                       |                                      |

** AU915 **

| Data Rate | Configuration             | Indicative Physical Bit Rate [bit/s] |
| --------- | ------------------------- | ------------------------------------ |
| 0         | LoRa: SF12 / 125 kHz | 250                                  |
| 1         | LoRa: SF11 / 125 kHz | 440                                  |
| 2         | LoRa: SF10 / 125 kHz | 980                                  |
| 3         | LoRa: SF9 / 125 kHz  | 1760                                 |
| 4         | LoRa: SF8 / 125 kHz  | 3125                                 |
| 5         | LoRa: SF7 / 125 kHz  | 5470                                 |
| 6         | LoRa: SF8 / 500 kHz  | 12500                                |
| 7         | RFU                       | RFU                                  |
| 8         | LoRa: SF12 / 500 kHz | 980                                  |
| 9         | LoRa: SF11 / 500 kHz | 1760                                 |
| 10        | LoRa: SF10 / 500 kHz | 3900                                 |
| 11        | LoRa: SF9 / 500 kHz  | 7000                                 |
| 12        | LoRa: SF8 / 500 kHz  | 12500                                |

** IN865 **

| Data Rate | Configuration             | Indicative Physical Bit Rate [bit/s] |
| --------- | ------------------------- | ------------------------------------ |
| 0         | LoRa: SF12 / 125 kHz | 250                                  |
| 1         | LoRa: SF11 / 125 kHz | 440                                  |
| 2         | LoRa: SF10 / 125 kHz | 980                                  |
| 3         | LoRa: SF9 / 125 kHz  | 1760                                 |
| 4         | LoRa: SF8 / 125 kHz  | 3125                                 |
| 5         | LoRa: SF7 / 125 kHz  | 5470                                 |
| 6         | RFU                       | RFU                                  |
| 7         | FSK: 50 kbps         | 50000                                |
| 8 ~ 15    | RFU                       | RFU                                  |

### Appendix II: TX Power by Region

** EU868 **

By default, MaxEIRP is considered to be +16 dBm.

| TXPower | Configuration (EIRP) |
| ------- | -------------------- |
| 0       | MaxEIRP              |
| 1       | MaxEIRP - 2 dB  |
| 2       | MaxEIRP - 4 dB  |
| 3       | MaxEIRP - 6 dB  |
| 4       | MaxEIRP - 8 dB  |
| 5       | MaxEIRP - 10 dB |
| 6       | MaxEIRP - 12 dB |
| 7       | MaxEIRP - 14 dB |
| 8 ~ 15  | RFU                  |

** US915 **

By default, MaxEIRP is considered to be +30 dBm based on LoRa Alliance specification.
However, the module's max TX power is only up to 20 dBm.

| TXPower | Configuration (Conducted Power) |
| ------- | ------------------------------- |
| 0       | MaxEIRP                         |
| 1       | MaxEIRP - 2 dB             |
| 2       | MaxEIRP - 4 dB             |
| 3 ~ 9   |                                 |
| 10      | 10 dBm                     |
| 11 ~ 15 | RFU                             |

** AU915 **

By default, MaxEIRP is considered to be +30 dBm based on LoRa Alliance specification.
However, the module's max TX power is only up to 20 dBm.

| TXPower | Configuration (EIRP) |
| ------- | -------------------- |
| 0       | MaxEIRP              |
| 1 ~ 10  | MaxEIRP - 2*TXPower  |
| 11 ~ 10 | RFU                  |

** KR920 **

By default, MaxEIRP is considered to be +14 dBm.

| TXPower | Configuration (EIRP) |
| ------- | -------------------- |
| 0       | MaxEIRP              |
| 1       | MaxEIRP - 2 dB  |
| 2       | MaxEIRP - 4 dB  |
| 3       | MaxEIRP - 6 dB  |
| 4       | MaxEIRP - 8 dB  |
| 5       | MaxEIRP - 10 dB |
| 6       | MaxEIRP - 12 dB |
| 7       | MaxEIRP - 14 dB |
| 8 ~ 15  | RFU                  |

** AS923 **

By default, Max EIRP shall be 16 dBm.

| TXPower | Configuration (EIRP) |
| ------- | -------------------- |
| 0       | MaxEIRP              |
| 1       | MaxEIRP - 2 dB  |
| 2       | MaxEIRP - 4 dB  |
| 3       | MaxEIRP - 6 dB  |
| 4       | MaxEIRP - 8 dB  |
| 5       | MaxEIRP - 10 dB |
| 6       | MaxEIRP - 12 dB |
| 7       | MaxEIRP - 14 dB |
| 8 ~ 15  | RFU                  |

** IN865 **

By default, MaxEIRP is considered to be +30 dBm based on LoRa Alliance specification.
However, the module's max TX power is only up to 20 dBm.

| TXPower | Configuration (EIRP) |
| ------- | -------------------- |
| 0       | MaxEIRP              |
| 1       | MaxEIRP - 2 dB  |
| 2       | MaxEIRP - 4 dB  |
| 3       | MaxEIRP - 6 dB  |
| 4       | MaxEIRP - 8 dB  |
| 5       | MaxEIRP - 10 dB |
| 6       | MaxEIRP - 12 dB |
| 7       | MaxEIRP - 14 dB |
| 8       | MaxEIRP - 16 dB |
| 9       | MaxEIRP - 18 dB |
| 10      | MaxEIRP - 20 dB |
| 11 ~ 15 | RFU                  |

** CN470 **

By default, MaxEIRP is considered to be +19.15 dBm.

| TXPower | Configuration (EIRP) |
| ------- | -------------------- |
| 0       | MaxEIRP              |
| 1       | MaxEIRP - 2 dB  |
| 2       | MaxEIRP - 4 dB  |
| 3       | MaxEIRP - 6 dB  |
| 4       | MaxEIRP - 8 dB  |
| 5       | MaxEIRP - 10 dB |
| 6       | MaxEIRP - 12 dB |
| 7       | MaxEIRP - 14 dB |
| 8 ~ 15  | RFU                  |

** EU433 **

By default, MAxEIRP is considered to be +12.15 dBm.

| TXPower | Configuration (EIRP) |
| ------- | -------------------- |
| 0       | MaxEIRP              |
| 1       | MaxEIRP - 2 dB  |
| 2       | MaxEIRP - 4 dB  |
| 3       | MaxEIRP - 6 dB  |
| 4       | MaxEIRP - 8 dB  |
| 5       | MaxEIRP - 10 dB |
| 6 ~ 15  | RFU                  |

### Appendix III: Maximum Transmission Load by Region

:::tip NOTE
The LoRaWAN stack adds 8 bytes to the user payload. In the following list, M is the maximum payload size and N is the maximum usable payload size for the user data without the MAC header.
::::

** EU868 **

| Data Rate | M           | N           |
| --------- | ----------- | ----------- |
| 0         | 59          | 51          |
| 1         | 59          | 51          |
| 2         | 59          | 51          |
| 3         | 123         | 115         |
| 4         | 250         | 242         |
| 5         | 250         | 242         |
| 6         | 250         | 242         |
| 7         | 250         | 242         |
| 8 ~ 15    | Not Defined | Not Defined |

** US915 **

| Data Rate | M           | N           |
| --------- | ----------- | ----------- |
| 0         | 19          | 11          |
| 1         | 61          | 53          |
| 2         | 133         | 125         |
| 3         | 250         | 242         |
| 4         | 250         | 242         |
| 5 ~ 7     | Not Defined | Not Defined |
| 8         | 61          | 53          |
| 9         | 137         | 129         |
| 10        | 250         | 242         |
| 11        | 250         | 242         |
| 12        | 250         | 242         |
| 13        | 250         | 242         |
| 14 ~ 15   | Not Defined | Not Defined |

** AU915 **

| Data Rate | M           | N           |
| --------- | ----------- | ----------- |
| 0         | 59          | 51          |
| 1         | 59          | 51          |
| 2         | 59          | 51          |
| 3         | 123         | 115         |
| 4         | 250         | 242         |
| 5         | 250         | 242         |
| 6         | 250         | 242         |
| 7         | Not Defined | Not Defined |
| 8         | 61          | 53          |
| 9         | 137         | 129         |
| 10        | 250         | 242         |
| 11        | 250         | 242         |
| 12        | 250         | 242         |
| 13        | 250         | 242         |
| 14 ~ 15   | Not Defined | Not Defined |

** KR920 **

| Data Rate | M           | N           |
| --------- | ----------- | ----------- |
| 0         | 59          | 51          |
| 1         | 59          | 51          |
| 2         | 59          | 51          |
| 3         | 123         | 115         |
| 4         | 250         | 242         |
| 5         | 250         | 242         |
| 6 ~ 15    | Not Defined | Not Defined |

** AS923 **

| Data Rate | Uplink MAC Payload Size (M) | Downlink MAC Payload Size (M) |  |  |
| --- | --- | --- | --- | --- |
|  | UplinkDwellTime = 0 | UplinkDwellTime = 1 | DownlinkDwellTime = 0 | DownlinkDwellTime = 1 |
| 0 | 59 | N/A | 59 | N/A |
| 1 | 59 | N/A | 59 | N/A |
| 2 | 59 | 19 | 59 | 19 |
| 3 | 123 | 61 | 123 | 61 |
| 4 | 250 | 133 | 250 | 133 |
| 5 | 250 | 250 | 250 | 250 |
| 6 | 250 | 250 | 250 | 250 |
| 7 | 250 | 250 | 250 | 250 |
| 8 | RFU | RFU | RFU | RFU |

** IN865 **

| Data Rate | M           | N           |
| --------- | ----------- | ----------- |
| 0         | 59          | 51          |
| 1         | 59          | 51          |
| 2         | 59          | 51          |
| 3         | 123         | 115         |
| 4         | 250         | 242         |
| 5         | 250         | 242         |
| 6         | 250         | 242         |
| 7         | 250         | 242         |
| 8 ~ 15    | Not Defined | Not Defined |

** CN470 **

| Data Rate | M           | N           |
| --------- | ----------- | ----------- |
| 0         | 59          | 51          |
| 1         | 59          | 51          |
| 2         | 59          | 51          |
| 3         | 123         | 115         |
| 4         | 250         | 242         |
| 5         | 250         | 242         |
| 6 ~ 15    | Not Defined | Not Defined |

** EU433 **

| Data Rate | M           | N           |
| --------- | ----------- | ----------- |
| 0         | 59          | 51          |
| 1         | 59          | 51          |
| 2         | 59          | 51          |
| 3         | 123         | 115         |
| 4         | 250         | 242         |
| 5         | 250         | 242         |
| 6         | 250         | 242         |
| 7         | 250         | 242         |
| 8 ~ 15    | Not Defined | Not Defined |

### Appendix IV: Pin Description of RAK811 Breakout Board

The pin definition of the RAK811 Breakout Board can be reviewed in the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak811-breakout-board/datasheet/#pin-definition" target="_blank">Pin Definition</a> section of the Datasheet.

Here is a summary of the pins on the RAK811 Breakout Board:

:::tip NOTE
Not all pins of the RAK811 module are exposed on the RAK811 Breakout board header connectors. Below are the pins available on the RAK811 Module that is on this Breakout board. For complete RAK811 module pinouts information, refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak811-breakout-board/datasheet/#pin-definition" target="_blank">datasheet</a>.
:::

1. **UART Pins**:

     - Pin 7 (RX1) and Pin 6 (TX1) are reserved for UART1.
     - Pin 26 (RX3) and Pin 25 (TX3) are reserved for UART3.
     - During sleep, Pin 7 (RX1) and Pin 26 (RX3) are automatically configured as wake-up pins and in external interrupt mode with internal pull-down resistor. Wake-up will be triggered by a rising edge on these RX pins.

2. **SWD debug Pins**: Pin 10 (SWDIO) and Pin 13 (SWCLK) are used for SWD connection.

3. **Power Pins**: The power pin on the RAK811 module includes the VCC pin on Pin 11, and Ground pins (GND) are on the Pin 1, Pin 12, Pin 21, Pin 28, Pin 29, Pin 30, Pin 31, Pin 32, and Pin 34.

4. **Reset Pin**: The reset pin on the RAK811 module is Pin 24 (RST).

5. **BOOT Pin**: The boot Pin on the RAK811 module is Pin 17 (BOOT0).

6. **RF Antenna Pin**: The RF antenna Pin on the RAK811 module is Pin 33 (RF_OUT).

7. **ADC Pins**: The ADC pins available on the RAK811 are different between the high and low-frequency modules.

  - In the low-frequency modules, the ADC Pins are the following:
    - Pin 2 (PB12)
    - Pin 3 (PB14)
    - Pin 4 (PB15)
    - Pin 5 (PB13)
    - Pin 15 (PA3)
    - Pin 20 (PA2)
    - Pin 22 (PA1)
    - Pin 23 (PA0)

  - In the high-frequency modules, the ADC Pins are the following:
    - Pin 2 (PB12)
    - Pin 3 (PB14)
    - Pin 4 (PB15)
    - Pin 20 (PA2)
    - Pin 22 (PA1)
    - Pin 23 (PA0)

8. **GPIO Pins**: The GPIO pins available on the RAK811 module are the following:
    - Pin 2
    - Pin 3
    - Pin 4
    - Pin 5
    - Pin 8
    - Pin 9
    - Pin 14
    - Pin 15
    - Pin 16
    - Pin 20
    - Pin 22
    - Pin 23

:::tip NOTE

If you plan to use the RAK811 Breakout Board in a product, it is essential to understand how to upgrade its firmware. The firmware can be updated via the **SWD** or **UART1** port, both of which require a general-purpose PC.

:::

