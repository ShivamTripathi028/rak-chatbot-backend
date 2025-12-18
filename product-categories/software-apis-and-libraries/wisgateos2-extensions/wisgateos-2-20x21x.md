---
title: WisGateOS 2 Manual | Customizable LoRaWAN Gateway Software
description: Explore WisGateOS 2 extensions, customize your LoRaWAN gateway, and enable secure connections with OpenVPN & WireGuard. Tailor your gateway to your needs!
image: "https://images.docs.rakwireless.com/product-logos/wisgateos2-extensions.svg"
keywords:
  - wisgateos 2
  - wisgateos 2 extensions
  - wisgateos 2 user manual
  - rak lora gateway software
  - lorawan gateway software manual
  - lora settings configuration
  - country settings for lorawan
  - lorawan gateway extensions guide
  - wisgateos 2 packet forwarding
  - custom logo extension wisgateos 2
  - failover reboot lorawan
  - openvpn wireguard for gateways
  - wifi ethernet integration wisgateos 2
sidebar_label: WisGateOS 2 2.0.x/2.1.x
date: 2022-04-07
tags:
  - wisgateos 2 extensions
  - wisgateos 2
  - user manual
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# WisGateOS 2 2.0.x/2.1.x

Before installing the extension, obtain the extension file in the `.ipk` format. Gateways running WisGateOS 2 2.0.x/2.1.x support the extensions shown in the table below.

