# SimulationHub Valve Geometry Automation

This repository contains Selenium and Playwright-based automation scripts for testing the Valve Design application on [SimulationHub](https://experiments.simulationhub.com/valve-design).

## Features

- Automated UI tests for valve type selection and diameter adjustment
- Screenshot capture and image comparison for visual regression
- Configurable browser and headless/headed modes
- Helper methods for interacting with sliders and dropdowns

## Project Structure

```
d:\SH_Playwright
│
├── pages/
│   └── valve_design_page.py      # Page object for Valve Design UI
│
├── tests/
│   └── test_valve_design.py      # Test cases for valve design features
│
├── conftest.py                   # Pytest fixtures and configuration
├── Readme.md                     # Project documentation
```

## Setup

1. **Install dependencies:**
   ```
   pip install selenium pillow pytest
   ```

2. **(Optional) Install Playwright and browsers:**
   ```
   pip install playwright pytest-playwright
   playwright install
   ```

3. **Configure browser options in `conftest.py` as needed.**

## Running Tests

- **Selenium tests:**
  ```
  pytest -v --selenium-browser=chrome
  ```

- **Playwright tests (if implemented):**
  ```
  pytest -v --headed
  ```

## Image Comparison

- Baseline images should be placed in the test directory.
- Screenshots are compared using pixel tolerance to allow minor rendering differences.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request
