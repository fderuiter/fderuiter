#!/usr/bin/env python3
"""Build the profile's SVG art: the animated banner, project cards and portfolio card.

Every image comes in a dark and a light version so the README can swap them with
<picture> to match the viewer's GitHub theme. The SVGs are self-contained: no
scripts, no web fonts, no remote assets. Animations are CSS only and switch off
for viewers who ask for reduced motion.

Run from the repository root:  python3 scripts/build_profile_art.py
Edit the PROJECTS list below to change a card's text.
"""

from __future__ import annotations

import base64
import math
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
FONT = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

THEMES = {
    "dark": {
        "bg": "#0f1218", "panel": "#161b22", "border": "#2a313c", "rule": "#232934",
        "text": "#f4f4f5", "muted": "#a1a1aa", "chip": "#1f2530", "chip_text": "#d4d4d8",
        "gold": "#fbbf24",
    },
    "light": {
        "bg": "#ffffff", "panel": "#f6f8fa", "border": "#d0d7de", "rule": "#e5e7eb",
        "text": "#18181b", "muted": "#52525b", "chip": "#f1f3f5", "chip_text": "#3f3f46",
        "gold": "#b45309",
    },
}

REDUCED_MOTION = "@media (prefers-reduced-motion: reduce) { * { animation: none !important; } }"


