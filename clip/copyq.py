import utils.commands


def copyq_copy(string):
    utils.commands.run_command_stdin(["copyq", "copy", "-"], string)
