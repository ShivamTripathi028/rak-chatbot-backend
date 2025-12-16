---
slug: /product-categories/wisblock/rak10700/at-command-manual/
title: RAK10700 WisBlock GNSS Tracker for LoRaWAN AT Command Manual
description: For an easier experience with your RAK10700 WisBlock GNSS Tracker for LoRaWAN, a comprehensive list of commands for the LoRa P2P and LoRaWAN communication is provided. A serial communication interface is also presented for the two-way communication of the GNSS Tracker.
image: "https://images.docs.rakwireless.com/wisblock/rak10700/rakbox-b2-enclosure.png"
keywords:
  - RAK10700
  - GNSS Tracker
  - AT Command Manual
  - wisblock
sidebar_label: AT Command Manual
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK10700 WisBlock GNSS Tracker for LoRaWAN AT Command Manual

To make it easy to set up the LoRaWAN credentials and LoRa P2P settings, an AT command interface over USB is implemented. It includes the basic commands required to define the node.

_**REMARK 1**_:
After changing the LoRaWAN parameters or LoRa P2P settings, the device must be reset by either the `ATZ` command or by pushing the reset button.

_**REMARK 2**_:
The Serial port connection is lost after the `ATZ` command or pushing the reset button. The connection must be re-established on the connected computer before log output can be seen or AT commands can be entered again.

_**REMARK 3**_:
The Serial port is set up for 115200 baud, 8N1. It cannot be changed by AT commands.


## AT Command Syntax

The AT command is based on ASCII characters. In general, the AT Command starts with the prefix `AT` and ends with `<CR><LF>` (i.e. `\r\n`). For the rest of the manual, the `\r\n` part is omitted for the sake of clarity.

The AT commands have the standard format `AT+XXX` with `XXX` denoting the command.

There are four available command formats:

| **AT COMMAND FORMAT**      | **Description**                                   |
| -------------------------- | ------------------------------------------------- |
| `AT+XXX?`                  | Provides a short description of the given command |
| `AT+XXX=?`                 | Reading the current value on the command          |
| `AT+XXX=<input parameter>` | Writing configuration on the command              |
| `AT+XXX`                   | Used to run a command                             |

The output of the commands is returned via UART.

The format of the reply is divided into two parts: **returned value** and the s**tatus return code**.

:::tip NOTE

`<CR>` stands for “**carriage return**” and `<LF>` stands for “**line feed**”.
:::

1. **`<value><CR><LF>`** is the first reply when **`AT+XXX?`** command description or **`AT+XXX=?`** reading value is executed, then it will be followed by the status return code. The formats with no return value like **`AT+XXX=<input parameter>`** writing configuration command and **`AT+XXX`** run command will just reply to the status return code.

2. **`<CR><LF><STATUS><CR><LF>`** is the second part of the reply, which is the status return code.

The possible status codes are:

| **STATUS RETURN CODE** | **Description**                              |
| ---------------------- | -------------------------------------------- |
| `OK`                   | Command executed correctly without error.    |
| `+CME ERROR:1`         | Generic error or input is not supported.     |
| `+CME ERROR:2`         | Command not allowed.                         |
| `+CME ERROR:5`         | The input parameter of the command is wrong. |
| `+CME ERROR:6`         | The parameter is too long.                   |
| `+CME ERROR:8`         | Value out of range.                          |

More details on each command description and examples are given in the remainder of this section.

## General Commands

### AT?

Description: Help

Returns a list of all available commands with a short description

| Command | Input Parameter | Return Value       | Return Code |
| ------- | --------------- | ------------------ | ----------- |
| `AT?`   | -               | *List of commands* | `OK`        |


```
AT?
AT?

+++++++++++++++
AT command list
+++++++++++++++
AT?         AT commands
ATR         Restore default
ATZ     ATZ Trig a MCU reset
AT+APPEUI   Get or set the application EUI
AT+APPKEY   Get or set the application key
AT+DEVEUI   Get or set the device EUI
AT+APPSKEY  Get or set the application session key
AT+NWKSKEY  Get or Set the network session key
AT+DEVADDR  Get or set the device address
AT+CFM      Get or set the confirm mode
AT+JOIN     Join network
AT+NJS      Get the join status
AT+NJM      Get or set the network join mode
AT+SENDFREQ Get or Set the automatic send time
AT+SEND Send data
AT+ADR      Get or set the adaptive data rate setting
AT+CLASS    Get or set the device class
AT+DR       Get or Set the Tx DataRate=[0..7]
AT+TXP      Get or set the transmit power
AT+BAND     Get and Set number corresponding to active regions
AT+MASK     Get and Set channels mask
AT+BAT      Get battery level
AT+RSSI     Last RX packet RSSI
AT+SNR      Last RX packet SNR
AT+VER      Get SW version
AT+STATUS   Show LoRaWAN status
AT+NWM  Switch LoRa workmode
AT+PFREQ    Set P2P frequency
AT+PSF  Set P2P spreading factor
AT+PBW  Set P2P bandwidth
AT+PCR  Set P2P coding rate
AT+PPL  Set P2P preamble length
AT+PTP  Set P2P TX power
AT+P2P  Set P2P configuration
AT+PSEND    P2P send data
AT+PRECV    P2P receive mode
+++++++++++++++

OK

```


