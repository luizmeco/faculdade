list = [0]*10

prim = -1
ult = 0

struct = []

def insert():
    if ult < 10:
        if prim == -1:
            list[0] = int(input("Informe um número: "))
            struct["valor"] = list[0]
            struct["prox"] = -1
            prim = 0
        else:
            list[ult+1] = int(input("Informe um número: "))
            struct.pop("prox")


insert()
print(list)