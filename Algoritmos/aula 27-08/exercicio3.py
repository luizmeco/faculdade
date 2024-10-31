import locale
locale.setlocale(locale.LC_ALL, "pt_BR.UTF8")
preco_unitario = 49.99
quantidade = 30
total = quantidade * preco_unitario
string_valor = "R$ " + f"{total:,.2f}".replace(",","x").replace(".",",").replace("x", ".")

print(string_valor)
print(f"Total : R$ {total:,.2f}")
print(locale.currency(total, grouping=True))