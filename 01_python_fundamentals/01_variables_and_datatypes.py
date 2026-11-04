"""
Module: 01_variables_and_datatypes.py
Description: Introduction to Python variables, data types, type casting, and string formatting.
Key Objectives Covered: Variables, standard data types, input/output operations.
"""

def main():
    print("=" * 60)
    print("         PYTHON FUNDAMENTALS: VARIABLES & DATA TYPES         ")
    print("=" * 60)

    # 1. Variable Assignment and Common Data Types
    user_name = "Alex"             # String (str)
    user_age = 21                  # Integer (int)
    gpa = 3.85                     # Floating point (float)
    is_enrolled = True             # Boolean (bool)
    interests = ["AI", "Python"]   # List (list)

    print("\n--- 1. Variable Values and Types ---")
    print(f"Name: {user_name} | Type: {type(user_name)}")
    print(f"Age: {user_age} | Type: {type(user_age)}")
    print(f"GPA: {gpa} | Type: {type(gpa)}")
    print(f"Enrolled Status: {is_enrolled} | Type: {type(is_enrolled)}")
    print(f"Interests: {interests} | Type: {type(interests)}")

    # 2. Type Casting (Conversion between data types)
    print("\n--- 2. Type Casting ---")
    string_number = "100"
    converted_int = int(string_number)
    converted_float = float(string_number)
    back_to_string = str(converted_float)

    print(f"Original string: '{string_number}' (Type: {type(string_number).__name__})")
    print(f"Converted to int: {converted_int} (Type: {type(converted_int).__name__})")
    print(f"Converted to float: {converted_float} (Type: {type(converted_float).__name__})")
    print(f"Converted back to string: '{back_to_string}' (Type: {type(back_to_string).__name__})")

    # 3. String Manipulation & Modern f-strings
    print("\n--- 3. String Formatting & Manipulation ---")
    greeting = f"Welcome, {user_name}! You currently have a {gpa} GPA and love {interests[0]}."
    print(greeting)
    print(f"Uppercase: {user_name.upper()}")
    print(f"Lowercase: {user_name.lower()}")
    print(f"Character Count: {len(user_name)}")

    # 4. Basic Math Operations
    print("\n--- 4. Basic Arithmetic Operations ---")
    a = 15
    b = 4
    print(f"a = {a}, b = {b}")
    print(f"Addition (a + b): {a + b}")
    print(f"Subtraction (a - b): {a - b}")
    print(f"Multiplication (a * b): {a * b}")
    print(f"Division (a / b): {a / b:.2f}")
    print(f"Floor Division (a // b): {a // b}")
    print(f"Modulus / Remainder (a % b): {a % b}")
    print(f"Exponentiation (a ** b): {a ** b}")

    print("\n[+] Variables & Data Types demonstration completed successfully!\n")

if __name__ == "__main__":
    main()
