# Contributing to Floating Lyrics Overlay

This Python/Tkinter desktop project displays lyrics in floating windows with typewriter, fade-out, and upward-drift effects.

## Clone and run
```bash
git clone https://github.com/joshuaarao42-arch/floating-lyrics-overlay.git
cd floating-lyrics-overlay
python lyrics_visualizer.py
```
Use Python 3.10 or newer with Tkinter installed.

## Project-specific contributions
- Improve floating-window positioning and screen-edge behavior.
- Refine typewriter timing, fade-out, and drift animations.
- Improve readability for long lines and different display resolutions.
- Make window behavior more predictable and configurable.

## Testing expectations
Test long and short lyric lines, repeated launches, multiple screen sizes, and animation timing. Keep UI updates compatible with Tkinter's event loop; avoid blocking callbacks. Include screenshots or a short recording for visual changes.

Use branches such as `feature/overlay-controls` or `fix/animation-timing`.
