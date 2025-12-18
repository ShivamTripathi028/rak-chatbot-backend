---
title: RAK11300 WisDuo LPWAN Module AT Command Manual
description: For easier use of your LoRaWAN module, a comprehensive list of commands for LoRa P2P and LoRaWAN communication is provided.  A serial communication interface is also presented for two-way communication with the RAK11300 WisDuo Module.
image: "https://images.docs.rakwireless.com/wisnode/rak11300-module/rak11300-module.png"
keywords:
    - wisduo
    - AT Command Manual
    - RAK11300
sidebar_label: AT Command Manual
slug: /product-categories/wisduo/rak11300-module/at-command-manual/
download: true
---

# RAK11300 WisDuo LPWAN Module AT Command Manual

## Introduction

The RAK11300 WisDuo LPWAN module is based on the Raspberry Pi RP2040 chip and SX1262 RF transceiver. It provides an easy-to-use, small, low-power solution for long-range wireless data applications. This module complies with LoRaWAN 1.0.2 Class A & C specifications. It can easily connect to various LoRaWAN server platforms such as TheThingsNetwork (TTN), ChirpStack, Helium, etc. It also supports LoRa point-to-point (P2P) communication, facilitating the quick implementation of customized long-range LoRa networks.

AT commands can be interfaced via USB (acting as a serial port, pins 2 **USB_DM** and 3 **USB_DP**) or via UART1 (pins 10 **TX1** and 9 **RX1**). The default AT command parameter is **115200/8-N-1**. Firmware upgrades are possible only via USB. To familiarize yourself with the module's pin distribution and find a reference application schematic , refer to the <a href="https://docs.rakwireless.com/product-categories/wisduo/rak11300-module/datasheet/" target="_blank">RAK11300 Module Datasheet</a>.

## AT Command Syntax

The AT command is based on ASCII characters. In general, the AT command starts with the prefix `AT` and ends with `<CR><LF>` (i.e., \r\n). For the rest of the document, the `\r\n` will be omitted for clarity.

The AT commands have the standard format “AT+XXX”, with XXX denoting the command.

There are four available command formats:

|   **AT COMMAND FORMAT**    |                  **Description**                  |
| :------------------------: | :-----------------------------------------------: |
|         `AT+XXX?`          | Provides a short description of the given command |
|         `AT+XXX=?`         |     Reading the current value on the command      |
| `AT+XXX=<input parameter>` |       Writing configuration on the command        |
|          `AT+XXX`          |               Used to run a command               |

The output of the commands is returned via UART.

The format of the reply is divided into two parts: returned value and the status return code.

:::tip NOTE

`<CR>` stands for “carriage return” and `<LF>` stands for “line feed”.

:::

1. **`<value><CR><LF>`** is the first reply when (**`AT+XXX?`**) command description or (**`AT+XXX=?`**) reading value is executed then it will be followed by the status return code. The formats with no return value like (**`AT+XXX=<input parameter>`**) writing configuration command and (**`AT+XXX`**) run command will just reply to the status return code.

2. **`<CR><LF><STATUS><CR><LF>`** is the second part of the reply which is the status return code.

The possible status codes are:

| **STATUS RETURN CODE** |               **Description**                |
| :--------------------: | :------------------------------------------: |
|          `OK`          |  Command executed correctly without error.   |
|     `+CME ERROR:1`     |   Generic error or input is not supported.   |
|     `+CME ERROR:2`     |             Command not allowed.             |
|     `+CME ERROR:5`     | The input parameter of the command is wrong. |
|     `+CME ERROR:6`     |          The parameter is too long.          |
|     `+CME ERROR:8`     |             Value out of range.              |

More details on each command description and examples are given in the remainder of this section.

:::tip NOTE

After changing LoRaWAN parameters, the device must be reset using either the `ATZ` command or the reset button.

The serial port connection is lost after the `ATZ` command or pressing the reset button. The connection must be re-established on the connected computer before log output can be viewed or AT commands can be entered again.

:::

## AT?

Description: Help

Returns a list of all available commands with a short description

| Command | Input Parameter |    Return Value    | Return Code |
| :-----: | :-------------: | :----------------: | :---------: |
|  `AT?`  |        -        | *List of commands* |    `OK`     |

```
AT?
AT?

+++++++++++++++
AT command list
+++++++++++++++
AT?     AT commands
ATR     Restore default
ATZ     ATZ Trig a MCU reset
AT+APPEUI       Get or set the application EUI
AT+APPKEY   Get or set the application key
AT+DEVEUI   Get or set the device EUI
AT+APPSKEY  Get or set the application session key
AT+NWKSKEY  Get or Set the network session key
AT+DEVADDR  Get or set the device address
AT+CFM  Get or set the confirm mode
AT+JOIN Join network
AT+NJS  Get the join status
AT+NJM  Get or set the network join mode
AT+SENDFREQ Get or Set the automatic send time
AT+SEND Send data
AT+ADR  Get or set the adaptive data rate setting
AT+CLASS    Get or set the device class
AT+DR   Get or Set the Tx DataRate=[0..7]
AT+TXP  Get or set the transmit power
AT+BAND Get and Set number corresponding to active regions
AT+MASK Get and Set channels mask
AT+BAT  Get battery level
AT+RSSI Last RX packet RSSI
AT+SNR  Last RX packet SNR
AT+VER  Get SW version
AT+STATUS   Show LoRaWAN status
+++++++++++++++

OK

```

