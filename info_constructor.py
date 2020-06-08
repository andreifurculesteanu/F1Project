from api import Api

name = input("Constructor name?")

api = Api()
print(api.get_info_constructor(name))
