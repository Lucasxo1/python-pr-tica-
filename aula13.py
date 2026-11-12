produto ={"nome": "suco de laranja", "preço": 7.50}
produto["estoque"] = 8
produto["vendido"] = int(input("Digite a quantidade que foi vendida "))
produto["estoque"] = produto["estoque"] - produto["vendido"]
if produto["estoque"]<=2:
    produto["alerta"] ="ALERTA, estoque abaixo"
else:
    produto["alerta"] ="estoque normal"

print(produto)