----

## ATR

This command is used to restore all parameters to the initial default values of the module.

| Command | Input Parameter | Return Value | Return Code |
| :-----: | :-------------: | :----------: | :---------: |
| `ATR?`  |        -        |      -       |    `OK`     |
|  `ATR`  |        -        |      -       |    `OK`     |

----

## ATZ

Description: MCU reset

This command is used to trigger an MCU reset.

| Command | Input Parameter |       Return Value       | Return Code |
| :-----: | :-------------: | :----------------------: | :---------: |
| `ATZ?`  |        -        | `ATZ: Trig a MCU reset`  |    `OK`     |
|  `ATZ`  |        -        | *No return. MCU resets.* |    `OK`     |

----

## AT+APPEUI

Description: Application unique identifier

This command is used to access and configure the APPEUI.

|            Command            | Input Parameter |            Return Value             |       Return Code        |
| :---------------------------: | :-------------: | :---------------------------------: | :----------------------: |
|         `AT+APPEUI? `         |        -        | `AT+APPEUI`: Get or set the App Eui |           `OK`           |
|         `AT+APPEUI=?`         |        -        |             *< 8 hex >*             |           `OK`           |
| `AT+APPEUI=<Input Parameter>` |   *< 8 hex >*   |                  -                  | `OK` or `AT_PARAM_ERROR` |

**Examples**:

```
AT+APPEUI?

+APPEUI: Get or set the application EUI
OK

AT+APPEUI=?

AT+APPEUI:70b3d57ed00201e1
OK

AT+APPEUI=70b3d57ed00201e1

OK

AT+APPEUI=70b3d57ed00201eh

+CME ERROR:5
```

----

## AT+APPKEY

Description: Application key

This command is used to access and configure the APPKEY.

|            Command            | Input Parameter |                Return Value                 |       Return Code        |
| :---------------------------: | :-------------: | :-----------------------------------------: | :----------------------: |
|         `AT+APPKEY?`          |        -        | `AT+APPKEY`: Get or set the Application Key |           `OK`           |
|         `AT+APPKEY=?`         |        -        |                *< 16 hex >*                 |           `OK`           |
| `AT+APPKEY=<Input Parameter>` |  *< 16 hex >*   |                      -                      | `OK` or `AT_PARAM_ERROR` |

**Examples**:

```
AT+APPKEY?

AT+APPKEY: Get or set the application key
OK

AT+APPKEY=?

AT+APPKEY:2b84e0b09b68e5cb42176fe753dcee79
OK

AT+APPKEY=2b84e0b09b68e5cb42176fe753dcee79

OK

AT+APPKEY=2b84e0b09b68e5cb42176fe753dcee7x

+CME ERROR:5
```

----

## AT+DEVEUI

Description: Device EUI or DEVEUI

This command is used to access and configure the device EUI or DEVEUI.

|            Command            | Input Parameter |              Return Value              |       Return Code        |
| :---------------------------: | :-------------: | :------------------------------------: | :----------------------: |
|         `AT+DEVEUI?`          |        -        | `AT+DEVEUI`: Get or set the Device EUI |           `OK`           |
|         `AT+DEVEUI=?`         |        -        |              *< 8 hex >*               |           `OK`           |
| `AT+DEVEUI=<Input Parameter>` |   *< 8 hex >*   |                   -                    | `OK` or `AT_PARAM_ERROR` |

**Examples**:

```
AT+DEVEUI?

+DEVEUI: Get or set the device EUI
OK

AT+DEVEUI=?

+DEVEUI:ac1f09fffe03efdc
OK

AT+DEVEUI=ac1f09fffe03efdc

OK

AT+DEVEUI=ac1f09fffe03efdx

+CME ERROR:5
```

----

## AT+APPSKEY

Description: Application session key

This command is used to access and configure the application session key or APPSKEY.

|            Command             | Input Parameter |                     Return Value                     |       Return Code        |
| :----------------------------: | :-------------: | :--------------------------------------------------: | :----------------------: |
|         `AT+APPSKEY?`          |        -        | `AT+APPSKEY`: Get or set the Application Session Key |           `OK`           |
|         `AT+APPSKEY=?`         |        -        |                     *< 16 hex >*                     |           `OK`           |
| `AT+APPSKEY=<Input Parameter>` |  *< 16 hex >*   |                          -                           | `OK` or `AT_PARAM_ERROR` |

**Examples**:

```
AT+APPSKEY?

AT+APPSKEY: Get or set the application session key
OK

AT+APPSKEY=?

AT+APPSKEY:3f6a66459d5edca63cbc4619cd61a11e
OK

AT+APPSKEY=3f6a66459d5edca63cbc4619cd61a11e

OK

AT+APPSKEY=3f6a66459d5edca63cbc4619cd61a11x

+CME ERROR:5
```

----

## AT+NWKSKEY

Description: Network session keys

This command is used to access and configure the network session keys or NWKSKEY.

|            Command             | Input Parameter |                   Return Value                   |       Return Code        |
| :----------------------------: | :-------------: | :----------------------------------------------: | :----------------------: |
|         `AT+NWKSKEY?`          |        -        | `AT+NWKSKEY`: Get or set the Network Session Key |           `OK`           |
|         `AT+NWKSKEY=?`         |        -        |                   *< 16 hex >*                   |           `OK`           |
| `AT+NWKSKEY=<Input Parameter>` |  *< 16 hex >*   |                        -                         | `OK` or `AT_PARAM_ERROR` |

