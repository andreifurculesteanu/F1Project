import requests
import json

year = input("year?")
try:
    intYear = int(year)
    r = requests.get("http://ergast.com/api/f1/{}.json".format(intYear))
    resultsJson = r.json()
    print(resultsJson)
    if(int(resultsJson['MRData']['total']) != 0):
        arrayRaces = resultsJson['MRData']['RaceTable']['Races']
        print("Year: {}".format((intYear)))
        for races in arrayRaces:
            print("Round: {} --- Race: {} --- Date: {} --- Circuit: {} --- Locality: {} --- Country: {}".format(races['round'], races['raceName'], races['date'], races['Circuit']['circuitName'], races['Circuit']['Location']['locality'], races['Circuit']['Location']['country']))
    else:
        print("There are no results for the year you are looking")

except ValueError:
    print("Please enter a year")