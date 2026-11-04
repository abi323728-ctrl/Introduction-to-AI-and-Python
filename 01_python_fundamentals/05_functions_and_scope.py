"""
Module: 05_functions_and_scope.py
Description: Defining reusable functions, understanding parameters, return types, and variable scope.
Key Objectives Covered: Functions, default parameters, scope, docstrings, and modular design.
"""

# Global variable
PLATFORM_NAME = "AI Learning Hub"

def greet_user(name: str, module: str = "Introduction to Python") -> str:
    """Returns a personalized greeting message with a default module title."""
    return f"Hello, {name}! Welcome to '{module}' on {PLATFORM_NAME}."

def calculate_stats(numbers: list[float]) -> tuple[float, float, float]:
    """Calculates min, max, and average of a list of numbers.
    Returns:
        tuple: (minimum, maximum, average)
    """
    if not numbers:
        return 0.0, 0.0, 0.0
    total = sum(numbers)
    count = len(numbers)
    return min(numbers), max(numbers), total / count

def demonstrate_scope():
    """Shows the difference between local variables and global variables."""
    local_message = "I exist only inside demonstrate_scope()"
    print(f"Inside function -> Global var access: {PLATFORM_NAME}")
    print(f"Inside function -> Local var: {local_message}")

def apply_discount(price: float, discount_percent: float = 10.0) -> float:
    """Applies percentage discount to a given price."""
    discount_amount = price * (discount_percent / 100)
    return round(price - discount_amount, 2)

def main():
    print("=" * 60)
    print("         PYTHON FUNDAMENTALS: FUNCTIONS & SCOPE             ")
    print("=" * 60)

    # 1. Calling functions with positional and keyword arguments
    print("\n--- 1. Function Calling & Default Arguments ---")
    msg1 = greet_user("Abishek")
    msg2 = greet_user(name="Sarah", module="Deep Learning Foundations")
    print(msg1)
    print(msg2)

    # 2. Returning Multiple Values (Tuples)
    print("\n--- 2. Returning Multiple Values ---")
    benchmark_scores = [78.5, 92.0, 85.5, 64.0, 99.0]
    minimum, maximum, avg = calculate_stats(benchmark_scores)
    print(f"Dataset: {benchmark_scores}")
    print(f"Stats -> Min: {minimum} | Max: {maximum} | Average: {avg:.2f}")

    # 3. Variable Scope Demonstration
    print("\n--- 3. Local vs Global Scope ---")
    demonstrate_scope()
    # local_message is not accessible here

    # 4. Lambda Functions (Anonymous one-liners)
    print("\n--- 4. Lambda Functions ---")
    cube = lambda x: x ** 3
    print(f"Cube of 4 using lambda: {cube(4)}")

    data_points = [(1, 5), (3, 2), (2, 8), (4, 1)]
    # Sort pairs by second element (y-coordinate)
    sorted_points = sorted(data_points, key=lambda pt: pt[1])
    print(f"Original points: {data_points}")
    print(f"Points sorted by second element: {sorted_points}")

    # 5. Reusable calculation helpers
    print("\n--- 5. Practical Helper Example ---")
    original_price = 150.0
    final_price = apply_discount(original_price, 20.0)
    print(f"Original: ${original_price:.2f} | 20% Off -> Final: ${final_price:.2f}")

    print("\n[+] Functions & Scope demonstration completed successfully!\n")

if __name__ == "__main__":
    main()
