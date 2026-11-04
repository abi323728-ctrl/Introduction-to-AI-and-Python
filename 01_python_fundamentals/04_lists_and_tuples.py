"""
Module: 04_lists_and_tuples.py
Description: Working with sequence data types in Python: Lists (mutable) and Tuples (immutable).
Key Objectives Covered: Lists, indexing, slicing, common list methods, comprehensions, and tuples.
"""

def main():
    print("=" * 60)
    print("         PYTHON FUNDAMENTALS: LISTS & SEQUENCES             ")
    print("=" * 60)

    # 1. List Creation & Basic Properties
    fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    print("\n--- 1. List Creation & Inspection ---")
    print(f"Original list: {fruits}")
    print(f"Length of list: {len(fruits)}")
    print(f"First element fruits[0]: {fruits[0]}")
    print(f"Last element fruits[-1]: {fruits[-1]}")

    # 2. Slicing Lists (start : stop : step)
    print("\n--- 2. List Slicing Techniques ---")
    print(f"First 3 items (fruits[0:3])  : {fruits[0:3]}")
    print(f"Middle items (fruits[1:4])   : {fruits[1:4]}")
    print(f"Every 2nd item (fruits[::2]) : {fruits[::2]}")
    print(f"Reversed list (fruits[::-1]) : {fruits[::-1]}")

    # 3. List Modification Methods
    print("\n--- 3. Modifying Lists (Methods) ---")
    programming_languages = ["Python", "C++", "Java"]
    print(f"Initial: {programming_languages}")

    # append: add to the end
    programming_languages.append("JavaScript")
    print(f"After .append('JavaScript'): {programming_languages}")

    # insert: add at specific index
    programming_languages.insert(1, "Rust")
    print(f"After .insert(1, 'Rust'): {programming_languages}")

    # remove: remove by value
    programming_languages.remove("Java")
    print(f"After .remove('Java'): {programming_languages}")

    # pop: remove by index and return element
    popped_item = programming_languages.pop()
    print(f"After .pop() (removed '{popped_item}'): {programming_languages}")

    # 4. Sorting and Reversing
    scores = [88, 42, 95, 71, 60, 99]
    print("\n--- 4. Sorting Operations ---")
    print(f"Raw scores: {scores}")
    sorted_scores = sorted(scores) # Returns new sorted list
    print(f"Using sorted() (non-destructive): {sorted_scores}")
    scores.sort(reverse=True)      # In-place sort descending
    print(f"Using .sort(reverse=True) (in-place): {scores}")

    # 5. List Comprehensions (Clean, pythonic data transforms)
    print("\n--- 5. List Comprehensions ---")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = [n for n in numbers if n % 2 == 0]
    squares = [n ** 2 for n in numbers]
    print(f"Numbers: {numbers}")
    print(f"Even numbers extracted: {evens}")
    print(f"Squares generated: {squares}")

    # 6. Tuples: Immutable Sequences
    print("\n--- 6. Tuples (Immutable alternative to lists) ---")
    image_resolution = (1920, 1080)
    print(f"Resolution Tuple: {image_resolution} (Width: {image_resolution[0]}, Height: {image_resolution[1]})")
    
    # Tuple Unpacking
    width, height = image_resolution
    print(f"Unpacked variables -> Width: {width}px, Height: {height}px")

    print("\n[+] Lists & Sequences demonstration completed successfully!\n")

if __name__ == "__main__":
    main()

