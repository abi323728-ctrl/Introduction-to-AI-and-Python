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
]

def main():
    print("=" * 75)
    print("      INTRODUCTION TO AI & PYTHON: MASTER VERIFICATION RUNNER        ")
    print("=" * 75)
    
    passed_count = 0
    start_time = time.time()

    for idx, script in enumerate(SCRIPTS_TO_EXECUTE, start=1):
        print(f"\n[{idx}/{len(SCRIPTS_TO_EXECUTE)}] Executing: {script} ...")
        res = subprocess.run([sys.executable, script], capture_output=True, text=True)
        
        if res.returncode == 0:
            print(f"       -> [PASSED]")
            passed_count += 1
        else:
            print(f"       -> [FAILED]")
            print(res.stderr)

    elapsed = time.time() - start_time
    print("\n" + "=" * 75)
    print(f"VERIFICATION SUMMARY: {passed_count}/{len(SCRIPTS_TO_EXECUTE)} scripts passed in {elapsed:.2f} seconds.")
    print("=" * 75)

if __name__ == "__main__":
    main()
