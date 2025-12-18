

# RUI Device General Format

This part supports all module with device API

## General Format

**rui_device_xxx()**

## RUI Device Version

```c
RUI_RETURN_STATUS rui_device_version(uint8_t *version)
```

| **@brief**  | This API is used to get the current firmware version of your device |
| ----------- | ------------------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                          |
| **@param**  | uint8_t \*version: the current firmware version                     |
| **@module** | RAK811, RAK4200, RAK8212-M, RAK5010, 4400 and RAK4600 core module   |

## RUI Device Reset

```c
RUI_RETURN_STATUS rui_device_reset(void)
```

| **@brief**  | This API is used to reset the device                              |
| ----------- | ----------------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                        |
| **@param**  | void                                                              |
| **@module** | RAK811, RAK4200, RAK8212-M, RAK5010, 4400 and RAK4600 core module |

## RUI Device Sleep

```c
typedef void (*sensor_wakeup)(void);

typedef void (*sensor_sleep)(void);

RUI_RETURN_STATUS rui_sensor_register_callback(sensor_wakeup callback1,sensor_sleep callback2);

RUI_RETURN_STATUS rui_device_sleep(uint32_t on);
```

| **@brief**  | This API is used to set the device to sleep mode.                                                                                                  |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **@return** | NULL                                                                                                                                               |
| **@param**  | uint32_t on/off: on/off

 sensor_wakeup, sensor_sleep: app callback, user can add sensor operation here to finish function and power control |
| **@module** | RAK811, RAK4200, RAK8212-M, RAK5010, 4400 and RAK4600 core module                                                                                  |

## RUI Device Boot

```c
void rui_device_boot()
```

| **@brief**   | This API is used to set the device to boot mode. |
| ------------ | ------------------------------------------------ |
| **@return**  | NULL                                             |
| **@param**   | NULL                                             |
| **@support** | RAK811 and RAK4200 core module                   |

