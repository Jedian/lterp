# Python Project Template

This project documentation is under construction.

## How to run
Build a virtual environment, install the project dependencies and then run it:

### Ubuntu/Debian-like
```bash
$ python -m venv .venv
$ source .venv/bin/activate
(.venv) $ poetry install
(.venv) $ python -m app
```

### Windows
```bash
$ python -m venv .venv
$ .\.venv\Scripts\Activate
(.venv) $ poetry install
(.venv) $ python -m app
```

## Environment Variables
For local development and testing, make a copy of the file `local.env` to 
`.env` and adapt it for your needs. The environment variables will be read from
it.
```bash
$ cp local.env .env
```