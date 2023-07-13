from random import randint

cards = ["Hearts","Clubs","Spades","Diamonds"]

random_number = randint(0,3)

my_random_card = cards[random_number]
print("My random card is: ", my_random_card)

card_found = False

while card_found == False:
    new_random_number = randint(0,3)
    new_card =cards[new_random_number]
    print(new_card)
    if new_card == my_random_card:
        card_found = True
