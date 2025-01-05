wachtwoord = "friet"
pogingen = 0

while pogingen < 5:
    antwoord = input("Vul het juiste wachtwoord in: ")
    if antwoord == wachtwoord:
        print(f"Correct! Je hebt het wachtwoord geraden in {pogingen} pogingen.")
        break
    else:
        pogingen += 1 
        print(f"Onjuist wachtwoord, je hebt nog {5 - pogingen} pogingen over.")


if pogingen == 5:
    print("Te vaak incorrect, toegang geweigerd.")
