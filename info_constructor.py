from api import get_info_constructor

name = input("Constructor name?")
api = get_info_constructor(name)
print(name)
print(api)