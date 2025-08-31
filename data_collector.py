import re
import json
import requests

all_uris=[]
# i havent included cities with a space in their name like 'Las Vegas'
locations='Anaheim Antlanta Austin Charlotte Chicago Cleveland DAllas Denver Detroit Houston Indianapolis Memphis Miami Minneapolis Nashville New Orleans New York City Omaha Philadelphia Pheonix Pittsburgh Portland Sacramento Seattle Tampa Washington'.split(' ')
subset=locations[0:1]
for city in subset:
    response = requests.get(f'https://charts.spotify.com/charts/view/citytoptrack-{city}-weekly/2025-08-28')
    uris = re.findall(r'https://open\.spotify\.com/track/[a-zA-Z0-9]+', response.text)
    all_uris.extend(uris)
print(all_uris)