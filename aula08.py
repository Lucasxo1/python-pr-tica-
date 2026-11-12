compras =["uva", "café", "pão"]
item1 = input("Digite outro produto: ")
item2 = input("Digite mais um outro produto: ")
compras.append(item1)
compras.append(item2)
if "ovos" not in compras:
    compras.append("ovos")

compras.sort()
print(compras)
print(len(compras))
