"""
Module: 03_loops_and_iterations.py
Description: Mastering repetition in Python using 'for' and 'while' loops, loop controls, and iterators.
Key Objectives Covered: for loops, while loops, range(), break, continue, and list iterations.
"""

def main():
    print("=" * 60)
    print("         PYTHON FUNDAMENTALS: LOOPS & ITERATION             ")
    print("=" * 60)

    # 1. Standard For Loop with range()
    print("\n--- 1. For Loop with range(start, stop, step) ---")
    print("Counting from 1 to 5:")
    for num in range(1, 6):
        print(f"  Step {num}: square = {num ** 2}")

    print("\nCounting backwards from 10 down to 2 with step -2:")
    for count in range(10, 0, -2):
        print(f"  Countdown value: {count}")

    # 2. Iterating over collections (Lists, Strings)
    print("\n--- 2. Iterating Through Collections ---")
    ai_subfields = ["Machine Learning", "Natural Language Processing", "Computer Vision", "Robotics"]
    print("Iterating with index using enumerate():")
    for idx, field in enumerate(ai_subfields, start=1):
        print(f"  [{idx}] Subfield: {field}")

    # 3. While Loop demonstration
    print("\n--- 3. While Loop (Controlled Accumulation) ---")
    energy_level = 5
    while energy_level > 0:
        print(f"  Training model iteration... Current energy remaining: {energy_level}")
        energy_level -= 1
    print("  Model training loop finished! Battery empty.")

    # 4. Loop Control Statements: break, continue, pass
    print("\n--- 4. Loop Controls: break & continue ---")
    dataset_records = ["valid", "valid", "corrupted", "valid", "stop_signal", "valid"]
    print(f"Processing dataset stream: {dataset_records}")
    
    for index, record in enumerate(dataset_records):
        if record == "corrupted":
            print(f"  [Skip] Record at index {index} is corrupted. Continuing to next record...")
            continue  # Skips the rest of this iteration
        
        if record == "stop_signal":
            print(f"  [Halt] Stop signal encountered at index {index}! Breaking loop.")
            break     # Exits loop immediately
        
        print(f"  [OK] Successfully ingested record at index {index}: '{record}'")

    # 5. Nested Loops: Generating a small multiplication / matrix grid
    print("\n--- 5. Nested Loops (2D Grid / Multiplication) ---")
    for row in range(1, 4):
        row_str = ""
        for col in range(1, 4):
            row_str += f"{row * col:4d}"
        print(f"  Row {row}: {row_str}")

    print("\n[+] Loops & Iterations demonstration completed successfully!\n")

if __name__ == "__main__":
    main()
