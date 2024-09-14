import utils.vprint
import utils.commands


def xclip_copy(string, verbose):
    try:
        utils.commands.run_command_stdin(["xclip"], string)
        utils.vprint.vprint(verbose, "[INFO] string copied with xclip")
    except FileNotFoundError:
        utils.vprint.vprint(verbose, "[WARN] xclip not found")
    except Exception as e:
        err = str(e)
        utils.vprint.vprint(verbose, f"[ERR] Error on xclip: {err}")
