---
slug: /product-categories/wisnode/rak7201v2/at-command-manual/
title: RAK7201V2 WisNode Button 4K At Command Manual
description: For an easier experience with your LoRaWAN Module, a comprehensive list of commands for the LoRa P2P and LoRaWAN communication is provided. A serial communication interface is also presented for the two-way communication of the RAK7201V2.
image: "https://images.docs.rakwireless.com/wisnode/rak7201v2/datasheet/rak7201v2.png"
keywords:
  - rak7201v2
  - at command manual
  - wisnode
sidebar_label: AT Command Manual
---

# RAK7201V2 WisNode Button 4K AT Command Manual

## Overview

The configuration of RAK7201V2 can be done by AT commands send by RAK Serial Tool through a USB cable between a PC and the button.

### AT Commands Basics

The maximum length of an AT command string is 255 characters (including `\r\n`).

The command must start with `at+` and end with `<CR><LF> (\r\n)`.

:::tip NOTE
Adding `\r\n` at the end of every AT command is not required if the RAK Serial Tool is used. All commands in this manual will be described without `\r\n` added as the RAK Serial Tool is used.
:::

### AT Commands Division

- **Read commands**: reads the configuration or status of the device.

  ```
  AT+VER=?
  ```

  The command name and the parameter are separated by `=`. If multiple parameters are included, they are separated by `:`.

- **Write commands**: writes/modifies the device configuration.

  ```
  AT+APPEUI=<input>
  ```

  The command name and the parameter are separated by `=`. If there are multiple parameters, they are separated by `:`.

- **Other commands** : neither read nor write.

For example, the command for LoRa to send data is:

  ```
  ATZ
  ```

### AT Command Responses

- When the execution of the command is successful, the following is the response：

```
OK
```

Read command response will start with **OK**, followed by the obtained information. A write command response will contain just **OK**.

Some special commands will trigger module restart. For example, the command `at+set_config=device:restart`. It ends with **"Initialization OK"**,  in the following format:

```
Current Work Mode: LoRaWAN.
/home/daniel/RAK7201/rui-v3/app/../app/RAK7201/src/power.c
sgm41562_get_state 334
```

- When the command configuration is unsuccessful：

```
ERROR: <error code>
```

The response will start with **"ERROR:"** followed by the error code.

## Error Code Meaning

| **Error Code** | **Meaning**                                                                                                                                                                              |
| :------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|       1        | The last command received is an unsupported AT command.                                                                                                                                  |
|       2        | An invalid parameter in the AT command.                                                                                                                                                  |
|       3        | There is an error when reading or writing the flash memory.                                                                                                                              |
|       5        | There is an error when sending data through the UART port.                                                                                                                               |
|       80       | The LoRa transceiver is busy, could not process a new command.                                                                                                                           |
|       81       | LoRa service is unknown. Unknown MAC command was received by the node. Execute commands that are not supported in the current state, such as sending the `at+join`  command in P2P mode. |
|       82       | The LoRa parameters are invalid.                                                                                                                                                         |
|       83       | The LoRa frequency is invalid.                                                                                                                                                           |
|       84       | The LoRa data rate is invalid.                                                                                                                                                           |
|       85       | The LoRa frequency and data rate are invalid.                                                                                                                                            |
|       86       | The device hasn’t joined a LoRa network.                                                                                                                                                 |
|       87       | The length of the packet exceeded the maximum allowed by the LoRa protocol.                                                                                                              |
|       88       | The service is closed by the server. Due to the limitation of the duty cycle, the server will send the "SRV_MAC_DUTY_CYCLE_REQ" MAC command to close the service.                        |
|       89       | This is an unsupported region code.                                                                                                                                                      |
|       90       | The duty cycle is restricted. Due to duty cycle, data cannot be sent at this time until the time limit is removed.                                                                       |
|       91       | No valid LoRa channel could be found.                                                                                                                                                    |
|       92       | No available LoRa channel could be found.                                                                                                                                                |
|       93       | Status is an error. Generally, the internal state of the protocol stack is wrong.                                                                                                        |
|       94       | Time out reached while sending the packet through the LoRa transceiver.                                                                                                                  |
|       95       | Time out reached while waiting for a packet in the LoRa RX1 window.                                                                                                                      |
|       96       | Time out reached while waiting for a packet in the LoRa RX2 window.                                                                                                                      |
|       97       | There is an error while receiving a packet during the LoRa RX1 window.                                                                                                                   |
|       98       | There is an error while receiving a packet during the LoRa RX2 window.                                                                                                                   |
|       99       | Failed to join into a LoRa network.                                                                                                                                                      |
|      100       | Duplicated downlink message is detected. A message with an invalid downlink count was received.                                                                                          |
|      101       | The payload size is not valid for the current data rate.                                                                                                                                 |
|      102       | There were many downlink packets lost.                                                                                                                                                   |
|      103       | Address fail. The address of the received packet does not match the address of the current  node.                                                                                        |
|      104       | Invalid MIC was detected in the LoRa message.                                                                                                                                            |

## General AT Commands

### ATZ

MCU Reset. This command is used to trigger a reset on the module.

| Command Type | Command | Input Parameter | Return Value | Response |
| ------------ | ------- | --------------- | ------------ | -------- |
| Read         | `ATZ`   | -               | -            | -        |

Example:

```
ATZ
```

### ATR

 Restore default parameters. This command is used to restore all parameters to the initial default values.

| Command Type | Command | Input Parameter | Return Value | Response |
| ------------ | ------- | --------------- | ------------ | -------- |
| Read         | `ATR`   | -               | -            | -        |

Example:

```
ATR
```

### ATE

AT Command Echo. This command is used to see the AT command input on the Serial Terminal.

| Command Type | Command | Input Parameter | Return Value | Response |
| ------------ | ------- | --------------- | ------------ | -------- |
| Read         | `ATE`   | -               | -            | OK       |

Example:

```
ATE
OK
```

### AT+SN

Serial number. This command can read the device serial number.

| Command Type | Command   | Input Parameter | Return Value                                               | Response |
| ------------ | --------- | --------------- | ---------------------------------------------------------- | -------- |
| Read         | `AT+SN?`  | -               | `AT+SN`: get the serial number of the device (max 18 char) | OK       |
| Read         | `AT+SN=?` | -               | `AT+SN=Serial number`                                      | OK       |

Example:

```
AT+SN=?
9181004E20900057
OK
```

### AT+BAT

Battery level. This command is used to access the battery level.

| Command Type | Command    | Input Parameter | Return Value                           | Response |
| ------------ | ---------- | --------------- | -------------------------------------- | -------- |
| Read         | `AT+BAT?`  | -               | `AT+BAT`: get the battery level (volt) | OK       |
| Read         | `AT+BAT=?` | -               | `AT+BAT=Battery level (volt)`          | OK       |

Example:

```
AT+BAT=?
AT+BAT=0.971191
OK
```

### AT+VER

Version of the firmware. This command is used to access the version of the firmware.

| Command Type | Command    | Input Parameter | Return Value                              | Response |
| ------------ | ---------- | --------------- | ----------------------------------------- | -------- |
| Read         | `AT+VER?`  | -               | `AT+VER`: get the version of the firmware | OK       |
| Read         | `AT+VER=?` | -               | `AT+VER=Firmware version`                 | OK       |

Example:

```
AT+VER=?
AT+VER=3.2.0-p2_22q1_final.87
OK
```

##  LoRaWAN AT Commands

### AT+APPEUI

This command is used to access the unique application identifier.

| Command Type | Command             | Input Parameter | Return Value                                                      | Response                 |
| ------------ | ------------------- | --------------- | ----------------------------------------------------------------- | ------------------------ |
| Read         | `AT+APPEUI?`        | -               | `AT+APPEUI`: get or set the application EUI (8 bytes in hex) | OK                       |
| Read         | `AT+APPEUI=?`       | -               | `AT+APPEUI=<8 hex>`                                               | OK                       |
| Write        | `AT+APPEUI=<input>` | `<8 hex>`       | -                                                                 | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+APPEUI?
AT+APPEUI: get or set the application EUI (8 bytes in hex)
OK

AT+APPEUI=?
AT+APPEUI=0102030405060708
OK

AT+APPEUI=0102030405060708
OK

AT+APPEUI=010203040506070809
AT_PARAM_ERROR
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when setting wrong or malformed value.
- Keys are MSB first. `<Input>`: 16 digit length, character 0-9, a-f, A-F only, representing eight (8) hexadecimal numbers.
:::

### AT+APPKEY

This command is used to access the application key.

| Command Type | Command             | Input Parameter | Return Value                                                  | Response                 |
| ------------ | ------------------- | --------------- | ------------------------------------------------------------- | ------------------------ |
| Read         | `AT+APPKEY? `       | -               | `AT+APPKEY`: get or set the application key (16 bytes in hex) | OK                       |
| Read         | `AT+APPKEY=?`       | -               | `AT+APPKEY=<16 hex>`                                          | OK                       |
| Write        | `AT+APPKEY=<input>` | `<16 hex>`      | -                                                             | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+APPKEY?
AT+APPKEY: get or set the application key (16 bytes in hex)
OK

AT+APPKEY=?
AT+APPKEY=01020AFBA1CD4D20010230405A6B7F88
OK

