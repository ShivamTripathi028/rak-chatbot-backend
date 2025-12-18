---
slug: /product-categories/accessories/rak9154/payload-decoder/
title: RAK9154 WisNode Sensor Hub Payload Decoder
description: Contains instructions and tutorials for installing and deploying your RAK9154. Instructions are written in a detailed and step-by-step manner for an easier experience in setting up your LoRaWAN Module.
image: "https://images.docs.rakwireless.com/wisnode/rak9154/rak9154.jpg"
keywords:
    - RAK9154
    - Payload Decoder
    - wisnode
    - sensor hub
sidebar_label: Payload Decoder
---

# RAK9154 Solar Battery Lite Data over SensorHub

## Solar Battery Data Unit Definition

| Name | RAK IPSO | Data type | Value Range | Unit |
| --- | --- | --- | --- | --- |
| Battery voltage | 0xBA | U16 | 0-0x05 DC (15.00 V) | 0.01 V |
| Battery current | 0xB9 | S16 | -150~150 (1.5 A) | 0.01 A |
| SOC (State of charge) | 0xB8 | U16 | 1~100 | 0.01 |
| Average Temperature | 0x67 | S16 | -30~105 | 0.1° C |
| Battery Errors | 0xF3 | U16 | Refer to below ErrorMessageTable | bit |
| BMS Firmware version | 0xF3 | U16 | Vxx.xx | bit |

### Example:

Cloud APP server gets a SensorHub uplink data in JSON format as below.  

```json
{
    'deviceName': '494', 'timestamp': 1701921826,  
    'fCnt': 40, 'rssi': -65, 'loRaSNR': 13.5,  
    'freq': 903700000, 'dr': 3, 'fPort': 2,  
    'data': '007e09480715ba046416b9004317b84518670d2e19f300001af30002',  
    'adr': True 
}  
```

The key **data** represents the SensorHub uplink payload transmitted over the LoRa network. This payload consists of multiple sensor data units. Each data unit includes three fields:

1. **ID** (1 byte)
2. **Data Type** (RAK IPSO, 1 byte)
3. **Data Value** (variable size)

Below is an example of a SensorHub uplink payload for a Battery device, which contains 7 data units. The first data unit corresponds to the SensorHub serial number (SN), while the remaining 6 units provide battery status data.

| Battery Data Unit | Uplink Payload |  |  |
| --- | --- | --- | --- |
| Serial Number | 1 Byte | 1 Byte | 3 Bytes |
| Voltage | 1 Byte | 1 Byte | 2 Bytes |
| Current | 1 Byte | 1 Byte | 2 Bytes |
| State of Charge | 1 Byte | 1 Byte | 1 Byte |
| Temperature | 1 Byte | 1 Byte | 2 Bytes |
| Battery Error | 1 Byte | 1 Byte | 2 Bytes |
| Battery FW Version | 1 Byte | 1 Byte | 2 Bytes |

                                                                         
### Decoder:

| Battery Data Unit | Uplink Payload | Decode Data |  |  |
| --- | --- | --- | --- | --- |
| Serial Number | 00 | 7e | 094807 | 94807 |
| Voltage | 15 | ba | 0464 | 11.24 V |
| Current | 16 | b9 | 0043 | 0.67 A |
| State of Charge | 17 | b8 | 45 | 69% |
| Temperature | 18 | 67 | 00d2 | 21.0° C |
| Battery Error | 19 | f3 | 0000 | no error |
| Battery FW Version | 1a | f3 | 0002 | V00.02 |

Convert the sensor data from hexadecimal to decimal:

- **Serial Number**: `007e`
- **Data**: `094807`

```
SN: 94807
```

- **Battery Voltage**: `15ba`
- **Data**: `0464`

```
0464 (hex) = 1124 (dec)
1124 x 0.01 (conversion factor) = 11.24 V
```

- **Battery Current**: `16b9`
- **Data**: `0043`

```
0043 (hex) = 67 (dec)
67 x 0.01 (conversion factor) = 0.67 A
```

- **Battery SOC**: `17b8`
- **Data**: `45`

```
45 (hex) = 69 (dec)
69 x 0.01 (conversion factor) = 0.69 = 69%
```

- **Battery Temperature**: `1867`
- **Data**: `00d2`

```
00d2 (hex) = 210 (dec)
210 x 0.1 (conversion factor) = 21.0° C
```

- **Battery Error**: `19f3`
- **Data**: `0000`  

```
Battery Error = no error
```

- **Battery FW Version**: `1af3`
- **Data**: `0002`  

```
Battery FW Version = v00.02
```

## Error Message Table

| Bit# | Description | Value |
| --- | --- | --- |
| Bit0 ~ Bit5 | Reserved | Reserved |
| Bit6 | Over voltage protect | 0 : normal 1 : fault |
| Bit7 | Charge over current protect | 0 : normal 1 : fault |
| Bit8 | Charge low temperature protect | 0 : normal 1 : fault |
| Bit9 | Charge high temperature protect | 0 : normal 1 : fault |
| Bit10 | Charge short circuit protect | 0 : normal 1 : fault |
| Bit11 | Charge over current lock | 0 : normal 1 : fault |
| Bit12 ~ Bit15 | Reserved | Reserved |

## Decoder Sample Code

### RAK IPSO Sensor type definition in JSON : filename *snsr_type_def.json*

<details>
<summary> Click to view the code </summary>

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

### Decoder example in Python

<details>
<summary> Click to view the code </summary>

```python
import re, json 
 
data='007e09480715ba046416b9004317b84518670d2e19f300001af30002' 
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

