"""
Project: 02_smart_calculator.py
Description: A functional calculator with operation history tracking, error handling,
             and arithmetic utility functions.
"""

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero is undefined.")
    return a / b

def power(a: float, b: float) -> float:
    return a ** b

def execute_operation(operation: str, num1: float, num2: float) -> tuple[float, str]:
    """Routes operation symbol to appropriate function and returns result with formatted expression."""
    ops = {
        "+": (add, "+"),
        "-": (subtract, "-"),
        "*": (multiply, "*"),
        "/": (divide, "/"),
        "^": (power, "^"),
    }
    if operation not in ops:
        raise ValueError(f"Unsupported operation: {operation}")
    
    func, symbol = ops[operation]
    result = func(num1, num2)
    record = f"{num1} {symbol} {num2} = {result:.4g}"
    return result, record

def run_automated_test_suite():
    """Runs a batch of calculations to demonstrate history tracking and validation."""
    history: list[str] = []
    test_cases = [
        ("+", 12.5, 7.5),
        ("-", 50, 18.25),
        ("*", 6.5, 4),
        ("/", 100, 8),
        ("^", 2, 8),
        ("/", 10, 0), # Intended to test error handling
    ]

    print("=" * 60)
    print("               SMART CALCULATOR & HISTORY LOG                ")
    print("=" * 60)

    for op, a, b in test_cases:
        try:
            res, record = execute_operation(op, a, b)
            history.append(record)
            print(f"[SUCCESS] {record}")
        except ZeroDivisionError as zde:
            history.append(f"{a} {op} {b} -> FAILED ({zde})")
            print(f"[CAUTION] {a} {op} {b} -> {zde}")
        except Exception as ex:
            print(f"[ERROR] {ex}")

    print("\n--- Final Calculation History (Stored in Memory List) ---")
    for i, log_item in enumerate(history, start=1):
        print(f"  #{i}: {log_item}")
    print("=" * 60)

if __name__ == "__main__":
    run_automated_test_suite()

