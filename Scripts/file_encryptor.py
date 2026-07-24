import sys
import argparse
import getpass
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

SALT_SIZE = 16
NONCE_SIZE = 16
KEY_SIZE = 32  # AES-256


def derive_key(password, salt):
    """Derive a 256-bit AES key from a password and salt using PBKDF2."""
    return PBKDF2(password, salt, dkLen=KEY_SIZE, count=200_000)


def encrypt_file(filepath, password):
    """Encrypt a file in place-compatible form, writing output as filepath + '.enc'."""
    salt = get_random_bytes(SALT_SIZE)
    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_EAX)

    try:
        with open(filepath, "rb") as f:
            data = f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        sys.exit(1)

    ciphertext, tag = cipher.encrypt_and_digest(data)

    output_path = filepath + ".enc"
    with open(output_path, "wb") as f:
        f.write(salt)
        f.write(cipher.nonce)
        f.write(tag)
        f.write(ciphertext)

    print(f"Encrypted: {filepath} -> {output_path}")


def decrypt_file(filepath, password):
    """Decrypt a file previously encrypted with encrypt_file()."""
    try:
        with open(filepath, "rb") as f:
            salt = f.read(SALT_SIZE)
            nonce = f.read(NONCE_SIZE)
            tag = f.read(16)
            ciphertext = f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        sys.exit(1)

    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    try:
        data = cipher.decrypt_and_verify(ciphertext, tag)
    except ValueError:
        print("Decryption failed: wrong password or corrupted/tampered file.")
        sys.exit(1)

    if filepath.endswith(".enc"):
        output_path = filepath[:-4]
    else:
        output_path = filepath + ".dec"

    with open(output_path, "wb") as f:
        f.write(data)

    print(f"Decrypted: {filepath} -> {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt a file using AES-256 with a password."
    )
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Operation to perform")
    parser.add_argument("filepath", help="Path to the file to encrypt/decrypt")

    args = parser.parse_args()
    password = getpass.getpass("Password: ")

    if args.mode == "encrypt":
        encrypt_file(args.filepath, password)
    else:
        decrypt_file(args.filepath, password)
