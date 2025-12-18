---
slug: /product-categories/wisnode/rak2171/helium-datacake/
title: RAK2171 WisNode TrackIt Helium Integration
description: Learn how to register the TrackIt device in the Helium console and make integration to Datacake, where you can use the dashboard to view the data in a more user-friendly way.
image: https://images.docs.rakwireless.com/wisnode/rak2171/rak2171.png
keywords:
    - lorawan
    - tracker
    - rak2171
    - wisnode
    - helium
sidebar_label: Helium + Datacake
---

# WisNode TrackIt Helium Integration

This guide shows how to register the TrackIt device in the Helium console and make integration to Datacake, where you can use the dashboard to view the data in a more user-friendly way. For example, create a map so you can see the location of the device.

Before you dive into registering the device in the Helium console and creating the Datacake integration, you need to set the device to work in [Third-Party LoRaWAN Network Server (LNS) Mode](https://docs.rakwireless.com/product-categories/wisnode/rak2171/quickstart/#third-party-lorawan-network-server-lns-mode).

## Register the TrackIt Node in the Helium Console

1. Login into your Helium console account. If you do not have one, head to the web page and create one. Once you are logged in, you will see the Welcome window.

> **Image:** Helium console main page

2. In the menu on the left side of the console, select **Devices** and click the **Add new device** button (<img width="20px" src="https://images.docs.rakwireless.com/wisnode/rak2171/helium-datacake/1.png"/>) to register your device.

> **Image:** Helium console devices page

3. In the **Name** field, type the preferred name of your device.

> **Image:** Add New Device page

4. You can see that the Helium console generates random **Dev EUI**, **App EUI**, and **App Key**. Since the TrackIt keys cannot be changed, you need to type your keys in the fields. These keys can be found in the TrackIt application in the LoRaWAN Working Mode (**Third Party NS**).

> **Image:** TrackIt keys

5. Optionally, you can select a **Profile** and **Attach a Label**. For this tutorial, they will be skipped. Note that **Profiles** and **Labels** can be added after the device is registered.

6. After typing in the required keys, click **Save Device**, and you will see the registered device. As mentioned by the console, the initial join process takes about 20 minutes for the device to join, so be patient.

## Create Datacake Integration

1. While the device is joining, you can create the integration. Select **Integrations** from the menu in the left panel.

> **Image:** Integration page

2. To create an integration, click the **Add New Integration button** (<img width="20px" src="https://images.docs.rakwireless.com/wisnode/rak2171/helium-datacake/2.png"/>). A list of the available integrations will appear. As for this guide, click Datacake. For further information, refer to the [**Integrations** documentation](https://docs.helium.com/use-the-network/console/integrations/).

> **Image:** List of available integrations

3. On the next page, you will need a **Datacake Token**. To generate one, you will need a Datacake account. If you don't have an account yet, you can create one on [Datacake's website](https://datacake.co/).

> **Image:** Datacake endpoint token

4. After logging in to your Datacake account, click your profile and select **Edit Profile.**

> **Image:** Datacake console page

5. In the **API** tab, you will find your API token. Copy and paste it into the **Enter Datacake Token** field in the Helium console, as shown in **Figure 9**.

> **Image:** Datacake endpoint

6. When you place the token, type a name of your choice for the integration and click **Add Integration** to continue.

> **Image:** Adding integration name

### Connection Between Helium and Datacake

1. Now that the device is registered and the integration created, you will need to make the connection between Helium and Datacake. Click **Flows** from the left menu.

> **Image:** Helium console flows

2. Click the **+** in the **Nodes area**. A window will pop up with four menus – **Labels, Devices, Functions**, and **Integrations**. Click **Devices**, and you will see your registered device.

> **Image:** Nodes

3. Now, click the registered device and drag and drop it on the blank page below, as shown in **Figure 13**.

4. Do the same with the created integration. Click the **Integrations** menu and drag and drop your created integration.

> **Image:** Creating the connection between the device and the integration

### Datacake Device Registration

1. You need to add the device to the Datacake console. Head to the **Devices** tab and click the **+ Add Device** button.

> **Image:** Datacake console

2. Datacake has ready-to-use TrackIt template. To add the device, click **LoRaWAN** and then **Next**.

> **Image:** Adding a new device

3. On the next window, in the **Search** field, type **TrackIt** and choose the **Device Template**. Then click **Next**.

> **Image:** Selecting product template

4. On the next page, choose **Helium** for Network server and click **Next**.

> **Image:** Choosing network server

5. On the next page, type the **Dev EUI** and the **Name of your device**. You can add more than one device. You can also drag and drop a `.csv` file, and it automatically adds multiple devices at once. Then click **Next**.

> **Image:** Adding device

6. Finally, choose a plan. For this example, choose the **Free** one. Click **Add 1 device** to finish.

> **Image:** Choosing a plan

7. Now, your device is registered in Datacake.

> **Image:** Registered TrackIt device in Datacake

8. You can click the name of your device and check the Dashboard.

> **Image:** TrackIt Dashboard

Everything in the Dashboard is pre-configured (fields, decoder, widgets), and it is ready to use.

<!--

## Configure the Device in Datacake

1. You need to decode the raw data that the device sends to Datacake, so you can preview it in a more user-friendly way. On the device page of the Datacake console, you can find different tabs like **Dashboard**, **History**, and **Downlinks**. For now, head to the **Configuration tab**.

> **Image:** Device’s Dashboard

2. Scroll down until you find the Payload Decoder field.

> **Image:** Device’s Configuration Page

3. In the **Payload Decoder** field, copy and paste the code below. Then click the **Save** button below the decoder field.

```js
function Decoder(bytes, port) {
    var decoded = {};

    // adjust time zone, here Asia/Manila = +8H
    var my_time_zone = (8 * 60 * 60);

    decoded.num = bytes[1];
    decoded.app_id = (bytes[2] << 24) | (bytes[3] << 16) | (bytes[4] << 8) | bytes[5];
    decoded.dev_id = (bytes[6] << 24) | (bytes[7] << 16) | (bytes[8] << 8) | bytes[9];
    switch (bytes[0]) {
        case 0xCA: // No Location fix
            decoded.acc = 0;
            decoded.fix = 0;
            decoded.batt = bytes[10];
            decoded.time = ((bytes[11] << 24) | (bytes[12] << 16) | (bytes[13] << 8) | bytes[14]);
            // adjust time zone
            decoded.time = decoded.time + my_time_zone;
            var dev_date = new Date(decoded.time * 1000);
            decoded.time_stamp = dev_date.getHours() + ":" + dev_date.getMinutes();
            decoded.date_stamp = dev_date.getDate() + "." + (dev_date.getMonth() + 1) + "." + dev_date.getFullYear();
            decoded.stat = bytes[15] & 0x03;
            decoded.gps = bytes[15] & 0x0C;
            break;
        case 0xCB: // Location fix
            decoded.fix = 1;
            decoded.batt = bytes[20];
            decoded.time = ((bytes[21] << 24) | (bytes[22] << 16) | (bytes[23] << 8) | bytes[24]);
            // adjust time zone
            decoded.time = decoded.time + my_time_zone;
            var dev_date = new Date(decoded.time * 1000);
            decoded.time_stamp = dev_date.getHours() + ":" + dev_date.getMinutes();
            decoded.date_stamp = dev_date.getDate() + "." + (dev_date.getMonth() + 1) + "." + dev_date.getFullYear();
            decoded.stat = bytes[25] & 0x03;
            decoded.gps = bytes[25] & 0x0C;
            decoded.lng = (((bytes[10] << 24) | (bytes[11] << 16) | (bytes[12] << 8) | bytes[13]) * 0.000001).toFixed(4);
            decoded.lat = (((bytes[14] << 24) | (bytes[15] << 16) | (bytes[16] << 8) | bytes[17]) * 0.000001).toFixed(4);
            decoded.location = decoded.lat + "," + decoded.lng;
            decoded.acc = bytes[18];
            decoded.gps_start = bytes[19];
            break;
        case 0xCC: // SOS
            decoded.sos = 1;
            decoded.lng = (((bytes[10] << 24) | (bytes[11] << 16) | (bytes[12] << 8) | bytes[13]) * 0.000001).toFixed(4);
            decoded.lat = (((bytes[14] << 24) | (bytes[15] << 16) | (bytes[16] << 8) | bytes[17]) * 0.000001).toFixed(4);
            if (bytes.length > 18) {
                var i;
                for (i = 18; i < 28; i++) {
                    decoded.name += bytes[i].toString();
                }
                for (i = 28; i < 40; i++) {
                    decoded.country += bytes[i].toString();
                }
                for (i = 39; i < 50; i++) {
                    decoded.phone += bytes[i].toString();
                }
            }
            break;
        case 0xCD:
            decoded.sos = 0;
            break;
        case 0xCE:
            decoded.alarm = 0x01;
            decoded.alarm_lvl = bytes[10];
            break;
    }
    return decoded;
}
```

4. Now you can see the decoded data you receive in the **Debug tab**.

> **Image:** TrackIt Data

5. Create fields for the different data that the device sends. Below is a list of the fields you can create:

| Type | Name | Identifier | Description |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Integer | Frame Counter | NUM | Packets Counter |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Integer | Application ID | APP_ID | The ID of the application |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Integer | Device ID | DEV_ID | The ID of the device |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Boolean | Fix | FIX | GPS fix |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Integer | Battery | BATT | Battery Level |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| String | Time Stamp | TIME_STAMP | Time of the packet |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| String | Date Stamp | DATE_STAMP | Date of the packet |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Integer | Status | STAT | 1=sending |  |  |  | 3=sending | Integer | GPS | GPS | GPS Status |  |  |  | 0:open the GPS fix |  |  |  | 4:locating |  |  |  | 8:successful |  |  |  | 12:failed | Integer | Accuracy | ACC | Accuracy of GPS | Geolocation | Location | LOCATION | GPS coordinates | String | Tracker ID | TRACKER_ID | The ID of the tracker | Integer | Alarm Level | ALARM_LVL | The level of the alarm set in the application | Integer | Alarm | ALARM | Shows if the alarm is triggered |
|  |  |  | 3=sending | Integer | GPS | GPS | GPS Status |  |  |  | 0:open the GPS fix |  |  |  | 4:locating |  |  |  | 8:successful |  |  |  | 12:failed | Integer | Accuracy | ACC | Accuracy of GPS | Geolocation | Location | LOCATION | GPS coordinates | String | Tracker ID | TRACKER_ID | The ID of the tracker | Integer | Alarm Level | ALARM_LVL | The level of the alarm set in the application | Integer | Alarm | ALARM | Shows if the alarm is triggered |  |  |  |  |
| Integer | GPS | GPS | GPS Status |  |  |  | 0:open the GPS fix |  |  |  | 4:locating |  |  |  | 8:successful |  |  |  | 12:failed | Integer | Accuracy | ACC | Accuracy of GPS | Geolocation | Location | LOCATION | GPS coordinates | String | Tracker ID | TRACKER_ID | The ID of the tracker | Integer | Alarm Level | ALARM_LVL | The level of the alarm set in the application | Integer | Alarm | ALARM | Shows if the alarm is triggered |  |  |  |  |  |  |  |  |
|  |  |  | 0:open the GPS fix |  |  |  | 4:locating |  |  |  | 8:successful |  |  |  | 12:failed | Integer | Accuracy | ACC | Accuracy of GPS | Geolocation | Location | LOCATION | GPS coordinates | String | Tracker ID | TRACKER_ID | The ID of the tracker | Integer | Alarm Level | ALARM_LVL | The level of the alarm set in the application | Integer | Alarm | ALARM | Shows if the alarm is triggered |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | 4:locating |  |  |  | 8:successful |  |  |  | 12:failed | Integer | Accuracy | ACC | Accuracy of GPS | Geolocation | Location | LOCATION | GPS coordinates | String | Tracker ID | TRACKER_ID | The ID of the tracker | Integer | Alarm Level | ALARM_LVL | The level of the alarm set in the application | Integer | Alarm | ALARM | Shows if the alarm is triggered |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | 8:successful |  |  |  | 12:failed | Integer | Accuracy | ACC | Accuracy of GPS | Geolocation | Location | LOCATION | GPS coordinates | String | Tracker ID | TRACKER_ID | The ID of the tracker | Integer | Alarm Level | ALARM_LVL | The level of the alarm set in the application | Integer | Alarm | ALARM | Shows if the alarm is triggered |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | 12:failed | Integer | Accuracy | ACC | Accuracy of GPS | Geolocation | Location | LOCATION | GPS coordinates | String | Tracker ID | TRACKER_ID | The ID of the tracker | Integer | Alarm Level | ALARM_LVL | The level of the alarm set in the application | Integer | Alarm | ALARM | Shows if the alarm is triggered |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Integer | Accuracy | ACC | Accuracy of GPS | Geolocation | Location | LOCATION | GPS coordinates | String | Tracker ID | TRACKER_ID | The ID of the tracker | Integer | Alarm Level | ALARM_LVL | The level of the alarm set in the application | Integer | Alarm | ALARM | Shows if the alarm is triggered |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Geolocation | Location | LOCATION | GPS coordinates |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| String | Tracker ID | TRACKER_ID | The ID of the tracker |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Integer | Alarm Level | ALARM_LVL | The level of the alarm set in the application |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Integer | Alarm | ALARM | Shows if the alarm is triggered |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

6. To create a field, in the **Configuration** tab for the device in the Datacake console, scroll down to the **Fields** field. Click on the **+ Add Field** button. In the **Add Field** window, fill in the following information based on the table above:

- **Type** – Type of the field.
- **Name** – Name of the field. Note that you can type a name of your choice. The above names are just a template.
- **Identifier** – The decoder decodes the data in fields (see **Figure 24**). The **Identifier** must be exactly the name of the field of the decoded data (e.g. **TIME_STAMP** for the Time Stamp field). Note that field names cannot be changed.
- **Unit (optional)** – The unit of the value (e.g. V for battery (volts)).
- **Use formula** - Formulas can be used to perform calculations on values based on other fields.

> **Image:** Adding a field

For example, to create a **LOCATION** field, choose **Geolocation** in the **Type** field. For the **Identifier** field, type the name of the decoded data field: **LOCATION**.

> **Image:** Location field

7. When you enter the required information, click **Add Field**. You will see the created field in the Field tab. Once a packet is received, the field will take the value of the identifier.

> **Image:** Successfully Created Field

Another example is if you want to create a field for the battery level. Click again **+ Add Field**, and select **Integer** in the **Type** field. Type **Battery** in the Name field and **BATT** in the Identifier field.

> **Image:** Add battery field

8. Do the same with the other fields. It is up to you to decide on what fields are required for your project. Make sure you select the right **Type** and enter the correct **Identifier**.

9. Now that the fields are created, head to the **Dashboard** of the device. Activate the **Edit mode** using the switch (<img src="https://images.docs.rakwireless.com/wisnode/rak2171/helium-datacake/4.png"/> ) and click **+ Add Widget**. You can create a widget to preview the data in the dashboard. Choose the correct widget for the desired field.

> **Image:** Datacake Widgets

For example, when creating a map, click the **Map (Displays a map)** widget.

> **Image:** Map Widget

10.  In the **Basics** tab, you can type a name for the widget. In the **Appearance** tab, you can set a design to your widget (color, style). The **Data** tab is most important. Here you need to select the location field you have created above. Click on the **+** **Add field** and select the **Location** field. In addition, in the **Timeframe** tab, you can enable whether the map will show historical data.

> **Image:** Map field

1.  Once you have set the field, click **Save** and you will see the map in the Dashboard.

> **Image:** Datacake map

In addition, if you want to add a widget to see the battery level of the device, click again **+ Add Widget** and select **Value**. In the **Data** tab, select **Battery** for **Field**. Then click **Save** to add the widget.

> **Image:** Add Battery Widget

12.  If you want, you can create other widgets. For example:

- **String/Integer** field - choose **Value** (Displays a measurement).
- **Boolean** field - choose **Boolean** (Displays a boolean state).

> **Image:** TrackIt Dashboard

13. Once you add your widgets, you can customize your Dashboard depending on your needs. Remember, when you finish customizing your Dashboard, deactivate the **Edit mode** by clicking the **yellow switch** to save your changes.

--->

