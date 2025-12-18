---
slug: /product-categories/wisgate/rak7271-rak7371/quickstart/
title: RAK7271/RAK7371 WisGate Developer Base Guide
description: Step-by-step instructions to set up and deploy the RAK7271/RAK7371 WisGate Developer Base, including hardware connections, software installation, and integration with Raspberry Pi or Linux systems.
image: "https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/rak7271-rak7371.png"
keywords:
    - RAK7271 guides
    - RAK7371 guides
    - WisGate Developer Base
    - LoRaWAN gateway
    - Raspberry Pi integration
    - mPCIe LoRa concentrator
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# RAK7271/RAK7371 Quick Start Guide

## Prerequisites

### Hardware

Before proceeding with the installation guide for the RAK7271/7371 WisGate Developer Base, ensure you have prepared the necessary items listed below.:

1. [WisGate Developer Base RAK7271 or RAK7371](https://store.rakwireless.com/products/wisgate-developer-base?utm_source=wisgatedeveloperbase&utm_medium=Document&utm_campaign=BuyFromStore)
2. A Host - Linux running PC/laptop or Raspberry Pi

:::warning
The SIM card slot of the cellular versions is not hot-swappable. Make sure the gateway is switched off before inserting or ejecting the SIM card.
:::

### Package Inclusion

1. 1pc WisGate Developer Base
2. 1pc USB Type C to A Cable
3. 1pc LoRa Antenna

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/1.package-content.png"
  width="60%"
  caption="Package Content"
/>


## Product Configuration

### Raspberry Pi as a Host

#### Interface Between the Raspberry Pi and the WisGate Developer Base

:::tip NOTE

It is assumed that your Raspberry Pi has already been installed with an [OS](https://www.raspberrypi.org/software/operating-systems) and has internet access. You must also have an access to it over SSH or directly to the command line interface (CLI).
:::

1. Connect the WisGate Developer Base using the included cable: insert the Type-C end into the Developer Base and the Type-A end into one of the Raspberry Pi's USB ports.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/2.connecting-to-raspberry-pi.png"
  width="50%"
  caption="Connect the WisGate Developer Base to the Raspberry Pi"
/>

2. After connecting the Developer Base to the Pi, the Power Led will be steady green. This means that the Base is properly powered.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/3.power-on.png"
  width="30%"
  caption="Power On the Developer Base"
/>

3. Check if the base is properly connected by running this command on the CLI:

```
lsusb
```

4. In the output, you should see a **STMicroelectronics Virtual COM Port** line. This means your RAK WisGate Developer Base is properly connoted to the Raspberry Pi.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/4.checking-connection.png"
  width="60%"
  caption="Check the Connection"
/>


```
pi@raspberrypi:~ $ lsusb
Bus 001 Device 005: ID 0483:5740 STMicroelectronics Virtual COM Port
Bus 001 Device 004: ID 0424:7800 Standard Microsystems Corp.
Bus 001 Device 003: ID 0424:2514 Standard Microsystems Corp. USB 2.0 Hub
Bus 001 Device 002: ID 0424:2514 Standard Microsystems Corp. USB 2.0 Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
pi@raspberrypi:~ $

```

### Install the Software

To use the Base, you must install and configure the necessary software.

1. To download the software, execute the following commands in the CLI:

- This command will check for the latest updates of the OS and download the Git tool that will allow downloading the software:

```
sudo apt update; sudo apt install git -y
```

* Download the required software.

```
git clone https://github.com/RAKWireless/rak_common_for_gateway.git
```

2. Enter the created directory.

```
cd ~/rak_common_for_gateway
```

3. Start the installation.

```
sudo ./install.sh
```

4. You will be prompted to select the model of the concentrator you are installing.

- Select ***9. RAK2287 USB*** if you are using the WisGate Developer Base **RAK7271**.
- Choose ***10. RAK5146 USB*** if you are using the WisGate Developer Base **RAK7371**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/5.selecting-concentrator-model.png"
  width="50%"
  caption="Select the Concentrator Model"
/>

:::tip NOTE

The script will also install ChirpStack, an open-source LoRaWAN Network Server stack. It enables you to set up a fully functional LoRaWAN Server locally on the Raspberry Pi.

:::

If you prefer not to install ChirpStack, run the installation script with the following parameter.:

```
sudo ./install.sh --chirpstack=not_install
```

5. After a few minutes, the installation will be completed.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/6.successful-installation.png"
  width="60%"
  caption="Successful Installation"
/>


```
Copy sys_config file success!
/home/pi/rak_common_for_gateway
***********************************************************
*   The RAKwireless gateway is successfully installed!    *
***********************************************************
pi@raspberrypi:~/rak_common_for_gateway $

```

### Linux Machine as a Host

#### Interface Between the Linux Machine and the WisGate Developer Base

Connect the two devices using the included USB cable to the host PC. It is recommended to use **Ubuntu 18.04 LTS** as the operating system.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/7.base-to-host.png"
  width="60%"
  caption="Connect the WisGate Developer Base to the Host"
/>

#### Software Installation

To use the Base, you need to install and configure the required software. The procedure varies slightly between the two variants of the WisGate Developer Base.

##### For RAK7271 WisGate Developer Base with RAK2287 Inside

1. Install the required **make** and **gcc** tools.

```
sudo apt install make
```

```
sudo apt install gcc
```

2. Download the archive from the Semtech repository:

```
wget https://github.com/Lora-net/sx1302_hal/archive/V2.0.1.tar.gz
```

3. After the download is complete, extract the files with the command:

```
tar -zxvf V2.0.1.tar.gz
```

4. Enter the created folder.

```
cd sx1302_hal-2.0.1
```

5. Run the **make** command to compile the software.

```
sudo make
```

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/8.install-software.png"
  width="80%"
  caption="Install the Software"
/>

After the compilation is complete, configure the correct channel plan by setting the appropriate `global_conf.json` file for the packet forwarder.

6. Navigate to the Packet forwarder folder.

   ```
   cd packet_forwarder
   ```

7. Then list the files and folders:

   ```
   ls -l
   ```

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/9.listing-the-content.png"
  width="80%"
  caption="List the Content of the Folder"
/>

8. You can see that there is a different example configuration files for different LoRaWAN bands and different types of concentrators. In this setup, you are using RAK Developer Base, which is the USB, and the EU868 band. Run this command to rename the correct file to `global_conf.json`:

```
 cp global_conf.json.sx1250.EU868.USB global_conf.json
```

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/10.after-renaming.png"
  width="80%"
  caption="List the Content of the Folder After Renaming"
/>

9. Start the packet forwarder process to bridge the LoRaWAN radio component with the Network Server.

```
sudo ./lora_pkt_fwd
```

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/11.starting-packet-forwarder.png"
  width="80%"
  caption="Start the Packet Forwarder"
/>

10. At the end of this example, you can see the concentrator's EUI. Save it somewhere as it will be needed to register your gateway in the Network Server later.

You can also retrieve the EUI using the `chip_id` tool located in the `util_chip_id` folder. Navigate to the folder and execute the following command:

```
sudo ./chip_id -u -d /dev/ttyACM0
```

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/12.concentrator-eui.png"
  width="80%"
  caption="Concentrator EUI"
/>


##### For RAK7371 WisGate Developer Base with RAK5146 Inside

1. Install the required **make** and **gcc** tools.

```
sudo apt install make
```

```
sudo apt install gcc
```

2. Clone the software from the Git reposiory:

```
sudo git clone https://github.com/Lora-net/sx1302_hal.git
```

3. After the download is complete, navigate to the newly created folder.

```
cd sx1302_hal
```

4. Run the **make** command to compile the software.

```
sudo make
```

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/13.install-software.png"
  width="80%"
  caption="Install the Software"
/>

5. Open the Packet forwarder folder with the following command:

```
cd packet_forwarder
```

6. And then list the files and folders.

```
ls -l
```

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/14.listing-the-content.png"
  width="80%"
  caption="List the Content of the Folder"
/>

7. You will find different example configuration files for various LoRaWAN bands and concentrator types. For this setup, you are using the RAK Developer Base (USB) with the EU868 band. Run the following command to rename the appropriate file to `global_conf.json`.

```
 cp global_conf.json.sx1250.EU868.USB global_conf.json
```


<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/15.after-renaming.png"
  width="80%"
  caption="List the Content of the Folder After Renaming"
/>

8. Start the packet forwarder process to bridge the LoRaWAN radio component with the Network Server.

```
sudo ./lora_pkt_fwd
```

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/16.starting-packet-forwarder.png"
  width="80%"
  caption="Start the Packet Forwarder"
/>

9. At this stage, you can view the concentrator's EUI. Be sure to save it, as it will be required to register your gateway in the Network Server later.

You can also retrieve the EUI using the `chip_id` tool located in the `util_chip_id` folder. Navigate to the folder and execute the following command:

```
sudo ./chip_id -u -d /dev/ttyACM0
```

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/17.concentrator-eui.png"
  width="80%"
  caption="Concentrator EUI"
/>



#### Connect to The Things Network V3 (TTNv3)

##### Using Raspberry Pi as a Host

Connecting to TTN is straightforward using the RAKwireless scripts.

1. Open the configuration tool by running the command in the Raspberry Pi CLI.

```
sudo gateway-config
```

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/18.configuration-tool.png"
  width="60%"
  caption="Open the Configuration Tool"
/>

2. Select the option **2 Setup RAK Gateway Channel Plan**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/19.selection.png"
  width="60%"
  caption="Make a Selection"
/>

3. On the next window, choose the option **1 Server is TTN**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/20.server.png"
  width="60%"
  caption="Select the Server"
/>

4. Select the correct band.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/21.channel.png"
  width="60%"
  caption="Select the Channel Plan"
/>

5. Select option **4 Edit packet-forwarder config**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/22.configuration-options.png"
  width="60%"
  caption="Configuration Options"
/>

6. Based on your location, set the appropriate TTN address for the packet forwarder. The configuration file will open for editing.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/23.file-content.png"
  width="80%"
  caption="File Content Configuration "
/>

7. Find the **"gateway_conf"** section:

```
  "gateway_conf": {
        "gateway_ID": "AA555A0000000000",
        /* change with default server address/ports */
        "server_address": "router.eu.thethings.network",
        "serv_port_up": 1700,
        "serv_port_down": 1700,
```

8.  In the configuration file, update the **"server_address"** line to the appropriate TTN URL. For example, the URL for Europe is:

```
  eu1.cloud.thethings.network
```

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/24.server-address.png"
  width="60%"
  caption="Change the server address"
/>

9. To save the changes, press **Ctrl+X** and then confirm by pressing **Y**.

10.  Restart the packet forwarder by choosing the **Option 3**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/25.restart.png"
  width="60%"
  caption="Restart the Packet Forwarder"
/>

11. Quit to exit from the configuration menu.

Now, you have a fully working gateway that is configured to use TTN as Network Server.

12. To register the gateway with TTN, you will need its EUI. Use the following command in the CLI to retrieve the EUI:

```
sudo gateway-version
```

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/26.gateway-eui.png"
  width="80%"
  caption="Get the Gateway's EUI"
/>

```
pi@rak-gateway:~ $ sudo gateway-version
Raspberry Pi 3 Model B Plus Rev 1.3, OS "10 (buster)", 5.10.17-v7+.
RAKwireless gateway RAK2287 for USB version 4.2..7R install from source code.
Gateway ID: B827EBFFFE7AFF6A.
pi@rak-gateway:~ $
```

13. Open the TTN website in your browser, login, and navigate to the console page. Click on **+Add Gateway button**.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/27.add-gateway.png"
  width="100%"
  caption="Add the Gateway"
/>

14. Enter the EUI along with the required details such as description and channel plan. If you have followed the steps correctly, your gateway will appear as connected and show activity.

<RkImage
  src="https://images.docs.rakwireless.com/wisgate/rak7271-rak7371/quickstart/28.register-gateway.png"
  width="100%"
  caption="Registered Gateway"
/>


<RkBottomNav/>