### ATR

This command restores all parameters to the initial default values of the module.

| Command | Input Parameter | Return Value | Return Code |
| ------- | --------------- | ------------ | ----------- |
| `ATR?`  | -               | -            | `OK`        |
| `ATR`   | -               | -            | `OK`        |

### ATZ

Description: MCU reset

This command is used to trigger an MCU reset.

| Command | Input Parameter | Return Value             | Return Code |
| ------- | --------------- | ------------------------ | ----------- |
| `ATZ?`  | -               | `ATZ`: Trig a MCU reset  | `OK`        |
| `ATZ`   | -               | *No return. MCU resets.* | `OK`        |

### AT+STATUS

Description: Show device status

This command is used to get the current device status.

| Command       | Input Parameter | Return Value                         | Return Code |
| ------------- | --------------- | ------------------------------------ | ----------- |
| `AT+STATUS?`  | -               | `AT+STATUS`: Show the LoRaWAN status | `OK`        |
| `AT+STATUS=?` | -               | *&lt; status &gt;*                      | `OK`        |

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

+STATUS:
OK
```



## Keys, IDs, and EUIs Management

### AT+APPEUI

Description: Application unique identifier

This command is used to access and configure the APPEUI.

| Command                           | Input Parameter | Return Value                        | Return Code              |
| --------------------------------- | --------------- | ----------------------------------- | ------------------------ |
| `AT+APPEUI?`                      | -               | `AT+APPEUI`: Get or set the App EUI | `OK`                     |
| `AT+APPEUI=?`                     | -               | *&lt;8 hex &gt;*                       | `OK`                     |
| `AT+APPEUI=<Input Parameter>` | *&lt;8 hex &gt;*   | -                                   | `OK` or `AT_PARAM_ERROR` |

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



### AT+APPKEY

Description: Application key

This command is used to access and configure the APPKEY.

| Command                       | Input Parameter | Return Value                                | Return Code              |
| ----------------------------- | --------------- | ------------------------------------------- | ------------------------ |
| `AT+APPKEY?`                  | -               | `AT+APPKEY`: Get or set the Application Key | `OK`                     |
| `AT+APPKEY=?`                 | -               | *&lt; 16 hex &gt;*                             | `OK`                     |
| `AT+APPKEY=<input parameter>` | *&lt; 16 hex &gt;* | -                                           | `OK` or `AT_PARAM_ERROR` |

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



### AT+DEVEUI

Description: Device EUI or DEVEUI

This command is used to access and configure the device EUI or DEVEUI.

| Command                       | Input Parameter   | Return Value                           | Return Code              |
| ----------------------------- | ----------------- | -------------------------------------- | ------------------------ |
| `AT+DEVEUI?`                  | -                 | `AT+DEVEUI`: Get or set the Device EUI | `OK`                     |
| `AT+DEVEUI=?`                 | -                 | *&lt; 8 hex &gt;*                         | `OK`                     |
| `AT+DEVEUI=<input parameter>` | *&lt; 8 hex &gt;* | -                                      | `OK` or `AT_PARAM_ERROR` |

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



### AT+APPSKEY

Description: Application session key

This command is used to access and configure the application session key or APPSKEY.

| Command                        | Input Parameter | Return Value                                         | Return Code              |
| ------------------------------ | --------------- | ---------------------------------------------------- | ------------------------ |
| `AT+APPSKEY?`                  | -               | `AT+APPSKEY`: Get or set the Application Session Key | `OK`                     |
| `AT+APPSKEY=?`                 | -               | *&lt;16 hex &gt;*                                       | `OK`                     |
| `AT+APPSKEY=<input parameter>` | *&lt;16 hex &gt;*  | -                                                    | `OK` or `AT_PARAM_ERROR` |

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



### AT+NWKSKEY

Description: Network session keys

This command is used to access and configure the network session keys or NWKSKEY.

| Command                        | Input Parameter | Return Value                                     | Return Code              |
| ------------------------------ | --------------- | ------------------------------------------------ | ------------------------ |
| `AT+NWKSKEY?`                  | -               | `AT+NWKSKEY`: Get or set the Network Session Key | `OK`                     |
| `AT+NWKSKEY=?`                 | -               | *&lt; 16 hex &gt;*                                     | `OK`                     |
| `AT+NWKSKEY=<input parameter>` | *&lt;16 hex &gt;*  | -                                                | `OK` or `AT_PARAM_ERROR` |

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

### AT+DEVADDR

Description: Device address or DEVADDR

This command is used to access and configure the device address or DEVADDR. If in OTAA mode and the device has joined the network, `AT+DEVADDR=?` will return the device address assigned by the network server

| Command                        | Input Parameter | Return Value                                | Return Code              |
| ------------------------------ | --------------- | ------------------------------------------- | ------------------------ |
| `AT+DEVADDR?`                  | -               | `AT+DEVADDR`: Get or set the Device address | `OK`                     |
| `AT+DEVADDR=?`                 | -               | *&lt;4 hex &gt;*                               | `OK`                     |
| `AT+DEVADDR=<input parameter>` | *&lt; 4 hex &gt;*  | -                                           | `OK` or `AT_PARAM_ERROR` |

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


## Joining and Sending Data to LoRaWAN Network

### AT+CFM

Description: Confirmed payload mode

This command is used to access and configure the type of payload of the device.

| Command                    | Input Parameter | Return Value                               | Return Code              |
| -------------------------- | --------------- | ------------------------------------------ | ------------------------ |
| `AT+CFM?`                  | -               | `AT+CFM`: Get or set the confirm mode      | `OK`                     |
| `AT+CFM=?`                 | -               | 0 *(if Unconfirmed)* or 1 *(if confirmed)* | `OK`                     |
| `AT+CFM=<input parameter>` | 0 or 1          | -                                          | `OK` or `AT_PARAM_ERROR` |

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



### AT+JOIN

Description: Join the LoRaWAN network

This command is used to join a LoRaWAN network.

| Command                     | Input Parameter                                                                                   | Return Value                     | Return Code             |
| --------------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------- | ----------------------- |
| `AT+JOIN?`                  | -                                                                                                 | `AT+JOIN`: Join network          | `OK`                    |
| `AT+JOIN=?`                 | -                                                                                                 | *Param1, Param2, Param3, Param4* | `OK` or `AT_BUSY_ERROR` |
| `AT+JOIN=<input parameter>` | *Param1:Param2:Param3:Param4*                                                                     | -                                | `OK`                    |
|                             | *Param1* = **Join command**: 1 for joining the network, 0 for stop joining                        |                                  |                         |
|                             | *Param2* = **Auto-Join config**: 1 for Auto-join on power up, 0 for no auto-join. (0 is default) |                                  |                         |
|                             | *Param3* = **Reattempt interval**: 7 - 255 seconds (30 is default)                                |                                  |                         |
|                             | *Param4* = **No. of join attempts**: 0 - 255 (0 is default)                                       |                                  |                         |

:::tip NOTE

- This is an asynchronous command. `OK` means that the device is joining. The completion of the JOIN can be verified with the `AT+NJS=?` command. The asynchronous responses can be:
    - `+EVT:JOINED` after successful join;
    - `+EVT:JOIN FAILED` if the join process did not succeed.
-  Param3 is not supported yet and is fixed to 30s always.

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

+EVT:JOINED

AT+JOIN=3:1:8:10

+CME ERROR:5
```


