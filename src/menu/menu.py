from src.api.api import Api
import sys


class Menu:
    dev = True

    def __init__(self, dev):
        self.dev = dev

    def _ask_input(self, msg):
        if (self.dev == True):
            return input(msg)
        else:
            return sys.stdin.readlines()[0].strip()

    def print_menu(self):
        print("________________________")
        print("Welcome to F1 App:")
        print("________________________")
        print("Choose an option:")
        print("1. Info races")
        print("2. Info constructor")
        print("3. Season list")
        print("0. Exit")

    def new_search(self):
        print("________________________")
        print("New search?")
        print("________________________")
        print("1. Yes")
        print("2. No")
        try:
            user_option = int(self._ask_input(""))
            available_entries = [1, 2]
            if user_option in available_entries:
                if user_option == 1:
                    self.menu()
                elif user_option == 2:
                    print("Bye! Hope to see you soon!")
            else:
                print("Choose one of the available options.")
                self.new_search()
        except ValueError:
            print("*** Error, choose a valid option! ***")

    def menu(self):
        while True:
            self.print_menu()
            try:
                api = Api()
                user_option = int(self._ask_input(""))
                available_entries = [0, 1, 2, 3]
                if user_option in available_entries:
                    if user_option == 1:
                        year = input(self._ask_input("year?"))
                        race_number = input(self._ask_input("Race number?"))
                        api.get_info_races(year, race_number)
                        self.new_search()
                    elif user_option == 2:
                        name = input(self._ask_input("Constructor name?"))
                        print(api.get_info_constructor(name))
                        self.new_search()
                    elif user_option == 3:
                        year = input(self._ask_input("year?"))
                        api.get_season_list(year)
                        self.new_search()
                    elif user_option == 0:
                        print("Bye! Hope to see you soon!")
                        break
                else:
                    print("Choose one of the available options.")
                    self.menu()
                break
            except ValueError:
                print("*** Error, choose a valid option! ***")
