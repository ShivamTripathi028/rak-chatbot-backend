---
title: RAK4600 WisDuo Evaluation Board AT Command Manual
description: Provides comprehensive information about your RAK4600 Evaluation Board to help you use it. This information includes technical specifications, characteristics, and requirements, and it also discusses the device components.
image: "https://images.docs.rakwireless.com/wisduo/rak4600-evaluation-board/rak4600-evaluation.png"
keywords:
    - RAK4600 Evaluation Board
    - wisduo
    - Datasheet
sidebar_label: AT Command Manual
---

# RAK4600 Evaluation Board AT Command Manual

## Introduction

RAK4600 Evaluation Board is designed to give you a quick start to explore the LoRa/LPWAN world. The board measures 30 x 60 mm and supports USB power supply, 3.7 V LiPo battery, and 5 V solar charging.

The board itself has the RAK4600 as its core which is a module that utilizes Nordic nRF52832 MCU and an SX1276 LoRa chip. The high level of integration allows for outstanding performance: Lora TX Power of up to 20 dBm.

The board complies with LoRaWAN 1.0.2 specification, and it also supports LoRa P2P Point-to-Point communication. The low power, long-range LoRa communication capabilities of the board make it suitable for a variety of applications in the IoT field such as home automation, sensor networks, building automation, and personal area networks applications, such as health/fitness sensors and monitors.

### Software Tool

If you don't have a serial port tool yet, it is recommended to download and install the RAK Serial Port Tool. There are some ready-made AT commands in this tool that will be very useful for you.

