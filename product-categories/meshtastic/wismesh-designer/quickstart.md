---
title: Meshtastic Designer Quick Start Guide
description: Contains instructions and tutorials for using the Meshtastic Designer.
image: "https://images.docs.rakwireless.com/meshtastic/designer/designer-logo.png"
keywords:
  - RAK4631
  - wisblock
  - Meshtastic
  - Nordic
  - nRF52840
  - Semtech
  - SX1262
sidebar_label: Quick Start Guide
---

import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'

# Meshtastic Designer Quick Start Guide

While exploring the needs of customers looking for Meshtastic devices, it became apparent that selecting the correct modules to build a specific Meshtastic device is often difficult.

With the Meshtastic Designer, the goal is to make this first and important step of selecting WisBlock modules easier.

Whether you are experienced with Meshtastic and WisBlock modules or a newbie, the Meshtastic Designer helps to:

- Select the sensor or/and IO modules
- Select the Base Board
- Select the MCU and LoRa frequency

To get started, open the <a href="https://meshtastic-designer.rakwireless.com" target="_blank">Meshtastic Designer</a> and click the _**Start**_ button.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/01-start-page.png"
  width="100%"
  caption="Start Page"
/>

:::tip NOTE
- On the first click of the _**Start**_ button, it might ask you to accept the cookies.
- The _**Login**_ button is for a future feature, where you can login with your RAK-ID and save your configurations for later reuse.
:::


## Left Side Menu

Before proceeding to the next steps, this section explains the functions of the left-side menu. You can select different categories of modules or enclosures, and the right-side menu will update with the corresponding options.

In addition to displaying the module categories, it also has buttons with the following functions:<br/>
1. Clear the selected device role, and goes back to the beginning.<br/>
2. Removes all modules.<br/>
3. Removes a specific module or all modules within a category.<br/>
4. Checkout and place an order for the Meshtastic device from the RAKwireless online store.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/20-left-side-functions.png"
  width="50%"
  caption="Left side menu"
/>


## Choose Between Expert or Guided Setup Option

- If you're already familiar with Meshtastic and WisBlock Modules, you can select _**Skip**_ on the pop-up screen to set everything up manually. You can find some helpful tips in the [**Expert Mode**](#expert-mode) guide below.
- However, you can go through the **Guided Setup Mode**, which automatically selects the required modules and suggests the correct placement for them on the WisBlock Base Boards.


### Guided Setup Mode

#### Select the Desired Functions

On the pop-up screen, you can see different sensors and other functions that are supported by Meshtastic and WisBlock modules.

1. Select the functions you want to use in your Meshtastic device.
  - In this example, the modules for a Meshtastic Client with location tracking capability, a temperature and humidity sensor, and an OLED display are being selected.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/02-select-functions.png"
  width="100%"
  caption="Device functions"
/>

2. After select the functions, press on _**Next**_.

#### Select a Country (Frequency Band)

Meshtastic uses LoRa transmission technology for communication, with different regions and countries operating on various frequencies for LoRa communications.

To make it easier to choose, a country selector with the correct frequency has been provided for the Meshtastic device. Currently, the WisBlock Core modules for Meshtastic only support the 9xx&nbsp;MHz and 8xx&nbsp;MHz frequency bands.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/03-frequency-selector.png"
  width="100%"
  caption="Regions"
/>

:::tip NOTE
- In some countries, multiple frequency ranges can be used. In such a case, select the frequency you want to use.
- For a faster selection, you can type the country name in the selector input box. It will show you automatically a list with matching countries.
:::

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/04-frequency-selector-by-country.png"
  width="75%"
  caption="Regions by country name"
/>

Click on _**Configure**_ to see the initial configuration for your Meshtastic Device.


#### Configured Meshtastic Device

You will now see the configured device with all modules placed in their respective module slots. Potential conflicts between different modules are already taken into account and the modules are placed in the correct module slots.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/05-preselected-device.png"
  width="100%"
  caption="Meshtastic device with selected modules"
/>

#### Add More Modules (Guided Setup Mode)

This section explains the **Guided Setup Mode** for selecting and adding modules to the device. For example, an acceleration sensor can detect device movements and update location information.

Follow the steps below to add more modules:

1. Scroll down on the left-side menu and look for _**WisBlock Sensor**_, then click on it.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/06-left-side-menu-sensors.png"
  width="50%"
  caption="Select WisBlock Sensors to add more sensors"
/>

The right-side menu will now display the available sensor modules.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/07-right-side-menu-sensor-slot-b.png"
  width="50%"
  caption="Updated right-side menu"
/>

The 3-Axis Acceleration Sensor is in the list but is greyed out because it is incompatible with sensor Slot B.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/08-why-sensor-cannot-be-used.png"
  width="100%"
  caption="Explanation why the module cannot be used"
/>

:::tip NOTE
Greyed-out modules in the list indicate incompatibility. To see the reason, hover the mouse over the sensor, and an explanation will appear. You will also see which slots the module is compatible with. In this case, Slot C is recommended.
:::

