# Simple RIFT event tracker

Written in Python. Just mirrors the RIFT web API 1:1 and does minimal formatting, nothing too fancy. Ugly CSS.

Requirements:

* Python 2 or 3
* `pip install yattag` , or on Ubuntu 16.10+, `apt-get install python-yattag`

Tested on Ubuntu 16.04.

Change the outputdir variable in `events.py`, or the HTML pages will be generated in the current directory.

Add a little custom text by copying `custom.txt.dist` to `custom.txt` and editing `custom.txt`. This text will not be interpreted (must be plain text). Or, change the source code as you wish!

Run the script every minute via cron.

Live version @ http://yaret.uK.to/; much fancier tracker @ http://yaret.uS.to/
