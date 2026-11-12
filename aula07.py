compras =["pão", "café", "suco"]
item1 = input("Digite outro produto que você gostaria: ")
item2 = input("digite outro: ")
compras.append(item1)
compras.append(item2)
if "ovos" not in compras:
    compras.append("ovos")

compras.sort()
print(compras)
print(len(compras))