**Examples**:

```
AT+NWKSKEY?

AT+NWKSKEY: Get or Set the network session key
OK

AT+NWKSKEY=?

AT+NWKSKEY:323d155a000df335307a16da0c9df53f
OK

AT+NWKSKEY=323d155a000df335307a16da0c9df53f

OK

AT+NWKSKEY=323d155a000df335307a16da0c9df53f0

+CME ERROR:5
```

----

## AT+DEVADDR

Description: Device address or DEVADDR

This command is used to access and configure the device address or DEVADDR.

|            Command             | Input Parameter |                Return Value                 |       Return Code        |
| :----------------------------: | :-------------: | :-----------------------------------------: | :----------------------: |
|         `AT+DEVADDR?`          |        -        | `AT+DEVADDR`: Get or set the device address |           `OK`           |
|         `AT+DEVADDR=?`         |        -        |                 *< 4 hex >*                 |           `OK`           |
| `AT+DEVADDR=<Input Parameter>` |   *< 4 hex >*   |                      -                      | `OK` or `AT_PARAM_ERROR` |

**Examples**:

```
AT+DEVADDR?

AT+DEVADDR: Get or set the device address
OK

AT+DEVADDR=?

AT+DEVADDR:26021FB0

OK

AT+DEVADDR=26021FB0

OK

AT+DEVADDR=26021FBX

+CME ERROR:5
```

----

## AT+CFM

Description: Confirmed payload mode

This command is used to access and configure the type of payload of the device.

|          Command           | Input Parameter |               Return Value               |       Return Code        |
| :------------------------: | :-------------: | :--------------------------------------: | :----------------------: |
|         `AT+CFM?`          |        -        |  `AT+CFM`: Get or set the confirm mode   |           `OK`           |
|         `AT+CFM=?`         |        -        | **0** (Unconfirmed) or **1** (Confirmed) |           `OK`           |
| `AT+CFM=<Input Parameter>` | **0** or **1**  |                    -                     | `OK` or `AT_PARAM_ERROR` |

**Examples**:

```
AT+CFM?

AT+CFM: Get or set the confirm mode
OK

AT+CFM=?

AT+CFM:0
OK

AT+CFM=0

OK

AT+CFM=3

+CME ERROR:5
```

----

## AT+JOIN

Description: Join the LoRaWAN network

This command is used to join a LoRaWAN network.

| Command                     | Input Parameter                                                                                   | Return Value                     | Return Code             |
| --------------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------- | ----------------------- |
| `AT+JOIN? `                 | -                                                                                                 | `AT+JOIN`: Join network          | `OK`                    |
| `AT+JOIN=? `                | -                                                                                                 | *Param1, Param2, Param3, Param4* | `OK` or `AT_BUSY_ERROR` |
| `AT+JOIN=<Input Parameter>` | *Param1:Param2:Param3:Param4*                                                                     | -                                | `OK`                    |
|                             | *Param1* = **Join command**: 1 for joining the network, 0 for stop joining                        |                                  |                         |
|                             | *Param2* = **Auto-Join config**: 1 for Auto-join on power up, 0 for no auto-join. (0 is default) |                                  |                         |
|                             | *Param3* = **Reattempt interval**: 7 - 255 seconds (30 is default)                                |                                  |                         |
|                             | *Param4* = **No. of join attempts**: 0 - 255 (0 is default)                                       |                                  |                         |

:::tip NOTE
- This is an asynchronous command. `OK` means the device is joining. The completion of the JOIN can be verified with the `AT+NJS=?` command.
- Param3 is not yet supported and is always fixed at 30 seconds.
:::

**Examples**:

```
AT+JOIN?

AT+JOIN: Join network
OK

AT+JOIN=?

AT+JOIN=0:1:8:10
OK

AT+JOIN=1:1:8:10

OK

AT+JOIN=SUCCESS

AT+JOIN=3:1:8:10

+CME ERROR:5
```

----

## AT+NJS

Description: Network join status.

This command checks the device's connection status to a LoRaWAN network.

|  Command   | Input Parameter |             Return Value             | Return Code |
| :--------: | :-------------: | :----------------------------------: | :---------: |
| `AT+NJS?`  |        -        |    `AT+NJS`: Get the join status     |    `OK`     |
| `AT+NJS=?` |        -        | **0** (not joined) or **1** (joined) |    `OK`     |

**Examples**:

```
AT+NJS?

AT+NJS: Get the join status
OK

AT+NJS=?

AT+NJS:1
OK
```

----

## AT+NJM

Description: LoRaWAN network join mode.

This command accesses and configures the device's activation method: OTAA or ABP.  A value of 1 indicates OTAA join mode; a value of 0 indicates ABP join mode.

|          Command           | Input Parameter |                Return Value                |       Return Code        |
| :------------------------: | :-------------: | :----------------------------------------: | :----------------------: |
|         `AT+NJM? `         |        -        | `AT+NJM`: Get or set the network join mode |           `OK`           |
|         `AT+NJM=?`         |        -        |               **0** or **1**               |           `OK`           |
| `AT+NJM=<Input Parameter>` | **0** or **1**  |                     -                      | `OK` or `AT_PARAM_ERROR` |

**Examples**:

```
AT+NJM?

AT+NJM: Get or set the network join mode
OK

AT+NJM=?

AT+NJM:0
OK

AT+NJM=0

OK

AT+NJM=2

+CME ERROR:5
```

