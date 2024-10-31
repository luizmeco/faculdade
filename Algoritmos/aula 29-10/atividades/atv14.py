def binario_pra_decimal(binario):
    decimal = 0
    for i, digito in enumerate(reversed(binario)):
        decimal += int(digito) * (2**i)
    return decimal

print(binario_pra_decimal("0011"))