- [RAK Serial Port Tool](https://downloads.rakwireless.com/#LoRa/Tools/)

For more detailed information on how to use this tool, refer to the following guide:

- [RAK Serial Port Tool Guide](https://docs.rakwireless.com/product-categories/wisduo/rak4600-evaluation-board/quickstart/)

## AT Command Syntax

The AT command is based on ASCII characters. A command begins with the prefix `at` and ends with `<CR><LF>` (i.e. \r\n). The maximum length is 255 characters, which includes the `<CR><LF>` characters at the end of the command. For the rest of the document, the `\r\n` part is omitted for the sake of clarity.

The AT commands can be classified into the following groups:

*   **Read Command**: Reads the current configuration or status of the module. The command name and the list of parameters are separated by the `=` character. The `<m>` parameter is separated with its associated value `<n>` by the `:` character.

```
at+get_config=<m>:<n>
```
*   **Write Command**: Writes/Modifies the current configuration of the module. The command name and the list of parameters are separated by the `=` character. The `<m>` parameter is separated with its associated value `<n>` by the `:` character.

```
at+set_config=<m>:<n>
```
*   **Operational Commands**: Some commands are neither read nor write commands but are used to execute an action.

```
at+send=lora:<m>:<n> // Sends data through the LoRa transceiver.
```

* **Special Command**: The RAK4600 UART port has two operational modes: **Configuration Mode** (default mode) and **Data Transmission Mode**. Data transmission mode allows you to send ASCII payloads directly to the network server via UART without using any AT Command interface like `at+send=lora:X:YYY`. Data transmission mode is explained further on [Interface Type AT Command](https://docs.rakwireless.com/product-categories/wisduo/rak4600-evaluation-board/at-command-manual/#interface-type-at-command) section of this document.

:::tip NOTE
To enable data transmission mode, you need to input `at+set_config=device:uart_mode:<index>:<mode>` command.  To switch back from data transmission mode to configuration mode (AT command default mode), the command to be entered is `+++` and does not contain terminators such as `\r` and `\n`.
:::

After the command is executed by the module, a reply is sent back to the external MCU. In the case the command is successful, the usual reply has the following format:

```
OK [information]\r\n
```

:::tip NOTE
Only Read commands have information in the replied message, while Write commands do not have an informative description.
:::

The firmware you developed, running in the external MCU, will expect at a minimum a string of `Ok\r\n` after sending a successful command to the board. On the other hand, when the command is not successfully executed by the board, a reply will be received in the following format:
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
| 41 | The BLE felt into an invalid state, could not applied the command. |
| 80 | The LoRa transceiver is busy, could not process a new command. |
| 81 | LoRa service is unknown. Unknown MAC command received by node. Execute commands that are not supported in the current state, such as sending "`at+join`" command in P2P mode. |
| 82 | The LoRa parameters are invalid. |
| 83 | The LoRa frequency is invalid. |
| 84 | The LoRa data rate (DR) is invalid. |
| 85 | The LoRa frequency and data rate are invalid. |
| 86 | The device hasn’t joined into a LoRa network. |
| 87 | The length of the packet exceeded that maximum allowed by the LoRa protocol. |
| 88 | Service is closed by the server. Due to the limitation of the duty cycle, the server will send the "SRV_MAC_DUTY_CYCLE_REQ" MAC command to close the service. |
| 89 | This is an unsupported region code. |
| 90 | Duty cycle is restricted. Due to the duty cycle, data cannot be sent at this time until the time limit is removed. |
| 91 | No valid LoRa channel could be found. |
| 92 | No available LoRa channel could be found. |
| 93 | Internal state error. Generally, the internal state of the protocol stack is wrong |
| 94 | Time out reached while sending the packet through the LoRa transceiver. |
| 95 | Time out reached while waiting for a packet in the LoRa RX1 window. |
| 96 | Time out reached while waiting for a packet in the LoRa RX2 window. |
| 97 | There is an error while receiving a packet during the LoRa RX1 window. |
| 98 | There is an error while receiving a packet during the LoRa RX2 window. |
| 99 | Failed to join into a LoRa network. |
| 100 | Duplicate downlink message is detected. A message with an invalid downlink count is received. |
| 101 | Payload size is not valid for the current data rate (DR). |
| 102 | Many downlink packets are lost. |
| 103 | Address fail. The address of the received packet does not match the address of the current node. |
| 104 | Invalid MIC is detected in the LoRa message. |

## General AT Command

1. **at+version**

This command is used to get version the current firmware version number.

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

This command is used to obtain all the AT commands supported by the current firmware.

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

LoRaWAM AT commands:
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

BLE AT commands:
  at+set_config=ble:work_mode:X:Y
```

3. **at+set_config=device:restart**

This command is used for restarting the device.

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

| status | 0: wake up1: sleep |
| --- | --- |

**Example**:
```
at+set_config=device:sleep:1\r\n
OK Sleep

at+set_config=device:sleep:0\r\n
OK Wake Up
```

:::tip NOTE

During sleep, Pin 22 (USART1_RX) is automatically configured as a wake up pin and in external interrupt mode with an internal pull-down resistor. Wake-up will be triggered by a rising edge on this RX pin.

:::

5. **at+get_config=device:status**

This command is used to obtain the current status of the device.

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

Parameter：

| index | UART Number |
| --- | --- |
| baud_rate | UART Baud rate:1200,2400,4800,9600,19200,38400,57600,115200 |

2. **at+set_config=device:uart_mode:`<index>:<mode>`**

This command is used to set the UART operation from AT **configuration mode** to **data transmission mode**.

During **data transmission mode**, all standard AT Commands will not work, and the data you sent to UART will go directly to the network server as ASCII payload with `\r\n`. If you input `AZ`, the network server will receive an uplink hex value of `415A0D0A`. This means **A**=`0x41`, **Z**=`0x5A`, **\r**=`0x0D` and **\n**=`0x0A`.

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
| data | The sending data format is in hexadecimal format. The possible values are between **00-FF**. The module internally will cast every two characters into a byte before sending it to the LoRa transceiver. The maximum length varies depending on the band frequency and DR (LoRaWAN standard). Refer toAppendix III. |

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

| region | EU433, CN470, IN865, EU868, US915, AU915, KR920, AS923.The default is EU868. |
| --- | --- |

**Example**：
```
at+set_config=lora:region:EU868\r\n
OK
```

:::tip NOTE
In the AS923 frequency band, the supported frequency plan is "as2" and dwell time is set to 1.
:::

4. **at+get_config=lora:channel**

This command is used for reading all the LoRa channel information for the device's current region.

| Operation | Command                      | Response                   |
| --------- | ---------------------------- | -------------------------- |
| Read      | `at+get_config=lora:channel` | `OK <channel information>` |

**Parameter**：None

**Example**：
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
| status | 0: off1: on |

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

This command is used to set the Network Session Key parameter for the LoRaWAN ABP mode

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

| IsEnable | 0: disable1: enableThe default is disable. |
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

| mode | Activation mode0: OTAA1: ABPThe default is OTAA. |
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

| class | 0: Class A1: Class B (Not supported at this time)2: Class CThe default is Class A. |
| --- | --- |

**Example**：
```
at+set_config=lora:class:0\r\n
OK
```

18. **at+set_config=lora:confirm:`<type>`**

This command is used to set the type of data to be sent: Confirmed/Unconfirmed.

| Operation | Command                             | Response |
| --------- | ----------------------------------- | -------- |
| Write     | `at+set_config=lora:confirm:<type>` | OK       |

**Parameter**：

| type | 0: unconfirm type1: confirm typeThe default is unconfirm type. |
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

| dr | The data rate of LoRa is related to the current region. In most LoRa areas, it is common to use 0 to 5. Detailed reference can be made to LoRaWan 1.0.2 specification. |
| --- | --- |

20. **at+set_config=lora:tx_power:`<tx_power>`**

This command is used to set the RF transmission power level of the LoRa transceiver.
| Operation | Command                                  | Response |
| --------- | ---------------------------------------- | -------- |
| Write     | `at+set_config=lora:tx_power:<tx_power>` | OK       |

**Parameter**:

| tx_power | Refer toAppendix IIfor possible values of tx_power. The table of Appendix II is based on LoRaWAN 1.0.2 specification. LoRa transmit power level varies depending on frequency band.If the resulting TX power is higher than the capability of LoRa Radio, the output power will be based on the max TX power of the LoRa Radio in the module. For RAK4600 module, the max TX power is 20dBm. Take note of this when using regional bands with MaxEIRP higher than 20dBm like US915, AU915 and IN865 whose MaxEIRP is 30dBm.The default setting is 0. |
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

| status | 0: Turn off1: Turn onThe default is on. |
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

This command is used for enabling or disabling the Duty Cycle feature.

| Operation | Command                                        | Response |
| --------- | ---------------------------------------------- | -------- |
| Write     | `at+set_config=lora:dutycycle_enable:<status>` | OK       |

**Parameter**：

| status | 0: disable1: enableThe default is disable. |
| --- | --- |

**Example**：
```
at+set_config=lora:dutycycle_enable:1\r\n
OK
```

24. **at+set_config=lora: send_repeat_cnt:`<num>`**

This command is used to set the number of retransmitting attempts on an uplink message. When activated, the board will resend a message if its corresponding ACK (downlink) is not received after sending a confirmed uplink message. The default value is 0, which means that the board will not resend any message by default.

| Operation | Command                                        | Response |
| --------- | ---------------------------------------------- | -------- |
| Write     | `at+set_config=lora: send_repeat_cnt:<status>` | OK       |

**Parameter**：

| num | Number of retries, up to 7.The default is 0. |
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

This command is used to switch the LoRa's transmission mode between the LoRaWAN and LoRA P2P mode. This command will cause the module to restart once applied.

| Operation | Command                               | Response |
| --------- | ------------------------------------- | -------- |
| Write     | `at+set_config=lora:work_mode:<mode>` |          |

**Parameter**：

| mode | Work mode of LoRa0: LoRaWAN1: LoRaP2PThe default is LoRaWAN mode |
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

This command is used to change the state of the LoRa transceiver between sending and receiving state, and it is only valid when the LoRa mode is set to LoRa P2P before.

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

This command is used to send data through LoRa P2P and is only valid when the LoRa work mode was set to LoRa P2P before.

| Operation | Command                  | Response |
| --------- | ------------------------ | -------- |
| Send      | `at+send=lorap2p:<data>` | OK       |

**Parameter**：

| data | The data to be sent, and the format is hexadecimal |
| --- | --- |

**Example**：
```
at+send=lorap2p:1234\r\n
OK
```
In LoRa P2P mode, the receiving node receives the data and outputs the data in the following format:

```
at+recv=<RSSI>,<SNR>,< Data Length >:< Data >
```

## BLE Type AT Command

1. **at+set_config=ble:work_mode:`<mode>:<long_range>`**

This command is used to configure the BLE mode.

| Operation | Command                                           | Response |
| --------- | ------------------------------------------------- | -------- |
| Write     | `at+set_config=ble:work_mode:<mode>:<long_range>` | OK       |

**Parameter**：

| mode | BLE work mode.0: Peripheral mode (Default)1: Central mode2: Beacon scan mode |
| --- | --- |
| long_range | Long range enable, only ‘0’ can be selected because RAK4600 does not support this feature. |

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
The LoRaWAN stack adds 8 bytes to the user payload. In the following list, M is the maximum payload size and N is the maximum usable payload size for the user data without the MAC header.
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

## Appendix IV: Pin Description of RAK4600

The pin definition of the RAK4600 module can be reviewed in the [Pin Definition](https://docs.rakwireless.com/product-categories/wisduo/rak4600-evaluation-board/datasheet/#pin-definition) section on the Datasheet.

:::warning
This pin definition is **only** for the RAK4600 Module not for the RAK4600 Evaluation Board.
:::

A summary of the pins of the RAK4600 module:

1. **About the UART Pin**:
    - Pin 22 (USART1_RX) and Pin 23 (USART1_TX).
    - During sleep, Pin 22 (USART1_RX) is automatically configured as a wake up pin and in external interrupt mode with an internal pull-down resistor. Wake-up will be triggered by a rising edge on this RX pin.

2. **About the SWD debug Pin**: Pin 37 (SYS_SWDIO) and Pin 38 (SYS_SWDCLK) are used for SWD debug programming.
3. **About the Power Pin**: The power pins on the RAK4600 module includes the VCC Pins on Pin 40 (3V3_IN) and Pin 41 (3V3_IN), and the ground pins (GND) are on the Pin 1, Pin 8, Pin 12, Pin 13, Pin 14, Pin 16, Pin 18, Pin 19, Pin 20, Pin 31, Pin 39, and Pin 42.
4.  **About the Reset Pin**: The reset pin on the RAK4600 module is the Pin 36 (MCU_NRST);
5.  **About the RF Antenna Pin**: The RF Antenna pins on the RAK4600 module are the pin15 (RF_BT) BLE antenna and Pin 17 (RF_L) LoRa antenna.
6.  **About the GPIO Pin**: The GPIO pins available on the RAK4600 module are Pin 4, Pin 5, Pin 6, Pin 7, Pin 9, Pin 10, Pin 21, and Pin 24.

:::tip NOTE
The subsequent firmware upgrade of the product is carried out through the OTA interface.
:::

