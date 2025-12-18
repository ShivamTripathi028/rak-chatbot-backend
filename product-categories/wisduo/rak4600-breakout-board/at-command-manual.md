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

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK4600 Breakout Board AT Command Manual

## Introduction

The RAK4600 Breakout Board simplifies both LoRa P2P peer-to-peer and LoRaWAN communication. Instead of dealing with complex SPI protocols for LoRa transceivers, this board provides a familiar serial communication interface to send commands and check the board's status. This design allows for seamless integration of LoRa technology into your projects.

Through its serial interface, the RAK4600 Breakout Board uses a defined set of AT commands. You can control the board with an external microcontroller as a standard AT modem. These AT commands allow you to configure LoRaWAN communication parameters, control GPIO pins, and manage analog inputs.

In the RAK4600 Breakout Board, the serial communication is available through the **UART1 port**, using J7 connector Pin 1 (USART1_RX) and Pin 2 (USART1_TX). The USART1 communication parameters are set to **115200 / 8-N-1**. You can also perform firmware upgrades through this port. For detailed pin distribution and schematic information, refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4600-breakout-board/datasheet/" target="_blank">RAK4600 Breakout Board Datasheet</a>.

Additionally, the RAK4600 Breakout Board supports BLE connectivity. You can communicate with the board via BLE interface using your mobile phone or use the board to scan for nearby Bluetooth beacon information. For more details, refer to <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4600-breakout-board/quickstart/#bluetooth-connection-modes" target="_blank">Bluetooth Connection Modes</a>.


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

- **Special Command**: The RAK811 UART port operates in two modes: **Configuration Mode** (default) and **Data Transmission Mode**. In Data Transmission Mode, ASCII payloads can be sent directly to the network server via UART without using the AT Command interface, such as `at+send=lora:X:YYY`. For more details, refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4600-breakout-board/at-command-manual/#interface-type-at-command" target="_blank">Interface Type AT Command</a> section of this document.

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

<table>
<thead>
  <tr>
    <th>Error Code</th>
    <th>Description</th>
  </tr>
</thead>
        <tr>
            <td>1</td>
            <td>The last command received is an unsupported AT command.</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Invalid parameter in the AT command.</td>
        </tr>
        <tr>
            <td>3</td>
            <td>There is an error when reading or writing the flash memory.</td>
        </tr>
        <tr>
            <td>5</td>
            <td>There is an error when sending data through the UART port.</td>
        </tr>
        <tr>
            <td>41</td>
            <td>The BLE felt into an invalid state, could not apply the command.</td>
        </tr>
        <tr>
            <td>80</td>
            <td>The LoRa transceiver is busy, could not process a new command.</td>
        </tr>
        <tr>
            <td>81</td>
            <td>The LoRa service is unavailable. The node received an unrecognized MAC command. This error occurs when executing unsupported commands in the current state, such as using the `at+join` command while in P2P mode.</td>
        </tr>
        <tr>
            <td>82</td>
            <td>The LoRa parameters are invalid.</td>
        </tr>
        <tr>
            <td>83</td>
            <td>The LoRa frequency is invalid.</td>
        </tr>
        <tr>
            <td>84</td>
            <td>The LoRa data rate (DR) is invalid.</td>
        </tr>
        <tr>
            <td>85</td>
            <td>The LoRa frequency and data rate are invalid.</td>
        </tr>
        <tr>
            <td>86</td>
            <td>The device hasn’t joined into a LoRa network.</td>
        </tr>
        <tr>
            <td>87</td>
            <td>The length of the packet exceeded the maximum allowed by the LoRa protocol.</td>
        </tr>
        <tr>
            <td>88</td>
            <td>The server has closed the service. Due to duty cycle limitations, the server sends a `SRV_MAC_DUTY_CYCLE_REQ` MAC command to terminate the service.</td>
        </tr>
        <tr>
            <td>89</td>
            <td>This is an unsupported region code.</td>
        </tr>
        <tr>
            <td>90</td>
            <td>Duty cycle is restricted. Due to the duty cycle, data cannot be sent at this time until the time limit is removed.</td>
        </tr>
        <tr>
            <td>91</td>
            <td>No valid LoRa channel could be found.</td>
        </tr>
        <tr>
            <td>92</td>
            <td>No available LoRa channel could be found.</td>
        </tr>
        <tr>
            <td>93</td>
            <td>Internal state error. Generally, the internal state of the protocol stack is incorrect</td>
        </tr>
        <tr>
            <td>94</td>
            <td>Time out reached while sending the packet through the LoRa transceiver.</td>
        </tr>
        <tr>
            <td>95</td>
            <td>Time out reached while waiting for a packet in the LoRa RX1 window.</td>
        </tr>
        <tr>
            <td>96</td>
            <td>Time out reached while waiting for a packet in the LoRa RX2 window.</td>
        </tr>
        <tr>
            <td>97</td>
            <td>An error occurred while receiving a packet during the LoRa RX1 window.</td>
        </tr>
        <tr>
            <td>98</td>
            <td>An error occurred while receiving a packet during the LoRa RX2 window.</td>
        </tr>
        <tr>
            <td>99</td>
            <td>Failed to join into a LoRa network.</td>
        </tr>
        <tr>
            <td>100</td>
            <td>Duplicate downlink message is detected. A message with an invalid downlink count is received.</td>
        </tr>
        <tr>
            <td>101</td>
            <td>Payload size is not valid for the current data rate (DR).</td>
        </tr>
        <tr>
            <td>102</td>
            <td>Many downlink packets are lost.</td>
        </tr>
        <tr>
            <td>103</td>
            <td>The address of the received packet does not match the current node's address.</td>
        </tr>
        <tr>
            <td>104</td>
            <td>Invalid MIC is detected in the LoRa message.</td>
        </tr>

