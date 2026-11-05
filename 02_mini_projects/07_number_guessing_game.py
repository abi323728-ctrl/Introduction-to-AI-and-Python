"""
Project: 07_number_guessing_game.py
Description: An interactive Number Guessing Game with AI binary-search hints,
             customizable difficulty levels, and performance score tracking.
Module: Module 02 - Python Mini Projects
"""

import random

DIFFICULTY_LEVELS = {
    "1": {"name": "Easy", "range": (1, 50), "max_attempts": 10},
    "2": {"name": "Medium", "range": (1, 100), "max_attempts": 7},
    "3": {"name": "Hard", "range": (1, 500), "max_attempts": 9},
}

def calculate_score(attempts_used: int, max_attempts: int, difficulty: str) -> int:
    """Calculates a game score based on attempts efficiency and difficulty multiplier."""
    multipliers = {"Easy": 1.0, "Medium": 2.0, "Hard": 5.0}
    remaining_ratio = max(0, (max_attempts - attempts_used + 1) / max_attempts)
    base_score = 1000 * remaining_ratio
    return int(base_score * multipliers.get(difficulty, 1.0))

def simulate_ai_game(target: int, low: int, high: int, max_attempts: int) -> dict:
    """Simulates an AI agent solving the number guessing game using binary search."""
    history = []
    current_low = low
    current_high = high
    attempts = 0
    solved = False

    while attempts < max_attempts and current_low <= current_high:
        attempts += 1
        guess = (current_low + current_high) // 2

        if guess == target:
            history.append({"attempt": attempts, "guess": guess, "feedback": "CORRECT! Target located."})
            solved = True
            break
        elif guess < target:
            history.append({"attempt": attempts, "guess": guess, "feedback": "Too LOW -> Narrowed range"})
            current_low = guess + 1
        else:
            history.append({"attempt": attempts, "guess": guess, "feedback": "Too HIGH -> Narrowed range"})
            current_high = guess - 1

    return {
        "target": target,
        "solved": solved,
        "attempts": attempts,
        "history": history
    }

def run_simulation_demo():
    print("=" * 70)
    print("       NUMBER GUESSING GAME & OPTIMAL BINARY SEARCH DEMO      ")
    print("=" * 70)

    target_number = 73
    low_bound, high_bound = 1, 100
    max_turns = 7

    print(f"\n[Game Parameters]: Range: [{low_bound} to {high_bound}] | Secret Target: {target_number} | Max Turns: {max_turns}")
    print("Simulating optimal algorithmic player (Binary Search Strategy)...")
    print("-" * 70)

    result = simulate_ai_game(target_number, low_bound, high_bound, max_turns)

    for step in result["history"]:
        print(f"  Turn #{step['attempt']}: Guess = {step['guess']:<3} | Status: {step['feedback']}")

    if result["solved"]:
        score = calculate_score(result["attempts"], max_turns, "Medium")
        print("-" * 70)
        print(f"Victory! Solved in {result['attempts']} attempts.")
        print(f"Performance Score: {score} Points (Rank: S-Tier Algorithmic Precision)")
    else:
        print("Game Over: Failed to locate target within turn limit.")

    print("=" * 70 + "\n")

if __name__ == "__main__":
    run_simulation_demo()

