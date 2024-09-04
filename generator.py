import random
import string


class PasswordGenerator:
    def generate_password(length=20, charset="full"):
        match charset:
            case "full":
                characters = string.ascii_letters \
                    + string.digits \
                    + string.punctuation
            case "alnum":
                characters = string.ascii_letters + string.digits
            case "letters":
                characters = string.ascii_letters
            case "digits":
                characters = string.digits

        password = ''.join(random.choice(characters) for _ in range(length))
        return password
