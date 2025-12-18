---
title: RAK7391 WisGate Connect Connecting to WisBlock
description: Learn how to connect WisBlock modules to the RAK7391 WisGate Connect gateway. This guide covers connector positions, pin definitions, supported modules, and example code for seamless integration.
image: "https://images.docs.rakwireless.com/wisgate/rak7391/rak7391.png"
keywords:
    - RAK7391
    - WisGate Connect
    - WisBlock integration
sidebar_label: Connecting to WisBlock
---

# RAK7391 WisGate Connect Connecting to WisBlock

## Connectors Position

There are two WisBlock slots on the RAK7391 board, right next to the USB 2.0 and USB 3.0 ports. The WisBlock slots support various industrial protocols via WisBlock modules: IO, Analog, 0-5 V, 4-20 mA, ModBUS, and LinBUS.

> **Image:** WisBlock slots

## Pin Definition

Both WisBlock slot connectors use 40-pin high-density headers. Each connector is linked to a GPIO expander (TPT29555-TS5R). The I2C addresses for these GPIO expander chips are 0x26 and 0x27. 

> **Image:** WisBlock slot pinouts

> **Image:** GIPO expand pinouts

## Supported Modules

The WisBlock slots support various industrial protocols via WisBlock modules: IO, Analog, 0-5 V, 4-20 mA, ModBUS, and LinBUS.

### Onboard

- TPT29555 GPIO Expander

### Interface

