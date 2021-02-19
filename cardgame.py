# Creates a version of Suck the Well A caribbean cardgame similar to Egyptian Rat Screw
# Or War. Opponents reveal the top card on their deck alternating turns until one person
# reveals a face card or ace. The opponent then has 1-4 cards to also play
# a face card or lose the pile. The number of cards relates to the face card played.
# The game ends when one player has all the cards
import random


class card:                                                 #This class allows us to store our cards suit and value as well as find out if it's a face card or not

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def isFace(self):
        if isinstance(self.value, str):
            return True
        else:
            return False




#This was just to create all of the cards in a 52 card deck

H2 = card('hearts',2)
H3 = card('hearts',3)
H4 = card('hearts',4)
H5 = card('hearts',5)
H6 = card('hearts',6)
H7 = card('hearts',7)
H8 = card('hearts',8)
H9 = card('hearts',9)
H10 = card('hearts',10)
HJ = card('hearts','J')
HQ = card('hearts','Q')
HK = card('hearts','K')
HA = card('hearts','A')
S2 = card('spades',2)
S3 = card('spades',3)
S4 = card('spades',4)
S5 = card('spades',5)
S6 = card('spades',6)
S7 = card('spades',7)
S8 = card('spades',8)
S9 = card('spades',9)
S10 = card('spades',10)
SJ = card('spades','J')
SQ = card('spades','Q')
SK = card('spades','K')
SA = card('spades','A')
C2 = card('clubs',2)
C3 = card('clubs',3)
C4 = card('clubs',4)
C5 = card('clubs',5)
C6 = card('clubs',6)
C7 = card('clubs',7)
C8 = card('clubs',8)
C9 = card('clubs',9)
C10 = card('clubs',10)
CJ = card('clubs','J')
CQ = card('clubs','Q')
CK = card('clubs','K')
CA = card('clubs','A')
D2 = card('diamonds',2)
D3 = card('diamonds',3)
D4 = card('diamonds',4)
D5 = card('diamonds',5)
D6 = card('diamonds',6)
D7 = card('diamonds',7)
D8 = card('diamonds',8)
D9 = card('diamonds',9)
D10 = card('diamonds',10)
DJ = card('diamonds','J')
DQ = card('diamonds','Q')
DK = card('diamonds','K')
DA = card('diamonds','A')

#then we put all of those cards into our deck
deck = [H2, H3, H4, H5, H6, H7, H8, H9, H10, HJ, HQ, HK, HA,
        S2, S3, S4, S5, S6, S7, S8, S9, S10, SJ, SQ, SK, SA,
        C2, C3, C4, C5, C6, C7, C8, C9, C10, CJ, CQ, CK, CA,
        D2, D3, D4, D5, D6, D7, D8, D9, D10, DJ, DQ, DK, DA]

#these are our global variables that we use throughout the program and in various functions

turn = 0                                       #keeps track of turns
you = []                                       #reperesents your deck
cpu = []                                       #represents the computer's deck
pile = []                                      #represents the common pile you're playing on

def whoseTurn():                               #a function to help figure out whose turn it is at any point
    global turn
    global you
    global cpu
    if turn == 1:
        return you
    else:
        return cpu

def playerName():                              #gives the current player as a string
    global turn
    if turn == 0:
        return 'cpu'
    else:
        return 'you'

def whoIsOpp():                                #similar to whoseTurn() but for the opponent
    global turn
    global you
    global cpu
    if turn == 1:
        return cpu
    else:
        return you

def oppName():                                 #similar to playerName() but for the opponent
    global turn
    if turn == 1:
        return 'cpu'
    else:
        return 'you'



def deal(deck, players):                            #function to help deal the cards to all the players
    random.shuffle(deck)
    numPlayers = len(players)        #alias
    count = 0                        #alias
    for card in deck:
        players[count].append(card)
        count = (count + 1)%numPlayers             #this function works for any number of players but for our game it's only 2 people

def changeTurn():                                   #this function helps us change the turn between plays
    global turn
    turn = (turn +1)%2


def checkCard(card):                               #this function helps to see if the card played is a face card and then prompts a response
    num = 0    #alias
    if card.isFace() == True:
        if card.value == 'J':
            num = 1                                #you get 1 card to beat a jack
            print('opponent has one card to play a face card')
        elif card.value == 'Q':
            num = 2                                #two cards to beat a queen
            print('opponent has two cards to play a face card')
        elif card.value == 'K':
            num = 3                                #three for a king
            print('opponent has three cards to play a face card')
        elif card.value == 'A':
            num = 4                                #four for an Ace
            print('opponent has four cards to play a face card')
    return num                                     #returns the number of cards you have to beat the played face card


def playCard(deck, pile):                          #This function is what plays the card from a players deck into the pile
    pName = playerName()           #alias
    card = deck[0]                 #shallow copy
    pile.append(card)                              #card goes to pile
    deck.remove(card)                              #and is removed from the deck
    print(pName, 'plays', card.value, card.suit)   #prints who played what
    return card                                    #returns the card played


def playTillLim(pile, lim):                           #this function allows handles playing against a face card, it lets a player play cards until the limit is reached or a face card is played. Then hands the pile to the winner of the duel
    count = 0
    player = whoseTurn()           #alias                   #identifies whose turn it is
    if player == you:
        action = input('what you wanna do, s or p ')        #if it's your turn, asks you if your like to shuffle first or just play. you cannot shuffle after playing your first card in your turn
        if action == 's':
            random.shuffle(player)
    while count < lim:                                      #as long as you haven't reached your limit
        if len(player) <= 0:                                #checks that you still have cards in your deck
            oName = oppName()     #alias
            print('game over,', oName, 'wins!')             #if you don't then game over
            break
        card = playCard(player, pile)      #alias                  #playes first card of your turn
        num = checkCard(card)               #alias                #checks if it's a face card
        if num == 0:
            count += 1                                      #if it's not a face card then your count goes up and you play again
        else:
            changeTurn()                                    #if you play a face card then the turn changes
            #player = whoseTurn()
            playTillLim(pile, num)                          #and yout opponent has to play to the new limit
            break
    if count == lim:                                        #if you fail to play a face card before the limit
        opp = whoIsOpp()           #alias
        print('pile goes to', oppName())                    #you lose the pile
        for card in pile:
            opp.append(card)                                #and it goes to your opponents deck
        pile.clear()













def playGame():
    global turn                                                             #by default the cpu goes first and they have turn 0
    global you
    global cpu
    global pile
    players = [cpu, you]            #shallow copy
    random.shuffle(deck)
    deal(deck, players)                                                 #deals the cards to each player
    persons = ['cpu', 'you']        #alias
    while len(you) != 0 and len(cpu) != 0:                              #as long as somebody has cards keep playing
        player = whoseTurn()        #alias
        if player == you:
            action = input('what you wanna do, s or p ')                #if it's your turn, the game asks if you'd like to shuffle or just pkay
            if action == 's':
                random.shuffle(player)
        card = playCard(player, pile)     #alias                              #plays a card on the pile
        changeTurn()
        num = checkCard(card)              #alias
        if num == 0:                                                    #if that card is not a face card then the next person just plays a card
            continue
        else:
            playTillLim(pile, num)                                      #if it is a face card then we enter a PlayTillLim or duel situation
    for i in range(len(players)):
        if len(players[i]) == 52:                                       #once someone has all the cards they are the winner!
            print('yay for', persons[i])








playGame()