----

## AT+SENDFREQ

Description: Set the automatic transmission period.

This command sets the interval, in seconds, between automatic packet transmissions. Setting it to 0 disables automatic packet transmission.

|             Command             |    Input Parameter    |                   Return Value                    |       Return Code        |
| :-----------------------------: | :-------------------: | :-----------------------------------------------: | :----------------------: |
|         `AT+SENDFREQ?`          |           -           | `AT+SENDFREQ`: Get or set the automatic send time |           `OK`           |
|         `AT+SENDFREQ=?`         |           -           |               `<period in seconds>`               |           `OK`           |
| `AT+SENDFREQ=<Input Parameter>` | `<period in seconds>` |                         -                         | `OK` or `AT_PARAM_ERROR` |

**Examples**:

```
AT+SENDFREQ?

AT+SENDFREQ: Get or Set the automatic send time
OK

AT+SENDFREQ=?

AT+SENDFREQ:60
OK

AT+SENDFREQ=60

OK
```

----

## AT+SEND

Description: Send payload data.

This command sends LoRaWAN payload data to a specific port.

| Command                     | Input Parameter | Return Value         | Return Code                                                        |
| --------------------------- | --------------- | -------------------- | ------------------------------------------------------------------ |
| `AT+SEND?`                  | -               | `AT+SEND`: Send data | `OK`                                                               |
| `AT+SEND=<Input Parameter>` | `port:payload`  | -                    | `OK`, `AT_NO_NETWORK_JOINED`, `AT_PARAM_ERROR`, or `AT_BUSY_ERROR` |

**Examples**:
```
AT+SEND?

AT+SEND: Send data
OK
```

Unconfirmed Payload
```
AT+SEND=2:1234

OK

AT+SEND=SUCCESS
```

Confirm Payload
```
AT+SEND=2:1234

OK

AT+SEND=SUCCESS
```
Downlink packet received

:::tip NOTE

- If there is a pending downlink message from the LNS (LoRaWAN Network Server), the downlink payload will be received after the `AT+SEND` command with the format `<fport>:<data length>:<rssi>:<snr>:<data>`.

- In this example, the format has the corresponding values:
  - **fport**: 2
  - **data length**: 6
  - **rssi**: -46 dBm
  - **snr**: 11 dB
  - **data payload**: 48656C6C6F0A

:::

```
AT+SEND=5:10AAFF45

OK

AT+SEND=SUCCESS
RX:2:6:-46:11:48656C6C6F0A
OK
```

----

## AT+ADR

Description: Adaptive data rate.

This command is used to access and configure the module's adaptive data rate.

|          Command           | Input Parameter |                    Return Value                     |       Return Code        |
| :------------------------: | :-------------: | :-------------------------------------------------: | :----------------------: |
|         `AT+ADR?`          |        -        | `AT+ADR`: Get or set the Adaptive Data Rate setting |           `OK`           |
|         `AT+ADR=?`         |        -        |          **0** (ADR off) or **1** (ARD on)          |           `OK`           |
| `AT+ADR=<Input Parameter>` | **0** or **1**  |                          -                          | `OK` or `AT_PARAM_ERROR` |

**Examples**:

```
AT+ADR?

+ADR: Get or set the adaptive data rate setting
OK

AT+ADR=?

AT+ADR:0
OK

AT+ADR=0

OK

AT+ADR=3

+CME ERROR:5
```

----

## AT+CLASS

Description: LoRaWAN class.

This command is used to access and configure the LoRaWAN class of the module.

|           Command            | Input Parameter |                   Return Value                    |       Return Code        |
| :--------------------------: | :-------------: | :-----------------------------------------------: | :----------------------: |
|         `AT+CLASS?`          |        -        | `AT+CLASS`: Get or set the Device Class (A, B, C) |           `OK`           |
|         `AT+CLASS=?`         |        -        |         **A** or **C** (B not supported)          |           `OK`           |
| `AT+CLASS=<Input Parameter>` | **A** or **C**  |                         -                         | `OK` or `AT_PARAM_ERROR` |

_**This FW of the device supports the LoRaWAN V1.0.2 stack**_.

**Examples**:

```
AT+CLASS?

+CLASS: Get or set the device class
OK

AT+CLASS=?

AT++CLASS:A
OK

AT+CLASS=A

OK

AT+CLASS=F

+CME ERROR:5
```

----

## AT+DR

Description: Data rate settings.

This command is used to access and configure data rate settings.

|          Command          |         Input Parameter         |                    Return Value                     |       Return Code        |
| :-----------------------: | :-----------------------------: | :-------------------------------------------------: | :----------------------: |
|         `AT+DR?`          |                -                | `AT+DR=<DataRate><CR>`: Get or set the Tx Data Rate |           `OK`           |
|         `AT+DR=?`         |                -                |           `0`,`1`,`2`,`3`,`4`,`5`,`6`,`7`           |           `OK`           |
| `AT+DR=<Input Parameter>` | `0`,`1`,`2`,`3`,`4`,`5`,`6`,`7` |                          -                          | `OK` or `AT_PARAM_ERROR` |

Check <a href="https://docs.rakwireless.com/product-categories/wisduo/rak11300-module/at-command-manual/#appendix-i-data-rate-by-region" target="_blank">Appendix I</a> for the input parameter depending on the frequency band selected.

**Examples**:

```
AT+DR?

AT+DR: Get or Set the Tx DataRate=[0..7]
OK

AT+DR=?

AT+DR:3
OK

AT+DR=3

OK
```

