import utils.vprint
import utils.commands


def powershell_copy(string, verbose):
    try:
        utils.commands.run_command_stdin(
            ["powershell.exe", "-c", "Set-Clipboard"], string)
        utils.vprint.vprint(verbose, "[INFO] string copied with powershell")
    except FileNotFoundError:
        utils.vprint.vprint(verbose, "[WARN] powershell not found")
    except Exception as e:
        err = str(e)
        utils.vprint.vprint(verbose, f"[ERR] Error on powershell: {err}")
