clientes = ["lucas","Luiz","João"]

add = input("adicione um cliente ")

while add != "0":
    clientes.append(add)
    clientes.pop(0)
    print(clientes)
    add = input("adicione um cliente ")