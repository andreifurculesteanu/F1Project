import requests


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
