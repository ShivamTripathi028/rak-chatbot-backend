---
slug: /product-categories/wisnode/rak7431/at-command-manual/
title: RAK7431 WisNode Bridge Serial AT Command Manual
description: For an easier experience with your LoRaWAN Module, a comprehensive list of commands for the LoRa P2P and LoRaWAN communication is provided. A serial communication interface is also presented for the two-way communication of the RAK7431.
image: "https://images.docs.rakwireless.com/wisnode/rak7431/datasheet/rak7431.png"
keywords:
  - RAK7431
  - wisnode
sidebar_label: AT Command Manual
---

# RAK7431 AT Command Manual

## Overview

This document applies to Modbus RS485 to LoRaWAN Bridge products. The supported product models include RAK7421/RAK7431/RAK7425.

### AT Command Syntax

In general, the AT Command for the RAK7431 start with `AT` or `at` and ends with `<CR> <LF>`.
* AT commands can be divided into:
    * **Reading commands** - read the configuration or status of the device, which is in the format of: `AT+<x>`
    * **Write commands** - write/modify the device configuration, which is in the format of: `AT+<x>=<m>:<n>`
    The command name and parameters are separated by "**=**". If there are multiple parameters, the parameters are separated by "**:**"
    * **Test commands** - is the test command executable, which is in the format of: `AT+<x>=?`

| Condition                        | Response                                    |
| -------------------------------- | ------------------------------------------- |
| Normal response with information | `<Response><CR><LF>OK<CR><LF>`              |
| Normal response                  | `OK<CR><LF>`                                |
| Response when an error occurs    | `ERROR <Error code>:<Error packet><CR><LF>` |

:::tip NOTE
AT commands are not case sensitive.
:::

### USB Configuration Interface

The devices are equipped with a standard USB interface for configuring the AT commands. The serial parameters are as follows:

| Parameter    | Value  |
| ------------ | ------ |
| Baud rate    | 115200 |
| Data bit     | 8      |
| Stop bit     | 1      |
| Verification | No     |

### Common Errors

| Error Code | Description                     |
| ---------- | ------------------------------- |
| ERROR 1    | Unsupported command             |
| ERROR 2    | Syntax error                    |
| ERROR 3    | Storage failure                 |
| ERROR 4    | System busy                     |
| ERROR 5    | Parameter format / number error |
| ERROR 6    | Insufficient resources          |
| ERROR 7    | Parameter out of valid range    |

## LoRaWAN Commands

1. **AT+DEVEUI**

This command reads or modifies the LoRaWAN Device EUI. The command takes effect after restart.

| Operation | AT Command               | Response                                                                                             |
| --------- | ------------------------ | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+DEVEUI`              | `<dev_eui>` 
 `OK`                                                                                |
| Write     | `AT+DEVEUI=<device_eui>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+DEVEUI=?`            | `OK`                                                                                                 |

| Parameter   | Information                                                     |
| ----------- | --------------------------------------------------------------- |
| **dev_eui** | **Device EUI**: Hexadecimal characters, 16 bytes in length |

2. **AT+REGION**

This command reads or modifies the Working Frequency Region/Band of the device. It will take effect after restart.

| Operation | AT Command           | Response                                                                                             |
| --------- | -------------------- | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+REGION`          | `<region>` 
 `OK`                                                                                 |
| Write     | `AT+REGION=<region>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+REGION=?`        | `OK`                                                                                                 |

| Parameter  | Information                                                                                           |
| ---------- | ----------------------------------------------------------------------------------------------------- |
| **region** | **Supports frequency bands:** EU433, CN470, CN470ALI, RU864, IN865, EU868, US915, AU915, KR920, AS923 |

3. **AT+JOINMODE**

This command reads or modifies the LoRaWAN Activation Mode of the device. It will take effect after restart.

| Operation | AT Command           | Response                                                                                             |
| --------- | -------------------- | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+JOINMODE`        | `<mode>` 
 `OK`                                                                                   |
| Write     | `AT+JOINMODE=<mode>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+JOINMODE=?`      | `OK`                                                                                                 |

| Parameter | Information                                |
| --------- | ------------------------------------------ |
| **mode**  | **Supported activation mode:** ABP or OTAA |

4.	**AT+PUBLIC**

This command reads or modifies the LoRaWAN Public Settings of the device. The working mode is set to Public by default (1 value of the parameter). The modification will take effect after restart.

| Operation | AT Command      | Response                                                                                             |
| --------- | --------------- | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+PUBLIC`     | `<x>` 
 `OK`                                                                                      |
| Write     | `AT+PUBLIC=<x>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+PUBLIC=?`   | `OK`                                                                                                 |

| Parameter | Information                                          |
| --------- | ---------------------------------------------------- |
| **x**     | **Is the node working with public LoRaWAN network?** |
| 0         | Not working in Public mode                           |
| 1         | Working in Public mode                               |

5.	**AT+CLASS**

This command reads or modifies the LoRaWAN working Class of the device. Effective immediately after modification.

| Operation | AT Command         | Response                                                                                             |
| --------- | ------------------ | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+CLASS`         | `<class>` 
 `OK`                                                                                  |
| Write     | `AT+CLASS=<class>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+CLASS=?`       | `OK`                                                                                                 |

| Parameter | Information                   |
| --------- | ----------------------------- |
| **class** | **Supported device Classes:** |
| A         | Class A                       |
| B         | Class B                       |
| C         | Class C                       |

6.	**AT+APPEUI**

The APPEUI parameter is valid when OTAA is activated. The modification will take effect after restart.

| Operation | AT Command            | Response                                                                                             |
| --------- | --------------------- | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+APPEUI`           | `<app_eui>` 
 `OK`                                                                                |
| Write     | `AT+APPEUI=<app_eui>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+APPEUI=?`         | `OK`                                                                                                 |

| Parameter   | Information                                                    |
| ----------- | -------------------------------------------------------------- |
| **app_eui** | **Application EUI:** Hexadecimal character, 16 bytes in length |

7.	**AT+APPKEY**

The APPKEY parameter is valid in OTAA Activation Mode. The modification will take effect after restart.

| Operation | AT Command            | Response                                                                                             |
| --------- | --------------------- | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+APPKEY`           | `<app_key>` 
 `OK`                                                                                |
| Write     | `AT+APPKEY=<app_key>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+APPKEY=?`         | `OK`                                                                                                 |

| Parameter   | Information                                                         |
| ----------- | ------------------------------------------------------------------- |
| **app_key** | **Application Key:** Hexadecimal character, 32 bytes in length |

8. **AT+DEVADDR**

The DEVADDR parameter is valid in ABP Activation Mode. The modification will take effect after restart.

| Operation | AT Command              | Response                                                                                             |
| --------- | ----------------------- | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+DEVADDR`            | `<dev_addr>` 
 `OK`                                                                               |
| Write     | `AT+DEVADDR=<dev_addr>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+DEVADDR=?`          | `OK`                                                                                                 |

| Parameter    | Information                                                       |
| ------------ | ----------------------------------------------------------------- |
| **dev_addr** | **Device Address:** Hexadecimal character, 8 bytes in length |

9.	**AT+APPSKEY**

The APPSKEY parameter is valid in ABP Activation Mode. The modification will take effect after restart.

| Operation | AT Command              | Response                                                                                             |
| --------- | ----------------------- | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+APPSKEY`            | `<apps_key>` 
 `OK`                                                                               |
| Write     | `AT+APPSKEY=<apps_key>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+APPSKEY=?`          | `OK`                                                                                                 |

| Parameter    | Information                                                                 |
| ------------ | --------------------------------------------------------------------------- |
| **apps_key** | **Application Session Key:** Hexadecimal character, 32 bytes in length |

10.	**AT+NWKSKEY**

The NWKSKEY parameter is valid in ABP Activation Mode. The modification will take effect after restart.

| Operation | AT Command             | Response                                                                                             |
| --------- | ---------------------- | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+NWKSKEY`           | `<nwks_key>` 
 `OK`                                                                               |