### AT+NJS

Description: Network join status

This command is used to check the status of the devices if it is connected to a LoRaWAN network.

| Command    | Input Parameter | Return Value                     | Return Code |
| ---------- | --------------- | -------------------------------- | ----------- |
| `AT+NJS?`  | -               | `AT+NJS`: Get the join status    | `OK`        |
| `AT+NJS=?` | -               | 0 *(not joined)* or 1 *(joined)* | `OK`        |

**Examples**:

```
AT+NJS?

AT+NJS: Get the join status
OK

AT+NJS=?

AT+NJS:1
OK
```


### AT+NJM

Description: LoRaWAN network join mode

This command is used to access and configure the activation method of the device either OTAA or ABP. A value of 1 means OTAA join mode, a value of 0 means ABP join mode

| Command                    | Input Parameter | Return Value                               | Return Code              |
| -------------------------- | --------------- | ------------------------------------------ | ------------------------ |
| `AT+NJM?`                  | -               | `AT+NJM`: Get or set the network join mode | `OK`                     |
| `AT+NJM=?`                 | -               | `0` or `1`                                 | `OK`                     |
| `AT+NJM=<input parameter>` | `0` or `1`      | -                                          | `OK` or `AT_PARAM_ERROR` |

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


### AT+SEND

Description: Send payload data

