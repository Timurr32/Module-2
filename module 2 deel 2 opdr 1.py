dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

for dag in dagen:
    print("- " + dag)

print(f"De weekenddagen zijn: {dagen[5]} & {dagen[6]}")

print("De werkdagen zijn:", *dagen[:5], sep=", ")

print("Alle dagen van de week in omgekeerde volgorde zijn: ")
for dag in reversed(dagen):
    print("- " + dag)


werkdagen = dagen[:5]
print("De werkdagen in omgekeerde volgorde zijn: ", end="")
print(*reversed(werkdagen), sep=", ")

weekenddagen = dagen[5:]

print("De weekenddagen in omgekeerde volgorde zijn: ", end="")
for dag in reversed(weekenddagen):
    print(dag, end=", ")


print(weekenddagen[-1])