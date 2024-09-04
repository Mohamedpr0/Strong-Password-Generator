import utils.commands


def xclip_copy(string):
    utils.commands.run_command_stdin(["xclip"], string)
