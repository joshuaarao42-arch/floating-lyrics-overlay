# Contributing to Floating Lyrics Overlay

Thank you for helping improve Floating Lyrics Overlay, a Python and Tkinter desktop application for displaying lyrics in floating windows with animated text effects.

## Getting started

```bash
git clone https://github.com/joshuaarao42-arch/floating-lyrics-overlay.git
cd floating-lyrics-overlay
python lyrics_visualizer.py
```

Use Python 3.10 or newer and ensure Tkinter is available in your Python installation. If the project documents additional dependencies or a different launch command, follow the README.

## What you can contribute

- Improve floating-window positioning, sizing, and screen-edge behavior.
- Refine typewriter timing, fade-out, and upward-drift animations.
- Improve readability for long lines and different display resolutions.
- Improve controls, configuration, and error handling.
- Fix bugs and improve documentation.

## Project-specific guidelines

Tkinter UI updates must remain compatible with its event loop. Avoid blocking the main thread with long-running tasks. Use scheduled UI callbacks for animation rather than busy loops. Ensure closing or restarting the overlay does not leave unwanted windows or callbacks running.

## Development standards

Follow the existing Python style and naming conventions. Keep animation logic and window behavior understandable. Add dependencies only when they provide clear value, and document any new installation requirements.

## Testing your changes

Run the application and test short and long lyric lines, repeated launches, window movement, screen boundaries, and animation timing. Check behavior at different screen sizes and scaling settings when possible. Include screenshots or a short recording for visual changes.

## Branch and commit workflow

Use a focused branch such as `feature/overlay-controls`, `fix/animation-timing`, or `docs/install-guide`. Use commit prefixes such as `feat:`, `fix:`, `docs:`, `style:`, `refactor:`, and `test:`.

## Opening a pull request

Explain the behavior before and after the change, list the steps used to test it, and include screenshots or a recording for visual or animation changes. Mention any platform-specific limitations.

## Reporting issues

Include your operating system, Python version, reproduction steps, expected behavior, actual behavior, and error output where available. Remove personal information from logs.

## Code of conduct

Keep collaboration respectful and constructive. Welcome beginners, explain feedback clearly, and avoid personal attacks or discriminatory behavior.
