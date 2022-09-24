# Password Generator
## Cross-platform GUI password generator written in Python

# Application Build:
## Install nuitka: ```pip install nuitka```
### Windows: ```nuitka --onefile --follow-imports --enable-plugin=pyside6 --windows-disable-console --windows-icon-from-ico=ui\icons\app-icon.ico --remove-output -o password-generator.exe app.py```
### Linux: ```python -m nuitka --onefile --follow-imports --enable-plugin=pyside6 --remove-output app.py```
### macOS: ```python3 -m nuitka --onefile --follow-imports --enable-plugin=pyside6 --macos-create-app-bundle --remove-output -o password-generator.app app.py```
