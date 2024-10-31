def excluir_duplicados(lista):
    for i in lista:
        if lista.count(i) >= 2:
            lista.remove(i)
    return lista

print(excluir_duplicados([1,1,2,3,4,5,6,6,7,3,4]))
