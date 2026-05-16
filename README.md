# Snake Water Gun

A Tkinter desktop game based on the classic Snake-Water-Gun rules.

## Overview

The game presents a simple GUI where the player chooses Snake, Water, or Gun and competes against a random computer choice. It includes loading behavior, image assets, rules, and result display.

## Key Features

- Desktop game UI
- Random computer opponent
- Built-in game rules screen
- Image assets for Snake, Water, and Gun
- Packaged build metadata through `Game.spec`

## Tech Stack

- Python
- Tkinter
- Pillow
- Threading and queue helpers

## Project Structure

```text
.
|-- Game.py                  # Main game application
|-- Game.spec                # PyInstaller spec
|-- snake.png
|-- water.png
|-- gun.png
|-- logo.PNG
`-- snake.ico
```

## Getting Started

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python Game.py
```

## GitHub Notes

Do not commit generated archives such as `.rar` files or OS files such as `Thumbs.db`.
