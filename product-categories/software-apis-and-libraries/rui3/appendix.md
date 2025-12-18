

# Appendix

## Data Rate by Region

**EU868/EU433/AS923**

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

## TX Power by Region

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
However, the module's max TX power is only up to 22 dBm. 

| TXPower | Configuration (Conducted Power) |
| ------- | ------------------------------- |
| 0       | MaxEIRP                         |
| 1       | MaxEIRP - 2 dB             |
| 2       | MaxEIRP - 4 dB             |
| 3 ~ 9   | -                               |
| 10      | 10 dBm                     |
| 11 ~ 15 | RFU                             |

**AU915**

By default, MaxEIRP is considered to be +30 dBm based on LoRa Alliance specification.
However, the module's max TX power is only up to 22 dBm. 

| TXPower | Configuration (EIRP) |
| ------- | -------------------- |
| 0       | MaxEIRP              |
| 1 ~ 10  | MaxEIRP - 2*TXPower  |
| 11 ~ 15 | RFU                  |

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

By default, Max EIRP is considered to be 16 dBm.

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
However, the module's max TX power is only up to 22 dBm. 

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

## Maximum Transmission Load by Region

:::tip NOTE
The LoRaWAN stack adds 8 bytes to the user payload. In the following list, M is the maximum payload size and N is the maximum usable payload size for the user data without the MAC header.
:::

**EU868**

| DataRate | M           | N           |
| -------- | ----------- | ----------- |
| 0        | 59          | 51          |
| 1        | 59          | 51          |
| 2        | 59          | 51          |
| 3        | 123         | 115         |
| 4        | 250         | 242         |
| 5        | 250         | 242         |
| 6        | 250         | 242         |
| 7        | 250         | 242         |
| 8 ~ 15   | Not Defined | Not Defined |

**US915**

| DataRate | M           | N           |
| -------- | ----------- | ----------- |
| 0        | 19          | 11          |
| 1        | 61          | 53          |
| 2        | 133         | 125         |
| 3        | 250         | 242         |
| 4        | 250         | 242         |
| 5 ~ 7    | Not Defined | Not Defined |
| 8        | 61          | 53          |
| 9        | 137         | 129         |
| 10       | 250         | 242         |
| 11       | 250         | 242         |
| 12       | 250         | 242         |
| 13       | 250         | 242         |
| 14 ~ 15  | Not Defined | Not Defined |

**AU915**

| DataRate | M           | N           |
| -------- | ----------- | ----------- |
| 0        | 59          | 51          |
| 1        | 59          | 51          |
| 2        | 59          | 51          |
| 3        | 123         | 115         |
| 4        | 250         | 242         |
| 5        | 250         | 242         |
| 6        | 250         | 242         |
| 7        | Not Defined | Not Defined |
| 8        | 61          | 53          |
| 9        | 137         | 129         |
| 10       | 250         | 242         |
| 11       | 250         | 242         |
| 12       | 250         | 242         |
| 13       | 250         | 242         |
| 14 ~ 15  | Not Defined | Not Defined |

**KR920**

| DataRate | M           | N           |
| -------- | ----------- | ----------- |
| 0        | 59          | 51          |
| 1        | 59          | 51          |
| 2        | 59          | 51          |
| 3        | 123         | 115         |
| 4        | 250         | 242         |
| 5        | 250         | 242         |
| 6 ~ 15   | Not Defined | Not Defined |

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
| 8 ~ 15 | RFU | RFU | RFU | RFU |

**IN865**

| DataRate | M           | N           |
| -------- | ----------- | ----------- |
| 0        | 59          | 51          |
| 1        | 59          | 51          |
| 2        | 59          | 51          |
| 3        | 123         | 115         |
| 4        | 250         | 242         |
| 5        | 250         | 242         |
| 6        | 250         | 242         |
| 7        | 250         | 242         |
| 8 ~ 15   | Not Defined | Not Defined |

**CN470**

| DataRate | M           | N           |
| -------- | ----------- | ----------- |
| 0        | 59          | 51          |
| 1        | 59          | 51          |
| 2        | 59          | 51          |
| 3        | 123         | 115         |
| 4        | 250         | 242         |
| 5        | 250         | 242         |
| 6 ~ 15   | Not Defined | Not Defined |

**EU433**

| DataRate | M           | N           |
| -------- | ----------- | ----------- |
| 0        | 59          | 51          |
| 1        | 59          | 51          |
| 2        | 59          | 51          |
| 3        | 123         | 115         |
| 4        | 250         | 242         |
| 5        | 250         | 242         |
| 6        | 250         | 242         |
| 7        | 250         | 242         |
| 8 ~ 15   | Not Defined | Not Defined |

