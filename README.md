![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Raspberry_Pi_Zero_2_W-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Compatibility](https://img.shields.io/badge/Compatibility-97%25-success.svg)
# Danish HID Keyboard Library

A complete HID keyboard library for Danish keyboard layout, designed for Raspberry Pi Zero 2 W BadUSB projects.

## Features
- **97% keyboard compatibility** for Danish layout
- **Easy-to-use API** for BadUSB projects
- **Complete modifier key support** (Ctrl, Alt, Shift, Win)
- **Practical helper functions** 
- **Tested and verified** 

## Install
```
pip install danish-hid-keyboard
```

## Quick Start
```python
from danish_hid_library import DanishHIDKeyboard

kb = DanishHIDKeyboard()
kb.open_powershell()
kb.type_string('echo "Hello from BadUSB!"')
kb.enter()
```

## Responsible Use
This library is intended for:
- Educational purposes
- Authorized penetration testing  
- IT automation on owned systems
- Security research

Never use on systems without explicit permission.
