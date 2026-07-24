import sys
import re
import argparse


COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123",
    "letmein", "monkey", "111111", "iloveyou", "admin",
    "welcome", "password1", "123456789", "football",
}


def check_password(password):
    """Evaluate a password's strength and return a score with feedback."""
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        return 0, ["This is one of the most commonly used passwords in the world. Do not use it."]

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short — use at least 12 characters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    else:
        feedback.append("Add special characters (e.g. !@#$%).")

    if re.search(r"(.)\1{2,}", password):
        feedback.append("Avoid repeating the same character 3+ times in a row.")
        score -= 1

    return max(score, 0), feedback


def rate(score):
    """Convert a numeric score into a human-readable strength label."""
    if score <= 1:
        return "Very Weak"
    elif score <= 3:
        return "Weak"
    elif score <= 5:
        return "Moderate"
    else:
        return "Strong"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check a password's strength against common security criteria."
    )
    parser.add_argument("password", help="Password to evaluate")

    args = parser.parse_args()
    score, feedback = check_password(args.password)

    print(f"\nStrength: {rate(score)} (score: {score}/6)")
    if feedback:
        print("\nSuggestions:")
        for f in feedback:
            print(f"  - {f}")
    else:
        print("No issues found.")
