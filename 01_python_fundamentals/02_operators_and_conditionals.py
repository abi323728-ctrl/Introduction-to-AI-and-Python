"""
Module: 02_operators_and_conditionals.py
Description: Decision making in Python using comparison operators, logical operators, and if-elif-else statements.
Key Objectives Covered: Conditional logic, boolean conditions, branch execution.
"""

def evaluate_eligibility(age: int, score: float, has_prerequisites: bool) -> str:
    """Evaluates student eligibility for an Advanced AI course."""
    if age < 16:
        return "Ineligible: Applicant must be at least 16 years old."
    elif score >= 85 and has_prerequisites:
        return "Accepted: Full scholarship admission to Advanced AI."
    elif score >= 70 or has_prerequisites:
        return "Accepted: Regular admission to Foundation Track."
    else:
        return "Waitlisted: Recommended to take Introductory Computer Science first."

def main():
    print("=" * 60)
    print("      PYTHON FUNDAMENTALS: OPERATORS & CONDITIONALS         ")
    print("=" * 60)

    # 1. Comparison Operators
    x = 10
    y = 20
    print("\n--- 1. Comparison Operations ---")
    print(f"x = {x}, y = {y}")
    print(f"x == y : {x == y}  (Equal)")
    print(f"x != y : {x != y}  (Not Equal)")
    print(f"x > y  : {x > y}   (Greater than)")
    print(f"x < y  : {x < y}   (Less than)")
    print(f"x >= 10: {x >= 10}  (Greater or equal)")

    # 2. Logical Operators (and, or, not)
    print("\n--- 2. Logical Operators ---")
    is_student = True
    has_discount_coupon = False
    print(f"is_student = {is_student}, has_discount_coupon = {has_discount_coupon}")
    print(f"is_student and has_discount_coupon: {is_student and has_discount_coupon}")
    print(f"is_student or has_discount_coupon : {is_student or has_discount_coupon}")
    print(f"not is_student                    : {not is_student}")

    # 3. If-Elif-Else Decision Making Pipeline
    print("\n--- 3. Decision Making Flow Simulation ---")
    candidates = [
        {"name": "Alice", "age": 20, "score": 92.5, "prereq": True},
        {"name": "Bob", "age": 19, "score": 74.0, "prereq": False},
        {"name": "Charlie", "age": 15, "score": 98.0, "prereq": True},
        {"name": "Diana", "age": 22, "score": 62.0, "prereq": False},
    ]

    for c in candidates:
        result = evaluate_eligibility(c["age"], c["score"], c["prereq"])
        print(f"Candidate: {c['name']:<8} | Age: {c['age']} | Score: {c['score']} | Status: {result}")

    # 4. Ternary / Conditional Expression (One-line if)
    print("\n--- 4. One-Line Ternary Condition ---")
    temp = 28
    weather = "Warm / Summer" if temp > 25 else "Cool / Mild"
    print(f"Temperature: {temp}°C -> Status: {weather}")

    print("\n[+] Operators & Conditionals demonstration completed successfully!\n")

if __name__ == "__main__":
    main()
