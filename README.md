# Cyfrowa Biblioteka — Test automation (pytest + Playwright)

This repository contains a pytest + Playwright test automation framework targeting the Cyfrowa Biblioteka system (default BASE_URL: http://localhost:8000).

Getting started

1. Create a virtual environment and activate it (recommended):

   python -m venv .venv
   source .venv/bin/activate  # macOS / Linux
   .\.venv\Scripts\activate   # Windows (PowerShell)

2. Install dependencies:

   python -m pip install --upgrade pip
   pip install -r requirements.txt

3. Install Playwright browsers:

   python -m playwright install

4. Run tests:

   pytest

Environment

- BASE_URL: Set to the application URL if not running on http://localhost:8000.

Notes

- Selectors in tests/pages/register_page.py are examples. Adjust them to match your application's HTML structure.
- The test suite includes examples for positive, negative, boundary, security, and basic accessibility tests.