def write(name: str, svg: str) -> None:
    path = ASSETS / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(svg.strip() + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- banner

TAGLINES = [
    "I build software for clinical research.",
    "I make complicated things usable.",
    "I put lasers on a loon once. On purpose.",
]
CYCLE = 12.0  # seconds for all three lines


def banner(theme: str) -> str:
    t = THEMES[theme]
    per = CYCLE / len(TAGLINES)
    x0, y0, size = 82, 178, 27
    char_w = 14.2  # textLength per character keeps typing steps exact in any font
    lines, styles = [], []
    for i, line in enumerate(TAGLINES):
        n = len(line)
        width = round(n * char_w, 1)
        start = i * per / CYCLE * 100
        typed = start + 1.6 / CYCLE * 100
        hold = start + (per - 0.7) / CYCLE * 100
        gone = start + (per - 0.2) / CYCLE * 100
        kf = (
            f"@keyframes type{i} {{"
            f" 0% {{ transform: scaleX(0); }}"
            f" {start:.2f}% {{ transform: scaleX(0); animation-timing-function: steps({n}, end); }}"
            f" {typed:.2f}% {{ transform: scaleX(1); }}"
            f" {hold:.2f}% {{ transform: scaleX(1); animation-timing-function: steps({n}, end); }}"
            f" {gone:.2f}% {{ transform: scaleX(0); }}"
            f" 100% {{ transform: scaleX(0); }} }}"
            f"@keyframes caret{i} {{"
            f" 0% {{ transform: translateX(0); opacity: 0; }}"
            + (f" {start - 0.01:.2f}% {{ transform: translateX(0); opacity: 0; }}" if i else "")
            + f" {start:.2f}% {{ transform: translateX(0); opacity: 1; animation-timing-function: steps({n}, end); }}"
            f" {typed:.2f}% {{ transform: translateX({width}px); opacity: 1; }}"
            f" {hold:.2f}% {{ transform: translateX({width}px); opacity: 1; animation-timing-function: steps({n}, end); }}"
            f" {gone:.2f}% {{ transform: translateX(0); opacity: 1; }}"
            f" {gone + 0.01:.2f}% {{ opacity: 0; }}"
            f" 100% {{ opacity: 0; }} }}"
            f".clip{i} {{ transform-box: fill-box; transform-origin: left; transform: scaleX(0);"
            f" animation: type{i} {CYCLE}s infinite; }}"
            f".caret{i} {{ opacity: 0; animation: caret{i} {CYCLE}s infinite; }}"
        )
        styles.append(kf)
        # Reduced motion: show the first line, fully typed.
        if i == 0:
            styles.append(
                "@media (prefers-reduced-motion: reduce) { .clip0 { transform: scaleX(1); }"
                f" .caret0 {{ opacity: 1; transform: translateX({width}px); }} }}"
            )
        lines.append(
            f'<clipPath id="c{i}"><rect class="clip{i}" x="{x0}" y="{y0 - 26}" width="{width + 4}" height="36"/></clipPath>'
            f'<text clip-path="url(#c{i})" x="{x0}" y="{y0}" font-family="{MONO}" font-size="{size}"'
            f' textLength="{width}" lengthAdjust="spacingAndGlyphs" fill="{t["text"]}">{escape(line)}</text>'
            f'<rect class="caret{i}" x="{x0 + 3}" y="{y0 - 24}" width="13" height="30" fill="{t["gold"]}"/>'
        )
    styles.append(REDUCED_MOTION.replace("* {", ".pulse, .spin {"))
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="280" viewBox="0 0 1200 280" role="img" aria-labelledby="title desc">
  <title id="title">Fred de Ruiter: clinical data, useful software, curious side projects.</title>
  <desc id="desc">Banner that types three lines in turn: {escape(' '.join(TAGLINES))}</desc>
  <style>
    {' '.join(styles)}
    @keyframes pulse {{ 0%, 100% {{ opacity: .35; }} 50% {{ opacity: 1; }} }}
    .pulse {{ animation: pulse 3s ease-in-out infinite; }}
    .pulse.b {{ animation-delay: 1s; }} .pulse.c {{ animation-delay: 2s; }}
    @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
    .spin {{ transform-box: view-box; transform-origin: 1060px 140px; animation: spin 40s linear infinite; }}
  </style>
  <rect x="0.5" y="0.5" width="1199" height="279" rx="20" fill="{t["bg"]}" stroke="{t["border"]}"/>
  <rect x="48" y="62" width="8" height="150" rx="4" fill="{t["gold"]}"/>
  <text x="82" y="84" font-family="{FONT}" font-size="16" font-weight="700" letter-spacing="3" fill="{t["gold"]}">CLINICAL DATA · USEFUL SOFTWARE · MINNEAPOLIS</text>
  <text x="80" y="138" font-family="{FONT}" font-size="50" font-weight="800" fill="{t["text"]}">Howdy, I’m Fred de Ruiter.</text>
  {''.join(lines)}
  <text x="82" y="236" font-family="{FONT}" font-size="17" fill="{t["muted"]}">deruiter.dev  ·  Python · TypeScript · C# · Rust</text>
  <g class="spin" fill="none" stroke="{t["gold"]}" stroke-width="2" opacity=".55">
    <circle cx="1060" cy="140" r="92" stroke-dasharray="4 10"/>
  </g>
  <g fill="none" stroke="{t["gold"]}" stroke-width="3">
    <circle cx="1060" cy="140" r="26"/>
    <path d="M1060 114V72M1060 166v42M1034 140h-42M1086 140h42" stroke-opacity=".5"/>
  </g>
  <g fill="{t["gold"]}">
    <circle class="pulse" cx="1060" cy="64" r="9"/>
    <circle class="pulse b" cx="1136" cy="140" r="9"/>
    <circle class="pulse c" cx="1060" cy="216" r="9"/>
    <circle class="pulse b" cx="984" cy="140" r="9"/>
  </g>
</svg>"""


# --------------------------------------------------------------------------- Laser Loon

LOON_SRC = ASSETS / "src" / "laser-loon.svg"  # Fred's CC0 artwork from fderuiter/Laser_Loon
LOON_BLUE, LOON_YELLOW = "#0156d9", "#fdf98b"
EYE = (762.04, 288.11)  # the loon's eye, where the lasers start
HIT = (1100, 440)       # where the beams land on the fish


def loon_parts() -> dict[str, str]:
    """Split the flag artwork into the pieces that move separately."""
    src = LOON_SRC.read_text(encoding="utf-8")
    elements = re.findall(r"<(?:path|rect|circle)\b[^>]*/>", src)
    colors = {"cls-1": LOON_BLUE, "cls-2": "#fff", "cls-3": LOON_YELLOW}

    def paint(el: str) -> str:
        m = re.search(r'class="(cls-\d)"', el)
        fill = colors[m.group(1)] if m else "#000"
        return re.sub(r'\s*class="cls-\d"', "", el).replace("/>", f' fill="{fill}"/>')

    els = [paint(e) for e in elements]
    # Index ranges follow the element order in the source file (checked by hand):
    # 0 background, 1-5 fish, 6-7 loon body, 8 eye, 9-161 loon markings,
    # 162 fish eye, 163 laser beams.
    assert len(els) == 164, f"unexpected Laser Loon artwork: {len(els)} elements"
    return {
        "fish": "".join(els[1:6]) + els[162],
        "loon": "".join(els[6:8]) + "".join(els[9:162]),
        "eye": els[8],
        "lasers": els[163],
    }


LOON_CSS = f"""
  @keyframes bob {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(10px); }} }}
  @keyframes fire {{ 0%, 8% {{ transform: scale(0); opacity: 0; }} 14% {{ transform: scale(1); opacity: 1; }}
    18% {{ opacity: .55; }} 22% {{ opacity: 1; }} 26% {{ opacity: .7; }} 30% {{ opacity: 1; }}
    44% {{ transform: scale(1); opacity: 1; }} 50%, 100% {{ transform: scale(1); opacity: 0; }} }}
  @keyframes glow {{ 0%, 6% {{ transform: scale(1); opacity: .0; }} 14%, 44% {{ transform: scale(2.6); opacity: .55; }}
    52%, 100% {{ transform: scale(1); opacity: 0; }} }}
  @keyframes zap {{ 0%, 13% {{ transform: scale(0) rotate(0); opacity: 0; }} 18% {{ transform: scale(1.1) rotate(20deg); opacity: 1; }}
    30% {{ transform: scale(.8) rotate(40deg); opacity: 1; }} 44% {{ transform: scale(1) rotate(60deg); opacity: .9; }}
    50%, 100% {{ transform: scale(0) rotate(80deg); opacity: 0; }} }}
  @keyframes dodge {{ 0%, 14% {{ transform: translate(0, 0); }} 17% {{ transform: translate(6px, -4px); }}
    20% {{ transform: translate(-5px, 3px); }} 23% {{ transform: translate(4px, -2px); }} 26%, 44% {{ transform: translate(0, 0); }}
    50% {{ transform: translate(14px, 0) rotate(-2deg); }} 70%, 100% {{ transform: translate(0, 0); }} }}
  @keyframes drift {{ from {{ transform: translateX(0); }} to {{ transform: translateX(-240px); }} }}
  .loon {{ animation: bob 4s ease-in-out infinite; }}
  .lasers {{ transform-box: view-box; transform-origin: {EYE[0]}px {EYE[1]}px; animation: fire 3.2s infinite; }}
  .glow {{ transform-box: view-box; transform-origin: {EYE[0]}px {EYE[1]}px; animation: glow 3.2s infinite; }}
  .zap {{ transform-box: view-box; transform-origin: {HIT[0]}px {HIT[1]}px; animation: zap 3.2s infinite; }}
  .fish {{ transform-box: view-box; transform-origin: 1300px 560px; animation: dodge 3.2s infinite; }}
  .ripple {{ animation: drift 6s linear infinite; }}
  @media (prefers-reduced-motion: reduce) {{
    .loon, .lasers, .glow, .zap, .fish, .ripple {{ animation: none !important; }}
    .glow, .zap {{ opacity: 0; }}
  }}
