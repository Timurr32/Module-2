import random

kleuren = ["harten", "klaveren", "schoppen", "ruiten"]
cijfers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas"]
deck = [f"{kleur} {cijfer}" for kleur in kleuren for cijfer in cijfers] + ["joker", "joker"]
random.shuffle(deck)

getrokken_kaarten = [deck.pop() for _ in range(5)]

print("Getrokken kaarten:")
for kaart in getrokken_kaarten:
    print(f"- {kaart}")

print(f"Overgebleven kaarten: {len(deck)}")
print("Deck:")
for kaart in deck:
    print(f"- {kaart}")
