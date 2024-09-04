import random
import string
import pyperclip
import subprocess


def generate_password(length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def run_command_stdin(command: list[str], stdin: str):
    proc = subprocess.Popen(command, stdout=subprocess.PIPE,
                            stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
    proc.communicate(input=stdin.encode())


def copy_password(password):
    """
    CROSS-PLATFORM function to copy a string into clipboard.
    """

    # Pyperclip (working on Windows)
    pyperclip.copy(password)

    # CopyQ (working on Linux)
    run_command_stdin(["copyq", "copy", "-"], password)


if __name__ == "__main__":
    generated_password = generate_password()

    print("Generated Password:", generated_password)

    copy_password(generated_password)

    print("Password copied to clipboard.")
