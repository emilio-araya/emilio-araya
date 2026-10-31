#!/usr/bin/env python3
"""Render the animated profile banner (dark and light) from a portrait photo.

Run from the repository root:

    python3 -m venv .venv && .venv/bin/pip install -r scripts/requirements.txt
    .venv/bin/python scripts/banner.py

Inputs:
    assets/source/portrait.png  head-and-shoulders photo with a transparent background
    data/profile.json           the YAML rows shown in the editor panel

Outputs:
    assets/banner-dark.svg, assets/banner-light.svg

The portrait is converted to a 1-bit Floyd-Steinberg dither and drawn as a single
SVG path, revealed by a scanline. The YAML rows then appear one by one.
"""

from __future__ import annotations

import json
from html import escape
from pathlib import Path

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parents[1]
PORTRAIT = ROOT / "assets/source/portrait.png"
PROFILE = ROOT / "data/profile.json"
ASSETS = ROOT / "assets"

W, H = 1180, 610
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

# Portrait grid: GRID_W x GRID_H dither cells, each drawn CELL px apart.
GRID_W, GRID_H, CELL = 240, 272, 1.4
FRAME_X, FRAME_Y, FRAME_W, FRAME_H = 49, 124, 390, 414
REVEAL_SECONDS = 2.4
ROW_START, ROW_STEP = 0.8, 0.14

# Pedidos360 repositories shown in the side panel, with their main technology.
SERVICES = [("frontend", "React"), ("bff", "Spring"), ("catalog", "Spring"),
            ("orders", "Spring"), ("infra", "Terraform")]

THEMES = {
    "dark": {
        "bg": "#0B1117", "panel": "#0F1822", "panel2": "#111D29", "line": "#223142",
        "muted": "#8B9BAB", "text": "#E6EDF3", "ink": "#6DB33F", "chrome": "#4FC3F7",
        "key": "#4FC3F7", "value": "#E6EDF3", "section": "#F2B84B", "ok": "#6DB33F",
    },
    "light": {
        "bg": "#F6F8FA", "panel": "#FFFFFF", "panel2": "#F0F4F8", "line": "#D0D7DE",
        "muted": "#57606A", "text": "#1F2328", "ink": "#1F5F24", "chrome": "#0969DA",
        "key": "#0969DA", "value": "#1F2328", "section": "#9A4F00", "ok": "#2E7D32",
    },
}


def floyd_steinberg(gray: np.ndarray) -> np.ndarray:
    """1-bit serpentine Floyd-Steinberg dither. True marks a white cell."""
    work = gray.astype(np.float32) / 255.0
    height, width = work.shape
    out = np.zeros((height, width), dtype=bool)
    for y in range(height):
        step = 1 if y % 2 == 0 else -1
        for x in range(width)[::step]:
            old = work[y, x]
            new = 1.0 if old >= 0.5 else 0.0
            out[y, x] = new == 1.0
            err = old - new
            if 0 <= x + step < width:
                work[y, x + step] += err * 7 / 16
            if y + 1 < height:
                if 0 <= x - step < width:
                    work[y + 1, x - step] += err * 3 / 16
                work[y + 1, x] += err * 5 / 16
                if 0 <= x + step < width:
                    work[y + 1, x + step] += err * 1 / 16
    return out


def portrait_cells(theme: str) -> np.ndarray:
    """Boolean grid of cells to draw: light areas on dark, dark areas on light."""
    source = Image.open(PORTRAIT).convert("RGBA").resize((GRID_W, GRID_H), Image.Resampling.LANCZOS)
    alpha = np.asarray(source.getchannel("A"), dtype=np.float32) / 255.0
    backdrop = Image.new("RGBA", source.size, "black" if theme == "dark" else "white")
    backdrop.alpha_composite(source)
    gray = ImageOps.grayscale(backdrop.convert("RGB"))
    gray = ImageOps.autocontrast(gray, cutoff=1)
    gray = ImageEnhance.Contrast(gray).enhance(1.3)
    if theme == "dark":
        # Lit cells carry the image on dark: pull midtones down so skin is not a solid block.
        gray = gray.point(lambda v: round(255 * (v / 255) ** 1.6))
    gray = gray.filter(ImageFilter.UnsharpMask(radius=2, percent=170, threshold=1))
    white = floyd_steinberg(np.asarray(gray))
    cells = white if theme == "dark" else ~white
    return cells & (alpha > 0.1)


