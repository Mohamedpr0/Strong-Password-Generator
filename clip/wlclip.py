import utils.commands


def wlclip_copy(string):
    utils.commands.run_command_stdin(["wl-copy"], string)
