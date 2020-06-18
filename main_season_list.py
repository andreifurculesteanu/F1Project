import requests
import json
import arrow
from api import Api

year = input("year?")
api = Api()
api.get_season_list(year)