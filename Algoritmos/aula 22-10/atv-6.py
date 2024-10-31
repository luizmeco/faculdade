lista = [11,10,10,10,10,9]

def imprimir_maior_lista(list):
    #imprime todo o conteúdo da lista separado por vígula
    numeros = 0
    print('maior', max(list))
    print('menor',min(list))
    for i in list:
        numeros += i
    media = numeros/len(list)
    print('soma', numeros)
    print('media', media)
imprimir_maior_lista(lista)