- [RAK5801 4-20mA Interface Module](https://docs.rakwireless.com/product-categories/wisblock/rak5801/overview/)
- [RAK5802 RS485 ModBUS Module](https://docs.rakwireless.com/product-categories/wisblock/rak5802/overview/)
- [RAK5811 0-5V Interface Module](https://docs.rakwireless.com/product-categories/wisblock/rak5811/overview/)
- [RAK13001 Relay IO Module](https://docs.rakwireless.com/product-categories/wisblock/rak13001/overview/)
- [RAK13004 PWM Expander Module](https://docs.rakwireless.com/product-categories/wisblock/rak13004/overview/)
- [RAK13005 LIN Module](https://docs.rakwireless.com/product-categories/wisblock/rak13005/overview/)
- [RAK13007 Relay Module](https://docs.rakwireless.com/product-categories/wisblock/rak13007/overview/)
- [RAK16001 ADC Module](https://docs.rakwireless.com/product-categories/wisblock/rak16001/overview/)
- [RAK17000 Motor Control Module](https://docs.rakwireless.com/product-categories/wisblock/rak17000/overview/)

### Sensors

- [RAK12004 MQ2 Gas Sensor Module](https://docs.rakwireless.com/product-categories/wisblock/rak12004/overview/)
- [RAK12006 PIR Sensor Module](https://docs.rakwireless.com/product-categories/wisblock/rak12006/overview/)
- [RAK12009 MQ3 Alcohol Gas Sensor Module](https://docs.rakwireless.com/product-categories/wisblock/rak12009/overview/)
- [RAK12015 Vibration Detection Sensor Module](https://docs.rakwireless.com/product-categories/wisblock/rak12015/overview/)
- [RAK13003 IO Expansion Module](https://docs.rakwireless.com/product-categories/wisblock/rak13003/overview/)
- [RAK16000 DC Current Module](https://docs.rakwireless.com/product-categories/wisblock/rak16000/overview/)

### Wireless

- [RAK13300 LPWAN Wireless Module](https://docs.rakwireless.com/product-categories/wisblock/rak13300/overview/)
- [RAK13600 NFC Reader Module](https://docs.rakwireless.com/product-categories/wisblock/rak13600/overview/)

## Example Code

For each module supported by RAK7391 WisBlock slot, there is a Python and Node-RED example script/flow prepared for you to get started with. You can download them from the links attached to each module below.

### Onboard

- TPT29555 GPIO Expander ([Python example](https://github.com/RAKWireless/wisblock-python/tree/master/rak7391/tpt29555))

### Interface

- RAK5801 4-20mA Interface Module ([Python example](https://github.com/RAKWireless/wisblock-python/tree/master/interface/rak5801), [Node-RED flow](https://github.com/RAKWireless/wisblock-node-red/tree/master/interface/rak5801))
- RAK5802 RS485 ModBUS Module ([Python example](https://github.com/RAKWireless/wisblock-python/tree/master/interface/rak5802), [Node-RED flow](https://github.com/RAKWireless/wisblock-node-red/tree/master/interface/rak5802/rak5802_modbus))
- RAK5811 0-5V Interface Module ([Python example](https://github.com/RAKWireless/wisblock-python/tree/master/interface/rak5811), [Node-RED flow](https://github.com/RAKWireless/wisblock-node-red/tree/master/interface/rak5811))
- RAK13001 Relay IO Module ([Python example](https://github.com/RAKWireless/wisblock-python/tree/master/interface/rak13001))
- RAK13004 PWM Expander Module ([Python example](https://github.com/RAKWireless/wisblock-python/tree/master/interface/rak13004), [Node-RED flow](https://github.com/RAKWireless/wisblock-node-red/tree/master/interface/rak13004/rak13004-servo))
- RAK13005 LIN Module ([Python example](https://github.com/RAKWireless/wisblock-python/tree/master/interface/rak13005), [Node-RED flow](https://github.com/RAKWireless/wisblock-node-red/tree/master/interface/rak13005/rak13005-linbus))
- RAK13007 Relay Module ([Python example](https://github.com/RAKWireless/wisblock-python/tree/master/interface/rak13007))
- RAK16001 ADC Module ([Python example](https://github.com/RAKWireless/wisblock-python/tree/master/interface/rak16001), [Node-RED flow](https://github.com/RAKWireless/wisblock-node-red/tree/master/interface/rak16001))
- RAK17000 Motor Control Module ([Python example](https://github.com/RAKWireless/wisblock-python/tree/master/interface/rak17000))

### Sensors

- RAK12004 MQ2 Gas Sensor Module ([Python example](https://github.com/RAKWireless/wisblock-python/tree/master/sensors/rak12004/rak12004-reading), [Node-RED flow](https://github.com/RAKWireless/wisblock-node-red/tree/master/sensors/rak12004/rak12004-reading))
- RAK12006 PIR Sensor Module ([Python example](https://github.com/RAKWireless/wisblock-python/tree/master/sensors/rak12006))
- RAK12009 MQ3 Alcohol Gas Sensor Module ([Python example](https://github.com/RAKWireless/wisblock-python/tree/master/sensors/rak12009/rak12009-reading), [Node-RED flow](https://github.com/RAKWireless/wisblock-node-red/tree/master/sensors/rak12009/rak12009-reading))
- RAK12015 Vibration Detection Sensor Module ([Python example](https://github.com/RAKWireless/wisblock-python/tree/master/sensors/rak12015), [Node-RED flow](https://github.com/RAKWireless/wisblock-node-red/tree/master/sensors/rak12015/rak12015-tampering-detector))
- RAK13003 IO Expansion Module ([Python example](https://github.com/RAKWireless/wisblock-python/tree/master/sensors/rak13003/rak13003-blink), [Node-RED flow using the same chip](https://github.com/RAKWireless/wisblock-node-red/tree/master/display/rak14003-example))
- RAK16000 DC Current Sensor ([Python example](https://github.com/RAKWireless/wisblock-python/tree/master/sensors/rak16000), [Node-RED flow](https://github.com/RAKWireless/wisblock-node-red/tree/master/sensors/rak16000))

### Wireless

- RAK13300 SX1262 LPWAN Module ([Python example](https://github.com/RAKWireless/wisblock-python/tree/master/wireless/rak13300/rak13300-p2p))
- RAK13600 NFC Reader Module ([Python example](https://github.com/RAKWireless/wisblock-python/tree/master/interface/rak13600), [Node-RED flow](https://github.com/RAKWireless/wisblock-node-red/tree/master/wireless/rak13600))

