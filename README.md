# PyDCviewer

A simple viewer for document cameras (to beamer/digital whiteboard) that offers basic image manipulation (pan, zoom, ...). PyDCviewer is written in Python 3 using OpenCV.

Its focus is to just show the webcam image and allow basic manipulations as:

- pan (with arrow keys or mouse/touch)
- zoom (by mousewheel or +/-)
- adjust color mode (color/greyscale/bw)
- adjust brightness and contrast

Additional features include:

- saving the actual frame to disk (a "silent" mode with automatic file renaming can be configured)
- webcam and resolution can be changed from menu
- fullscreen (f)
- show blank page where the color is configurable (to match digital boards background colour or for fashion-conscious people)
- show/hide ui menu buttons
- pause the actual frame (p)
- basic ocr on selectable area of the screen (thanks to pytesseract)


Installation (global, no venv, Linux):

- clone the repo: `sudo git clone https://gitlab.com/thoschi/pydcviewer.git /opt/pydcviewer`
- install dependencies: `sudo pip install -r /opt/pydcviewer/requirements.txt`

After these two steps it should be possible to run the program by `python3 /opt/pydcviewer/pydcviewer.py`. There is a desktop file to your convenience:

- link desktop-file: `sudo ln -s /opt/pydcviewer/support/pydcviewer.desktop /usr/share/applications/pydcviewer.desktop`

Installation (as user, in virtual environment, Linux):

- clone the repo: `sudo git clone https://gitlab.com/thoschi/pydcviewer.git && cd pydcviewer`
- create virtual environment: `python3 -m venv env`
- activate virtual environment: `source env/bin/activate`
- install dependencies: `pip install -r /opt/pydcviewer/requirements.txt`
- run with: `python pydcviewer.py`

There is another desktop-file for virtual env-installation in support. Adapt it to your situation.

~~For Windows there is a standalone executable in the dist directory for your convenience.~~ (not working yet)

Actual dependencies

- imutils (0.5.4) mostly for image resizing
- numpy (1.20.3) used by opencv
- opencv-python (4.5.2.52) for most image conversion
- Pillow (8.2.0) for images and text
- pyperclip (1.8.2) for copying recognized text to clipboard
- pytesseract (0.3.7) for OCR functionality
- sys, os for error handling and saving files

- Tkinter for window management (if not installed: `apt install python3-tk`)
- (to be checked) Python QT Bindings for OCR (seems not to be installed always as a dependency: `apt install python3-qt-binding`)

Any comments, ideas and contributions are welcome!

