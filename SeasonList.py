import requests
import json

year = input("year?")
try:
    intYear = int(year)
    r = requests.get("http://ergast.com/api/f1/{}.json".format(intYear))
    resultsJson = r.json()
    if(int(resultsJson['MRData']['total']) != 0):
        
    else:
        print("There are no results for the year you are looking")

except ValueError:
    print("Please enter a year")