def cells_path(cells: np.ndarray) -> str:
    """One compact path: an absolute move per row, relative moves between dots."""
    rows = []
    for y in range(cells.shape[0]):
        xs = np.flatnonzero(cells[y])
        if xs.size == 0:
            continue
        parts = [f"M{xs[0]} {y}h.8"]
        prev = xs[0]
        for x in xs[1:]:
            parts.append(f"m{x - prev - 0.8:g} 0h.8")
            prev = x
        rows.append("".join(parts))
    return "".join(rows)


def text(x: float, y: float, body: str, fill: str, size: int = 13, weight: str = "400",
         anchor: str = "start", extra: str = "") -> str:
    return (f'<text x="{x:g}" y="{y:g}" fill="{fill}" font-family="{MONO}" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}"{extra}>{escape(body)}</text>')


def render(theme: str, profile: dict) -> str:
    c = THEMES[theme]
    rows = profile["yaml"]
    grid_w, grid_h = GRID_W * CELL, GRID_H * CELL
    px = FRAME_X + (FRAME_W - grid_w) / 2
    py = FRAME_Y + (FRAME_H - grid_h) / 2
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(profile["name"])} — {escape(profile["role"])}</title>',
        '<desc id="desc">Animated terminal banner with a dithered portrait and a YAML profile.</desc>',
        f'<defs><clipPath id="reveal"><rect x="{px:g}" y="{py:g}" width="{grid_w:g}" height="0">'
        f'<animate attributeName="height" from="0" to="{grid_h:g}" dur="{REVEAL_SECONDS}s" '
        f'fill="freeze"/></rect></clipPath>'
        f'<linearGradient id="scan" x1="0" x2="0" y1="0" y2="1"><stop stop-color="{c["chrome"]}" '
        f'stop-opacity="0"/><stop offset="1" stop-color="{c["chrome"]}" stop-opacity=".55"/>'
        f'</linearGradient></defs>',
        f'<rect width="{W}" height="{H}" rx="18" fill="{c["bg"]}"/>',
        f'<rect x="13" y="13" width="{W - 26}" height="{H - 26}" rx="13" fill="{c["panel"]}" '
        f'stroke="{c["line"]}"/>',
        f'<path d="M13 62H{W - 13}" stroke="{c["line"]}"/>',
        '<circle cx="38" cy="38" r="6" fill="#FF5F57"/><circle cx="59" cy="38" r="6" '
        'fill="#FEBC2E"/><circle cx="80" cy="38" r="6" fill="#28C840"/>',
        text(W / 2, 43, "vim ~/profile.yaml", c["muted"], 13, anchor="middle"),
        # Portrait panel.
        f'<rect x="35" y="88" width="418" height="472" rx="6" fill="{c["panel2"]}" stroke="{c["line"]}"/>',
        f'<path d="M35 124H453" stroke="{c["line"]}"/>',
        text(49, 111, "PORTRAIT.DITHER", c["chrome"], 13, "700", extra=' letter-spacing="1.2"'),
        text(438, 111, f"{GRID_W}×{GRID_H} / 1-BIT", c["muted"], 11, anchor="end"),
        f'<g clip-path="url(#reveal)"><path transform="translate({px:g} {py + 0.4 * CELL:g}) '
        f'scale({CELL})" d="{cells_path(portrait_cells(theme))}" fill="none" stroke="{c["ink"]}" '
        f'stroke-width=".8"/></g>',
        # Scanline: sweeps once with the reveal, then idles as a faint periodic sweep.
        f'<rect x="{px:g}" y="{py:g}" width="{grid_w:g}" height="18" fill="url(#scan)" opacity="0">'
        f'<animate attributeName="y" values="{py - 18:g};{py + grid_h - 18:g}" dur="{REVEAL_SECONDS}s" '
        f'fill="freeze"/><animate attributeName="opacity" values="1;1;0" keyTimes="0;.9;1" '
        f'dur="{REVEAL_SECONDS}s" fill="freeze"/></rect>',
        text(58, 551, "FLOYD-STEINBERG · SERPENTINE", c["muted"], 10),
    ]

    # Editor panel.
    ex, top, step = 470, 88, 21.5
    out += [
        f'<rect x="{ex}" y="{top}" width="460" height="472" rx="6" fill="{c["panel2"]}" '
        f'stroke="{c["line"]}"/>',
        f'<path d="M{ex} 124H{ex + 460}" stroke="{c["line"]}"/>',
        text(ex + 16, 111, "profile.yaml", c["chrome"], 13, "700"),
        text(ex + 444, 111, "[YAML]", c["muted"], 11, anchor="end"),
    ]
    for i, (indent, key, value) in enumerate(rows):
        y = 148 + i * step
        begin = f"{ROW_START + i * ROW_STEP:.2f}s"
        line_no = text(ex + 32, y, f"{i + 1:>2}", c["muted"], 12, anchor="end", extra=' opacity=".5"')
        x = ex + 46 + indent * 16
        key_color = c["section"] if indent == 0 else c["key"]
        body = text(x, y, f"{key}:", key_color, 13, "700" if indent == 0 else "400")
        if value:
            body += text(x + 7.8 * (len(key) + 1) + 6, y, value, c["value"], 13)
        out.append(f'{line_no}<g opacity="0"><animate attributeName="opacity" from="0" to="1" '
                   f'begin="{begin}" dur=".25s" fill="freeze"/>{body}</g>')
    status_y = 536
    out += [
        f'<rect x="{ex}" y="{status_y - 14}" width="460" height="22" fill="{c["line"]}" opacity=".55"/>',
        f'<rect x="{ex}" y="{status_y - 14}" width="66" height="22" fill="{c["ok"]}"/>',
        text(ex + 33, status_y + 1, "NORMAL", c["bg"], 11, "700", anchor="middle"),
        text(ex + 78, status_y + 1, "profile.yaml", c["text"], 12),
        text(ex + 448, status_y + 1, f"{len(rows)}L  utf-8  100%", c["muted"], 11, anchor="end"),
    ]
    cursor_y = 148 + len(rows) * step
    out.append(
        f'<rect x="{ex + 46}" y="{cursor_y - 12:g}" width="8" height="15" fill="{c["ok"]}" opacity="0">'
        f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.1s" '
        f'begin="{ROW_START + len(rows) * ROW_STEP:.2f}s" repeatCount="indefinite"/></rect>'
    )

    # Side panel: the Pedidos360 repositories.
    sx = 947
    out += [
        f'<rect x="{sx}" y="88" width="198" height="472" rx="6" fill="{c["panel2"]}" stroke="{c["line"]}"/>',
        f'<path d="M{sx} 124H{sx + 198}" stroke="{c["line"]}"/>',
        text(sx + 99, 111, f'@{profile["handle"]}', c["chrome"], 13, "700", anchor="middle"),
        text(sx + 16, 158, "$ ls pedidos360/", c["section"], 12, "700"),
    ]
    for i, (name, tech) in enumerate(SERVICES):
        y = 192 + i * 30
        delay = 0.3 * i
        out += [
            f'<circle cx="{sx + 22}" cy="{y - 4}" r="4.5" fill="{c["ok"]}">'
            f'<animate attributeName="opacity" values="1;.35;1" dur="2.4s" begin="{delay:.1f}s" '
            f'repeatCount="indefinite"/></circle>',
            text(sx + 36, y, name, c["text"], 13),
            text(sx + 182, y, tech, c["muted"], 11, anchor="end"),
        ]
    facts = [("java", "17 · Spring Boot 3.5"), ("db", "Oracle · Flyway"),
             ("auth", "Entra ID · Cognito"), ("iac", "Terraform · AWS")]
    out.append(f'<path d="M{sx + 16} 352H{sx + 182}" stroke="{c["line"]}"/>')
    for i, (key, value) in enumerate(facts):
        y = 380 + i * 40
        out += [text(sx + 16, y, key, c["muted"], 11), text(sx + 16, y + 17, value, c["text"], 12)]
    out.append("</svg>")
    return "".join(out)


def main() -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    for theme in THEMES:
        target = ASSETS / f"banner-{theme}.svg"
        target.write_text(render(theme, profile), encoding="utf-8")
        print(f"wrote {target.relative_to(ROOT)} ({target.stat().st_size // 1024} KiB)")


if __name__ == "__main__":
    main()
