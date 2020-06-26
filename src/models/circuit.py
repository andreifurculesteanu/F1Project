class Circuit:
    name = ""
    location = ""
    country = ""

    def __init__(self, name, location, country):
        self.name = name
        self.location = location
        self.country = country

    def __str__(self):
        return "Circuit: {} --- Locality: {} --- Country: {}".format(
            self.name, self.location, self.country)
