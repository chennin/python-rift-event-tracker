#!/usr/bin/env python
import requests
import time
import math
import os
import tempfile
from yattag import Doc

outputdir = "./"

allshards = {
  'us': {
    1704: 'Deepwood',
    1707: 'Faeblight',
    1702: 'Greybriar',
    1721: 'Hailol',
    1708: 'Laethys',
    1701: 'Seastone',
    1706: 'Wolfsbane',
  },
  'eu': {
    2702: 'Bloodiron',
    2714: 'Brisesol',
    2711: 'Brutwacht',
    2721: 'Gelidra',
    2741: 'Typhiria',
    2722: 'Zaviel',
  }
}

url = "https://web-api-us.riftgame.com/chatservice/zoneevent/list?shardId="
os.environ['TZ'] = 'America/Los_Angeles'

for dc in allshards:
  # Construct a page at a time
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
      # Links to other DCs
      with tag('p'):
        for otherdc in allshards:
          if (otherdc != dc):
            with tag('a', href = otherdc + ".html"):
              text(otherdc.upper())
      # Event table
      with tag('table'):
        with tag('thead'):
          with tag('tr'):
            for title in ['Shard', 'Zone', 'Event Name', 'Elapsed Time']:
              with tag('th'):
                text(title)
        with tag('tbody'):
          # Get each shard's events
          for shardid in sorted(allshards[dc], key=allshards[dc].get):
            r = requests.get("https://web-api-" + dc + ".riftgame.com/chatservice/zoneevent/list?shardId=" + str(shardid))
            r.raise_for_status() # fail
            data = r.json()["data"]
            displayshard = allshards[dc][shardid]
            for zone in data:
              # An event is running in a zone, so add a table row
              if "name" in zone:
                with tag('tr'):
                  with tag('td', klass = "bold"):
                    text(displayshard)
                  zoneclass = "old"
                  if zone['zone'] in ['Ashenfell', 'Scatherran Forest', 'Xarth Mire', 'Gedlo Badlands']:
                    zoneclass = "bold"
                  for display in [zone['zone'], zone['name'], str(int( math.floor((time.time() - zone['started']) / 60) )) + " min" ]:
                    with tag('td', klass = zoneclass):
                      text(display)
                # already printed the shard name, so clear it
                displayshard = ""
      with tag('p', klass = 'small'):
        text(time.strftime("%x %X %Z"))
  # Write page then move it over the old one
  with tempfile.NamedTemporaryFile(delete=False) as outfile:
    outfile.write(doc.getvalue().encode('utf8'))
    os.chmod(outfile.name, 0644)
  os.rename(outfile.name, outputdir + dc + ".html")
