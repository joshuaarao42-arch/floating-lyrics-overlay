# Contributing to Floating Lyrics Overlay

Thanks for contributing to this Python and Tkinter desktop lyrics visualizer.

## Set up the project
```bash
git clone https://github.com/joshuaarao42-arch/floating-lyrics-overlay.git
cd floating-lyrics-overlay
python lyrics_visualizer.py
```
Use Python 3.10 or newer. Tkinter must be available in your Python installation.

## What to improve
- Floating lyric-window behavior and positioning.
- Typewriter timing, fade-out, and upward-drift animations.
- Window readability, sizing, and usability across screen resolutions.
- Stability when displaying long lines or rapidly changing lyrics.
- Clear setup and usage documentation.

## Desktop-app checks
Test window placement, animation smoothness, long text, repeated launches, and behavior on different screen sizes. Avoid blocking the Tkinter event loop with long-running work. Keep animation updates compatible with Tkinter's event-driven model.

## Pull requests
Use branches such as `feature/overlay-controls` or `fix/animation-timing`. Describe the behavior before and after your change and include a screenshot or short recording when it helps demonstrate a visual improvement.
