# Python Mini Projects & AI Fundamentals 🚀

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code Style: PEP 8](https://img.shields.io/badge/code%20style-PEP%208-green.svg)](https://pep8.org/)
[![Status: Completed](https://img.shields.io/badge/Status-Completed-success.svg)]()
[![Verification: 12/12 Passed](https://img.shields.io/badge/Tests-12%2F12%20Passing-brightgreen.svg)]()

A production-grade Python repository built for the **AI & Python Internship**, covering **Module 01 (Introduction to AI & Python)** and **Module 02 (Python Mini Projects)**. Contains 7 complete mini-projects, comprehensive core fundamentals, and academic learning documentation.

---

## 📋 Table of Contents
- [Curriculum & Objectives](#-curriculum--objectives)
- [Repository Architecture](#-repository-architecture)
- [Interactive Main Application (`main.py`)](#-interactive-main-application-mainpy)
- [Featured Python Mini Projects (Module 02)](#-featured-python-mini-projects-module-02)
  - [1. Personal Expense Tracker](#1-personal-expense-tracker)
  - [2. Secure Password Generator](#2-secure-password-generator)
  - [3. Number Guessing Challenge Game](#3-number-guessing-challenge-game)
  - [4. Student Grade Manager & Calculator](#4-student-grade-manager--calculator)
  - [5. Smart Scientific Calculator](#5-smart-scientific-calculator)
  - [6. Rule-Based AI Chatbot](#6-rule-based-ai-chatbot)
  - [7. AI Sentiment Analysis Engine](#7-ai-sentiment-analysis-engine)
- [Python Language Fundamentals (Module 01)](#-python-language-fundamentals-module-01)
- [Comprehensive Learning Notes](#-comprehensive-learning-notes)
- [Quickstart: How to Run](#-quickstart-how-to-run)
- [Automated Master Verification Test Suite](#-automated-master-verification-test-suite)
- [Author & Submission Info](#-author--submission-info)

---

## 🎯 Curriculum & Objectives

### Module 01: Introduction to AI & Python
- Understand AI vs Machine Learning vs Deep Learning paradigms.
- Study real-world AI use cases across Healthcare, Autonomous Mobility, NLP, and Finance.
- Master Python programming syntax: variables, conditionals, loops, lists, and functions.

### Module 02: Python Mini Projects
- Apply Python primitives to build real-world, functional applications.
- Implement error handling, JSON persistence, statistical analytics, and algorithmic strategies.
- Maintain production code quality adhering to PEP 8 standards and modular software design.

---

## 📂 Repository Architecture

```text
INTERSHIP/
│
├── main.py                                   # Master Interactive CLI Application Launcher
├── README.md                                 # Complete documentation & project manual
├── LEARNING_NOTES.md                         # Full study guide (Google Docs / Notion format)
├── LEARNING_NOTES.html                       # Styled HTML version of learning notes
├── run_all_demos.py                          # Automated 12-test verification runner
├── .gitignore                                # Git ignore file for cache & environments
│
├── 01_python_fundamentals/                   # Core Python Primitives (Module 01)
│   ├── 01_variables_and_datatypes.py         # Type system, casting, arithmetic, f-strings
│   ├── 02_operators_and_conditionals.py      # Logic operators, branching, ternary logic
│   ├── 03_loops_and_iterations.py            # For/while loops, range, enumerate, break/continue
│   ├── 04_lists_and_tuples.py                # Slicing, list mutation, comprehensions, tuples
│   └── 05_functions_and_scope.py             # Functions, parameters, multiple return, scope
│
└── 02_mini_projects/                         # Hands-on Applications (Module 02)
    ├── 01_student_grade_manager.py           # Student performance tracker & grade report
    ├── 02_smart_calculator.py                # Calculator with history logging & error handling
    ├── 03_rule_based_chatbot.py              # Classical Symbolic AI / NLP rule-based assistant
    ├── 04_ai_sentiment_analyzer.py           # NLP sentiment classifier & negation handling
    ├── 05_personal_expense_tracker.py        # Expense & budget monitor with JSON persistence
    ├── 06_secure_password_generator.py       # Password generator with entropy security rating
    └── 07_number_guessing_game.py           # Game with AI binary search optimal solver
```

---

## 🎮 Interactive Main Application (`main.py`)

Launch all projects from a single unified interactive console menu:

```bash
python main.py
```

```text
======================================================================
           PYTHON MINI PROJECTS SUITE - MODULE 02             
======================================================================
Select a project from the menu to launch:
  [1] Personal Expense Tracker
  [2] Secure Password Generator
  [3] Number Guessing Challenge Game
  [4] Student Grade Manager & Calculator
  [5] Smart Scientific Calculator
  [6] Rule-Based AI Assistant Chatbot
  [7] AI Sentiment Analysis Engine
  [8] Run Complete Verification Test Suite
  [0] Exit Application
======================================================================
```

---

## 🚀 Featured Python Mini Projects (Module 02)

### 1. Personal Expense Tracker
- **File:** [`02_mini_projects/05_personal_expense_tracker.py`](02_mini_projects/05_personal_expense_tracker.py)
- **Features:**
  - Categorizes spending into Food, Transport, Utilities, Entertainment, Education, etc.
  - Generates budget utilization metrics and ASCII category breakdown bars.
  - Persists financial records into a local JSON file (`expenses_data.json`).

### 2. Secure Password Generator
- **File:** [`02_mini_projects/06_secure_password_generator.py`](02_mini_projects/06_secure_password_generator.py)
- **Features:**
  - Configurable length, uppercase, lowercase, numbers, and symbols.
  - Excludes visually ambiguous characters (`l, 1, I, 0, O`).
  - Mathematically calculates **information entropy in bits** ($E = L \times \log_2(R)$) to rate password strength (Weak, Moderate, Strong, Enterprise Grade).

### 3. Number Guessing Challenge Game
- **File:** [`02_mini_projects/07_number_guessing_game.py`](02_mini_projects/07_number_guessing_game.py)
- **Features:**
  - Multiple difficulty presets (Easy: 1-50, Medium: 1-100, Hard: 1-500).
  - Dynamic proximity feedback ("Too High", "Too Low").
  - Includes an **AI Optimal Solver** demonstrating logarithmic binary search ($O(\log N)$) efficiency and performance scoring.

### 4. Student Grade Manager & Calculator
- **File:** [`02_mini_projects/01_student_grade_manager.py`](02_mini_projects/01_student_grade_manager.py)
- **Features:**
  - Parses student records and assigns academic letter grades (`A` to `F`).
  - Calculates class average, standard distribution, top ranker, and lowest score.
  - Generates clean tabular ASCII report cards.

### 5. Smart Scientific Calculator
- **File:** [`02_mini_projects/02_smart_calculator.py`](02_mini_projects/02_smart_calculator.py)
- **Features:**
  - Arithmetic evaluation (`+`, `-`, `*`, `/`, `^`).
  - Graceful exception recovery for undefined operations (division by zero).
  - Maintains a session history memory log.

### 6. Rule-Based AI Chatbot
- **File:** [`02_mini_projects/03_rule_based_chatbot.py`](02_mini_projects/03_rule_based_chatbot.py)
- **Features:**
  - Illustrates the foundation of **Symbolic AI / Expert Systems**.
  - Token-level query classification, punctuation normalization, and intent matching.
  - Answers domain queries about AI, Machine Learning, Deep Learning, and Python.

### 7. AI Sentiment Analysis Engine
- **File:** [`02_mini_projects/04_ai_sentiment_analyzer.py`](02_mini_projects/04_ai_sentiment_analyzer.py)
- **Features:**
  - Intro-level Natural Language Processing (NLP) text classifier.
  - Lexicon-based polarity scoring with negation awareness (e.g. *"not good"* vs *"good"*).
  - Outputs sentiment classification (`POSITIVE`, `NEUTRAL`, `NEGATIVE`) with confidence percentage.

---

## ⚡ Quickstart: How to Run

### Clone the Repository
```bash
git clone https://github.com/abi323728-ctrl/Introduction-to-AI-and-Python.git
cd Introduction-to-AI-and-Python
```

### Launch Interactive CLI
```bash
python main.py
```

### Run Any Script Individually
```bash
# Mini Projects:
python 02_mini_projects/05_personal_expense_tracker.py
python 02_mini_projects/06_secure_password_generator.py
python 02_mini_projects/07_number_guessing_game.py
python 02_mini_projects/01_student_grade_manager.py
python 02_mini_projects/02_smart_calculator.py
python 02_mini_projects/03_rule_based_chatbot.py
python 02_mini_projects/04_ai_sentiment_analyzer.py

# Fundamentals:
python 01_python_fundamentals/01_variables_and_datatypes.py
python 01_python_fundamentals/02_operators_and_conditionals.py
python 01_python_fundamentals/03_loops_and_iterations.py
python 01_python_fundamentals/04_lists_and_tuples.py
python 01_python_fundamentals/05_functions_and_scope.py
```

---

## 🧪 Automated Master Verification Test Suite

Verify all 12 modules and projects in under 1 second with the built-in test runner:

```bash
python run_all_demos.py
```

```text
===========================================================================
      PYTHON MINI PROJECTS: MASTER VERIFICATION RUNNER        
===========================================================================
[01/12] Executing: 01_python_fundamentals/01_variables_and_datatypes.py    ... [PASSED]
[02/12] Executing: 01_python_fundamentals/02_operators_and_conditionals.py ... [PASSED]
[03/12] Executing: 01_python_fundamentals/03_loops_and_iterations.py       ... [PASSED]
[04/12] Executing: 01_python_fundamentals/04_lists_and_tuples.py           ... [PASSED]
[05/12] Executing: 01_python_fundamentals/05_functions_and_scope.py        ... [PASSED]
[06/12] Executing: 02_mini_projects/01_student_grade_manager.py            ... [PASSED]
[07/12] Executing: 02_mini_projects/02_smart_calculator.py                 ... [PASSED]
[08/12] Executing: 02_mini_projects/03_rule_based_chatbot.py               ... [PASSED]
[09/12] Executing: 02_mini_projects/04_ai_sentiment_analyzer.py            ... [PASSED]
[10/12] Executing: 02_mini_projects/05_personal_expense_tracker.py         ... [PASSED]
[11/12] Executing: 02_mini_projects/06_secure_password_generator.py        ... [PASSED]
[12/12] Executing: 02_mini_projects/07_number_guessing_game.py             ... [PASSED]
===========================================================================
VERIFICATION SUMMARY: 12/12 scripts passed in 0.60 seconds.
===========================================================================
```

---

## 📬 Author & Submission Info

- **Author:** Abishek J
- **GitHub Profile:** [@abi323728-ctrl](https://github.com/abi323728-ctrl)
- **Module Deliverables:**
  - **Module 01 (Intro to AI & Python):** [GitHub Repo](https://github.com/abi323728-ctrl/Introduction-to-AI-and-Python) | [Learning Notes](LEARNING_NOTES.md)
  - **Module 02 (Python Mini Project):** [GitHub Repo](https://github.com/abi323728-ctrl/Introduction-to-AI-and-Python)
- **License:** MIT