</table>

## General AT Command

1. <b>at+version</b>

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

<br />

2. <b>at+help</b>

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

<br />

3. <b>at+set_config=device:restart</b>

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

<br />

4. <b>at+set_config=device:sleep:`<status>`</b>

This command is used to change the current state of the device between the sleep and the wake-up mode.

| Operation | Command                               | Response      |
| --------- | ------------------------------------- | ------------- |
| Write     | `at+set_config=device:sleep:<status>` | `OK <STATUS>` |

**Parameter**:

<table>
        <tr>
            <td>status</td>
            <td>0: wake up <br />1: sleep </td>
        </tr>

</table>

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

<br />

5. <b>at+get_config=device:status</b>

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

1. <b>at+set_config=device:uart:`<index>:<baud_rate>`</b>

This command is used to configure the baud rate for a UART port.

| Operation | Command                                         | Response |
| --------- | ----------------------------------------------- | -------- |
| Write     | `at+set_config=device:uart:<index>:<baud_rate>` | `OK`     |

**Parameter**：

<table>
        <tr>
            <td>index</td>
            <td>UART Number</td>
        </tr>
        <tr>
            <td>baud_rate</td>
            <td>UART Baud rate:<br />1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200</td>
        </tr>

</table>

**Example**:

```
at+set_config=device:uart:1:115200\r\n
OK
```

<br />

2. <b>at+set_config=device:uart_mode:`<index>:<mode>`</b>

This command is used to set the UART operation from AT **configuration mode** to **data transmission mode**.

During **data transmission mode**, standard AT Commands are disabled and all data sent to UART is transmitted directly to the network server as ASCII payload with `\r\n`. For example, if you input `AZ`, the network server receives an uplink hex value of `415A0D0A`, where **A**=`0x41`, **Z**=`0x5A`, **\r**=`0x0D`, and **\n**=`0x0A`.

:::tip NOTE

To switch back from data transmission mode to configuration mode, use `+++` (`+++` without `\ r\ n`).

:::



| Operation | Command                                         | Response |
| --------- | ----------------------------------------------- | -------- |
| Write     | `at+set_config=device:uart_mode:<index>:<mode>` | `OK`     |

**Parameter**:

<table>
    <tr>
      <td> index </td>
      <td> UART Port Number. Currently, the RAK4600 only supports UART1.  </td>
    </tr>
    <tr>
      <td> mode </td>
      <td> UART Mode： Only 1 can be selected, which means the UART is set to data transmission mode. </td>
    </tr>
</table>




**Example**:

```
at+set_config=device:uart_mode:1:1\r\n
OK

+++
OK
```

<br />


## LoRaWAN Type AT Command

1. <b>at+join</b>

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

<br />

2. <b>at+send=lora:`<port>:<data>`</b>

This command is used to send data via LoRaWAN.

| Operation | Command                      | Response |
| --------- | ---------------------------- | -------- |
|           | `at+send=lora:<port>:<data>` | OK       |

**Parameter**：

<table>
        <tr>
            <td>port</td>
            <td>Sending port of LoRa. The value range is 1-223.</td>
        </tr>
        <tr>
            <td>data</td>
            <td>The sending data format is in hexadecimal format. The possible values are between <b>00-FF</b>. The board internally will cast every two characters into a byte before sending it to the LoRa transceiver. The maximum length varies depending on the band frequency and DR (LoRaWAN standard). Refer to <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4600-module/at-command-manual/#appendix-iii-maximum-transmission-load-by-region" >Appendix III</a>.</td>
        </tr>
</table>

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

<br />

3. <b>at+set_config=lora:region:`<region>`</b>

This command is used to set the appropriate working frequency band.

