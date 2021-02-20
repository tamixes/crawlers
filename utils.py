import re

def find_term(pattern, string, flags=0):
    """Returns a clean term based on the pattern received."""

    term = re.findall(pattern, string, flags=flags)

    return term