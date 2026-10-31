#!/usr/bin/env python3
"""Render the radar charts and the whoami card of the GitHub profile.

Standard library only. Run from the repository root:

    python3 scripts/charts.py                      # redraw from data/*.json
    python3 scripts/charts.py --refresh-languages  # re-read languages from the GitHub API

Outputs:
    assets/radar-skills-{dark,light}.svg  from data/skills.json (self-assessed)
    assets/radar-langs-{dark,light}.svg   from data/languages.json (bytes per language)
    assets/whoami.svg                     from data/profile.json
"""

from __future__ import annotations

import argparse
import json
import math
import os
import urllib.request
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
ASSETS = ROOT / "assets"

MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
SANS = "ui-sans-serif,-apple-system,Segoe UI,Helvetica,Arial,sans-serif"

# Languages that describe markup, styling or packaging rather than code.
EXCLUDED_LANGUAGES = {"HTML", "CSS", "Dockerfile", "Makefile", "Batchfile"}
LANGUAGE_AXES = 6

THEMES = {
    "dark": {
        "bg": "#0B1117", "panel": "#0F1822", "grid": "#223142", "spoke": "#1A2633",
        "text": "#E6EDF3", "muted": "#8B9BAB", "fill": "#6DB33F", "accent": "#4FC3F7",
    },
    "light": {
        "bg": "#FFFFFF", "panel": "#F6F8FA", "grid": "#D0D7DE", "spoke": "#E4E8EC",
        "text": "#1F2328", "muted": "#57606A", "fill": "#2E7D32", "accent": "#0969DA",
    },
}


def num(value: float) -> str:
    return f"{value:.1f}".rstrip("0").rstrip(".")


def radar_svg(title: str, axes: list[dict], theme: str, unit: str = "") -> str:
    """Return an animated radar chart; values are 0-100 and scale to the outer ring."""
    c = THEMES[theme]
    width, height = 680, 500
    cx, cy, radius = width / 2, 262, 160
    count = len(axes)

    def point(index: int, scale: float) -> tuple[float, float]:
        angle = -math.pi / 2 + 2 * math.pi * index / count
        return cx + radius * scale * math.cos(angle), cy + radius * scale * math.sin(angle)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">',
        f'<rect width="{width}" height="{height}" rx="14" fill="{c["bg"]}"/>',
        f'<rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="13" fill="none" '
        f'stroke="{c["grid"]}"/>',
        f'<text x="{num(cx)}" y="40" text-anchor="middle" font-family="{MONO}" font-size="15" '
        f'font-weight="700" fill="{c["text"]}">{escape(title)}</text>',
    ]
    for ring in (0.25, 0.5, 0.75, 1.0):
        ring_points = " ".join(f"{num(x)},{num(y)}" for x, y in (point(i, ring) for i in range(count)))
        parts.append(f'<polygon points="{ring_points}" fill="none" stroke="{c["grid"]}"/>')
    for i in range(count):
        x, y = point(i, 1.0)
        parts.append(f'<line x1="{num(cx)}" y1="{num(cy)}" x2="{num(x)}" y2="{num(y)}" '
                     f'stroke="{c["spoke"]}"/>')

    values = [max(0.0, min(100.0, float(axis["value"]))) / 100 for axis in axes]
    shape = " ".join(f"{num(x)},{num(y)}" for x, y in (point(i, v) for i, v in enumerate(values)))
    # Grow the shape from the centre: scale around (cx, cy) by translating first.
    parts.append(
        f'<g transform="translate({num(cx)} {num(cy)})"><g>'
        f'<animateTransform attributeName="transform" type="scale" values="0.05;1" dur="1.2s" '
        f'calcMode="spline" keyTimes="0;1" keySplines="0.2 0.9 0.3 1" fill="freeze"/>'
        f'<g transform="translate({num(-cx)} {num(-cy)})">'
        f'<polygon points="{shape}" fill="{c["fill"]}" fill-opacity="0.22" stroke="{c["fill"]}" '
        f'stroke-width="2.5" stroke-linejoin="round"/>'
    )
    for i, v in enumerate(values):
        x, y = point(i, v)
        parts.append(f'<circle cx="{num(x)}" cy="{num(y)}" r="4" fill="{c["accent"]}"/>')
    parts.append("</g></g></g>")

    for i, axis in enumerate(axes):
        x, y = point(i, 1.17)
        anchor = "middle" if abs(x - cx) < 1 else ("start" if x > cx else "end")
        if abs(x - cx) < 1:
            y += -4 if y < cy else 14
        parts.append(
            f'<text x="{num(x)}" y="{num(y)}" text-anchor="{anchor}" font-family="{SANS}" '
            f'font-size="13" font-weight="600" fill="{c["text"]}">{escape(axis["label"])}'
            f'<tspan font-family="{MONO}" font-weight="400" fill="{c["muted"]}"> '
            f'{escape(str(axis.get("display", axis["value"])))}{unit}</tspan></text>'
        )
    parts.append("</svg>")
    return "".join(parts)


