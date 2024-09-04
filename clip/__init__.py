from .pyperclip import pyperclip_copy
from .copyq import copyq_copy
from .xclip import xclip_copy
from .wlclip import wlclip_copy


class ClipboardDriver:
    def copy_password(password):
        """
        CROSS-PLATFORM function to copy a string into clipboard.
        """

        pyperclip_copy(password)
        copyq_copy(password)
        xclip_copy(password)
        wlclip_copy(password)
