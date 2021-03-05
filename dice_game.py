#Zackary Campbell
#COMP 3006
#Project 4
#Dice Game: You start the game with 10000 ZC (ZackCoin) each turn you get to choose
#how much money to bet, how many dice you roll and how many sides are on each die.
#You and a computer will both roll the same dice. Whoever has the higher sum on the
#face of their dice wins the pot. Then the game ends when yuo either cash out or go broke
#ZackCoin is not redeemable currency

import numpy as np

class dice:

    def __init__(self, numFaces):
        self.faces = numFaces
        self.num = 'not rolled'                                 #by default our dice have no values

    def __str__(self):
        return str(self.num)                                    #prints the value of the die

    def __add__(self, other):
        if type(self) == type(other):
            return self.num + other.num                         #add dice
        elif type(other) == int:
            return self.num + other                             #this lets you add dice to integers
        else:
            return NotImplemented


    def roll(self):                                             #rolls the dice for us
        num = np.random.randint(self.faces) + 1                 #make sure you get at least 1
        self.num = num
        return num

    def __eq__(self, other):                                    #the following are all the magic methods,
                                                                # simply compare the value on the face of the die
        if type(self) == type(other):
            return self.num == other.num
        else:
            return NotImplemented

    def __ne__(self, other):
        if type(self) == type(other):
            return self.num != other.num
        else:
            return NotImplemented


    def __lt__(self, other):
        if type(self) == type(other):
            return self.num < other.num
        else:
            return NotImplemented


    def __gt__(self, other):
        if type(self) == type(other):
            return self.num > other.num
        else:
            return NotImplemented

    def __le__(self, other):
        if type(self) == type(other):
            return self.num <= other.num
        else:
            return NotImplemented


    def __ge__(self, other):
        if type(self) == type(other):
            return self.num >= other.num
        else:
            return NotImplemented



class cupOfDice:

    def __init__(self, numDice, numFaces):
        self.cup = []                                               #our cup of dice is a list of dice
        self.total = 0
        self.numDice = numDice
        self.numFaces = numFaces
        for i in range(self.numDice):
            die = dice(self.numFaces)
            self.cup.append(die)                                    #generates list with dice in each spot

    def __str__(self):
        if self.total == 0:
            return 'not rolled'                                     #since each die must be at least 1, if the total is 0 you haven't rolled
        else:
            return str(self.total)

    def roll(self):
        for i in range(self.numDice):
            die = self.cup[i]
            die.roll()                                             #rolls each die in the list
            self.total = die + self.total                          #adds the total of each die roll
        return self.total

#the following are all the magic methods, simply compare the totals of the cups
    def __eq__(self, other):
        if type(self) == type(other):
            return self.total == other.total
        else:
            return NotImplemented

    def __ne__(self, other):
        if type(self) == type(other):
            return self.total != other.total
        else:
            return NotImplemented


    def __lt__(self, other):
        if type(self) == type(other):
            return self.total < other.total
        else:
            return NotImplemented


    def __gt__(self, other):
        if type(self) == type(other):
            return self.total > other.total
        else:
            return NotImplemented

    def __le__(self, other):
        if type(self) == type(other):
            return self.total <= other.total
        else:
            return NotImplemented


    def __ge__(self, other):
        if type(self) == type(other):
            return self.total >= other.total
        else:
            return NotImplemented



def main():
    numDice = int(input('How many dice per player? '))
    numFaces = int(input('How many faces per die? (must be at least 2) '))
    playerBank = 10000
    cpuBank = 10000                                         #default hands for you and opponent

    while playerBank > 0 and cpuBank > 0:                   #as long as one of you has ZC
        if numFaces < 2:
            return print("you didn't listen!")              #ensures we aren't playing a rigged game
        else:
            you = cupOfDice(numDice, numFaces)
            cpu = cupOfDice(numDice, numFaces)
            entered = input(f"you have {playerBank} ZC left. What's your bet? ")            #takes your initial bet
            if entered == 'cash out':                                   #if you cash out, the game ends
                print(f'you won {playerBank} ZC. Congratulations!')
                break
            else:
                bet = int(entered)
            while bet > playerBank:                         #makes sure we aren't betting more money than we have
                newBet = int(input('bet less '))
                bet = newBet
            you.roll()
            print(f'your roll = {you}')                     #rolls your dice and prints your total
            cpu.roll()
            print(f'cpu roll = {cpu}')                      #rolls opponent dice and prints their toal
            if you > cpu:
                print('you win')
                playerBank += bet                           #if you win, you win the bet and the opponent loses money
                cpuBank -= bet
            elif cpu > you:
                print('you lose, better luck next time')
                playerBank -= bet                          #if you lose, you lose money and the opponent wins money
                cpuBank += bet
            elif cpu == you:
                return print("it's a tie!")                #if it's a tie, nothing happens

            if playerBank == 0:
                print("you've run out of money. Play again soon")

            if cpuBank == 0:
                print("you're opponent is bankrupt. You're the big winner!")





main()
