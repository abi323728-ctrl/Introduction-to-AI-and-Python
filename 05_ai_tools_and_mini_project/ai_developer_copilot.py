"""
Project: ai_developer_copilot.py
Description: An AI-Powered Developer & Productivity Copilot demonstrating the integration
             of AI tools in software engineering, automated code review, documentation synthesis,
             and prompt engineering optimization.
Module: Module 05 - AI Tools & Mini Project
Author: Abishek J (abi323728-ctrl)
Organization: Codomax Digital Solutions
"""

import os
import sys
import time

def explain_and_optimize_code(code_snippet: str) -> dict:
    """Analyzes a Python code snippet, evaluates time complexity, and suggests optimizations."""
    lines = [line.strip() for line in code_snippet.strip().split("\n") if line.strip()]
    
    # Static analysis heuristics
    has_nested_loops = False
    loop_depth = 0
    max_loop_depth = 0
    uses_type_hints = "->" in code_snippet or ":" in code_snippet
    has_docstring = '"""' in code_snippet or "'''" in code_snippet

    for line in lines:
        if line.startswith("for ") or line.startswith("while "):
            loop_depth += 1
            if loop_depth > max_loop_depth:
                max_loop_depth = loop_depth
        elif line.startswith("return ") or line.startswith("def "):
            loop_depth = 0

    if max_loop_depth >= 2:
        complexity = "O(n^2) - Quadratic (Consider optimizing with Hash Sets/Dictionaries)"
    elif max_loop_depth == 1:
        complexity = "O(n) - Linear"
    else:
        complexity = "O(1) - Constant Time"

    suggestions = []
    if not has_docstring:
        suggestions.append("Add descriptive docstrings for better codebase maintainability.")
    if not uses_type_hints:
        suggestions.append("Incorporate Python type annotations (PEP 484) to improve code safety.")
    if max_loop_depth >= 2:
        suggestions.append("Nested loops detected: Replace linear lookups with set/dict lookups for O(1) membership testing.")

    return {
        "lines_analyzed": len(lines),
        "estimated_complexity": complexity,
        "type_hints_present": uses_type_hints,
        "docstring_present": has_docstring,
        "actionable_suggestions": suggestions or ["Code meets high standards of clean code principles."]
    }

def synthesize_unit_tests(function_name: str, parameters: list[str]) -> str:
    """Generates automated Python unittest template for a specified function."""
    param_str = ", ".join(parameters)
    test_code = f"""import unittest
from {function_name}_module import {function_name}

class Test{function_name.capitalize()}(unittest.TestCase):
    def test_standard_case(self):
        \"\"\"Verify behavior on normal inputs.\"\"\"
        result = {function_name}({param_str})
        self.assertIsNotNone(result)

    def test_edge_case_empty(self):
        \"\"\"Verify behavior on empty or minimum boundaries.\"\"\"
        # TODO: Adjust parameters for boundary testing
        pass

    def test_invalid_type_raises_exception(self):
        \"\"\"Verify exception handling on invalid arguments.\"\"\"
        with self.assertRaises(TypeError):
            {function_name}(None)

if __name__ == '__main__':
    unittest.main()
"""
    return test_code

def summarize_technical_article(text: str) -> dict:
    """Extracts executive key points, word count reduction, and action takeaways from technical prose."""
    sentences = [s.strip() for s in text.split(".") if len(s.strip()) > 15]
    words = text.split()
    original_word_count = len(words)

    # Heuristic importance extraction
    high_value_keywords = ["ai", "machine learning", "performance", "scalability", "pipeline", "security", "model"]
    ranked_points = []
    for s in sentences:
        score = sum(1 for kw in high_value_keywords if kw in s.lower())
        if score > 0:
            ranked_points.append(s)

    summary_bullets = ranked_points[:3] if ranked_points else sentences[:3]
    summary_word_count = sum(len(b.split()) for b in summary_bullets)

    return {
        "original_word_count": original_word_count,
        "summary_word_count": summary_word_count,
        "compression_ratio": f"{((1 - summary_word_count / max(1, original_word_count)) * 100):.1f}%",
        "key_takeaways": summary_bullets
    }

def optimize_developer_prompt(rough_prompt: str, domain: str = "Backend Development") -> str:
    """Transforms informal, vague prompts into structured high-precision AI prompts."""
    structured = f"""======================================================================
[OPTIMIZED STRUCTURED DEVELOPER PROMPT]
======================================================================
[Role & Persona]:
  You are an expert Principal Engineer specializing in {domain}.

[Core Objective]:
  {rough_prompt.strip()}

[Technical Context & Constraints]:
  - Language / Framework: Python 3.10+ / Production Best Practices
  - Code Quality: Follow PEP 8, provide explicit type hints, and include docstrings.
  - Performance: Optimize for time/space complexity and avoid unneeded allocations.
  - Error Resilience: Add defensive try-except blocks with explicit exception types.

[Expected Output]:
  1. Complete, executable, bug-free source code.
  2. Brief technical explanation of architectural decisions.
  3. 3 unit tests verifying happy path, boundary cases, and edge errors.
======================================================================"""
    return structured

def run_automated_demonstration():
    print("=" * 75)
    print("      MODULE 05: AI DEVELOPER COPILOT & PRODUCTIVITY ENGINE         ")
    print("=" * 75)
    print("Author: Abishek J | Organization: Codomax Digital Solutions\n")

    # 1. Code Optimization Test
    sample_code = """
def find_common_elements(list1, list2):
    common = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                common.append(item1)
    return common
"""
    print("--- 1. AI Code Analysis & Complexity Estimation ---")
    print("Input Code Snippet:" + sample_code)
    analysis = explain_and_optimize_code(sample_code)
    print(f"Lines Analyzed        : {analysis['lines_analyzed']}")
    print(f"Estimated Complexity  : {analysis['estimated_complexity']}")
    print("Recommendations:")
    for rec in analysis["actionable_suggestions"]:
        print(f"  • {rec}")

    # 2. Automated Test Generation
    print("\n--- 2. Automated Unit Test Synthesis ---")
    tests = synthesize_unit_tests("process_payment", ["user_id='USR101'", "amount=250.0"])
    print(tests)

    # 3. Technical Research Summarization
    print("--- 3. AI Research Document Summarizer ---")
    article = (
        "Artificial Intelligence and Machine Learning are transforming modern cloud architecture. "
        "Engineers are deploying automated data pipeline workflows that monitor model performance in real time. "
        "By integrating automated testing with continuous evaluation, development teams reduce production defects. "
        "Security, scalability, and ethical data governance remain top priorities for enterprise adoption."
    )
    summary = summarize_technical_article(article)
    print(f"Original Length : {summary['original_word_count']} words | Compression: {summary['compression_ratio']}")
    print("Key Takeaways Extracted:")
    for pt in summary["key_takeaways"]:
        print(f"  ✓ {pt}.")

    # 4. Prompt Engineering Optimization
    print("\n--- 4. Prompt Engineering Studio (Rough -> Structured) ---")
    rough = "Write a python script to validate user login passwords"
    optimized_prompt = optimize_developer_prompt(rough, domain="Cybersecurity & Authentication")
    print(optimized_prompt)

    print("\n" + "=" * 75)
    print("      AI DEVELOPER COPILOT DEMONSTRATION SUCCESSFULLY FINISHED!      ")
    print("=" * 75 + "\n")

if __name__ == "__main__":
    run_automated_demonstration()
