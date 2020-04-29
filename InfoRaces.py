import requests
import json

year = input("year?")
if(year.isdigit()): #IMPROVE: change isdigit with cast to int and catch exception
    raceNumber = input("Race number?")
    if(raceNumber.isdigit()):
        r = requests.get("http://ergast.com/api/f1/{}/{}/results.json".format(year, raceNumber))
        resultsJson = r.json()
        print((resultsJson))
        total = resultsJson['MRData']['total']
        print(total)
        if(int(resultsJson['MRData']['total']) != 0):
            
        else:
            print("The race you are looking for doesn't exist")
    else:
        print("Race number error. Ex: 10")
else:
    print("Year error. Ex: 1993")



