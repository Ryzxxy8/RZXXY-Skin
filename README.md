🌌 RZXXY NEBULA

AI DEVELOPMENT SYSTEM — Custom Terminal Skin Engine

RZXXY NEBULA is a Python-based terminal skin and personality configuration engine designed to provide customizable terminal branding, color themes, and AI assistant personality profiles.

✨ Features

* YAML Configuration — Manage terminal skin settings.
* Personality System — Load custom AI personality profiles.
* ANSI Color Engine — Display colored terminal output.
* RGB & HEX Conversion — Convert HEX colors into RGB and ANSI formats.
* Terminal Branding — Display custom RZXXY banners.
* Skin Preview — Preview skin configuration and personality settings.
* Python Launcher — Start the system through a single entry point.

## 📁 Project Structure
```
RZXXY-Skin/
│
├── engine/
│   ├── banner.py
│   ├── color.py
│   ├── preview.py
│   └── skin_loader.py
│
├── personalities/
│   └── nebula.md
│
├── skins/
│   └── nebula.yaml
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```
⚙️ Requirements

* Python 3.9 or higher
* PyYAML 6.0.3

🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Ryzxxy8/RZXXY-Skin.git
```

Enter the project directory:

```bash
cd RZXXY-Skin
```

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```



## ▶️ Usage

Start RZXXY NEBULA:
```bash
python3 main.py
```
## 🔍 Preview

Display the skin configuration and personality:
```bash
python3 engine/preview.py
```
Display the terminal banner:
```bash
python3 engine/banner.py
```
🎨 Default Theme

| Property | Value |
|---|---|
| Theme Name | RZXXY NEBULA |
| Background | `#0B0B14` |
| Foreground | `#E6E6FA` |
| Primary | `#A855F7` |
| Secondary | `#22D3EE` |
| Accent | `#FF8C42` |

🧠 Personality

The default personality is NEBULA, designed around:

* Analytical thinking
* Technical communication
* Security-conscious development
* Practical problem solving
* Step-by-step guidance

📱 Platform

Developed and tested in an iSH Alpine Linux environment.

Terminal color support may vary depending on the terminal emulator.

📜 License

MIT License

⸻

RZXXY NEBULA
AI DEVELOPMENT SYSTEM

Built with Python. Customized by RZXXY.
