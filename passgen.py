import generator
import clip


if __name__ == "__main__":
    generated_password = generator.PasswordGenerator.generate_password()

    print("Generated Password:", generated_password)

    clip.ClipboardDriver.copy_password(generated_password)

    print("Password copied to clipboard.")
