# Contributing to floating-lyrics-overlay

Thank you for considering a contribution to this project. This guide explains how to propose changes, prepare your development environment, and submit work for review.

## Project overview

Python and Tkinter floating lyrics desktop application.

## Getting started

```bash
git clone https://github.com/joshuaarao42-arch/floating-lyrics-overlay.git
cd floating-lyrics-overlay
python lyrics_visualizer.py
```

Follow the repository README and existing project configuration if setup commands or entry points have changed. Review the current code before introducing new tools or dependencies.

## What you can contribute

- Improve floating-window positioning
- Typewriter timing
- Fade-out and drift animations
- Readability
- Configuration
- And screen-size behavior.

Bug reports, documentation improvements, accessibility fixes, and reproducible tests are also welcome.

## Project-specific requirements

Use Python 3.10+ with Tkinter. Keep UI updates on Tkinter's event loop and avoid blocking callbacks. Test long and short lines, repeated launches, animation timing, and different display sizes.

## Coding standards

- Follow the language, naming, formatting, and file-organization conventions already used in the repository.
- Keep changes focused and functions or components easy to understand.
- Validate user input and handle errors clearly.
- Avoid unrelated refactoring and unnecessary dependencies.
- Never commit secrets, credentials, generated local data, or personal information.

## Testing

Run the application using the documented setup and test every workflow affected by your change. Include edge cases, not only the successful path. State what you tested and the result. Add screenshots for interface changes and sample inputs with expected outputs for calculation or logic changes.

## Branch and commit workflow

Create a branch from the default branch. Use descriptive names such as `feature/short-description`, `fix/short-description`, or `docs/short-description`.

Use clear commit prefixes:
- `feat:` new functionality
- `fix:` bug fixes
- `docs:` documentation
- `style:` formatting or visual-only changes
- `refactor:` code restructuring without behavior changes
- `test:` tests

## Pull request guidelines

Before submitting, make sure your changes are focused and tested. In the pull request:
1. Explain the problem and why the change is useful.
2. Summarize what you changed.
3. Link a related issue, if one exists.
4. List the tests performed and their results.
5. Add screenshots or sample output when relevant.
6. Mention breaking changes, new dependencies, or known limitations.

## Reporting bugs and requesting features

Search existing issues before opening a new one. For bugs, include steps to reproduce, expected behavior, actual behavior, environment details, and sanitized screenshots or logs. For feature requests, explain the use case and the expected benefit. Do not publish credentials or private data.

## Code of conduct

Be respectful, patient, and constructive. Critique code and ideas rather than people. Harassment, discrimination, and abusive behavior are not acceptable.
