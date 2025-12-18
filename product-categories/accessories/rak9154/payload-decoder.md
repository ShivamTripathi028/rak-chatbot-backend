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

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'
import RkCertificationIcons from '@site/src/components/CertificationPage/IconList'

# RAK9154 Solar Battery Lite Data over SensorHub

## Solar Battery Data Unit Definition

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>RAK IPSO</th>
      <th>Data type</th>
      <th>Value Range</th>
      <th>Unit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Battery voltage</td>
      <td>0xBA</td>
      <td>U16</td>
      <td>0-0x05&nbsp;DC (15.00&nbsp;V)</td>
      <td>0.01&nbsp;V</td>
    </tr>
    <tr>
      <td>Battery current</td>
      <td>0xB9</td>
      <td>S16</td>
      <td>-150~150 (1.5&nbsp;A)</td>
      <td>0.01&nbsp;A</td>
    </tr>
    <tr>
      <td>SOC (State of charge)</td>
      <td>0xB8</td>
      <td>U16</td>
      <td>1~100</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>Average Temperature</td>
      <td>0x67</td>
      <td>S16</td>
      <td>-30~105</td>
      <td>0.1°&nbsp;C</td>
    </tr>
    <tr>
      <td>Battery Errors</td>
      <td>0xF3</td>
      <td>U16</td>
      <td>Refer to below <br/> ErrorMessageTable</td>
      <td>bit</td>
    </tr>
    <tr>
      <td>BMS Firmware version</td>
      <td>0xF3</td>
      <td>U16</td>
      <td>Vxx.xx</td>
      <td>bit</td>
    </tr>
  </tbody>
</table>

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


<table>
  <thead>
    <tr>
      <th rowSpan="2">Battery Data Unit</th>
      <th colSpan="3">Uplink Payload</th>
    </tr>
    <tr>
      <th>ID</th>
      <th>IPSO</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Serial Number</td>
      <td>1 Byte</td>
      <td>1 Byte</td>
      <td>3 Bytes</td>
    </tr>
    <tr>
      <td>Voltage</td>
      <td>1 Byte</td>
      <td>1 Byte</td>
      <td>2 Bytes</td>
    </tr>
    <tr>
      <td>Current</td>
      <td>1 Byte</td>
      <td>1 Byte</td>
      <td>2 Bytes</td>
    </tr>
    <tr>
      <td>State of Charge</td>
      <td>1 Byte</td>
      <td>1 Byte</td>
      <td>1 Byte</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>1 Byte</td>
      <td>1 Byte</td>
      <td>2 Bytes</td>
    </tr>
    <tr>
      <td>Battery Error</td>
      <td>1 Byte</td>
      <td>1 Byte</td>
      <td>2 Bytes</td>
    </tr>
    <tr>
      <td>Battery FW Version</td>
      <td>1 Byte</td>
      <td>1 Byte</td>
      <td>2 Bytes</td>
    </tr>
  </tbody>
</table>
                                                                         
### Decoder:

<table>
  <thead>
    <tr>
      <th rowSpan="2">Battery Data Unit</th>
      <th colSpan="3">Uplink Payload</th>
      <th rowSpan="2">Decode Data</th>
    </tr>
    <tr>
      <th>ID</th>
      <th>IPSO</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Serial Number</td>
      <td>00</td>
      <td>7e</td>
      <td>094807</td>
      <td>94807</td>
    </tr>
    <tr>
      <td>Voltage</td>
      <td>15</td>
      <td>ba</td>
      <td>0464</td>
      <td>11.24&nbsp;V</td>
    </tr>
    <tr>
      <td>Current</td>
      <td>16</td>
      <td>b9</td>
      <td>0043</td>
      <td>0.67&nbsp;A</td>
    </tr>
    <tr>
      <td>State of Charge</td>
      <td>17</td>
      <td>b8</td>
      <td>45</td>
      <td>69%</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18</td>
      <td>67</td>
      <td>00d2</td>
      <td>21.0°&nbsp;C</td>
    </tr>
    <tr>
      <td>Battery Error</td>
      <td>19</td>
      <td>f3</td>
      <td>0000</td>
      <td>no error</td>
    </tr>
    <tr>
      <td>Battery FW Version</td>
      <td>1a</td>
      <td>f3</td>
      <td>0002</td>
      <td>V00.02</td>
    </tr>
  </tbody>
</table>

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

<table>
  <thead>
    <tr>
      <th>Bit#</th>
      <th>Description</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Bit0 ~ Bit5</td>
      <td>Reserved</td>
      <td>Reserved</td>
    </tr>
    <tr>
      <td>Bit6</td>
      <td>Over voltage protect</td>
      <td>0 : normal <br/> 1 : fault</td>
    </tr>
    <tr>
      <td>Bit7</td>
      <td>Charge over current protect</td>
      <td>0 : normal <br/> 1 : fault</td>
    </tr>
    <tr>
      <td>Bit8</td>
      <td>Charge low temperature protect</td>
      <td>0 : normal <br/> 1 : fault</td>
    </tr>
    <tr>
      <td>Bit9</td>
      <td>Charge high temperature protect</td>
      <td>0 : normal <br/> 1 : fault</td>
    </tr>
    <tr>
      <td>Bit10</td>
      <td>Charge short circuit protect</td>
      <td>0 : normal <br/> 1 : fault</td>
    </tr>
    <tr>
      <td>Bit11</td>
      <td>Charge over current lock</td>
      <td>0 : normal <br/> 1 : fault</td>
    </tr>
    <tr>
      <td>Bit12 ~ Bit15</td>
      <td>Reserved</td>
      <td>Reserved</td>
    </tr>
  </tbody>
</table>

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

<RkBottomNav/>