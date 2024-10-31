validado = False
numGrenais = 0
vitInter = 0
vitGremio = 0
empates = 0

while validado == False :
        grenal = input("Novo grenal (1-sim 2-nao)")
        if grenal == "1":
            numGrenais += 1
            golInter = int(input("Quantos gols do Inter: "))
            golGremio = int(input("Quantos gols do Grêmio: "))
            if golInter > golGremio :
                  vitInter += 1
            if golInter == golGremio :
                  empates += 1
            if golGremio > golInter:
                vitGremio +=1
        else:
              validado = True


print(f"{numGrenais} Grenais")
print(f"Inter: {vitInter}")
print(f"Grêmio: {vitGremio}")
print(f"Empates: {empates}")
if vitInter > vitGremio :
      print("Inter venceu mais")
else:
      print("Grêmio venceu mais")