AT+APPKEY=01020AFBA1CD4D20010230405A6B7F88
OK

AT+APPKEY=01020AFBA1CD4D20010230405A6B7F
AT_PARAM_ERROR
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when setting wrong or malformed value.
- Keys are MSB first. `<Input>`: 32 digit length, character 0-9, a-f, A-F only, representing 16 hexadecimal numbers.
:::

### AT+APPSKEY

This command is used to set the application session key.

| Command Type | Command              | Input Parameter | Return Value                                         | Response                 |
| ------------ | -------------------- | --------------- | ---------------------------------------------------- | ------------------------ |
| Read         | `AT+APPSKEY?`        | -               | `AT+APPSKEY`: get or set the application session key | OK                       |
| Read         | `AT+APPSKEY=?`       | -               | `AT+APPSKEY=<16hex>`                                 | OK                       |
| Write        | `AT+APPSKEY=<input>` | `<16 hex>`      | -                                                    | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+APPSKEY?
AT+APPSKEY: get or set the application session key
OK

AT+APPSKEY=01020AFBA1CD4D20010230405A6B7F88
OK

AT+APPSKEY=01020AFBA1CD4D20010230405A6B7F
AT_PARAM_ ERROR
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when setting wrong or malformed value.
- Keys are MSB first. `<Input>`: 32 digit length, character 0-9, a-f, A-F only, representing 16 hexadecimal numbers.
:::

### AT+DEVADDR

This command is used to access the device address.

| Command Type | Command              | Input Parameter | Return Value                                                 | Response                 |
| ------------ | -------------------- | --------------- | ------------------------------------------------------------ | ------------------------ |
| Read         | `AT+DEVADDR?`        | -               | `AT+DEVADDR`: get or set the device address (4 bytes in hex) | OK                       |
| Read         | `AT+DEVADDR=?`       | -               | `AT+DEVADDR=<4 hex>`                                         | OK                       |
| Write        | `AT+DEVADDR=<input>` | `<4 hex>`       | -                                                            | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+DEVADDR?
AT+DEVADDR: get or set the device address (4 bytes in hex)
OK

AT+DEVADDR=?
AT+DEVADDR=01020A0B
OK

AT+DEVADDR=01020A0B
OK

AT+DEVADDR=01020A0
AT_PARAM_ERRORR
```

:::tip NOTE
 - `AT_PARAM_ERROR` is returned when setting wrong or malformed value.
 - Keys are MSB first. `<Input>`: 8 digit length, character 0-9, a-f, A-F only, representing four (4) hexadecimal numbers.
:::

### AT+DEVEUI

This command is used to access the unique end-device ID.

| Command Type | Command             | Input Parameter | Return Value                                            | Response                 |
| ------------ | ------------------- | --------------- | ------------------------------------------------------- | ------------------------ |
| Read         | `AT+DEVEUI?`        | -               | `AT+DEVEUI`: get or set the device EUI (8 bytes in hex) | OK                       |
| Read         | `AT+DEVEUI=?`       | -               | `AT+DEVEUI=<8 hex>`                                     | OK                       |
| Write        | `AT+DEVEUI=<input>` | `<8 hex>`       | -                                                       | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+DEVEUI?
AT+DEVEUI: get or set the device EUI (8 bytes in hex)
OK

AT+DEVEUI=?
AT+DEVEUI=1122334455667788
OK

AT+DEVEUI=1122334455667788
OK

AT+DEVEUI=112233445566778
AT_PARAM_ERROR
```

:::tip NOTE
  - `AT_PARAM_ERROR` is returned when setting wrong or malformed value.
  - Keys are MSB first. `<Input>`: 16 digit length, character 0-9, a-f, A-F only, representing eight (8) hexadecimal numbers.
:::

### AT+NETID

This command is used to access the network identifier (NetID) of 3 octets.

| Command Type | Command            | Input Parameter | Return Value                                                   | Response                 |
| ------------ | ------------------ | --------------- | -------------------------------------------------------------- | ------------------------ |
| Read         | `AT+NETID?`        | -               | `AT+NETID`: get or set the network ID (NetID) (3 bytes in hex) | OK                       |
| Read         | `AT+NETID=?`       | -               | `AT+NETID=<3 hex>`                                             | OK                       |
| Write        | `AT+NETID=<input>` | `<3 hex>`       | -                                                              | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+NETID?
AT+NETID: get or set the network ID (NetID) (3 bytes in hex)
OK

AT+NETID=?
AT+NETID=000001
OK
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when setting wrong or malformed value.
- Keys are MSB first. **Return Value:** 6-digit length, character 0-9, a-f, A-F only, representing three (3) hexadecimal numbers.
:::

### AT+NWKSKEY

This command is used to get or set the network session key.

| Command Type | Command              | Input Parameter | Return Value                                                       | Response                 |
| ------------ | -------------------- | --------------- | ------------------------------------------------------------------ | ------------------------ |
| Read         | `AT+NWKSKEY?`        | -               | `AT+NWKSKEY`: get or set the network session key (16 bytes in hex) | OK                       |
| Read         | `AT+NWKSKEY=?`       | -               | `AT+NWKSKEY=<16 hex>`                                              | OK                       |
| Write        | `AT+NWKSKEY=<input>` | `<16 hex>`      | -                                                                  | OK 
 `AT_PARAM_ERROR` |

Example:
```
AT+NWKSKEY?
AT+NWKSKEY: get or set the network session key (16 bytes in hex)
OK

AT+NWKSKEY=?
AT+NWKSKEY=01020AFBA1CD4D20010230405A6B7F88
OK

AT+NWKSKEY=01020AFBA1CD4D20010230405A6B7F88
OK

AT+NWKSKEY=01020AFBA1CD4D20010230405A6B7F8
AT_PARAM_ERROR
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when setting wrong or malformed value.
- Keys are MSB first. `<Input>`: 32 digit length, character 0-9, a-f, A-F only, representing 16 hexadecimal numbers.
:::

### AT+MCROOTKEY

This command is used to get the mc root key of the device.

| Command Type | Command                | Input Parameter | Return Value                                          | Response                 |
| ------------ | ---------------------- | --------------- | ----------------------------------------------------- | ------------------------ |
| Read         | `AT+MCROOTKEY?`        | -               | `AT+MCROOTKEY`: get the mc root key (32 bytes in hex) | OK                       |
| Read         | `AT+MCROOTKEY=?`       | -               | `AT+MCROOTKEY=<32 hex>`                               | OK                       |
| Write        | `AT+MCROOTKEY=<input>` | `<32 hex>`      | -                                                     | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+MCROOTKEY?
AT+MCROOTKEY: get the mc root key (32 bytes in hex)
OK

AT+MCROOTKEY=?
AT+MCROOTKEY=46B1A450DDDE349310F0EFDEEDFBB44B
OK
```

### AT+CFM

This command is used to configure the uplink payload to be confirmed or unconfirmed type.

| Command Type | Command          | Input Parameter | Return Value                                     | Response                 |
| ------------ | ---------------- | --------------- | ------------------------------------------------ | ------------------------ |
| Read         | `AT+CFM?`        | -               | `AT+CFM`: get or set the confirmation mode (0-1) | OK                       |
| Read         | `AT+CFM=?`       | -               | `AT+CFM=(0 or 1)`                                | OK                       |
| Write        | `AT+CFM=<input>` | 0 or 1          | -                                                | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+CFM?
AT+CFM: get or set the confirmation mode (0-1)
OK

AT+CFM=?
AT+CFM=1
OK

AT+CFM=1
OK

AT+CFM=2
AT_PARAM_ERROR
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when setting wrong or malformed value.
- In this case, the **default value is 0**. `AT+CFS=?` is used to know whether or not the last sent message has been confirmed. When the confirmation mode is 1, each sent message must be confirmed FAILED or OK. For example:
```
 ?>at+send=12:123456
 ?>+EVT: SEND CONFIRMED FAILED
 ?>at+send=12:123456
 ?>+EVT: SEND CONFIRMED OK
```
:::

### AT+CFS

This command is used to access the status of the last **SEND** command.

| Command Type | Command    | Input Parameter | Return Value                                                                         | Response |
| ------------ | ---------- | --------------- | ------------------------------------------------------------------------------------ | -------- |
| Read         | `AT+CFS?`  | -               | `AT+CFS`: get the confirmation status of the last AT+SEND (0 = failure, 1 = success) | OK       |
| Read         | `AT+CFS=?` | -               | 0 or 1                                                                               | OK       |

Example:

```
AT+CFS?
AT+CFS: get the confirmation status of the last AT+SEND (0 = failure, 1 = success)
OK

AT+CFS=?
AT+CFS=0
OK
```

:::tip NOTE
- This command works together with `AT+CFM=1`, which is the confirm mode configuration. If the return of this command is `1`, the last confirmed uplink is successful.
- If it is `0`, then the last confirmed uplink attempt failed. It's a read-only command, with a default value on device startup of `0`.
:::

### AT+JOIN

This command is used to join a LoRaWAN network.

