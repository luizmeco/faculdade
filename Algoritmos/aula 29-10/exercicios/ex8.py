def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
        
    return True

numero = 15

print(eh_primo(numero))
