# TutorialsNinja BDD Framework

Selenium Python Behave BDD framework for [TutorialsNinja Demo](https://tutorialsninja.com/demo/)

\---

## Tech Stack

|Tool|Purpose|
|-|-|
|Python 3|Programming language|
|Selenium 4|Browser automation|
|Behave|BDD framework (Gherkin syntax)|
|Allure Behave|Test reporting|
|Page Object Model|Design pattern|

\---

## Project Structure

```
PythonTutorialsNinjaBehaveBDD/
├── configurations/
│   └── config.ini
├── features/
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── home_page.py
│   │   ├── login_page.py
│   │   ├── register_page.py
│   │   ├── my_account_page.py
│   │   ├── account_success_page.py
│   │   ├── change_password_page.py
│   │   └── search_page.py
│   ├── steps/
│   │   ├── login_steps.py
│   │   ├── search_steps.py
│   │   └── end_to_end_steps.py
│   ├── utils/
│   │   ├── config_reader.py
│   │   └── driver_factory.py
│   ├── environment.py
│   ├── login.feature
│   └── search.feature
├── reports/
│   └── screenshots/
├── results/
│   ├── allure-report/
│   └── allure-results/
├── behave.ini
└── requirements.txt
```

\---

## Test Coverage

|Module|Feature File|TC Range|Total|
|-|-|-|-|
|Login|login.feature|TC\_LF\_001 – TC\_LF\_023|23|
|Search|search.feature|TC\_SF\_001 – TC\_SF\_022|22|
|**Total**|||**45**|

\---

## Run Tests

```bash
# All tests
behave

# Specific feature
behave features/login.feature
behave features/search.feature

# Single test case
behave --tags=@TC_LF_001

# By module
behave --tags=@Login
behave --tags=@Search

# By type
behave --tags=@smoke
behave --tags=@regression
behave --tags=@negative
behave --tags=@security

# Stop on first failure
behave --stop
```

\---

## Allure Report

```bash
behave -f allure_behave.formatter:AllureFormatter -o results/allure-results
allure serve results/allure-results
```

\---

## Reports

|Output|Location|
|-|-|
|Allure results|`results/allure-results/`|
|Allure HTML report|`results/allure-report/`|
|Failure screenshots|`reports/screenshots/`|

> Screenshots are captured automatically on scenario failure.

