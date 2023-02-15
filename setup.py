from setuptools import setup

APP = ['image-orientation-finder.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'includes': ['tkinter'],
    'packages': ['PIL'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'pyinstaller': OPTIONS},
    setup_requires=['pyinstaller'],
    install_requires=['Pillow'],
)
