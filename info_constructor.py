from api import Api

name = input("Constructor name?")
# api = get_info_constructor(name)
# print(api)

url = "api/f1/constructors/{}.json"
api = Api()
print(api.get_info_constructor(url, name))
