import utils.commands
import utils.vprint


def copyq_copy(string, verbose):
    try:
        utils.commands.run_command_stdin(["copyq", "copy", "-"], string)
        utils.vprint.vprint(verbose, "[INFO] string copied with CopyQ")
    except FileNotFoundError:
        utils.vprint.vprint(verbose, "[WARN] CopyQ not found")
    except Exception as e:
        err = str(e)
        utils.vprint.vprint(verbose, f"[ERR] Error on CopyQ: {err}")
