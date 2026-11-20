#!/usr/bin/env python3

from pathlib import Path
import yaml

BASE_DIR = Path(__file__).resolve().parent.parent
SKIN_FILE = BASE_DIR / "skins" / "nebula.yaml"
PERSONALITY_DIR = BASE_DIR / "personalities"


def load_skin():
    if not SKIN_FILE.exists():
        raise FileNotFoundError(f"Skin file not found: {SKIN_FILE}")

    with SKIN_FILE.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if not isinstance(config, dict):
        raise ValueError("Invalid skin configuration")

    return config


def load_personality(name):
    personality_file = PERSONALITY_DIR / f"{name}.md"

    if not personality_file.exists():
        raise FileNotFoundError(
            f"Personality file not found: {personality_file}"
        )

    return personality_file.read_text(encoding="utf-8")


if __name__ == "__main__":
    skin = load_skin()
    personality = load_personality(skin["personality"])

    print("RZXXY SKIN LOADER: OK")
    print("Name:", skin["name"])
    print("Theme:", skin["description"])
    print("Personality:", skin["personality"])
    print("Personality loaded:", bool(personality))
