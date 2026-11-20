#!/usr/bin/env python3

from engine.skin_loader import load_skin, load_personality
from engine.color import color_text
from pathlib import Path

def main():
    skin = load_skin()
    colors = skin["colors"]

    print()
    print(color_text("=" * 45, colors["primary"]))
    print(color_text(skin["branding"]["title"], colors["primary"]))
    print(color_text(skin["branding"]["subtitle"], colors["secondary"]))
    print(color_text("=" * 45, colors["primary"]))

    print()
    print(color_text("Skin:", colors["secondary"]), skin["name"])
    print(color_text("Author:", colors["secondary"]), skin["branding"]["author"])

    personality = load_personality(skin["personality"])
    print(color_text("Personality:", colors["secondary"]), bool(personality))

    print()
    print(color_text("RZXXY NEBULA SYSTEM: READY", colors["accent"]))


if __name__ == "__main__":
    main()