----

## AT+TXP

Description: Transmit Power.

This command is used to access and configure the transmit power.

|          Command           | Input Parameter |              Return Value               |       Return Code        |
| :------------------------: | :-------------: | :-------------------------------------: | :----------------------: |
|         `AT+TXP?`          |        -        | `AT+TXP`: Get or set the transmit power |           `OK`           |
|         `AT+TXP=?`         |        -        |               *< value >*               | `OK` or `AT+PARAM_ERROR` |
| `AT+TXP=<Input Parameter>` |   *< value >*   |                    -                    | `OK` or `AT_PARAM_ERROR` |

Check <a href="https://docs.rakwireless.com/product-categories/wisduo/rak11300-module/at-command-manual/#appendix-ii-tx-power-by-region" target="_blank">Appendix II</a> for the input parameter depending on the frequency band selected.

For example, at EU868, a value of 2 represents **MaxEIRP - 4 dB** where MaxEIRP = +16 dBm.

**Examples**:

```
AT+TXP?

AT+TXP: Get or set the transmit power
OK

AT+TXP=?

AT+TXP:0
OK

AT+TXP=0

OK
```

----

## AT+BAND

Description: Regional frequency band.

This command is used to access and configure the regional frequency band.

|           Command           | Input Parameter |                            Return Value                            |       Return Code        |
| :-------------------------: | :-------------: | :----------------------------------------------------------------: | :----------------------: |
|         `AT+BAND?`          |        -        |   `AT+BAND`: Get and Set number corresponding to active regions    |           `OK`           |
|         `AT+BAND=?`         |        -        | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12` |           `OK`           |
| `AT+BAND=<Input Parameter>` |  *< 0 to 12 >*  |                                 -                                  | `OK` or `AT_PARAM_ERROR` |

**List of Band Parameter Options**

| Code  | Regional Band |       | Code  | Regional Band |
| :---: | :-----------: | :---: | :---: | :-----------: |
|   0   |    AS923-1    |       |   7   |     IN865     |
|   1   |     AU915     |       |   8   |     US915     |
|   2   |     CN470     |       |   9   |    AS923-2    |
|   3   |     CN779     |       |  10   |    AS923-3    |
|   4   |     EU433     |       |  11   |    AS923-4    |
|   5   |     EU868     |       |  12   |     RU864     |
|   6   |     KR920     |       |       |               |

**Examples**:

```
AT+BAND?

AT+BAND: Get and Set number corresponding to active regions
OK

AT+BAND=?

AT+BAND:10
OK

AT+BAND=10

OK

AT+BAND=22

+CME ERROR:8
```

----

## AT+MASK

Description: Regional channel mask.

This command accesses and configures the regional channel mask. Channel masks can only be set for these regions: AU915, CN470, and US915.

|           Command           | Input Parameter |                         Return Value                          |       Return Code        |
| :-------------------------: | :-------------: | :-----------------------------------------------------------: | :----------------------: |
|         `AT+MASK?`          |        -        |             `AT+MASK: Get and Set channels mask`              |           `OK`           |
|         `AT+MASK=?`         |        -        | `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12` |           `OK`           |
| `AT+MASK=<Input Parameter>` |  *< 0 to 12 >*  |                               -                               | `OK` or `AT_PARAM_ERROR` |

**List of mask channels per region**

| **Mask (Sub-Band)** | **US915** | **AU915** | **CN470** |
| :-----------------: | :-------: | :-------: | :-------: |
|          1          |    0-7    |    0-7    |    0-7    |
|          2          |   8-15    |   8-15    |   8-15    |
|          3          |   16-23   |   16-23   |   16-23   |
|          4          |   24-31   |   24-31   |   24-31   |
|          5          |   32-39   |   32-39   |   32-39   |
|          6          |   40-47   |   40-47   |   40-47   |
|          7          |   48-55   |   48-55   |   48-55   |
|          8          |   56-63   |   56-63   |   56-63   |
|          9          |     -     |     -     |   64-71   |
|         10          |     -     |     -     |   72-79   |
|         11          |     -     |     -     |   80-87   |
|         12          |     -     |     -     |   88-95   |

**Examples**:

```
AT+MASK?

AT+MASK: Get and Set channels mask
OK

AT+MASK=?

AT+MASK:10
OK

AT+MASK=10

OK

AT+MASK=13

+CME ERROR:8
```

----

## AT+BAT

Description: Read the battery voltage.

This command reads the device's battery voltage.

|  Command   | Input Parameter |        Return Value         |       Return Code        |
| :--------: | :-------------: | :-------------------------: | :----------------------: |
| `AT+BAT?`  |        -        | `AT+BAT`: Get battery level |           `OK`           |
| `AT+BAT=?` |        -        |         *< value >*         | `OK` or `AT+PARAM_ERROR` |

:::tip NOTE

_**The battery level is returned as a value between 0 and 255**_.

:::

**Examples**:

```
AT+BAT?

+BAT:"Get battery level"
OK

AT+BAT=?

+BAT:254
OK
```

----

## AT+RSSI

Description: Receive signal strength indicator.

This command retrieves the RSSI value of the last received packet.

|   Command   | Input Parameter |                    Return Value                     | Return Code |
| :---------: | :-------------: | :-------------------------------------------------: | :---------: |
| `AT+RSSI?`  |        -        | `AT+RSSI`: Get the RSSI of the last received packet |    `OK`     |
| `AT+RSSI=?` |        -        |                *< integer > in dBm*                 |    `OK`     |

:::tip NOTE

The reply will be **'0'** if there is no last packet received yet.

:::

**Examples**:

```
AT+RSSI?