| **Extension Names** |                                                  **Extension Files**                                                   |
|---------------------|:----------------------------------------------------------------------------------------------------------------------:|
| Breathing Light     |  [Download](https://downloads.rakwireless.com/LoRa/WisGateOS2/WisGateOS2-Extensions/wes-breathing-light-1.0.0_b6.ipk)  |
| Custom Logo         |   [Download](https://downloads.rakwireless.com/LoRa/WisGateOS2/WisGateOS2-Extensions/wes-custom-logo-1.0.1_b18.ipk)    |
| Country Settings    | [Download](https://downloads.rakwireless.com/LoRa/WisGateOS2/WisGateOS2-Extensions/wes-country-settings-1.0.0_b28.ipk) |
| Open/Close Port     | [Download](https://downloads.rakwireless.com/LoRa/WisGateOS2/WisGateOS2-Extensions/wes-open-close-port-0.0.1_b11.ipk)  |
| Solar Battery       |  [Download](https://downloads.rakwireless.com/LoRa/WisGateOS2/WisGateOS2-Extensions/wes-solar-battery-1.0.0_b19.ipk)   |
| WireGuard           |    [Download](https://downloads.rakwireless.com/LoRa/WisGateOS2/WisGateOS2-Extensions/wes-wireguard-1.0.1_b46.ipk)     |
| OpenVPN Client      |     [Download](https://downloads.rakwireless.com/LoRa/WisGateOS2/WisGateOS2-Extensions/wes-openvpn-1.0.0_b14.ipk)      |

## How to Add an Extension

1. To install an extension, access the gateway by referring to the <a href="https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/overview/#access-the-wisgateos-2-web-ui" target="_blank">Access the WisGateOS 2 Web UI</a> user manual.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/1.login-page.svg"
  width="100%"
  caption="WisGateOS 2 login page"
/>

2. Once logged in successfully, navigate to the **Extensions** tab (<img src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/2.svg" />).

:::tip NOTE
- You can click on the WisGate logo (<img src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/3.svg"/>) to expand the menu on the left and see the full names of the tabs.
- By default, no extensions are installed.
:::

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/4.extensions-tab.svg"
  width="100%"
  caption="Extensions tab"
/>

3. Proceed with the installation by clicking on the **Add new extension** button or the **install one now** link. This will open the **Add new extension** window.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/5.new-extensions.svg"
  width="100%"
  caption="Add new extension"
/>

4. In the window, either drag and drop the extension file into the **Drop your Extension file here** area, or click the **choose file** link in the form to browse and select the extension file manually.

:::tip NOTE
The extension files are in `.ipk` format, specifically created for the WisGateOS 2 and WisGate Edge hardware platform. A general `.ipk` file for OpenWrt cannot be installed.
:::

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/6.choose-extensions.svg"
  width="100%"
  caption="Choose an Extension"
/>

5. Once the extension file is selected, click **Add extension** to begin the installation. The process may take a few moments to complete.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/7.add-extensions.svg"
  width="100%"
  caption="Add an Extension"
/>

6. When the installation is complete, the WisGateOS will automatically reboot, and you will need to log in again.
7. After logging in, navigate back to the **Extensions** tab. The newly installed extension should now be listed and visible in the interface.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/9.installed-extension.svg"
  width="100%"
  caption="Installed Extension"
/>

8. To install additional extensions, use the **Add new extension** button or manage existing ones by clicking the **Launch** button next to the desired extension.

## How to Remove an Extension

1. Navigate to the **Extensions** tab and click on the **Remove** button of the extension you want to uninstall.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/10.installed.svg"
  width="100%"
  caption="Remove the installed Extension"
/>

2. A pop-up window will appear to verify if you want delete the extension. Click **Remove** and wait for the process to finish.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/11.remove-extension.svg"
  width="100%"
  caption="Confirm the Extension removal"
/>

At this point, the uninstalled extension will no longer appear on the **Extensions** page.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/13.removed-extension.svg"
  width="100%"
  caption="Successful Extension removal"
/>

## How to Use the Extensions

### Breathing Light

The breathing light LED is located on the top cover of the WisGate Edge Lite 2 gateways, making it easy to visually identify the gateway's status. This extension allows you to enable or disable the breathing light, which operates by default with a **slowly blinking blue light**.

:::tip NOTE
The **Breathing Light** extension is available only for the WisGate Edge Lite 2 version 2 gateways.
:::

#### Working Mode

By using the Breathing Light extension, the working mode, frequency, and color of the LED light are now customizable. This extension has two working modes: **All** and **Warning Only**.

- Choosing the **All** mode can:
  - Change the **Normal light** color, that is the light you see when the gateway is working properly.
  - Set the blinking frequency from **slow**, **fast**, and **steady**.
  - Configure the color of the **Warning light**.
    :::tip NOTE
    The colors for the **Normal** and the **Warning** Light should not be the same.
    :::
- If you choose **Warning only** mode:
  - The LED light will only work in case of abnormal activities like internet connection loss.
  - Light's color can be modified, but not its frequency.

#### Install the Breathing Light Extension

To install the extension, follow the steps in [How to Add an Extension](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/#how-to-add-an-extension) section.

#### Configure the Breathing Light Extension

1. To access the **Breathing Light** extension, click **Launch**.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/14.light-extension.svg"
  width="100%"
  caption="Launch the Breathing Light Extension"
/>

2. In the **Configuration** page, configure the mode, color, and blinking frequency of the LED.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/15.light-config.svg"
  width="100%"
  caption="Configuration Page"
/>

- **Interface**
  * **Enable Breathing Light**: Enables or disables the breathing light extension.
  * **Mode**: Sets the mode of the extension.
    * **All**: The **Normal light** is enabled.
    * **Warning only**: Disables the **Normal light** settings and only **Warning light** will glow.
- **Normal light**: The settings for the normal light.
  * **Color**: The color of the light (red, green, blue).
  * **Frequency**: Blink frequency of the led (slow, fast, steady).
  :::tip NOTE
  The **Normal light** settings are disabled if **Warning only** mode is selected.
  :::
- **Warning Light**: The color of the warning light.

3. Once done with the configuration, click **Save changes**. You can check the status of the LED on the gateway itself.

### Custom Logo

The Custom Logo extension allows you to upload your logo in the Web UI. This extension is universally compatible with all gateways running WisGateOS 2. It was developed with both small or bigger enterprises in mind, allowing them to have their logo recognized and used in their daily operations.

:::info
Having the capability to rebrand your Web UI is essential for companies that need to effectively promote and visualize their brand or product. This necessity is met by RAKWireless' white label feature, which allows clients to customize the user interface to reflect their branding elements seamlessly.
:::

#### Size and Format Requirements

The uploaded logo image must be in `.svg` format and cannot exceed 300&nbsp;kb. You can preview the **Web UI** page before finally switching RAKWireless' logo with your brand logo.

#### Install the Custom Logo Extension

To install the extension, follow the steps in [How to Add an Extension](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/#how-to-add-an-extension) section.

#### Configure the Custom Logo Extension

1. To access the Custom Logo extension, click **Launch**.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/16.custom-logo.svg"
  width="100%"
  caption="Launch the Custom Logo Extension"
/>

2. In the **Configuration** page, you can set a custom logo on the login page and on the sidebar menu.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/17.config-page.svg"
  width="100%"
  caption="Configuration Page"
/>

   - **Interface**: Enables/disables custom logo extension.
   - **Large logo**: This logo will be used on the login page and the expanded sidebar menu. Upload a logo by dragging and dropping it, or by clicking **Choose File** to browse manually.
   - **Small logo**: This logo will be used for mobile view and the collapsed sidebar menu. Upload the logo by dragging and dropping it, or by clicking **Choose File** to browse manually.
   - **Preview**: After selecting the images, click **Preview** to see how the logo appears on the login page and sidebars in both desktop and mobile views.


<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/19.logo-preview.svg"
  width="100%"
  caption="Logo Preview for Desktop Users"
/>

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/20.mobile-users.svg"
  width="100%"
  caption="Logo Preview for Mobile Users"
/>

3. To apply the selected logos, click **Save changes**. The page reloads automatically, applying the selected logos.

### Country Settings

LBT (Listen Before Talk) means that, before transmitting, the gateway checks the availability of the channel. This is necessary because LoRaWAN is a multi-channel protocol and uses ISM Band. Anyone can use the band, so a collision occurs if two or more end devices send signals simultaneously.

The gateway checks for empty channels and uses one of them to send downlink data. If a channel is occupied, the gateway performs a random back off. In case all of the channels are occupied, the gateway waits for a free channel and tries to send the downlink data again.

LBT is usually governed by regulations per country. In WisGateOS 2 2.x, there is a country table which includes proper configurations for all countries so you can set the country code in WisGateOS 2 2.x.

:::tip NOTE
AS923 end-devices operating in Japan shall perform Listen Before Talk (LBT), based on ARIB STD-T108 regulations. The ARIB STD-T108 regulation is available for free and should be consulted as needed.
:::


You can switch the frequency plan in the following regions:

* AS923, KR920
* EU868, RU864, IN865
* CN470

The frequency plan will be limited to a particular region. Tx power will be limited to under the maximum.

* Downlink Tx Power
* Beacon Tx Power


#### Install the Country Settings Extension

To install the extension, follow the steps in [How to Add an Extension](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/#how-to-add-an-extension) section.

#### Configure the Country Settings Extension


1. To access the Country Settings extension, click **Launch**.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/1.extensions-tab.svg"
  width="100%"
  caption="Launch the Country Settings/LBT Extension"
/>

2. In the **Configuration** page, click the **Select your Country** button to set your country.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/2.country-selection.svg"
  width="100%"
  caption="Country selection"
/>

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/3.country-list.svg"
  width="100%"
  caption="Find your country in the list"
/>

3. In the new window, find your country and select it. Tick the checkbox below to confirm that you have chosen the country where the gateway is located. Then click **Confirm** to set the LBT for your country.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/4.confirm-country.svg"
  width="100%"
  caption="Confirm your country"
/>

4. Enable the LBT by clicking on the **Enable Listen Before Talk** switch.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/5.enable-lbt.svg"
  width="100%"
  caption="Enable LBT"
/>

5. Click **Save changes** to apply the configuration. LBT is now enabled on your gateway.



### Open/Close Port

This extension allows you to add or delete packet traffic management rules on the gateway, allowing any (or specific) host IP from a designated subnet to communicate with the gateway through specified ports.

#### Install the Open/Close Port Extension

To install the extension, follow the steps in [How to Add an Extension](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/#how-to-add-an-extension) section.

#### Configure the Open/Close Port Extension

1. To access the Open/Close Port extension, click **Launch**.


<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/1.extension-tab.svg"
  width="100%"
  caption="Launch the Open/Close Port Extension"
/>

After clicking **Launch**, the **Traffic rules** page will be displayed, showing the default rules of the **Open/Close port** extension with the following parameters:

* **Service name**: A readable name for the service.
* **Protocol**: The protocol used.
* **Family**: The protocol version used for the traffic.
* **From**: External source
* **To**: Internal source

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/v22x-open-close-extension.svg"
  width="100%"
  caption="Traffic rules page"
/>

For example, the **Allow-http** service indicates that any host in WAN can communicate with the gateway through port 80 using the TCP protocol type.

2. To add a new rule, click the **Add new rule** and configure the following information:
* **Service name**: Provide a readable name for the rule.
* **Protocol**: Select the protocol used for the rule:
  * TCP
  * UDP
  * TCP + UDP
* **Sources**:
  * **Allow any host**: Allows any host to access the rule.
  * **Source IP address**: Specify up to three host IPs.
* **Destination port**: The destination port for routing.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/v22x-new-rule.svg"
  width="100%"
  caption="Add a new rule"
/>


3. To save the changes, click **Add new rule**. The newly created rule will then appear in the **Traffic rules** interface.

### Solar Battery

The Solar Battery extension is used to display the operational status information of the solar battery used by the gateway. This includes information on the performance of the solar battery, battery health status, cycle period, battery capacity, charging and discharging modes, and more.

This extension is compatible with the following gateways:

+ **RAK7240V2**
+ **RAK7267**
+ **RAK7289V2**
+ **RAK7285**

You can learn the status of the solar battery in real-time through the UI interface.

#### Install the Solar Battery Extension

To install the extension, follow the steps in [How to Add an Extension](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/#how-to-add-an-extension) section.

#### Enable and View Solar Battery Monitoring

1. To access the Solar Battery extension, click **Launch**.


<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/solar-battery-extensions-tab.svg"
  width="100%"
  caption="Launch the Solar Battery Extension"
/>

After clicking **Launch**, the **Details** page will be displayed, showing information about the Solar Battery:

* **Solar battery performance**: Shows the real-time performance of the battery.
  * **Temperature**: The temperature of the battery. Used to prevent overheating or freezing.
  * **Voltage**: The voltage level of the battery.
  * **State of charge**: The current battery level.
  * **Current**: Indicates whether the battery is charging or discharging.

* **About solar battery**: Contains additional information about the battery.
  * **State of Health**: Represents the battery's overall condition.
  * **Cycle times**: The number of charge/recharge cycles.
  * **Remaining Capacity**: The current available capacity of the battery.
  * **Full-charge capacity**: The maximum capacity when the battery is fully charged.
  * **Battery working mode**: Indicates whether the battery is charging or discharging.

* **Solar battery active events**: Notifies users about battery-related issues.
  * **FAULT**: The system detects a potentially damaged battery and recommends immediate replacement.
  * **PROTECT**: The system detects a serious issue and shuts down the battery as a protective measure. Once conditions are safe, the battery resumes operation automatically.

2. Enable the switch to activate **Monitor solar battery**.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/2.solar-battery-page.svg"
  width="100%"
  caption="Details page"
/>


### WireGuard

WireGuard is a simple but fast VPN. It aims to be faster, simpler, and leaner than the IPsec protocol. It intends to be more performant than the well-known RAKwireless - OpenVPN. Before, it was not possible to use the WireGuard protocol on the RAKwireless gateways, but that is not the case now.

The new WisGateOS 2 now offers Extension features, where you can install and set up the WireGuard extension. In this tutorial, you will learn how to set the WireGuard client on the gateway.

This guide assumes that you have some knowledge in setting up a WireGuard server and have a WireGuard server set up.

#### Install the WireGuard Extension

To install the extension, follow the steps in [How to Add an Extension](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/#how-to-add-an-extension) section.

#### Configure the WireGuard Extension

1. To access the WireGuard extension, click **Launch**.


<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/wireguard-extensions-tab.svg"
  width="100%"
  caption="Launch the WireGuard Extension"
/>

2. In the **Configuration** page, enable the **Enable WireGuard** switch and configure the following information:
* **Interface**: Settings for the WireGuard client.
  * **Address with netmask**: The address used by the WireGuard client. It must be in the same range (e.g., `10.0.8.0` to `10.0.8.255`) defined by the server.
  * **Generate key pair**: Automatically generates the key pair.
  * **Public key**: The public key of the WireGuard client.
  * **Private key**: The private key of the WireGuard client.
    :::tip NOTE
    Do not share your private key with anyone.
    :::

* **Server**: Settings for the WireGuard server.
  * **Endpoint Host**: The IP address of the machine or cloud service where the WireGuard server is hosted.
  * **Endpoint Port**: The port used for WireGuard traffic.
  * **Persistent Keepalive (ms)**: The interval at which keepalive packets are sent to maintain the connection.
  * **Public Key**: The public key of the WireGuard server.
  * **Enable Preshared Key**: Enables the preshared key field. This key is used as part of the Noise protocol during encrypted connection setup between the two peers.
      <RkImage
        src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/3.preshared-key.svg"
        width="50%"
        caption="Enable preshared key"
      />
* **Route All Traffic**: Allows traffic from all IPs.
  * **Allowed IPs**: Specifies the IPs that are allowed to connect to the gateway via the WireGuard IP. This option is only available when **Route All Traffic** is disabled.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/2.enable-wireguard.svg"
  width="100%"
  caption="Configuration page"
/>

3. To save the changes, click **Save changes**.
:::tip NOTE
Remember to add the WireGuard Client credentials to the WireGuard server configuration.
:::

4. After the connection is established, open the **Status** tab to view the WireGuard connection.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/4.wireguard-status.svg"
  width="60%"
  caption="WireGuard status"
/>

### OpenVPN Client

OpenVPN (Open Virtual Private Network) is a type of VPN in which a server is deployed to allow both the Gateway and multiple client devices, such as PCs, phones, and other endpoints, to connect via a public IP address. This setup can be implemented using any backhaul connectivity supported by the gateway, including Ethernet, Wi-Fi, or LTE. When using LTE as the backhaul, make sure that the gateway has a static public IP address.

By connecting to the OpenVPN server from a remote client, the gateway can be securely managed from anywhere, at any time. As mentioned above, an OpenVPN server is required. Detailed instructions for deploying a server in the AWS cloud can be found in the <a href="https://learn.rakwireless.com/hc/en-us/articles/26527371792535-How-To-Configure-WisGate-Edge-V2-Gateways-Remote-Management-OpenVPN#deploy-the-openvpn-server" target="_blank">How to Configure WisGate Edge v2 Gateways Remote Management - OpenVPN</a> guide.

#### Install the OpenVPN Client Extension

To install the extension, follow the steps in [How to Add an Extension](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2-extensions/wisgateos-2-20x21x/#how-to-add-an-extension) section.

#### Configure the OpenVPN Client Extension

Make sure you have local network access to your gateway and connect to it to access the Web UI.

1. To access the OpenVPN Client extension, click **Launch**.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/1-start-openvpn.svg"
  width="100%"
  caption="Launch the OpenVPN Client Extension"
/>

2. Add an OpenVPN tunnel by clicking the **Add tunnel** button or the **add one now** link.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/2-add-openvpn-tunnel.svg"
  width="100%"
  caption="Add OpenVPN tunnel"
/>

3. Click the **choose file** link and browse for the `.ovpn` file or drag and drop the `.ovpn` file you created by following the <a href="https://learn.rakwireless.com/hc/en-us/articles/26527371792535-How-To-Configure-WisGate-Edge-V2-Gateways-Remote-Management-OpenVPN" target="_blank">How to Configure WisGate Edge v2 Gateways Remote Management - OpenVPN</a> guide.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/3-add-.ovpn-file-to-the-gateway.svg"
  width="100%"
  caption="Add .ovpn file to the gateway"
/>

4. Once the file is added, click **Add tunnel** to add the OpenVPN tunnel.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/4-add-openvpn-tunnel.svg"
  width="100%"
  caption="Add OpenVPN tunnel"
/>

When the tunnel is added successfully, a confirmation message will appear at the bottom of the screen.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/5-successfully-added-tunnel.svg"
  width="100%"
  caption="Successfully added tunnel"
/>

5. Click the **Configure** button of the VPN tunnel. On the next window, toggle the **Enable Connection** switch to enable the OpenVPN tunnel and click **Save changes**.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/6-start-the-openvpn-tunnel.svg"
  width="100%"
  caption="Start the OpenVPN tunnel"
/>

:::tip NOTE
- Once the configurations are set, you can check the OpenVPN status under the **Logs** tab.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/7-openvpn-tunnel-status.svg"
  width="100%"
  caption="OpenVPN tunnel status"
/>

- You can also view the assigned IP on the **OpenVPN Overview** page.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2-extensions/wisgateos-2-20x21x/8-openvpn-assigned-ip.svg"
  width="100%"
  caption="OpenVPN assigned IP"
/>
:::

<RkBottomNav/>
