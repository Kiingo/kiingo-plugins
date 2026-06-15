#!/usr/bin/env python3
"""
Generate the Vistage whimsy icon set (navy on transparent) as PNGs.

The 18 icons are already pre-rendered in ../assets/icons, so you normally do NOT
need to run this. Run it only to add a new icon or change the palette.

Requires: cairosvg  (pip install cairosvg --break-system-packages)
Fonts: Montserrat must be on fontconfig for the 'parking' glyph (see SKILL.md).
"""
import os, cairosvg

NAVY = "#003E5E"
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "icons")
os.makedirs(OUT, exist_ok=True)

def svg(inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
            f'<g fill="none" stroke="{NAVY}" stroke-width="6.5" '
            f'stroke-linecap="round" stroke-linejoin="round">{inner}</g></svg>')

N = NAVY
ICONS = {
"whistle": f'<circle cx="42" cy="58" r="19"/><rect x="58" y="49" width="26" height="15" rx="5"/><circle cx="42" cy="33" r="5"/><path d="M42 38 V46"/>',
"stopwatch": f'<circle cx="50" cy="57" r="23"/><rect x="43" y="22" width="14" height="9" rx="2"/><path d="M50 31 V36"/><path d="M69 37 L74 32"/><path d="M50 57 V44"/><path d="M50 57 L61 62"/>',
"parking": f'<rect x="24" y="18" width="52" height="64" rx="10"/><text x="50" y="68" font-family="Montserrat" font-size="50" font-weight="800" fill="{N}" stroke="none" text-anchor="middle">P</text>',
"bolt": f'<path d="M58 10 L33 54 L47 54 L42 90 L70 43 L53 43 Z" fill="{N}" stroke="{N}" stroke-width="4"/>',
"owl": f'<ellipse cx="50" cy="60" rx="24" ry="28"/><path d="M32 38 L36 22 L46 36"/><path d="M68 38 L64 22 L54 36"/><circle cx="41" cy="50" r="9"/><circle cx="59" cy="50" r="9"/><circle cx="41" cy="50" r="2.6" fill="{N}"/><circle cx="59" cy="50" r="2.6" fill="{N}"/><path d="M50 56 L46 62 L54 62 Z" fill="{N}"/><path d="M40 86 L40 90"/><path d="M60 86 L60 90"/>',
"thermometer": f'<rect x="42" y="16" width="16" height="50" rx="8"/><circle cx="50" cy="74" r="13"/><rect x="46" y="44" width="8" height="30" fill="{N}" stroke="none"/><circle cx="50" cy="74" r="8" fill="{N}" stroke="none"/><path d="M61 26 H67"/><path d="M61 36 H67"/><path d="M61 46 H67"/>',
"glove": f'<path d="M32 44 Q32 26 50 26 Q70 26 70 46 L70 64 Q70 73 61 73 L41 73 Q32 73 32 64 Z"/><path d="M32 50 Q22 50 22 60 Q22 70 32 68"/><rect x="39" y="73" width="30" height="12" rx="3"/><path d="M41 46 Q50 52 60 46"/>',
"quote": f'<path d="M22 24 H78 Q84 24 84 30 V58 Q84 64 78 64 H44 L30 80 L33 64 H22 Q16 64 16 58 V30 Q16 24 22 24 Z"/><text x="50" y="56" font-family="Georgia,serif" font-size="40" font-weight="700" fill="{N}" stroke="none" text-anchor="middle">&#8220;&#8221;</text>',
"lock": f'<rect x="28" y="46" width="44" height="38" rx="7"/><path d="M38 46 V38 Q38 22 50 22 Q62 22 62 38 V46"/><circle cx="50" cy="62" r="4" fill="{N}" stroke="none"/><path d="M50 66 V72"/>',
"thumbsup": f'<path d="M44 46 L44 32 Q44 24 51 24 Q57 24 57 31 L57 48 L72 48 Q79 48 78 55 L74 74 Q73 80 66 80 L44 80 Z"/><rect x="26" y="50" width="14" height="32" rx="3"/>',
"phoneoff": f'<rect x="36" y="20" width="28" height="52" rx="6"/><path d="M44 28 H56"/><circle cx="50" cy="64" r="2.4" fill="{N}" stroke="none"/><path d="M24 22 L78 78" stroke-width="7"/>',
"confetti": f'<path d="M26 82 L48 50 L60 62 Z" fill="{N}" stroke="{N}" stroke-width="3"/><circle cx="66" cy="32" r="3.2" fill="{N}" stroke="none"/><circle cx="78" cy="44" r="3.2" fill="{N}" stroke="none"/><circle cx="60" cy="22" r="3.2" fill="{N}" stroke="none"/><path d="M70 60 L76 66"/><path d="M52 30 L57 35"/>',
"give": f'<path d="M32 82 V60 Q32 56 36 56 H60 Q68 56 68 64 V82 Z"/><path d="M38 56 V44 Q38 40 42 40 Q46 40 46 44 V56"/><path d="M50 56 V40 Q50 36 54 36 Q58 36 58 40 V56"/><path d="M62 56 V46 Q62 42 66 42 Q70 42 70 46 V64"/><path d="M50 14 L53 24 L63 27 L53 30 L50 40 L47 30 L37 27 L47 24 Z" fill="{N}" stroke="{N}" stroke-width="2"/>',
"gift": f'<rect x="28" y="44" width="44" height="36" rx="3"/><rect x="23" y="34" width="54" height="13" rx="3"/><path d="M50 34 V80"/><path d="M50 34 Q40 34 40 26 Q40 21 45 23 Q50 26 50 34"/><path d="M50 34 Q60 34 60 26 Q60 21 55 23 Q50 26 50 34"/>',
"heart": f'<path d="M50 80 L26 54 Q16 42 28 32 Q40 24 50 38 Q60 24 72 32 Q84 42 74 54 Z" fill="{N}" stroke="{N}" stroke-width="4"/>',
"chat": f'<path d="M22 24 H78 Q84 24 84 30 V56 Q84 62 78 62 H44 L30 78 L33 62 H22 Q16 62 16 56 V30 Q16 24 22 24 Z"/><circle cx="36" cy="43" r="3" fill="{N}" stroke="none"/><circle cx="50" cy="43" r="3" fill="{N}" stroke="none"/><circle cx="64" cy="43" r="3" fill="{N}" stroke="none"/>',
"cake": f'<rect x="26" y="54" width="48" height="26" rx="4"/><path d="M26 64 Q34 72 42 64 Q50 72 58 64 Q66 72 74 64"/><path d="M38 54 V42"/><path d="M50 54 V42"/><path d="M62 54 V42"/><circle cx="38" cy="38" r="2.8" fill="{N}" stroke="none"/><circle cx="50" cy="38" r="2.8" fill="{N}" stroke="none"/><circle cx="62" cy="38" r="2.8" fill="{N}" stroke="none"/>',
"star": f'<path d="M50 16 L60 40 L86 42 L66 59 L72 84 L50 70 L28 84 L34 59 L14 42 L40 40 Z" fill="{N}" stroke="{N}" stroke-width="4"/>',
}

if __name__ == "__main__":
    for name, inner in ICONS.items():
        cairosvg.svg2png(bytestring=svg(inner).encode(),
                         write_to=os.path.join(OUT, f"{name}.png"),
                         output_width=240, output_height=240)
    print("rendered", len(ICONS), "icons ->", OUT)
