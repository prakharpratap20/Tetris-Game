from setuptools import setup

APP = ['main.py']
DATA_FILES = []  # Include additional data files if needed
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pygame'],  # Add any other necessary packages
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