| Operation | Command                              | Response |
| --------- | ------------------------------------ | -------- |
| Write     | `at+set_config=lora:region:<region>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>region</td>
            <td>EU433, CN470, IN865, EU868, US915, AU915, KR920, AS923.<br />The default is EU868.</td>
        </tr>

</table>

**Example**：
```
at+set_config=lora:region:EU868\r\n
OK
```

:::tip NOTE
In the AS923 frequency band, the supported frequency plan is "as2" and the dwell time is set to 1.
:::

<br />

4. <b>at+get_config=lora:channel</b>

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

With <b>*0,on,868100000,0,5</b> as an example，the following is the channel parameter analysis:

- `*` at the beginning, if the channel is open;
- `0` is the channel ID;
- `on` indicates the current status of the channel;
- `868100000` is the actual frequency of the channel，unit is Hz;
- `0,5` indicates the DR of the channel, DR0~DR5.

:::

<br />

5. <b>at+set_config=lora:ch_mask:`<channel_number>:<status>`</b>

This command is used to enable (on) or disable (off) a channel in the current region.

| Operation | Command                                                | Response |
| --------- | ------------------------------------------------------ | -------- |
| Write     | `at+set_config=lora:ch_mask:<channel_number>:<status>` | OK       |

**Parameter**：

<table>
        <tr>
            <td>channel_number</td>
            <td>Channel number</td>
        </tr>
        <tr>
            <td>status</td>
            <td>0: off<br />1: on</td>
        </tr>

</table>

**Example**:
```
at+set_config=lora:ch_mask:0:0\r\n
OK
```

<br />

6. <b>at+set_config=lora:dev_eui:`<dev_eui>`</b>

This command is used to set the Device EUI parameter for LoRaWAN OTAA mode.

| Operation | Command                                | Response |
| --------- | -------------------------------------- | -------- |
| Write     | `at+set_config=lora:dev_eui:<dev_eui>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>dev_eui</td>
            <td>Device EUI</td>
        </tr>

</table>

**Example**：
```
at+set_config=lora:dev_eui:3530353064377716\r\n
OK
```

<br />

7.  <b>at+set_config=lora:app_eui:`<app_eui>`</b>

This command is used to set the Application EUI parameter for the LoRaWAN OTAA mode.

| Operation | Command                                | Response |
| --------- | -------------------------------------- | -------- |
| Write     | `at+set_config=lora:app_eui:<app_eui>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>app_eui</td>
            <td>Application EUI</td>
        </tr>

</table>

:::tip NOTE
All zero value Application EUI `at+set_config=lora:app_eui:0000000000000000` is **not supported** and will return error.
:::

**Example**：
```
at+set_config=lora:app_eui:0000000000000001\r\n
OK
```

<br />

8. <b>at+set_config=lora:app_key:`<app_key>`</b>

This command is used to set the Application Key parameter for the LoRaWAN OTAA mode.

| Operation | Command                                | Response |
| --------- | -------------------------------------- | -------- |
| Write     | `at+set_config=lora:app_key:<app_key>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>app_key</td>
            <td>Application Key</td>
        </tr>

</table>

**Example**：
```
at+set_config=lora:app_key:841986913ACD00BBC2BE2479D70F3228\r\n
OK
```

<br />

9. <b>at+set_config=lora:dev_addr:`<dev_addr>`</b>

This command is used to set the Device Address parameter for the LoRaWAN ABP mode.

| Operation | Command                                  | Response |
| --------- | ---------------------------------------- | -------- |
| Write     | `at+set_config=lora:dev_addr:<dev_addr>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>dev_addr</td>
            <td>Device Address</td>
        </tr>

</table>

**Example**：
```
at+set_config=lora:dev_addr:260125D7\r\n
OK
```

<br />

10. <b>at+set_config=lora:apps_key:`<apps_key>`</b>

This command is used to set the Application Session Key parameter for the LoRaWAN ABP mode.

| Operation | Command                                  | Response |
| --------- | ---------------------------------------- | -------- |
| Write     | `at+set_config=lora:apps_key:<apps_key>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>apps_key</td>
            <td>Application Session Key</td>
        </tr>

</table>

**Example**：
```
at+set_config=lora:apps_key:841986913ACD00BBC2BE2479D70F3228\r\n
OK
```

<br />

11. <b>at+set_config=lora:nwks_key:`<nwks_key>`</b>

This command is used to set the Network Session Key parameter for the LoRaWAN ABP mode.

| Operation | Command                                  | Response |
| --------- | ---------------------------------------- | -------- |
| Read      | `at+set_config=lora:nwks_key:<nwks_key>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>nwks_key</td>
            <td>Network Session Key</td>
        </tr>

</table>

**Example**：
```
at+set_config=lora:nwks_key:69AF20AEA26C01B243945A28C9172B42\r\n
OK
```

<br />

12. <b>at+set_config=lora:multicastenable:`<IsEnable>`</b>

This command is used to enable or disable the multicast feature.

| Operation | Command                                         | Response |
| --------- | ----------------------------------------------- | -------- |
| Write     | `at+set_config=lora:multicastenable:<IsEnable>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>IsEnable</td>
            <td>0: disable<br />1: enable<br />The default is disable.</td>
        </tr>

</table>

**Example**：
```
at+set_config=lora:multicastenable:1\r\n
OK
```
<br />

13. <b>at+set_config=lora:multicast_dev_addr:`<multicast_dev_addr>`</b>

This command is used to set the Device Address for the multicast feature.

