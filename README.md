# Power lock timeouts

An [Omarchy](https://omarchy.org) shell plugin that adds screen-lock quick settings to the battery menu in the bar.

It replaces the built-in Power widget. Battery level, charge stats, and power profiles stay as they are. Under them, **Screen lock** offers two rows:

- **Plugged in**
- **On battery**

Each row is 5 minutes, 15 minutes, 30 minutes, 1 hour, or 2 hours. The active power source decides which timeout the session uses. Plugging in or unplugging switches to that row's choice.

Omarchy's idle service reads a single `idle.lock` value in `~/.config/omarchy/shell.json`. This plugin stores both choices next to it:

```json
"idle": {
  "screensaver": 150,
  "lock": 3600,
  "lockOnAc": 3600,
  "lockOnBattery": 300
}
```

`lock` follows the current source. `lockOnAc` and `lockOnBattery` are seconds. The screensaver timeout is left alone.

## Install

```bash
omarchy plugin add https://github.com/andp97/omarchy-power-lock.git --enable
```

Enabling it takes the place of `omarchy.power` in the bar, in the same position. Open the battery icon to use the new rows.

To go back to the built-in widget:

```bash
omarchy plugin disable andp97.power
```

## Requirements

Omarchy 4, with the shell battery menu, and `python3` (already part of a normal Omarchy install).

## License

MIT. `Panel.qml` and `Model.js` are derived from the Omarchy power panel, copyright David Heinemeier Hansson, also MIT. See [LICENSE](LICENSE).
