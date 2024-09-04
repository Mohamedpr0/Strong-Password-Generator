import utils.commands


def xclip_copy(string):
    try:
        utils.commands.run_command_stdin(["xclip"], string)
    except FileNotFoundError:
        pass  # Xclip not installed
