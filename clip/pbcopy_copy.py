import utils.vprint
import utils.commands


def pbcopy_copy(string, verbose):
    try:
        utils.commands.run_command_stdin(["pbcopy"], string)
        utils.vprint.vprint(verbose, "[INFO] string copied with pbcopy")
    except FileNotFoundError:
        utils.vprint.vprint(verbose, "[WARN] pbcopy not found")
    except Exception as e:
        err = str(e)
        utils.vprint.vprint(verbose, f"[ERR] Error on pbcopy: {err}")
