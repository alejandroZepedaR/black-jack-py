class Player:
    def __init__(self, name, hand, money):
        self.name = name
        self.hand = hand
        self.money = money

    def draw(self, card):
        self.hand.append(card)
    
    def win_bet(self, bet):
        self.money += bet
    
    def lose_bet(self, bet):
        self.money -= bet
    
    def get_hand(self):
        return self.hand
    
    def get_money(self):
        return self.money
    
    def calculate_hand(self):
        total = 0
        aces = 0
        for card in self.hand:
            if card.get_value() == (1, 11):
                aces += 1
            else:
                total += card.get_value()
        
        if aces > 0:
            if total + 11 + (aces - 1) > 21:
                total += aces
            else:
                total += 11 + (aces - 1)
                
        return total

    def __str__(self):
        return self.name + " has " + str(self.money) + " dollars."
    
