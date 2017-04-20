# Simple RIFT event tracker

Written in Python. Just mirrors the RIFT web API 1:1 and does minimal formatting, nothing too fancy. Ugly CSS.

## Requirements

* Python 3.5
* Yattag: `pip install yattag` , or on Ubuntu 16.10+, `apt-get install python-yattag`

Tested on Ubuntu 16.04.

## Example

See: http://yaret.uK.to/

(different, much fancier tracker @ https://rift.events/)

## Install

1. Clone the source code via git
2. Copy `config.txt.dist` to `config.txt` and customize the values as you like
3. Run `events.py` every minute via cron.

## Quick Start Recipe

Deploy a new Ubuntu 16.04 VM. You will need to know its IP later. You may want your own domain name, but this document will not cover that nor DNS setup. Log in, become root, and run the following commands:

    apt-get update && apt-get -y dist-upgrade
    apt-get -y install git python python-pip python-requests nginx
    pip install yattag
    git clone https://github.com/chennin/python-rift-event-tracker.git
    cd python-rift-event-tracker
    cp config.txt.dist config.txt

Edit `config.txt` if you wish.

Run:

    crontab -e

and paste the following on its own line:

    * * * * * $HOME/python-rift-event-tracker/events.py

Now wait a minute and then browse to http://YOUR-IP/, and you should see it!


### Disclaimer

Trion, Trion Worlds, RIFT, Storm Legion, Nightmare Tide, Starfall Prophecy, Telara, and their respective logos, are trademarks or registered trademarks of Trion Worlds, Inc. in the U.S. and other countries. This project is not affiliated with Trion Worlds or any of its affiliates.
