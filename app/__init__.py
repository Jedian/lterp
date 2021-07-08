"""
The presence of this file (even if empty) makes Python treat the directory it
is in as a importable package/subpackage. But if there is code in here, it will
be executed when it is imported.
"""

""" 
This optional variable defines what is to be imported when you write
>>> from app import *
(but to actually import packages like this is considered a bad practice)
"""
__all__ = ["__main__"]