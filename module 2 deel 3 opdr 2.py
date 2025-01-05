getal = 50 
som = 0 
huidige_getallen = "" 

while som <= 980:
    som += getal 
    huidige_getallen += f"{getal} + " 
    
    print(f"{huidige_getallen[:-3]} = {som}")  
    
    getal += 1 