| Write     | `AT+NWKSKEY=<nwkskey>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+NWKSKEY=?`         | `OK`                                                                                                 |

| Parameter    | Information                                                             |
| ------------ | ----------------------------------------------------------------------- |
| **nwks_key** | **Network Session Key:** Hexadecimal character, 32 bytes in length |

11. **AT+ADR**

Turn on/off the LoRaWAN dynamic rate adjustment function of the device, which is “on” by default. The modification will take effect immediately.

| Operation | AT Command   | Response                                                                                             |
| --------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+ADR`     | `<n>` 
 `OK`                                                                                      |
| Write     | `AT+ADR=<n>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+ADR=?`   | `OK`                                                                                                 |

| Parameter | Information            |
| --------- | ---------------------- |
| **n**     | **Adaptive Data Rate** |
| 0         | Disable ADR            |
| 1         | Enable ADR             |

12.	 **AT+DATARATE**

Read/modify the LoRaWAN DataRate setting of the device, which is valid when the ADR function is turned off. The modification will take effect immediately.

| Operation | AT Command        | Response                                                                                             |
| --------- | ----------------- | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+DATARATE`     | `<n>` 
 `OK`                                                                                      |
| Write     | `AT+DATARATE=<n>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+DATARATE=?`   | `OK`                                                                                                 |

| Parameter | Information                              |
| --------- | ---------------------------------------- |
| **n**     | **LoRaWAN DataRate**                     |
| 0 ~ 7     | DataRate from 0 to 7 s is possible. |

