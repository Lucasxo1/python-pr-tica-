cliente = {"nome": "ana", "total_compras": 120.0}
cliente["compras_hoje"] = float(input("Digite o valor da compra de hoje: "))
cliente["total_compras"] = cliente["total_compras"] + cliente["compras_hoje"]
if cliente["total_compras"] >= 150.0:
    cliente["categioria"] = "vip"
    cliente["desconto"] = 0.15
    cliente["valor_a_pagar"] = cliente["compras_hoje"] - (cliente["compras_hoje"] * cliente["desconto"])
    print(cliente["total_compras"])
    print(cliente["valor_a_pagar"])
    print(cliente["categioria"])
else:
    cliente["categioria"] = "comum"
    print(cliente["total_compras"])
    print(cliente["categioria"])
