

# RUI Interface General Format

This part support all module with BSP API.

## General Format

**rui\_"Interface Type"\_xxx()**

## General Definition

### RUI_UART_DEF

```c
typedef enum RUI_UART_DEF
{
	RUI_UART0 = 0,
	RUI_UART1 = 1,
	RUI_UART2 = 2,
	RUI_UART3 = 3
}RUI_UART_DEF;
```

### RUI_IF_READ_WRITE

```c
typedef enum RUI_IF_READ_WRITE
{
	RUI_IF_READ = 0,
	RUI_IF_WRITE = 1
}RUI_IF_READ_WRITE;
```

### RUI_I2C_ST

```c
typedef struct RUI_I2C_ST
{
	uint32_t INSTANCE_ID;
	uint32_t PIN_SDA;   // SDA pin num
	uint32_t PIN_SCL;   // SCL pin num
	uint32_t FREQUENCY;
	uint32_t REG_NULL; // if no reg , should be 0xAA
}RUI_I2C_ST;
```

### RUI_I2C_FREQ_ST

```c
typedef enum RUI_I2C_FREQ_ST
{
	RUI_I2C_FREQ_100K,
	RUI_I2C_FREQ_400K
}RUI_I2C_FREQ_ST;
```

### RUI_SPI_ST

```c
typedef struct
{
	uint32_t INSTANCE_ID;
	uint32_t PIN_CS;   //
	uint32_t PIN_SCL;   //
	uint32_t PIN_MISO;   //
	uint32_t PIN_MOSI;   //
	uint32_t FREQUENCY;
} RUI_SPI_ST;
```

### RUI_SPI_FREQ_ST

```c
typedef enum RUI_SPI_FREQ_ST
{
	RUI_I2C_FREQ_125K,
	RUI_I2C_FREQ_250K,
	RUI_I2C_FREQ_500K,
	RUI_I2C_FREQ_1M,
	RUI_I2C_FREQ_2M,
	RUI_I2C_FREQ_4M,
	RUI_I2C_FREQ_8M
}RUI_SPI_FREQ_ST;
```

### RUI_GPIO_PIN_DIR_ST

```c
typedef enum
{
	RUI_GPIO_PIN_DIR_INPUT, // Input.
	RUI_GPIO_PIN_DIR_OUTPUT // Output.
} RUI_GPIO_PIN_DIR_ST;
```

### RUI_GPIO_PIN_PULL_ST

```c
typedef enum
{
	RUI_GPIO_PIN_NOPULL,   //  Pin pull-up resistor disabled.
	RUI_GPIO_PIN_PULLDOWN, //  Pin pull-down resistor enabled.
	RUI_GPIO_PIN_PULLUP    //  Pin pull-up resistor enabled.
} RUI_GPIO_PIN_PULL_ST;
```

### RUI_GPIO_INTERRUPT_EDGE

```c
typedef enum
{
    RUI_GPIO_EDGE_RAISE,
    RUI_GPIO_EDGE_FALL,
    RUI_GPIO_EDGE_FALL_RAISE
} RUI_GPIO_INTERRUPT_EDGE;
```

### RUI_GPIO_INTERRUPT_PRIORITY

```c
typedef enum
{
    RUI_GPIO_IRQ_HIGH_PRIORITY,
    RUI_GPIO_IRQ_NORMAL_PRIORITY,
    RUI_GPIO_IRQ_LOW_PRIORITY,
} RUI_GPIO_INTERRUPT_PRIORITY;
```

### RUI_GPIO_ST

```c
typedef struct
{
	uint32_t pin_num;
	RUI_GPIO_PIN_DIR_ST dir;
	RUI_GPIO_PIN_PULL_ST pull;
}RUI_GPIO_ST;
```

### RUI_TIMER_MODE_ST

```c
typedef enum
{
	RUI_TIMER_MODE_SINGLE_SHOT,     /**< The timer will expire only once. */
	RUI_TIMER_MODE_REPEATED        /**< The timer will restart each time it expires. */
} RUI_TIMER_MODE_ST;
```

### RUI_TIMER_ST

```c
typedef void (* TIMER_CALLBACK) (void);

typedef struct{
	uint32_t timeout_ms;
	RUI_TIMER_MODE_ST timer_mode;
	TIMER_CALLBACK timer_callback;
}RUI_TIMER_ST;
```

### RUI_FLASH_MOD

```c
typedef enum
{
    RUI_FLASH_USER = 0,                  // a region for user , less than 128 bytes
    RUI_FLASH_ORIGIN              //inner struct region , advise not modify it
}RUI_FLASH_MODE;
```

## RUI UART Initialize

```c
RUI_RETURN_STATUS rui_uart_init(RUI_UART_DEF uart_def,RUI_UART_BAUDRATE baudrate);
```

