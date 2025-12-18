---
title: Environment Test Report
description: Displays the RAK7243 test requirements and results in different temperature work and storage scenarios. This ensures that your LoRaWAN Gateway can operate efficiently in various conditions.
keywords:
- RAK7243
- Environment Test Report
- wisgate
image: https://images.docs.rakwireless.com/wisgate/rak7243/quickstart/1.main/RAK7243.png
sidebar_label: Test Report
---

    

# Environment Test Report

## Product Information

| Sample name     | Model                                            | Quantity |
| --------------- | ------------------------------------------------ | -------- |
| LoRaWAN gateway | RAK7243 (Raspberry Pi 3B+ + LTE + RAK2245 EU868) | 1        |

## Test Project

| No. | Test item                     | Temperature conditions |
| --- | ----------------------------- | ---------------------- |
| 1   | Low-temperature storage test  | -40 ℃                  |
| 2   | Low-temperature work test     | -40 ℃                  |
| 3   | High-temperature storage test | 85 ℃                   |
| 4   | High-temperature work test    | 85 ℃                   |

## Test Equipment

| Test equipment                   | Model                                           | Quantity |
| -------------------------------- | ----------------------------------------------- | -------- |
| Multi-channel temperature tester | WD-08A                                          | 1        |
| Environmental test chamber       | Mini BTC 03                                     | 1        |
| Equipment being tested           | RAK7243 (Raspberry Pi3B+ + LTE + RAK2245 EU868) | 1        |
| LoRa Nodes                       | RAK5205                                         | 7        |

## Pictures of the Test Equipment

> **Image:** Multi-channel temperature tester

> **Image:** RAK7243

> **Image:** Environmental test chamber

> **Image:** LoRa nodes

## Test requirements

- Low-temperature storage test:

Place the DUT in the temperature chamber and set the low temperature to -40º C. The DUT can power up and login via SSH when all temperature monitoring points reach -40℃.

- Low-temperature work test:

a. When all test points reach -40º C, The DUT can power up and login via SSH.

b. It can connect to the cloud server to send and receive LoRa packets.

c. The LAN port and Wi-Fi work well.

- High-temperature storage test:

Place the DUT in the temperature chamber and set the high temperature to 85º C. The DUT can power up and login via SSH when all temperature monitoring points reach 85º C.

- High-temperature work test:

a. When all test points reach 85º C, The DUT can power up and login via SSH.

b. It can connect to the cloud server to send and receive LoRa packets.

c. The LAN port and Wi-Fi work well.

- Temperature monitoring points of RAK7243:

| Chains | Monitoring point                                           | Color  | Max temperature |
| ------ | ---------------------------------------------------------- | ------ | --------------- |
| ch1    | Raspberry Pi 3B+' CPU                                      | RED    | 106.7º C        |
| ch2    | Raspberry Pi 3B+' power chip                               | YELLOW | 107º C          |
| ch3    | Raspberry Pi 3B+' Wi-Fi module                             | BLUE   | 104.1º C        |
| ch4    | Raspberry Pi 3B+' PHY chip                                 | PURPLE | 106.5º C        |
| ch5    | RAK2013 LTE module                                         | CYAN   | 101º C          |
| ch6    | Heat dissipation aluminum of RAK2245                       | GREEN  | 100.9º C        |
| ch7    | The internal temperature of the environmental test chamber | WHITE  | 85.6º C         |

> **Image:** Temperature monitoring points

## Test Results

| Test project             | Test result                                                               | Conclusion |
| ------------------------ | ------------------------------------------------------------------------- | ---------- |
| Low-temperature storage  | The DUT can power up and login via SSH.                                   | PASS       |
| Low-temperature work     | Can send and receive LoRa packets normally and the Wi-Fi also works well. | PASS       |
| High-temperature storage | The DUT can power up and login via SSH.                                   | PASS       |
| High-temperature work    | Can send and receive LoRa packets normally and the Wi-Fi also works well. | PASS       |

> **Image:** Send and receive LoRa packets at -40º C

> **Image:** Send and receive packets at 85º C

> **Image:** Wi-Fi works well at -40º C

> **Image:** Wi-Fi works well at 85º C

## Test Date and Location

| Item           | Information                                                               |
| -------------- | ------------------------------------------------------------------------- |
| Test date:     | 19 November 2019                                                          |
| Test location: | Room 307, building 3, Guofeng Meitang building, Huilongguan town, Beijing |
| Prepared by:   | Hairui Tao                                                                |
| Approved by:   | Ken Yu                                                                    |