| Command Type | Command           | Input Parameter                    | Return Value                               | Response            |
| ------------ | ----------------- | ---------------------------------- | ------------------------------------------ | ------------------- |
| Read         | `AT+JOIN?`        | -                                  | `AT+JOIN`: join network                    | OK                  |
| Read         | `AT+JOIN=?`       | -                                  | `AT+JOIN=Param1, Param2, Param3 or Param4` | OK
AT_BUSY_ERROR |
| Write        | `AT+JOIN=<input>` | Param1, Param2, Param3, or Param4, | -                                          | OK                  |

Where:

- *Param1* = **Join command**: 1 for joining the network, 0 for stop joining.
- *Param2* = **Auto-Join config**: 1 for Auto-join on power up, 0 for no auto-join. (Default value: 0)
- *Param3* = **Reattempt interval**: 7 - 255 seconds (Default value: 8)
- *Param4* = **No. of join attempts**: 0 - 255 (Default value: 0)

:::tip NOTE
- `AT+JOIN` is an asynchronous command. `OK` means that the device is joining. The completion of the JOIN can be verified with the `AT+NJS=?` command.
- The parameters of the `AT+JOIN` command are optional. You can use `AT+JOIN` directly to join the LoRaWAN network. If no parameters are configured, the device will use the default values.
:::

Examples:

- Successful join attempt

```
AT+JOIN=1:0:10:8

OK
+EVT:JOINED
```

- Failed join attempt

```
AT+JOIN=1:0:10:8

OK
+EVT:JOIN FAILED
```

:::tip NOTE
If joining fails, make sure your device is within the coverage of the gateway. Also, ensure that the RUI3 LoRaWAN device is in LoRaWAN mode via `AT+NWM=1`. The region is correct via `AT+BAND`, and the EUIs and keys are correct.
:::

### AT+NJM

This command is used to access the network join mode.

| Command Type | Command          | Input Parameter | Return Value                                                   | Response                 |
| ------------ | ---------------- | --------------- | -------------------------------------------------------------- | ------------------------ |
| Read         | `AT+NJM?`        | -               | `AT+NJM`: get or set the network join mode (0 = ABP, 1 = OTAA) | OK                       |
| Read         | `AT+NJM=?`       | -               | `AT+NJM=(0 or 1)`                                              | OK                       |
| Write        | `AT+NJM=<Input>` | 0 or 1          | -                                                              | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+NJM?
AT+NJM: get or set the network join mode (0 = ABP, 1 = OTAA)
OK

AT+NJM=?
0
OK

AT+NJM=1
OK

AT+NJM=2
AT_PARAM_ERROR
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when setting wrong or malformed value.
- In this case, the default value is `1`.
:::

### AT+NJS

This command is used to access the current activation status of the device. It shows if the device joined or not in a LoRaWAN network.

| Command Type | Command          | Input Parameter | Return Value                                               | Response                 |
| ------------ | ---------------- | --------------- | ---------------------------------------------------------- | ------------------------ |
| Read         | `AT+NJS?`        | -               | `AT+NJS`: get the join status (0 = not joined, 1 = joined) | OK                       |
| Read         | `AT+NJS=?`       | -               | `AT+NJS=(0 or 1)`                                          | OK                       |
| Write        | `AT+NJS=<input>` | 0 or 1          | -                                                          | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+NJS?
AT+NJS: get the join status (0 = not joined, 1 = joined)
OK

AT+NJS=?
AT+NJS=1
OK
```

:::tip NOTE
The command will return `1` if the device has successfully joined the network and `0` if the device hasn't joined the network yet.
:::

### AT+RECV

This command is used to access the last received data in hex format.

| Command Type | Command     | Input Parameter | Return Value                                          | Response |
| ------------ | ----------- | --------------- | ----------------------------------------------------- | -------- |
| Read         | `AT+RECV?`  | -               | `AT+RECV`: print the last received data in hex format | OK       |
| Read         | `AT+RECV=?` | -               | `AT+RECV=<port>:<payload>`                            | OK       |

Where:
- `<port>`: 1 decimal integer and the range of values is 1~233.
- `<payload>`: 2~500 digit length, must be an even number of digits and character 0-9, a-f, A-F only,
representing 1~256 hexadecimal numbers.

Example:

```
AT+RECV?
AT+RECV: print the last received data in hex format
OK

AT+RECV=?
AT+RECV=45:112233
OK
```

- This command returns the last received data in a form, along with the port on which it was received. The format of the output is as follows:

```
<port>:<payload><CR><LF>
<CR><LF>OK<CR><LF>
```

- When called twice, without new data received between the calls, the second `AT+RECV=?` returns an empty value as shown below:

```
0:
OK
```

### AT+SEND

This command provides a way to send data on a dedicated port number.

| Command Type | Command           | Input Parameter    | Return Value                                         | Response                                                                    |
| ------------ | ----------------- | ------------------ | ---------------------------------------------------- | --------------------------------------------------------------------------- |
| Read         | `AT+SEND?`        | -                  | `AT+SEND`: send data along with the application port | OK                                                                          |
| Read         | `AT+SEND=?`       | -                  | -                                                    | `AT_PARAM_ERROR`                                                            |
| Write        | `AT+SEND=<input>` | `<port>:<payload>` | -                                                    | OK 
 `AT_PARAM_ERROR`  
 `AT_BUSY_ERROR`  
 `AT_NO_NETWORK_JOINED` |

Where:
* `<port>`: 1 decimal integer and the range of values is 1~233.
* `<payload>`: 2~500-digit length, must be an even number of digits and character 0-9, a-f, A-F only,
representing 1~256 hexadecimal numbers.

Example:

```
AT+SEND=12:112233
OK
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when setting wrong or malformed value.
- `AT_BUSY_ERROR` is returned when the previous send is not complete (send waiting for duty cycle, rx window not consumed).
- `AT_NO_NETWORK_JOINED` is returned when the network is not yet joined.
:::

### AT+RETY

This command sets the number of retransmissions of confirmed packet data.

| Command Type | Command           | Input Parameter          | Return Value                                                        | Response                 |
| ------------ | ----------------- | ------------------------ | ------------------------------------------------------------------- | ------------------------ |
| Read         | `AT+RETY?`        | -                        | `AT+RETY`: set the number of retransmissions of Confirm packet data | OK                       |
| Read         | `AT+RETY=?`       | -                        | `AT+RETY=(0,1,2,3,4,5,6 or 7)`                                      | OK                       |
| Write        | `AT+RETY=<input>` | 0, 1, 2, 3, 4, 5, 6 or 7 | -                                                                   | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+RETY?
AT+RETY: set the number of retransmissions of Confirm packet data
OK

AT+RETY=?
AT+RETY=3
OK

AT+RETY=2
OK

AT+RETY=8
AT_PARAM_ERROR
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when setting wrong or malformed value.
- In this case, the default value is 0, and the retry cycle range of values is 0~7.
:::

### AT+ADR

This command is used to access the adaptive data rate.

| Command Type | Command          | Input Parameter | Return Value                                                          | Response                 |
| ------------ | ---------------- | --------------- | --------------------------------------------------------------------- | ------------------------ |
| Read         | `AT+ADR?`        | -               | `AT+ADR`: get or set the adaptive data rate setting (0 = off, 1 = on) | OK                       |
| Read         | `AT+ADR=?`       | -               | `AT+ADR=(0 or 1)`                                                     | OK                       |
| Write        | `AT+ADR=<input>` | 0 or 1          | -                                                                     | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+ADR?
AT+ADR: get or set the adaptive data rate setting (0 = off, 1 = on)
OK

AT+ADR=?
AT+ADR=1
OK

AT+ADR=1
OK

AT+ADR=2
AT_PARAM_ERROR
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when setting wrong or malformed value.
- In this case, the default value is `1`.
:::

### AT+DCS

Duty cycle settings

| Command Type | Command          | Input Parameter | Return Value                                                                 | Response                 |
| ------------ | ---------------- | --------------- | ---------------------------------------------------------------------------- | ------------------------ |
| Read         | `AT+DCS?`        | -               | `AT+DCS`: get or set the ETSI duty cycle setting (0 = disabled, 1 = enabled) | OK                       |
| Read         | `AT+DCS=?`       | -               | `AT+DCS=(0 or 1)`                                                            | OK                       |
| Write        | `AT+DCS=<input>` | 0 or 1          | -                                                                            | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+DCS?
AT+DCS: get or set the ETSI duty cycle setting (0 = disabled, 1 = enabled)
OK

AT+DCS=?
AT+DCS=1
OK

AT+DCS=1
OK

AT+DCS=2
AT_PARAM_ERROR
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when setting wrong or malformed value.
- In this case, the **EU868 default value is 1**.
- It depends on the region to disable or enable, and it can only be read.
:::

### AT+DR

This command is used to access and configure data rate settings.

| Command Type | Command         | Input Parameter        | Return Value                      | Response                 |
| ------------ | --------------- | ---------------------- | --------------------------------- | ------------------------ |
| Read         | `AT+DR?`        | -                      | `AT+DR`: get or set the data rate | OK                       |
| Read         | `AT+DR=?`       | -                      | `AT+DR=(0, 1, 2, 3, 4, 5, 6, 7)`  | OK                       |
| Write        | `AT+DR=<input>` | 0, 1, 2, 3, 4, 5, 6, 7 | -                                 | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+DR?
AT+DR: get or set the data rate
OK

