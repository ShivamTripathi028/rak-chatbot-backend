---
slug: /product-categories/wisnode/rak7432-rak7434/at-command-manual/
title: RAK7432/RAK7434 WisNode Bridge Analog AT Command Manual
description: For an easier experience with your LoRaWAN Module, a comprehensive list of commands for the LoRa P2P and LoRaWAN communication is provided. A serial communication interface is also presented for the two-way communication of the RAK7432/RAK7434.
image: "https://images.docs.rakwireless.com/wisnode/rak7432-RAK7432/rak7432-RAK7432.png"
keywords:
  - RAK7432
  - RAK7434
  - AT Command Manual
  - wisnode
sidebar_label: AT Command Manual
---

# RAK7432/RAK7434 AT Command Manual

## Overview

This document applies to Analog to LoRaWAN Bridge products. The supported product models include RAK7432/RAK7434.

### AT Command Syntax

The AT command must start with `AT` or `at` and ends with `<CR> <LF>`.

AT commands can be divided into:
   - **Read commands** - read the configuration or status of the device, which is in the format of `AT+<x>`
   - **Write commands** - write/modify the device configuration, which is in the format of `AT+<x>=<m>:<n>`
   The command name and parameters are separated by "**=**". If there are multiple parameters, the parameters are separated by "**:**".
   - **Test commands** - is the test command executable, which is in the format of `AT+<x>=?`

The response format of the command is usually:

| Condition                        | Response                                    |
| -------------------------------- | ------------------------------------------- |
| Normal response with information | `<Response><CR><LF>OK<CR><LF>`              |
| Normal response                  | `OK<CR><LF>`                                |
| Response when an error occurs    | `ERROR <Error code>:<Error packet><CR><LF>` |

:::tip NOTE
AT commands are not case-sensitive.
:::

### USB Configuration Interface

The devices are equipped with a standard USB interface for configuring via AT commands. The serial parameters are as follows:

| Parameter | Value |
| --- | --- |
| Baud rate | 115200 |
| Data bit | 8 |
| Stop bit | 1 |
| Vrification | No |

### Common Errors

| Error Code | Description |
| --- | --- |
| ERROR 1 | Unsupported command |
| ERROR 2 | Syntax Error |
| ERROR 3 | Storage failure |
| ERROR 4 | System busy |
| ERROR 5 | Parameter format / number error |
| ERROR 6 | Insufficient resources |
| ERROR 7 | Parameter out of valid range |

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

4.  **AT+PUBLIC**

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

| Parameter | Information                                              |
| --------- | -------------------------------------------------------- |
| **x**     | **Is the node working with the public LoRaWAN network?** |
| 0         | Not working in Public mode                               |
| 1         | Working in Public mode                                   |

5.  **AT+CLASS**

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

6.  **AT+APPEUI**

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

| Parameter   | Information                                                         |
| ----------- | ------------------------------------------------------------------- |
| **app_eui** | **Application EUI:** Hexadecimal character, 16 bytes in length |

7.  **AT+APPKEY**

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

9.  **AT+APPSKEY**

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

10. **AT+NWKSKEY**

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

