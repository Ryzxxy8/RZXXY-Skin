# RZXXY NEBULA

**AI DEVELOPMENT SYSTEM — Custom Terminal Skin Engine**

RZXXY NEBULA is a Python-based terminal skin and personality configuration project.

## Features

- YAML-based skin configuration
- Custom personality loader
- Terminal ANSI color engine
- RGB and HEX color conversion
- Terminal banner
- Skin preview engine
- Main launcher

## Project Structure

```text
RZXXY-Skin/
├── engine/
│   ├── banner.py
│   ├── color.py
│   ├── preview.py
│   └── skin_loader.py
├── personalities/
│   └── nebula.md
├── skins/
│   └── nebula.yaml
├── main.py
├── .gitignore
└── README.md

Requirements

Python 3.9+
PyYAML 6.0.3

Installation

Bash
python3 -m pip install PyYAML

Run

Bashpython3 main.py


Preview

Bash
python3 engine/preview.py

License

MIT License
