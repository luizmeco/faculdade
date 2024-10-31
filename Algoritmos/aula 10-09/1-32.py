horaI = int(input("Qual horário começou a jogar "))
horaf = int(input("Qual horário terminou de jogar "))

if horaI < horaf :
    print(f"O JOGO DUROU {horaf - horaI} HORA(S)")
else :
    horas = (24 - horaI)+horaf
    print(f"O JOGO DUROU {horas} HORA(S)")
    