AT+RSSI: Last RX packet RSSI
OK

AT+RSSI=?

AT+RSSI:-41
OK
```

----

## AT+SNR

Description: Signal-to-Noise Ratio

This command retrieves the SNR value of the last received packet.

|  Command   | Input Parameter |                   Return Value                    | Return Code |
| :--------: | :-------------: | :-----------------------------------------------: | :---------: |
| `AT+SNR?`  |        -        | `AT+SNR`: Get the SNR of the last received packet |    `OK`     |
| `AT+SNR=?` |        -        |                *< integer >* in dB                |    `OK`     |

:::tip NOTE

The reply will be **'0'** if there is no last packet received yet.

:::

**Examples**:

```
AT+SNR?

AT+SNR: Last RX packet SNR
OK

AT+SNR=?

AT+SNR:11
OK
```

----

## AT+VER

Description: Firmware version

This command retrieves the device's installed firmware version.

|  Command   | Input Parameter |               Return Value                | Return Code |
| :--------: | :-------------: | :---------------------------------------: | :---------: |
| `AT+VER?`  |        -        | `AT+VER`: Get the version of the firmware |    `OK`     |
| `AT+VER=?` |        -        |                *< V.x.y >*                |    `OK`     |

**Examples**:

```
AT+VER?

AT+VER: Get SW version
OK

AT+VER=?

AT+VER:1.0.0.0 May 27 2021 17:11:12
OK
```

----

## AT+STATUS

Description: Show device status.

This command retrieves the current device status.

|    Command    | Input Parameter |           Return Value           | Return Code |
| :-----------: | :-------------: | :------------------------------: | :---------: |
| `AT+STATUS?`  |        -        | `AT+STATUS`: Show LoRaWAN status |    `OK`     |
| `AT+STATUS=?` |        -        |           *< status >*           |    `OK`     |

**Examples**:

```
AT+STATUS?

AT+STATUS: Show LoRaWAN status
OK

AT+STATUS=?
LoRaWAN status:
   Auto join disabled
   OTAA enabled
   Dev EUI 5032333338350012
   App EUI 1200353833333250
   App Key 50323333383500121200353833333250
   NWS Key 50323333383500121200353833333250
   Apps Key 50323333383500121200353833333250
   Dev Addr 83986D12
   Repeat time 120000
   ADR disabled
   Public Network
   Dutycycle disabled
   Join trials 10
   TX Power 0
   DR 3
   Class 0
   Subband 1
   Fport 2
   Unconfirmed Message
   Region 10
   Network joined
   Mode User

