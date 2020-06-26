class Race:
    round_number = 0
    name = ""
    date = ""
    circuit = None

    def __init__(self, round_number, name, date, circuit):
        self.round_number = round_number
        self.name = name
        self.date = date
        self.circuit = circuit
