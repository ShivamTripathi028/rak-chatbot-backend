---
slug: /product-categories/wisnode/rak2560/payload-decoder/
title: RAK2560 WisNode Sensor Hub Payload Decoder
description: Contains instructions and tutorials for installing and deploying your RAK2560. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: "https://images.docs.rakwireless.com/wisnode/rak2560/rak2560.jpg"
keywords:
    - RAK2560
    - quickstart
    - wisnode
    - sensor hub
sidebar_label: Payload Decoder
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK2560 WisNode Sensor Hub Payload Decoder

## Sensor Hub LoRaWAN Payload and NB IoT JSON Format

###  Sensor Probe

 The RAK1901, RAK1902, RAK1904, and RAK1906 all incorporate multiple sensors integrated into a single sensor IC.

| WisBlock Module | Sensor IC |             Sensor Type             |                                                                        Sensor Data Values                                                                         |
|:---------------:|:---------:|:-----------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|     RAK1901     |   SHTC3   |      Temperature and Humidity       |                                       Temperature (-40°&nbsp;C to +125°&nbsp;C)<br/>Humidity (0&nbsp;to&nbsp;100%&nbsp;RH)                                        |
|     RAK1902     |  KPS22HB  | Temperature and Barometric Pressure |                                      Temperature (-40°&nbsp;C to +85°&nbsp;C)<br/>Pressure (260&nbsp;to&nbsp;1260&nbsp;hPa)                                       |
|     RAK1904     |  LIS3DH   |         3-Axis Acceleration         |                                                                           3-Axis (XYZ)                                                                            |
|     RAK1906     |  BME680   |            Environmental            | Temperature (-40°&nbsp;C to 85°&nbsp;C)<br/>Humidity (0&nbsp;to&nbsp;100%&nbsp;RH)<br/>Pressure (300&nbsp;to&nbsp;1100 hPa)<br/>Gas (0&nbsp;to&nbsp;500&nbsp;IAQ) |

The four (4) WisBlock modules will have four (4) sensor types as follows:

|   Sensor    | Type | Data Size |
|:-----------:|:-----|:---------:|
| Temperature | 0x67 |     2     |
|  Humidity   | 0x68 |     1     |
|  Pressure   | 0x66 |     2     |
|   3-axis    | 0x71 |     6     |

RAK Sensor Type is 1&nbsp;Byte, which uses the IPSO Object ID minus 3200 in the below conversion rule:

```
RAK_DATA_TYPE = IPSO_OBJECT_ID - 3200
```

| Type                   | IPSO ID | RAK Data Type (Decimal) | RAK Data Type (Hex) | Data Size | Data Resolution per Bit          | Sensor Hub NB IoT Json |
|------------------------|---------|-------------------------|---------------------|-----------|----------------------------------|------------------------|
| Temperature sensor     | 3303    | 103                     | 0x67                | 2         | 0.1°&nbsp;C Signed MSB           | "Temperature"          |
| Humidity sensor        | 3304    | 104                     | 0x68                | 1         | 0.1% Unsigned                    | "Humidity"             |
| Accelerometer (3-Axis) | 3313    | 113                     | 0x71                | 6         | 0.001&nbsp;G Signed MSB per axis | "Accelerometer"        |
| Barometer (Pressure)   | 3315    | 115                     | 0x73                | 2         | 0.1&nbsp;hPa Unsigned MSB        | "Barometer"            |

###  Sensor Hub

| Type                   | RAK Data Type (Decimal) | RAK Data Type (Hex) | Data Size | Data Resolution per Bit          | Sensor Hub NB IoT Json |
|------------------------| -------------------------|---------------------|-----------|----------------------------------|------------------------|
| HUB Voltage            | 187                     | 0xBB                | 2         | 0.01&nbsp;V MAX: 655.32          | "HUB_Voltage"          |
| X-Axis Gravity         | 27                      | 0x1B                | 2         | 1&nbsp;mg 2000 ~ -2000           | "X-gravity"            |
| Y-Axis Gravity         | 28                      | 0x1C                | 2         | 1&nbsp;mg 2000 ~ -2000           | "Y-gravity"            |
| Z-Axis Gravity         | 29                      | 0x1D                | 2         | 1&nbsp;mg 2000 ~ -2000           | "Z-gravity"            |