| Operation | Command                                                      | Response |
| --------- | ------------------------------------------------------------ | -------- |
| Write     | `at+set_config=lora:multicast_dev_addr:<multicast_dev_addr>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>multicast_dev_addr</td>
            <td>Multicast Device Address</td>
        </tr>

</table>

**Example**：
```
at+set_config=lora:multicast_dev_addr:260111fd\r\n
OK
```

<br />

14. <b>at+set_config=lora:multicast_apps_key:`<multicast_apps_key>`</b>

This command is used to set the Application Session Key for the multicast feature.

| Operation | Command                                                      | Response |
| --------- | ------------------------------------------------------------ | -------- |
| Write     | `at+set_config=lora:multicast_apps_key:<multicast_apps_key>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>multicast_apps_key</td>
            <td>Multicast Application Session Key</td>
        </tr>

</table>

**Example**：
```
at+set_config=lora:multicast_apps_key:F13DDFA2619B10411F02F042E1C0F356\r\n
OK
```

<br />

15. <b>at+set_config=lora:multicast_nwks_key:`<multicast_nwks_key>`</b>

This command is used to set the Network Session Key for the multicast feature.

| Operation | Command                                                      | Response |
| --------- | ------------------------------------------------------------ | -------- |
| Write     | `at+set_config=lora:multicast_nwks_key:<multicast_nwks_key>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>multicast_nwks_key</td>
            <td>Multicast Network Session Key</td>
        </tr>

</table>

**Example**：
```
at+set_config=lora:multicast_nwks_key:1D1991F5377C675879C39B6908D437A6\r\n
OK
```

<br />

16. <b>at+set_config=lora:join_mode:`<mode>`</b>

This command is used to switch the LoRaWAN access mode between the OTAA and the ABP mode.

| Operation | Command                               | Response |
| --------- | ------------------------------------- | -------- |
| Write     | `at+set_config=lora:join_mode:<mode>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>mode</td>
            <td>Activation mode<br />0: OTAA<br />1: ABP <br />The default is OTAA.</td>
        </tr>

</table>

**Example**：
```
at+set_config=lora:join_mode:1\r\n
OK
```

<br />

17. <b>at+set_config=lora:class:`<class>`</b>

This command is used to set LoRaWAN class to Class A, Class B, or Class C.

| Operation | Command                            | Response |
| --------- | ---------------------------------- | -------- |
| Write     | `at+set_config=lora:class:<class>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>class</td>
            <td>0: Class A<br />1: Class B  (Not supported at this time.)<br />2: Class C<br />The default is Class A.</td>
        </tr>

</table>

**Example**：
```
at+set_config=lora:join_mode:1\r\n
OK
```

<br />

18. <b>at+set_config=lora:confirm:`<type>`</b>

This command is used to set the type data to be sent: Confirmed/Unconfirmed.

| Operation | Command                             | Response |
| --------- | ----------------------------------- | -------- |
| Write     | `at+set_config=lora:confirm:<type>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>type</td>
            <td>0: unconfirm type<br />1: confirm type<br />The default is unconfirm type.</td>
        </tr>

</table>

**Example**：
```
at+set_config=lora:confirm:0\r\n
OK
```

<br />

19. <b>at+set_config=lora:dr:`<dr>`</b>

This command is used to set the data rate (DR) of LoRa.

| Operation | Command                      | Response |
| --------- | ---------------------------- | -------- |
| Write     | `at+set_config=lora:dr:<dr>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>dr</td>
            <td>The data rate of LoRa depends on the specific region. In most LoRa regions, data rates commonly range from 0 to 5. For detailed information, refer to the LoRaWAN 1.0.2 specification.</td>
        </tr>

</table>

<br />

20. <b>at+set_config=lora:tx_power:`<tx_power>`</b>

This command is used to set the RF transmission power level of the LoRa transceiver.

| Operation | Command                                  | Response |
| --------- | ---------------------------------------- | -------- |
| Write     | `at+set_config=lora:tx_power:<tx_power>` | OK       |

**Parameter**:

<table>
    <tr>
      <td>tx_power </td>
      <td> Refer to <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4600-breakout-board/at-command-manual/#appendix-ii-tx-power-by-region" >Appendix II</a> for possible values of tx_power. The table of Appendix II is based on LoRaWAN 1.0.2 specification. LoRa transmit power level varies depending on frequency band.  <br />If the resulting TX power is higher than the capability of LoRa Radio, the output power will be based on the max TX power of the LoRa Radio in the module. For RAK4600 module, the max TX power is 20&nbsp;dBm. Take note of this when using regional bands with MaxEIRP higher than 20&nbsp;dBm like US915, AU915 and IN865 whose MaxEIRP is 30&nbsp;dBm.<br /> The default setting is 0.</td>
     </tr>
</table>

**Example**：

```
at+set_config=lora:tx_power:0\r\n
OK
```
<br />

21. <b>at+set_config=lora:adr:`<status>`</b>

This command is used to turn on/off the ADR feature of the LoRa communication.

| Operation | Command                           | Response |
| --------- | --------------------------------- | -------- |
| Write     | `at+set_config=lora:adr:<status>` | OK       |

**Parameter**：

<table>
        <tr>
            <td>status</td>
            <td>0: Turn off<br />1: Turn on<br />The default is on.</td>
        </tr>

</table>

**Example**：
```
at+set_config=lora:adr:0\r\n
OK
```

<br />

22. <b>at+get_config=lora:status</b>

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

<br />

23. <b>at+set_config=lora:dutycycle_enable:`<status>`</b>

This command is used to enable or disable the Duty Cycle feature.

| Operation | Command                                        | Response |
| --------- | ---------------------------------------------- | -------- |
| Write     | `at+set_config=lora:dutycycle_enable:<status>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>status</td>
            <td>0: disable<br />1: enable<br />The default is disable.</td>
        </tr>

