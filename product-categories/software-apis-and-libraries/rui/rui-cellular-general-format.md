

# RUI Cellular General Format

This part supports **RAK5010** and **RAK8212**(M) only.

```c
rui_cellular_xxx()
```

## RUI Cellular Send

```c
RUI_RETURN_STATUS rui_cellular_send(uint8_t *data)
```

| @brief | This API is used to send data through cellular. | 
| ---- | ---- | 
| **@return** | [RUI_RETURN_STATUS](/RUI/#rui-return-status.html) | 
| **@param** | __uint8_t *data__: the data which will be sent through cellular. | 
| **@module** | RAK8212-M and RAK5010 core module. | 

## RUI Cellular Response

```c
RUI_RETURN_STATUS rui_cellular_response(uint8_t *response, uint32_t len, uint32_t timeout)
```

| @brief | This API is used to wait for a correct response from cellular module. | 
| ---- | ---- | 
| **@return ** | [RUI_RETURN_STATUS](/RUI/#rui-return-status.html) | 
| **@param** | __uint8_t *response__: the response of server string 
 **uint32_t len**: response data length 
 **uint32_ t timeout**: the time to wait for response until timeout | 
| **@module** | RAK8212-M and RAK5010 core module. | 

## RUI Cellular Register Receive Callback

```c
typdef void(*cellular_receive)(uint8_t *data);
RUI_RETURN_STATUS rui_cellular_register_recv_callback(cellular_receive callback)
```

| @brief | This API is used to register a callback function for cellular in application so that application can receive cellular data automatically. | 
| ---- | ---- | 
| **@return** | [RUI_RETURN_STATUS](/RUI/#rui-return-status.html) | 
| **@param** | **cellular_receive callback**: the callback function for receiving cellular data. | 
| **@module** | RAK8212-M and RAK5010 core module. | 

## RUI Cellular Set Mode

```c
RUI_RETURN_STATUS rui_cellular_set_mode(DRIVER_MODE mode)
```

| @brief | This API is used to set the work mode of the cellular module. | 
| ---- | ---- | 
| **@return** | [RUI_RETURN_STATUS](#rui-return-status.html) | 
| **@param** | [DRIVER_MODE](#driver-mode.html) mode: the cellular module’s work mode | 
| **@module** | RAK8212-M and RAK5010 core module. | 

## RUI Cellular Open Socket

```c
RUI_RETURN_STATUS rui_cellular_open_socket(uint8_t* data)
```

| @brief | This API is used to open a TCP socket with a remote server. | 
| ---- | ---- | 
| **@return** | [RUI_RETURN_STATUS](/RUI/#rui-return-status.html) | 
| **@param** | __uint8_t* data__: open TCP link cmd 
 For example: AT+QIOPEN=1,0,"TCP","ip",%port,0,1" | 
| **@module** | RAK8212-M and RAK5010 core module. | 

## RUI Cellular Set Operator

```c
RUI_RETURN_STATUS rui_cellular_set_operator(uint8_t *APN,uint8_t *operator_long_name,uint8_t *operator_short_name,uint8_t operator_net)
```

| @brief | This API is used to configure parameters of Cellular operator. | 
| ---- | ---- | 
| **@return** | [RUI_RETURN_STATUS](/RUI/#rui-return-status.html) | 
| **@param** | __uint8_t *APN__: The APN name of Cellular operator 
 __uint8_t *operator_long_name__: The operator’s long name. 
 For example: “CHINAMOBILE”. 
 __uint8_t *operator_short_name__: The operator's short name. 
 For example, "CMCC" 
 __uint8_t operator_net__: The cellular network type. | 
| **@module** | RAK8212-M and RAK5010 core module. | 

## RUI Cellular Mode

```c
RUI_RETURN_STATUS rui_cellular_mode(uint8_t on);
```

| @brief | This API is used to open or close cellular. | 
| ---- | ---- | 
| @return | [RUI_RETURN_STATUS](/RUI/#rui-return-status.html) | 
| @param | **uint8_t on**: 0-off, 1-on | 
| @module | RAK8212-M and RAK5010 core module. | 

