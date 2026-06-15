# Build notes & gotchas

Detailed reference for the `vistage-chair-deck` skill. Read when you need exact
geometry, the rebuild decisions that worked, or to debug rendering.

## Canvas & spacing

- Slide is 16:9 → 13.333 in × 7.5 in. At 96 DPI that's 1280 × 720 px (handy for
  PIL composites).
- Content margin: 0.8 in left. Header bar: full width × 1.15 in tall, navy, title
  white Montserrat-Bold 30 pt, vertically centered, left 0.6 in; white wordmark at
  x≈11.0, y≈0.42, height 0.30.
- Footer baseline y≈7.03–7.04: V-mark height 0.22 at x 0.6; text 9 pt gray; slide
  number right-aligned near x 12.0.
- Gold badge motif: ellipse filled gold; icon pasted at ~0.62× the badge diameter,
  centered. Numbers use Montserrat-Bold navy.

## Slide-type cheatsheet (matches `Deck` methods)

- **title** — full navy; gold group name kicker, white wordmark (~5.2 in wide),
  white headline 40, gold subtitle 22, gray footnote 16.
- **divider** — full navy; small gold tick, "SECTION 0N" gold 16, title white 42,
  sub gray 19, small white wordmark bottom-center.
- **big_question** — full navy; gold kicker 18, white question 38, centered.
- **agenda** — gold rounded time chips (1.45×0.62) + navy labels, rows ~0.83 apart.
- **content_bullets** — optional bold navy lead; gold dot bullets in two columns.
- **cards** — N navy rounded cards; gold icon badge (1.0 in) top-center; white
  heading 18; gray desc 13. Used for Operating Agreements and Give/Get/Thankful.
- **roles** — two columns × 4; 0.62 in icon badge + navy name 16 + gray desc 12 +
  light "Assigned: ____" line.
- **list_numbered** — gold number badges + navy items (onboarding, talk-a-person).
- **issue_funnel** — 8 stacked centered rounded bars, decreasing/uniform widths,
  shaded navy→grays→gold ending on "Member & Group Value" (gold).
- **photo / photo_grid** — full-bleed or 3-up; center-cropped; navy caption band.

## Rebuild decisions that worked (from the reference project)

- **Resolve month/owner mismatches.** Reused templates often carry a prior
  month's title/agenda/speaker. Rebuild the title + a single correct agenda.
- **Collapse duplicates.** A messy whiteboard capture + its cleaned version =
  keep one clean slide. Two "check-in" slides = one.
- **Typeset whiteboard photos.** Convert photographed brainstorm text into real
  text slides; pull starred items into a gold "Priorities" panel.
- **Replace generic clip art** (stock balloons w/ watermark, cartoon characters,
  Looney-Tunes "That's all Folks", red CHECK-IN button) with bundled icons or a
  branded divider. **Keep** authentic host/tour/dinner photos.
- **Section dividers** replace blank footer-only "transition" slides.

## Fonts

- Install bundled Montserrat to fontconfig before rendering: copy to `/tmp/.fonts`
  (or `~/.fonts`) and `fc-cache -f`. `HOME=/tmp` if the real home is read-only.
- The deck names "Montserrat"; PowerPoint substitutes a sans if the user lacks it.
  Montserrat is a free Google font — fine to recommend installing.

## Rendering / verification gotchas

- **PDF export frequently fails** in sandbox LibreOffice with
  `impl_store ... 0xc10 Io ... Write`. Don't fight it — `render_preview.py`
  splits the deck and PNG-exports single slides, which works.
- **Embedded images don't decode** in that same LibreOffice — even a clean PIL
  PNG renders as white, and JPEGs show as red "Picture N" placeholders. This is a
  renderer limitation; the .pptx is fine. Prove it by unzipping and checking
  `ppt/media/`, and verify image/icon slides via PIL composite.
- **Disk pressure** can also break LibreOffice export; clear large files in /tmp.
- **Logo PNG format:** use the bundled `vistage-wordmark-white.png` (clean RGBA).
  An ImageMagick gray+alpha PNG once rendered as a broken placeholder in some
  viewers; re-encoding to straight RGBA with PIL fixed it.

## PIL composite recipe (verifying icon/photo slides)

Mirror the builder coordinates at 1280×720: fill bg (white for content, navy for
dividers), draw the header bar, `draw.ellipse(...)` in gold for each badge, then
`paste(icon_rgba, ..., icon_rgba)` at 0.62× the badge box. For photos, center-crop
to the target aspect ratio, paste full-bleed, then draw the navy caption band and
text. Save and view to confirm faces aren't covered and icons are centered.

## Icon set

18 icons, navy stroke `#003E5E`, width 6.5, round caps, on transparent. The
`parking` glyph uses Montserrat (needs the font on fontconfig at render time); all
others are pure geometry. To extend, add one SVG entry to `make_icons.py` and
rerun (`pip install cairosvg --break-system-packages`). Keep the same stroke/
palette so new icons match.
