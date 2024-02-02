class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.set_value()

    def set_value(self):
        if self.rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            return int(self.rank)
        elif self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return (1, 11)
    
    def get_value(self):
        return self.value
     
    def __str__(self):
        return self.rank + " of " + self.suit