</table>

**Example**：
```
at+set_config=lora:dutycycle_enable:1\r\n
OK
```

<br />

24. <b>at+set_config=lora:send_repeat_cnt:`<num>`</b>

This command is used to set the number of retransmitting attempts on an uplink message. When activated, the board will resend a message if its corresponding ACK (downlink) is not received after sending a confirmed uplink message. The default value is 0, which means that the board will not resend any message by default.

| Operation | Command                                       | Response |
| --------- | --------------------------------------------- | -------- |
| Write     | `at+set_config=lora:send_repeat_cnt:<status>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>num</td>
            <td>Number of retries, up to 7.<br />The default is 0.</td>
        </tr>

</table>

**Example**：
```
at+set_config=lora:send_repeat_cnt:1\r\n
OK
```

<br />

25. <b>at+set_config=lora:default_parameters</b>

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

1. <b>at+set_config=lora:work_mode:`<mode>`</b>

This command is used to switch the LoRa work mode between the LoRaWAN and the LoRa P2P mode. This command will cause the module to restart.

| Operation | Command                               | Response |
| --------- | ------------------------------------- | -------- |
| Write     | `at+set_config=lora:work_mode:<mode>` |          |

**Parameter**：
<table>
        <tr>
            <td>mode</td>
            <td>LoRa work mode<br />0: LoRaWAN<br />1: LoRa P2P <br />The default is LoRaWAN mode.</td>
        </tr>

</table>

**Example**：
```
at+set_config=lora:work_mode:1\r\n
UART1 work mode: RUI_UART_NORMAL
Current work_mode:P2P
Initialization OK
```

<br />

2. <b>at+set_config=lorap2p:`<frequency>:<spreadfact>:<bandwidth>:<codingrate>:<preamlen>:<power>`</b>

This command is used to set the relevant parameters of LoRA P2P mode and is only valid when the LoRa work mode is changed to LoRa P2P before.

| Operation | Command                                                                                      | Response |
| --------- | -------------------------------------------------------------------------------------------- | -------- |
| Write     | `at+set_config=lorap2p:<frequency>:<spreadfact>:<bandwidth>:<codingrate>:<preamlen>:<power>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>frequency</td>
            <td>Frequency, the unit is Hz<br />The default is 869525000&nbsp;Hz.</td>
        </tr>
        <tr>
            <td>spreadfact</td>
            <td>Spreading factor<br />The default is 12.</td>
        </tr>
        <tr>
            <td>bandwidth</td>
            <td>0:  125&nbsp;kHz<br />1:  250&nbsp;kHz<br />2:  500&nbsp;kHz<br />The default is 0.</td>
        </tr>
        <tr>
            <td>codingrate</td>
            <td>1:  4/5<br />2:  4/6<br />3:  4/7<br />4:  4/8<br />The default is 1.</td>
        </tr>
        <tr>
            <td>preamble</td>
            <td>Preamble Length. 5~65535<br />The default is 8.</td>
        </tr>
        <tr>
            <td>power</td>
            <td>TX power. The unit is in dBm. 5~20<br />The default is 20.</td>
        </tr>

</table>

**Example**：
```
at+set_config=lorap2p:869525000:12:0:1:8:20\r\n
OK
```

<br />

3. <b>at+set_config=lorap2p:transfer_mode:`<mode>`</b>

This command is used to switch the state of the LoRa transceiver between sending and receiving. It is only valid when the LoRa mode has been set to LoRa P2P beforehand.

| Operation | Command                                      | Response |
| --------- | -------------------------------------------- | -------- |
| Write     | `at+set_config=lorap2p:transfer_mode:<mode>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>mode</td>
            <td>1: receiver mode<br />2: sender mode<br />The default is sender mode.</td>
        </tr>

</table>

**Example**：
```
at+set_config=lorap2p:transfer_mode:1\r\n
OK
```

<br />

4. <b>at+send=lorap2p:`<data>`</b>

This command is used to send data through LoRa P2P and is only valid when the LoRa work mode is set to LoRa P2P before.

| Operation | Command                  | Response |
| --------- | ------------------------ | -------- |
| Send      | `at+send=lorap2p:<data>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>data</td>
            <td>The data to be sent, and the format is hexadecimal. </td>
        </tr>

