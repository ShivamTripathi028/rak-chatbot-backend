---
title: RAK4600 WisDuo Breakout Board At Command Manual
description: For an easier experience with your LoRaWAN Module, a comprehensive list of commands for the LoRa P2P and LoRaWAN communication is provided. A serial communication interface is also presented for the two-way communication of the RAK4600 Breakout Board.
image: "https://images.docs.rakwireless.com/wisduo/rak4600-breakout-board/rak4600-breakout.png"
keywords:
    - RAK4600 Breakout Board
    - wisduo
    - AT Command Manual
sidebar_label: AT Command Manual
slug: /product-categories/wisduo/rak4600-breakout-board/at-command-manual/
download: true
---

# RAK4600 Breakout Board AT Command Manual

## Introduction

The RAK4600 Breakout Board simplifies both LoRa P2P peer-to-peer and LoRaWAN communication. Instead of dealing with complex SPI protocols for LoRa transceivers, this board provides a familiar serial communication interface to send commands and check the board's status. This design allows for seamless integration of LoRa technology into your projects.

Through its serial interface, the RAK4600 Breakout Board uses a defined set of AT commands. You can control the board with an external microcontroller as a standard AT modem. These AT commands allow you to configure LoRaWAN communication parameters, control GPIO pins, and manage analog inputs.

