# Single Bet Placement QA Assignment

## Overview

This repository contains the solution for the QA Engineer take-home assignment focused on the **Single Bet Placement** feature of a sports betting web application.

The project includes:
- Manual test planning
- Bug reporting and exploratory findings
- UI automation using Selenium WebDriver and Pytest
- API automation using Python requests
- CI execution using GitHub Actions

The automation framework was designed with a strong focus on:
- maintainability
- readability
- stable locator strategy
- reusable Page Object Model structure
- reliable synchronization using explicit waits

---

# Project Scope

## Manual QA
- Prioritized test plan covering critical business flows and validation scenarios
- Manual execution results
- Detailed defect reports with supporting evidence
- Exploratory testing observations

## Automation
### UI Automation
- End-to-end successful single bet placement flow

### API Automation
- Unauthorized API request validation (`401 Unauthorized`)

## CI/CD
- Automated execution via GitHub Actions
- UI and API test execution on push and pull request events

---

# Tech Stack

- Python 3.11
- Selenium WebDriver
- Pytest
- Requests
- GitHub Actions
- pytest-html

---

# Project Structure

```text
single-bet-placement-qa-assignment/
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── docs/
│   ├── test-plan.md
│   ├── execution-results-bug-report.md
│   └── strategy-recommendations.md
│
├── evidence/
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── bet_slip_page.py
│   └── receipt_modal.py
│
├── tests/
│   ├── api/
│   │   └── test_auth_validation.py
│   │
│   └── ui/
│       └── test_place_bet.py
│
├── utils/
│   ├── api_client.py
│   └── config.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Setup

## Clone Repository

```bash
git clone https://github.com/dpopovic1990/single-bet-placement-qa-assignment.git
cd single-bet-placement-qa-assignment
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Tests

## Run Full Test Suite

```bash
pytest
```

---

## Run UI Tests Only

```bash
pytest tests/ui -v
```

---

## Run API Tests Only

```bash
pytest tests/api -v
```

---

## Generate HTML Test Report

```bash
pytest --html=reports/report.html --self-contained-html
```

Generated reports are stored inside the `reports/` directory.

---

# Automated Tests

## UI Automation Test

### Successful Single Bet Placement

This test validates the application's primary business flow:
- match selection
- odds selection
- stake entry
- successful bet placement
- success receipt visibility

The test was selected because it represents the application's critical revenue-generating user journey.

---

## API Automation Test

### Unauthorized Bet Placement Request

This API test validates that requests without the required `x-user-id` header are rejected with `401 Unauthorized`.

The scenario was selected because authentication and authorization validation represent high-risk backend protections with strong regression value.

---

# Framework Design Decisions

## Page Object Model (POM)

The UI automation framework follows the Page Object Model pattern to improve:
- maintainability
- readability
- locator centralization
- test reusability

---

## Stable Locator Strategy

Automation primarily relies on stable element IDs to reduce test fragility and improve long-term reliability.

---

## Explicit Wait Strategy

The framework uses reusable explicit wait helpers instead of hardcoded sleeps to reduce flaky test behavior and improve synchronization with asynchronous UI updates.

---

## Headless CI Execution

GitHub Actions UI execution runs in headless Chrome mode using CI-safe browser configuration for reliable Linux runner execution.

---

# CI/CD

GitHub Actions workflow automatically executes:
- UI automation tests
- API automation tests

on:
- pull requests
- pushes

This provides fast regression feedback and basic CI validation for the automation suite.

---

# Notes

During manual testing, several frontend synchronization inconsistencies were identified:
- incorrect payout rendering in the success receipt modal
- UI balance not updating despite successful backend deduction

Additional details are documented in:
- `docs/execution-results-bug-report.md`

Backend API validation generally behaved consistently with the provided specification.

For simplicity and reproducible execution within this public take-home assignment, the provided test `user-id` is stored directly in configuration.

In a production environment, sensitive configuration and credentials would be externalized through environment variables or CI/CD secret management solutions rather than committed into source control.