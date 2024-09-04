import utils.commands


def powershell_copy(string):
    try:
        utils.commands.run_command_stdin(
            ["powershell.exe", "-c", "Set-Clipboard"], string)
    except FileNotFoundError:
        pass  # Xclip not installed
