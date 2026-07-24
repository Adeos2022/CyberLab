import sys
import argparse
import string


def shift_char(char, shift):
    """Shift a single character by the given amount, wrapping around the alphabet."""
    if char.isupper():
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    elif char.islower():
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
        return char


def caesar_encrypt(text, shift):
    """Encrypt text using a Caesar cipher with the given shift."""
    return "".join(shift_char(c, shift) for c in text)


def caesar_decrypt(text, shift):
    """Decrypt text using a Caesar cipher with the given shift."""
    return "".join(shift_char(c, -shift) for c in text)


def caesar_crack(text):
    """Try all 25 possible shifts and print each result, for brute-force cracking."""
    for shift in range(1, 26):
        print(f"Shift {shift:2}: {caesar_decrypt(text, shift)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Encrypt, decrypt, or brute-force crack Caesar cipher text."
    )
    parser.add_argument("mode", choices=["encrypt", "decrypt", "crack"], help="Operation to perform")
    parser.add_argument("text", help="Text to process")
    parser.add_argument("-s", "--shift", type=int, default=3, help="Shift amount (default: 3, ignored for crack mode)")

    args = parser.parse_args()

    if args.mode == "encrypt":
        print(caesar_encrypt(args.text, args.shift))
    elif args.mode == "decrypt":
        print(caesar_decrypt(args.text, args.shift))
    else:
        caesar_crack(args.text)
