#!/usr/bin/env python3

from skin_loader import load_skin, load_personality
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def show_preview():
    skin = load_skin()
    personality = load_personality(skin["personality"])

    print("\n" + "=" * 45)
    print("          RZXXY NEBULA PREVIEW")
    print("=" * 45)

    print("\nName:", skin["name"])
    print("Description:", skin["description"])

    print("\n--- BRANDING ---")
    for key, value in skin["branding"].items():
        print(f"{key.title()}: {value}")

    print("\n--- COLORS ---")
    for name, color in skin["colors"].items():
        print(f"{name.title()}: {color}")

    print("\n--- PERSONALITY ---")
    print(personality)

    print("=" * 45)


if __name__ == "__main__":
    show_preview()
