import sys


def vprint(verbose, message):
    if verbose:
        print(message, file=sys.stderr)