AT+DR=?
AT+DR=3
OK

AT+DR=2
OK
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when setting wrong or malformed value.
- In this case, the EU868 default value is 0. **EU433 / RU864 / IN865 / EU868 / CN470 / KR920** and the data rate range of values is 0-5 (DR0-DR5). **AS923** and the data rate range of values is 2-5 (DR2-DR5). **US915** and the data rate range of values is 0-4 (DR0-DR4). **AU915** and the data rate range of values is 0-6 (DR0-DR6).
- Complete information about DR parameter on each region can be found on [RUI3 Appendix - LoRaWAN Regional Parameter (Data Rate)](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/appendix#data-rate-by-region).
:::

### AT+JN1DL

This command is used to configure the join delay on RX window 1. The range of acceptable values is 1 to 14 seconds.

| Command Type | Command            | Input Parameter | Return Value                                                                                          | Response                                  |
| ------------ | ------------------ | --------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| Read         | `AT+JN1DL?`        | -               | `AT+JN1DL`: get or set the join accept delay between the end of TX and the join RX window 1 in second | OK                                        |
| Read         | `AT+JN1DL=?`       | -               | `AT+JN1DL=seconds (1-14)`                                                                             | OK 
 `AT_BUSY_ERROR`                   |
| Write        | `AT+JN1DL=<input>` | seconds (1-14)  | -                                                                                                     | OK 
 `AT_PARAM_ERROR
AT_BUSY_ERROR` |

Example:

```
AT+JN1DL?
AT+JN1DL: get or set the join accept delay between the end of TX and the join RX window 1 in second
OK

AT+JN1DL=?
AT+JN1DL=5
OK

AT+JN1DL=10
OK
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when a join or a send is being processed.
- `AT_BUSY_ERROR` is returned when setting wrong or malformed value.
- In this case, the default value is **5**. `<Input>`: 1-decimal integer and the range of values is 1~14.
:::

### AT+JN2DL

This command is used to configure the join delay on RX window 2. The range of acceptable values is 2 to 15 seconds.

| Command Type | Command            | Input Parameter | Return Value                                                                                   | Response                                      |
| ------------ | ------------------ | --------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------- |
| Read         | `AT+JN2DL?`        | -               | `AT+JN2DL`: get the join accept delay between the end of TX and the join RX window 2 in second | OK                                            |
| Read         | `AT+JN2DL=?`       | -               | `AT+JN2DL=seconds (2-15)`                                                                      | OK 
 `AT_BUSY_ERROR`                       |
| Write        | `AT+JN2DL=<input>` | seconds (2-15)  | -                                                                                              | OK 
 `AT_PARAM_ERROR` 
 `AT_BUSY_ERROR` |

Example:

```
AT+JN2DL?
AT+JN2DL: get the join accept delay between the end of TX and the join RX window 2 in second
OK

AT+JN2DL=?
AT+JN2DL=6
OK

AT+JN2DL=6
OK
```

:::tip NOTE
- `AT+JN2DL` must be larger than `AT+JN1DL` or it will not work. `AT_PARAM_ERROR` is returned when wrong setting is applied.
- Also, `AT_PARAM_ERROR` is returned when a join or a send is being processed.
- `AT_BUSY_ERROR` is returned when setting wrong or malformed value.
:::

### AT+PNM

This command is used to access the public network mode.

| Command Type | Command          | Input Parameter | Return Value                                                   | Response                 |
| ------------ | ---------------- | --------------- | -------------------------------------------------------------- | ------------------------ |
| Read         | `AT+PNM?`        | -               | `AT+PNM`: get or set the public network mode (0 = off, 1 = on) | OK                       |
| Read         | `AT+PNM=?`       | -               | `AT+PNM=(0 or 1)`                                              | OK                       |
| Write        | `AT+PNM=<input>` | 0 or 1          | -                                                              | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+PNM?
AT+PNM: get or set the public network mode (0 = off, 1 = on)
OK

AT+PNM=?
AT+PNM=0
OK

AT+PNM=1
OK

AT+PNM=2
AT_PARAM_ERROR
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when setting wrong or malformed value.
- In this case, the default value is 1.
:::

### AT+RX1DL

This command is used to access the delay of the received window 1. The range of acceptable values is 1 to 15 seconds. Whenever `AT+RX1DL` is updated, `AT+RX2DL` is also updated automatically.

| Command Type | Command            | Input Parameter | Return Value                                                                                | Response                                      |
| ------------ | ------------------ | --------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------- |
| Read         | `AT+RX1DL?`        | -               | `AT+RX1DL`: get or set the delay between the end of TX and the RX window 1 in second (1-15) | OK                                            |
| Read         | `AT+RX1DL=?`       | -               | `AT+RX1DL=seconds (1-15)`                                                                   | OK                                            |
| Write        | `AT+RX1DL=<input>` | seconds (1-15)  | -                                                                                           | OK 
 `AT_PARAM_ERROR` 
 `AT_BUSY_ERROR` |

Example:

```
AT+RX1DL?
AT+RX1DL: get or set the delay between the end of TX and the RX window 1 in second (1-15)
OK

AT+RX1DL=?
AT+RX1DL=1
OK

AT+RX1DL=10
OK
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when a join or a send is being processed.
- `AT_BUSY_ERROR` is returned when setting wrong or malformed value.
- In this case, the default value is 1. `<Input>`: 1-decimal integer and the range of values is 1~15.
:::

### AT+RX2DL

This command is used to access the delay of the received window 2. The range of acceptable values is 2 to 16 seconds. Whenever `AT+RX2DL` is updated, `AT+RX1DL` is also updated automatically.

| Command Type | Command            | Input Parameter | Return Value                                                                         | Response                |
| ------------ | ------------------ | --------------- | ------------------------------------------------------------------------------------ | ----------------------- |
| Read         | `AT+RX2DL?`        | -               | `AT+RX2DL`: get the delay between the end of TX and the RX window 2 in second (2-16) | OK                      |
| Read         | `AT+RX2DL=?`       | -               | `AT+RX2DL=seconds (2-16)`                                                            | OK 
 `AT_BUSY_ERROR` |
| Write        | `AT+RX2DL=<input>` | seconds (2-16)  | -                                                                                    | OK                      |

Example:

```
AT+RX2DL?
AT+RX2DL: get the delay between the end of TX and the RX window 2 in second (2-16)
OK

AT+RX2DL=?
AT+RX2DL=2
OK
```

:::tip NOTE
`AT_BUSY_ERROR` is returned when setting the wrong or malformed value.
:::

### AT+RX2DR

This command is used to access the data rate of received window 2.

| Command Type | Command            | Input Parameter                                | Return Value                                                  | Response                                      |
| ------------ | ------------------ | ---------------------------------------------- | ------------------------------------------------------------- | --------------------------------------------- |
| Read         | `AT+RX2DR?`        | -                                              | `AT+RX2DR`: get or set the RX2 window data rate               | OK                                            |
| Read         | `AT+RX2DR=?`       | -                                              | `AT+RX2DR=(0, 1, 2, 3, 4, 5, 6, 7) or (8, 9, 10, 11, 12, 13)` | OK 
 `AT_BUSY_ERROR`                       |
| Write        | `AT+RX2DR=<input>` | 0, 1, 2, 3, 4, 5, 6, 7 or 8, 9, 10, 11, 12, 13 | -                                                             | OK 
 `AT_PARAM_ERROR` 
 `AT_BUSY_ERROR` |

Example:

```
AT+RX2DR?
AT+RX2DR: get or set the RX2 window data rate
OK

AT+RX2DR=?
AT+RX2DR=6
OK

AT+RX2DR=5
OK
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when a join or a send is being processed.
- `AT_BUSY_ERROR` is returned when setting wrong or malformed value.
- In this case, the EU868 default value is 0 and the US915 default value is 8. **EU433 / RU864 / IN865 / EU868 / CN470 / KR920** and the data rate range of values is 0-5 (DR0-DR5). **AS923** and the data rate range of values is 2-5 (DR2-DR5). **US915** / **AU915** and the data rate range of values is 8-13 (DR8-DR13).
:::

### AT+RX2FQ

This command is used to access the frequency of the received window 2.

| Command Type | Command      | Input Parameter | Return Value                                  | Response                |
| ------------ | ------------ | --------------- | --------------------------------------------- | ----------------------- |
| Read         | `AT+RX2FQ?`  | -               | `AT+RX2FQ`: get the Rx2 window frequency (Hz) | OK                      |
| Read         | `AT+RX2FQ=?` | -               | `AT+RX2FQ=Frequency` in Hz                    | OK 
 `AT_BUSY_ERROR` |

Example:

```
AT+RX2FQ?
AT+RX2FQ: get the Rx2 window frequency (Hz)
OK

AT+RX2FQ=?
AT+RX2FQ=869535000
OK
```

:::tip NOTE
- `AT_BUSY_ERROR` is returned when setting wrong or malformed value.
- In this case, the EU868 default value is 869525000. It depends on the region frequency, and it can only be read.
:::

### AT+TXP

This command is used to access the transmit power.

| Command Type | Command          | Input Parameter | Return Value                                | Response                 |
| ------------ | ---------------- | --------------- | ------------------------------------------- | ------------------------ |
| Read         | `AT+TXP?`        | -               | `AT+TXP`: get or set the transmitting power | OK                       |
| Read         | `AT+TXP=?`       | -               | `AT+TXP=<value>`                            | OK 
 `AT_PARAM_ERROR` |
| Write        | `AT+TXP=<input>` | `<value>`       | -                                           | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+TXP?
AT+TXP: get or set the transmitting power
OK

AT+TXP=?
AT+TXP=1
OK

AT+TXP=4
OK
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when a join or a send is being processed.
- In this case, the TX Power default value is 0. **EU868 / RU864 / KR920 / AS923 / CN470** and Transmit power range of values is 0-7. **US915 / AU915** and Transmit power range of values is 0-14. **EU433** and Transmit power range of values is 0-5. **IN865** and Transmit power range of values is 0-10.
- Highest power start from 0. Complete information about TXP parameter on each region can be found on [RUI3 Appendix - LoRaWAN Regional Parameter (TX Power)](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/appendix#tx-power-by-region)
:::

### AT+LINKCHECK

This command is used to access and configure the device network link status.

| Command Type | Command                | Input Parameter | Return Value                                                                              | Response                 |
| ------------ | ---------------------- | --------------- | ----------------------------------------------------------------------------------------- | ------------------------ |
| Read         | `AT+LINKCHECK?`        | -               | `AT+LINKCHECK`: get or set the link check setting (0 = disabled, 1 = once, 2 = everytime) | OK                       |
| Read         | `AT+LINKCHECK=?`       | -               | `AT+LINKCHECK=(0, 1 or 2)`                                                                | OK                       |
| Write        | `AT+LINKCHECK=<input`> | 0, 1 or 2       | -                                                                                         | OK 
 `AT_PARAM_ERROR` |

Where:

- 0 - Disable Link Check
- 1 - Execute Link Check just once on the next payload uplink.
- 2 - Module will automatically execute one-time Link Check after every payload uplink.

Example:
```
AT+LINKCHECK=?
AT+LINKCHECK=0
OK

AT+LINKCHECK=1
OK

AT+SEND=3:12341234
OK

+EVT:LINKCHECK:0,21,1,-60,11
```

:::tip NOTE

`LINKCHECK` is a dedicated LoRaWAN MAC command that checks the connectivity status of the end-device to the network. You will have the `LINKCHECK` status reply once the `AT+SEND` command is executed. In case of a failed uplink (regardless if confirmed or unconfirmed), the `LINKCHECK` reply will be `+EVT:LINKCHECK:1,0,0,0,0`.

Reply format: `+EVT:LINKCHECK:Y0,Y1,Y2,Y3,Y4`:

- **Y0** represents the result of Link Check
  -	0 – represents the Link Check execute success (`+EVT:LINKCHECK:0,0,1,-107,4`)
  -	Non-0 – represents the Link Check execute fail (`+EVT:LINKCHECK:1,0,0,0,0`)
- **Y1** represents the DemodMargin
- **Y2** represents the NbGateways
- **Y3** represents the RSSI
- **Y4** represents the SNR
:::

### AT+TIMEREQ

This command is used to request the current date and time.

| Command Type | Command              | Input Parameter | Return Value                                                            | Response                 |
| ------------ | -------------------- | --------------- | ----------------------------------------------------------------------- | ------------------------ |
| Read         | `AT+TIMEREQ?`        | -               | `AT+TIMEREQ`: request the current date and time (0=Disabled, 1=Enabled) | OK                       |
| Read         | `AT+TIMEREQ=?`       | -               | `AT+TIMEREQ=(0 or 1)`                                                   | OK                       |
| Write        | `AT+TIMEREQ=<input>` | 0 or 1          | -                                                                       | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+TIMEREQ?
AT+TIMEREQ: request the current date and time (0=Disabled, 1=Enabled)
OK

AT+TIMEREQ=?
AT+TIMEREQ=0
OK

AT+TIMEREQ=0
OK

AT+TIMEREQ=2
AT_PARAM_ERROR
```

:::tip NOTE
`AT_PARAM_ERROR` is returned when setting wrong or malformed value.
:::

### AT+LBT

This command is used to enable or disable LoRaWAN Listen Before Talk (LBT).

| Command Type | Command          | Input Parameter | Return Value                                                                       | Response                 |
| ------------ | ---------------- | --------------- | ---------------------------------------------------------------------------------- | ------------------------ |
| Read         | `AT+LBT?`        | -               | `AT+LBT`: get or set the LoRaWAN LBT (support Korea Japan) (0=Disabled; 1=Enabled) | OK                       |
| Read         | `AT+LBT=?`       | -               | `AT+LBT=(0 or 1)`                                                                  | OK                       |
| Write        | `AT+LBT=<input>` | 0 or 1          | -                                                                                  | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+LBT?
AT+LBT: get or set the LoRaWAN LBT (support Korea Japan) (0=Disabled; 1=Enabled)
OK

AT+LBT=?
AT+LBT=0
OK

AT+LBT=0
OK

AT+LBT=2
AT_PARAM_ERROR
```

:::tip NOTE
`AT_PARAM_ERROR` is returned when setting wrong or malformed value.
:::

### AT+LBTRSSI

This command is used to set or get LoRaWAN LBT RSSI.

| Command Type | Command              | Input Parameter | Return Value                                                        | Response                 |
| ------------ | -------------------- | --------------- | ------------------------------------------------------------------- | ------------------------ |
| Read         | `AT+LBTRSSI?`        | -               | `AT+LBTRSSI`: get or set the LoRaWAN LBT RSSI (support Korea Japan) | OK                       |
| Read         | `AT+LBTRSSI=?`       | -               | `AT+LBTRSSI=RSSI`                                                   | OK                       |
| Write        | `AT+LBTRSSI=<input>` | RSSI            | -                                                                   | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+LBTRSSI=?
AT+LBTRSSI=-80
OK
```

:::tip NOTE
`AT_PARAM_ERROR` is returned when setting the wrong or malformed value.
:::

### AT+LBTSCANTIME

This command is used to set or get LoRaWAN LBT Scantime.

| Command Type | Command                  | Input Parameter | Return Value                                                                | Response                 |
| ------------ | ------------------------ | --------------- | --------------------------------------------------------------------------- | ------------------------ |
| Read         | `AT+LBTSCANTIME?`        | -               | `AT+LBTSCANTIME`: get or set the LoRaWAN LBT scantime (support Korea Japan) | OK                       |
| Read         | `AT+LBTSCANTIME=?`       | -               | `AT+LBTSCANTIME=time`                                                       | OK                       |
| Write        | `AT+LBTSCANTIME=<input>` | time (in msec)  | -                                                                           | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+LBTSCANTIME=?
AT+LBTSCANTIME=5
OK
```

:::tip NOTE
`AT_PARAM_ERROR` is returned when setting the wrong or malformed value.
:::

### AT+LTIME

This command is used to access the local time in a UTC format.

| Command Type | Command      | Input Parameter | Return Value                                           | Response |
| ------------ | ------------ | --------------- | ------------------------------------------------------ | -------- |
| Read         | `AT+LTIME?`  | -               | `AT+LTIME`: get the local time                         | OK       |
| Read         | `AT+LTIME=?` | -               | `LTIME:<HOUR>h<MINUTE>m<SECOND>s <YEAR>-<DAY>-<MONTH>` | OK       |

Example:

```
AT+LTIME?
AT+LTIME: get the local time
OK

AT+LTIME=?
LTIME: 00h37m58s 2018-11-14
OK
```

### AT+RSSI

This command is used to access the RSSI on reception.

| Command Type | Command     | Input Parameter | Return Value                                        | Response |
| ------------ | ----------- | --------------- | --------------------------------------------------- | -------- |
| Read         | `AT+RSSI?`  | -               | `AT+RSSI`: get the RSSI of the last received packet | OK       |
| Read         | `AT+RSSI=?` | -               | `AT+RSSI=(RSSI)`                                    | OK       |

Example:

```
AT+RSSI=0
OK
```

:::tip NOTE
-  `AT+RSSI=?` provides a value in dBm, and it can only be read.
-  When the connection is successful, it gets the RSSI of the last received packet.
:::

### AT+ARSSI

This command allows you to view all open channels RSSI

| Command Type | Command       | Input Parameter | Return Value                                                               | Response |
| ------------ | ------------- | --------------- | -------------------------------------------------------------------------- | -------- |
| Read         | `AT+ARSSI?`   | -               | `AT+ARSSI`: access all open channel RSSI                                   | OK       |
| Read         | ` AT+ARSSI=?` | -               | ` 0: <Channel 0 rssi>
1: <Channel 1 rssi>
.... 15:<Channel 15 rssi>` | OK       |

Example:

```
AT+ARSSI=?
0:-57,1:-57,2:-57
OK
```

:::tip NOTE
- `AT+ARSSI=?` provides a value in dBm, and it can only be read.
- When the connection is successful, it views all open channels RSSI of the last received packet.
:::

### AT+SNR

This command is used to access the SNR of the last received packet.

| Command Type | Command    | Input Parameter | Return Value                                      | Response |
| ------------ | ---------- | --------------- | ------------------------------------------------- | -------- |
| Read         | `AT+SNR?`  | -               | `AT+SNR`: get the SNR of the last received packet | OK       |
| Read         | `AT+SNR=?` | -               | `AT+SNR=(SNR)`                                    | OK       |

Example:

```
AT+SNR=?
AT+SNR=0
OK
```

:::tip NOTE
`AT+SNR=?` provides a value in db and it can only be read. When the connection is successful and gets the SNR of the last received packet.
:::

### AT+MASK

This command configures the channel of the device by setting the hexadecimal channel mask.

| Command Type | Command           | Input Parameter       | Return Value                                                                                       | Response                                       |
| ------------ | ----------------- | --------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Read         | `AT+MASK?`        | -                     | `AT+MASK`: get or set the channel mask to close or open the channel (only for US915, AU915, CN470) | OK                                             |
| Read         | `AT+MASK=?`       | -                     | `AT+MASK=(mask)`                                                                                   | OK                                             |
| Write        | `AT+MASK=<input>` | mask (4-digit length) | -                                                                                                  | OK 
 `AT_PARAM_ERROR` 
  `AT_BUSY_ERROR` |

Example:

```
AT+MASK=?
AT+MASK=0001
OK

AT+MASK=0001
OK
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when setting wrong or malformed value.
- `AT_BUSY_ERROR` is returned when the set command process is already running.
-  In this case, the channel mask mode is only for US915, AU915, CN470. US915 / AU915 default value is 01FF and CN470 and default value is 0FFF.
- `<Input>`: 4-digit length, character 0-9, a-f, A-F only, representing a 16-bit mask.
:::

### AT+CHE

This command sets the node to eight-channel mode.

| Command Type | Command          | Input Parameter | Return Value                                                          | Response                 |
| ------------ | ---------------- | --------------- | --------------------------------------------------------------------- | ------------------------ |
| Read         | `AT+CHE?`        | -               | `AT+CHE`: get or set eight channels mode (only for US915 AU915 CN470) | OK                       |
| Read         | `AT+CHE=?`       | -               | `AT+CHE=(value)`                                                      | OK                       |
| Write        | `AT+CHE=<input>` | value           | -                                                                     | OK 
 `AT_PARAM_ERROR` |

Example:

```
AT+CHE=?
AT+CHE=1:2:3:4
OK

AT+CHE=1:2:3:4
OK
```

:::tip NOTE
- `AT_PARAM_ERROR` is returned when setting wrong or malformed value.
- In this case, the eight-channel mode is only for US915, AU915, CN470. US915 / AU915 range of values is 0~9, and CN470 range of values is 0~12. For example, use `AT+CHE=1:2:3:4` to enable ch0~31. `<value>`: maximum 12 decimal numbers and the range of values depends on region.
- According to LoRaWAN Regional Parameters v1.0.3revA, the first 64 channels are numbered 0 to 63, starting at 902.3 MHz and increments linearly by 200 kHz to 914.9 MHz. The next eight (8) channels numbered 64 to 71 are starting at 903.0 MHz and increments linearly by 1.6 MHz to 914.2 MHz.
:::

- US915 Uplink Channels & Attached List

| CHE | US915 Uplink Channels (125 kHz,4/5,Unit:MHz,CHS=0) |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 |
| 1 | 902.3 | 902.5 | 902.7 | 902.9 | 903.1 | 903.3 | 903.5 | 903.7 | Channel 0-7 |
| 2 | 903.9 | 904.1 | 904.3 | 904.5 | 904.7 | 904.9 | 905.1 | 905.3 | Channel 8-15 |
| 3 | 905.5 | 905.7 | 905.9 | 906.1 | 906.3 | 906.5 | 906.7 | 906.9 | Channel 16-23 |
| 4 | 907.1 | 907.3 | 907.5 | 907.7 | 907.9 | 908.1 | 908.3 | 908.5 | Channel 24-31 |
| 5 | 908.7 | 908.9 | 909.1 | 909.3 | 909.5 | 909.7 | 909.9 | 910.1 | Channel 32-39 |
| 6 | 910.3 | 910.5 | 910.7 | 910.9 | 911.1 | 911.3 | 911.5 | 911.7 | Channel 40-47 |
| 7 | 911.9 | 912.1 | 912.3 | 912.5 | 912.7 | 912.9 | 913.1 | 913.3 | Channel 48-55 |
| 8 | 913.5 | 913.7 | 913.9 | 914.1 | 914.3 | 914.5 | 914.7 | 914.9 | Channel 56-63 |
| 9 | 903.0 | 904.6 | 906.2 | 907.8 | 909.4 | 911.0 | 912.6 | 914.2 | Channel 64-71 |

:::tip NOTE
According to LoRaWAN Regional Parameters v1.0.3revA, the first 64 channels are numbered 0 to 63, starting at 902.3 MHz and increments linearly by 200 kHz to 914.9 MHz. The next eight (8) channels numbered 64 to 71 are starting at 903.0 MHz and increments linearly by 1.6 MHz to 914.2 MHz.
:::

- AU915 Uplink Channels & Attached List

| CHE | AU915 Uplink Channels (125 kHz, 4/5, Unit:MHz, CHS=0) |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 |
| 1 | 915.2 | 915.4 | 915.6 | 915.8 | 916.0 | 916.2 | 916.4 | 916.6 | Channel 0-7 |
| 2 | 916.8 | 917.0 | 917.2 | 917.4 | 917.6 | 917.8 | 918.0 | 918.2 | Channel 8-15 |
| 3 | 918.4 | 918.6 | 918.8 | 919.0 | 919.2 | 919.4 | 919.6 | 919.8 | Channel 16-23 |
| 4 | 920.0 | 920.2 | 920.4 | 920.6 | 920.8 | 921.0 | 921.2 | 921.4 | Channel 24-31 |
| 5 | 921.6 | 921.8 | 922.0 | 922.2 | 922.4 | 922.6 | 922.8 | 923.0 | Channel 32-39 |
| 6 | 923.2 | 923.4 | 923.6 | 923.8 | 924.0 | 924.2 | 924.4 | 924.6 | Channel 40-47 |
| 7 | 924.8 | 925.0 | 925.2 | 925.4 | 925.6 | 925.8 | 926.0 | 926.2 | Channel 48-55 |
| 8 | 926.4 | 926.6 | 926.8 | 927.0 | 927.2 | 927.4 | 927.6 | 927.8 | Channel 56-63 |
| 9 | 915.9 | 917.5 | 919.1 | 920.7 | 922.3 | 923.9 | 925.5 | 927.1 | Channel 64-71 |

:::tip NOTE
According to LoRaWAN Regional Parameters v1.0.3revA, the first 64 channels are numbered 0 to 63, starting at 915.2 MHz and increments linearly by 200 kHz to 927.8 MHz. The next eight (8) channels numbered 64 to 71 start at 915.9 MHz and increments linearly by 1.6 MHz to 927.1 MHz.
:::

- CN470 Uplink Channels & Attached List

| CHE | CN470 Uplink Channels (125 kHz, 4/5, Unit:MHz, CHS=0) |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | ENABLE Channel 0-95 | ENABLE Channel 0-95 | ENABLE Channel 0-95 | ENABLE Channel 0-95 | ENABLE Channel 0-95 | ENABLE Channel 0-95 | ENABLE Channel 0-95 | ENABLE Channel 0-95 | ENABLE Channel 0-95 |
| 1 | 470.3 | 470.5 | 470.7 | 470.9 | 471.1 | 471.3 | 471.5 | 471.7 | Channel 0-7 |
| 2 | 471.9 | 472.1 | 472.3 | 472.5 | 472.7 | 472.9 | 473.1 | 473.3 | Channel 8-15 |
| 3 | 473.5 | 473.7 | 473.9 | 474.1 | 474.3 | 474.5 | 474.7 | 474.9 | Channel 16-23 |
| 4 | 475.1 | 475.3 | 475.5 | 475.7 | 475.9 | 476.1 | 476.3 | 476.5 | Channel 24-31 |
| 5 | 476.7 | 476.9 | 477.1 | 477.3 | 477.5 | 477.7 | 477.9 | 478.1 | Channel 32-39 |
| 6 | 478.3 | 478.5 | 478.7 | 478.9 | 479.1 | 479.3 | 479.5 | 479.7 | Channel 40-47 |
| 7 | 479.9 | 480.1 | 480.3 | 480.5 | 480.7 | 480.9 | 481.1 | 481.3 | Channel 48-55 |
| 8 | 481.5 | 481.7 | 481.9 | 482.1 | 482.3 | 482.5 | 482.7 | 482.9 | Channel 56-63 |
| 9 | 483.1 | 483.3 | 483.5 | 483.7 | 483.9 | 484.1 | 484.3 | 484.5 | Channel 64-71 |
| 10 | 484.7 | 484.9 | 485.1 | 485.3 | 485.5 | 485.7 | 485.9 | 486.1 | Channel 72-79 |
| 11 | 486.3 | 486.5 | 486.7 | 486.9 | 487.1 | 487.3 | 487.5 | 487.7 | Channel 80-87 |
| 12 | 487.9 | 488.1 | 488.3 | 488.5 | 488.7 | 488.9 | 489.1 | 489.3 | Channel 88-95 |

:::tip NOTE
According to LoRaWAN Regional Parameters v1.0.3revA, the 96 channels are numbered 0 to 95, starting at 470.3 MHz and increment linearly by 200 kHz to 489.3 MHz.
:::

### AT+CHS

This command sets the node to single-channel mode.

| Command Type | Command          | Input Parameter | Return Value                                                           | Response |
| ------------ | ---------------- | --------------- | ---------------------------------------------------------------------- | -------- |
| Read         | `AT+CHS?`        | -               | `AT+CHS`: get or set single channels mode (only for US915 AU915 CN470) | OK       |
| Read         | `AT+CHS=?`       | -               | `AT+CHS=0` or frequency                                                | OK       |
| Write        | `AT+CHS=<input>` | frequency       | -                                                                      | OK       |

Example:

```
AT+CHS=?
AT+CHS=902300000
OK

AT+CHS=902300000
OK
```

:::tip NOTE
In this case, the single-channel mode is only for US915, AU915, CN470.

- US915 frequency range is from 902300000 to 914900000 and increments linearly by 200 kHz (ch0-63).
- US915 frequency range is from 903000000 to 914200000 and increments linearly by 1.6 MHz (ch64-71).
- AU915 frequency range is from 915200000 to 927800000 and increments linearly by 200 kHz (ch0-63).
- AU915 frequency range is from 915900000 to 927100000 and increments linearly by 1.6 MHz (ch64-71).
- CN470 frequency range is from 470300000 to 489300000 and increments linearly by 200 kHz (ch0-95).
- If you input `AT+CHS=903900000`, it will overwrite the `AT+MASK` and `AT+CHE` settings.
- `AT+MASK=0001(single channel mode: 903900000)`, the 0001 is the previous one, and the current is 90390000.
:::

- US915 Uplink Channels Frequency & Attached List

| US915 Uplink Channels (125k Hz, 4/5, Unit: MHz, CHS=Frequency) |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 |
| Channel 0-7 | 902300000 | 902500000 | 902700000 | 902900000 | 903100000 | 903300000 | 903500000 | 903700000 |
| Channel 8-15 | 903900000 | 904100000 | 904300000 | 904500000 | 904700000 | 904900000 | 905100000 | 905300000 |
| Channel 16-23 | 905500000 | 905700000 | 905900000 | 906100000 | 906300000 | 906500000 | 906700000 | 906900000 |
| Channel 24-31 | 907100000 | 907300000 | 907500000 | 907700000 | 907900000 | 908100000 | 908300000 | 908500000 |
| Channel 32-39 | 908700000 | 908900000 | 909100000 | 909300000 | 909500000 | 909700000 | 909900000 | 910100000 |
| Channel 40-47 | 910300000 | 910500000 | 910700000 | 910900000 | 911100000 | 911300000 | 911500000 | 911700000 |
| Channel 48-55 | 911900000 | 912100000 | 912300000 | 912500000 | 912700000 | 912900000 | 913100000 | 913300000 |
| Channel 56-63 | 913500000 | 913700000 | 913900000 | 914100000 | 914300000 | 914500000 | 914700000 | 914900000 |
| Channel 64-71 | 903000000 | 904600000 | 906200000 | 907800000 | 909400000 | 911000000 | 912600000 | 914200000 |

:::tip NOTE
According to LoRaWAN Regional Parameters v1.0.3revA, the first 64 channels are numbered 0 to 63, starting at 902. 3 MHz and increments linearly by 200 kHz to 914.9 MHz. The next eight (8) channels numbered 64 to 71 are starting at 903.0 MHz and increment linearly by 1.6 MHz to 914.2 MHz.
:::

- AU915 Uplink Channels Frequency & Attached List

| AU915 Uplink Channels (125 kHz, 4/5, Unit:MHz, CHS=Frequency) |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 | ENABLE Channel 0-71 |
| Channel 0-7 | 915200000 | 915400000 | 915600000 | 915800000 | 916000000 | 916200000 | 916400000 | 916600000 |
| Channel 8-15 | 916800000 | 917000000 | 917200000 | 917400000 | 917600000 | 917800000 | 918000000 | 918200000 |
| Channel 16-23 | 918400000 | 918600000 | 918800000 | 919000000 | 919200000 | 919400000 | 919600000 | 919800000 |
| Channel 24-31 | 920000000 | 920200000 | 920400000 | 920600000 | 920800000 | 921000000 | 921200000 | 921400000 |
| Channel 32-39 | 921600000 | 921800000 | 922000000 | 922200000 | 922400000 | 922600000 | 922800000 | 923000000 |
| Channel 40-47 | 923200000 | 923400000 | 923600000 | 923800000 | 924000000 | 924200000 | 924400000 | 924600000 |
| Channel 48-55 | 924800000 | 925000000 | 925200000 | 925400000 | 925600000 | 925800000 | 926000000 | 926200000 |
| Channel 56-63 | 926400000 | 926600000 | 926800000 | 927000000 | 927200000 | 927400000 | 927600000 | 927800000 |
| Channel 64-71 | 915900000 | 917500000 | 919100000 | 920700000 | 922300000 | 923900000 | 925500000 | 927100000 |

:::tip NOTE
According to LoRaWAN Regional Parameters v1.0.3revA, the first 64 channels are numbered 0 to 63, starting at 915.2 MHz and incrementing linearly by 200 kHz to 927.8 MHz. The next eight (8) channels numbered 64 to 71 start at 915.9 MHz and increment linearly by 1.6 MHz to 927.1 MHz.
:::

- CN470 Uplink Channels Frequency & Attached List

| CN470 Uplink Channels (125 kHz, 4/5, Unit:MHz, CHS=Frequency) |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ENABLE Channel 0-95 | ENABLE Channel 0-95 | ENABLE Channel 0-95 | ENABLE Channel 0-95 | ENABLE Channel 0-95 | ENABLE Channel 0-95 | ENABLE Channel 0-95 | ENABLE Channel 0-95 | ENABLE Channel 0-95 |
| Channel 0-7 | 470300000 | 470500000 | 470700000 | 470900000 | 471100000 | 471300000 | 471500000 | 471700000 |
| Channel 8-15 | 471900000 | 472100000 | 472300000 | 472500000 | 472700000 | 472900000 | 473100000 | 473300000 |
| Channel 16-23 | 473500000 | 473700000 | 473900000 | 474100000 | 474300000 | 474500000 | 474700000 | 474900000 |
| Channel 24-31 | 475100000 | 475300000 | 475500000 | 475700000 | 475900000 | 476100000 | 476300000 | 476500000 |
| Channel 32-39 | 476700000 | 476900000 | 477100000 | 477300000 | 477500000 | 477700000 | 477900000 | 478100000 |
| Channel 40-47 | 478300000 | 478500000 | 478700000 | 478900000 | 479100000 | 479300000 | 479500000 | 479700000 |
| Channel 48-55 | 479900000 | 480100000 | 480300000 | 480500000 | 480700000 | 480900000 | 481100000 | 481300000 |
| Channel 56-63 | 481500000 | 481700000 | 481900000 | 482100000 | 482300000 | 482500000 | 482700000 | 482900000 |
| Channel 64-71 | 483100000 | 483300000 | 483500000 | 483700000 | 483900000 | 484100000 | 484300000 | 484500000 |
| Channel 72-79 | 484700000 | 484900000 | 485100000 | 485300000 | 485500000 | 485700000 | 485900000 | 486100000 |
| Channel 80-87 | 486300000 | 486500000 | 486700000 | 486900000 | 487100000 | 487300000 | 487500000 | 487700000 |
| Channel 88-95 | 487900000 | 488100000 | 488300000 | 488500000 | 488700000 | 488900000 | 489100000 | 489300000 |

:::tip NOTE
According to LoRaWAN Regional Parameters v1.0.3revA, the 96 channels are numbered 0 to 95, starting at 470.3 MHz and increments linearly by 200 kHz to 489.3 MHz.
:::

### AT+BAND

This command sets numbers corresponding to active regions.

| Command Type | Command           | Input Parameter                        | Return Value                                                                                                                                                                                | **Response**                                   |
| ------------ | ----------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Read         | `AT+BAND?`        | -                                      | `AT+BAND`: get or set the active region 
 (0 = EU433, 1 = CN470, 2 = RU864, 3 = IN865, 4 = EU868, 5 = US915, 6 = AU915, 7 = KR920, 8 = AS923-1, 9 = AS923-2, 10 = AS923-3, 11 = AS923-4) | OK                                             |
| Read         | `AT+BAND=?`       | -                                      | `AT+BAND=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 or 11)`                                                                                                                                          | OK                                             |
| Write        | `AT+BAND=<input>` | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 or 11 | -                                                                                                                                                                                           | OK 
  `AT_PARAM_ERROR` 
 `AT_BUSY_ERROR` |

Example:
```
AT+BAND=?
AT+BAND=3
OK

AT+BAND=2
OK
```

:::tip NOTE
- If you are using US915, it is common to have an 8-ch Gateway/LNS setup with channels 8–15. To enable these channels, use `AT+MASK=0002`.
- `AT_PARAM_ERROR` is returned when setting wrong or malformed value.
- `AT_BUSY_ERROR` is returned when the set command process is already running.
- In this case, the default value is 4, and it depends on the region. 0: EU433 1: CN470 2: RU864 3: IN865 4: EU868 5: US915 6: AU915 7: KR920 8: AS923-1 9: AS923-2 `<Input>`: 1 decimal integer and the range of values is 0~8.
- RUI3 LoRa/LoRaWAN devices are divided into two variants - Low Frequency and High Frequency. Examples are the RAK4630(L) and RAK4630(H) devices.
    - Low frequency variant is compatible only to 0 - 1.
    - High frequency variant is compatible only to 2 - 9.
:::

## Button-Specific AT Commands

### at+button=`<button>:<port>:<data>`

This command is used to configure every button frame port and data.

| Command Type | Command                            | Input Parameter          | Return Value | Response |
| ------------ | ---------------------------------- | ------------------------ | ------------ | -------- |
| Other        | `at+button=<button>:<port>:<data>` | `<button>:<port>:<data>` | -            | OK       |

Where:

- **button** - Set the key for sending data, range 1-4.
- **port** - The sending port of LoRa, with a value range of 1-223.
- **data** - The data to be sent by the key, max. 10 characters.

Example: Configure button 1 to send data 1234 on frame port 1.

```
at+button=1:1:1234
OK
```

### at+heartbeat=`<interval>`

This command is used to configure the device's heartbeat. The heartbeat is used to send a packet to the server at a defined period. This command is disabled by default.

| Command Type | Command                   | Input Parameter                                                         | Return Value | Response |
| ------------ | ------------------------- | ----------------------------------------------------------------------- | ------------ | -------- |
| Write        | `at+heartbeat=<interval>` | Heartbeat sending interval, value range 1-120, unit hours. 0 = disable. | -            | OK       |

Example:

```
at+heartbeat=1
OK
```

### at+firmwarever

This command is used to view the firmware version of RAK7201V2 .

| Command Type | Command          | Input Parameter | Return Value                       | Response |
| ------------ | ---------------- | --------------- | ---------------------------------- | -------- |
| Read         | `at+firmwarever` | -               | The firmware version of the device | -        |

Example:

```
at+firmwarever
2.0
```

## Appendix 1: Data Rate

### EU868/AS923

| Data Rate | Configuration           | Indicative Physical Bit Rate (bit/s) |
| --------- | ----------------------- | ------------------------------------ |
| 0         | LoRa: SF12/125 kHz | 250                                  |
| 1         | LoRa: SF11/125 kHz | 440                                  |
| 2         | LoRa: SF10/125 kHz | 980                                  |
| 3         | LoRa: SF9/125 kHz  | 1760                                 |
| 4         | LoRa: SF8/125 kHz  | 3125                                 |
| 5         | LoRa: SF7/125 kHz  | 5470                                 |
| 6         | LoRa: SF7/250 kHz  | 11000                                |
| 7         | FSK: 50 kbps       | 50000                                |
| 8-15      | RFU                     | RFU                                  |

### KR920

| Data Rate | Configuration           | Indicative Physical Bit Rate (bit/s) |
| --------- | ----------------------- | ------------------------------------ |
| 0         | LoRa: SF12/125 kHz | 250                                  |
| 1         | LoRa: SF11/125 kHz | 440                                  |
| 2         | LoRa: SF10/125 kHz | 980                                  |
| 3         | LoRa: SF9/125 kHz  | 1760                                 |
| 4         | LoRa: SF8/125 kHz  | 3125                                 |
| 5         | LoRa: SF7/125 kHz  | 5470                                 |
| 6-15      | RFU                     | RFU                                  |

### US915

| Data Rate | Configuration           | Indicative Physical Bit Rate (bit/s) |
| --------- | ----------------------- | ------------------------------------ |
| 0         | LoRa: SF10/125 kHz | 980                                  |
| 1         | LoRa: SF9/125 kHz  | 1760                                 |
| 2         | LoRa: SF8/125 kHz  | 3125                                 |
| 3         | LoRa: SF7/125 kHz  | 5470                                 |
| 4         | LoRa: SF8/500 kHz  | 12500                                |
| 5-7       | RFU                     | RFU                                  |
| 8         | LoRa: SF12/500 kHz | 980                                  |
| 9         | LoRa: SF11/500 kHz | 1760                                 |
| 10        | LoRa: SF10/500 kHz | 3900                                 |
| 11        | LoRa: SF9/500 kHz  | 7000                                 |
| 12        | LoRa: SF8/500 kHz  | 12500                                |
| 13        | LoRa: SF7/500 kHz  | 21900                                |
| 14-15     | RFU                     | RFU                                  |

### AU915

| Data Rate | Configuration           | Indicative Physical Bit Rate (bit/s) |
| --------- | ----------------------- | ------------------------------------ |
| 0         | LoRa: SF12/125 kHz | 250                                  |
| 1         | LoRa: SF11/125 kHz | 440                                  |
| 2         | LoRa: SF10/125 kHz | 980                                  |
| 3         | LoRa: SF9/125 kHz  | 1760                                 |
| 4         | LoRa: SF8/125 kHz  | 3125                                 |
| 5         | LoRa: SF7/125 kHz  | 5470                                 |
| 6         | LoRa: SF8/500 kHz  | 12500                                |
| 7         | RFU                     | RFU                                  |
| 8         | LoRa: SF12/500 kHz | 980                                  |
| 9         | LoRa: SF11/500 kHz | 1760                                 |
| 10        | LoRa: SF10/500 kHz | 3900                                 |
| 11        | LoRa: SF9/500 kHz  | 7000                                 |
| 12        | LoRa: SF8/500 kHz  | 12500                                |

### IN865

| Data Rate | Configuration           | Indicative Physical Bit Rate (bit/s) |
| --------- | ----------------------- | ------------------------------------ |
| 0         | LoRa: SF12/125 kHz | 250                                  |
| 1         | LoRa: SF11/125 kHz | 440                                  |
| 2         | LoRa: SF10/125 kHz | 980                                  |
| 3         | LoRa: SF9/125 kHz  | 1760                                 |
| 4         | LoRa: SF8/125 kHz  | 3125                                 |
| 5         | LoRa: SF7/125 kHz  | 5470                                 |
| 6         | RFU                     | RFU                                  |
| 7         | FSK: 50 kbps       | 50000                                |
| 8-15      | RFU                     | RFU                                  |

## Appendix 2: TX Power

### EU868

By default, Max EIRP is considered to be +16 dBm.

| TX Power | Configuration (EIRP)  |
| -------- | --------------------- |
| 0        | Max EIRP              |
| 1        | Max EIRP - 2 db  |
| 2        | Max EIRP - 4 db  |
| 3        | Max EIRP - 6 db  |
| 4        | Max EIRP - 8 db  |
| 5        | Max EIRP - 10 db |
| 6        | Max EIRP - 12 db |
| 7        | Max EIRP - 14 db |
| 8-15     | RFU                   |

### US915

| TX Power | Configuration (Conducted Power) |
| -------- | ------------------------------- |
| 0        | 30 dBm - 2*TXpower         |
| 1        | 28 dBm                     |
| 2        | 26 dBm                     |
| 3-9      | -                               |
| 10       | 10 dBm                     |
| 11-15    | RFU                             |

### AU915

By default, Ma EIRP is considered to be +30 dBm.

| TX Power | Configuration (EIRP) |
| -------- | -------------------- |
| 0        | Max EIRP             |
| 1-10     | Max EIRP - 2*TXpower |
| 11-15    | RFU                  |

### KR920

By default, Max EIRP is considered to be +14 dBm.

| TX Power | Configuration (EIRP)  |
| -------- | --------------------- |
| 0        | Max EIRP              |
| 1        | Max EIRP - 2 db  |
| 2        | Max EIRP - 4 db  |
| 3        | Max EIRP - 6 db  |
| 4        | Max EIRP - 8 db  |
| 5        | Max EIRP - 10 db |
| 6        | Max EIRP - 12 db |
| 7        | Max EIRP - 14 db |
| 8-15     | RFU                   |

### AS923

By default, Max EIRP is considered to be 16 dBm.

| TX Power | Configuration (EIRP)  |
| -------- | --------------------- |
| 0        | Max EIRP              |
| 1        | Max EIRP - 2 db  |
| 2        | Max EIRP - 4 db  |
| 3        | Max EIRP - 6 db  |
| 4        | Max EIRP - 8 db  |
| 5        | Max EIRP - 10 db |
| 6        | Max EIRP - 12 db |
| 7        | Max EIRP - 14 db |
| 8-15     | RFU                   |

### IN865

By default, Max EIRP is considered to be 30 dBm.

| TX Power | Configuration (EIRP)  |
| -------- | --------------------- |
| 0        | Max EIRP              |
| 1        | Max EIRP - 2 db  |
| 2        | Max EIRP - 4 db  |
| 3        | Max EIRP - 6 db  |
| 4        | Max EIRP - 8 db  |
| 5        | Max EIRP - 10 db |
| 6        | Max EIRP - 12 db |
| 7        | Max EIRP - 14 db |
| 8        | Max EIRP - 16 db |
| 9        | Max EIRP - 18 db |
| 10       | Max EIRP - 20 db |
| 11-15    | RFU                   |

