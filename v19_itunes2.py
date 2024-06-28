import json
import requests
import sys

if len(sys.argv) != 3:
    sys.exit("Too few or too many arguments")
response = requests.get("https://itunes.apple.com/search?entity=song&limit=" + sys.argv[1] + "&term=" + sys.argv[2])
o = response.json()
for result in o["results"]:
    print(result["trackName"])