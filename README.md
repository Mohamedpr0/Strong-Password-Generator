# Password Generator and Clipboard Copier

![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**This Python script generates a secure random password and copies it to the clipboard for immediate use.**

## Features

- Generates a random password of default length 20 characters.
- Includes a mix of uppercase letters, lowercase letters, digits, and special characters.
- Copies the generated password to the clipboard automatically.
- Easy customization of password length.

## Usage

### Prerequisites

- Python 3.x installed on your system.
- Ability to run commands in your terminal or command prompt.

### Installation


Install the required Python packages using pip:
### pip install pyperclip
Navigate to the directory containing passgen.py.

Run the script:


python passgen.py
The generated password will be displayed on the console and copied to your clipboard automatically.

Customization
By default, the script generates a 20-character password using a mix of letters, digits, and special characters.
You can customize the length of the generated password by modifying the length parameter in the generate_password function inside generate_password.py.
Example
After running the script, the generated password will be displayed on the console and copied to your clipboard automatically. You can then paste it into your desired application or service.

Notes
Ensure pyperclip is supported on your operating system for clipboard functionality.
This script provides a convenient way to generate strong, randomized passwords for various applications.