### RAKwireless Standardized Payload Decoder

On [GitHub,](https://github.com/RAKWireless/RAKwireless_Standardized_Payload/blob/main/RAKwireless_Standardized_Payload.js) you can find a standard version of the decoder that works with all solutions.

### Sensor Probe IO

| Type                                                   | IPSO ID | RAK Data Type (Decimal) | RAK Data Type (HEX) | Data Size | Data Resolution per Bit                                   | Sensor Hub NB IoT Json                                                                                     |
|--------------------------------------------------------|---------|-------------------------|---------------------|-----------|-----------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Digital Input                                          | 3200    | 0                       | 0x00                | 1         | (ON/OFF)                                                  | "Digital-Input"                                                                                            |
| Digital  Output                                        | 3201    | 1                       | 0x01                | 1         | (ON /  OFF)                                               | "Digital-Output"                                                                                           |
| Analog  Input                                          | 3202    | 2                       | 0x02                | 2         | 0.01mA(V),  Min: 0.0, MAX: 655.35                         | "Analog-Input"                                                                                             |
| Nitrogen                                               | 3216    | 16                      | 0x10                | 2         | 1mg/Kg,  Min: 0, MAX: 65535                               | "NITROGEN"                                                                                                 |
| Phosphorus                                             | 3217    | 17                      | 0x11                | 2         | 1mg/Kg,  Min: 0, MAX: 65535                               | "PHOSPHORUS"                                                                                               |
| Potassium                                              | 3218    | 18                      | 0x12                | 2         | 1mg/Kg,  Min: 0, MAX: 65535                               | "POTASSIUM"                                                                                                |
| Salinity                                               | 3219    | 19                      | 0x13                | 2         | 1mg/L,  Min: 0, MAX: 65535                                | "SALINITY"                                                                                                 |
| Dissolved  oxygen (DO)                                 | 3220    | 20                      | 0x14                | 2         | 0.01mg/L,  Min: 0.0, MAX: 655.35                          | "Dissolved-Oxygen"                                                                                         |
| Oxidation  Reduction Potential (ORP)                   | 3221    | 21                      | 0x15                | 2         | 0.1mv  sign                                               | "ORP"                                                                                                      |
| Chemical  Oxygen Demand (COD)                          | 3222    | 22                      | 0x16                | 2         | 1mg/L,  Min: 0, MAX: 65535                                | "COD"                                                                                                      |
| Turbidity                                              | 3223    | 23                      | 0x17                | 2         | 1NTU,  Min: 0, MAX: 65535                                 | "Turbidity"                                                                                                |
| NO3                                                    | 3224    | 24                      | 0x18                | 2         | 0.1ppm,  Min: 0.0, MAX: 6553.5                            | "NO3"                                                                                                      |
| NH4+                                                   | 3225    | 25                      | 0x19                | 2         | 0.01ppm,  Min: 0.0, MAX: 655.35                           | "NH4PULS"                                                                                                  |
| Biochemical  oxygen demand (BOD)                       | 3226    | 26                      | 0x1A                | 2         | 1mg/L,  Min: 0, MAX: 65535                                | "BOD"                                                                                                      |
| Illuminance                                            | 3301    | 101                     | 0x65                | 4         | 1Lux,  Min: 0, MAX:4294967295                             | "Illuminance"                                                                                              |
| Presence                                               | 3302    | 102                     | 0x66                | 1         | (Yes/No)                                                  | "Presence"                                                                                                 |
| Temperature                                            | 3303    | 103                     | 0x67                | 2         | 0.1°C, Min: -3276.8, MAX:3276.7                           | "Temperature"                                                                                              |
| Humidity  Sensor     Soil Humidity      SCD30 humidity | 3304    | 104                     | 0x68                | 1         | 1%RH  Unsigned                                            | "Humidity"                                                                                                 |
| Air  Quality Index                                     | 3305    | 105                     | 0x69                | 2         | 1  Unsigned MSB     1, Min: 0, MAX: 65535                 | "GAS"                                                                                                      |
| Humidity                                               | 3312    | 112                     | 0x70                | 2         | 0.1%,  Min: 0.0, MAX:100.0                                | "High-Precise-Humidity"                                                                                    |
| Accelerometer  (3-Axis)                                | 3313    | 113                     | 0x71                | 6         | 0.001 G  Signed MSB per axis                              | "Accelerometer"                                                                                            |
| Pressure                                               | 3315    | 115                     | 0x73                | 2         | 0.1hPa, Min: 0.0, MAX: 6553.5                             | "Barometer"                                                                                                |
| Battery  Level (Battery Voltage)                       | 3316    | 116                     | 0x74                | 2         | 0.01V,  Min: 0.0, MAX: 655.35                             | "BatteryValue"                                                                                             |
| Precipitation                                          | 3317    | 117                     | 0x77                | 2         | 1mm/h,  Min: 0, MAX: 65535                                | "Precipitation"                                                                                            |
| Percentage                                             | 3320    | 120                     | 0x78                | 1         | 1%, Min: 0, Max:100                                       | "Percentage"                                                                                               |
| CO2 concentration                                      | 3325    | 125                     | 0x7D                | 2         | 1ppm,  Min: 0, MAX: 65535                                 | "CO2"                                                                                                      |
| EC                                                     | 3392    | 192                     | 0xC0                | 2         | 0.001mS/cm,  Min: 0.0, Max:65.535                         | "EC"                                                                                                       |
| EC                                                     | 3327    | 127                     | 0x7F                | 4         | 0.001uS/cm,  Min: 0.0, Max:4294967.295                    | "High-Precision-EC"                                                                                        |
| Distance                                               | 3330    | 130                     | 0x82                | 4         | 0.001 m                                                   | "Distance"                                                                                                 |
| RAK Device Serial Number                               |         | 126                     | 0x7E                | 3         | 3 bytes Serial number in MSB "SSN"                        | "Serial Number"                                                                                            |
| VOC                                                    | 3338    | 138                     | 0x8A                | 2         | 1, Min:  0, MAX: 65535                                    | "VOC"                                                                                                      |
| Wind  Speed                                            | 3346    | 146                     | 0x92                | 2         | 0.01m/s,  Min: 0.0, MAX: 655.35                           | "GustWindSpeed"                                                                                            |
| Strikes                                                | 3347    | 147                     | 0x93                | 2         | 1, Min:  0, MAX: 65535                                    | "Strikes"                                                                                                  |
| Capacity                                               | 3384    | 184                     | 0xB8                | 1         | 1%RH,  Min: 0, MAX: 100                                   | "Capacity"                                                                                                 |
| DC  Current                                            | 3385    | 185                     | 0xB9                | 2         | 0.01A,  Min: -327.68, MAX: 327.67                         | "DC_Current"                                                                                               |
| DC  Voltage                                            | 3386    | 186                     | 0xBA                | 2         | 0.01V,  Min: 0.0, MAX: 655.35                             | "DC_Voltage"                                                                                               |
| Moisture                                               | 3388    | 188                     | 0xBC                | 2         | 0.1%,  Min:0.0, Max:100.0                                 | "Moisture"                                                                                                 |
| Wind  Speed                                            | 3390    | 190                     | 0xBE                | 2         | 0.01m/s,  Min: 0.0, MAX: 655.35                           | "Wind-Speed"                                                                                               |
| Wind  Direction (0o -  North)                          | 3391    | 191                     | 0xBF                | 2         | 1o , in 0~359o                                            | "Wind-Direction"                                                                                           |
| pH                                                     | 3393    | 193                     | 0xC1                | 2         | 0.01,  Min: 0.0, MAX: 655.35                              | "High_Precision_PH"                                                                                        |
| Normal  Precision pH                                   | 3394    | 194                     | 0xC2                | 2         | 0.1 pH                                                    | "PH"                                                                                                       |
| Pyranometer                                            | 3395    | 195                     | 0xC3                | 2         | 1  unsigned MSB (W/m2)                                    | "PYRANOMETER"                                                                                              |
| PM10                                                   | 3427    | 227                     | 0xE3                | 2         | 1ug/m3, Min: 0, MAX: 65535                                | "PM10"                                                                                                     |
| PM2.5                                                  | 3428    | 228                     | 0xE4                | 2         | 1ug/m3,  Min: 0, MAX: 65535                               | "PM2.5"                                                                                                    |
| Noise                                                  | 3433    | 233                     | 0xE9                | 2         | 0.1dB,  Min: 0.0, MAX: 6553.5                             | "Noise"                                                                                                    |
| Orientation                                            | 3429    | 229                     | 0xE5                | 2         | 0.1°,  Min: -90.0, MAX: 90.0                              | "ORIENTATION"                                                                                              |
| Raw Data  in Binary (Modbus ADU)                       | 3441    | 241                     | 0xF1                | /         |                                                           | TLV  format binary raw data for Modbus, RS232 or other specific data format "BinaryRaw" (NBIOT Json  Mode) |
| Binary2byte                                            | 3443    | 243                     | 0xF3                | 2         | Modbus  content                                           | "Raw2byte"                                                                                                 |
| Binary4byte                                            | 3424    | 224                     | 0xF4                | 4         | Modbus  content                                           | "Raw4byte"                                                                                                 |
| Generic  Float (IEEE754)                               | 3445    | 245                     | 0xF5                | 4         |                                                           | "Float"                                                                                                    |
| Generic  Integer (32bit)                               | 3446    | 246                     | 0xF6                | 4         | Min:  -2147483648, Max: 2147483647                        | "Int32"                                                                                                    |
| Generic  Unsigned Integer (32bit)                      | 3447    | 247                     | 0xF7                | 4         | Min: 0,  Max: 4294967295                                  | "uInt32"                                                                                                   |
| Raw Data  in Binary                                    | 3448    | 248                     | 0xF8                | /         | TLV  format binary raw data "BinaryTLV" (NBIOT Json Mode) | "BinaryTLV"                                                                                                |

## RK900-09 Weather Station Sample Payload Decoder

<details>
<summary> Click to view the Payload Decoder code </summary>

```js
function Decoder(bytes, port) {  
    var decoded = {};  
    var str = bin2HexStr(bytes);  
    var i = 0;  
    while (i < str.length) {  
        var channelId = parseShort(str.slice(i, i + 4), 16);  
        var value = parseShort(str.slice(i + 4, i + 8), 16);  
        i += 8;  
        switch (channelId) {  
            case 0x01BE:  
                decoded.wind_speed = value / 100;  
                break;  
            case 0x02BF:  
                decoded.wind_direction = value;  
                break;  
            case 0x0367:  
                decoded.temperature = value / 10.0;  
                break;  
            case 0x0470:  
                decoded.humidity = value / 10.0;  
                break;  
            case 0x0573:  
                decoded.pressure = value / 10.0;  
                break;  
            default:  
                break;  
        }  
    }  
  
    try {  
        decoded.lorawan_rssi = (port && port.metadata && port.metadata.rssi) || 0;  
        decoded.lorawan_snr = (port && port.metadata && port.metadata.snr) || 0;  
        decoded.lorawan_datarate = (port && port.metadata && port.metadata.data_rate) || '';  
    } catch (e) {  
        console.log('Failed to read gateway metadata');  
    }  
  
    return decoded;  
}  
  
function bin2HexStr(bytesArr) {  
    var str = '';  
    for (var i = 0; i < bytesArr.length; i++) {  
        var tmp = (bytesArr[i] & 0xff).toString(16);  
        if (tmp.length == 1) {  
            tmp = '0' + tmp;  
        }  
        str += tmp;  
    }  
    return str;  
}  
  
// convert string to short integer  
function parseShort(str, base) {  
    var n = parseInt(str, base);  
    return (n << 16) >> 16;  
}  
  
// convert string to triple bytes integer  
function parseTriple(str, base) {  
    var n = parseInt(str, base);  
    return (n << 8) >> 8;  
}
```
</details>

<b>Data Interpretation</b>

| Sensor Data Unit | ID (Channel) | Type   | Data    |
|------------------|--------------|--------|---------|
| Serial Number    | 1 Byte       | 1 Byte | 3 Bytes |
| Wind Speed       | 1 Byte       | 1 Byte | 2 Bytes |
| Wind Direction   | 1 Byte       | 1 Byte | 2 Bytes |
| Temperature      | 1 Byte       | 1 Byte | 2 Bytes |
| Humidity         | 1 Byte       | 1 Byte | 2 Bytes |
| Air Pressure     | 1 Byte       | 1 Byte | 2 Bytes |

With the defined data, here's how to interpret the payload received data:


### RK900-09 Weather Station Data Sample

Payload (hex) received data: `007E006F07 01BE0000 02BF0000 036700C6 047002E7 05732719`

| Sensor Data Unit | ID (Channel) | Type | Data   |
|------------------|--------------|------|--------|
| Serial Number    | 00           | 7e   | 006f07 |
| Wind Speed       | 01           | be   | 0000   |
| Wind Direction   | 02           | bf   | 0000   |
| Temperature      | 03           | 67   | 00c6   |
| Humidity         | 04           | 70   | 02e7   |
| Air Pressure     | 05           | 73   | 2719   |

Convert the sensor data from hexadecimal to decimal:

- **Serial Number**: `007e`
- **Data**: `006f07`

```
SN: 006f07
```

- **Wind Speed**: `01be`
- **Data**: `0000`

```
0000 (hex) = 0 (dec)
0 x 0.01 (conversion factor) = 0 m/s
```

- **Wind Direction**: `02bf`
- **Data**: `0000`

```
0000 (hex) = 0 (dec)
0 x 1 (conversion factor) = 0°
```

- **Temperature**: `0367`
- **Data**: `00C6`

```
00C6 (hex) = 198 (dec)
198 x 0.1 (conversion factor) = 19.8° C
```

- **Humidity**: `0470`
- **Data**: `02E7`

```
02E7 (hex) = 743 (dec)
743 x 0.1 (conversion factor) = 74.3%RH
```

- **Air Pressure**: `0573`
- **Data**: `2719`  

```
2719 (hex) = 10009 (dec)
10009 x 0.1 (conversion factor) = 1000.9 hPa
```

## RAK9154 Solar Battery Sample Payload Decoder

### RAK IPSO Sensor type definition in JSON

- Filename: ***snsr_type_def.json***

<details>
<summary> Click to view the Payload Decoder code </summary>

```json
{
"7e": {
      "name": "SSN", 
      "resolution" : 1, 
      "length": 3, 
      "unit": "" 
      },
"14": {
      "name": "Dissolved-Oxygen", 
      "resolution" : 0.01, 
      "length": 2, 
      "unit": "mg/L" 
      },
"15": {
      "name": "Oxidation Reduction Potential",
      "resolution" : 0.1, 
      "length": 2, 
      "unit": "mV", 
      "sign": "-1000～+1000mv" 
      },
"67": {
      "name": "Temperature", 
      "resolution" : 0.1, 
      "length": 2, 
      "unit": "°C" 
      },
 
"68": {
      "name": "Humidity", 
      "resolution" : 1, 
      "length": 1, 
      "unit": "%" 
           },
"73": {
      "name": "Barmoeter", 
      "resolution" : 0.1, 
      "length": 2, 
      "unit": "hPA" 
      },
"71": {
      "name": "A", 
      "resolution" : 0.001, 
      "length": 6, 
      "unit": "G" 
      },
"be": {
      "name": "Wind-Speed", 
      "resolution" : 0.01, 
      "length": 2, 
      "unit": "m/s" 
      },
"bf": {
      "name": "Wind-Direction", 
      "resolution" : 1, 
      "length": 2, 
      "unit": "°" 
      },
"65": {
      "name": "Illuminance", 
      "resolution" : 1, 
      "length": 4, 
      "unit": "lux" 
      },
"70": {
      "name": "High-Precise-Humidity", 
      "resolution" : 0.1, 
      "length": 2, 
      "unit": "%" 
         },
"c1": {
      "name": "High_Precision_pH", 
      "resolution" : 0.01, 
      "length": 2, 
      "unit": "pH" 
      },
"c2": {
      "name": "pH",
      "resolution" : 0.1, 
      "length": 2, 
      "unit": "" 
      },
"c3": {
      "name": "Pyranometer", 
      "resolution" : 1, 
      "length": 2, 
      "unit": "W/m2" 
      },
"c0": {
      "name": "EC", 
      "resolution" : 0.001, 
      "length": 2, 
      "unit": "mS/cm" 
      },
"7f": {
      "name": "High-Precision-EC", 
      "resolution" : 0.001, 
      "length": 4, 
      "unit": "us/cm" 
      },
"13": {
      "name": "Salt", 
      "resolution" : 1, 
      "length": 2, 
      "unit": "mg/L" 
      },
"b8": {
      "name": "Capacity", 
      "resolution" : 1, 
      "length": 1, 
      "unit": "%" 
      },
"b9": {
      "name": "Current", 
      "resolution" : 0.01, 
      "length": 2, 
      "unit": "A" 
      },
"ba": {
      "name": "Voltage", 
      "resolution" : 0.01, 
      "length": 2, 
      "unit": "V" 
      },
"10": {
      "name": "Nitrogen", 
      "resolution" : 1, 
      "length": 2, 
      "unit": "mg/kg" 
      },
"11": {
      "name": "phosphorus", 
      "resolution" : 1, 
      "length": 2, 
      "unit": "mg/kg" 
      },
"12": {
      "name": "potassium", 
      "resolution" : 1, 
      "length": 2, 
      "unit": "mg/kg" 
      },
"77": {
      "name": "Dummy", 
      "resolution" : 1, 
      "length": 4, 
      "unit": "qq" 
      },
"7d": {
      "name": "CO2", 
      "resolution" : 1, 
      "length": 2, 
      "unit": "ppm" 
      },
"82": {
      "name": "Distance", 
      "resolution" : 0.001, 
      "length": 2, 
      "unit": "m" 
      },
"e5": {
      "name": "ORIENTATION", 
      "resolution" : 0.1, 
      "length": 2, 
      "unit": "°", 
      "sign": "–90° to 90°" 
      },
"e9": {
      "name": "Noise", 
      "resolution" : 0.1, 
      "length": 2, 
      "unit": "dB" 
      },
"f1": {
      "name": "RS485", 
      "resolution" : 1, 
      "length": 1, 
      "unit": "" 
      },
"f2": {
      "name": "BINARY", 
      "resolution" : 1, 
      "length": 2, 
      "unit": "" 
      },
"02": {
      "name": "AIC", 
      "resolution" : 0.01, 
      "length": 2, 
      "unit": "" 
      },
"03": {
      "name": "AIV", 
      "resolution" : 0.01, 
      "length": 2, 
      "unit": "" 
      }
} 
```
</details>

### Decoder in Python

<details>
<summary> Click to view the Payload Decoder code </summary>

```python
import re, json 
 
data='007e00280c15ba04f116b9000017b8641867011819f300401af30001' 
pattern = re.compile('.{2}') 
handle_data = re.findall(pattern, data) 
 
snsr_id_index = 0 
ssn = '' 
value = '' 
 
 
def twos_complement_hex(hex_str): 
    decimal_num = int(hex_str, 16) 
    twos_complement = (decimal_num + (1 << (len(hex_str) * 4))) % (1 << (len(hex_str) * 4)) 
    return twos_complement  # Return the integer value 
 
 
with open('snsr_type_def.json', 'r', encoding='UTF-8') as f: 
    unit_dict = json.load(f) 
 
while (snsr_id_index+1) < len(handle_data): 
    ipso_index = snsr_id_index+1 
 
    if handle_data[ipso_index] not in unit_dict.keys(): 
        pass 
    elif (len(handle_data[ipso_index-1:]) - 
(2+unit_dict[handle_data[ipso_index]]['length']) ) < 0: 
        pass 
    else: 
        inner_dict = unit_dict[handle_data[ipso_index]] 
        name = inner_dict['name'] 
        resolution = inner_dict['resolution'] 
        unit = inner_dict['unit'] 
        data_index = ipso_index+1 
        sensor_id_type = ''.join(i for i in handle_data[data_index-2: 
data_index]) 
        if name == 'RS485': 
            inner_dict['length'] = len(handle_data[data_index:]) 
        hex_data = ''.join(i for i in handle_data[data_index: 
data_index+inner_dict['length']]) 
        dec_data = '' 
        if name == 'SSN': 
            dec_data = hex_data 
            ssn = hex_data 
        elif name == 'RS485': 
            dec_data = hex_data 
        elif name == 'A': 
            for A in range(3): 
                dec_data += 
'%s,'%round(twos_complement_hex(hex_data[A*4:(A+1)*4])*resolution,2)  
            dec_data = dec_data[0:-1] 
        else: 
            dec_data = round(twos_complement_hex(hex_data)*resolution, 
len(str(resolution ))-1) 
        value += '%s: %s%s, '   %(name, dec_data, unit) 
        snsr_id_index += (1+inner_dict['length']) 
 
    snsr_id_index += 1 
 
print(value)
```

</details>

<b>Data Interpretation</b>

| Data Unit                     | ID (Channel) | Type   | Data    |
|-------------------------------|--------------|--------|---------|
| Serial Number                 | 1 Byte       | 1 Byte | 3 Bytes |
| Battery Voltage               | 1 Byte       | 1 Byte | 2 Bytes |
| Battery Current               | 1 Byte       | 1 Byte | 2 Bytes |
| Battery SOC (State of charge) | 1 Byte       | 1 Byte | 1 Byte  |
| Battery Temperature           | 1 Byte       | 1 Byte | 2 Bytes |
| Battery Error                 | 1 Byte       | 1 Byte | 2 Bytes |
| Battery FW Version            | 1 Byte       | 1 Byte | 2 Bytes |

With the defined data, here's how to interpret the payload received data:


### RAK9154 Solar Battery Data Sample

Payload (hex) received data: `007e 00280c 15ba04f1 16b90000 17b864 18 670118 19 f30040 1af30001`

| Data Unit           | ID (Channel) | Type | Data   |
|---------------------|--------------|------|--------|
| Serial Number       | 00           | 7e   | 00280C |
| Battery Voltage     | 15           | ba   | 04F1   |
| Battery Current     | 16           | b9   | 0000   |
| Battery SOC         | 17           | b8   | 64     |
| Battery Temperature | 18           | 67   | 0118   |
| Battery Error       | 19           | f3   | 0040   |
| Battery FW Version  | 1a           | f3   | 0001   |

Convert the sensor data from hexadecimal to decimal:

- **Serial Number**: `007e`
- **Data**: `00280c`

```
SN: 00280C
```

- **Battery Voltage**: `15ba`
- **Data**: `04f1`

```
04F1 (hex) = 1265 (dec)
1265 x 0.01 (conversion factor) = 12.65 V
```

- **Battery Current**: `16b9`
- **Data**: `0000`

```
0000 (hex) = 0 (dec)
0 x 0.01 (conversion factor) = 0 A
```

- **Battery SOC**: `17b8`
- **Data**: `64`

```
64 (hex) = 100 (dec)
100 x 0.01 (conversion factor) = 1.00 = 100%
```

- **Battery Temperature**: `1867`
- **Data**: `	0118`

```
0118 (hex) = 280 (dec)
280 x 0.1 (conversion factor) = 28.0° C
```

- **Battery Error**: `19f3`
- **Data**: `0040`  

```
Battery Error = no error
```

- **Battery FW Version**: `1af3`
- **Data**: `0001`  

```
Battery FW Version = v00.01
```

## RAK200-03 Pyranometer Sample Payload Decoder

<details>
<summary> Click to view the Payload Decoder code </summary>

````js
function Decoder(bytes, port) {
var decoded = {};
var str = bin2HexStr(bytes);
    var i = 0;  
    while (i < str.length) {  
        var channelId = parseShort(str.slice(i, i + 4), 16);  
        var value = parseShort(str.slice(i + 4, i + 8), 16);  
        i += 8;  
        switch (channelId) {  
            case 0x01C3:  
                decoded.pyranometer = value;  
                break;  
            default:  
                break;  
        }  
    }  
  
    try {  
        decoded.lorawan_rssi = (port && port.metadata && port.metadata.rssi) || 0;  
        decoded.lorawan_snr = (port && port.metadata && port.metadata.snr) || 0;  
        decoded.lorawan_datarate = (port && port.metadata && port.metadata.data_rate) || '';  
    } catch (e) {  
        console.log('Failed to read gateway metadata');  
    }  
  
    return decoded;  
}  
  
function bin2HexStr(bytesArr) {  
    var str = '';  
    for (var i = 0; i < bytesArr.length; i++) {  
        var tmp = (bytesArr[i] & 0xff).toString(16);  
        if (tmp.length == 1) {  
            tmp = '0' + tmp;  
        }  
        str += tmp;  
    }  
    return str;  
}  
  
// convert string to short integer  
function parseShort(str, base) {  
    var n = parseInt(str, base);  
    return (n << 16) >> 16;  
}  
  
// convert string to triple bytes integer  
function parseTriple(str, base) {  
    var n = parseInt(str, base);  
    return (n << 8) >> 8;  
}      var n = parseInt(str, base);  
    return (n << 8) >> 8;   
````

</details>

<b>Data Interpretation</b>

| Sensor Data Unit | ID (Channel) | Type   | Data    |
|------------------|--------------|--------|---------|
| Serial Number    | 1 Byte       | 1 Byte | 3 Bytes |
| Pyranometer      | 1 Byte       | 1 Byte | 2 Bytes |

With the defined data, here's how to interpret the payload received data:



### RK200-03 Solar Pyranometer Data Sample

Payload (hex) received data: `007e 006f03 01c3 0000`

| Sensor Data Unit | ID (Channel) | Type | Data   |
|------------------|--------------|------|--------|
| Serial Number    | 00           | 7e   | 006f03 |
| Pyranometer      | 01           | c3   | 0000   |

Convert the sensor data from hexadecimal to decimal:

- **Serial Number**: `007e`
- **Data**: `006f07`

```
SN: 006f03
```

- **Pyranometer**: `01c3`
- **Data**: `0000`

```
0000 (hex) = 0 (dec)
0 x 1 (conversion factor) = 0 W/m2
```

<RkBottomNav/>