:::tip NOTE
The DataRate value and the default value are related to LoRaWAN regional parameters. Refer to [Appendix I: DataRate list of each region](#appendix-i-data-rate-of-each-region) in this document.
:::

13.	**AT+CONFIRM**

Turn on/off the LoRaWAN packet confirmation mechanic, which is set to be “on” by default. The modification will take effect immediately.

When the confirm function is enabled, the packets sent by the device will require the LoRa network server to send an ACK response. Unless a confirmation is received the device will resend the packet. For more information on the resending mechanic refer to “**14. AT+RETRY**”.

| Operation | AT Command       | Response                                                                                             |
| --------- | ---------------- | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+CONFIRM`     | `<n>` 
 `OK`                                                                                      |
| Write     | `AT+CONFIRM=<n>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+CONFIRM=?`   | `OK`                                                                                                 |

| Parameter | Information                |
| --------- | -------------------------- |
| **n**     | **Type of uplink packets** |
| 0         | Unconfirmed uplink packets |
| 1         | Confirmed uplink packets   |

14. **AT+RETRY**

Set the maximum number of retry attempts of the same LoRaWAN message, that will be valid when the confirm function is enabled. The default value is 3. The modification will take effect immediately.

When retry = n (n! = 1), if the device does not receive an ACK of a LoRaWAN message, it will resend the message until the ACK is received, or the retry counter expires.

| Operation | AT Command     | Response                                                                                             |
| --------- | -------------- | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+RETRY`     | `<n>` 
 `OK`                                                                                      |
| Write     | `AT+RETRY=<n>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+RETRY=?`   | `OK`                                                                                                 |

| Parameter | Information                                  |
| --------- | -------------------------------------------- |
| **n**     | **Max resend times**                         |
| 1 ~ 8     | The number of retries can be between 1 and 8 |

15. **AT+CHANNEL**

When the LoRaWAN channel plan of the device is CN470 / US915 / AU915, it can be read/modified through this instruction. After execution of this command, all channels from “start ID” to “end ID” in the instruction parameters are turned on, and the other channels are turned off. The modification will take effect after restart.

When the device is working in one of the following bands this command can only be used for reading the parameters: EU433 / RU864 / IN865 / EU868 / KR920 / AS923.

| Operation                                                      | AT Command                     | Response                                                                                             |
| -------------------------------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------- |
| Read                                                           | `AT+CHANNEL`                   | `<id>:<freq>:<drmin>:<drmax>` 
...
 `OK`                                                       |
| Write
(Only valid when Region
 is CN470 / US915 / AU915) | `AT+CHANNEL=<startid>:<endid>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test                                                           | `AT+CHANNEL=?`                 | `OK`                                                                                                 |

| Parameter   | Information                           |
| ----------- | ------------------------------------- |
| **id**      | Channel ID                            |
| **freq**    | Center frequency of channel, unit: Hz |
| **drmin**   | DataRate (Min)                        |
| **drmax**   | DataRate (Max)                        |
| **startid** | Start channel ID                      |
| **endid**   | Stop channel ID                       |

16. **AT+ADDCHANNEL**

Add a LoRaWAN channel.

This instruction is valid when the working frequency band of LoRaWAN is EU433 / RU864 / EU868 / KR920 / AS923. The modification will take effect after restart.

| Operation | AT Command                             | Response                                                                                             |
| --------- | -------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Write     | `AT+ADDCHANNEL=<freq>:<drmin>:<drmax>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+ADDCHANNEL=?`                      | `OK`                                                                                                 |

| Parameter | Information                           |
| --------- | ------------------------------------- |
| **freq**  | Center frequency of channel, unit: Hz |
| **drmin** | DataRate (Min)                        |
| **drmax** | DataRate (Max)                        |

17. **AT+RMCHANNEL**

Delete a LoRaWAN channel.

This instruction is valid when the working frequency band is EU433 / RU864 / EU868 / KR920 / AS923. The modification takes effect after restart.

| Operation | AT Command                            | Response                                                                                             |
| --------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Write     | `AT+RMCHANNEL=<freq>:<drmin>:<drmax>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+RMCHANNEL=?`                      | `OK`                                                                                                 |

| Parameter | Information                           |
| --------- | ------------------------------------- |
| **freq**  | Center frequency of channel, unit: Hz |
| **drmin** | DataRate (Min)                        |
| **drmax** | DataRate (Max)                        |

18. **AT+CHANMASK**

Read the currently configured LoRaWAN Channel Mask. It is determined by the currently open channels. This instruction is “read-only”.

| Operation | AT Command      | Response            |
| --------- | --------------- | ------------------- |
| Read      | `AT+CHANMASK`   | `<chanmsk>`
`OK` |
| Test      | `AT+CHANMASK=?` | `OK`                |

| Parameter    | Information                                                                                   |
| ------------ | --------------------------------------------------------------------------------------------- |
| **chanmask** | **Channel mask:** Hexadecimal string, right to left corresponding channel ID from low to high |

19. **AT+TXPOWER**

The TXPOWER parameter is valid when the ADR function is turned off. The modification will take effect immediately.

| Operation | AT Command           | Response                                                                                             |
| --------- | -------------------- | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+TXPOWER`         | `<txpwr>`
`OK`                                                                                    |
| Write     | `AT+TXPOWER=<txpwr>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+TXPOWER=?`       | `OK`                                                                                                 |

| Parameter | Information                                                                                                                                                                                                                                                                                                                                            |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **txpwr** | Transmit power (dBm, floating-point)
The value range is 0 ~ maxeirp, and the effective step size is 2dbm, that is, txpwr = maxeirp – 2 * n, and n is an integer greater than or equal to 0
The maxeirp is the Maximum EIRP (Equivalent Isotropic Radiated Power) defined for the specific band you are using in the LoRa Alliance documentation. |

20. **AT+PINGNB**

Set the PingSlot Number in each Beacon Period for Class B mode. The number of ping slots determines the period of the downlink packet of the device. The modification will take effect after restart.

| Operation | AT Command      | Response                                                                                              |
| --------- | --------------- | ----------------------------------------------------------------------------------------------------- |
| Read      | `AT+PINGNB`     | `<N>`
`OK`                                                                                         |
| Write     | `AT+PINGNB=<N>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<message>` |
| Test      | `AT+PINGNB=?`   | `OK`                                                                                                  |

| Parameter | Information                                                                   |
| --------- | ----------------------------------------------------------------------------- |
| **N**     | PingSlot Number in Beacon Period
1
2
4
8
16
32
64
128 |

21. **AT+LPTP**

LoRa Private Transport Protocol (LPTP) is a RAK proprietary message splitting protocol, which can send data with a length exceeding the maximum permissible size, using multiple messages. As it is proprietary it only works with the RAK LoRa networks server built-into our commercial gateways. It is “Off” by default. The modification will take effect immediately.

| Operation | AT Command    | Response                                                                                             |
| --------- | ------------- | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+LPTP`     | `<x>`
`OK`                                                                                        |
| Write     | `AT+LPTP=<x>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+LPTP=?`   | `OK`                                                                                                 |

| Parameter | Information     |
| --------- | --------------- |
| **x**     | **LPTP status** |
| 0         | disabled        |
| 1         | enabled         |

## Data Interface Commands

1.	**AT+BAUDRATE**

The command is used to read or modify the baud rate of the device's data serial port. The modification will take affect after restarting.

| Operation | AT Command               | Response                                                                                              |
| --------- | ------------------------ | ----------------------------------------------------------------------------------------------------- |
| Read      | `AT+BAUDRATE`            | `<baudrate>`
`OK`                                                                                  |
| Write     | `AT+BAUDRATE=<baudrate>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<message>` |
| Test      | `AT+BAUDRATE=?`          | `OK`                                                                                                  |

| Parameter    | Information                                                                                          |
| ------------ | ---------------------------------------------------------------------------------------------------- |
| **baudrate** | Baud rate of serial port data:
2400
4800
9600
14400
19200
38400
57600
115200 |

2. **AT+DATABIT**

Read or modify the data bit of the serial data. The modification will take effect after restart.

| Operation | AT Command              | Response                                                                                              |
| --------- | ----------------------- | ----------------------------------------------------------------------------------------------------- |
| Read      | `AT+DATABIT`           | `<databit>`
`OK`                                                                                   |
| Write     | `AT+DATABIT=<databit>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<message>` |
| Test      | `AT+DATABIT=?`         | `OK`                                                                                                  |

| Parameter   | Information                       |
| ----------- | --------------------------------- |
| **databit** | **Data bit of serial port data:** |
| 7           | 7th bit                           |
| 8           | 8th bit                           |

3. **AT+STOPBIT**

Read or modify the serial port data stop bit. The modification will take effect after restart.

| Operation | AT Command                   | Response                                                                                              |
| --------- | ---------------------------- | ----------------------------------------------------------------------------------------------------- |
| Read      | `AT+STOPBIT`                 | `<stopbit>`
`OK`                                                                                   |
| Write     | `Write	AT+STOPBIT=<stopbit>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<message>` |
| Test      | `AT+STOPBIT=?`               | `OK`                                                                                                  |

| Parameter   | Information          |
| ----------- | -------------------- |
| **stopbit** | **Serial stop bit:** |
| 1           | 1bit                 |
| 1.5         | 1.5bits              |
| 2           | 2bits                |

4. **AT+PARITY**

Read or modify the parity check bit of the data. The modification will take effect after restart.

| Operation | AT Command           | Response                                                                                              |
| --------- | -------------------- | ----------------------------------------------------------------------------------------------------- |
| Read      | `AT+PARITY`          | `<parity>`
`OK`                                                                                    |
| Write     | `AT+PARITY=<parity>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<message>` |
| Test      | `AT+PARITY=?`        | `OK`                                                                                                  |

| Parameter  | Information       |
| ---------- | ----------------- |
| **parity** | **Parity check:** |
| NONE       | No check          |
| EVEN       | Even parity check |
| ODD        | Odd parity check  |

5. **AT+DTUMODE**

Read or modify the operating mode of the device’s data interface. The data interface supports two modes: P2P and MODBUS. The modification will take effect immediately.

| Operation | AT Command          | Response                                                                                              |
| --------- | ------------------- | ----------------------------------------------------------------------------------------------------- |
| Read      | `AT+DTUMODE`        | `<mode>`
`OK`                                                                                      |
| Write     | `AT+DTUMODE=<mode>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<message>` |
| Test      | `AT+DTUMODE=?`      | `OK`                                                                                                  |

| Parameter | Information         |
| --------- | ------------------- |
| **mode**  | **Operating mode:** |
| P2P       | Point to point mode |
| MODBUS    | Modbus mode         |

6. **AT+MODBUSTIMEOUT**

Read or modify the Modbus instruction timeout of the device. It is valid when the data interface is in MODBUS Mode. The modification will take effect immediately.

| Operation | AT Command             | Response                                                                                              |
| --------- | ---------------------- | ----------------------------------------------------------------------------------------------------- |
| Read      | `AT+MODBUSTIMEOUT`     | `<n>`
`OK`                                                                                         |
| Write     | `AT+MODBUSTIMEOUT=<n>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<message>` |
| Test      | `AT+MODBUSTIMEOUT=?`   | `OK`                                                                                                  |

| Parameter | Information          |
| --------- | -------------------- |
| n         | Modbus timeout in ms |

7. **AT+TRANSPARENT**

When the serial data port of the device works in MODBUS mode, the data encapsulation format can be divided into two types: transparent transmission mode and non-transparent transmission mode.

In transparent mode, the Modbus execution instruction response data (data, received by the node) will be directly forwarded through LoRaWAN network.

In the non-transparent mode, the Modbus execution instruction response data (data, received by the node) will be encapsulated in the message header according to the Modbus protocol, and then transmitted to the server through LoRaWAN. Please refer to [**Appendix II: MODBUS Data Encapsulation Protocol**](#appendix-ii-modbus-data-encapsulation-protocol) for details.

Non-transparent mode is the default one. The modification will take effect immediately.

| Operation | AT Command           | Response                                                                                              |
| --------- | -------------------- | ----------------------------------------------------------------------------------------------------- |
| Read      | `AT+TRANSPARENT`     | `<n>`
`OK`                                                                                         |
| Write     | `AT+TRANSPARENT=<n>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<message>` |
| Test      | `AT+TRANSPARENT=?`   | `OK`                                                                                                  |

| Parameter | Information          |
| --------- | -------------------- |
| **n**     | **Operating mode:**  |
| 0         | non-transparent mode |
| 1         | transparent mode     |

8. **AT+MODBUSRETRY**

When the device works in MODBUS mode, with this command the number of retries, when a MODBUS instruction does not get response, is specified. By default, there is no retransmission value added. The modification will take effect immediately.

| Operation | AT Command           | Response                                                                                              |
| --------- | -------------------- | ----------------------------------------------------------------------------------------------------- |
| Read      | `AT+MODBUSRETRY`     | `<n>`
`OK`                                                                                         |
| Write     | `AT+MODBUSRETRY=<n>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<message>` |
| Test      | `AT+MODBUSRETRY=?`   | `OK`                                                                                                  |

| Parameter | Information            |
| --------- | ---------------------- |
| **n**     | **Number of retries:** |
| 0         | No retry               |
| 1 ~ 8     | 1 ~ 8 retries          |

9. **AT+ENABLEPOLL**

When the device works in MODBUS mode, it supports the timed polling function.

This means that the device will perform a polling operation every given period (polling cycle). During polling, the device will send the pre-added MODBUS instructions in turn and forward the corresponding response data through the LoRaWAN network.

The device turns on timed polling by default. The modification shall take effect after restart.

| Operation | AT Command          | Response                                                                                              |
| --------- | ------------------- | ----------------------------------------------------------------------------------------------------- |
| Read      | `AT+ENABLEPOLL`     | `<n>`
`OK`                                                                                         |
| Write     | `AT+ENABLEPOLL=<n>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<message>` |
| Test      | `AT+ENABLEPOLL=?`   | `OK`                                                                                                  |

| Parameter | Information                   |
| --------- | ----------------------------- |
| **n**     | **Scheduled polling status:** |
| 0         | Disabled                      |
| 1         | Enabled                       |

10. **AT+POLLPERIOD**

This command sets/reads the scheduled polling cycle. This command only works if scheduled polling is enabled. The modification takes effect after the next polling cycle or a restart.

| Operation | AT Command          | Response                                                                                              |
| --------- | ------------------- | ----------------------------------------------------------------------------------------------------- |
| Read      | `AT+POLLPERIOD`     | `<n>`
`OK`                                                                                         |
| Write     | `AT+POLLPERIOD=<n>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<message>` |
| Test      | `AT+POLLPERIOD=?`   | `OK`                                                                                                  |

| Parameter | Information                  |
| --------- | ---------------------------- |
| **n**     | **Polling cycle in seconds** |

11. **AT+ADDPOLL**

Add a polling instruction with this command.
Up to 32 polling instructions are supported. The modification takes effect after the next polling cycle or a restart.

| Operation | AT Command              | Response                                                                                              |
| --------- | ----------------------- | ----------------------------------------------------------------------------------------------------- |
| Write     | `AT+ADDPOLL=<n>:<xxxx>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<message>` |
| Test      | `AT+ADDPOLL=?`          | `OK`                                                                                                  |

| Parameter | Information                                                                           |
| --------- | ------------------------------------------------------------------------------------- |
| **n**     | **Polling instruction ID, value range 1 ~ 127**                                       |
| xxxx      | Polling instruction content, hexadecimal string, maximum instruction length 128 bytes |

12. **AT+RMPOLL**

Delete a polling instruction. The modification takes effect after the next polling cycle or a restart

| Operation | AT Command      | Response                                                                                              |
| --------- | --------------- | ----------------------------------------------------------------------------------------------------- |
| Write     | `AT+RMPOLL=<n>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<message>` |
| Test      | `AT+RMPOLL=?`   | `OK`                                                                                                  |

| Parameter | Information                                     |
| --------- | ----------------------------------------------- |
| **n**     | **Polling instruction ID, value range 1 ~ 127** |

13. **AT+POLLTASK**

Query the list of scheduled polling instructions.

| Operation | AT Command      | Response                                                                                                       |
| --------- | --------------- | -------------------------------------------------------------------------------------------------------------- |
| Write     | `AT+POLLTASK`   | When it is successful:
`<n>:<xxxx>`
...
`OK`
When modification fails: 
`ERROR <code>:<message>` |
| Test      | `AT+POLLTASK=?` | `OK`                                                                                                           |

| Parameter | Information                                 |
| --------- | ------------------------------------------- |
| **n**     | Polling instruction ID, value range 1 ~ 127 |
| xxxx      | Instruction content, hexadecimal string     |

14.	**AT+ADDSCHEDULETASK**

Schedule an instruction. The modification takes effect immediately after setting.
The time in the command is local time.

| Operation | AT Command                                              | Response                                                                                              |
| --------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Write     | `AT+ADDSCHEDULETASK=<id>:<type>:<w>:<h>:<m>:<s>:<data>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<message>` |
| Test      | `AT+ADDSCHEDULETASK =?`                                 | `OK`                                                                                                  |

| Parameter | Information                                                                                              |
| --------- | -------------------------------------------------------------------------------------------------------- |
| **id**    | Task ID，value is： 1 ~ 127                                                                              |
| **type**  | the type of schedule task:
**WEEK** - once a week
**DAY** - once a day
**HOUR** - once an hour* |
| **w**     | WEEK, only need add the value when the type = WEEK;
0 - For Sunday
1 ~ 6 For Monday ~ Saturday     |
| **h**     | Hour:  0 ~ 23                                                                                            |
| **m**     | Minute： 0 ~ 59                                                                                          |
| **s**     | Second： 0 ~ 59                                                                                          |

:::tip NOTE
*If selected type is HOUR, the parameter `<h>` is not used from the system.
:::

15. **AT+RMSCHEDULETASK**

A command to delete a scheduled instruction. The modification takes effect immediately after setting.

| Operation | AT Command              | Response                                                                                              |
| --------- | ----------------------- | ----------------------------------------------------------------------------------------------------- |
| Write     | `AT+RMSCHEDULETASK=<n>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<message>` |
| Test      | `AT+RMSCHEDULETASK=?`   | `OK`                                                                                                  |

| Parameter | Information                |
| --------- | -------------------------- |
| **n**     | Task ID，value is: 1 ~ 127 |

## System Related Commands

1.	**AT+TIMEZONE**

With this command, the time zone of the device is set.

| Operation | AT Command         | Response                                                                                              |
| --------- | ------------------ | ----------------------------------------------------------------------------------------------------- |
| Read      | `AT+TIMEZONE`      | `<TZ>`
`OK`                                                                                        |
| Write     | `AT+TIMEZONE=<TZ>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<message>` |
| Test      | `AT+TIMEZONE=?`    | `OK`                                                                                                  |

| Parameter | Information             |
| --------- | ----------------------- |
| **TZ**    | UTC time zone: -12 ~ 12 |

2.	**AT+VERSION**

Read the firmware version of the device.

| Operation | AT Command   | Response                                                                                                                     |
| --------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| Read      | `AT+VERSION` | When the modification is successful:
`
<a>.**.<cccc>`
`OK`
When modification fails: 
`ERROR <code>:<packet>` |

| Parameter    | Information                              |
| ------------ | ---------------------------------------- |
| **a.b.cccc** | Firmware Version, for example “1.1.0050” |

3.	<b>AT+SYSLOGLVL**

Read or set the system log level.
The module turns off the system log output by default. The user can modify the log output level through this command. The modification takes effect immediately after setting.

| Operation | AT Command             | Response       |
| --------- | ---------------------- | -------------- |
| Read      | `AT+SYSLOGLVL`         | `<TZ>`
`OK` |
| Write     | `AT+SYSLOGLVL=<level>` | `OK`           |
| Test      | `AT+SYSLOGLVL=?`       | `OK`           |

| Parameter | Information                                           |
| --------- | ----------------------------------------------------- |
| **level** | **Output log level**                                  |
| 0         | does not output any logs                              |
| 1 ~ 6     | log with output level less than or equal to the value |

4. **AT+ECHO**

Turns local echo of the AT command-line interface on/off. Echo is turned off by default. It takes effect immediately after modification and is automatically turned off after a restart.

| Operation | AT Command    | Response                                                                                             |
| --------- | ------------- | ---------------------------------------------------------------------------------------------------- |
| Write     | `AT+ECHO=<n>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |

| Parameter | Information    |
| --------- | -------------- |
| **n**     | **Local echo** |
| 0         | Disabled       |
| 1         | Enabled        |

5. **AT+BOOT**

The device supports switching to boot mode. In boot mode, the dedicated upgrade software can be used for firmware update.

| Operation | AT Command | Response      |
| --------- | ---------- | ------------- |
| Write     | `AT+BOOT`  | `<BOOT MODE>` |

6.	**AT+RESTART**
Reboot the device.

| Operation | AT Command   | Response |
| --------- | ------------ | -------- |
| Write     | `AT+RESTART` | `Null`   |

7.	**AT+FACTORY**

The command restores the device to the factory settings. This operation will last for about 60s. Do not cut off the power supply of the device before it automatically restarts.

| Operation | AT Command   | Response |
| --------- | ------------ | -------- |
| Write     | `AT+FACTORY` | `Null`   |

8.	**AT+SYSTIME**

Show the real running time.

| Operation | AT Command   | Response         |
| --------- | ------------ | ---------------- |
| Write     | `AT+SYSTIME` | `<time>`
`OK` |

| Parameter | Information                          |
| --------- | ------------------------------------ |
| **time**  | Timestamp in UNIX format, in seconds |

9.	**AT+DATETIME**

Show the synchronized with the LoRaWAN Network Server time. Needs LoRaWAN1.0.3 specification support from the server side.

| Operation | AT Command    | Response             |
| --------- | ------------- | -------------------- |
| Read      | `AT+DATETIME` | `<datetime>`
`OK` |

| Parameter    | Information                        |
| ------------ | ---------------------------------- |
| **datetime** | Date / Time in YYYY/MM/DD hh:mm:ss |

10. **AT+SYSINFO**

This command gives the system information of the device.

| Operation | AT Command   | Response                                                                  |
| --------- | ------------ | ------------------------------------------------------------------------- |
| Read      | `AT+SYSINFO` | `<model>`
`<sn>`
`<version>`
`<vendor>`
`<copyright>`
`OK` |

| Parameter     | Information       |
| ------------- | ----------------- |
| **model**     | Model info        |
| **sn**        | Product SN info   |
| **version**   | Firmware version  |
| **vendor**    | Manufacturer info |
| **copyright** | Copyright info    |

11. **AT+WAKEUPBYTE**

This command allows you to check or change the wake up byte.

| Operation | AT Command           | Response         |
| --------- | -------------------- | ---------------- |
| Read      | `AT+WAKEUPBYTE`      | `<XX>`
`<OK>` |
| Write     | `AT+WAKEUPBYTE=<XX>` | `<OK>`           |

| Parameter | Information  |
| --------- | ------------ |
| **XX**    | Wake up byte |

:::tip NOTE
Default value is 0xAA.
:::

## Event Notification

When the working state of the module changes, an event notification will be output through the AT command-line interface.
The event notification format is:

```sh
EVENT:[EVENT_ID]:[EVENT_MSG]:<ADDITIONAL_INFO>
```

| Event               | Description                                                                                                                                           |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **EVENT_ID**        | Event ID                                                                                                                                              |
| **EVENT_MSG**       | Event name                                                                                                                                            |
| **ADDITIONAL_INFO** | Additional information - Optional 
 Some events need to output additional information. Multiple additional information sets are separated by ":" |

The module supports the following event notifications:

| ID | EVENT_MSG     | Description                              |
| -- | ------------- | ---------------------------------------- |
| 0  | STARTUP       | System startup complete                  |
| 1  | JOIN_NETWORK  | Successful join to the LoRaWAN network   |
| 2  | LEAVE_NETWORK | Unsuccessful join to the LoRaWAN network |
| 5  | SYSTEM_WAKEUP | System wakeup                            |
| 6  | RESTART       | System restart                           |

1. **STARTUP Event** - Appears after system initialization.
    * **Message format**:

```sh
EVENT:0:STARTUP
No additional information.
```

2. **JOIN_NETWORK Event** - LoRaWAN network activation successful. It appears after OTAA join successful.
    * **Message format**:

```sh
EVENT:1:JOIN_NETWORK
No additional information.
```

3. **LORA_LEAVE_NETWORK Event** - In OTAA activation mode, if eight consecutive uplink confirmed packets do not receive a response, the LORA_LEAVE_NETWORK event will be triggered. After the LORA_LEAVE_NETWORK event is triggered, the module will stop sending LoRaWAN message and start OTAA activation again.
    * **Message format**:

```sh
EVENT:2:LEAVE_NETWORK
No additional information.
```

4. **SYSTEM_WAKEUP Event** - A module in a low-power state can be awaken by receiving input from the AT command line interface. After wakeup, the module will no longer enter low-power mode. If you want the module to enter low power mode again, use the command: `AT+SLEEP\r\n`
    * **Message format**:

```sh
EVENT:5:SYSTEM_WAKEUP
```

5.	**RESTART Event** - Triggered before the module restarts.
    * **Message format**:

```sh
EVENT:6:RESTART
```

6. **Low Power Operation and Wakeup** -The module supports low power mode. When the device is working in Class A, it automatically enters into low power operation mode. The module can be woken up at any time, when one of the following events occurs:
    * **Wakeup on system interrupt** - When module needs to perform tasks such as sending/receiving, it will wake up automatically. Automatically returns to low power mode after the task is completed.
    * **Wakeup via the AT command-line interface** - Any instruction sent through the AT command line interface can wake up the module. After wakeup, the SYSTEM_WAKEUP event is triggered, and the low power mode is no longer entered so that the user can use the AT command line to modify the module configuration info. If you want the module to enter low power mode again, use the command: `AT+SLEEP\r\n`

##	LoRaWAN FPort Definition

### Uplink Message FPort Definition

| FPort     | Message Type                                                    | Note                                       |
| --------- | --------------------------------------------------------------- | ------------------------------------------ |
| 1 ~ 128   | RS485/232 Scheduled task/poll uplink message                    | Fport is consistent scheduled task/poll ID |
| 129       | Non-transparent mode, reply of remote instruction message                                                   ||
| 130       | In transparent transmission mode, RS485/232 data upload message                                             ||
| 131 ~ 223 | Reserved                                                        | not used                                   |

### Downlink Message FPort Definition

| FPort     | Message Type                                                           | Note                                             |
| --------- | ---------------------------------------------------------------------- | ------------------------------------------------ |
| 1 ~ 128   | Reserved                                                               | not used                                         |
| 129       | Non-transparent mode, remote instruction                                                                                 ||
| 130       | RS485/232 downlink data sent remotely in transparent transmission mode                                                   ||
| 131 ~ 119 | Reserved                                                               | not used                                         |
| 200       | Remote restart command                                                                                                   ||
| 201       | Remote on/off ADR command                                                                                                ||
| 202       | Remote set working rate command                                        | Valid when ADR is closed                         |
| 203       | Remote set transmit power command                                      | Valid when ADR is closed                         |
| 204       | Remote on/off message acknowledgment                                                                                     ||
| 205       | Remote settings retransmission at this time                            | Valid when the confirmed message mechanism is on |

## Appendix I: Data Rate of Each Region

### EU433/RU864/EU868/AS923

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

### CN470/KR920

| Data Rate | Configuration             | Indicative Physical Bit Rate [bit/s] |
| --------- | ------------------------- | ------------------------------------ |
| 0         | LoRa: SF12 / 125 kHz | 250                                  |
| 1         | LoRa: SF11 / 125 kHz | 440                                  |
| 2         | LoRa: SF10 / 125 kHz | 980                                  |
| 3         | LoRa: SF9 / 125 kHz  | 1760                                 |
| 4         | LoRa: SF8 / 125 kHz  | 3125                                 |
| 5         | LoRa: SF7 / 125 kHz  | 5470                                 |
| 6 ~ 15    | RFU                       |                                      |

### US915

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

### AU915

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

### IN865

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

## Appendix II: Modbus Data Encapsulation Protocol

This section describes the definition of the Modbus message encapsulation format.

| Message Command | Message Sequence Number | Data Length | Data  |
| --------------- | ----------------------- | ----------- | ----- |
| DTU_CMD         | MSER                    | MDATA_LEN   | MDATA |
| 1Byte           | 2Byte                   | 2Byte       | nByte |

* **DTU_CMD**: Message Command (Chapter 9.1)
* **MSER**: Message Sequence Number
* **DTU report message actively** - DTU incremental cycle count.
* **Platform query message** - consistent with the sequence number of the message issued by the platform.

### Message Command DTU_CMD Definition

| Data Bits | BIT7 | BIT6 | BIT5 | BIT4 | BIT3 | BIT2 | BIT1 | BIT0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Definition | DIR | STATUS | RESERVED | Message TYPE | Message TYPE | Message TYPE | Message TYPE | Message TYPE |
| Description | 0: Downlink 1: Uplink | 0: Success 1: Fail | 0: Reserved | 0x00: Reserved 0x01: Scheduled polling task data 0x02: Transparent instruction / data 0x03: Add scheduled polling task list 0x04: Remove scheduled polling task list 0x05: Read scheduled polling task list 0x06: Read LoRa configuration 0x07: Set LoRa configuration 0x08: Read DTU configuration 0x09: Set DTU configuration 0x1D: Initialize LoRa configuration 0x1E: Initialize DTU configuration 0x1F: System restart | 0x00: Reserved 0x01: Scheduled polling task data 0x02: Transparent instruction / data 0x03: Add scheduled polling task list 0x04: Remove scheduled polling task list 0x05: Read scheduled polling task list 0x06: Read LoRa configuration 0x07: Set LoRa configuration 0x08: Read DTU configuration 0x09: Set DTU configuration 0x1D: Initialize LoRa configuration 0x1E: Initialize DTU configuration 0x1F: System restart | 0x00: Reserved 0x01: Scheduled polling task data 0x02: Transparent instruction / data 0x03: Add scheduled polling task list 0x04: Remove scheduled polling task list 0x05: Read scheduled polling task list 0x06: Read LoRa configuration 0x07: Set LoRa configuration 0x08: Read DTU configuration 0x09: Set DTU configuration 0x1D: Initialize LoRa configuration 0x1E: Initialize DTU configuration 0x1F: System restart | 0x00: Reserved 0x01: Scheduled polling task data 0x02: Transparent instruction / data 0x03: Add scheduled polling task list 0x04: Remove scheduled polling task list 0x05: Read scheduled polling task list 0x06: Read LoRa configuration 0x07: Set LoRa configuration 0x08: Read DTU configuration 0x09: Set DTU configuration 0x1D: Initialize LoRa configuration 0x1E: Initialize DTU configuration 0x1F: System restart | 0x00: Reserved 0x01: Scheduled polling task data 0x02: Transparent instruction / data 0x03: Add scheduled polling task list 0x04: Remove scheduled polling task list 0x05: Read scheduled polling task list 0x06: Read LoRa configuration 0x07: Set LoRa configuration 0x08: Read DTU configuration 0x09: Set DTU configuration 0x1D: Initialize LoRa configuration 0x1E: Initialize DTU configuration 0x1F: System restart |

:::tip NOTE
* **Bit7 direction**: The message sent by the platform to DTU is a downlink message. This is 0. The message sent by DTU to the platform is an uplink message. This is 1.
* **Bit6 status**: The result of DTU executing instruction/task - 0 for success and 1 for failure.
:::

### Message Type Definition

1.	**Data for Scheduled Polling Task**

The scheduled polling task list is responsible for sending the read data when the scheduled task list is executed by the platform. This message needs to be sent whether the execution is successful or not. When the execution fails, the status flag position in the DTU_CMD command is 1, and the data length is 0. When the execution is successful, the status flag position is 0 in the DTU_CMD command.

* Execution success message format:

| DTU_CMD | MSER | MDATA_LEN | MDATA |  |
| --- | --- | --- | --- | --- |
| 0x81 | 2Byte | 2Byte | TASK_ID | DATA |
| 0x81 | 2Byte | 2Byte | 1Byte | nByte |

* Execution failure message format:

| DTU_CMD | MSER | MDATA_LEN | MDATA |  |
| --- | --- | --- | --- | --- |
| 0xC1 | 2Byte | 2Byte | TASK_ID | ERROR_CODE |
| 0xC1 | 2Byte | 2Byte | 1Byte | 1Byte |

:::tip NOTE
* **TASK_ID**: Task list ID.
* **DATA**: Data. When the scheduled task list fails to execute, the data length is 0.
:::

2. **Transparent Instruction / Data Message**

The transparent transmission instructions and the execution results of the instructions issued by the platform are transmitted through this message.

This message needs to be sent whether or not the instruction is executed successfully. When the execution fails, the STATUS bit position in the DTU_CMD command is 1, and the data length is 0. When the execution is successful, the STATUS flag position in the DTU_CMD command is 0.

* Format of downlink instruction message:

| DTU_CMD | MSER | MDATA_LEN | MDATA |
| --- | --- | --- | --- |
| 0x02 | 2Byte | 2Byte | DATA |
| 0x02 | 2Byte | 2Byte | nByte |

* Uplink data message format when execution successful:

| DTU_CMD | MSER | MDATA_LEN | MDATA |
| --- | --- | --- | --- |
| 0x82 | 2Byte | 2Byte | DATA |
| 0x82 | 2Byte | 2Byte | nByte |

* Uplink data message format when execution failed:

| DTU_CMD | MSER | MDATA_LEN | MDATA |
| --- | --- | --- | --- |
| 0xC2 | 2Byte | 2Byte | ERROR_CODE |
| 0xC2 | 2Byte | 2Byte | 1Byte |

:::tip NOTE
* **DATA**: Instruction content / data
* **ERROR_CODE**: Error code
:::

3. **Add Scheduled Polling Task List message**

DTU timing task list and execution result are added to the platform and transmitted through this message

This message needs to be sent to the platform whether or not the scheduled task list is added successfully. When the execution fails, the STATUS bit position in the DTU_CMD command is 1, and the data length is 0. When the execution is successful, the STATUS flag position in the DTU_CMD command is 0.

* Format of downlink instruction message:

| DTU_CMD | MSER | MDATA_LEN | MDATA |  |
| --- | --- | --- | --- | --- |
| 0x03 | 2Byte | 2Byte | TASK_ID | DATA |
| 0x03 | 2Byte | 2Byte | 1Byte | nByte |

* Uplink data message format when execution successful:

| DTU_CMD | MSER | MDATA_LEN | MDATA |
| --- | --- | --- | --- |
| 0x83 | 2Byte | 2Byte | TASK_ID |
| 0x83 | 2Byte | 2Byte | 1Byte |

* Uplink data message format when execution failed:

| DTU_CMD | MSER | MDATA_LEN | MDATA |  |
| --- | --- | --- | --- | --- |
| 0xC3 | 2Byte | 2Byte | TASK_ID | ERROR_CODE |
| 0xC3 | 2Byte | 2Byte | 1Byte | 1Byte |

:::tip NOTE
* **TASK_ID**: Task list id
* **DATA**: Task list content
* **ERROR_CODE**: Error code
:::

4. **Remove Polling Task List**

The platform removes the DTU timing task list and the execution results are transmitted through this message.

The message needs to be sent to the platform whether or not the scheduled task list is successfully removed. When the execution fails, the STATUS bit position in the DTU_CMD command is 1, and the data length is 0. When the execution is successful, the STATUS flag position in the DTU_CMD command is 0.

:::tip NOTE
If the specified task list ID is not found in the DTU, it will be regarded as successful execution.
:::

* Format of downlink instruction message:

| DTU_CMD | MSER | MDATA_LEN | MDATA |
| --- | --- | --- | --- |
| 0x04 | 2Byte | 2Byte | TASK_ID |
| 0x04 | 2Byte | 2Byte | 1Byte |

* Message format when execution successful:

| DTU_CMD | MSER | MDATA_LEN | MDATA |
| --- | --- | --- | --- |
| 0x84 | 2Byte | 2Byte | TASK_ID |
| 0x84 | 2Byte | 2Byte | 1Byte |

* Message format when execution failed:

| DTU_CMD | MSER | MDATA_LEN | MDATA |  |
| --- | --- | --- | --- | --- |
| 0xC4 | 2Byte | 2Byte | TASK_ID | ERROR_CODE |
| 0xC4 | 2Byte | 2Byte | 1Byte | 1Byte |

:::tip NOTE
* **TASK_ID**: Task list id
* **ERROR_CODE**: Error code
:::

5. **Read the Polling Task List**

The platform reads the DTU timing task list and transmits the execution result through this message.

The message needs to be sent to the platform whether or not the scheduled task list is read successfully. When the execution fails, the STATUS bit position in the DTU_CMD command is 1, and the data length is 0. When the execution is successful, the STATUS flag position in the DTU_CMD command is 0.

* Format of downlink instruction message:

| DTU_CMD | MSER | MDATA_LEN | MDATA |
| --- | --- | --- | --- |
| 0x05 | 2Byte | 2Byte | TASK_ID |
| 0x05 | 2Byte | 2Byte | 1Byte |

* Uplink data message format when execution successful:

| DTU_CMD | MSER | MDATA_LEN | MDATA |  |
| --- | --- | --- | --- | --- |
| 0x85 | 2Byte | 2Byte | TASK_ID | DATA |
| 0x85 | 2Byte | 2Byte | 1Byte | nByte |

* Uplink data message format when execution failed:

| DTU_CMD | MSER | MDATA_LEN | MDATA |  |
| --- | --- | --- | --- | --- |
| 0xC5 | 2Byte | 2Byte | TASK_ID | ERROR_CODE |
| 0xC5 | 2Byte | 2Byte | 1Byte | 1Byte |

:::tip NOTE
* **TASK_ID**: Task list id
* **DATA**: Task list content
* **ERROR_CODE**: Error code
:::

6. **Add Scheduled Task Message**

The platform adds DTU scheduled task message and transmits the result through this message.

This message needs to be sent to the platform no matter whether the scheduled task is added successfully or not. When the execution fails, the STATUS bit position in the DTU_CMD command is 1, and the data length is 0. When the execution is successful, the STATUS flag position in the DTU_CMD command is 0.

* The format of the downlink instruction message:

| DTU_CMD | MSER | MDATA_LEN | MDATA |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0x0A | 2Byte | 2Byte | TASK_ID | SCH_TYPE | W | H | M | S | DATA |
| 0x0A | 2Byte | 2Byte | 1Byte | nByte | 1Byte | 1Byte | 1Byte | 1Byte | nByte |

* Uplink data message when execution successful:

| DTU_CMD | MSER | MDATA_LEN | MDATA |
| --- | --- | --- | --- |
| 0x8A | 2Byte | 2Byte | TASK_ID |
| 0x8A | 2Byte | 2Byte | 1Byte |

* Uplink data message when execution failed:

| DTU_CMD | MSER | MDATA_LEN | MDATA |  |
| --- | --- | --- | --- | --- |
| 0xCA | 2Byte | 2Byte | TASK_ID | ERROR_CODE |
| 0xCA | 2Byte | 2Byte | 1Byte | 1Byte |

:::tip NOTE
* **TASK_ID**：Task ID
* **SCH_TYPE**: Type of scheduled task
    * 0x00 execute once per hour
    * 0x01 execute once per day
    * 0x02 execute once per week
* **W**: Which day of this week; 0 For Sunday, 1 ~ 6 For Monday ~ Saturday
* **H**: Hour
* **M**: Minute
* **S**: Second
* **DATA**：The data of the task
* **ERROR_CODE**: error code
:::

7. **Remove Scheduled Task Message**

The platform removes DTU scheduled task message and transmits the result through this message.

This message needs to be sent to the platform no matter whether the scheduled task is removed successfully or not. When the execution fails, the STATUS bit position in the DTU_CMD command is 1, and the data length is 0. When the execution is successful, the STATUS flag position in the DTU_CMD command is 0.

:::tip NOTE
When the specified task list ID is not found in DTU, it is considered that the execution is successful.
:::

* The format of the downlink instruction message:

| DTU_CMD | MSER | MDATA_LEN | MDATA |
| --- | --- | --- | --- |
| 0x0B | 2Byte | 2Byte | TASK_ID |
| 0x0B | 2Byte | 2Byte | 1Byte |

* Uplink data message when execution successful:

| DTU_CMD | MSER | MDATA_LEN | MDATA |
| --- | --- | --- | --- |
| 0x8B | 2Byte | 2Byte | TASK_ID |
| 0x8B | 2Byte | 2Byte | 1Byte |

* Uplink data message when execution failed:

| DTU_CMD | MSER | MDATA_LEN | MDATA |  |
| --- | --- | --- | --- | --- |
| 0xCB | 2Byte | 2Byte | TASK_ID | ERROR_CODE |
| 0xCB | 2Byte | 2Byte | 1Byte | 1Byte |

:::tip NOTE
* **TASK_ID**：Task ID
* **ERROR_CODE**: error code
:::

8. **Read Scheduled Task Message**

The platform reads DTU scheduled task message and transmits the result through this message.

This message needs to be sent to the platform no matter whether the scheduled task is read successfully or not. When the execution fails, the STATUS bit position in the DTU_CMD command is 1, and the data length is 0. When the execution is successful, the STATUS flag position in the DTU_CMD command is 0.

* The format of the downlink instruction message:

| DTU_CMD | MSER | MDATA_LEN | MDATA |
| --- | --- | --- | --- |
| 0x0C | 2Byte | 2Byte | TASK_ID |
| 0x0C | 2Byte | 2Byte | 1Byte |

* Uplink data message when execution successful:

| DTU_CMD | MSER | MDATA_LEN | MDATA |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0x8C | 2Byte | 2Byte | TASK_ID | SCH_TYPE | W | H | M | S | DATA |
| 0x8C | 2Byte | 2Byte | 1Byte | 1Byte | 1Byte | 1Byte | 1Byte | 1Byte | nByte |

* Uplink data message when execution failed:

| DTU_CMD | MSER | MDATA_LEN | MDATA |  |
| --- | --- | --- | --- | --- |
| 0xCC | 2Byte | 2Byte | TASK_ID | ERROR_CODE |
| 0xCC | 2Byte | 2Byte | 1Byte | 1Byte |

:::tip NOTE
* **TASK_ID**：task ID
* **SCH_TYPE**: type of scheduled task
	* 0x00 execute once per hour
	*	0x01 execute once per day
  *  0x02 execute once per week
* **W**: which day of this week; 0 For Sunday, 1 ~ 6 For Monday ~ Saturday
* **H**: Hour
* **M**: Minute
* **S**: Second
* **DATA**：The data of the task
:::

9. **Read LoRa Configuration**

The platform reads the LoRa configuration and transmits the result through this message. Platform read message fdata is empty.

This message needs to be sent to the platform whether the LoRa configuration is read successfully or not. When the execution fails, the STATUS bit position in the DTU_CMD command is 1, and the data length is 0. When the execution is successful, the STATUS flag position in the DTU_CMD command is 0.

* Format of downlink instruction message:

| DTU_CMD | MSER  | MDATA_LEN | MDATA |
| ------- | ----- | --------- | ----- |
| 0x06    | 2Byte | 2Byte     | 0Byte |

* Uplink data message format when execution successful:

| DTU_CMD | MSER | MDATA_LEN | MDATA |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0x86 | 2Byte | 2Byte | DATARATE | TXPWR | CONFIRM | RETRY | ADR | DUTY CYCLE |
| 0x86 | 2Byte | 2Byte | 1Byte | 1Byte | 1Byte | 1Byte | 1Byte | 1Byte |

* Uplink data message format when execution failed:

| DTU_CMD | MSER | MDATA_LEN | MDATA |
| --- | --- | --- | --- |
| 0xC6 | 2Byte | 2Byte | ERROR_CODE |
| 0xC6 | 2Byte | 2Byte | 1Byte |

:::tip NOTE
* **DATARATE**: Rate (0 – 5)
* **TXPOWER**: Transmit power (0 - 20)
* **CONFIRM**: Whether to turn on ack. 0 - off, 1 - on
* **RETRY**: Maximum retransmission times when ACK is on (0 ~ 15)
* **ADR**: Whether to turn on dynamic rate adjustment (ADR) 0 - off, 1 - on
* **DUTYCYCLE**: Is the duty cycle limit on 0 - off, 1 – on
:::

10. **Set LoRa Configuration**

The platform reads the configuration and transmits the result through this message. Platform read message fdata is empty.

This message needs to be sent to the platform whether the LoRa configuration is read successfully or not. When the execution fails, the STATUS bit position in the DTU_CMD command is 1, and the data length is 0. When the execution is successful, the STATUS flag position in the DTU_CMD command is 0.

* Format of downlink instruction message:

| DTU_CMD | MSER | MDATA_LEN | MDATA |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0x07 | 2Byte | 2Byte | DATARATE | TXPWR | CONFIRM | RETRY | ADR | DUTY CYCLE |
| 0x07 | 2Byte | 2Byte | 1Byte | 1Byte | 1Byte | 1Byte | 1Byte | 1Byte |

* Uplink data message format when execution successful:

| DTU_CMD | MSER  | MDATA_LEN | MDATA |
| ------- | ----- | --------- | ----- |
| 0x87    | 2Byte | 2Byte     | 0Byte |

* Uplink data message format when execution failed:

| DTU_CMD | MSER | MDATA_LEN | MDATA |
| --- | --- | --- | --- |
| 0xC7 | 2Byte | 2Byte | ERROR_CODE |
| 0xC7 | 2Byte | 2Byte | 1Byte |

:::tip NOTE
* **DATARATE**: Rate (0 – 5)
* **TXPOWER**: Transmit power (0 - 20)
* **CONFIRM**: Whether to turn on ACK, 0 - off, 1 - on
* **RETRY**: Maximum retransmission times when ACK is on (0 ~ 15)
* **ADR_ENABLE**: Whether to turn on dynamic rate adjustment (ADR) 0 - off, 1 - on
* **DUTYCYCLE_ENABLE**: Is the duty cycle limit on 0-off, 1-on
:::

11. **Read DTU Configuration**

The DTU configuration and results read by the platform are transmitted through this message. Platform read message fdata is empty.

This message needs to be sent to the platform whether the DTU configuration is read successfully or not. When the execution fails, the STATUS bit position in the DTU_CMD command is 1, and the data length is 0. When the execution is successful, the STATUS flag position in the DTU_CMD command is 0.

* Format of downlink instruction message:

| DTU_CMD | MSER  | MDATA_LEN | MDATA |
| ------- | ----- | --------- | ----- |
| 0x08    | 2Byte | 2Byte     | 0Byte |

* Uplink data message format when execution successful:

| DTU_CMD | MSER | MDATA_LEN | MDATA |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0x88 | 2Byte | 2Byte | POLL ENABLE | POLL PERIOD | BUS TIMEOUT | RETRY | RS485 |
| 0x88 | 2Byte | 2Byte | 1Byte | 1Byte | 1Byte | 1Byte | 1Byte |

* Uplink data message format when execution failed:

| DTU_CMD | MSER | MDATA_LEN | MDATA |
| --- | --- | --- | --- |
| 0xC8 | 2Byte | 2Byte | ERROR_CODE |
| 0xC8 | 2Byte | 2Byte | 1Byte |

:::tip NOTE
* **POLL ENABLE**: Enables scheduled polling, 0 - off, 1 - on
* **POLL PERIOD**: Polling period, in seconds
* **BUS TIMEOUT**: Bus timeout. The unit is seconds.
* **RETRY**: Number of retries after bus timeout. 0 - turn off retry function
* **RS485**: 485 bus parameters
:::

| Definition | BIT7 | BIT6 | BIT5 | BIT4 | BIT3 | BIT2 | BIT1 | BIT0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Details | 0: 2400 1: 4800 2: 9600 3: 14400 4: 19200 5: 38400 6: 57600 7: 115200 | 0: 2400 1: 4800 2: 9600 3: 14400 4: 19200 5: 38400 6: 57600 7: 115200 | 0: 2400 1: 4800 2: 9600 3: 14400 4: 19200 5: 38400 6: 57600 7: 115200 | 0: 8bit 1: 9bit | 0: 1bit 1: 1.5bit 2: 2bit | 0: 1bit 1: 1.5bit 2: 2bit | 0: NONE 1: EVEN 2: ODD | 0: NONE 1: EVEN 2: ODD |

12. **Set DTU Configuration**

DTU configuration and results of platform settings are transmitted through this message. Set the result message fdata to null.

This message needs to be sent to the platform whether the DTU configuration is read successfully or not. When the execution fails, the STATUS bit position in the DTU_CMD command is 1, and the data length is 0. When the execution is successful, the STATUS flag position in the DTU_CMD command is 0.

* Format of downlink instruction message:

| DTU_CMD | MSER | MDATA_LEN | MDATA |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0x09 | 2Byte | 2Byte | POLL ENABLE | POLL PERIOD | BUS TIMEOUT | RETRY | RS485 |
| 0x09 | 2Byte | 2Byte | 1Byte | 1Byte | 1Byte | 1Byte | 1Byte |

* Uplink data message format when execution successful:

| DTU_CMD | MSER  | MDATA_LEN | MDATA |
| ------- | ----- | --------- | ----- |
| 0x89    | 2Byte | 2Byte     | 0Byte |

* Uplink data message format when execution failed:

| DTU_CMD | MSER | MDATA_LEN | MDATA |
| --- | --- | --- | --- |
| 0xC9 | 2Byte | 2Byte | ERROR_CODE |
| 0xC9 | 2Byte | 2Byte | 1Byte |

:::tip NOTE
* **POLL ENABLE**: Enables scheduled polling, 0 - off, 1 - on
* **POLL PERIOD**: Polling period, in seconds
* **BUS TIMEOUT**: Bus timeout. The unit is seconds.
* **RETRY**: Number of retries after bus timeout. 0 - turn off retry function
* **RS485**: 485 bus parameters
:::

| Definition | BIT7 | BIT6 | BIT5 | BIT4 | BIT3 | BIT2 | BIT1 | BIT0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Details | 0: 2400 1: 4800 2: 9600 3: 14400 4: 19200 5: 38400 6: 57600 7: 115200 | 0: 2400 1: 4800 2: 9600 3: 14400 4: 19200 5: 38400 6: 57600 7: 115200 | 0: 2400 1: 4800 2: 9600 3: 14400 4: 19200 5: 38400 6: 57600 7: 115200 | 0: 7bit 1: 8bit | 0: 1bit 1: 1.5bit 2: 2bit | 0: 1bit 1: 1.5bit 2: 2bit | 0: NONE 1: EVEN 2: ODD | 0: NONE 1: EVEN 2: ODD |

13. **Initialize LoRa Configuration**

LoRa configuration and results of platform initial call are transmitted through this message. The message fdata is empty.

It needs to be sent to the platform whether the DTU configuration is read successfully or not. When the execution fails, the STATUS bit position in the DTU_CMD command is 1, and the data length is 0. When the execution is successful, the STATUS flag position in the DTU_CMD command is 0.

* Format of downlink instruction message:

| DTU_CMD | MSER  | MDATA_LEN | MDATA |
| ------- | ----- | --------- | ----- |
| 0x1D    | 2Byte | 2Byte     | 0Byte |

* Uplink data message format when execution successful:

| DTU_CMD | MSER  | MDATA_LEN | MDATA |
| ------- | ----- | --------- | ----- |
| 0x9D    | 2Byte | 2Byte     | 0Byte |

* Uplink data message format when execution failed:

| DTU_CMD | MSER | MDATA_LEN | MDATA |
| --- | --- | --- | --- |
| 0xDD | 2Byte | 2Byte | ERROR_CODE |
| 0xDD | 2Byte | 2Byte | 1Byte |

* The initial value of LoRa configuration:

| DATARATE | 0 – DR_0 |
| --- | --- |
| TXPOWER | 19 – 19dBm |
| CONFIRM | 1 – open |
| RETRY | 3 – retransmission 3 times |
| ADR_ENABLE | 1 – open |
| DUTYCYCLE_ENABLE | 0 – close |

14. **Initialize DTU Configuration**

LoRa configuration and results of platform initial call are transmitted through this message. The message data is empty.

It needs to be sent to the platform whether the DTU configuration is read successfully or not. When the execution fails, the STATUS bit position in the DTU_CMD command is 1, and the data length is 0. When the execution is successful, the STATUS flag position in the DTU_CMD command is 0.

* Format of downlink instruction message:

| DTU_CMD | MSER  | MDATA_LEN | MDATA |
| ------- | ----- | --------- | ----- |
| 0x1E    | 2Byte | 2Byte     | 0Byte |

* Uplink data message format when execution successful:

| DTU_CMD | MSER  | MDATA_LEN | MDATA |
| ------- | ----- | --------- | ----- |
| 0x9E    | 2Byte | 2Byte     | 0Byte |

* Uplink data message format when execution failed:

| DTU_CMD | MSER | MDATA_LEN | MDATA |
| --- | --- | --- | --- |
| 0xDE | 2Byte | 2Byte | ERROR_CODE |
| 0xDE | 2Byte | 2Byte | 1Byte |

* The initial value of DTU:

| POLL_ENABLE | 1 (opened） | 1 (opened） |
| --- | --- | --- |
| POLL_PERIOD | 3600（seconds） | 3600（seconds） |
| BUS TIMEOUT | 1000（milliseconds） | 1000（milliseconds） |
| RS485 | 0xE0 | Baud rate: 115200 Data bits: 8 Stop bit: 1 Check code: NONE |

