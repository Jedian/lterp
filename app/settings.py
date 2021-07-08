from prettyconf import config

"""
You can put your environment variables and secrets here, they will be read from
the machine environment variables (or a ".env" file on the project directory)

More info at https://prettyconf.readthedocs.io/en/latest/index.html
"""

MAIN_MESSAGE = config("MAIN_MESSAGE", default="Hello World!")
