from .pyperclip import pyperclip_copy
from .copyq import copyq_copy
from .xclip import xclip_copy
from .wlclip import wlclip_copy
from .powershell_copy import powershell_copy
from .pbcopy_copy import pbcopy_copy


class ClipboardDriver:
    def copy_password(password, verbose=False):
        """
        CROSS-PLATFORM function to copy a string into clipboard.
        """

        pyperclip_copy(password, verbose)
        copyq_copy(password, verbose)
        xclip_copy(password, verbose)
        wlclip_copy(password, verbose)
        powershell_copy(password, verbose)
        pbcopy_copy(password, verbose)
