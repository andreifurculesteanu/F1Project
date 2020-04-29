import requests
import json

year = input("year?")
if(year.isdigit()):
    raceNumber = input("Race number?")
    if(raceNumber.isdigit()):
        url = "http://ergast.com/api/f1/" + str(year) + "/" + str(raceNumber) + "/results.json"
        print(url)
        r = requests.get(url)
        resultsJson = r.json()
        print((resultsJson))
        total = resultsJson['MRData']['total']
        print(total)
        if(int(resultsJson['MRData']['total']) != 0):
            print("exist. all ok")
        else:
            print("The race you are looking for doesn't exist")
    else:
        print("Race number error. Ex: 10")
else:
    print("Year error. Ex: 1993")



