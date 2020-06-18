import requests
import json

from api import Api

year = input("year?")
raceNumber = input("Race number?")

api = Api()
api.get_info_races(year, raceNumber)