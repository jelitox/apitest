import time

"""This module does today mask."""


def today(mask="%m/%d/%Y"):
    """
    This is the second line of the docstring.
    """
    return time.strftime(mask)
