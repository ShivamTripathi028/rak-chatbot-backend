---
slug: /product-categories/software-apis-and-libraries/wisgateos2/firmware/
title: WisGateOS 2 User Manual | Complete Guide for LoRaWAN Gateway Software
description: Check and upgrade the firmware on your WisGateOS 2 gateway.
image: "https://images.docs.rakwireless.com/product-logos/wisgateos2.png"
keywords:
  - firmware upgrade gateway
  - gateway firmware
tags:
  - firmware upgrade
sidebar_label: Firmware Upgrade
date: 2022-08-01
---



import RkImage from '@site/src/components/Image'
import RkBottomNav from '@site/src/components/Document/BottomNav'



# Firmware Upgrade

This section guides you through the process of checking and upgrading the firmware on your **WisGateOS 2** gateway.

## Check the Firmware Version

Go to **Settings> Firmware** to view the current firmware version.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/settings/settings-firmware.png"
  width="100%"
  caption="Firmware tab"
/>

## Firmware Upgrade

### Before You Upgrade

#### Backup Before Any Upgrade

Before performing any firmware upgrade, it is **highly recommended** to create a full backup of your configuration. This ensures you can restore your settings in case of unexpected issues or if a reset is required.

For detailed steps on how to back up your configuration, refer to [Backup Configuration](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/wisgateos2/settings/#backup-configuration).

#### Upgrade to WisGateOS 2.2.x

When upgrading **from WisGateOS 2.1.x or earlier to 2.2.x**, take note of the following important considerations:

- **Downgrading Restrictions**<br/>
  After upgrading to WisGateOS 2.2.x, reverting to version 2.1.x through the standard downgrade method (WebUI) is not possible. Make sure that all **critical data is backed up** before proceeding with the upgrade.
  
  Downgrading is only possible through a **recovery procedure**. For details, see [OpenWRT Recovery Procedure](https://learn.rakwireless.com/hc/en-us/articles/26743834483351-How-To-Perform-OpenWRT-Recovery-Procedure) on the RAK Learn site.

- **Extension Signature Requirement**<br/>
  Starting with **WisGateOS 2.2.x**, all official extensions are released with valid signatures to maintain security and compatibility. The system still allows uploading custom extensions without signatures, mainly for development or customization purposes.

  Unsigned extensions installed before the upgrade remain functional and do not require reinstallation.

- **Internet Connection Requirement**<br/>
  An Internet connection is required during the upgrade to verify the new firmware and extension signatures.

- **Dual Firmware Support**<br/>
  Both 2.1.x and 2.2.x will be supported. Make sure the correct extensions for each version to avoid compatibility issues.

### Upgrade Steps

:::warning
Do not disconnect the power during the gateway upgrade.
::::

1. Download the latest version of the [WisGateOS 2 firmware](https://downloads.rakwireless.com/LoRa/WisGateOS2/WisGateOS2_Latest_Firmware.zip) for the gateway and unzip the file.
2. Drag and drop the `.rwi` file in the **Drop your RWI file here or choose file** form, or click the **choose file** link to browse for the file.
3. Check the **Keep settings after updating** option.
    <RkImage
     src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/settings/select-firmware-file.png"
     width="80%"
     caption="Upload the firmware file"
   />
   :::tip NOTE
   The **Keep settings after updating** check box is selected by default. Unchecking it will reset the gateway to stock settings after the upgrade.
   :::
4. Click **Update** to initiate the firmware flashing process.
   <RkImage
     src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/settings/upgrading.png"
     width="80%"
     caption="Upgrading"
   />
5. After the upgrade is complete, log in to the gateway and check the **Firmware tab** to confirm that the installed firmware version is correct.

## Troubleshooting

### WisDM Firmware Upgrade Management

When the gateway is integrated with WisDM and FOTA is enabled, the firmware upgrade is managed remotely by WisDM.

<RkImage
  src="https://images.docs.rakwireless.com/software-apis-and-library/wisgateos2/settings/upgrade-over-wisdm.png"
  width="100%"
  caption="Firmware tab inactive"
/>

To enable firmware upgrades through the gateway:

1. Navigate to the **WisDM tab**.
2. Disable the **Enable FOTA** option.
3. Save the changes.

Once FOTA is disabled, the **Firmware** tab will becomes active, allowing you to perform the firmware upgrade.

:::info NOTE
Disabling FOTA will prevent the gateway from receiving automatic firmware updates via WisDM and allow you to manage the firmware updates directly through WisGateOS.
:::

<RkBottomNav/>