from app import settings

def main():
    print(settings.MAIN_MESSAGE)

if __name__ == '__main__':
    """
    This will only be run when you "run" the package, for instance:
    $ python -m app
    """
    main()