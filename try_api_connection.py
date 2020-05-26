import requests
import json

r = requests.get('http://ergast.com/api/f1/2011/5/pitstops.json')
print(r.status_code)
"""
responseJson = r.json()
mydate = responseJson['date']
print(mydate)
"""

if r.status_code == 200:
    responseJson = r.json()
    # mydate = responseJson['date']
    # print(mydate)
    print(responseJson)
    season = responseJson['MRData']['RaceTable']['Races']['season']
    print(season)