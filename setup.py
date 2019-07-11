"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['osx_main.py']
DATA_FILES = ['ndn_app.png', 'static', 'templates']
OPTIONS = {'argv_emulation': True,
           'iconfile': 'ndn_app.icns',
           'includes': [
               'asn1crypto',
               'cffi',
               'Click',
               'cryptography',
               'Flask',
               'Flask-SocketIO',
               'itsdangerous',
               'Jinja2',
               'MarkupSafe',
               'protobuf',
               'pycparser',
               'PyNDN',
               'python-engineio',
               'python-socketio',
               'six',
               'Werkzeug',
               'pystray',
               'Pillow',

               'ndncc',
               'engineio.async_drivers.threading',
               'jinja2.ext',
               ],
           'plist': {
               'CFBundleIdentifier': "com.ndn.ndncc",
               'CFBundleName': "NDNCC",
               'CFBundleVersion': '1001',
               'CFBundleShortVersionString': '1.0',
               'NSHumanReadableCopyright': 'Copyright 2019 NDN team'
           }
          }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)