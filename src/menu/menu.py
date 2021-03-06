from src.api.api import Api


class Menu:
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
            user_option = int(input(""))
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
                user_option = int(input(""))
                available_entries = [0, 1, 2, 3]
                if user_option in available_entries:
                    if user_option == 1:
                        year = input(input("year?"))
                        race_number = input(input("Race number?"))
                        api.get_info_races(year, race_number)
                        self.new_search()
                    elif user_option == 2:
                        name = input(input("Constructor name?"))
                        print(api.get_info_constructor(name))
                        self.new_search()
                    elif user_option == 3:
                        year = input(input("year?"))
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
