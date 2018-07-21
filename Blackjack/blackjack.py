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
    def draw_card(self):
        self.cards.append(deck.pop())
        self.set_score()
    def set_score(self):
        self.score = sum([card.score for card in self.cards])
        for card in self.cards:
            if card.score == 1 and self.score + 10 <= 21:
                self.score = self.score + 10
        show_cards()
        end_game()
def startnewgame():
    global deck, win, finish, player, dealer
    deck = random.sample([Card(i, _) for i in suits for _ in scores], k = 52)
    player, dealer = Hand(), Hand()
    root.hitbutton.pack(side = LEFT)
    root.staybutton.pack(side = LEFT)
    root.newgamebutton.forget()
    win, finish = False, False
    
    player.draw_card(), player.draw_card(), dealer.draw_card(), dealer.draw_card()
    end_game()
def show_cards():
    root.info.config(text = 'The Dealer is dealt \n' + str(dealer) + f'\n(score {dealer.score})\n' + 'You are dealt \n' + str(player) +\
                     f'\n(score {player.score})\n',  font = ('times', 20))
def hit_button():
    player.draw_card()
def stay_button():
    global finish
    finish = True
    end_game()
def end_game():
    global win, finish 
    if finish == False:
        if player.score > 21:
            game_over()
        elif player.score == 21:
            win = True
            game_over()
        elif len(player.cards) == 5 and player.score < 21:
            win = True
            game_over()
    else:
        if len(dealer.cards) == 5 and dealer.score <= 21:
            game_over()
        elif dealer.score < player.score <= 21:
            dealer.draw_card()
            end_game()
        elif dealer.score > 21:
            win = True
            game_over()
        elif dealer.score == player.score:
            win = 'Tie'
            game_over()
        else:
            game_over()
def game_over():
    global win
    root.hitbutton.forget()
    root.staybutton.forget()
    root.newgamebutton.pack(side = LEFT)
    if win == True:
            root.info.config(text = 'The Dealer is dealt \n' + str(dealer) + f'\n(score {dealer.score})\n' + 'You are dealt \n' + str(player) +\
                     f'\n(score {player.score})\nYOU WIN',  font = ('times', 20))
    elif win == False:
                root.info.config(text = 'The Dealer is dealt \n' + str(dealer) + f'\n(score {dealer.score})\n' + 'You are dealt \n' + str(player) +\
                     f'\n(score {player.score})\nDEALER WINS',  font = ('times', 20))
    elif win == 'Tie':
            root.info.config(text = 'The Dealer is dealt \n' + str(dealer) + f'\n(score {dealer.score})\n' + 'You are dealt \n' + str(player) +\
                     f'\n(score {player.score})\nPUSH GAME',  font = ('times', 20))
#Tkinter set up.
class Blackjack(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Blackjack")
        self.iconbitmap('spade.ico')
        self.frame = Frame(self, height = 300, width = 300, bd = 3, relief = SUNKEN, bg = 'green')
        self.maxsize(400, 1000)
        self.minsize(400, 600)
        self.hitbutton = Button(self.frame, text = 'Hit' , command =  hit_button)
        self.staybutton = Button(self.frame, text = 'Stay', command = stay_button)
        self.newgamebutton = Button(self.frame, text = "New Game", command = startnewgame)
        self.info = Label(self.frame, anchor = N, text = "Welcome to Blackjack", font = ("times", 30), height = '5', width =  500, bg = 'green', fg = 'white')
        self.open()
        
    def open(self):
        self.frame.pack(side = TOP, fill = 'both', expand = True)
        self.info.pack(side =TOP, fill = 'both', expand = True)
        self.newgamebutton.pack(side = LEFT)
root = Blackjack()
root.mainloop()

