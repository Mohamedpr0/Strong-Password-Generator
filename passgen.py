import generator
import clip

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser("passgen.py")

    parser.add_argument("-l", "--length", default=20, required=False,
                        help="Length pf password", type=int)
    parser.add_argument("-c", "--charset", default="full", required=False,
                        choices=["full", "alnum", "letters", "digits"],
                        help="Character set. Allowed: `full`, `alnum`, `letters`, `digits`")
    parser.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()

    generated_password = generator.PasswordGenerator.generate_password(
        args.length, charset=args.charset)

    print("Generated Password:", generated_password)

    clip.ClipboardDriver.copy_password(
        generated_password, verbose=args.verbose)

    print("Password copied to clipboard.")
