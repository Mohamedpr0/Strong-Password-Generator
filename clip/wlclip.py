import utils.vprint
import utils.commands


def wlclip_copy(string, verbose):
    try:
        utils.commands.run_command_stdin(["wl-copy"], string)
        utils.vprint.vprint(verbose, "[INFO] string copied with wl-clip")
    except FileNotFoundError:
        utils.vprint.vprint(verbose, "[WARN] wl-clip not found")
    except Exception as e:
        err = str(e)
        utils.vprint.vprint(verbose, f"[ERR] Error on wl-clip: {err}")