3. Select Slot C from the top of the right-side menu, and the 3-Axis Acceleration Sensor will become selectable.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/09-change-slot-to-compatible.png"
  width="50%"
  caption="Change Slot"
/>

4. Select the sensor module and it will be placed in Sensor Slot C.

5. After you selected the module, turn the 3D model around and you can see the sensor placed in Slot C.

In addition, the 3-Axis Acceleration Sensor is now showing in the used module list in the right-side menu.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/10-rak1904-added.png"
  width="100%"
  caption="3-Axis sensor added"
/>

#### Add an Enclosure

:::tip NOTE
At the time this guide was written, enclosures supporting the OLED display were still unavailable from RAKwireless. However, the steps to add an enclosure and mounting plate are still provided here.
:::

Follow the steps below to add an enclosure:

1. Scroll down the left-side menu to the _**Enclosure**_ category and click on it to refresh the right-side menu with enclosure options.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/11-select-enclosure-category.png"
  width="50%"
  caption="Select Enclosures"
/>

2. On the right-side menu, select an enclosure and mounting plates listed.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/12-enclosures-mounting-plates.png"
  width="50%"
  caption="Enclosures and mounting plates"
/>

To avoid external antennas, the Unify WisBlock Mounting Plate with an integrated antenna is an ideal solution. Since Germany was selected as the region, only the mounting plate with an antenna for the 863-870&nbsp;MHz frequencies is selectable.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/13-mounting-plate.png"
  width="50%"
  caption="Mounting plate with integrated antenna for EU868"
/>

:::tip NOTE
It is also possible to choose another mounting plate without an integrated antenna. These mounting plates come with pre-installed stand-offs for the different WisBlock Base Boards.
:::

3. After selecting the mounting plate, it will appear in the 3D view. This also serves as a guide for how the Base Board should be mounted on the plate.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/14-device-on-mounting-plate.png"
  width="100%"
  caption="Device on the mounting plate"
/>

Now going back to the right-side menu, you can see that only one enclosure is left to be selected. This is because the mounting plate with integrated antennas is only compatible with the Unify Enclosure 100&nbsp;mm x 75&nbsp;mm x 38&nbsp;mm.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/15-select-enclosure.png"
  width="50%"
  caption="Matching enclosures"
/>

4. Click on the enclosure to show the device inside.

5. To open the lid, click the _**Enclosure Lid Open**_ button at the bottom of the screen.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/16-open-lid.png"
  width="50%"
  caption="Open the enclosure lid"
/>

Now you can see your Meshtastic Device inside the enclosure.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/17-device-in-enclosure.png"
  width="100%"
  caption="Device inside the enclosure"
/>

