seg = int(input("Informe o horário em segundos: "))

horas = seg/3600
min = (seg%3600)/60
seg = (seg%3600)%60

print(f"{int(horas)}:{int(min)}:{int(seg)}")