12.  **AT+DATARATE**

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
The DataRate value and the default value are related to LoRaWAN regional parameters. Refer to [Appendix: DataRate list of each region](#appendix-data-rate-of-each-region) in this document.
:::

13. **AT+CONFIRM**

Turn on/off the LoRaWAN packet confirmation mechanic, which is set to be “on” by default. The modification will take effect immediately.

When the confirm function is enabled, the packets sent by the device will require the LoRa network server to send an ACK response. Unless a confirmation is received the device will resend the packet. For more information on the resending mechanic refer to **14. AT+RETRY**.

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

| Parameter | Information                                                                    |
| --------- | ------------------------------------------------------------------------------ |
| **N**     | PingSlot Number in Beacon Period:
1
2
4
8
16
32
64
128 |

21. **AT+LPTP**

LoRa Private Transport Protocol (LPTP) is a RAK proprietary message splitting protocol, which can send data with a length exceeding the maximum permissible size, using multiple messages. As it is proprietary it only works with the RAK LoRa networks server built into our commercial gateways. It is “Off” by default. The modification will take effect immediately.

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

## Data Acquisition Setting Commands

1.  **AT+AINPERIOD**

The command is used to read or modify the analog data acquisition reporting period. The value is in seconds and the default value is 600s.

| Operation | AT Command         | Response                                                                                             |
| --------- | ------------------ | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+AINPERIOD`     | `<N>`
`OK`                                                                                        |
| Write     | `AT+AINPERIOD=<N>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+AINPERIOD=?`   | `OK`                                                                                                 |

| Parameter | Information                                         |
| --------- | --------------------------------------------------- |
| **N**     | **Analog acquisition cycle**                        |
| 5 ~ 43200 | The value is in the range of 5 ~ 43200 seconds |

2.  **AT+AINVALUERANGE**

Read or modify the actual values represented by the minimum and maximum values of the analog interface range. The analog data read by the system will be linearly converted and reported over LoRaWAN.

The default values are:

**4-20 mA interface:** 4-20

**0-5 V interface:** 0-5

| Operation | AT Command                               | Response                                                                                             |
| --------- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+AINVALUERANGE`                       | `1:<MIN>:<MAX>`
`2:<MIN>:< MAX>`                                                                  |
| Write     | `AT+AINVALUERANGE=<channel>:<MIN>:<MAX>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+AINVALUERANGE=?`                     | `OK`                                                                                                 |

| Parameter     | Information                                |
| ------------- | ------------------------------------------ |
| **CHANNEL**   | The analog input interface (AIN1=1/AIN2=2) |
| **MIN VALUE** | Allowed range [-300,300]                   |
| **MAX VALUE** | Allowed range [-300,300]                   |

3.  **AT+AINLPMODE**

Set the analog data interface in low-power operation mode. When the low-power operation mode is enabled the power output and the analog data input interface will be turned off while there is no acquisition.

| Operation | AT Command         | Response                                                                                             |
| --------- | ------------------ | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+AINLPMODE`     | `<N>`
`OK`                                                                                        |
| Write     | `AT+AINLPMODE=<N>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+AINLPMODE=?`   | `OK`                                                                                                 |

| Parameter | Information          |
| --------- | -------------------- |
| **N**     | **AINLPMODE status** |
| 0         | disabled             |
| 1         | enabled              |

4.  **AT+AINWARMUP**

When the analog data interface is working in low power consumption mode, the device needs to turn the acquisition circuit and warm up the sensor before data acquisition. The command allows setting the warm-up time. The value is in milliseconds (ms), and the default value is 1000 ms.

| Operation | AT Command         | Response                                                                                             |
| --------- | ------------------ | ---------------------------------------------------------------------------------------------------- |
| Read      | `AT+AINWARMUP`     | `<N>`
`OK`                                                                                        |
| Write     | `AT+AINWARMUP=<N>` | When the modification is successful:
`OK`
When modification fails: 
`ERROR <code>:<packet>` |
| Test      | `AT+AINWARMUP=?`   | `OK`                                                                                                 |

| Parameter | Information |
| --- | --- |
| N | Warm-up time, ms |

5.  **AT+AINREAD**

Read the current analog input interface data.

| Operation | AT Command   | Response      |
| --------- | ------------ | ------------- |
| Read      | `AT+AINREAD` | `<N>`
`OK` |

| Parameter   | Information                 |
| ----------- | --------------------------- |
| **channel** | **Analog input channel ID** |
| 1           | AIN1                        |
| 2           | AIN2                        |

## System-Related Commands

1.  **AT+TIMEZONE**

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

2.  **AT+VERSION**

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

3.  <b>AT+SYSLOGLVL**

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

5.  **AT+RESTART**
Reboot the device.

| Operation | AT Command   | Response |
| --------- | ------------ | -------- |
| Write     | `AT+RESTART` | `Null`   |

6.  **AT+FACTORY**

The command restores the device to the factory settings. This operation will last for about 60 seconds. Do not cut off the power supply of the device before it automatically restarts.

| Operation | AT Command   | Response |
| --------- | ------------ | -------- |
| Write     | `AT+FACTORY` | `Null`   |

7.  **AT+SYSTIME**

Show the real running time.

| Operation | AT Command   | Response         |
| --------- | ------------ | ---------------- |
| Write     | `AT+SYSTIME` | `<time>`
`OK` |

| Parameter | Information                          |
| --------- | ------------------------------------ |
| **time**  | Timestamp in UNIX format, in seconds |

8.  **AT+DATETIME**

Show the synchronized with the LoRaWAN Network Server time. Needs LoRaWAN1.0.3 specification support from the server side.

| Operation | AT Command    | Response             |
| --------- | ------------- | -------------------- |
| Read      | `AT+DATETIME` | `<datetime>`
`OK` |

| Parameter    | Information                        |
| ------------ | ---------------------------------- |
| **datetime** | Date / Time in YYYY/MM/DD hh:mm:ss |

9. **AT+SYSINFO**

This command gives the system information about the device.

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

## Event Notification

When the working state of the module changes, an event notification will be output through the AT command-line interface.
The event notification format is:

```sh
EVENT:[EVENT_ID]:[EVENT_MSG]:<ADDITIONAL_INFO>
```

| Event               | Description                                                                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **EVENT_ID**        | Event ID                                                                                                                                          |
| **EVENT_MSG**       | Event name                                                                                                                                        |
| **ADDITIONAL_INFO** | Additional information - Optional
Some events need to output additional information. Multiple additional information sets are separated by ":" |

The module supports the following event notifications:

| ID  | EVENT_MSG     | Description                              |
| --- | ------------- | ---------------------------------------- |
| 0   | STARTUP       | System startup complete                  |
| 1   | JOIN_NETWORK  | Successful join to the LoRaWAN network   |
| 2   | LEAVE_NETWORK | Unsuccessful join to the LoRaWAN network |
| 5   | SYSTEM_WAKEUP | System wakeup                            |
| 6   | RESTART       | System restart                           |

1. **STARTUP Event** - Appears after system initialization.
    * **Message format**:

```sh
EVENT:0:STARTUP
No additional information.
```

2. **JOIN_NETWORK Event** - LoRaWAN network activation successful. It appears after OTAA joins successfully.
    * **Message format**:

```sh
EVENT:1:JOIN_NETWORK
No additional information.
```

3. **LORA_LEAVE_NETWORK Event** - In OTAA activation mode, if eight consecutive uplink-confirmed packets do not receive a response, the LORA_LEAVE_NETWORK event will be triggered. After the LORA_LEAVE_NETWORK event is triggered, the module will stop sending LoRaWAN messages and start OTAA activation again.
    * **Message format**:

```sh
EVENT:2:LEAVE_NETWORK
No additional information.
```

4. **SYSTEM_WAKEUP Event** - A module in a low-power state can be awakened by receiving input from the AT command line interface. After wakeup, the module will no longer enter low-power mode. If you want the module to enter low power mode again, use the command: `AT+SLEEP\r\n`
    * **Message format**:

```sh
EVENT:5:SYSTEM_WAKEUP
```

5.  **RESTART Event** - Triggered before the module restarts.
    * **Message format**:

```sh
EVENT:6:RESTART
```

## LoRaWAN Data Format Definition

The basic message format is defined as follows:

| Channel ID 1 | Type 1 | Data 1 | Channel ID 2 | Type 2 | Data 2 |
| --- | --- | --- | --- | --- | --- |
| 1Byte | 1Byte | nBytes | 1Byte | 1Byte | nBytes |

The data adopts big-endian byte order, that is, the high byte is in Uplink

### Message Data Format

The channel ID: analog input interface ID, interface AIN1: 0x01, interface AIN2: 0x02

type: fixed value 0x02, indicating analog input data.length of this type of data is 2 bytes of data: the analog input value of this channel\*100. Length 2 bytes, signed integer,

* Parsing example:

0x010401EF02040474

| Channel ID 1 | type 1 | data 1 |
| --- | --- | --- |
| 0x01 | 0x04 | 0x01EF |
| AIN1 | analog input data | 0x01EF=495=>4.95 |

| Channel ID 2 | type 2 | data 2 |
| --- | --- | --- |
| 0x02 | 0x04 | 0x0474 |
| AIN2 | analog input data | 0x0474=1140=>11.4 |

## Appendix: Data Rate of Each Region

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

