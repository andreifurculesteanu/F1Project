import requests
import arrow

from src.models.circuit import Circuit
from src.models.constructor import Constructor
from src.models.race import Race


class Api:
    base_url = "http://ergast.com/{}"

    # Starts with _ because it's private
    def _make_request(self, url):
        request = requests.get(self.base_url.format(url))
        return request.json()

    def get_info_constructor(self, name):
        name = name.strip()
        name = name.replace(" ", "_")
        results_json = self._make_request("api/f1/constructors/{}.json".format(name))
        if int(results_json['MRData']['total']) != 0:
            constructor = Constructor(results_json['MRData']['ConstructorTable']['Constructors'][0]['name'], results_json['MRData']['ConstructorTable']['Constructors'][0]['url'])
            print(constructor)
        else:
            print("The team doesn't exist")

    def get_season_list(self, year):
        try:
            int_year = int(year)
            results_json = self._make_request("api/f1/{}.json".format(int_year))
            if int(results_json['MRData']['total']) != 0:
                array_race = results_json['MRData']['RaceTable']['Races']
                print("Year: {}".format(int_year))
                for races in array_race:
                    races_circuit = races['Circuit']
                    circuit = Circuit(races_circuit['circuitName'], races_circuit['Location']['locality'], races_circuit['Location']['country'])
                    parsed_date = arrow.get(races['date']).format('MMM Do, YYYY')
                    race = Race(races['round'], races['raceName'], parsed_date, circuit)
                    print(race)
            else:
                print("There are no results for the year you are looking")
        except ValueError:
            print("Please enter a year")

    def get_info_races(self, year, race_number):
        try:
            int_year = int(year)
            if int_year < 1950 or int_year > 2020:
                print("Formula 1 has started in 1950, and we are in 2020")
            else:
                try:
                    int_race_number = race_number
                    results_json = self._make_request("api/f1/{}/{}/results.json".format(year, int_race_number))
                    if int(results_json['MRData']['total']) != 0:
                        array_races = results_json['MRData']['RaceTable']['Races']
                        circuit = array_races[0]['Circuit']
                        print()
                        print('Circuit name: {}'.format(circuit['circuitName']))
                        print('{} --- {} --- Round: {}'.format(array_races[0]['raceName'], array_races[0]['season'],
                                                               array_races[0]['round']))
                        print('{}, {}'.format(circuit['Location']['locality'], circuit['Location']['country']))
                        print()
                        array_results = array_races[0]['Results']
                        for result in array_results:
                            driver = result['Driver']
                            print('{}. {} --- {} --- Car: {} --- Points: {}'.format(result['position'], driver['familyName'],
                                                                                    driver['nationality'],
                                                                                    result['Constructor']['name'],
                                                                                    result['points']))
                    else:
                        print("The race you are looking for doesn't exist")
                except ValueError:
                    print("Race number error. Ex: 10")
        except ValueError:
            print("Year error. Ex: 1993")