+STATUS:
OK
```

----

## Appendix

### Appendix I Data Rate by Region

** EU433/EU868/RU864/AS923 **

| Data Rate |       Configuration       | Indicative Physical Bit Rate [bit/s] |
| :-------: | :-----------------------: | :----------------------------------: |
|     0     | LoRa: SF12 / 125 kHz |                 250                  |
|     1     | LoRa: SF11 / 125 kHz |                 440                  |
|     2     | LoRa: SF10 / 125 kHz |                 980                  |
|     3     | LoRa: SF9 / 125 kHz  |                 1760                 |
|     4     | LoRa: SF8 / 125 kHz  |                 3125                 |
|     5     | LoRa: SF7 / 125 kHz  |                 5470                 |
|     6     | LoRa: SF7 / 250 kHz  |                11000                 |
|     7     |     FSK: 50 kbps     |                50000                 |
|  8 ~ 15   |            RFU            |                                      |

** CN470/KR920 **

| Data Rate |       Configuration       | Indicative Physical Bit Rate [bit/s] |
| :-------: | :-----------------------: | :----------------------------------: |
|     0     | LoRa: SF12 / 125 kHz |                 250                  |
|     1     | LoRa: SF11 / 125 kHz |                 440                  |
|     2     | LoRa: SF10 / 125 kHz |                 980                  |
|     3     | LoRa: SF9 / 125 kHz  |                 1760                 |
|     4     | LoRa: SF8 / 125 kHz  |                 3125                 |
|     5     | LoRa: SF7 / 125 kHz  |                 5470                 |
|  6 ~ 15   |            RFU            |                                      |

** US915 **

| Data Rate |       Configuration       | Indicative Physical Bit Rate [bit/s] |
| :-------: | :-----------------------: | :----------------------------------: |
|     0     | LoRa: SF10 / 125 kHz |                 980                  |
|     1     | LoRa: SF9 / 125 kHz  |                 1760                 |
|     2     | LoRa: SF8 / 125 kHz  |                 3125                 |
|     3     | LoRa: SF7 / 125 kHz  |                 5470                 |
|     4     | LoRa: SF8 / 500 kHz  |                12500                 |
|   5 ~ 7   |            RFU            |                                      |
|     8     | LoRa: SF12 / 500 kHz |                 980                  |
|     9     | LoRa: SF11 / 500 kHz |                 1760                 |
|    10     | LoRa: SF10 / 500 kHz |                 3900                 |
|    11     | LoRa: SF9 / 500 kHz  |                 7000                 |
|    12     | LoRa: SF8 / 500 kHz  |                12500                 |
|    13     | LoRa: SF7 / 500 kHz  |                21900                 |
|  14 ~ 15  |            RFU            |                                      |

** AU915 **

| Data Rate |       Configuration       | Indicative Physical Bit Rate [bit/s] |
| :-------: | :-----------------------: | :----------------------------------: |
|     0     | LoRa: SF12 / 125 kHz |                 250                  |
|     1     | LoRa: SF11 / 125 kHz |                 440                  |
|     2     | LoRa: SF10 / 125 kHz |                 980                  |
|     3     | LoRa: SF9 / 125 kHz  |                 1760                 |
|     4     | LoRa: SF8 / 125 kHz  |                 3125                 |
|     5     | LoRa: SF7 / 125 kHz  |                 5470                 |
|     6     | LoRa: SF8 / 500 kHz  |                12500                 |
|     7     |            RFU            |                 RFU                  |
|     8     | LoRa: SF12 / 500 kHz |                 980                  |
|     9     | LoRa: SF11 / 500 kHz |                 1760                 |
|    10     | LoRa: SF10 / 500 kHz |                 3900                 |
|    11     | LoRa: SF9 / 500 kHz  |                 7000                 |
|    12     | LoRa: SF8 / 500 kHz  |                12500                 |

** IN865 **

| Data Rate |       Configuration       | Indicative Physical Bit Rate [bit/s] |
| :-------: | :-----------------------: | :----------------------------------: |
|     0     | LoRa: SF12 / 125 kHz |                 250                  |
|     1     | LoRa: SF11 / 125 kHz |                 440                  |
|     2     | LoRa: SF10 / 125 kHz |                 980                  |
|     3     | LoRa: SF9 / 125 kHz  |                 1760                 |
|     4     | LoRa: SF8 / 125 kHz  |                 3125                 |
|     5     | LoRa: SF7 / 125 kHz  |                 5470                 |
|     6     |            RFU            |                 RFU                  |
|     7     |     FSK: 50 kbps     |                50000                 |
|  8 ~ 15   |            RFU            |                 RFU                  |

----

### Appendix II TX Power by Region

** EU868 **

By default, MaxEIRP is considered to be +16 dBm.

| TXPower | Configuration (EIRP) |
| :-----: | :------------------: |
|    0    |       MaxEIRP        |
|    1    | MaxEIRP - 2 dB  |
|    2    | MaxEIRP - 4 dB  |
|    3    | MaxEIRP - 6 dB  |
|    4    | MaxEIRP - 8 dB  |
|    5    | MaxEIRP - 10 dB |
|    6    | MaxEIRP - 12 dB |
|    7    | MaxEIRP - 14 dB |
| 8 ~ 15  |         RFU          |

** US915 **

| TXPower | Configuration (Conducted Power) |
| :-----: | :-----------------------------: |
|    0    |     30 dBm - 2*TXpower     |
|    1    |           28 dBm           |
|    2    |           26 dBm           |
|  3 ~ 9  |                -                |
|   10    |           10 dBm           |
| 11 ~ 15 |               RFU               |

** AU915 **

By default, MaxEIRP is considered to be +30 dBm.

| TXPower | Configuration (EIRP) |
| :-----: | :------------------: |
|    0    |       MaxEIRP        |
| 1 ~ 10  | MaxEIRP - 2*TXPower  |
| 11 ~ 10 |         RFU          |

** KR920 **

By default, MaxEIRP is considered to be +14 dBm.

| TXPower | Configuration (EIRP) |
| :-----: | :------------------: |
|    0    |       MaxEIRP        |
|    1    | MaxEIRP - 2 dB  |
|    2    | MaxEIRP - 4 dB  |
|    3    | MaxEIRP - 6 dB  |
|    4    | MaxEIRP - 8 dB  |
|    5    | MaxEIRP - 10 dB |
|    6    | MaxEIRP - 12 dB |
|    7    | MaxEIRP - 14 dB |
| 8 ~ 15  |         RFU          |

** AS923 **

By default, Max EIRP is considered to be 16 dBm.

| TXPower | Configuration (EIRP) |
| :-----: | :------------------: |
|    0    |       MaxEIRP        |
|    1    | MaxEIRP - 2 dB  |
|    2    | MaxEIRP - 4 dB  |
|    3    | MaxEIRP - 6 dB  |
|    4    | MaxEIRP - 8 dB  |
|    5    | MaxEIRP - 10 dB |
|    6    | MaxEIRP - 12 dB |
|    7    | MaxEIRP - 14 dB |
| 8 ~ 15  |         RFU          |

** IN865 **

By default, MaxEIRP is considered to be 30 dBm.

| TXPower | Configuration (EIRP) |
| :-----: | :------------------: |
|    0    |       MaxEIRP        |
|    1    | MaxEIRP - 2 dB  |
|    2    | MaxEIRP - 4 dB  |
|    3    | MaxEIRP - 6 dB  |
|    4    | MaxEIRP - 8 dB  |
|    5    | MaxEIRP - 10 dB |
|    6    | MaxEIRP - 12 dB |
|    7    | MaxEIRP - 14 dB |
|    8    | MaxEIRP - 16 dB |
|    9    | MaxEIRP - 18 dB |
|   10    | MaxEIRP - 20 dB |
| 11 ~ 15 |         RFU          |

** RU864 **

By default, MaxEIRP is considered to be +16 dBm.

| TXPower | Configuration (EIRP) |
| :-----: | :------------------: |
|    0    |       MaxEIRP        |
|    1    | MaxEIRP - 2 dB  |
|    2    | MaxEIRP - 4 dB  |
|    3    | MaxEIRP - 6 dB  |
|    4    | MaxEIRP - 8 dB  |
|    5    | MaxEIRP - 10 dB |
|    6    | MaxEIRP - 12 dB |
|    7    | MaxEIRP - 14 dB |
| 8 ~ 15  |         RFU          |

** CN470 **

By default, MaxEIRP is considered to be +19.15 dBm.

| TXPower | Configuration (EIRP) |
| :-----: | :------------------: |
|    0    |       MaxEIRP        |
|    1    |  MaxEIRP 2 dB   |
|    2    |  MaxEIRP 4 dB   |
|    3    |  MaxEIRP 6 dB   |
|    4    |  MaxEIRP 8 dB   |
|    5    | MaxEIRP - 10 dB |
|    6    | MaxEIRP - 12 dB |
|    7    | MaxEIRP - 14 dB |
| 8 ~ 15  |         RFU          |

** EU433 **

By default, MAxEIRP is considered to be +12.15 dBm.

| TXPower | Configuration (EIRP) |
| :-----: | :------------------: |
|    0    |       MaxEIRP        |
|    1    | MaxEIRP - 2 dB  |
|    2    | MaxEIRP - 4 dB  |
|    3    | MaxEIRP - 6 dB  |
|    4    | MaxEIRP - 8 dB  |
|    5    | MaxEIRP - 10 dB |
| 6 ~ 15  |         RFU          |

----

### Appendix III Maximum Transmission Load by Region

:::tip NOTE
In the following list, M is the length including the MAC header; N is the maximum usable payload size for user data, excluding the MAC header.
:::

** EU868 **

| Data Rate |      M      |      N      |
| :-------: | :---------: | :---------: |
|     0     |     59      |     51      |
|     1     |     59      |     51      |
|     2     |     59      |     51      |
|     3     |     123     |     115     |
|     4     |     250     |     242     |
|     5     |     250     |     242     |
|     6     |     250     |     242     |
|     7     |     250     |     242     |
|  8 ~ 15   | Not Defined | Not Defined |

** US915 **

| Data Rate |      M      |      N      |
| :-------: | :---------: | :---------: |
|     0     |     19      |     11      |
|     1     |     61      |     53      |
|     2     |     133     |     125     |
|     3     |     250     |     242     |
|     4     |     250     |     242     |
|   5 ~ 7   | Not Defined | Not Defined |
|     8     |     61      |     53      |
|     9     |     137     |     129     |
|    10     |     250     |     242     |
|    11     |     250     |     242     |
|    12     |     250     |     242     |
|    13     |     250     |     242     |
|  14 ~ 15  | Not Defined | Not Defined |

** AU915 **

| Data Rate |      M      |      N      |
| :-------: | :---------: | :---------: |
|     0     |     59      |     51      |
|     1     |     59      |     51      |
|     2     |     59      |     51      |
|     3     |     123     |     115     |
|     4     |     250     |     242     |
|     5     |     250     |     242     |
|     6     |     250     |     242     |
|     7     | Not Defined | Not Defined |
|     8     |     61      |     53      |
|     9     |     137     |     129     |
|    10     |     250     |     242     |
|    11     |     250     |     242     |
|    12     |     250     |     242     |
|    13     |     250     |     242     |
|  14 ~ 15  | Not Defined | Not Defined |

** KR920 **

| Data Rate |      M      |      N      |
| :-------: | :---------: | :---------: |
|     0     |     59      |     51      |
|     1     |     59      |     51      |
|     2     |     59      |     51      |
|     3     |     123     |     115     |
|     4     |     250     |     242     |
|     5     |     250     |     242     |
|  6 ~ 15   | Not Defined | Not Defined |

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

| Data Rate |      M      |      N      |
| :-------: | :---------: | :---------: |
|     0     |     59      |     51      |
|     1     |     59      |     51      |
|     2     |     59      |     51      |
|     3     |     123     |     115     |
|     4     |     250     |     242     |
|     5     |     250     |     242     |
|     6     |     250     |     242     |
|     7     |     250     |     242     |
|  8 ~ 15   | Not Defined | Not Defined |

** RU864 **

| Data Rate |      M      |      N      |
| :-------: | :---------: | :---------: |
|     0     |     59      |     51      |
|     1     |     59      |     51      |
|     2     |     59      |     51      |
|     3     |     123     |     115     |
|     4     |     230     |     222     |
|     5     |     230     |     222     |
|     6     |     230     |     222     |
|     7     |     230     |     222     |
|  8 ~ 15   | Not Defined | Not Defined |

** CN470 **

| Data Rate |      M      |      N      |
| :-------: | :---------: | :---------: |
|     0     |     59      |     51      |
|     1     |     59      |     51      |
|     2     |     59      |     51      |
|     3     |     123     |     115     |
|     4     |     250     |     242     |
|     5     |     250     |     242     |
|  6 ~ 15   | Not Defined | Not Defined |

** EU433 **

| Data Rate |      M      |      N      |
| :-------: | :---------: | :---------: |
|     0     |     59      |     51      |
|     1     |     59      |     51      |
|     2     |     59      |     51      |
|     3     |     123     |     115     |
|     4     |     250     |     242     |
|     5     |     250     |     242     |
|     6     |     250     |     242     |
|     7     |     250     |     242     |
|  8 ~ 15   | Not Defined | Not Defined |

