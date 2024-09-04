import utils.commands


def wlclip_copy(string):
    try:
        utils.commands.run_command_stdin(["wl-copy"], string)
    except FileNotFoundError:
        pass  # wl-clip not installed
