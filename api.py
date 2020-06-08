import requests

class Api:

    base_url = "http://ergast.com/{}"

    # Starts with _ because it's private
    def _make_request(self, url):
        request = requests.get(self.base_url.format(url))
        return request.json()

    # URL has to come with {} to add constructor name
    def get_info_constructor(self, url, name):
        name = name.strip()
        name = name.replace(" ", "_")
        url = url.format(name)
        results_json = self._make_request(url)
        print(results_json)
        if (int(results_json['MRData']['total']) != 0):
            return results_json['MRData']['ConstructorTable']['Constructors'][0]['url']
        return "The team doesn't exist"

    # Uncomment line to replace " " with "_"
    # Change var "name" with "new_name" in the request
    # def get_info_constructor(self, name):
    #     name = name.strip()
    #     name = name.replace(" ", "_")
    #     r = requests.get("http://ergast.com/api/f1/constructors/{}.json".format(name))
    #     results_json = r.json()
    #     print(results_json)
    #     if (int(results_json['MRData']['total']) != 0):
    #         return results_json['MRData']['ConstructorTable']['Constructors'][0]['url']
    #     return "The team doesn't exist"


