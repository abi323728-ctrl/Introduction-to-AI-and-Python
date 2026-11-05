"""
Master Application Launcher: main.py
Title: Python Mini Projects Suite
Module: Module 02 - Python Mini Projects
Author: Abishek J (abi323728-ctrl)
"""

import os
import subprocess
import sys

PROJECTS = {
    "1": ("Personal Expense Tracker", "02_mini_projects/05_personal_expense_tracker.py"),
    "2": ("Secure Password Generator", "02_mini_projects/06_secure_password_generator.py"),
    "3": ("Number Guessing Challenge Game", "02_mini_projects/07_number_guessing_game.py"),
    "4": ("Student Grade Manager & Calculator", "02_mini_projects/01_student_grade_manager.py"),
    "5": ("Smart Scientific Calculator", "02_mini_projects/02_smart_calculator.py"),
    "6": ("Rule-Based AI Assistant Chatbot", "02_mini_projects/03_rule_based_chatbot.py"),
    "7": ("AI Sentiment Analysis Engine", "02_mini_projects/04_ai_sentiment_analyzer.py"),
    "8": ("AI Developer & Productivity Copilot (Module 05)", "05_ai_tools_and_mini_project/ai_developer_copilot.py"),
    "9": ("Run Complete Verification Test Suite", "run_all_demos.py"),
}

def print_banner():
    print("=" * 70)
    print("           PYTHON MINI PROJECTS SUITE - MODULE 02             ")
    print("=" * 70)
    print("Select a project from the menu to launch:")
    for key, (name, _) in PROJECTS.items():
        print(f"  [{key}] {name}")
    print("  [0] Exit Application")
    print("=" * 70)

def main():
    while True:
        print_banner()
        choice = input("Enter your selection (0-8) [default=8 to run all]: ").strip()
        
        if not choice:
            choice = "8"

        if choice == "0":
            print("\nExiting Python Mini Projects Suite. Happy coding!\n")
            break

        if choice in PROJECTS:
            name, path = PROJECTS[choice]
            print(f"\n>>> Launching: {name} ({path})\n")
            if os.path.exists(path):
                subprocess.run([sys.executable, path])
            else:
                print(f"[Error]: Script '{path}' not found.")
            print("\n" + "-" * 70 + "\n")
        else:
            print("\n[Invalid Selection] Please choose a valid option (0-8).\n")

if __name__ == "__main__":
    # If run in non-interactive environment (CI/tests), run verification demo
    if not sys.stdin.isatty():
        subprocess.run([sys.executable, "run_all_demos.py"])
    else:
        main()

