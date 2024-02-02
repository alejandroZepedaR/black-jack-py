import Player

class Dealer(Player):
    def __init__(self, name, hand, money):
        Player.__init__(self, name, hand, money)
        self.hidden_card = None
    
    def draw_hidden(self, card):
        self.hidden_card = card
    
    def show_hidden(self):
        return self.hidden_card
    