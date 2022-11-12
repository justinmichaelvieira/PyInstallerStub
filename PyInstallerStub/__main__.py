"""Startup for the program."""
import sys

from PyInstallerStub import __version__


def main():
    # Run your startup code below this comment.
    # For example, call tkinter || PyQT && QApplication to load a ui,
    # (typically within the call to sys.exit()) or
    # run background processes and/or services.

    print("PyInstallerStub ${__version__}: Application finishing normally...")
    sys.exit()


if __name__ == "__main__":
    main()
