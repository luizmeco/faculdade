dias = int(input("Informe os dias: "))


if dias > 0:
    print(f"{int(dias/365)} ano(s)")
    dias = dias%365

if dias > 0:
    print(f"{int(dias/30)} mes(es)")
    dias = dias%30

if dias > 0:
    print(f"{int(dias/1)} dia(s)")
    dias = dias%1
