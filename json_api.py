import json
from urllib.request import urlopen

with urlopen("http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json") as response:
    source = response.read()
data = json.loads(source)
# print(json.dumps(data, indent=2))

dataseries=list()
temp=dict()

for item in data['dataseries']:  
    
    
    
    
    dataseries.append({
        'Timepoint':item['timepoint'],
        'Cloudcover': item['cloudcover'],
        'Seeing': item['seeing'],
        'Sransparency': item['transparency'],
        'Rh2m': item['rh2m'],
        'Lifted_index': item['lifted_index']
    })     
    
with open('Weather_forecasts.json', 'w') as f:
  json.dump(dataseries, f, indent=2)



