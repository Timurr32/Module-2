
vertaal_dict = {
    "kat": "poes",
    "huis": "woning",
    "boom": "struik",
    "fiets": "rijwiel",
    "vriend": "kameraad"
}

def woorden_vertalen():
    
    verhaal = input("Verzin een verhaaltje van 10 zinnen met deze woorden: [kat, huis, boom, fiets, vriend]\n")
    
    
    woorden = verhaal.split()
    vertaald_verhaal = " ".join([vertaal_dict.get(woord, woord) for woord in woorden])
    
    
    return vertaald_verhaal


vertaald_verhaal = woorden_vertalen()
print("\nHerhaalde tekst:")
print(vertaald_verhaal)