</table>

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

1. <b>at+set_config=ble:work_mode:`<mode>:<long_range>`</b>

This command is used to configure the BLE mode.

| Operation | Command                                           | Response |
| --------- | ------------------------------------------------- | -------- |
| Write     | `at+set_config=ble:work_mode:<mode>:<long_range>` | OK       |

**Parameter**：
<table>
        <tr>
            <td>mode</td>
            <td>BLE work mode.<br />0: Peripheral mode (Default)<br />1: Central mode<br />2: Beacon scan mode</td>
        </tr>
        <tr>
            <td>long_range</td>
            <td>Long-range enable, only ‘0’ can be selected because RAK4600 Breakout does not support this feature.</td>
        </tr>

</table>

**Example**：
```
at+set_config=ble:work_mode:0:0\r\n
OK
```

## Appendix I: Data Rate by Region

<b>EU433/EU868/AS923</b>

| Data Rate | Configuration             | Indicative Physical Bit Rate [bit/s] |
| --------- | ------------------------- | ------------------------------------ |
| 0         | LoRa: SF12 / 125&nbsp;kHz | 250                                  |
| 1         | LoRa: SF11 / 125&nbsp;kHz | 440                                  |
| 2         | LoRa: SF10 / 125&nbsp;kHz | 980                                  |
| 3         | LoRa: SF9 / 125&nbsp;kHz  | 1760                                 |
| 4         | LoRa: SF8 / 125&nbsp;kHz  | 3125                                 |
| 5         | LoRa: SF7 / 125&nbsp;kHz  | 5470                                 |
| 6         | LoRa: SF7 / 250&nbsp;kHz  | 11000                                |
| 7         | FSK: 50&nbsp;kbps         | 50000                                |
| 8 ~ 15    | RFU                       |                                      |

<br />

<b>CN470/KR920</b>

| Data Rate | Configuration             | Indicative Physical Bit Rate [bit/s] |
| --------- | ------------------------- | ------------------------------------ |
| 0         | LoRa: SF12 / 125&nbsp;kHz | 250                                  |
| 1         | LoRa: SF11 / 125&nbsp;kHz | 440                                  |
| 2         | LoRa: SF10 / 125&nbsp;kHz | 980                                  |
| 3         | LoRa: SF9 / 125&nbsp;kHz  | 1760                                 |
| 4         | LoRa: SF8 / 125&nbsp;kHz  | 3125                                 |
| 5         | LoRa: SF7 / 125&nbsp;kHz  | 5470                                 |
| 6 ~ 15    | RFU                       |                                      |

<br />

<b>US915</b>

| Data Rate | Configuration             | Indicative Physical Bit Rate [bit/s] |
| --------- | ------------------------- | ------------------------------------ |
| 0         | LoRa: SF10 / 125&nbsp;kHz | 980                                  |
| 1         | LoRa: SF9 / 125&nbsp;kHz  | 1760                                 |
| 2         | LoRa: SF8 / 125&nbsp;kHz  | 3125                                 |
| 3         | LoRa: SF7 / 125&nbsp;kHz  | 5470                                 |
| 4         | LoRa: SF8 / 500&nbsp;kHz  | 12500                                |
| 5 ~ 7     | RFU                       |                                      |
| 8         | LoRa: SF12 / 500&nbsp;kHz | 980                                  |
| 9         | LoRa: SF11 / 500&nbsp;kHz | 1760                                 |
| 10        | LoRa: SF10 / 500&nbsp;kHz | 3900                                 |
| 11        | LoRa: SF9 / 500&nbsp;kHz  | 7000                                 |
| 12        | LoRa: SF8 / 500&nbsp;kHz  | 12500                                |
| 13        | LoRa: SF7 / 500&nbsp;kHz  | 21900                                |
| 14 ~ 15   | RFU                       |                                      |

<br />

<b>AU915</b>

| Data Rate | Configuration             | Indicative Physical Bit Rate [bit/s] |
| --------- | ------------------------- | ------------------------------------ |
| 0         | LoRa: SF12 / 125&nbsp;kHz | 250                                  |
| 1         | LoRa: SF11 / 125&nbsp;kHz | 440                                  |
| 2         | LoRa: SF10 / 125&nbsp;kHz | 980                                  |
| 3         | LoRa: SF9 / 125&nbsp;kHz  | 1760                                 |
| 4         | LoRa: SF8 / 125&nbsp;kHz  | 3125                                 |
| 5         | LoRa: SF7 / 125&nbsp;kHz  | 5470                                 |
| 6         | LoRa: SF8 / 500&nbsp;kHz  | 12500                                |
| 7         | RFU                       | RFU                                  |
| 8         | LoRa: SF12 / 500&nbsp;kHz | 980                                  |
| 9         | LoRa: SF11 / 500&nbsp;kHz | 1760                                 |
| 10        | LoRa: SF10 / 500&nbsp;kHz | 3900                                 |
| 11        | LoRa: SF9 / 500&nbsp;kHz  | 7000                                 |
| 12        | LoRa: SF8 / 500&nbsp;kHz  | 12500                                |

