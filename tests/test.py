"""This module does today mask."""
import time

def today(mask="%m/%d/%Y"):
    """
    This is the second line of the docstring.
    """
    return time.strftime(mask)
