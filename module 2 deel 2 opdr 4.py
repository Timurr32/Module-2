import random


kleuren = ['rood', 'blauw', 'groen', 'geel', 'bruin']


aantal_mms = int(input("Hoeveel M&M's wil je aan de zak toevoegen? "))

zak_met_mms = {}

for _ in range(aantal_mms):
    gekozen_kleur = random.choice(kleuren)
    if gekozen_kleur in zak_met_mms:
        zak_met_mms[gekozen_kleur] += 1
    else:
        zak_met_mms[gekozen_kleur] = 1


print("Zak met M&M's:")
for kleur, aantal in zak_met_mms.items():
    print(f"{kleur}: {aantal}")