This command is used to send the LoRaWAN payload to a specific port.

| Command                     | Input Parameter | Return Value         | Return Code                                                        |
| --------------------------- | --------------- | -------------------- | ------------------------------------------------------------------ |
| `AT+SEND?`                  | -               | `AT+SEND`: Send data | `OK`                                                               |
| `AT+SEND=<input parameter>` | `port:payload`  | -                    | `OK`, `AT_NO_NETWORK_JOINED`, `AT_PARAM_ERROR`, or `AT_BUSY_ERROR` |

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

+EVT:SEND OK
```

Confirm Payload, ACK received
```
AT+SEND=2:1234

OK

+EVT:SEND CONFIRMED SUCCESS
```

Confirm Payload, no ACK received
```
AT+SEND=2:1234

OK

+EVT:SEND CONFIRMED FAIL
```

Downlink packet received
```
AT+SEND=5:10AAFF45

OK

+EVT:SEND OK
+EVT:RX_1, RSSI -66, SNR 15
+EVT:2:48656C6C6F
```


## LoRaWAN Device Configuration

### AT+SENDFREQ

Description: Set the automatic transmission period (valid for both LoRaWAN and LoRa P2P modes)

This command allows to set the period in seconds between automatic packet transmissions. If set to 0, automatic packet transmission is disabled.

| Command                         | Input Parameter       | Return Value                                      | Return Code              |
| ------------------------------- | --------------------- | ------------------------------------------------- | ------------------------ |
| `AT+SENDFREQ?`                  | -                     | `AT+SENDFREQ`: Get or set the automatic send time | `OK`                     |
| `AT+SENDFREQ=?`                 | -                     | `<period in seconds>`                             | `OK`                     |
| `AT+SENDFREQ=<input parameter>` | `<period in seconds>` | -                                                 | `OK` or `AT_PARAM_ERROR` |

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

:::tip NOTE

_**REMARK**_
The GNSS module will take some time to get a location fix. The time depends on many factors but can take up to 45 seconds. The period of how often a location should be sent should be calculated taking into account:
1) Time to get a location fix (up to 45 seconds)
2) Local LoRaWAN regulations regarding duty cycles

_**If the sending period is set too small (location cannot be fixed by the GNSS module), the device will not be able to send valid location data to the LoRaWAN server.**_

:::



### AT+ADR

Description: Adaptive data rate

This command is used to access and configure the adaptive data rate of the module.

| Command                    | Input Parameter | Return Value                                                | Return Code              |
| -------------------------- | --------------- | ----------------------------------------------------------- | ------------------------ |
| `AT+ADR?`                  | -               | `AT+ADR`: Get or set the Adaptive Data Rate setting` | `OK` |
| `AT+ADR=?`                 | -               | `0` *(ADR off)* or `1` *(ARD on)*                           | OK                       |
| `AT+ADR=<input parameter>` | `0` or `1`      | -                                                           | `OK` or `AT_PARAM_ERROR` |

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


### AT+CLASS

Description: LoRaWAN class

This command is used to access and configure the LoRaWAN class of the module.

| Command                      | Input Parameter | Return Value                                      | Return Code              |
| ---------------------------- | --------------- | ------------------------------------------------- | ------------------------ |
| `AT+CLASS?`                  | -               | `AT+CLASS`: Get or set the Device Class=[A, B, C] | `OK`                     |
| `AT+CLASS=?`                 | -               | `A` or `C` (B not supported)                      | `OK`                     |
| `AT+CLASS=<input parameter>` | `A` or `C`      | -                                                 | `OK` or `AT_PARAM_ERROR` |

:::tip NOTE

**This FW of the device supports the LoRaWAN V1.0.2 stack**.

:::

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


### AT+DR

Description: Data rate settings

This command is used to access and configure data rate settings.

| Command                   | Input Parameter                        | Return Value                                       | Return Code              |
| ------------------------- | -------------------------------------- | -------------------------------------------------- | ------------------------ |
| `AT+DR?`                  | -                                      | `AT+DR=<DataRate><CR>`: Get or set the Tx DataRate | `OK`                     |
| `AT+DR=?`                 | -                                      | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`             | `OK`                     |
| `AT+DR=<Input Parameter>` | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7` | -                                                  | `OK` or `AT_PARAM_ERROR` |

