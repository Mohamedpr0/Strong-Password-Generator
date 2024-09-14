import subprocess


def run_command_stdin(command: list[str], stdin: str):
    proc = subprocess.Popen(command, stdout=subprocess.PIPE,
                            stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
    proc.communicate(input=stdin.encode())
