# Clipboard Typer

This Python script allows users to "type" the clipboard content instead of pasting it. It is useful in environments where pasting from the clipboard is restricted, but typing is allowed.

## Features
- Monitors keyboard inputs and listens for `Cmd + Shift + V` (on macOS) or `Ctrl + Shift + V` (on Windows/Linux).
- When the key combination is pressed, the script types out the current clipboard content character by character.
- Ensures that the function triggers only once per key press sequence.

## Use Case
Some applications or remote environments disable direct pasting from the clipboard for security reasons. This script bypasses that restriction by simulating keystrokes, effectively "typing" the clipboard content into any text field where manual typing is permitted.

## Requirements
Ensure you have Python installed (version 3.x recommended) and install the required dependencies:
```sh
pip install pynput pyperclip
```

## How to Use
1. Run the script:
   ```sh
   python script.py
   ```
2. Copy any text to your clipboard.
3. Place the cursor where you want to insert the clipboard content.
4. Press `Cmd + Shift + V` (on macOS) or `Ctrl + Shift + V` (on Windows/Linux) to "type" the clipboard content.

## How It Works
- The script listens for key presses using `pynput`.
- When `Cmd + Shift + V` (or `Ctrl + Shift + V`) is detected, it retrieves the clipboard content using `pyperclip`.
- Instead of pasting, the script uses `pynput.keyboard.Controller` to simulate typing each character.
- This allows the content to appear as if it were manually typed, bypassing clipboard paste restrictions.

## Notes
- Ensure the script is running in the background while using it.
- Some applications with advanced security measures might detect simulated keystrokes.
- The script currently works for text-based clipboard content only.

## License
This script is open-source and can be modified as needed.