Check [Appendix I](https://docs.rakwireless.com/product-categories/wisblock/rak10700/at-command-manual/#appendix-i-data-rate-by-region) for the input parameter depending on the frequency band selected.

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


### AT+TXP

Description: Transmit Power

This command is used to access and configure the transmit power.

| Command                    | Input Parameter | Return Value                            | Return Code              |
| -------------------------- | --------------- | --------------------------------------- | ------------------------ |
| `AT+TXP?`                  | -               | `AT+TXP`: \et or set the transmit power | `OK`                     |
| `AT+TXP=?`                 | -               | *&lt; value &gt;*                          | `OK` or `AT+PARAM_ERROR` |
| `AT+TXP=<input parameter>` | *&lt; value &gt;*  | -                                       | `OK` or `AT_PARAM_ERROR` |

Check [Appendix II](https://docs.rakwireless.com/product-categories/wisblock/rak10700/at-command-manual/#appendix-ii-tx-power-by-region) for the input parameter depending on the frequency band selected.

For example:
At EU868, a value of 2 represents **MaxEIRP - 4&nbsp;dB**, where MaxEIRP = +16&nbsp;dBm.

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


### AT+BAND

Description: Regional frequency band

This command is used to access and configure the regional frequency band.

| Command                     | Input Parameter | Return Value                                                            | Return Code              |
| --------------------------- | --------------- | ----------------------------------------------------------------------- | ------------------------ |
| `AT+BAND?`                  | -               | `AT+BAND`: Get and set number corresponding to active regions           | `OK`                     |
| `AT+BAND=?`                 | -               | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`      | `OK`                     |
| `AT+BAND=<input parameter>` | *&lt; 0 to 12 &gt;*   | -                                                                       | `OK` or `AT_PARAM_ERROR` |

**List of Band Parameter Options**

| Code | Regional Band |     | Code | Regional Band |
| ---- | ------------- | --- | ---- | ------------- |
| 0    | AS923-1       |     | 7    | IN865         |
| 1    | AU915         |     | 8    | US915         |
| 2    | CN470         |     | 9    | AS923-2       |
| 3    | CN779         |     | 10   | AS923-3       |
| 4    | EU433         |     | 11   | AS923-4       |
| 5    | EU868         |     | 12   | RU864         |
| 6    | KR920         |     |      |               |

:::tip NOTE

The GNSS Tracker is only available for the following regions:
AU915, EU868, KR920, IN865, US915, RU864, AS923-1, AS923-2, AS923-3, AS923-4,
:::

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


### AT+MASK

Description: Regional channel mask

This command is used to access and configure the regional channel mask. Channel mask can only be set for the following regions: AU915, CN470, and US915

| Command                     | Input Parameter | Return Value                                                       | Return Code              |
| --------------------------- | --------------- | ------------------------------------------------------------------ | ------------------------ |
| `AT+MASK?`                  | -               | `AT+MASK`: Get and set channels mask                               | `OK`                     |
| `AT+MASK=?`                 | -               | `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`      | `OK`                     |
| `AT+MASK=<input parameter>` | *&lt; 1 to 12 &gt;*   | -                                                                  | `OK` or `AT_PARAM_ERROR` |

**List of channel masks**

| Regional Band | Available Channels |
| ------------- | ------------------ |
| AU915         | 1 - 9              |
| CN470         | 1 - 12             |
| US915         | 1 - 9              |

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


## Device Information

### AT+BAT

Description: Read the battery voltage

This command allows to read the battery voltage of the device

| Command    | Input Parameter | Return Value                    | Return Code              |
| ---------- | --------------- | ------------------------------- | ------------------------ |
| `AT+BAT?`  | -               | `AT+BAT`: Get the battery level | `OK`                     |
| `AT+BAT=?` | -               | *&lt; value &gt;*                     | `OK` or `AT+PARAM_ERROR` |

:::tip NOTE
**The battery level is returned as a value between 0 and 255**. 
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


### AT+RSSI

Description: Receive signal strength indicator

This command is used to get the RSSI value of the last packet received.

| Command     | Input Parameter | Return Value                                        | Return Code |
| ----------- | --------------- | --------------------------------------------------- | ----------- |
| `AT+RSSI?`  | -               | `AT+RSSI`: Get the RSSI of the last received packet | `OK`        |
| `AT+RSSI=?` | -               | *&lt; integer &gt; in dBm*                                | `OK`        |

**Examples**:

```
AT+RSSI?

AT+RSSI: Last RX packet RSSI
OK

AT+RSSI=?

AT+RSSI:-41
OK
```


### AT+SNR

Description: Signal to Noise Ratio

This command is used to get the SNR value of the last packet received.

| Command    | Input Parameter | Return Value                                      | Return Code |
| ---------- | --------------- | ------------------------------------------------- | ----------- |
| `AT+SNR?`  | -               | `AT+SNR`: Get the SNR of the last received packet | `OK`        |
| `AT+SNR=?` | -               | *&lt; integer &gt;*                                     | `OK`        |

**Examples**:

```
AT+SNR?

AT+SNR: Last RX packet SNR
OK

AT+SNR=?

AT+SNR:11
OK
```


### AT+VER

Description: Version of the firmware

This command is used to get the firmware version installed on the device.

| Command    | Input Parameter | Return Value                              | Return Code |
| ---------- | --------------- | ----------------------------------------- | ----------- |
| `AT+VER?`  | -               | `AT+VER`: Get the version of the firmware | `OK`        |
| `AT+VER=?` | -               | *&lt; V.x.y   &gt;*                             | `OK`        |

**Examples**:

```
AT+VER?

AT+VER: Get SW version
OK

AT+VER=?

AT+VER:1.0.0.0 May 27 2021 17:11:12
OK
```


## P2P Mode

### AT+NWM

Description: LoRa network work mode (LoRaWAN or P2P)

This command is used to switch to LoRaWAN or (P2P)point-to-point mode.

| Command                    | Input Parameter          | Return Value                                                 | Return Code |
| -------------------------- | ------------------------ | ------------------------------------------------------------ | ----------- |
| `AT+NWM?`                  | -                        | `AT+NWM`: Get or set the network work NWM (0:P2P, 1:LoRaWAN) | `OK`        |
| `AT+NWM=?`                 | -                        | &lt; 0 &gt; (P2P) or &lt; 1 &gt; (LoRaWAN)                          | -           |
| `AT+NWM=<input parameter>` | *&lt; 0 P2P or 1 LoRaWAN &gt;* | -                                                            | `OK`        |

**Examples**:
Query status

```
AT+NWM=?

+NWM:0
OK
```

Switch from LoRa P2P to LoRaWAN

```
AT+NWM=1
```
Module will restart

Switch from LoRaWAN to LoRa P2P

```
AT+NWM=0
```
Module will restart


### AT+PFREQ

Description: P2P mode frequency

This command is used to access and configure P2P mode frequency.

| Command                      | Input Parameter       | Return Value                | Return Code |
| ---------------------------- | --------------------- | --------------------------- | ----------- |
| `AT+PFREQ?`                  | -                     | `AT+NWM`: Set P2P frequency | `OK`        |
| `AT+PFREQ=?`                 | -                     | *&lt; frequency &gt;* in Hz       | -           |
| `AT+PFREQ=<input parameter>` | *&lt; frequency &gt;* in Hz | -                           | `OK`        |

**Examples**:

```
AT+PFREQ=868000000

OK
AT+PFREQ=?

+PFREQ:916000000
OK
```


### AT+PSF

Description: P2P mode spreading factor

This command is used to access and configure the P2P mode spreading factor.

| Command                    | Input Parameter | Return Value                    | Return Code |
| -------------------------- | --------------- | ------------------------------- | ----------- |
| `AT+PSF?`                  | -               | `AT+NWM`: Set the P2P frequency | `OK`        |
| `AT+PSF=?`                 | -               | *&lt; Spreading factor &gt;*          | -           |
| `AT+PSF=<input parameter>` | *&lt; 7 to 12 &gt;*   | -                               | `OK`        |

**Examples**:

```
AT+PSF=9

OK
AT+PSF=?

+PSF:7
OK
```


### AT+PBW

Description: P2P mode bandwidth

This command is used to access and configure P2P mode bandwidth.

| Command                    | Input Parameter                                                           | Return Value                                                         | Return Code |
| -------------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------- | ----------- |
| `AT+PBW?`                  | -                                                                         | `AT+PBW`: Set the P2P bandwidth                                      | `OK`        |
| `AT+PBW=?`                 | -                                                                         | `125`, `250`, `500`, `062`, `041`, `031`, `020`, `015`, `010`, `007` | -           |
| `AT+PBW=<input parameter>` | *&lt; `125`, `250`, `500`, `062`, `041`, `031`, `020`, `015`, `010`, `007`&gt;* | -                                                                    | `OK`        |

**Examples**:

```
AT+PBW=125

OK
AT+PBW=?

+PBW:125
OK
```


### AT+PCR

Description: P2P mode coding rate

This command is used to access and configure the P2P mode coding rate. (4/5=1, 4/6=2, 4/7=3, 4/8=4)

| Command                    | Input Parameter         | Return Value                      | Return Code |
| -------------------------- | ----------------------- | --------------------------------- | ----------- |
| `AT+PCR?`                  | -                       | `AT+PCR`: Set the P2P coding rate | `OK`        |
| `AT+PCR=?`                 | -                       | `1`, `2`, `3`, `4`                | -           |
| `AT+PCR=<input parameter>` | *&lt; `1`, `2`, `3`, `4`&gt;* | -                                 | `OK`        |

**Examples**:

```
AT+PCR=1

OK
AT+PCR=?

+PCR:1
OK
```


### AT+PPL

Description: P2P mode preamble length

This command is used to access and configure P2P mode preamble length.

| Command                    | Input Parameter    | Return Value                          | Return Code |
| -------------------------- | ------------------ | ------------------------------------- | ----------- |
| `AT+PPL?`                  | -                  | `AT+PPL`: Set the P2P preamble length | `OK`        |
| `AT+PPL=?`                 | -                  | `1` to `254`                          | -           |
| `AT+PPL=<input parameter>` | *&lt; `1` to `254` &gt;* | -                                     | `OK`        |

**Examples**:

```
AT+PPL=8

OK
AT+PPL=?

+PPL:8
OK
```


### AT+PTP

Description: P2P mode coding rate

This command is used to access and configure the P2P mode coding rate. (4/5=1, 4/6=2, 4/7=3, 4/8=4)

| Command                    | Input Parameter   | Return Value               | Return Code |
| -------------------------- | ----------------- | -------------------------- | ----------- |
| `AT+PTP?`                  | -                 | `AT+PTP`: Set P2P TX power | `OK`        |
| `AT+PTP=?`                 | -                 | `0` to `22`                | -           |
| `AT+PTP=<input parameter>` | *&lt; `0` to `22`* &gt; | -                          | `OK`        |

**Examples**:

```
AT+PTP=22

OK
AT+PTP=?

+PTP:22
OK
```


### AT+P2P

Description: P2P configuration settings

This command is used to access and configure all P2P mode settings: Frequency, Spreading Factor, Bandwidth, Codingrate, Preamble Length, TX Power.

| Command                    | Input Parameter                                         | Return Value                                  | Return Code |
| -------------------------- | ------------------------------------------------------- | --------------------------------------------- | ----------- |
| `AT+P2P?`                  | -                                                       | `AT+PTP`: Set P2P TX power                    | `OK`        |
| `AT+P2P=?`                 | -                                                       | *`Freq`*:*`SF`*:*`BW`*:*`CR`*:*`PPL`*:*`PWR`* | -           |
| `AT+P2P=<input parameter>` | &lt; *`Freq`*:*`SF`*:*`BW`*:*`CR`*:*`PPL`*:*`PWR`* &gt; | -                                             | `OK`        |

**Examples**:

```
AT+P2P=916000000:7:0:1:8:10

OK
AT+P2P=?

+P2P:916000000:7:0:1:8:10
OK
```

### AT+PSEND

Description: P2P send data

This command is used to send P2P data.

| Command                      | Input Parameter   | Return Value              | Return Code |
| ---------------------------- | ----------------- | ------------------------- | ----------- |
| `AT+PSEND?`                  | -                 | `AT+PSEND`: P2P send data | `OK`        |
| `AT+PSEND=<input parameter>` | &lt; *`Payload`* &gt; | -                         | `OK`        |

**Examples**:

```
AT+PSEND=313233

OK

+EVT:SEND OK
```

:::tip NOTE

_**REMARK**_
Received data is not shown in the AT Command interface. The data has to be handled in the user application.

:::

### AT+PRECV

Description: P2P receive mode

This command is used to set the P2P RX mode and timeout for the RX window.

| Command                      | Input Parameter   | Return Value                  | Return Code |
| ---------------------------- | ----------------- | ----------------------------- | ----------- |
| `AT+PRECV?`                  | -                 | `AT+PRECV`: P2P receive mode  | `OK`        |
| `AT+PRECV=?`                 | -                 | `RX timeout in milliseconds` | `OK`        |
| `AT+PRECV=<input parameter>` | &lt; *`Payload`* &gt; | -                             | `OK`        |

**Examples**:

```
AT+PRECV=15000

OK

+EVT:RXP2P, RSSI -54, SNR 12
+EVT:30313334
```
:::tip NOTE

_**REMARK**_
- If the value is set to **65534**, the device will continuously listen to P2P LoRa TX packets without any timeout. This is the same as setting the device in RX mode.
- If the value is set to **65535**, the device will listen to P2P TX packets without a timeout. But it will stop listening once a P2P LoRa packet is received to save power.
- If the value is **0**, the device will stop listening to P2P TX packets. The device is in TX mode.
:::



## Appendix

### Appendix I Data Rate by Region

<b> EU433/EU868/RU864/AS923 </b>

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


<b> CN470/KR920 </b>

| Data Rate | Configuration             | Indicative Physical Bit Rate [bit/s] |
| --------- | ------------------------- | ------------------------------------ |
| 0         | LoRa: SF12 / 125&nbsp;kHz | 250                                  |
| 1         | LoRa: SF11 / 125&nbsp;kHz | 440                                  |
| 2         | LoRa: SF10 / 125&nbsp;kHz | 980                                  |
| 3         | LoRa: SF9 / 125&nbsp;kHz  | 1760                                 |
| 4         | LoRa: SF8 / 125&nbsp;kHz  | 3125                                 |
| 5         | LoRa: SF7 / 125&nbsp;kHz  | 5470                                 |
| 6 ~ 15    | RFU                       |                                      |


<b> US915 </b>

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

<b> AU915 </b>

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

<b> IN865 </b>

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


### Appendix II TX Power by Region

<b> EU868 </b>

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




<b> US915 </b>

| TXPower | Configuration (Conducted Power) |
| ------- | ------------------------------- |
| 0       | 30&nbsp;dBm - 2*TXpower         |
| 1       | 28&nbsp;dBm                     |
| 2       | 26&nbsp;dBm                     |
| 3 ~ 9   | -                               |
| 10      | 10&nbsp;dBm                     |
| 11 ~ 15 | RFU                             |



<b> AU915 </b>

By default, MaxEIRP is considered to be +30&nbsp;dBm.

| TXPower | Configuration (EIRP) |
| ------- | -------------------- |
| 0       | MaxEIRP              |
| 1 ~ 10  | MaxEIRP - 2*TXPower  |
| 11 ~ 10 | RFU                  |




<b> KR920 </b>

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




<b> AS923 </b>

By default, Max EIRP is considered to be 16&nbsp;dBm.

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




<b> IN865 </b>

By default, MaxEIRP is considered to be 30&nbsp;dBm.

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


<b> RU864 </b>

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


<b> CN470 </b>

By default, MaxEIRP is considered to be +19.15&nbsp;dBm.

| TXPower | Configuration (EIRP) |
| ------- | -------------------- |
| 0       | MaxEIRP              |
| 1       | MaxEIRP 2&nbsp;dB    |
| 2       | MaxEIRP 4&nbsp;dB    |
| 3       | MaxEIRP 6&nbsp;dB    |
| 4       | MaxEIRP 8&nbsp;dB    |
| 5       | MaxEIRP - 10&nbsp;dB |
| 6       | MaxEIRP - 12&nbsp;dB |
| 7       | MaxEIRP - 14&nbsp;dB |
| 8 ~ 15  | RFU                  |



<b> EU433 </b>

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


### Appendix III Maximum Transmission Load by Region

_**M in the following list is the length with MAC header, N is the maximum usable payload size for the user data without MAC header.**_

<b> EU868 </b>

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



<b> US915 </b>

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



<b> AU915 </b>

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



<b> KR920 </b>

| Data Rate | M           | N           |
| --------- | ----------- | ----------- |
| 0         | 59          | 51          |
| 1         | 59          | 51          |
| 2         | 59          | 51          |
| 3         | 123         | 115         |
| 4         | 250         | 242         |
| 5         | 250         | 242         |
| 6 ~ 15    | Not Defined | Not Defined |



<b> AS923 </b>

<table>
<thead>
  <tr>
    <th>Data Rate</th>
    <th colspan="2">Uplink MAC Payload Size (M)</th>
    <th colspan="2">Downlink MAC Payload Size (M)</th>
  </tr>
</thead>
<tbody>
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
</tbody>
</table>


<b> IN865 </b>

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


<b> RU864 </b>

| Data Rate | M           | N           |
| --------- | ----------- | ----------- |
| 0         | 59          | 51          |
| 1         | 59          | 51          |
| 2         | 59          | 51          |
| 3         | 123         | 115         |
| 4         | 230         | 222         |
| 5         | 230         | 222         |
| 6         | 230         | 222         |
| 7         | 230         | 222         |
| 8 ~ 15    | Not Defined | Not Defined |


<b> CN470 </b>

| Data Rate | M           | N           |
| --------- | ----------- | ----------- |
| 0         | 59          | 51          |
| 1         | 59          | 51          |
| 2         | 59          | 51          |
| 3         | 123         | 115         |
| 4         | 250         | 242         |
| 5         | 250         | 242         |
| 6 ~ 15    | Not Defined | Not Defined |


<b> EU433 </b>

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



<RkBottomNav/>