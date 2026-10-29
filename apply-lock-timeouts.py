#!/usr/bin/env python3
"""Persist AC and battery screen-lock timeouts in ~/.config/omarchy/shell.json.

The stock idle service reads a single idle.lock value. This script stores the
two quick settings and points idle.lock at whichever one matches the current
power source.
"""

import json
import os
import sys


def main() -> int:
    path, ac_raw, battery_raw, on_battery = sys.argv[1:]
    ac = int(ac_raw)
    battery = int(battery_raw)
    if ac < 0 or battery < 0:
        return 1
    active = battery if on_battery == "1" else ac

    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    idle = data.setdefault("idle", {})
    if (
        idle.get("lockOnAc") == ac
        and idle.get("lockOnBattery") == battery
        and idle.get("lock") == active
    ):
        return 0

    idle["lockOnAc"] = ac
    idle["lockOnBattery"] = battery
    idle["lock"] = active

    directory = os.path.dirname(path) or "."
    temporary = path + ".tmp"
    fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except Exception:
        try:
            os.unlink(temporary)
        except OSError:
            pass
        raise
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)
