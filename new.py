import random
deck = [1,2,3,4,5,6,7,8,9,10,10,10,10] * 4  # Simplified deck
random.shuffle(deck)
player_hand = random.choice(deck), random.choice(deck)
banker_hand = random.choice(deck), random.choice(deck)
print("Player hand:", player_hand)
print("Banker hand:", banker_hand)

print("Player score:", sum(player_hand ))
print("Banker score:", sum(banker_hand ))
