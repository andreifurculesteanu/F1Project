import requests

# Uncomment line to replace " " with "_"
# Change var "name" with "new_name" in the request
def get_info_constructor(name):
    name = name.strip()
    name = name.replace(" ", "_")
    r = requests.get("http://ergast.com/api/f1/constructors/{}.json".format(name))
    results_json = r.json()
    print(results_json)
    if (int(results_json['MRData']['total']) != 0):
        return results_json['MRData']['ConstructorTable']['Constructors'][0]['url']

    return "The team doesn't exist"


