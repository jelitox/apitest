import time

def today(mask="%m/%d/%Y"):
"""Return the time with mask""" 
    return time.strftime(mask)