"""


def loon_scene(ripples: bool = True) -> str:
    """The flag artwork as animated layers, in the source's 1920x1080 coordinates."""
    parts = loon_parts()
    points = []
    for k in range(16):  # an eight-pointed spark where the beams land
        r = 46 if k % 2 == 0 else 16
        points.append(f"{HIT[0] + r * math.cos(k * math.pi / 8):.1f},{HIT[1] + r * math.sin(k * math.pi / 8):.1f}")
    star = " ".join(points)
    waves = ""
    if ripples:
        wave = "".join(f"q30 -14 60 0 t60 0" for _ in range(20))
        waves = (f'<g class="ripple" fill="none" stroke="#fff" stroke-opacity=".18" stroke-width="5" stroke-linecap="round">'
                 f'<path d="M0 760 {wave}"/><path d="M120 820 {wave}"/><path d="M40 880 {wave}"/></g>')
    return (
        f'<rect width="1920" height="1080" fill="{LOON_BLUE}"/>{waves}'
        f'<g class="fish">{parts["fish"]}</g>'
        f'<g class="loon">{parts["loon"]}'
        f'<g class="lasers">{parts["lasers"]}</g>'
        f'<circle class="glow" cx="{EYE[0]}" cy="{EYE[1]}" r="13" fill="{LOON_YELLOW}"/>{parts["eye"]}</g>'
        f'<polygon class="zap" points="{star}" fill="{LOON_YELLOW}"/>'
    )