| **@brief**  | This API is used to configure the parameters for UART.                                                               |
| ----------- | -------------------------------------------------------------------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                                                                           |
| **@param**  | [RUI_UART_DEF](rui-interface-general-format#rui_uart_def) uart_def:the instance of UART.

 RUI_UART_BAUDRATE baudrate: UART baudrate value |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, and RAK5010.                                                                      |

## RUI UART Uninitialize

```c
RUI_RETURN_STATUS rui_uart_unint(RUI_UART_DEF uart_def);
```

| **@brief**  | This API is used to uninitialize UART.                        |
| ----------- | ------------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                    |
| **@param**  | [RUI_UART_DEF](rui-interface-general-format#rui_uart_def) uart_def: the instance of UART. |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, and RAK5010.               |

## RUI UART Send

```c
RUI_RETURN_STATUS rui_uart_send(RUI_UART_DEF uart_def, uint8_t *pdata, uint16_t len)
```

| **@brief**  | This API is used to send data via UART.                                                                                                                            |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                                                                                                                         |
| **@param**  | [RUI_UART_DEF](rui-interface-general-format#rui_uart_def) uart_def : the instance of UART.
uint8t \*pdata : the pointer of data you want to send.
uint16_t len : the length of the data. |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, and RAK5010.                                                                                                                    |

## RUI UART Receive

```c
void rui_uart_recv(RUI_UART_DEF uart_def, uint8_t *pdata, uint16_t len)
```

| **@brief**  | This API is used to receive data from UART.                                                                                                                            |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **@return** | NULL                                                                                                                                                                   |
| **@param**  | [RUI_UART_DEF](rui-interface-general-format#rui_uart_def) uart_def : the instance of UART.
uint8_t \*pdata : the pointer of data.
uint16_t len : the length of data. This value is always 1. |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, and RAK5010.                                                                                                                        |

## RUI UART Configure Mode

```c
RUI_RETURN_STATUS rui_uart_mode_config(RUI_UART_DEF uart_def,RUI_UART_MODE uart_mode);
```

| **@brief**  | This API is used to configure uart work mode.                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                                                                                                   |
| **@param**  | [RUI_UART_DEF](rui-interface-general-format#rui_uart_def) uart_def: the instance of UART.
RUI_UART_MODE uart_mode: value for RUI_UART_NORMAL, RUI_UART_UNVARNISHED. |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, and RAK5010.                                                                                              |

## RUI GPIO Initialize

```c
RUI_RETURN_STATUS rui_gpio_init(RUI_GPIO_ST *rui_gpio);
```

| **@brief**  | This API is used to configure GPIO.                          |
| ----------- | ------------------------------------------------------------ |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                   |
| **@param**  | [RUI_GPIO_ST](rui-interface-general-format#rui_gpio_st)\*rui_gpio: the instance of GPIO. |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M.    |

## RUI GPIO Uninitialize

```c
void rui_gpio_uninit(RUI_GPIO_ST *rui_gpio);
```

| **@brief**  | This API is used to deinitialize GPIO.                        |
| ----------- | ------------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                    |
| **@param**  | [RUI_GPIO_ST](rui-interface-general-format#rui_gpio_st) \*rui_gpio: the instance of gpio. |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M.     |

## RUI GPIO Read/Write

```c
RUI_RETURN_STATUS rui_gpio_rw(RUI_IF_READ_WRITE rw_status,RUI_GPIO_ST *rui_gpio,uint8_t* status);
```

| **@brief**  | This API is used to read or set a certain GPIO's Status.                                                                                                                                    |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                                                                                                                                                  |
| **@param**  | [RUI_IF_READ_WRITE](rui-interface-general-format#rui_if_read_write) \*rui_gpio: the pin number of the GPIO which you want to read or set.
uint8_t\* status: the pointer of GPIO Value. 0 : low level, 1: high Level. |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M.                                                                                                                                   |

## RUI GPIO Interrupt

```c
typedef void (*interrupt_callback)(void);
RUI_RETURN_STATUS rui_gpio_interrupt(bool control, RUI_GPIO_ST st, RUI_GPIO_INTERRUPT_EDGE edge, RUI_GPIO_INTERRUPT_PRIORITY pro,calback callback);
```

| **@brief**  | This API is used to register external GPIO, it may lead to power current increase. e.g 130 µA in Nordic platform.                                       |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                                                                                                              |
| **@param**  | bool control: true or false, use it or not.

[RUI_GPIO_ST](rui-interface-general-format#rui_gpio_st) pro: priority for interrupt

calback callback: interrupt callback. |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M.                                                                                               |

## RUI Timer Initialize

```c
RUI_RETURN_STATUS rui_timer_init(void *obj, void ( *callback )( void ));
```

| **@brief**  | This API is used to create/initialize a timer.                                        |
| ----------- | ------------------------------------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                                            |
| **@param**  | void \*obj : timer instance
void (\*callback)(void): timer event callback function |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M.                             |

## RUI Timer Uninitialize

```c
RUI_RETURN_STATUS rui_timer_uninit(void *obj);
```

| **@brief**  | This API is used to uninitialize a timer.  |
| ----------- | ------------------------------------------ |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status) |
| **@param**  | void \*obj: timer instance.                |
| **@module** | RAK4600, RAK5010 and RAK8212-M.            |

## RUI Timer Set Value

```c
RUI_RETURN_STATUS rui_timer_setvalue(void *obj, uint32_t value );
```

| **@brief**  | This API is used to set the interval value for timer.     |
| ----------- | --------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                |
| **@param**  | void \*obj: timer instance
uint32_t value: timer value |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M. |

## RUI Timer Start

```c
RUI_RETURN_STATUS rui_timer_start(void *obj);
```

| **@brief**  | This API is used to start the timer                       |
| ----------- | --------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                |
| **@param**  | void \*obj: timer instance                                |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M. |

## RUI Timer Stop

```c
RUI_RETURN_STATUS rui_timer_stop(void *obj);
```

| **@brief**  | This API is used to stop the timer.                       |
| ----------- | --------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                |
| **@param**  | void \*obj: timer instance                                |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M. |

## RUI ADC Initialize

```c
RUI_RETURN_STATUS rui_adc_init(RUI_GPIO_ST *rui_gpio);
```

| **@brief**  | This API is used to initialize ADC                            |
| ----------- | ------------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                    |
| **@param**  | [RUI_GPIO_ST](rui-interface-general-format#rui_gpio_st) \*rui_gpio: the instance of GPIO. |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M.     |

## RUI ADC Uninitialize

```c
RUI_RETURN_STATUS rui_adc_uninit(RUI_GPIO_ST *rui_gpio);
```

| **@brief**   | This API is used to uninitialize ADC                          |
| ------------ | ------------------------------------------------------------- |
| **@return**  | [RUI_RETURN_STATUS](#rui-return-status)                    |
| **@param**   | [RUI_GPIO_ST](rui-interface-general-format#rui_gpio_st) \*rui_gpio: the instance of GPIO. |
| **@support** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M.     |

## RUI ADC Read

```c
RUI_RETURN_STATUS rui_adc_get(RUI_GPIO_ST *rui_gpio, uint16_t* value);
```

| **@brief**  | This API is used to read the value of the ADC Pin                                                          |
| ----------- | ---------------------------------------------------------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                                                                 |
| **@param**  | uint8_t\* value: the value which is read from ADC.
[RUI_GPIO_ST](rui-interface-general-format#rui_gpio_st) \*rui_gpio : GPIO struct |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M.                                                  |

## RUI I2C Initialization

```c
RUI_RETURN_STATUS rui_i2c_init(RUI_I2C_ST *rui_i2c);
```

| **@brief**  | This API is used to init I2C.                                      |
| ----------- | ------------------------------------------------------------------ |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                         |
| **@param**  | [RUI_I2C_ST](#rui-i2c-st) \*rui_i2c: initialize parameters struct. |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, and RAK5010.                    |

## RUI I2C Read/Write

```c
RUI_RETURN_STATUS rui_i2c_rw(RUI_I2C_ST *rui_i2c, uint8_t devAddr, uint16_t regAddr, uint8_t* data, uint16_t len)
```

| **@brief**  | This API is used to Read/Write Through I2C.                                                                                                                                                                                                                            |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                                                                                                                                                                                                                             |
| **@param**  | RUI_I2C_ST \*rui_i2c: init parameters struct. uint8_t devAddr: device address in HEX Format. uint16_t regAddr: the sensor's register address in HEX Format. uint8_t \*data: the data output or data to be written through I2C. uint16_t len : the data length in byte. |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, and RAK5010.                                                                                                                                                                                                                        |
## RUI SPI Initialization

```c
RUI_RETURN_STATUS rui_spi_init(RUI_SPI_ST *rui_spi);
```

| **@brief**  | This API is used to initialize SPI.                               |
| ----------- | ----------------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                        |
| **@param**  | [RUI_SPI_ST](#rui-spi-st) \*rui_spi: initialize parameters struct |
| **@module** | RAK4400, RAK4600 and RAK5010.                                     |

## RUI SPI Read/Write

```c
RUI_RETURN_STATUS rui_spi_rw(RUI_IF_READ_WRITE rw, uint8_t *tx, uint16_t tx_len, uint8_t *rx, uint16_t rx_len);
```

| **@brief**  | This API is used to read/write through SPI.                                                                                                                                                                           |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                                                                                                                                                                            |
| **@param**  | [RUI_IF_READ_WRITE](rui-interface-general-format#rui_if_read_write) rw: read or write through SPI.

uint8_t \*tx: write through SPI.

uint16_t tx_len: TX length

uint8_t \*rx: read buffer.

uint16_t rx_len: RX length. |
| **@module** | RAK4400, RAK4600 and RAK5010.                                                                                                                                                                                         |
## RUI PWM Initialize

```c
RUI_RETURN_STATUS rui_pwm_init(RUI_PWM_ST* pwm_st);
```

| **@brief**  | This API is used to initialize PWM         |
| ----------- | ------------------------------------------ |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status) |
| **@param**  | RUI_PWM_ST\* pwm_st: pwm structure pointer |
| **@module** | RAK811                                     |

## RUI PWM Start

```c
RUI_RETURN_STATUS rui_pwm_start(RUI_PWM_ST* pwm_st)
```

| **@brief**  | This API is used to start PWM              |
| ----------- | ------------------------------------------ |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status) |
| **@param**  | RUI_PWM_ST\* pwm_st: pwm structure pointer |
| **@module** | RAK811                                     |

## RUI PWM Stop

```c
RUI_RETURN_STATUS rui_pwm_stop(RUI_PWM_ST* pwm_st)
```

| **@brief**  | This API is used to stop PWM.              |
| ----------- | ------------------------------------------ |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status) |
| **@param**  | RUI_PWM_ST\* pwm_st: pwm structure pointer |
| **@module** | RAK811                                     |

## RUI Delay Milliseconds

```c
RUI_RETURN_STATUS rui_delay_ms( uint32_t value );
```

| **@brief**  | This API is used to delay time in milliseconds (ms).      |
| ----------- | --------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                |
| **@param**  | uint32_t value : delay time value.                        |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M. |

## RUI Delay Microseconds

```c
RUI_RETURN_STATUS rui_delay_us( uint32_t value );
```

| **@brief**  | This API is used to delay time in microseconds (µs).      |
| ----------- | --------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                |
| **@param**  | uint32_t value: delay time value.                         |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M. |

## RUI Initialize System

```c
void rui_init(void);
```

| **@brief**  | This API is used to initialize the system.                |
| ----------- | --------------------------------------------------------- |
| **@return** | NONE                                                      |
| **@param**  | NONE                                                      |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M. |

## RUI Running

```c
void rui_running(void);
```

| **@brief**  | This API is used to run preset tasks, including low-power processing. |
| ----------- | --------------------------------------------------------------------- |
| **@return** | NONE                                                                  |
| **@param**  | NONE                                                                  |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M.             |

## RUI Print Log

```c
void RUI_LOG_PRINTF(fmt, args...);
```

| **@brief**  | This API is used to print log.                            |
| ----------- | --------------------------------------------------------- |
| **@return** | NONE                                                      |
| **@param**  | Custom                                                    |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M. |

## RUI Flash Write

```c
RUI_RETURN_STATUS rui_flash_write(RUI_FLASH_MODE mode, uint8_t *str, uint32_t len);
```

| **@brief**  | This API is used to write user data to flash                                                                                 |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                                                                                           |
| **@param**  | uint8_t \*str

 uint32_t len: For STM Series (RAK811/RAK4200/RAK4270) - Max 128 Bytes. For Nordic Series (RAK8212/RAK5010/RAK4600) - Max 64KB

[RUI_FLASH_MODE](rui-interface-general-format#rui_flash_mod) mode: user data or origin data |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M.                                                                            |

## RUI Flash Read

```c
RUI_RETURN_STATUS rui_flash_read(RUI_FLASH_MODE mode,uint8_t *str, uint32_t len);
```

| **@brief**  | This API is used to read user data from flash                                                                                 |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                                                                                           |
| **@param**  | uint8_t \*str

 uint32_t len: For STM Series (RAK811/RAK4200/RAK4270) - Max 128 Bytes. For Nordic Series (RAK8212/RAK5010/RAK4600) - Max 64KB

[RUI_FLASH_MODE](rui-interface-general-format#rui_flash_mod) mode: user data or origin data |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M.                                                                            |

## RUI AT Response

```c
void  rui_at_response(bool is_success, uint8_t *p_msg, uint16_t ret_code);
```

| **@brief**  | This API is used to return info for user defined AT, so that application can use their AT.                     |
| ----------- | -------------------------------------------------------------------------------------------------------------- |
| **@return** | [RUI_RETURN_STATUS](#rui-return-status)                                                                                  |
| **@param**  | bool is_success: true or false

 uint8_t \*p_msg: user message

 uint16_t ret_code:user error code |
| **@module** | RAK811, RAK4200, RAK4400, RAK4600, RAK5010 and RAK8212-M.                                                      |

