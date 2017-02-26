#!/usr/bin/env python
import requests
import json
import sys
import json
import genshi

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
  for shardid in allshards[dc]:
    r = requests.get('https://web-api-' + dc + '.riftgame.com/chatservice/zoneevent/list?shardId=' + str(shardid))
    r.raise_for_status()
    data = r.json()["data"]
    for zone in data:
      if "name" in zone:
        print allshards[dc][shardid] + " " + zone['zone'] + " " + zone["name"]
    sys.exit()
