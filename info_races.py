import requests
import json

year = input("year?")
if(year.isdigit()): #IMPROVE: change isdigit with cast to int and catch exception
    raceNumber = input("Race number?")
    if(raceNumber.isdigit()):
        r = requests.get("http://ergast.com/api/f1/{}/{}/results.json".format(year, raceNumber))
        resultsJson = r.json()
        if(int(resultsJson['MRData']['total']) != 0):
            arrayRaces = resultsJson['MRData']['RaceTable']['Races']
            circuit = arrayRaces[0]['Circuit']
            print()
            print('Circuit name: {}'.format(circuit['circuitName']))
            print('{} --- {} --- Round: {}'.format(arrayRaces[0]['raceName'], arrayRaces[0]['season'], arrayRaces[0]['round']))
            print('{}, {}'.format(circuit['Location']['locality'], circuit['Location']['country']))
            print()
            arrayResults = arrayRaces[0]['Results']
            for result in arrayResults:
                driver = result['Driver']
                print('{}. {} --- {} --- Car: {} --- Points: {}'.format(result['position'], driver['familyName'], driver['nationality'] , result['Constructor']['name'], result['points']))
        else:
            print("The race you are looking for doesn't exist")
    else:
        print("Race number error. Ex: 10")
else:
    print("Year error. Ex: 1993")



