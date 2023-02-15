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
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
