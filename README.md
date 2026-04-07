# 🤖 Robot Framework Automation Project

A beginner-friendly, scalable **Robot Framework automation framework** designed for Web and API testing.
This project follows a **clean structure, reusable components, and clear conventions** so that any new user can quickly understand and start contributing.

---

# 📖 1. Overview (Start Here)

This framework is built to:

* Automate **UI (Web)** and **API** testing
* Maintain **readable and reusable test cases**
* Support **multiple environments (QA, UAT, Prod)**
* Enable **easy execution locally and in CI/CD**

👉 If you're new, follow this order:

1. Setup → Installation
2. Understand → Project Structure
3. Learn → Naming Conventions
4. Run → Test Execution
5. Extend → Add new tests

---

# ⚙️ 2. Setup & Installation

## Prerequisites

* Python (>= 3.8)
* pip
* Browser (Chrome/Firefox)
* WebDriver (ChromeDriver, GeckoDriver)

## Step-by-Step Setup

### 1. Clone Repository

```bash
git clone <repo-url>
cd project-root
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📁 3. Project Structure (Very Important)

Understanding this is key to working in the framework.

```
project-root/
│
├── tests/                 # ✅ Test cases (WHAT to test)
│   ├── web/
│   ├── api/
│   └── mobile/
│
├── resources/             # ✅ Reusable logic (HOW to test)
│   ├── keywords/          # Custom keywords
│   ├── locators/          # UI locators
│   └── testdata/          # Test data files
│
├── config/                # ✅ Environment configs
│   ├── env.yaml
│   └── settings.py
│
├── drivers/               # Browser drivers
├── reports/               # Execution outputs
├── utils/                 # Helper functions
│
├── requirements.txt
└── README.md
```

### 🔍 Simple Understanding

| Folder                | Purpose              |
| --------------------- | -------------------- |
| `tests/`              | Contains test cases  |
| `resources/keywords/` | Reusable actions     |
| `resources/locators/` | UI elements          |
| `resources/testdata/` | Input data           |
| `config/`             | Environment settings |

---

# 🧱 4. Framework Design (How It Works)

We follow a **layered approach**:

```
Test Case  →  Keywords  →  Locators  →  Application
```

### Example Flow

```
Test Case: Login Test
    ↓
Keyword: Login To Application
    ↓
Locators: username, password, login button
```

👉 This ensures:

* Reusability
* Easy maintenance
* Clean separation of logic

---

# 🏷️ 5. Naming Conventions (Follow Strictly)

Consistency makes the framework readable.

## Test Cases

```
Verify_<Feature>_<Scenario>
```

✅ Example:

```
Verify_Login_With_Valid_Credentials
```

## Keywords

```
<Action> <Object>
```

✅ Example:

```
Click Login Button
Enter Username
```

## Variables

```
${UPPER_CASE}
```

✅ Example:

```
${BASE_URL}
${USERNAME}
```

## Files

| Type          | Format                        |
| ------------- | ----------------------------- |
| Test Files    | `test_<feature>.robot`        |
| Keyword Files | `<feature>_keywords.resource` |

---

# ⚙️ 6. Configuration Management

All environment-related data is centralized.

📂 File:

```
config/env.yaml
```

### Example:

```yaml
env: qa
base_url: https://qa.example.com
browser: chrome
timeout: 10
```

👉 Benefits:

* No hardcoding
* Easy environment switch

---

# 🧪 7. Writing Test Cases

### Basic Example

```
*** Test Cases ***
Verify Login With Valid Credentials
    Open Browser    ${BASE_URL}    ${BROWSER}
    Input Text      id=username    ${USERNAME}
    Input Text      id=password    ${PASSWORD}
    Click Button    id=login
```

---

# 🔁 8. Reusable Keywords

📂 Location:

```
resources/keywords/
```

### Example:

```
*** Keywords ***
Login To Application
    Open Browser    ${BASE_URL}    ${BROWSER}
    Input Text      id=username    ${USERNAME}
    Input Text      id=password    ${PASSWORD}
    Click Button    id=login
```

👉 Rule:

* Do NOT duplicate logic
* Always reuse keywords

---

# ▶️ 9. Test Execution

## Run All Tests

```bash
robot tests/
```

## Run Specific Module

```bash
robot tests/web/
```

## Run with Environment

```bash
robot -v ENV:qa tests/
```

## Parallel Execution

```bash
pabot tests/
```

---

# 📊 10. Reports & Logs

After execution, check:

```
reports/
```

### Generated Files

* `report.html` → Summary
* `log.html` → Detailed steps
* `output.xml` → Raw results

---

# 🐞 11. Debugging Tips

* Use:

```
Log    message
Log To Console    message
```

* Capture failure screenshots:

```
Capture Page Screenshot
```

---

# 🚀 12. CI/CD Integration

Supported tools:

* Jenkins
* GitHub Actions
* GitLab CI

### Typical Flow

1. Code commit
2. Pipeline triggers
3. Tests execute
4. Reports published

---

# 📚 13. Best Practices

* Keep tests independent
* Avoid hardcoding
* Use test data files
* Follow naming conventions
* Use tags:

```
[Tags]    smoke    regression
```

---

# 🔮 14. Future Improvements

* Docker execution
* Cloud testing (BrowserStack)
* Allure reporting
* Advanced logging

---

# 🤝 15. Contribution Guide

1. Create a branch
2. Follow structure & naming rules
3. Add/update tests
4. Raise Pull Request

---

# 📌 Final Notes for New Users

If you're just starting:

👉 First understand:

* Project Structure
* Naming Conventions

👉 Then:

* Run existing tests
* Slowly start adding new ones

---

**This framework is designed to be simple, readable, and scalable. Follow the structure, and everything will stay clean and maintainable. 🚀**
