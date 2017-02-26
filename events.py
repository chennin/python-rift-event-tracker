#!/usr/bin/env python
import requests
import json
import sys
import json
import time
import math
from yattag import Doc

url = "https://web-api-us.riftgame.com/chatservice/zoneevent/list?shardId="

allshards = {
  'us': {
    1701: 'Seastone',
    1702: 'Greybriar',
    1704: 'Deepwood',
    1706: 'Wolfsbane',
    1707: 'Faeblight',
    1708: 'Laethys',
    1721: 'Hailol'
  },
  'eu': {
    2702: 'Bloodiron',
    2711: 'Brutwacht',
    2714: 'Brisesol',
    2721: 'Gelidra',
    2722: 'Zaviel',
    2741: 'Typhiria'
  }
}

for dc in allshards:
  doc, tag, text = Doc().tagtext()
  with tag('html'):
    with tag('head'):
      doc.stag('meta', ('http-equiv', "Refresh"), ('content', 60))
      doc.stag('meta', ('http-equiv', "Content-Type"), ('content', "text/html; charset=UTF-8"))
      doc.stag('link', ('rel', "stylesheet"), ('type', "text/css"), ('href', "style.css"))
      with tag('title'):
        text('Rift Events')
    with tag('body'):
      with tag('h2'):
        text('Rift Events - ', dc.upper())
      for shardid in allshards[dc]:
        r = requests.get("https://web-api-" + dc + ".riftgame.com/chatservice/zoneevent/list?shardId=" + str(shardid))
        r.raise_for_status()
        data = r.json()["data"]
        for zone in data:
          if "name" in zone:
            with tag('table'):
              with tag('thead'):
                with tag('tr'):
                  for title in ['Event Name', 'Shard', 'Zone', 'Elapsed Time']:
                    with tag('th'):
                      text(title)
              with tag('tbody'):
                with tag('tr'):
                  for display in [allshards[dc][shardid], zone['zone'], zone['name'], math.floor((time.time() - zone['started']) / 60)]:
                    with tag('td'):
                       text(display)
  print(doc.getvalue())
