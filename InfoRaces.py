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
            print('\n')
            print('Circuit name: {}'.format(arrayRaces[0]['Circuit']['circuitName']))
            print('{} --- {} --- Round: {}'.format(arrayRaces[0]['raceName'], arrayRaces[0]['season'], arrayRaces[0]['round']))
            print('{}, {}'.format(arrayRaces[0]['Circuit']['Location']['locality'], arrayRaces[0]['Circuit']['Location']['country']))
            print('\n')
            arrayResults = arrayRaces[0]['Results']
            for result in arrayResults:
                print('{}. {} --- {} --- Car: {} --- Points: {}'.format(result['position'], result['Driver']['familyName'], result['Driver']['nationality'] , result['Constructor']['name'], result['points']))
        else:
            print("The race you are looking for doesn't exist")
    else:
        print("Race number error. Ex: 10")
else:
    print("Year error. Ex: 1993")



