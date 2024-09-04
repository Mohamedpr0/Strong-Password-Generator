from .pyperclip import pyperclip_copy
from .copyq import copyq_copy


class ClipboardDriver:
    def copy_password(password):
        """
        CROSS-PLATFORM function to copy a string into clipboard.
        """

        # Pyperclip (working on Windows)
        pyperclip_copy(password)

        # CopyQ (working on Linux)
        copyq_copy(password)
