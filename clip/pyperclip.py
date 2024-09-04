def pyperclip_copy(string):
    try:
        import pyperclip
        pyperclip.copy(string)
    except ImportError:
        pass  # pyperclip is not installed
