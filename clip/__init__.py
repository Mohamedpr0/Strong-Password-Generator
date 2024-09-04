import pyperclip
import utils.commands


class ClipboardDriver:
    def copy_password(password):
        """
        CROSS-PLATFORM function to copy a string into clipboard.
        """

        # Pyperclip (working on Windows)
        pyperclip.copy(password)

        # CopyQ (working on Linux)
        utils.commands.run_command_stdin(["copyq", "copy", "-"], password)
