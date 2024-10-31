def contar_primos(n1, n2):
    primos = []
    for i in range(n1,n2+1):
        if eh_primo(i) == True:
            primos.append(i)
    return primos


def eh_primo(n):

    if n <= 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
        
    return True


print(contar_primos(1,50))