<br />


<b>IN865</b>

| Data Rate | Configuration             | Indicative Physical Bit Rate [bit/s] |
| --------- | ------------------------- | ------------------------------------ |
| 0         | LoRa: SF12 / 125&nbsp;kHz | 250                                  |
| 1         | LoRa: SF11 / 125&nbsp;kHz | 440                                  |
| 2         | LoRa: SF10 / 125&nbsp;kHz | 980                                  |
| 3         | LoRa: SF9 / 125&nbsp;kHz  | 1760                                 |
| 4         | LoRa: SF8 / 125&nbsp;kHz  | 3125                                 |
| 5         | LoRa: SF7 / 125&nbsp;kHz  | 5470                                 |
| 6         | RFU                       | RFU                                  |
| 7         | FSK: 50&nbsp;kbps         | 50000                                |
| 8 ~ 15    | RFU                       | RFU                                  |

## Appendix II: TX Power by Region

<b>EU868</b>

By default, MaxEIRP is considered to be +16&nbsp;dBm.

| TXPower | Configuration (EIRP) |
| ------- | -------------------- |
| 0       | MaxEIRP              |
| 1       | MaxEIRP - 2&nbsp;dB  |
| 2       | MaxEIRP - 4&nbsp;dB  |
| 3       | MaxEIRP - 6&nbsp;dB  |
| 4       | MaxEIRP - 8&nbsp;dB  |
| 5       | MaxEIRP - 10&nbsp;dB |
| 6       | MaxEIRP - 12&nbsp;dB |
| 7       | MaxEIRP - 14&nbsp;dB |
| 8 ~ 15  | RFU                  |

<br />


<b>US915</b>

By default, MaxEIRP is considered to be +30&nbsp;dBm based on LoRa Alliance specification.
However, the module's max TX power is only up to 20&nbsp;dBm.

| TXPower | Configuration (Conducted Power) |
| ------- | ------------------------------- |
| 0       | MaxEIRP                         |
| 1       | MaxEIRP - 2&nbsp;dB             |
| 2       | MaxEIRP - 4&nbsp;dB             |
| 3 ~ 9   |                                 |
| 10      | 10&nbsp;dBm                     |
| 11 ~ 15 | RFU                             |

<br />


<b>AU915</b>

By default, MaxEIRP is considered to be +30&nbsp;dBm based on LoRa Alliance specification.
However, the module's max TX power is only up to 20&nbsp;dBm.

| TXPower | Configuration (EIRP) |
| ------- | -------------------- |
| 0       | MaxEIRP              |
| 1 ~ 10  | MaxEIRP - 2*TX Power |
| 11 ~ 10 | RFU                  |

<br />

<b>KR920</b>

By default, MaxEIRP is considered to be +14&nbsp;dBm.

| TXPower | Configuration (EIRP) |
| ------- | -------------------- |
| 0       | MaxEIRP              |
| 1       | MaxEIRP - 2&nbsp;dB  |
| 2       | MaxEIRP - 4&nbsp;dB  |
| 3       | MaxEIRP - 6&nbsp;dB  |
| 4       | MaxEIRP - 8&nbsp;dB  |
| 5       | MaxEIRP - 10&nbsp;dB |
| 6       | MaxEIRP - 12&nbsp;dB |
| 7       | MaxEIRP - 14&nbsp;dB |
| 8 ~ 15  | RFU                  |

<br />


<b>AS923</b>

By default, MaxEIRP shall be 16&nbsp;dBm.

| TXPower | Configuration (EIRP) |
| ------- | -------------------- |
| 0       | MaxEIRP              |
| 1       | MaxEIRP - 2&nbsp;dB  |
| 2       | MaxEIRP - 4&nbsp;dB  |
| 3       | MaxEIRP - 6&nbsp;dB  |
| 4       | MaxEIRP - 8&nbsp;dB  |
| 5       | MaxEIRP - 10&nbsp;dB |
| 6       | MaxEIRP - 12&nbsp;dB |
| 7       | MaxEIRP - 14&nbsp;dB |
| 8 ~ 15  | RFU                  |

<br />


<b>IN865</b>

By default, MaxEIRP is considered to be +30&nbsp;dBm based on LoRa Alliance specification.
However, the module's max TX power is only up to 20&nbsp;dBm.

| TXPower | Configuration (EIRP) |
| ------- | -------------------- |
| 0       | MaxEIRP              |
| 1       | MaxEIRP - 2&nbsp;dB  |
| 2       | MaxEIRP - 4&nbsp;dB  |
| 3       | MaxEIRP - 6&nbsp;dB  |
| 4       | MaxEIRP - 8&nbsp;dB  |
| 5       | MaxEIRP - 10&nbsp;dB |
| 6       | MaxEIRP - 12&nbsp;dB |
| 7       | MaxEIRP - 14&nbsp;dB |
| 8       | MaxEIRP - 16&nbsp;dB |
| 9       | MaxEIRP - 18&nbsp;dB |
| 10      | MaxEIRP - 20&nbsp;dB |
| 11 ~ 15 | RFU                  |

