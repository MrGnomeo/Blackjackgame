import random
from tkinter import *
#card set-up
suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
scores = {'Ace':1 , 'King': 10, 'Queen': 10, 'Jack': 10, 'Ten' : 10, 'Nine' : 9, 'Eight' : 8 ,\
           'Seven' : 7 , 'Six' : 6, 'Five' : 5, 'Four' : 4, 'Three' : 3, 'Two' : 2}

class Card():
    """Creates a card with suit, rank, score, and a string format"""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.score = scores[value]
        self.string = f'{self.value} of {self.suit}'

class Hand():
    """Creates a hand object of card objects with the ability to draw them, 
    total the score, and give a nice string format of all of the cards."""
    def __init__(self):
        self.cards = []
        self.score = 0
    def __repr__(self):
        return '\n'.join([card.string for card in self.cards])
    def set_score(self):
        self.score = sum([card.score for card in self.cards])
        for card in self.cards:
            if card.score == 1 and self.score + 10 <= 21:
                self.score = self.score + 10
            else:
                pass
        root.show_cards()
        root.end_game()
    def __call__(self):
        self.cards.append(root.deck.pop())
        self.set_score()
#Tkinter set up.

class Blackjack(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Blackjack")
        self.iconbitmap('spade.ico')
        self.frame = Frame(self, height = 300, width = 300, bd = 3, relief = SUNKEN, bg = 'green')
        self.maxsize(400, 1000)
        self.minsize(400, 600)
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.hitbutton = Button(self.frame, text = 'Hit' , command =  self.player_hand)
        self.staybutton = Button(self.frame, text = 'Stay', command = self.stay_button)
        self.newgamebutton = Button(self.frame, text = "New Game", command = self.startnewgame)
        self.info = Label(self.frame, anchor = N, text = "Welcome to Blackjack", font = ("times", 30), height = '5', width =  500, bg = 'green', fg = 'white')
        self.open()
        self.finish = False
        self.win = False
        self.cards_list = [Card(i, _) for i in suits for _ in scores]
    def startnewgame(self):
        if self.finish == True:
            self.finish = False
            self.win = False
            self.player_hand.cards.clear()
            self.dealer_hand.cards.clear()
        else:
            pass
        self.deck = self.create_deck(self.cards_list)
        self.hitbutton.pack(side = LEFT)
        self.staybutton.pack(side = LEFT)
        self.newgamebutton.forget()
        self.player_hand(), self.player_hand(), self.dealer_hand(), self.dealer_hand(), self.end_game()
    def create_deck(self, cards_list):
        return random.sample(cards_list, k = 52)
        
    def open(self):
        self.frame.pack(side = TOP, fill = 'both', expand = True)
        self.info.pack(side =TOP, fill = 'both', expand = True)
        self.newgamebutton.pack(side = LEFT)
    def stay_button(self):
        self.finish = True
        self.end_game()
    def show_cards(self):
        self.info.config(text = 'The Dealer is dealt \n' + str(self.dealer_hand) + f'\n(score {self.dealer_hand.score})\n' + 'You are dealt \n' + str(self.player_hand) +\
                     f'\n(score {self.player_hand.score})\n' , font = ('times', 20))
    def end_game(self): 
        if self.finish == False:
            if self.player_hand.score > 21:
                self.finish = True
                self.game_over()
            elif self.player_hand.score == 21:
                self.finish = True
                self.win = True
                self.game_over()
                
            elif len(self.player_hand.cards) == 5 and self.player_hand.score < 21:
                self.win = True
                self.finish = True
                self.game_over()
        elif self.finish == True and self.win == False:
            if len(self.dealer_hand.cards) == 5 and self.dealer_hand.score <= 21:
                self.game_over()
            elif self.dealer_hand.score < self.player_hand.score <= 21:
                self.dealer_hand()
                self.end_game()
            elif self.dealer_hand.score > 21:
                self.win = True
                self.game_over()
            elif self.dealer_hand.score == self.player_hand.score:
                self.win = 'Tie'
                self.game_over()
            else:
                self.game_over()
    def game_over(self):
        self.hitbutton.forget()
        self.staybutton.forget()
        self.newgamebutton.pack(side = LEFT)
        if self.win == True:
                self.info.config(text = 'The Dealer is dealt \n' + str(self.dealer_hand) + f'\n(score {self.dealer_hand.score})\n' + 'You are dealt \n' + str(self.player_hand) +\
                     f'\n(score {self.player_hand.score})\nYOU WIN',  font = ('times', 20))
        elif self.win == False:
                self.info.config(text = 'The Dealer is dealt \n' + str(self.dealer_hand) + f'\n(score {self.dealer_hand.score})\n' + 'You are dealt \n' + str(self.player_hand) +\
                     f'\n(score {self.player_hand.score})\nDEALER WINS',  font = ('times', 20))
        elif self.win == 'Tie':
                self.info.config(text = 'The Dealer is dealt \n' + str(self.dealer_hand) + f'\n(score {self.dealer_hand.score})\n' + 'You are dealt \n' + str(self.player_hand) +\
                     f'\n(score {self.player_hand.score})\nPUSH GAME',  font = ('times', 20))
root = Blackjack()
root.mainloop()

