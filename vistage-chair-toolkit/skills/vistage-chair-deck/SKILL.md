---
name: vistage-chair-deck
description: >-
  Create or rebuild Vistage Chair meeting PowerPoint decks in a uniform Vistage
  navy-and-gold brand system with Montserrat fonts, official logos, consistent
  headers/footers, custom role icons, photo layouts, agendas, operating
  agreements, birthdays, anniversaries, closing exercises, and a native
  issue-processing funnel. Use for Vistage deck cleanup, rebranding,
  standardization, or new Chair meeting slides.
---

# Vistage Chair Deck Builder

Build clean, uniform, on-brand Vistage Chair meeting decks. This skill exists
because Chair decks tend to drift: mixed fonts, clip art from a dozen sources,
inconsistent footers, blank "transition" slides, and leftover content from prior
months. The fix is to pour the Chair's *content* into ONE disciplined brand
system while keeping the *personality* (the playful role icons, the warm photos)
that makes a meeting feel like theirs.

Guiding principle: **whimsy in the subject, discipline in the execution.**
Recreate fun ideas (a whistle for the Break Enforcer, an owl Historian) as
original icons in a single style and palette — never paste mismatched third-party
clip art, and never copy a competitor's or Vistage's own raster diagrams; rebuild
them natively so they're uniform and yours to use.

## What's bundled

- `assets/logos/` — official Vistage marks. Use `vistage-wordmark-white.png`
  (clean RGBA white wordmark, for navy backgrounds) and `vistage-v-mark.png`
  (footer mark). Others are source/full-color variants.
- `assets/fonts/` — Montserrat (Regular→ExtraBold). Vistage's real face is Sofia
  Pro (paid); Montserrat is the free geometric near-match used here.
- `assets/icons/` — 18 pre-rendered two-tone icons (navy on transparent), sized
  to sit inside the gold badge. Names: whistle, stopwatch, parking, bolt, owl,
  thermometer, glove, quote, lock, thumbsup, phoneoff, confetti, give, gift,
  heart, chat, cake, star.
- `assets/brand/VISTAGE-Brand-Reference.md` — palette, type, logo usage.
- `scripts/vistage_deck.py` — the `Deck` toolkit (all slide builders + the issue
  funnel). This is the engine; assemble content with it.
- `scripts/make_icons.py` — regenerate or extend the icon set (needs cairosvg).
- `scripts/render_preview.py` — split + render slides to PNG for QA.

## Brand system (non-negotiable for uniformity)

- Colors: **Navy `#003E5E`** (titles, header bar, dividers), **Gold `#EDC11C`**
  (badges, accents, kickers), white, cool gray `#5A6B75` (secondary text).
- Type: **Montserrat** — Bold for titles, Regular for body.
- Every content slide: full-width navy header bar (white title + small white
  wordmark, right) and a consistent footer (gold V-mark + "Group · Meeting ·
  Date" + slide number). One repeating motif: the **gold circle badge**, holding
  either a number or an icon.
- Layout families: **DIVIDER** (full navy, "SECTION 0N"), **CONTENT** (white,
  navy header bar), **PHOTO** (full-bleed image + navy caption band), and the
  full-navy **big-question** "think" slide.

## Setup (run once per session)

```bash
# 1) install the Montserrat fonts so rendering uses the brand face
export HOME=/tmp
mkdir -p /tmp/.fonts && cp <skill>/assets/fonts/*.ttf /tmp/.fonts/ && fc-cache -f /tmp/.fonts
# 2) python deps
pip install python-pptx Pillow --break-system-packages -q
# (cairosvg only needed if regenerating icons)
```

## Build workflow

1. **Gather the Chair's content first.** If rebuilding an existing deck, read it
   — extract the agenda, roles, operating agreements, issues, birthdays/
   anniversaries, photos. Use vision on image-only slides. Drop leftover/stale
   slides, merge duplicates, and convert whiteboard-photo text into typeset text.
   Keep authentic meeting photos; replace generic clip art with bundled icons.
2. **Assemble with the toolkit.** Import `Deck` from `scripts/vistage_deck.py`
   and call the slide builders in meeting order. Example assembly is in that
   file's `__main__` (run it to see a full sample deck). Available builders:
   `title`, `agenda`, `content_bullets`, `cards` (icon cards), `roles`,
   `list_numbered`, `divider`, `big_question`, `issue_funnel`, `photo`,
   `photo_grid`, `closing_adjourn`.
3. **Icon mapping for the Roles slide** (the heart of the whimsy): Break Enforcer
   →whistle, Time Keeper→stopwatch, Parking Lot Attendant→parking, Energizer→
   bolt, Bibliographer/Historian→owl, Environmental Engineer→thermometer,
   Challenger→glove, Quotician→quote. Operating Agreements: Confidentiality→lock,
   Respect→thumbsup, Phones Off→phoneoff, Have Fun→confetti. Closing Exercise:
   Give→give, Get→gift, Thankful→heart. Birthdays→cake, Anniversaries→star,
   Check-In→chat.
4. **Verify** (see below), then save the .pptx to the outputs folder and present
   it.

## Verification (important — read this)

The .pptx is standard and opens correctly in PowerPoint, but **sandbox
LibreOffice often cannot decode embedded images** (and cannot export multi-slide
PDFs). So:

- Use `scripts/render_preview.py deck.pptx /out` to PNG-render each slide. This
  confirms text, layout, dividers, badges, and the issue funnel. Photos/logos/
  icons may show as broken "Picture N" placeholders — that is a *renderer* limit,
  not a file defect.
- To check image/icon slides, **composite them with PIL** at the same
  coordinates the builder uses (white/navy bg → draw the gold badge ellipse →
  paste the icon or photo). A quick standalone PIL mock of just those slides is
  the reliable way to confirm icons sit centered and photo crops/captions look
  right.
- Confirm package soundness: unzip the .pptx and check `ppt/media/` contains the
  expected JP/PNG files with valid bytes and correct slide rels.

## Notes & guardrails

- The issue-processing funnel is rebuilt natively in `Deck.issue_funnel()` in the
  exact brand colors — do not paste in Vistage's original funnel image; the
  native version is more uniform and avoids reproducing their artwork.
- Photos are the Chair's own; the skill ships no meeting photos. `photo()` and
  `photo_grid()` center-crop to avoid distortion.
- To add an icon, edit `scripts/make_icons.py` (one SVG entry) and rerun it; keep
  stroke width 6.5 and navy `#003E5E` so it matches the set.
- See `references/build-notes.md` for exact slide coordinates, the rebuild
  decisions that worked, and gotchas.
