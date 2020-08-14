import re

if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        css_line = input()
        hex_colors = re.findall(
            r"#(?:[0-9a-f]{3}){1,2}(?!$|\s*{$)", css_line, re.IGNORECASE
        )
        if hex_colors:
            print(*hex_colors, sep="\n")
