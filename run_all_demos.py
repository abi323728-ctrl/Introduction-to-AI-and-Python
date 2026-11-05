"""
Script: run_all_demos.py
Description: Master test runner that executes all fundamental modules and mini-projects
             in sequential order to verify functionality.
"""

import subprocess
import sys
import time

SCRIPTS_TO_EXECUTE = [
    "01_python_fundamentals/01_variables_and_datatypes.py",
    "01_python_fundamentals/02_operators_and_conditionals.py",
    "01_python_fundamentals/03_loops_and_iterations.py",
    "01_python_fundamentals/04_lists_and_tuples.py",
    "01_python_fundamentals/05_functions_and_scope.py",
    "02_mini_projects/01_student_grade_manager.py",
    "02_mini_projects/02_smart_calculator.py",
    "02_mini_projects/03_rule_based_chatbot.py",
    "02_mini_projects/04_ai_sentiment_analyzer.py",
    "02_mini_projects/05_personal_expense_tracker.py",
    "02_mini_projects/06_secure_password_generator.py",
    "02_mini_projects/07_number_guessing_game.py",
    "05_ai_tools_and_mini_project/ai_developer_copilot.py",
]

def main():
    print("=" * 75)
    print("      PYTHON MINI PROJECTS: MASTER VERIFICATION RUNNER        ")
    print("=" * 75)
    
    passed_count = 0
    start_time = time.time()

    for idx, script in enumerate(SCRIPTS_TO_EXECUTE, start=1):
        print(f"[{idx:02d}/{len(SCRIPTS_TO_EXECUTE):02d}] Executing: {script:<55} ...", end=" ")
        res = subprocess.run([sys.executable, script], capture_output=True, text=True)
        
        if res.returncode == 0:
            print("[PASSED]")
            passed_count += 1
        else:
            print("[FAILED]")
            print(res.stderr)

    elapsed = time.time() - start_time
    print("=" * 75)
    print(f"VERIFICATION SUMMARY: {passed_count}/{len(SCRIPTS_TO_EXECUTE)} scripts passed in {elapsed:.2f} seconds.")
    print("=" * 75)

if __name__ == "__main__":
    main()
