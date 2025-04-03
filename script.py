from pynput.keyboard import Controller, Listener, Key, KeyCode
import pyperclip

keyboard_ = Controller()
pressed_keys = set()  # To track pressed keys
triggered = False  # Flag to trigger action once

def type_clipboard():
    text = pyperclip.paste()
    print(f"Clipboard content: {text}")
    keyboard_.type(text)

def on_press(key):
    global triggered
    pressed_keys.add(key)

    # Only trigger once when Cmd, Shift, and 'V' are pressed together
    if Key.cmd in pressed_keys and Key.shift in pressed_keys and KeyCode.from_char('v') in pressed_keys:
        if not triggered:
            triggered = True
            type_clipboard()
            print("Clipboard content typed.", triggered)

def on_release(key):
    global triggered
    if key in pressed_keys:
        pressed_keys.remove(key)


    # Reset trigger if all keys are released
    if Key.cmd not in pressed_keys and Key.shift not in pressed_keys and KeyCode.from_char('v') not in pressed_keys:

        triggered = False

print("Press Cmd + Shift + V to type clipboard contents")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