In the RAK4600 Breakout Board, the serial communication is available through the **UART1 port**, using J7 connector Pin 1 (USART1_RX) and Pin 2 (USART1_TX). The USART1 communication parameters are set to **115200 / 8-N-1**. You can also perform firmware upgrades through this port. For detailed pin distribution and schematic information, refer to the [RAK4600 Breakout Board Datasheet](https://docs.rakwireless.com/product-categories/wisduo/rak4600-breakout-board/datasheet/).

Additionally, the RAK4600 Breakout Board supports BLE connectivity. You can communicate with the board via BLE interface using your mobile phone or use the board to scan for nearby Bluetooth beacon information. For more details, refer to [Bluetooth Connection Modes](https://docs.rakwireless.com/product-categories/wisduo/rak4600-breakout-board/quickstart/#bluetooth-connection-modes).

## AT Command Syntax

The AT command uses ASCII characters, beginning with the prefix `at` and ending with `<CR><LF>` (i.e. \r\n). Commands have a maximum length of **255 characters**, including the `<CR><LF>` characters at the end. For clarity, the `\r\n` part is omitted in the rest of this document.

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

- **Special Command**: The RAK811 UART port operates in two modes: **Configuration Mode** (default) and **Data Transmission Mode**. In Data Transmission Mode, ASCII payloads can be sent directly to the network server via UART without using the AT Command interface, such as `at+send=lora:X:YYY`. For more details, refer to the [Interface Type AT Command](https://docs.rakwireless.com/product-categories/wisduo/rak4600-breakout-board/at-command-manual/#interface-type-at-command) section of this document.

:::tip NOTE
To enable Data Transmission Mode, use the command: `at+set_config=device:uart_mode:<index>:<mode>`. To switch back to Configuration Mode (default AT Command mode), input `+++`. Note that the `+++` command does not include terminators such as `\r` or `\n`.
:::

After the command is executed by the board, a reply is sent back to the external MCU. In the case the command is successful, the usual reply has the following format:

```
OK [information]\r\n
```

:::tip NOTE
Only Read Commands provide information in the reply message, whereas Write Commands do not include an informative description in their responses.
:::

The firmware developed running in the external MCU will expect at a minimum string of `Ok\r\n` after sending a successful command to the board. On the other hand, when the command is not successfully executed by the board, you will receive a response in the following format:

```
ERROR: [Err Code]\r\n
```
## Error Code Table

| Error Code | Description |
| --- | --- |
| 1 | The last command received is an unsupported AT command. |
| 2 | Invalid parameter in the AT command. |
| 3 | There is an error when reading or writing the flash memory. |
| 5 | There is an error when sending data through the UART port. |
| 41 | The BLE felt into an invalid state, could not apply the command. |
| 80 | The LoRa transceiver is busy, could not process a new command. |
| 81 | The LoRa service is unavailable. The node received an unrecognized MAC command. This error occurs when executing unsupported commands in the current state, such as using the `at+join` command while in P2P mode. |
| 82 | The LoRa parameters are invalid. |
| 83 | The LoRa frequency is invalid. |
| 84 | The LoRa data rate (DR) is invalid. |
| 85 | The LoRa frequency and data rate are invalid. |
| 86 | The device hasn’t joined into a LoRa network. |
| 87 | The length of the packet exceeded the maximum allowed by the LoRa protocol. |
| 88 | The server has closed the service. Due to duty cycle limitations, the server sends a `SRV_MAC_DUTY_CYCLE_REQ` MAC command to terminate the service. |
| 89 | This is an unsupported region code. |
| 90 | Duty cycle is restricted. Due to the duty cycle, data cannot be sent at this time until the time limit is removed. |
| 91 | No valid LoRa channel could be found. |
| 92 | No available LoRa channel could be found. |
| 93 | Internal state error. Generally, the internal state of the protocol stack is incorrect |
| 94 | Time out reached while sending the packet through the LoRa transceiver. |
| 95 | Time out reached while waiting for a packet in the LoRa RX1 window. |
| 96 | Time out reached while waiting for a packet in the LoRa RX2 window. |
| 97 | An error occurred while receiving a packet during the LoRa RX1 window. |
| 98 | An error occurred while receiving a packet during the LoRa RX2 window. |
| 99 | Failed to join into a LoRa network. |
| 100 | Duplicate downlink message is detected. A message with an invalid downlink count is received. |
| 101 | Payload size is not valid for the current data rate (DR). |
| 102 | Many downlink packets are lost. |
| 103 | The address of the received packet does not match the current node's address. |
| 104 | Invalid MIC is detected in the LoRa message. |

## General AT Command

1. **at+version**

This command is used to get the current firmware version number.

| Operation | Command      | Response              |
| --------- | ------------ | --------------------- |
| Read      | `at+version` | `OK <version number>` |

**Parameter**: None

**Example**:
```
at+version\r\n
OK V3.3.0.14
```

2. **at+help**

This command retrieves all the AT commands supported by the current firmware.

| Operation | Command   | Response               |
| --------- | --------- | ---------------------- |
| Read      | `at+help` | `OK <all AT commands>` |

**Parameter**: None

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

LoRa P2P AT commands:
  at+set_config=lorap2p:XXX:Y:Z:A:B:C
  at+set_config=lorap2p:transfer_mode:X
  at+send=lorap2p:XXX

BLE AT commands:
  at+set_config=ble:work_mode:X:Y
```

3. **at+set_config=device:restart**

This command is used to restart the device.

| Operation | Command                        | Response |
| --------- | ------------------------------ | -------- |
| Write     | `at+set_config=device:restart` |          |

**Parameter**: None

**Example**:
```
at+set_config=device:restart\r\n
UART1 work mode: RUI_UART_NORMAL
Current work_mode:LoRaWAN, join_mode:ABP, Class: A
Initialization OK
```

4. **at+set_config=device:sleep:`<status>`**

This command is used to change the current state of the device between the sleep and the wake-up mode.

| Operation | Command                               | Response      |
| --------- | ------------------------------------- | ------------- |
| Write     | `at+set_config=device:sleep:<status>` | `OK <STATUS>` |

**Parameter**:

| status | 0: wake up 1: sleep |
| --- | --- |

**Example**:
```
at+set_config=device:sleep:1\r\n
OK Sleep

at+set_config=device:sleep:0\r\n
OK Wake Up
```

:::tip NOTE

During sleep mode, Pin 22 (USART1_RX) is automatically configured as a wake-up pin with external interrupt mode and an internal pull-down resistor. A rising edge on this RX pin triggers the wake-up.

:::

5. **at+get_config=device:status**

This command retrieves the current status of the device.

| Operation | Command                       | Response           |
| --------- | ----------------------------- | ------------------ |
| Read      | `at+get_config=device:status` | `OK <information>` |

**Parameter**: None

**Example**:
```
at+get_config=device:status\r\n
OK Board Core:RAK4600
MCU:nRF52832
LoRa chip:SX1276
```

## Interface Type AT Command

1. **at+set_config=device:uart:`<index>:<baud_rate>`**

This command is used to configure the baud rate for a UART port.

| Operation | Command                                         | Response |
| --------- | ----------------------------------------------- | -------- |
| Write     | `at+set_config=device:uart:<index>:<baud_rate>` | `OK`     |

**Parameter**：

| index | UART Number |
| --- | --- |
| baud_rate | UART Baud rate: 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200 |

**Example**:

```
at+set_config=device:uart:1:115200\r\n
OK
```

2. **at+set_config=device:uart_mode:`<index>:<mode>`**

This command is used to set the UART operation from AT **configuration mode** to **data transmission mode**.

During **data transmission mode**, standard AT Commands are disabled and all data sent to UART is transmitted directly to the network server as ASCII payload with `\r\n`. For example, if you input `AZ`, the network server receives an uplink hex value of `415A0D0A`, where **A**=`0x41`, **Z**=`0x5A`, **\r**=`0x0D`, and **\n**=`0x0A`.

:::tip NOTE

To switch back from data transmission mode to configuration mode, use `+++` (`+++` without `\ r\ n`).

:::

| Operation | Command                                         | Response |
| --------- | ----------------------------------------------- | -------- |
| Write     | `at+set_config=device:uart_mode:<index>:<mode>` | `OK`     |

**Parameter**:

| index | UART Port Number. Currently, the RAK4600 only supports UART1. |
| --- | --- |
| mode | UART Mode： Only 1 can be selected, which means the UART is set to data transmission mode. |

**Example**:

```
at+set_config=device:uart_mode:1:1\r\n
OK

+++
OK
```

## LoRaWAN Type AT Command

1. **at+join**

This command is used to join a LoRaWAN network.

| Operation | Command   | Response        |
| --------- | --------- | --------------- |
|           | `at+join` | OK Join Success |

**Parameter**: None

**Example**：
```
at+join\r\n
OK Join Success
```

2. **at+send=lora:`<port>:<data>`**

This command is used to send data via LoRaWAN.

| Operation | Command                      | Response |
| --------- | ---------------------------- | -------- |
|           | `at+send=lora:<port>:<data>` | OK       |

**Parameter**：

| port | Sending port of LoRa. The value range is 1-223. |
| --- | --- |
| data | The sending data format is in hexadecimal format. The possible values are between 00-FF . The board internally will cast every two characters into a byte before sending it to the LoRa transceiver. The maximum length varies depending on the band frequency and DR (LoRaWAN standard). Refer to Appendix III . |

**Example**：

When sending data as unconfirmed uplink:
```
at+send=lora:1:5A00\r\n
OK
```
When sending data as confirmed uplink:
```
OK
at+recv=0,-105,-12,0
```

:::tip NOTE

* When sending a confirmed message, you will receive an ACK response, i.e. `at+recv=...`.
The `0, -105, -12,0` stands for:
  * `0`: For the LoRa port;
  * `-105`: For the RSSI;
  * `-12`: For the SNR;
  * `0`: For the length of the data (no valid data in ACK).

* When sending an unconfirmed message, sometimes the gateway will send MAC commands to nodes, and the node will also receive `at+recv=...`.

:::

3. **at+set_config=lora:region:`<region>`**

This command is used to set the appropriate working frequency band.

| Operation | Command                              | Response |
| --------- | ------------------------------------ | -------- |
| Write     | `at+set_config=lora:region:<region>` | OK       |

**Parameter**：

| region | EU433, CN470, IN865, EU868, US915, AU915, KR920, AS923. The default is EU868. |
| --- | --- |

**Example**：
```
at+set_config=lora:region:EU868\r\n
OK
```

:::tip NOTE
In the AS923 frequency band, the supported frequency plan is "as2" and the dwell time is set to 1.
:::

4. **at+get_config=lora:channel**

This command is used to read all the LoRa channel information given the current region configured on the board.

| Operation | Command                      | Response                   |
| --------- | ---------------------------- | -------------------------- |
| Read      | `at+get_config=lora:channel` | `OK <channel information>` |

**Parameter**：None

**Example**：EU868 Region

```
at+get_config=lora:channel\r\n
OK *0,on,868100000,0,5; *1,on,868300000,0,5; *2,on,868500000,0,5; 3,off,0,0,0; 4,off,0,0,0; 5,off,0,0,0; 6,off,0,0,0; 7,off,0,0,0; *8,on,867100000,0,5; *9,on,867300000,0,5; *10,on,867500000,0,5; *11,on,867700000,0,5; *12,on,867900000,0,5; 13,off,0,0,0; 14,off,0,0,0; 15,off,0,0,0

```
:::tip NOTE

With ***0,on,868100000,0,5** as an example，the following is the channel parameter analysis:

- `*` at the beginning, if the channel is open;
- `0` is the channel ID;
- `on` indicates the current status of the channel;
- `868100000` is the actual frequency of the channel，unit is Hz;
- `0,5` indicates the DR of the channel, DR0~DR5.

:::

5. **at+set_config=lora:ch_mask:`<channel_number>:<status>`**

This command is used to enable (on) or disable (off) a channel in the current region.

| Operation | Command                                                | Response |
| --------- | ------------------------------------------------------ | -------- |
| Write     | `at+set_config=lora:ch_mask:<channel_number>:<status>` | OK       |

**Parameter**：

| channel_number | Channel number |
| --- | --- |
| status | 0: off 1: on |

**Example**:
```
at+set_config=lora:ch_mask:0:0\r\n
OK
```

6. **at+set_config=lora:dev_eui:`<dev_eui>`**

This command is used to set the Device EUI parameter for LoRaWAN OTAA mode.

| Operation | Command                                | Response |
| --------- | -------------------------------------- | -------- |
| Write     | `at+set_config=lora:dev_eui:<dev_eui>` | OK       |

**Parameter**：

| dev_eui | Device EUI |
| --- | --- |

**Example**：
```
at+set_config=lora:dev_eui:3530353064377716\r\n
OK
```

7.  **at+set_config=lora:app_eui:`<app_eui>`**

This command is used to set the Application EUI parameter for the LoRaWAN OTAA mode.

| Operation | Command                                | Response |
| --------- | -------------------------------------- | -------- |
| Write     | `at+set_config=lora:app_eui:<app_eui>` | OK       |

**Parameter**：

| app_eui | Application EUI |
| --- | --- |

:::tip NOTE
All zero value Application EUI `at+set_config=lora:app_eui:0000000000000000` is **not supported** and will return error.
:::

**Example**：
```
at+set_config=lora:app_eui:0000000000000001\r\n
OK
```

8. **at+set_config=lora:app_key:`<app_key>`**

This command is used to set the Application Key parameter for the LoRaWAN OTAA mode.

| Operation | Command                                | Response |
| --------- | -------------------------------------- | -------- |
| Write     | `at+set_config=lora:app_key:<app_key>` | OK       |

**Parameter**：

| app_key | Application Key |
| --- | --- |

**Example**：
```
at+set_config=lora:app_key:841986913ACD00BBC2BE2479D70F3228\r\n
OK
```

9. **at+set_config=lora:dev_addr:`<dev_addr>`**

This command is used to set the Device Address parameter for the LoRaWAN ABP mode.

| Operation | Command                                  | Response |
| --------- | ---------------------------------------- | -------- |
| Write     | `at+set_config=lora:dev_addr:<dev_addr>` | OK       |

**Parameter**：

| dev_addr | Device Address |
| --- | --- |

**Example**：
```
at+set_config=lora:dev_addr:260125D7\r\n
OK
```

10. **at+set_config=lora:apps_key:`<apps_key>`**

This command is used to set the Application Session Key parameter for the LoRaWAN ABP mode.

| Operation | Command                                  | Response |
| --------- | ---------------------------------------- | -------- |
| Write     | `at+set_config=lora:apps_key:<apps_key>` | OK       |

**Parameter**：

| apps_key | Application Session Key |
| --- | --- |

**Example**：
```
at+set_config=lora:apps_key:841986913ACD00BBC2BE2479D70F3228\r\n
OK
```

11. **at+set_config=lora:nwks_key:`<nwks_key>`**

This command is used to set the Network Session Key parameter for the LoRaWAN ABP mode.

| Operation | Command                                  | Response |
| --------- | ---------------------------------------- | -------- |
| Read      | `at+set_config=lora:nwks_key:<nwks_key>` | OK       |

**Parameter**：

| nwks_key | Network Session Key |
| --- | --- |

**Example**：
```
at+set_config=lora:nwks_key:69AF20AEA26C01B243945A28C9172B42\r\n
OK
```

12. **at+set_config=lora:multicastenable:`<IsEnable>`**

This command is used to enable or disable the multicast feature.

| Operation | Command                                         | Response |
| --------- | ----------------------------------------------- | -------- |
| Write     | `at+set_config=lora:multicastenable:<IsEnable>` | OK       |

**Parameter**：

| IsEnable | 0: disable 1: enable The default is disable. |
| --- | --- |

**Example**：
```
at+set_config=lora:multicastenable:1\r\n
OK
```

13. **at+set_config=lora:multicast_dev_addr:`<multicast_dev_addr>`**

This command is used to set the Device Address for the multicast feature.

| Operation | Command                                                      | Response |
| --------- | ------------------------------------------------------------ | -------- |
| Write     | `at+set_config=lora:multicast_dev_addr:<multicast_dev_addr>` | OK       |

**Parameter**：

| multicast_dev_addr | Multicast Device Address |
| --- | --- |

**Example**：
```
at+set_config=lora:multicast_dev_addr:260111fd\r\n
OK
```

14. **at+set_config=lora:multicast_apps_key:`<multicast_apps_key>`**

This command is used to set the Application Session Key for the multicast feature.

| Operation | Command                                                      | Response |
| --------- | ------------------------------------------------------------ | -------- |
| Write     | `at+set_config=lora:multicast_apps_key:<multicast_apps_key>` | OK       |

**Parameter**：

| multicast_apps_key | Multicast Application Session Key |
| --- | --- |

**Example**：
```
at+set_config=lora:multicast_apps_key:F13DDFA2619B10411F02F042E1C0F356\r\n
OK
```

15. **at+set_config=lora:multicast_nwks_key:`<multicast_nwks_key>`**

This command is used to set the Network Session Key for the multicast feature.

| Operation | Command                                                      | Response |
| --------- | ------------------------------------------------------------ | -------- |
| Write     | `at+set_config=lora:multicast_nwks_key:<multicast_nwks_key>` | OK       |

**Parameter**：

| multicast_nwks_key | Multicast Network Session Key |
| --- | --- |

**Example**：
```
at+set_config=lora:multicast_nwks_key:1D1991F5377C675879C39B6908D437A6\r\n
OK
```

16. **at+set_config=lora:join_mode:`<mode>`**

This command is used to switch the LoRaWAN access mode between the OTAA and the ABP mode.

| Operation | Command                               | Response |
| --------- | ------------------------------------- | -------- |
| Write     | `at+set_config=lora:join_mode:<mode>` | OK       |

**Parameter**：

| mode | Activation mode 0: OTAA 1: ABP The default is OTAA. |
| --- | --- |

**Example**：
```
at+set_config=lora:join_mode:1\r\n
OK
```

17. **at+set_config=lora:class:`<class>`**

This command is used to set LoRaWAN class to Class A, Class B, or Class C.

| Operation | Command                            | Response |
| --------- | ---------------------------------- | -------- |
| Write     | `at+set_config=lora:class:<class>` | OK       |

**Parameter**：

| class | 0: Class A 1: Class B (Not supported at this time.) 2: Class C The default is Class A. |
| --- | --- |

**Example**：
```
at+set_config=lora:join_mode:1\r\n
OK
```

18. **at+set_config=lora:confirm:`<type>`**

This command is used to set the type data to be sent: Confirmed/Unconfirmed.

| Operation | Command                             | Response |
| --------- | ----------------------------------- | -------- |
| Write     | `at+set_config=lora:confirm:<type>` | OK       |

**Parameter**：

| type | 0: unconfirm type 1: confirm type The default is unconfirm type. |
| --- | --- |

**Example**：
```
at+set_config=lora:confirm:0\r\n
OK
```

19. **at+set_config=lora:dr:`<dr>`**

This command is used to set the data rate (DR) of LoRa.

| Operation | Command                      | Response |
| --------- | ---------------------------- | -------- |
| Write     | `at+set_config=lora:dr:<dr>` | OK       |

**Parameter**：

| dr | The data rate of LoRa depends on the specific region. In most LoRa regions, data rates commonly range from 0 to 5. For detailed information, refer to the LoRaWAN 1.0.2 specification. |
| --- | --- |

20. **at+set_config=lora:tx_power:`<tx_power>`**

This command is used to set the RF transmission power level of the LoRa transceiver.

| Operation | Command                                  | Response |
| --------- | ---------------------------------------- | -------- |
| Write     | `at+set_config=lora:tx_power:<tx_power>` | OK       |

**Parameter**:

| tx_power | Refer to Appendix II for possible values of tx_power. The table of Appendix II is based on LoRaWAN 1.0.2 specification. LoRa transmit power level varies depending on frequency band. If the resulting TX power is higher than the capability of LoRa Radio, the output power will be based on the max TX power of the LoRa Radio in the module. For RAK4600 module, the max TX power is 20 dBm. Take note of this when using regional bands with MaxEIRP higher than 20 dBm like US915, AU915 and IN865 whose MaxEIRP is 30 dBm. The default setting is 0. |
| --- | --- |

**Example**：

```
at+set_config=lora:tx_power:0\r\n
OK
```

21. **at+set_config=lora:adr:`<status>`**

This command is used to turn on/off the ADR feature of the LoRa communication.

| Operation | Command                           | Response |
| --------- | --------------------------------- | -------- |
| Write     | `at+set_config=lora:adr:<status>` | OK       |

**Parameter**：

| status | 0: Turn off 1: Turn on The default is on. |
| --- | --- |

**Example**：
```
at+set_config=lora:adr:0\r\n
OK
```

22. **at+get_config=lora:status**

This command is used to get all the information related to the current LoRa status, except channel information.

| Operation | Command                     | Response                  |
| --------- | --------------------------- | ------------------------- |
| Read      | `at+get_config=lora:status` | `OK <lora status detail>` |

**Parameter**：None

**Example**：
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
| Write     | `at+set_config=lora:dutycycle_enable:<status>` | OK       |

**Parameter**：

| status | 0: disable 1: enable The default is disable. |
| --- | --- |

**Example**：
```
at+set_config=lora:dutycycle_enable:1\r\n
OK
```

24. **at+set_config=lora:send_repeat_cnt:`<num>`**

This command is used to set the number of retransmitting attempts on an uplink message. When activated, the board will resend a message if its corresponding ACK (downlink) is not received after sending a confirmed uplink message. The default value is 0, which means that the board will not resend any message by default.

| Operation | Command                                       | Response |
| --------- | --------------------------------------------- | -------- |
| Write     | `at+set_config=lora:send_repeat_cnt:<status>` | OK       |

**Parameter**：

| num | Number of retries, up to 7. The default is 0. |
| --- | --- |

**Example**：
```
at+set_config=lora:send_repeat_cnt:1\r\n
OK
```

25. **at+set_config=lora:default_parameters**

This command is used to restore OTAA, ABP, multicast related network access parameters set at the factory, including dev_eui，app_eui, etc.

| Operation | Command                                 | Response |
| --------- | --------------------------------------- | -------- |
| Write     | `at+set_config=lora:default_parameters` | OK       |

**Parameter**：None

**Example**：
```
at+set_config=lora:default_parameters\r\n
OK
```

## LoRa P2P Type AT Command

1. **at+set_config=lora:work_mode:`<mode>`**

This command is used to switch the LoRa work mode between the LoRaWAN and the LoRa P2P mode. This command will cause the module to restart.

| Operation | Command                               | Response |
| --------- | ------------------------------------- | -------- |
| Write     | `at+set_config=lora:work_mode:<mode>` |          |

**Parameter**：

| mode | LoRa work mode 0: LoRaWAN 1: LoRa P2P The default is LoRaWAN mode. |
| --- | --- |

**Example**：
```
at+set_config=lora:work_mode:1\r\n
UART1 work mode: RUI_UART_NORMAL
Current work_mode:P2P
Initialization OK
```

2. **at+set_config=lorap2p:`<frequency>:<spreadfact>:<bandwidth>:<codingrate>:<preamlen>:<power>`**

This command is used to set the relevant parameters of LoRA P2P mode and is only valid when the LoRa work mode is changed to LoRa P2P before.

| Operation | Command                                                                                      | Response |
| --------- | -------------------------------------------------------------------------------------------- | -------- |
| Write     | `at+set_config=lorap2p:<frequency>:<spreadfact>:<bandwidth>:<codingrate>:<preamlen>:<power>` | OK       |

**Parameter**：

| frequency | Frequency, the unit is Hz The default is 869525000 Hz. |
| --- | --- |
| spreadfact | Spreading factor The default is 12. |
| bandwidth | 0: 125 kHz 1: 250 kHz 2: 500 kHz The default is 0. |
| codingrate | 1: 4/5 2: 4/6 3: 4/7 4: 4/8 The default is 1. |
| preamble | Preamble Length. 5~65535 The default is 8. |
| power | TX power. The unit is in dBm. 5~20 The default is 20. |

**Example**：
```
at+set_config=lorap2p:869525000:12:0:1:8:20\r\n
OK
```

3. **at+set_config=lorap2p:transfer_mode:`<mode>`**

This command is used to switch the state of the LoRa transceiver between sending and receiving. It is only valid when the LoRa mode has been set to LoRa P2P beforehand.

| Operation | Command                                      | Response |
| --------- | -------------------------------------------- | -------- |
| Write     | `at+set_config=lorap2p:transfer_mode:<mode>` | OK       |

**Parameter**：

| mode | 1: receiver mode 2: sender mode The default is sender mode. |
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

## BLE Type AT Command

1. **at+set_config=ble:work_mode:`<mode>:<long_range>`**

This command is used to configure the BLE mode.

| Operation | Command                                           | Response |
| --------- | ------------------------------------------------- | -------- |
| Write     | `at+set_config=ble:work_mode:<mode>:<long_range>` | OK       |

**Parameter**：

| mode | BLE work mode. 0: Peripheral mode (Default) 1: Central mode 2: Beacon scan mode |
| --- | --- |
| long_range | Long-range enable, only ‘0’ can be selected because RAK4600 Breakout does not support this feature. |

**Example**：
```
at+set_config=ble:work_mode:0:0\r\n
OK
```

## Appendix I: Data Rate by Region

**EU433/EU868/AS923**

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

**CN470/KR920**

| Data Rate | Configuration             | Indicative Physical Bit Rate [bit/s] |
| --------- | ------------------------- | ------------------------------------ |
| 0         | LoRa: SF12 / 125 kHz | 250                                  |
| 1         | LoRa: SF11 / 125 kHz | 440                                  |
| 2         | LoRa: SF10 / 125 kHz | 980                                  |
| 3         | LoRa: SF9 / 125 kHz  | 1760                                 |
| 4         | LoRa: SF8 / 125 kHz  | 3125                                 |
| 5         | LoRa: SF7 / 125 kHz  | 5470                                 |
| 6 ~ 15    | RFU                       |                                      |

**US915**

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

**AU915**

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

**IN865**

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

## Appendix II: TX Power by Region

**EU868**

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

**US915**

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

**AU915**

By default, MaxEIRP is considered to be +30 dBm based on LoRa Alliance specification.
However, the module's max TX power is only up to 20 dBm.

| TXPower | Configuration (EIRP) |
| ------- | -------------------- |
| 0       | MaxEIRP              |
| 1 ~ 10  | MaxEIRP - 2*TX Power |
| 11 ~ 10 | RFU                  |

**KR920**

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

**AS923**

By default, MaxEIRP shall be 16 dBm.

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

**IN865**

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

**CN470**

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

**EU433**

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

## Appendix III: Maximum Transmission Load by Region

:::tip NOTE
In the following list:

- **M**: The total length, including the MAC header.
- **N**: The maximum usable payload size for user data, excluding the MAC header.
::::

**EU868**

| DataRate |      M      |      N      |
| :------: | :---------: | :---------: |
|    0     |     59      |     51      |
|    1     |     59      |     51      |
|    2     |     59      |     51      |
|    3     |     123     |     115     |
|    4     |     250     |     242     |
|    5     |     250     |     242     |
|    6     |     250     |     242     |
|    7     |     250     |     242     |
|  8 ~ 15  | Not Defined | Not Defined |

**US915**

| DataRate |      M      |      N      |
| :------: | :---------: | :---------: |
|    0     |     19      |     11      |
|    1     |     61      |     53      |
|    2     |     133     |     125     |
|    3     |     250     |     242     |
|    4     |     250     |     242     |
|  5 ~ 7   | Not Defined | Not Defined |
|    8     |     61      |     53      |
|    9     |     137     |     129     |
|    10    |     250     |     242     |
|    11    |     250     |     242     |
|    12    |     250     |     242     |
|    13    |     250     |     242     |
| 14 ~ 15  | Not Defined | Not Defined |

**AU915**

| DataRate |      M      |      N      |
| :------: | :---------: | :---------: |
|    0     |     59      |     51      |
|    1     |     59      |     51      |
|    2     |     59      |     51      |
|    3     |     123     |     115     |
|    4     |     250     |     242     |
|    5     |     250     |     242     |
|    6     |     250     |     242     |
|    7     | Not Defined | Not Defined |
|    8     |     61      |     53      |
|    9     |     137     |     129     |
|    10    |     250     |     242     |
|    11    |     250     |     242     |
|    12    |     250     |     242     |
|    13    |     250     |     242     |
| 14 ~ 15  | Not Defined | Not Defined |

**KR920**

| DataRate |      M      |      N      |
| :------: | :---------: | :---------: |
|    0     |     59      |     51      |
|    1     |     59      |     51      |
|    2     |     59      |     51      |
|    3     |     123     |     115     |
|    4     |     250     |     242     |
|    5     |     250     |     242     |
|  6 ~ 15  | Not Defined | Not Defined |

**AS923**

| DataRate | Uplink MAC Payload Size (M) | Downlink MAC Payload Size (M) |  |  |
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

**IN865**

| DataRate |      M      |      N      |
| :------: | :---------: | :---------: |
|    0     |     59      |     51      |
|    1     |     59      |     51      |
|    2     |     59      |     51      |
|    3     |     123     |     115     |
|    4     |     250     |     242     |
|    5     |     250     |     242     |
|    6     |     250     |     242     |
|    7     |     250     |     242     |
|  8 ~ 15  | Not Defined | Not Defined |

**CN470**

| DataRate |      M      |      N      |
| :------: | :---------: | :---------: |
|    0     |     59      |     51      |
|    1     |     59      |     51      |
|    2     |     59      |     51      |
|    3     |     123     |     115     |
|    4     |     250     |     242     |
|    5     |     250     |     242     |
|  6 ~ 15  | Not Defined | Not Defined |

**EU433**

| DataRate |      M      |      N      |
| :------: | :---------: | :---------: |
|    0     |     59      |     51      |
|    1     |     59      |     51      |
|    2     |     59      |     51      |
|    3     |     123     |     115     |
|    4     |     250     |     242     |
|    5     |     250     |     242     |
|    6     |     250     |     242     |
|    7     |     250     |     242     |
|  8 ~ 15  | Not Defined | Not Defined |

## Appendix IV: Pin Description of RAK4600 Breakout Board

The pin definition of the RAK4600 Breakout Board can be reviewed in the [Pin Definition](https://docs.rakwireless.com/product-categories/wisduo/rak4600-breakout-board/datasheet/#pin-definition) section of the Datasheet.

The following is a summary of the pins on the RAK4270 Breakout Board:

:::tip NOTE
Not all pins of the RAK4600 module are exposed on the RAK4600 Breakout board header connectors. Below are the pins available on the RAK4600 Module that is on this Breakout board. For complete RAK4600 module pinouts information, refer to the [datasheet](https://docs.rakwireless.com/product-categories/wisduo/rak4600-module/datasheet/#pin-definition).
:::

1. **UART Pins**:
     - Pin 22 (RX) and Pin 21 (TX) are reserved for UART1.
     - During sleep, Pin 22 (USART1_RX) is automatically configured as a wake up pin and in external interrupt mode with an internal pull-down resistor. Wake-up will be triggered by a rising edge on this RX pin.

2. **SWD debug Pins**: Pin 37 (SWDIO) and Pin 38 (SWCLK) are used for SWD debug port.

3. **Power Pins**: The power pins on the RAK4600 module includes the VCC pins on Pin 40 (3V3_IN) and Pin 41 (3V3_IN), and the Ground pins (GND) are on the Pin 1, Pin 8, Pin 12, Pin 13, Pin 14, Pin 16, Pin 18, Pin 19, Pin 20, Pin 31, Pin 39, and Pin 42.

4.  **Reset Pin**: The reset pin on the RAK4600 module is Pin 36 (MCU_NRST).

5.  **RF Antenna Pins**: The RF Antenna pins on the RAK4600 module are Pin 15 (RF_BT) BLE antenna and Pin 17 (RF_L) LoRa antenna.

6.  **GPIO Pins**: The GPIO pins available on the RAK4600 module are the following:
     - Pin 4 (I2C1_SDA)
     - Pin 5 (I2C1_SCL)
     - Pin 6 (NFC1)
     - Pin 7 (NFC2)
     - Pin 9 (P0.18)
     - Pin 10 (P0.19)
     - Pin 21 (Reserved / P0.14)
     - Pin 24 (Reserved / P0.17)

:::tip NOTE
The subsequent firmware upgrade of the product is carried out through the OTA interface.
:::

