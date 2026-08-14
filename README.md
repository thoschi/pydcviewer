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

- clone the repo: `git clone https://gitlab.com/thoschi/pydcviewer.git && cd pydcviewer`
- create virtual environment: `python3 -m venv env`
- activate virtual environment: `source env/bin/activate`
- install dependencies: `pip install -r requirements.txt`
- run with: `python pydcviewer.py`

There is another desktop-file for virtual env-installation in support. Adapt it to your situation.

Command line options:

- select a camera by its device number: `python pydcviewer.py --camera 2` (uses `/dev/video2`)
- request a starting resolution: `python pydcviewer.py --resolution 1920x1080`
- set the initial zoom factor from 1 to 5: `python pydcviewer.py --zoom 1.5`
- adjust automatic menu scaling: `python pydcviewer.py --ui-scale 1.5`
- options can be combined, for example: `python pydcviewer.py -c 2 -r 1920x1080 -z 1.5`

~~For Windows there is a standalone executable in the dist directory for your convenience.~~ (not working yet)

Actual dependencies

- imutils (0.5.4) mostly for image resizing
- numpy (2.2.1) used by opencv
- opencv-python (4.10.0.84) for most image conversion
- Pillow (11.1.0) for images and text
- pyperclip (1.9.0) for copying recognized text to clipboard
- pytesseract (0.3.13) for OCR functionality
- sys, os for error handling and saving files

- Tkinter for window management (if not installed: `apt install python3-tk`)
- Tesseract for OCR (if not installed: `apt install tesseract-ocr`)

Any comments, ideas and contributions are welcome!