def laser_loon() -> str:
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1920 1080" role="img" aria-labelledby="title">
  <title id="title">Laser Loon: a loon on a blue Minnesota flag fires yellow laser beams from its eye at a startled fish.</title>
  <style>{LOON_CSS}</style>
  <defs><clipPath id="flag"><rect width="1920" height="1080" rx="40"/></clipPath></defs>
  <g clip-path="url(#flag)">{loon_scene()}</g>
</svg>"""


# --------------------------------------------------------------------------- project cards

PROJECTS = [
    {
        "slug": "cadence", "accent": ("#2dd4bf", "#0f766e"),
        "label": "CLINICAL RESEARCH PLATFORM", "name": "Cadence",
        "hook": ["One clinical kernel holds the truth.", "EDC, CTMS and the rest are apps on it."],
        "chips": [".NET 10", "C# 14", "Vue 3", "PostgreSQL"],
        "cta": "Explore the staff demo", "glyph": "orbit",
    },
    {
        "slug": "oxidizemath", "accent": ("#fb923c", "#c2410c"),
        "label": "MATH AND SIMULATION", "name": "OxidizeMath",
        "hook": ["MRI physics, chaos, fluids and quantum", "mechanics you can play with."],
        "chips": ["Rust", "egui", "WebAssembly", "Lean 4"],
        "cta": "Run it in your browser", "glyph": "wave",
    },
    {
        "slug": "wedding", "accent": ("#f472b6", "#be185d"),
        "label": "SELF-HOSTED WEDDING SITE", "name": "Wedding website",
        "hook": ["RSVPs, seating charts, photos, a registry.", "Your guests’ data on your own server."],
        "chips": ["Next.js", "TypeScript", "PostgreSQL", "Three.js"],
        "cta": "Tour the demo wedding", "glyph": "rings",
    },
    {
        "slug": "qrcraftly", "accent": ("#22d3ee", "#0e7490"),
        "label": "BROWSER QR STUDIO", "name": "QRCraftly",
        "hook": ["Styled QR codes that still scan.", "No ads, no tracking, no sign-up."],
        "chips": ["React 19", "TypeScript", "Rust → WASM"],
        "cta": "Make a QR code", "glyph": "qr",
    },
    {
        "slug": "imednet", "accent": ("#60a5fa", "#1d4ed8"),
        "label": "CLINICAL API TOOLKIT", "name": "imednet-toolkit",
        "hook": ["Python SDK and CLI for the iMednet API.", "Try it live in the browser with Pyodide."],
        "chips": ["Python", "CLI", "PyPI", "Pyodide"],
        "cta": "Run the live tutorial", "glyph": "terminal",
    },
    {
        "slug": "sortify", "accent": ("#4ade80", "#15803d"),
        "label": "OFFLINE FILE ORGANIZER", "name": "Sortify",
        "hook": ["Point it at a messy folder. It reads each file", "and sorts it, offline, with a dry run and undo."],
        "chips": ["Python", "Textual", "scikit-learn", "SQLCipher"],
        "cta": "See how it sorts", "glyph": "folders",
    },
]


def glyph(kind: str, c: str) -> str:
    cx, cy = 512, 78
    if kind == "orbit":
        dots = "".join(
            f'<circle cx="{cx + 40 * x:.1f}" cy="{cy + 40 * y:.1f}" r="6" fill="{c}"/>'
            for x, y in [(1, 0), (.5, .866), (-.5, .866), (-1, 0), (-.5, -.866), (.5, -.866)]
        )
        return (f'<g class="spin" style="transform-origin:{cx}px {cy}px">'
                f'<circle cx="{cx}" cy="{cy}" r="40" fill="none" stroke="{c}" stroke-opacity=".4" stroke-width="2"/>{dots}</g>'
                f'<circle cx="{cx}" cy="{cy}" r="15" fill="{c}"/>')
    if kind == "wave":
        return (f'<path d="M462 78h100M512 38v80" stroke="{c}" stroke-opacity=".35" stroke-width="2"/>'
                f'<path d="M466 78c12-44 34-44 46 0s34 44 46 0" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round"/>'
                f'<circle class="pulse" cx="512" cy="78" r="8" fill="{c}"/>')
    if kind == "rings":
        return (f'<circle cx="494" cy="82" r="28" fill="none" stroke="{c}" stroke-width="5"/>'
                f'<circle cx="530" cy="82" r="28" fill="none" stroke="{c}" stroke-width="5"/>'
                f'<path class="pulse" d="M494 46l6-8 6 8-6 6z" fill="{c}"/>')
    if kind == "qr":
        out = []
        for ox, oy in [(470, 36), (526, 36), (470, 92)]:
            out.append(f'<rect x="{ox + 3}" y="{oy + 3}" width="26" height="26" rx="4" fill="none" stroke="{c}" stroke-width="5"/>'
                       f'<rect x="{ox + 11}" y="{oy + 11}" width="10" height="10" rx="2" fill="{c}"/>')
        cells = [(530, 96), (546, 96), (538, 108), (530, 120), (554, 112), (546, 124)]
        for k, (x, y) in enumerate(cells):
            cls = ' class="pulse"' if k % 2 else ""
            out.append(f'<rect{cls} x="{x}" y="{y}" width="9" height="9" rx="1.5" fill="{c}"/>')
        return "".join(out)
    if kind == "terminal":
        return (f'<rect x="464" y="40" width="96" height="76" rx="10" fill="none" stroke="{c}" stroke-width="4"/>'
                f'<path d="M478 64l14 12-14 12" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
                f'<rect class="blink" x="500" y="84" width="22" height="6" rx="2" fill="{c}"/>')
    if kind == "scale":
        return (f'<path d="M512 42v74M490 116h44M470 58h84" stroke="{c}" stroke-width="5" stroke-linecap="round"/>'
                f'<g class="tilt" style="transform-origin:512px 58px">'
                f'<path d="M470 58l-14 30h28zM554 58l-14 30h28z" fill="none" stroke="{c}" stroke-width="3.5" stroke-linejoin="round"/></g>'
                f'<circle cx="512" cy="42" r="6" fill="{c}"/>')
    if kind == "folders":
        docs = "".join(
            f'<g class="drop d{k}"><rect x="{x}" y="22" width="20" height="26" rx="3" fill="none" stroke="{c}" stroke-width="3"/>'
            f'<path d="M{x + 5} 31h10M{x + 5} 38h7" stroke="{c}" stroke-width="2.5" stroke-linecap="round"/></g>'
            for k, x in enumerate((476, 502, 528))
        )
        return (docs +
                f'<path d="M462 72h30l8 9h52a6 6 0 0 1 6 6v34a6 6 0 0 1-6 6H468a6 6 0 0 1-6-6z" fill="{c}" fill-opacity=".18" stroke="{c}" stroke-width="4" stroke-linejoin="round"/>')
    raise ValueError(kind)


def card(p: dict, theme: str) -> str:
    t = THEMES[theme]
    accent = p["accent"][0 if theme == "dark" else 1]
    chips, x = [], 32
    for chip in p["chips"]:
        w = round(len(chip) * 8.6 + 26)
        chips.append(f'<rect x="{x}" y="214" width="{w}" height="30" rx="15" fill="{t["chip"]}" stroke="{t["border"]}"/>'
                     f'<text x="{x + w / 2}" y="234" text-anchor="middle" font-family="{FONT}" font-size="15" fill="{t["chip_text"]}">{escape(chip)}</text>')
        x += w + 8
    hook = "".join(f'<text x="32" y="{148 + 28 * i}" font-family="{FONT}" font-size="20" fill="{t["muted"]}">{escape(line)}</text>'
                   for i, line in enumerate(p["hook"]))
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="320" viewBox="0 0 600 320" role="img" aria-labelledby="title">
  <title id="title">{escape(p["name"])}: {escape(' '.join(p["hook"]))} {escape(p["cta"])}.</title>
  <style>
    @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
    @keyframes pulse {{ 0%, 100% {{ opacity: .3; }} 50% {{ opacity: 1; }} }}
    @keyframes blink {{ 0%, 49% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}
    @keyframes tilt {{ 0%, 100% {{ transform: rotate(-6deg); }} 50% {{ transform: rotate(6deg); }} }}
    .spin {{ animation: spin 24s linear infinite; }}
    .pulse {{ animation: pulse 2.4s ease-in-out infinite; }}
    .blink {{ animation: blink 1.1s step-end infinite; }}
    .tilt {{ animation: tilt 5s ease-in-out infinite; }}
    @keyframes drop {{ 0%, 10% {{ transform: translateY(0); opacity: 1; }} 30% {{ transform: translateY(58px); opacity: 0; }}
      31%, 60% {{ transform: translateY(0); opacity: 0; }} 75%, 100% {{ transform: translateY(0); opacity: 1; }} }}
    .drop {{ animation: drop 3.6s ease-in infinite; }} .d1 {{ animation-delay: .5s; }} .d2 {{ animation-delay: 1s; }}
    {REDUCED_MOTION}
  </style>
  <rect x="1" y="1" width="598" height="318" rx="18" fill="{t["bg"]}" stroke="{t["border"]}" stroke-width="2"/>
  <rect x="1" y="1" width="598" height="6" rx="3" fill="{accent}"/>
  <text x="32" y="58" font-family="{FONT}" font-size="14" font-weight="700" letter-spacing="2.5" fill="{accent}">{escape(p["label"])}</text>
  <text x="30" y="104" font-family="{FONT}" font-size="38" font-weight="800" fill="{t["text"]}">{escape(p["name"])}</text>
  {glyph(p["glyph"], accent)}
  {hook}
  {''.join(chips)}
  <path d="M32 268H568" stroke="{t["rule"]}"/>
  <text x="32" y="298" font-family="{FONT}" font-size="18" font-weight="700" fill="{accent}">{escape(p["cta"])}  →</text>
</svg>"""


