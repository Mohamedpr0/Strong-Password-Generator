import utils.vprint


def pyperclip_copy(string, verbose):
    try:
        import pyperclip
        pyperclip.copy(string)
        utils.vprint.vprint(verbose, "[INFO] string copied with Pyperclip")
    except ImportError:
        utils.vprint.vprint(verbose, "[WARN] Pyperclip not found")
    except Exception as e:
        err = str(e)
        utils.vprint.vprint(verbose, f"[ERR] Error on Pyperclip: {err}")
