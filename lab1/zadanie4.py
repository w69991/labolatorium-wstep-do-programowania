print("Szacowanie zuzycia paliwa i kosztu podrozy")

d = (float(input("Podaj dlugosc drogi: ")))
x = (float(input("Podaj srednie spalanie paliwa w litrach na 100km: ")))

zuzycie = d*x/100

print(f"Przewidywane zuzycie paliwa to: {round(zuzycie, 2)} l")     #komenda round by przybliżyć do części setnych

koszt = zuzycie*6.5

print(f"Przewidywany koszt podrozy to: {round(koszt, 2)} zl")
