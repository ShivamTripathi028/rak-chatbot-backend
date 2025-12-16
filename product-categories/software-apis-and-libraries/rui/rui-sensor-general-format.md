
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RUI Sensor General Format

## General Format

### GGAData

```c
typedef struct GGAData
{
	uint8_t UTC[4];
	uint8_t Date[3];
	bool LatitudeNS;      		//0:N1:S
	uint8_t LatitudeDegree;
	uint32_t LatitudeMinute;
	double Latitude;
	bool LongitudaEW;			//0:E1:W
	uint8_t LongitudaDegree;
	double Longitude;
	uint32_t LongitudaMinute;
	int Quality;
	int NumSatellities;
	int16_t HDOP;
	int16_t Altitude;
	int16_t GeoidHeight;
}RUI_GGA_Data;
```


## RUI GPS Get

```c
RUI_RETURN_STATUS rui_gps_get(RUI_GGA_Data*gps_data)
```

| **@brief**  | This API is used to get the GPS data from GPS module which is integrated in the communicate module like Quectel BG96. |
| ----------- | --------------------------------------------------------------------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                                                                            |
| **@param**  | [RUI_GGA_Data](#ggadata)\*gps_data: the GPS data, GPGGA format                                                        |
| **@module** | RAK5010 and RAK8212-M                                                                                                 |

## RUI GPS Set Mode

```c
RUI_RETURN_STATUS rui_gps_set_mode(DRIVER_MODE mode)
```

| **@brief**  | This API is used to set the work mode of the GPS module which is integrated in the communicate module like Quectel BG96. |
| ----------- | ------------------------------------------------------------------------------------------------------------------------ |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                                                                               |
| **@param**  | [DRIVER_MODE mode](#driver-mode): the GPS module’s work mode.                                                         |
| **@module** | RAK5010 and RAK8212                                                                                                      |


<RkBottomNav/>