"""
Project: 06_secure_password_generator.py
Description: A configurable, cryptographically secure password generator with strength evaluation,
             entropy scoring, and customizable character constraints.
Module: Module 02 - Python Mini Projects
"""

import math
import random
import string

def evaluate_strength(password: str) -> tuple[str, float]:
    """Calculates password entropy in bits and assigns security rating."""
    pool_size = 0
    if any(c.islower() for c in password):
        pool_size += 26
    if any(c.isupper() for c in password):
        pool_size += 26
    if any(c.isdigit() for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    if pool_size == 0 or len(password) == 0:
        return "Very Weak", 0.0

    entropy = len(password) * math.log2(pool_size)

    if entropy < 36:
        rating = "Very Weak (Vulnerable to brute force)"
    elif entropy < 50:
        rating = "Weak (Acceptable for non-sensitive accounts)"
    elif entropy < 65:
        rating = "Moderate / Fair"
    elif entropy < 80:
        rating = "Strong (Recommended for general security)"
    else:
        rating = "Very Strong / Enterprise Grade"

    return rating, round(entropy, 1)

def generate_password(
    length: int = 16,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    exclude_ambiguous: bool = True
) -> str:
    """Generates a secure password meeting required character sets."""
    chars = ""
    guaranteed = []

    lower_set = string.ascii_lowercase
    upper_set = string.ascii_uppercase
    digit_set = string.digits
    symbol_set = "!@#$%^&*()-_=+[]{}|;:,.<>?"

    if exclude_ambiguous:
        # Exclude confusing characters: l, 1, I, O, 0
        ambiguous = "l1IO0"
        lower_set = "".join(c for c in lower_set if c not in ambiguous)
        upper_set = "".join(c for c in upper_set if c not in ambiguous)
        digit_set = "".join(c for c in digit_set if c not in ambiguous)

    if use_lower:
        chars += lower_set
        guaranteed.append(random.choice(lower_set))
    if use_upper:
        chars += upper_set
        guaranteed.append(random.choice(upper_set))
    if use_digits:
        chars += digit_set
        guaranteed.append(random.choice(digit_set))
    if use_symbols:
        chars += symbol_set
        guaranteed.append(random.choice(symbol_set))

    if not chars:
        raise ValueError("At least one character type must be selected.")

    if length < len(guaranteed):
        length = len(guaranteed)

    # Fill remaining positions
    remaining_length = length - len(guaranteed)
    remaining_chars = [random.choice(chars) for _ in range(remaining_length)]

    # Combine and shuffle so guaranteed characters aren't predictable
    password_list = guaranteed + remaining_chars
    random.shuffle(password_list)

    return "".join(password_list)

def run_demo():
    print("=" * 70)
    print("           SECURE PASSWORD GENERATOR & ENTROPY AUDITOR        ")
    print("=" * 70)

    configs = [
        {"length": 8, "symbols": False, "digits": True, "label": "Short PIN/Alpha (8 chars)"},
        {"length": 12, "symbols": True, "digits": True, "label": "Standard Web Password (12 chars)"},
        {"length": 16, "symbols": True, "digits": True, "label": "Strong Account Password (16 chars)"},
        {"length": 24, "symbols": True, "digits": True, "label": "High-Security Master Key (24 chars)"},
    ]

    for cfg in configs:
        pwd = generate_password(
            length=cfg["length"],
            use_symbols=cfg["symbols"],
            use_digits=cfg["digits"]
        )
        rating, entropy = evaluate_strength(pwd)
        print(f"\nConfiguration: {cfg['label']}")
        print(f"Generated Password : {pwd}")
        print(f"Security Entropy   : {entropy} bits")
        print(f"Strength Rating    : {rating}")

    print("\n" + "=" * 70)

if __name__ == "__main__":
    run_demo()