# --------------------------------------------------------------------------- portfolio card

def portfolio(theme: str) -> str:
    t = THEMES[theme]
    shot = base64.b64encode((ASSETS / "src" / "deruiter-home.webp").read_bytes()).decode()
    items = [("Clinical", "Design a CRF, then trace a fictional study to tables"),
             ("Labs", "Logic proofs, a 3D MRI brain, an outage simulator"),
             ("Arcade", "Twelve browser games, one about a Costco wedding")]
    rows = "".join(
        f'<text x="48" y="{196 + 40 * i}" font-family="{FONT}" font-size="19" fill="{t["muted"]}">'
        f'<tspan font-weight="700" fill="{t["text"]}">{a}</tspan>  {escape(b)}</text>'
        for i, (a, b) in enumerate(items))
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1200" height="400" viewBox="0 0 1200 400" role="img" aria-labelledby="title">
  <title id="title">Visit my portfolio at deruiter.dev: clinical demos, interactive labs and twelve arcade games, most of it running in your browser.</title>
  <style>
    @keyframes nudge {{ 0%, 100% {{ transform: translateX(0); }} 50% {{ transform: translateX(6px); }} }}
    .nudge {{ animation: nudge 1.6s ease-in-out infinite; }}
    {REDUCED_MOTION}
  </style>
  <defs><clipPath id="shot"><rect x="680" y="65" width="480" height="270" rx="14"/></clipPath></defs>
  <rect x="1" y="1" width="1198" height="398" rx="22" fill="{t["bg"]}" stroke="{t["gold"]}" stroke-width="2"/>
  <text x="48" y="78" font-family="{FONT}" font-size="15" font-weight="700" letter-spacing="3" fill="{t["gold"]}">MY PORTFOLIO</text>
  <text x="46" y="134" font-family="{FONT}" font-size="54" font-weight="800" fill="{t["text"]}">deruiter.dev</text>
  {rows}
  <rect x="48" y="300" width="300" height="56" rx="28" fill="{t["gold"]}"/>
  <text x="80" y="335" font-family="{FONT}" font-size="21" font-weight="800" fill="{THEMES["dark"]["bg"] if theme == "dark" else "#ffffff"}">Visit the portfolio</text>
  <text class="nudge" x="296" y="336" font-family="{FONT}" font-size="24" font-weight="800" fill="{THEMES["dark"]["bg"] if theme == "dark" else "#ffffff"}">→</text>
  <image x="680" y="65" width="480" height="270" preserveAspectRatio="xMidYMid slice" clip-path="url(#shot)" xlink:href="data:image/webp;base64,{shot}"/>
  <rect x="680" y="65" width="480" height="270" rx="14" fill="none" stroke="{t["border"]}" stroke-width="2"/>
</svg>"""


def main() -> None:
    write("laser-loon.svg", laser_loon())
    for theme in THEMES:
        write(f"banner-{theme}.svg", banner(theme))
        write(f"portfolio-{theme}.svg", portfolio(theme))
        for p in PROJECTS:
            write(f"cards/{p['slug']}-{theme}.svg", card(p, theme))


if __name__ == "__main__":
    main()
