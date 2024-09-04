from .pyperclip import pyperclip_copy
from .copyq import copyq_copy
from .xclip import xclip_copy
from .wlclip import wlclip_copy
from .powershell_copy import powershell_copy
from .pbcopy_copy import pbcopy_copy


class ClipboardDriver:
    def copy_password(password):
        """
        CROSS-PLATFORM function to copy a string into clipboard.
        """

        pyperclip_copy(password)
        copyq_copy(password)
        xclip_copy(password)
        wlclip_copy(password)
        powershell_copy(password)
        pbcopy_copy(password)
