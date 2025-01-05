import random

kleuren = ["oranje", "blauw", "groen", "bruin"]

aantal = int(input("Hoeveel M'M's moeten er aan de zak toegevoegd worden? ").lower().strip())

zak = []

for x in range(aantal):
    kleur = random.choice(kleuren)
    zak.append(kleur)

print("De inhoud van de zak met M&M's:", zak)