from random import shuffle

# Classes needed:
#   -Dealer (holds points, methods: ?)
#   -Player (holds points, methods: able to place bet, hit, stay)
#   -Table (game play itself, methods: end game, compare scores, deal card to player, deal card to dealer)
#   -Deck (holds cards, methods: shuffle, deal)


class Dealer():
    def __init__(self):
        self.name = 'Dealer'
        self.score = 0
        self.hand = [] 

class Player():
    def __init__(self, name, cash, bet=0):
        self.name = name
        self.cash = cash
        self.bet = bet
        self.hand = []

    def hit_stay():
        while True:
            player_call = input('Would you like to hit? (y/n)').lower()
            if player_call == 'y':
                return True 
            elif player_call == 'n':
                return False
            else:
                print("Please enter a 'y' or a 'n'")
                continue

    def place_bet(self):
        bet = input('How much would you like to wager?')
        wager = int(bet)
        if wager > self.cash: ####
            print('You don\'t have enough funds')
        else:
            self.cash -= wager
            self.bet += wager

class Deck():
    def __init__(self):
        self.stack = [('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('J', 11), ('Q', 12), ('K', 13)]
        self.deck = self.stack * 4
        self.shuffle()
        
    def shuffle(self):
        shuffle(self.deck)

    def deal_card(self):
        card = self.deck.pop()
        return card 


class Table():
    def __init__(self, player, cash=500):
        self.dealer = Dealer()
        self.player = Player(player, cash)
        self.deck = Deck()
        self.begin_game()

    def begin_game(self):
        self.deck.shuffle()
        self.player.place_bet()
        # deal cards
        print('Dealer\'s cards are ...')
        self.deal_card(self.dealer) 
        self.deal_card(self.dealer) 

        print('Player\'s cards are ... ')
        self.deal_card(self.player) 
        self.deal_card(self.player) 
        # calc scores
        self.calc_score(self.dealer)
        self.calc_score(self.player)

        self.run()

    # run game
    def run(self):
        while True:
            player_move = self.player.hit_stay()
            if player_move is True:
                self.deal_card(self.player)
                self.calc_score(self.player)
            elif player_move is False:
                self.dealer_hit()


    def deal_card(self, player):
        card = self.deck.stack.pop()
        player.hand.append(card)
        print(f"{card}")


    def dealer_hit(self):
        score = self.dealer.score
        while True:
            if score < 17:
                self.deal_card(self.dealer)
                self.calc_score(self.dealer)
            elif score >= 17:
                self.final_score()


    def calc_score(self, player):
        score = 0 
        for card in player.hand:
            score += card[1]
        player.score = score 
        if player.score > 21:
            player.score -= 10
            player.score = score 
        self.check_hand(score, player)
        return 
    

    def check_hand(self, score, player):
        if score > 21:
            print(f"{player.name} busts!")
            self.end()
        elif score == 21:
            print(f"{player.name} has Blackjack! You win!")
            self.end()
        else:
            return
        

    def final_score(self):
        dealer_score = self.dealer.score
        player_score = self.player.score
        if dealer_score > player_score:
            print("Dealer wins!")
            self.end()
        else:
            print(f"{self.player.name} wins!")
            print(f"You have walked away with ${self.player.cash}!")


    def end(self):
        player_acc = self.player.cash
        if player_acc >= 10:
            play_again = input("Would you like to play again? (y/n)").lower()
            if play_again == 'y':
                blackjack()
            else: 
                print(f"Thanks for playing!")
                return 
        

def blackjack():
    player_name = input('Welcome to BlackJack! Please input your name:   ')
    Table(player_name)

blackjack()