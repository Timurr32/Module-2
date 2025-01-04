aantal_lijstjes = int(input("Hoeveel lijstjes wilt u zien? "))

for x in range(1, aantal_lijstjes + 1):
    
    lengte = int(input(f"Hoelang moet lijst {x} zijn? "))
    

    lijst = list(range(x, x * lengte + 1, x))
    
    
    print(f"Lijst {x}: {lijst}")