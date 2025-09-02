deck_length = 52
deck = []

suits = ['s','h','c','d']
faces = [10,11,12,13]

for suit in suits:
    for x in range(13):
        print(f"{x} {suit}")