#!/usr/bin/env python3

def hex_to_rgb(hex_color):
    value = hex_color.lstrip("#")

    if len(value) != 6:
        raise ValueError("Expected a 6-digit HEX color")

    return tuple(
        int(value[i:i + 2], 16)
        for i in (0, 2, 4)
    )


def rgb_to_ansi(hex_color):
    red, green, blue = hex_to_rgb(hex_color)
    return f"\033[38;2;{red};{green};{blue}m"


def color_text(text, hex_color):
    color = rgb_to_ansi(hex_color)
    reset = "\033[0m"
    return f"{color}{text}{reset}"


if __name__ == "__main__":
    print(color_text("RZXXY NEBULA", "#A855F7"))
    print(color_text("AI DEVELOPMENT SYSTEM", "#22D3EE"))
    print(color_text("COLOR ENGINE: OK", "#FF8C42"))
