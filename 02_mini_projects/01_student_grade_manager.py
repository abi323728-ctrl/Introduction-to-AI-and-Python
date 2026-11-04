"""
Project: 01_student_grade_manager.py
Description: A beginner-friendly student performance tracker demonstrating variables, lists,
             dictionaries, loops, conditionals, and functions.
"""

def calculate_letter_grade(score: float) -> str:
    """Assigns an academic letter grade based on numeric score percentage."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def process_student_records(students: list[dict]) -> dict:
    """Processes a list of student score dictionaries and generates a report."""
    total_class_score = 0.0
    highest_student = None
    lowest_student = None

    for student in students:
        score = student["score"]
        student["letter_grade"] = calculate_letter_grade(score)
        total_class_score += score

        if highest_student is None or score > highest_student["score"]:
            highest_student = student
        if lowest_student is None or score < lowest_student["score"]:
            lowest_student = student

    class_average = total_class_score / len(students) if students else 0.0

    return {
        "class_average": class_average,
        "highest": highest_student,
        "lowest": lowest_student,
        "count": len(students)
    }

def print_grade_report(students: list[dict], summary: dict):
    """Prints a structured ASCII report table."""
    print("=" * 65)
    print("                STUDENT GRADE MANAGER REPORT                 ")
    print("=" * 65)
    print(f"{'ID':<6} | {'Student Name':<18} | {'Score':<8} | {'Grade':<6} | {'Status'}")
    print("-" * 65)

    for idx, s in enumerate(students, start=101):
        status = "PASSED" if s["score"] >= 60 else "NEEDS HELP"
        print(f"{idx:<6} | {s['name']:<18} | {s['score']:<8.1f} | {s['letter_grade']:<6} | {status}")

    print("-" * 65)
    print(f"Total Students Evaluated : {summary['count']}")
    print(f"Class Average Score      : {summary['class_average']:.2f}")
    if summary["highest"]:
        print(f"Top Performer            : {summary['highest']['name']} ({summary['highest']['score']} - Grade {summary['highest']['letter_grade']})")
    if summary["lowest"]:
        print(f"Lowest Score             : {summary['lowest']['name']} ({summary['lowest']['score']} - Grade {summary['lowest']['letter_grade']})")
    print("=" * 65)

def main():
    # Sample initial student dataset
    students_database = [
        {"name": "Alice Johnson", "score": 94.5},
        {"name": "Brian Smith", "score": 78.0},
        {"name": "Clara Davis", "score": 88.5},
        {"name": "David Martinez", "score": 55.0},
        {"name": "Emma Wilson", "score": 91.0},
        {"name": "Frank Miller", "score": 67.5},
    ]

    summary = process_student_records(students_database)
    print_grade_report(students_database, summary)

if __name__ == "__main__":
    main()
