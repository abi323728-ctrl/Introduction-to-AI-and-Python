# Introduction to AI & Python 🚀

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code Style: PEP 8](https://img.shields.io/badge/code%20style-PEP%208-green.svg)](https://pep8.org/)
[![Status: Completed](https://img.shields.io/badge/Status-Completed-success.svg)]()

A comprehensive repository for the **Introduction to AI & Python** internship module. This repository contains foundational Python scripts, beginner-friendly mini-projects demonstrating classical rule-based AI and NLP concepts, and in-depth academic learning notes.

---

## 📋 Table of Contents
- [Key Objectives](#-key-objectives)
- [Repository Structure](#-repository-structure)
- [Module Breakdown](#-module-breakdown)
  - [1. Python Fundamentals](#1-python-fundamentals)
  - [2. Hands-on Mini Projects](#2-hands-on-mini-projects)
- [Comprehensive Learning Notes](#-comprehensive-learning-notes)
- [Quickstart: Installation & Execution](#-quickstart-installation--execution)
- [Automated Master Test Runner](#-automated-master-test-runner)
- [Author & Submission Details](#-author--submission-details)

---

## 🎯 Key Objectives

This repository satisfies all key deliverables outlined in the module syllabus:
1. **Understand AI & Machine Learning Foundations:** Definitions, history, paradigms (Supervised, Unsupervised, Reinforcement).
2. **Differentiate AI vs ML vs Deep Learning:** Hierarchical relations, feature engineering differences, and comparison matrix.
3. **Explore Real-World Applications:** Healthcare, autonomous mobility, finance, NLP, and ethical AI considerations.
4. **Master Python Programming Primitives:** Variables, data types, conditionals, loops, lists, and functions.
5. **Develop Beginner-Friendly Python Programs:** Functional applications and AI-concept demonstrators.

---

## 📂 Repository Structure

```text
INTERSHIP/
│
├── README.md                                 # Main repository overview and documentation
├── LEARNING_NOTES.md                         # In-depth study notes (ready for Google Docs/Notion)
├── run_all_demos.py                          # Master execution runner verifying all scripts
├── .gitignore                                # Git ignore file for bytecode & environments
│
├── 01_python_fundamentals/                   # Core Python language concepts
│   ├── 01_variables_and_datatypes.py         # Variables, types, type-casting, f-strings
│   ├── 02_operators_and_conditionals.py      # Comparison, logic operators, decision branching
│   ├── 03_loops_and_iterations.py            # For & while loops, range, break, continue
│   ├── 04_lists_and_tuples.py                # Slicing, list methods, comprehensions, tuples
│   └── 05_functions_and_scope.py             # Function definitions, parameters, return, scope
│
└── 02_mini_projects/                         # Hands-on beginner applications
    ├── 01_student_grade_manager.py           # Grade processing, statistical distributions
    ├── 02_smart_calculator.py                # Calculator with history memory & error handling
    ├── 03_rule_based_chatbot.py              # Classical Symbolic AI / NLP rule-based assistant
    └── 04_ai_sentiment_analyzer.py           # NLP Sentiment scoring & negation handling
```

---

## 💻 Module Breakdown

### 1. Python Fundamentals (`01_python_fundamentals/`)

- **`01_variables_and_datatypes.py`**
  - Explores primitive data types: `str`, `int`, `float`, `bool`.
  - Type-casting conversions between string and numeric types.
  - Basic arithmetic operations and modern f-string interpolation.

- **`02_operators_and_conditionals.py`**
  - Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`).
  - Boolean logic using `and`, `or`, and `not`.
  - Multi-branch decision pipelines (`if`, `elif`, `else`) and ternary operators.

- **`03_loops_and_iterations.py`**
  - Definite iteration using `for` loops and `range(start, stop, step)`.
  - Iteration with indexing using `enumerate()`.
  - Indefinite iteration with `while` loops.
  - Flow control using `break` and `continue`.

- **`04_lists_and_tuples.py`**
  - List indexing and non-destructive slicing (`[start:stop:step]`).
  - In-place mutation methods: `.append()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`.
  - Pythonic list comprehensions for concise data transformation.
  - Immutable sequences with `tuples` and tuple unpacking.

- **`05_functions_and_scope.py`**
  - Function declaration syntax (`def`), parameters, default arguments, and docstrings.
  - Multiple return values using tuple packing.
  - Variable scoping rules (Local vs Global namespace).
  - Introduction to anonymous `lambda` functions.

---

### 2. Hands-on Mini Projects (`02_mini_projects/`)

- **`01_student_grade_manager.py`**
  - Ingests student performance records into structured dictionaries.
  - Automatically maps percentage scores to academic letter grades (`A` to `F`).
  - Computes class average, top performer, and minimum score.
  - Generates a formatted ASCII console grade sheet.

- **`02_smart_calculator.py`**
  - Evaluates basic and exponential arithmetic expressions.
  - Includes robust error handling for mathematical exceptions (e.g., division by zero).
  - Maintains an internal audit log of all calculations performed during the session.

- **`03_rule_based_chatbot.py`**
  - Demonstrates the principles of **Symbolic AI / Expert Systems**.
  - Tokenizes input, strips punctuation, and matches user queries to intents.
  - Answers common questions regarding AI, Machine Learning, Deep Learning, and Python.

- **`04_ai_sentiment_analyzer.py`**
  - Demonstrates introductory **Natural Language Processing (NLP)** classification.
  - Evaluates text polarity using positive and negative lexicon dictionaries.
  - Detects negation contexts (e.g., distinguishing between *"good"* vs *"not good"*).
  - Outputs classified category (`POSITIVE`, `NEUTRAL`, `NEGATIVE`) with confidence percentage.

---

## 📖 Comprehensive Learning Notes

Complete theoretical documentation is compiled in [LEARNING_NOTES.md](LEARNING_NOTES.md). Topics covered include:
- **Foundations of AI & ML:** Definitions, historical transition from Symbolic AI to Data-Driven paradigms.
- **The AI vs ML vs DL Hierarchy:** Clear nested diagrams, feature extraction comparison, data requirements, and hardware needs.
- **Real-World Applications:** In-depth case studies across Healthcare, Autonomous Driving, Finance, NLP, and E-commerce.
- **Python for AI:** Architectural reasons behind Python's leadership in data science and machine learning.
- **Ethics & Safety:** Addressing bias, fairness, transparency, and data privacy in modern AI systems.

> **Tip for Submission:** The content inside `LEARNING_NOTES.md` is formatted with standard GitHub Markdown and can be directly copied and pasted into **Google Docs** or **Notion**.

---

## ⚡ Quickstart: Installation & Execution

### Prerequisites
- Python 3.10 or higher installed on your system.
- Git installed.

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Running Individual Fundamentals Scripts
```bash
python 01_python_fundamentals/01_variables_and_datatypes.py
python 01_python_fundamentals/02_operators_and_conditionals.py
python 01_python_fundamentals/03_loops_and_iterations.py
python 01_python_fundamentals/04_lists_and_tuples.py
python 01_python_fundamentals/05_functions_and_scope.py
```

### 3. Running Mini Projects
```bash
python 02_mini_projects/01_student_grade_manager.py
python 02_mini_projects/02_smart_calculator.py
python 02_mini_projects/03_rule_based_chatbot.py
python 02_mini_projects/04_ai_sentiment_analyzer.py
```

---

## 🧪 Automated Master Test Runner

You can execute all modules and projects simultaneously using the included verification runner:

```bash
python run_all_demos.py
```

**Sample Output:**
```text
===========================================================================
      INTRODUCTION TO AI & PYTHON: MASTER VERIFICATION RUNNER        
===========================================================================

[1/9] Executing: 01_python_fundamentals/01_variables_and_datatypes.py ...
       -> [PASSED]
[2/9] Executing: 01_python_fundamentals/02_operators_and_conditionals.py ...
       -> [PASSED]
[3/9] Executing: 01_python_fundamentals/03_loops_and_iterations.py ...
       -> [PASSED]
[4/9] Executing: 01_python_fundamentals/04_lists_and_tuples.py ...
       -> [PASSED]
[5/9] Executing: 01_python_fundamentals/05_functions_and_scope.py ...
       -> [PASSED]
[6/9] Executing: 02_mini_projects/01_student_grade_manager.py ...
       -> [PASSED]
[7/9] Executing: 02_mini_projects/02_smart_calculator.py ...
       -> [PASSED]
[8/9] Executing: 02_mini_projects/03_rule_based_chatbot.py ...
       -> [PASSED]
[9/9] Executing: 02_mini_projects/04_ai_sentiment_analyzer.py ...
       -> [PASSED]

===========================================================================
VERIFICATION SUMMARY: 9/9 scripts passed in 0.75 seconds.
===========================================================================
```

---

## 📬 Author & Submission Details

- **Module:** Introduction to AI & Python
- **GitHub Repository Deliverable:** Provided via repository link.
- **Learning Notes Deliverable:** Provided via Google Docs / Notion public view link.
- **License:** MIT