6. Proceed to the [Checkout](#checkout) to order your device.

### Expert Mode

#### Select a Base Board

1. Select a Base Board that matches with the required sensor and IO slots.

2. Click on the left-side menu on _**WisBlock Base**_.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/21-select-base-boards.png"
  width="50%"
  caption="Select Base Board category"
/>

Now, the available WisBlock Base Boards will be shown in the right-side menu.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/22-available-base-boards.png"
  width="50%"
  caption="Available Base Boards"
/>

3. For this example, choose the Base Board with 4 sensor slots and 1 IO slot.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/23-selected-base-board.png"
  width="100%"
  caption="Selected Base Board"
/>

#### Select a WisBlock Core Modules (Microcontrollers with LoRa)

1. Select _**WisBlock Core**_ from the left-side menu to show the available modules on the right.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/24-available-core-modules.png"
  width="50%"
  caption="Available Core Modules"
/>

2. Choose the correct frequency from the selector.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/25-core-frequency.png"
  width="50%"
  caption="Frequency Selector"
/>

3. Use the table below to select the correct frequency for your region:

| Country                             | Meshtastic Region Name | Frequency    |
|-------------------------------------|------------------------|--------------|
| United States                       | US                     | 9xx&nbsp;MHz |
| European Union868MHz (including UK) | EU_868                 | 8xx&nbsp;MHz |
| Japan                               | JP                     | 9xx&nbsp;MHz |
| Australia & New Zealand             | ANZ                    | 9xx&nbsp;MHz |
| Korea                               | KR                     | 9xx&nbsp;MHz |
| Taiwan                              | TW                     | 9xx&nbsp;MHz |
| Russia                              | RU                     | 8xx&nbsp;MHz |
| India                               | IN                     | 8xx&nbsp;MHz |
| New Zealand 865MHz                  | NZ_865                 | 8xx&nbsp;MHz |
| Thailand                            | TH                     | 9xx&nbsp;MHz |
| Ukraine 868MHz                      | UA_868                 | 8xx&nbsp;MHz |
| Malaysia 919MHz                     | MY_919                 | 9xx&nbsp;MHz |
| Singapore 923MHz                    | SG_923                 | 9xx&nbsp;MHz |


:::tip NOTE
- This table might not be accurate and is subject to change by Meshtastic.
- If you are unsure which frequency to choose, check the frequency list per country on the <a href="https://meshtastic.org/docs/configuration/region-by-country/" target="_blank">Meshtastic website</a>.
:::

4. Click on the RAK4631 module to add it to the Base Board, as illustrated in **Figure 24**.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/26-core-added.png"
  width="100%"
  caption="RAK4631 on the Base Board"
/>

:::tip NOTE
At the launch of the WisBlock Meshtastic Designer application, only the RAK4631 was included. Other Meshtastic-compatible WisBlock Core modules will be added in the future.
:::

#### Add a Module

This section explains the **Expert Mode** for selecting and adding modules to the device. For example, an acceleration sensor can detect device movements and update location information.

Follow the steps below to add more modules:

1. Selecting a module group from the left-side menu.

:::tip NOTE
For example, click on _**WisBlock Sensor**_ and the right-side menu will now display the available sensor modules.
:::

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/27-select-additional-modules.png"
  width="100%"
  caption="Change to add Sensors"
/>

2. On the top of the right-side menu, select the IO slot you want to add the module to.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/28-select-slot.png"
  width="50%"
  caption="Select Sensor"
/>

3. After choosing the slot, select the module you want to add.

:::tip NOTE
Greyed-out modules in the list indicate incompatibility. To see the reason, hover the mouse over the sensor and an explanation will appear. You will also see which slots the module is compatible with. In this case, Slot A and D are recommended.
:::

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/29-incompatible-slot.png"
  width="100%"
  caption="Incompatible slot warning"
/>

4. Select Slot A and double click on the module to be used. After clicking, the 3D view of the Meshtastic device will appear.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/30-placed-sensor-module.png"
  width="100%"
  caption="Sensor on the Base Board"
/>

:::tip NOTE
Some WisBlock modules, like the recently added RAK12039, are separated into two parts that are connected to each other. For these modules, only the WisBlock module is shown in the 3D view, while the sensor itself is not visible.
:::

<b>Add More Modules</b>

1. To add more modules, select an unoccupied slot, and the right-side menu will display which modules can be used in that slot.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/31-another-slot-selected.png"
  width="50%"
  caption="Select 2nd sensor slot"
/>

2. Select a second sensor and add it to the Meshtastic device.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/32-second-sensor-placed.png"
  width="50%"
  caption="2nd Sensor placed"
/>


#### Add an Enclosure

1. Scroll down the left-side menu to the _**Enclosure**_ category and click on it to refresh the right-side menu with enclosure options.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/11-select-enclosure-category.png"
  width="50%"
  caption="Select Enclosure category"
/>

2. On the right-side menu, select an enclosure and mounting plates listed.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/12-enclosures-mounting-plates.png"
  width="50%"
  caption="Enclosures and mounting plates"
/>

To avoid external antennas, the Unify WisBlock Mounting Plate with an integrated antenna is an ideal solution. Since Germany was selected as the region, only the mounting plate with an antenna for the 863-870&nbsp;MHz frequencies is selectable.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/13-mounting-plate.png"
  width="50%"
  caption="Mounting plate with integrated antenna for EU868"
/>

:::tip NOTE
It is also possible to choose another mounting plate without an integrated antenna. These mounting plates come with pre-installed stand-offs for the different WisBlock Base Boards.
:::

3. After selecting the mounting plate, it will appear in the 3D view. This also serves as a guide for how the Base Board should be mounted on the plate.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/14-device-on-mounting-plate.png"
  width="100%"
  caption="Device on the mounting plate"
/>

Now going back to the right-side menu, you can see that only one enclosure is left to be selected. This is because the mounting plate with integrated antennas is only compatible with the Unify Enclosure 100&nbsp;mm x 75&nbsp;mm x 38&nbsp;mm.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/15-select-enclosure.png"
  width="50%"
  caption="Matching enclosures"
/>

4. Click on the enclosure to show the device inside.

5. To open the lid, click the _**Enclosure Lid Open**_ button at the bottom of the screen.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/16-open-lid.png"
  width="50%"
  caption="Open the enclosure lid"
/>

Now you can see your Meshtastic Device inside the enclosure.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/17-device-in-enclosure.png"
  width="100%"
  caption="Device inside the enclosure"
/>

6. Proceed to the [Checkout](#checkout) to order your device.


### Checkout

Once you've added all the required modules, the total cost will appear at the bottom of the left-side menu. To complete your purchase, follow these steps:

1. Review your items in the shopping cart.

2. Click the _**Purchase**_ button to be redirected to the RAKwireless online store.

3. Select _**Place Order**_ to confirm.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/50-place-order.png"
  width="50%"
  caption="Order"
/>

After pressing _**Place Order**_, you will be redirected to the RAKwireless Store Payment page.

3. Entering your payment details and proceed with the checkout.

<RkImage
  src="https://images.docs.rakwireless.com/meshtastic/designer/51-order-cart-in-store.png"
  width="100%"
  caption="Checkout"
/>


<RkBottomNav/>