import requests
import json
import arrow

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
            parsedDate = arrow.get(races['date']).format('MMM Do, YYYY')
            print("Round: {} --- Race: {} --- Date: {} --- Circuit: {} --- Locality: {} --- Country: {}".format(races['round'], races['raceName'], parsedDate, races['Circuit']['circuitName'], races['Circuit']['Location']['locality'], races['Circuit']['Location']['country']))
    else:
        print("There are no results for the year you are looking")

except ValueError:
    print("Please enter a year")