import utils.commands


def pbcopy_copy(string):
    try:
        utils.commands.run_command_stdin(
            ["pbcopy"], string)
    except FileNotFoundError:
        pass  # Xclip not installed