<br />

<b>CN470</b>

By default, MaxEIRP is considered to be +19.15&nbsp;dBm.

| TXPower | Configuration (EIRP) |
| ------- | -------------------- |
| 0       | MaxEIRP              |
| 1       | MaxEIRP - 2&nbsp;dB  |
| 2       | MaxEIRP - 4&nbsp;dB  |
| 3       | MaxEIRP - 6&nbsp;dB  |
| 4       | MaxEIRP - 8&nbsp;dB  |
| 5       | MaxEIRP - 10&nbsp;dB |
| 6       | MaxEIRP - 12&nbsp;dB |
| 7       | MaxEIRP - 14&nbsp;dB |
| 8 ~ 15  | RFU                  |

<br />

<b>EU433</b>

By default, MAxEIRP is considered to be +12.15&nbsp;dBm.

| TXPower | Configuration (EIRP) |
| ------- | -------------------- |
| 0       | MaxEIRP              |
| 1       | MaxEIRP - 2&nbsp;dB  |
| 2       | MaxEIRP - 4&nbsp;dB  |
| 3       | MaxEIRP - 6&nbsp;dB  |
| 4       | MaxEIRP - 8&nbsp;dB  |
| 5       | MaxEIRP - 10&nbsp;dB |
| 6 ~ 15  | RFU                  |

## Appendix III: Maximum Transmission Load by Region

:::tip NOTE
In the following list:

- **M**: The total length, including the MAC header.
- **N**: The maximum usable payload size for user data, excluding the MAC header.
::::

<b>EU868</b>

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

<br />

<b>US915</b>

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

<br />

<b>AU915</b>

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

<br />

<b>KR920</b>

| DataRate |      M      |      N      |
| :------: | :---------: | :---------: |
|    0     |     59      |     51      |
|    1     |     59      |     51      |
|    2     |     59      |     51      |
|    3     |     123     |     115     |
|    4     |     250     |     242     |
|    5     |     250     |     242     |
|  6 ~ 15  | Not Defined | Not Defined |

<br />

<b>AS923</b>

<table>
<thead>
  <tr>
    <th>DataRate</th>
    <th colspan = "2">Uplink MAC Payload Size (M)</th>
    <th colspan = "2">Downlink MAC Payload Size (M)</th>
  </tr>
</thead>
        <tr>
            <td></td>
            <td>UplinkDwellTime = 0</td>
            <td>UplinkDwellTime = 1</td>
            <td>DownlinkDwellTime = 0</td>
            <td>DownlinkDwellTime = 1</td>
        </tr>
        <tr>
            <td>0</td>
            <td>59</td>
            <td>N/A</td>
            <td>59</td>
            <td>N/A</td>
        </tr>
        <tr>
            <td>1</td>
            <td>59</td>
            <td>N/A</td>
            <td>59</td>
            <td>N/A</td>
        </tr>
        <tr>
            <td>2</td>
            <td>59</td>
            <td>19</td>
            <td>59</td>
            <td>19</td>
        </tr>
        <tr>
            <td>3</td>
            <td>123</td>
            <td>61</td>
            <td>123</td>
            <td>61</td>
        </tr>
        <tr>
            <td>4</td>
            <td>250</td>
            <td>133</td>
            <td>250</td>
            <td>133</td>
        </tr>
        <tr>
            <td>5</td>
            <td>250</td>
            <td>250</td>
            <td>250</td>
            <td>250</td>
        </tr>
        <tr>
            <td>6</td>
            <td>250</td>
            <td>250</td>
            <td>250</td>
            <td>250</td>
        </tr>
        <tr>
            <td>7</td>
            <td>250</td>
            <td>250</td>
            <td>250</td>
            <td>250</td>
        </tr>
        <tr>
            <td>8</td>
            <td colspan="2">RFU</td>
            <td colspan="2">RFU</td>
        </tr>

</table>

<br />


<b>IN865</b>

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

<br />


<b>CN470</b>

| DataRate |      M      |      N      |
| :------: | :---------: | :---------: |
|    0     |     59      |     51      |
|    1     |     59      |     51      |
|    2     |     59      |     51      |
|    3     |     123     |     115     |
|    4     |     250     |     242     |
|    5     |     250     |     242     |
|  6 ~ 15  | Not Defined | Not Defined |



<b>EU433</b>

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

The pin definition of the RAK4600 Breakout Board can be reviewed in the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4600-breakout-board/datasheet/#pin-definition" target="_blank">Pin Definition</a> section of the Datasheet.

The following is a summary of the pins on the RAK4270 Breakout Board:

:::tip NOTE
Not all pins of the RAK4600 module are exposed on the RAK4600 Breakout board header connectors. Below are the pins available on the RAK4600 Module that is on this Breakout board. For complete RAK4600 module pinouts information, refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak4600-module/datasheet/#pin-definition" target="_blank">datasheet</a>.
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

<RkBottomNav/>