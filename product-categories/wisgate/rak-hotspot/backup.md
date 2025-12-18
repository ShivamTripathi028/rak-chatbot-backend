---
title: SD Card Backup
description: Guides you on how to back up the files from your RAK Hotspot to either macOS or Windows OS and also, on how to restore images. With these backup tools, it lessens the hassle of saving the SD Card files of your LoRaWAN Gateway.
keywords:
- RAK Hotspo
- Backup
- wisgate
image: https://images.docs.rakwireless.com/wisgate/rak-hotspot/rak-hotspot.png
sidebar_label: Backup
---

    

# SD Card Backup

## Prerequisites

### Hardware

1. [**RAK Hotspot**](https://store.rakwireless.com/products/rak-hotspot-miner?utm_source=RAKHotspotMiner&utm_medium=Document&utm_campaign=BuyFromStore)
2. USB microSD Card Reader
3. 32 GB or larger microSD Card (optional, to store the backup). To maintain similar performance we recommend a UHS-I compliant microSD card, for example, Sandisk™ High Endurance or Extreme.

### Power Down the RAK Hotspot

:::warning
Handle the microSD card from the Hotspot with care, as it is fragile. Using small pliers is highly recommended for safe removal.
:::

1. Disconnect the RAK Hotspot from the power supply. It needs to be off.
2. Extract the microSD card from the Hotspot slot.
3. Insert the microSD into the USB microSD card reader.

## SD Clone for macOS

1. Start by downloading [SD Clone](https://twocanoes.com/products/mac/sd-clone/).

> **Image:** Download SD Clone

2. After downloading, open the application. You will be prompted to choose between purchasing the full version or continuing with the trial. Select the trial option.

> **Image:** Select Clone Trial or Buy Option

### Image Backup

1. Insert your card, and if the message shown in the following figure appears, click **OK**.

> **Image:** SD Clone Authentication

2. Next, the application will request access to your SD storage, click "**OK**" in both windows.

> **Image:** Access SD Storage

> **Image:** Allow SD Clone to Access Files

3. Click the **Save Image** button, then click the **Save Image...** option.

> **Image:** Save Image

4. This will open a window where you can select the location to save your image. Once you click the blue **Save** button, the backup process will begin.

> **Image:** Select File Folder

5. A bar will be displayed indicating the cloning progress in percentage.

> **Image:** Ongoing Cloning Process

1. A notification window will appear once the cloning process is complete. In this example, it took approximately 40 minutes to back up a 32 GB card containing a Helium Hotspot image.

> **Image:** Clone Complete

### Restoring Image

1. If you want to restore an image, you must first select the storage drive.

> **Image:** Select Storage Device

2. Select the image in the side panel.

> **Image:** Select Image

3. Press the **Restore to Volume...** button. In the new window, you will be asked to confirm one final time; click the **Restore** button to start the process.

> **Image:** Restore Image to Volume

## Win32 Disk Imager for Windows OS

1. Start by downloading [**Win32 Disk Imager**](https://win32diskimager.download/download-win32-disk-imager/). Unzip the archive and install it.

2. Once done, you should see the same window as shown in **Figure 12**. The interface is minimalistic and easy to use.

> **Image:** Download Win32 Disk Imager

### Image Backup

1. Select the drive letter corresponding to the drive where your card is located. This is where the image will be copied from.

> **Image:** Select Storage Device

2. Provide the path to the file where the data will be backed up. You can do this either by entering it manually in the text box or by clicking the folder icon.

> **Image:** Select Image File Path

3. If you choose the second option, navigate to the desired location and enter a name in the text box. Make sure to add the **.img** extension to the file name, then click the **Open** button.

> **Image:** Enter Image File Name

4. Finally, with the path and filename set, start the backup process by clicking the **Read** button.

> **Image:** Start the Backup Process

5. The progress bar will start filling up, indicating the completion level of the process. The time required will vary depending on the size of your image and the card's speed.

> **Image:** Ongoing Backup Process

### Restore Image

The restoration procedure is even more streamlined than the backup.

1. Select the drive you want to flash the backup file to. Make sure you have the correct drive letter.

> **Image:** Select Storage Device

2. Navigate to your file either via the folder button or directly enter the path in the text box.

> **Image:** Select Image File Location

> **Image:** Locate the Image File Path

3. Confirm at the prompt with the **Yes** button.

> **Image:** Start the Restoring Process

4. You can monitor the progress using the bar. Simply wait for the process to complete.

> **Image:** Ongoing Restoring Process
