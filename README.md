# Danish HID Keyboard Library

A complete HID keyboard library for Danish keyboard layout, designed for Raspberry Pi Zero 2 W BadUSB projects.

## Features
- **97% keyboard compatibility** for Danish layout
- **Easy-to-use API** for BadUSB projects
- **Complete modifier key support** (Ctrl, Alt, Shift, Win)
- **Practical helper functions** for IT automation
- **Tested and verified** with real Danish keyboards

## Quick Start
```python
from danish_hid_library import DanishHIDKeyboard

kb = DanishHIDKeyboard()
kb.open_powershell()
kb.type_string('echo "Hello from BadUSB!"')
kb.enter()
