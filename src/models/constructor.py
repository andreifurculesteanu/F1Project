class Constructor:
    name =""
    url = ""

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __str__(self):
        return "Team: {} --- Url: {} ".format(self.name, self.url)