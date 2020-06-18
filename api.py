import requests
import arrow


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
        print(results_json)
        if int(results_json['MRData']['total']) != 0:
            return results_json['MRData']['ConstructorTable']['Constructors'][0]['url']
        return "The team doesn't exist"

    def get_season_list(self, year):
        try:
            int_year = int(year)
            results_json = self._make_request("api/f1/{}.json".format(int_year))
            if int(results_json['MRData']['total']) != 0:
                array_race = results_json['MRData']['RaceTable']['Races']
                print("Year: {}".format(int_year))
                for races in array_race:
                    parsed_date = arrow.get(races['date']).format('MMM Do, YYYY')
                    print("Round: {} --- Race: {} --- Date: {} --- Circuit: {} --- Locality: {} --- Country: {}".format(
                        races['round'], races['raceName'], parsed_date, races['Circuit']['circuitName'],
                        races['Circuit']['Location']['locality'], races['Circuit']['Location']['country']))
            else:
                print("There are no results for the year you are looking")
        except ValueError:
            print("Please enter a year")