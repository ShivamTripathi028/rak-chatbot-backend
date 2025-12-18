

# Watchdog

:::warning
With RUI3 version V4.1.1, the watchdog cannot be disabled. It will stay active until a power cycle of the device is performed.
:::

## enable

### enable()

Initialize the watchdog

```c
api.system.wdt.enable(reload_value);
```

| **Function**   | `void enable(int reload_value)`                                                                                                                                                                   |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Parameters** | Setting the reload value, only accept following values: 15 ms, 30 ms, 60 ms, 120 ms, 250 ms, 500 ms, 1 s, 2 s, 4 s, and 8 s, Units:milliseconds |
| **Returns**    | void                                                                                                                                                                                              |

<details>
<summary> Click to view the code</summary>

```c{2,3}
void setup() {
  api.system.wdt.enable(8000); //8 seconds for watchdog to feed, otherwise reset occurs.
}

void loop() {
  api.system.wdt.reset();
  delay(5000);
}
```
</details>

### reset()

Reset the watchdog Timer

```c
api.system.wdt.reset();
```

| **Function** | `void reset(void)` |
|--------------|--------------------|
| **Returns**  | void               |

<details>
<summary> Click to view the code</summary>

```c{6}
void setup() {
  api.system.wdt.enable(8000); //8 seconds for watchdog to feed, otherwise reset occurs.
}

void loop() {
  api.system.wdt.reset();
  delay(5000);
}
```
</details>

