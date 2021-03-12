#Zackary Campbell
#Comp 3006
#Project 5



values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

suits = ['Hearts', 'clubs', 'diamonds', 'spades']


cards = []

for suit in suits:
    suitList = [suit]
    for val in values:
        valList = [val]
        card = list(zip(suitList, valList))
        cards.append(card)


print(cards)
