Dependencies
============
- Python 3
  - Ubuntu 16.04 needs [New Python Versions PPA](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa)
  - Ubuntu 16.04 or later: `sudo apt install python3 python3-venv`
- Ubuntu needs `sudo apt install budgie-indicator-applet` for tray icon


Setup Development Environment
=============================
Python venv:
```bash
python3 -m venv ./venv
./venv/bin/python -m pip install -r requirements.txt
```

Execute
=======
HTTP server:
```bash
./venv/bin/python app.py
```

Tray menu:
```bash
./venv/bin/python main.py
```

Generate OSX App
================
To generate a OSX Application, Pillow needs to be compiled from source.
```bash
git clone --branch 6.1.0 https://github.com/python-pillow/Pillow.git
cd Pillow
sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /
LDFLAGS="-headerpad_max_install_names" python setup.py install
```
And then use `py2app`.
```bash
. venv/bin/activate
python setup.py py2app
```
This application needs to be codesigned manually. e.g.:
```bash
cd dist && codesign -s "76FE2218A74493CB0A06975687BCA4457E98C491" NDNCC.app --deep --force
```
