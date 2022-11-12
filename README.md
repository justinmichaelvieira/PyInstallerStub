# PyInstallerStub
Python3 "stub" meant to wrap the `__main__.py` file of a standard module, for mostly-painless deployment with the PyInstaller bundler.

## Development
- `python3 -m PyInstallerStub` executes the project.
- `PyInstallerStub\__main__.py` is the entry point of the app. Typically, you will start your edits, there.
- Optional: You may want to all occurences of `PyInstallerStub` in the python module files/filenames to whatever you want to name your project.

## When ready to bundle binary
Use:
- `pip install -r requirements.txt` - installs latest available version of PyInstaller
- `pyinstaller --onefile PyInstallerStub/__main__.py` - generates a binary at `dist/__main__` (rename this binary executable to whatever you want before sharing it),
