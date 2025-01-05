
# 1. Vraag om het te betalen bedrag en het betaalde bedrag.
# 2. Bereken het wisselgeld.
# 3. Geef wisselgeld terug in beschikbare muntstukken.
# 4. Controleer of al het wisselgeld is teruggegeven.
# 5. Toon een overzicht van de teruggegeven muntstukken.

# Lijst van beschikbare muntwaarden (in centen)
coinValues = [500, 200, 100, 50, 20, 10, 5, 2, 1]  # Muntstukken van groot naar klein

# Vraag de gebruiker om het te betalen bedrag en het betaalde bedrag
toPay = int(float(input('Amount to pay: ')) * 100)  # Zet het te betalen bedrag om naar centen
paid = int(float(input('Paid amount: ')) * 100)    # Zet het betaalde bedrag om naar centen
change = paid - toPay  # Bereken het wisselgeld dat teruggegeven moet worden

# Dictionary om het aantal teruggegeven munten bij te houden
returnedCoins = {}

# Wisselgeld teruggeven
while change > 0 and coinValues:  # Terwijl er nog wisselgeld is en er munten zijn om uit te delen
    coinValue = coinValues.pop(0)  # Haal de grootste munt uit de lijst
    nrCoins = change // coinValue  # Bereken hoeveel van deze munten nodig zijn

    if nrCoins > 0:  # Als er munten van deze waarde kunnen worden teruggegeven
        print(f'Return maximal {nrCoins} coins of {coinValue} cents!')  # Print hoeveel munten maximaal kunnen worden gegeven
        nrCoinsReturned = int(input(f'How many coins of {coinValue} cents did you return? '))  # Vraag de gebruiker hoeveel munten er daadwerkelijk zijn teruggegeven
        change -= nrCoinsReturned * coinValue  # Trek het aantal teruggegeven munten af van het wisselgeld

        # Sla het aantal teruggegeven munten op in de dictionary
        if nrCoinsReturned > 0:
            returnedCoins[coinValue] = returnedCoins.get(coinValue, 0) + nrCoinsReturned

# Controle of er nog wisselgeld over is na de loop
if change > 0:
    print(f'\n⚠️ Change not returned: {change} cents')  # Meld als er nog niet al het wisselgeld is teruggegeven
else:
    print('\n✅ Done! All change has been returned.')  # Bevestig als al het wisselgeld correct is teruggegeven

# Toon overzicht van de teruggegeven munten
print("\n🪙 Overview of returned coins:")
for coin, amount in returnedCoins.items():
    if coin >= 100:  # Als het muntstuk euro's is (100 cent of meer)
        print(f"{amount} x {coin // 100} euro")  # Toon het aantal euro's
    else:  # Als het muntstuk centen is
        print(f"{amount} x {coin} cent")  # Toon het aantal centen