def refresh_languages(user: str) -> None:
    """Sum language bytes over the user's own public, non-fork repositories."""
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

    def get(url: str):
        request = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
        if token:
            request.add_header("Authorization", f"Bearer {token}")
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)

    repos = get(f"https://api.github.com/users/{user}/repos?per_page=100&type=owner")
    totals: dict[str, int] = {}
    for repo in repos:
        if repo["fork"]:
            continue
        for language, size in get(repo["languages_url"]).items():
            totals[language] = totals.get(language, 0) + size
    payload = {
        "_comment": "Bytes per language over public non-fork repositories. "
                    "Regenerate with: python3 scripts/charts.py --refresh-languages",
        "user": user,
        "bytes": dict(sorted(totals.items(), key=lambda item: -item[1])),
    }
    (DATA / "languages.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def language_axes() -> list[dict]:
    """Top languages by share; the largest language reaches the outer ring."""
    raw = json.loads((DATA / "languages.json").read_text(encoding="utf-8"))["bytes"]
    kept = {k: v for k, v in raw.items() if k not in EXCLUDED_LANGUAGES}
    top = sorted(kept.items(), key=lambda item: -item[1])[:LANGUAGE_AXES]
    total = sum(kept.values())
    largest = top[0][1]
    return [
        {"label": name, "value": 100 * size / largest, "display": round(100 * size / total)}
        for name, size in top
    ]


def whoami_svg(profile: dict) -> str:
    """A terminal card with identity, mission and expertise folders."""
    w, h = 960, 380
    green, cyan, amber, pink = "#6DB33F", "#4FC3F7", "#F2B84B", "#F28FAD"
    text, muted, line = "#C9D4DF", "#8B9BAB", "#223142"

    def t(x, y, body, fill, size=17, weight="400", extra=""):
        return (f'<text x="{x}" y="{y}" fill="{fill}" font-family="{MONO}" font-size="{size}" '
                f'font-weight="{weight}"{extra}>{escape(body)}</text>')

    slug = profile["name"].lower().replace(" ", "_")
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'role="img" aria-label="{escape(profile["name"])} — {escape(profile["role"])}">',
        f'<defs><linearGradient id="edge" x1="0" x2="1" y1="0" y2="1">'
        f'<stop stop-color="{green}"/><stop offset="1" stop-color="{cyan}"/></linearGradient></defs>',
        f'<rect width="{w}" height="{h}" rx="16" fill="#0B1117"/>',
        f'<rect x="8" y="8" width="{w - 16}" height="{h - 16}" rx="12" fill="none" '
        f'stroke="url(#edge)" stroke-width="2"/>',
        '<circle cx="34" cy="34" r="5.5" fill="#FF5F57"/><circle cx="53" cy="34" r="5.5" '
        'fill="#FEBC2E"/><circle cx="72" cy="34" r="5.5" fill="#28C840"/>',
        t(96, 40, f'{profile["handle"]}@github: ~', muted, 14),
        f'<path d="M28 58H{w - 28}" stroke="{line}"/>',
        f'<rect x="28" y="76" width="600" height="276" rx="9" fill="#0F1822" stroke="{line}"/>',
        t(48, 110, "$ whoami", green, 19, "700"),
        t(48, 142, slug, text),
        t(48 + 10.3 * len(slug) + 12, 142, "—", muted),
        t(48 + 10.3 * len(slug) + 40, 142, profile["role"], amber),
        f'<path d="M48 162H608" stroke="{line}"/>',
        t(48, 190, "where:", muted, 16), t(140, 190, f'{profile["location"]} ({profile["timezone"]})', cyan, 16),
        t(48, 216, "goal:", muted, 16), t(140, 216, profile["mission"], green, 16),
        t(48, 256, "$ ls expertise/", green, 19, "700"),
    ]
    for i, (folder, detail) in enumerate(profile["expertise"]):
        y = 286 + 25 * i
        parts += [t(48, y, folder, pink, 15), t(160, y, detail, text, 15)]

    # Right panel: a tiny live "health check" log, revealed line by line.
    parts += [
        f'<rect x="652" y="76" width="280" height="276" rx="9" fill="#0F1822" stroke="{line}"/>',
        t(672, 108, "$ ./healthcheck", amber, 15, "700"),
    ]
    checks = [("build", "PASS"), ("tests", "PASS"), ("migrations", "OK"),
              ("jwt.verify", "OK"), ("stock.lock", "HELD"), ("coffee", "LOW")]
    for i, (name, state) in enumerate(checks):
        y = 142 + 26 * i
        color = pink if state == "LOW" else green
        begin = f"{0.4 + 0.35 * i:.2f}s"
        parts.append(
            f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="{begin}" '
            f'dur="0.2s" fill="freeze"/>{t(672, y, name, text, 14)}'
            f'{t(800, y, "." * 6, line, 14)}{t(860, y, state, color, 14, "700")}</g>'
        )
    parts.append(t(672, 330, profile["status"], muted, 12))
    parts.append(
        f'<rect x="922" y="321" width="7" height="13" fill="{green}">'
        f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1.1s" '
        f'repeatCount="indefinite"/></rect>'
    )
    parts.append("</svg>")
    return "".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--refresh-languages", action="store_true",
                        help="re-read language bytes from the GitHub API before drawing")
    args = parser.parse_args()

    profile = json.loads((DATA / "profile.json").read_text(encoding="utf-8"))
    if args.refresh_languages:
        refresh_languages(profile["handle"])

    skills = json.loads((DATA / "skills.json").read_text(encoding="utf-8"))
    langs = language_axes()
    ASSETS.mkdir(exist_ok=True)
    for theme in THEMES:
        (ASSETS / f"radar-skills-{theme}.svg").write_text(
            radar_svg(skills["title"], skills["axes"], theme), encoding="utf-8")
        (ASSETS / f"radar-langs-{theme}.svg").write_text(
            radar_svg("Language Share (% of code)", langs, theme, unit="%"), encoding="utf-8")
    (ASSETS / "whoami.svg").write_text(whoami_svg(profile), encoding="utf-8")
    print("wrote radar-skills, radar-langs (dark/light) and whoami.svg")


if __name__ == "__main__":
    main()
