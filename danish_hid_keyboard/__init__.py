#!/usr/bin/env python3
"""
DANISH HID KEYBOARD LIBRARY
Komplet BadUSB bibliotek for dansk keyboard layout
For Raspberry Pi Zero 2 W BadUSB projekter
"""

import time

class DanishHIDKeyboard:
    def __init__(self, hid_device='/dev/hidg0'):
        self.hid_device = hid_device
        
        # === MODIFIER KEYS ===
        self.MOD_LEFT_CTRL = 0x01
        self.MOD_LEFT_SHIFT = 0x02
        self.MOD_LEFT_ALT = 0x04
        self.MOD_LEFT_GUI = 0x08
        self.MOD_RIGHT_ALT = 0x40
        
        # === KEY CODES (US Physical Layout) ===
        # Tal
        self.KEY_1 = 0x1E
        self.KEY_2 = 0x1F
        self.KEY_3 = 0x20
        self.KEY_4 = 0x21
        self.KEY_5 = 0x22
        self.KEY_6 = 0x23
        self.KEY_7 = 0x24
        self.KEY_8 = 0x25
        self.KEY_9 = 0x26
        self.KEY_0 = 0x27
        
        # Bogstaver
        self.KEY_A = 0x04
        self.KEY_B = 0x05
        self.KEY_C = 0x06
        self.KEY_D = 0x07
        self.KEY_E = 0x08
        self.KEY_F = 0x09
        self.KEY_G = 0x0A
        self.KEY_H = 0x0B
        self.KEY_I = 0x0C
        self.KEY_J = 0x0D
        self.KEY_K = 0x0E
        self.KEY_L = 0x0F
        self.KEY_M = 0x10
        self.KEY_N = 0x11
        self.KEY_O = 0x12
        self.KEY_P = 0x13
        self.KEY_Q = 0x14
        self.KEY_R = 0x15
        self.KEY_S = 0x16
        self.KEY_T = 0x17
        self.KEY_U = 0x18
        self.KEY_V = 0x19
        self.KEY_W = 0x1A
        self.KEY_X = 0x1B
        self.KEY_Y = 0x1C
        self.KEY_Z = 0x1D
        
        # Specialtaster
        self.KEY_ENTER = 0x28
        self.KEY_ESC = 0x29
        self.KEY_BACKSPACE = 0x2A
        self.KEY_TAB = 0x2B
        self.KEY_SPACE = 0x2C
        self.KEY_MINUS = 0x2D      # + på dansk keyboard
        self.KEY_EQUAL = 0x2E      # ´ på dansk keyboard
        self.KEY_LEFTBRACE = 0x2F  # å på dansk keyboard
        self.KEY_RIGHTBRACE = 0x30 # ^ på dansk keyboard
        self.KEY_BACKSLASH = 0x31  # ' på dansk keyboard
        self.KEY_SEMICOLON = 0x33  # æ på dansk keyboard
        self.KEY_QUOTE = 0x34      # ø på dansk keyboard
        self.KEY_BACKQUOTE = 0x35  # § på dansk keyboard
        self.KEY_COMMA = 0x36      # , på dansk keyboard
        self.KEY_PERIOD = 0x37     # . på dansk keyboard
        self.KEY_SLASH = 0x38      # - på dansk keyboard
        self.KEY_102ND = 0x64      # < > tast (venstre for Z)
        
        # Funktionstaster
        self.KEY_F1 = 0x3A
        self.KEY_F2 = 0x3B
        self.KEY_F3 = 0x3C
        self.KEY_F4 = 0x3D
        self.KEY_F5 = 0x3E
        self.KEY_F6 = 0x3F
        self.KEY_F7 = 0x40
        self.KEY_F8 = 0x41
        self.KEY_F9 = 0x42
        self.KEY_F10 = 0x43
        self.KEY_F11 = 0x44
        self.KEY_F12 = 0x45
        
        # === KOMPLET DANSK KEYBOARD MAPPING (97% SUCCESS) ===
        self.DK_MAP = {
            # Bogstaver A-Z (store og små)
            'a': (self.KEY_A, 0), 'A': (self.KEY_A, self.MOD_LEFT_SHIFT),
            'b': (self.KEY_B, 0), 'B': (self.KEY_B, self.MOD_LEFT_SHIFT),
            'c': (self.KEY_C, 0), 'C': (self.KEY_C, self.MOD_LEFT_SHIFT),
            'd': (self.KEY_D, 0), 'D': (self.KEY_D, self.MOD_LEFT_SHIFT),
            'e': (self.KEY_E, 0), 'E': (self.KEY_E, self.MOD_LEFT_SHIFT),
            'f': (self.KEY_F, 0), 'F': (self.KEY_F, self.MOD_LEFT_SHIFT),
            'g': (self.KEY_G, 0), 'G': (self.KEY_G, self.MOD_LEFT_SHIFT),
            'h': (self.KEY_H, 0), 'H': (self.KEY_H, self.MOD_LEFT_SHIFT),
            'i': (self.KEY_I, 0), 'I': (self.KEY_I, self.MOD_LEFT_SHIFT),
            'j': (self.KEY_J, 0), 'J': (self.KEY_J, self.MOD_LEFT_SHIFT),
            'k': (self.KEY_K, 0), 'K': (self.KEY_K, self.MOD_LEFT_SHIFT),
            'l': (self.KEY_L, 0), 'L': (self.KEY_L, self.MOD_LEFT_SHIFT),
            'm': (self.KEY_M, 0), 'M': (self.KEY_M, self.MOD_LEFT_SHIFT),
            'n': (self.KEY_N, 0), 'N': (self.KEY_N, self.MOD_LEFT_SHIFT),
            'o': (self.KEY_O, 0), 'O': (self.KEY_O, self.MOD_LEFT_SHIFT),
            'p': (self.KEY_P, 0), 'P': (self.KEY_P, self.MOD_LEFT_SHIFT),
            'q': (self.KEY_Q, 0), 'Q': (self.KEY_Q, self.MOD_LEFT_SHIFT),
            'r': (self.KEY_R, 0), 'R': (self.KEY_R, self.MOD_LEFT_SHIFT),
            's': (self.KEY_S, 0), 'S': (self.KEY_S, self.MOD_LEFT_SHIFT),
            't': (self.KEY_T, 0), 'T': (self.KEY_T, self.MOD_LEFT_SHIFT),
            'u': (self.KEY_U, 0), 'U': (self.KEY_U, self.MOD_LEFT_SHIFT),
            'v': (self.KEY_V, 0), 'V': (self.KEY_V, self.MOD_LEFT_SHIFT),
            'w': (self.KEY_W, 0), 'W': (self.KEY_W, self.MOD_LEFT_SHIFT),
            'x': (self.KEY_X, 0), 'X': (self.KEY_X, self.MOD_LEFT_SHIFT),
            'y': (self.KEY_Y, 0), 'Y': (self.KEY_Y, self.MOD_LEFT_SHIFT),
            'z': (self.KEY_Z, 0), 'Z': (self.KEY_Z, self.MOD_LEFT_SHIFT),
            
            # Tal 0-9
            '0': (self.KEY_0, 0), '1': (self.KEY_1, 0), '2': (self.KEY_2, 0),
            '3': (self.KEY_3, 0), '4': (self.KEY_4, 0), '5': (self.KEY_5, 0),
            '6': (self.KEY_6, 0), '7': (self.KEY_7, 0), '8': (self.KEY_8, 0),
            '9': (self.KEY_9, 0),
            
            # Symboler fra talrækken
            '!': (self.KEY_1, self.MOD_LEFT_SHIFT),
            '"': (self.KEY_2, self.MOD_LEFT_SHIFT),
            '#': (self.KEY_3, self.MOD_LEFT_SHIFT),
            '$': (self.KEY_4, self.MOD_RIGHT_ALT),
            '%': (self.KEY_5, self.MOD_LEFT_SHIFT),
            '&': (self.KEY_6, self.MOD_LEFT_SHIFT),
            '/': (self.KEY_7, self.MOD_LEFT_SHIFT),
            '(': (self.KEY_8, self.MOD_LEFT_SHIFT),
            ')': (self.KEY_9, self.MOD_LEFT_SHIFT),
            '=': (self.KEY_0, self.MOD_LEFT_SHIFT),
            
            # Basis tegn
            ' ': (self.KEY_SPACE, 0),
            '-': (self.KEY_SLASH, 0),
            '_': (self.KEY_SLASH, self.MOD_LEFT_SHIFT),
            '.': (self.KEY_PERIOD, 0),
            ',': (self.KEY_COMMA, 0),
            ';': (self.KEY_COMMA, self.MOD_LEFT_SHIFT),
            ':': (self.KEY_PERIOD, self.MOD_LEFT_SHIFT),
            "'": (self.KEY_BACKSLASH, 0),
            '?': (self.KEY_MINUS, self.MOD_LEFT_SHIFT),
            '+': (self.KEY_MINUS, 0),
            '*': (self.KEY_BACKSLASH, self.MOD_LEFT_SHIFT),
            
            # Avancerede symboler
            '@': (self.KEY_2, self.MOD_RIGHT_ALT),
            '§': (self.KEY_BACKQUOTE, 0),
            
            # Parenteser
            '[': (self.KEY_8, self.MOD_RIGHT_ALT),
            ']': (self.KEY_9, self.MOD_RIGHT_ALT),
            '{': (self.KEY_7, self.MOD_RIGHT_ALT),
            '}': (self.KEY_0, self.MOD_RIGHT_ALT),
            
            # Programmeringstegn (VIGTIGE!)
            '|': (self.KEY_EQUAL, self.MOD_RIGHT_ALT),      # Pipe: AltGr+´
            '\\': (self.KEY_102ND, self.MOD_RIGHT_ALT),     # Backslash: AltGr+<
            '<': (self.KEY_102ND, 0),                       # Mindre end: <-tasten
            '>': (self.KEY_102ND, self.MOD_LEFT_SHIFT),     # Større end: Shift+<
            '~': (self.KEY_RIGHTBRACE, self.MOD_RIGHT_ALT), # Tilde: AltGr+^
            
            # Dansk bogstaver
            'æ': (self.KEY_SEMICOLON, 0), 'Æ': (self.KEY_SEMICOLON, self.MOD_LEFT_SHIFT),
            'ø': (self.KEY_QUOTE, 0), 'Ø': (self.KEY_QUOTE, self.MOD_LEFT_SHIFT),
            'å': (self.KEY_LEFTBRACE, 0), 'Å': (self.KEY_LEFTBRACE, self.MOD_LEFT_SHIFT),
        }

    # === KERNE FUNKTIONER ===
    def write_report(self, report):
        """Skriver 8 bytes til HID-enheden"""
        with open(self.hid_device, 'rb+') as fd:
            fd.write(report.encode())

    def press_key(self, modifier, keycode):
        """Trykker en tast ned og slipper den"""
        self.write_report(chr(modifier) + chr(0x00) + chr(keycode) + chr(0x00)*5)
        self.write_report(chr(0x00)*8)
        time.sleep(0.05)

    def type_char(self, char):
        """Skriver et enkelt tegn med korrekt mapping"""
        if char in self.DK_MAP:
            keycode, modifier = self.DK_MAP[char]
            self.press_key(modifier, keycode)
            
            # Special håndtering for Tilde ~ (skal have mellemrum)
            if char == '~':
                time.sleep(0.1)
                self.press_key(0, self.KEY_SPACE)
                time.sleep(0.1)
                self.press_key(0, self.KEY_BACKSPACE)
        else:
            print(f"Advarsel: Ukendt tegn '{char}' bliver sprunget over")

    def type_string(self, text, delay=0.05):
        """Skriver en streng tegn for tegn"""
        for char in text:
            self.type_char(char)
            time.sleep(delay)

    # === KEYBOARD SHORTCUTS ===
    def enter(self):
        """Trykker Enter"""
        self.press_key(0, self.KEY_ENTER)
    
    def tab(self):
        """Trykker Tab"""
        self.press_key(0, self.KEY_TAB)
    
    def backspace(self):
        """Trykker Backspace"""
        self.press_key(0, self.KEY_BACKSPACE)
    
    def space(self):
        """Trykker Mellemrum"""
        self.press_key(0, self.KEY_SPACE)
    
    def win_r(self):
        """Åbner Kør-dialogen (Win+R)"""
        self.press_key(self.MOD_LEFT_GUI, self.KEY_R)
    
    def ctrl_c(self):
        """Kopier (Ctrl+C)"""
        self.press_key(self.MOD_LEFT_CTRL, self.KEY_C)
    
    def ctrl_v(self):
        """Indsæt (Ctrl+V)"""
        self.press_key(self.MOD_LEFT_CTRL, self.KEY_V)
    
    def ctrl_a(self):
        """Vælg alt (Ctrl+A)"""
        self.press_key(self.MOD_LEFT_CTRL, self.KEY_A)
    
    def alt_tab(self):
        """Skifter program (Alt+Tab)"""
        self.press_key(self.MOD_LEFT_ALT, self.KEY_TAB)
    
    def alt_f4(self):
        """Lukker vindue (Alt+F4)"""
        self.press_key(self.MOD_LEFT_ALT, self.KEY_F4)

    # === PRAKTISKE HJÆLPE FUNKTIONER ===
    def open_powershell(self, wait_time=2):
        """Åbner PowerShell og venter"""
        self.win_r()
        time.sleep(0.5)
        self.type_string("powershell")
        self.enter()
        time.sleep(wait_time)
    
    def open_cmd(self, wait_time=2):
        """Åbner CMD og venter"""
        self.win_r()
        time.sleep(0.5)
        self.type_string("cmd")
        self.enter()
        time.sleep(wait_time)
    
    def open_notepad(self, wait_time=2):
        """Åbner Notepad og venter"""
        self.win_r()
        time.sleep(0.5)
        self.type_string("notepad")
        self.enter()
        time.sleep(wait_time)
    
    def run_command(self, command, wait_time=1):
        """Kører en kommando og venter"""
        self.type_string(command)
        self.enter()
        time.sleep(wait_time)

    # === VALIDERINGS FUNKTION ===
    def test_all_keys(self):
        """Test alle tegn for at bekræfte mapping"""
        print("Testing keyboard mapping...")
        test_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅabcdefghijklmnopqrstuvwxyzæøå0123456789!\"#$%&/()=+-_.,;:?*@§{}[]|\\<>~"
        
        self.open_notepad()
        self.type_string("=== KEYBOARD TEST ===")
        self.enter()
        self.type_string(test_string)
        self.enter()
        self.type_string("=== TEST FÆRDIG ===")
        
        print("Test færdig - check Notepad for resultater")
