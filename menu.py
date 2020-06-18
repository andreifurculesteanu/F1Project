from api import Api


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

    def menu(self):
        while True:
            self.print_menu()
            try:
                user_option = int(input(""))
                if user_option in range(5):
                    if user_option == 1:
                        year = input("year?")
                        race_number = input("Race number?")
                        api = Api()
                        api.get_info_races(year, race_number)
                    elif user_option == 2:
                        name = input("Constructor name?")
                        api = Api()
                        print(api.get_info_constructor(name))
                    elif user_option == 3:
                        year = input("year?")
                        api = Api()
                        api.get_season_list(year)
                    elif user_option == 0:
                        print("Bye! Hope to see you soon!")
                        break
                else:
                    print("Choose one of the available options.")
                break
            except ValueError:
                print("*** Error, choose a valid option! ***")