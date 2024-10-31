'''def ler_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
    print(conteudo)

ler_arquivo("texto.txt")

'''

def ler(nome):
    f = open(nome, "r", encoding='utf-8')
    print(f.readline())
    f.close()    

ler("texto.txt")