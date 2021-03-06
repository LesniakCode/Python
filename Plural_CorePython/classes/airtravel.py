"""Model for aircraft flights"""

class Flight:
    """
    
    """
    #talk to your friend
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")
        if not number[:2].isupper:
            raise ValueError(f"Invalid airline code '{number}'")
        if not (number[2:].isdigit() and int(number[2:]) <=9999):
            raise ValueError(f"Invalid route number '{number}'")

        self._number = number
        self._aircraft = aircraft

    def aircraft_model(self):
        return self._aircraft.model()
        
    def number(self):
        return self._number
    
    def airline(self):
        return self._number[:2]

class Aircraft:

    def __init__(self, reg, mod, num_rows, num_seats_pr):
        self._reg = reg
        self._mod = mod
        self._num_rows = num_rows
        self._num_seats_pr = num_seats_pr

    def registration(self):
        return self._reg

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows +1),
                "ABCDEFGHJK"[:self._num_seats_pr])
