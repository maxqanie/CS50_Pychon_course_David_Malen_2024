## using http request to search for a song
## use of dictionary
## Command line prompt
## use of JSON to sort out a dictionary
## Interacting with a real-life API

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Too few or too many arguments")
# This is https request using Python to the server: just like us typing URLs into a browser and hit enter
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# Finding one result of the band Weezer; note that the output is a dictionary
print(response.json())
print(json.dumps(response.json(), indent=2))

# Extracting the name of the song
o = response.json()
for result in o["results"]:
    print(result["trackName"])


if len(sys.argv) != 3:
    sys.exit("Too few or too many arguments")
response = requests.get("https://itunes.apple.com/search?entity=song&limit=" + sys.argv[1] + "&term=" + sys.argv[2])
o = response.json()
for result in o["results"]:
    print(result["trackName"])